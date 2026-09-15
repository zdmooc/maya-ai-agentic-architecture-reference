# Designing Data-Intensive Applications — Architecture Alignment for AI

Status: **DESIGNED — DISTRIBUTED-DATA EXTRACTION COMPLETE / NO DEDICATED POC REQUIRED**

Source: *Designing Data-Intensive Applications — 2nd Edition* — Martin Kleppmann, Chris Riccomini, O'Reilly, February 2026.

Purpose: extract the distributed-data and systems principles that an **AI Solution Architect / AI Platform Architect** needs for RAG, agentic systems, vector indexes, event-driven AI, model/data pipelines and auditability.

## 1. Architecture-relevant themes

The second edition covers:
- operational vs analytical systems;
- systems of record and derived data;
- cloud vs self-hosting trade-offs;
- storage/indexing, including vector embeddings;
- schema/encoding evolution;
- REST/RPC, durable workflows and event-driven architectures;
- replication;
- sharding;
- transactions/isolation;
- partial failures in distributed systems;
- consistency and consensus;
- batch processing;
- stream processing;
- data integration and derived state;
- correctness, integrity, privacy and accountability.

## 2. Why this matters to AI architecture

AI systems are still distributed data systems.

Examples:
- RAG uses source systems, ingestion, chunk/embedding/index stores and retrieval services;
- agentic systems use session/workflow state and tool/API calls;
- AI gateways cache and route requests;
- ML systems consume batch/stream features;
- payment AI consumes MQ/Kafka events;
- AI audit/compliance relies on durable evidence and lineage.

A vector database, LLM or agent framework does not remove ordinary distributed-systems trade-offs.

## 3. New gap closed

### GAP-DDIA-01 — Explicit AI data-systems architecture principles

Closed by `AI-DATA-SYSTEMS-ARCHITECTURE-PRINCIPLES.md`.

The repository already had data/knowledge contracts, MQ/Kafka and RAG lifecycle. This book adds a stronger, explicit set of principles for:
- authoritative vs derived state;
- replication/sharding/consistency trade-offs;
- schema evolution;
- batch/stream choice;
- end-to-end correctness;
- partial failure reasoning.

## 4. System of record vs derived data

Architect rule:

- business/core systems remain authoritative for their domain state;
- vector indexes, caches, feature stores, search indexes and AI session summaries are normally **derived data**;
- derived stores must be rebuildable or have an explicit authoritative role if not.

For RAG:

`governed source -> extraction/chunking -> embedding -> vector index`

The vector index is not automatically the source of truth.

## 5. Schema and encoding evolution

AI integrations need versioned contracts for:
- events;
- APIs;
- tool schemas;
- document metadata;
- model I/O;
- embeddings/index metadata.

Compatibility strategy matters because producers and consumers evolve independently.

## 6. Replication and sharding

Use replication for combinations of:
- availability/durability;
- read scaling;
- geographic locality.

Use sharding when scale/tenant isolation/data locality requires partitioning.

Architect must make hot-spot, routing, rebalance and cross-shard-query consequences explicit.

Do not choose a distributed store merely because it is fashionable.

## 7. Transactions and consistency

Not every AI state requires strict serializability, but some surrounding business operations may.

Examples:
- chat/session cache may tolerate weaker consistency;
- payment/action approval state may require stronger transactional guarantees;
- entitlement/security policy must not depend on stale eventually consistent state without explicit risk acceptance.

Consistency is a business correctness decision, not only a database configuration.

## 8. Distributed failure model

Expect:
- partial network failure;
- timeout ambiguity;
- retries/duplicate processing;
- clock differences;
- process pauses;
- split availability across dependencies.

AI-specific consequence:
A timeout from a tool/model does not prove whether an external side effect occurred. Sensitive actions therefore require idempotency, status reconciliation and bounded retry.

## 9. Batch vs stream

Batch fits when:
- freshness can be minutes/hours/days;
- throughput/economics dominate latency;
- periodic enrichment/indexing/retraining is enough.

Stream/event-driven fits when:
- business state changes continuously;
- low-latency detection/action is required;
- replayable domain events are valuable.

Hybrid architectures are common.

## 10. Event-driven correctness

For Kafka/MQ/event AI:
- preserve event identity;
- define ordering assumptions;
- design idempotent consumers;
- distinguish at-least-once transport from exactly-once business effect;
- use DLQ/backout/replay deliberately;
- preserve correlation/causation;
- make side effects reconstructable.

## 11. Storage/indexing principle for AI

Different workloads justify different stores:
- OLTP relational state;
- object storage for documents/models/datasets;
- log/event store;
- vector/full-text index;
- cache;
- analytical warehouse/lakehouse.

Avoid forcing all AI data into one database product.

## 12. Privacy and accountability

Derived AI data can multiply sensitive information across:
- raw corpus;
- chunks;
- embeddings;
- indexes;
- caches;
- logs;
- archives;
- training/evaluation datasets.

Deletion/retention architecture must therefore track derived copies, not only the original source.

## 13. Material deliberately skipped

No need for the current track to master:
- low-level consensus algorithms implementation;
- database-engine internals;
- storage-engine coding;
- distributed-systems proofs.

The architect must understand their trade-offs and failure implications.

## 14. POC policy

No standalone DDIA POC.

Reuse existing evidence:
- IBM MQ/OpenShift repo;
- Kafka/DDD/OpenShift repo;
- RAG/knowledge architecture;
- PostgreSQL/vector patterns;
- OpenShift/platform labs.

Future experiments only when a concrete architecture decision needs evidence on consistency, throughput, replay, vector indexing or data placement.

## 15. Interview outcomes

An AI Solution Architect should be able to answer:
- What is the system of record in a RAG architecture?
- Is a vector DB authoritative or derived?
- When do you choose batch versus stream ingestion?
- What happens when a tool call times out after possibly executing an action?
- How do replication/sharding trade-offs affect AI platform design?
- How do you propagate deletion into embeddings/indexes/caches?
- What does exactly-once mean at the business-effect level?

## 16. Conclusion

This book strengthens the foundation beneath AI architecture: **dataflow, correctness, consistency, evolution and distributed failure**. These principles are now explicitly represented without creating another runtime project.
