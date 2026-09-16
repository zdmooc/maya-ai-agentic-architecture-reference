# Enterprise Retrieval & Vector Database Architecture

Status: **DESIGNED — ARCHITECTURE REFERENCE / NO PRODUCTION BENCHMARK CLAIM**

## Purpose

Deepen the RAG architecture below the generic `retriever -> reranker -> context` level. This note covers embedding selection, dense/sparse retrieval, ANN indexing, hybrid search, metadata/ACL filtering, quality metrics, sizing, HA and operations.

## Retrieval pipeline

`query -> normalization -> identity/ACL filter -> dense + sparse/lexical candidate retrieval -> rank fusion -> reranking -> context budget -> generation -> citation verification`

Security rule: **authorization is applied before candidate chunks are exposed to the model**.

## Embeddings

Do not select an embedding model by vector dimension alone. Evaluate it against the actual languages, domain vocabulary and document types.

Capture:

- model and tokenizer version;
- vector dimension and numeric precision;
- maximum input length;
- language/domain coverage;
- throughput and latency;
- license/provenance;
- quality on a frozen retrieval test set.

## Dense, sparse and lexical retrieval

- **Dense**: semantic similarity and paraphrases.
- **Sparse**: learned/token-weighted lexical-semantic signal.
- **BM25 / inverted index**: exact names, versions, identifiers, error codes and rare terms.
- **Multi-vector**: multiple representations per document/chunk when justified.

Enterprise default to evaluate: `dense + lexical/sparse + metadata filter + reranking`.

## Distance metrics

Common families:

- cosine similarity;
- inner product;
- L2 distance.

The metric must match the embedding model and index implementation. Changing distance semantics after index construction is an architecture change, not a harmless configuration tweak.

## Exact search vs ANN

Exact search maximizes recall but scales poorly with large corpora. Approximate Nearest Neighbor indexes trade a bounded amount of recall for materially better latency/capacity.

### HNSW

Architectural parameters include:

- graph connectivity (`M`);
- construction search breadth (`efConstruction`);
- query search breadth (`efSearch`).

Higher values usually improve recall at the cost of RAM, build time or latency.

### IVF family

Partition/vector-cluster approaches reduce the search space by probing selected partitions. Architecture decisions include number of lists/partitions, probes, training data quality and rebuild strategy.

## Hybrid search and rank fusion

Do not directly add incomparable dense and BM25 scores without calibration. Reciprocal Rank Fusion (RRF) is a robust baseline because it fuses ranks rather than raw score scales.

Candidate pattern:

`dense top-N + sparse/BM25 top-N -> RRF -> cross-encoder reranker -> top-K context`

## Reranking

A cross-encoder or comparable reranker improves precision on a smaller candidate set but adds latency and compute cost. Treat candidate count and final context size as explicit capacity knobs.

## ACL and metadata

Recommended chunk metadata includes:

- source/document id;
- immutable version/hash;
- page/section;
- classification;
- allowed groups/roles/tenants;
- owner/domain/application;
- validity dates;
- language;
- retention/deletion state;
- embedding/index version.

ACL predicates derived from authenticated claims must be pushed into retrieval, not applied after top-K.

## Retrieval quality metrics

Use a frozen golden set with relevant-document/chunk labels where feasible.

Core metrics:

- Recall@K;
- Precision@K;
- Mean Reciprocal Rank (MRR);
- nDCG;
- ACL leakage rate;
- no-answer/abstention correctness;
- citation correctness;
- retrieval latency p50/p95/p99.

Generation quality must not hide poor retrieval. Diagnose retrieval and generation separately.

## Sizing

Capacity depends on:

- number of chunks;
- vector dimension and precision;
- index overhead;
- payload/metadata size;
- replication factor;
- write/update rate;
- query rate and concurrency;
- reranker workload;
- backup/snapshot overhead.

For HNSW-like indexes, raw vector bytes significantly underestimate RAM because graph structures, payloads and runtime buffers add overhead.

## Sharding, replication and multi-tenancy

Decide explicitly:

- shard key and growth strategy;
- replica count and failure tolerance;
- tenant isolation model;
- cross-tenant query prohibition;
- backup/snapshot/rebuild path;
- zero/low-downtime index migration.

Prefer versioned collections/indexes for material embedding/chunking changes rather than silent in-place mutation.

## Operational lifecycle

`source version -> chunking version -> embedding version -> index version -> baseline/candidate -> evaluation -> promote -> rollback/rebuild`

Required runbooks:

- vector DB unavailable;
- stale index;
- failed reindex;
- ACL regression;
- bad embedding release;
- capacity saturation;
- restore/rebuild from governed sources.

## Required evidence before `VERIFIED`

- frozen retrieval golden set;
- dense vs lexical vs hybrid comparison;
- ACL negative tests with zero leakage;
- reranker comparison;
- measured recall/precision/latency;
- restart/restore/rebuild drill;
- version lineage from source to index.