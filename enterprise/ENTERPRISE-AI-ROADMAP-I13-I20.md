# Enterprise AI Roadmap — I13 to I20

Status: **PLANNED / NOT IMPLEMENTED**

This roadmap extends the existing I0-I12 evidence-driven Agentic AI program toward the Enterprise AI Portfolio V10 baseline.

It does not replace the existing iterations. It closes the enterprise architecture, knowledge-platform, governance, AI infrastructure and multi-cloud gaps identified in `enterprise/V10-GAP-MATRIX.md`.

## Program rules

Every iteration must follow:

`ANALYSE -> AUDIT -> ARCHITECTURE -> REUSE DECISION -> IMPLEMENT -> TEST -> EVIDENCE -> DOCUMENT -> COMMIT -> BILAN -> STOP`

A capability remains `PLANNED`, `DESIGNED` or `IMPLEMENTED` until test/deployment evidence justifies a higher status.

The repository must reuse specialist repositories deliberately rather than duplicate them.

---

## I13 — Enterprise Knowledge Copilot & Governed Knowledge Ingestion

V10 coverage: **A + I + J**

### Goal

Transform the existing workflow-specific RAG capability into a generic, enterprise-grade Knowledge Copilot for operators and architects of critical platforms.

### Scope

- generic `/v1/chat`, `/v1/ingestion/jobs`, `/v1/feedback`, `/v1/health`, `/v1/metrics` APIs;
- fictitious enterprise corpus: OpenShift, IBM MQ, Java/WebSphere/Open Liberty, architecture standards, runbooks and synthetic payment-incident procedures;
- source/version/date visibility and clickable citation contract;
- explicit abstention/no-answer behavior;
- source vs synthesis vs hypothesis distinction;
- bilingual FR/EN test set;
- role-oriented answer modes: operator, architect, support;
- ingestion connectors or adapters for Git/files/API and reference contracts for SharePoint/GED/DB;
- zones: Raw, Quarantine, Curated, Index, Audit;
- document data contract including source URI, version/hash, domain, application, environment, classification, ACL, owner, validation, expiry, language, retention, purpose, residency, authorized providers, usage rights/license, PII flag and deletion state;
- deletion lineage from source to derived chunks/embeddings/index/cache/audit proof;
- FastAPI/Pydantic/OpenAPI contracts;
- API/model/prompt/index version fields;
- correlation IDs, typed errors, security and observability hooks.

### Reuse

- I6 RAG security/admission patterns;
- I8 observability/security patterns;
- API patterns from `mayabank-api-management-architecture` where useful.

### Exit criteria

- one end-to-end synthetic document ingestion flow;
- one governed RAG query flow with citations;
- one intentional no-answer test;
- one ACL-negative test;
- one deletion-lineage test;
- FR/EN golden questions;
- CI evidence and README/demo instructions.

---

## I14 — Enterprise AI Evaluation, Feedback, FinOps & GreenOps

V10 coverage: **M + G**

### Goal

Create a measurable quality/cost/feedback loop for the Knowledge Copilot and reusable AI services.

### Scope

- golden dataset with security, ACL and no-answer cases;
- baseline vs candidate evaluation;
- retrieval recall/relevance, grounding, citation correctness, abstention and useful-answer metrics;
- latency/error/cost measurements;
- FR/EN quality checks;
- online feedback contract and triage workflow;
- feedback -> annotation -> correction -> regression loop;
- CI/CD evaluation gates;
- token, request, latency, retrieval and model metrics;
- cost per useful response, user and assisted incident;
- provider cost attribution;
- cache-hit and logging-cost KPIs;
- budget/forecast/anomaly concepts;
- showback schema;
- energy/token and accelerator utilization fields when measured data is available.

### Reuse

- I5 evaluation discipline;
- I8 OpenTelemetry/metrics;
- `mayabank-carbon-aware-decision-architecture` for GreenOps patterns;
- Azure FinOps guidance from `mayabank-azure-cloud-ai-platform`.

### Exit criteria

- reproducible evaluation report;
- candidate promotion gate;
- feedback round-trip test;
- cost-attribution example;
- no claim of energy efficiency without measured data.

---

## I15 — Enterprise AI Architecture Pack, Design Authority & Reference Catalog

V10 coverage: **K + V + W + X + Y + Z**

### Goal

Elevate the repository from an advanced solution architecture reference into an explicit Enterprise AI Architecture and Design Authority portfolio.

### Scope

