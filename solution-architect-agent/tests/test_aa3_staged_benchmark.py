"""No HTTP: source-pinned 2-stage D099 benchmark safety regressions."""
import json
import tempfile
import sys
from pathlib import Path
from jsonschema import Draft202012Validator
from unittest import TestCase
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "evals"))

from local_aa3_staged_benchmark import (
    assemble_benchmark, clipped_schema, make_request,
    source_conformance, evaluate, process, check_previous, PROTOCOL,
    sha256_bytes,
)


class StagedBenchmarkTests(TestCase):
    def setUp(self):
        self.packet, _ = assemble_benchmark("daarops")

    def test_phase_schemas_are_disjoint_but_cover_full_11_keys(self):
        a = clipped_schema(self.packet["schema"], "stage1")
        b = clipped_schema(self.packet["schema"], "stage2")
        self.assertFalse(set(a["required"]) & set(b["required"]))
        self.assertEqual(set(a["required"]) | set(b["required"]),
                         set(self.packet["schema"]["required"]))
        self.assertEqual(a["properties"]["requirements"]["properties"]
                         ["FR"]["maxItems"], 3)
        self.assertEqual(b["properties"]["options"]["minItems"], 3)

    def test_stage1_freezes_goldens_and_never_calls_tools(self):
        req, digest = make_request(self.packet, "stage1")
        self.assertEqual(req["model"], "qwen3.5:9b-q4_K_M")
        self.assertEqual(req["options"]["num_ctx"], 8192)
        self.assertEqual(req["options"]["num_predict"], 1750)
        self.assertEqual(req["keep_alive"], 0)
        self.assertFalse(req["think"])
        self.assertNotIn("tools", req)
        self.assertIn("FROZEN_INPUT_JSON", req["prompt"])
        self.assertNotIn('"canonical_owner":"GOVERNANCE"', req["prompt"])
        self.assertEqual(len(digest), 64)

    def test_stage1_wrong_mission_and_repo_fail_closed(self):
        from jsonschema import Draft202012Validator
        source = self.packet["bundle"]["sources"][0]["id"]
        candidate = {
            "mission": {"id": "WRONG", "title": "Wrong", "source": source},
            "requirements": {"FR": [{
                "id": "FR1", "text": "Operator", "acceptance": "Reconcile",
                "source": source,
            }], "NFR": [{
                "id": "N1", "text": "Safety", "acceptance": "No mutation",
                "source": source,
            }]},
            "repositories": [{
                "name": "zdmooc/invented", "revision": "UNKNOWN",
                "canonical_owner": "FAKE", "source": source,
            }],
            "gaps": [],
        }
        self.assertFalse(list(Draft202012Validator(
            clipped_schema(self.packet["schema"], "stage1")
        ).iter_errors(candidate)))
        defects = source_conformance(self.packet, candidate)
        self.assertIn("STAGE1_MISSION_ID_MISMATCH", defects)
        self.assertIn("STAGE1_UNSOURCED_REPOSITORY", defects)

    def test_truncation_does_not_count_as_valid_json(self):
        model, faults = evaluate("stage1", self.packet, {
            "response": '{"mission": {"id":', "done": True,
            "done_reason": "length",
        })
        self.assertIsNone(model)
        self.assertIn("GENERATION_TRUNCATED", faults)
        self.assertIn("MODEL_JSON_NOT_VALID", faults)

    def test_a_valid_stage1_snapshot_is_rechecked_offline_before_stage2(self):
        src = self.packet["bundle"]["sources"][0]["id"]
        stage1 = {
            "mission": {"id": "DAAROPS", "title": "Operator assessment",
                        "source": src},
            "requirements": {
                "FR": [{"id": "FR1", "text": "Controller reconciliation",
                        "acceptance": "Observe and Manage boundaries",
                        "source": src}],
                "NFR": [{"id": "NFR1", "text": "No unsafe takeover",
                         "acceptance": "Owner conflict stops mutation",
                         "source": src}],
            },
            "repositories": [{
                "name": "zdmooc/shared-platform-services-openshift",
                "canonical_owner": "PLATFORM_OPERATOR",
                "revision": "UNKNOWN", "source": src,
            }],
            "gaps": [],
        }
        schema = clipped_schema(self.packet["schema"], "stage1")
        self.assertFalse(list(Draft202012Validator(schema).iter_errors(stage1)))
        self.assertEqual(source_conformance(self.packet, stage1), [])
        with tempfile.TemporaryDirectory() as temp:
            folder = Path(temp)
            artifact = json.dumps(stage1, ensure_ascii=False,
                                  sort_keys=True, indent=2).encode("utf-8")
            (folder / "stage1.candidate.local.json").write_bytes(artifact)
            (folder / "stage1.summary.json").write_text(json.dumps({
                "status": "AA3_STAGE1_STATIC_READY_FOR_REVIEW",
                "candidate_sha256": sha256_bytes(artifact),
                "protocol": PROTOCOL, "model": "qwen3.5:9b-q4_K_M",
                "case": "DAAROPS",
                "source_commit": self.packet["bundle"]["source_commit"],
            }))
            verified, _ = check_previous(self.packet, folder)
            self.assertEqual(verified, stage1)
            req, _ = make_request(self.packet, "stage2", verified)
            self.assertEqual(req["options"]["num_predict"], 1550)
            self.assertNotIn("tools", req)
            self.assertIn("STAGE1_MODEL_OUTPUT_UNTRUSTED_JSON", req["prompt"])
            # Tampering after summary creation must fail closed.
            (folder / "stage1.candidate.local.json").write_text("{}")
            with self.assertRaisesRegex(ValueError, "MISMATCH"):
                check_previous(self.packet, folder)

    def test_stage2_truncation_does_not_silently_merge(self):
        model, faults = evaluate("stage2", self.packet, {
            "response": "{", "done": True, "done_reason": "length",
        }, stage1={})
        self.assertIsNone(model)
        self.assertIn("GENERATION_TRUNCATED", faults)
        self.assertIn("MODEL_JSON_NOT_VALID", faults)

    @patch("local_aa3_staged_benchmark.build_opener",
           side_effect=AssertionError("MODEL_CALLED"))
    def test_no_consent_or_existing_dir_calls_model(self, model):
        with tempfile.TemporaryDirectory() as temp:
            out = Path(temp) / "D099-NOT-YET"
            with self.assertRaisesRegex(ValueError, "CONSENT"):
                process("stage1", "daarops",
                        "http://192.168.56.1:11434",
                        out, None, consent="")
            out.mkdir()
            with self.assertRaisesRegex(ValueError, "ALREADY_EXISTS"):
                process("stage1", "daarops",
                        "http://192.168.56.1:11434",
                        out, None, consent="YES")
            model.assert_not_called()

    def test_nonmatching_previous_stage_refused(self):
        with tempfile.TemporaryDirectory() as temp:
            base = Path(temp)
            (base / "stage1.summary.json").write_text(json.dumps({
                "status": "AA3_STAGE1_STATIC_READY_FOR_REVIEW",
                "case": "SQY", "protocol": PROTOCOL,
            }))
            (base / "stage1.candidate.local.json").write_text("{}")
            with self.assertRaisesRegex(ValueError, "MISMATCH"):
                check_previous(self.packet, base)
