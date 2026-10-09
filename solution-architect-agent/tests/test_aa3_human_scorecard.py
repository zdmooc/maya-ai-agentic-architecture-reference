"""AA3 scorecard regression tests, discovered by CI unittest."""
import sys
from pathlib import Path
import unittest

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


class ScorecardTests(unittest.TestCase):
    def test_synthetic_100_never_qualifies_agent_or_identity(self):
        outcome = inspect_scorecard(template())
        self.assertEqual(outcome["status"], "AA3_SCORECARD_FORMAT_VALID")
        self.assertEqual(outcome["score"], 100)
        self.assertFalse(outcome["AA3_ARCHITECT_REASONING_VALIDATED"])
        self.assertFalse(outcome["human_signature_cryptographically_verified"])

    def test_missing_real_trace_and_human_review_declarations_block(self):
        m = template()
        m["external_tool_trace_reviewed"] = False
        m["source_fidelity_reviewed"] = False
        outcome = inspect_scorecard(m)
        self.assertIn("EXTERNAL_TOOL_TRACE_REVIEW_REQUIRED", outcome["violations"])
        self.assertIn("SOURCE_FIDELITY_REVIEW_REQUIRED", outcome["violations"])

    def test_policy_violation_disqualifies_score(self):
        m = template()
        m["critical_policy_violation"] = True
        outcome = inspect_scorecard(m)
        self.assertIn("CRITICAL_POLICY_OUTCOME_UNVERIFIED", outcome["violations"])
        self.assertFalse(outcome["meets_numeric_threshold"])

    def test_score_boundaries_and_boolean_values_rejected(self):
        m = template()
        m["scores"]["tool_trajectory"] = True
        m["scores"]["options_tradeoffs"] = 16
        outcome = inspect_scorecard(m)
        self.assertIn("INVALID_SCORE:tool_trajectory", outcome["violations"])
        self.assertIn("INVALID_SCORE:options_tradeoffs", outcome["violations"])
        self.assertIsNone(outcome["score"])

    def test_below_threshold_does_not_pass(self):
        m = template()
        m["scores"]["requirements_traceability"] = 0
        outcome = inspect_scorecard(m)
        self.assertEqual(outcome["score"], 80)
        self.assertFalse(outcome["meets_numeric_threshold"])


if __name__ == "__main__":
    unittest.main()
