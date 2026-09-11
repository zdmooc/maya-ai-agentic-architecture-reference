# Trading Architecture

## Scope

Phase 1 produces **analysis + signal + paper/shadow workflow + Human-in-the-Loop**. It does not autonomously execute real money.

## Signal contract

```yaml
signal_id: uuid
instrument: string
direction: LONG|SHORT|NO_TRADE
entry_zone:
  min: decimal|null
  max: decimal|null
invalidation: string
stop: decimal|null
targets: []
risk_reward: number|null
timeframe: string
market_regime: string
pattern: string
ml:
  score: number|null
  probability: number|null
  calibrated: boolean
  model_version: string|null
risk:
  status: ACCEPT|VETO|REVIEW
  reasons: []
data:
  freshness_ms: number
  quality_status: string
evidence: []
decision: ENTRY_ALLOWED|NO_TRADE|HUMAN_REVIEW
correlation_id: string
```

If `calibrated=false`, `probability` must remain null.

## Pattern engine minimum catalogue

- confirmed breakout;
- breakout + retest;
- failed/fake breakout;
- pullback;
- support/resistance rejection;
- compression -> expansion;
- EMA/VWAP reclaim or rejection;
- HH/HL and LH/LL;
- RSI/MACD divergence;
- momentum + volume confirmation;
- opening range breakout;
- previous-day/weekly high-low interaction;
- gap continuation/failure;
- liquidity sweep;
- post-macro reaction.

Every pattern needs a formal definition, required data, invalidation, timeframe, tests, backtest statistics and documented limitations.

## Regime engine

Minimum states:

`TREND_UP`, `TREND_DOWN`, `RANGE`, `HIGH_VOLATILITY`, `LOW_VOLATILITY`, `BREAKOUT`, `POST_EVENT`, `RISK_ON`, `RISK_OFF`.

Strategies and patterns have an explicit regime compatibility matrix. A strong setup in the wrong regime can still be rejected.

## Data source policy

For IG-targeted paper/live simulation:

- IG bid/ask and market state are authoritative for execution assumptions;
- other broker/data feeds are corroborating context;
- macro/VIX/DXY/yields are context/features with explicit timestamps;
- stale or conflicting data is surfaced, not averaged away.

## Decision flow

```text
Data Quality
 -> Deterministic Technical/Pattern/Regime Evidence
 -> Feature Pipeline
 -> ML Score (calibrated only when proven)
 -> Specialized Agent Synthesis
 -> Fusion / Conflict Resolution
 -> Deterministic Risk Gate
 -> Human Review
 -> Paper/Shadow Outcome
 -> Feedback / Evaluation
```

## Backtesting contract

A backtest is acceptable as evidence only if it records:

- dataset/version/time range;
- strategy/pattern config;
- spread/slippage/cost model;
- execution timing convention;
- no-lookahead controls;
- out-of-sample/walk-forward protocol;
- number of trades, win rate, average R, expectancy, profit factor, max drawdown;
- performance by regime/session/timeframe/pattern;
- commit SHA and random seed where applicable.

## Risk precedence

`AI recommendation -> deterministic risk gate -> ACCEPT | VETO | REVIEW`

A VETO is terminal for that decision instance. The only allowed response is to create a new decision with changed factual inputs or policy-authorized human workflow; an agent cannot reinterpret a veto into approval.
