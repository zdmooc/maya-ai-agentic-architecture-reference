"""D099 AA4 I6: validate an inert, synthetic worktree plan; never execute it."""
from __future__ import annotations
import re
from typing import Any

TEST_IDS = frozenset({"UNIT", "SCHEMA", "POLICY_NEGATIVE"})
REPO = "lab/notification-api"  # fictional isolated fixture only
STEPS = frozenset({"prepare", "edit", "test", "review", "rollback"})


def _safe_file(path: Any) -> bool:
    if not isinstance(path, str) or not path or len(path) > 240:
        return False
    if path.startswith(("/", "\\")) or "\\" in path or ":" in path or "\x00" in path:
        return False
    parts = path.split("/")
    if any(p in ("", ".", "..") or p.startswith(".") for p in parts):
        return False
    if any(p.lower() in {"secret", "secrets", "credentials", "kubeconfig"}
           or p.lower().startswith(".env") for p in parts):
        return False
    if path.lower().endswith((".key", ".pem", ".p12", ".pfx")):
        return False
    return path.startswith(("docs/", "src/", "tests/"))


def check_plan(plan: object, *, trusted_allowed_files: frozenset[str]) -> dict[str, Any]:
    problems: list[str] = []
    if not isinstance(plan, dict):
        problems.append("PLAN_NOT_OBJECT")
        plan = {}
    allowed_keys = {"repository", "source_revision", "branch", "worktree_id",
                    "target_files", "test_ids", "rollback", "steps"}
    if set(plan) != allowed_keys:
        problems.append("PLAN_FIELDS_NOT_APPROVED")
    if plan.get("repository") != REPO:
        problems.append("SYNTHETIC_REPOSITORY_ONLY")
    sha = plan.get("source_revision")
    if not isinstance(sha, str) or re.fullmatch(r"[a-f0-9]{40}", sha) is None:
        problems.append("PINNED_40_HEX_SOURCE_REVISION_REQUIRED")
    branch = plan.get("branch")
    if not isinstance(branch, str) or not re.fullmatch(r"d099-aa4-[a-z0-9-]{1,48}", branch):
        problems.append("ISOLATED_BRANCH_REQUIRED")
    worktree = plan.get("worktree_id")
    if not isinstance(worktree, str) or not re.fullmatch(
        r"d099-aa4-synthetic-[a-z0-9-]{1,48}", worktree
    ):
        problems.append("SYNTHETIC_WORKTREE_REQUIRED")
    files = plan.get("target_files")
    if (not isinstance(files, list) or not files or
            any(not _safe_file(path) or path not in trusted_allowed_files
                for path in files) or len(set(map(str, files))) != len(files)):
        problems.append("FILE_SCOPE_DENIED")
    tests = plan.get("test_ids")
    if (not isinstance(tests, list) or not tests
            or any(not isinstance(x, str) or x not in TEST_IDS for x in tests)):
        problems.append("TEST_COMMANDS_NOT_ALLOWLISTED")
    if plan.get("rollback") != "DISCARD_DISPOSABLE_WORKTREE":
        problems.append("ROLLBACK_NOT_BOUNDED")
    if plan.get("steps") != ["prepare", "edit", "test", "review", "rollback"]:
        problems.append("CONTROLLED_SEQUENCE_REQUIRED")
    return {
        "status": "AA4_STATIC_PLAN_REVIEW_ONLY",
        "violations": sorted(set(problems)),
        "plan_structurally_bounded": not problems,
        "human_approval_required": True,
        "build_executed": False,
        "branch_created": False,
        "AA4_CONTROLLED_BUILD_VALIDATED": False,
    }
