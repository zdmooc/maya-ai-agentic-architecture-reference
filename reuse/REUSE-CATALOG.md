# Reuse Catalog

This catalog defines ownership boundaries so the portfolio remains understandable and avoids duplicate implementations.

| Capability | Source of truth / preferred source | Decision | Notes |
|---|---|---|---|
| Architecture vision / target state | `maya-ai-agentic-architecture-reference` | REUSE | Central portfolio index |
| Executable trading integration | `TradeOps-GenAI-Integration` | ADAPT | Primary implementation baseline |
| CRC trading deployment patterns | `openshift2026-openshift-local-trading-gateway` | ADAPT | Harvest manifests/scripts selectively |
| Enterprise DDD / Kafka governance | `mayabank-kafka-ddd-openshift` | REFERENCE | Translate patterns, do not duplicate runtime |
| Azure architecture | `mayabank-azure-cloud-ai-platform` | REFERENCE | Reuse Landing Zone, IAM, network, observability, FinOps/GreenOps patterns |
| OpenShift platform patterns | `openshift-platform-blueprints` | REFERENCE | Platform engineering source |
| Governed deterministic decisioning analogue | `mayabank-ibm-odm-ai-decision-architecture` | REFERENCE | Strong enterprise policy/ML/GenAI/HITL pattern |
| Product/company umbrella | `Maya` | REFERENCE | Context only until distinct executable need exists |
| Maya GitOps | `Maya-gitops` | DEFER / ADAPT | Use when concrete Maya workloads are ready |
| Enterprise AI platform empty repo | `maya-interlink-enterprise-ai-platform` | IGNORE | Do not create duplicate architecture |
| IG connectivity | official IG REST/Streaming docs + thin adapter | INTEGRATE | `trading-ig` is convenience/reference, not authority |
| Backtesting/replay architecture | NautilusTrader + selected internal code | REFERENCE / ADAPT | Evaluate before building a large custom engine |
| Independent backtest reference | QuantConnect LEAN | REFERENCE | Useful comparison, not mandatory runtime dependency |
| Agent orchestration | LangGraph candidate | ADAPT | Real framework only after ADR/POC |
| Azure-oriented agent alternative | Microsoft Agent Framework | REFERENCE | Evaluate, do not dual-stack by default |
| MCP protocol | official MCP specs/SDK/reference servers | REFERENCE | Production security is our responsibility |
| Vector store | Qdrant | REUSE | Already in TradeOps baseline |
| MLOps registry/tracking | MLflow | INTEGRATE | Central model/evaluation evidence |
| Feature store | Feast | DEFER | Requirement-driven only |
| Local LLM | Ollama | REUSE | Local development |
| Enterprise model serving | OpenShift AI + KServe + vLLM | TARGET | Version-pin against supported platform matrix |
| Observability | OpenTelemetry + Prometheus + Grafana | INTEGRATE | Replace placeholder OTel hook with actual traces |
| AI eval UI | Phoenix | OPTIONAL | ELv2 license review first |
| GitOps | Argo CD + Kustomize/Helm | INTEGRATE | Complete packaging required |
| Policy-as-code | Kyverno | INTEGRATE | Pin current supported APIs |

## Decision rules

### REUSE

Use the asset substantially as-is because it already matches the target need and has acceptable quality/evidence.

### ADAPT

Reuse structure or code but change it materially to satisfy target NFRs, security, architecture or evidence requirements.

### REFERENCE

Use concepts, contracts or examples without creating runtime coupling.

### REPLACE

The current asset is demonstrative or structurally wrong for the target and should not survive as the target implementation.

### DEPRECATE

Stop investing in the asset after its useful content has been migrated or linked.

### IGNORE

No current value or creates duplication risk.

## Mandatory provenance

Any copied/adapted public code must record:

- upstream repository and commit/tag;
- original license;
- files/components actually reused;
- local modifications;
- dependency/security review status.

Prefer dependency/API integration over source copying whenever possible.
