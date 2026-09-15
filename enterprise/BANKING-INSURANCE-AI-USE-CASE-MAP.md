# Banking & Insurance AI Use-Case Architecture Map

Status: **DESIGNED — DOMAIN ARCHITECTURE REFERENCE**

Purpose: map common banking/insurance business capabilities to the most appropriate AI pattern family, controls and integration concerns. This is not a model-recommendation list; pattern choice remains use-case specific.

## 1. Payments / transaction operations

### Payment investigation / exception handling
Pattern:
- event-driven AI + RAG + read-only tools + HITL.

Inputs:
- ISO 20022/payment events;
- MQ/Kafka history;
- payment status;
- runbooks/incident knowledge.

Controls:
- no autonomous replay/remediation by default;
- correlation/causation IDs;
- evidence citations;
- deterministic status/risk checks;
- human approval for action.

### Payment-failure / settlement-failure prediction
Pattern:
- classic ML classification/ranking;
- optional GenAI explanation layer.

Controls:
- calibrated outcome definition;
- feature/data lineage;
- drift monitoring;
- no LLM replacement for numeric prediction.

## 2. Fraud and anomaly detection

Pattern:
- classic ML/anomaly detection + deterministic rules;
- GenAI for analyst investigation/summarization.

Why:
- high-volume numeric/event scoring favors ML/rules;
- analyst workflow can benefit from RAG/LLM synthesis.

Controls:
- false-positive/false-negative cost;
- model drift;
- explainability where required;
- case/audit trail;
- human escalation.

## 3. AML / financial crime

Pattern:
- deterministic rules + graph/ML scoring + GenAI investigation assistant.

GenAI role:
- case summarization;
- evidence aggregation;
- policy/runbook retrieval;
- draft SAR/case narrative where legally appropriate and human-reviewed.

Controls:
- no autonomous final compliance decision;
- source provenance;
- strict PII/security;
- immutable case evidence;
- human compliance ownership.

## 4. Trade surveillance

Pattern:
- event/rule/ML detection + GenAI investigation support.

Controls:
- market/event chronology;
- explainability/evidence;
- no model-only enforcement action;
- retention and audit.

## 5. Credit risk / lending

Pattern:
- deterministic eligibility + classic ML/risk score where approved;
- GenAI for document processing, customer/analyst assistance and explanation support.

Controls:
- regulated decision governance;
- fairness/explainability;
- model validation;
- prohibited-variable review;
- human/accountable decision boundary;
- no free-form LLM as credit policy engine.

## 6. Customer service / banking copilot

Pattern:
- enterprise RAG + workflow + selected tools.

Use cases:
- product/policy Q&A;
- account/process guidance;
- support agent assistant;
- document summarization.

Controls:
- customer/employee entitlement;
- citations;
- no-answer behavior;
- PII masking;
- tool read/write separation;
- HITL for financial action.

## 7. Wealth management / advisory support

Pattern:
- deterministic suitability/policy + analytics/ML + RAG/LLM assistant.

GenAI role:
- research synthesis;
- document navigation;
- advisor drafting/explanation.

Controls:
- suitability rules remain authoritative;
- source/date provenance;
- market-data freshness;
- explicit advisory/human-review boundary;
- regulated-record retention where applicable.

## 8. Capital markets research / sales support

Pattern:
- search/RAG + summarization + quantitative engines/ML where relevant.

Controls:
- licensed source usage;
- source timestamps;
- no invented prices/fundamentals;
- separation of quantitative calculation and LLM narrative.

## 9. Insurance underwriting

Pattern:
- deterministic underwriting rules + classic ML risk models + document/GenAI assistance.

GenAI role:
- document extraction;
- case summarization;
- guideline retrieval;
- draft rationale.

Controls:
- fairness/explainability;
- human underwriter accountability where required;
- document provenance;
- sensitive-data policy;
- model validation.

## 10. Insurance claims

Pattern:
- OCR/IDP + ML fraud/anomaly + workflow + GenAI document/case assistant.

Controls:
- page/region citations;
- extraction confidence;
- low-confidence human validation;
- fraud score separate from LLM narrative;
- audit trail;
- no fabricated missing facts.

## 11. Document and contract analysis

Pattern:
- multimodal/IDP + RAG + controlled document workflow.

Use cases:
- policy/contracts;
- KYC documents;
- architecture/operations documents;
- claims/support records.

Controls:
- document-level ACL;
- retention/deletion;
- citations;
- OCR confidence;
- human validation for legally material output.

## 12. IT/operations copilot

Pattern:
- RAG runbooks + events/metrics + read-only diagnostic tools + HITL remediation.

Good targets:
- OpenShift/MQ/Java/WebSphere/Oracle incident investigation;
- impact analysis;
- ticket/runbook drafting.

Controls:
- least-privilege tools;
- no autonomous destructive production action;
- deterministic health/status evidence;
- traceability.

## 13. Architecture / engineering copilot

Pattern:
- governed enterprise RAG + code/document search + architecture patterns.

Use cases:
- standards Q&A;
- ADR/SAD navigation;
- impact/dependency analysis;
- design-review assistance.

Controls:
- source/version visibility;
- no fabricated enterprise standards;
- document ACL;
- Design Authority remains human/accountable.

## 14. Pattern decision matrix

| Use-case type | Primary pattern | LLM role | Hard control |
|---|---|---|---|
| Numeric risk/prediction | Classic ML | optional explanation | calibrated model + policy |
| Hard eligibility/authorization | deterministic | none/advisory | rules/IAM |
| Knowledge Q&A | RAG | synthesis | ACL + citations |
| Complex investigation | RAG + agent/tools | planning/synthesis | tool auth + HITL |
| Payment/ops event response | event-driven AI | investigation | idempotence + risk gate |
| Document processing | IDP/multimodal + workflow | extraction/synthesis | confidence + validation |
| Regulated decision | rules/ML + HITL | advisory | accountable human/policy |

## 15. Architect interview rule

A credible banking AI architecture answer should always identify:

1. system of record;
2. business decision/action;
3. deterministic vs ML vs GenAI boundary;
4. data source/classification;
5. integration path (API/MQ/Kafka/document/RAG);
6. human oversight;
7. evaluation metric;
8. audit/explainability requirement;
9. production/SRE concerns;
10. residual risk owner.
