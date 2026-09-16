# Executive Summary — Enterprise Agentic AI

Status: **DESIGNED — COMMITTEE TEMPLATE**

## Business objective

Enable enterprise users and operations teams to use Agentic AI for governed investigation, knowledge retrieval, recommendation and selected bounded actions while preserving deterministic security, business and compliance controls.

## Target value

Candidate outcomes:

- reduce time spent gathering operational evidence;
- improve access to architecture/runbook/CMDB knowledge;
- accelerate incident diagnosis and preparation of remediation;
- reduce repetitive operational work where automation is safe;
- provide traceable, entitlement-aware RAG answers;
- standardize AI security, evaluation and governance instead of building isolated copilots.

Every pilot must define a measurable baseline before value claims are made.

## Target architecture

```text
Users / Applications
        |
        v
API Gateway / IAM
        |
        v
AI Gateway / policy
        |
        v
Agent Runtime / LangGraph
   |                 |
   v                 v
Enterprise RAG     MCP/tool layer
   |            /       |        \
   |       OpenShift   IBM MQ   CMDB/ITSM
   |                 |
   +-----------------+
        |
Deterministic Systems of Record
        |
Policy / HITL for sensitive actions
        |
Evaluation / LLMOps / Observability / Audit
```

## Non-negotiable controls

- least privilege and authoritative server-side authorization;
- ACL filtering before RAG context construction;
- no unrestricted shell/SQL/platform/payment mutation tool;
- explicit L0-L4 autonomy classification;
- HITL for production/payment/security-sensitive actions by default;
- model output cannot override deterministic risk/security/business policy;
- end-to-end correlation and audit;
- provider/model/data placement governed by classification and policy;
- evaluation, security regression and rollback evidence before promotion.

## Key architecture decisions

Committee decisions normally include:

1. selected use case and business owner;
2. maximum autonomy level;
3. allowed tools and Systems of Record;
4. data classes/corpora permitted for AI processing;
5. private/cloud/provider eligibility;
6. target IAM/delegation pattern;
7. RAG and retention model;
8. production readiness/evaluation gates;
9. incident/rollback/accountability model;
10. regulatory/applicability review owners.

## Current portfolio evidence

The reference architecture reuses specialist repositories rather than duplicating implementation:

- executable LangGraph/RAG/HITL/security/observability/OpenShift baseline: `TradeOps-GenAI-Integration`;
- IBM MQ/JMS payment platform evidence: `mayabank-ibm-mq-native-ha-openshift-eda-platform`;
- Azure/cloud architecture: `mayabank-azure-cloud-ai-platform`;
- API Management architecture: `mayabank-api-management-architecture`;
- event-driven/Kafka/OpenShift specialist repositories where relevant.

## Explicit limitations

Do not infer from this pack:

- client production experience that is not documented in the professional record;
- native MCP protocol conformance without runtime evidence;
- production IAM federation;
- production-scale RAG/GPU benchmarks;
- regulatory certification or legal compliance.
