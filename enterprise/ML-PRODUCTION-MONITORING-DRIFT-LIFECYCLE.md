# ML Production Monitoring, Drift & Retraining Lifecycle

Status: **DESIGNED — CLASSIC ML PRODUCTION REFERENCE**

Purpose: provide an architect-level lifecycle for classic ML systems whose quality can degrade because data and business conditions change.

## 1. Monitoring layers

### Data quality
Monitor:
- schema/type violations;
- missing values;
- range violations;
- freshness;
- duplicate/out-of-order events;
- source availability;
- unexpected category/cardinality changes.

### Distribution monitoring
Monitor:
- input/feature distributions;
- prediction-score distribution;
- class balance;
- segment-level behavior;
- training-vs-serving skew where relevant.

### Model quality
When labels/outcomes become available:
- task metric drift;
- calibration drift;
- false-positive/false-negative behavior;
- segment disparities;
- threshold effectiveness.

### Service health
Monitor:
- availability;
- p95/p99 latency;
- throughput;
- error rate;
- queue depth;
- CPU/GPU/memory;
- dependency failures.

### Business outcome
Monitor:
- business KPI tied to model use;
- operator overrides;
- downstream decision success;
- economic/risk impact.

## 2. Drift taxonomy

Architect-level distinctions:

- **data/covariate shift** — input distribution changes;
- **label/prior shift** — target prevalence changes;
- **concept shift** — relationship between inputs and target changes;
- **schema/data-pipeline drift** — technical representation changes;
- **business-policy drift** — model objective/threshold no longer matches current process.

A statistical distribution change is not automatically a production incident. Impact must be interpreted against task/business metrics.

## 3. Delayed labels

Many banking/insurance outcomes arrive later.

Before ground truth is available, monitor proxies:
- input quality/distribution;
- score distribution;
- confidence/calibration proxies;
- operator overrides;
- process/business anomalies;
- known control thresholds.

When labels arrive, backfill true performance evaluation.

## 4. Drift response workflow

`signal -> validate data pipeline -> assess segment/business impact -> identify root cause -> decide action`

Possible actions:
- no action/continue observation;
- adjust alert threshold;
- repair data/source pipeline;
- recalibrate threshold/model;
- retrain;
- rollback to prior model;
- disable model and degrade to rules/manual process.

## 5. Retraining trigger

Do not retrain simply because “drift detected.”

Retraining should consider:
- material quality degradation;
- business KPI degradation;
- enough new representative labels/data;
- regulatory/model-validation rules;
- expected benefit versus operational risk/cost.

## 6. Retraining lifecycle

1. Freeze/version source data.
2. Validate quality/lineage.
3. Create train/validation/test splits without leakage.
4. Train candidate.
5. Compare against current champion/baseline.
6. Validate calibration, segment behavior and risk controls.
7. Approve candidate.
8. Deploy via shadow/canary/champion-challenger as appropriate.
9. Monitor production outcomes.
10. Roll back if guardrail/SLO thresholds fail.

## 7. Deployment patterns

### Shadow
Candidate receives production traffic/data but does not influence live decisions.

Use for:
- realistic performance/latency evidence;
- score comparison;
- safe pre-production validation.

### Canary
Candidate controls a limited fraction/segment of eligible production decisions.

Use for:
- blast-radius control;
- operational validation.

### A/B
Randomized variants compare product/business effects.

Use only when ethical/regulatory and statistically appropriate.

### Champion/challenger
Current approved model remains champion while challengers are evaluated against it.

Useful in governed model-lifecycle environments.

## 8. Version and lineage

Every production prediction should be traceable to:
- model/version;
- feature/data version where practical;
- code/config version;
- threshold/policy version;
- timestamp;
- correlation/business event ID.

## 9. Architecture roles

- Data owner: source meaning/quality.
- ML team: model quality/retraining.
- Platform/MLOps: pipelines/registry/deployment/monitoring.
- Solution Architect: end-to-end lifecycle/NFR/integration trade-offs.
- Risk/Model Validation: approval/controls where regulated.
- Operations: production response/runbook.
- Business owner: KPI/value/acceptable residual risk.

## 10. Fail-safe behavior

Define what happens when:
- model endpoint unavailable;
- features missing/stale;
- quality confidence too low;
- critical drift threshold breached;
- downstream system unavailable.

Safe degradation may include deterministic rules, prior approved model, queue/defer or manual review depending on use case.

## 11. Architecture review checklist

Ask:
1. What labels/outcomes arrive and how late?
2. Which drift signals are monitored before labels?
3. Who decides retraining?
4. How is the new candidate evaluated?
5. What deployment strategy limits risk?
6. How quickly can rollback occur?
7. What is the manual/deterministic fallback?
8. How are segment/fairness effects monitored?
9. Which model/data/policy versions are auditable?
10. What business KPI proves the model is still useful?
