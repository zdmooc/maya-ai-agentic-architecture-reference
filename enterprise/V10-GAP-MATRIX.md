# Enterprise AI Portfolio V10 — Gap Matrix

Status: **BASELINE GAP ANALYSIS — NOT AN IMPLEMENTATION CLAIM**

This document maps the current `maya-ai-agentic-architecture-reference` program against the Enterprise AI Portfolio V10 baseline dated 2026-09-14.

The purpose is to extend the existing, evidence-driven Agentic AI program into a broader **Enterprise AI Architecture / AI Platform / Hybrid Multi-Cloud reference portfolio** without duplicating capabilities that are already implemented and tested.

## Status vocabulary

- **STRONG** — substantial capability already exists with implementation/test evidence in the current program or its explicitly reused runtime.
- **PARTIAL** — useful design or implementation exists, but the V10 capability is incomplete.
- **GAP** — capability is not yet represented as a first-class, evidence-backed program capability.
- **REUSE** — the capability should reuse a specialist repository rather than be reimplemented from zero.

Nothing in this matrix upgrades a capability to `IMPLEMENTED`, `TESTED`, `DEPLOYED`, or `VERIFIED` without evidence.

## Executive conclusion

The current repository is already strong in:

- governed Agentic AI and Human-in-the-Loop;
- RAG used inside a decision workflow;
- MCP-shaped governed tool boundaries;
- ML/MLOps experimentation, registry and drift mechanics;
- end-to-end observability and LLMOps;
- OpenShift/GitOps packaging;
- OpenShift AI / KServe / model-serving contracts;
- Azure/ARO target architecture.

The major V10 gaps are not "more agents". They are:

1. Enterprise Knowledge Copilot as a generic employee/operator product;
2. governed enterprise knowledge ingestion and lifecycle;
3. Enterprise AI Gateway / policy enforcement / multi-provider routing;
4. Enterprise Architecture governance, Design Authority and reference catalog;
5. Responsible AI / privacy / compliance lifecycle;
6. AI Factory infrastructure depth and GPU operations;
7. true multi-cloud placement and policy-based routing;
8. executable payment/operations transposition;
9. multimodal / IDP / OCR;
10. adoption, value measurement and COMEX decision material.

## POC-by-POC mapping

