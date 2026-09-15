# Maya AI Agentic Architecture Reference

**AI Solution Architect — Agentic AI, Enterprise AI Platform & Real-Time Systems**

This repository is the architecture reference and portfolio index for a demonstrable enterprise-grade AI solution architecture program. Trading is the primary real-time domain used to exercise the architecture, but the patterns are designed to transfer to banking, payments, insurance, fraud, risk, anomaly detection, cybersecurity, IT operations and enterprise decisioning.

The program extends toward a broader **Enterprise AI Architecture / AI Platform / Hybrid Multi-Cloud** reference portfolio while preserving evidence-first status discipline.

## Start here

- [AI Architect Knowledge Base Index](enterprise/AI-ARCHITECT-KNOWLEDGE-BASE-INDEX.md)
- [AI Architect book/source baseline — 9/9 complete](enterprise/AI-ARCHITECT-BOOK-BACKLOG.md)
- [Enterprise AI theoretical design I13-I20](enterprise/ENTERPRISE-AI-THEORETICAL-DESIGN-I13-I20.md)
- [AI Engineering fundamentals](enterprise/AI-ENGINEERING-FUNDAMENTALS.md)
- [Target architecture](architecture/TARGET-ARCHITECTURE.md)
- [Roadmap / evidence status](ROADMAP.md)

## Scope

This repository is intentionally an **architecture and evidence hub**, not a second implementation repository.

Specialist repositories are reused as implementation/evidence sources:

