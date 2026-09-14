# Enterprise AI Theoretical Design — I13 to I20

Status: **DESIGNED — THEORETICAL ARCHITECTURE COMPLETE / IMPLEMENTATION POCs DEFERRED**

This document completes the architecture-level design of I13-I20 without claiming implementation, deployment, benchmark or production evidence. The rule is deliberate: the reference architecture is completed now; executable POCs are triggered later only when a concrete business use case, mission, interview requirement or platform constraint justifies the investment.

The implementation roadmap remains in `ENTERPRISE-AI-ROADMAP-I13-I20.md`. The V10 capability gap baseline remains in `V10-GAP-MATRIX.md`.

## 1. Design principles

1. **Business-first** — no AI component is introduced without a business capability, decision, workflow or measurable operational outcome.
2. **Evidence-first** — `DESIGNED` never means `IMPLEMENTED`; implementation status requires code/tests/runtime evidence.
3. **Deterministic controls stay authoritative** — LLM/agent output cannot override security, risk, compliance, entitlement or transaction controls.
4. **RAG before fine-tuning by default** when the problem is knowledge freshness, citations, policy or document grounding.
5. **Workflow before agent** when a deterministic process is sufficient; agentic behavior is introduced only where planning/tool choice/uncertainty brings value.
6. **Human oversight for sensitive action** — high-impact remediation, payment, entitlement or configuration change requires explicit approval unless a later governance decision proves otherwise.
7. **Provider portability** — application logic must not embed irreversible provider coupling.
8. **Data policy drives placement** — classification, residency, authorized providers, latency/SLA and cost determine eligible execution locations.
9. **Observable by design** — request, retrieval, model, tool, policy and business decisions share correlation/trace context.
10. **FinOps/GreenOps by design** — token, model, cache, GPU and infrastructure choices must expose cost drivers; energy claims require measured evidence.
11. **Secure-by-default and fail-closed** — missing entitlement, policy ambiguity, stale evidence or invalid tool input stops the sensitive path.
12. **Reuse before rebuild** — OpenShift, MQ, Kafka, Azure, API Management and GreenOps specialist repositories remain evidence sources rather than duplicated codebases.

## 2. Enterprise target architecture

```text
Users / Channels / Operations / Applications
                  |
                  v
          API Gateway / IAM
                  |
                  v
              AI Gateway
    +-------------+--------------+
    | AuthN/AuthZ / quotas       |
    | PII/data policy            |
    | prompt/output controls     |
    | provider/model policy      |
    | budget/rate limit/cache    |
    +-------------+--------------+
                  |
                  v
        Orchestration / Workflow
      +-----------+-----------+
      |                       |
      v                       v
  RAG / Knowledge         Agent Runtime
      |                 +-----+------+-----+
      |                 | tools | MCP | HITL|
      |                 +-----+------+-----+
      +-----------+-----------+
                  |
                  v
           Model Router
     +------------+------------+
     |            |            |
 Local/Private   Azure       AWS/GCP
 vLLM/KServe    Models       Models
     |            |            |
     +------------+------------+
                  |
                  v
        Policy + Evidence Layer
                  |
                  v
 Evaluation / LLMOps / Observability / FinOps / SRE
                  |
                  v
 OpenShift AI / AI Factory / Hybrid Multi-Cloud Platform
```

Cross-cutting planes:

- Identity, secrets, certificates, tenant isolation and least privilege.
- Data classification, residency, retention, deletion and lineage.
- AI-BOM and provenance: models, prompts, datasets, embeddings/indexes, tools and licenses.
- Architecture governance, ADRs, standards, exceptions and technical debt.
- Metrics: quality, grounding, safety, latency, availability, throughput, cost and adoption.

---

# I13 — Enterprise Knowledge Copilot & Governed Knowledge Ingestion

Status: **DESIGNED / POC DEFERRED**

## Business objective

