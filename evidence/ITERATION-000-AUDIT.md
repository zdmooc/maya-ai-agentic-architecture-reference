# Iteration 000 — Audit Evidence

Date: **2026-09-11**

Status: **VERIFIED for repository inspection; DESIGNED/IMPLEMENTED for the documentation baseline.**

No runtime tests or deployments were executed as part of this iteration.

## Scope inspected

- `zdmooc/maya-ai-agentic-architecture-reference`
- `zdmooc/TradeOps-GenAI-Integration`
- `zdmooc/Maya`
- `zdmooc/Maya-gitops`
- `zdmooc/mayabank-kafka-ddd-openshift`
- `zdmooc/mayabank-azure-cloud-ai-platform`
- `zdmooc/openshift2026-openshift-local-trading-gateway`
- `zdmooc/openshift-platform-blueprints`
- `zdmooc/mayabank-ibm-odm-ai-decision-architecture`
- `zdmooc/maya-interlink-enterprise-ai-platform`
- public projects listed in `reuse/PUBLIC-REPOSITORIES.md`

## Verified findings

### Master repository

Before I0 the GitHub contents API returned the repository as empty. I0 initializes it as the architecture/reuse/evidence hub.

### TradeOps executable baseline

Observed concrete files include services for agent controller, RAG, MCP server, signal engine, risk engine, paper OMS, workflow API, market data and shared Kafka/audit/metrics utilities, plus Postgres/Redpanda/Prometheus/Grafana configuration, Helm/GitOps assets, tests and evidence samples.

Important limitations were verified directly in code:

1. `services/signal_engine/worker.py` generates BUY/SELL from the fractional part of a synthetic/demo price. This is deliberately arbitrary demo logic and is marked **REPLACE** for the target architecture.
2. `services/risk_engine/worker.py` uses demo quantity sizing and a simple `MAX_QTY` breach. This is not the required deterministic portfolio/risk engine and is marked **REPLACE/EXPAND**.
3. `services/common/otel.py` is only a minimal placeholder hook. End-to-end OpenTelemetry is therefore a genuine gap.
4. `services/agent_controller/graph.py` describes itself as “LangGraph-style” but explicitly implements the sequence without the LangGraph dependency. It includes RAG and MCP calls plus a heuristic confidence calculation. It is marked **ADAPT** and must not be presented as calibrated or as a real LangGraph runtime.
5. `services/mcp_server/tools.py` implements an internal tool registry with synthetic prices, demo risk and paper order placement. The tool-boundary concept is reusable, but the target must implement standards-aligned MCP security and explicit paper/live separation.

Observed source blob SHAs at audit time:

- signal engine: `86ed6807f195cb2ae552ccbd316a53e069a7162b`
- risk engine: `9cae1c504e2c69d116644b658375dd31d0e440d5`
- OTel hook: `69be476ad2787c21c147625f2244b4a3ea675d03`
- agent graph: `9436bd5aef6492e0ff66f822c85dd361dcce3713`
- MCP tools: `bd79f3f86855b922b773ff3103c49daf43adb0d6`

### Maya and Maya-gitops

`Maya` currently contains documentation rather than product code. `Maya-gitops` currently contains its README and CRC documentation but not the full target GitOps tree described in the README. Both are references, not competing executable baselines.

### Other useful internal assets

- `mayabank-kafka-ddd-openshift`: strong enterprise EDA/DDD reasoning and Kafka governance reference.
- `mayabank-azure-cloud-ai-platform`: broad Azure architecture and selected Terraform labs; repository correctly distinguishes designed from actually executed labs.
- `openshift2026-openshift-local-trading-gateway`: concrete CRC/Kustomize/trading platform manifests and scripts; useful for deployment patterns.
- `openshift-platform-blueprints`: OpenShift/platform engineering capitalisation reference.
- `mayabank-ibm-odm-ai-decision-architecture`: especially relevant analogue for deterministic policy + ML + GenAI + governed tools + HITL.
- `maya-interlink-enterprise-ai-platform`: empty during audit and therefore ignored to prevent duplication.

## Public-project verification highlights

- Official IG documentation still exposes REST and Lightstreamer streaming concepts; demo-account use is recommended by IG for testing.
- NautilusTrader was active during the audit window and uses LGPL-3.0.
- LangGraph is active and MIT-licensed.
- Microsoft Agent Framework current Python metadata identifies MIT and Production/Stable.
- Official MCP reference servers warn that examples are references, not production-ready solutions; current project licensing is transitioning toward Apache-2.0 for new contributions.
- Qdrant is Apache-2.0.
- MLflow is Apache-2.0 and highly active.
- Feast is Apache-2.0.
- XGBoost is Apache-2.0, LightGBM MIT, scikit-learn BSD-3-Clause.
- OpenTelemetry is active and Apache-2.0.
- Phoenix is currently Elastic License 2.0; it is not treated as an unquestioned OSS baseline.
- Redpanda server code currently uses BSL 1.1 terms with a later change license; use is therefore license-aware.
- KServe is Apache-2.0 and current Red Hat OpenShift AI 3.4 documentation covers KServe/vLLM model-serving patterns.
- Ollama is MIT and suitable for the local-development option.
- Kyverno is Apache-2.0; current 2026 evolution requires API-version pinning rather than copying old policy manifests.

## Test / deployment declaration

I0 changed architecture documentation only.

- Unit tests: **NOT RUN in I0**
- Integration tests: **NOT RUN in I0**
- CRC deployment: **NOT RUN in I0**
- Azure deployment: **NOT RUN in I0**
- Live market connectivity: **NOT RUN in I0**
- Backtest profitability: **NOT CLAIMED**
- ML calibration: **NOT CLAIMED**
- HA: **NOT CLAIMED**

This is deliberate: the purpose of I0 is to establish a truthful architecture and reuse baseline before implementation changes.
