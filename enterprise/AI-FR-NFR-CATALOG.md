# AI Functional / Non-Functional Requirements Catalog

Status: **REFERENCE CATALOG / DESIGN AUTHORITY**

Purpose: provide reusable requirement categories for AI Solution Architecture. This is a design reference, not implementation evidence.

## Functional requirement families

### FR-01 — AI interaction

- ask a question / submit a task;
- receive an answer/result;
- receive source/citation/evidence where required;
- receive uncertainty/abstention status;
- submit feedback/correction.

### FR-02 — Knowledge / RAG

- ingest approved content;
- validate and classify content;
- index authorized content;
- enforce document/chunk ACLs;
- retrieve/rerank relevant evidence;
- cite exact sources;
- support deletion lineage and index rebuild.

### FR-03 — Agent / tools

- select approved tools;
- invoke typed tool contracts;
- respect identity/scope/policy;
- expose reasoning outcome/evidence without relying on hidden chain-of-thought;
- stop on veto, uncertainty or unavailable critical evidence;
- request human approval for sensitive actions.

### FR-04 — Model/provider

- route to an eligible model;
- apply provider/data-placement policy;
- support fallback where approved;
- expose model alias/version in telemetry;
- support structured output where required.

### FR-05 — Evaluation / feedback

- evaluate baseline and candidate;
- run golden/regression datasets;
- collect explicit/implicit feedback where lawful;
- triage issues;
- block promotion when quality/security thresholds fail.

### FR-06 — Operations

- expose health/readiness/metrics;
- trace requests end to end;
- record auditable policy/tool decisions;
- support rollback/recovery;
- support incident diagnosis.

## Non-functional requirement families

### NFR-01 — Availability

Define target availability per capability and dependency. Example:

- user-facing AI API availability target;
- deterministic business service availability target;
- RAG/index availability target;
- provider dependency assumptions.

Architecture rule: failure of an optional AI capability must not unnecessarily take down authoritative deterministic services.

### NFR-02 — Latency

Specify:

- end-to-end p50/p95/p99;
- TTFT target for streamed responses;
- maximum retrieval/reranking latency;
- maximum tool-call latency;
- timeout budgets.

### NFR-03 — Throughput and concurrency

Specify:

- requests/sec;
- concurrent sessions;
- tokens/sec where relevant;
- queue depth/backlog thresholds;
- burst expectations.

### NFR-04 — Scalability

Define:

- horizontal/vertical scaling model;
- CPU/GPU scaling;
- autoscaling limits;
- stateful bottlenecks;
- provider quota limits.

### NFR-05 — Resilience

Require:

- retries with bounded policy;
- circuit breakers;
- bulkheads/isolation;
- fallback/degraded mode;
- stale-data handling;
- replay/idempotency where events are used;
- dependency failure behavior.

### NFR-06 — Recoverability / DR

Specify:

- RTO/RPO;
- backup/rebuild strategy;
- vector index reconstruction;
- model artifact recovery;
- configuration/prompt/policy recovery;
- tested restore evidence.

### NFR-07 — Security

Cover:

- AuthN/AuthZ;
- least privilege;
- tenant isolation;
- secrets/certificates;
- tool authorization;
- prompt injection/jailbreak controls;
- supply-chain controls;
- network segmentation;
- output validation.

### NFR-08 — Privacy / residency

Specify:

- data classes;
- PII handling;
- retention;
- residency;
- authorized providers/regions;
- deletion obligations;
- logging/redaction rules.

### NFR-09 — Quality / grounding

Define measurable criteria such as:

- task correctness;
- grounding/faithfulness;
- citation correctness;
- retrieval recall/relevance;
- structured-output validity;
- abstention correctness;
- domain-specific acceptance thresholds.

### NFR-10 — Safety

Require:

- deterministic hard controls for critical rules;
- forbidden actions;
- human approval boundaries;
- safe failure/abstention;
- red-team regression scenarios;
- no autonomous bypass of policy.

### NFR-11 — Explainability / traceability

Require traceability of:

`request -> identity -> policy -> retrieval -> model -> tool -> decision -> evidence -> outcome`.

Do not require exposure of private hidden chain-of-thought.

### NFR-12 — Auditability

Audit:

- model/provider/version;
- prompt/template version;
- index/corpus version;
- policy decision;
- tool invocation;
- human approval;
- deployment/config version.

### NFR-13 — Observability

Require:

- metrics;
- traces;
- logs;
- model/RAG/tool telemetry;
- SLO/SLI dashboards;
- alerting;
- correlation IDs.

### NFR-14 — Operability / supportability

Specify:

- ownership;
- support hours;
- runbooks;
- escalation;
- maintenance windows;
- incident classes;
- dependency/provider support model.

### NFR-15 — Maintainability

Require:

- modular service boundaries;
- testability;
- versioned prompts/policies/contracts;
- automated validation;
- controlled technical debt;
- documented deprecation path.

### NFR-16 — Portability / reversibility

Define:

- provider abstraction;
- model aliases;
- exportable datasets/index sources;
- infrastructure portability;
- exit strategy;
- coupling explicitly justified by ADR.

### NFR-17 — Cost / FinOps

Specify:

- monthly budget;
- cost/request;
- cost/useful answer;
- token budgets;
- GPU/infrastructure budgets;
- cache targets;
- anomaly thresholds;
- showback/chargeback if required.

### NFR-18 — Sustainability / GreenOps

Where measurable:

- resource utilization;
- idle capacity;
- accelerator efficiency;
- energy/carbon indicators;
- workload placement considerations.

Do not label estimates as measurements.

### NFR-19 — Compliance / governance

Require where applicable:

- use-case registration;
- privacy assessment;
- model/data/prompt ownership;
- AI-BOM;
- licensing/provenance;
- risk classification;
- review/approval lifecycle.

### NFR-20 — Accessibility / usability

Specify:

- accessible UI expectations;
- understandable uncertainty/citation presentation;
- response format;
- user confirmation for sensitive actions;
- failure/error clarity.

## Requirement quality rule

Every important NFR should be testable or reviewable. Avoid statements such as `the system must be fast`, `secure`, or `highly available` without target, context and verification method.

Recommended structure:

`ID | requirement | target | measurement method | owner | evidence status | priority`.

## AI architecture rule

The model is only one component. NFRs apply to the complete system, including identity, gateway, retrieval, model, tools, deterministic controls, storage, platform and operations.