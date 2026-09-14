# AI Architect Book Backlog

Status: **CURATED READING / ARCHITECTURE EXTRACTION BACKLOG**

Purpose: maintain a focused reading backlog for **AI Solution Architect / Enterprise AI Architect / AI Platform Architect** work. This list intentionally excludes developer-first books whose main value is Python, LangChain, application coding or Data Science implementation.

The method for each book is:

`READ -> EXTRACT ARCHITECTURE PRINCIPLES -> MAP TO REFERENCE ARCHITECTURE -> IDENTIFY GAPS -> ADD ADR/NFR/PATTERN -> DEFER POC UNTIL BUSINESS DEMAND`

No book creates a mandatory implementation roadmap by itself.

---

## Priority 0 — Completed baseline

### 1. AI Engineering — Chip Huyen

Status: **THEORETICAL ALIGNMENT COMPLETE**

Focus retained for architecture:

- foundation-model selection and constraints;
- evaluation and model/system selection;
- prompt/context architecture;
- RAG and agents;
- fine-tuning decision criteria;
- dataset engineering;
- inference optimization;
- AI Gateway, Model Router, cache, observability and user feedback.

Repository mapping:

- `AI-ENGINEERING-FUNDAMENTALS.md`
- `AI-ENGINEERING-BOOK-ALIGNMENT.md`
- I13-I20 theoretical design.

---

# Priority 1 — Core AI / Solution Architecture

## 2. Solutions Architect's Handbook — 3rd Edition

Authors: Saurabh Shrivastava, Neelanjali Srivastav.

Why it matters:

- solution-architect role and responsibilities;
- architecture principles and design patterns;
- FR/NFR and quality attributes;
- cloud-native architecture;
- machine-learning architecture;
- generative-AI architecture;
- modernization and legacy integration;
- Solution Architecture Document (SAD);
- architecture communication and decision making.

What to extract into our reference:

- formal SAD structure for AI solutions;
- FR/NFR template for AI applications;
- architecture pattern catalog;
- modernization/integration patterns for legacy banking systems;
- GenAI reference-architecture comparison;
- stakeholder and design-authority deliverables.

POC policy: **none by default**. Mostly an architecture/documentation/design-authority source.

---

## 3. Enterprise Generative AI Well-Architected Framework & Patterns

Why it matters:

- explicit enterprise GenAI architecture viewpoint;
- Well-Architected pillars adapted to GenAI;
- operational excellence;
- security and compliance;
- guardrails/content moderation;
- enterprise adoption patterns;
- architecture trade-offs for foundation models.

What to extract:

- GenAI Well-Architected scorecard;
- architecture review checklist;
- guardrail and compliance control matrix;
- mapping with I15/I16 Design Authority and Responsible AI;
- anti-pattern catalog.

POC policy: only if a mission asks for **AI governance / Well-Architected assessment / regulated GenAI**.

---

## 4. Architecting Generative AI Applications — Leonid Kuligin

Publication: 2026.

Why it matters:

- production-oriented GenAI architecture;
- transition from prototype to production;
- evaluation;
- LLMOps;
- SRE and reliability;
- scalable architecture patterns;
- operationalization of GenAI systems.

What to extract:

- prototype-to-production maturity model;
- production reference architecture;
- LLMOps/SRE control points;
- resilience and failure-mode catalog;
- scalability and performance NFRs;
- mapping against I14, I16 and I17.

POC policy: activate only for **GenAI production / LLMOps / AI SRE / platform** missions.

---

# Priority 2 — AI Platform / Multi-Cloud Architecture

## 5. Google Machine Learning and Generative AI for Solutions Architects

Author: Kieran Kavanagh.

Why it matters:

- written specifically for Solutions Architects;
- enterprise AI/ML system design;
- GenAI architecture;
- MLOps;
- scalable platform patterns;
- cloud AI reference architectures.

Scope rule:

Read for **architecture concepts**, not to become a Google Cloud specialist.

What to extract:

- GCP GenAI/ML reference architecture patterns;
- comparison with Azure/OpenShift targets;
- MLOps platform building blocks;
- multi-cloud placement implications;
- portability and provider-lock-in ADRs;
- inputs for I18 Hybrid/Multi-Cloud AI.

POC policy: no GCP POC unless required by a mission.

---

## 6. The Machine Learning Solutions Architect Handbook — 2nd Edition

Author: David Ping.

Important scope restriction: **not a Data Science learning path for us**.

