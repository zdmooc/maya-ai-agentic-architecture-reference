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

    def test_windows_executable_discovery_rejects_npm_stub(self):
        from tempfile import TemporaryDirectory
        with TemporaryDirectory() as folder:
            root = Path(folder)
            native = root / "node_modules" / "opencode-ai" / "node_modules" / (
                "opencode-windows-x64" ) / "bin" / "opencode.exe"
            native.parent.mkdir(parents=True)
            native.write_bytes(b"MZ" + b"0" * 1_000_001)
            stub = root / "node_modules" / "opencode-ai" / "bin" / "opencode.exe"
            stub.parent.mkdir(parents=True)
            stub.write_bytes(b"#!/bin/sh\\necho stub\\n")
            selected = PILOT._first_windows_native(
                PILOT._windows_native_candidates([root])
            )
            self.assertEqual(selected, native.resolve())

    def test_windows_placeholder_only_is_not_executable(self):
        from tempfile import TemporaryDirectory
        with TemporaryDirectory() as folder:
            root = Path(folder)
            stub = root / "node_modules" / "opencode-ai" / "bin" / "opencode.exe"
            stub.parent.mkdir(parents=True)
            stub.write_bytes(b"MZ" + b"0" * 400)
            self.assertIsNone(PILOT._first_windows_native(
                PILOT._windows_native_candidates([root])
            ))

    def test_missing_native_executable_returns_structured_result(self):
        from tempfile import TemporaryDirectory
        with TemporaryDirectory() as folder:
            with patch.object(PILOT, "pilot_one",
                              side_effect=FileNotFoundError("no exe")):
                with patch.object(PILOT, "assert_isolated_config",
                                  return_value={"model": PILOT.MODEL}):
                    with patch.dict(os.environ, {
                        "D099_ALLOW_LOCAL_INFERENCE": "YES",
                    }):
                        code = PILOT.main_argv([
                            "--case", "daarops", "--out", folder,
                        ])
            self.assertEqual(code, 2)
            report = json.loads((Path(folder) / "summary.json").read_text())
            self.assertEqual(
                report["cases"][0]["status"],
                "LOCAL_PILOT_WINDOWS_LAUNCH_BLOCKED",
            )

    def test_stderr_diagnostic_reports_categories_without_secret_text(self):
        import subprocess
        result = PILOT.safe_process_diagnostic(subprocess.CompletedProcess(
            args=["redacted"], returncode=1, stdout="",
            stderr="Unknown option --title; Bearer HIDDEN_SECRET and C:\\secret\\key.txt",
        ))
        self.assertEqual(result["stderr_categories"], ["CLI_OPTION_REJECTED"])
        self.assertEqual(result["stdout_bytes"], 0)
        self.assertGreater(result["stderr_bytes"], 0)
        self.assertNotIn("HIDDEN_SECRET", str(result))
        self.assertNotIn("key.txt", str(result))

    def test_stderr_empty_is_reported(self):
        import subprocess
        data = PILOT.safe_process_diagnostic(subprocess.CompletedProcess(
            args=[], returncode=1, stdout="", stderr="",
        ))
        self.assertEqual(data["stderr_categories"], ["NO_STDERR_CAPTURED"])

    def test_smoke_uses_short_prompt_and_same_process_runner(self):
        import subprocess
        from tempfile import TemporaryDirectory
        sample = '\n'.join([
            json.dumps({"type": "step_start", "part": {}}),
            json.dumps({"type": "text",
                        "part": {"type": "text", "text": "D099_LOCAL_SMOKE_OK"}}),
        ])
        with TemporaryDirectory() as folder:
            with patch.object(PILOT, "execute_local_turn", return_value=(
                subprocess.CompletedProcess(
                    args=["opencode"], returncode=0, stdout=sample, stderr="",
                )
            )) as invoke:
                outcome = PILOT.smoke_transport(Path(folder))
            self.assertEqual(outcome["status"], "LOCAL_OPENCODE_SMOKE_TRANSPORT_PASS")
            self.assertIn("text", outcome["event_types"])
            self.assertEqual(invoke.call_count, 1)
            self.assertLess(len(invoke.call_args.args[0]), 100)
            self.assertTrue((Path(folder) / "smoke.events.jsonl").exists())

    def test_failed_smoke_is_fail_closed_and_diagnostic_only(self):
        import subprocess
        from tempfile import TemporaryDirectory
        with TemporaryDirectory() as folder:
            with patch.object(PILOT, "execute_local_turn", return_value=(
                subprocess.CompletedProcess(
                    args=["opencode"], returncode=1, stdout="",
                    stderr="Error: unknown option --title",
                )
            )):
                outcome = PILOT.smoke_transport(Path(folder))
            self.assertEqual(outcome["status"], "LOCAL_OPENCODE_SMOKE_FAILED")
            self.assertFalse(outcome["AA3_ARCHITECT_REASONING_VALIDATED"])
            self.assertEqual(outcome["diagnostic"]["stderr_categories"],
                             ["CLI_OPTION_REJECTED"])

    def test_model_tool_call_is_disallowed(self):
        with self.assertRaisesRegex(ValueError, "MODEL_ATTEMPTED_TOOL_USE"):
            PILOT.extract(json.dumps({"type": "tool_use", "part": {}}) + "\n" +
                          json.dumps({"type": "text", "part": {"type": "text",
                                                              "text": '{"ok":true}'}}))


if __name__ == "__main__":
    unittest.main()
