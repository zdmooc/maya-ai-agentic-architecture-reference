"""AA3 M2: preliminary safety/feasibility prompts for human review ONLY.

This is a small lexical watchlist, NOT a semantic entailment engine and
NEVER architecture approval or an 85+/100 score. Known contradictions in
reported 2026-10-09 model design texts are useful negative regressions.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
EVIDENCE = {
    "NOTIFY-01": HERE / "observed/aa3_operator_design_notify_2026-10-09.json",
    "INVENTORY-02": HERE / "observed/aa3_operator_design_inventory_2026-10-09.json",
}


def preliminary_flags(case: str, design: object) -> dict:
    if case not in EVIDENCE:
        raise ValueError("UNKNOWN_ARCHITECTURE_CASE")
    flags = []
    if not isinstance(design, dict) or not isinstance(design.get("options"), list):
        return {
            "status": "AA3_PRELIMINARY_REVIEW_REQUIRED",
            "flags": [{"id": "DESIGN_SHAPE_UNAVAILABLE", "severity": "REVIEW"}],
            "is_independent_human_review": False,
            "architecture_semantically_validated": False,
            "AA3_ARCHITECT_REASONING_VALIDATED": False,
        }
    for option in design["options"]:
        if not isinstance(option, dict):
            flags.append({"id": "OPTION_NOT_OBJECT", "severity": "REVIEW"})
            continue
        oid = option.get("id")
        approach = str(option.get("approach", "")).casefold()
        advantage = str(option.get("advantage", "")).casefold()
        if case == "NOTIFY-01":
            if "unbounded retries" in approach or "unlimited retries" in approach:
                flags.append({
                    "id": "BOUND_RETRY_CONTRADICTION",
                    "option": oid, "severity": "MAJOR",
                    "reason": "Explicit unbounded retries conflict with frozen N2"
                              " mission's bounded asynchronous delivery",
                })
            if ("acceptance test" in approach or "acceptance tests" in advantage):
                terms = ("bounded", "dedup", "idempoten", "dead-letter",
                         "retry", "delivery status", "replay")
                if not any(t in approach for t in terms):
                    flags.append({
                        "id": "TEST_ACTIVITY_MAY_NOT_BE_DISTINCT_ARCHITECTURE",
                        "option": oid, "severity": "REVIEW",
                        "reason": "Verify option covers delivery failure/traceability"
                                  " and differs structurally from other options",
                    })
        if case == "INVENTORY-02":
            if "guarantees strict consistency" in advantage:
                flags.append({
                    "id": "UNPROVEN_STRICT_CONSISTENCY_GUARANTEE",
                    "option": oid, "severity": "REVIEW",
                    "reason": "A fictional frozen source cannot certify"
                              " concurrency guarantees without test evidence",
                })
            if "high throughput" in advantage:
                flags.append({
                    "id": "UNMEASURED_THROUGHPUT_CLAIM",
                    "option": oid, "severity": "REVIEW",
                    "reason": "No observed throughput/latency benchmarks supplied",
                })
            if "event-driven" in approach and not any(
                s in approach for s in ("idempotent consumer", "outbox", "replay")
            ):
                flags.append({
                    "id": "EVENT_PUBLICATION_AND_REPLAY_NEEDS_REVIEW",
                    "option": oid, "severity": "REVIEW",
                    "reason": "Validate producer atomicity, ordering, deduplication"
                              " and recovery before accepting this option",
                })
    return {
        "status": "AA3_PRELIMINARY_REVIEW_REQUIRED",
        "case_id": case,
        "flags": flags,
        "lexical_watchlist_exhaustive": False,
        "source_semantic_entailment_reviewed": False,
        "is_independent_human_review": False,
        "human_architecture_score": "NOT_SCORED",
        "adr_approved": False,
        "AA3_ARCHITECT_REASONING_VALIDATED": False,
        "D099_CLOSED": False,
    }


def review_observed(case: str) -> dict:
    payload = json.loads(EVIDENCE[case].read_text(encoding="utf-8"))
    if payload.get("origin") != "OPERATOR_TRANSCRIPTION_UNATTESTED" or (
        payload.get("model", payload.get("local_model")) != "qwen3.5:9b-q4_K_M"
    ):
        raise ValueError("UNVERIFIED_OBSERVATION_WRAPPER")
    return preliminary_flags(case, payload.get("design"))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--case", required=True, choices=sorted(EVIDENCE))
    opts = parser.parse_args()
    print(json.dumps(review_observed(opts.case), indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
