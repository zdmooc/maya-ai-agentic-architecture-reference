# AI Architecture Risk Register

Status: **DESIGNED — REFERENCE REGISTER / TAILOR PER USE CASE**

Purpose: provide a reusable risk baseline for AI Solution Architecture reviews. Each project must assign owner, likelihood, impact, controls, residual risk and evidence.

| ID | Risk | Typical impact | Preventive / detective controls | Default treatment |
|---|---|---|---|---|
| R-01 | Hallucinated or unsupported answer | Wrong business decision, user harm | RAG grounding, citation validation, abstention, evals, authoritative-system checks | Mitigate |
| R-02 | Prompt injection / jailbreak | Policy bypass, data/tool abuse | trust-boundary separation, untrusted-content handling, tool allowlists, deterministic authZ, negative tests | Mitigate |
| R-03 | Sensitive data disclosure | Privacy/regulatory incident | classification, PII/secrets inspection, ACL-before-context, DLP, provider eligibility, redaction | Mitigate/Avoid |
| R-04 | Cross-tenant / ACL leakage | Unauthorized disclosure | tenant isolation, entitlement filtering before retrieval, cache partitioning, negative tests | Avoid |
| R-05 | Stale knowledge/index | Incorrect guidance | source freshness, versioning, expiry, rebuild pipeline, stale-data status | Mitigate |
| R-06 | Poisoned documents/embeddings | Manipulated output | source trust, quarantine/curation, provenance, ingestion validation, signed/owned sources | Mitigate |
| R-07 | Excessive agency | Unsafe autonomous action | bounded tools, max steps/budget, deterministic veto, HITL, least privilege | Avoid/Mitigate |
| R-08 | Tool misuse / malicious arguments | External system damage | typed schemas, server-side validation/authZ, idempotence, rate/timeout, dry-run/HITL | Mitigate |
| R-09 | Model/provider outage | Service degradation | fallback policy, circuit breaker, graceful deterministic degradation, SLO/runbooks | Mitigate |
| R-10 | Provider lock-in | Cost/exit/strategy risk | model aliases, portable contracts/prompts/evals, exit ADR, externalized knowledge | Mitigate/Accept explicitly |
| R-11 | Model quality regression | Production quality decline | baseline/candidate eval, canary, version pinning, rollback, continuous regression | Mitigate |
| R-12 | Prompt/config regression | Incorrect behavior | prompt registry/versioning, CI eval gates, rollback | Mitigate |
| R-13 | Retrieval regression | Lower grounding/citation quality | golden retrieval dataset, recall/relevance metrics, index/version controls | Mitigate |
| R-14 | Unbounded token/cost consumption | Budget overrun / denial-of-wallet | quotas, token budgets, cache, routing, context limits, anomaly alerts | Mitigate |
| R-15 | Latency/SLA breach | Poor UX / failed process | performance budget, streaming, routing, cache, timeout/fallback, capacity tests | Mitigate |
| R-16 | GPU/VRAM saturation | Queue/backlog/outage | capacity model, quotas, autoscaling, admission, monitoring, workload classes | Mitigate |
| R-17 | Inaccurate capacity estimate | Under/over-provisioning | label estimates, representative benchmark, headroom, sensitivity analysis | Mitigate |
| R-18 | Weak observability | Undiagnosable failures | end-to-end correlation, traces/metrics/logs/evals, sensitive-data logging policy | Mitigate |
| R-19 | Training/eval data leakage | False quality confidence | strict dataset split/versioning, dedup, contamination review | Mitigate |
| R-20 | Biased/unfair outcome | User/regulatory harm | use-case risk classification, representative evals, human review, fairness analysis where applicable | Mitigate/Avoid |
| R-21 | Missing human oversight | High-impact uncontrolled decision | risk-based HITL policy, explicit approval state, audit evidence | Avoid |
| R-22 | Inadequate provenance | Inability to explain/reconstruct | AI-BOM, model/prompt/dataset/index/tool lineage, audit trail | Mitigate |
| R-23 | Supply-chain vulnerability | Compromise / licensing issue | SBOM/AI-BOM, trusted registries, scanning, signed artifacts, dependency/license review | Mitigate |
| R-24 | Model/license restriction | Legal/commercial exposure | model/data/license inventory, approved-use review, procurement/legal gates | Avoid/Mitigate |
| R-25 | Data residency violation | Regulatory/security breach | placement policy engine, approved regions/providers, egress controls | Avoid |
| R-26 | Unclear accountability | Incident or governance gap | named business owner, system owner, model/data owners, RACI, incident owner | Mitigate |
| R-27 | Feedback poisoning | Degraded future behavior | feedback moderation/triage, no direct auto-training, provenance, regression gate | Mitigate |
| R-28 | Unsafe cache reuse | Data leak/stale response | identity/policy/version-aware keys, TTL, sensitive-content policy, invalidation | Mitigate |
| R-29 | Non-reconstructable vector index | DR/deletion/compliance failure | governed source of truth, versioned pipeline, backup/restore/rebuild tests | Mitigate |
| R-30 | AI replaces hard business rule | Financial/compliance error | deterministic authoritative controls, model advisory boundary, ADR | Avoid |
| R-31 | Event duplicate/replay causes duplicate action | Payment/ops impact | idempotence, correlation/causation IDs, DLQ/backout, replay controls | Mitigate |
| R-32 | Misleading sustainability claim | Governance/reputation risk | declared methodology, measured-vs-estimated labels, auditable inputs | Avoid |

## Risk scoring

Suggested qualitative scale:

- Likelihood: `LOW / MEDIUM / HIGH`.
- Impact: `LOW / MEDIUM / HIGH / CRITICAL`.
- Residual status: `ACCEPTED / MITIGATED / OPEN / BLOCKING`.

A risk is **BLOCKING** when architecture review determines that production use cannot proceed before evidence/control exists.

## Risk record template

For every material risk record:

- Risk ID / title.
- Use case / component.
- Cause.
- Event.
- Consequence.
- Likelihood.
- Impact.
- Existing controls.
- Planned controls.
- Evidence/test required.
- Owner.
- Target date.
- Residual risk.
- Acceptance authority.
- Review date.

## Design Authority rule

Architecture approval does not mean risk disappears. Approval means material risks are either mitigated with evidence, explicitly accepted by an authorized owner, or tracked with conditions and deadlines.
