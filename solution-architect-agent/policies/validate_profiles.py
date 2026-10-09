"""D-099 AA2: deterministic review of the *design* role matrix, no tool execution."""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PERMISSIONS = {
    "maya-architect": {
        "read": "ALLOW", "search": "ALLOW", "web": "ASK", "shell": "ASK",
        "edit": "DENY", "git_push": "DENY", "oc_mutation": "DENY",
    },
    "maya-reviewer": {
        "read": "ALLOW", "git_diff": "ALLOW", "tests": "ASK",
        "edit": "DENY", "git_push": "DENY", "auto_fix": "DENY",
    },
    "maya-builder": {
        "read": "ALLOW", "edit": "ASK", "tests": "ALLOW", "commit": "ASK",
        "git_push": "DENY", "runtime_mutation": "DENY",
        "workspace": "ISOLATED_WORKTREE",
    },
    "maya-openshift-reader": {
        "oc_get": "ALLOW_SCOPED", "oc_describe": "ALLOW_SCOPED",
        "oc_logs": "ALLOW_SCOPED", "oc_exec": "ASK",
        "oc_apply": "DENY", "oc_delete": "DENY",
    },
}
MANDATORY_GUARDS = {
    "authenticated_subject", "repo_allowlist", "namespace_allowlist",
    "file_scope_allowlist", "server_side_policy",
    "approval_action_hash_binding", "approval_expiry_and_single_use",
    "independent_reviewer_identity", "deny_by_default", "audit_redaction",
}
PROHIBITED_COMMANDS = {
    "git push", "git reset --hard", "git clean -fdx", "rm -rf",
    "oc apply", "oc delete", "kubectl apply", "kubectl delete",
    "argocd app sync", "helm upgrade",
}


def check_profiles(document: object) -> list[str]:
    if not isinstance(document, dict):
        return ["ROLE_DOCUMENT_INVALID"]
    errors: list[str] = []
    if document.get("version") != "D099-AA2-v1":
        errors.append("ROLE_VERSION_MISMATCH")
    if document.get("status") != "DESIGNED_NOT_ENFORCED":
        errors.append("ROLE_MUST_REMAIN_DESIGN_ONLY")
    if document.get("default_decision") != "DENY":
        errors.append("DEFAULT_DENY_REQUIRED")
    profiles = document.get("profiles")
    if not isinstance(profiles, dict) or set(profiles) != set(PERMISSIONS):
        errors.append("ROLE_SET_CHANGED")
    else:
        for role, expected in PERMISSIONS.items():
            if profiles.get(role) != expected:
                errors.append("PERMISSION_MATRIX_CHANGED:" + role)
    guards = document.get("required_guards")
    if not isinstance(guards, list) or not MANDATORY_GUARDS.issubset(set(
        str(item) for item in guards
    )):
        errors.append("REQUIRED_GUARDS_MISSING")
    denied = document.get("denied_commands")
    if not isinstance(denied, list) or not PROHIBITED_COMMANDS.issubset(set(
        str(item) for item in denied
    )):
        errors.append("MANDATORY_DENIED_COMMAND_MISSING")
    return sorted(set(errors))


def check_file() -> list[str]:
    return check_profiles(json.loads(
        (ROOT / "role-profiles.json").read_text(encoding="utf-8")))


if __name__ == "__main__":
    import sys
    violations = check_file()
    print(json.dumps({"status": "AA2_ROLE_DESIGN_VALIDATION_ONLY",
                      "violations": violations,
                      "AA2_RUNTIME_ENFORCEMENT_VERIFIED": False}, indent=2))
    sys.exit(bool(violations))
