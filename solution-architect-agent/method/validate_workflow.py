"""D-099 AA0: deterministic method-stage contract, not an execution engine."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
ORDER = (
    "DISCOVERY", "REQUIREMENTS", "REPO_MAPPING", "GAP_ANALYSIS",
    "OPTIONS", "ADR", "BACKLOG", "BUILD", "TEST_REVIEW",
    "RUNTIME", "EVIDENCE", "DEMO",
)
OWNERS = {
    "DISCOVERY": "maya-architect", "REQUIREMENTS": "maya-architect",
    "REPO_MAPPING": "maya-architect", "GAP_ANALYSIS": "maya-architect",
    "OPTIONS": "maya-architect", "ADR": "maya-architect",
    "BACKLOG": "maya-architect", "BUILD": "maya-builder",
    "TEST_REVIEW": "maya-reviewer", "RUNTIME": "maya-openshift-reader",
    "EVIDENCE": "maya-reviewer", "DEMO": "maya-architect",
}
HUMAN_GATES = frozenset({"ADR", "BUILD", "TEST_REVIEW", "RUNTIME"})


def check_stages(stages: object) -> list[str]:
    """Return explicit failures. Success verifies architecture *design* only."""
    if not isinstance(stages, list):
        return ["STAGES_NOT_LIST"]
    ids = [item.get("id") if isinstance(item, dict) else None for item in stages]
    errors: list[str] = []
    if tuple(ids) != ORDER:
        errors.append("STAGE_ORDER_OR_MEMBERSHIP_CHANGED")
    if len(ids) != len(set(str(i) for i in ids)):
        errors.append("DUPLICATE_STAGE")
    for item in stages:
        if not isinstance(item, dict) or item.get("id") not in OWNERS:
            continue
        stage_id = item["id"]
        if item.get("owner") != OWNERS[stage_id]:
            errors.append("STAGE_OWNER_MISMATCH:" + stage_id)
        if item.get("approval_gate") != (
            "AUTHENTICATED_HUMAN_APPROVAL" if stage_id in HUMAN_GATES else "NONE"
        ):
            errors.append("APPROVAL_GATE_MISMATCH:" + stage_id)
        for field in ("inputs", "outputs"):
            if not isinstance(item.get(field), list) or not item[field] or not all(
                isinstance(v, str) and v for v in item[field]
            ):
                errors.append("STAGE_" + field.upper() + "_INVALID:" + stage_id)
        if not isinstance(item.get("refusal"), str) or not item["refusal"]:
            errors.append("STAGE_REFUSAL_MISSING:" + stage_id)
    return sorted(set(errors))


def check_file(path: Path | None = None) -> list[str]:
    target = path or ROOT / "stages.json"
    return check_stages(json.loads(target.read_text(encoding="utf-8")))


if __name__ == "__main__":
    import sys
    faults = check_file()
    print(json.dumps({"status": "AA0_CONTRACT_STATIC_ONLY",
                      "violations": faults, "AA0_CLOSED": False}, indent=2))
    sys.exit(bool(faults))