- Executable agentic/trading baseline: [`zdmooc/TradeOps-GenAI-Integration`](https://github.com/zdmooc/TradeOps-GenAI-Integration)
- OpenShift/CRC patterns: [`zdmooc/openshift2026-openshift-local-trading-gateway`](https://github.com/zdmooc/openshift2026-openshift-local-trading-gateway)
- Kafka/DDD enterprise reference: [`zdmooc/mayabank-kafka-ddd-openshift`](https://github.com/zdmooc/mayabank-kafka-ddd-openshift)
- IBM MQ/OpenShift payment EDA: [`zdmooc/mayabank-ibm-mq-native-ha-openshift-eda-platform`](https://github.com/zdmooc/mayabank-ibm-mq-native-ha-openshift-eda-platform)
- Azure architecture/reference: [`zdmooc/mayabank-azure-cloud-ai-platform`](https://github.com/zdmooc/mayabank-azure-cloud-ai-platform)
- API Management: [`zdmooc/mayabank-api-management-architecture`](https://github.com/zdmooc/mayabank-api-management-architecture)
- GreenOps/carbon-aware decisioning: [`zdmooc/mayabank-carbon-aware-decision-architecture`](https://github.com/zdmooc/mayabank-carbon-aware-decision-architecture)

The program backlog and architecture decisions remain mastered here. Specialist repositories are not copied wholesale.

## Enterprise AI architecture maturity

The current I0-I12 program already covers substantial Agentic AI, MLOps, OpenShift/GitOps, OpenShift AI/KServe model serving, observability/security/LLMOps and Azure/ARO architecture.

I13-I20 extend the reference with Enterprise Knowledge/RAG, governed ingestion, evaluation/feedback/FinOps, Design Authority, AI Gateway/security/Responsible AI, AI Factory/GPU operations, hybrid multi-cloud placement, payment/operations AI and multimodal/document automation.

- [Enterprise AI V10 gap baseline](enterprise/V10-GAP-MATRIX.md)
- [Implementation roadmap I13-I20](enterprise/ENTERPRISE-AI-ROADMAP-I13-I20.md)
- [Theoretical design I13-I20](enterprise/ENTERPRISE-AI-THEORETICAL-DESIGN-I13-I20.md)

**I13-I20 are `DESIGNED` at architecture/theory level. Their runtime POCs remain `NOT IMPLEMENTED` until a concrete business use case, mission, interview requirement or platform constraint justifies the evidence work.**

No deployment, benchmark or production claim is implied by `DESIGNED`.

## AI Solution Architecture dossier

Reusable deliverables for **AI Solution Architect / Enterprise AI Architect / Design Authority** work:

- [Canonical AI Solution Architecture Document template](enterprise/AI-SOLUTION-ARCHITECTURE-DOCUMENT-TEMPLATE.md)
- [AI FR/NFR catalog](enterprise/AI-FR-NFR-CATALOG.md)
- [Architecture constraints register](enterprise/AI-ARCHITECTURE-CONSTRAINTS-REGISTER.md)
- [Performance budget template](enterprise/AI-PERFORMANCE-BUDGET-TEMPLATE.md)
- [Architecture review checklist](enterprise/AI-ARCHITECTURE-REVIEW-CHECKLIST.md)
- [Architecture pattern catalog](enterprise/AI-ARCHITECTURE-PATTERN-CATALOG.md)
- [ADR reference set](enterprise/AI-ARCHITECTURE-ADR-REFERENCE.md)
- [AI risk register](enterprise/AI-ARCHITECTURE-RISK-REGISTER.md)
- [Architecture RACI](enterprise/AI-ARCHITECTURE-RACI.md)
- [Legacy-to-AI integration patterns](enterprise/LEGACY-TO-AI-INTEGRATION-PATTERNS.md)

Architect operating model:

`Business demand -> discovery -> FR/NFR -> constraints -> options -> target architecture -> ADR -> POC only if material uncertainty remains -> architecture review -> delivery governance -> production readiness -> post-launch operability`

## Well-Architected, governance and production

- [GenAI Well-Architected scorecard](enterprise/GENAI-WELL-ARCHITECTED-SCORECARD.md)
- [AI interaction archival/compliance pattern](enterprise/AI-INTERACTION-ARCHIVAL-COMPLIANCE-PATTERN.md)
- [GenAI production maturity model](enterprise/GENAI-PRODUCTION-MATURITY-MODEL.md)
- [GenAI platform capability map](enterprise/GENAI-PLATFORM-CAPABILITY-MAP.md)
- [GenAI SRE / SLO / error-budget model](enterprise/GENAI-SRE-SLO-ERROR-BUDGET.md)
- [Online experimentation pattern](enterprise/GENAI-ONLINE-EXPERIMENTATION-PATTERN.md)
- [AI architecture fitness functions](enterprise/AI-ARCHITECTURE-FITNESS-FUNCTIONS.md)

## AI/ML and banking/insurance architecture

- [Unified AI/ML Solution Architecture lifecycle](enterprise/AI-ML-SOLUTION-ARCHITECTURE-LIFECYCLE.md)
- [Banking & Insurance AI use-case map](enterprise/BANKING-INSURANCE-AI-USE-CASE-MAP.md)
- [ML production monitoring/drift/retraining lifecycle](enterprise/ML-PRODUCTION-MONITORING-DRIFT-LIFECYCLE.md)
- [AI data-systems architecture principles](enterprise/AI-DATA-SYSTEMS-ARCHITECTURE-PRINCIPLES.md)

The core boundary is explicit:

`deterministic controls -> classic ML where predictive scoring is appropriate -> GenAI/RAG/agents where language/knowledge/orchestration is appropriate -> HITL for sensitive actions`

LLM output never overrides hard security, entitlement, compliance, transaction or risk policy.

## Architecture-source baseline

Nine architecture sources have been extracted into the reference:

1. *AI Engineering* — Chip Huyen.
2. *Solutions Architect's Handbook — 3rd Edition*.
3. *Enterprise Generative AI Well-Architected Framework & Patterns*.
4. *Architecting Generative AI Applications*.
5. *Google Machine Learning and Generative AI for Solutions Architects*.
6. *The Machine Learning Solutions Architect Handbook — 2nd Edition*.
7. *Designing Machine Learning Systems* — Chip Huyen.
8. *Designing Data-Intensive Applications — 2nd Edition*.
9. *Building Evolutionary Architectures — 2nd Edition*.

See [AI Architect Book Backlog](enterprise/AI-ARCHITECT-BOOK-BACKLOG.md) for mappings and scope decisions.

A new source is added only when it closes a real architecture gap, supports a target mission/domain/provider, or reflects a material change in regulation/industry practice.

## Current maturity and evidence rule

Detailed implementation/evidence status for I0-I12 is maintained in [`ROADMAP.md`](ROADMAP.md) and versioned evidence under [`evidence/`](evidence/).

For architecture/theory versus runtime proof, always distinguish:

- **Architecture/theory:** `DESIGNED`.
- **Executable POC/runtime evidence:** remains `NOT IMPLEMENTED` until code/tests/deployment evidence exists.

POC selection is demand-driven rather than sequential: Enterprise RAG activates I13/I14; AI Security activates I16; OpenShift AI/AI Platform activates I17; hybrid/multi-cloud activates I18; banking/payments AI activates I19; multimodal/document automation activates I20.

## Status vocabulary

`DESIGNED -> IMPLEMENTED -> TESTED -> DEPLOYED -> VERIFIED`

`DESIGNED` means architecture/design material exists. It does not imply executable runtime evidence.

## Safety and financial scope

The financial/trading scope remains analysis, signal generation, replay/backtesting, paper/shadow trading and explicit human approval. Automated real-money execution is out of scope until a later architecture decision is backed by controls, test evidence and operational governance.
