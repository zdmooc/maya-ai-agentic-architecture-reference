# Solutions Architect's Handbook — Architecture Alignment

Status: **IN PROGRESS — ARCHITECTURE EXTRACTION / NO IMPLEMENTATION CLAIM**

Source: *Solutions Architect's Handbook — 3rd Edition* (Saurabh Shrivastava, Neelanjali Srivastav).

Purpose: extract only the material useful to an **AI Solution Architect / Enterprise AI Architect / AI Platform Architect**, compare it with the current reference repository, and close architecture-documentation gaps without turning this into a developer or Data Science learning path.

## 1. Why this book matters to this repository

The book covers the role of the Solution Architect, functional and non-functional requirements, solution architecture patterns, cloud-native architecture, performance, ML architecture, Generative AI architecture, legacy modernization, Solution Architecture Documents and architecture communication.

For this repository, the main value is not learning one cloud product. It is strengthening the **architecture method and deliverables** around the existing AI capabilities.

## 2. Current strengths already present

The repository already covers strongly:

- end-to-end AI/Agentic target architecture;
- C4-style component responsibilities;
- deterministic / ML / LLM boundaries;
- RAG, agents, MCP and HITL;
- OpenShift / OpenShift AI / KServe / vLLM;
- Azure/ARO target architecture;
- observability, security and LLMOps;
- resilience principles including timeouts, circuit breakers, degraded modes and replay;
- Enterprise AI theoretical design I13-I20;
- AI Gateway, Model Router and hybrid/multi-cloud strategy;
- Responsible AI, AI-BOM and governance intent;
- Design Authority intent and ADR-based decisions.

## 3. Gaps identified from an Architect viewpoint

### GAP-SA-01 — Formal Solution Architecture Document (SAD)

The repository contains architecture documents, but not yet one canonical **AI Solution Architecture Document template** tying the material together.

Target SAD structure:

1. Executive summary and business context.
2. Scope / out of scope.
3. Stakeholders and concerns.
4. Functional requirements.
5. Non-functional requirements / quality attributes.
6. Constraints and assumptions.
7. Current-state architecture.
8. Target-state architecture.
9. Application/service view.
10. Data/knowledge view.
11. Integration/API/event view.
12. AI/model/RAG/agent view.
13. Security/privacy/compliance view.
14. Deployment/platform/network view.
15. Observability/SRE/operations view.
16. Capacity/performance/cost view.
17. Resilience/BCP/DR view.
18. Architecture decisions / ADRs.
19. Risks, trade-offs and technical debt.
20. Transition architecture / roadmap.
21. Validation/evidence status.

Future action: create a reusable SAD template under I15 / Design Authority work. No POC required.

### GAP-SA-02 — Explicit FR/NFR separation

The current repository has many NFR-like controls but no canonical FR/NFR catalog for an AI solution.

Minimum AI NFR families:

- availability;
- latency and throughput;
- scalability;
- resilience and recoverability;
- security;
- privacy and data residency;
- explainability/traceability;
- quality/grounding;
- safety/abstention;
- observability;
- operability/supportability;
- portability/reversibility;
- maintainability;
- cost/FinOps;
- GreenOps where measurable;
- compliance and auditability.

Future action: consolidate these as an architecture checklist and use them as Architecture Review Board criteria.

### GAP-SA-03 — Architecture constraints register

Add one explicit register for:

- regulatory constraints;
- data locality;
- cloud/provider constraints;
- platform constraints;
- legacy dependencies;
- licensing;
- performance/SLA;
- organization/skills constraints;
- budget constraints;
- delivery deadlines;
- model/provider availability.

Each constraint should map to one or more ADRs.

### GAP-SA-04 — Performance architecture as a first-class viewpoint

The repository already has inference-performance concepts, but Solution Architecture should also make generic performance architecture explicit:

`latency budget -> component budget -> concurrency -> throughput -> caching -> autoscaling -> queueing -> storage/network -> model inference -> SLO`.

For AI specifically:

`user latency = gateway + retrieval + reranking + model TTFT + decode + tool calls + policy/output validation`.

This belongs in I14/I17 and the SAD template.

