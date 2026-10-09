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


def request_payload(packet: dict) -> dict:
    return {
        "model": MODEL,
        "prompt": build_fact_prompt(packet),
        "stream": False,
        "format": "json",
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
    facts = None
    if not isinstance(content, dict) or set(content) != {"facts"}:
        problems.append("FACT_OUTPUT_MUST_HAVE_ONLY_FACTS_KEY")
    else:
        facts = content["facts"]
    if not isinstance(facts, list):
        problems.append("FACT_OUTPUT_NOT_ARRAY")
    fact_report = evaluate_facts(packet, facts if isinstance(facts, list) else [])
    problems.extend(fact_report["violations"])
    stats = response if isinstance(response, dict) else {}
    return {
        "status": "AA3_LOCAL_FACT_GATE_PASS" if not problems
                  else "AA3_LOCAL_FACT_GATE_FAIL",
        "mission_id": packet.get("mission_id"),
        "model": MODEL,
        "requested_context": CONTEXT,
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
