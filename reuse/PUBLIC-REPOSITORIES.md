# Public Project Audit

Verification date: **2026-09-11**. Versions and licenses must be rechecked when dependencies are pinned.

## Market connectivity and trading engines

| Project | Current finding | License | Decision | Intended use |
|---|---|---|---|---|
| IG REST + Streaming / Lightstreamer | Official IG documentation still describes REST plus Lightstreamer for real-time prices/trade/account updates | IG service terms apply | **INTEGRATE contract** | Primary IG connectivity specification; demo first |
| `ig-python/trading-ig` | Maintained Python wrapper; package currently identifies as v0.0.24 / Alpha and supports REST + Lightstreamer | BSD-3-Clause | ADAPT / REFERENCE | Speed up adapter implementation, but validate behavior against official IG API docs |
| `nautechsystems/nautilus_trader` | Active production-grade deterministic event-driven trading engine; updated 2026-09-10 during audit | LGPL-3.0 | **REFERENCE / POC** | Backtesting, replay, event-model and execution architecture study; avoid unnecessary reimplementation |
| `QuantConnect/Lean` | Mature algorithmic engine with local backtest/optimization/live workflows | Apache-2.0 | REFERENCE | Independent backtesting/reference option and architecture comparison |

## Agentic AI and MCP

| Project | Current finding | License | Decision | Intended use |
|---|---|---|---|---|
| `langchain-ai/langgraph` | Active low-level framework for stateful/durable agent orchestration | MIT | **ADAPT / candidate baseline** | Replace the hand-written “LangGraph-style” controller after ADR/POC |
| `microsoft/agent-framework` | Current Python metadata identifies production/stable package line and MIT license | MIT | REFERENCE / POC | Enterprise/Azure alternative to evaluate, not run in parallel by default |
| `modelcontextprotocol/servers` | Official reference implementations; project explicitly warns they are educational references, not production-ready | licensing transition: new contributions Apache-2.0, some existing MIT | **REFERENCE** | Protocol/sdk patterns only; implement security for our threat model |
| LiteLLM | Active multi-provider LLM gateway project | MIT (current project/docs audit) | ADAPT | Provider abstraction, routing/cost controls when multiple LLM providers are actually needed |
| Envoy AI Gateway | Active Kubernetes-native AI gateway with MCP-related work visible in 2026 | Apache-2.0 | REFERENCE / later POC | Evaluate only if gateway-scale routing/policy justifies complexity |

## RAG / ML / MLOps

| Project | Current finding | License | Decision | Intended use |
|---|---|---|---|---|
| Qdrant | Active production-ready vector database | Apache-2.0 | **REUSE** | Keep as initial vector store unless evaluation shows a reason to change |
| MLflow | Very active; current project positions itself across ML, agents and LLMs | Apache-2.0 | **INTEGRATE** | Experiment tracking, model registry, evaluation metadata, lifecycle evidence |
| Feast | Active feature store | Apache-2.0 | DEFER | Add only when online/offline feature consistency requires it |
| XGBoost | Active/stable gradient boosting library | Apache-2.0 | INTEGRATE candidate | Baseline tree model after leakage-safe dataset exists |
| LightGBM | Active gradient boosting library | MIT | INTEGRATE candidate | Compare against XGBoost where justified |
| scikit-learn | Mature ML library; current copyright/license reviewed | BSD-3-Clause | **INTEGRATE** | Baselines, preprocessing, calibration and metrics |

## Observability

| Project | Current finding | License | Decision | Intended use |
|---|---|---|---|---|
| OpenTelemetry | Highly active CNCF ecosystem | Apache-2.0 | **INTEGRATE** | End-to-end traces/metrics/log correlation |
| Prometheus + Grafana | Existing TradeOps baseline already uses them | respective project licenses | **REUSE** | Runtime and business metrics/dashboards |
| Arize Phoenix | Very active AI observability/evaluation project | **Elastic License 2.0** | OPTIONAL / LICENSE REVIEW | Useful for LLM/agent evaluation, but not a default “open-source” baseline without legal/usage review |

## Streaming / platform

| Project | Current finding | License | Decision | Intended use |
|---|---|---|---|---|
| Apache Kafka | Industry-standard event backbone | Apache-2.0 | TARGET CONTRACT | Production-neutral event architecture |
| Redpanda | Kafka-compatible and convenient for local labs; current Redpanda server licensing is BSL 1.1 with an additional-use grant and later change to Apache-2.0 by release | BSL 1.1 (server current line) | **LAB / LICENSE-AWARE** | CRC/dev convenience, not an unexamined enterprise default |
| Argo CD | Very active GitOps controller | Apache-2.0 | **INTEGRATE** | GitOps reconciliation |
| Kustomize / Helm | Mature Kubernetes packaging tools | permissive OSS licenses | INTEGRATE | environment overlays and packaging |
| Kyverno | Active policy-as-code project; 2026 releases deprecate legacy policy types in favor of newer APIs | Apache-2.0 | **INTEGRATE after API pinning** | admission/governance/SBOM/security policies |

## AI serving / OpenShift

| Project | Current finding | License | Decision | Intended use |
|---|---|---|---|---|
| OpenShift AI | Red Hat documentation for current 3.4 line documents KServe-based model deployment and vLLM runtimes | product subscription terms + upstream licenses | **TARGET** | Enterprise AI platform on OpenShift where required |
| KServe | Active Kubernetes inference platform; current release line includes v0.18.0 in 2026 audit | Apache-2.0 | **INTEGRATE target** | Standard model serving on Kubernetes/OpenShift |
| vLLM | Very active high-throughput LLM serving project | Apache-2.0 | **INTEGRATE target** | LLM serving where supported hardware exists |
| Ollama | Active local model runtime | MIT | **REUSE for local dev** | Run LLM outside CRC when local resource constraints favor it |

## Selection principles

- Prefer **official protocol/API documentation** over a convenience wrapper when behavior conflicts.
- Prefer one orchestration framework after an ADR; do not build framework tourism into the architecture.
- Keep the event contract Kafka-compatible and portable.
- Use Redpanda for local efficiency only with explicit license awareness.
- Do not introduce Feast, Envoy AI Gateway or Phoenix until a concrete requirement pays for their operational/licensing complexity.
- Reference mature trading engines for replay/backtest design instead of inventing every subsystem.

## Verification URLs

- https://labs.ig.com/
- https://github.com/ig-python/trading-ig
- https://github.com/nautechsystems/nautilus_trader
- https://github.com/QuantConnect/Lean
- https://github.com/langchain-ai/langgraph
- https://github.com/microsoft/agent-framework
- https://github.com/modelcontextprotocol/servers
- https://github.com/BerriAI/litellm
- https://github.com/envoyproxy/ai-gateway
- https://github.com/qdrant/qdrant
- https://github.com/mlflow/mlflow
- https://github.com/feast-dev/feast
- https://github.com/dmlc/xgboost
- https://github.com/lightgbm-org/LightGBM
- https://github.com/scikit-learn/scikit-learn
- https://github.com/open-telemetry
- https://github.com/Arize-ai/phoenix
- https://github.com/redpanda-data/redpanda
- https://github.com/argoproj/argo-cd
- https://github.com/kyverno/kyverno
- https://github.com/kserve/kserve
- https://github.com/vllm-project/vllm
- https://github.com/ollama/ollama
- https://docs.redhat.com/en/documentation/red_hat_openshift_ai_self-managed/3.4/
