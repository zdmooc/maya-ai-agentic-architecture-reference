"""AA3 M3: assemble a local-only, non-authoritative reviewer handoff index.

Never verifies signatures, authorizes execution or qualifies AA3. External
tool and human review must be examined independently, outside the model.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

from human_scorecard import THRESHOLD, WEIGHTS, inspect_scorecard

MAX_BYTES = 256 * 1024
CASES = ("daarops", "sqy")


def read_bounded_json(path: Path) -> tuple[object, str]:
    if not path.is_file() or path.stat().st_size > MAX_BYTES:
        raise ValueError("LOCAL_REPORT_MISSING_OR_OVERSIZE")
    data = path.read_bytes()
    return json.loads(data.decode("utf-8")), hashlib.sha256(data).hexdigest()


def prepare_handoff(reports: dict[str, object],
                    scorecards: dict[str, object] | None = None) -> dict:
    if set(reports) - set(CASES):
        raise ValueError("UNKNOWN_D099_BENCHMARK_CASE")
    results: dict[str, dict[str, Any]] = {}
    for case in CASES:
        report = reports.get(case)
        if not isinstance(report, dict):
            results[case] = {"status": "NOT_SUBMITTED",
                             "static_review_ready": False}
            continue
        candidate_status = report.get("status")
        results[case] = {
            "status": candidate_status if candidate_status in {
                "AA3_FULL_ASSESSMENT_STATIC_READY_FOR_REVIEW",
                "AA3_FULL_ASSESSMENT_STATIC_FAIL",
                "AA3_FULL_BENCHMARK_BLOCKED",
            } else "UNVERIFIED_REPORT_STATUS",
            "static_review_ready": (
                candidate_status == "AA3_FULL_ASSESSMENT_STATIC_READY_FOR_REVIEW"
                and report.get("violations") == []
                and report.get("AA3_ARCHITECT_REASONING_VALIDATED") is False
            ),
            "model": ((report.get("metadata") or {}).get("model")
                      if isinstance(report.get("metadata"), dict) else None),
            "reported_runtime_observation": report.get(
                "runtime_observation", "NOT_OBSERVED"
            ),
            "independent_source_reverification": "REQUIRED",
            "independent_tool_trace": "REQUIRED",
            "independent_human_signoff": "REQUIRED",
        }
        if scorecards and case in scorecards:
            outcome = inspect_scorecard(scorecards[case])
            results[case]["scorecard_format"] = outcome["status"]
            results[case]["unverified_scoring_points"] = outcome["score"]
            results[case]["human_identity_verified"] = False
        else:
            results[case]["scorecard_format"] = "NOT_SUBMITTED"
    ready = all(results[case].get("static_review_ready") for case in CASES)
    return {
        "status": "AA3_REVIEW_HANDOFF_PREPARED_NOT_APPROVED",
        "benchmark_cases": results,
        "static_both_candidates_ready_for_review": ready,
        "reviewer_weights": WEIGHTS,
        "per_case_threshold": THRESHOLD,
        "golden_references_reviewed_by_independent_human": False,
        "local_64k_context_qualified": False,
        "real_authenticated_host_tool_audit": False,
        "actual_model_tool_denial_verified": False,
        "human_signature_independently_verified": False,
        "safety_and_source_reviewer_signoff": False,
        "adr_approved": False,
        "AA3_ARCHITECT_REASONING_VALIDATED": False,
        "D099_CLOSED": False,
        "note": "Input reports and scorecards are untrusted local statements, "
                "not signed host evidence. Never promote automatically.",
    }


def main() -> int:
    cli = argparse.ArgumentParser()
    cli.add_argument("--daarops-summary", type=Path)
    cli.add_argument("--sqy-summary", type=Path)
    cli.add_argument("--daarops-scorecard", type=Path)
    cli.add_argument("--sqy-scorecard", type=Path)
    args = cli.parse_args()
    inputs: dict[str, object] = {}
    digest: dict[str, str] = {}
    reviews: dict[str, object] = {}
    for case in CASES:
        path = getattr(args, case + "_summary")
        if path is not None:
            data, sha = read_bounded_json(path)
            inputs[case] = data
            digest[case] = sha
        scorepath = getattr(args, case + "_scorecard")
        if scorepath is not None:
            data, sha = read_bounded_json(scorepath)
            reviews[case] = data
            digest[case + "_scorecard"] = sha
    packet = prepare_handoff(inputs, reviews)
    packet["local_submitted_file_sha256"] = digest
    print(json.dumps(packet, sort_keys=True, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
