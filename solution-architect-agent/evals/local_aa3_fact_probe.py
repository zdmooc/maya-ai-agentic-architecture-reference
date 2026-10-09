"""D099 AA3 opt-in, single synthetic fact-extraction probe for local Ollama.

Runs ONLY against two known host-only Ollama endpoints. No tools, shell,
repository modifications, OpenCode, CRC access or automatic context escalation.
CI tests mock HTTP and never invoke a model.
"""
from __future__ import annotations

import argparse
import json
import os
import sys
from urllib.request import ProxyHandler, Request, build_opener

from jsonschema import Draft202012Validator

from grounding_gate import evaluate_facts
from independent.prepare_case import assemble_case
from prompt_stages import build_fact_prompt

MODEL = "qwen3.5:9b-q4_K_M"
ENDPOINTS = frozenset({
    "http://127.0.0.1:11434",
    "http://192.168.56.1:11434",
})
CONTEXT = 8192
MAX_GENERATED = 384


def facts_format_schema(packet: dict) -> dict:
    """Enforce shape only; names/quotes still require independent source checks.

    The simple required-string shape is intentionally compatible with Ollama's
    structured JSON format. Irrelevant value/repository fields must be empty.
    """
    owners = packet.get("repository_sources")
    sources = packet.get("sources")
    if not isinstance(owners, dict) or not owners or not isinstance(sources, list):
        raise ValueError("AA3_UNPINNED_FORMAT_SOURCES")
    ids = [s.get("id") for s in sources if isinstance(s, dict)]
    if not ids or len(set(ids)) != len(ids) or not all(
        isinstance(source_id, str) and source_id for source_id in ids
    ):
        raise ValueError("AA3_INVALID_FORMAT_SOURCE_IDS")
    count = len(owners) + 1
    return {
        "type": "object",
        "additionalProperties": False,
        "required": ["facts"],
        "properties": {
            "facts": {
                "type": "array",
                "minItems": count,
                "maxItems": count,
                "items": {
                    "type": "object",
                    "additionalProperties": False,
                    "required": [
                        "id", "kind", "source_id", "quote",
                        "value", "repository",
                    ],
                    "properties": {
                        "id": {"type": "string", "minLength": 1},
                        "kind": {"type": "string", "enum": [
                            "mission", "repository",
                        ]},
                        "source_id": {"type": "string", "enum": ids},
                        "quote": {"type": "string", "minLength": 1},
                        "value": {"type": "string"},
                        "repository": {"type": "string"},
                    },
                },
            },
        },
    }


def identity_prompt(packet: dict) -> str:
    owners = packet["repository_sources"]
    expected = len(owners)
    return build_fact_prompt(packet) + (
        "\\n\\nSTRICT IDENTITY CHECK ONLY: Return EXACTLY "
        + str(expected + 1)
        + " facts (ONE mission, then EXACTLY "
        + str(expected)
        + " repository facts). Do NOT emit extra mission facts even when "
          "more than one source mentions the mission. Do NOT emit "
          "requirements, gaps, discussion or duplicates. "
          "Every fact MUST contain ALL six string keys: "
          "id, kind, source_id, quote, value, repository. "
          "The ONE mission fact has kind=mission, "
          "value exactly the mission_id in the source packet, and "
          "repository=empty string. The repository facts have "
          "kind=repository, repository exactly ONE name from the "
          "trusted repository_sources map each, value=empty string, "
          "source_id exactly the mapped source ID, and quote "
          "an EXACT contiguous substring from that source naming the repo. "
          "The mission quote must contain the mission_id. "
          "Never invent source text, never manufacture approvals. "
          'Response shape: {"facts":[{"id":"M1","kind":"mission",'
          '"source_id":"...","quote":"...","value":"...","repository":""},'
          '{"id":"R1","kind":"repository","source_id":"...",'
          '"quote":"...","value":"","repository":"..."}]}. '
          "This is a shape illustration, NOT an answer."
    )


def request_payload(packet: dict) -> dict:
    return {
        "model": MODEL,
        "prompt": identity_prompt(packet),
        "stream": False,
        "format": facts_format_schema(packet),
        "think": False,
        "keep_alive": "5m",
        "options": {
            "num_ctx": CONTEXT,
            "num_predict": MAX_GENERATED,
            "temperature": 0,
        },
    }


