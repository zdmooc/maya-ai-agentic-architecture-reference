# Agentic Interoperability — MCP + A2A

Status: **DESIGNED — D-092 M2 / INTEROPERABILITY REFERENCE**

Purpose: distinguish agent-to-tool integration from agent-to-agent collaboration and define the enterprise controls required to combine MCP and A2A safely.

## 1. Core separation

```text
Agent
  -> MCP
      -> Tools / Data / Enterprise Systems

Agent
  -> A2A
      -> Other independent Agents
```

MCP and A2A solve different boundaries and may coexist in the same workflow.

## 2. Current protocol baseline — 2026-10-04

### MCP

Reference version: **MCP 2026-07-28**.

The 2026-07-28 specification introduces a stateless protocol core, explicit request metadata, routable method/tool headers, cacheable list responses, an extensions framework, authorization hardening and a Tasks extension for long-running work.

Reference:
- https://blog.modelcontextprotocol.io/posts/2026-07-28/
- https://modelcontextprotocol.io/

Enterprise implication: MCP servers can be treated more like horizontally scalable HTTP workloads, but protocol adoption does not remove IAM, policy, data-classification or HITL requirements.

### A2A

Reference baseline observed on 2026-10-04: **A2A specification release 1.0.1**, wire protocol version **1.0**, Python SDK baseline **a2a-sdk 1.2.1**.

A2A provides a standard for discovering agent capabilities and exchanging messages/tasks/artifacts between independent agents without exposing their internal state or tools.

Reference:
- https://a2a-protocol.org/latest/
- https://a2a-protocol.org/latest/topics/key-concepts/

Core concepts include Agent Card, Message, Task, Part and Artifact.

## 3. Target architecture

```text
                       Enterprise IAM / Policy
                               |
         +---------------------+---------------------+
         |                                           |
         v                                           v
   Agent A Runtime                              Agent B Runtime
         |                                           |
         | A2A discovery / task / message            |
         +----------------------->--------------------+
         |                                           |
         | MCP                                       | MCP
         v                                           v
   MCP Gateway A                               MCP Gateway B
    /      |      \                            /      |      \
  OCP     MQ    Knowledge                  CRM      DB      ITSM
```

A2A delegates work between agents. MCP exposes bounded resources/tools to an agent.

## 4. Discovery

A2A discovery must not become an unauthenticated enterprise directory leak.

Required controls:

- public vs authenticated Agent Card profile;
- canonical agent ID and endpoint;
- supported protocol version;
- declared skills/capabilities;
- authentication requirements;
- data classification;
- trust domain;
- version and owner metadata;
- optional signed metadata where implementation supports it.

Registry governance is defined in `enterprise/AGENT-REGISTRY-LIFECYCLE-GOVERNANCE.md`.

## 5. Trust and identity

For A2A calls distinguish:

- initiating user/service;
- calling agent workload;
- remote agent workload;
- delegated subject/context;
- downstream MCP/tool identity.

Minimum audit chain:

```text
subject
 -> calling_agent_id/version
 -> remote_agent_id/version
 -> task_id
 -> downstream tool/resource
 -> policy decision
 -> result/artifact
```

Do not treat the remote agent's natural-language claim as identity or authorization.

## 6. Authorization and delegation

An A2A call is allowed only if:

- caller workload identity is valid;
- target agent is approved/discoverable for the caller;
- requested skill/task is allowed;
- tenant/domain boundary passes;
- delegation context is valid;
- data classification permits transfer;
- autonomy policy permits delegation;
- budgets/timeouts are within policy.

The receiving agent re-authorizes its own downstream MCP/tool calls. Authorization is never transitive by default.

## 7. Task lifecycle

Enterprise task handling should map protocol task states to internal operational states and evidence.

Required semantics:

- unique task ID;
- correlation/trace propagation;
- start/working/input-required/completed/failed/canceled mapping;
- explicit timeout;
- cancellation;
- idempotence where mutations can repeat;
- retry policy;
- artifact provenance;
- retention/expiry.

Long-running A2A tasks must not bypass workload queues, SLOs or cost limits.

## 8. Contract/version compatibility

Every inter-agent contract should define:

- protocol version;
- agent version;
- skill schema/version;
- accepted input/output media/types;
- timeout/cancellation semantics;
- error classes;
- backward compatibility window;
- deprecation date;
- retry/idempotence contract.

Compatibility must be tested between at least two independently versioned agents before claiming interoperability.

## 9. MCP + A2A security threats

Specific threats:

- agent impersonation;
- Agent Card poisoning;
- malicious capability advertisement;
- delegation abuse;
- cross-agent prompt injection;
- task replay;
- confused deputy;
- excessive recursive delegation;
- data exfiltration through artifacts;
- A2A loop / task storm;
- remote agent returning malicious tool instructions;
- trust of unverified remote metadata.

Controls:

- signed/verified registry metadata where available;
- authenticated discovery for non-public details;
- allowlisted peers/skills;
- max delegation depth;
- task/time/token/cost budgets;
- schema validation;
- content/data classification checks;
- remote output treated as untrusted input;
- circuit breaker/quarantine;
- end-to-end audit.

## 10. MCP-specific boundary

MCP remains responsible for tool/resource exposure.

Minimum controls continue to be:

- server-side authZ;
- tool allowlist;
- typed schema;
- rate/timeout/budget;
- HITL for sensitive mutation;
- correlation/audit;
- secret isolation;
- deny-by-default.

MCP tool discovery must return only capabilities the caller is entitled to see when the implementation supports authorization-aware catalogs.

## 11. Example — Payment Operations

```text
Investigation Agent
   |
   | A2A
   v
Operations Agent
   |
   | MCP
   +--> openshift.get_pods
   +--> openshift.get_metrics
   +--> mq.get_queue_depth
   +--> cmdb.get_dependencies
```

For remediation:

```text
Investigation Agent
 -> A2A recommendation/delegation
 -> Operations Agent
 -> deterministic policy
 -> HUMAN_APPROVAL_REQUIRED
 -> MCP bounded mutation
 -> target verification
 -> A2A artifact/result
 -> audit
```

## 12. Evidence gate

Architecture is `DESIGNED`.

Runtime A2A claim requires:

1. two agents with distinct identities;
2. discoverable/validated Agent Card;
3. authenticated message/task exchange;
4. cancellation/failure behavior;
5. downstream MCP call by the remote agent;
6. correlated trace/audit;
7. denied unauthorized peer/skill;
8. version/interoperability test.

Until then: **A2A_RUNTIME_INTEROPERABILITY = NOT_PROVEN**.

## 13. Portfolio implementation update — 2026-10-04

`TradeOps-GenAI-Integration` now contains an implemented A2A Payment Operations baseline:

```text
Investigation Agent
 -> A2A JSON-RPC
 -> Payment Operations Agent
 -> native MCP client
 -> bounded IBM MQ read tools
```

Evidence state:
- A2A SDK/server/client-side policy baseline = **IMPLEMENTED + TESTED IN CI** ;
- CI run `37219263119` = SUCCESS ;
- complete TradeOps suite = **278 passed** ;
- unknown peer and unauthorized skill negative tests = PASS ;
- Agent Card / HTTP packaging validators = PASS ;
- live A2A peer authentication/interoperability = **PENDING** ;
- native MCP R1-R4 = **TESTED IN CI** ;
- native MCP R5 -> IBM MQ live CRC = **PENDING** until the local R5 evidence bundle exists.

Therefore:
`A2A_RUNTIME_INTEROPERABILITY = NOT_PROVEN` remains correct.

