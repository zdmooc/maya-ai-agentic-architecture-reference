# Target Architecture and Options — Enterprise Agentic AI

Status: **DESIGNED — DECISION VIEW**

## 1. Target architecture

```text
Channels / Users / Applications
             |
             v
       API Gateway / IAM
             |
             v
          AI Gateway
 authZ / quotas / DLP / routing
             |
             v
 Agent Orchestrator / LangGraph
      +------+-------+
      |              |
      v              v
 Enterprise RAG    MCP Client
 ACL/versioning      |
      |          MCP Gateway
      |         /     |      \
      |        v      v       v
      |      OCP     MQ    CMDB/ITSM
      |        \      |       /
      +---------+-----+------+
                |
       Systems of Record
                |
       Policy + HITL boundary
                |
 Evaluation / LLMOps / Observability / Audit
```

Cross-cutting controls:

- IAM, workload identity and delegated authorization;
- data classification, residency and retention;
- model/provider policy and portability;
- AI-BOM/SBOM/provenance;
- security testing and policy-as-code;
- FinOps/GreenOps and capacity controls;
- resilience/SRE/rollback.

## 2. Architecture options

### Agent framework

| Option | Strength | Constraint | Reference position |
|---|---|---|---|
| LangGraph | explicit state/graph, existing executable evidence | framework lifecycle/dependency | executable baseline |
| Microsoft Agent Framework | Azure/Microsoft ecosystem integration | introduces second agent stack | evaluate only when justified |
| deterministic workflow + LLM step | simpler, lower agency/risk | less flexible planning | prefer when sufficient |

Decision principle: **workflow before agent when deterministic orchestration meets the need**.

### Model placement

| Option | Strength | Constraint | Use when |
|---|---|---|---|
| managed cloud model | rapid access, elastic | provider/data/egress dependency | policy permits data/provider |
| private OpenShift model | control/data locality | GPU/platform operations | confidentiality/sovereignty/latency justify it |
| hybrid router | flexibility/fallback | governance/operational complexity | multiple classes/SLA/providers require it |

### Knowledge architecture

| Option | Position |
|---|---|
| prompt-only | use for stable small context |
| governed RAG | default for fresh/versioned enterprise knowledge |
| fine-tuning | use only when RAG/prompt/workflow cannot meet requirement |

### Tool integration

| Option | Position |
|---|---|
| direct bespoke API call | acceptable for bounded local integration |
| governed API/tool gateway | current executable pattern |
| native MCP | target interoperability pattern; security controls remain server-side |

Native MCP adoption is not a reason to expose broader tools or bypass API/IAM policy.

## 3. Recommended architecture decision criteria

Score options against:

- business fit;
- safety/risk;
- data classification/residency;
- identity/authorization capability;
- latency/SLA;
- availability/DR;
- observability;
- cost and capacity;
- portability/exit;
- platform operational burden;
- evidence maturity;
- regulatory constraints.

Do not produce a universal provider/framework winner. The ADR records the choice for one context and the conditions that would change it.

## 4. Transition architecture

```text
Stage A — read-only assistant
L0: RAG + observability/CMDB reads

Stage B — recommendations
L1: multi-agent diagnosis + remediation proposal

Stage C — controlled action
L2: approved MCP mutation + audit/rollback

Stage D — bounded autonomy
L3: only for proven low-risk reversible actions
```

L4 is not a default enterprise target for regulated/high-impact operations.

## 5. Architecture exit criteria

Before moving beyond design:

- business outcome and baseline KPI defined;
- FR/NFR and constraints approved;
- trust/data flows reviewed;
- autonomy/tool matrix approved;
- provider/model/data placement approved;
- RAG security and lifecycle defined;
- failure/rollback behavior defined;
- evaluation/evidence plan defined;
- operating ownership established;
- residual risks accepted by authorized owners.
