# Agentic AI and MCP Architecture

## Current-state finding

`TradeOps-GenAI-Integration` contains a useful agent-controller concept, RAG calls, MCP-like tool dispatch, confidence gating, audit and paper-order flow. The current graph is explicitly a **LangGraph-style** sequential Python state machine implemented without the LangGraph dependency. This is reusable as a behavioral prototype, not evidence of a production agent framework.

The current confidence formula is heuristic. It must not be represented as a calibrated probability.

## Target agent roles

Do not create one agent per indicator. Indicators remain deterministic functions.

### Data Quality Agent

Consumes deterministic feed-quality evidence and explains missing/stale/conflicting sources. It cannot redefine freshness thresholds.

### Market Agent

Synthesizes session, liquidity, spread and cross-source market context.

### Technical Agent

Explains deterministic indicator and market-structure outputs.

### Pattern Agent

Explains which formally tested patterns are active, invalid or conflicting.

### Macro Agent

Adds scheduled-event and cross-asset context with source/evidence attribution.

### Risk Agent

Explains risk-engine results and policy evidence. It has no ability to override a deterministic veto.

### Fusion / Decision Agent

Combines evidence with explicit weights/decision rules based on data quality, regime, calibrated ML evidence and historical expectancy. It is not a majority-vote agent.

## Agent output contract

Every agent output should include:

```yaml
agent: string
status: OK|UNKNOWN|DATA_STALE|CONFLICT|ERROR
conclusion: string
confidence_type: heuristic|calibrated|none
confidence: number|null
evidence:
  - source: string
    ref: string
    freshness_ms: number|null
assumptions: []
conflicts: []
correlation_id: string
```

## Orchestration choice

### Baseline candidate: LangGraph

Use for explicit state, durable workflows, checkpoints and controlled branching after an ADR and small proof of concept. The implementation must use the real framework if the repository claims LangGraph.

### Alternative: Microsoft Agent Framework

Evaluate as an enterprise/Microsoft ecosystem alternative, especially when Azure/Foundry integration and .NET/Python interoperability matter. Do not introduce two agent frameworks into the executable baseline without a demonstrated need.

## MCP domains

### MCP-IG / Market Connectivity

Read-only in initial phases:

- `get_price`
- `get_candles`
- `get_spread`
- `get_market_status`

### MCP-MarketData

- `get_vix`
- `get_dxy`
- `get_us10y`
- `get_breadth`

### MCP-Macro

- `get_calendar`
- `get_event`
- `get_consensus`

### MCP-TradingDB

- `save_signal`
- `get_signal_history`
- `get_similar_setups`
- `get_statistics`

### MCP-Backtest

- `run_backtest`
- `get_backtest_result`

## MCP security controls

Every tool has:

- authenticated caller identity;
- scoped authorization;
- explicit allowlist;
- typed input schema and bounds;
- output schema and redaction;
- timeout and cancellation;
- rate limit;
- correlation ID;
- immutable/auditable call record;
- network egress restrictions;
- HITL for sensitive actions.

Never expose arbitrary shell execution, unrestricted SQL, deployment mutation or real-money order placement to a general-purpose agent.

## Paper-order boundary

If `oms.place_order` exists during development, it is explicitly named and enforced as paper/simulated. A later live connector requires a separate namespace/tool identity, policy set and ADR; it must not be enabled by changing a configuration flag on the same unrestricted tool.

## RAG architecture

Use RAG for evidence retrieval—not for market-price truth. Candidate corpora:

- risk policies;
- strategy specifications;
- pattern definitions;
- ADRs and runbooks;
- prior signal/trade evidence;
- postmortems;
- model cards and evaluation reports.

Every answer used in a decision must preserve document IDs/versions and retrieval citations.

## Failure behavior

- RAG unavailable -> continue only with capabilities that do not require it and mark context incomplete;
- MCP tool unavailable -> ERROR/UNKNOWN, not invented output;
- stale market data -> DATA_STALE and no entry permission;
- conflicting evidence -> CONFLICT and deterministic escalation policy;
- risk veto -> terminal VETO regardless of agent confidence.