Read only the architecture-relevant sections:

- ML lifecycle from a Solution Architecture viewpoint;
- business use cases;
- enterprise ML architecture;
- data/platform architecture;
- MLOps;
- security, governance and compliance;
- Generative AI project lifecycle;
- Generative AI platforms and solutions.

Skip/deprioritize:

- algorithm implementation detail;
- model-training exercises;
- Data Scientist-oriented hands-on content that does not affect architecture decisions.

What to extract:

- AI/ML platform capability map;
- lifecycle responsibilities;
- governance gates;
- architecture roles and operating model;
- GenAI platform requirements;
- security/compliance requirements.

POC policy: only if an **ML platform / MLOps / AI platform** mission needs proof.

---

## 7. Designing Machine Learning Systems — Chip Huyen

Scope: **systems architecture**, not Data Science.

Why it matters:

- business objectives -> system requirements;
- reliability, scalability, maintainability and adaptability;
- data distribution shifts;
- model deployment and prediction services;
- monitoring;
- continual learning;
- production testing;
- MLOps infrastructure and tooling;
- responsible AI.

What to extract:

- ML-system NFR model;
- architecture lifecycle from business objective to production;
- deployment patterns: shadow, canary, A/B;
- monitoring/drift architecture;
- model/platform operational boundaries;
- mapping to I5/I10/I14/I17.

POC policy: none by default; selected POCs only for MLOps/platform missions.

---

# Priority 3 — Data and Distributed Systems Foundations for AI Architects

## 8. Designing Data-Intensive Applications — 2nd Edition

Authors: Martin Kleppmann, Chris Riccomini.

Publication: 2026.

Why it matters to an AI Architect:

AI systems are still distributed data systems. RAG, agents, event-driven AI, vector indexes, feature pipelines, knowledge ingestion and audit cannot be architected correctly without data-system trade-offs.

Architecture topics to extract:

- operational vs analytical systems;
- system of record vs derived data;
- cloud vs self-hosting;
- distributed-system failure modes;
- NFRs;
- data models;
- replication and sharding;
- transactions/consistency;
- streams/events;
- batch and distributed processing;
- data governance implications.

Mapping:

- I13 knowledge platform;
- I17 AI Factory data plane;
- I18 hybrid placement;
- I19 Kafka/MQ/event-driven AI.

POC policy: no dedicated POC. Reuse MQ/Kafka/RAG/platform evidence.

---

## 9. Building Evolutionary Architectures — 2nd Edition

Authors: Neal Ford, Rebecca Parsons, Patrick Kua, Pramod Sadalage.

Why it matters:

AI stacks change rapidly. The architecture must evolve without losing security, cost, reliability or portability.

What to extract:

- fitness functions;
- evolutionary architecture principles;
- incremental change;
- architectural characteristics;
- governance through automated checks;
- coupling and changeability;
- architecture transition strategy.

Mapping:

- I15 Design Authority;
- I16 governance/policy;
- I18 provider reversibility;
- architecture fitness functions for model/provider/prompt/index evolution.

POC policy: architecture/governance only; no standalone POC.

---

# Reading order

Recommended order for the architecture program:

1. `AI Engineering` — **DONE**.
2. `Solutions Architect's Handbook, 3rd Ed.`
3. `Enterprise Generative AI Well-Architected Framework & Patterns`
4. `Architecting Generative AI Applications`
5. `Google Machine Learning and Generative AI for Solutions Architects`
6. `The Machine Learning Solutions Architect Handbook, 2nd Ed.` — architecture chapters only.
7. `Designing Machine Learning Systems` — systems/production chapters only.
8. `Designing Data-Intensive Applications, 2nd Ed.`
9. `Building Evolutionary Architectures, 2nd Ed.`

This order goes from **AI application architecture -> enterprise governance -> production AI -> AI platform/multi-cloud -> ML systems -> data/distributed systems -> evolutionary governance**.

---

# Extraction rule for every future book

For each book, create a dedicated alignment document only when we start it. The document must answer:

1. What architecture concepts are new?
2. What is already covered by the repository?
3. What is missing theoretically?
4. Which ADRs/NFRs/patterns should be added?
5. Which content is developer/Data Science detail and can be skipped?
6. Which future POCs become relevant only for a concrete business demand?
7. Which interview questions should an AI Solution Architect be able to answer after the book?

The objective is **not to accumulate books**. The objective is to turn each selected source into a stronger, coherent AI architecture reference without unnecessary implementation work.
