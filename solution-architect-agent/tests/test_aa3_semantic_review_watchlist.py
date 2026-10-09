"""AA3 M2 lexical warning regressions never masquerade as reviewer signoff."""
import json
import sys
from pathlib import Path
from unittest import TestCase

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "evals"))
from aa3_semantic_review_watchlist import (
    EVIDENCE, preliminary_flags, review_observed,
)


class PreliminaryReviewTests(TestCase):
    def test_notif_known_conflicts_preserved(self):
        result = review_observed("NOTIFY-01")
        ids = {item["id"] for item in result["flags"]}
        self.assertIn("BOUND_RETRY_CONTRADICTION", ids)
        self.assertIn("TEST_ACTIVITY_MAY_NOT_BE_DISTINCT_ARCHITECTURE", ids)
        self.assertFalse(result["AA3_ARCHITECT_REASONING_VALIDATED"])
        self.assertFalse(result["is_independent_human_review"])

    def test_inventory_overclaims_preserved(self):
        result = review_observed("INVENTORY-02")
        ids = {item["id"] for item in result["flags"]}
        self.assertIn("UNPROVEN_STRICT_CONSISTENCY_GUARANTEE", ids)
        self.assertIn("UNMEASURED_THROUGHPUT_CLAIM", ids)
        self.assertIn("EVENT_PUBLICATION_AND_REPLAY_NEEDS_REVIEW", ids)
        self.assertFalse(result["adr_approved"])
        self.assertEqual(result["human_architecture_score"], "NOT_SCORED")

    def test_no_watchlist_flags_never_means_semantically_valid(self):
        example = json.loads(EVIDENCE["NOTIFY-01"].read_text())
        for item in example["design"]["options"]:
            item["approach"] = "Neutral architecture placeholder"
            item["advantage"] = "Unknown"
        result = preliminary_flags("NOTIFY-01", example["design"])
        self.assertEqual(result["flags"], [])
        self.assertEqual(result["status"], "AA3_PRELIMINARY_REVIEW_REQUIRED")
        self.assertFalse(result["source_semantic_entailment_reviewed"])

    def test_missing_design_never_auto_passes(self):
        report = preliminary_flags("INVENTORY-02", {})
        self.assertTrue(report["flags"])
        self.assertFalse(report["AA3_ARCHITECT_REASONING_VALIDATED"])
