# AI Architecture Review Checklist

Status: **REFERENCE CHECKLIST / DESIGN AUTHORITY**

Purpose: provide a concise Architecture Review Board checklist for AI Solution Architecture.

## 1. Business and scope

- [ ] Business problem is explicit.
- [ ] Expected measurable outcome is defined.
- [ ] AI is justified versus deterministic software/search/workflow.
- [ ] Scope and out-of-scope are explicit.
- [ ] Business owner and technical owner are identified.

## 2. FR / NFR

- [ ] Functional requirements are documented.
- [ ] NFRs are measurable where possible.
- [ ] Availability, latency, throughput and scalability targets exist.
- [ ] Security/privacy/residency requirements exist.
- [ ] Quality/grounding/safety targets exist.
- [ ] Operability, portability and cost requirements exist.

## 3. Architecture pattern decision

- [ ] Prompt-only vs RAG vs workflow vs agent vs fine-tuning decision is justified.
- [ ] Deterministic business rules remain outside probabilistic model authority.
- [ ] HITL boundary is explicit.
- [ ] Tool access is minimized and typed.
- [ ] Agent autonomy is bounded.

## 4. Model and provider

- [ ] Model capability requirements are explicit.
- [ ] Provider/model selection criteria are documented.
- [ ] API vs self-host/private decision is documented.
- [ ] Data/provider eligibility is enforced.
- [ ] Fallback/reversibility strategy exists where required.
- [ ] Model/version is traceable.

## 5. Data / knowledge / RAG

- [ ] Systems of record are identified.
- [ ] Knowledge sources have owner/version/classification.
- [ ] ACL/entitlements are enforced before context construction.
- [ ] Ingestion/index lifecycle is documented.
- [ ] Retention/deletion lineage is defined.
- [ ] Retrieval and generation are evaluated separately.
- [ ] Citation/abstention policy exists where grounding is required.

## 6. Security / Responsible AI

- [ ] Threat model exists.
- [ ] AuthN/AuthZ/least privilege are defined.
- [ ] Prompt injection/jailbreak risk is addressed.
- [ ] Tool authorization is deterministic.
- [ ] PII/secrets/output controls exist.
- [ ] AI-BOM/provenance ownership is defined.
- [ ] Human oversight and risk classification are defined.
- [ ] Incident and misuse paths are defined.

## 7. Integration

- [ ] API/event/tool contracts are versioned.
- [ ] Timeout/retry/circuit-breaker behavior is defined.
- [ ] Idempotency and correlation are defined where needed.
- [ ] MQ/Kafka/event replay/DLQ patterns are used where relevant.
- [ ] Legacy integration avoids unnecessary replacement.

## 8. Platform and deployment

- [ ] Environment topology is documented.
- [ ] CPU/GPU/runtime requirements are known or labelled estimates.
- [ ] Network/private endpoint/egress policy is defined.
- [ ] Secrets and configuration lifecycle are defined.
- [ ] GitOps/IaC ownership is defined.
- [ ] State and storage are explicit.

## 9. Performance and capacity

- [ ] End-to-end latency budget exists.
- [ ] TTFT/tokens-per-second metrics exist where relevant.
- [ ] Concurrency/throughput assumptions are explicit.
- [ ] Cache strategy considers identity, freshness and versioning.
- [ ] Capacity estimates are clearly distinguished from measurements.
- [ ] Load/benchmark evidence is planned where risk requires it.

## 10. Resilience / DR

- [ ] Critical dependencies and failure modes are listed.
- [ ] Degraded modes are defined.
- [ ] Provider/model outage behavior is defined.
- [ ] RTO/RPO are defined where required.
- [ ] Backup/rebuild/restore strategy exists.
- [ ] Recovery tests are planned for critical paths.

## 11. Evaluation / observability / feedback

- [ ] Representative evaluation dataset exists or is planned.
- [ ] Baseline/candidate comparison is defined.
- [ ] Quality/security regression gates exist.
- [ ] End-to-end traceability exists.
- [ ] SLO/SLI and alerting are defined.
- [ ] Feedback is governed before becoming training/regression data.

## 12. FinOps / GreenOps

- [ ] Cost drivers are identified.
- [ ] Model/token/infrastructure budgets exist.
- [ ] Cost per useful response or business outcome is considered.
- [ ] Provider/GPU utilization is observable where applicable.
- [ ] Energy/carbon claims distinguish estimates from measurements.

## 13. Architecture governance

- [ ] Major decisions have ADRs.
- [ ] Constraints and assumptions are documented.
- [ ] Risks and technical debt have owners.
- [ ] Exceptions have expiry/review conditions.
- [ ] Transition architecture is documented.
- [ ] Exit/reversibility strategy is defined for major provider coupling.

## 14. POC decision

A POC is justified only when it reduces a material unknown.

- [ ] Unknown is explicitly stated.
- [ ] Success/failure criteria are defined before implementation.
- [ ] The POC is minimal and does not become accidental production.
- [ ] Evidence will be captured.
- [ ] A POC is not being created merely because a technology is fashionable.

## 15. Production readiness

- [ ] Security review complete.
- [ ] Architecture review complete.
- [ ] Evaluation gates pass.
- [ ] NFR evidence acceptable.
- [ ] Monitoring/runbooks/escalation ready.
- [ ] Rollback/recovery path validated.
- [ ] Owners/support model defined.
- [ ] Cost budget approved.
- [ ] Known limitations/non-claims documented.

## Decision outcomes

Use one:

- `APPROVED`
- `APPROVED WITH CONDITIONS`
- `POC REQUIRED — MATERIAL UNCERTAINTY`
- `REWORK REQUIRED`
- `REJECTED`
- `EXCEPTION GRANTED — TIME-BOUNDED`

Every decision must include rationale and owner.