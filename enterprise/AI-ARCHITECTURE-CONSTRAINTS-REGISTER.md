# AI Architecture Constraints Register

Status: **REFERENCE REGISTER / DESIGN AUTHORITY**

Purpose: capture constraints that materially shape an AI solution before technology selection.

## Constraint schema

Use:

`ID | category | constraint | source/owner | impact | affected decisions | mandatory? | expiry/review | evidence/status`

## Constraint categories

### C-REG — Regulatory / compliance

Examples:

- regulated data handling;
- audit retention;
- privacy obligations;
- human oversight;
- record-keeping;
- sector-specific controls.

Architecture impact: provider eligibility, logging, data movement, HITL, explainability, evidence retention.

### C-DATA — Data classification / residency

Examples:

- SECRET/CONFIDENTIAL/INTERNAL/PUBLIC;
- EU-only residency;
- no external provider for selected classes;
- retention/deletion constraints;
- document ACL inheritance.

Architecture impact: model placement, RAG filtering, index location, egress, provider routing.

### C-SEC — Security

Examples:

- enterprise IAM only;
- mTLS/private endpoints;
- no public ingress;
- secrets in approved vault;
- tool calls least privilege;
- no sensitive prompt logging.

Architecture impact: gateway, network, observability, tool integration, deployment topology.

### C-PLAT — Platform

Examples:

- OpenShift / ARO mandatory;
- approved database/vector platforms;
- approved GitOps/IaC tooling;
- GPU hardware availability;
- namespace/project quotas.

Architecture impact: serving runtime, scheduling, capacity, portability.

### C-CLOUD — Cloud/provider

Examples:

- Azure strategic cloud;
- approved LLM providers only;
- private endpoints required;
- no provider-specific business logic without ADR;
- exit/reversibility requirement.

Architecture impact: Model Router, AI Gateway, data placement, contracts.

### C-LEGACY — Existing systems

Examples:

- mainframe/core banking unchanged;
- IBM MQ mandatory for selected flows;
- Oracle/Exadata system of record;
- WebSphere/Java estate;
- API limitations.

Architecture impact: API facade, event integration, read-only tools, migration sequence.

### C-PERF — Performance / SLA

Examples:

- p95 response target;
- synchronous timeout budget;
- event processing deadline;
- concurrency/load profile;
- no model call on hard real-time path.

Architecture impact: caching, model choice, routing, async pattern, deterministic fallback.

### C-AVAIL — Availability / DR

Examples:

- multi-AZ requirement;
- RTO/RPO;
- no single model/provider dependency;
- degraded service mandatory.

Architecture impact: redundancy, fallback, replication, rebuild strategy.

### C-COST — Budget / FinOps

Examples:

- monthly AI budget;
- token/request budget;
- GPU budget;
- cloud spend cap;
- showback requirement.

Architecture impact: model size/provider, caching, self-host vs API, autoscaling.

### C-GREEN — Sustainability

Examples:

- reuse existing platform capacity;
- avoid idle GPU pools;
- carbon/energy reporting where methodology exists.

Architecture impact: placement, scaling, workload scheduling.

### C-ORG — Organization / skills / support

Examples:

- operations team supports OpenShift but not bespoke GPU stack;
- 24/7 support requirement;
- limited Data Science capability;
- architecture standards/Design Authority process.

Architecture impact: complexity budget, managed vs self-host, operational ownership.

### C-LIC — Licensing / legal

Examples:

- model license restrictions;
- corpus usage rights;
- open-source license policy;
- export/commercial-use constraints.

Architecture impact: model/data/tool eligibility and AI-BOM.

### C-TIME — Delivery

Examples:

- fixed regulatory deadline;
- MVP deadline;
- procurement lead time;
- environment availability.

Architecture impact: transition architecture, reuse vs build, POC scope.

## Example entries

| ID | Category | Constraint | Architecture consequence |
|---|---|---|---|
| C-DATA-001 | Residency | Confidential documents remain in approved EU/private environment | Data Policy Engine excludes unauthorized providers |
| C-LEGACY-001 | Legacy | Payment system of record remains unchanged | Integrate through API/MQ/Kafka; no direct agent mutation |
| C-SEC-001 | Security | Sensitive action requires deterministic authorization | LLM/agent cannot grant permission |
| C-COST-001 | FinOps | Monthly model budget capped | Router/caching/model tiers required |
| C-PERF-001 | Performance | User p95 bounded | latency budget and fallback model required |

## Constraint-to-ADR rule

Any constraint that materially changes technology choice or architecture must be referenced by an ADR.

Example:

`C-DATA-001 -> ADR-MODEL-PLACEMENT-001 -> restricted corpus uses private/OpenShift inference only.`

## Review rule

Constraints are not eternal assumptions. Every non-regulatory constraint should have an owner and review/expiry condition where possible.