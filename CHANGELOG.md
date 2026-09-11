# Changelog

## 2026-09-11 — Iteration 5

### Implemented in `TradeOps-GenAI-Integration`

- versioned point-in-time feature contract for technical, pattern, structure, regime, spread, latency and data-quality inputs;
- explicit leakage guards for future/outcome/label/PnL/MFE/MAE semantics;
- chronological TRAIN / VALIDATION / CALIBRATION / TEST split with no random shuffle;
- rolling walk-forward windows with independent calibration/test blocks;
- four ML baselines: scikit-learn logistic regression, scikit-learn histogram gradient boosting, XGBoost and LightGBM;
- validation-only champion selection;
- Platt calibration on a dedicated calibration segment;
- untouched TEST metrics including ROC-AUC, Brier, log loss and expected calibration error;
- probability qualification that fails closed to `SCORE_ONLY` when sample, discrimination, calibration or drift gates fail;
- PSI and standardized-mean-shift drift monitoring;
- deterministic synthetic dataset generator/spec and experiment protocol;
- MLflow 3.16 tracking, artifact logging and Model Registry smoke test;
- SQLite local/CI tracking backend and explicit Skops trusted-type allowlist for the two project-owned calibration classes;
- Feast intentionally deferred until a real online/offline feature-consistency requirement appears.

### Evidence

- I5 runtime commit sequence: `2be132fc0659b3669c23013604760da78b45e839`, `16d283f1663830e6427ada1bb5579760f8d6bd1f`, `52492d5d1666dc4f774341886aa5e5542032cabd`, final HEAD `bca514ce35fab3e63ef16e487394fea576523d7b`;
- runtime is 4 commits ahead of I4 and zero behind, with 20 changed files;
- first integration CI exposed MLflow FileStore maintenance-mode rejection; local/CI tracking was migrated to SQLite rather than enabling the FileStore opt-out;
- second integration CI exposed Skops rejection of project custom classes; exactly those two governed classes were explicitly allowlisted;
- final GitHub Actions run `34646841551`: SUCCESS;
- final CI: Ruff clean, 87 tests passed, 69 non-blocking deprecation warnings;
- I5 adds 19 passing tests over the 68-test I4 baseline;
- final CI runs CPython 3.11.16 and successfully installs `xgboost==3.2.0`, `lightgbm==4.7.0`, `mlflow==3.16.0`;
- pinned synthetic champion: `sklearn_logistic`;
- final synthetic TEST set: 72 observations;
- calibrated synthetic TEST ROC-AUC ≈ 0.7407, Brier ≈ 0.2005, log loss ≈ 0.5882, ECE ≈ 0.0937;
- drift status WATCH with maximum PSI ≈ 0.2428;
- qualification status `CALIBRATED_OUT_OF_SAMPLE_SYNTHETIC`.

### Explicit non-claims

- I5 does not establish calibrated probability on real historical or live market data;
- synthetic metrics do not establish trading alpha or profitability;
- no production feature store is claimed;
- the MLflow CI backend is an isolated SQLite validation backend, not a production remote deployment;
- ML cannot override the deterministic I3 risk veto;
- automated real-money execution remains outside scope.

## 2026-09-11 — Iteration 4

### Implemented in `TradeOps-GenAI-Integration`

- deterministic event-driven backtest package;
- next-bar-open execution semantics to prevent same-bar lookahead;
- explicit spread, slippage and per-order commission assumptions;
- conservative `STOP_FIRST` handling for same-bar stop/target ambiguity;
- I3 risk-gate integration: only `risk_status=APPROVED` signals can execute;
- trade-level PnL, R-multiple, MFE/MAE, exit reason and bars-held evidence;
- aggregate win rate, total/average PnL, average R / expectancy R, gross profit/loss, profit factor and maximum drawdown;
- metric breakdowns by regime, session, timeframe and pattern;
- chronological train/test split and rolling walk-forward windows without random shuffle;
- buy-and-hold baseline under the same transaction-cost model;
- versioned synthetic dataset, experiment protocol, result schema, CLI demo and dedicated tests;
- dataset SHA-256 and config SHA-256 embedded in backtest reports.

