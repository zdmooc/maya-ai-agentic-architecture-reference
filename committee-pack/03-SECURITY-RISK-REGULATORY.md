# Security, Risk and Regulatory View — Enterprise Agentic AI

Status: **DESIGNED — COMMITTEE RISK VIEW**

## 1. Principal risks

| Risk | Primary architecture response | Committee question |
|---|---|---|
| prompt injection/jailbreak | trust boundaries, prompt policy, negative tests | can untrusted input alter privileged behavior? |
| indirect injection/poisoned RAG | source trust, quarantine, ACL-before-context, provenance | can a document manipulate tools or leak data? |
| excessive agency | L0-L4 policy, bounded tools, HITL | what is the maximum autonomous action? |
| privilege escalation | user/workload identity, scopes, server-side AuthZ | can the agent increase its own privilege? |
| cross-tenant/data leakage | tenant-aware IAM/RAG/cache | can one user receive another tenant's content? |
| hallucinated action | Systems of Record, deterministic validation/veto | what prevents invented operational facts? |
| malicious tool result | schema validation, provenance, output handling | are tool results trusted blindly? |
| provider/model outage | fallback/degradation/SLO/runbook | what happens without the preferred model? |
| supply-chain compromise | SBOM/AI-BOM, signed/approved artifacts, scanning | can model/tool/library provenance be reconstructed? |
| denial-of-wallet | quotas/token budgets/routing/cache | how is uncontrolled spend prevented? |
| unsafe remediation | approval, blast-radius limits, rollback | can a bad action be stopped/reversed? |

## 2. Trust boundaries

```text
[User]
  | identity
  v
[Gateway/IAM] ---- policy boundary
  |
  v
[Agent Runtime] --- model output is NOT authorization
  |
  +--> [RAG boundary] ---- ACL/source trust
  |
  +--> [MCP boundary] ---- tool AuthZ/autonomy/HITL
                              |
                              v
                      [Systems of Record]
```

The highest-risk boundary is the transition from generated reasoning/recommendation to an external side effect.

## 3. Autonomy policy

Default posture:

- L0 read/summarize: allowed within entitlement;
- L1 recommend: no side effect;
- L2 execute after authenticated approval: default for sensitive mutation;
- L3 bounded autonomy: exception requiring proven reversibility, limits and governance approval;
- L4 broad autonomy: not a default target.

See `enterprise/AGENT-AUTONOMY-HITL-MODEL.md`.

## 4. Identity and least privilege

Sensitive execution requires both accountable initiating identity and an approved workload/tool identity. Authorization is performed server-side from authoritative claims/policy; model output cannot grant scopes.

See `enterprise/IDENTITY-PROPAGATION-MCP-IAM.md`.

## 5. Regulatory traceability

The architecture includes controls intended to support assessment against:

- EU AI Act themes such as transparency, human oversight, risk management, logging, robustness and documentation where applicable;
- GDPR themes such as purpose limitation, minimisation, rights, security, retention and processor/provider governance where personal data is processed;
- NIS2/French cybersecurity themes such as risk management, incident handling, continuity, supply chain, access control and security monitoring where applicable;
- legacy OSE/SIE concerns when the client's historical regulatory scope uses those terms.

Applicability and compliance remain legal/RSSI/DPO decisions. See `enterprise/REGULATORY-CONTROL-MAPPING-EU-FR.md`.

## 6. Blocking conditions

Production approval should be blocked when any material condition applies:

- unknown or unowned high/critical risk;
- sensitive tool without explicit authorization/autonomy metadata;
- missing rollback/recovery for high-impact action;
- RAG ACL bypass or cross-tenant leakage;
- unresolved secret/PII exposure path;
- missing model/provider/data-placement approval;
- no audit trail for sensitive decision/action;
- evaluation/security regression below required gate;
- regulatory applicability unresolved for a materially affected use case;
- no named operational/security/business owner.

## 7. Required committee evidence

- current risk register;
- threat/trust-boundary diagram;
- autonomy/tool matrix;
- IAM/delegation design;
- adversarial/security tests;
- RAG ACL/poisoning tests;
- AI-BOM/SBOM;
- model/provider register;
- recovery/rollback evidence;
- regulatory applicability/control mapping;
- residual-risk acceptance records.

## 8. D-092 registry and A2A threat extension

Additional platform-scale threats:

| Threat | Required response |
|---|---|
| rogue/impersonated agent | stable workload identity, authenticated registry, peer allowlist |
| registry/Agent Card poisoning | controlled publishing/review, provenance, authenticated discovery, schema validation |
| delegation abuse/confused deputy | non-transitive authorization, caller+remote agent identity, tenant/resource binding |
| cross-agent prompt injection | remote messages/artifacts are untrusted input; deterministic policy remains authoritative |
| recursive delegation/task storm | max depth/fan-out/time/token/cost, cancellation and circuit breakers |
| protocol/version skew | versioned contracts, compatibility tests, canary and deprecation policy |
| cross-tenant memory/state leakage | partitioned state/memory/cache plus negative isolation tests |

Security review must cover both boundaries:

```text
Agent -> A2A -> Agent
Agent -> MCP -> Tool/System
```

An authenticated A2A peer does not inherit authorization to downstream MCP tools. The receiving agent must re-authorize every sensitive downstream action.

