# AI Control Plane vs Runtime Plane

Status: **DESIGNED — ARCHITECTURE REFERENCE / NO RUNTIME CLAIM**

Purpose: define a clear separation between enterprise AI governance/control capabilities and runtime execution capabilities. The objective is to prevent application teams from embedding governance, provider coupling or high-impact policy decisions inside individual AI applications.

## 1. Architecture principle

```text
Business / Applications / Channels
              |
              v
        AI CONTROL PLANE
  identity / policy / catalog
  AI Gateway / routing policy
  model aliases / provider policy
  evaluation / promotion gates
  cost / quota / budget controls
  audit / provenance / observability
              |
              v
        AI RUNTIME PLANE
  model serving / inference
  RAG / retrieval
  agents / workflows
  MCP / governed tools
  application adapters
  data connectors
              |
              v
   Deterministic Systems of Record
       + Human Approval where needed
```

The control plane governs **what is allowed, which provider/model is eligible, which controls apply and how evidence is collected**. The runtime plane performs **inference, retrieval, orchestration and tool execution** within those constraints.

## 2. AI Control Plane responsibilities

- identity, authentication and authorization integration;
- tenant/application/service registration;
- model catalog and model aliases;
- provider eligibility and data-classification rules;
- AI Gateway policy and routing policy;
- quotas, rate limits and budget limits;
- prompt/policy/version metadata;
- evaluation baselines and promotion gates;
- security/Responsible AI controls;
- provenance and AI-BOM metadata;
- audit and evidence retention;
- cost and usage accounting;
- architecture fitness functions;
- policy-as-code enforcement;
- operational dashboards and SLO governance.

The control plane is not a business System of Record and must not silently modify business truth.

## 3. AI Runtime Plane responsibilities

- model serving through KServe/vLLM or approved managed providers;
- RAG ingestion/retrieval/generation paths;
- vector/index/cache runtime access;
- agent/workflow state execution;
- MCP/tool invocation;
- application-specific context assembly;
- deterministic validation and guardrails at execution time;
- human-review workflow integration;
- telemetry emission;
- provider/model fallback according to control-plane policy.

Runtime components must consume policy rather than invent policy locally.

## 4. Centralized vs distributed decisions

Centralize when the concern is enterprise-wide:

- identity and provider eligibility;
- data classification/residency constraints;
- global model aliases;
- security baselines;
- budget controls;
- audit/provenance schema;
- evaluation/promotion gates.

Keep close to the workload when the concern is application-specific:

- retrieval strategy and domain corpus;
- agent state machine;
- business tool contracts;
- latency-sensitive caching;
- business fallback;
- human-review workflow.

## 5. Failure boundary

If the control plane becomes unavailable, sensitive runtime actions must fail safely. Previously authorized configuration may be cached only when its validity window and revocation model are explicit.

If the runtime plane fails, the control plane must preserve evidence and expose the failure state without fabricating a successful AI outcome.

## 6. Repository mapping

- AI Gateway / routing: `AI-GATEWAY-IMPLEMENTATION-OPTIONS.md` and I18.
- Enterprise RAG: I13.
- Evaluation / promotion: I14.
- Security / policy / Responsible AI: I16.
- OpenShift AI / KServe / vLLM: I17.
- Hybrid placement / provider strategy: I18.
- Payments AI: I19.
- Fitness functions: `AI-ARCHITECTURE-FITNESS-FUNCTIONS.md`.
- Executable agent/RAG evidence: `zdmooc/TradeOps-GenAI-Integration`.

## 7. Status discipline

This document defines the logical separation only.

`DESIGNED` does not imply that a centralized enterprise control plane has been implemented or deployed.