# Architecture Vision

## Business problem

Real-time decision systems fail when they mix uncertain AI output, stale data, hidden risk rules and opaque execution in one component. The reference architecture separates acquisition, deterministic computation, ML estimation, agentic reasoning, risk policy and human approval so every decision can be traced and challenged.

## Primary scenario

A user wants a high-quality LONG / SHORT / NO TRADE recommendation for an instrument using live market data, technical structure, pattern context, macro context and measured historical evidence. The architecture must remain safe when feeds disagree, data is stale, a model is uncertain, an MCP tool fails or an agent hallucinates.

## Stakeholders

- trader / analyst;
- risk owner;
- platform/SRE team;
- AI/ML engineering;
- security/IAM;
- enterprise architect / Architecture Review Board;
- compliance/audit;
- FinOps/GreenOps.

## Architecture qualities

Priority NFRs:

1. correctness and data freshness before model sophistication;
2. deterministic risk veto;
3. traceability and auditability;
4. reproducibility of replay/backtesting;
5. graceful degradation when sources/tools/models fail;
6. security and least privilege;
7. latency measured by stage rather than hidden in a monolith;
8. portability between local/OpenShift/Azure targets;
9. cost and resource visibility;
10. explainability of evidence and trade-offs.

## Capability map

```text
Market Connectivity
├─ REST / Streaming adapters
├─ Authentication / session lifecycle
└─ Multi-source normalization

Real-Time Data
├─ Data Quality
├─ Canonical Market Model
├─ Event Streaming
├─ Replay
└─ Multi-timeframe aggregation

Quantitative Intelligence
├─ Technical Engine
├─ Pattern Engine
├─ Regime Engine
├─ Feature Pipeline
└─ Backtesting

ML / MLOps
├─ Training and validation
├─ Calibration
├─ Registry
├─ Serving
└─ Drift/performance monitoring

Agentic AI
├─ RAG
├─ Specialized agents
├─ MCP tools
├─ Fusion / disagreement handling
└─ Human-in-the-Loop

Governance
├─ Deterministic Risk Gate
├─ Security / IAM
├─ Audit
├─ Policy-as-Code
└─ Model/tool governance

Platform
├─ OpenShift / ARO
├─ GitOps
├─ Observability / SRE
├─ Azure integration
└─ FinOps / GreenOps
```

## Explicit non-goals for the first phase

- HFT or microsecond latency;
- autonomous real-money order execution;
- claims of profitability without repeatable data;
- LLM-generated market prices or indicator calculations;
- a single opaque agent making every decision;
- copying whole external repositories into the portfolio.

## Success criterion

The portfolio is successful when an Architecture Board can inspect one recommendation end-to-end—from raw source and data-quality status through quantitative evidence, ML version, agent/tool calls, risk result and human decision—and when the same architectural patterns can be explained for a bank or insurer without relying on trading-specific terminology.
