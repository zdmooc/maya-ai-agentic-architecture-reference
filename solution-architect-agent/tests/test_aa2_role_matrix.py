"""AA2 role design guards, no model, credentials or runtime access."""
import copy
import importlib.util
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location(
    "aa2_role_contract", ROOT / "policies" / "validate_profiles.py")
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
ROLES = json.loads(
    (ROOT / "policies" / "role-profiles.json").read_text(encoding="utf-8"))


class AA2RoleContractTests(unittest.TestCase):
    def test_matrix_matches_declared_policy(self):
        self.assertEqual(mod.check_profiles(ROLES), [])

    def test_rejects_builder_push_and_runtime_tool(self):
        for key in ("git_push", "runtime_mutation"):
            data = copy.deepcopy(ROLES)
            data["profiles"]["maya-builder"][key] = "ALLOW"
            self.assertIn("PERMISSION_MATRIX_CHANGED:maya-builder",
                          mod.check_profiles(data))

    def test_rejects_oc_delete_even_if_scope_is_valid(self):
        data = copy.deepcopy(ROLES)
        data["profiles"]["maya-openshift-reader"]["oc_delete"] = "ALLOW_SCOPED"
        self.assertIn("PERMISSION_MATRIX_CHANGED:maya-openshift-reader",
                      mod.check_profiles(data))

    def test_rejects_automatic_approval_and_weakening(self):
        data = copy.deepcopy(ROLES)
        data["default_decision"] = "ALLOW"
        data["required_guards"].remove("approval_expiry_and_single_use")
        self.assertIn("DEFAULT_DENY_REQUIRED", mod.check_profiles(data))
        self.assertIn("REQUIRED_GUARDS_MISSING", mod.check_profiles(data))

    def test_agent_cannot_claim_implemented_policy(self):
        data = copy.deepcopy(ROLES)
        data["status"] = "RUNTIME_PROVEN"
        self.assertIn("ROLE_MUST_REMAIN_DESIGN_ONLY", mod.check_profiles(data))

    def test_unknown_privileged_role_and_dangerous_command_fail(self):
        data = copy.deepcopy(ROLES)
        data["profiles"]["maya-root"] = {"shell": "ALLOW"}
        data["denied_commands"].remove("argocd app sync")
        self.assertIn("ROLE_SET_CHANGED", mod.check_profiles(data))
        self.assertIn("MANDATORY_DENIED_COMMAND_MISSING", mod.check_profiles(data))


if __name__ == "__main__":
    unittest.main()
