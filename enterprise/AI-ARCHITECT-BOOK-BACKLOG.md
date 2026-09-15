# AI Architect Book Backlog

Status: **BASELINE COMPLETE — 9/9 ARCHITECTURE SOURCES EXTRACTED / FUTURE SOURCES DEMAND-DRIVEN**

Purpose: maintain a focused source backlog for **AI Solution Architect / Enterprise AI Architect / AI Platform Architect** work. Developer-first books centered on Python, LangChain or Data Science implementation are intentionally excluded unless they contain a material architecture gap.

Method:

`SOURCE -> EXTRACT ARCHITECTURE PRINCIPLES -> MAP TO REFERENCE -> IDENTIFY REAL GAP -> ADD ADR/NFR/PATTERN -> DEFER POC UNTIL BUSINESS DEMAND`

No book creates a mandatory implementation roadmap by itself.

## Completion matrix

| # | Source | Status | Main contribution retained |
|---|---|---|---|
| 1 | *AI Engineering* — Chip Huyen | **DONE** | foundation models, evaluation, prompting, RAG/agents, fine-tuning decisions, datasets, inference, gateway/router, feedback |
| 2 | *Solutions Architect's Handbook — 3rd Ed.* | **DONE** | Solution Architect method, SAD, FR/NFR, constraints, patterns, ADRs, risk/RACI, performance, legacy integration |
| 3 | *Enterprise Generative AI Well-Architected Framework & Patterns* | **DONE** | GenAI Well-Architected assessment, governance, security/privacy, compliance, reliability, cost, archival |
| 4 | *Architecting Generative AI Applications* | **DONE** | prototype-to-production, LLMOps, platform capabilities, SRE/error budgets, online experimentation |
| 5 | *Google Machine Learning and Generative AI for Solutions Architects* | **DONE** | unified classic-ML/GenAI lifecycle, governance and provider-neutral platform mapping |
| 6 | *The Machine Learning Solutions Architect Handbook — 2nd Ed.* | **DONE** | regulated-industry/financial-services use cases and ML/GenAI Solution Architecture framing |
| 7 | *Designing Machine Learning Systems* — Chip Huyen | **DONE** | production ML, monitoring, drift, retraining, shadow/canary/A-B, adaptability |
| 8 | *Designing Data-Intensive Applications — 2nd Ed.* | **DONE** | system of record/derived state, consistency, partial failure, schemas, replication/sharding, batch/stream |
| 9 | *Building Evolutionary Architectures — 2nd Ed.* | **DONE** | fitness functions, automated governance, reversibility, incremental/evolvable architecture |

## 1. AI Engineering — Chip Huyen

Status: **THEORETICAL ALIGNMENT COMPLETE**

Repository outputs:
- `AI-ENGINEERING-FUNDAMENTALS.md`
- `AI-ENGINEERING-BOOK-ALIGNMENT.md`
- enterprise I13-I20 theoretical design.

Architect focus:
- model/system selection;
- evaluation;
- prompt/context;
- RAG and agents;
- fine-tuning decision criteria;
- dataset engineering;
- inference optimization;
- gateway/router/cache/observability/feedback.

## 2. Solutions Architect's Handbook — 3rd Edition

Status: **ARCHITECTURE EXTRACTION COMPLETE**

Repository outputs:
- `SOLUTIONS-ARCHITECTS-HANDBOOK-ALIGNMENT.md`
- `AI-SOLUTION-ARCHITECTURE-DOCUMENT-TEMPLATE.md`
- `AI-FR-NFR-CATALOG.md`
- `AI-ARCHITECTURE-CONSTRAINTS-REGISTER.md`
- `AI-PERFORMANCE-BUDGET-TEMPLATE.md`
- `AI-ARCHITECTURE-REVIEW-CHECKLIST.md`
- `AI-ARCHITECTURE-PATTERN-CATALOG.md`
- `AI-ARCHITECTURE-ADR-REFERENCE.md`
- `AI-ARCHITECTURE-RISK-REGISTER.md`
- `AI-ARCHITECTURE-RACI.md`
- `LEGACY-TO-AI-INTEGRATION-PATTERNS.md`

No implementation POC required.

## 3. Enterprise Generative AI Well-Architected Framework & Patterns

Status: **ARCHITECTURE EXTRACTION COMPLETE**

Repository outputs:
- `ENTERPRISE-GENAI-WELL-ARCHITECTED-ALIGNMENT.md`
- `GENAI-WELL-ARCHITECTED-SCORECARD.md`
- `AI-INTERACTION-ARCHIVAL-COMPLIANCE-PATTERN.md`

Architect focus:
- operational excellence;
- security/privacy;
- compliance/Responsible AI;
- reliability;
- cost;
- interaction archival/audit;
- guardrails and observability.

