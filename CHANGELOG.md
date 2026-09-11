# Changelog

## 2026-09-11 — Iteration 0

### Added

- master charter and architecture principles;
- architecture vision and capability map;
- target real-time trading / agentic AI architecture;
- deterministic / ML / LLM separation;
- agent roles and secure MCP boundary;
- ML, deterministic risk and observability architecture;
- trading signal/backtesting contracts;
- personal-repository audit and reuse decisions;
- public-project audit with current licensing caveats;
- reuse catalog and machine-readable source map;
- enterprise transposability mapping;
- roadmap from data/replay to Excellence;
- Iteration 0 evidence and explicit non-claims.

### Key decisions

- `TradeOps-GenAI-Integration` is the primary executable trading baseline and will be adapted rather than duplicated.
- `maya-ai-agentic-architecture-reference` remains an architecture/reuse/evidence hub, not a second runtime.
- current TradeOps demo signal/risk/confidence logic is not accepted as target quantitative/risk capability.
- OpenTelemetry, secure MCP, replay/backtesting, pattern/regime engines and calibrated ML are explicit future gaps.
- Redpanda remains useful for local labs but is license-aware; the architecture contract remains Kafka-compatible.
- automated real-money execution remains outside the initial program scope.
