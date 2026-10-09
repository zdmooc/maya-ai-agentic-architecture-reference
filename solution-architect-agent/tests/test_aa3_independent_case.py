"""AA3 I5 independent synthetic fixture and golden non-disclosure."""
import importlib.util
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1] / "evals" / "independent"
spec = importlib.util.spec_from_file_location(
    "independent_packet", ROOT / "prepare_case.py")
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)


class IndependentCaseTests(unittest.TestCase):
    def test_packet_is_not_real_customer_or_repository(self):
        packet, metadata = mod.assemble()
        self.assertEqual(packet["mission_id"], "NOTIFY-01")
        self.assertEqual(set(packet["repository_sources"]),
                         {"lab/notification-api", "lab/event-relay"})
        self.assertEqual(metadata["source_provenance"],
                         "FICTIONAL_FIXTURE_PIN_TO_COMMIT_BEFORE_MODEL_RUN")
        self.assertFalse(metadata["model_invoked"])

    def test_no_reference_or_response_leakage(self):
        packet, metadata = mod.assemble()
        self.assertFalse(metadata["reference_exposed"])
        self.assertNotIn("reference", packet)
        self.assertNotIn("golden", packet)
        self.assertNotIn("chosen", packet)
        self.assertNotIn("solution", packet)

    def test_sources_have_valid_self_consistency_digests(self):
        import hashlib
        packet, _ = mod.assemble()
        for src in packet["sources"]:
            self.assertEqual(src["sha256"],
                             hashlib.sha256(src["text"].encode()).hexdigest())

    def test_source_ids_cover_repository_mapping(self):
        packet, _ = mod.assemble()
        ids = {source["id"] for source in packet["sources"]}
        self.assertTrue(set(packet["repository_sources"].values()) <= ids)


if __name__ == "__main__":
    unittest.main()
