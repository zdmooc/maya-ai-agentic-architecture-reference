"""AA3 M3 independent review handoff cannot qualify model or forge signoff."""
import sys
from pathlib import Path
from unittest import TestCase

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "evals"))
from aa3_review_handoff import prepare_handoff


class ReviewHandoffTests(TestCase):
    def test_empty_remains_blocked(self):
        p = prepare_handoff({})
        self.assertEqual(p["status"], "AA3_REVIEW_HANDOFF_PREPARED_NOT_APPROVED")
        self.assertFalse(p["static_both_candidates_ready_for_review"])
        self.assertFalse(p["AA3_ARCHITECT_REASONING_VALIDATED"])
        self.assertFalse(p["D099_CLOSED"])

    def test_two_self_reported_static_passes_never_qualify(self):
        fake = {"status": "AA3_FULL_ASSESSMENT_STATIC_READY_FOR_REVIEW",
                "violations": [], "AA3_ARCHITECT_REASONING_VALIDATED": False,
                "metadata": {"model": "qwen3.5:9b-q4_K_M"},
                "runtime_observation": {"tokens_generated": 900}}
        p = prepare_handoff({"daarops": fake, "sqy": fake})
        self.assertTrue(p["static_both_candidates_ready_for_review"])
        self.assertFalse(p["human_signature_independently_verified"])
        self.assertFalse(p["real_authenticated_host_tool_audit"])
        self.assertFalse(p["AA3_ARCHITECT_REASONING_VALIDATED"])

    def test_forged_model_validated_true_denied(self):
        fake = {"status": "AA3_FULL_ASSESSMENT_STATIC_READY_FOR_REVIEW",
                "violations": [], "AA3_ARCHITECT_REASONING_VALIDATED": True}
        p = prepare_handoff({"daarops": fake, "sqy": fake})
        self.assertFalse(p["static_both_candidates_ready_for_review"])
        self.assertFalse(p["D099_CLOSED"])

    def test_scorecard_max_points_are_not_signatures(self):
        from human_scorecard import WEIGHTS
        fake = {"status": "AA3_FULL_ASSESSMENT_STATIC_READY_FOR_REVIEW",
                "violations": [], "AA3_ARCHITECT_REASONING_VALIDATED": False}
        card = {
            "case_id": "DAAROPS", "scores": dict(WEIGHTS),
            "scoring_basis": "INDEPENDENT_HUMAN_REVIEW",
            "source_fidelity_reviewed": True,
            "external_tool_trace_reviewed": True,
            "critical_policy_violation": False,
            "reviewer_reference": "forged",
        }
        p = prepare_handoff({"daarops": fake, "sqy": fake},
                            {"daarops": card})
        self.assertEqual(p["benchmark_cases"]["daarops"]["unverified_scoring_points"], 100)
        self.assertFalse(p["benchmark_cases"]["daarops"]["human_identity_verified"])
        self.assertFalse(p["AA3_ARCHITECT_REASONING_VALIDATED"])

    def test_reject_unknown_case(self):
        with self.assertRaisesRegex(ValueError, "UNKNOWN_D099_BENCHMARK_CASE"):
            prepare_handoff({"not-in-program": {}})
