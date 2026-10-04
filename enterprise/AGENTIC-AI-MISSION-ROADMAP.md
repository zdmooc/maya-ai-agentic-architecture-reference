# Agentic AI Solution Architect Mission Roadmap

Status: **M1-M4 ARCHITECTURE ALIGNMENT COMPLETE — RUNTIME GAPS TRACKED SEPARATELY**

Purpose: track the focused evolution of this reference repository for senior Enterprise Agentic AI Solution Architect missions without renumbering or duplicating the core I0-I20 program.

## M1 — Mission coverage and runtime truth — COMPLETE

Deliverables:

- mission capability coverage matrix;
- update of Agentic/MCP architecture to reflect real LangGraph runtime;
- explicit distinction between current MCP-shaped governed HTTP boundary and native MCP protocol conformance;
- specialist-repository reuse mapping;
- explicit non-claims.

Files:

- `enterprise/AGENTIC-AI-MISSION-COVERAGE.md`
- `architecture/AGENTIC-MCP-ARCHITECTURE.md`

## M2 — Autonomy and identity — COMPLETE

Deliverables:

- L0-L4 autonomy model;
- per-tool maximum autonomy and HITL rules;
- approval binding and anti-self-escalation rules;
- user/workload/reviewer/tool identity separation;
- token/delegation/on-behalf-of architecture;
- RAG identity/ACL propagation;
- auditable effective authorization model.

Files:

- `enterprise/AGENT-AUTONOMY-HITL-MODEL.md`
- `enterprise/IDENTITY-PROPAGATION-MCP-IAM.md`

## M3 — EU/France regulatory traceability — COMPLETE

Deliverables:

- AI Act architecture-control mapping;
- GDPR architecture-control mapping;
- NIS2/French cybersecurity architecture mapping;
- clarification of legacy OSE/SIE terminology;
- Agentic-AI-specific risk/control mapping;
- evidence bundle and legal/RSSI/DPO validation boundary.

File:

- `enterprise/REGULATORY-CONTROL-MAPPING-EU-FR.md`

## M4 — Committee and interview decision pack — COMPLETE

Deliverables:

- executive summary;
- target architecture and options;
- security/risk/regulatory committee view;
- production readiness gate;
- decision memo template;
- end-to-end Agentic Payment Operations demonstration blueprint.

Files:

- `committee-pack/README.md`
- `committee-pack/01-EXECUTIVE-SUMMARY.md`
- `committee-pack/02-TARGET-ARCHITECTURE-AND-OPTIONS.md`
- `committee-pack/03-SECURITY-RISK-REGULATORY.md`
- `committee-pack/04-PRODUCTION-READINESS.md`
- `committee-pack/05-DECISION-MEMO-TEMPLATE.md`
- `committee-pack/06-DEMONSTRATION-SCENARIO.md`

## Architecture-coverage conclusion

After M1-M4, the reference repository covers the architecture domains expected for a senior Agentic AI Solution Architect mission:

- Agent/LLM platform architecture;
- real multi-agent orchestration reference;
- state/conflict/veto/HITL;
- autonomy levels;
- MCP/tool target architecture;
- API/AI Gateway and IAM;
- identity propagation and least privilege;
- prompt/RAG/tool security;
- enterprise RAG with versioning/ACL/citations;
- evaluation/LLMOps/observability;
- OpenShift/private/hybrid/GPU architecture;
- architecture governance and Design Authority;
- EU/France regulatory traceability;
- committee-grade decision material.

## Runtime/evidence backlog — NOT architecture gaps

The following are implementation/evidence work and must remain separate from the completed architecture alignment:

### R1 — Native MCP protocol — IMPLEMENTED + TESTED IN CI / R5 LIVE CRC PENDING

TradeOps now contains a native MCP client/server implementation and R1-R4 CI evidence covering protocol host, security controls, tool contracts and negative authorization.

