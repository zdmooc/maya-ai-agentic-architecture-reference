# Iteration 3 Evidence — Market Regime and Deterministic Risk v1

Date: 2026-09-11

## Status

**IMPLEMENTED + TESTED. CI GREEN.**

Iteration 3 is implemented in the executable runtime repository
`zdmooc/TradeOps-GenAI-Integration`. This master repository records architecture status and
verifiable evidence; it does not duplicate runtime code.

Functional runtime commit:

`6e0768321f73c99dc6997a5963f727ed7aa99825`

Lint correction / final I3 runtime HEAD:

`bd5edfd32f894995233658aac27616f4a120d6dc`

Final GitHub Actions run:

`34644295181` — job `lint-test` — **SUCCESS**

## Runtime delta

Compared with final I2 HEAD, I3 changes 14 files across:

- `services/market_regime/`;
- `services/risk_engine/`;
- event schemas;
- risk scenarios;
- documentation;
- CLI demonstration;
- dedicated tests.

The existing `risk_engine/worker.py` placeholder using fixed `qty=100` and `MAX_QTY` was
replaced by a fail-closed adapter around the deterministic I3 policy engine.

## Market-regime engine

`services/market_regime/engine.py`

The classifier consumes the I2 `TechnicalAnalysis` contract plus explicit market context. It
emits one deterministic `RegimeSnapshot` with machine-readable evidence and an allowlist.

Supported regimes:

- `TREND_UP`;
- `TREND_DOWN`;
- `RANGE`;
- `HIGH_VOLATILITY`;
- `LOW_VOLATILITY`;
- `BREAKOUT`;
- `POST_EVENT`;
- `RISK_ON`;
- `RISK_OFF`;
- `UNKNOWN` as the fail-closed fallback.

Deterministic precedence:

1. post-event window;
2. explicit `RISK_ON` / `RISK_OFF` context;
3. breakout evidence from I2 patterns;
4. ATR-based high/low volatility;
5. structure + ADX trend;
6. range;
7. unknown.

No LLM is involved. The classifier exposes evidence rather than an invented probabilistic
confidence value.

## Strategy allowlists

Each regime maps to an explicit allowlist. Examples:

- trend regimes allow trend-following / pullback / breakout families;
- range allows mean-reversion and support/resistance families;
- post-event and unknown regimes allow no strategy by default.

These lists are configurable policy examples. They are not profitability claims.

## Risk contracts

`services/risk_engine/models.py`

I3 introduces validated immutable contracts:

- `TradeIntent` — instrument, LONG/SHORT, strategy, entry, stop, quantity, point value;
- `RiskState` — equity, P&L, exposures, spread, slippage, freshness, ATR%, event flag and
  circuit-breaker inputs;
- `RiskLimits` — deterministic configurable thresholds;
- `RiskDecision` — approved/vetoed status, regime, ordered veto reasons, circuit-breaker state
  and computed metrics.

LONG/SHORT stop invariants are validated before risk evaluation.

## Deterministic risk gate

`services/risk_engine/policy.py`

The engine evaluates:

- risk per trade as stop distance × quantity × point value divided by equity;
- current daily loss;
- gross exposure after the proposed trade;
- instrument concentration after the proposed trade;
- correlated exposure after the proposed trade;
- ATR volatility percentage;
- event blackout;
- spread;
- estimated slippage;
- market-data age;
- regime strategy allowlist;
- unknown-regime fallback.

Exposure-after-trade calculations are deliberately conservative: absolute proposed notional is
added to existing exposure. I3 does not silently assume hedge/netting benefits.

## Explicit veto reasons

I3 can emit:

- `KILL_SWITCH_ACTIVE`;
- `FEED_DEGRADED`;
- `DAILY_LOSS_LIMIT`;
- `MAX_CONSECUTIVE_LOSSES`;
- `RISK_PER_TRADE_LIMIT`;
- `GROSS_EXPOSURE_LIMIT`;
- `CONCENTRATION_LIMIT`;
- `CORRELATION_LIMIT`;
- `VOLATILITY_LIMIT`;
- `EVENT_WINDOW_BLOCKED`;
- `SPREAD_LIMIT`;
- `SLIPPAGE_LIMIT`;
- `STALE_MARKET_DATA`;
- `UNKNOWN_REGIME`;
- `STRATEGY_NOT_ALLOWED_IN_REGIME`.

All triggered reasons are returned together in deterministic order. The hard circuit-breaker flag
is activated for kill switch, degraded feed, daily loss and maximum consecutive losses.

## Fail-closed event adaptation

`services/risk_engine/adapter.py`

The adapter requires:

- `risk_intent`;
- `risk_state`;
- `regime`.

Missing or invalid structured context is rejected instead of being filled with optimistic default
risk assumptions. The Kafka worker emits `I3_CONTEXT_INVALID` for those legacy/incomplete input
events.

This means the pre-existing arbitrary demo `signal_engine` cannot accidentally bypass I3 simply
because it publishes `signals.generated`.

## Schemas and scenarios

Versioned schemas:

- `schemas/events/market.regime.schema.json`;
- `schemas/events/risk.decision.schema.json`.

Versioned scenarios:

`data/replay/i3_risk_scenarios.json`

They include:

- an approved `TREND_UP` / `PULLBACK` example;
- a vetoed example with stale market data and excessive spread.

The CLI demonstration is `python scripts/demo_risk_gate.py`.

## Test evidence

Dedicated I3 tests cover 22 cases, including parameterized negative gates.

Final repository CI:

```text
ruff check .
All checks passed!

pytest -q
.................................................... [100%]
52 passed, 3 warnings in 1.81s
```

The three warnings are pre-existing Starlette/FastAPI deprecation warnings and are not caused by
I3.

The first CI run `34644207171` correctly failed before Pytest on 10 Ruff packaging/import issues.
Those imports were corrected in commit `bd5edfd32f894995233658aac27616f4a120d6dc` without
disabling any lint rule. Run `34644295181` then passed Ruff and the entire 52-test repository.

## Explicit non-claims

Iteration 3 does **not** claim:

- profitability or positive expectancy;
- optimal strategy allowlists;
- portfolio VaR/CVaR;
- portfolio optimization or realistic cross-asset hedge/netting;
- calibrated ML probabilities;
- transaction-cost-calibrated backtesting;
- out-of-sample or walk-forward performance;
- real-money autonomous execution.

Those performance and experiment-discipline claims require I4 and later evidence.

## Exit decision

I3 exit criterion was negative tests proving unsafe signals are vetoed. That criterion is met:
all dedicated tests and the complete runtime suite pass, risk vetoes are explicit and the event
adapter fails closed on incomplete context.

**Iteration 3 is complete. Do not infer I4 completion from this evidence.**