Provide an enterprise copilot for architects, operators and support teams that answers from governed knowledge, cites the exact sources used, abstains when evidence is insufficient and respects document-level access controls.

## Primary use cases

- Architecture standards Q&A.
- OpenShift/MQ/Java/WebSphere/Open Liberty operational assistance.
- Incident/runbook investigation.
- Payment-platform support guidance.
- Architecture-document navigation and impact analysis.

## Logical components

```text
Sources
 Git / Files / GED / SharePoint / API / DB
              |
              v
        Ingestion Adapters
              |
              v
 Raw -> Quarantine -> Curated -> Index
              |                    |
              +------ Audit -------+
                                   |
User -> /v1/chat -> Policy -> Retriever -> Reranker -> Context Builder
                                   |
                                   v
                                  LLM
                                   |
                      Citation / Abstention / Output Policy
                                   |
                                   v
                                Answer
```

## Knowledge contract

Every document/chunk must carry at minimum:

- source URI and source system;
- immutable hash/version;
- domain/application/environment;
- owner and validation status;
- language;
- security classification and ACL/entitlements;
- residency and authorized-provider constraints;
- retention/expiry/deletion state;
- usage rights/license;
- PII/sensitivity flag;
- chunk/index/embedding lineage;
- ingestion timestamp and index version.

## RAG design

Retrieval pipeline:

`Query normalization -> identity/ACL filter -> lexical/vector/hybrid retrieval -> reranking -> context budget -> generation -> citation verification -> abstention policy`.

Rules:

- retrieved content outside entitlement is excluded before model context construction;
- source/citation metadata is mandatory for grounded claims;
- absence of sufficient evidence returns `NO_ANSWER` or escalation rather than hallucination;
- synthesis, source fact and hypothesis are distinguishable;
- prompt and index version are attached to every response trace.

## API contracts

- `POST /v1/chat`
- `POST /v1/ingestion/jobs`
- `GET /v1/ingestion/jobs/{id}`
- `POST /v1/feedback`
- `GET /v1/health`
- `GET /v1/metrics`

Core response metadata: correlation ID, answer status, source references, prompt version, model alias, index version, policy decision and latency.

## NFRs

- fail-closed ACL enforcement;
- traceable citations;
- deterministic deletion lineage;
- bounded context/token budget;
- bilingual FR/EN support;
- auditable ingestion and answer paths;
- recoverable/rebuildable indexes.

## Future POC trigger

Build I13 only when a mission/use case requires **Enterprise RAG, Knowledge Copilot, operator assistant, architecture assistant, support assistant or governed document Q&A**.

Minimum POC: ingest a synthetic enterprise corpus, execute cited Q&A, prove ACL denial, no-answer behavior and deletion lineage.

---

# I14 — Enterprise AI Evaluation, Feedback, FinOps & GreenOps

Status: **DESIGNED / POC DEFERRED**

## Business objective

Make AI quality and cost measurable enough to decide whether a candidate model/prompt/index can be promoted.

## Evaluation architecture

```text
Golden Dataset
     |
     v
Baseline ----- Candidate
     |            |
     +---- Eval --+
            |
   Quality / Safety / Cost / Latency
            |
            v
      Promotion Policy
      PASS / FAIL / REVIEW
```

## Offline evaluation dimensions

- answer usefulness/correctness;
- retrieval relevance/recall;
- grounding/faithfulness;
- citation correctness;
- abstention correctness;
- ACL/security negative cases;
- prompt-injection resistance;
- FR/EN consistency;
- latency and error rate;
- token/request cost.

## Online feedback lifecycle

`User feedback -> triage -> annotation -> root-cause class -> prompt/data/model/policy correction -> regression dataset -> candidate evaluation -> controlled promotion`.

Feedback categories include wrong answer, incomplete answer, bad citation, stale source, access problem, unsafe output and UX issue.

## FinOps model

Measure or estimate separately:

