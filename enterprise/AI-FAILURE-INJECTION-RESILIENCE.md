# AI Failure Injection & Resilience

Status: **DESIGNED — RESILIENCE TEST CATALOG / NO EXECUTION CLAIM**

Purpose: define AI-specific failure scenarios that an enterprise AI platform or application should be able to detect, contain and recover from safely.

## 1. Principle

Resilience testing must cover failures that are specific to AI systems in addition to normal distributed-system failures.

The objective is not chaos for its own sake. Each injected failure must validate one or more NFRs: availability, graceful degradation, safety, auditability, rollback, provider portability, latency or cost containment.

## 2. LLM/provider failure scenarios

Inject or simulate:

- provider timeout;
- HTTP 5xx;
- rate limit / quota exhaustion;
- authentication failure;
- model alias points to unavailable model;
- provider returns malformed structured output;
- context-window rejection;
- latency spike;
- unexpectedly high token usage;
- provider region unavailable.

Expected controls:

- bounded timeout/retry;
- circuit breaker where appropriate;
- approved fallback model/provider;
- fail-closed for high-risk actions;
- explicit degraded-mode response;
- cost/token cap;
- audit of the fallback path.

## 3. RAG failure scenarios

Inject or simulate:

- vector store unavailable;
- empty retrieval;
- stale index;
- corrupted or partial index;
- ACL metadata missing;
- retrieval returns conflicting evidence;
- document ingestion lag;
- bad embedding version mismatch;
- malicious or poisoned document;
- citation source unavailable.

Expected controls:

- abstain or degrade instead of hallucinating;
- preserve ACL enforcement;
- identify stale/unknown evidence;
- rebuild derived index from authoritative source when possible;
- version and rollback index/embedding changes;
- route low-confidence/conflicting results to review.

## 4. Agent/MCP failure scenarios

Inject or simulate:

- tool timeout;
- tool returns malformed payload;
- unauthorized tool request;
- tool server unavailable;
- repeated/looping plan;
- excessive number of tool calls;
- conflicting tool outputs;
- stale agent memory;
- MCP/server authentication failure;
- tool output contains injection content.

Expected controls:

- bounded step/tool-call budget;
- allowlist + scopes;
- input/output schema validation;
- timeout/rate limit;
- deterministic stop conditions;
- no privilege escalation;
- no high-impact autonomous execution;
- HITL where policy requires it.

## 5. AI Gateway failure scenarios

Inject or simulate:

- gateway unavailable;
- routing policy misconfiguration;
- budget service unavailable;
- model alias misresolution;
- provider eligibility service unavailable;
- quota counter failure;
- telemetry sink unavailable.

Expected controls:

- explicit safe failure mode;
- no bypass around gateway policy for sensitive workloads;
- cached policy only with bounded validity when explicitly designed;
- observable failure and correlation ID;
- no untracked direct-provider fallback.

## 6. Model serving failure scenarios

For private KServe/vLLM-style serving:

- pod/model server crash;
- model load failure;
- out-of-memory / accelerator pressure;
- queue saturation;
- slow prefill/decode;
- failed rollout;
- incompatible model artifact;
- node/zone loss where applicable.

Expected controls:

- readiness/liveness behavior;
- capacity limits/backpressure;
- rollout rollback;
- previous known-good version;
- replica/capacity strategy appropriate to the SLO;
- explicit distinction between CRC/lab proof and production HA.

## 7. Evaluation pipeline failures

Simulate:

- candidate model regresses on golden dataset;
- RAG grounding score regresses;
- prompt injection regression fails;
- latency exceeds budget;
- cost exceeds budget;
- evaluator unavailable or non-reproducible;
- new model/provider violates placement policy.

Expected result: promotion is blocked until the relevant gate is satisfied or an approved exception exists.

## 8. Payment Investigation Agent scenario

For the I19 payment use case, an AI investigation may consume:

```text
payment status + ISO 20022 events + Kafka/MQ history + logs + metrics + runbooks + RAG
```

Failure exercises should verify that missing or contradictory evidence produces an explicit `UNKNOWN / INSUFFICIENT_EVIDENCE / REVIEW_REQUIRED` state rather than a fabricated root cause.

The agent may recommend reconciliation or investigation actions, but deterministic controls and human approval remain authoritative for sensitive operations.

## 9. Evidence format

Each executed scenario should capture:

- scenario ID;
- injected fault;
- start/end time;
- expected behavior;
- observed behavior;
- telemetry/correlation IDs;
- fallback/degraded mode;
- safety/HITL outcome;
- recovery time;
- residual issue;
- status: PASS/PARTIAL/FAIL.

## 10. Repository mapping

- SRE/error budgets: `GENAI-SRE-SLO-ERROR-BUDGET.md`.
- AI evaluation: I14.
- AI security/policy: I16.
- private serving: I17.
- provider routing: I18.
- payment investigation: I19.
- executable agent/RAG runtime baseline: `zdmooc/TradeOps-GenAI-Integration`.

No scenario in this document is considered executed until evidence exists.