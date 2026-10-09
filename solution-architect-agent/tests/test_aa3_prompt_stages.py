"""AA3 two-prompt construction uses fictional, locally pinned sources only."""
import json
import sys
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "evals"))
from independent.prepare_case import assemble
from prompt_stages import build_fact_prompt, build_design_prompt
from test_aa3_staged_review import sample


class AA3PromptStagesTests(unittest.TestCase):
    def test_fact_prompt_is_source_packet_only(self):
        packet, _ = assemble()
        prompt = build_fact_prompt(packet)
        self.assertIn("NOTIFY-01", prompt)
        self.assertIn("SOURCE_PACKET_JSON", prompt)
        self.assertIn("UNTRUSTED DATA", prompt)
        self.assertNotIn("DAAROPS", prompt)
        self.assertNotIn("golden", prompt.casefold())

    def test_design_prompt_requires_all_grounded_repository_facts(self):
        packet, _ = assemble()
        facts, _ = sample()
        prompt = build_design_prompt(packet, facts)
        self.assertIn("FACTS_AND_HOST_INVENTORY_JSON", prompt)
        self.assertIn("lab/event-relay", prompt)
        self.assertIn("status=PROPOSED", prompt)
        self.assertNotIn("SOURCE_PACKET_JSON", prompt)

    def test_bad_fact_blocks_design_prompt(self):
        packet, _ = assemble()
        facts, _ = sample()
        facts[2]["quote"] = "fabricated missing source"
        with self.assertRaisesRegex(ValueError, "AA3_FACT_GATE_DENIED"):
            build_design_prompt(packet, facts)

    def test_wrong_owner_blocks_design_prompt(self):
        packet, _ = assemble()
        facts, _ = sample()
        facts[2]["repository"] = "lab/imaginary"
        with self.assertRaisesRegex(ValueError, "AA3_FACT_GATE_DENIED"):
            build_design_prompt(packet, facts)

    def test_missing_host_packet_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "AA3_UNPINNED_SOURCE_PACKET"):
            build_fact_prompt({"mission_id": "NOTIFY-01", "sources": []})


if __name__ == "__main__":
    unittest.main()
