# GenAI Well-Architected Scorecard

Status: **DESIGNED — ARCHITECTURE ASSESSMENT TEMPLATE**

Purpose: assess an enterprise GenAI solution consistently across business, architecture, operations, security, compliance, reliability, performance, cost, AI quality, data/knowledge and portability.

Scoring:

- `0` — absent / unknown.
- `1` — ad hoc / undocumented.
- `2` — designed but not evidenced.
- `3` — implemented/tested with evidence.
- `4` — operationally verified and governed.

A high total score does not override a blocking risk. Any critical control marked blocking prevents production approval.

## Pillar 1 — Business & Architecture Fitness

Check:
- business outcome/KPI defined;
- AI justified versus deterministic/search alternatives;
- selected pattern documented;
- rejected options/trade-offs recorded;
- business owner/accountability named;
- success/failure/abstention criteria explicit;
- architecture SAD exists;
- key ADRs approved;
- exit/revisit triggers defined.

Red flags:
- “use AI” is the requirement;
- no measurable value;
- agent chosen before workflow analysis;
- no system-of-record boundary.

## Pillar 2 — Operational Excellence

Check:
- deployment/promotion process defined;
- model/prompt/index/tool versions traceable;
- runbooks exist;
- incident ownership named;
- SLOs/alerts defined;
- production support model defined;
- rollback tested;
- observability cost/log-retention considered;
- change management covers model/provider updates.

Red flags:
- deployment success treated as quality acceptance;
- no rollback;
- no on-call/run ownership.

## Pillar 3 — Security & Privacy

Check:
- IAM/authN/authZ architecture;
- least privilege for tools;
- secrets/certificates lifecycle;
- tenant isolation;
- ACL enforced before RAG context construction;
- PII/secrets inspection;
- provider/data eligibility controls;
- network/egress controls;
- cache isolation;
- prompt-injection/tool-abuse negative tests;
- sensitive logging policy.

Blocking examples:
- model decides authorization;
- broad admin/shell/SQL tool access;
- cross-tenant context leakage.

## Pillar 4 — Compliance & Responsible AI

Check:
- use-case registry entry;
- purpose and affected-user scope;
- risk classification;
- human oversight level;
- limitations documented;
- privacy/DPIA hooks where applicable;
- explainability/fairness applicability assessed;
- interaction archival/retention policy;
- legal hold/deletion responsibilities;
- AI-BOM/provenance;
- incident/accountability owner;
- retirement plan.

Red flags:
- indefinite raw prompt retention by default;
- no accountable business/risk owner.

## Pillar 5 — Reliability & Resilience

Check:
- dependency map includes model, vector store, tools, IAM, gateway, network and workflow;
- timeouts/circuit breakers;
- provider quota/rate failure strategy;
- graceful degradation;
- fallback eligibility policy;
- stale-data behavior;
- knowledge/index restore/rebuild;
- retry/idempotence where actions/events occur;
- HA/DR targets;
- failure/chaos scenarios identified;
- rollback/canary strategy.

Red flags:
- silent use of stale knowledge;
- unsafe provider failover that violates data policy.

## Pillar 6 — Performance & Scalability

Check:
- end-to-end latency budget;
- TTFT/decode/tool/retrieval budgets;
- p50/p95/p99 targets;
- throughput/concurrency target;
- queue/admission controls;
- autoscaling approach;
- cache design;
- context-size limits;
- GPU/CPU/VRAM capacity estimate;
- representative benchmark plan;
- batch/async option assessed.

Red flags:
- only average latency measured;
- estimates presented as benchmark facts.

## Pillar 7 — Cost & GreenOps

Check:
- token/input/output cost tracked;
- embedding/vector cost tracked;
- GPU/infrastructure allocation tracked;
- cache efficiency measured;
- logging/observability cost included;
- cost/request and cost/useful-answer available;
- budgets/quotas/alerts;
- model routing/right-sizing strategy;
- private vs managed economics assessed;
- energy/carbon claims distinguish measured vs estimated.

Red flags:
- model selected only by token price;
- no usage budget or denial-of-wallet controls.

## Pillar 8 — AI Quality & Evaluation

Check:
- representative evaluation dataset;
- exact/functional metrics where possible;
- LLM-as-judge controlled/calibrated where used;
- hallucination/grounding metrics;
- citation correctness;
- abstention correctness;
- prompt injection/security evals;
- baseline vs candidate evaluation;
- component-level evaluation;
- regression gate in promotion;
- user feedback triage loop.

Red flags:
- public benchmark used as acceptance test;
- anecdotal “looks good” evaluation.

## Pillar 9 — Data & Knowledge Governance

Check:
- source ownership/provenance;
- classification/ACL metadata;
- source/version/hash lineage;
- chunk/embedding/index lineage;
- freshness/expiry;
- retention/deletion;
- licensing/usage rights;
- PII flags;
- quarantine/curation path;
- rebuildable index;
- train/eval separation for tuned models.

Blocking examples:
- private content indexed without entitlement model;
- deletion cannot propagate to derived stores.

## Pillar 10 — Portability & Hybrid Placement

Check:
- model aliases/provider abstraction;
- provider eligibility by data class;
- residency/region controls;
- portable prompt/evaluation assets;
- externalized knowledge/state;
- explicit coupling ADRs;
- compliant fallback;
- exit strategy;
- private/cloud placement decision matrix;
- observability/audit portability.

Red flags:
- application logic irreversibly embeds one provider without business justification;
- fallback ignores classification/residency.

## Assessment summary

Record:
- use case;
- assessment date;
- reviewers;
- score per pillar;
- blocking findings;
- conditions to approval;
- evidence links;
- accepted risks;
- next review date.

Suggested interpretation:
- `0–15`: prototype/ad hoc, not production-ready.
- `16–25`: architecture partially designed; major gaps.
- `26–32`: credible design; evidence gaps remain.
- `33–36`: strong implementation/test maturity.
- `37–40`: operationally mature, subject to no blocking finding.

The numeric score is a communication aid, not a substitute for architecture judgment or risk acceptance.
