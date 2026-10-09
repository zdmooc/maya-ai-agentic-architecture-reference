# D-099 AA4 I6 — preparatory dry-run build plan, not execution

Scope: **fictional `lab/notification-api` only**. This is not a GitHub
repository, worktree creation, CI job runner or command executor.

`build/plan_guard.py` validates a proposed file-scoped plan for an
isolated worktree, an exact 40-hex revision, bounded test IDs and a
non-destructive rollback description. All extra keys including
`human_approved` are rejected: **approval does not originate from an
LLM plan**. Even a passing plan prints `AA4_STATIC_PLAN_REVIEW_ONLY`
and `AA4_CONTROLLED_BUILD_VALIDATED=false` — never authorizes a
build. No filesystem mutations, Git calls or cluster access are in
this module.

Before AA4 implementation: finish AA3 scored acceptance, bind a real
worktree to an approved SHA, authenticate the independent human
reviewer via the existing TradeOps gate, use durable single-use
approval outside the model, run exact reviewed tests in a separate
sandbox, record a diff, safety/CI checks, independent review,
postconditions and rollback. Do not open production or CRC access.