- input/output tokens;
- embedding volume;
- vector-search operations;
- model/provider cost;
- cache hit ratio;
- request and useful-answer cost;
- cost per active user / assisted incident;
- GPU seconds and infrastructure allocation where applicable;
- logging/observability cost.

`cost_per_useful_answer = total_AI_service_cost / accepted_or_successful_answers`

## GreenOps rule

Energy/carbon KPIs remain `ESTIMATE` unless supported by measured energy/utilization data and a declared methodology.

## Future POC trigger

Build I14 when a mission asks for **LLMOps, GenAIOps, RAG evaluation, model comparison, cost optimization, AI observability or FinOps/GreenOps**.

Minimum POC: baseline/candidate evaluation with golden questions, CI promotion gate, feedback round-trip and cost-per-useful-answer report.

---

# I15 — Enterprise AI Architecture Pack, Design Authority & Reference Catalog

Status: **DESIGNED / POC DEFERRED**

## Business objective

Provide the deliverables expected from an Enterprise/AI Solution Architect, independently of any single runtime implementation.

## Architecture viewpoints

The dossier must include:

- Motivation/business outcomes and stakeholder map.
- Capability map and value streams.
- Application/service view.
- Data/knowledge view.
- Technology/platform view.
- Security/trust boundaries.
- Integration/API/event view.
- Deployment/hybrid-cloud view.
- Operational/SRE view.
- Transition architecture and roadmap.

## Design Authority operating model

```text
Use Case Intake
     |
     v
Architecture Assessment
     |
     +-> Pattern selection
     +-> Security/privacy review
     +-> Data/provider eligibility
     +-> NFR/SRE review
     +-> Cost/value review
     |
     v
Architecture Review Board
     |
  APPROVE / CONDITIONAL / REJECT / EXCEPTION
     |
     v
Decision + ADR + Debt/Exception Tracking
```

## Reference catalog

Approved pattern entries should cover:

- prompt-only;
- RAG;
- agentic workflow;
- deterministic workflow + LLM step;
- MCP/tool integration;
- model gateway/router;
- private model serving;
- evaluation pipeline;
- human approval;
- event-driven AI;
- multimodal/IDP.

Each catalog entry defines: context, when to use, when not to use, dependencies, security constraints, NFRs, cost drivers and evidence links.

## Adoption/value model

Track adoption, useful answers, assisted incidents, time saved, error reduction, user satisfaction, cost and risk reduction rather than model usage alone.

## Future POC trigger

Build I15 deliverables when targeting **Enterprise Architect, AI Solution Architect, Design Authority, Architecture Governance or COMEX/decision-pack missions**.

Minimum demonstrator: one full architecture dossier, scorecard, five ADRs, pattern catalog and executive decision memo applied to a selected use case.

---

# I16 — AI Security Gateway, Responsible AI & Knowledge Lifecycle

Status: **DESIGNED / POC DEFERRED**

## Business objective

Create a policy-control plane between enterprise consumers and AI capabilities.

## AI Gateway control chain

```text
Request
  -> IAM / Tenant / Application identity
  -> Authorization / Entitlement
  -> Data classification / residency policy
  -> PII/secrets inspection
  -> Prompt policy
  -> Rate/token/budget control
  -> Model/provider allowlist
  -> Cache policy
  -> Model Router
  -> Output validation / DLP
  -> Audit / telemetry
  -> Response
```

## Threat model

Minimum threats:

- direct/indirect prompt injection;
- sensitive-data disclosure/exfiltration;
- ACL bypass;
- poisoned documents/embeddings;
- malicious tool arguments;
- excessive agency;
- insecure output handling;
- model/provider supply-chain risk;
- secrets leakage;
- tenant crossover;
- denial-of-wallet/token abuse;
- unsafe autonomous remediation.

## Responsible AI lifecycle

Every AI use case must register:

