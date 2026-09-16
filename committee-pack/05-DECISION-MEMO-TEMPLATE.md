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
