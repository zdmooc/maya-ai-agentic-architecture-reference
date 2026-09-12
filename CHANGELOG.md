# Changelog

## 2026-09-12 — Iteration 10

### Implemented in `TradeOps-GenAI-Integration`

- versioned Red Hat OpenShift AI 3.4 target for model serving;
- KServe custom `ServingRuntime` and `InferenceService` resources for the I5 signal-quality model;
- executable FastAPI online-serving boundary with liveness, readiness, prediction and Prometheus metrics endpoints;
- exact I5 feature-contract enforcement with rejection of missing, extra and non-finite inputs;
- validated `predict_proba` output shape/range;
- explicit `LAB` / `PRODUCTION` serving modes;
- hard production guard requiring `CALIBRATED_OUT_OF_SAMPLE_REAL_MARKET`, so the I5 synthetic calibration cannot be promoted by configuration drift;
- OpenShift ImageStream and binary BuildConfig for `tradeops-ai-runtime:i10`;
- RHOAI-managed MLflow target with service-account RoleBinding to `mlflow-operator-mlflow-integration` and Kubernetes namespaced authentication settings;
- model URI, qualification and serving mode kept out of Git and injected through a runtime Secret;
- initial two-replica HA floor and four-replica ceiling for signal-quality serving;
- versioned vLLM KServe example using the platform `vllm-runtime`, one NVIDIA GPU per replica and a deliberate `s3://REPLACE-ME/...` storage placeholder;
- Prometheus serving SLO rules for unavailable responses, error ratio and p95 latency;
- deterministic capacity estimator with an explicit non-benchmark status;
- RHOAI preflight, deploy and verify scripts;
- I10 static platform validator added to CI;
- 17 new I10 tests for model-serving contracts, production qualification, API behavior, platform manifests, vLLM reference and capacity logic.

### Evidence

- runtime commit / final I10 HEAD: `316a6a0f1cf09b35b4594d8f2061f206ee31f45c`;
- runtime delta from I9: 1 commit ahead, 0 behind, 24 changed files;
- GitHub Actions run `34681817517`: SUCCESS;
- final job `103521706237`: Ruff PASS, `SECURITY_AUDIT_PASS`, `SBOM_CHECK_PASS`, I9 Helm/validator gates PASS and `I10_AI_SERVING_VALIDATION_PASS`;
- final Pytest: 184 passed, 69 non-blocking deprecation warnings in 13.26s;
- net increase from I9: 17 passing tests;
- the first I10 CI run was green; no quality or safety gate required weakening or bypassing.

### Explicit non-claims

- I10 does not claim a live RHOAI 3.4 deployment on the user's CRC cluster;
- no live KServe InferenceService Ready status has been captured yet;
- no production RHOAI MLflow workspace/model version has been created or verified;
- the existing I5 `CALIBRATED_OUT_OF_SAMPLE_SYNTHETIC` model remains lab-only;
- the vLLM resource values are a starting reference, not measured GPU capacity;
- no LLM model artifact or object-storage path is pretended to exist; the example intentionally keeps `s3://REPLACE-ME/...`;
- no measured cold/warm p50/p95/p99 latency, throughput, GPU utilization, saturation or failover recovery is claimed;
- no automated real-money execution or live IG order routing is enabled;
- Azure/ARO implementation remains I11 work.

## 2026-09-12 — Iteration 9

### Implemented in `TradeOps-GenAI-Integration`

- complete OpenShift Local / CRC target packaging for nine application workloads plus PostgreSQL, Redpanda, Qdrant, OpenTelemetry Collector, Prometheus and Grafana;
- unified OpenShift-compatible Python runtime image to reduce duplicated CRC image storage;
- explicit exclusion of the legacy pre-I2 `signal-engine` from the target runtime;
- Helm chart upgraded from the historical three-API demonstrator to the I9 target slice;
- startup/readiness/liveness probes for HTTP APIs and readiness checks for stateful/platform workloads;
- explicit CPU/memory requests and limits, ServiceAccount hardening, `RuntimeDefault` seccomp, disabled privilege escalation and capability drop `ALL`;
- ResourceQuota, LimitRange, restricted Pod Security labels and CRC overlay;
- default-deny NetworkPolicy plus explicit intra-namespace, DNS, router-ingress and selected HTTPS-egress rules;
- OpenShift ImageStream and BuildConfig using `Dockerfile.openshift` and output tag `tradeops-runtime:i9`;
- Argo CD AppProject and three Applications for platform guardrails, Kyverno policies and Helm runtime;
- real repository URL and explicit `main` targetRevision replacing the old placeholder;
- Kyverno CEL `policies.kyverno.io/v1` `ValidatingPolicy` guardrails for resources, non-latest tags and container security;
- CRC preflight, deploy and verify scripts plus a fail-closed Trivy image-scan helper;
- CI gates for Helm lint, Helm rendering and I9 platform-contract validation;
- ten I9 platform tests.

### Evidence

