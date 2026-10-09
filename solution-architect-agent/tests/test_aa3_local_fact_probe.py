"""No-network unittest coverage of the bounded D099 AA3 local fact probe."""
import json
import sys
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "evals"))
from independent.prepare_case import assemble_case
from local_aa3_fact_probe import (
    CONTEXT, ENDPOINTS, MODEL, assess_response, request_payload, single_probe,\n    facts_format_schema, identity_prompt,
)


def synthetic_facts():
    return [
        {"id": "M1", "kind": "mission", "value": "NOTIFY-01",
         "source_id": "N1",
         "quote": "Mission NOTIFY-01 covers notification preference management."},
        {"id": "R1", "kind": "repository", "repository": "lab/notification-api",
         "source_id": "N1",
         "quote": "Canonical repo lab/notification-api owns REST user preferences and opt-out enforcement."},
        {"id": "R2", "kind": "repository", "repository": "lab/event-relay",
         "source_id": "N2",
         "quote": "Canonical repo lab/event-relay owns delivery queue consumers, deduplication keys and delivery status events."},
    ]


class LocalAA3ProbeTests(unittest.TestCase):
    def setUp(self):
        self.packet, _ = assemble_case("notification_case.json")

    def test_prompt_is_bounded_8k_and_no_tools(self):
        payload = request_payload(self.packet)
        self.assertEqual(payload["model"], MODEL)
        self.assertEqual(payload["options"]["num_ctx"], 8192)
        self.assertEqual(payload["options"]["num_predict"], 384)
        self.assertFalse(payload["think"])
        self.assertFalse(payload["stream"])
        self.assertEqual(payload["format"], facts_format_schema(self.packet))\n        self.assertEqual(payload["format"]["properties"]["facts"]["minItems"], 0)\n        self.assertEqual(payload["format"]["properties"]["facts"]["maxItems"], 3)\n        self.assertIn("EXACTLY 3 facts", payload["prompt"])\n        self.assertIn("ONE mission", payload["prompt"])
        self.assertIn("facts", payload["prompt"])
        self.assertNotIn("tools", payload)

    def test_valid_synthetic_fact_output_still_never_closes_aa3(self):
        response = {"response": json.dumps({"facts": synthetic_facts()}),
                    "done": True, "eval_count": 120}
        report = assess_response(self.packet, response)
        self.assertEqual(report["status"], "AA3_LOCAL_FACT_GATE_PASS")
        self.assertFalse(report["AA3_ARCHITECT_REASONING_VALIDATED"])
        self.assertFalse(report["D099_CLOSED"])

    def test_missing_second_owner_is_denied(self):
        response = {"response": json.dumps({"facts": synthetic_facts()[:2]}),
                    "done": True}
        report = assess_response(self.packet, response)
        self.assertIn(
            "REQUIRED_REPOSITORY_FACT_MISSING_OR_DUPLICATE:lab/event-relay",
            report["violations"])

    def test_wrong_mission_or_unknown_repo_is_denied(self):
        facts = synthetic_facts()
        facts[0]["value"] = "WRONG"
        facts[1]["repository"] = "lab/hallucinated"
        report = assess_response(
            self.packet, {"response": json.dumps({"facts": facts}),
                          "done": True})
        self.assertIn("MISSION_ID_MISMATCH", report["violations"])
        self.assertIn("REPOSITORY_NOT_IN_TRUSTED_INVENTORY",
                      report["violations"])

    def test_real_2026_10_09_model_output_missing_identity_fields_fails(self):
        # Sanitized reproduction of actual HP output: correct quotes, no
        # mission value, no repository name, duplicate mission entry.
        observed = [
            {"id": "F001", "kind": "mission", "source_id": "N1",
             "quote": "Mission NOTIFY-01 covers notification preference management."},
            {"id": "F002", "kind": "repository", "source_id": "N1",
             "quote": "Canonical repo lab/notification-api owns REST user preferences and opt-out enforcement."},
            {"id": "F003", "kind": "mission", "source_id": "N2",
             "quote": "Mission NOTIFY-01 requires bounded asynchronous delivery."},
            {"id": "F004", "kind": "repository", "source_id": "N2",
             "quote": "Canonical repo lab/event-relay owns delivery queue consumers, deduplication keys and delivery status events."},
        ]
        outcome = assess_response(self.packet, {
            "response": json.dumps({"facts": observed}), "done": True,
            "eval_count": 231, "prompt_eval_count": 475,
            "total_duration": 181050000000, "load_duration": 24790000000,
        })
        self.assertEqual(outcome["status"], "AA3_LOCAL_FACT_GATE_FAIL")
        self.assertIn("MODEL_FACT_JSON_SCHEMA_INVALID", outcome["violations"])
        self.assertIn("MISSION_FACT_COUNT_INVALID", outcome["violations"])
        self.assertFalse(outcome["AA3_ARCHITECT_REASONING_VALIDATED"])

    def test_blank_wrong_fields_do_not_bypass_deterministic_gate(self):
        facts = synthetic_facts()
        for f in facts:
            f.setdefault("value", "")
            f.setdefault("repository", "")
        facts[1]["repository"] = "lab/not-real"
        result = assess_response(self.packet, {
            "response": json.dumps({"facts": facts}), "done": True,
        })
        self.assertIn("REPOSITORY_NOT_IN_TRUSTED_INVENTORY",
                      result["violations"])
        self.assertEqual(result["status"], "AA3_LOCAL_FACT_GATE_FAIL")

    def test_schema_mandates_all_identity_keys(self):
        payload = facts_format_schema(self.packet)
        fact = payload["properties"]["facts"]["items"]
        self.assertTrue({"value", "repository", "quote", "kind",
                         "source_id"} <= set(fact["required"]))
        self.assertEqual(payload["properties"]["facts"]["minItems"], 0)
        self.assertNotIn("lab/notification-api", str(payload))
        self.assertIn("value=empty string", identity_prompt(self.packet))

    def test_unexpected_root_shape_denied(self):
        report = assess_response(self.packet, {
            "response": json.dumps({"unexpected": []}), "done": True})
        self.assertIn("FACT_OUTPUT_MUST_HAVE_ONLY_FACTS_KEY",
                      report["violations"])

    def test_truncated_or_invalid_json_denied(self):
        report = assess_response(self.packet, {
            "response": "not-json", "done": False, "done_reason": "length"})
        self.assertIn("INFERENCE_NOT_COMPLETED", report["violations"])
        self.assertIn("INFERENCE_TRUNCATED", report["violations"])

    @patch("local_aa3_fact_probe.build_opener",
           side_effect=AssertionError("HTTP_CALLED"))
    def test_consent_denied_without_network(self, opener):
        with self.assertRaisesRegex(ValueError,
                                    "EXPLICIT_LOCAL_INFERENCE_CONSENT_REQUIRED"):
            single_probe(endpoint="http://192.168.56.1:11434",
                         case="notification_case.json", consent="")
        opener.assert_not_called()

    @patch("local_aa3_fact_probe.build_opener",
           side_effect=AssertionError("HTTP_CALLED"))
    def test_external_endpoint_denied_without_network(self, opener):
        with self.assertRaisesRegex(ValueError, "UNAPPROVED_OLLAMA_ENDPOINT"):
            single_probe(endpoint="http://bad.example:11434",
                         case="notification_case.json", consent="YES")
        opener.assert_not_called()


if __name__ == "__main__":
    unittest.main()
