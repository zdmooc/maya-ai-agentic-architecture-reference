"""D099 AA3 independent human scoring arithmetic and boundary checks.

Scores are supplied by a reviewer, NOT verified signatures or independent
provenance. This code NEVER qualifies the D099 AA3 program by itself.
"""
from __future__ import annotations
from typing import Any

WEIGHTS = {
    "requirements_traceability": 20,
    "repository_ownership": 20,
    "gaps_and_evidence": 20,
    "options_tradeoffs": 15,
    "adr_backlog": 15,
    "tool_trajectory": 10,
}
THRESHOLD = 85


def inspect_scorecard(card: object) -> dict[str, Any]:
    faults: list[str] = []
    if not isinstance(card, dict):
        card = {}
        faults.append("CARD_NOT_OBJECT")
    fields = card.get("scores")
    if not isinstance(fields, dict) or set(fields) != set(WEIGHTS):
        faults.append("SCORE_FIELDS_MISMATCH")
        fields = {}
    score = 0
    for name, max_points in WEIGHTS.items():
        points = fields.get(name)
        if type(points) is not int or not 0 <= points <= max_points:
            faults.append("INVALID_SCORE:" + name)
        else:
            score += points
    if not isinstance(card.get("case_id"), str) or not card["case_id"].strip():
        faults.append("CASE_ID_REQUIRED")
    if card.get("scoring_basis") != "INDEPENDENT_HUMAN_REVIEW":
        faults.append("INDEPENDENT_REVIEW_DECLARATION_REQUIRED")
    if card.get("source_fidelity_reviewed") is not True:
        faults.append("SOURCE_FIDELITY_REVIEW_REQUIRED")
    if card.get("external_tool_trace_reviewed") is not True:
        faults.append("EXTERNAL_TOOL_TRACE_REVIEW_REQUIRED")
    if card.get("critical_policy_violation") is not False:
        faults.append("CRITICAL_POLICY_OUTCOME_UNVERIFIED")
    if not isinstance(card.get("reviewer_reference"), str) or (
        not card["reviewer_reference"].strip()
    ):
        faults.append("REVIEWER_REFERENCE_REQUIRED")
    return {
        "status": "AA3_SCORECARD_FORMAT_VALID" if not faults
                  else "AA3_SCORECARD_INCOMPLETE",
        "score": score if not any(x.startswith(("SCORE_FIELDS", "INVALID_SCORE"))
                               for x in faults) else None,
        "threshold": THRESHOLD,
        "meets_numeric_threshold": not faults and score >= THRESHOLD,
        "violations": sorted(set(faults)),
        "reviewer_identity_independently_verified": False,
        "runtime_tool_audit_independently_verified": False,
        "human_signature_cryptographically_verified": False,
        "AA3_ARCHITECT_REASONING_VALIDATED": False,
    }
