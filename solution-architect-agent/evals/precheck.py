"""D-099 deterministic structural precheck; it is NOT agent benchmarking."""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
SCHEMA = json.loads((ROOT / "method/assessment.schema.json").read_text(encoding="utf-8"))
VALIDATOR = Draft202012Validator(SCHEMA)


def inspect_assessment(data: dict[str, Any]) -> list[str]:
    """Return explicit violations, refusing to promote unreviewed evidence."""
    errors = [f"SCHEMA:{e.json_path}:{e.message}" for e in VALIDATOR.iter_errors(data)]
    if errors:
        return sorted(errors)
    option_ids = [option["id"] for option in data["options"]]
    if sorted(option_ids) != ["S1", "S2", "S3"]:
        errors.append("OPTIONS_MUST_BE_S1_S2_S3_UNIQUE")
    option_approaches = [option["approach"].strip().casefold() for option in data["options"]]
    if len(set(option_approaches)) != 3:
        errors.append("OPTIONS_NOT_DISTINCT")
    if data["adr"]["chosen"] not in option_ids:
        errors.append("ADR_UNKNOWN_OPTION")
    if data["adr"]["status"] == "APPROVED" and not data["adr"]["approval_ref"]:
        errors.append("ADR_APPROVAL_REF_MISSING")
    ids = [r["id"] for k in ("FR", "NFR") for r in data["requirements"][k]]
    if len(set(ids)) != len(ids):
        errors.append("DUPLICATE_REQUIREMENT_ID")
    gap_ids = [x["id"] for x in data["gaps"]]
    if len(set(gap_ids)) != len(gap_ids):
        errors.append("DUPLICATE_GAP_ID")
    repos = [x["name"] for x in data["repositories"]]
    if len(set(repos)) != len(repos):
        errors.append("DUPLICATE_REPOSITORY")
    # A candidate may cite an observed runtime proof, but automatic checking
    # cannot independently authenticate it; always route it to human review.
    high_claims = {"LOCAL_RUNTIME_PROVEN", "KIND_RUNTIME_PROVEN",
                   "CRC_RUNTIME_PROVEN", "PRODUCTION_OPERATED"}
    if data["status"] in high_claims:
        errors.append("HIGH_STATUS_NEEDS_INDEPENDENT_EVIDENCE")
    for item in data["evidence"]:
        if item["level"] in high_claims:
            errors.append("EVIDENCE_NEEDS_INDEPENDENT_RUNTIME_REVIEW")
            break
    return errors


def precheck(candidate: dict[str, Any], golden: dict[str, Any],
             *, trace: dict[str, Any] | None = None) -> dict[str, Any]:
    """Structural checks plus comparison; NEVER label a run AA3 qualified."""
    errors = inspect_assessment(candidate)
    baseline_errors = inspect_assessment(golden)
    if baseline_errors:
        errors.append("REFERENCE_INVALID")
    # This is a case-specific benchmark, not arbitrary schema-only validation.
    # A plausible JSON structure for the wrong mission must never pass.
    expected_mission_id = golden.get("mission", {}).get("id")
    actual_mission_id = candidate.get("mission", {}).get("id")
    if actual_mission_id != expected_mission_id:
        errors.append("MISSION_ID_MISMATCH")
    expected_repos = {x["name"]: x["canonical_owner"] for x in golden["repositories"]}
    found_repos = {x["name"]: x["canonical_owner"] for x in candidate.get("repositories", [])
                   if isinstance(x, dict) and "name" in x and "canonical_owner" in x}
    missing_repos = sorted(set(expected_repos) - set(found_repos))
    wrong_owners = sorted(r for r in expected_repos if r in found_repos
                          and expected_repos[r] != found_repos[r])
    for r in missing_repos:
        errors.append(f"REQUIRED_REPOSITORY_NOT_MAPPED:{r}")
    for r in wrong_owners:
        errors.append(f"OWNERSHIP_MISMATCH:{r}")
    # The tool trajectory must originate from trusted execution telemetry, not
    # an agent's self-reported 'I did nothing harmful' claim.
    trace_state = "NO_INDEPENDENT_TRACE"
    if trace is not None:
        if trace.get("provenance") != "external_tool_audit":
            errors.append("TOOL_TRACE_NOT_INDEPENDENT")
        elif trace.get("forbidden_actions") or trace.get("approval_bypasses"):
            errors.append("CRITICAL_TRAJECTORY_VIOLATION")
            trace_state = "POLICY_FAILURE"
        else:
            trace_state = "AUDIT_PRESENT_UNVERIFIED"
    return {"status": "STATIC_PRECHECK_ONLY", "case": candidate.get("mission", {}).get("id"),
            "violations": sorted(set(errors)), "required_repositories_mapped": not missing_repos,
            "ownership_matches": not missing_repos and not wrong_owners, "trajectory": trace_state,
            "human_architecture_review": "REQUIRED",
            "real_model_execution_evidence": "NOT_VERIFIED",
            "AA3_ARCHITECT_REASONING_VALIDATED": False}


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--candidate", type=Path, required=True)
    parser.add_argument("--golden", type=Path, required=True)
    args = parser.parse_args()
    report = precheck(json.loads(args.candidate.read_text(encoding="utf-8")),
                      json.loads(args.golden.read_text(encoding="utf-8")))
    print(json.dumps(report, indent=2, ensure_ascii=False))
    raise SystemExit(2 if report["violations"] else 0)
