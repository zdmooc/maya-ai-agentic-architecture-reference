# AI Architecture Fitness Functions

Status: **DESIGNED — GOVERNANCE CATALOG / AUTOMATION OPTIONAL**

Purpose: turn important AI architecture characteristics into repeatable checks so model, provider, prompt, data and platform changes do not silently degrade the system.

A fitness function may be automated, manual, triggered, continual, temporal, atomic or holistic. The objective is evidence, not automation for its own sake.

## 1. Security & privacy fitness functions

### FF-SEC-01 — Provider eligibility
Rule: classified data must route only to policy-eligible providers/regions.
Evidence:
- policy-as-code test;
- negative routing tests;
- audit of selected endpoint.

### FF-SEC-02 — Tool least privilege
Rule: agents may invoke only tools/scopes explicitly approved for the use case.
Evidence:
- allowlist test;
- forbidden-tool negative tests;
- permission diff review.

### FF-SEC-03 — ACL before RAG context
Rule: unauthorized documents/chunks must be excluded before model context construction.
Evidence:
- cross-user/tenant negative tests;
- retrieval trace.

### FF-SEC-04 — Secrets not persisted in logs
Rule: known secret patterns/credentials must not appear in retained telemetry or archives.
Evidence:
- log scan;
- redaction tests.

### FF-SEC-05 — Cache entitlement isolation
Rule: cache keys and access prevent cross-tenant/user disclosure.
Evidence:
- negative cache tests;
- configuration review.

## 2. AI quality fitness functions

### FF-QUAL-01 — Grounding threshold
Rule: governed RAG candidate must meet agreed grounding/faithfulness threshold on regression data.

### FF-QUAL-02 — Citation correctness
Rule: citations must resolve to evidence supporting the associated claim.

### FF-QUAL-03 — Abstention behavior
Rule: insufficient evidence must produce `NO_ANSWER`, `UNKNOWN` or escalation rather than fabricated certainty.

### FF-QUAL-04 — Structured output compliance
Rule: machine-consumed output validates against its schema above the agreed threshold; critical workflows may require 100% after retries/validation.

### FF-QUAL-05 — Baseline/candidate non-regression
Rule: no model/prompt/index candidate is promoted if critical quality/safety metrics regress beyond accepted tolerance.

## 3. RAG / knowledge fitness functions

### FF-RAG-01 — Retrieval regression
Rule: representative query set maintains minimum retrieval relevance/recall.

### FF-RAG-02 — Freshness
Rule: indexed knowledge must remain within the use-case freshness SLA or be marked stale.

### FF-RAG-03 — Provenance completeness
Rule: every indexed chunk has required source/version/owner/classification/ACL/lineage metadata.

### FF-RAG-04 — Deletion lineage
Rule: deletion of governed source content propagates to derived chunks/embeddings/index/cache according to policy.

### FF-RAG-05 — Rebuildability
Rule: an index can be reconstructed from governed sources and versioned processing configuration.

## 4. Agent/tool fitness functions

### FF-AG-01 — Max steps/time/token budget
Rule: agent execution cannot exceed approved bounds without explicit escalation.

### FF-AG-02 — Sensitive action HITL
Rule: high-impact tools cannot execute without required approval state.

### FF-AG-03 — No untyped tool interface
Rule: production agent tools expose validated typed contracts rather than unrestricted shell/SQL/admin interfaces.

### FF-AG-04 — Loop/failure handling
Rule: agent stops safely on repeated failure/loop conditions and records state/evidence.

### FF-AG-05 — Policy authority external
Rule: agent/LLM output cannot override deterministic security, entitlement, transaction or risk controls.

## 5. Performance fitness functions

### FF-PERF-01 — End-to-end p95/p99
Rule: representative workload remains within agreed latency budget.

### FF-PERF-02 — Component budget
Rule: retrieval, rerank, TTFT, decode and tool-call stages remain inside allocated sub-budgets or trigger investigation.

### FF-PERF-03 — Throughput/concurrency
Rule: service sustains target load with agreed headroom and acceptable queueing.

### FF-PERF-04 — Context budget
Rule: requests cannot grow context/token use beyond approved limits without explicit exception.

### FF-PERF-05 — Capacity headroom
Rule: CPU/GPU/VRAM/queue saturation remains below agreed operational thresholds under target load.

## 6. Reliability fitness functions

### FF-REL-01 — Fallback policy compliance
Rule: failover routes only to policy-eligible endpoints.

### FF-REL-02 — Degraded-mode test
Rule: model/RAG/tool outage results in documented safe degradation rather than uncontrolled failure.

### FF-REL-03 — Rollback readiness
Rule: each deployable model/prompt/index/policy change has a valid rollback target and procedure.

### FF-REL-04 — Idempotent side effects
Rule: retried event/tool workflows do not create duplicate business effects.

