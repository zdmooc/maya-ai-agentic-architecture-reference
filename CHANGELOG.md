# Changelog

## 2026-09-11 — Iteration 2

### Implemented in `TradeOps-GenAI-Integration`

- canonical validated OHLCV `Bar` model;
- deterministic M1/M5/M15/M30/H1/H4/D1 aggregation and resampling;
- conversion of I1 historical `MarketEvent` BAR data while preserving OHLCV;
- EMA, VWAP, ATR, ADX/+DI/-DI, RSI, MACD and Bollinger implementations in transparent pure Python;
- confirmed swing-high/swing-low detection and HH/HL/LH/LL labels;
- BULLISH / BEARISH / RANGE / UNKNOWN structure classification;
- deterministic breakout/retest, failed breakout, pullback, support/resistance rejection, compression/expansion, gap and liquidity-sweep rules;
- explicit timeframe, preconditions, invalidation level/rule, lookback and machine-readable evidence on every emitted pattern;
- JSON Schema for `PatternSignal`;
- labelled replay fixtures and CLI demonstration;
- dedicated I2 test suite.

### Evidence

- functional runtime commit: `4979abb4b53047364c1a661308e551603dd5552b`;
- lint correction commit / final I2 runtime HEAD: `5c0a77cfd70f620ec6eb867472181632ced6777e`;
- first CI correctly rejected three ambiguous variable names (Ruff E741); no rule was disabled;
- dedicated I2 local tests after correction: 11 passed;
- GitHub Actions run `34643453395`: SUCCESS;
- final full runtime CI: Ruff clean, 30 tests passed with 3 non-blocking pre-existing deprecation warnings;
- labelled examples deterministically matched `BREAKOUT_RETEST/LONG` and `FAILED_BREAKOUT/SHORT`.

### Explicit non-claims

- I2 does not implement market-regime classification or the target risk gate; those belong to I3;
- I2 does not prove profitability, expectancy, drawdown or walk-forward performance; those belong to I4;
- no calibrated ML probability is produced;
- no LLM/agent is used to calculate indicators or detect these deterministic patterns;
- live-money execution remains out of scope.

## 2026-09-11 — Iteration 1

### Implemented in `TradeOps-GenAI-Integration`

- canonical `MarketEvent` model with UTC event/ingest timestamps, source, bid/ask/last, spread, status, latency and staleness fields;
- IG REST adapter for v2 session authentication and v3 historical prices;
- IG Lightstreamer adapter using modern `PRICE:{account}:{epic}` subscriptions and the `Pricing` data adapter;
- data-quality engine for stale, duplicate, out-of-order, future timestamp, missing-price and invalid-spread conditions;
- deterministic clock and JSONL replay engine;
- canonical JSON Schema and versioned replay fixture;
- dedicated I1 tests, replay demo and configuration documentation;
- `lightstreamer-client-lib==2.2.3` added to runtime dependencies.

### Evidence

- runtime commit: `38a4f9637da31e8b96f0de8444a59c29a33bc9f3`;
- local I1 tests: 5 passed;
- replay fixture: 2 accepted / 0 rejected;
- GitHub Actions run `34642186132`: SUCCESS;
- full runtime CI: Ruff clean, 19 tests passed with 3 non-blocking deprecation warnings.

### Explicit non-claims

- actual IG Demo authentication and live Lightstreamer streaming remain pending until credentials/network evidence is captured;
- no real-world latency measurement is claimed;
- no technical indicator, pattern engine, ML probability, profitability or real-money execution is claimed by I1.

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
