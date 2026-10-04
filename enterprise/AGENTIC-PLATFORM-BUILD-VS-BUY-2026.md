# Agentic Platform Build vs Buy / Hybrid — 2026

Status: **DESIGNED — D-092 M4 / DECISION FRAMEWORK**

**Assessment date: 2026-10-04**

Purpose: provide a current, vendor-neutral framework for deciding whether an enterprise should build, buy or combine agentic platform capabilities.

This is not a permanent product ranking. Vendor capabilities evolve quickly; every client decision must refresh primary-source evidence.

## 1. Decision principle

Do not ask:

> Which agent platform is best?

Ask:

> Which capabilities must we own, which can we consume as managed services, and which constraints force portability or private operation?

Possible outcomes:

1. **Internal/OpenShift-heavy**
2. **Managed-cloud-heavy**
3. **Code-first + managed primitives**
4. **Hybrid**

## 2. Capability dimensions

Compare:

- agent runtime/hosting;
- registry/catalog/lifecycle;
- agent identity/delegation;
- MCP/tool gateway;
- A2A interoperability;
- model gateway/routing;
- sessions/state/memory;
- RAG/knowledge;
- evaluation;
- observability;
- guardrails/policy;
- sandbox/code execution;
- private model serving;
- multi-tenancy/isolation;
- CI/CD/versioning;
- SRE/DR;
- FinOps/showback;
- data residency;
- portability/exit.

## 3. Option A — Internal / OpenShift

Typical stack:

```text
OpenShift
 -> agent runtime (LangGraph/custom)
 -> API/AI Gateway
 -> IAM/OIDC
 -> MCP servers/gateway
 -> A2A endpoints
 -> PostgreSQL/state + governed RAG
 -> OTel/Prometheus/Grafana
 -> KServe/vLLM/RHOAI where private models are required
 -> GitOps/policy-as-code
```

Strengths:
- maximum placement/data/control flexibility;
- portable runtime;
- reuse of existing enterprise OpenShift/IAM/observability;
- easier sovereign/private model strategy;
- framework freedom.

Costs/risks:
- highest integration/operations burden;
- registry/lifecycle/evaluation/security need to be assembled;
- platform team must own upgrades, SRE and interoperability;
- GPU/model serving can be expensive operationally.

Use when sovereignty, private connectivity, platform control or portability dominate.

## 4. Option B — Microsoft Foundry Agent Service

Primary-source snapshot:

Microsoft Foundry Agent Service is documented as a managed platform for building, deploying and scaling agents. It provides prompt agents and hosted agents, managed endpoints, automatic scaling, dedicated Entra identities for hosted agents, observability, tools/toolboxes including MCP integration, and publishing/versioning capabilities.

Sources:
- https://learn.microsoft.com/en-us/azure/foundry/agents/overview
- https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/runtime-components

Architecture fit:
- strong when Microsoft/Azure/Entra is strategic;
- managed hosting reduces runtime operations;
- hosted agents can run custom frameworks/code;
- evaluate VNet/networking, regional availability, residency, preview/GA status and exit portability at decision time.

Do not infer universal feature parity across regions/agent types without current verification.

## 5. Option C — Google Vertex AI Agent Builder / Agent Engine

Primary-source snapshot:

Google documents Vertex AI Agent Builder as a suite to build, scale and govern agents in production. Agent Engine provides managed runtime/scaling, sessions, memory, code execution, observability and governance capabilities; it supports several agent frameworks and A2A integration. Google ADK is open-source and intended for modular agent development.

Sources:
- https://docs.cloud.google.com/agent-builder
- https://docs.cloud.google.com/agent-builder/agent-engine/overview
- https://docs.cloud.google.com/agent-builder/agent-development-kit/overview

Architecture fit:
- strong when GCP/Vertex/Gemini and native A2A support are strategic;
- managed runtime plus sessions/memory/evaluation can reduce platform assembly;
- validate preview/GA status, IAM model, regional availability and portability for the specific client.

## 6. Option D — Amazon Bedrock AgentCore

Primary-source snapshot:

