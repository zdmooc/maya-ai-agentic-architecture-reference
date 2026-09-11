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

## I2 — Deterministic technical and pattern engines

- indicators: EMA, VWAP, ATR, ADX, RSI, MACD, Bollinger;
- market structure: swings, HH/HL, LH/LL;
- patterns: breakout/retest, failed breakout, pullback, support/resistance rejection, compression/expansion, gaps, liquidity sweep;
- formal preconditions, invalidation, timeframe and evidence for every pattern;
- multi-timeframe aggregation.

Exit evidence: unit/property tests and replay-labelled examples.

## I3 — Market regime and deterministic risk v1

- regimes: TREND_UP, TREND_DOWN, RANGE, HIGH_VOLATILITY, LOW_VOLATILITY, BREAKOUT, POST_EVENT, RISK_ON, RISK_OFF;
- regime-specific strategy allowlist;
- risk per trade, daily loss, exposure, concentration, correlation, volatility, event/spread/slippage/freshness gates;
- circuit breakers and explicit veto reasons.

Exit evidence: negative tests proving that unsafe signals are vetoed.

## I4 — Backtesting and experiment discipline

- historical dataset contracts;
- event-driven backtest/replay;
- transaction cost, spread and slippage assumptions;
- out-of-sample and walk-forward protocols;
- metrics: expectancy, average R, profit factor, drawdown, Sharpe/Sortino where meaningful, per-regime/session/timeframe/pattern performance;
- comparison against simple baselines.

Reference engines: NautilusTrader first for architecture/replay study; LEAN as independent reference/validation option.

Exit evidence: reproducible run from pinned data/config/commit.

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