| V10 POC | Capability | Current status | Current evidence / reusable baseline | Gap to close |
|---|---|---:|---|---|
| A | Enterprise Knowledge Copilot | GAP | I6 provides governed RAG inside an agentic trading workflow | Build a generic operator/architect copilot with citations, abstention, feedback, source/version visibility, bilingual tests and role-oriented UX |
| I | Data Engineering & Knowledge Ingestion | GAP | Data-quality patterns exist for market/event data | Add enterprise document ingestion: sources, Raw/Quarantine/Curated/Index/Audit zones, document data contracts, ACL/classification, retention and deletion lineage |
| J | API Engineering & GenAIOps | PARTIAL | FastAPI-style APIs, contracts, security, observability and CI already exist in the reused runtime | Add generic AI APIs `/v1/chat`, `/v1/ingestion/jobs`, `/v1/feedback`; version API/model/prompt/index; formal GenAIOps API governance |
| G | FinOps, Observability & GreenOps AI | PARTIAL | I8 tracks latency/token/cost metadata; I11 has Azure cost-control discipline | Add showback, budget/forecast, cost per useful answer/user/incident, cache efficiency, GPU-second/token metrics and energy-oriented KPIs |
| M | Evaluation Pipeline & Feedback Loop | PARTIAL | I5 has ML evaluation; I6-I8 have agent/security regression mechanics | Add RAG golden datasets, grounding/citation/ACL/no-answer tests, online feedback, triage/annotation and CI promotion gates for knowledge workflows |
| K | AI Framing & COMEX Decision Pack | GAP | Architecture Vision exists | Add business value, risk, cost, options, roadmap, decision memo and executive scorecard |
| V | Enterprise AI Architecture Pack | PARTIAL | `ARCHITECTURE-VISION.md`, `TARGET-ARCHITECTURE.md`, agentic/ML architecture docs exist | Add TOGAF/ArchiMate views, complete NFR catalog, enterprise data/application/technology/deployment views, risk register and decision dossier |
| W | AI Integration Blueprint | PARTIAL | Kafka-compatible event backbone and enterprise transposition exist | Add formal API Gateway + AI Gateway + domain API/event integration blueprint with OpenAPI/AsyncAPI, IBM MQ, Kafka, outbox, DLQ/replay and DDD integration patterns |
| X | AI Architecture Governance & Design Authority | GAP | Architecture Review Board is a stakeholder concept | Add review workflow, scorecards, standards, exceptions, technical debt register, decision logs and go/no-go criteria |
| Y | AI Platform Reference Catalog | PARTIAL | `reuse/` provides repository and source reuse catalogs | Add first-class catalog of approved AI patterns/components, templates, contracts, policies, prompts/tools and anti-patterns |
| Z | AI Product Adoption & Value Measurement | GAP | No enterprise adoption workstream | Add adoption KPIs, onboarding, champions, satisfaction, value hypotheses, feedback-to-backlog loop |
| P | AI Security & Red Teaming | PARTIAL/STRONG | I6 tool-policy negative tests; I8 security gates, OIDC-compatible identity, prompt-injection regression and SBOM | Expand formal threat model to poisoning, exfiltration, ACL bypass, excessive agency, output handling, supply chain and repeatable red-team scenarios |
| Q | AI Gateway & Policy Enforcement | GAP | Model/provider abstraction exists only as architecture intent | Implement/evaluate an AI Gateway with AuthN/AuthZ, tenant/app/user quotas, token budgets, PII controls, routing, caching, model aliases, audit and provider abstraction |
| R | AI SRE, Resilience & Chaos Testing | PARTIAL | Resilience principles, SLO/alerts and OpenShift deployment contracts exist | Add executable chaos/failure tests, fallback drills, canary/rollback, restoration and platform/AI runbooks with evidence |
| AA | Responsible AI, Privacy & Compliance by Design | GAP | Human approval and deterministic safety principles exist | Add use-case registry, purpose/data classification, risk level, human oversight, DPIA/PIA hooks, explainability/fairness considerations, deletion and accountability |
| AC | Knowledge Lifecycle, Release & DR | GAP | Prompt/model/version evidence exists in several iterations | Add versioned corpus/chunk/embedding/index lifecycle, baseline/candidate/canary/rollback, backups, index reconstruction and restore tests |
| AD | Enterprise AI Infrastructure & AI Factory | PARTIAL | I9 OpenShift/GitOps; I10 RHOAI/KServe/vLLM contracts | Expand to CPU/GPU pools, workload classes, queues/admission, training/fine-tuning paths, object storage, vector/data services, network/storage architecture, operational capacity and runbooks |
| D | Spec-driven Document Agent | GAP | Agent orchestration patterns exist | Add controlled document-generation workflow with templates/spec contracts, source lineage and mandatory human review |
| F | Secure Copilot Studio | GAP | No Copilot Studio implementation | Add Teams/Copilot Studio reference path, DLP and approved-connector governance without making it the primary runtime |
| E | Azure PaaS, Terraform & Azure DevOps | PARTIAL/REUSE | I11 Terraform/ARO; `mayabank-azure-cloud-ai-platform` is an explicit reuse source | Reuse Azure patterns; add only AI-specific Azure PaaS and delivery integration where not already covered |
| L | ADR — AI Pattern Selection | PARTIAL | Architectural trade-offs are documented but not as a complete ADR decision series | Add explicit ADRs for RAG vs prompt-only vs fine-tuning vs workflow vs agent |
| N | ADR — Model / Vendor Selection | GAP | Azure/OpenShift portability principle exists | Add model/provider decision matrix for quality, cost, latency, sovereignty, reversibility and operability |
| O | Inference Optimisation Lab | PARTIAL | I10 serving and capacity estimator exist | Add routing, cache, context compression, batching, load tests, fallback and measured cold/warm latency/throughput evidence |
| U | AI Governance, AI-BOM & Compliance | PARTIAL | SPDX SBOM exists in I8 | Extend to AI-BOM covering models, prompts, datasets, embeddings/indexes, tools, licenses, provenance and ownership |
| S | Hybrid Private AI Platform on OpenShift/Azure | PARTIAL | I9-I11 cover OpenShift, RHOAI and ARO target architecture | Formalize a generic private/hybrid AI platform with model-locality, egress, mTLS, private data placement and cloud/local fallback |
| S+ | Multi-Cloud Hybrid AI Decision Platform | GAP | Azure + OpenShift only; portability intent is documented | Add AWS/GCP reference targets, Model Router, policy-based placement and a Data Policy Engine based on classification/residency/cost/latency/SLA |
| T | Event-Driven AI for Payments & Operations | PARTIAL/REUSE | `TRADING-TO-ENTERPRISE.md` defines payment transposition | Build executable payment/operations scenario using MQ/Kafka evidence, RAG investigation, ticket draft/reconciliation guidance and HITL; reuse the MQ/Kafka repositories |
| C | Governed Agentic System with MCP | STRONG | I6 + I7 | Keep and harden; do not rebuild from zero |
| B | End-to-end MLOps | STRONG | I5 + I10 serving contracts | Keep; add only production/live evidence and rollback/explainability gaps |
| H | Multimodal RAG / IDP | GAP | No first-class multimodal pipeline | Add OCR, tables/images, extraction quality scoring and page-level citations |
| AB | Private AI Capacity & GPU Operations | PARTIAL | I10 capacity estimator and vLLM GPU reference | Add MIG/time-slicing/vGPU decision patterns, multi-tenancy, quotas, VRAM sizing, saturation, power/temp/ECC metrics, HA/DR and energy/cost evidence |

