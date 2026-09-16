# AI Platform HA / DR / Multi-Cluster Architecture

Status: **DESIGNED — REFERENCE / NO MULTI-SITE FAILOVER CLAIM**

## Purpose

Deepen resilience for AI platforms beyond generic Kubernetes HA. AI recovery must account for models, object storage, vector indexes, metadata databases, Kafka/event state, agent state, secrets, registries, GPU capacity and model warm-up.

## Distinguish three problems

- **HA**: survive local pod/node/component failures without changing site.
- **DR/PRA**: recover from loss of a cluster/site/failure domain.
- **Backup/restore**: recover from deletion, corruption or logical error.

Do not use one mechanism as a substitute for the other two.

## State inventory first

Before designing failover, classify every stateful asset:

| State | Preferred treatment |
|---|---|
| Git/IaC/policies | external source of truth, replicated/backed up |
| Container/model artifacts | immutable registry/object storage, replicated |
| RAG source corpus | versioned object storage |
| Vector indexes | snapshot/replication or deterministic rebuild |
| Metadata DB | replication + PITR + restore test |
| Agent/checkpoint state | durable DB/store with replication/backup |
| Kafka/events/offsets | replication/mirroring + replay strategy |
| Secrets/keys | external secret/KMS/HSM continuity plan |
| OpenShift/RHOAI manifests | GitOps reconstruction |

The first PRA deliverable is this state inventory plus RPO/RTO, not a network diagram.

## Multi-cluster topology

A production reference should decide:

- number and independence of OpenShift clusters;
- hub/management continuity;
- GitOps source availability;
- identity/PKI/KMS dependency placement;
- registry/object-storage replication;
- DNS/GSLB/load-balancer failover;
- GPU standby capacity;
- data replication mode;
- split-brain prevention.

## RPO / RTO by service

Define targets independently. Example classes:

- stateless APIs/agents/tool gateways: reconstruct via GitOps, low RTO;
- model serving: immutable model RPO 0, but warm-up/GPU availability drives RTO;
- corpus/object storage: replication/backup drives RPO;
- vector index: snapshot or rebuild may justify a larger RPO/RTO;
- transactional metadata/agent state: tighter DB RPO/RTO;
- Kafka: event and offset protection tied to replay semantics.

## Model-serving DR

A standby cluster is not ready merely because manifests exist. Validate:

- model artifact is present/accessible;
- compatible serving runtime exists;
- GPU capacity is actually allocatable;
- runtime can load within RTO;
- warm-up succeeds;
- synthetic inference passes before traffic is shifted.

## RAG DR

Recover in dependency order:

`governed corpus -> metadata/ACL -> embedding model/version -> index snapshot or rebuild -> retrieval validation -> generation validation`

Vector index recovery must preserve source/version/ACL lineage. If rebuild is the strategy, measure rebuild RTO at representative corpus size.

## Event-driven and agent state

For Kafka/EDA and long-running agent workflows:

- preserve event identity and deduplication;
- define offset/mirror semantics;
- avoid duplicate side effects after failover;
- persist checkpoints outside ephemeral pods;
- validate idempotency during replay;
- gate sensitive resume actions through deterministic policy/HITL.

## Split-brain control

Failover is not DNS redirection. Before enabling writes at Site B, prove Site A cannot continue writing to the same authoritative states or execute the same side effects.

Use explicit fencing, ownership/lease mechanisms or operational controls appropriate to each data service.

## GitOps and site independence

Anything reconstructable should be outside the failed site:

- Git;
- container/model registry;
- policies;
- immutable release manifests;
- secret roots/secret manager;
- externalized configuration.

Both sites should be able to converge on the same approved release digest.

## Backup tooling and storage DR

Platform mechanisms such as OADP/Velero-style backup, ODF/storage replication, snapshots or cloud-native DR may be used where supported, but version/support matrices must be validated for the target platform release.

Do not infer application consistency from a successful volume snapshot alone.

## Failover runbook order

1. Declare incident and freeze unsafe writes.
2. Fence/confirm loss of primary authority.
3. Validate identity, secrets, registry and data dependencies at recovery site.
4. Restore/activate stateful services.
5. Reconcile OpenShift/RHOAI via GitOps.
6. Validate GPU/model-serving readiness.
7. Validate RAG/index consistency.
8. Resume Kafka/agent workflows with idempotency controls.
9. Execute end-to-end synthetic checks.
10. Shift traffic.
11. Measure actual RPO/RTO and collect evidence.

Failback requires its own tested procedure.

## Required evidence before `VERIFIED`

- explicit state inventory and RPO/RTO matrix;
- two-site/cluster configuration evidence or equivalent lab;
- backup/restore proof;
- index restore/rebuild proof;
- model warm-up timing;
- event/agent replay without duplicate side effect;
- failover and failback timestamps;
- split-brain/fencing evidence.