# ADR-D099-AA0 — Method before engine

Status: **PROPOSED / review needed** — 2026-10-08.

Context: the architecture hub already owns FR/NFR catalogs, SAD, ADR and autonomy/HITL references; TradeOps has LangGraph and native MCP but not the mission-to-ADR pipeline. D-099 ACCEPTED prohibits a new generic platform.

Decision proposed: versioned schemas/stages/prompts/role-policy design/golden evaluation references in this hub, reuse TradeOps for later execution and external deterministic enforcement, reuse Shared Platform for OIDC, OTel, Argo CD and Operator. Human approvals for ADR, write, deployment and merge remain independent. AA2 permission JSON is **not** tool enforcement.

Alternatives: S1 prose-only (insufficient machine checks), S2 schema-driven method over existing runtime (proposed), S3 new monolithic agent repo (duplicates ownership).

Risks and limits: no AA1 OpenCode/Ollama measurement, no AA2 runtime permission tests, no AA3 model benchmark, no AA8 CRC execution. D-093 OP1–OP4 open PRs are not merged; exact OLM on OpenShift not inferred. R5 CRC evidence is independently documented in TradeOps; 2026-10-04 hub R5 pending text is stale and needs factual follow-up.

Rollback: leave PR unmerged or revert the bounded merge after approval. No runtime mutation.
