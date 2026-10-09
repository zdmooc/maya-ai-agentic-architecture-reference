"""D099 M3 frozen source and pilot contract tests; never start OpenCode."""
import importlib.util
import json
import os
from pathlib import Path
import unittest
from unittest.mock import patch

HERE = Path(__file__).resolve().parents[1]
SCRIPT = HERE / "evals" / "run_aa3_pilot.py"
SPEC = importlib.util.spec_from_file_location("d099_aa3_pilot", SCRIPT)
PILOT = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(PILOT)


def config():
    return {
        "model": "ollama/qwen2.5:3b",
        "enabled_providers": ["ollama"],
        "provider": {"ollama": {
            "npm": "@ai-sdk/openai-compatible",
            "models": {"qwen2.5:3b": {"name": "Qwen 2.5 3B"}},
            "options": {"baseURL": "http://192.168.56.1:11434/v1"}}},
        "permission": {"*": "deny", "bash": "deny", "edit": "deny"},
        "agent": {"plan": {"permission": {"*": "deny"}}},
        "share": "disabled", "autoupdate": False,
    }


class AA3PilotTests(unittest.TestCase):
    def test_frozen_sources_verified_for_both_cases(self):
        for case in ("daarops", "sqy"):
            prompt, meta = PILOT.assemble(case)
            self.assertGreater(meta["characters"], 5000)
            self.assertLess(meta["characters"], PILOT.MAX_PROMPT)
            self.assertEqual(len(meta["source_git_blobs"]), 1)
            self.assertIn("MISSION:", prompt)
            self.assertIn("SCHEMA:", prompt)
            self.assertNotIn("ADR-D099-GOLDEN-DAAROPS", prompt)
            self.assertNotIn("ADR-D099-GOLDEN-SQY", prompt)
            self.assertNotIn("ARCHITECT_REASONING_VALIDATED=true", prompt)

    def test_local_deny_only_config_accepted(self):
        with patch.dict(os.environ, {
            "OPENCODE_CONFIG_CONTENT": json.dumps(config()),
        }):
            self.assertEqual(
                PILOT.assert_isolated_config()["policy_config"],
                "DENY_ONLY_REQUESTED",
            )

    def test_reject_remote_provider_and_approval_opening(self):
        bad = config()
        bad["enabled_providers"] = ["ollama", "openai"]
        with patch.dict(os.environ, {"OPENCODE_CONFIG_CONTENT": json.dumps(bad)}):
            with self.assertRaisesRegex(ValueError, "PROVIDER_ALLOWLIST_INVALID"):
                PILOT.assert_isolated_config()
        bad = config()
        bad["agent"]["plan"]["permission"]["bash"] = "allow"
        with patch.dict(os.environ, {"OPENCODE_CONFIG_CONTENT": json.dumps(bad)}):
            with self.assertRaisesRegex(ValueError, "TOOL_PERMISSION_OPEN"):
                PILOT.assert_isolated_config()

    def test_parses_candidate_but_never_qualifies(self):
        lines = [
            json.dumps({"type": "step_start", "part": {"type": "step-start"}}),
            json.dumps({"type": "text", "part": {"type": "text",
                                                "text": '{"mission":{"id":"sqy"}}'}}),
            json.dumps({"type": "step_finish",
                        "part": {"tokens": {"total": 50}}}),
        ]
        obj, trace = PILOT.extract("\n".join(lines))
        self.assertEqual(obj["mission"]["id"], "sqy")
        self.assertEqual(trace["external_tool_audit"], "NOT_PRESENT")

    def test_one_shot_config_generated_when_absent(self):
        with patch.dict(os.environ, {
            "OLLAMA_HOST": "192.168.56.1:11434",
        }):
            os.environ.pop("OPENCODE_CONFIG_CONTENT", None)
            data = PILOT.assert_isolated_config()
            self.assertEqual(data["model"], "ollama/qwen2.5:3b")
            cfg = json.loads(os.environ["OPENCODE_CONFIG_CONTENT"])
            self.assertEqual(cfg["permission"]["bash"], "deny")
            self.assertEqual(cfg["provider"]["ollama"]["options"]["baseURL"],
                             "http://192.168.56.1:11434/v1")
            os.environ.pop("OPENCODE_CONFIG_CONTENT", None)

    def test_rejects_remote_host_auto_configuration(self):
        with patch.dict(os.environ, {"OLLAMA_HOST": "evil.invalid:11434"}):
            os.environ.pop("OPENCODE_CONFIG_CONTENT", None)
            with self.assertRaisesRegex(ValueError, "OLLAMA_HOST_NOT_APPROVED"):
                PILOT.assert_isolated_config()

    def test_child_environment_redacts_host_tokens_and_proxy(self):
        with patch.dict(os.environ, {
            "GH_TOKEN": "PRIVATE_GITHUB_TOKEN",
            "KUBECONFIG": "/private/kubeconfig",
            "AWS_SECRET_ACCESS_KEY": "PRIVATE_AWS_KEY",
            "HTTP_PROXY": "http://untrusted-proxy.invalid",
            "OPENCODE_CONFIG_CONTENT": json.dumps(config()),
        }):
            env = PILOT.child_environment()
            self.assertNotIn("GH_TOKEN", env)
            self.assertNotIn("KUBECONFIG", env)
            self.assertNotIn("AWS_SECRET_ACCESS_KEY", env)
            self.assertNotIn("HTTP_PROXY", env)
            self.assertIn("OPENCODE_CONFIG_CONTENT", env)
            self.assertEqual(env["OPENCODE_DISABLE_DEFAULT_PLUGINS"], "1")

    def test_extra_plugin_definition_is_rejected(self):
        bad = config()
        bad["mcp"] = {"malicious": {"type": "local", "command": ["bash"]}}
        with patch.dict(os.environ, {"OPENCODE_CONFIG_CONTENT": json.dumps(bad)}):
            with self.assertRaisesRegex(ValueError, "EXTRA_TOOLS_OR_PLUGINS"):
                PILOT.assert_isolated_config()

    def test_model_tool_call_is_disallowed(self):
        with self.assertRaisesRegex(ValueError, "MODEL_ATTEMPTED_TOOL_USE"):
            PILOT.extract(json.dumps({"type": "tool_use", "part": {}}) + "\n" +
                          json.dumps({"type": "text", "part": {"type": "text",
                                                              "text": '{"ok":true}'}}))


if __name__ == "__main__":
    unittest.main()
