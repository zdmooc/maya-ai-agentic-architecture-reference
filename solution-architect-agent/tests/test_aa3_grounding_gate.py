"""AA3 staged fact/quote grounding. No OpenCode/Ollama or real repo calls."""
import copy
import hashlib
import importlib.util
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location(
    "aa3_facts", ROOT / "evals" / "grounding_gate.py")
gate = importlib.util.module_from_spec(spec)
spec.loader.exec_module(gate)


def fixture():
    text = "Mission NOTIFY-01 migrates alerts. Canonical repo is lab/notify. Retry must be bounded."
    packet = {
        "mission_id": "NOTIFY-01",
        "sources": [{"id": "S-01", "text": text,
                     "sha256": hashlib.sha256(text.encode()).hexdigest()}],
        "repository_sources": {"lab/notify": "S-01"},
    }
    facts = [
        {"id": "F1", "kind": "mission", "value": "NOTIFY-01",
         "source_id": "S-01", "quote": "Mission NOTIFY-01 migrates alerts."},
        {"id": "F2", "kind": "repository", "repository": "lab/notify",
         "source_id": "S-01", "quote": "Canonical repo is lab/notify."},
        {"id": "F3", "kind": "requirement", "source_id": "S-01",
         "quote": "Retry must be bounded."},
    ]
    return packet, facts


class GroundingTests(unittest.TestCase):
    def test_exact_quotes_pass_only_lexical_check(self):
        packet, facts = fixture()
        result = gate.evaluate_facts(packet, facts)
        self.assertEqual(result["violations"], [])
        self.assertTrue(result["lexical_grounding_pass"])
        self.assertFalse(result["may_generate_approved_adr"])

    def test_model_invented_repo_is_rejected(self):
        packet, facts = fixture()
        facts[1]["repository"] = "lab/nonexistent"
        self.assertIn("REPOSITORY_NOT_IN_TRUSTED_INVENTORY",
                      gate.evaluate_facts(packet, facts)["violations"])

    def test_untrusted_quote_is_rejected(self):
        packet, facts = fixture()
        facts[2]["quote"] = "Production tested on 9 sites."
        self.assertIn("QUOTE_NOT_IN_PINNED_SOURCE",
                      gate.evaluate_facts(packet, facts)["violations"])

    def test_rewritten_sources_fail_digest(self):
        packet, facts = fixture()
        packet["sources"][0]["text"] = "Altered source material."
        report = gate.evaluate_facts(packet, facts)
        self.assertTrue(any("SOURCE_DIGEST_MISMATCH" in v for v in report["violations"]))

    def test_wrong_mission_and_duplicate_fact_are_rejected(self):
        packet, facts = fixture()
        facts[0]["value"] = "OTHER-CASE"
        facts[1]["id"] = "F1"
        report = gate.evaluate_facts(packet, facts)
        self.assertIn("MISSION_ID_MISMATCH", report["violations"])
        self.assertIn("FACT_ID_INVALID_OR_DUPLICATE", report["violations"])



    def test_second_expected_repo_must_have_its_own_fact(self):
        packet, facts = fixture()
        packet["repository_sources"]["lab/another"] = "S-01"
        faults = gate.evaluate_facts(packet, facts)["violations"]
        self.assertIn("REQUIRED_REPOSITORY_FACT_MISSING_OR_DUPLICATE:lab/another", faults)

    def test_duplicate_owner_fact_fails(self):
        packet, facts = fixture()
        duplicate = dict(facts[1])
        duplicate["id"] = "F4"
        facts.append(duplicate)
        faults = gate.evaluate_facts(packet, facts)["violations"]
        self.assertIn("REQUIRED_REPOSITORY_FACT_MISSING_OR_DUPLICATE:lab/notify", faults)

    def test_quote_must_explicitly_name_its_mission_and_repository(self):
        packet, facts = fixture()
        facts[0]["quote"] = "Retry must be bounded."
        facts[1]["quote"] = "Retry must be bounded."
        faults = gate.evaluate_facts(packet, facts)["violations"]
        self.assertIn("MISSION_ID_NOT_IN_QUOTE", faults)
        self.assertIn("REPOSITORY_NAME_NOT_IN_QUOTE", faults)


if __name__ == "__main__":
    unittest.main()
