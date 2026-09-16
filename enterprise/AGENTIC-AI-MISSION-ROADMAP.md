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

### R1 — Native MCP protocol

Implement a real MCP client/server transport using the selected current standard/SDK while preserving the existing governed-tool authorization controls.

Evidence required:

- protocol interoperability test;
- authenticated/authorized tool discovery and calls;
- transport failure behavior;
- audit/correlation propagation;
- negative authorization tests.

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
