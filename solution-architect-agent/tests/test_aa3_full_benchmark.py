"""No-network benchmark assembly, provenance, denial and output regression."""
import json
import sys
from pathlib import Path
from unittest import TestCase
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "evals"))
from local_aa3_full_benchmark import (
    assemble_benchmark, prompt_for, request_payload, allowed_source_path,
    review_candidate, summarize_response,
)


class FullBenchmarkOfflineTests(TestCase):
    def test_both_historical_cases_pinned_without_goldens(self):
        for case, mission in (("daarops", "DAAROPS"), ("sqy", "SQY")):
            payload, meta = assemble_benchmark(case)
            self.assertEqual(payload["bundle"]["case_id"], mission)
            self.assertTrue(meta["source_blobs"])
            prompt = prompt_for(payload)
            self.assertIn("FROZEN_INPUT_JSON", prompt)
            self.assertIn("NOT a current runtime audit", prompt)
            self.assertNotIn('"required": [', prompt)
            # Mission documents can mention the withheld golden PATH as
            # a warning; that is not the golden CONTENT being exposed.
            golden_data = (ROOT / "evals/golden" / f"{case}.json").read_text()
            self.assertNotIn(golden_data, prompt)
            self.assertNotIn('"canonical_owner":"PRIMARY_CAAS_LIFECYCLE_N3"',
                             prompt)
            self.assertLessEqual(len(prompt), 23000)

    def test_request_single_local_json_schema_no_tools(self):
        packet, _ = assemble_benchmark("daarops")
        req = request_payload(packet)
        self.assertEqual(req["model"], "qwen3.5:9b-q4_K_M")
        self.assertEqual(req["options"]["num_ctx"], 8192)
        self.assertEqual(req["options"]["num_predict"], 2100)
        self.assertFalse(req["think"])
        self.assertFalse(req["stream"])
        self.assertEqual(req["keep_alive"], 0)
        self.assertNotIn("tools", req)
        self.assertIn("requirements", req["format"]["required"])

    def test_frozen_source_citations_bounded(self):
        p, _ = assemble_benchmark("daarops")
        source = p["bundle"]["sources"][0]["id"]
        self.assertTrue(allowed_source_path(p, source))
        self.assertTrue(allowed_source_path(
            p, "zdmooc/cadrage_202682030/" + source))
        self.assertFalse(allowed_source_path(p, "invented_proof.md"))

    def test_golden_is_host_only_and_wrong_mission_fails(self):
        p, _ = assemble_benchmark("daarops")
        from precheck import inspect_assessment
        golden = json.loads((ROOT / "evals/golden/daarops.json").read_text())
        self.assertFalse(inspect_assessment(golden))
        false_candidate = json.loads(json.dumps(golden))
        false_candidate["mission"]["id"] = "WRONG"
        review = review_candidate(false_candidate, p, "daarops")
        self.assertIn("MISSION_ID_MISMATCH", review["violations"])
        self.assertFalse(review["AA3_ARCHITECT_REASONING_VALIDATED"])

    def test_frozen_snapshot_no_runtime_promotion(self):
        p, _ = assemble_benchmark("daarops")
        golden = json.loads((ROOT / "evals/golden/daarops.json").read_text())
        golden["evidence"][0]["level"] = "CRC_RUNTIME_PROVEN"
        result = review_candidate(golden, p, "daarops")
        self.assertIn("CLAIM_LEVEL_EXCEEDS_FROZEN_SCOPE",
                      result["violations"])

    def test_unknown_source_rejected_even_on_correct_golden(self):
        p, _ = assemble_benchmark("daarops")
        golden = json.loads((ROOT / "evals/golden/daarops.json").read_text())
        golden["mission"]["source"] = "https://invalid.example/forged"
        review = review_candidate(golden, p, "daarops")
        self.assertIn("CITATION_NOT_IN_FROZEN_SOURCE_PACKET",
                      review["violations"])

    def test_truncated_model_output_never_passes(self):
        answer, errors, stats = summarize_response({
            "response": '{"version":', "done": False,
            "done_reason": "length", "eval_count": 2})
        self.assertIsNone(answer)
        self.assertIn("GENERATION_TRUNCATED", errors)
        self.assertIn("MODEL_JSON_NOT_VALID", errors)

    def test_no_data_never_qualifies(self):
        p, _ = assemble_benchmark("sqy")
        result = review_candidate([], p, "sqy")
        self.assertEqual(result["status"], "AA3_FULL_ASSESSMENT_STATIC_FAIL")
        self.assertFalse(result["AA3_ARCHITECT_REASONING_VALIDATED"])
