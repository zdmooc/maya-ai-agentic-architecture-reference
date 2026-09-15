# Own Repository Audit

Audit date: **2026-09-15**.

Decision vocabulary: `REUSE`, `ADAPT`, `REFERENCE`, `REPLACE`, `DEPRECATE`, `IGNORE`.

| Repository | Capability | Current maturity observed | Reusable assets | Problems / limits | Decision | Target / action |
|---|---|---|---|---|---|---|
| `maya-ai-agentic-architecture-reference` | Architecture portfolio hub | Mature architecture/knowledge hub; I13-I20 designed; book and portfolio consolidation complete | AI architecture, governance, SAD/NFR/ADR, control/runtime plane, gateway, policy-as-code, evaluation/observability, resilience | runtime proof lives in specialist repos by design | **REUSE / CANONICAL** | Keep as the single architecture/reuse/evidence index |
| `TradeOps-GenAI-Integration` | Executable GenAI/Agentic integration | Real service/config/test/OpenShift structure with RAG/agents/MCP/HITL and CRC evidence | event services, workflow API, RAG/Qdrant, governed MCP boundary, audit, risk gate, HITL, Redpanda/Postgres, observability, UI | domain is trading; some capabilities remain mission-specific | **ADAPT / PRIMARY RUNTIME** | Keep as principal executable AI evidence baseline |
| `Maya` | Product/AI/trading umbrella | Documentation/context | local-first principles, code-vs-GitOps separation | no need for another executable AI runtime | REFERENCE | Keep as corporate/product context only |
| `Maya-gitops` | Maya OpenShift GitOps | Supporting deployment repository | GitOps principles and CRC separation | not AI-specific | REFERENCE / ADAPT later | Use only when a concrete workload needs it |
| `openshift2026-openshift-local-trading-gateway` | Trading platform lab on CRC | Concrete platform/deployment patterns | namespaces/quotas, Kustomize, CRC workflows | lab-grade and overlaps TradeOps platform role | **ADAPT** | Harvest platform patterns; avoid second business runtime |
| `mayabank-kafka-ddd-openshift` | Enterprise EDA/Kafka/DDD architecture | Architecture/audit baseline | DDD/Event Storming, event contracts, Kafka governance | not an AI repository | **REFERENCE** | Use as AI integration/EDA foundation |
| `mayabank-azure-cloud-ai-platform` | Azure Solution Architecture + AI | Broad architecture complete at design level; selected Terraform assets | Landing Zone, Entra, network, AKS/APIM, Foundry/AI Search concepts, observability, HA/DR, FinOps/GreenOps | not all Azure labs executed | **REFERENCE / REUSE docs** | Azure-specific companion to canonical AI hub |
| `openshift-platform-blueprints` | OpenShift/platform engineering reference | Large platform reference | GitOps, security, observability, platform engineering, multi-cluster concepts | broad consolidation repo, not an application | REFERENCE | Reuse platform patterns by link/selected assets only |
| `mayabank-ibm-odm-ai-decision-architecture` | Governed enterprise decisioning | Rich architecture with CRC evidence for portable façade | deterministic policy-vs-ML-vs-GenAI separation, governed MCP, HITL, decision audit | proprietary ODM runtime not public | **REFERENCE / SPECIALIST** | Strong regulated AI/insurance specialist evidence |
| `mayabank-carbon-aware-decision-architecture` | AI/ML + GreenOps decision architecture | Architecture and portable logic implemented through I10 | forecast/anomaly/ranking, deterministic gates, Pareto optimization, human approval | CRC deployment pending | **REFERENCE / SPECIALIST** | Keep as Green AI / GreenOps differentiator |
| `mayabank-pega-ai-case-management-openshift` | Pega/Case Management + governed AI | Architecture/configuration present; licensed runtime not validated | RAG/summarization/recommendation/HITL patterns + OpenShift platform design | Pega entitlement/runtime dependency | **REFERENCE / SPECIALIST** | Keep for Pega/CRM/case-management missions |
| `maya-interlink-enterprise-ai-platform` | Generic Enterprise AI platform plan | **QUEUED / NOT STARTED**; master prompt only | useful AI intent has been absorbed into canonical hub | duplicates hub + runtime/specialist repos; no unique AI implementation | **DEPRECATE** | **Safe to delete from AI portfolio after owner action**. See `MAYA-INTERLINK-AI-CONSOLIDATION.md` |

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

- agent controller and MCP boundary only when a mission requires further standards/runtime proof;
- Helm/GitOps and platform security when new deployment targets are required;
- RAG evaluation and corpus governance as concrete evidence needs evolve.

## AI duplication rules

1. One principal executable GenAI/Agentic baseline: **TradeOps-GenAI-Integration** unless an ADR later replaces it.
2. One central AI architecture index: **maya-ai-agentic-architecture-reference**.
3. `Maya` remains product/company context, not another AI engine.
4. `maya-interlink-enterprise-ai-platform` is deprecated after AI-only consolidation and must not be restarted as a competing generic AI platform.
5. Specialist repositories remain authoritative for their specialist domains (Azure AI, ODM AI Decision, Carbon-Aware AI, Pega AI, Kafka/MQ/API/OpenShift support).
