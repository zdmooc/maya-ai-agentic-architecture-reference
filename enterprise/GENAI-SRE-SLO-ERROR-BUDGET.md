# GenAI SRE — SLI, SLO and Error Budget Model

Status: **DESIGNED — SRE REFERENCE / PRODUCTION EVIDENCE SEPARATE**

Purpose: adapt SRE discipline to enterprise GenAI systems where reliability depends on more than endpoint uptime.

## 1. Service-level perspective

A GenAI application is a chain:

`client -> gateway -> policy -> retrieval/context -> model -> tools/agents -> deterministic controls -> response/action`

Reliability must be measured end-to-end from the user/business perspective.

## 2. Candidate SLIs

### Availability / request success
- valid request success rate;
- non-5xx response rate;
- workflow completion rate;
- successful fallback/degradation rate.

### Quality / correctness
- grounded-answer rate;
- citation-correctness rate;
- abstention correctness;
- schema-valid output rate;
- tool-selection/tool-call success;
- human-review rejection rate;
- stale-evidence rate.

### Performance
- end-to-end p50/p95/p99 latency;
- time to first token;
- tokens/second or decode latency;
- retrieval/rerank latency;
- tool-call latency;
- queue delay.

### Policy / safety
- correct policy-denial rate;
- unauthorized-tool-call prevention;
- prompt-injection test pass rate;
- PII/security control violation rate.

### Capacity / platform
- model endpoint availability;
- GPU/CPU saturation;
- queue depth;
- vector-store availability;
- provider quota exhaustion;
- cache hit ratio.

## 3. SLO examples

Illustrative only; every project sets its own targets.

- 99.9% successful eligible API requests over 30 days.
- p95 end-to-end latency under target budget for interactive traffic.
- 99% schema-valid outputs for machine-consumed responses.
- 99% citation correctness on approved regression set.
- zero tolerated unauthorized production tool execution.
- stale-evidence rate below agreed threshold.

Do not copy example percentages blindly. SLOs must come from business criticality and user expectations.

## 4. Error budget

If an availability SLO is 99.9% over a period, the remaining 0.1% is the error budget for that objective.

For AI systems, error budget can also be applied to quality/service indicators, for example allowable grounded-answer failures or p95 latency violations, provided the metric and measurement method are stable.

Error budget is a decision tool:

- healthy budget -> normal feature/change velocity;
- budget burning too fast -> slow risky changes, prioritize reliability;
- budget exhausted -> production reliability work takes priority until risk is restored.

## 5. Multi-dimensional reliability

A system can have 100% HTTP uptime and still be operationally bad because:

- RAG retrieves stale/irrelevant evidence;
- model answers are ungrounded;
- tools fail;
- provider rate limits create unacceptable latency;
- HITL queue blocks workflows;
- policy engine incorrectly denies/permits actions.

Therefore architecture reviews should define a small set of user-relevant SLIs rather than only infrastructure uptime.

## 6. Dependency failure modes

For each dependency define:

- failure detection;
- timeout;
- retry/bounded retry;
- circuit breaker;
- fallback eligibility;
- degraded behavior;
- user-facing status;
- alert/runbook;
- recovery/rollback.

Dependencies include:
- identity/IAM;
- gateway;
- vector store/search;
- model provider/private serving;
- tools/APIs/MQ/Kafka;
- session/workflow state;
- policy engine;
- human approval service;
- observability stack.

## 7. GenAI degradation patterns

Safe examples:
- LLM unavailable -> deterministic/search-only response where meaningful;
- vector search degraded -> return `NO_ANSWER` rather than invent;
- one provider unavailable -> route only to a policy-eligible fallback;
- tool unavailable -> explain inability and stop sensitive action;
- stale source -> `DATA_STALE` status;
- budget exceeded -> downgrade eligible non-critical request to cheaper approved model or defer.

Unsafe examples:
- bypass authorization because policy service is unavailable;
- silently route confidential data to an ineligible public provider;
- use stale evidence without marking it;
- retry non-idempotent actions indefinitely.

## 8. Observability dimensions

Trace at least:
- request/correlation ID;
- gateway/policy decision;
- retrieval queries/results metadata;
- model alias/version;
- prompt/index/tool versions;
- tool calls;
- HITL transitions;
- latency/cost;
- outcome/evaluation status.

Sensitive content logging must remain policy-controlled.

## 9. Error-budget governance

Architecture/SRE review should define:

1. SLI owner.
2. Measurement source.
3. SLO window.
4. Budget calculation.
5. Burn-rate alert thresholds.
6. Change-freeze/reliability-action rules.
7. Exceptions/acceptance authority.
8. Post-incident learning.

## 10. POC/evidence trigger

No standalone POC by default. Runtime evidence becomes necessary when a mission claims production reliability or SRE maturity. Evidence may include load tests, provider-failure drills, stale-RAG scenarios, fallback tests, SLO dashboards and recovery exercises.
