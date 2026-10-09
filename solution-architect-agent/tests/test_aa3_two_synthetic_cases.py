"""D099 AA3 two-case static-only synthetic integration; unittest-discovered."""
import hashlib
import sys
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "evals"))
from independent.prepare_case import assemble_case, case_path
from staged_review import review
from test_aa3_staged_review import sample


def inventory():
    facts = [
        {"id": "I-M", "kind": "mission", "value": "INVENTORY-02",
         "source_id": "I1",
         "quote": "Mission INVENTORY-02 covers inventory reservation and expiry."},
        {"id": "I-R1", "kind": "repository", "repository": "lab/inventory-api",
         "source_id": "I1",
         "quote": "Canonical repo lab/inventory-api owns stock availability API and reservation request validation."},
        {"id": "I-R2", "kind": "repository", "repository": "lab/stock-ledger",
         "source_id": "I2",
         "quote": "Canonical repo lab/stock-ledger owns reservation IDs, stock mutation journal and idempotency keys."},
    ]
    _, obj = sample()
    obj["mission"].update({"id": "INVENTORY-02", "title": "Fictional stock reservation",
                           "source": "I1"})
    for kind in ("FR", "NFR"):
        for r in obj["requirements"][kind]:
            r["source"] = "I1" if kind == "FR" else "I2"
    obj["repositories"][0].update({"name": "lab/inventory-api", "source": "I1"})
    obj["repositories"][1].update({"name": "lab/stock-ledger", "source": "I2"})
    obj["gaps"][0]["source"] = "I1"
    obj["evidence"][0]["source"] = "I2"
    return facts, obj


class TwoSyntheticCasesTests(unittest.TestCase):
    def test_two_fictional_cases_share_same_review_contract(self):
        for name, expected in (
            ("notification_case.json", "NOTIFY-01"),
            ("inventory_case.json", "INVENTORY-02"),
        ):
            packet, meta = assemble_case(name)
            self.assertEqual(packet["mission_id"], expected)
            self.assertFalse(meta["model_invoked"])
            self.assertEqual(len(packet["repository_sources"]), 2)
        facts, candidate = inventory()
        digest = hashlib.sha256(case_path("inventory_case.json").read_bytes()).hexdigest()
        result = review(facts, candidate, expected_fixture_sha256=digest,
                        fixture_name="inventory_case.json")
        self.assertEqual(result["status"], "AA3_OFFLINE_PRECHECK_PASS")
        self.assertFalse(result["AA3_ARCHITECT_REASONING_VALIDATED"])

    def test_unapproved_case_name_rejected(self):
        with self.assertRaisesRegex(ValueError, "UNAPPROVED_INDEPENDENT_FIXTURE"):
            case_path("../../private/file.json")

    def test_mixed_case_sources_and_identity_do_not_pass(self):
        facts, candidate = inventory()
        digest = hashlib.sha256(case_path("notification_case.json").read_bytes()).hexdigest()
        result = review(facts, candidate, expected_fixture_sha256=digest,
                        fixture_name="notification_case.json")
        self.assertEqual(result["status"], "AA3_OFFLINE_PRECHECK_FAIL")
        self.assertIn("MISSION_ID_MISMATCH", result["violations"])
        self.assertIn("REPOSITORY_REQUIRED_MISSING:lab/notification-api",
                      result["violations"])


if __name__ == "__main__":
    unittest.main()
