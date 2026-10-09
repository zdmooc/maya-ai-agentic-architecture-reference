"""D-099 AA0 method tests are purely synthetic; no model/tools/CRC."""
import copy
import importlib.util
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location(
    "d099_method_contract", ROOT / "method" / "validate_workflow.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
STAGES = json.loads((ROOT / "method" / "stages.json").read_text(encoding="utf-8"))


class MethodContractTests(unittest.TestCase):
    def test_canonical_method_is_static_valid(self):
        self.assertEqual(module.check_stages(STAGES), [])
        self.assertEqual(len(STAGES), 12)

    def test_reordered_stage_is_rejected(self):
        mutated = copy.deepcopy(STAGES)
        mutated[0], mutated[1] = mutated[1], mutated[0]
        self.assertIn("STAGE_ORDER_OR_MEMBERSHIP_CHANGED",
                      module.check_stages(mutated))

    def test_no_weakening_human_gates(self):
        for stage in module.HUMAN_GATES:
            mutated = copy.deepcopy(STAGES)
            next(x for x in mutated if x["id"] == stage)["approval_gate"] = "NONE"
            self.assertIn("APPROVAL_GATE_MISMATCH:" + stage,
                          module.check_stages(mutated))

    def test_stage_owner_cannot_claim_runtime(self):
        mutated = copy.deepcopy(STAGES)
        next(x for x in mutated if x["id"] == "RUNTIME")["owner"] = "maya-builder"
        self.assertIn("STAGE_OWNER_MISMATCH:RUNTIME",
                      module.check_stages(mutated))

    def test_malformed_or_missing_inputs_fail_closed(self):
        mutated = copy.deepcopy(STAGES)
        mutated[0]["inputs"] = []
        self.assertIn("STAGE_INPUTS_INVALID:DISCOVERY",
                      module.check_stages(mutated))
        self.assertEqual(module.check_stages({}), ["STAGES_NOT_LIST"])


if __name__ == "__main__":
    unittest.main()
