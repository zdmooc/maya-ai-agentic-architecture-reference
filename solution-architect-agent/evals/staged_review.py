"""AA3 staged offline review on one fictional NOTIFY-01 fixture.

This runner does not use a model, network, tools, host repo access, or approval.
An external, independently reviewed git-pinned fixture SHA is a prerequisite
for comparability; a caller self-computed SHA is NOT independent provenance.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import re
from pathlib import Path
from typing import Any

from grounding_gate import evaluate_facts
from decision_gate import evaluate_design
from independent.prepare_case import assemble, SOURCE

MAX_INPUT_BYTES = 256 * 1024


def review(facts: object, candidate: object, *,
           expected_fixture_sha256: str) -> dict[str, Any]:
    observed = hashlib.sha256(SOURCE.read_bytes()).hexdigest()
    if (not isinstance(expected_fixture_sha256, str)
            or re.fullmatch(r"[a-f0-9]{64}", expected_fixture_sha256) is None
            or observed != expected_fixture_sha256):
        return {
            "status": "AA3_SOURCE_PIN_MISMATCH",
            "violations": ["TRUSTED_FIXTURE_DIGEST_MISMATCH"],
            "fact_gate_pass": False, "design_gate_pass": False,
            "ready_for_independent_human_review": False,
            "AA3_ARCHITECT_REASONING_VALIDATED": False,
        }
    packet, _ = assemble()
    facts_status = evaluate_facts(packet, facts)
    design_status = evaluate_design(candidate, packet, facts_status)
    violations = sorted(set(facts_status["violations"] +
                            design_status["violations"]))
    return {
        "status": "AA3_OFFLINE_PRECHECK_PASS" if not violations
                  else "AA3_OFFLINE_PRECHECK_FAIL",
        "case": packet["mission_id"],
        "fixture_sha256": observed,
        "fact_gate_pass": facts_status["lexical_grounding_pass"],
        "design_gate_pass": not design_status["violations"],
        "violations": violations,
        "ready_for_independent_human_review": not violations,
        "trusted_runtime_tool_audit": "NOT_PRESENT",
        "human_architecture_score": "NOT_SCORED",
        "approved_adr": False,
        "AA3_ARCHITECT_REASONING_VALIDATED": False,
    }


def read_json(path: Path) -> Any:
    # Purely local, bounded offline input; this tool never executes content.
    if not path.is_file() or path.stat().st_size > MAX_INPUT_BYTES:
        raise ValueError("INVALID_OR_OVERSIZE_LOCAL_INPUT")
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    cli = argparse.ArgumentParser()
    cli.add_argument("--facts", required=True, type=Path)
    cli.add_argument("--candidate", required=True, type=Path)
    cli.add_argument("--expected-fixture-sha256", required=True)
    opts = cli.parse_args()
    result = review(read_json(opts.facts), read_json(opts.candidate),
                    expected_fixture_sha256=opts.expected_fixture_sha256)
    print(json.dumps(result, indent=2, sort_keys=True, ensure_ascii=False))
    return 0 if result["status"] == "AA3_OFFLINE_PRECHECK_PASS" else 2


if __name__ == "__main__":
    raise SystemExit(main())