### Evidence

- runtime commit / final I4 HEAD: `381b7dedf85a2170d8ff59205678bdf4692e5146`;
- I4 is one commit ahead of I3 with 13 files added and no pre-I4 runtime file modified;
- dedicated I4 tests added: 16;
- GitHub Actions run `34645138469`: SUCCESS;
- full runtime CI: Ruff clean, 68 tests passed with 3 non-blocking pre-existing deprecation warnings;
- labelled synthetic fixture executes 4 approved trades, skips 1 I3-vetoed signal and produces 3 TARGET / 1 STOP outcomes;
- synthetic fixture win rate is 75% only as deterministic mechanics evidence;
- tests prove costs reduce performance versus a zero-cost configuration;
- tests prove chronological and walk-forward train intervals end before their test intervals start;
- report output is deterministic for identical dataset and config hashes.

### Reference-engine review

- NautilusTrader remains the primary independent architecture/replay reference. Current documentation recommends `BacktestNode` for config-driven backtesting; the reviewed current release line includes `2.0.0rc4`, so a future comparison must pin an exact tested release.
- QuantConnect LEAN remains the second independent reference and supports event-driven local backtesting; no LEAN run is claimed in I4.

### Explicit non-claims

- the I4 fixture is synthetic and does not establish strategy profitability;
- no real IG historical transaction-cost distribution is used yet;
- no statistically significant out-of-sample alpha is claimed;
- no Sharpe/Sortino figure is emitted from the tiny fixture because that would imply false precision;
- NautilusTrader and LEAN are reviewed references, not executed validation engines in I4;
- no calibrated ML probability is produced;
- automated real-money execution remains outside scope.

## 2026-09-11 — Iteration 3

### Implemented in `TradeOps-GenAI-Integration`

- deterministic market-regime engine using I2 technical evidence;
- `TREND_UP`, `TREND_DOWN`, `RANGE`, `HIGH_VOLATILITY`, `LOW_VOLATILITY`, `BREAKOUT`, `POST_EVENT`, `RISK_ON`, `RISK_OFF` and fail-closed `UNKNOWN`;
- explicit deterministic regime precedence and configurable strategy allowlists;
- validated `TradeIntent`, `RiskState`, `RiskLimits` and `RiskDecision` contracts;
- risk-per-trade, daily-loss, gross-exposure, concentration, correlated-exposure, ATR-volatility, event, spread, slippage and freshness gates;
- circuit breakers for kill switch, degraded feed, daily-loss threshold and consecutive losses;
- explicit aggregated veto reasons with deterministic ordering;
- fail-closed structured event adapter requiring `risk_intent`, `risk_state` and `regime`;
- Kafka risk worker upgraded to the I3 policy engine; the previous fixed `qty=100/MAX_QTY` placeholder was removed;
- JSON Schemas for market-regime and risk-decision outputs;
- versioned positive/negative risk scenarios, CLI demo and dedicated I3 test suite.

### Evidence

- functional runtime commit: `6e0768321f73c99dc6997a5963f727ed7aa99825`;
- lint correction / final I3 runtime HEAD: `bd5edfd32f894995233658aac27616f4a120d6dc`;
- runtime delta from I2: 14 files changed across regime, risk, schemas, docs, fixture, demo and tests;
- first CI run `34644207171` rejected 10 Ruff import/re-export issues; no lint rule was disabled;
- dedicated I3 test suite: 22 cases;
- final GitHub Actions run `34644295181`: SUCCESS;
- final full runtime CI: Ruff clean, 52 tests passed with 3 non-blocking pre-existing deprecation warnings.

### Explicit non-claims

- I3 does not prove trading profitability or strategy expectancy;
- no VaR/CVaR, portfolio optimizer or sophisticated netting model is claimed;
- exposure-after-trade calculations are deliberately conservative and additive in I3;
- no calibrated ML probability is produced;
- no agent or LLM can override the deterministic risk veto;
- backtesting, transaction-cost experiments, out-of-sample and walk-forward evidence belong to I4;
- automated real-money execution remains outside scope.

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
