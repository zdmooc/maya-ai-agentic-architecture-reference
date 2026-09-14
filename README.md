# Maya AI Agentic Architecture Reference

**AI Solution Architect — Agentic AI, Enterprise AI Platform & Real-Time Systems**

This repository is the architecture reference and portfolio index for a demonstrable enterprise-grade AI solution architecture program. Trading is the primary real-time domain used to exercise the architecture, but the patterns are designed to transfer to banking, payments, insurance, fraud, risk, anomaly detection, cybersecurity, IT operations and enterprise decisioning.

The program is now also being extended toward a broader **Enterprise AI Architecture / AI Platform / Hybrid Multi-Cloud** reference portfolio while preserving the evidence-first rules of the existing I0-I12 roadmap.

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

The next enterprise extension closes the remaining gaps around Knowledge Copilot, governed knowledge ingestion, AI Gateway/policy enforcement, Design Authority, Responsible AI, AI Factory/GPU operations, hybrid multi-cloud placement and payment operations.

- [Enterprise AI Portfolio V10 gap matrix](enterprise/V10-GAP-MATRIX.md)
- [Enterprise AI Roadmap I13-I20](enterprise/ENTERPRISE-AI-ROADMAP-I13-I20.md)

**I13-I20 are PLANNED / NOT IMPLEMENTED until evidence proves otherwise.**

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

The detailed capability status is maintained in [`ROADMAP.md`](ROADMAP.md) and the versioned evidence files under [`evidence/`](evidence/).

The enterprise I13-I20 extension is a planned roadmap and must not be interpreted as implementation evidence.

See:

- [`MASTER-CHARTER.md`](MASTER-CHARTER.md)
- [`ROADMAP.md`](ROADMAP.md)
- [`architecture/vision/ARCHITECTURE-VISION.md`](architecture/vision/ARCHITECTURE-VISION.md)
- [`architecture/TARGET-ARCHITECTURE.md`](architecture/TARGET-ARCHITECTURE.md)
- [`reuse/OWN-REPOSITORIES.md`](reuse/OWN-REPOSITORIES.md)
- [`reuse/PUBLIC-REPOSITORIES.md`](reuse/PUBLIC-REPOSITORIES.md)
- [`evidence/`](evidence/)

## Status vocabulary

Every claim must use one of these states according to evidence:

`DESIGNED` → `IMPLEMENTED` → `TESTED` → `DEPLOYED` → `VERIFIED`

Planned work must be labelled explicitly as `PLANNED / NOT IMPLEMENTED`.

## Safety and financial scope

The financial/trading scope remains analysis, signal generation, replay/backtesting, paper/shadow trading and explicit human approval. Automated real-money execution is out of scope until a later architecture decision is backed by controls, test evidence and operational governance.
