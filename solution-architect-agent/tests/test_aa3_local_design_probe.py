"""D099 AA3 S1/S2/S3 synthetic design slice, unit tests never call a model."""
import json
import sys
from pathlib import Path
from unittest import TestCase
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "evals"))
from local_aa3_design_probe import (
    assess_design, design_prompt, design_schema, format_valid,
    local_probe, operator_observation, request_payload,
    verify_transcribed_facts,
)


def example_design():
    return {
        "case_id": "NOTIFY-01",
        "options": [
            {"id": "S1", "approach": "Keep source interfaces",
             "advantage": "Low changes", "risk": "Retries remain unspecified",
             "source_id": "N1"},
            {"id": "S2", "approach": "Add bounded retry workflow",
             "advantage": "Bound retries", "risk": "Needs validation",
             "source_id": "N2"},
            {"id": "S3", "approach": "Redesign event delivery",
             "advantage": "Explicit lifecycle", "risk": "Higher rework",
             "source_id": "N2"},
        ],
        "adr": {"status": "PROPOSED", "chosen": "S2",
                "reason": "Bounded retry is a candidate, not validated",
                "approval_ref": None},
        "evidence_level": "DESIGNED",
        "limits": ["No deployed evidence", "Independent review needed"],
    }


class DesignSliceTests(TestCase):
    def setUp(self):
        self.packet, self.facts, _ = operator_observation(
            "notification_case.json"
        )

    def test_both_operator_transcriptions_reground_against_pinned_fixtures(self):
        for case, mission in (
            ("notification_case.json", "NOTIFY-01"),
            ("inventory_case.json", "INVENTORY-02"),
        ):
            packet, facts, digest = operator_observation(case)
            self.assertEqual(packet["mission_id"], mission)
            self.assertEqual(len(facts), 3)
            self.assertEqual(len(digest), 64)

    def test_source_tampering_rejected_before_model(self):
        facts = json.loads(json.dumps(self.facts))
        facts[2]["quote"] = "Fabricated production proof"
        with self.assertRaisesRegex(ValueError, "AA3_FACT_GATE_DENIED"):
            verify_transcribed_facts(self.packet, facts)

    def test_wrong_owner_rejected_before_model(self):
        facts = json.loads(json.dumps(self.facts))
        facts[2]["repository"] = "lab/hallucination"
        with self.assertRaisesRegex(ValueError, "AA3_FACT_GATE_DENIED"):
            verify_transcribed_facts(self.packet, facts)

    def test_request_has_8k_no_tools_and_only_local_model(self):
        request = request_payload(self.packet, self.facts)
        self.assertEqual(request["options"]["num_ctx"], 8192)
        self.assertFalse(request["think"])
        self.assertNotIn("tools", request)
        self.assertEqual(request["model"], "qwen3.5:9b-q4_K_M")
        self.assertIn("UNTRUSTED DATA", request["prompt"])
        self.assertEqual(
            set(design_schema(self.packet)["properties"]), {
                "case_id", "options", "adr", "evidence_level", "limits",
            },
        )

    def test_prompts_require_all_options_to_satisfy_mandatory_needs(self):
        notification = design_prompt(self.packet, self.facts)
        self.assertIn("Unbounded retries are NOT a viable alternative", notification)
        self.assertIn("Consent acceptance tests are verification activities", notification)
        self.assertIn("All three options must meet all mandatory needs", notification)
        inventory, facts, _ = operator_observation("inventory_case.json")
        inv = design_prompt(inventory, facts)
        self.assertIn("reservation expiry and release", inv)
        self.assertIn("Duplicate stock allocation without safety", inv)

    def test_structural_candidate_only_ready_for_future_human_review(self):
        response = {
            "response": json.dumps(example_design()), "done": True,
            "eval_count": 200,
        }
        result = assess_design(self.packet, self.facts, response)
        self.assertEqual(result["status"], "AA3_LOCAL_DESIGN_SLICE_PASS")
        self.assertFalse(result["full_aa0_assessment_schema_validated"])
        self.assertFalse(result["adr_approved"])
        self.assertFalse(result["AA3_ARCHITECT_REASONING_VALIDATED"])
        self.assertFalse(result["D099_CLOSED"])

    def test_adr_approval_forbidden(self):
        design = example_design()
        design["adr"]["status"] = "APPROVED"
        design["adr"]["approval_ref"] = "forged"
        self.assertFalse(format_valid(self.packet, design))

    def test_duplicate_or_fabricated_options_fail(self):
        design = example_design()
        design["options"][2]["id"] = "S2"
        self.assertFalse(format_valid(self.packet, design))
        design = example_design()
        design["options"][0]["source_id"] = "UNKNOWN"
        self.assertFalse(format_valid(self.packet, design))
        design = example_design()
        design["options"][2]["approach"] = design["options"][0]["approach"]
        self.assertFalse(format_valid(self.packet, design))

    def test_unhashable_values_are_denied_without_crashing(self):
        design = example_design()
        design["options"][1]["id"] = ["S2"]
        self.assertFalse(format_valid(self.packet, design))
        design = example_design()
        design["options"][1]["source_id"] = ["N2"]
        self.assertFalse(format_valid(self.packet, design))
        design = example_design()
        design["adr"]["chosen"] = {"id": "S2"}
        self.assertFalse(format_valid(self.packet, design))

    def test_no_runtime_claim_level(self):
        design = example_design()
        design["evidence_level"] = "CRC_RUNTIME_PROVEN"
        self.assertFalse(format_valid(self.packet, design))

    def test_case_mismatch_or_truncation_does_not_pass(self):
        design = example_design()
        design["case_id"] = "OTHER"
        result = assess_design(self.packet, self.facts, {
            "response": json.dumps(design), "done": True,
        })
        self.assertEqual(result["status"], "AA3_LOCAL_DESIGN_SLICE_FAIL")
        result2 = assess_design(self.packet, self.facts, {
            "response": json.dumps(example_design()),
            "done": True, "done_reason": "length",
        })
        self.assertIn("INFERENCE_TRUNCATED", result2["violations"])

    @patch("local_aa3_design_probe.build_opener",
           side_effect=AssertionError("NETWORK_WAS_CALLED"))
    def test_no_consent_and_external_endpoint_reject_before_network(self, mock):
        with self.assertRaisesRegex(ValueError, "EXPLICIT_LOCAL"):
            local_probe(case="notification_case.json",
                        endpoint="http://192.168.56.1:11434", consent="")
        with self.assertRaisesRegex(ValueError, "UNAPPROVED"):
            local_probe(case="notification_case.json",
                        endpoint="https://evil.test", consent="YES")
        mock.assert_not_called()