AWS documents AgentCore as an agentic platform with modular services including Runtime, Memory, Gateway, Identity, Registry, observability and policy-related capabilities. Runtime is framework/model agnostic and supports MCP and A2A. AgentCore Registry is documented as a centralized catalog for agents, MCP servers, tools, skills and custom resources.

Sources:
- https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/
- https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agents-tools-runtime.html
- https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/identity.html

Architecture fit:
- strong when AWS is strategic and managed modular agent infrastructure is preferred;
- explicit Registry/Identity/Gateway capabilities map closely to enterprise control-plane needs;
- validate regional support, tenancy/network controls, pricing and portability at decision time.

## 7. Option E — Code-first framework layer

Examples:
- LangGraph;
- Microsoft Agent Framework;
- Google ADK;
- other approved OSS/custom frameworks.

Strength:
- orchestration logic stays portable and testable in code.

Constraint:
- framework != enterprise platform.

A code-first framework still needs IAM, model access, tool governance, registry/lifecycle, observability, deployment, SRE, evaluation and policy.

## 8. Protocol portability

### MCP

As of 2026-10-04, MCP 2026-07-28 is the current released protocol revision observed in primary sources, with a stateless core and enterprise-oriented authorization/scalability changes.

Source:
- https://blog.modelcontextprotocol.io/posts/2026-07-28/

### A2A

A2A provides cross-framework/vendor agent interoperability through Agent Cards, tasks/messages/artifacts and standardized transports. On 2026-10-04, the latest specification release observed is 1.0.1; the v1 wire protocol is 1.0, and the TradeOps executable baseline pins Python SDK 1.2.1.

Source:
- https://a2a-protocol.org/latest/

Protocol support reduces coupling but does not eliminate semantic, IAM, data-policy or operational lock-in.

## 9. Decision scorecard

Score each option 1-5, then apply mandatory gates.

| Criterion | Weight guidance |
|---|---:|
| Security / IAM / delegation | 5 |
| Data residency / sovereignty | 5 |
| Tool/MCP governance | 5 |
| A2A / interoperability | 4 |
| Multi-tenancy / isolation | 5 |
| Observability / audit | 5 |
| Runtime/SRE burden | 4 |
| Scalability | 4 |
| Model/provider portability | 4 |
| Framework portability | 3 |
| RAG/state/memory services | 3 |
| Private model serving | 4 when required |
| CI/CD/version lifecycle | 4 |
| Cost transparency | 4 |
| Exit/reversibility | 5 |
| Existing enterprise skills/platform fit | 5 |

A weighted score never overrides a mandatory regulatory/security constraint.

## 10. Hybrid reference position

A likely enterprise pattern is hybrid:

```text
Enterprise identity / API / policy
          |
          v
Portable application/agent contract
          |
     +----+------------------+
     |                       |
     v                       v
Managed agent runtime     OpenShift runtime
for eligible workloads    for private/regulated workloads
     |                       |
     +---- MCP / A2A --------+
          |
 Enterprise tools / data / SoR
```

Possible split:
- managed service for low/medium-risk elastic agents;
- OpenShift for private/high-control workloads;
- shared enterprise registry/policy/evidence model above both;
- portable protocols/contracts;
- provider-specific adapters behind stable interfaces.

## 11. Build vs buy ADR questions

1. Which capabilities are strategic IP?
2. Which data classes may leave private infrastructure?
3. Is per-agent workload identity required?
4. Which protocols must remain portable?
5. Is private model serving mandatory?
6. What is the acceptable managed-service dependency?
7. What exit time/RTO is required from a provider?
8. Which controls must remain enterprise-owned?
9. Who operates 24x7?
10. What evidence proves cost and operational advantage?

## 12. D-090 G5 relationship

This document **does not decide G5 now**.

D-090 requires:
- G1 real AI access;
- G2 governed single consumer;
- G3 second consumer;
- G4 isolation;
- then G5 decision.

At G5 the options are:

```text
KEEP hosted in TradeOps
vs
EXTRACT specialist internal platform
vs
MANAGED provider
vs
HYBRID
```

The decision must use observed reuse, operations, security, cost and portability evidence.

## 13. Truth boundary

Vendor feature statements above are a dated architecture snapshot from official documentation, not implementation claims in this portfolio.

No cloud-managed agent platform is claimed deployed unless separate runtime evidence exists.
