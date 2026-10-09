"""D-099 semantic and benchmark harness tests; synthetic, no live model."""
import copy
import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "evals"))
from precheck import inspect_assessment, precheck

ROOT = Path(__file__).resolve().parents[1]
def load(name):
    return json.loads((ROOT / name).read_text(encoding="utf-8"))

import unittest

class AA3PrecheckTests(unittest.TestCase):
    def test_both_reference_contracts_are_structurally_sound(self):
        for name in ("daarops", "sqy"):
            self.assertEqual(inspect_assessment(load(f"evals/golden/{name}.json")), [])

    def test_duplicate_option_is_denied(self):
        obj = load("evals/golden/daarops.json")
        obj["options"][1]["id"] = "S1"
        self.assertIn("OPTIONS_MUST_BE_S1_S2_S3_UNIQUE", inspect_assessment(obj))

    def test_repeated_approach_is_denied(self):
        obj = load("evals/golden/sqy.json")
        obj["options"][2]["approach"] = obj["options"][1]["approach"]
        self.assertIn("OPTIONS_NOT_DISTINCT", inspect_assessment(obj))

    def test_forged_decision_approval_is_denied(self):
        obj = load("evals/golden/daarops.json")
        obj["adr"]["status"] = "APPROVED"
        self.assertIn("ADR_APPROVAL_REF_MISSING", inspect_assessment(obj))

    def test_runtime_claim_requires_external_review(self):
        obj = load("evals/golden/sqy.json")
        obj["evidence"][0]["level"] = "CRC_RUNTIME_PROVEN"
        self.assertIn("EVIDENCE_NEEDS_INDEPENDENT_RUNTIME_REVIEW", inspect_assessment(obj))

    def test_self_reported_trajectory_cannot_validate(self):
        golden = load("evals/golden/daarops.json")
        out = precheck(golden, golden, trace={"provenance": "llm_self_report", "forbidden_actions": []})
        self.assertIn("TOOL_TRACE_NOT_INDEPENDENT", out["violations"])
        self.assertIs(out["AA3_ARCHITECT_REASONING_VALIDATED"], False)

    def test_no_trace_never_qualifies_a_candidate(self):
        case = load("evals/golden/sqy.json")
        report = precheck(case, case)
        self.assertEqual(report["violations"], [])
        self.assertEqual(report["trajectory"], "NO_INDEPENDENT_TRACE")
        self.assertIs(report["AA3_ARCHITECT_REASONING_VALIDATED"], False)

    def test_wrong_mission_id_fails_even_when_schema_is_valid(self):
        golden = load("evals/golden/daarops.json")
        candidate = copy.deepcopy(golden)
        candidate["mission"]["id"] = "mission-id-123"
        report = precheck(candidate, golden)
        self.assertIn("MISSION_ID_MISMATCH", report["violations"])
        self.assertEqual(report["case"], "mission-id-123")
        self.assertIs(report["AA3_ARCHITECT_REASONING_VALIDATED"], False)

    def test_missing_every_required_repo_is_not_ownership_success(self):
        golden = load("evals/golden/daarops.json")
        candidate = copy.deepcopy(golden)
        candidate["repositories"] = [{
            "name": "zdmooc/fictional-generic-repo",
            "canonical_owner": "UNVERIFIED",
            "revision": "unknown",
            "source": "synthetic"
        }]
        report = precheck(candidate, golden)
        self.assertEqual(
            sorted(v for v in report["violations"]
                   if v.startswith("REQUIRED_REPOSITORY_NOT_MAPPED:")),
            [
                "REQUIRED_REPOSITORY_NOT_MAPPED:zdmooc/argocd-expert-pack",
                "REQUIRED_REPOSITORY_NOT_MAPPED:zdmooc/cadrage_202682030",
                "REQUIRED_REPOSITORY_NOT_MAPPED:zdmooc/shared-platform-services-openshift",
            ],
        )
        self.assertIs(report["required_repositories_mapped"], False)
        self.assertIs(report["ownership_matches"], False)

    def test_wrong_owner_is_detected(self):
        golden = load("evals/golden/daarops.json")
        candidate = copy.deepcopy(golden)
        candidate["repositories"][0]["canonical_owner"] = "RUNTIME"
        report = precheck(candidate, golden)
        self.assertTrue(any(v.startswith("OWNERSHIP_MISMATCH:") for v in report["violations"]))
