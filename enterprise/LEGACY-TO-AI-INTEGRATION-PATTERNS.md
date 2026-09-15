# Legacy-to-AI Integration Patterns

Status: **DESIGNED — REFERENCE PATTERNS / POC DEMAND-DRIVEN**

Purpose: integrate AI capabilities with existing banking/insurance/enterprise systems without forcing unnecessary core replacement.

Modernization decision ladder:

`encapsulate -> API enable -> event enable -> replatform -> refactor -> rearchitect -> replace`

The AI use case does not automatically justify moving to the right.

## Principle 1 — Preserve the system of record

Core payment, policy, customer, accounting, entitlement and risk systems remain authoritative unless a separately approved modernization program changes that responsibility.

AI consumes governed data/evidence or proposes actions; it does not silently become the system of record.

## Pattern A — Read-only API facade

Use when an agent/copilot needs live state from a legacy application.

`AI workflow -> API Gateway -> domain facade -> legacy service/database interface`

Controls:
- explicit read-only contract;
- authorization outside the model;
- response schema validation;
- timeouts/circuit breaker;
- rate limits;
- sensitive-field minimization;
- audit/correlation ID.

Typical use: account/payment status inquiry, configuration lookup, incident investigation.

## Pattern B — Governed command facade with HITL

Use when AI may propose but not autonomously execute a sensitive legacy action.

`AI recommendation -> deterministic validation -> human approval -> command API -> legacy system`

Controls:
- typed command;
- business/risk rules;
- maker/checker where applicable;
- idempotency key;
- approval identity/time;
- before/after state evidence;
- rollback/compensation path.

## Pattern C — MQ integration

Use for established enterprise messaging environments, especially when legacy/core applications already expose durable queues.

`legacy producer -> IBM MQ -> canonical adapter -> AI investigation/enrichment -> controlled downstream workflow`

Retain:
- persistent delivery semantics where required;
- backout/DLQ;
- correlation IDs;
- replay policy;
- idempotent consumer;
- schema/version governance.

AI must not bypass MQ resilience by replacing it with direct calls merely for convenience.

## Pattern D — Kafka/event-stream integration

Use when AI benefits from replayable domain events, real-time enrichment or multi-consumer analytics.

`domain event -> Kafka -> canonical event/data quality -> AI/ML consumer -> evidence/decision -> event or workflow`

Controls: schema registry, event ownership, partition/order assumptions, replay/idempotence, PII policy, retention, observability.

## Pattern E — Outbox/CDC bridge

Use when a legacy application cannot directly publish reliable business events.

Options:
- transactional outbox;
- CDC from approved operational tables;
- scheduled/batch export for lower criticality.

Do not infer business semantics from raw DB changes without explicit mapping/ownership.

## Pattern F — RAG over legacy documentation

Use when the immediate value is operational knowledge rather than runtime integration.

Sources: runbooks, architecture docs, incident procedures, standards, interface specs, controlled knowledge bases.

This is often lower risk and faster than exposing production tools to an agent.

Required: source ownership, ACL, version/freshness, citations, abstention and deletion lifecycle.

## Pattern G — AI sidecar / advisory service

Use when a legacy application cannot be changed deeply.

The AI capability runs beside the application and provides recommendations, classifications or summaries through an approved interface.

Legacy flow remains functional if AI is unavailable.

This pattern supports graceful adoption and rollback.

## Pattern H — Strangler modernization around AI-enabled capability

Use when a business capability is already scheduled for modernization.

Introduce a new bounded-context service/API/event layer, gradually migrate consumers, and isolate legacy dependencies behind adapters.

AI integration then targets the new capability boundary rather than the legacy implementation.

Avoid using AI as the sole justification for a large rewrite.

## Pattern I — Batch/offline AI enrichment

Use when real-time response is unnecessary.

Examples: document classification, case prioritization, anomaly triage, knowledge indexing, reporting enrichment.

Advantages: lower operational coupling, easier governance, predictable cost/capacity.

## Pattern J — Event-driven incident copilot

Use for payments/operations:

`MQ/Kafka incident/payment events -> status/metrics/history -> RAG runbooks -> read-only diagnostic tools -> evidence-backed hypothesis -> deterministic policy -> HITL -> ITSM/remediation draft`

No blind replay, restart or production remediation by the LLM.

## Integration architecture selection criteria

For every legacy integration assess:
- business criticality;
- system-of-record ownership;
- read vs write requirement;
- transactionality;
- consistency/timing needs;
- existing API/MQ/Kafka capability;
- data classification;
- authorization model;
- throughput/latency;
- replay/idempotence;
- failure isolation;
- observability;
- modernization roadmap;
- support-team skills;
- cost and delivery risk.

## Anti-patterns

- Direct LLM access to production databases.
- Giving agents generic shell/SQL/admin tools.
- Replacing deterministic core rules with prompts.
- Bypassing established MQ/Kafka/API governance.
- Coupling AI directly to vendor-specific legacy internals when a domain facade is feasible.
- Treating raw CDC records as canonical business events without domain mapping.
- Forcing synchronous AI into a latency-critical transaction path when asynchronous/advisory processing meets the use case.
- Making the core business transaction unavailable when the AI service is down unless AI is explicitly business-critical and engineered to that SLO.

## Banking/payment transposition

This repository should preferentially reuse:
- IBM MQ/OpenShift reference for durable payment messaging;
- Kafka/DDD/OpenShift reference for event-driven domain architecture;
- API Management reference for governed synchronous integration;
- Wero/ISO 20022/payment references for business-message semantics;
- OpenShift/AI platform patterns for AI runtime placement.

POCs remain demand-driven. The architecture pattern can be `DESIGNED` without claiming that a specific legacy system has been integrated or tested.
