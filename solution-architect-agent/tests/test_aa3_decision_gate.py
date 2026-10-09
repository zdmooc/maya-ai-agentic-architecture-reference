"""AA3 I4 decision stage, synthetic and offline, no model."""
import copy
import importlib.util
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location(
    "aa3_decision", ROOT / "evals" / "decision_gate.py")
gate = importlib.util.module_from_spec(spec)
spec.loader.exec_module(gate)
FACT = {"lexical_grounding_pass": True, "violations": []}
PACKET = {"mission_id": "NOTIFY-01",
          "repository_sources": {"lab/notify": "S-01"}}


def candidate():
    return {
        "version": "D099-AA0-v1",
        "mission": {"id": "NOTIFY-01", "title": "Synthetic notification",
                    "source": "S-01"},
        "requirements": {
            "FR": [{"id": "FR1", "text": "Retry", "acceptance": "3 retries",
                    "source": "S-01"}],
            "NFR": [{"id": "NFR1", "text": "Bounded", "acceptance": "No infinite retry",
                     "source": "S-01"}],
        },
        "repositories": [{"name": "lab/notify", "canonical_owner": "NOTIFICATIONS",
                          "revision": "test-only", "source": "S-01"}],
        "gaps": [{"id": "G1", "description": "No capped retry", "source": "S-01",
                  "action": "Add cap in approved worktree"}],
        "options": [
            {"id": i, "approach": name, "advantages": ["demo"],
             "risks": ["review required"], "evidence_limit": "synthetic"}
            for i, name in [("S1", "Keep existing"), ("S2", "Bound retries"),
                            ("S3", "Replace queue")]],
        "adr": {"id": "ADR-N1", "status": "PROPOSED", "chosen": "S2",
                "reason": "Evaluate bounded retries", "approval_ref": None},
        "evidence": [{"claim": "Design draft", "level": "DESIGNED",
                      "source": "S-01", "scope": "synthetic"}],
        "limits": ["No runtime proof"], "next_actions": ["Human review"],
        "status": "DESIGNED",
    }


class AA3DecisionTests(unittest.TestCase):
    def test_valid_structure_requests_review_not_approval(self):
        result = gate.evaluate_design(candidate(), PACKET, FACT)
        self.assertEqual(result["violations"], [])
        self.assertTrue(result["may_request_human_review"])
        self.assertFalse(result["adr_approved"])
        self.assertFalse(result["builder_authorized"])

    def test_wrong_mission_and_fictional_extra_repository_are_denied(self):
        obj = candidate()
        obj["mission"]["id"] = "OTHER"
        obj["repositories"][0]["name"] = "unknown/repo"
        faults = gate.evaluate_design(obj, PACKET, FACT)["violations"]
        self.assertIn("MISSION_ID_MISMATCH", faults)
        self.assertIn("REPOSITORY_REQUIRED_MISSING:lab/notify", faults)
        self.assertIn("REPOSITORY_NOT_IN_TRUSTED_INVENTORY:unknown/repo", faults)

    def test_missing_fact_gate_denies_even_valid_candidate(self):
        faults = gate.evaluate_design(candidate(), PACKET,
            {"lexical_grounding_pass": False,
             "violations": ["QUOTE_NOT_IN_PINNED_SOURCE"]})["violations"]
        self.assertIn("FACT_GATE_NOT_PASSED", faults)

    def test_human_approval_cannot_be_forged(self):
        obj = candidate()
        obj["adr"]["status"] = "APPROVED"
        obj["adr"]["approval_ref"] = "fabricated"
        self.assertIn("ADR_MUST_BE_UNAPPROVED_PROPOSAL",
                      gate.evaluate_design(obj, PACKET, FACT)["violations"])

    def test_false_production_evidence_is_flagged(self):
        obj = candidate()
        obj["evidence"][0]["level"] = "PRODUCTION_OPERATED"
        self.assertIn("UNVERIFIED_RUNTIME_OR_CI_CLAIM",
                      gate.evaluate_design(obj, PACKET, FACT)["violations"])

    def test_duplicate_option_rejected(self):
        obj = candidate()
        obj["options"][2]["id"] = "S2"
        self.assertIn("OPTIONS_MUST_BE_S1_S2_S3",
                      gate.evaluate_design(obj, PACKET, FACT)["violations"])


if __name__ == "__main__":
    unittest.main()
