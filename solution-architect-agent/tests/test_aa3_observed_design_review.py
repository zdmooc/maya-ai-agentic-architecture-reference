"""Historical real design output regression: structural gate != semantic review."""
import json
import sys
from pathlib import Path
from unittest import TestCase
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "evals"))
from review_aa3_observed_design import OBSERVED, inspect_observation
from local_aa3_design_probe import operator_observation, format_valid


class ObservedDesignReviewTests(TestCase):
    def test_real_notif_output_structural_pass_but_architecture_needs_review(self):
        data = json.loads(OBSERVED.read_text(encoding="utf-8"))
        packet, _, digest = operator_observation("notification_case.json")
        self.assertEqual(data["fixture_sha256"], digest)
        self.assertTrue(format_valid(packet, data["design"]))
        reviewed = inspect_observation(data)
        self.assertEqual(reviewed["status"],
                         "AA3_STRUCTURAL_PASS_PRELIMINARY_REVIEW_NEEDED")
        self.assertEqual(len(reviewed["issues"]), 2)
        self.assertFalse(reviewed["semantic_conformance_proven"])
        self.assertFalse(reviewed["adr_approved"])
        self.assertFalse(reviewed["AA3_ARCHITECT_REASONING_VALIDATED"])

    def test_defect_notes_cannot_be_dropped(self):
        data = json.loads(OBSERVED.read_text(encoding="utf-8"))
        data["preliminary_assistant_review"]["issues"] = []
        with self.assertRaisesRegex(ValueError, "PRELIMINARY_REVIEW_MISSING"):
            inspect_observation(data)

    def test_foreign_option_and_approval_block_schema(self):
        data = json.loads(OBSERVED.read_text(encoding="utf-8"))
        data["design"]["adr"]["status"] = "APPROVED"
        result = inspect_observation(data)
        self.assertEqual(result["status"], "AA3_REPORTED_DESIGN_FORMAT_FAIL")
