# Iteration 5 Evidence — ML Signal Quality, Calibration and MLflow

Date: 2026-09-11

## Status

**IMPLEMENTED + TESTED. SYNTHETIC OUT-OF-SAMPLE CALIBRATION EVIDENCE. REAL-MARKET CALIBRATION PENDING.**

Iteration 5 is implemented in the executable runtime repository `zdmooc/TradeOps-GenAI-Integration`. This architecture repository records the capability gate, evidence and non-claims.

Final runtime HEAD:

`bca514ce35fab3e63ef16e487394fea576523d7b`

Final GitHub Actions run:

`34646841551` — job `lint-test` — **SUCCESS**

## Runtime delta

The final I5 HEAD is four commits ahead of I4 HEAD `381b7dedf85a2170d8ff59205678bdf4692e5146` and zero commits behind.

I5 commit sequence:

1. `2be132fc0659b3669c23013604760da78b45e839` — initial signal-quality model contracts;
2. `16d283f1663830e6427ada1bb5579760f8d6bd1f` — calibrated signal-quality ML lifecycle;
3. `52492d5d1666dc4f774341886aa5e5542032cabd` — migrate local MLflow tracking from FileStore to SQLite;
4. `bca514ce35fab3e63ef16e487394fea576523d7b` — explicitly trust the two governed calibration classes for Skops model serialization.

Git compare from I4 to final I5 shows 20 changed files: 19 new files plus `requirements.txt` extended with the I5 runtime dependencies. Existing I1-I4 deterministic engines were not rewritten.

## Capability implemented

### Point-in-time feature contract

The `i5-v1` feature contract contains:

- RSI;
- MACD histogram;
- ATR percentage;
- ADX;
- EMA slope;
- VWAP distance percentage;
- volatility percentage;
- volume z-score;
- market-structure score;
- pattern score;
- relative strength;
- session code;
- distance to level in ATR units;
- regime code;
- spread in basis points;
- latency in milliseconds;
- data-quality score.

Every feature row has a timezone-aware `feature_time`; every target has a `label_time` that must be strictly later than the feature cutoff.

The contract rejects leakage-prone feature names containing terms such as `target`, `future`, `outcome`, `label`, `exit`, `pnl`, `profit`, `mfe`, `mae` or `tp_before_sl`.

## Versioned synthetic dataset

I5 intentionally uses a deterministic synthetic dataset only to validate the ML lifecycle mechanics.

Dataset spec:

`data/ml/i5_signal_quality_dataset.json`

Protocol:

`experiments/i5_signal_quality_protocol.json`

The spec pins:

- 480 records;
- seed `20260911`;
- start time `2026-01-05T08:00:00Z`;
- five-minute feature frequency;
- 30-minute label horizon;
- generator version `stable-logit-v1`;
- scope `SYNTHETIC_TEST_ONLY`.

The generated canonical rows are hashed with SHA-256 before model training. Tests assert that the hash is stable for the pinned specification.

## Temporal separation and leakage control

No random shuffle is used.

The final experiment split is:

- TRAIN: indices 0-239 — 50%;
- VALIDATION: 240-335 — 20%;
- CALIBRATION: 336-407 — 15%;
- TEST: 408-479 — 15%.

The final TEST set therefore contains 72 records and is not used for fitting the base model, selecting the champion, or fitting the calibrator.

Walk-forward evidence uses ten rolling windows with:

- train: 100 records;
- validation: 30;
- calibration: 30;
- test: 30;
- step: 30.

Every train/validation/calibration segment ends before its test segment begins. If a calibration segment contains only one class, that window remains score-only instead of manufacturing a calibration.

## Baselines

I5 executes four seeded baselines:

- scikit-learn logistic regression with standardization;
- scikit-learn histogram gradient boosting;
- XGBoost;
- LightGBM.

Pinned runtime dependencies added by I5:

- `xgboost==3.2.0`;
- `lightgbm==4.7.0`;
- `mlflow==3.16.0`.

The final CI installed all three successfully on CPython 3.11.16.

Champion selection is performed only on VALIDATION data, using ROC-AUC first and Brier score as deterministic tie-break. On the pinned synthetic fixture, the champion is:

`sklearn_logistic`

Raw classifier output remains explicitly labelled `SCORE_UNCALIBRATED` until the separate calibration stage succeeds.

## Calibration and qualification

I5 uses Platt logistic calibration fitted only on the CALIBRATION segment.

Final TEST metrics for the pinned synthetic fixture are approximately:

- observations: 72;
- ROC-AUC: `0.7407`;
- Brier score: `0.2005`;
- log loss: `0.5882`;
- expected calibration error: `0.0937`;
- accuracy: `0.6667`;
- precision: `0.6000`;
- recall: `0.3333`;
- observed positive rate: `0.3750`.

The probability qualification policy requires:

- at least 40 final-test records;
- ECE <= 0.15;
- positive Brier skill versus a prevalence-only baseline;
- ROC-AUC > 0.5;
- no feature-drift ALERT.

The pinned synthetic result passes those implementation gates and therefore receives the explicit status:

