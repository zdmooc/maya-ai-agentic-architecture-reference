# AI Platform Physical & GPU Architecture Reference

Status: **DESIGNED — ARCHITECTURE REFERENCE / NO HARDWARE BENCHMARK CLAIM**

## Purpose

Complete the enterprise AI reference below the OpenShift/OpenShift AI layer. This note captures the physical decisions that materially affect AI workloads: CPU, NUMA, PCIe, GPU memory, interconnects, storage, network, power and cooling.

## Decision chain

`Business workload -> SLO -> model/runtime profile -> memory/compute demand -> server topology -> cluster topology -> rack/datacenter feasibility`

Do not start with a GPU SKU. Start with workload characteristics and measurable service objectives.

## Four sizing levels

| Level | Main question | Evidence expected |
|---|---|---|
| Model | Does the model and its runtime fit? | weights, precision, KV cache, runtime overhead |
| Server | Can one server feed the accelerators correctly? | CPU/RAM/PCIe/NIC/NVMe topology |
| Cluster | Can the service meet SLOs and survive failure? | replicas, GPU pools, fabric, HA, queueing |
| Datacenter | Can the site power and cool the design? | rack kW, PDU, cooling, floor/rack constraints |

## CPU / NUMA / PCIe

Architectural checks:

- Distinguish socket, physical core, logical thread and Kubernetes CPU unit.
- Verify memory channels and bandwidth, not only RAM capacity.
- Preserve CPU-memory-device locality for latency-sensitive workloads.
- Inspect PCIe root complexes, switches, link width, oversubscription and negotiated speed.
- Evaluate IOMMU, SR-IOV and device isolation only when the workload justifies them.
- For sensitive workloads, evaluate OpenShift CPU Manager and Topology Manager rather than assuming generic scheduling is sufficient.

A fast GPU attached through a poor CPU/PCIe/NIC topology can be slower than a nominally weaker but balanced system.

## GPU architecture dimensions

Treat four dimensions independently:

1. **Compute** — tensor/matrix throughput at the precision actually used.
2. **Memory** — HBM/VRAM capacity for weights, KV cache, activations, buffers and margin.
3. **Bandwidth/interconnect** — HBM bandwidth, host-device path, GPU-GPU path and node-node fabric.
4. **Operability** — drivers, runtime, scheduling, sharing, ECC/RAS, telemetry, energy and replacement procedures.

### Memory model

First-order serving estimate:

`weight_memory ~= parameter_count x bytes_per_parameter`

Then add:

- quantization metadata;
- KV cache;
- runtime/workspace buffers;
- allocator fragmentation;
- safety headroom.

A model that nominally fits in VRAM can still fail under concurrency because KV cache grows with active sequences and context length.

## GPU communication

Keep three problems separate:

- host <-> GPU: PCIe / coherent host links;
- GPU <-> GPU in one node: NVLink/NVSwitch, Infinity Fabric or PCIe P2P;
- node <-> node: Ethernet, RoCE or InfiniBand when benchmark evidence justifies it.

Tensor parallel, pipeline parallel, data parallel and expert parallel impose different communication patterns. Multi-GPU sizing therefore requires measured collective communication behavior, not only aggregate GPU count.

## Storage and data path

Separate:

- object storage for datasets, model artifacts and checkpoints;
- shared/PVC storage for workspace and state where appropriate;
- local NVMe/cache for hot data and checkpoint staging;
- registry/object-store durability from ephemeral compute nodes.

Measure cold start, model load, checkpoint write/read and dataset feed rate. A GPU waiting for storage is wasted capacity.

## Network planes

At minimum distinguish:

- client/inference traffic;
- east-west service traffic;
- storage/data traffic;
- training/collective traffic when applicable;
- management and out-of-band administration.

Encryption, routing, QoS and failure domains should be explicit per plane.

## Power and cooling

GPU platform capacity is bounded by electrical and thermal design. Record:

- board/server power envelope;
- rack density and PDU limits;
- cooling design and redundancy;
- headroom for growth and failure scenarios;
- energy telemetry where available.

FinOps and GreenOps estimates must distinguish measured energy from estimates.

## OpenShift mapping

Physical topology must be translated into schedulable policy:

- node labels and MachineConfigPool / node-pool boundaries;
- taints/tolerations;
- affinity/anti-affinity and topology spread;
- extended GPU resources;
- hardware profiles / quotas;
- PriorityClass and queue/admission policy;
- topology-aware placement for sensitive workloads.

## Required evidence before `VERIFIED`

- hardware topology capture;
- `lspci` / NUMA / accelerator topology evidence or equivalent;
- OpenShift allocatable resource evidence;
- representative inference/training benchmark;
- GPU memory, utilization, power and queue metrics;
- failure/recovery test;
- documented rack/power feasibility for production design.

Until those exist, this capability remains `DESIGNED`.