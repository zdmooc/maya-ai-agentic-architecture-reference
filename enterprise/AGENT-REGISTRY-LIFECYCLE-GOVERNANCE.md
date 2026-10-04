# Agent Registry & Lifecycle Governance

Status: **DESIGNED — D-092 M1 / ENTERPRISE AGENT GOVERNANCE STANDARD**

Purpose: define the minimum enterprise contract for registering, governing, versioning, approving, operating, suspending and retiring AI agents without turning the registry itself into a business system of record.

## 1. Principle

An enterprise agent is not only code plus a prompt. It is a governed workload with:

- accountable ownership;
- stable identity;
- declared purpose and risk;
- bounded autonomy;
- approved models/tools/data;
- lifecycle state;
- operational SLOs;
- evidence and audit history.

The registry is the control-plane source for **what the agent is allowed to be**, not a substitute for the runtime, IAM, CMDB or business system of record.

## 2. Canonical lifecycle

```text
DESIGN
  -> REGISTER
  -> RISK_CLASSIFY
  -> IDENTITY_ASSIGN
  -> ENTITLE
  -> EVALUATE
  -> APPROVE
  -> DEPLOY
  -> OBSERVE
  -> CHANGE / VERSION
  -> SUSPEND | KILL
  -> RETIRE
```

No lifecycle transition is inferred from deployment alone.

## 3. Minimum agent record

```yaml
agent_id: string
name: string
description: string
business_domain: string
business_owner: string
technical_owner: string
security_owner: string

version: string
framework: string
runtime_type: prompt|hosted|code-first|custom
deployment_target: string
status: DESIGN|REGISTERED|APPROVED|DEPLOYED|SUSPENDED|RETIRED

identity:
  workload_identity: string
  tenant: string|null
  delegated_user_supported: boolean
  reviewer_identity_required: boolean

risk:
  classification: LOW|MEDIUM|HIGH|CRITICAL
  autonomy_default: L0|L1|L2|L3|L4
  autonomy_maximum: L0|L1|L2|L3|L4
  prohibited_actions: []

models:
  aliases: []
  provider_policy: string
  data_residency_policy: string

tools:
  mcp_servers: []
  a2a_peers: []
  direct_tools: []
  scopes: []

data:
  allowed_classes: []
  rag_corpora: []
  retention_policy: string

operations:
  slo_profile: string
  token_budget: number|null
  cost_budget: number|null
  max_steps: number|null
  max_runtime_seconds: number|null
  kill_switch: string
  runbook: string

governance:
  policy_version: string
  evaluation_baseline: string
  approval_record: string
  evidence_bundle: string
  last_reviewed_at: string
  next_review_at: string
```

## 4. Ownership model

### Business owner
Owns purpose, expected outcome, business risk and acceptance criteria.

### Technical owner
Owns implementation, runtime, deployment, SLO and operational lifecycle.

### Security owner
Owns trust boundaries, identity, authorization, secrets, security controls and residual-security review.

### Data/knowledge owner
Owns source quality, entitlement, retention and deletion semantics for governed corpora.

### Platform owner
Owns shared runtime/control capabilities, not the business purpose of the agent.

No agent may be production-approved with an unowned business, technical or security responsibility.

## 5. Registration gate

Registration requires at minimum:

- purpose/use case;
- owners;
- framework/runtime;
- model policy;
- data classes;
- tools/MCP/A2A interfaces;
- autonomy ceiling;
- risk classification;
- target environment;
- observability/evidence expectations.

Registration is not approval.

## 6. Risk classification

Risk increases with:

- high-impact business decisions;
- sensitive data;
- privileged tool access;
- cross-system mutation;
- high autonomy;
- long-running delegated tasks;
- external/third-party agent collaboration;
- broad memory retention;
- high financial or operational blast radius.

Risk classification must influence evaluation depth, approval authority, HITL and monitoring.

## 7. Identity assignment

Every deployed agent must have a stable workload identity independent from end-user identity.

Rules:

- never derive identity from model output;
- no shared super-agent credential;
- distinguish user, agent workload, reviewer and tool-execution identity;
- bind entitlements to agent version/policy where material;
- revoke/suspend identity when the agent is suspended or retired.

See `IDENTITY-PROPAGATION-MCP-IAM.md`.

## 8. Entitlement gate

The registry must declare what the agent can discover/call:

- model aliases/providers;
- MCP servers/tools;
- A2A peers;
- RAG corpora/data classes;
- allowed environments/tenants;
- allowed mutation classes.

Runtime authorization remains server-side and authoritative. Registry metadata does not replace target-system authorization.

## 9. Evaluation and approval

Before APPROVED:

- functional/golden tests;
- negative security tests;
- RAG ACL tests where applicable;
- tool authorization tests;
- autonomy/HITL tests;
- resilience/failure tests;
- latency/cost/capacity evidence as required;
- provider/model/data-placement approval.

Higher autonomy requires a separate promotion decision.

## 10. Versioning and change

Material changes create a new agent version or new approval record:

- model/provider change;
- prompt/system-policy change;
- new tool or MCP server;
- new A2A peer;
- increased autonomy;
- new sensitive corpus;
- identity/tenant boundary change;
- runtime/framework major upgrade;
- changed retention/memory policy.

A version must be reconstructable from code/config/policy/evidence.

## 11. Suspend / kill / quarantine

The platform must support:

- administrative suspension;
- runtime kill/disable;
- credential revocation;
- tool access revocation;
- provider/model deny;
- A2A peer isolation;
- queue/task cancellation where supported.

Typical triggers:

- security incident;
- evaluation regression;
- runaway cost;
- cross-tenant leakage;
- unsafe tool behavior;
- unbounded loop;
- compromised dependency;
- owner loss / unsupported version.

## 12. Retirement

Retirement requires:

- endpoint disabled;
- identity revoked;
- tool/A2A registrations withdrawn;
- retained state/memory handled per policy;
- evidence/audit archived per retention;
- dependent consumers identified;
- replacement/migration documented when applicable.

## 13. Evidence and claim discipline

`DESIGNED` means this governance model exists.

Do not claim an implemented enterprise Agent Registry until a concrete registry, lifecycle API/workflow and runtime integration are deployed and verified.

Possible implementations may include a custom internal registry, cloud-managed agent registry/catalog capabilities, or a hybrid model. Product selection is handled by the build-vs-buy ADR.
