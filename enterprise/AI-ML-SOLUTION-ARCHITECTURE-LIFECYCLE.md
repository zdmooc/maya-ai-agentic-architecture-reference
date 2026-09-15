# AI/ML Solution Architecture Lifecycle

Status: **DESIGNED — ARCHITECT REFERENCE**

Purpose: give the Solution Architect one lifecycle spanning **deterministic software, classic ML and GenAI**, without requiring Data Scientist-level implementation depth.

## 1. Business framing

Define:
- business capability/outcome;
- users and affected stakeholders;
- measurable KPI;
- acceptable risk;
- expected decision/action;
- latency/availability/cost envelope;
- human oversight requirement.

First decision:

`Can deterministic software/search/rules solve this adequately?`

If yes, AI may not be justified.

## 2. Workload classification

### Deterministic
Use for:
- explicit business rules;
- authorization;
- transaction controls;
- arithmetic;
- exact validation.

### Classic ML
Use for:
- classification;
- regression;
- ranking;
- forecasting;
- anomaly detection;
- calibrated predictive scores.

### GenAI
Use for:
- language understanding/generation;
- semantic knowledge interaction;
- document synthesis;
- multimodal interpretation;
- dynamic tool orchestration/agents.

### Hybrid
Combine only when responsibilities are explicit.

Example:

`rules -> ML risk score -> RAG/LLM synthesis -> deterministic policy -> HITL`

## 3. Data / knowledge architecture

Classic ML asks:
- training/validation/test datasets;
- feature/data pipelines;
- labels/targets;
- train/serve consistency;
- drift/quality monitoring.

GenAI asks:
- prompt/context sources;
- corpus/knowledge lifecycle;
- embeddings/indexes;
- ACL/classification;
- prompt/index/tool lineage;
- feedback/eval datasets.

Both require:
- ownership;
- provenance;
- privacy/security;
- retention/deletion;
- quality controls.

## 4. Model strategy

Classic ML:
- build/train versus managed/pretrained;
- model class and complexity;
- explainability needs;
- batch/online serving;
- retraining lifecycle.

GenAI:
- managed foundation model versus private/open-weight;
- model capability/quality;
- prompt-only vs RAG vs workflow vs agent vs fine-tuning;
- provider/placement policy;
- inference/cost constraints.

## 5. Evaluation strategy

Classic ML examples:
- precision/recall/F1;
- ROC-AUC;
- calibration;
- RMSE/MAE;
- business threshold metrics.

GenAI examples:
- exact/functional correctness;
- grounding/faithfulness;
- citation correctness;
- retrieval relevance/recall;
- abstention;
- LLM-as-judge with controls;
- agent/tool success;
- safety/security regression.

Both require representative data and baseline/candidate comparison.

## 6. Architecture and NFRs

Define:
- application/service boundaries;
- integration/API/event patterns;
- state management;
- security/privacy;
- latency/throughput;
- availability/resilience;
- observability;
- scalability/capacity;
- cost/FinOps;
- portability/reversibility;
- audit/compliance.

## 7. Platform decision

Capabilities may be provided by:
- existing enterprise platform;
- OpenShift/OpenShift AI;
- managed cloud AI/ML services;
- hybrid combination.

Architect selection criteria:
- data residency/classification;
- workload type;
- team skill;
- SLA;
- scale;
- model availability;
- GPU/CPU needs;
- economics;
- governance;
- existing enterprise standards;
- reversibility.

## 8. MLOps / LLMOps lifecycle

### Shared concerns
- source control;
- artifact/version registry;
- CI/CD/promotion;
- environment separation;
- evaluation gates;
- deployment/rollback;
- observability;
- incident handling;
- retirement.

### Additional ML concerns
- training pipelines;
- feature/data versioning;
- drift;
- retraining.

### Additional GenAI concerns
- prompt/version lifecycle;
- corpus/index lifecycle;
- model-provider changes;
- tool registry;
- RAG/agent evaluation;
- token/cost budgets;
- guardrails/HITL.

## 9. Production operations

Define:
- SLI/SLO/error budget;
- support/runbook owner;
- capacity and scaling;
- fallback/degraded modes;
- backup/restore/rebuild;
- cost monitoring;
- periodic quality/risk review;
- model/data/provider deprecation handling.

## 10. Governance gates

Recommended gates:

1. Business justification.
2. Workload/pattern classification.
3. Data/privacy/security eligibility.
4. Architecture/NFR review.
5. Model/evaluation strategy approval.
6. POC only if material uncertainty remains.
7. Production-readiness/SRE review.
8. Go-live approval.
9. Periodic re-evaluation.
10. Retirement/deletion.

## 11. Architect versus specialist depth

The AI Solution Architect must understand **why and where** each lifecycle component exists and what trade-off it creates.

The architect does not need to personally:
- derive ML algorithms;
- tune hyperparameters deeply;
- implement training loops;
- write every RAG/agent component;
- administer every GPU runtime.

The architect must be able to challenge and integrate specialist decisions into one coherent solution.

## 12. Interview shorthand

When asked “Are you ML or GenAI?”, the architecture answer is:

`Enterprise AI architecture spans deterministic controls, classic ML and GenAI. The workload determines the pattern; the platform and governance must support the lifecycle of each without forcing every problem into an LLM.`
