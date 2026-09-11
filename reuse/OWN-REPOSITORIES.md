# Own Repository Audit

Audit date: **2026-09-11**.

Decision vocabulary: `REUSE`, `ADAPT`, `REFERENCE`, `REPLACE`, `DEPRECATE`, `IGNORE`.

| Repository | Capability | Current maturity observed | Reusable assets | Problems / limits | Decision | Target / action |
|---|---|---|---|---|---|---|
| `maya-ai-agentic-architecture-reference` | Architecture portfolio hub | Empty before I0 | Repository identity | No content before this iteration | REUSE | Make it the single architecture/reuse/evidence index |
| `TradeOps-GenAI-Integration` | Executable trading integration | Real service/config/test structure; demo-grade quantitative logic | event services, workflow API, RAG/Qdrant, MCP-like tool registry, audit, paper OMS, Redpanda/Postgres, Prometheus/Grafana, Helm/GitOps skeleton | signal logic arbitrary demo; risk very limited; OpenTelemetry placeholder; agent graph hand-written “LangGraph-style”; no serious pattern/regime/backtest/ML calibration; incomplete full-stack OpenShift packaging | **ADAPT** | Primary implementation baseline. Keep integration spine; replace/strengthen quantitative/risk/agent/observability layers |
| `Maya` | Product/AI/trading umbrella | Documentation only in current tree | local-first principles, code-vs-GitOps separation | target structure is aspirational; no executable implementation | REFERENCE | Keep as corporate/product context only; do not build a competing trading runtime |
| `Maya-gitops` | Maya OpenShift GitOps | README + CRC documentation; target tree largely aspirational | GitOps principles, CRC separation, external Ollama pattern | no mature Argo/Kustomize baseline yet | REFERENCE / ADAPT later | Use only when a concrete Maya workload needs deployment; do not duplicate TradeOps packaging |
| `openshift2026-openshift-local-trading-gateway` | Trading platform lab on CRC | Concrete manifests, Kustomize, Redpanda/Postgres, optional Keycloak, trading microservices/scripts | namespaces/quotas, Kustomize deployment patterns, CRC bootstrap/build/push/deploy workflow, platform ownership pattern | lab-grade; separate trading implementation could duplicate TradeOps | **ADAPT** | Harvest OpenShift/CRC deployment patterns into the primary implementation; avoid merging whole repo |
| `mayabank-kafka-ddd-openshift` | Enterprise EDA/Kafka/DDD architecture | Architecture/audit baseline established; implementation journey ongoing | DDD/Event Storming, event contracts, Kafka-vs-alternatives reasoning, OpenShift enterprise framing | banking-specific and not trading runtime | **REFERENCE** | Use for EDA governance and enterprise transposability; no code copy unless asset has clear benefit |
| `mayabank-azure-cloud-ai-platform` | Azure Solution Architecture | Broad architecture complete at design level; selected Terraform labs; unexecuted expensive labs explicitly marked | Landing Zone, Entra, network, AKS/APIM, observability, HA/DR, FinOps/GreenOps, Foundry, migration framing | not all Azure labs executed; targets AKS more than ARO in parts | **REFERENCE / REUSE docs** | Reuse Azure architecture decisions and adapt ARO/OpenShift target; preserve evidence status |
| `openshift-platform-blueprints` | OpenShift/platform engineering reference | Large documentation/blueprint repository | GitOps, security, observability, platform engineering, multi-cluster concepts | broad consolidation repo, not an application | REFERENCE | Reuse platform patterns by link/selected assets only |
| `mayabank-ibm-odm-ai-decision-architecture` | Governed enterprise decisioning | Rich architecture; documented CRC validation evidence | deterministic policy-vs-ML-vs-GenAI separation, governed MCP, HITL, decision audit pattern | insurance/ODM-specific; proprietary ODM runtime not public | **REFERENCE** | Strong enterprise analogue for deterministic Risk Gate / governed agents |
| `maya-interlink-enterprise-ai-platform` | Enterprise AI platform | Empty | none currently | duplicate risk, no assets | **IGNORE for now** | Do not populate until a distinct capability exists that does not belong here or elsewhere |

## Detailed finding: TradeOps-GenAI-Integration

### REUSE

- service decomposition and event-driven integration skeleton;
- PostgreSQL workflow/audit concepts;
- Qdrant/RAG service boundary;
- paper-order path;
- correlation IDs/audit intent;
- Redpanda local event bus concept;
- Prometheus/Grafana baseline;
- scripts/evidence structure;
- existing tests as regression seed.

### ADAPT

- agent controller: retain state-machine intent but implement a real selected agent framework if claimed;
- MCP facade: move from local registry/HTTP-dispatch demo toward standards-compliant, authenticated MCP boundaries;
- Helm/GitOps: package the complete runnable slice and add security/resources/policies;
- RAG: add versioned citations, policy corpus governance and evaluation.

### REPLACE

- demo signal algorithm based on fractional price;
- demo confidence arithmetic presented as decision confidence;
- simplistic risk implementation as the target risk engine.

### GAPS

- actual IG live/demo connectivity and Lightstreamer lifecycle;
- canonical market model and data-quality engine;
- replay and deterministic clock;
- multi-timeframe bar aggregation contract;
- tested technical/pattern/regime engines;
- serious backtesting/out-of-sample/walk-forward;
- ML feature pipeline, registry and calibration;
- disagreement-aware multi-agent fusion;
- standards-aligned secure MCP;
- end-to-end OpenTelemetry;
- complete OpenShift/GitOps deployment and runtime evidence;
- 100+ paper/shadow decision evidence set.

## Duplication rules

1. One executable trading baseline: **TradeOps-GenAI-Integration** unless an ADR later replaces it.
2. One central architecture index: **this repository**.
3. `Maya` remains product/company context, not another trading engine.
4. `openshift2026-openshift-local-trading-gateway` supplies deployment/platform patterns rather than a second long-lived business implementation.
5. Specialist repositories remain authoritative for their specialist architecture (Azure, Kafka/DDD, OpenShift platform, ODM decisioning).
