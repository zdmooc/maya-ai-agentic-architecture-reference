# GenAI Online Experimentation Pattern

Status: **DESIGNED — PRODUCT/ARCHITECTURE EVIDENCE PATTERN**

Purpose: define when and how A/B testing or controlled online experiments can validate whether a GenAI change improves real user/business outcomes after offline safety and quality gates have passed.

## 1. Offline evaluation first

Online experiments do not replace offline evaluation.

Before exposing users to a candidate:
- security/privacy controls pass;
- blocking safety tests pass;
- functional/schema tests pass;
- representative offline quality evaluation passes;
- latency/cost are within provisional limits;
- rollback path exists.

## 2. Appropriate experiment targets

Examples:
- prompt version;
- eligible model alias;
- retrieval/reranking strategy;
- context compression strategy;
- answer presentation/UX;
- cache/routing behavior;
- agent workflow variant;
- escalation/HITL UX;
- recommendation or drafting strategy.

Do not experiment by weakening hard security, entitlement, payment-risk, regulatory or privacy controls.

## 3. Hypothesis

Every experiment needs an explicit hypothesis:

`Changing X for eligible users will improve Y without violating guardrail Z.`

Example:

`Hybrid retrieval + reranking increases accepted grounded answers while keeping p95 latency and cost/useful-answer within agreed limits.`

## 4. Metrics

### Primary outcome
Choose one main business/user metric when possible:
- useful/accepted answer rate;
- task completion;
- support resolution time;
- operator time saved;
- user satisfaction;
- escalation rate;
- conversion/adoption where appropriate.

### Guardrail metrics
Always monitor constraints such as:
- safety/security violation rate;
- hallucination/grounding failure;
- citation correctness;
- p95/p99 latency;
- cost/request/useful answer;
- error rate;
- HITL rejection rate.

A candidate that improves the primary metric but violates a guardrail is not a success.

## 5. Experiment eligibility

Segment users/requests only when segmentation is lawful, ethical and compatible with product/risk policy.

Exclude use cases where random assignment could create unacceptable harm or inequitable treatment without explicit governance approval.

## 6. Version and lineage

Each experiment arm records:
- experiment ID;
- model alias/version;
- prompt version;
- index/corpus version;
- router/policy version;
- tools/workflow version;
- start/end time;
- target population;
- metrics definition.

## 7. Statistical discipline

Architecture/product review should require:
- predeclared hypothesis and primary metric;
- expected effect size where possible;
- sample-size/power thinking;
- experiment duration sufficient for representative traffic;
- avoidance of repeated premature peeking/decision-making;
- awareness of Type I/Type II errors;
- handling of multiple comparisons where applicable.

The architect need not be the statistician, but must ensure the product decision is evidence-driven rather than based on a visually appealing dashboard.

## 8. Rollback / stop conditions

Immediate stop examples:
- security/privacy violation;
- material safety regression;
- significant error/latency/cost breach;
- provider instability;
- unacceptable business/user harm.

Rollback must be technically available before the experiment begins.

## 9. RAG experiment examples

Candidate dimensions:
- lexical vs vector vs hybrid retrieval;
- top-k;
- reranker;
- chunk strategy;
- context budget;
- query expansion.

Measure retrieval and final-answer effects separately.

## 10. Agent experiment examples

Candidate dimensions:
- deterministic workflow vs agentic planning;
- tool set;
- max steps;
- memory strategy;
- planner model;
- escalation threshold.

Guardrails include loops, tool misuse, time/cost budgets and HITL rejection.

## 11. Relationship with feature flags and canaries

- **Feature flag** controls exposure/configuration.
- **Canary** reduces deployment/reliability blast radius.
- **A/B test** estimates causal product/quality impact between variants.

They may be combined but serve different purposes.

## 12. Decision record

At experiment close, record:
- hypothesis;
- result/confidence;
- primary and guardrail metrics;
- known caveats;
- segment effects;
- cost impact;
- architecture implications;
- promote/reject/retest decision;
- ADR or backlog reference.

## 13. POC policy

No experiment is required merely because a book describes A/B testing. Activate this pattern only when online user/business evidence is necessary to choose between already-safe candidate designs.
