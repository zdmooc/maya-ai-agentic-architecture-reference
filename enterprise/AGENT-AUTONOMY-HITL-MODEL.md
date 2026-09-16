# Agent Autonomy and Human-in-the-Loop Model

Status: **DESIGNED — ENTERPRISE AUTONOMY POLICY MODEL**

Purpose: define explicit autonomy levels for agentic systems and bind every tool/action to deterministic authorization, risk and human-approval requirements.

The autonomy level is an architecture/policy decision. An LLM cannot choose, increase or waive its own autonomy level.

## 1. Autonomy levels

| Level | Name | Agent capability | Human role | Typical examples |
|---|---|---|---|---|
| L0 | Observe | read, summarize, classify, explain | none for normal reads | logs, metrics, architecture Q&A |
| L1 | Recommend | produce diagnosis/options/recommended action | human decides outside agent | incident recommendation, remediation proposal |
| L2 | Execute with approval | prepare and execute a bounded action only after authenticated approval | mandatory pre-execution approval | restart workload, controlled replay, ticket change |
| L3 | Bounded autonomous | execute pre-approved low-risk actions inside explicit policy envelope | oversight, exception/review | cache refresh, safe retry, reversible housekeeping |
| L4 | High autonomy | broad goal-driven execution across multiple tools/systems | governance-defined exceptional use only | normally prohibited for regulated/high-impact banking operations |

Default enterprise posture for this reference:

- read-only knowledge/observability: L0;
- architecture/incident recommendations: L1;
- production/payment/configuration mutations: L2 unless a stronger approved policy exists;
- L3 requires explicit risk acceptance, rollback, bounded scope and runtime evidence;
- L4 is not a default target and must never be enabled by configuration alone.

## 2. Tool policy contract

Every tool definition must include policy metadata similar to:

```yaml
tool: openshift.restart_deployment
autonomy:
  max_level: L2
  default_level: L1
risk_class: HIGH
required_scopes:
  - platform.read
  - platform.remediate
human_approval:
  required: true
  approver_role: operations-reviewer
constraints:
  namespace_allowlist: [payments-prod]
  max_replicas_affected: 1
  dry_run_supported: true
rollback:
  required: true
audit:
  required: true
```

The server-side policy is authoritative. Agent-supplied values cannot increase permissions or bypass approval.

## 3. Example tool classification

| Tool/action | Default | Maximum | Approval | Notes |
|---|---:|---:|---|---|
| `knowledge.search_runbook` | L0 | L0 | no | ACL-aware read only |
| `cmdb.get_dependencies` | L0 | L0 | no | entitlement filtered |
| `openshift.get_pods` | L0 | L0 | no | namespace-scoped |
| `openshift.get_logs` | L0 | L0 | no | redact secrets/PII |
| `mq.get_queue_depth` | L0 | L0 | no | operational read |
| `payment.get_status` | L0 | L0 | no | subject to business authorization |
| `incident.propose_remediation` | L1 | L1 | no execution | recommendation only |
| `openshift.restart_deployment` | L1 | L2 | yes | bounded target + rollback evidence |
| `mq.replay_message` | L1 | L2 | yes | idempotence/correlation mandatory |
| `payment.reprocess` | L1 | L2 | yes | business/risk controls authoritative |
| generic shell / unrestricted SQL | prohibited | prohibited | n/a | not exposed as agent tool |
| unrestricted payment execution | prohibited | prohibited | n/a | not exposed to general agent |

## 4. Approval workflow

```text
Agent recommendation
        |
        v
Deterministic policy/risk evaluation
        |
        +-- DENY -> stop + audit
        |
        v
Approval required?
   | no           | yes
   v              v
bounded call   create approval case
                  |
                  v
          authenticated reviewer
           approve / reject / expire
                  |
                  v
         short-lived authorization
                  |
                  v
             tool execution
                  |
                  v
        evidence + outcome + audit
```

Approval must bind at least:

- actor/reviewer identity;
- action/tool;
- canonical arguments or argument hash;
- target resource;
- validity window;
- correlation/workflow ID;
- policy version;
- expected rollback or recovery path.

An approval for one action must not be reusable as a generic privileged token.

## 5. Conditions that force HITL

HITL is mandatory by default when any of the following apply:

- financial/customer transaction impact;
- production mutation;
- entitlement/security change;
- destructive action;
- regulated/high-impact decision;
- uncertain/conflicting/stale evidence;
- action outside historical bounded envelope;
- non-reversible operation;
- elevated or cross-domain privilege;
- policy classifies the tool at L2 maximum.

## 6. L3 bounded-autonomy admission criteria

A candidate action can move from L2 to L3 only if all required criteria are met:

1. deterministic preconditions and hard bounds exist;
2. action is low impact and reversible;
3. least-privilege workload identity exists;
4. blast radius is explicitly constrained;
5. idempotence/retry behavior is proven;
6. rollback or compensation is tested;
7. monitoring can detect failure quickly;
8. rate/budget/step limits are enforced server-side;
9. security/adversarial tests pass;
10. governance authority explicitly accepts the residual risk;
11. runtime evidence supports the claim.

## 7. Fail-closed rules

- missing identity -> deny;
- missing scope -> deny;
- unknown tool -> deny;
- autonomy metadata absent on a sensitive tool -> deny;
- approval expired or mismatched -> deny;
- stale/insufficient evidence -> no sensitive execution;
- policy service unavailable -> sensitive actions fail closed;
- agent attempt to change autonomy level -> ignore/deny and audit.

## 8. Observability and KPIs

Track at minimum:

- calls by autonomy level;
- approval requested/approved/rejected/expired;
- denied tool calls by policy reason;
- autonomous actions by tool/domain;
- rollback/compensation rate;
- failed action rate;
- human override rate;
- time-to-approval;
- incidents caused or prevented by agent actions;
- policy-version distribution.

## 9. Evidence discipline

This model is `DESIGNED` until implemented by a runtime policy/approval mechanism. Existing I7 runtime evidence demonstrates a concrete HITL lifecycle for the specialist Agentic AI runtime, but this document does not imply that every enterprise tool/domain already implements L0-L4 enforcement.
