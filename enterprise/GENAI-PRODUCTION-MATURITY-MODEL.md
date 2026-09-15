# GenAI Production Maturity Model

Status: **DESIGNED — ARCHITECTURE ASSESSMENT MODEL**

Purpose: distinguish a convincing demo from a production-ready enterprise AI capability.

## Level 0 — Idea

Characteristics:
- business problem is informal;
- no measurable success criteria;
- no architecture decision;
- no data/security assessment.

Exit criteria:
- business owner and outcome defined;
- AI justified against simpler alternatives;
- main risks/constraints identified.

## Level 1 — Prototype

Characteristics:
- one model/provider path;
- manual prompt/configuration;
- synthetic/sample data;
- limited local evaluation;
- no production SLO or operational ownership.

What it proves:
- feasibility of a narrow interaction or workflow.

What it does not prove:
- production quality, security, scalability, resilience, cost or compliance.

Exit criteria:
- representative use case and data;
- baseline quality evidence;
- architecture pattern selected;
- known gaps documented.

## Level 2 — Controlled POC

Characteristics:
- representative corpus/workload;
- explicit hypothesis to validate;
- baseline/candidate evaluation;
- basic security and policy controls;
- trace/cost/latency capture;
- reproducible environment/config.

Exit criteria:
- POC uncertainty resolved with evidence;
- go/no-go decision;
- target FR/NFR defined;
- production gap register created.

## Level 3 — Pre-Production

Characteristics:
- environment separation;
- versioned code/model/prompt/index/tools;
- CI/CD or controlled promotion;
- regression/evaluation gates;
- secrets/IAM/network controls;
- observability;
- rollback;
- performance/capacity testing;
- runbooks and ownership;
- threat/risk/compliance review.

Exit criteria:
- production-readiness review passed or conditionally approved;
- SLOs and support model accepted;
- blocking risks closed.

## Level 4 — Production Managed

Characteristics:
- SLI/SLO monitoring;
- error-budget tracking;
- alerting/on-call or operational ownership;
- model/provider/prompt/index lifecycle controls;
- cost/showback visibility;
- feedback triage;
- incident/rollback process;
- periodic quality/security regression;
- interaction retention policy;
- DR/failure/fallback strategy.

Exit criteria:
- sustained operational evidence;
- measurable business outcomes;
- predictable change process.

## Level 5 — Enterprise Platformized

Characteristics:
- reusable AI Gateway/model routing;
- shared prompt registry;
- governed RAG/knowledge platform;
- tool registry/sandboxing;
- session/state services;
- shared evaluation and feedback services;
- serving/training infrastructure;
- standard observability/SRE;
- policy/Responsible AI/AI-BOM;
- FinOps and capacity management;
- developer self-service/templates;
- portfolio governance and Design Authority.

Outcome:
- teams build approved AI products on reusable governed capabilities rather than rebuilding infrastructure per use case.

## Maturity dimensions

Score each dimension independently from 0 to 5:

- Business value/product ownership.
- Architecture/SAD/ADRs.
- Model/evaluation quality.
- Data/knowledge governance.
- Security/privacy.
- Responsible AI/compliance.
- LLMOps/change management.
- Reliability/SRE.
- Performance/capacity.
- Cost/FinOps.
- Observability/audit.
- Portability/exit strategy.
- Operational ownership.
- Platform reuse.

Do not average away a blocking deficiency: a production candidate cannot be considered mature if a critical security, compliance or reliability control is missing.

## Architect use

Use this model to answer:

1. What maturity level is the use case today?
2. What level is actually required by business criticality?
3. Which dimension is the limiting factor?
4. Which evidence is missing?
5. Is a new POC needed, or is the remaining work architecture/engineering/governance?
6. Which shared platform capabilities should replace application-specific components?
