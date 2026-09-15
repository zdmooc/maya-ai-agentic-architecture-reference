# AI Data Systems Architecture Principles

Status: **DESIGNED — DISTRIBUTED DATA REFERENCE FOR AI ARCHITECTS**

Purpose: make explicit the distributed-data principles behind RAG, agentic systems, AI platforms, event-driven AI, auditability and ML pipelines.

## 1. System of record versus derived state

Every architecture must identify the authoritative source for each business fact.

Typical authoritative sources:
- core banking/payment systems;
- customer/product/policy systems;
- governed document repositories;
- approved operational databases;
- authoritative event sources.

Typical derived stores:
- vector indexes;
- full-text indexes;
- caches;
- feature stores;
- embeddings;
- materialized views;
- session summaries;
- analytical replicas.

Derived data must either be rebuildable from governed sources or have an explicitly documented authoritative role.

## 2. RAG dataflow principle

Canonical enterprise knowledge path:

`source -> ingestion -> quarantine/validation -> curated representation -> chunks -> embeddings -> indexes -> retrieval -> context -> answer`

The index is not automatically the source of truth.

Required lineage:
- source/version/hash;
- extraction configuration;
- chunking version;
- embedding model/version;
- index version;
- deletion/expiry state.

## 3. Schema and contract evolution

Version contracts for:
- REST/API payloads;
- MQ/Kafka events;
- tool/MCP schemas;
- model input/output schemas;
- document metadata;
- RAG chunk metadata;
- audit/evidence records.

Compatibility must be deliberate because producers and consumers evolve independently.

Preferred rules:
- additive evolution where feasible;
- tolerant readers only where semantically safe;
- explicit breaking-version path;
- contract tests;
- deprecation window;
- ownership of each schema.

## 4. Replication principle

Use replication only for explicit goals such as:
- availability;
- durability;
- read scale;
- geographic locality;
- disaster recovery.

Architectural questions:
- synchronous or asynchronous?
- acceptable replication lag?
- read-after-write requirement?
- conflict/failover model?
- region/residency constraints?

Do not assume replicas are immediately consistent.

## 5. Sharding and partitioning principle

Partition when scale, tenant isolation, locality or workload management requires it.

Partition key selection must consider:
- even distribution;
- hot keys;
- tenant boundaries;
- query patterns;
- rebalance cost;
- cross-partition transactions/queries;
- data residency.

Vector stores and event streams can also suffer hot partitions.

## 6. Consistency is a business correctness decision

Different state requires different consistency guarantees.

Examples:
- ephemeral chat cache may tolerate eventual consistency;
- RAG index freshness can tolerate bounded delay if explicitly surfaced;
- payment approval state may require transactional consistency;
- authorization/entitlement decisions must not rely on dangerously stale state;
- audit evidence may require immutable ordering/integrity properties.

Choose the weakest consistency model that still satisfies correctness and risk requirements—not weaker.

## 7. Distributed timeout ambiguity

A timeout means the caller does not know the outcome, not necessarily that nothing happened.

For AI tools with side effects:
- use idempotency keys;
- reconcile status before retry;
- bound retries;
- persist correlation/action IDs;
- separate command acceptance from completion;
- use compensation where required;
- require HITL for high-impact ambiguous actions.

Never retry destructive/non-idempotent operations blindly because an LLM or agent saw a timeout.

## 8. Exactly-once business effect

Transport semantics and business semantics differ.

Even if infrastructure advertises exactly-once processing, the architect must design for exactly-once **business effect** using combinations of:
- idempotent consumers;
- unique business keys;
- transactional outbox/inbox;
- deduplication;
- status reconciliation;
- deterministic state transitions.

## 9. Batch versus stream

Choose batch when:
- freshness requirement is relaxed;
- economics/throughput dominate latency;
- periodic indexing/enrichment/scoring is sufficient.

Choose streaming/events when:
- state changes continuously;
- reaction latency matters;
- replayable domain history is useful;
- multiple consumers need decoupled updates.

Hybrid is normal:
- streaming for live business events;
- batch for reindexing, retraining, historical backfill and large-scale evaluation.

## 10. Event-driven AI rules

For MQ/Kafka/event AI:
- preserve event identity;
- preserve source timestamp and ingestion timestamp;
- define ordering assumptions;
- use correlation/causation IDs;
- handle duplicates;
- provide DLQ/backout and replay controls;
- separate event detection from sensitive action execution;
- make replay side effects safe.

## 11. Storage is workload-specific

Common roles:
- relational OLTP: authoritative transactional/workflow state;
- object storage: documents, datasets, models, artifacts;
- event log: replayable domain events;
- vector/full-text index: retrieval acceleration;
- cache: latency/cost optimization;
- analytical warehouse/lakehouse: reporting/training/large-scale analysis;
- immutable evidence/archive store: compliance/audit where justified.

Avoid one-database-for-everything architecture.

## 12. Cache correctness

AI cache keys may need to include:
- tenant/identity scope;
- authorization/policy context;
- model alias/version;
- prompt version;
- index/corpus version;
- tool/config version;
- locale/language;
- freshness/TTL.

A fast cache that leaks entitlements or serves stale regulated content is an architecture failure.

## 13. Derived-data deletion

Deletion can propagate through:

`source -> extracted copy -> chunks -> embeddings -> vector index -> caches -> evaluation datasets -> archives/backups according to policy`

Architecture must document:
- what is deletable;
- what is retained under legal/regulatory obligation;
- rebuild/invalidation process;
- deletion evidence.

## 14. Data locality and hybrid placement

Before model routing, determine whether data may leave its current trust/residency boundary.

Placement dimensions:
- classification;
- residency;
- provider authorization;
- encryption/key policy;
- network egress;
- latency;
- replication location;
- backup/archive location.

## 15. Partial failure is normal

Design each dependency assuming independent failure:
- model endpoint;
- vector store;
- IAM;
- API/tool;
- MQ/Kafka;
- workflow database;
- human-approval service;
- observability stack.

For each dependency define timeout, retry, circuit breaker, degraded mode, reconciliation and recovery.

## 16. Correctness over component optimism

A healthy component does not imply a correct system.

End-to-end correctness requires:
- valid source data;
- compatible schemas;
- correct entitlement;
- fresh enough state;
- correct model/prompt/index/tool version;
- successful deterministic controls;
- auditable final business effect.

## 17. Architect review questions

1. What is authoritative for every critical fact?
2. Which stores are derived and how are they rebuilt?
3. What consistency does each state require?
4. What happens on timeout after a possible side effect?
5. How are duplicates/replays made safe?
6. Why batch or stream?
7. How do schemas evolve?
8. Where can data be replicated geographically?
9. How is deletion propagated through derived stores?
10. What are the expected partial failures and degraded modes?

## 18. POC policy

No standalone data-systems POC is required. Reuse IBM MQ, Kafka/DDD, RAG/vector and OpenShift evidence. Build focused tests only when a concrete decision needs measured throughput, consistency, replay, indexing or placement evidence.
