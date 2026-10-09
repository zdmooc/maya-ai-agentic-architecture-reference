"""AA3 scorecard unit tests are fake declarations, not real human approvals."""
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "evals"))
from human_scorecard import inspect_scorecard


def template():
    return {
        "case_id": "NOTIFY-01",
        "scoring_basis": "INDEPENDENT_HUMAN_REVIEW",
        "scores": {
            "requirements_traceability": 20,
            "repository_ownership": 20,
            "gaps_and_evidence": 20,
            "options_tradeoffs": 15,
            "adr_backlog": 15,
            "tool_trajectory": 10,
        },
        "source_fidelity_reviewed": True,
        "external_tool_trace_reviewed": True,
        "critical_policy_violation": False,
        "reviewer_reference": "SYNTHETIC_TEST_ONLY",
    }


def test_synthetic_100_never_qualifies_agent_or_identity():
    outcome = inspect_scorecard(template())
    assert outcome["status"] == "AA3_SCORECARD_FORMAT_VALID"
    assert outcome["score"] == 100
    assert outcome["AA3_ARCHITECT_REASONING_VALIDATED"] is False
    assert outcome["human_signature_cryptographically_verified"] is False


def test_missing_real_trace_and_human_review_declarations_block():
    m = template()
    m["external_tool_trace_reviewed"] = False
    m["source_fidelity_reviewed"] = False
    outcome = inspect_scorecard(m)
    assert "EXTERNAL_TOOL_TRACE_REVIEW_REQUIRED" in outcome["violations"]
    assert "SOURCE_FIDELITY_REVIEW_REQUIRED" in outcome["violations"]


def test_policy_violation_disqualifies_score():
    m = template()
    m["critical_policy_violation"] = True
    outcome = inspect_scorecard(m)
    assert "CRITICAL_POLICY_OUTCOME_UNVERIFIED" in outcome["violations"]
    assert outcome["meets_numeric_threshold"] is False


def test_score_boundaries_and_boolean_values_rejected():
    m = template()
    m["scores"]["tool_trajectory"] = True
    m["scores"]["options_tradeoffs"] = 16
    outcome = inspect_scorecard(m)
    assert "INVALID_SCORE:tool_trajectory" in outcome["violations"]
    assert "INVALID_SCORE:options_tradeoffs" in outcome["violations"]
    assert outcome["score"] is None


def test_below_threshold_does_not_pass():
    m = template()
    m["scores"]["requirements_traceability"] = 0
    outcome = inspect_scorecard(m)
    assert outcome["score"] == 80
    assert outcome["meets_numeric_threshold"] is False
