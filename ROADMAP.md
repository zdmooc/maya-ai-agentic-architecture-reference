# Roadmap to Excellence

The roadmap is capability-gated, not calendar-gated. Each level requires evidence.

## I0 — Baseline, audit and architecture map — IMPLEMENTED (documentation)

Deliverables:

- architecture vision and target architecture;
- audit of existing personal repositories;
- reuse/adapt/replace/reference decisions;
- current public-project shortlist and licensing notes;
- initial gaps and evidence plan;
- target separation between deterministic, ML and agentic layers.

No runtime validation is claimed in this repository for I0.

## I1 — Canonical market data and replay — IMPLEMENTED + TESTED OFFLINE / LIVE IG PENDING

Goal: establish trustworthy input before adding intelligence.

- IG demo REST authentication and historical data adapter;
- IG Lightstreamer streaming adapter;
- canonical `MarketEvent` model;
- bid/ask/spread/market-status/timestamp/source/latency/staleness fields;
- data-quality rules, duplicate/out-of-order handling;
- event schemas and replay from captured data;
- deterministic clock for reproducible tests.

Exit evidence: reproducible replay and stale/bad-data tests.

Status evidence:

- runtime commit: `38a4f9637da31e8b96f0de8444a59c29a33bc9f3`;
- dedicated I1 tests: 5 passed locally;
- full runtime CI: 19 passed, Ruff clean;
- replay fixture: 2 accepted / 0 rejected;
- actual IG Demo authentication, live Lightstreamer feed and real latency measurements remain pending and are not claimed.

See `evidence/ITERATION-001-MARKET-DATA-REPLAY.md`.

## I2 — Deterministic technical and pattern engines — IMPLEMENTED + TESTED

- indicators: EMA, VWAP, ATR, ADX, RSI, MACD, Bollinger;
- market structure: swings, HH/HL, LH/LL;
- patterns: breakout/retest, failed breakout, pullback, support/resistance rejection, compression/expansion, gaps, liquidity sweep;
- formal preconditions, invalidation, timeframe and evidence for every pattern;
- multi-timeframe aggregation.

Exit evidence: unit/property tests and replay-labelled examples.

Status evidence:

- functional runtime commit: `4979abb4b53047364c1a661308e551603dd5552b`;
- lint-fix runtime commit / current I2 HEAD: `5c0a77cfd70f620ec6eb867472181632ced6777e`;
- dedicated I2 tests: 11 passed locally;
- GitHub Actions run `34643453395`: SUCCESS;
- full runtime CI: Ruff clean, 30 tests passed, 3 non-blocking pre-existing deprecation warnings;
- labelled fixtures: breakout/retest LONG and failed-breakout SHORT both matched deterministically;
- no profitability, market-regime, risk-gate, ML-probability or live-execution claim is made by I2.

See `evidence/ITERATION-002-TECHNICAL-PATTERNS.md`.

## I3 — Market regime and deterministic risk v1 — IMPLEMENTED + TESTED

- regimes: TREND_UP, TREND_DOWN, RANGE, HIGH_VOLATILITY, LOW_VOLATILITY, BREAKOUT, POST_EVENT, RISK_ON, RISK_OFF plus UNKNOWN fail-closed fallback;
- regime-specific strategy allowlist;
- risk per trade, daily loss, exposure, concentration, correlation, volatility, event/spread/slippage/freshness gates;
- circuit breakers and explicit veto reasons;
- structured `TradeIntent`, `RiskState`, `RiskLimits`, `RiskDecision` contracts;
- fail-closed event adapter requiring risk intent, risk state and regime context;
- legacy fixed-quantity/MAX_QTY risk placeholder removed from the Kafka worker.

Exit evidence: negative tests proving that unsafe signals are vetoed.

Status evidence:

- functional runtime commit: `6e0768321f73c99dc6997a5963f727ed7aa99825`;
- lint-fix runtime commit / current I3 HEAD: `bd5edfd32f894995233658aac27616f4a120d6dc`;
- dedicated I3 tests: 22 cases;
- first CI correctly rejected 10 Ruff packaging/import issues; no rule was disabled;
- GitHub Actions run `34644295181`: SUCCESS;
- final full runtime CI: Ruff clean, 52 tests passed, 3 non-blocking pre-existing deprecation warnings;
- versioned risk scenarios include an approved trend pullback and a stale/wide-spread veto;
- no profitability, VaR, optimized sizing, ML probability, backtest expectancy or live execution claim is made by I3.

See `evidence/ITERATION-003-MARKET-REGIME-RISK.md`.

## I4 — Backtesting and experiment discipline — IMPLEMENTED + TESTED (SYNTHETIC MECHANICS)

- versioned historical-dataset contract and deterministic dataset/config SHA-256 evidence;
- event-driven next-bar-open execution to avoid same-bar lookahead;
- explicit half-spread, slippage and commission assumptions on both sides of a trade;
- conservative `STOP_FIRST` policy for same-bar stop/target ambiguity;
- I3 `risk_status=APPROVED` enforcement before execution;
- chronological out-of-sample split and rolling walk-forward windows with no shuffle;
- metrics: trade count, win rate, PnL, average R / expectancy R, profit factor and drawdown;
- MFE/MAE per trade and breakdowns by regime/session/timeframe/pattern;
- buy-and-hold baseline using the same cost model;
- versioned result schema, experiment protocol, synthetic fixture and CLI demo.

