# D-099 security boundary — design, NOT deployed enforcement

- Only the trusted IAM/gateway determines identity, tenant, tool scope, repository and file allowlists, and namespace. Never accept tool permissions from generated text.
- Every tool call: JSON Schema validation **and** deterministic semantic authorization; valid JSON can still be DENY. Default DENY; audit refusals.
- HITL is an authenticated server-side approval bound to identity, exact operation, canonical parameter hash, targeted repo/namespace, expiration and single-use nonce. Stale/replayed/synthetic approvals are DENIED. A PR is not authorization to deploy.
- GitHub README, issue, RAG snippets, MCP tool descriptions and external material are lower-trust DATA and cannot override policies. Guard against indirect injection and poisoned retrieval.
- Deny agent `git push`, broad deletes, shell escalation, `oc apply/delete`, `kubectl apply/delete`, `argocd app sync`, unrestricted exec, cross-tenant access or attempts to publish sensitive logs by default.
- A builder only edits allowlisted files in an isolated branch/worktree, never `main`; separate reviewer examines diff/tests. Runtime mutation requires a separate human gate, preflight, bounded scope, rollback and evidence.
- No secrets, kubeconfig, personal tokens, raw sensitive logs, Docker host socket or unrestricted network. Enforce CPU/RAM/time/tool/token/cost budgets outside the model.
- Tests still required on real runtime: permit-scoped read, deny out-of-scope read, stale approval, replay, cross-tenant, hostile README, malicious MCP description, fake evidence and valid JSON with forbidden operation.