## Specialist repositories to reuse

The reference repository remains the architecture/program source of truth. Specialist repositories provide implementation patterns or evidence and should not be copied wholesale.

- `zdmooc/TradeOps-GenAI-Integration` — executable agentic/trading runtime and test evidence.
- `zdmooc/mayabank-azure-cloud-ai-platform` — Azure landing zone, identity, network, APIM, data, observability, HA/DR, FinOps/GreenOps and AI patterns.
- `zdmooc/openshift-platform-blueprints` — OpenShift platform, GitOps, security and observability patterns.
- `zdmooc/mayabank-kafka-ddd-openshift` — DDD/event-driven/Kafka payments patterns.
- `zdmooc/mayabank-ibm-mq-native-ha-openshift-eda-platform` — IBM MQ/OpenShift payment messaging and resilience evidence.
- `zdmooc/mayabank-api-management-architecture` — API lifecycle, security and integration architecture patterns.
- `zdmooc/mayabank-carbon-aware-decision-architecture` — FinOps/GreenOps/carbon-aware decision patterns.
- `zdmooc/mayabank-ibm-odm-ai-decision-architecture` — deterministic decision + ML/GenAI/MCP/HITL patterns.

## Priority order

The V10 gaps should be closed in this order:

1. **A + I + J** — Enterprise Knowledge Copilot and governed knowledge platform.
2. **M + G** — evaluation, feedback, FinOps/GreenOps.
3. **K + V + W + X + Y + Z** — enterprise architecture and Design Authority.
4. **P + Q + U + AA + AC + L** — security, gateway, governance and lifecycle.
5. **AD + AB + O** — AI Factory and GPU operations.
6. **S + S+ + N + E** — hybrid/multi-cloud placement and provider strategy.
7. **T** — event-driven AI for payments/operations using reusable MQ/Kafka evidence.
8. **D + F + H** — targeted document, Copilot Studio and multimodal extensions.

See `enterprise/ENTERPRISE-AI-ROADMAP-I13-I20.md` for the versioned execution plan.