- business purpose and owner;
- affected users;
- data classes;
- model/provider;
- risk level;
- human oversight;
- expected limitations;
- privacy/DPIA hooks;
- explainability/fairness applicability;
- monitoring and incident owner;
- retirement/deletion responsibilities.

## AI-BOM

The bill of materials records:

`Application -> model/version -> prompt/version -> dataset/corpus -> embedding model -> index -> tools/MCP servers -> libraries/images -> licenses -> owner -> provenance`.

## Lifecycle and rollback

All deployable AI artifacts support baseline/candidate/canary/rollback where applicable. Knowledge stores must be reconstructable from governed source plus versioned processing configuration.

## Pattern-selection ADR rule

Default decision path:

`deterministic software -> prompt-only -> RAG -> workflow -> agent -> fine-tuning`

Move right only when the simpler option cannot meet the requirement.

## Future POC trigger

Build I16 when a mission requires **AI security, AI Gateway, guardrails, Responsible AI, governance, privacy, regulated AI or model-provider control**.

Minimum POC: gateway policy enforcement, negative tests, AI-BOM generation, use-case registry entry and corpus/index rebuild exercise.

---

# I17 — Enterprise AI Factory & Private GPU Operations

Status: **DESIGNED / POC DEFERRED**

## Business objective

Provide a production-oriented AI platform blueprint on OpenShift/OpenShift AI with explicit workload isolation, model serving, capacity and SRE controls.

## Platform topology

```text
OpenShift / OpenShift AI
|
+-- Control / platform services
+-- CPU general-purpose pool
+-- GPU inference pool
+-- GPU training/fine-tuning pool
+-- Data services
+-- Observability/SRE services
|
+-- Object storage
+-- Model registry
+-- Vector store
+-- PostgreSQL/metadata
+-- Cache
+-- KServe / vLLM / selected runtimes
```

## Workload classes

- document ingestion;
- embeddings;
- interactive inference;
- batch inference;
- evaluation;
- fine-tuning/LoRA;
- optional distributed training.

Each class defines priority, resource requests/limits, queue/admission policy, data locality, maximum concurrency and SLO.

## Scheduling strategy

Use node labels/affinity, taints/tolerations, PriorityClass, quotas, admission/queues and controlled autoscaling. GPU sharing is a decision, not a default.

GPU modes to evaluate:

- dedicated whole GPU;
- MIG where hardware/workload supports partitioning;
- time-slicing for suitable non-isolated workloads;
- vGPU only where platform/licensing/security constraints justify it.

## Runtime-selection ADR

Compare KServe, vLLM, Triton and TGI against model support, batching, streaming, autoscaling, GPU efficiency, observability, operational burden and OpenShift integration.

## Capacity model

Conceptual sizing inputs:

- model parameter count and precision/quantization;
- model weights memory;
- KV cache requirement;
- context and output length;
- concurrent sequences;
- runtime overhead;
- target TTFT and tokens/s;
- headroom and HA replica count.

Every result is labelled `ESTIMATE` until benchmarked.

## AI SRE

SLO/alert/runbook categories:

- model unavailable;
- GPU unavailable/saturated;
- VRAM exhaustion;
- queue backlog;
- latency p95/p99 breach;
- vector store unavailable;
- model load failure;
- node loss;
- cache failure;
- provider fallback activated.

## Future POC trigger

Build I17 when a mission requires **OpenShift AI/RHOAI, AI Platform, private LLM, KServe, vLLM, GPU platform, MLOps infrastructure or AI SRE**.

Minimum POC: one private model/embedding or small inference service on available infrastructure, resource policies, measured latency/throughput, failure/recovery test and capacity report.

---

# I18 — Hybrid / Multi-Cloud AI Placement & Model/Vendor Strategy

Status: **DESIGNED / POC DEFERRED**

## Business objective

Decide where data and AI workloads may execute without coupling the application to a single model provider or cloud.

## Placement architecture

