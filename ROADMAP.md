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

## I5 — ML signal quality — IMPLEMENTED + TESTED / SYNTHETIC OOS CALIBRATION

- versioned point-in-time feature contract using technical, structure, pattern, regime, market-quality, spread and latency evidence;
- explicit leakage guards rejecting future/outcome/label/PnL/MFE/MAE semantics in feature names;
- strictly chronological TRAIN / VALIDATION / CALIBRATION / TEST roles with no random shuffle;
- ten rolling walk-forward windows with separate calibration and test segments;
- scikit-learn logistic regression and histogram-gradient-boosting baselines;
- XGBoost and LightGBM baselines;
- validation-only champion selection;
- Platt calibration fitted only on a dedicated calibration segment;
- final untouched TEST metrics: ROC-AUC, Brier, log loss, ECE, accuracy, precision and recall;
- explicit probability qualification that fails closed to `SCORE_ONLY` when sample, calibration, discrimination or drift gates fail;
- PSI and standardized-mean-shift drift monitoring;
- real MLflow tracking and Model Registry smoke test using SQLite plus controlled Skops trusted-type allowlist;
- Feast deferred until a real online/offline feature-consistency need exists.

Exit evidence: calibrated out-of-sample mechanics on a pinned synthetic dataset plus end-to-end MLflow registry validation. Real-market probability calibration remains pending.

Status evidence:

- final runtime HEAD: `bca514ce35fab3e63ef16e487394fea576523d7b`;
- runtime delta from I4: 4 commits ahead, 20 files changed, zero commits behind;
- final GitHub Actions run `34646841551`: SUCCESS;
- final full runtime CI: Ruff clean, 87 tests passed;
- I5 adds 19 passing tests over the I4 baseline;
- final CI runs CPython 3.11.16 with XGBoost 3.2.0, LightGBM 4.7.0 and MLflow 3.16.0 installed successfully;
- pinned synthetic champion: `sklearn_logistic`;
- final synthetic TEST set: 72 observations;
- calibrated synthetic TEST ROC-AUC ≈ 0.7407, Brier ≈ 0.2005, log loss ≈ 0.5882 and ECE ≈ 0.0937;
- synthetic drift status: WATCH, maximum PSI ≈ 0.2428;
- qualification status: `CALIBRATED_OUT_OF_SAMPLE_SYNTHETIC`;
- two earlier CI failures were retained as hardening evidence: FileStore was replaced by SQLite, then Skops custom classes were explicitly allowlisted rather than bypassing serialization controls;
- no live or historical real-market calibrated probability, alpha, profitability or live-money readiness is claimed.

See `evidence/ITERATION-005-ML-SIGNAL-QUALITY.md`.

## I6 — RAG, governed MCP and specialized agents — IMPLEMENTED + TESTED / ANALYSIS ONLY

- real LangGraph `StateGraph` orchestration pinned to `langgraph==1.2.11`;
- specialized Market, Technical, Pattern, Macro, Risk and Fusion agents consuming I1-I5 evidence rather than recomputing deterministic capabilities;
- explicit `SUPPORTED`, `UNKNOWN`, `DATA_STALE`, `CONFLICT` and terminal `VETO` states;
- deterministic I3 risk `VETO` remains authoritative and cannot be overridden by agent/RAG/ML agreement;
- versioned RAG corpus for strategies, risk policies, runbooks, agent boundary and evidence lineage;
- governed RAG admission checks for approved source types, relevance, bounded text and prompt-injection markers;
- server-side bearer-token principals/scopes for the tool boundary;
- tool allowlist, strict argument validation, per-principal/tool rate limits, timeouts and audit redaction;
- general-agent identity has no `paper.execute` scope;
- paper-order tool requires separate reviewer scope plus explicit human approval;
- legacy autonomous `/agent/trade` execution path disabled; `/agent/assessment` is analysis-only;
- versioned disagreement/staleness/veto fixtures and agent assessment JSON Schema with `execution_allowed=false`.

Exit evidence: actual LangGraph execution, disagreement scenarios and negative tool-policy tests in the full CI.

Status evidence:

- runtime commit / final I6 HEAD: `faa16245013155265ef1edb8e3f47ba1b9b77415`;
- runtime delta from I5: exactly 1 commit ahead, 22 files changed, zero commits behind;
- GitHub Actions run `34648593641`: SUCCESS;
- final full runtime CI: Ruff clean, 111 tests passed, 69 non-blocking deprecation warnings;
- net test increase over I5: 24 tests;
- versioned policy fixture proves aligned LONG -> `SUPPORTED`, directional disagreement -> `CONFLICT`, stale market -> `DATA_STALE`, deterministic risk veto -> `VETO`;
- tests prove unauthenticated, missing-scope, unknown-tool, unknown-argument, invalid enum/quantity, rate-limit and timeout paths fail closed;
- tests prove the general-agent token cannot self-escalate to paper execution even when the request submits `human_approved=true`;
- official MCP Python SDK v2 was reviewed but is not added; I6 claims a governed MCP-shaped compatibility boundary, not native MCP protocol conformance or Streamable HTTP deployment;
- Microsoft Agent Framework remains an evaluated alternative and is not added alongside LangGraph;
- no executable I7 fusion/HITL workflow, live-money execution or production OIDC identity federation is claimed.

See `evidence/ITERATION-006-RAG-MCP-AGENTS.md`.

## I7 — Decision fusion and Human-in-the-Loop — IMPLEMENTED + TESTED

- deterministic gate-based fusion; no majority voting and no auto-approval;
- I6 assessment must be `SUPPORTED` and I3 deterministic risk must remain `ACCEPT`;
- hard gates for freshness, evidence quality, regime allowlist, R/R, historical sample size, historical expectancy and directionally valid entry/stop/target geometry;
- synthetic I5 calibration remains non-decisive; only explicitly qualified real-market calibrated probability can activate the ML gate;
- informational evidence score cannot override hard policy/risk gates;
- eligible proposals become only `REVIEW_REQUIRED` with `human_approval_required=true` and `execution_allowed=false`;
- persisted HITL lifecycle: `PENDING_REVIEW -> APPROVED|REJECTED|EXPIRED`;
- approved cases can become `EXECUTED_SHADOW` or `EXECUTED_PAPER`, with expiry and duplicate-execution guards;
- reviewer authentication is separate from the agent identity;
- SHADOW requires approval but never calls the order tool;
- PAPER requires approval and uses the governed I6 tool boundary with reviewer identity plus `human_approved=true`;
- proposal ID is preserved as the paper order `workflow_id` for decision -> review -> order lineage;
- full I7 case is persisted using the existing `workflows` table under `payload.i7`;
- audit events: `decision.proposed`, `decision.reviewed`, `decision.executed`;
- versioned proposal schema and synthetic policy scenarios.

Exit evidence: authenticated API flow for proposal/review/SHADOW/PAPER, negative gate tests, expiry/duplicate tests and full CI.

Status evidence:

- functional runtime commit: `ab6154b6cd9dbe60e6b30d893c5e7d3d57837d13`;
- final runtime HEAD after test correction/API coverage: `f2e8536da9dc5c0e63134d97c3052f7b00ba1d0a`;
- first GitHub Actions run `34650643058`: Ruff clean; 141 passed / 1 failed because the legacy I6 health test still expected `ANALYSIS_ONLY` after I7 correctly changed service mode to `ANALYSIS_PLUS_HITL`;
- no I7 fusion/HITL functional test failed in the first run;
- final GitHub Actions run `34650953035`: SUCCESS;
- final full runtime CI: Ruff clean, 145 tests passed, 69 non-blocking deprecation warnings;
- net test increase over I6: 34 tests;
- API tests prove the general agent cannot approve, reviewer approval is required, SHADOW is order-free, duplicate execution is rejected and PAPER preserves proposal-to-order workflow lineage;
- automated real-money execution, live IG order routing, real-market ML calibration and production OIDC/RBAC remain explicitly unclaimed.

See `evidence/ITERATION-007-DECISION-FUSION-HITL.md`.

## I8 — End-to-end observability, security and LLMOps — IMPLEMENTED + TESTED IN CI / DEPLOYMENT VALIDATION PENDING

- real OpenTelemetry SDK replaces the previous placeholder;
- W3C `traceparent` plus `X-Correlation-ID` propagation across HTTP/Kafka helper paths;
- business spans for decision fusion and deterministic risk evaluation;
- LLM spans with provider/model/status/latency metadata while avoiding prompt-body capture;
- Prometheus service/business/security/LLM metrics;
- Grafana I8 dashboard, Prometheus alert rules and OpenTelemetry Collector configuration;
- LLM token/cost/latency metrics with estimated usage clearly distinguished from provider-native usage;
- reusable identity layer with local static principals plus OIDC/JWT-compatible issuer/audience/JWKS/expiry/role/scope verification;
- tracked `.env` removed and forbidden by CI hygiene rules;
- weak local password defaults corrected to explicit placeholders;
- focused secret/private-key audit gate;
- deterministic SPDX SBOM for pinned direct Python requirements plus CI consistency check;
- prompt-injection regression, OIDC fail-closed, trace/correlation and SBOM/security tests.