Reference engines remain NautilusTrader first for architecture/replay study and LEAN as an independent comparison option. Neither external engine is claimed as executed in I4.

Exit evidence: reproducible synthetic run from pinned data/config/commit plus CI tests proving execution timing, costs, veto handling, splits and metrics.

Status evidence:

- runtime commit / I4 HEAD: `381b7dedf85a2170d8ff59205678bdf4692e5146`;
- runtime delta from I3: 1 commit, 13 files added, no I0-I3 runtime files modified;
- dedicated I4 tests added: 16;
- GitHub Actions run `34645138469`: SUCCESS;
- final full runtime CI: Ruff clean, 68 tests passed, 3 non-blocking pre-existing deprecation warnings;
- synthetic fixture executes 4 approved trades and skips 1 I3-vetoed signal;
- labelled synthetic outcomes are 3 TARGET and 1 STOP, giving a fixture win rate of 75% only as a mechanics assertion, not a profitability claim;
- tests prove explicit costs reduce performance versus a zero-cost run;
- chronological and walk-forward tests prove train intervals finish before test intervals begin;
- Sharpe/Sortino are intentionally omitted for the tiny synthetic fixture because the sample is not statistically meaningful;
- no real-market profitability, out-of-sample alpha, real IG transaction-cost distribution or external-engine validation is claimed.

See `evidence/ITERATION-004-BACKTESTING-EXPERIMENTS.md`.

## I5 — ML signal quality

- feature contracts and leakage checks;
- XGBoost/LightGBM/scikit-learn baselines;
- train/validation/test and walk-forward;
- calibration (for example Platt/isotonic as justified);
- MLflow tracking/model registry;
- drift/performance monitoring;
- Feast only if online/offline feature consistency creates a real need.

Exit evidence: calibrated out-of-sample metrics. Until then outputs remain `score`, not `probability`.

## I6 — RAG, governed MCP and specialized agents

- RAG over strategies, risk policies, runbooks, ADRs, past setups and evidence;
- actual agent framework implementation after ADR (LangGraph baseline candidate; Microsoft Agent Framework evaluated as alternative);
- specialized Market, Technical, Pattern, Macro, Risk and Fusion agents;
- UNKNOWN / DATA_STALE / CONFLICT states;
- governed MCP tools with authn/authz, allowlists, validation, timeouts, rate limits, audit and HITL;
- no arbitrary shell or unrestricted trading tool.

Exit evidence: disagreement scenarios and tool-policy tests.

## I7 — Decision fusion and Human-in-the-Loop

Fusion must use evidence quality, data quality, regime, calibrated ML evidence, historical expectancy and risk vetoes—not majority voting.

Output contract includes instrument, direction, entry zone, invalidation, stop, targets, R/R, timeframe, regime, pattern, ML score/probability status, risk status, freshness, evidence and final decision.

Exit evidence: paper/shadow workflow with explicit approval and auditable rationale.

## I8 — End-to-end observability, security and LLMOps

- OpenTelemetry traces across event -> feature -> pattern -> ML -> agent -> MCP -> fusion -> risk -> decision;
- Prometheus/Grafana service and business metrics;
- optional Phoenix evaluation/observability only after ELv2 license review;
- LLM cost/token/latency metrics;
- OIDC/RBAC, secrets, NetworkPolicy, mTLS where justified, SBOM, image scanning and Policy-as-Code;
- prompt-injection/tool-abuse tests.

Exit evidence: trace correlation IDs, dashboards, alerts, threat-model tests.

## I9 — OpenShift Local / CRC and GitOps

- package the complete runnable slice rather than only selected services;
- resource requests/limits, probes, quotas, network policies;
- GitOps using Argo CD + Kustomize/Helm;
- Kyverno policies based on current supported APIs;
- local LLM may remain outside CRC through Ollama when GPU/RAM economics justify it.

Exit evidence: deploy/verify scripts and versioned command/test output.

## I10 — OpenShift AI / production AI serving

- OpenShift AI model-serving architecture;
- KServe for standardized serving;
- vLLM for supported LLM serving;
- MLflow lifecycle integration;
- SLOs, capacity, HA and failure-mode exercises.

Exit evidence: measured deployment, not a diagram-only claim.

## I11 — Azure / ARO enterprise target

Reuse the existing Azure architecture reference for:

- Landing Zone / Entra ID / Key Vault;
- private networking and endpoints;
- Azure Monitor/OpenTelemetry;
- Microsoft Foundry/Azure OpenAI where selected;
- ARO as the OpenShift-on-Azure target;
- Terraform/IaC, FinOps and GreenOps.

Exit evidence: architecture decision pack plus selectively executed affordable labs.

## I12 — Excellence graduation

Minimum graduation evidence:

- live multi-source input plus replay;
- data-quality engine;
- multi-timeframe technical/pattern/regime engines;
- reproducible backtesting, out-of-sample and walk-forward;
- genuinely calibrated ML if probabilistic claims are made;
- specialized agents with conflict handling;
- secure MCP;
- deterministic risk gate and HITL;
- at least 100 documented paper/shadow signals with outcome metrics;
- end-to-end observability and security controls;
- GitOps/OpenShift and Azure target architecture;
- ADR/NFR/resilience/FinOps/GreenOps evidence;
- interview demonstration pack and explicit banking/insurance transposition.
