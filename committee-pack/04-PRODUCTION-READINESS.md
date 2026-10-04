# Production Readiness — Enterprise Agentic AI

Status: **DESIGNED — PRODUCTION GATE TEMPLATE**

Purpose: define minimum evidence before an Agentic AI use case is promoted to production or to a higher autonomy level.

## 1. Gate summary

| Domain | Minimum gate |
|---|---|
| Business | owner, outcome, baseline KPI and failure impact defined |
| Architecture | approved target/transition architecture and ADRs |
| Data/RAG | classification, ACL, lineage, retention/deletion and rebuild path |
| Model | approved model/provider/version/placement and fallback policy |
| Agent | bounded state/workflow, termination and conflict behavior |
| Tools/MCP | allowlist, schemas, least privilege, rate/timeout, autonomy classification |
| HITL | authenticated reviewer flow for all L2 actions |
| Identity | user/workload/tool identities traceable end to end |
| Security | threat model + prompt/RAG/tool negative tests pass |
| Evaluation | golden/adversarial set and promotion thresholds pass |
| Observability | logs/metrics/traces/audit/SLO dashboards and alerts |
| Resilience | dependency failure, timeout, fallback, restart/recovery tests |
| Operations | runbooks, support/escalation/on-call ownership |
| Compliance | applicability review and required DPO/RSSI/legal inputs |
| Supply chain | SBOM/AI-BOM, dependency/model/tool provenance |
| FinOps | budget/token/provider/GPU cost controls and showback basis |
| Rollback | model/prompt/index/policy/application rollback path proven |

## 2. RAG readiness

Required evidence:

- source inventory and ownership;
- immutable source/version metadata;
- ACL/entitlement negative tests;
- retrieval relevance/grounding tests;
- citation correctness;
- abstention/no-answer behavior;
- poisoned/untrusted document scenario;
- deletion/rebuild path;
- cache isolation and invalidation policy;
- index/embedding/prompt version traceability.

## 3. Agent/tool readiness

Required evidence:

- maximum step/tool/time/token budget;
- allowed state transitions;
- explicit stop/error/conflict/veto states;
- per-tool autonomy level;
- server-side authorization;
- invalid/malicious argument tests;
- tool timeout/unavailability behavior;
- duplicate/idempotence handling for mutation;
- HITL approval binding for L2;
- blast-radius limit and rollback for sensitive action.

## 4. Model/provider readiness

Required evidence:

- approved model alias and pinned deployment/version where applicable;
- data/provider eligibility;
- measured representative quality/latency/cost where required;
- provider outage/fallback behavior;
- context/token limits;
- safety/output controls;
- exit/substitution strategy for critical dependency.

## 5. Observability readiness

Minimum common correlation across:

`request -> retrieval -> model -> agent state -> tool -> policy -> approval -> target system -> response`.

Track:

- task success/failure;
- retrieval/grounding/citation quality;
- tool success/denial;
- approval rate and time;
- latency p50/p95/p99 where material;
- token/cost;
- security denials;
- error/fallback/timeout;
- business outcome KPI.

## 6. Promotion levels

### DESIGN -> IMPLEMENTED

Code/config/policies exist and are reviewable.

### IMPLEMENTED -> TESTED

Automated/controlled tests prove intended and negative behavior.

### TESTED -> DEPLOYED

Artifacts are running in the target-like environment with deployment evidence.

### DEPLOYED -> VERIFIED

Representative end-to-end scenarios, observability, failure/recovery and operational controls are evidenced.

No level is inferred from documentation alone.

## 7. Autonomy promotion gate

Moving a tool/use case to a higher autonomy level requires a separate decision. Production deployment does not automatically permit L3/L4 autonomy.

L2 -> L3 requires at minimum:

- low-risk/reversible action;
- deterministic policy bounds;
- proven idempotence;
- blast-radius constraint;
- rollback/compensation test;
- least-privilege identity;
- high-quality monitoring;
- security/evaluation regression pass;
- named authority accepting residual risk.

## 8. Go/No-Go record

Final record should state:

```yaml
use_case: string
release: string
autonomy_level: L0|L1|L2|L3|L4
decision: GO|CONDITIONAL|NO_GO
conditions: []
open_risks: []
accepted_risks: []
rollback_version: string
evidence_bundle: string
business_owner: string
technical_owner: string
security_owner: string
approval_date: string
```

## 9. D-092 platform-scale readiness

Before calling the solution a shared or multi-tenant Agentic AI platform, require evidence for:

### Registry/lifecycle
- agent registered with named owners;
- stable workload identity;
- approved risk/autonomy classification;
- version/change history;
- suspend/kill/retire path;
- tool/A2A entitlement records.

### A2A
- two independently versioned agents;
- validated discovery/Agent Card;
- authenticated task/message exchange;
- denied unauthorized peer/skill;
- timeout/cancel/failure behavior;
- correlated trace and audit;
- downstream MCP call re-authorized by the receiving agent.

### Multi-tenancy
- distinct tenant identities;
- data/RAG isolation;
- state/memory/cache isolation;
- quota/budget isolation;
- tool entitlement isolation;
- cross-tenant negative tests;
- telemetry separation.

### Fleet operations
- canary/rollback;
- bulk quarantine/kill;
- protocol/version compatibility;
- cost/showback;
- high-cardinality telemetry controls;
- representative capacity/load evidence.

### Scope claims

Allowed only with matching evidence:

```text
DESIGNED × SINGLE_CONSUMER
IMPLEMENTED/TESTED × SINGLE_CONSUMER
VERIFIED × SHARED
VERIFIED × MULTI_TENANT_PROVEN
```

Architecture documentation alone cannot promote the scope to `SHARED` or `MULTI_TENANT_PROVEN`.

