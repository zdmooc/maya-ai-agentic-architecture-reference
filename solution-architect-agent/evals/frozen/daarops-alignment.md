# DAAROPS — Architecte / Platform Engineer Kubernetes & Go — Mission Alignment

Date: 2026-10-07  
Status: **DAAROPS_RECRUITER_CONTACT_RECEIVED / PORTFOLIO_READY / I6A-I6C CLOSED / OPERATOR_FIRST_ENRICHMENT_PLANNED / NEXT_STEP_PENDING**

## Mission target

Target positioning:

**Architecte Technique OpenShift / Platform Engineer — Kubernetes, GitOps, Operators & Day-2**

The mission signal is centered on:
- Kubernetes / OpenShift platform services;
- self-service / Platform Engineering;
- Go Operators, controllers and CRDs;
- Kubebuilder / Operator SDK;
- Argo CD / GitOps;
- security, scalability and Day-2;
- enterprise / banking / finance context;
- multi-cloud awareness.

## Recruiter signal — Operator-first focus

The 2026-10-07 phone exchange with Samir sharpened the mission reading: **Kubernetes Operators are the strongest technical focus to prepare for the next exchange**.

This does not reopen I6A/I6B/I6C. It adds a bounded four-iteration enrichment lane:

| Iteration | Objective | Primary repository | Supporting repositories |
|---|---|---|---|
| **OP1** | CRD/Reconcile/idempotence/SSA/Conditions/Events/retry/leader-election interview hardening | `shared-platform-services-openshift` | none required |
| **OP2** | OLM install/upgrade/uninstall replay directly on OpenShift Local/CRC | `shared-platform-services-openshift` | `openshift-platform-blueprints` if needed |
| **OP3** | Operator + Argo CD + Day-2 integrated proof with real consumer #1 | `shared-platform-services-openshift` | `argocd-expert-pack`, `mayabank-instant-payments-resilience-platform` |
| **OP4** | Operator-first 12–15 minute recruiter demo/evidence pack | `shared-platform-services-openshift` + `cadrage_202682030` | evidence reuse |

Direct mission repository: **`zdmooc/shared-platform-services-openshift`**.

Explicit non-prerequisites: **TradeOps, LiteLLM, Ollama, LLM, RAG, IBM ODM and MCP-R5/IBM MQ**. TradeOps consumer #2 remains a separate D-093 program lane and must not block DAAROPS preparation.

## Fit matrix

| Mission requirement | Evidence | Status |
|---|---|---|
| Kubernetes / OpenShift | BPCE modernization + CRC/OpenShift portfolio runtime | STRONG |
| Platform Engineering | Shared Platform + CapabilityConsumption Golden Path | STRONG |
| Go Operator / controller-runtime | real reconciler in `shared-platform-services-openshift` | DEMONSTRABLE PERSONAL PORTFOLIO |
| CRD / Kubebuilder | `CapabilityConsumption` v1alpha1, controller-gen, envtest | DEMONSTRABLE PERSONAL PORTFOLIO |
| GitOps / Argo CD | D-093 K1 drift/self-heal/prune/rollback on CRC | RUNTIME PROVEN |
| Day-2 / failure engineering | I6B retry/backoff, Degraded, leader failover, recovery | KIND RUNTIME PROVEN |
| OLM packaging | I6C bundles/FBC/install-upgrade-uninstall lifecycle | KIND OLM RUNTIME PROVEN |
| OpenShift runtime | I5 consumer #1 on CRC 4.22.7, SCC restricted-v2 | CRC RUNTIME PROVEN |
| Security | RBAC/SCC/NetworkPolicy/OIDC/TLS/Secrets | STRONG |
| Observability | Prometheus/Grafana/Loki/OpenTelemetry/Dynatrace | STRONG |
| Large enterprise / bank | BPCE/Natixis banking & payments | STRONG |
| Multi-cloud | Azure/AWS experience + AKS architecture path | PARTIAL RUNTIME / STRONG ARCHITECTURE |
| Open source | public GitHub portfolio | PUBLIC PORTFOLIO, NOT UPSTREAM CONTRIBUTOR CLAIM |

