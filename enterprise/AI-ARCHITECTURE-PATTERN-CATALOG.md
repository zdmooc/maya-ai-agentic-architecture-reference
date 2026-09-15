# AI Solution Architecture Pattern Catalog

Status: **DESIGNED — ARCHITECTURE REFERENCE / IMPLEMENTATION EVIDENCE SEPARATE**

Purpose: provide a reusable catalog for AI Solution Architects to select the simplest pattern that satisfies business, security, data, operational and cost requirements.

Decision rule:

`deterministic software -> prompt-only -> RAG -> deterministic workflow + LLM -> agentic workflow -> fine-tuning`

Move to the right only when the simpler option cannot meet the requirement.

## Pattern 1 — Deterministic software first

Use when:
- business rules are explicit and stable;
- exact reproducibility is required;
- arithmetic, eligibility, authorization or transaction controls are involved.

Avoid replacing deterministic rules with an LLM merely for novelty.

Typical controls: schema validation, rule engine, API contracts, audit logs, tests.

## Pattern 2 — Prompt-only AI capability

Use when:
- task is transformation, summarization, classification or drafting;
- all required context fits safely in the request;
- no private knowledge retrieval is needed.

Risks: hallucination, prompt sensitivity, stale model knowledge, prompt injection.

Required architecture controls: prompt version, model alias, output schema, guardrails, eval dataset, trace/correlation ID.

## Pattern 3 — Enterprise RAG

Use when:
- answers must rely on private or changing knowledge;
- citations and source traceability matter;
- access control must be applied at document/chunk level.

Canonical flow:

`identity -> policy/ACL -> query normalization -> lexical/vector/hybrid retrieval -> rerank -> context construction -> LLM -> citation validation -> answer/abstain`

Required controls: corpus lifecycle, ACL filtering before context, provenance, index version, deletion lineage, no-answer behavior, retrieval and generation evaluation separately.

## Pattern 4 — Deterministic workflow with bounded LLM steps

Use when:
- process steps are known;
- only selected steps require interpretation or generation;
- business control must remain predictable.

Example:

`validate input -> retrieve evidence -> LLM classify/summarize -> deterministic policy -> human approval -> downstream action`

This is preferred over an autonomous agent when orchestration can be predefined.

## Pattern 5 — Governed agentic workflow

Use when:
- task requires dynamic planning or tool selection;
- number/order of steps cannot be fully predetermined;
- multi-source investigation is required.

Required controls:
- typed tool contracts;
- least privilege;
- server-side authorization;
- max steps/time/token/cost budget;
- stop conditions;
- deterministic veto controls;
- human approval for sensitive actions;
- traceable state and evidence;
- failure/loop/tool-abuse tests.

Never grant an agent unrestricted production access by default.

## Pattern 6 — Multi-agent specialization

Use when specialized roles materially improve separation of concerns or independent evidence production.

Examples: retrieval agent, technical analyst, policy/risk agent, operations agent, synthesis agent.

Avoid multi-agent architecture when one orchestrator plus deterministic services is sufficient; extra agents increase latency, cost, state complexity and failure surface.

## Pattern 7 — AI Gateway + Model Router

Use when multiple applications/models/providers must be governed centrally.

Gateway responsibilities:
- identity and authorization;
- tenant/application quotas;
- PII/secrets inspection;
- policy enforcement;
- token/budget/rate control;
- audit/telemetry;
- cache policy;
- provider/model allowlist.

Router dimensions:
- data classification/residency;
- capability/quality;
- latency/SLA;
- cost;
- availability;
- context length;
- tool/structured-output support;
- reversibility/provider constraints.

## Pattern 8 — Private/self-hosted model serving

Use when sovereignty, latency, predictable throughput, offline operation or data restrictions justify operational complexity.

Typical platform: OpenShift AI/RHOAI + KServe/vLLM/Triton/TGI according to ADR.

Required architecture: capacity model, GPU/CPU pools, quotas, autoscaling, model registry, observability, rollback, vulnerability/model provenance, SRE runbooks.

## Pattern 9 — Managed cloud model API

Use when leading model capability and low infrastructure burden outweigh provider coupling and external-processing constraints.

Controls: approved region/provider, private networking where supported, data-retention policy, key/secrets lifecycle, quotas, cost controls, fallback and exit strategy.

## Pattern 10 — Hybrid / multi-cloud model placement

Use when data classes, regional constraints, model capability and resilience require several eligible execution locations.

Policy engine chooses from private/OpenShift and approved cloud endpoints. Application uses provider-neutral contracts/model aliases.

Required: explicit placement policy, compliant fallback rules, portable prompts/evals, observability export and exit ADR.

## Pattern 11 — Event-driven AI

Use when AI reacts to business/domain events rather than synchronous user prompts.

Typical flow:

`MQ/Kafka event -> canonical event -> evidence/state -> AI investigation/enrichment -> deterministic policy -> HITL -> action/ticket/recommendation`

Required: idempotence, correlation/causation IDs, replay, DLQ/backout, event schema/versioning, no blind production replay.

## Pattern 12 — Human-in-the-Loop decision

Use for regulated, financial, entitlement, production-remediation or high-impact actions.

State model example:

`PENDING_REVIEW -> APPROVED | REJECTED | EXPIRED`

Evidence, actor identity, timestamp, model/prompt/index/tool versions and decision rationale must be auditable.

## Pattern 13 — Fine-tuned / adapted model

Use only when stable behavior/task adaptation cannot be achieved economically and reliably with prompting/RAG/workflow.

Required: base model/version, dataset provenance, training config, baseline/candidate evaluation, safety regression, model registry, rollback, serving capacity and licensing review.

## Pattern 14 — Multimodal / IDP pipeline

Use for documents containing text, images, tables or scanned material.

Flow:

`document -> OCR/layout/table extraction -> quality checks -> structured content -> index/knowledge -> page/region citation -> human validation for low confidence`

Do not treat OCR output as authoritative without quality controls.

## Pattern 15 — Feedback-driven controlled improvement

Use when production feedback should improve the system.

Flow:

`feedback -> triage -> root-cause classification -> prompt/data/model/policy change -> regression dataset -> evaluation -> controlled promotion`

Feedback must not directly mutate production prompts/models or trigger automatic retraining without governance.

## Architecture selection scorecard

For every use case, score at minimum:
- business criticality;
- deterministic feasibility;
- knowledge freshness;
- need for citations;
- action autonomy;
- data classification/residency;
- latency/SLA;
- availability/resilience;
- quality/evaluation difficulty;
- cost/volume;
- provider portability;
- audit/regulatory requirements.

The selected pattern and rejected alternatives must be recorded in an ADR.