- functional runtime commit: `80ee9297a299133a63c7326b34bddf33d588bab5`;
- final runtime HEAD after lint correction: `92e0718640e8a19f61df671c14a74e163a5af445`;
- final runtime delta from I8: 2 commits ahead, 0 behind, 35 files changed;
- first GitHub Actions run `34681157466`: dependency install passed and Ruff rejected one unused `Path` import before later gates ran; no rule was disabled;
- corrective commit removed only that unused import;
- final GitHub Actions run `34681213356`: SUCCESS;
- final job `103520072644`: Ruff PASS, `SECURITY_AUDIT_PASS`, `SBOM_CHECK_PASS`, Helm lint PASS, Helm template PASS and `I9_PLATFORM_VALIDATION_PASS`;
- final Pytest: 167 passed, 69 non-blocking deprecation warnings in 16.83s;
- net increase from I8: 10 passing tests;
- Helm reported `1 chart(s) linted, 0 chart(s) failed`.

### Explicit non-claims

- I9 does not claim that the user's local CRC cluster has executed the deployment yet;
- no live evidence is claimed yet for BuildConfig completion, image pulls, PVC binding, Routes, runtime health checks, Argo CD sync, Kyverno admission decisions or actual CRC trace delivery;
- the Trivy helper is versioned but the CRC-built image has not been scanned in CI;
- PostgreSQL, Redpanda, Qdrant, Prometheus and Grafana are single-instance local-lab dependencies, not production HA designs;
- standard NetworkPolicy does not provide FQDN-level egress filtering and I9 does not claim it;
- no full service-to-service mTLS is claimed;
- OpenShift AI, KServe and vLLM serving remain I10 work;
- no automated real-money execution or live IG order routing is enabled.

## 2026-09-12 — Iteration 8

### Implemented in `TradeOps-GenAI-Integration`

- real OpenTelemetry SDK replacing the previous placeholder;
- W3C `traceparent` and application `X-Correlation-ID` propagation across HTTP/Kafka helper paths;
- business spans for decision fusion and deterministic risk evaluation;
- LLM spans and Prometheus metrics for provider/model/status/latency plus estimated token/cost usage without intentional prompt-body capture;
- expanded Prometheus scrape configuration, I8 Grafana dashboard, alert rules and OpenTelemetry Collector configuration;
- reusable identity layer supporting the local static demonstrator and OIDC/JWT-compatible issuer/audience/JWKS/expiry/role/scope verification;
- tracked `.env` removed and ignored;
- weak local Postgres password defaults replaced by explicit placeholders;
- CI secret/private-key hygiene scanner;
- deterministic SPDX JSON SBOM generated from pinned direct Python requirements;
- CI SBOM consistency gate;
- I8 tests for trace/correlation, OIDC fail-closed behavior, security scanning, SBOM determinism and prompt-injection regression.

### Evidence

- functional runtime commit: `eea28b5d5317f3fd200de56ba882f9a6d93371d4`;
- corrective security-hardening commit / final I8 HEAD: `90976dd60a9b80272e39db07ed027ae500f947c1`;
- runtime delta from I7: 2 commits ahead, 0 behind, 30 files changed;
- first GitHub Actions run `34653286233`: dependency install and Ruff passed, then the newly added security audit failed on weak defaults and scanner false positives; SBOM/Pytest were skipped as intended;
- no quality/security gate was disabled;
- active weak defaults were corrected and scanner exclusions were limited to its own source plus historical redacted `evidence-sample/` artifacts;
- final GitHub Actions run `34654382558`: SUCCESS;
- final job `103443477579`: Ruff PASS, `SECURITY_AUDIT_PASS`, `SBOM_CHECK_PASS`;
- final Pytest: 157 passed, 69 non-blocking deprecation warnings in 15.78s;
- net increase from I7: 12 passing tests.

### Explicit non-claims

- no production trace backend or retained end-to-end trace stream is claimed from I8;
- Grafana dashboard rendering and alert delivery are configured but not deployment-verified against live traffic;
- OIDC/JWT verification mechanics are tested, but no real production IdP federation is claimed;
- the SPDX SBOM covers pinned direct Python requirements and is not claimed as a complete transitive container/image SBOM;
- the focused secret audit is not a replacement for an enterprise secret-scanning/SAST platform;
- prompt-injection marker detection is not comprehensive prompt-injection immunity;
- NetworkPolicy, mTLS, image scanning and cluster Policy-as-Code remain I9 deployment work;
- Phoenix remains intentionally unadded pending an explicit ELv2 adoption decision;
- no automated real-money execution or live IG order routing is enabled.

## 2026-09-11 — Iteration 7

### Implemented in `TradeOps-GenAI-Integration`

