# Architecting Generative AI Applications — Architecture Alignment

Status: **DESIGNED — ARCHITECTURE EXTRACTION COMPLETE / IMPLEMENTATION EVIDENCE SEPARATE**

Source: *Architecting Generative AI Applications* — Leonid Kuligin, Packt, March 2026.

Public references checked:
- O'Reilly: https://www.oreilly.com/library/view/architecting-generative-ai/9781806678655/
- Packt: https://www.packtpub.com/en-us/product/architecting-generative-ai-applications-9781806678648

Purpose: extract only material relevant to **AI Solution Architect / AI Platform Architect / GenAI production architecture**, not developer-first code walkthroughs.

## 1. Relevant book structure

Architecture-relevant chapters/topics:

- prototype and POC discipline;
- evaluation, including RAG/agent evaluation, LLM-as-judge and HITL;
- key architectures: prompt templates, vector DB, hybrid search/reranking, context management, agents and memory;
- DevOps -> MLOps -> LLMOps;
- stateless/stateful deployment, IaC, secrets/config, Kubernetes, caching, throttling and graceful failure;
- Responsible AI, fairness, explainability, safety/security and privacy;
- SRE: SLI/SLO/SLA, error budgets, logs/metrics/traces, GenAI observability;
- post-deployment maintenance and GenAI platform capabilities;
- model gateway, prompt store, tool registry, execution sandbox, session store, feedback service, HITL, serving/training infrastructure;
- A/B testing and online experiments.

## 2. Existing repository coverage

Already strong:

- business-first use-case framing and POC-only-for-uncertainty rule;
- evaluation theory and I14 evaluation pipeline;
- RAG/hybrid retrieval/reranking/context engineering;
- governed agents, MCP tools and HITL;
- OpenShift/GitOps/RHOAI/KServe/vLLM;
- AI Gateway and Model Router;
- observability/OpenTelemetry;
- security/privacy/Responsible AI;
- performance budget and capacity concepts;
- graceful degradation/circuit breakers/fallback;
- feedback lifecycle;
- Design Authority/SAD/NFR/risk/ADR/RACI.

## 3. New gaps closed from this book

### GAP-PROD-01 — Prototype-to-production maturity model

Closed by `GENAI-PRODUCTION-MATURITY-MODEL.md`.

A prototype proving user interest or API feasibility is not production readiness. Production requires evidence across quality, security, reliability, operations, cost, governance and ownership.

### GAP-PROD-02 — Explicit GenAI platform capability map

Closed by `GENAI-PLATFORM-CAPABILITY-MAP.md`.

The repository had the components across I8-I18 but not one concise platform-product map grouping reusable capabilities for many GenAI applications.

### GAP-PROD-03 — SRE error-budget discipline for GenAI

Closed by `GENAI-SRE-SLO-ERROR-BUDGET.md`.

The repository already used SLO concepts but now formalizes error budget as a decision mechanism balancing reliability and delivery velocity.

### GAP-PROD-04 — Online experimentation / A-B testing as controlled product evidence

Closed by `GENAI-ONLINE-EXPERIMENTATION-PATTERN.md`.

Offline evaluation and production monitoring are not enough for all use cases. Controlled online experiments can validate whether an AI change improves a business/user outcome.

## 4. Prototype / POC architect rule

A POC should answer a material uncertainty such as:

- does the model meet task-quality threshold?
- can RAG retrieve and cite the required enterprise evidence?
- can a legacy/API/MQ/Kafka integration meet constraints?
- can the service meet latency/throughput/capacity targets?
- can security controls prevent unacceptable tool/data access?
- is private/cloud placement economically and operationally viable?

A prototype is not evidence of:

- production reliability;
- security approval;
- regulatory compliance;
- scalable operations;
- cost at target volume;
- recoverability;
- adoption/business value.

## 5. LLMOps architecture interpretation

LLMOps extends DevOps/MLOps because application behavior depends on a coupled set of mutable artifacts:

`code + model + prompt + corpus/index + tools + policies + eval data + configuration`

Architecture therefore needs:

- independent versioning and lineage;
- candidate/baseline evaluation;
- promotion/rollback;
- environment separation;
- policy/security gates;
- cost/latency evaluation;
- traceability to production outcomes.

## 6. Deployment and scaling principles retained

- stateless compute where feasible, explicit external state where required;
- IaC and repeatable configuration;
- secret separation;
- Kubernetes/OpenShift orchestration where justified;
- identity-aware/version-aware caching;
- throttling/admission controls;
- bounded retries;
- graceful failure/degradation;
- state/session design for agents;
- avoid cascading failure from model/tool dependencies.

## 7. Platform-team viewpoint

At enterprise scale, multiple GenAI applications should reuse platform capabilities rather than each application rebuilding them.

Reusable capability domains:

- model access/gateway/router;
- prompt registry;
- knowledge/RAG services;
- tool registry and secure execution;
- agent/session state;
- evaluation service;
- feedback/HITL;
- serving/training infrastructure;
- observability/SRE;
- security/policy/governance;
- FinOps/showback;
- developer self-service/templates.

## 8. SRE interpretation

Reliability must be measured from the user/business service perspective, not merely model endpoint uptime.

Candidate SLIs include:

- request success;
- valid/grounded answer rate;
- citation correctness;
- tool/action success;
- no-answer/abstention correctness;
- end-to-end latency;
- stale-evidence rate;
- policy-denial correctness;
- queue delay;
- provider/fallback availability.

Error budgets govern how much unreliability is acceptable before reliability work takes priority over feature velocity.

## 9. Online experimentation

Use A/B testing only when:

- experiment is ethically/security/regulatorily acceptable;
- outcome metric is meaningful;
- assignment does not expose users to unacceptable risk;
- statistical design and duration are appropriate;
- offline safety/quality gates have already passed.

Never A/B test hard security, legal or payment-risk controls by weakening them for one cohort.

## 10. Material deliberately skipped

Not promoted to architect fundamentals:

- code/API wrapping tutorials;
- generic Kubernetes command-level deployment steps;
- tool-specific managed-platform walkthroughs;
- developer implementation details already covered by specialist teams/repos.

## 11. POC policy

No new mandatory POC.

Possible future evidence triggers:

- GenAI production-readiness mission -> score one use case with maturity model;
- AI Platform mission -> implement selected platform capability gap;
- SRE/LLMOps mission -> SLO/error-budget dashboard and failure drill;
- product optimization mission -> controlled online experiment after offline gates.

## 12. Interview outcomes

An AI Solution Architect should now be able to answer:

- Why is a successful POC not production readiness?
- What changes from DevOps/MLOps to LLMOps?
- Which capabilities belong in a shared GenAI platform?
- How do you design state/session handling for agentic applications?
- What are appropriate GenAI SLIs/SLOs?
- What is an error budget and how does it change architecture priorities?
- When should online experiments be used after offline evaluation?
- How do you prevent cascading failures across model, RAG and tools?

## 13. Conclusion

This book's strongest contribution to the reference is the **production operating model**: maturity, platform productization, SRE/error budgets and controlled experimentation. Those gaps are now represented as architecture artifacts without claiming production implementation.
