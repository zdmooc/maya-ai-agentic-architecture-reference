# AI Repository Portfolio Map

Status: **CURRENT CLASSIFICATION — 2026-09-15**

Purpose: classify the repositories owned by `zdmooc` that directly implement, design or materially support AI/ML/GenAI architecture. This map prevents portfolio duplication and clarifies which repositories should be shown first for AI Solution Architect missions.

## 1. Tier S — Primary AI portfolio

### `maya-ai-agentic-architecture-reference`

Role: **canonical AI architecture / knowledge / governance hub**.

Scope:
- Enterprise AI architecture;
- Agentic AI, RAG, MCP, HITL;
- AI Gateway / Model Router;
- Responsible AI, risk, governance, ADR/NFR/SAD;
- OpenShift AI / KServe / vLLM;
- hybrid multi-cloud;
- LLMOps/SRE/FinOps/GreenOps;
- banking/insurance transposition.

Portfolio decision: **KEEP AS THE SINGLE AI ARCHITECTURE REFERENCE HUB**.

Do not create another generic AI architecture repository.

### `TradeOps-GenAI-Integration`

Role: **primary executable GenAI / Agentic AI runtime evidence**.

Scope:
- RAG + Qdrant;
- LangGraph / specialized agents;
- governed MCP boundary;
- deterministic Risk Gate + HITL;
- workflow and audit;
- Kafka-compatible event backbone;
- OpenShift/CRC;
- RHOAI/KServe target;
- observability;
- React business cockpit;
- shadow/paper execution only.

Portfolio decision: **KEEP AS THE MAIN EXECUTABLE AI DEMONSTRATOR**.

Use it as runtime proof for architecture claims made in `maya-ai-agentic-architecture-reference`.

---

## 2. Tier A — Strong specialist AI repositories

### `mayabank-ibm-odm-ai-decision-architecture`

Role: **Decision Intelligence / governed AI for insurance**.

AI scope:
- ML scoring;
- GenAI document extraction;
- governed MCP / agents;
- deterministic IBM ODM policy boundary;
- HITL;
- event-driven decisioning;
- audit and OpenShift validation.

Portfolio value: **VERY HIGH** for regulated AI, insurance, decision management and explainable enterprise AI.

Decision: **KEEP / PRIORITIZE FOR BANK-INSURANCE AI INTERVIEWS**.

### `mayabank-azure-cloud-ai-platform`

Role: **Azure Solution Architecture + AI Platform**.

AI scope:
- Microsoft Foundry / AI Search / models;
- AI Landing Zone concepts;
- RAG lab target;
- AKS/ARO/hybrid migration;
- identity/network/security/observability/FinOps around AI workloads.

Portfolio value: **HIGH** for Azure AI Solution Architect / hybrid cloud roles.

Decision: **KEEP**. It is the Azure-specific companion to the vendor-neutral AI reference.

### `mayabank-carbon-aware-decision-architecture`

Role: **AI/ML + GreenOps + decision optimization**.

AI scope:
- forecast CPU/power/consumption;
- anomaly detection/ranking;
- confidence gating;
- deterministic decision engine;
- Pareto multi-criteria optimization;
- human approval;
- Recommendation API/event-driven integration.

Portfolio value: **HIGH AND DIFFERENTIATING** because it links AI with Green IT and infrastructure decisions.

Decision: **KEEP** as a specialist proof for Green AI / GreenOps / sustainable architecture.

### `mayabank-pega-ai-case-management-openshift`

Role: **CRM/Case Management + governed AI + OpenShift**.

AI scope:
- Pega Decisioning / CDH concepts;
- case summarization;
- RAG over procedures;
- recommended next investigation step;
- HITL;
- provenance/guardrails;
- AI as recommendation layer, not system of record.

Portfolio value: **HIGH for Pega/CRM/case-management roles**, secondary for generic AI Architect roles.

Decision: **KEEP AS DOMAIN SPECIALIST**, not as a central AI platform repository.

---

## 3. Tier B — AI platform / data architecture with broader scope

### `MayaBank-V2`

Role: **OpenShift / banking platform architecture with a substantial Data/AI pillar**.

AI scope:
- data pipelines;
- vector database patterns;
- ML serving;
- RAG/retrieval patterns;
- analytics workers;
- AI governance, capacity and FinOps implications.

Primary identity remains OpenShift/platform architecture, not pure AI.

Decision: **KEEP AS CROSS-DOMAIN PLATFORM REFERENCE**. Reuse Data/AI platform patterns; do not position it ahead of the Tier S repositories for an AI mission.