- deterministic gate-based decision fusion with no majority voting and no autonomous approval;
- I6 `SUPPORTED` assessment and I3 deterministic `ACCEPT` risk status required before review eligibility;
- hard fusion gates for freshness, evidence quality, regime, R/R, historical sample, historical expectancy and price geometry;
- I5 synthetic calibration explicitly remains non-decisive; only explicitly qualified real-market calibration can enter the ML probability gate;
- informational evidence score that cannot override hard gates;
- `NO_TRADE` / `REVIEW_REQUIRED` proposal contract with `human_approval_required=true` and `execution_allowed=false`;
- persisted HITL lifecycle with `PENDING_REVIEW`, `APPROVED`, `REJECTED`, `EXPIRED`, `EXECUTED_SHADOW` and `EXECUTED_PAPER`;
- authenticated agent proposal identity separated from reviewer approval/execution identity;
- SHADOW execution after approval without order placement;
- PAPER execution after approval through the governed I6 tool boundary with `human_approved=true`;
- exact proposal ID preserved as paper-order `workflow_id` for lineage;
- I7 case persistence reusing the existing `workflows` table under `payload.i7`;
- audit events for proposal, review and execution;
- versioned proposal JSON Schema, synthetic policy fixture and I7 documentation;
- API tests covering propose -> review -> SHADOW/PAPER, reviewer authorization and duplicate execution rejection.

### Evidence

- functional runtime commit: `ab6154b6cd9dbe60e6b30d893c5e7d3d57837d13`;
- final runtime HEAD: `f2e8536da9dc5c0e63134d97c3052f7b00ba1d0a`;
- first GitHub Actions run `34650643058`: Ruff PASS, 141 tests passed and one legacy I6 health assertion failed because it still expected `ANALYSIS_ONLY` after the I7 mode change;
- no I7 fusion/HITL functional test failed in that first run;
- corrective commit updated the health contract and added API-level HITL coverage without weakening any gate;
- final GitHub Actions run `34650953035`: SUCCESS;
- final CI: Ruff clean, 145 tests passed, 69 non-blocking deprecation warnings;
- net increase from I6: 34 passing tests;
- tests prove risk veto/no-accept paths fail closed, stale/weak/low-RR/negative-expectancy cases do not enter review, review expiry is enforced and duplicate review/execution is rejected;
- tests prove a general agent cannot approve, SHADOW does not call paper execution and PAPER preserves proposal-to-order workflow lineage.

### Explicit non-claims

- no automated real-money execution is enabled;
- no live IG order execution is claimed;
- no real-market calibrated ML probability is claimed;
- static bearer tokens are a local demonstrator and not production OIDC/RBAC;
- end-to-end OpenTelemetry, production dashboards/SLOs and Policy-as-Code remain I8 work;
- synthetic fusion fixtures do not establish strategy profitability.

## 2026-09-11 — Iteration 6

### Implemented in `TradeOps-GenAI-Integration`

- real LangGraph `StateGraph` orchestration using `langgraph==1.2.11`;
- specialist Market, Technical, Pattern, Macro, Risk and Fusion agents;
- explicit `SUPPORTED`, `UNKNOWN`, `DATA_STALE`, `CONFLICT` and `VETO` states;
- deterministic I3 risk veto preserved as terminal;
- versioned governed RAG corpus and pre-agent admission checks;
- prompt-injection marker rejection and fail-closed RAG UNKNOWN/CONFLICT behavior;
- server-side bearer-token principals/scopes at the tool boundary;
- explicit tool allowlist, argument/type/enum validation, rate limiting, timeouts and audit redaction;
- distinct general-agent and reviewer identities;
- `paper.execute` excluded from the general-agent scopes;
- explicit human approval additionally required for `oms.place_order`;
- legacy autonomous `/agent/trade` execution disabled;
- analysis-only `/agent/assessment` endpoint and output schema with `execution_allowed=false`;
- versioned aligned/disagreement/stale/veto scenarios;
- ADR documenting LangGraph selection and MCP conformance boundary.

### Evidence

- runtime commit / final I6 HEAD: `faa16245013155265ef1edb8e3f47ba1b9b77415`;
- runtime is exactly 1 commit ahead of I5, zero behind, with 22 changed files;
- GitHub Actions run `34648593641`: SUCCESS;
- full CI: Ruff clean, 111 tests passed, 69 non-blocking deprecation warnings;
- net increase from I5: 24 passing tests;
- CI installs and executes `langgraph==1.2.11` on CPython 3.11.16;
- versioned fixtures prove SUPPORTED, CONFLICT, DATA_STALE and VETO paths;
- negative tool-policy tests prove auth, scope, allowlist, argument, approval, rate-limit and timeout failures are fail-closed;
- general-agent identity cannot self-escalate into paper execution by sending `human_approved=true`.

### Explicit non-claims

- I6 is analysis-only and does not implement I7 executable fusion/HITL workflow;
- no automated real-money execution is enabled;
- the static bearer-token mapping is a testable local boundary, not production OIDC/RBAC federation;
- the hardened `/call` API is not claimed as native MCP protocol conformance or Streamable HTTP deployment;
- Microsoft Agent Framework is evaluated but not added alongside LangGraph;
- RAG checks do not claim comprehensive defense against all possible prompt-injection techniques;
- agents do not replace deterministic technical, pattern, regime or risk engines.

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
