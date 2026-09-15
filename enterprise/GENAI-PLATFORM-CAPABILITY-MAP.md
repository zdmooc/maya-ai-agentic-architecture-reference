# GenAI Platform Capability Map

Status: **DESIGNED — ENTERPRISE AI PLATFORM REFERENCE**

Purpose: define reusable platform capabilities that should be shared across enterprise GenAI products when scale justifies productizing common infrastructure.

## 1. Access and policy plane

Capabilities:
- AI Gateway;
- authentication/authorization;
- tenant/application identity;
- quotas/rate/token budgets;
- PII/secrets controls;
- provider/model allowlists;
- audit and policy decisions;
- API lifecycle/versioning.

## 2. Model access and routing

Capabilities:
- model aliases;
- provider abstraction;
- private/cloud endpoint registry;
- model router;
- data-classification/residency eligibility;
- fallback policy;
- latency/cost/quality-aware routing;
- model metadata/version/provenance.

## 3. Prompt and context management

Capabilities:
- prompt registry;
- version/promotion/rollback;
- templates/variables;
- system/user/context boundary rules;
- test/evaluation linkage;
- context budgets;
- prompt policy/security checks.

## 4. Knowledge / RAG platform

Capabilities:
- source connectors;
- raw/quarantine/curated/index zones;
- document metadata contract;
- ACL/classification filtering;
- chunking/embedding;
- lexical/vector/hybrid retrieval;
- reranking;
- citation/provenance;
- index/version lifecycle;
- freshness/expiry/deletion;
- backup/rebuild/DR.

## 5. Agent and tool platform

Capabilities:
- agent/orchestrator runtime;
- tool registry;
- typed contracts;
- governed MCP/tool adapters;
- server-side authorization;
- execution sandbox;
- budgets/max steps/timeouts;
- human approval workflow;
- state/memory controls;
- audit/traceability.

## 6. Session and state services

Capabilities:
- short-lived conversation/session state;
- durable workflow state where required;
- memory lifecycle/TTL;
- tenant isolation;
- privacy/deletion policy;
- state recovery;
- separation of ephemeral context from governed long-term memory.

## 7. Evaluation and quality services

Capabilities:
- golden/regression datasets;
- baseline/candidate comparison;
- exact/functional metrics;
- retrieval evaluation;
- grounding/citation/abstention evaluation;
- LLM-as-judge with controlled rubric/version;
- agent/tool evaluation;
- security negative tests;
- CI promotion gates;
- experiment tracking.

## 8. Feedback and HITL services

Capabilities:
- explicit feedback;
- structured corrections;
- incident/user feedback ingestion;
- triage/annotation;
- HITL approval/rejection/expiry;
- maker-checker patterns where applicable;
- feedback-to-regression workflow;
- no automatic production mutation from raw feedback.

## 9. Model serving and training/adaptation

Serving:
- managed cloud endpoints;
- private KServe/vLLM/Triton/TGI as selected by ADR;
- autoscaling;
- batching/streaming;
- GPU/CPU scheduling;
- model registry;
- canary/rollback.

Adaptation/training:
- dataset governance;
- SFT/PEFT/LoRA/QLoRA workload path;
- experiment/evaluation;
- model lineage;
- training isolation and quotas.

## 10. Observability and SRE

Capabilities:
- distributed trace/correlation;
- model/RAG/tool/policy spans;
- logs/metrics/traces;
- latency/TTFT/tokens/s;
- queue/capacity/GPU metrics;
- quality/eval signals;
- SLI/SLO/error budget;
- alerting;
- incident/runbook;
- graceful degradation/fallback evidence.

## 11. Security, Responsible AI and compliance

Capabilities:
- use-case registry;
- risk classification;
- AI-BOM/provenance;
- privacy/DPIA hooks;
- content moderation/guardrails;
- threat model/red teaming;
- interaction archival/retention;
- policy-as-code;
- secrets/certificates;
- audit access controls;
- model/data/license governance.

## 12. FinOps / GreenOps

Capabilities:
- provider/token cost;
- embedding/vector cost;
- GPU seconds/infrastructure allocation;
- cost/request/useful-answer/user;
- budget/quota/forecast;
- cache efficiency;
- showback/chargeback;
- energy/carbon estimates with declared methodology;
- workload right-sizing/routing.

## 13. Developer / product self-service

Capabilities:
- approved templates/reference architectures;
- SDK/API examples;
- sandbox environments;
- onboarding documentation;
- golden paths;
- policy-compliant starter projects;
- architecture review checklist;
- standard dashboards/eval suites.

## 14. Platform vs application responsibility

Platform should own reusable cross-cutting capabilities. Application/product teams should own:
- business use case;
- domain-specific prompts/workflows;
- business acceptance criteria;
- domain knowledge sources and owners;
- application-specific FR/NFR;
- business feedback and value KPIs.

Do not force every capability into a centralized platform. Centralize where reuse, policy, operations or economics justify it.

## 15. OpenShift / hybrid mapping

Typical private enterprise mapping:
- OpenShift/ARO: portable runtime and platform services;
- OpenShift AI: workbench/training/serving lifecycle where useful;
- KServe/vLLM: selected private serving patterns;
- Argo CD/GitOps: declarative promotion;
- Kafka/MQ: event integration;
- object storage: models/datasets/documents;
- PostgreSQL/vector store: metadata/state/knowledge as designed;
- OTel/Prometheus/Grafana: observability;
- cloud AI providers: eligible managed foundation-model endpoints behind gateway/router.

## 16. Platformization trigger

Do not build a full AI platform for one small POC. Platformization becomes justified when several use cases repeatedly need the same controls, model access, knowledge, tool, evaluation, SRE or governance capabilities.
