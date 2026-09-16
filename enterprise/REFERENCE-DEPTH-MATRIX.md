# AI Architecture Reference Depth Matrix

Status: **DESIGNED — NAVIGATION AID**

This matrix shows where the reference now goes deep enough for architecture decisions and where runtime evidence is still required.

| Domain | Reference depth | Runtime evidence |
|---|---:|---:|
| AI Solution Architecture / FR-NFR / ADR | Strong | N/A or specialist POCs |
| ML/LLM lifecycle | Strong architecture | Partial |
| RAG / retrieval / Vector DB | Strong architecture | Partial via reused runtime |
| Agentic AI / HITL / MCP | Strong architecture | Partial/strong via reused runtime |
| Enterprise SI integration | Strong architecture | Partial via MQ/Kafka repos |
| RHOAI / OpenShift AI | Strong architecture | Partial/deferred |
| Physical GPU / NUMA / PCIe / fabric | Strong architecture | Deferred |
| Distributed training / fine-tuning | Strong architecture | Deferred |
| AI SRE / HA / DR / multi-cluster | Strong architecture | Deferred/partial |
| Zero Trust / supply chain / AI security | Strong architecture | Partial |
| FinOps / GreenOps / unit economics | Strong architecture | Partial |
| Hybrid / multi-cloud AI | Strong architecture | Deferred |
| Payments / operations AI | Strong architecture | Integration POC deferred |
| Multimodal / IDP | Designed | Deferred |

## Interpretation

`Strong architecture` means the repository contains sufficient decision principles, target patterns, controls and evidence criteria for design/review work.

It does **not** mean production proof. Runtime status remains governed by the repository status vocabulary and linked evidence.