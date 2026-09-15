# AI Performance Budget Template

Status: **REFERENCE TEMPLATE / ARCHITECTURE CAPACITY**

Purpose: define end-to-end performance budgets for AI applications before implementation or benchmarking.

## 1. User journey

Document one measurable journey:

`User -> Gateway -> Policy -> Retrieval -> Reranking -> Context -> Model -> Tools -> Output validation -> Response`

## 2. End-to-end SLO

Record:

- p50 target;
- p95 target;
- p99 target;
- timeout ceiling;
- streaming TTFT target;
- maximum acceptable degraded-mode latency.

## 3. Component latency budget

| Component | Target p95 | Timeout | Notes |
|---|---:|---:|---|
| API Gateway/IAM | TBD | TBD | identity/network |
| AI Gateway/policy | TBD | TBD | quotas, PII, routing |
| Retrieval | TBD | TBD | vector/lexical/hybrid |
| Reranking | TBD | TBD | optional |
| Model TTFT | TBD | TBD | provider/runtime |
| Decode | TBD | TBD | output length dependent |
| Tool calls | TBD | TBD | per-tool budget |
| Output validation | TBD | TBD | schema/DLP/policy |
| Network overhead | TBD | TBD | cross-zone/cloud |

Rule:

`end-to-end budget >= sum of critical-path budgets + safety margin`.

## 4. Workload assumptions

- requests/second average;
- peak requests/second;
- concurrent sessions;
- average input tokens;
- p95 input tokens;
- average output tokens;
- tool-call rate;
- retrieval rate;
- cacheable request percentage;
- geography/network assumptions.

## 5. AI-specific metrics

- TTFT;
- inter-token latency;
- tokens/second;
- queue time;
- batch size;
- concurrent sequences;
- context length;
- KV-cache usage;
- GPU/CPU utilization;
- VRAM/RAM;
- cache hit ratio;
- fallback activation rate.

## 6. RAG metrics

Performance dimensions:

- embedding latency;
- vector/lexical search latency;
- reranking latency;
- number of retrieved candidates;
- number of final chunks;
- context-token volume;
- index size;
- query concurrency.

Performance must not be optimized by silently reducing retrieval quality below acceptance thresholds.

## 7. Tool / agent performance

For each tool:

- p50/p95 latency;
- timeout;
- retry policy;
- dependency SLA;
- maximum calls per workflow;
- parallel vs sequential execution;
- fail/abstain behavior.

Agent loop budgets must be bounded by:

- maximum steps;
- maximum wall-clock time;
- maximum tool calls;
- maximum token/cost budget.

## 8. Capacity assumptions

For private inference:

- model size;
- precision/quantization;
- model weight memory;
- KV-cache estimate;
- runtime overhead;
- maximum context;
- target concurrency;
- HA replicas;
- headroom.

All pre-benchmark values must be labelled `ESTIMATE`.

## 9. Cache architecture

Document separately:

- response cache;
- semantic cache;
- prefix/KV cache;
- retrieval cache;
- tool-result cache.

For every cache, define:

- key dimensions;
- identity/tenant isolation;
- TTL;
- invalidation;
- model/prompt/index version coupling;
- sensitive-data policy.

## 10. Scaling strategy

Define:

- horizontal scaling trigger;
- vertical scaling boundary;
- GPU node-pool behavior;
- queue/admission control;
- min/max replicas;
- scale-up/down delays;
- provider quota ceilings.

## 11. Degraded modes

Examples:

- primary model slow -> fallback model;
- reranker unavailable -> baseline retrieval if quality policy permits;
- external provider unavailable -> private model or explicit unavailable response;
- tool slow -> partial answer/abstain/escalate;
- RAG stale -> no-answer/warning;
- agent workflow too slow -> deterministic workflow path where available.

## 12. Cost/performance trade-off

Measure together:

- latency;
- throughput;
- quality;
- cost/request;
- cost/useful answer;
- GPU utilization;
- cache hit rate.

A faster or cheaper configuration is not acceptable if quality/security/NFRs regress below threshold.

## 13. Benchmark plan

A benchmark is required when material uncertainty exists.

Define before test:

- workload dataset;
- warm/cold conditions;
- concurrency levels;
- context/output sizes;
- test duration;
- metrics;
- pass/fail thresholds;
- infrastructure/version;
- model/runtime version.

## 14. Result status

Every value is one of:

- `TARGET`
- `ESTIMATE`
- `MEASURED-LAB`
- `MEASURED-PREPROD`
- `MEASURED-PRODUCTION`

Never present an estimate as measured performance.