### GAP-SA-05 — Legacy modernization / AI integration

This is especially relevant for banking and insurance.

Reference decision ladder:

`encapsulate -> API enable -> event enable -> replatform -> refactor -> rearchitect -> replace`.

AI must not force unnecessary core-system replacement. Prefer governed interfaces around legacy systems where feasible:

- REST/API facade;
- MQ/Kafka events;
- read-only tools for agents;
- RAG over documentation/runbooks;
- deterministic policy around sensitive actions;
- HITL for high-impact remediation.

This maps directly to the existing IBM MQ, Kafka, API Management and payment repositories.

### GAP-SA-06 — Solution Architect operating model

The book reinforces that architecture is not only diagrams. Formalize the lifecycle:

`Business demand -> discovery -> FR/NFR -> constraints -> options -> trade-off analysis -> target architecture -> ADR -> POC only if uncertainty requires it -> review -> delivery governance -> production readiness -> post-launch operability`.

POCs should be used to reduce material uncertainty, not as a default engineering activity.

## 4. GenAI architecture chapter — mapping to current repository

The book includes a dedicated Generative AI Architecture chapter with foundation-model selection, hallucination mitigation, a reference architecture and implementation challenges.

Current repository mapping:

| Book concern | Current repository |
|---|---|
| GenAI use cases | Architecture Vision + I15 |
| Foundation-model selection | AI Engineering fundamentals + I18 |
| GenAI system architecture | I13-I20 theoretical design |
| Hallucination mitigation | RAG + citations + abstention + deterministic evidence |
| Security | I16 + I8 |
| Cloud deployment | I11/I17/I18 |
| ML/MLOps | I5/I10/I14/I17 |
| Human oversight | I7 + I16 |
| Production operations | I8/I14/I17 |

Conclusion: the repository is already stronger than this chapter on modern enterprise GenAI controls. The main additions from this book are therefore **architecture discipline and deliverable structure**, not new AI runtime components.

## 5. Solution Architecture patterns relevant to AI

Patterns to retain explicitly in the reference catalog:

- layered/n-tier where appropriate;
- API/service-oriented boundaries;
- DDD bounded contexts;
- circuit breaker;
- bulkhead/isolation;
- cache patterns;
- stateless services where possible;
- stateful stores where required;
- event-driven architecture;
- queues and back-pressure;
- saga/orchestration for distributed workflows;
- service mesh where justified;
- clean architecture / dependency inversion;
- anti-pattern: tight provider coupling;
- anti-pattern: hidden state in agents;
- anti-pattern: unbounded context/tool access;
- anti-pattern: LLM as authoritative policy engine.

## 6. Architecture artefacts to add later

No local PC is needed to design these. They are documentation artifacts:

1. `AI-SOLUTION-ARCHITECTURE-DOCUMENT-TEMPLATE.md`
2. `AI-FR-NFR-CATALOG.md`
3. `AI-ARCHITECTURE-CONSTRAINTS-REGISTER.md`
4. `AI-ARCHITECTURE-REVIEW-CHECKLIST.md`
5. `AI-PERFORMANCE-BUDGET-TEMPLATE.md`
6. `LEGACY-TO-AI-INTEGRATION-PATTERNS.md`

These should be created only as architecture documents; executable POCs remain demand-driven.

## 7. Interview outcomes

After this alignment, an AI Solution Architect should be able to answer:

- How do you move from a business requirement to an AI target architecture?
- How do FRs differ from NFRs in an AI solution?
- How do you build and maintain a SAD?
- How do you choose among API, event, RAG, agent and deterministic integration?
- How do you integrate AI with a legacy banking platform without unnecessary replacement?
- How do you design for latency, throughput, failure and degradation?
- When is a POC justified?
- How do you document trade-offs and architecture decisions?
- What must be validated before production readiness?

## 8. Current conclusion

**No new AI implementation POC is required from this book.**

The main value is to upgrade the repository from a strong AI technical reference into a stronger **Solution Architecture dossier** by formalizing SAD, FR/NFR, constraints, performance budgets, modernization patterns and the architect operating model.

Next extraction target after this book: Enterprise Generative AI Well-Architected Framework & Patterns.