def assess_response(packet: dict, response: object) -> dict:
    problems: list[str] = []
    content = None
    if not isinstance(response, dict):
        problems.append("MODEL_RESPONSE_NOT_OBJECT")
    else:
        try:
            content = json.loads(response.get("response", ""))
        except (TypeError, ValueError):
            problems.append("MODEL_RESPONSE_NOT_VALID_JSON")
        if response.get("done") is not True:
            problems.append("INFERENCE_NOT_COMPLETED")
        if response.get("done_reason") == "length":
            problems.append("INFERENCE_TRUNCATED")
    if isinstance(content, dict):
        validation = Draft202012Validator(facts_format_schema(packet))
        if not validation.is_valid(content):
            problems.append("MODEL_FACT_JSON_SCHEMA_INVALID")
    facts = None
    if not isinstance(content, dict) or set(content) != {"facts"}:
        problems.append("FACT_OUTPUT_MUST_HAVE_ONLY_FACTS_KEY")
    else:
        facts = content["facts"]
    if not isinstance(facts, list):
        problems.append("FACT_OUTPUT_NOT_ARRAY")
    fact_report = evaluate_facts(packet, facts if isinstance(facts, list) else [])\n    # No repair/normalization: malformed or omitted fields remain model failures.\n    if isinstance(facts, list):\n        for fact in facts:\n            if not isinstance(fact, dict):\n                continue\n            if fact.get("kind") == "mission" and fact.get("repository") != "":\n                problems.append("MISSION_EXTRANEOUS_REPOSITORY_FIELD")\n            if fact.get("kind") == "repository" and fact.get("value") != "":\n                problems.append("REPOSITORY_EXTRANEOUS_VALUE_FIELD")
    problems.extend(fact_report["violations"])
    stats = response if isinstance(response, dict) else {}
    return {
        "status": "AA3_LOCAL_FACT_GATE_PASS" if not problems
                  else "AA3_LOCAL_FACT_GATE_FAIL",
        "mission_id": packet.get("mission_id"),
        "model": MODEL,
        "requested_context": CONTEXT,\n        "generation_format": "OLLAMA_JSON_SCHEMA",
        "observed_context": "CHECK_OLLAMA_PS_SEPARATELY",
        "facts": facts if isinstance(facts, list) and len(facts) <= 16 else None,
        "violations": sorted(set(problems)),
        "tokens_generated": stats.get("eval_count"),
        "tokens_prompt": stats.get("prompt_eval_count"),
        "total_seconds": round(stats.get("total_duration", 0) / 1e9, 2),
        "load_seconds": round(stats.get("load_duration", 0) / 1e9, 2),
        "agent_tools_exposed": False,
        "external_model_tool_audit": "NOT_TESTED",
        "architecture_reasoning_scored": False,
        "AA3_ARCHITECT_REASONING_VALIDATED": False,
        "D099_CLOSED": False,
    }


def single_probe(*, endpoint: str, case: str, consent: str) -> dict:
    if consent != "YES":
        raise ValueError("EXPLICIT_LOCAL_INFERENCE_CONSENT_REQUIRED")
    if endpoint not in ENDPOINTS:
        raise ValueError("UNAPPROVED_OLLAMA_ENDPOINT")
    packet, _ = assemble_case(case)
    data = json.dumps(request_payload(packet)).encode("utf-8")
    req = Request(endpoint + "/api/generate", data=data,
                  headers={"Content-Type": "application/json"},
                  method="POST")
    client = build_opener(ProxyHandler({}))
    with client.open(req, timeout=300) as reply:
        result = json.load(reply)
    return assess_response(packet, result)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--case", choices=["notification_case.json",
                                           "inventory_case.json"],
                        default="notification_case.json")
    parser.add_argument("--endpoint", choices=sorted(ENDPOINTS),
                        default="http://192.168.56.1:11434")
    args = parser.parse_args(argv)
    try:
        report = single_probe(
            endpoint=args.endpoint, case=args.case,
            consent=os.environ.get("D099_ALLOW_LOCAL_INFERENCE", ""),
        )
    except (OSError, ValueError, TimeoutError) as exc:
        print(json.dumps({
            "status": "AA3_LOCAL_FACT_PROBE_BLOCKED",
            "reason": type(exc).__name__,
            "AA3_ARCHITECT_REASONING_VALIDATED": False,
        }))
        return 2
    print(json.dumps(report, indent=2, ensure_ascii=False, sort_keys=True))
    return 0 if report["status"] == "AA3_LOCAL_FACT_GATE_PASS" else 2


if __name__ == "__main__":
    sys.exit(main())
