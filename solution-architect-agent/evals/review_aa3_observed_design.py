"""D099 offline inspection of reported local design: not an independent attestation."""
from __future__ import annotations
import json
from pathlib import Path
from independent.prepare_case import assemble_case
from local_aa3_design_probe import format_valid

OBSERVED = Path(__file__).resolve().parent / "observed" / (
    "aa3_operator_design_notify_2026-10-09.json"
)


def inspect_observation(document: object) -> dict:
    packet, meta = assemble_case("notification_case.json")
    if not isinstance(document, dict):
        raise ValueError("UNTRUSTED_OBSERVATION_NOT_OBJECT")
    design = document.get("design")
    review = document.get("preliminary_assistant_review")
    issues = review.get("issues") if isinstance(review, dict) else None
    if not isinstance(issues, list) or not issues:
        raise ValueError("PRELIMINARY_REVIEW_MISSING")
    ids = {x.get("id") for x in issues if isinstance(x, dict)}
    required = {
        "OPTION_S1_CONFLICTS_MANDATORY_BOUNDED_RETRY",
        "OPTION_S3_TEST_ACTIVITY_NOT_DISTINCT_ARCHITECTURE",
    }
    if not required.issubset(ids):
        raise ValueError("KNOWN_DEFECTS_NOT_RECORDED")
    return {
        "status": "AA3_STRUCTURAL_PASS_PRELIMINARY_REVIEW_NEEDED"
        if format_valid(packet, design) else "AA3_REPORTED_DESIGN_FORMAT_FAIL",
        "case_id": packet["mission_id"],
        "reported_run": document.get("reported_status"),
        "fixture_sha256": meta["fixture_sha256"],
        "issues": issues,
        "review_provenance": "ASSISTANT_PRELIMINARY_NOT_INDEPENDENT_HUMAN",
        "semantic_conformance_proven": False,
        "independent_human_score": "NOT_SCORED",
        "adr_approved": False,
        "AA3_ARCHITECT_REASONING_VALIDATED": False,
        "D099_CLOSED": False,
    }


def main() -> None:
    result = inspect_observation(json.loads(OBSERVED.read_text(encoding="utf-8")))
    print(json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