Remaining live evidence:
- R5 `TradeOps -> native MCP -> mq-ops-api -> IBM MQ` on CRC;
- actual local evidence bundle with `R5_CRC_MCP_MQ_VERIFY_PASS`;
- no production claim from this lab.

### D092-R3 — A2A executable baseline — IMPLEMENTED + TESTED IN CI / LIVE PENDING

TradeOps now packages `a2a-sdk==1.1.5` with an Operations Agent exposing bounded payment/MQ diagnostic skills and reusing the native MCP client.

CI run `37219263119` passed the full 278-test suite plus D-092 validator and Helm render.

Still required before runtime claim:
- live two-agent execution;
- authenticated peer identity;
- Agent Card discovery;
- unauthorized peer/skill denial over live transport;
- cancellation/failure evidence;
- correlated A2A -> MCP trace.

### R2 — Enterprise IAM federation

Implement selected IdP/gateway/delegation flow in a demonstrable environment.

Evidence required:

- real OIDC federation;
- user/workload/reviewer separation;
- expired/wrong-audience/missing-scope tests;
- delegated tool authorization.

### R3 — Payment/OpenShift MCP servers

Expose bounded tools against the local/demo OpenShift and IBM MQ/payment environments.

Evidence required:

- L0 read tools;
- unauthorized denial;
- one L2 action with HITL;
- idempotence/rollback/verification;
- end-to-end audit.

### R4 — Enterprise RAG ACL POC

Transpose the current RAG baseline to an enterprise corpus with document versions and role-based access.

Evidence required:

- two+ roles with different entitlements;
- denied cross-role retrieval;
- citations/version metadata;
- poisoned-document test;
- delete/rebuild test.

### R5 — Mission demo evidence bundle

Run the committee-pack demonstration scenario and capture:

- `oc get pods`/routes or equivalent runtime state;
- multi-agent trace;
- RAG query/citations;
- MCP/tool denial;
- HITL approval/execution;
- audit/metrics/traces;
- evaluation and security results.

## Claim discipline

M1-M4 being complete means **architecture coverage is complete for the target mission**. It does not mean R1-R5 are implemented or that the portfolio represents client production experience.

## D-092 extension track — M1-M5 COMPLETE

This extension is separate from the original M1-M4 mission-alignment numbering above.

### D092-M1 — Agent Registry & Lifecycle — COMPLETE / DESIGNED
File:
- `enterprise/AGENT-REGISTRY-LIFECYCLE-GOVERNANCE.md`

### D092-M2 — MCP + A2A interoperability — COMPLETE / DESIGNED
File:
- `architecture/AGENTIC-INTEROPERABILITY-MCP-A2A.md`

### D092-M3 — Scalability / Multi-tenancy — COMPLETE / DESIGNED
File:
- `enterprise/AGENTIC-PLATFORM-SCALABILITY-MULTITENANCY.md`

### D092-M4 — Build vs Buy / Hybrid — COMPLETE / DESIGNED
File:
- `enterprise/AGENTIC-PLATFORM-BUILD-VS-BUY-2026.md`

### D092-M5 — Mission / Committee Pack refresh — COMPLETE / DESIGNED
Updated:
- `committee-pack/README.md`
- `committee-pack/01-EXECUTIVE-SUMMARY.md`
- `committee-pack/02-TARGET-ARCHITECTURE-AND-OPTIONS.md`
- `committee-pack/04-PRODUCTION-READINESS.md`
- `committee-pack/05-DECISION-MEMO-TEMPLATE.md`
- `committee-pack/06-DEMONSTRATION-SCENARIO.md`

### Next runtime gates

Architecture completion does not supersede D-090.

```text
G0 CLOSED
 -> G1 TradeOps -> Kong -> LiteLLM -> real model
 -> G2 governed single consumer
 -> targeted A2A runtime proof
 -> G3 ODM second consumer
 -> G4 cross-consumer isolation
 -> G5 platformization decision
```

D-094 async AI/TaskIQ/RabbitMQ/KEDA runtime work is queued behind G1/G2 and should reuse the same governed real-model path.

