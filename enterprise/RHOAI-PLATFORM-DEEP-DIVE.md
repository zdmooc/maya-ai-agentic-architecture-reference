# Red Hat OpenShift AI Platform Deep Dive

Status: **DESIGNED — REFERENCE / VERSION-SENSITIVE DETAILS MUST BE REVALIDATED**

## Purpose

Complete the reference between OpenShift infrastructure and application-level AI workloads. This note captures the platform architecture of Red Hat OpenShift AI (RHOAI): Operators, DataScienceCluster, projects, workbenches, pipelines, registry, serving, training, queues, GPU enablement and operational boundaries.

## Core mental model

RHOAI is **not a separate cluster**. It is an AI platform layer on top of OpenShift and inherits the cluster's scheduler, RBAC, storage, networking, routes, Operators, SCC/security and failure domains.

`Datacenter -> OpenShift -> GPU/device enablement -> RHOAI Operator -> DataScienceCluster -> Projects -> Workbench/Pipeline/Training/Serving`

## Responsibility boundary

| Need | OpenShift | RHOAI |
|---|---|---|
| Nodes / scheduler / CRI-O | owns | consumes |
| Namespace / RBAC / SCC | owns | consumes |
| NetworkPolicy / Route / Service | owns | consumes |
| CSI/PVC | owns | consumes |
| GPU resource exposure | GPU/operator stack + Kubernetes | consumes through profiles/workloads |
| Workbench | generic only | first-class AI experience |
| AI pipelines | can be assembled | managed AI capability |
| Model registry | external/custom possible | managed/integrated capability |
| Model serving | generic workload possible | KServe/runtime integration |
| Distributed training | generic jobs possible | AI-specific operators/runtime integration |

## Preflight gates

Before activating AI services, validate independently:

1. OpenShift node and ClusterOperator health.
2. DNS, certificates and Routes.
3. StorageClass and PVC behavior.
4. Registry/image access and disconnected/mirror strategy where applicable.
5. User-workload observability.
6. GPU/resource exposure when accelerators are required.
7. Namespace, quota and policy model.

## GPU enablement chain

A physical GPU is not schedulable until the platform exposes it as a Kubernetes resource.

Typical chain:

`hardware -> feature discovery -> kernel/driver management -> GPU operator/runtime -> device plugin -> nvidia.com/gpu or equivalent -> scheduler -> RHOAI hardware profile/workload`

Architecture must distinguish failures in the hardware/driver/device-plugin chain from failures in RHOAI itself.

## Operator model

RHOAI follows the Kubernetes Operator reconciliation model. Desired state is expressed through custom resources and continuously reconciled.

Operational rule: **change the supported declarative source of truth, not a generated Deployment, unless product documentation explicitly instructs otherwise.**

## DataScienceCluster / installation control

The central architecture decision is which capabilities are activated, managed externally or omitted. Do not enable every component merely because it exists.

Expected capability areas:

- dashboard / workbenches;
- AI pipelines;
- model registry;
- KServe/model serving;
- TrustyAI/governance components;
- Ray / distributed compute;
- training operator/runtime;
- queue/admission integration such as Kueue, depending on supported architecture.

Exact APIs, versions and `managementState` options must be checked against the target RHOAI release.

## Namespace and tenancy model

Separate at least:

- system/operator namespaces;
- shared AI platform services;
- product/data-science projects;
- production model-serving namespaces where stricter controls apply.

A Data Science Project is simultaneously a collaboration boundary, quota boundary, RBAC boundary, storage boundary and blast-radius boundary.

Avoid a single global namespace for all AI teams.

## Workbench architecture

Golden-path decisions include:

- approved images and Python/CUDA stacks;
- CPU/GPU hardware profiles;
- PVC workspace sizing;
- S3/object-store connections;
- package repository policy;
- internet/egress policy;
- secret injection model;
- idle shutdown and cost controls.

## AI Pipelines

Treat pipelines as reproducible orchestration, not as the system of record for governance. Separate responsibilities:

- pipeline engine: workflow orchestration;
- experiment tracking: runs/metrics;
- object storage: artifacts;
- model registry: approved/versioned model metadata;
- queue/admission: capacity arbitration;
- Git: declarative configuration and review.

## Model serving

Serving architecture should define:

- KServe deployment mode/runtime choice;
- model artifact source;
- authentication and network path;
- GPU requests and replica strategy;
- TTFT / token throughput / queue metrics;
- canary/rollback pattern;
- autoscaling only after a stable measured baseline.

## Distributed training

If training is required, define separately:

- supported trainer/operator APIs;
- Ray/KubeRay usage;
- queue/admission and quota model;
- GPU topology and collective communication;
- checkpoint persistence to object storage;
- preemption/restart semantics;
- Technology Preview vs GA status.

## Security

RHOAI security depends on OpenShift controls plus AI-specific governance:

- OIDC/RBAC and project isolation;
- SCC/pod security constraints;
- NetworkPolicy and egress controls;
- secret manager integration;
- approved workbench/runtime images;
- model and dataset provenance;
- supply-chain controls;
- audit and telemetry minimization.

## Required evidence before `VERIFIED`

- Operator and DataScienceCluster state capture;
- project/namespace RBAC and quota evidence;
- workbench or equivalent workload running;
- storage and object-store connectivity evidence;
- serving/training evidence for the activated capability;
- failure/recovery evidence;
- explicit version/support matrix.