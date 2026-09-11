# ML, Risk and Observability Architecture

## ML problem framing

The first ML objective is not “predict the market”. It is to improve measurable decision quality for precisely defined outcomes.

Candidate targets:

- rank candidate setups;
- classify regime or anomaly state;
- estimate `TP-before-SL` for a fixed horizon and execution assumption;
- predict expected adverse/favorable excursion buckets;
- estimate signal quality conditional on pattern/regime/session.

A target must be defined before training and must include a no-lookahead labelling rule.

## Feature groups

- RSI/MACD/ATR/ADX and EMA slope;
- VWAP distance;
- volatility/volume;
- market structure and pattern type;
- relative strength;
- distance to session/previous-day/weekly levels;
- time-of-day/session;
- VIX/DXY/yields/breadth when source quality allows it;
- macro-event distance;
- spread, latency and data-quality status.

## Training lifecycle

```text
Feature contract
 -> point-in-time dataset
 -> train/validation/test
 -> walk-forward
 -> calibration
 -> MLflow experiment + model registry
 -> serving
 -> outcome collection
 -> drift/performance monitoring
```

Baselines come first: logistic regression or simple tree models, then XGBoost/LightGBM if they materially improve out-of-sample results.

Feast is optional. Introduce it only if the architecture needs consistent online/offline features and the simpler dataset/versioning approach has become insufficient.

## Probability discipline

A raw classifier score is `ml_score`. It becomes a probability only after calibration is measured on data not used to fit the model. Record calibration method, reliability metrics/plots and the exact outcome definition.

## Backtest validity controls

- no future leakage;
- timestamp-aligned external/macro data;
- spread/slippage/cost assumptions;
- market-open/closed rules;
- walk-forward rather than one static split for time-series claims;
- per-regime/session/timeframe/pattern metrics;
- sensitivity to parameter changes;
- reproducible dataset and config hashes.

## Deterministic Risk Gate

The risk gate is independent from LLM/agent output.

Minimum inputs:

```yaml
instrument: string
direction: LONG|SHORT
entry: decimal
stop: decimal
targets: [decimal]
quantity: decimal
account_equity: decimal
portfolio_exposure: object
correlations: object
volatility: object
spread: decimal
slippage_assumption: decimal
data_freshness_ms: number
market_status: string
macro_event_state: string
signal_quality: object
```

Minimum policy families:

- max risk per trade;
- max daily loss;
- portfolio gross/net exposure;
- concentration and correlated exposure;
- volatility limit/adaptive sizing;
- event-risk restriction;
- spread/slippage ceiling;
- stale-data veto;
- market-status veto;
- drawdown/circuit breaker.

Output:

```yaml
status: ACCEPT|VETO|REVIEW
reasons: []
policy_version: string
calculated_risk: object
correlation_id: string
```

## Observability

The current executable trading repository only has a placeholder OpenTelemetry hook, so end-to-end tracing is a target gap rather than an achieved capability.

Target trace chain:

`market-event -> quality -> features -> patterns -> regime -> ML inference -> agent -> RAG/MCP -> fusion -> risk -> HITL -> paper outcome`

### Technical metrics

- ingest and end-to-end latency;
- reconnects/feed failures;
- dropped/out-of-order events;
- queue lag;
- service errors;
- model inference latency;
- MCP latency/errors;
- LLM latency/tokens/cost;
- resource CPU/RAM/GPU and saturation.

### Decision-quality metrics

- stale-data veto count;
- pattern frequency/outcome;
- score calibration/error;
- decision distribution LONG/SHORT/NO TRADE;
- risk veto reasons;
- human override rate/reasons;
- paper/shadow outcomes and expectancy;
- drift by regime/session.

### Tooling baseline

- OpenTelemetry instrumentation + Collector;
- Prometheus/Grafana for platform/business metrics;
- MLflow for ML experiment/model lifecycle;
- Phoenix can be evaluated for agent/LLM observability but its current Elastic License 2.0 requires an explicit licensing decision before making it a baseline dependency.

## Security integration

- OIDC and RBAC;
- least-privilege service accounts;
- Vault/External Secrets or platform-approved secret management;
- NetworkPolicy and controlled egress;
- mTLS where justified;
- request/tool validation;
- prompt-injection and data-exfiltration controls;
- image signing/scanning and SBOM;
- dependency pinning;
- Kyverno or equivalent policy-as-code;
- audit log integrity and PII/secret redaction.