### FF-REL-05 — SLO/error-budget health
Rule: when error budget burns beyond policy, risky change velocity is reduced and reliability action is triggered.

## 7. Cost / FinOps fitness functions

### FF-COST-01 — Cost per useful outcome
Rule: candidate architecture remains within agreed cost/useful-answer or business-outcome budget.

### FF-COST-02 — Token/request budget
Rule: application/model route respects per-request/user/application budgets.

### FF-COST-03 — Cache efficiency
Rule: expected cache-enabled workload maintains minimum useful hit-rate where caching is part of the cost model.

### FF-COST-04 — Expensive-model routing
Rule: high-cost models are used only when policy/capability requires them, not as universal default.

### FF-COST-05 — Observability cost
Rule: telemetry/log retention does not exceed agreed budget without explicit justification.

## 8. Portability / reversibility fitness functions

### FF-PORT-01 — Provider-specific dependency boundary
Rule: provider SDK/types remain inside approved adapter modules unless an ADR explicitly accepts coupling.

### FF-PORT-02 — Model aliases
Rule: applications reference governed model aliases/capabilities rather than scattered hard-coded endpoint IDs.

### FF-PORT-03 — Portable evaluation
Rule: core regression datasets/metrics can evaluate replacement models/providers.

### FF-PORT-04 — Externalized enterprise knowledge
Rule: enterprise knowledge remains in governed stores rather than relying solely on opaque model memory where freshness/deletion/citations matter.

### FF-PORT-05 — Exit trigger review
Rule: provider/model ADRs include review/exit triggers such as deprecation, price, quality, region or compliance change.

## 9. Governance / provenance fitness functions

### FF-GOV-01 — AI-BOM completeness
Rule: production service identifies model, prompt, dataset/corpus, embedding/index, tools, libraries/images, licenses and owners.

### FF-GOV-02 — Use-case registry
Rule: material AI use case has purpose, owner, risk level, data classes, human oversight and retirement responsibilities.

### FF-GOV-03 — Version traceability
Rule: significant AI response/action is traceable to model/prompt/index/tool/policy versions.

### FF-GOV-04 — Evidence status truthfulness
Rule: architecture docs do not label `IMPLEMENTED/TESTED/DEPLOYED/VERIFIED` without corresponding evidence.

### FF-GOV-05 — Risk acceptance freshness
Rule: accepted high/critical risks have owner, expiry/review date and current acceptance authority.

## 10. Data / integration fitness functions

### FF-DATA-01 — Contract compatibility
Rule: API/event/tool schema changes pass compatibility tests against supported consumers.

### FF-DATA-02 — Business-event identity
Rule: event-driven AI retains required event/correlation/causation/idempotency fields.

### FF-DATA-03 — Source-of-truth declaration
Rule: every critical data domain names its authoritative source; vector/cache/derived stores cannot silently become authoritative.

### FF-DATA-04 — Data residency
Rule: replicas, backups, archives, indexes and model context comply with placement constraints.

### FF-DATA-05 — Stale data visibility
Rule: data exceeding freshness policy cannot be presented as current without explicit stale status.

## 11. Compliance / Responsible AI fitness functions

### FF-RAI-01 — HITL requirement preserved
Rule: regulated/high-impact workflows cannot remove mandatory human oversight through a prompt/model/config change.

### FF-RAI-02 — Interaction retention policy
Rule: archived AI interactions comply with classification, minimization, retention and deletion policy.

### FF-RAI-03 — Fairness/explainability gate
Rule: use cases where fairness/explainability are applicable cannot promote a model without required evidence/review.

### FF-RAI-04 — License/use-right gate
Rule: model/data/corpus licensing is approved for the intended use.

## 12. Evolution cadence

Fitness functions may run:
- on every commit/PR;
- on model/prompt/index promotion;
- during deployment;
- continuously in runtime;
- daily/weekly/monthly;
- during Architecture Review Board or risk review.

Choose cadence based on how fast the protected characteristic can degrade.

## 13. Manual versus automated

Automate when:
- rule is objective and repeatable;
- failure should block promotion;
- frequent change makes manual checks unreliable.

Keep human review when:
- trade-off is contextual;
- legal/risk acceptance is required;
- business value/judgment is involved;
- metric cannot adequately represent the architecture characteristic.

## 14. Documentation template

For each implemented fitness function record:
- ID/name;
- architectural characteristic protected;
- scope;
- metric/rule;
- threshold;
- cadence;
- automated/manual;
- evidence source;
- owner;
- action on failure;
- exception authority;
- review date.

## 15. Implementation priority

Do not automate this entire catalog at once.

When a mission/use case becomes active:
1. identify the 5–10 highest-risk architectural characteristics;
2. select the smallest useful fitness-function set;
3. automate objective high-frequency checks first;
4. retain Architecture/Risk review for contextual trade-offs;
5. add functions only when they protect real architectural value.
