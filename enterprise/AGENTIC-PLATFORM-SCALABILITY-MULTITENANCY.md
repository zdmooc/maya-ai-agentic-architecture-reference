# Agentic Platform Scalability & Multi-tenancy

Status: **DESIGNED — D-092 M3 / NFR & OPERATING MODEL**

Purpose: define what changes when an enterprise grows from a few agent prototypes to tens, hundreds or thousands of governed agent workloads.

## 1. Scale dimensions

Agentic scale is not only requests per second.

Track at least:

- number of registered agents;
- active agent versions;
- tenants/business domains;
- concurrent sessions/tasks;
- model requests/tokens;
- agent-to-agent task fan-out;
- MCP/tool calls;
- workflow state/memory volume;
- queue depth;
- trace/span cardinality;
- evaluation volume;
- policy decisions;
- cost by agent/tenant/use case.

## 2. Scale stages

### Stage S0 — 1 to 10 agents
Focus:
- explicit owners;
- per-agent identity;
- basic quotas;
- common telemetry;
- manual registry/governance acceptable.

### Stage S1 — 10 to 100 agents
Require:
- machine-readable registry;
- standardized onboarding;
- policy templates;
- automated evaluation gates;
- version lifecycle;
- common dashboards;
- tenant/domain ownership.

### Stage S2 — 100 to 1000 agents
Require:
- automated lifecycle workflows;
- delegated administration;
- policy-as-code;
- hierarchical quotas;
- registry federation/search;
- A2A trust policy;
- fleet-level rollout;
- cost/showback;
- high-cardinality observability design.

### Stage S3 — 1000+ agents / ecosystem
Require:
- multi-region/federated registry strategy;
- strong tenancy boundaries;
- lifecycle automation;
- protocol compatibility management;
- bulk quarantine/kill;
- fleet health and version skew controls;
- explicit capacity engineering and blast-radius segmentation.

The stages are architecture guidance, not current runtime claims.

## 3. Multi-tenancy dimensions

Separate:

- identity tenant;
- runtime/compute tenant;
- data/RAG tenant;
- memory/state tenant;
- model quota tenant;
- tool entitlement tenant;
- observability/audit tenant;
- billing/showback tenant.

A shared runtime does not automatically imply shared data or shared memory.

## 4. Isolation model

Default requirements:

- tenant-aware workload identity;
- namespace/project/account boundary as appropriate;
- data ACL before retrieval;
- separate cache/memory security keys;
- per-tenant model/tool quotas;
- no cross-tenant prompt or tool context;
- audit partitioning and access control;
- resource quotas/limits;
- network policy/egress restrictions;
- negative cross-tenant tests.

## 5. Agent identity cardinality

Avoid one shared identity for a fleet.

Patterns:

- identity per deployed agent/version for high-risk agents;
- identity per logical agent with version-bound policy;
- grouped workload identity only for low-risk homogeneous workers with compensating controls.

Trade-off: finer identity increases governance/credential objects but improves revocation, audit and blast-radius control.

## 6. Quotas and budgets

Hierarchical limits:

```text
Enterprise
 -> business domain
   -> tenant
     -> application
       -> agent
         -> user/session/task
```

Control:

- requests;
- concurrent tasks;
- tokens;
- model/provider spend;
- tool invocations;
- A2A fan-out/depth;
- runtime seconds;
- memory/state size;
- GPU/CPU where private serving applies.

Denial-of-wallet is an SRE/security problem, not only FinOps.

## 7. State and memory

Classify explicitly:

- ephemeral request context;
- session state;
- durable workflow state;
- user memory;
- enterprise knowledge;
- audit/evidence.

Rules:

- no implicit promotion from session context to durable memory;
- tenant/user partitioning;
- TTL and deletion;
- encryption and access control;
- versioned schema;
- backup/recovery only where durability is required;
- memory unavailable must degrade explicitly.

## 8. A2A fan-out and backpressure

Agent-to-agent collaboration can amplify load.

Controls:

- max delegation depth;
- max children/fan-out;
- per-task deadline;
- total token/time budget;
- queue/broker for long work;
- bounded retries;
- circuit breaker;
- cancellation propagation;
- priority classes;
- admission control.

Example:

```text
1 request
 -> 5 agents
   -> 5 peers each
      = 25 downstream tasks
```

Without limits, recursive delegation becomes a capacity and cost incident.

## 9. MCP/tool capacity

Treat tools as dependencies with their own budgets:

- QPS/concurrency limits;
- connection pools;
- timeout;
- bulkhead;
- rate limits;
- dependency-specific retry;
- mutation serialization/idempotence where needed;
- degradation mode.

Do not scale agents faster than authoritative downstream systems can safely accept.

## 10. Model serving and provider capacity

Track separately:

- provider RPM/TPM/concurrency;
- private-model replicas;
- queue depth;
- TTFT;
- tokens/s;
- GPU/CPU/memory saturation;
- cold start;
- batching;
- context length distribution;
- fallback capacity.

Agent autoscaling without model-capacity controls can create retry storms.

## 11. Observability at fleet scale

Required dimensions:

- agent_id/version;
- tenant/domain;
- model alias/actual provider;
- A2A peer;
- MCP server/tool;
- policy decision;
- autonomy level;
- task outcome;
- cost/token;
- error/fallback.

Protect telemetry systems from unbounded cardinality:

- controlled labels;
- logs/traces for high-cardinality IDs;
- metrics for bounded dimensions;
- sampling policy;
- retention tiers;
- sensitive-data redaction.

## 12. Rollout and version skew

Support:

- canary agent version;
- percentage/tenant rollout;
- pinned peer compatibility;
- rollback;
- protocol deprecation;
- prompt/model/tool policy version pinning.

A2A peers and MCP clients/servers may evolve independently; compatibility tests are mandatory.

## 13. Kill switch and quarantine

Fleet controls must support:

- one agent/version disable;
- one tenant disable;
- one tool/MCP server deny;
- one A2A peer block;
- one model/provider block;
- emergency global policy.

Quarantine should preserve evidence while stopping unsafe execution.

## 14. Capacity evidence

Before a scale claim, measure representative:

- request/task throughput;
- p50/p95/p99 latency;
- queue depth and drain time;
- agent concurrency;
- model saturation;
- tool dependency saturation;
- trace ingestion;
- cost per successful task;
- failure/retry rate.

Do not extrapolate 1000-agent capacity from a single-node CRC lab.

## 15. Truth boundary

Current status: **DESIGNED**.

No claim of production-scale multi-tenant agent fleet is permitted until a runtime test demonstrates isolation, load, failure and operational controls at representative scale.
