# EU/France Regulatory Control Mapping for Enterprise Agentic AI

Status: **DESIGNED — ARCHITECTURE TRACEABILITY / NOT LEGAL CERTIFICATION**

Last architecture review: **2026-09-16**.

Purpose: map enterprise Agentic AI architecture controls to regulatory themes explicitly relevant to European/French deployments, including the EU AI Act, GDPR and NIS2/OSE-related cybersecurity expectations.

This is an architecture control map, not legal advice. Applicability, legal qualification, entity status, sector obligations and deadlines must be validated with the client's legal/DPO/RSSI/compliance functions against the current official texts.

## 1. Regulatory-status guardrail

Regulatory timelines evolve. Architecture documents must therefore record the review date and source version instead of treating compliance dates as immutable configuration.

At the 2026-09-16 review point:

- the EU AI Act is in progressive application/enforcement, with transparency obligations applying from 2 August 2026 and later dates for parts of the high-risk regime;
- GDPR remains applicable whenever personal-data processing falls within its scope;
- NIS2 cybersecurity obligations must be assessed against the organisation's sector/entity status and the current French transposition/implementation framework;
- legacy French/EU NIS terminology such as OSE/SIE must not be mechanically treated as identical to NIS2's essential/important entity model.

## 2. Traceability model

Every regulatory item should map as:

```text
Regulatory requirement/theme
 -> applicability decision
 -> architecture control
 -> technical/organizational implementation
 -> evidence
 -> control owner
 -> residual risk / exception
 -> review date
```

No `COMPLIANT` claim is created solely because a control exists in this repository.

## 3. EU AI Act architecture mapping

| Regulatory theme | Architecture control | Expected evidence |
|---|---|---|
| AI system/use-case classification | AI use-case registry, purpose/owner/risk class | approved registry record + applicability assessment |
| Human oversight | L0-L4 autonomy model, HITL for sensitive actions | tool/autonomy policy + approval audit |
| Transparency to users where applicable | channel disclosure policy, output metadata | UX/API test + policy version |
| Logging/traceability | correlation IDs, immutable audit, model/prompt/tool/index versions | trace/audit evidence bundle |
| Risk management | AI risk register, threat model, NFRs, fitness functions | reviewed risks + mitigation evidence |
| Data governance | source lineage, classification, quality, ACL, provenance | corpus/data contracts + lineage reports |
| Accuracy/robustness/cybersecurity | evaluation gates, security tests, SLOs, resilience controls | evaluation/security/resilience reports |
| Technical documentation | solution architecture dossier, ADRs, AI-BOM | versioned architecture pack |
| AI literacy/governance | RACI, operating model, review process | role/training/governance evidence supplied by organisation |
| GPAI/provider dependencies where applicable | provider/model catalog, AI-BOM, provider eligibility/contract controls | model/provider inventory + contract/security assessment |

High-risk or other regulated classifications are legal/applicability decisions, not labels inferred by the LLM or this repository.

## 4. GDPR architecture mapping

| GDPR theme | Architecture control | Expected evidence |
|---|---|---|
| purpose limitation | registered use case and declared processing purpose | use-case/data-processing record |
| data minimisation | context filtering, prompt minimisation, bounded retrieval | tests/config + design review |
| lawfulness/transparency | DPO/legal process + user/privacy information hooks | organisation legal basis + notices |
| access control/confidentiality | IAM, ACL-before-context, least privilege, tenant isolation | negative access tests + IAM policy |
| data subject rights | source/index lineage and deletion/rebuild paths | deletion/rectification test where applicable |
| retention limitation | retention/expiry metadata and controlled archival | retention policy + purge evidence |
| security of processing | encryption, secrets management, network controls, logging policy | platform/security evidence |
| processor/provider governance | provider eligibility, contracts, data-location controls | approved-provider record/DPA assessment |
| DPIA trigger/support | risk/use-case registry and DPIA integration hook | DPIA decision/record owned by DPO/legal |
| automated decision concerns | deterministic business rules, HITL and explicit decision boundary | ADR + workflow evidence |

Personal data must not be copied into prompts, traces, evaluation datasets or vector stores by default merely because the technology permits it.

## 5. NIS2 / French cybersecurity architecture mapping

