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

def test_both_reference_contracts_are_structurally_sound():
    for name in ("daarops", "sqy"):
        assert inspect_assessment(load(f"evals/golden/{name}.json")) == []

def test_duplicate_option_is_denied():
    obj = load("evals/golden/daarops.json")
    obj["options"][1]["id"] = "S1"
    assert "OPTIONS_MUST_BE_S1_S2_S3_UNIQUE" in inspect_assessment(obj)

def test_repeated_approach_is_denied():
    obj = load("evals/golden/sqy.json")
    obj["options"][2]["approach"] = obj["options"][1]["approach"]
    assert "OPTIONS_NOT_DISTINCT" in inspect_assessment(obj)

def test_forged_decision_approval_is_denied():
    obj = load("evals/golden/daarops.json")
    obj["adr"]["status"] = "APPROVED"
    assert "ADR_APPROVAL_REF_MISSING" in inspect_assessment(obj)

def test_runtime_claim_requires_external_review():
    obj = load("evals/golden/sqy.json")
    obj["evidence"][0]["level"] = "CRC_RUNTIME_PROVEN"
    assert "EVIDENCE_NEEDS_INDEPENDENT_RUNTIME_REVIEW" in inspect_assessment(obj)

def test_self_reported_trajectory_cannot_validate():
    golden = load("evals/golden/daarops.json")
    out = precheck(golden, golden, trace={"provenance": "llm_self_report", "forbidden_actions": []})
    assert "TOOL_TRACE_NOT_INDEPENDENT" in out["violations"]
    assert out["AA3_ARCHITECT_REASONING_VALIDATED"] is False

def test_no_trace_never_qualifies_a_candidate():
    case = load("evals/golden/sqy.json")
    report = precheck(case, case)
    assert report["violations"] == []
    assert report["trajectory"] == "NO_INDEPENDENT_TRACE"
    assert report["AA3_ARCHITECT_REASONING_VALIDATED"] is False

def test_wrong_owner_is_detected():
    golden = load("evals/golden/daarops.json")
    candidate = copy.deepcopy(golden)
    candidate["repositories"][0]["canonical_owner"] = "RUNTIME"
    report = precheck(candidate, golden)
    assert any(v.startswith("OWNERSHIP_MISMATCH:") for v in report["violations"])
