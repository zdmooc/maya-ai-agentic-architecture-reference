# AI Architect Knowledge Base Index

Status: **DESIGNED — NAVIGATION INDEX**

Purpose: provide one entry point into the architecture knowledge base. Use this file before creating new theory documents or POCs.

## 1. Core AI engineering fundamentals

- `AI-ENGINEERING-FUNDAMENTALS.md` — foundation models, evaluation, prompting, RAG/agents, fine-tuning, datasets, inference, feedback.
- `AI-ENGINEERING-BOOK-ALIGNMENT.md` — chapter-by-chapter alignment with Chip Huyen's *AI Engineering*.
- `AI-ML-SOLUTION-ARCHITECTURE-LIFECYCLE.md` — unified deterministic / classic ML / GenAI lifecycle.

## 2. Enterprise AI target architecture

- `ENTERPRISE-AI-THEORETICAL-DESIGN-I13-I20.md` — enterprise RAG, evaluation/FinOps, Design Authority, AI Gateway/security, AI Factory, hybrid placement, payments AI, multimodal/document automation.
- `GENAI-PLATFORM-CAPABILITY-MAP.md` — reusable enterprise GenAI platform capabilities.
- `GENAI-PRODUCTION-MATURITY-MODEL.md` — Idea -> Prototype -> Controlled POC -> Pre-Production -> Managed Production -> Platformized.

## 3. Solution Architecture deliverable pack

- `AI-SOLUTION-ARCHITECTURE-DOCUMENT-TEMPLATE.md` — canonical SAD.
- `AI-FR-NFR-CATALOG.md` — functional/non-functional requirement catalog.
- `AI-ARCHITECTURE-CONSTRAINTS-REGISTER.md` — regulatory/data/platform/legacy/budget/SLA constraints.
- `AI-PERFORMANCE-BUDGET-TEMPLATE.md` — end-to-end latency/throughput/capacity budget.
- `AI-ARCHITECTURE-REVIEW-CHECKLIST.md` — Design Authority review.
- `AI-ARCHITECTURE-RACI.md` — responsibilities across business, architecture, data, security, platform, operations and risk.
- `AI-ARCHITECTURE-RISK-REGISTER.md` — reusable AI risk baseline.

## 4. Patterns and decisions

- `AI-ARCHITECTURE-PATTERN-CATALOG.md` — deterministic, prompt-only, RAG, workflow, agent, multi-agent, gateway/router, private/cloud/hybrid, event-driven, HITL, fine-tuning, multimodal, feedback.
- `AI-ARCHITECTURE-ADR-REFERENCE.md` — reference ADR set.
- `LEGACY-TO-AI-INTEGRATION-PATTERNS.md` — API/MQ/Kafka/CDC/RAG/sidecar/strangler/batch/event-driven/HITL integration.
- `AI-DATA-SYSTEMS-ARCHITECTURE-PRINCIPLES.md` — system of record, derived state, consistency, replay, idempotence, batch/stream, schema evolution.
- `AI-ARCHITECTURE-FITNESS-FUNCTIONS.md` — continuous architectural governance.

## 5. Well-Architected / governance / compliance

- `GENAI-WELL-ARCHITECTED-SCORECARD.md` — ten-pillar GenAI architecture assessment.
- `AI-INTERACTION-ARCHIVAL-COMPLIANCE-PATTERN.md` — audit evidence, retention, legal hold, deletion and privacy minimization.
- `ENTERPRISE-GENAI-WELL-ARCHITECTED-ALIGNMENT.md` — book alignment and vendor-neutral interpretation.

## 6. Production, LLMOps and SRE

- `ARCHITECTING-GENAI-APPLICATIONS-ALIGNMENT.md` — production architecture alignment.
- `GENAI-SRE-SLO-ERROR-BUDGET.md` — SLIs/SLOs/error-budget model.
- `GENAI-ONLINE-EXPERIMENTATION-PATTERN.md` — A/B/controlled online experimentation.
- `ML-PRODUCTION-MONITORING-DRIFT-LIFECYCLE.md` — classic ML drift/retraining/shadow/canary lifecycle.
- `DESIGNING-ML-SYSTEMS-ALIGNMENT.md` — systems/production extraction from Chip Huyen.

## 7. Banking and insurance transposition

- `BANKING-INSURANCE-AI-USE-CASE-MAP.md` — payments, fraud, AML, surveillance, credit, customer service, wealth, underwriting, claims, IT ops.
- `ML-SOLUTIONS-ARCHITECT-HANDBOOK-ALIGNMENT.md` — banking/insurance ML/GenAI architect interpretation.
- `LEGACY-TO-AI-INTEGRATION-PATTERNS.md` — modernization/integration boundary.

Specialist evidence repositories to reuse rather than duplicate:
- IBM MQ/OpenShift payment EDA;
- Kafka/DDD/OpenShift;
- API Management;
- Azure/ARO AI platform;
- GitOps/OpenShift;
- Wero/ISO 20022/payment references;
- TradeOps agentic runtime.

## 8. Multi-cloud / provider-neutral architecture

- `GOOGLE-AI-SOLUTIONS-ARCHITECT-ALIGNMENT.md` — portable lessons from the Google-focused book.
- I18 in `ENTERPRISE-AI-THEORETICAL-DESIGN-I13-I20.md` — policy-based private/Azure/AWS/GCP placement.
- `AI-ARCHITECTURE-ADR-REFERENCE.md` — provider-neutral contracts, placement, gateway/router, reversibility.
- `AI-ARCHITECTURE-FITNESS-FUNCTIONS.md` — provider eligibility and portability checks.

## 9. Distributed-data foundation

- `DESIGNING-DATA-INTENSIVE-APPLICATIONS-ALIGNMENT.md` — distributed-data alignment for AI.
- `AI-DATA-SYSTEMS-ARCHITECTURE-PRINCIPLES.md` — practical AI data-system rules.

## 10. Evolutionary architecture

- `BUILDING-EVOLUTIONARY-ARCHITECTURES-ALIGNMENT.md` — evolutionary architecture interpretation for AI.
- `AI-ARCHITECTURE-FITNESS-FUNCTIONS.md` — testable governance catalog.

## 11. Book program

- `AI-ARCHITECT-BOOK-BACKLOG.md` — source list, extraction status and future-source policy.

Architecture book baseline currently processed:
1. *AI Engineering*.
2. *Solutions Architect's Handbook — 3rd Edition*.
3. *Enterprise Generative AI Well-Architected Framework & Patterns*.
4. *Architecting Generative AI Applications*.
5. *Google Machine Learning and Generative AI for Solutions Architects*.
6. *The Machine Learning Solutions Architect Handbook — 2nd Edition*.
7. *Designing Machine Learning Systems*.
8. *Designing Data-Intensive Applications — 2nd Edition*.
9. *Building Evolutionary Architectures — 2nd Edition*.

## 12. How to use the knowledge base for a mission

1. Extract mission/business capabilities.
2. Map them to existing architecture knowledge and runtime evidence.
3. Start with SAD + FR/NFR + constraints.
4. Select pattern(s) and ADRs.
5. Run Well-Architected/risk/security review.
6. Identify only the material uncertainties that need evidence.
7. Reuse existing specialist repos first.
8. Build the smallest targeted POC only if evidence is missing.
9. Record test/deployment evidence and upgrade status truthfully.
10. Stop; do not create unrelated POCs.

## 13. Status discipline

`DESIGNED -> IMPLEMENTED -> TESTED -> DEPLOYED -> VERIFIED`

Architecture theory can be complete while runtime evidence remains deferred. Never infer runtime maturity from the presence of a design document.
