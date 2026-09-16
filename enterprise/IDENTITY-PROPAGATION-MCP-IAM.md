# Identity Propagation across IAM, Agent Runtime and MCP

Status: **DESIGNED — ENTERPRISE IDENTITY/DELEGATION PATTERN**

Purpose: preserve accountable identity and least privilege from the initiating user/service through the AI gateway, agent runtime and MCP/tool execution boundary.

## 1. Security objective

Every sensitive action must answer:

- who initiated the request;
- which application/workload acted on the request;
- which agent/workflow selected the tool;
- which policy authorized or denied it;
- which effective scopes/roles were used;
- whether a human reviewer approved it;
- what target/resource was affected;
- which correlation/trace ID links the end-to-end evidence.

The architecture must avoid both extremes:

- forwarding broad end-user tokens everywhere;
- replacing user identity with one over-privileged shared service account.

## 2. Logical flow

```text
User / Service
     |
     | OIDC/OAuth2 authentication
     v
API Gateway / AI Gateway
     |
     | validated identity + tenant/app/user claims
     v
Agent Runtime
     |
     | workload identity + delegated subject/context
     v
MCP Gateway / Policy Enforcement
     |
     | tool-specific short-lived authorization
     v
MCP Server / Enterprise Adapter
     |
     v
OpenShift / MQ / CMDB / ITSM / Knowledge
```

## 3. Identity classes

### End-user identity

Represents the human requester. Typical claims:

- `sub`;
- tenant/organization;
- groups/roles;
- business entitlements;
- assurance/authentication context where needed.

### Application/workload identity

Represents the AI application, agent runtime, MCP gateway or server. Prefer workload identity/service accounts/managed identity over static shared secrets.

### Reviewer identity

A distinct authenticated human identity used for HITL approval. It must not be the agent identity and must not be synthesized from model output.

### Tool execution identity

The least-privilege identity actually accepted by the target system. It may be obtained via token exchange/on-behalf-of/delegation or a tightly scoped workload credential plus verified delegated subject context, depending on target-system capabilities.

## 4. Token and delegation rules

1. validate issuer, audience, signature, expiry and required claims at every trust boundary where the token is consumed;
2. never pass provider/API secrets in prompts or model context;
3. prefer short-lived credentials;
4. do not reuse a broad frontend token as an unrestricted backend/tool token;
5. bind authorization to tool/resource/action, not merely to successful authentication;
6. preserve original subject and acting workload in audit evidence;
7. separate user authorization from service authorization when both are required;
8. use token exchange/on-behalf-of where supported and justified;
9. prevent confused-deputy behavior by validating audience/resource and caller intent;
10. never let an agent mint, expand or rewrite its own scopes.

## 5. Effective authorization model

A tool call is allowed only when all applicable dimensions pass:

```text
ALLOW =
  valid_user_or_service_identity
  AND valid_workload_identity
  AND approved_use_case
  AND required_user_entitlement
  AND required_workload_scope
  AND resource/tenant boundary
  AND tool allowlist
  AND autonomy/HITL policy
  AND data classification/residency policy
```

The exact terms vary by use case; the important rule is that the model output itself is not an authorization source.

## 6. MCP authorization context

Conceptual server-side context:

```yaml
principal:
  subject: user-123
  tenant: bank-fr
  roles: [ops-analyst]
actor:
  workload: agent-runtime
  client_id: agent-runtime-prod
delegation:
  mode: on-behalf-of
  scopes: [mq.read, platform.read]
workflow:
  id: wf-456
  correlation_id: corr-789
policy:
  autonomy_level: L1
  human_approval_required: false
```

For L2 execution after approval:

```yaml
approval:
  reviewer_subject: reviewer-42
  decision: APPROVED
  approved_tool: openshift.restart_deployment
  arguments_hash: sha256:...
  expires_at: 2026-09-16T12:00:00Z
```

## 7. RAG identity propagation

The retriever must receive authoritative entitlement context before retrieval.

```text
Identity
  -> entitlement resolution
  -> ACL/security filter
  -> retrieval
  -> reranking
  -> context construction
  -> LLM
```

Unauthorized chunks must be excluded before they enter model context. Post-generation redaction is not a substitute for retrieval authorization.

Cache keys must include the security dimensions necessary to prevent cross-user/tenant leakage.

## 8. Tool-specific examples

### OpenShift

- user can request diagnosis with `platform.read`;
- agent workload can query allowed namespaces;
- remediation requires separate `platform.remediate` scope;
- restart/reconfiguration is L2 by default and requires approval bound to target deployment.

### IBM MQ / payments

- queue depth/channel status: read scope;
- message browse may require additional business-data entitlement;
- replay/reprocess: privileged mutation scope + HITL + idempotence controls;
- payment/business authorization remains authoritative outside the LLM.

### CMDB/ITSM

- dependency/owner lookup: read-only entitlement;
- ticket draft: L1 recommendation;
- production change submission/execution: separate role and approval workflow.

## 9. Audit schema

Minimum audit record:

```yaml
timestamp: string
correlation_id: string
trace_id: string
workflow_id: string
subject: string
actor_workload: string
tenant: string
tool: string
resource: string
action: string
scopes: []
policy_version: string
autonomy_level: string
approval_id: string|null
policy_decision: ALLOW|DENY
reason_code: string
duration_ms: number
result_classification: string
```

Sensitive values and secrets are never copied into audit merely for completeness.

## 10. Failure and attack cases

Deny and audit:

- expired/invalid token;
- wrong audience;
- missing tenant/resource binding;
- missing entitlement/scope;
- token replay where replay prevention is required;
- mismatched approval/action arguments;
- cross-tenant resource request;
- agent attempts to request higher privilege than its registered workload policy;
- target adapter receives a generic privileged credential where delegated authorization is required.

## 11. Implementation options

Possible enterprise implementations include combinations of:

- Keycloak/enterprise IdP for OIDC/OAuth2;
- cloud IAM/workload identity/managed identity;
- API Management/AI Gateway for token validation and policy;
- OPA or equivalent policy engine for contextual authorization;
- Kubernetes/OpenShift service accounts and RBAC;
- target-system ACL/OAM/role mechanisms;
- Vault/approved secret store for credentials that cannot yet use workload identity.

Product selection remains an ADR; this reference defines the required security semantics.

## 12. Evidence discipline

The current executable Agentic AI runtime contains OIDC/JWT-compatible identity validation and separate agent/reviewer identities, but this document does not claim production enterprise federation or end-to-end token exchange with OpenShift/MQ/CMDB. Those require implementation and runtime evidence in the selected environment.