```text
Request + Data Classification + SLA + Budget
                     |
                     v
              Data Policy Engine
                     |
       +-------------+-------------+
       |             |             |
   Private/OCP     Azure         AWS/GCP
       |             |             |
       +-------------+-------------+
                     |
                Model Router
                     |
             Selected endpoint
```

## Policy dimensions

- data classification;
- geographic residency;
- provider authorization;
- private/public model eligibility;
- latency/SLA;
- availability;
- quality tier;
- cost/token budget;
- context-window requirement;
- tool/function support;
- reversibility/exit constraints.

Example policy:

```text
SECRET/regulated      -> private/explicit approved endpoint only
CONFIDENTIAL          -> approved region/provider with private controls
INTERNAL              -> private or approved cloud
PUBLIC                -> optimize quality/cost/latency
```

## Model/provider decision matrix

For each candidate: functional quality, benchmark evidence, latency, cost, context, multimodality, tool calling, data-use policy, sovereignty, enterprise support, portability and operational burden.

## Fallback strategy

Fallback is policy-governed. A failure cannot silently route restricted data to a disallowed provider.

## Exit/reversibility strategy

Use model aliases, provider-neutral application contracts, portable prompt/evaluation assets, externalized knowledge, open telemetry and exportable audit data.

## Future POC trigger

Build I18 when a mission requires **hybrid AI, multi-cloud AI, model routing, Azure/AWS/GCP choice, sovereignty or provider-selection architecture**.

Minimum POC: policy-as-code routing with at least private + one cloud target, negative restricted-data test and provider failover that preserves policy.

---

# I19 — Event-Driven AI for Payments & Operations

Status: **DESIGNED / POC DEFERRED**

## Business objective

Prove that the architecture is transferable from the trading demonstration to a banking/payment operational scenario.

## Reference use case

Synthetic payment incident investigation:

```text
Payment Event
   |
 MQ / Kafka
   |
 Event History / Status / Metrics
   |                |
   +------ Agent Investigation ------+
                  |                  |
                  v                  v
              RAG Runbooks      Read-only Tools
                  |                  |
                  +--------+---------+
                           v
                 Evidence-backed hypothesis
                           |
                     Deterministic policy
                           |
                     Human review/HITL
                           |
               Draft remediation / ITSM action
```

## Design constraints

- ISO 20022-aligned synthetic messages/IDs where useful;
- correlation/causation IDs end-to-end;
- idempotency for events/commands;
- DLQ/replay/outbox patterns;
- read-only investigation tools by default;
- no blind replay of payment messages;
- no autonomous production remediation;
- uncertainty and abstention represented explicitly;
- evidence links to events/logs/runbooks included in findings.

## Agent roles

Potential roles: incident investigator, payment-flow analyst, runbook/knowledge agent and reconciliation assistant. Sensitive action remains outside the agent unless a governed HITL workflow authorizes it.

## Future POC trigger

Build I19 when a mission requires **banking/payments, IBM MQ, Kafka/EDA, incident automation, operations copilot or AI applied to transaction platforms**.

Minimum POC: replay one synthetic payment failure, investigate via MQ/Kafka evidence + RAG, generate a cited diagnosis and remediation draft, and prove an abstention/escalation case.

---

# I20 — Multimodal, Document Automation & Portfolio Graduation

Status: **DESIGNED / POC DEFERRED**

## Business objective

Extend governed knowledge workflows to complex enterprise documents and provide a final architecture portfolio that can be demonstrated by role.

## Multimodal/IDP flow

```text
PDF / Image / Table
        |
        v
OCR / Layout / Table extraction
        |
        v
Quality scoring + validation
        |
 Raw -> Curated structured representation
        |
 Chunk / Embed / Index
        |
 Retrieval with page/region citation
        |
 Human validation where confidence is low
```

## Document automation

A document agent must be spec-driven:

`template/contract -> required sources -> extraction -> draft -> validation -> citation/lineage -> human approval -> publish/export`.

