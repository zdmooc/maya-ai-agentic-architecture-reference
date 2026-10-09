"""AA3 OpenCode JSONL extraction unit tests. No model or network."""
import importlib.util
import json
from pathlib import Path
import unittest

PATH = Path(__file__).resolve().parents[1] / "evals" / "extract_opencode_candidate.py"
SPEC = importlib.util.spec_from_file_location("aa3_extraction", PATH)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


def event(kind, **part):
    return {"type": kind, "part": part}


class AA3TraceTests(unittest.TestCase):
    def test_extracts_strict_json_and_remains_unverified(self):
        events = [
            event("step_start", type="step-start"),
            event("text", type="text", text='{"mission":{"id":"DAAROPS"}}'),
            event("step_finish", type="step-finish",
                  tokens={"total": 15, "input": 10, "output": 5}),
        ]
        out = MODULE.extract(events)
        self.assertEqual(out["candidate"]["mission"]["id"], "DAAROPS")
        self.assertEqual(out["metadata"]["reported_tokens"]["total"], 15)
        self.assertIs(out["metadata"]["AA3_ARCHITECT_REASONING_VALIDATED"], False)

    def test_rejects_non_json_explanation(self):
        events = [event("text", type="text", text="I would produce JSON")]
        with self.assertRaises(MODULE.CandidateExtractionError):
            MODULE.extract(events)

    def test_rejects_missing_text(self):
        with self.assertRaises(MODULE.CandidateExtractionError):
            MODULE.extract([event("step_finish", type="step-finish")])

    def test_does_not_claim_runtime_tool_audit(self):
        events = [
            event("tool_use", type="tool", name="bash"),
            event("text", type="text", text='{"status":"DESIGNED"}'),
        ]
        out = MODULE.extract(events)
        self.assertEqual(out["metadata"]["independent_tool_audit"], "NOT_PRESENT")
        self.assertIs(out["metadata"]["AA3_ARCHITECT_REASONING_VALIDATED"], False)

    def test_rejects_non_object_json(self):
        with self.assertRaises(MODULE.CandidateExtractionError):
            MODULE.extract([event("text", type="text", text='[1,2,3]')])

    def test_jsonl_parser(self):
        from tempfile import TemporaryDirectory
        with TemporaryDirectory() as folder:
            path = Path(folder) / "trace.jsonl"
            path.write_text("\n".join([
                json.dumps(event("step_start", type="step-start")),
                json.dumps(event("text", type="text", text='{"ok":true}')),
            ]), encoding="utf-8")
            self.assertEqual(len(MODULE.read_events(path)), 2)


if __name__ == "__main__":
    unittest.main()
