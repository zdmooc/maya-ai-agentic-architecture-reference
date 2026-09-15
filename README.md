# Maya AI Agentic Architecture Reference

**AI Solution Architect — Agentic AI, Enterprise AI Platform & Real-Time Systems**

This repository is the architecture reference and portfolio index for a demonstrable enterprise-grade AI solution architecture program. Trading is the primary real-time domain used to exercise the architecture, but the patterns are designed to transfer to banking, payments, insurance, fraud, risk, anomaly detection, cybersecurity, IT operations and enterprise decisioning.

The program is also extended toward a broader **Enterprise AI Architecture / AI Platform / Hybrid Multi-Cloud** reference portfolio while preserving the evidence-first rules of the existing I0-I12 roadmap.

## Scope

The repository is intentionally an **architecture and evidence hub**, not a second implementation repository.

- Executable trading integration baseline: [`zdmooc/TradeOps-GenAI-Integration`](https://github.com/zdmooc/TradeOps-GenAI-Integration)
- OpenShift/CRC trading platform patterns: [`zdmooc/openshift2026-openshift-local-trading-gateway`](https://github.com/zdmooc/openshift2026-openshift-local-trading-gateway)
- Enterprise Kafka/DDD reference: [`zdmooc/mayabank-kafka-ddd-openshift`](https://github.com/zdmooc/mayabank-kafka-ddd-openshift)
- IBM MQ/OpenShift EDA payment reference: [`zdmooc/mayabank-ibm-mq-native-ha-openshift-eda-platform`](https://github.com/zdmooc/mayabank-ibm-mq-native-ha-openshift-eda-platform)
- Azure pattern/reference source: [`zdmooc/mayabank-azure-cloud-ai-platform`](https://github.com/zdmooc/mayabank-azure-cloud-ai-platform)
- API Management architecture reference: [`zdmooc/mayabank-api-management-architecture`](https://github.com/zdmooc/mayabank-api-management-architecture)
- Carbon-aware / GreenOps decision reference: [`zdmooc/mayabank-carbon-aware-decision-architecture`](https://github.com/zdmooc/mayabank-carbon-aware-decision-architecture)

The program backlog and architecture decisions remain mastered in this repository. Specialist repositories are reused as implementation/evidence sources; they are not merged wholesale into this repository.

## Enterprise AI V10 extension

The current I0-I12 program already covers substantial Agentic AI, MLOps, OpenShift/GitOps, OpenShift AI/KServe model serving, observability/security/LLMOps and Azure/ARO architecture.

The Enterprise AI extension covers Knowledge Copilot, governed knowledge ingestion, AI Gateway/policy enforcement, Design Authority, Responsible AI, AI Factory/GPU operations, hybrid multi-cloud placement, payment operations and multimodal/document automation.

- [Enterprise AI Portfolio V10 gap matrix](enterprise/V10-GAP-MATRIX.md)
- [Enterprise AI implementation roadmap I13-I20](enterprise/ENTERPRISE-AI-ROADMAP-I13-I20.md)
- [Enterprise AI theoretical design I13-I20](enterprise/ENTERPRISE-AI-THEORETICAL-DESIGN-I13-I20.md)
- [AI Engineering fundamentals reference](enterprise/AI-ENGINEERING-FUNDAMENTALS.md)
- [AI Engineering official book/repository alignment](enterprise/AI-ENGINEERING-BOOK-ALIGNMENT.md)
- [AI Architect book decomposition backlog](enterprise/AI-ARCHITECT-BOOK-BACKLOG.md)
- [Solutions Architect's Handbook alignment](enterprise/SOLUTIONS-ARCHITECTS-HANDBOOK-ALIGNMENT.md)

**I13-I20 are now `DESIGNED` at architecture/theory level. Their runtime POCs remain `NOT IMPLEMENTED` and are intentionally deferred until a concrete business use case, mission or interview requirement justifies them.**

Theoretical completion includes the target architecture, design principles, component responsibilities, data and knowledge contracts, security/governance rules, NFRs, provider/placement principles, AI Factory design, payment transposition and a business-demand-to-POC activation matrix. The AI Engineering fundamentals reference covers foundation-model concepts, evaluation, prompt engineering, RAG/agents, fine-tuning, dataset engineering, inference optimization and feedback architecture. The official-book alignment closes remaining theory details such as scaling-law concepts, benchmark limitations, fine-tuning memory composition, agent memory/evaluation and feedback limitations. No deployment or benchmark claim is implied by `DESIGNED`.

## AI Solution Architecture dossier

The repository now includes a reusable architect deliverable pack derived from the Solution Architecture alignment work:

- [AI Solution Architecture Document template](enterprise/AI-SOLUTION-ARCHITECTURE-DOCUMENT-TEMPLATE.md)
- [AI FR/NFR catalog](enterprise/AI-FR-NFR-CATALOG.md)
- [AI architecture constraints register](enterprise/AI-ARCHITECTURE-CONSTRAINTS-REGISTER.md)
- [AI performance budget template](enterprise/AI-PERFORMANCE-BUDGET-TEMPLATE.md)
- [AI architecture review checklist](enterprise/AI-ARCHITECTURE-REVIEW-CHECKLIST.md)
- [AI architecture pattern catalog](enterprise/AI-ARCHITECTURE-PATTERN-CATALOG.md)
- [AI architecture ADR reference set](enterprise/AI-ARCHITECTURE-ADR-REFERENCE.md)
- [AI architecture risk register](enterprise/AI-ARCHITECTURE-RISK-REGISTER.md)
- [AI architecture RACI](enterprise/AI-ARCHITECTURE-RACI.md)
- [Legacy-to-AI integration patterns](enterprise/LEGACY-TO-AI-INTEGRATION-PATTERNS.md)

These artifacts are designed for **AI Solution Architect / Enterprise AI Architect / Design Authority** work. They structure business demand, FR/NFR, constraints, patterns, trade-offs, risks, responsibilities, review gates and production-readiness evidence. They do not imply implementation or live-environment validation.

Architect operating model:

`Business demand -> discovery -> FR/NFR -> constraints -> options -> target architecture -> ADR -> POC only if material uncertainty remains -> architecture review -> delivery governance -> production readiness -> post-launch operability`

For the Azure/ARO industrialization work, see:

- [`enterprise/AZURE-ARO-INDUSTRIALIZATION-BACKLOG.md`](enterprise/AZURE-ARO-INDUSTRIALIZATION-BACKLOG.md)
- executable implementation/evidence in [`zdmooc/TradeOps-GenAI-Integration`](https://github.com/zdmooc/TradeOps-GenAI-Integration)

For the demonstrable business UI / trading cockpit workstream, see:

- [`enterprise/TRADEOPS-WEB-COCKPIT.md`](enterprise/TRADEOPS-WEB-COCKPIT.md)
- implementation backlog: [`TradeOps docs/27-tradeops-web-cockpit.md`](https://github.com/zdmooc/TradeOps-GenAI-Integration/blob/main/docs/27-tradeops-web-cockpit.md)
- CRC demo URL catalog: [`TradeOps docs/28-demo-urls.md`](https://github.com/zdmooc/TradeOps-GenAI-Integration/blob/main/docs/28-demo-urls.md)

## Architecture rule

```text
Live/Replay Sources
  -> Source Adapters
  -> Data Quality + Canonical Market Model
  -> Kafka-compatible Event Backbone
  -> Deterministic Technical / Pattern / Regime Engines
  -> Feature Pipeline
  -> Calibrated ML Signal Quality
  -> Specialized Agents + RAG + Governed MCP Tools
  -> Fusion
  -> DETERMINISTIC RISK GATE
  -> Human-in-the-Loop
  -> Alert / Dashboard / Paper or Shadow Trading
```

The LLM never invents prices, replaces quantitative calculations, or bypasses risk policy. A model score is not called a probability unless calibration has been demonstrated.

For enterprise transposition, the same control philosophy applies: deterministic policy remains authoritative, agents orchestrate governed capabilities, evidence is traceable and sensitive actions require explicit controls and human approval.

## Current maturity

The detailed implementation/evidence status for I0-I12 is maintained in [`ROADMAP.md`](ROADMAP.md) and the versioned evidence files under [`evidence/`](evidence/).

For I13-I20, distinguish two dimensions:

- **Architecture/theory:** `DESIGNED`.
- **Executable POC/runtime evidence:** `NOT IMPLEMENTED` until selected by business demand and proven by code/tests/deployment evidence.

The selection rule is demand-driven rather than sequential: Enterprise RAG activates I13/I14; AI Security activates I16; OpenShift AI/AI Platform activates I17; hybrid/multi-cloud activates I18; banking/payments AI activates I19; multimodal/document automation activates I20.

Book-alignment status:

- **AI Engineering — Chip Huyen:** theoretical alignment complete.
- **Solutions Architect's Handbook — 3rd Edition:** architecture extraction complete; no mandatory POC produced.
- Next target: **Enterprise Generative AI Well-Architected Framework & Patterns**.

See:

- [`MASTER-CHARTER.md`](MASTER-CHARTER.md)
- [`ROADMAP.md`](ROADMAP.md)
- [`architecture/vision/ARCHITECTURE-VISION.md`](architecture/vision/ARCHITECTURE-VISION.md)
- [`architecture/TARGET-ARCHITECTURE.md`](architecture/TARGET-ARCHITECTURE.md)
- [`enterprise/ENTERPRISE-AI-THEORETICAL-DESIGN-I13-I20.md`](enterprise/ENTERPRISE-AI-THEORETICAL-DESIGN-I13-I20.md)
- [`enterprise/AI-ENGINEERING-FUNDAMENTALS.md`](enterprise/AI-ENGINEERING-FUNDAMENTALS.md)
- [`enterprise/AI-ENGINEERING-BOOK-ALIGNMENT.md`](enterprise/AI-ENGINEERING-BOOK-ALIGNMENT.md)
- [`enterprise/SOLUTIONS-ARCHITECTS-HANDBOOK-ALIGNMENT.md`](enterprise/SOLUTIONS-ARCHITECTS-HANDBOOK-ALIGNMENT.md)
- [`enterprise/AI-ARCHITECT-BOOK-BACKLOG.md`](enterprise/AI-ARCHITECT-BOOK-BACKLOG.md)
- [`reuse/OWN-REPOSITORIES.md`](reuse/OWN-REPOSITORIES.md)
- [`reuse/PUBLIC-REPOSITORIES.md`](reuse/PUBLIC-REPOSITORIES.md)
- [`evidence/`](evidence/)

## Status vocabulary

Every claim must use one of these states according to evidence:

`DESIGNED` -> `IMPLEMENTED` -> `TESTED` -> `DEPLOYED` -> `VERIFIED`

`DESIGNED` means architecture/design material exists. It does not imply executable runtime evidence. Planned implementation work must remain explicitly labelled `NOT IMPLEMENTED` until evidence exists.

## Safety and financial scope

The financial/trading scope remains analysis, signal generation, replay/backtesting, paper/shadow trading and explicit human approval. Automated real-money execution is out of scope until a later architecture decision is backed by controls, test evidence and operational governance.
