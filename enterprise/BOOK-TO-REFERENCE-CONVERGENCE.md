# Book-to-Reference Convergence Matrix

Status: **DESIGNED — KNOWLEDGE CONVERGENCE BASELINE**

## Purpose

Track the architecture knowledge that existed in the `architecteAI` learning material but was previously absent or too condensed in this repository.

The repository remains a concise architecture reference. It does **not** copy the books. It extracts durable architecture principles, decision models, controls and evidence criteria.

## Convergence additions

| Knowledge area from learning material | Repository addition | Status |
|---|---|---|
| CPU, NUMA, PCIe, GPU/HBM, NVLink/RDMA, rack/power/cooling | `AI-PLATFORM-PHYSICAL-GPU-ARCHITECTURE.md` | DESIGNED |
| Vector DB internals, ANN/HNSW/IVF, BM25, hybrid, rerank, MRR/nDCG | `ENTERPRISE-RETRIEVAL-VECTOR-DATABASE-ARCHITECTURE.md` | DESIGNED |
| RHOAI Operator, DataScienceCluster, projects, workbenches, pipelines, serving, GPU enablement | `RHOAI-PLATFORM-DEEP-DIVE.md` | DESIGNED |
| Kueue, distributed training, checkpoints, SFT/LoRA/QLoRA, registry/promotion | `DISTRIBUTED-TRAINING-FINETUNING-LIFECYCLE.md` | DESIGNED |
| RHACM/ODF/OADP-style patterns, RAG/model/Kafka state, failover/failback | `AI-PLATFORM-HA-DR-MULTICLUSTER.md` | DESIGNED |
| API/Kafka/MQ/ITSM/CMDB/GitOps integration contracts, idempotency, DLQ, outbox | `AI-SI-INTEGRATION-CONTRACTS.md` | DESIGNED |
| GPU/token telemetry, unit economics, energy/carbon methodology | `AI-FINOPS-GREENOPS-TELEMETRY.md` | DESIGNED |
| Zero Trust, SBOM/AI-BOM, signatures, RAG/agent security, red-team controls | `AI-ZERO-TRUST-SUPPLY-CHAIN-CONTROLS.md` | DESIGNED |

## Intentionally not duplicated

The books remain the learning source for detailed pedagogy on:

- ML mathematics and model families;
- neural networks/backpropagation;
- transformer internals and Q/K/V;
- tokenizer mechanics;
- vendor/product walkthroughs;
- step-by-step laboratory commands.

The repository keeps only what an architect needs for reusable design, review, governance and evidence.

## Repository-only strengths retained

The repository remains stronger than the books in several portfolio/governance areas:

- status discipline `DESIGNED -> IMPLEMENTED -> TESTED -> DEPLOYED -> VERIFIED`;
- Agent autonomy/HITL model;
- Agent/MCP identity propagation;
- EU/France regulatory control mapping;
- mission capability mapping;
- committee pack and demonstrable payment-operations scenario;
- reuse links to specialist MQ/Kafka/Azure/API/GreenOps repositories.

## Rule for future convergence

A book topic is promoted into this repository only if it provides at least one of:

1. a reusable architecture decision;
2. a reusable target pattern;
3. a security/governance control;
4. a measurable NFR/capacity method;
5. a production-readiness/evidence criterion.

Pure teaching detail stays in the learning material.

## Current convergence result

The main architecture gaps identified during the September 2026 comparison are now represented at `DESIGNED` level.

This does **not** change runtime status. Physical GPU benchmarks, RHOAI distributed training, multi-site DR, enterprise SI federation and measured GreenOps evidence remain future implementation work until concrete POC evidence exists.