`CALIBRATED_OUT_OF_SAMPLE_SYNTHETIC`

This status is deliberately different from an unrestricted real-market probability claim.

## Drift monitoring

I5 computes for every feature:

- Population Stability Index (PSI);
- standardized mean shift.

Threshold policy:

- OK below PSI 0.10 and standardized mean shift 0.5;
- WATCH at PSI >= 0.10 or standardized mean shift >= 0.5;
- ALERT at PSI >= 0.25 or standardized mean shift >= 1.0.

A drift ALERT automatically demotes probability qualification to `SCORE_ONLY`.

The pinned synthetic train-to-test drift status is `WATCH`, with maximum PSI approximately `0.2428`; it does not cross the configured ALERT threshold.

## MLflow lifecycle

I5 integrates a real MLflow tracking and registry smoke test.

The runtime logs:

- dataset hash;
- feature-contract version;
- champion model;
- calibration method;
- raw and calibrated TEST metrics;
- the complete I5 report artifact;
- the serialized calibrated model;
- a registered model version;
- qualification tag on that model version.

The local/CI tracking backend uses SQLite rather than the legacy FileStore path.

Model serialization uses Skops. The only non-library custom types explicitly trusted by the I5 integration are:

- `services.ml_signal_quality.calibration.CalibratedSignalQualityModel`;
- `services.ml_signal_quality.calibration.PlattCalibrator`.

This explicit allowlist was chosen instead of weakening serialization controls or switching to a more permissive workaround.

## CI hardening history

I5 intentionally kept failing integration checks visible until the MLflow lifecycle was actually valid.

### CI run 1

Runtime HEAD `16d283f1663830e6427ada1bb5579760f8d6bd1f`:

- Ruff passed;
- 86 tests passed;
- one test failed: MLflow 3.16 rejected FileStore as the local tracking backend because that path is in maintenance mode.

Resolution: local/CI tracking moved to SQLite; the FileStore maintenance-mode opt-out was not enabled.

### CI run 2

Runtime HEAD `52492d5d1666dc4f774341886aa5e5542032cabd`:

- Ruff passed;
- 86 tests passed;
- one test failed: Skops rejected the two custom calibration classes as untrusted types.

Resolution: the two project-owned calibration classes were explicitly allowlisted for Skops serialization.

### Final CI

Runtime HEAD `bca514ce35fab3e63ef16e487394fea576523d7b`:

```text
ruff check .
All checks passed!

pytest -q
........................................................................ [ 82%]
...............                                                          [100%]
87 passed, 69 warnings in 14.97s
```

GitHub Actions run `34646841551`: **SUCCESS**.

The warning count is dominated by SciPy/scikit-learn L-BFGS-B deprecation warnings exercised repeatedly by the I5 calibration tests, plus the older Starlette/FastAPI deprecation warnings. They are non-blocking but should be reduced in later dependency-maintenance work.

I5 adds 19 passing tests over the 68-test I4 baseline.

Covered I5 evidence includes:

- deterministic dataset generation and SHA-256;
- point-in-time feature contract;
- forbidden leakage feature names;
- label-time cutoff enforcement;
- four-way temporal split;
- ten walk-forward windows;
- four model baselines;
- calibration requires both classes;
- bounded classification/calibration metrics;
- drift OK and ALERT scenarios;
- validation-only champion selection;
- untouched TEST metrics;
- probability qualification gate;
- calibrated model probability shape/range;
- deterministic repeated experiment;
- insufficient-sample demotion to score-only;
- MLflow SQLite tracking and Model Registry smoke test.

## Feast decision

Feast is intentionally deferred in I5.

The current implementation has no demonstrated production online/offline feature-consistency requirement that justifies introducing a feature-store service. The architecture can add Feast later if serving/training skew becomes a real operational requirement rather than a portfolio dependency added for appearance.

## Explicit non-claims

I5 does **not** claim:

- calibrated probability on live or historical real-market data;
- statistically stable real-market alpha;
- real trading profitability;
- production feature-store operation;
- production remote MLflow deployment;
- drift thresholds validated against real market distributions;
- permission for ML to override the deterministic I3 risk veto;
- automated real-money execution readiness.

The synthetic ROC-AUC, Brier, ECE, accuracy, precision and recall values validate the code path and experiment discipline only.

## I5 exit decision

The I5 capability gate is considered satisfied for **ML signal-quality architecture and synthetic out-of-sample calibration mechanics** because:

- feature and target cutoffs are explicit;
- known leakage semantics are rejected;
- train/validation/calibration/test roles are disjoint and chronological;
- four independent baseline model families execute;
- champion selection precedes calibration/test use;
- Platt calibration is measured on untouched TEST data;
- qualification can fail closed to `SCORE_ONLY`;
- drift can revoke probability qualification;
- walk-forward windows are implemented;
- MLflow tracking plus model registration is tested end to end;
- the full repository CI is green.

Real historical-market calibration remains pending evidence and must be completed before a live-market output may be described without the `SYNTHETIC` qualification.