- business context and AI capability map;
- TOGAF-aligned architecture lifecycle mapping;
- ArchiMate views or version-controlled equivalent for motivation/business/application/technology/data/deployment;
- C4/solution views;
- NFR catalog;
- enterprise risk register;
- architecture roadmap and transition states;
- COMEX decision pack: value, costs, risks, options and recommendation;
- AI Integration Blueprint: API Gateway, AI Gateway, RAG service, Agent service, Evaluation/Policy service, domain APIs and event integration;
- OpenAPI/AsyncAPI integration standards;
- commands/events/queries, correlation/causation IDs, idempotency, outbox, DLQ/replay and versioning principles;
- Architecture Review Board workflow;
- review scorecard;
- exception and technical-debt process;
- go/no-go criteria;
- approved pattern/component catalog;
- anti-pattern catalog;
- adoption/value KPIs, onboarding and feedback-to-backlog model.

### Reuse

- current Architecture Vision and Target Architecture;
- existing `reuse/` catalog;
- Kafka/MQ/API specialist repositories;
- TOGAF/ArchiMate companion repositories as learning/reference sources, not runtime dependencies.

### Exit criteria

- enterprise architecture dossier that can be presented independently of trading;
- architecture review scorecard applied to at least one AI use case;
- at least five formal ADRs;
- catalog entries for RAG, agents, MCP, AI Gateway, model serving and evaluation;
- executive decision pack.

---

## I16 — AI Security Gateway, Responsible AI & Knowledge Lifecycle

V10 coverage: **P + Q + U + AA + AC + L**

### Goal

Add the regulated-enterprise control plane around models, RAG, tools, data and knowledge.

### Scope

- formal AI threat model;
- red-team regression scenarios: prompt injection, data exfiltration, ACL bypass, poisoning, unsafe output handling, excessive agency and supply-chain compromise;
- Enterprise AI Gateway evaluation and baseline implementation/reference;
- AuthN/AuthZ and tenant/app/user quotas;
- token budgets and rate limits;
- PII masking/redaction policy;
- output validation;
- model aliases, routing, caching and provider abstraction;
- MCP/tool policy enforcement and audit;
- multi-tenant isolation requirements;
- AI use-case registry;
- purpose, data classes, risk level and human-oversight fields;
- DPIA/PIA integration points;
- explainability/fairness considerations where applicable;
- deletion and accountability controls;
- AI-BOM: models, prompts, datasets, indexes/embeddings, tools, licenses, provenance and owners;
- corpus/chunk/embedding/index/prompt/model/API/tool version lifecycle;
- baseline/candidate/canary/rollback;
- backup/index reconstruction/restore tests;
- ADR series for RAG vs prompt-only vs fine-tuning vs deterministic workflow vs agent.

### Exit criteria

- repeatable red-team test pack;
- AI Gateway negative-policy tests;
- one AI use case registered end-to-end;
- AI-BOM generated for the demonstrator;
- one successful index rebuild/restore exercise;
- no provider-specific coupling hidden in application code.

---

## I17 — Enterprise AI Factory & Private GPU Operations

V10 coverage: **AD + AB + O**

### Goal

Expand the current OpenShift AI serving baseline into a complete AI Factory / AI infrastructure architecture with capacity and operations evidence.

### Scope

- workload classes: ingestion, embeddings, interactive inference, batch inference, evaluation, fine-tuning and optional distributed training reference;
- node-pool model: control, CPU general, GPU inference, GPU training, data and observability;
- taints/tolerations, labels/affinity, requests/limits, PriorityClass, quotas and queues/admission;
- HPA/KEDA and bounded preemption policy;
- whole GPU, MIG, time-slicing and vGPU decision matrix;
- KServe/vLLM/Triton/TGI runtime ADR where relevant;
- object storage/model registry/vector/PostgreSQL/Redis reference data plane;
- AI network architecture including ingress, east-west controls, private connectivity and GPU-interconnect reference requirements;
- storage throughput/IOPS/checkpoint requirements;
- GPU observability: utilization, VRAM, temperature, power, ECC and link metrics when available;
- inference metrics: TTFT, tokens/s, queue time, batching, cache and p95/p99;
- capacity model: model size/quantization/context/output/concurrency/VRAM/headroom/HA;
- inference optimization: model routing, caching, context compression, batching, fallback and load test;
- AI SRE runbooks for GPU unavailable/saturated, model serving unavailable, vector store unavailable, queue backlog and node loss.

### Reuse

- I9 OpenShift/GitOps foundation;
- I10 OpenShift AI/KServe/vLLM baseline;
- OpenShift platform blueprints.

### Exit criteria

