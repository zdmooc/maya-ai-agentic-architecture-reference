# Maya AI Agentic Architecture Reference

**AI Solution Architect — Agentic AI & Real-Time Trading Systems**

This repository is the architecture reference and portfolio index for a demonstrable enterprise-grade AI solution architecture program. Trading is the primary real-time domain used to exercise the architecture, but the patterns are designed to transfer to banking, payments, insurance, fraud, risk, anomaly detection, cybersecurity and real-time enterprise decisioning.

## Scope

The repository is intentionally an **architecture and evidence hub**, not a second implementation repository.

- Executable trading integration baseline: [`zdmooc/TradeOps-GenAI-Integration`](https://github.com/zdmooc/TradeOps-GenAI-Integration)
- OpenShift/CRC trading platform patterns: [`zdmooc/openshift2026-openshift-local-trading-gateway`](https://github.com/zdmooc/openshift2026-openshift-local-trading-gateway)
- Enterprise Kafka/DDD reference: [`zdmooc/mayabank-kafka-ddd-openshift`](https://github.com/zdmooc/mayabank-kafka-ddd-openshift)
- Azure pattern/reference source: [`zdmooc/mayabank-azure-cloud-ai-platform`](https://github.com/zdmooc/mayabank-azure-cloud-ai-platform)

The program backlog and architecture decisions remain mastered in this repository. `mayabank-azure-cloud-ai-platform` is reused as an Azure pattern/reference source; it is not the master backlog for the Agentic AI program.

For the Azure/ARO industrialization work, see:

- [`enterprise/AZURE-ARO-INDUSTRIALIZATION-BACKLOG.md`](enterprise/AZURE-ARO-INDUSTRIALIZATION-BACKLOG.md)
- executable implementation/evidence in [`zdmooc/TradeOps-GenAI-Integration`](https://github.com/zdmooc/TradeOps-GenAI-Integration)

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

## Current maturity

**Iteration 0 — Architecture baseline and reuse audit: IMPLEMENTED in documentation.**

No production deployment, profitable strategy, calibrated model, HA claim or live-money execution is asserted by this repository at Iteration 0.

See:

- [`MASTER-CHARTER.md`](MASTER-CHARTER.md)
- [`ROADMAP.md`](ROADMAP.md)
- [`architecture/vision/ARCHITECTURE-VISION.md`](architecture/vision/ARCHITECTURE-VISION.md)
- [`architecture/TARGET-ARCHITECTURE.md`](architecture/TARGET-ARCHITECTURE.md)
- [`reuse/OWN-REPOSITORIES.md`](reuse/OWN-REPOSITORIES.md)
- [`reuse/PUBLIC-REPOSITORIES.md`](reuse/PUBLIC-REPOSITORIES.md)
- [`evidence/ITERATION-000-AUDIT.md`](evidence/ITERATION-000-AUDIT.md)

## Status vocabulary

Every future claim must use one of these states according to evidence:

`DESIGNED` → `IMPLEMENTED` → `TESTED` → `DEPLOYED` → `VERIFIED`

## Safety and financial scope

The initial financial scope is analysis, signal generation, replay/backtesting, paper/shadow trading and explicit human approval. Automated real-money execution is out of scope until the architecture, controls and evidence justify a separate decision.