| Cybersecurity theme | Architecture control | Expected evidence |
|---|---|---|
| risk management | risk register, threat model, asset/service mapping | risk assessment + architecture review |
| incident handling | SLO/alerts/runbooks, correlation, escalation | incident/runbook exercise |
| business continuity / crisis / recovery | HA/DR, backup/rebuild, fallback, chaos/failure tests | recovery/failure evidence |
| supply-chain security | SBOM/AI-BOM, approved images/providers/tools | supply-chain inventory + scan/approval results |
| vulnerability/security hygiene | CI scanning, patch/version policy, dependency controls | CI/security reports |
| access control | IAM, least privilege, tool scopes, workload identities | authorization tests |
| cryptography/secrets | TLS/mTLS target, certificates, Vault/secret-store patterns | configuration/evidence in selected runtime |
| security monitoring | OTel/logs/metrics/security denials/audit | dashboard/alert evidence |
| governance/accountability | RACI, security owner, exception/risk acceptance | named owner + review records |
| service dependency visibility | CMDB/dependency map, platform/MQ/API inventory | architecture/service map |

For French NIS2 scope, entity qualification and mandatory controls must be revalidated against ANSSI/current French law and implementing texts. The ReCyF can be used as a security-reference input where relevant, but its legal status/version must be recorded.

## 6. OSE / NIS legacy mapping

Some mission descriptions still mention `OSE`. Treat this as a scope signal requiring clarification, not as proof that the organisation has a particular legal status.

Legacy OSE/SIE architecture concerns remain useful:

- identify essential business services;
- map supporting information systems;
- assess availability/integrity/confidentiality impact;
- apply security controls to critical systems;
- retain incident/audit evidence;
- support security review and notification processes.

The target dossier must distinguish:

- historical/legacy OSE/SIE obligations;
- current NIS2 essential/important entity applicability;
- sector-specific overlays;
- client internal security standards.

## 7. Agentic-AI-specific control traceability

| Agentic risk | Primary control | Regulatory relevance |
|---|---|---|
| prompt injection | untrusted-content boundary + policy + negative tests | cybersecurity/risk management |
| indirect injection in RAG | source trust/quarantine + ACL-before-context | GDPR/confidentiality/cybersecurity |
| excessive agency | autonomy levels + bounded tools + HITL | human oversight/risk management |
| tool privilege escalation | identity propagation + server-side authorization | access control/cybersecurity |
| hallucinated operational action | authoritative SoR checks + deterministic veto + HITL | robustness/human oversight |
| cross-tenant leakage | tenant-aware IAM/retrieval/cache | GDPR/confidentiality |
| poisoned corpus | provenance/quarantine/versioning | data governance/cybersecurity |
| model/provider dependency risk | provider catalog + AI-BOM + exit/fallback ADR | governance/supply chain |
| missing traceability | correlation/model/prompt/index/tool versions | logging/technical documentation |
| unsafe autonomous remediation | L2 default + reviewer approval + rollback | human oversight/operational resilience |

## 8. Evidence bundle expected for architecture review

Minimum evidence pack:

- use-case/applicability assessment;
- data classification and flow diagram;
- identity/trust-boundary diagram;
- autonomy/tool matrix;
- RAG ACL and data-lineage tests;
- security/adversarial test report;
- evaluation/quality report;
- AI-BOM/SBOM;
- provider/model register;
- risk register and residual-risk decisions;
- observability/audit examples;
- incident/recovery runbook evidence;
- architecture decision records;
- DPO/RSSI/legal sign-offs where required by organisational process.

## 9. Official-source baseline

Architecture reviewers should re-check current official sources, including:

- European Commission / EU AI Act implementation and enforcement material;
- EUR-Lex authoritative EU legal texts;
- CNIL guidance for AI and personal-data processing;
- ANSSI NIS2/MonEspaceNIS2/ReCyF material;
- Légifrance for current French implementing law and regulations.

## 10. Claim discipline

Allowed architecture statement:

> The solution architecture includes controls and traceability designed to support AI Act, GDPR and cybersecurity/NIS2 compliance work, subject to client applicability assessment and legal/RSSI/DPO validation.

Not allowed without formal evidence/authority:

> The platform is AI Act/GDPR/NIS2 certified or legally compliant because this reference document exists.