It must not silently fabricate missing mandatory fields.

## Copilot/enterprise channel integration

Teams/Copilot Studio is treated as a channel/integration option, subject to DLP, connector allowlists, tenant policy and identity propagation. It does not replace the core governed AI architecture.

## Portfolio graduation model

Every capability is mapped to one of:

`DESIGNED -> IMPLEMENTED -> TESTED -> DEPLOYED -> VERIFIED`

with links to evidence and explicit non-claims.

Interview journeys should exist for:

- AI Solution Architect;
- Enterprise AI Architect;
- AI Platform/OpenShift AI Architect;
- Agentic AI/RAG Architect;
- AI Security/Governance Architect;
- Banking/Payments AI Architect.

## Future POC trigger

Build I20 when a mission requires **multimodal RAG, IDP/OCR, document automation, Copilot/Teams integration or portfolio/demo graduation**.

Minimum POC: PDF/table/image ingestion with page-level citations plus one controlled document-generation flow with mandatory human validation.

---

# 3. Future POC activation matrix

POCs are not executed sequentially merely because their iteration number exists. Select the smallest POC that proves the capability needed by a target mission or business use case.

| Market / business demand | POC to activate first | Secondary POC |
|---|---|---|
| Enterprise RAG / Knowledge Copilot | I13 | I14, I16 |
| LLMOps / evaluation / cost | I14 | I13, I16 |
| Enterprise AI Architect / Design Authority | I15 | I16, I18 |
| AI Security / Governance / AI Gateway | I16 | I14, I18 |
| OpenShift AI / RHOAI / private LLM / GPU | I17 | I14, I16 |
| Hybrid / Multi-cloud AI / model strategy | I18 | I16, I17 |
| Banking / payments / IBM MQ / Kafka + AI | I19 | I13, I16 |
| Multimodal / OCR / document automation | I20 | I13, I14 |
| Agentic AI mission | Reuse I6-I7 first | I16 if governance is required |
| Azure AI architecture | Reuse I11 + Azure specialist repo | I18 if multi-provider/hybrid is required |

# 4. Implementation priority rule

For each new mission or business request:

```text
1. Extract required capabilities from the job/use case.
2. Map them to existing evidence I0-I12 and designed capabilities I13-I20.
3. Reuse existing runtime/evidence wherever possible.
4. Select ONE missing high-value capability.
5. Build the smallest demonstrable POC for that capability.
6. Test and capture evidence.
7. Upgrade only that capability from DESIGNED to IMPLEMENTED/TESTED.
8. Stop; do not open unrelated POCs.
```

This prevents the portfolio from becoming a collection of unfinished labs and keeps implementation aligned with market demand.

# 5. Theoretical design completion matrix

| Iteration | Architecture status | Runtime status | Deferred proof |
|---|---|---|---|
| I13 | **DESIGNED** | NOT IMPLEMENTED | governed Knowledge Copilot + ingestion |
| I14 | **DESIGNED** | NOT IMPLEMENTED | evaluation/feedback/cost loop |
| I15 | **DESIGNED** | NOT IMPLEMENTED | architecture dossier/Design Authority demonstrator |
| I16 | **DESIGNED** | NOT IMPLEMENTED | AI Gateway/security/governance controls |
| I17 | **DESIGNED** | NOT IMPLEMENTED | AI Factory/GPU/private serving benchmark |
| I18 | **DESIGNED** | NOT IMPLEMENTED | policy-based multi-cloud/model routing |
| I19 | **DESIGNED** | NOT IMPLEMENTED | payment-operations AI incident scenario |
| I20 | **DESIGNED** | NOT IMPLEMENTED | multimodal/document automation demonstrator |

## Non-claim

The architecture described here is a design baseline. It does not claim live cloud deployment, GPU benchmark, production model routing, enterprise identity federation, regulated-production approval, real customer data, production payment remediation or production Copilot integration. Those claims require future implementation and evidence.