# Agentic AI and MCP Architecture

Status: **REFERENCE ARCHITECTURE — RUNTIME EVIDENCE REUSED FROM `TradeOps-GenAI-Integration`**

## Current-state finding

`TradeOps-GenAI-Integration` is now an executable Agentic AI baseline rather than only a behavioral prototype.

The current runtime includes:

- real LangGraph `StateGraph` orchestration pinned to `langgraph==1.2.11`;
- specialized Market, Technical, Pattern, Macro, Risk and Fusion agents;
- governed RAG and a versioned knowledge corpus;
- explicit conflict, stale-data and deterministic risk-veto states;
- persisted Human-in-the-Loop review/execution lifecycle;
- governed tool calls with authentication, scopes, allowlists, input validation, rate limits, timeouts, audit correlation and redaction;
- OpenTelemetry/Prometheus observability and OpenShift/CRC deployment evidence.

The current tool service is deliberately described as an **MCP-shaped governed compatibility boundary**, not as native MCP protocol conformance. It exposes governed HTTP tool operations and reuses the security semantics expected around MCP, but the official MCP SDK/protocol transport is not yet part of the executable baseline. Native MCP conformance therefore remains a targeted implementation gap rather than an already-proven capability.

The confidence/evidence model must still distinguish heuristic scores from calibrated probabilities. No agent score is presented as calibrated probability unless qualification evidence exists.

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
status: OK|UNKNOWN|DATA_STALE|CONFLICT|ERROR|VETO
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
autonomy_level: L0|L1|L2|L3|L4
human_approval_required: boolean
```

Autonomy policy is defined in `enterprise/AGENT-AUTONOMY-HITL-MODEL.md`.

## Orchestration choice

### Baseline: LangGraph

The executable baseline now uses the real LangGraph framework for explicit state and controlled orchestration. Durable production workflows, checkpoint persistence and advanced branching remain subject to use-case-specific ADRs and runtime evidence.

### Alternative: Microsoft Agent Framework

Evaluate as an enterprise/Microsoft ecosystem alternative, especially when Azure/Foundry integration and .NET/Python interoperability matter. Do not introduce two agent frameworks into the executable baseline without a demonstrated need.

## MCP target architecture

```text
User / Service identity
        |
        v
API / AI Gateway
        |
        v
Agent Runtime / MCP Client
        |
        v
MCP Gateway / policy enforcement
        |
   +----+------------------+
   |         |             |
   v         v             v
MCP Server  MCP Server    MCP Server
OpenShift   Payments/MQ   Knowledge/CMDB
   |         |             |
   +---------+-------------+
             |
             v
      Enterprise systems
```

Native MCP implementation must preserve the security boundary already proven by the governed tool service. Protocol adoption must not weaken authorization or introduce a generic privileged execution channel.

## MCP domains

### MCP-Platform / OpenShift

Initial read-only capabilities:

- `get_pods`
- `get_deployment_status`
- `get_logs`
- `get_metrics`
- `get_events`

Sensitive operations such as `restart_deployment` require explicit policy and HITL.

### MCP-Payments / IBM MQ

- `get_queue_depth`
- `get_channel_status`
- `get_dlq_summary`
- `get_payment_status`
- `get_processing_health`

Mutation/replay/remediation operations are separate tools with stronger scopes and approval requirements.

### MCP-Knowledge / CMDB

- `search_runbook`
- `get_architecture_document`
- `get_application`
- `get_dependencies`
- `get_owner`

### Existing market/trading domains

The reusable executable baseline also contains market-oriented tool domains such as price/market data, macro evidence, trading history and backtest lookup. These remain domain-specific examples rather than the target enterprise mission itself.

## MCP security controls

Every tool must have:

- authenticated caller identity;
- end-to-end identity/claim propagation or explicit workload delegation;
- scoped authorization;
- explicit allowlist;
- typed input schema and bounds;
- output schema and redaction;
- timeout and cancellation;
- rate limit and budget limit where applicable;
- correlation/trace ID;
- immutable/auditable call record;
- network egress restrictions;
- autonomy-level classification;
- HITL for sensitive actions.

Identity propagation is detailed in `enterprise/IDENTITY-PROPAGATION-MCP-IAM.md`.

Never expose arbitrary shell execution, unrestricted SQL, unrestricted Kubernetes mutation, secret-store browsing or payment execution to a general-purpose agent.

## Human approval boundary

A human approval decision is an authorization event, not merely a boolean supplied by the LLM.

For sensitive actions the expected chain is:

```text
Agent recommendation
 -> deterministic policy evaluation
 -> approval request
 -> authenticated reviewer decision
 -> short-lived execution authorization
 -> MCP tool call
 -> audit/evidence
```

The agent cannot self-promote its autonomy level, mint reviewer identity or waive required approval.

## RAG architecture

Use RAG for governed evidence retrieval—not as a substitute for Systems of Record.

Candidate corpora:

- risk and security policies;
- payment-platform architecture;
- runbooks and operating procedures;
- ADRs and technical standards;
- CMDB/service metadata snapshots where appropriate;
- postmortems;
- model cards and evaluation reports;
- strategy specifications and prior evidence in domain-specific demonstrations.

Every answer used in a decision must preserve document IDs/versions and retrieval citations. Entitlement filtering must occur before unauthorized content enters model context.

## Failure behavior

- RAG unavailable -> continue only with capabilities that do not require it and mark context incomplete;
- MCP tool unavailable -> `ERROR/UNKNOWN`, never invented output;
- missing/expired identity -> fail closed;
- authorization ambiguity -> deny;
- stale operational data -> `DATA_STALE` and block sensitive remediation;
- conflicting evidence -> `CONFLICT` and deterministic escalation policy;
- risk/security veto -> terminal `VETO` regardless of agent confidence;
- approval service unavailable -> no sensitive execution.

## Evidence and claim discipline

Current executable evidence may be reused from `TradeOps-GenAI-Integration` for real LangGraph orchestration, governed RAG, HITL, security controls, observability and OpenShift deployment.

Do not claim until separately evidenced:

- native MCP protocol conformance/Streamable HTTP deployment;
- production enterprise IAM federation;
- payment/OpenShift MCP servers executing against production systems;
- unrestricted autonomous remediation;
- production-scale RAG corpus or GPU platform performance.

## MCP + A2A interoperability boundary

D-092 adds a distinct inter-agent boundary:

```text
Agent -> MCP -> tools/data/systems
Agent -> A2A -> independent agent
```

MCP remains the governed tool/resource integration protocol. A2A covers discovery and task/message/artifact exchange between independent agents.

The detailed architecture is maintained in:
`architecture/AGENTIC-INTEROPERABILITY-MCP-A2A.md`.

Current reference baselines on 2026-10-04:
- MCP specification: `2026-07-28`;
- A2A latest released version observed: `1.0.0`.

A2A adoption must preserve workload identity, peer allowlists, delegation controls, data classification, max delegation depth, time/token/cost budgets, cancellation, audit and fail-closed semantics.

**A2A_RUNTIME_INTEROPERABILITY remains NOT_PROVEN.**

