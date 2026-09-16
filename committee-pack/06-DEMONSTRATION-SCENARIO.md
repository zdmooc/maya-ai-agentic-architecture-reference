# Demonstration Scenario — Agentic Payment Operations

Status: **DESIGNED — DEMONSTRATION BLUEPRINT / REUSES EXECUTABLE SPECIALIST REPOSITORIES**

Purpose: provide one coherent interview/demo scenario that exercises the mission requirements without building a generic chatbot.

## Scenario

Business prompt:

> Instant-payment processing latency has increased. Investigate the incident, identify likely causes, retrieve the relevant runbook, assess operational risk and propose a remediation. Do not execute a sensitive action without approval.

## Architecture path

```text
Operator
  |
  v
OIDC / API Gateway
  |
  v
Agentic AI Runtime / LangGraph
  |
  +--> Observability Agent
  |      -> OpenShift metrics/logs
  |
  +--> Payment Agent
  |      -> IBM MQ queue/channel/payment state
  |
  +--> Knowledge Agent
  |      -> ACL-aware RAG/runbooks/architecture
  |
  +--> Security/Risk Agent
  |      -> policy + evidence + autonomy classification
  |
  v
Fusion / Incident Assessment
  |
  +--> L1 recommendation
  |
  +--> sensitive remediation selected?
            |
            v
       L2 approval workflow
            |
       authenticated reviewer
            |
            v
       MCP tool execution
            |
            v
       audit + verification
```

## Demonstration steps

1. authenticate as an operations user;
2. ask the incident question;
3. show the LangGraph multi-agent state/trace;
4. retrieve the relevant runbook with document/version/citation metadata;
5. show an OpenShift read-only tool call;
6. show an MQ/payment read-only tool call;
7. demonstrate an unauthorized tool request being denied;
8. inject an untrusted/prompt-injection document and show the control behavior;
9. generate a remediation recommendation;
10. request a sensitive action such as restart/reprocess;
11. show `HUMAN_APPROVAL_REQUIRED` / L2 policy;
12. approve with a separate reviewer identity;
13. execute only the bounded approved action;
14. verify the target system outcome;
15. show correlation ID, audit, metrics/traces and evaluation result.

## Specialist repository reuse

### Agentic runtime

`zdmooc/TradeOps-GenAI-Integration`

Reuse:

- real LangGraph orchestration;
- RAG service;
- HITL lifecycle;
- governed tool authorization patterns;
- OTel/Prometheus/Grafana;
- OpenShift/CRC deployment evidence.

### Payments / IBM MQ

`zdmooc/mayabank-ibm-mq-native-ha-openshift-eda-platform`

Reuse:

- IBM MQ/JMS payment processing;
- queue/channel/payment concepts;
- authentication and operational evidence;
- DLQ/backout/replay/idempotence patterns where evidenced.

### Reference architecture

This repository provides:

- native MCP target architecture;
- identity propagation;
- L0-L4 autonomy model;
- regulatory/security controls;
- architecture/committee decision material.

## MCP tool contract examples

```text
openshift.get_pods          L0
openshift.get_logs          L0
openshift.get_metrics       L0
mq.get_queue_depth          L0
mq.get_channel_status       L0
payment.get_status          L0
incident.propose_remedy     L1
openshift.restart_deployment L2 + HITL
mq.replay_message            L2 + HITL
payment.reprocess            L2 + HITL
```

Actual implementation must use only tools supported by the target environment and evidence.

## Success criteria

The demo succeeds when it proves:

- multi-agent orchestration rather than one prompt chain;
- authoritative evidence and explicit conflict/stale states;
- entitlement-aware RAG with citations;
- least-privilege tool boundary;
- denied unauthorized call;
- prompt/RAG security control;
- explicit autonomy level;
- separate reviewer identity and HITL;
- bounded tool execution;
- end-to-end trace/audit;
- measurable task/security/latency/cost evidence.

## Explicit non-claims

The demonstration does not claim:

- a production banking deployment;
- real customer payment mutation;
- production-native MCP unless the protocol implementation is actually tested;
- production enterprise IAM federation unless evidenced;
- business gains before measured pilot results.