### `maya-interlink-enterprise-ai-platform`

Role: **future enterprise AI platform implementation**.

Target scope:
- Enterprise Architecture;
- hybrid multi-cloud;
- OpenShift/OpenShift AI;
- GitOps;
- AI Platform;
- RAG/Agents/MCP;
- LLMOps/SRE/FinOps/GreenOps;
- payment investigation demonstrator.

Current state: **QUEUED / NOT STARTED**.

Decision: **FREEZE FOR NOW**. Its target overlaps strongly with the now-mature `maya-ai-agentic-architecture-reference`. Start implementation only when a distinct platform-runtime capability is required and cannot be represented in the existing reference + specialist repos.

---

## 4. Tier C — Intelligence / automation adjacent to AI

### `maya-freelance-mission-intelligence`

Role: **market intelligence / portfolio intelligence / controlled automation**.

Current strengths:
- acquisition and normalization;
- deterministic mission scoring;
- CV/portfolio matching;
- PostgreSQL memory;
- n8n workflows;
- controlled CRM actions;
- human approval;
- runtime evidence on CRC.

It is a strong intelligent automation system, but its current README does not make LLM/RAG/agentic AI the architectural core.

Decision: **KEEP**, but present it as **decision-support / automation / personal intelligence**, not as one of the primary GenAI architecture demonstrations unless a future AI layer is explicitly added and evidenced.

### `Maya`

Role: **product/company/AI/trading umbrella context**.

Decision: **REFERENCE ONLY**. Do not turn it into another executable AI runtime.

---

## 5. AI-enabling repositories — important but not AI repositories

These repositories should be referenced by AI solutions, but not marketed individually as AI projects.

| Repository | AI-enabling capability | Classification |
|---|---|---|
| `mayabank-kafka-ddd-openshift` | DDD, event-driven architecture, Kafka, replay, event contracts | AI integration foundation |
| `mayabank-ibm-mq-native-ha-openshift-eda-platform` | IBM MQ / EDA / payment messaging / HA | AI event & legacy integration foundation |
| `mayabank-api-management-architecture` | APIs, OAuth/OIDC, gateway, quotas, resilience | AI Gateway/API foundation |
| `Maya-gitops` | deployment/GitOps patterns | AI platform delivery support |
| `openshift2026-openshift-local-trading-gateway` | CRC/OpenShift deployment patterns | AI runtime platform support |
| `openshift-platform-blueprints` | OpenShift platform engineering | AI platform support |
| `payment-hub-iso20022-opf-reference` | payments/ISO 20022 domain | AI business-domain source |
| `wero-organisme-poc` | Wero/payment investigation domain | AI business-domain source |
| `cadrage_202682030` | program/portfolio coordination | portfolio governance, not AI runtime |

These are **supporting evidence sources** for an AI architecture, not competing AI repositories.

---

## 6. Recommended AI portfolio hierarchy

For a generic **AI Solution Architect / Enterprise AI Architect** interview or CV, show repositories in this order:

1. `maya-ai-agentic-architecture-reference` — architecture, methods, governance and complete knowledge base.
2. `TradeOps-GenAI-Integration` — executable RAG/Agents/MCP/HITL/OpenShift evidence.
3. `mayabank-ibm-odm-ai-decision-architecture` — regulated enterprise decision intelligence.
4. `mayabank-azure-cloud-ai-platform` — Azure AI / hybrid-cloud architecture.
5. `mayabank-carbon-aware-decision-architecture` — Green AI / decision optimization differentiator.
6. `mayabank-pega-ai-case-management-openshift` — CRM/case-management AI specialization.
7. `MayaBank-V2` — broad OpenShift/Data/AI platform reference.
8. `maya-freelance-mission-intelligence` — intelligent automation / decision support.
9. `maya-interlink-enterprise-ai-platform` — future platform, not yet runtime evidence.

## 7. Portfolio rule

The AI portfolio should have **one hub, one principal executable runtime, and specialist domain/platform repositories**.

Target model:

```text
maya-ai-agentic-architecture-reference
  -> architecture / knowledge / governance / portfolio index

TradeOps-GenAI-Integration
  -> principal executable GenAI/Agentic runtime evidence

Specialists
  -> ODM/AI Decision
  -> Azure AI Platform
  -> Carbon-Aware AI
  -> Pega AI Case Management
  -> Data/AI Platform

Enablers
  -> Kafka / MQ / API Management / GitOps / OpenShift / Payments
```

Do not build additional generic AI repositories unless a concrete mission exposes a capability that is genuinely absent from this model.