- capacity calculator or deterministic sizing tool;
- at least one live or controlled runtime benchmark if hardware/environment permits;
- explicit `ESTIMATE` vs `MEASURED` status in all capacity output;
- one serving failover/recovery test;
- GPU-specific claims only when observed.

---

## I18 — Hybrid / Multi-Cloud AI Placement & Model/Vendor Strategy

V10 coverage: **S + S+ + N + E**

### Goal

Move from Azure + OpenShift portability to an explicit multi-cloud AI decision and placement architecture.

### Scope

- private/hybrid AI architecture for on-prem OpenShift and Azure/ARO;
- AWS and GCP reference landing/placement targets at architecture level;
- model/provider catalog;
- provider/model ADR matrix: quality, latency, cost, sovereignty, reversibility, supportability and operational burden;
- Model Router architecture;
- Data Policy Engine deciding eligible placement based on classification, residency, authorized providers, latency/SLA, cost and fallback rules;
- cloud/local fallback policy;
- egress control and private-endpoint principles;
- Terraform/IaC boundaries and reuse of existing Azure assets;
- no cloud deployment claim unless actual evidence exists.

### Exit criteria

- one deterministic placement policy engine or policy-as-code prototype;
- scenario tests proving restricted data cannot be routed to unauthorized providers;
- model/provider selection ADR;
- Azure/OpenShift path plus AWS/GCP reference views;
- reversibility/exit strategy documented.

---

## I19 — Event-Driven AI for Payments & Operations

V10 coverage: **T**, with reuse of **C + B + W**

### Goal

Prove that the existing Agentic AI architecture transfers from trading into a banking/payment operations scenario.

### Scope

- synthetic payment event flow;
- ISO 20022-aligned synthetic identifiers/messages where useful;
- MQ/Kafka event ingestion or replay;
- transaction/correlation/causation IDs;
- timeout/failure scenario;
- RAG over synthetic payment runbooks and architecture procedures;
- governed read-only tools for payment status, event history, logs/metrics and reconciliation status;
- agent investigation with evidence-backed root-cause hypothesis;
- recommended action with abstention/uncertainty;
- no blind replay;
- HITL before sensitive remediation;
- draft ITSM/reconciliation action, not autonomous production change;
- event contracts, idempotency, DLQ/replay and outbox references.

### Reuse

- `mayabank-ibm-mq-native-ha-openshift-eda-platform`;
- `mayabank-kafka-ddd-openshift`;
- I6/I7 governed agents and HITL;
- `mayabank-api-management-architecture`.

### Exit criteria

- one reproducible payment incident scenario;
- one evidence-backed investigation result;
- one negative scenario where the agent must abstain or escalate;
- event/API contracts versioned;
- explicit boundary between reused specialist implementation and this architecture repository.

---

## I20 — Multimodal, Document Automation & Enterprise Portfolio Graduation

V10 coverage: **D + F + H**, plus final portfolio integration.

### Goal

Close the targeted extension gaps and graduate the portfolio as an enterprise-ready architecture demonstration.

### Scope

- multimodal/IDP ingestion for PDF, tables and images;
- OCR quality scoring;
- page-level citations;
- extraction validation and human review;
- spec-driven document agent with template/contract validation and source lineage;
- Copilot Studio/Teams reference integration with DLP and approved connectors where environment access permits;
- architecture portfolio index mapping every V10 POC to `DESIGNED / IMPLEMENTED / TESTED / DEPLOYED / VERIFIED`;
- complete evidence index;
- interview/demo journeys for AI Solution Architect, AI Platform Architect, Enterprise Architect, OpenShift AI Architect and SRE/AI roles;
- final known-limitations and non-claims register.

### Exit criteria

- one multimodal document demonstrator;
- one controlled document-generation flow;
- one enterprise portfolio dashboard/index;
- no unchecked claim in the final portfolio;
- every capability either has evidence or is explicitly marked reference-only/not deployed.

---

## Target end state

After I20, the repository should be able to present one coherent architecture story:

```text
Business need / use case
  -> Enterprise Architecture / Design Authority
  -> governed data and knowledge
  -> AI Gateway / policy control
  -> RAG / ML / agents / MCP
  -> deterministic controls + HITL
  -> OpenShift AI / AI Factory
  -> hybrid and multi-cloud placement
  -> observability / SRE / security / FinOps / GreenOps
  -> evidence / value / adoption
```

Trading remains a demanding real-time proof domain, but the repository must also demonstrate at least one executable banking/payment operations transposition and one generic enterprise Knowledge Copilot path.