Exit evidence: code/CI trace-correlation tests, dashboard/alert/collector configuration, JWT/security negative tests, SBOM/security gates and full regression CI.

Status evidence:

- functional runtime commit: `eea28b5d5317f3fd200de56ba882f9a6d93371d4`;
- final runtime HEAD after security hardening: `90976dd60a9b80272e39db07ed027ae500f947c1`;
- runtime delta from I7: 2 commits ahead, 0 behind, 30 files changed;
- first GitHub Actions run `34653286233`: dependency install and Ruff passed; the newly introduced security audit correctly failed on weak defaults and scanner false positives; SBOM/Pytest were skipped;
- no security gate or lint rule was disabled; weak defaults were corrected and exclusions were narrowed to scanner self-text plus historical redacted evidence;
- final GitHub Actions run `34654382558`: SUCCESS;
- final job `103443477579`: Ruff PASS, `SECURITY_AUDIT_PASS`, `SBOM_CHECK_PASS`, 157 tests passed, 69 non-blocking deprecation warnings;
- net test increase over I7: 12 tests;
- deployment of the Collector/Grafana dashboard/alerts against live traffic and production external OIDC federation are not claimed in I8;
- NetworkPolicy, mTLS, image scanning and cluster Policy-as-Code remain I9 deployment work;
- Phoenix is intentionally not added before a deliberate ELv2 adoption decision.

See `evidence/ITERATION-008-OBSERVABILITY-SECURITY-LLMOPS.md`.

## I9 — OpenShift Local / CRC and GitOps — IMPLEMENTED + TESTED IN CI / LIVE CRC DEPLOYMENT PENDING

- unified OpenShift runtime image used by nine target application workloads;
- target slice includes market-data, workflow-api, genai-api, rag-api, agent-controller, mcp-server, deterministic risk-engine, paper-oms and notifier;
- legacy pre-I2 `signal-engine` explicitly excluded from the target deployment;
- PostgreSQL, Redpanda and Qdrant local StatefulSets with PVCs;
- OpenTelemetry Collector, Prometheus and Grafana local observability services;
- explicit CPU/memory requests and limits for application and platform containers;
- startup/readiness/liveness probes for HTTP APIs plus stateful readiness checks;
- restricted-security-compatible pod/container settings with arbitrary-UID image permissions;
- ResourceQuota, LimitRange and CRC-specific resource/storage overrides;
- default-deny NetworkPolicy plus explicit intra-namespace, DNS, OpenShift router ingress and selected HTTPS egress rules;
- OpenShift ImageStream/BuildConfig building `Dockerfile.openshift` into `tradeops-runtime:i9`;
- Argo CD AppProject plus platform, Kyverno-policy and runtime Applications;
- real repository URL and explicit `main` revision replace the old placeholder;
- Kyverno CEL `policies.kyverno.io/v1` `ValidatingPolicy` policies for resources, explicit image tags and container security;
- CRC preflight/deploy/verify scripts and fail-closed Trivy image-scan helper;
- Helm lint/render and I9 platform-contract checks added to CI.

Exit evidence: versioned deploy/verify scripts, reproducible Helm rendering, policy/platform tests and full CI. Actual CRC execution remains a separate deployment-evidence step.

Status evidence:

- functional runtime commit: `80ee9297a299133a63c7326b34bddf33d588bab5`;
- final runtime HEAD after lint correction: `92e0718640e8a19f61df671c14a74e163a5af445`;
- runtime delta from I8: 2 commits ahead, 0 behind, 35 files changed;
- first GitHub Actions run `34681157466`: dependency install passed; Ruff rejected one unused import and later gates were skipped; no rule was disabled;
- final GitHub Actions run `34681213356`: SUCCESS;
- final job `103520072644`: Ruff PASS, `SECURITY_AUDIT_PASS`, `SBOM_CHECK_PASS`, Helm lint PASS, Helm template PASS and `I9_PLATFORM_VALIDATION_PASS`;
- final Pytest: 167 passed, 69 non-blocking deprecation warnings in 16.83s;
- net test increase over I8: 10 tests;
- live CRC BuildConfig execution, image pulls, PVC binding, Routes, Argo CD sync, Kyverno admission and actual image scan remain pending and are not claimed.

See `evidence/ITERATION-009-OPENSHIFT-CRC-GITOPS.md`.

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