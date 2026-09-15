# Designing Machine Learning Systems — Architecture Alignment

Status: **DESIGNED — SYSTEMS/PRODUCTION EXTRACTION COMPLETE / DATA-SCIENCE DETAIL DEPRIORITIZED**

Source: *Designing Machine Learning Systems* — Chip Huyen, O'Reilly, 2022.

Public references checked:
- O'Reilly: https://www.oreilly.com/library/view/designing-machine-learning/9781098107956/
- Official GitHub repository: https://github.com/chiphuyen/dmls-book

Purpose: extract the book's systems-design value for an **AI/ML Solution Architect**, not its implementation detail.

## 1. Architecture-relevant book themes

- when ML is justified;
- business and ML objectives;
- reliability, scalability, maintainability and adaptability;
- data engineering and dataflow;
- training/evaluation lineage;
- deployment and prediction services;
- batch vs online prediction;
- compression/quantization implications;
- data distribution shifts;
- monitoring and observability;
- continual learning/retraining;
- test-in-production patterns: shadow, A/B, canary;
- MLOps infrastructure/platform decisions;
- build vs buy;
- human/organizational side and Responsible AI.

## 2. Current repository coverage

Already covered:
- unified classic-ML/GenAI lifecycle;
- AI/ML NFRs;
- model registry/serving concepts;
- OpenShift AI/KServe/vLLM;
- evaluation and calibration;
- observability/SRE;
- A/B experimentation;
- AI platform capability map;
- risk/Responsible AI/RACI;
- data/knowledge governance.

## 3. New gap closed

### GAP-DMLS-01 — Explicit production ML monitoring/drift/retraining architecture

Closed by `ML-PRODUCTION-MONITORING-DRIFT-LIFECYCLE.md`.

The current repository already contains drift mechanics inside ML iterations, but this book makes the full architect loop explicit:

`data quality -> prediction service -> outcome/business metric -> drift detection -> investigation -> retraining decision -> candidate evaluation -> controlled deployment -> monitoring`

This is important because classic ML systems degrade even when software does not change.

## 4. System-design principles retained

### Reliability
A reliable ML system must handle both software failures and ML-specific failures such as bad/stale inputs, distribution shift, label delay and model degradation.

### Scalability
Scale concerns include:
- data volume/velocity;
- training compute;
- inference QPS/concurrency;
- feature/data access;
- batch vs online paths;
- monitoring volume.

### Maintainability
Require versioned data/model/code/config, clear ownership, reproducible evaluation and manageable platform interfaces.

### Adaptability
Architecture must anticipate model/data/business change, not freeze the first successful model.

## 5. Batch versus online prediction

Architect choice depends on:
- freshness requirement;
- latency/SLA;
- event frequency;
- input availability;
- cost;
- operational complexity.

Do not force online inference where batch scoring satisfies the business process.

## 6. Deployment patterns retained

- shadow deployment for production-like evidence without affecting decisions;
- canary for limited production exposure;
- A/B testing for causal product comparison;
- staged promotion/rollback;
- champion/challenger where appropriate.

These patterns have different objectives and should not be conflated.

## 7. Monitoring principle

Monitor more than model accuracy:
- input/data quality;
- data distribution;
- feature health;
- prediction distribution;
- calibration/quality when labels arrive;
- service SLO;
- business KPI;
- cost/capacity.

A delayed ground-truth label does not justify monitoring nothing in the meantime.

## 8. Continual learning principle

Continual learning does not mean autonomous uncontrolled retraining.

Architectural stages:
1. detect change;
2. determine whether retraining is justified;
3. construct/validate new data;
4. train candidate;
5. offline evaluate;
6. controlled test/deploy;
7. monitor and rollback if necessary.

Regulated/high-impact models require explicit governance and approval.

## 9. Infrastructure / MLOps platform lesson

Platform investment should match organizational scale and specialization. Avoid building a large internal ML platform before repeated needs justify it.

Core reusable capabilities:
- storage/compute;
- standardized environments;
- scheduling/orchestration;
- experiment tracking;
- model registry;
- deployment/serving;
- monitoring;
- feature/data services where justified.

This maps to the broader `GENAI-PLATFORM-CAPABILITY-MAP.md` for enterprise AI.

## 10. Human/organizational lesson

Production ML is cross-functional. Architecture must connect business, data science/ML, software/platform, security/risk and operations. A technically accurate model with no operating owner or poor user workflow is not a successful system.

## 11. Material deliberately skipped

Not promoted to core architect curriculum:
- detailed feature-engineering techniques;
- sampling formulas;
- hands-on training implementation;
- deep AutoML/ensemble specifics.

The architect needs awareness and trade-off understanding, not practitioner depth in every modeling technique.

## 12. POC policy

No mandatory POC.

Future evidence only when a mission requires:
- model drift monitoring;
- real-time vs batch architecture comparison;
- shadow/canary rollout;
- retraining pipeline;
- ML platform architecture.

## 13. Interview outcomes

An AI/ML Solution Architect should be able to answer:
- Why can an ML system degrade without a software change?
- What do you monitor before ground-truth labels arrive?
- How do batch and online prediction architectures differ?
- When should retraining occur?
- What is the difference between shadow, canary and A/B deployment?
- How do you design for reliability, scalability, maintainability and adaptability in ML?

## 14. Conclusion

The book adds depth to **production ML system lifecycle and adaptability**. The unique gap for this repository is now captured in a dedicated monitoring/drift/retraining architecture reference.
