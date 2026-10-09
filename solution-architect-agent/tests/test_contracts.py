"""D-099 static contract checks. Never claim LLM or OpenShift runtime."""
import json
from pathlib import Path
import unittest
from jsonschema import Draft202012Validator, ValidationError

ROOT = Path(__file__).resolve().parents[1]
def read(relative):
    return json.loads((ROOT / relative).read_text(encoding="utf-8"))

class D099Contracts(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.schema = read("method/assessment.schema.json")
        cls.roles = read("policies/role-profiles.json")
        cls.stages = read("method/stages.json")
        cls.validator = Draft202012Validator(cls.schema)

    def test_schema(self):
        Draft202012Validator.check_schema(self.schema)

    def test_two_golden_cases(self):
        for file in ("evals/golden/daarops.json", "evals/golden/sqy.json"):
            with self.subTest(file=file):
                case = read(file)
                self.validator.validate(case)
                self.assertEqual({x["id"] for x in case["options"]}, {"S1", "S2", "S3"})
                self.assertEqual(case["adr"]["status"], "PROPOSED")

    def test_negative_schema(self):
        case = read("evals/golden/daarops.json")
        del case["repositories"][0]["source"]
        with self.assertRaises(ValidationError):
            self.validator.validate(case)

    def test_fake_runtime_claim_level(self):
        case = read("evals/golden/sqy.json")
        case["evidence"][0]["level"] = "MAGIC_RUNTIME_PROVEN"
        with self.assertRaises(ValidationError):
            self.validator.validate(case)

    def test_stages_and_human_gates(self):
        self.assertEqual(len(self.stages), 12)
        self.assertEqual([x["id"] for x in self.stages][:3], ["DISCOVERY","REQUIREMENTS","REPO_MAPPING"])
        for s in self.stages:
            for key in ("inputs","outputs","owner","autonomy","approval_gate","validator","refusal"):
                self.assertTrue(s[key])
        self.assertEqual(self.stages[9]["approval_gate"],"AUTHENTICATED_HUMAN_APPROVAL")

    def test_roles_fail_closed(self):
        self.assertEqual(self.roles["default_decision"], "DENY")
        self.assertEqual(self.roles["profiles"]["maya-architect"]["edit"],"DENY")
        self.assertEqual(self.roles["profiles"]["maya-reviewer"]["edit"],"DENY")
        self.assertEqual(self.roles["profiles"]["maya-builder"]["git_push"],"DENY")
        self.assertEqual(self.roles["profiles"]["maya-openshift-reader"]["oc_apply"],"DENY")
        self.assertIn("approval_expiry_and_single_use",self.roles["required_guards"])
        self.assertIn("argocd app sync",self.roles["denied_commands"])

if __name__ == "__main__":
    unittest.main()
