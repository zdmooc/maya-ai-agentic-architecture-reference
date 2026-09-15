# Maya Interlink Enterprise AI Platform — AI-Only Consolidation

Status: **COMPLETE — NO UNIQUE AI ARCHITECTURE CONTENT REMAINS**

Source repository assessed: `zdmooc/maya-interlink-enterprise-ai-platform`.

Scope of this consolidation: **AI/ML/GenAI architecture only**. Generic TOGAF/BIAN/BPMN organisation, generic cloud foundations, generic Terraform/GitOps and payment-domain content are intentionally excluded from this decision.

## 1. AI capabilities in the source and destination mapping

| Source AI capability | Destination in `maya-ai-agentic-architecture-reference` / evidence repos | Status |
|---|---|---|
| AI Control Plane vs Runtime Plane | `enterprise/AI-CONTROL-RUNTIME-PLANE.md` | ABSORBED |
| AI Gateway / provider abstraction | I18 + `enterprise/AI-GATEWAY-IMPLEMENTATION-OPTIONS.md` | ABSORBED |
| LiteLLM executable option | `enterprise/AI-GATEWAY-IMPLEMENTATION-OPTIONS.md` | ABSORBED |
| Envoy AI Gateway reference option | `enterprise/AI-GATEWAY-IMPLEMENTATION-OPTIONS.md` | ABSORBED |
| OpenShift AI / Open Data Hub | I17 Enterprise AI Factory | ALREADY COVERED |
| KServe / vLLM model serving | I10/I17 | ALREADY COVERED |
| Enterprise RAG | I13 + AI Engineering/RAG architecture | ALREADY COVERED |
| Agents / agent state / HITL | I6/I7 + architecture pattern catalog | ALREADY COVERED |
| MCP governed tools | I6/I7/I19 + TradeOps runtime evidence | ALREADY COVERED |
| LLMOps / prompt/model promotion / rollback | I14/I16 + production maturity model | ALREADY COVERED |
| Promptfoo evaluation option | `enterprise/AI-EVALUATION-OBSERVABILITY-TOOLING.md` | ABSORBED |
| Phoenix AI observability option | `enterprise/AI-EVALUATION-OBSERVABILITY-TOOLING.md` | ABSORBED |
| OpenTelemetry AI telemetry | I8 + evaluation/observability tooling | ALREADY COVERED |
| AI Policy-as-Code | `enterprise/AI-POLICY-AS-CODE-CONTROLS.md` | ABSORBED |
| model-id / provider / risk-class / human-review controls | `enterprise/AI-POLICY-AS-CODE-CONTROLS.md` | ABSORBED |
| GPU quota / AI workload controls | I17 + AI Policy-as-Code controls | ABSORBED |
| AI FinOps | I14/I17/I18 + Well-Architected scorecard | ALREADY COVERED |
| AI GreenOps | I14/I17 + Carbon-Aware specialist repository | ALREADY COVERED |
| LLM/RAG/agent/gateway failure injection | `enterprise/AI-FAILURE-INJECTION-RESILIENCE.md` | ABSORBED |
| AI SRE / SLO / error budget | `enterprise/GENAI-SRE-SLO-ERROR-BUDGET.md` | ALREADY COVERED |
| Payment Investigation Agent | I19 Event-Driven AI + payment specialist repositories | ALREADY COVERED |
| multi-provider/hybrid placement | I18 | ALREADY COVERED |
| Responsible AI / deterministic controls / HITL | I16 + ADR/risk/pattern catalogs | ALREADY COVERED |
| evaluation datasets / RAG and agent evaluation | I14 + AI Engineering alignment | ALREADY COVERED |
| AI observability: TTFT/tokens/cost/tool spans | I8/I14 + `AI-EVALUATION-OBSERVABILITY-TOOLING.md` | ABSORBED |

## 2. Explicitly not migrated

The following source topics are outside the AI-only consolidation and already belong in other architecture repositories or are generic architecture/program concerns:

- TOGAF / ArchiMate / BIAN / BPMN / generic C4 method;
- Tribe/Squad/Chapter organisation model;
- generic Azure/AWS/GCP landing-zone design;
- generic Terraform and Ansible organisation;
- generic OpenShift/GitOps platform build;
- European payment protocol/domain material not specific to AI;
- interview profiles unrelated to AI architecture.

Their presence does not justify a second generic Enterprise AI repository.

## 3. Portfolio decision

For AI architecture purposes, `maya-interlink-enterprise-ai-platform` now has **no unique capability that requires a separate repository**.

Canonical model:

```text
maya-ai-agentic-architecture-reference
  = AI architecture / governance / knowledge source of truth

TradeOps-GenAI-Integration
  = primary executable GenAI / Agentic AI evidence

Specialist repositories
  = Azure AI / ODM AI Decision / Carbon-Aware AI / Pega AI / Payments / Integration
```

Decision: **DEPRECATE / SAFE TO DELETE FROM THE AI PORTFOLIO**.

No implementation from the source repository was lost because the source remained `QUEUED / NOT STARTED`; its useful AI content was architectural intent contained in the master prompt and has now been incorporated into the canonical reference.

## 4. Status discipline

The newly absorbed documents are `DESIGNED`. They do not create new runtime claims. Implementation remains demand-driven and should reuse existing executable repositories first.