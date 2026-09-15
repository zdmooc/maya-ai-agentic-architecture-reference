# AI Policy-as-Code Controls

Status: **DESIGNED — CONTROL CATALOG / NO ENFORCEMENT CLAIM**

Purpose: define AI-specific controls that can be enforced in CI/CD, admission policy, gateway policy or runtime policy engines.

## 1. Control principles

AI policy-as-code must protect real architecture qualities, not exist as decorative YAML.

Every control should have:

- policy objective;
- scope;
- enforcement point;
- evidence;
- exception process;
- version;
- owner.

## 2. Workload metadata controls

Require metadata such as:

- application/service owner;
- business domain;
- environment;
- data classification;
- AI risk class;
- model-id/model-alias;
- provider-id where applicable;
- cost center;
- human-review requirement;
- retention class;
- residency requirement;
- approved-use-case identifier.

## 3. Model/provider controls

Examples:

- only approved model aliases may be used;
- direct application coupling to unapproved provider endpoints is denied;
- restricted data classes may use only eligible providers/placements;
- model versions must be pinned for promoted workloads;
- fallback models must have an explicitly approved policy;
- deprecated or blocked models cannot receive new traffic.

## 4. Data and RAG controls

- retrieval corpus must carry classification and ACL metadata;
- restricted documents cannot be indexed into an ineligible store;
- ingestion must record source, hash, lineage and retention policy;
- citations/provenance required for designated high-risk RAG use cases;
- stale/expired corpus versions can be blocked;
- deletion requirements must propagate to derived indexes where applicable.

## 5. Agent and tool controls

- tool allowlist by agent/use case;
- explicit scopes/permissions per tool;
- timeout and rate-limit requirements;
- no arbitrary shell/command execution by default;
- high-impact tools require deterministic policy and/or HITL;
- sensitive actions require audit correlation IDs;
- agent autonomy budget/step limit must be bounded.

## 6. Human-review controls

Policy may require human approval when:

- business impact exceeds an agreed threshold;
- financial, customer, compliance or production change is involved;
- model confidence/evidence quality is below threshold;
- conflicting evidence exists;
- policy explicitly classifies the action as non-autonomous.

No policy engine should allow an LLM to self-waive a human-review requirement.

## 7. Resource and platform controls

Examples for OpenShift/Kubernetes environments:

- CPU/memory requests and limits;
- approved registries;
- signed/verified images when required;
- non-privileged execution;
- NetworkPolicy baseline;
- namespace/tenant boundaries;
- GPU requests/limits and quotas;
- approved accelerator classes;
- labels for model/workload/accounting identity;
- secrets outside Git and approved secret-store patterns.

## 8. Cost controls

- per-application/provider/model budget;
- token/request caps;
- concurrency caps;
- GPU quota;
- expensive-model eligibility only for justified use cases;
- budget breach -> throttle/fallback/reject according to policy;
- no silent escalation to a more expensive model.

## 9. Evaluation/promotion controls

Promotion to a higher environment can require:

- minimum evaluation score;
- no regression on critical golden tests;
- prompt-injection/security regression pass;
- latency/cost budget pass;
- model/provider eligibility pass;
- rollback target available;
- evidence bundle produced.

## 10. Enforcement points

Controls may be implemented through:

- CI validators;
- GitOps policy checks;
- Kyverno or another Kubernetes policy engine;
- AI Gateway policy;
- application/runtime guardrails;
- IAM/RBAC;
- data-platform ACLs;
- evaluation/promotion pipelines.

Do not force every AI concern into Kubernetes admission policy. Place the control where it has authoritative context.

## 11. Status discipline

This file is a **DESIGNED control catalog**. Individual controls become `IMPLEMENTED/TESTED/DEPLOYED/VERIFIED` only when corresponding code, tests and runtime evidence exist.