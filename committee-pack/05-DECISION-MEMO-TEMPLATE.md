# Decision Memo Template — Enterprise Agentic AI

Status: **TEMPLATE**

## Decision requested

State the exact decision required from the Architecture Review Board / Design Authority / steering committee.

Example structure:

> Approve / conditionally approve / reject the proposed Agentic AI use case, target architecture, maximum autonomy level, model/provider placement and implementation/evidence plan.

## Business context

- business problem;
- affected process/users;
- current baseline/time/cost/risk;
- expected measurable outcome;
- business owner.

## Scope

In scope:

- use cases;
- channels/users;
- corpora/data classes;
- systems/tools;
- environments.

Out of scope:

- explicitly excluded actions/data/systems;
- real-money or destructive actions unless separately approved;
- claims without evidence.

## Options considered

| Option | Benefits | Risks/constraints | Evidence | Decision impact |
|---|---|---|---|---|
| deterministic workflow | | | | |
| RAG assistant | | | | |
| agentic workflow | | | | |
| private model | | | | |
| managed model | | | | |
| hybrid routing | | | | |

## Proposed architecture

Reference the approved architecture diagram and summarize:

- gateway/IAM;
- AI Gateway/policy;
- agent/orchestration;
- RAG;
- MCP/tools;
- Systems of Record;
- HITL;
- evaluation/observability;
- deployment/placement.

## Maximum autonomy

```yaml
default_level: L0|L1|L2|L3|L4
maximum_level: L0|L1|L2|L3|L4
sensitive_tools: []
hitl_required_for: []
prohibited_actions: []
```

## Security and compliance summary

- data classification/residency;
- IAM/authorization/delegation;
- prompt/RAG/tool threats;
- privacy/DPIA status;
- AI Act applicability status;
- NIS2/OSE/sector applicability status;
- open security/compliance conditions.

## NFR and operability summary

- latency/SLA/SLO;
- availability/DR;
- observability/audit;
- capacity/cost;
- rollback;
- incident ownership.

## Evidence status

| Capability | Status | Evidence |
|---|---|---|
| architecture | DESIGNED | |
| runtime | IMPLEMENTED/TESTED/... | |
| RAG | | |
| identity | | |
| security | | |
| HITL | | |
| deployment | | |
| resilience | | |

## Material risks

List blocking/high risks, owner, mitigation and residual acceptance authority.

## Recommendation for committee record

Use only factual decision wording, for example:

- `APPROVE` — all mandatory gates satisfied;
- `CONDITIONAL` — approved subject to enumerated conditions before promotion;
- `NO_GO` — blocking risk/evidence gap remains.

## Decision record

```yaml
decision: APPROVE|CONDITIONAL|NO_GO
conditions: []
exceptions: []
accepted_risks: []
decision_owner: string
date: YYYY-MM-DD
review_date: YYYY-MM-DD
linked_adrs: []
linked_evidence: []
```

## Platform sourcing decision — D-092 extension

When the committee is deciding platform strategy rather than only a use case, add:

### Scope requested

```yaml
platform_scope: APPLICATION|SHARED_CAPABILITY|ENTERPRISE_PLATFORM
target_consumers: []
tenancy_model: string
registry_owner: string
lifecycle_owner: string
```

### Interoperability

```yaml
mcp_required: true|false
mcp_reference_version: string
a2a_required: true|false
a2a_reference_version: string
approved_a2a_trust_domains: []
max_delegation_depth: number
```

### Sourcing options

| Option | Decision evidence |
|---|---|
| internal/OpenShift | control, residency, operations, private serving, portability |
| managed cloud | managed runtime/identity/registry/tooling, region/security/cost |
| code-first + managed primitives | orchestration portability vs integration burden |
| hybrid | placement policy, identity federation, protocol/exit contracts |

Use `enterprise/AGENTIC-PLATFORM-BUILD-VS-BUY-2026.md` as the dated option framework.

### Platformization evidence

Before approving extraction/shared platform:

- first consumer runtime proven;
- second consumer real, not hypothetical;
- identity/policy separation;
- cross-consumer negative tests;
- operational owner;
- measured cost/operability;
- exit/reversibility plan.

### Decision

```yaml
platform_decision: KEEP_IN_PRODUCT|EXTRACT_INTERNAL|MANAGED|HYBRID|DEFER
rationale: string
mandatory_conditions: []
revisit_trigger: string
```