## Core demonstrable repository

`zdmooc/shared-platform-services-openshift`

Architecture:

```text
Git desired intent
      |
      v
CapabilityConsumption CRD
      |
      v
Go/controller-runtime Operator
      |
      +--> Observe / conflict detection
      +--> explicit Manage
      +--> Server-Side Apply
      +--> Namespace / SA / RBAC
      +--> ResourceQuota / LimitRange
      +--> NetworkPolicy
      |
      +--> Conditions / Events / Metrics
      +--> retry/backoff / Degraded
      +--> leader election / failover
      |
      v
Product workloads remain product-owned and Argo CD reconciled
```

## Evidence ladder

### I4 / Kind Operator baseline
- Go/controller-runtime;
- CRD;
- Manage;
- Server-Side Apply;
- drift recovery;
- restart recovery;
- Observe/OwnershipConflict;
- explicit adoption;
- Retain.

Claim: `KIND_RUNTIME_PROVEN_PLATFORM_OPERATOR`.

### I5 / OpenShift consumer #1
Observed on OpenShift Local / CRC 4.22.7:
- SCC `restricted-v2`;
- Observe -> Manage;
- ResourceQuota / LimitRange / RBAC / NetworkPolicies;
- zero double ownership;
- Argo CD Synced/Healthy;
- Shared OIDC + Shared OTel;
- payment non-regression.

Claim: `CONSUMER_1_CRC_RUNTIME_PROVEN`.

### I6A / production-style engineering
- controller-gen;
- CRD validation;
- Progressing/Degraded;
- Prometheus reconciliation metrics;
- Lease leader election;
- partial failure recovery envtest.

Claim: `PLATFORM_CI_PROVEN + KIND_RUNTIME_PROVEN_I6A`.

### I6B / Day-2 failure engineering
- root error propagated to controller-runtime;
- automatic retry/backoff;
- transient RBAC apply failure;
- automatic convergence without CR mutation;
- bounded failure metrics;
- leader loss and Lease failover;
- post-failover resource reconstruction.

Claim: `PLATFORM_CI_PROVEN + KIND_RUNTIME_PROVEN_I6B_DAY2`.

### I6C / OLM
Final combined claim:
`KIND_OLM_LIFECYCLE_PROVEN + OPENSHIFT_OPERATOR_RUNTIME_PROVEN_CONSUMER_1`.

Do **not** claim `OPENSHIFT_OLM_LIFECYCLE_PROVEN` until the exact OLM installation/upgrade/uninstall is replayed on CRC/OpenShift.

## Truth boundary for CV/interview

Use:
> Go/Kubebuilder/controller-runtime: personal technical portfolio, executable and demonstrable in public GitHub.

Do not use:
> X years of professional Go Operator development.

The commercial value is the ability to explain and demonstrate the architecture, controller semantics, ownership model, failure modes, GitOps integration and evidence—not to manufacture client history.

## Recommendation

**GO / APPLY.**

The DAAROPS technical and commercial portfolio gates are closed. Exact OpenShift OLM replay remains an optional evidence enhancement, not a blocker for the application pack.


## Application status and follow-up

- **2026-10-07** — Collective application submitted and confirmation observed.
- Status: `RECRUITER_PHONE_CONTACT_RECEIVED / NEXT_STEP_PENDING`.
- **2026-10-07** — phone contact received from **Samir** after the Collective submission.
- Follow-up reference: https://www.linkedin.com/posts/samir-bouadi_kubernetes-golang-openshift-share-7511006775635013632-XcNl/?utm_source=chatgpt.com
- The recruiter exchange should continue to reference the public `shared-platform-services-openshift` proof and the targeted positioning **Architecte Technique OpenShift / Platform Engineer**.
- No duplicate application; record the next commercial/technical step only when explicitly confirmed.
