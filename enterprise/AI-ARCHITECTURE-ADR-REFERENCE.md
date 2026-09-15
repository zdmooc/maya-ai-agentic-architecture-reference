# AI Architecture ADR Reference Set

Status: **DESIGNED — REFERENCE DECISIONS / ADAPT PER USE CASE**

Purpose: give the AI Solution Architect a reusable decision set. These ADRs are reference decisions, not universal mandates. Each concrete project must restate context, options, constraints and evidence.

## ADR-001 — AI only where deterministic software is insufficient

Decision: prefer deterministic software/search/rules when the requirement can be satisfied predictably without a model.

Rationale: lower risk, cost and operational complexity.

Trigger to revisit: requirement involves language understanding, semantic retrieval, open-ended synthesis or uncertain multi-step reasoning.

## ADR-002 — RAG before fine-tuning for changing enterprise knowledge

Decision: use RAG by default when knowledge freshness, citations, ACLs and deletion are required.

Fine-tuning is considered for stable behavioral/task adaptation, not as the primary mechanism for frequently changing facts.

## ADR-003 — Workflow before autonomous agent

Decision: prefer deterministic orchestration with bounded LLM steps when the process is known.

Agentic planning is justified only when tool/step selection must be dynamic.

## ADR-004 — Deterministic policy remains authoritative

Decision: LLM/agent outputs never override security, entitlement, compliance, transaction or hard-risk policy.

Implication: policy/rule engine decisions are outside the model and fail closed.

## ADR-005 — Human approval for sensitive action

Decision: production remediation, payments, entitlements, destructive configuration and similarly high-impact actions require explicit HITL unless a later approved risk decision proves otherwise.

## ADR-006 — AI Gateway as enterprise control plane

Decision: when several consumers/providers/models exist, centralize identity, policy, budget/rate, PII controls, model aliases, audit and observability through an AI Gateway.

Avoid embedding provider credentials and policies independently in every application.

## ADR-007 — Provider-neutral application contracts

Decision: application code should target business/model capability contracts rather than provider-specific SDK semantics where practical.

Reason: reversibility, multi-cloud placement and controlled provider substitution.

Exceptions must document the value of deliberate coupling.

## ADR-008 — Data classification drives placement

Decision: eligibility of private/cloud model endpoints is determined before routing using classification, residency, authorized-provider and egress policy.

Performance/cost optimization occurs only among eligible endpoints.

## ADR-009 — Evaluation gate before promotion

Decision: prompt/model/index/tool/policy changes require baseline-versus-candidate evaluation against representative regression data before promotion.

Production deployment success alone is not acceptance evidence.

## ADR-010 — RAG retrieval and generation evaluated separately

Decision: measure retrieval relevance/recall and answer grounding/citation/abstention as separate concerns.

Reason: final-answer scoring alone cannot reliably identify retrieval versus generation failure.

## ADR-011 — Structured output for machine-to-machine integration

Decision: when downstream software consumes LLM output, use typed schema/JSON/function contracts plus deterministic validation.

Free-form generated text is treated as untrusted input.

## ADR-012 — Explicit model/prompt/index/tool provenance

Decision: every significant AI response/action carries traceable model alias/version, prompt version, index/corpus version, tool calls, policy result and correlation ID.

## ADR-013 — OpenShift/OpenShift AI for private enterprise AI where justified

Decision: portable/private workloads may target OpenShift/OpenShift AI when enterprise isolation, platform governance, existing operational capability or sovereignty justify it.

This does not prohibit managed cloud AI; placement is policy/use-case driven.

## ADR-014 — Runtime choice is workload-driven

Decision: compare KServe, vLLM, Triton, TGI or managed endpoints against model support, batching/streaming, autoscaling, hardware efficiency, security, observability and operational burden.

No runtime is the default for every model.

## ADR-015 — Estimates are not benchmark evidence

Decision: capacity, GPU, cost, latency and energy calculations remain labelled `ESTIMATE` until measured under representative workload.

## ADR-016 — Cost is an architecture quality attribute

Decision: token, embedding, vector-search, GPU/infrastructure and observability cost are tracked as first-class NFR/FinOps dimensions.

Useful metric examples: cost/request, cost/useful answer, cost/active user, GPU-seconds/workload.

## ADR-017 — GreenOps claims require declared methodology

Decision: carbon/energy values are not presented as measured facts unless backed by measured data and declared methodology.

## ADR-018 — Security trust boundaries outside prompt semantics

Decision: authorization, tenant isolation, secret handling and provider eligibility are enforced by deterministic controls. Prompts may guide model behavior but are not security boundaries.

## ADR-019 — Tool access is least-privilege and server-side authorized

Decision: agent tools expose narrowly scoped, typed operations with independent authorization, timeout/rate controls and audit.

Do not trust the model to self-restrict privileges.

## ADR-020 — Cache is identity/policy/version aware

Decision: AI/RAG caches include relevant identity/tenant, policy, model, prompt and knowledge/index freshness dimensions to prevent stale or cross-entitlement disclosure.

## ADR-021 — Enterprise knowledge is reconstructable

Decision: vector/index stores are derived data. The authoritative governed source and versioned processing pipeline must support deterministic rebuild and deletion lineage.

## ADR-022 — Event-driven AI preserves domain-event guarantees

Decision: AI consumers of MQ/Kafka events follow idempotence, schema/versioning, correlation/causation, replay and DLQ/backout practices. AI does not justify bypassing messaging resilience controls.

## ADR-023 — Explicit abstention is a valid outcome

Decision: AI workflows support `UNKNOWN`, `NO_ANSWER`, `DATA_STALE`, `CONFLICT` or escalation states rather than forcing a confident answer/action.

## ADR-024 — Responsible AI is use-case specific

Decision: every material AI use case records purpose, owner, affected users, data classes, risk, human oversight, limitations, monitoring and retirement/accountability responsibilities.

## ADR-025 — POCs are uncertainty reducers, not mandatory phases

Decision: build a POC only when a material architecture uncertainty requires evidence—for example model quality, retrieval effectiveness, integration feasibility, performance, capacity, security or operational behavior.

A POC that proves nothing needed for a decision is not justified.

## ADR template for project-specific use

Each concrete ADR should contain:

1. Title and status.
2. Context/problem.
3. Business and technical drivers.
4. Constraints/NFRs.
5. Options considered.
6. Decision.
7. Rationale/trade-offs.
8. Security/data/compliance impact.
9. Cost/operations impact.
10. Consequences and technical debt.
11. Evidence/POC required, if any.
12. Revisit/exit triggers.
