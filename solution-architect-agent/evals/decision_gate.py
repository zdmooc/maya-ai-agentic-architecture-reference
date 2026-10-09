"""D-099 AA3 I4: deterministic architecture decision review, never approval."""
from __future__ import annotations
import json
from pathlib import Path
from typing import Any
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
SCHEMA = json.loads((ROOT / "method" / "assessment.schema.json").read_text(
    encoding="utf-8"))
VALIDATOR = Draft202012Validator(SCHEMA)


def evaluate_design(candidate: object, packet: dict[str, Any],
                    fact_report: dict[str, Any]) -> dict[str, Any]:
    """Validate an output against host-pinned scenario identity and owners.

    Static checks neither prove source relevance nor authorize ADR/changes.
    """
    problems: list[str] = []
    if not isinstance(candidate, dict):
        problems.append("CANDIDATE_NOT_OBJECT")
    else:
        violations = sorted(VALIDATOR.iter_errors(candidate), key=lambda e: e.json_path)
        problems.extend("SCHEMA:" + e.json_path for e in violations)
        if not violations:
            mission = packet.get("mission_id")
            if candidate["mission"]["id"] != mission:
                problems.append("MISSION_ID_MISMATCH")
            owners = packet.get("repository_sources")
            if not isinstance(owners, dict) or not owners:
                problems.append("HOST_INVENTORY_REQUIRED")
                owners = {}
            mapped = [r["name"] for r in candidate["repositories"]]
            for required in owners:
                if required not in mapped:
                    problems.append("REPOSITORY_REQUIRED_MISSING:" + required)
            for name in mapped:
                if name not in owners:
                    problems.append("REPOSITORY_NOT_IN_TRUSTED_INVENTORY:" + name)
            if len(set(mapped)) != len(mapped):
                problems.append("DUPLICATE_REPOSITORY")
            if {opt["id"] for opt in candidate["options"]} != {"S1", "S2", "S3"}:
                problems.append("OPTIONS_MUST_BE_S1_S2_S3")
            approaches = [opt["approach"].strip().casefold()
                          for opt in candidate["options"]]
            if len(set(approaches)) != 3:
                problems.append("OPTIONS_NOT_DISTINCT")
            adr = candidate["adr"]
            if (adr["status"] != "PROPOSED" or adr["approval_ref"] is not None):
                problems.append("ADR_MUST_BE_UNAPPROVED_PROPOSAL")
            if adr["chosen"] not in {opt["id"] for opt in candidate["options"]}:
                problems.append("ADR_UNKNOWN_OPTION")
            if candidate["status"] not in {"PLANNED", "DESIGNED"} or any(
                e["level"] not in {"PLANNED", "DESIGNED"}
                for e in candidate["evidence"]
            ):
                problems.append("UNVERIFIED_RUNTIME_OR_CI_CLAIM")
    if fact_report.get("lexical_grounding_pass") is not True or (
        fact_report.get("violations")
    ):
        problems.append("FACT_GATE_NOT_PASSED")
    result = sorted(set(problems))
    return {
        "status": "AA3_STATIC_DESIGN_REVIEW_ONLY",
        "violations": result,
        "may_request_human_review": not result,
        "adr_approved": False,
        "builder_authorized": False,
        "AA3_ARCHITECT_REASONING_VALIDATED": False,
    }