AWS-specific tutorials are deferred unless an AWS mission requires them.

## 4. Architecting Generative AI Applications

Status: **ARCHITECTURE EXTRACTION COMPLETE**

Repository outputs:
- `ARCHITECTING-GENAI-APPLICATIONS-ALIGNMENT.md`
- `GENAI-PRODUCTION-MATURITY-MODEL.md`
- `GENAI-PLATFORM-CAPABILITY-MAP.md`
- `GENAI-SRE-SLO-ERROR-BUDGET.md`
- `GENAI-ONLINE-EXPERIMENTATION-PATTERN.md`

Architect focus:
- prototype versus production;
- LLMOps;
- reusable platform capabilities;
- SRE/error budgets;
- resilience;
- controlled online experimentation.

## 5. Google Machine Learning and Generative AI for Solutions Architects

Status: **ARCHITECTURE EXTRACTION COMPLETE**

Repository outputs:
- `GOOGLE-AI-SOLUTIONS-ARCHITECT-ALIGNMENT.md`
- `AI-ML-SOLUTION-ARCHITECTURE-LIFECYCLE.md`

Architect focus:
- deterministic versus classic ML versus GenAI;
- ML lifecycle awareness without Data Scientist depth;
- MLOps/governance;
- provider-neutral logical architecture.

No GCP POC unless a target mission requires GCP/Vertex AI evidence.

## 6. The Machine Learning Solutions Architect Handbook — 2nd Edition

Status: **ARCHITECTURE EXTRACTION COMPLETE**

Repository outputs:
- `ML-SOLUTIONS-ARCHITECT-HANDBOOK-ALIGNMENT.md`
- `BANKING-INSURANCE-AI-USE-CASE-MAP.md`

Architect focus:
- payments/settlement;
- fraud/anomaly;
- AML/trade surveillance;
- credit;
- customer service;
- wealth/advisory;
- insurance underwriting/claims;
- regulated AI boundaries.

Algorithm and AWS lab detail is deliberately deprioritized.

## 7. Designing Machine Learning Systems — Chip Huyen

Status: **ARCHITECTURE EXTRACTION COMPLETE**

Repository outputs:
- `DESIGNING-ML-SYSTEMS-ALIGNMENT.md`
- `ML-PRODUCTION-MONITORING-DRIFT-LIFECYCLE.md`

Architect focus:
- reliability/scalability/maintainability/adaptability;
- batch versus online prediction;
- drift and delayed labels;
- retraining governance;
- shadow/canary/A-B/champion-challenger;
- production ownership.

## 8. Designing Data-Intensive Applications — 2nd Edition

Status: **ARCHITECTURE EXTRACTION COMPLETE**

Repository outputs:
- `DESIGNING-DATA-INTENSIVE-APPLICATIONS-ALIGNMENT.md`
- `AI-DATA-SYSTEMS-ARCHITECTURE-PRINCIPLES.md`

Architect focus:
- system of record versus derived state;
- vector/index/cache as derived data;
- schema evolution;
- replication/sharding;
- consistency;
- partial failures/timeouts;
- idempotence/exactly-once business effects;
- batch versus streaming;
- deletion through derived stores.

No standalone DDIA POC; reuse MQ/Kafka/RAG/platform evidence.

## 9. Building Evolutionary Architectures — 2nd Edition

Status: **ARCHITECTURE EXTRACTION COMPLETE**

Repository outputs:
- `BUILDING-EVOLUTIONARY-ARCHITECTURES-ALIGNMENT.md`
- `AI-ARCHITECTURE-FITNESS-FUNCTIONS.md`

Architect focus:
- guided incremental change;
- fitness functions;
- continuous/automated governance;
- reversibility;
- last responsible moment;
- provider/model/prompt/index evolution;
- architecture for testability;
- bounded coupling and anticorruption layers.

Automation of fitness functions is demand-driven; the catalog does not imply all checks are implemented.

## Navigation

Use `AI-ARCHITECT-KNOWLEDGE-BASE-INDEX.md` as the primary entry point into the resulting architecture knowledge base.

## Future-source policy

The baseline book program is now closed. A new source is added only when at least one condition is true:

1. it addresses a material gap not already covered;
2. a target mission requires a technology/provider/domain-specific architecture;
3. a regulation/standard changes materially;
4. a new architecture paradigm changes enterprise AI design practice;
5. it provides authoritative evidence needed for an architecture decision.

Do not accumulate books for volume.

## Future POC policy

For any mission/use case:

1. map requirements to this knowledge base;
2. reuse existing specialist implementation evidence;
3. identify the smallest missing evidence;
4. build only that POC;
5. test/capture evidence;
6. update status truthfully;
7. stop.

Architecture/theory may remain `DESIGNED` while runtime proof is intentionally deferred.
