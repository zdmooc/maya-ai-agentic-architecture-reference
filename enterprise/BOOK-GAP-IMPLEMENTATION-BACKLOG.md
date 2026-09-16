# Book-Derived Architecture Gap — Implementation Backlog

Status: **DESIGNED / IMPLEMENTATION DEMAND-DRIVEN**

Documentation convergence is complete for the identified gaps. Runtime work remains demand-driven.

## Backlog

| Capability | Architecture | Runtime next proof |
|---|---|---|
| Physical GPU/platform topology | DESIGNED | capture real topology + benchmark |
| Advanced retrieval/vector DB | DESIGNED | hybrid retrieval + ACL + golden-set metrics |
| RHOAI deep platform | DESIGNED | install/activate selected components and capture state |
| Distributed training/fine-tuning | DESIGNED | small LoRA/QLoRA or distributed training run with lineage |
| Multi-cluster HA/DR | DESIGNED | two-cluster failover/restore lab |
| SI integration contracts | DESIGNED | end-to-end MQ/Kafka/ITSM/GitOps scenario |
| FinOps/GreenOps telemetry | DESIGNED | measured GPU/token/energy dashboard |
| Zero Trust/supply chain | DESIGNED | SBOM/signature/admission + negative tests |

## Activation rule

Do not execute these in sequence just because they exist. For each mission:

1. extract required capabilities;
2. map to existing evidence;
3. choose one missing high-value proof;
4. implement the smallest demonstrator;
5. capture tests/evidence;
6. upgrade only that capability's maturity status.