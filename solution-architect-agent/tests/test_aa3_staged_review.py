"""Real AA3 offline stage wiring, synthetic facts and synthetic candidate only."""
import copy
import hashlib
import sys
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "evals"))
from staged_review import SOURCE, review


def sample():
    obj = {
        "version": "D099-AA0-v1",
        "mission": {"id": "NOTIFY-01", "title": "Synthetic notification service",
                    "source": "N1"},
        "requirements": {
            "FR": [{"id": "FR-1", "text": "Opt-out", "acceptance": "User can opt out",
                    "source": "N1"}],
            "NFR": [{"id": "NFR-1", "text": "Retry cap",
                     "acceptance": "Retries must be bounded", "source": "N2"}],
        },
        "repositories": [
            {"name": "lab/notification-api", "canonical_owner": "PREFERENCES",
             "revision": "synthetic-only", "source": "N1"},
            {"name": "lab/event-relay", "canonical_owner": "EVENT_DELIVERY",
             "revision": "synthetic-only", "source": "N2"},
        ],
        "gaps": [{"id": "G-1", "description": "Missing revocation acceptance test",
                  "source": "N1", "action": "Design independent check"}],
        "options": [
            {"id": ident, "approach": approach, "advantages": ["Tradeoff documented"],
             "risks": ["Human review"], "evidence_limit": "No runtime"}
            for ident, approach in (
                ("S1", "Preserve current flows"),
                ("S2", "Add bounded retry and revocation checks"),
                ("S3", "Replace event relay"))],
        "adr": {"id": "ADR-NOTIFY-01", "status": "PROPOSED", "chosen": "S2",
                "reason": "Evaluate bounded changes", "approval_ref": None},
        "evidence": [{"claim": "Synthetic design", "level": "DESIGNED",
                      "source": "N2", "scope": "fictional"}],
        "limits": ["Human review required"], "next_actions": ["Score the proposal"],
        "status": "DESIGNED",
    }
    facts = [
        {"id": "F-M", "kind": "mission", "value": "NOTIFY-01",
         "source_id": "N1", "quote": "Mission NOTIFY-01 covers notification preference management."},
        {"id": "F-R1", "kind": "repository", "repository": "lab/notification-api",
         "source_id": "N1", "quote": "Canonical repo lab/notification-api owns REST user preferences and opt-out enforcement."},
        {"id": "F-R2", "kind": "repository", "repository": "lab/event-relay",
         "source_id": "N2", "quote": "Canonical repo lab/event-relay owns delivery queue consumers, deduplication keys and delivery status events."},
        {"id": "F-G", "kind": "gap", "source_id": "N2",
         "quote": "Current documentation describes retry without an explicit maximum; dead-letter handling is a proposed design, not deployed."},
    ]
    return facts, obj


def sha():
    return hashlib.sha256(SOURCE.read_bytes()).hexdigest()


class ReviewIntegration(unittest.TestCase):
    def test_correct_synthetic_packet_reaches_human_review_only(self):
        facts, candidate = sample()
        result = review(facts, candidate, expected_fixture_sha256=sha())
        self.assertEqual(result["status"], "AA3_OFFLINE_PRECHECK_PASS")
        self.assertTrue(result["ready_for_independent_human_review"])
        self.assertFalse(result["AA3_ARCHITECT_REASONING_VALIDATED"])
        self.assertFalse(result["approved_adr"])

    def test_missing_one_canonical_repo_blocks_both_stages(self):
        facts, candidate = sample()
        facts.pop(2)
        candidate["repositories"].pop()
        result = review(facts, candidate, expected_fixture_sha256=sha())
        self.assertFalse(result["ready_for_independent_human_review"])
        self.assertIn("REQUIRED_REPOSITORY_FACT_MISSING_OR_DUPLICATE:lab/event-relay",
                      result["violations"])
        self.assertIn("REPOSITORY_REQUIRED_MISSING:lab/event-relay",
                      result["violations"])

    def test_wrong_mission_and_invented_source_block(self):
        facts, candidate = sample()
        candidate["mission"]["id"] = "OTHER"
        candidate["requirements"]["FR"][0]["source"] = "invented"
        result = review(facts, candidate, expected_fixture_sha256=sha())
        self.assertIn("MISSION_ID_MISMATCH", result["violations"])
        self.assertIn("CITATION_NOT_IN_TRUSTED_SOURCES", result["violations"])

    def test_digest_pin_rejects_tampering(self):
        facts, candidate = sample()
        result = review(facts, candidate, expected_fixture_sha256="0" * 64)
        self.assertEqual(result["status"], "AA3_SOURCE_PIN_MISMATCH")
        self.assertFalse(result["ready_for_independent_human_review"])


if __name__ == "__main__":
    unittest.main()
