# I11/O5 — Azure / ARO industrialization master backlog

## Role of this document

This is the **master architecture backlog** for industrializing the Azure/ARO execution path of the Maya AI Agentic Architecture program.

Repository responsibilities are intentionally separated:

- `zdmooc/maya-ai-agentic-architecture-reference` = architecture reference, roadmap, decisions, backlog and graduation criteria;
- `zdmooc/TradeOps-GenAI-Integration` = executable runtime, Terraform/ARO helpers, GitHub Actions, GitOps manifests, tests and live evidence;
- `zdmooc/mayabank-azure-cloud-ai-platform` = reusable Azure architecture reference only (Landing Zone, Entra/RBAC, networking, observability, FinOps patterns). It is **not** the master backlog for this program.

Industrialization does not change the I11 target architecture. It turns the already-defined Terraform + ARO + OpenShift GitOps design into a reproducible enterprise lifecycle before the first paid Azure deployment.

## Current verified baseline — 2026-09-12

Observed on the target Azure subscription:

- subscription enabled;
- target region: `francecentral`;
- Azure CLI observed locally: `2.62.0` and must be upgraded before managed-identity ARO creation;
- `Microsoft.RedHatOpenShift`: `NotRegistered`;
- ARO versions observed in France Central: `4.18.26`, `4.18.34`, `4.19.20`, `4.19.24`, `4.20.15`, `4.21.22`;
- selected current lab baseline: **ARO 4.20.15** with **RHOAI 3.4**;
- regional vCPU quota observed: **10**;
- `Standard DSv5 Family vCPUs` quota observed: **0**;
- no paid ARO resource has been created yet.

## Sizing baseline

First graduation lab target:

| Component | Count | SKU | Per node | Aggregate |
|---|---:|---|---|---|
| ARO control plane | 3 | `Standard_D8s_v5` | 8 vCPU / 32 GiB | 24 vCPU / 96 GiB |
| ARO workers | 3 | `Standard_D8s_v5` | 8 vCPU / 32 GiB | 24 vCPU / 96 GiB |
| Total steady-state nodes | 6 | D8s_v5 | — | **48 vCPU / 192 GiB** |

Quota target for the first lab:

- regional vCPU quota: **>= 64** in France Central;
- DSv5 family quota: **>= 64** in France Central;
- final creation remains blocked until the live ARO validation/preflight succeeds.

The quota target deliberately leaves headroom instead of sizing exactly to the steady-state 48 vCPU footprint.

## Cost baseline and FinOps rules

The current planning snapshot for the 3+3 D8s_v5 ARO topology is approximately **USD 3.714/hour for ARO node compute + worker OpenShift fees**, before managed disks, networking, public/private endpoints, Log Analytics, Azure Monitor, Key Vault, Terraform state storage, backup/snapshots and data transfer.

Indicative node subtotal only:

| Runtime | Approximate subtotal |
|---:|---:|
| 4 h | USD 14.86 |
| 6 h | USD 22.28 |
| 8 h | USD 29.71 |
| 12 h | USD 44.57 |
| 24 h | USD 89.14 |

Rules:

1. Pricing must be refreshed immediately before every paid run; this snapshot is not contractual.
2. Personal learning budget objective remains **EUR 50/month maximum**.
3. First paid ARO lab hard runtime target is **<= 8 hours**.
4. The go/no-go estimate must include compute, ARO fees, disks, network, monitoring/logging, private endpoints/DNS, Key Vault, Terraform state and any optional AI resources.
5. Estimated cost and measured Azure Cost Management `ActualCost` must remain separate evidence classes.
6. An `expiry`/TTL must be fixed before CREATE.
7. The destroy path must be operational before the create path is authorized.
8. No paid resource is created automatically on a simple push to `main`.

## Target delivery architecture

```text
GitHub
  |
  +--> GitHub Actions CI
  |      tests / security / SBOM / lint / terraform validate
  |
  +--> Azure lifecycle workflow
         |
         +--> GitHub OIDC -> Azure
         +--> provider/version/quota preflight
         +--> refreshed sizing + cost estimate
         +--> terraform plan
         +--> protected approval
         +--> terraform apply foundation
         +--> ARO validate/create
         +--> OpenShift GitOps bootstrap
         +--> Argo CD reconciliation
         +--> RHOAI + TradeOps verification
         +--> FinOps/GreenOps evidence
         +--> controlled destroy / TTL safety net
```

Control-plane responsibilities:

- **GitHub Actions**: CI, lifecycle orchestration, approvals, evidence and scheduling;
- **Terraform**: Azure foundation, declarative Azure resources and IAM where supported;
- **Azure CLI / ARO API**: explicit ARO lifecycle helper until/unless the cluster lifecycle is deliberately moved into Terraform;
- **Argo CD / OpenShift GitOps**: OpenShift desired state reconciliation;
- **Helm/Kustomize/Operators**: OpenShift packaging and platform operators;
- **Ansible**: optional Day-2/runbook/external middleware automation only, not primary Azure IaC.

## Master backlog

| ID | Priority | Status | Capability | Definition of Done |
|---|---|---|---|---|
| AZ-01 | P0 | TODO | Upgrade Azure CLI | Supported CLI version captured in evidence and managed-identity ARO arguments available. |
| AZ-02 | P0 | TODO | Register required providers | Required Azure providers verified `Registered`. |
| AZ-03 | P0 | BLOCKED_QUOTA | Raise France Central quotas | Regional + DSv5 quotas meet target and live ARO validation succeeds. |
| AZ-04 | P0 | TODO | Freeze ARO/RHOAI compatibility | Region availability and RHOAI support matrix rechecked immediately before paid deployment. |
| AZ-05 | P0 | TODO | Terraform remote state | Azure Storage backend/bootstrap documented; local state is not authoritative for lifecycle automation. |
| AZ-06 | P0 | TODO | GitHub OIDC federation | GitHub Actions authenticates to Azure without a long-lived client secret. |
| AZ-07 | P0 | TODO | IAM / Entra / RBAC | Deployment identity and workload identities are least-privilege, scoped and evidenced. |
| AZ-08 | P0 | TODO | FinOps policy-as-code | Mandatory tags, `expiry`, budget/alerts, log-retention constraints and SKU guardrails exist. |
| AZ-09 | P0 | TODO | Sizing + pricing gate | Timestamped region/SKU/quota/runtime/all-in estimate produced before paid apply. |
| AZ-10 | P0 | TODO | CREATE workflow | Manual `workflow_dispatch`, preflight, plan, approval, foundation apply, ARO create and evidence capture. |
| AZ-11 | P0 | TODO | ARO lifecycle contract | Managed identity, selected visibility profile and fail-closed paid/public gates retained. |
| AZ-12 | P0 | TODO | OpenShift GitOps bootstrap | Argo CD/OpenShift GitOps installed/validated and Git becomes the desired-state source. |
| AZ-13 | P0 | TODO | RHOAI deployment | Supported RHOAI installation and serving path validated on the live cluster. |
| AZ-14 | P0 | TODO | Runtime verification | Node sizing, namespaces, GitOps sync, identity, monitoring and application probes captured. |
| AZ-15 | P0 | TODO | FinOps/GreenOps evidence | Resource inventory, Cost Management and provider carbon availability/result captured without fabricated claims. |
| AZ-16 | P0 | TODO | DESTROY workflow | Evidence first, delete ARO, verify absence, Terraform destroy foundation, verify residual resources. |
| AZ-17 | P0 | TODO | TTL / auto-destroy | Scheduled safety net detects expiry and triggers/forces the controlled cleanup path. |
| AZ-18 | P0 | TODO | Destroy verification | No billable lab resources remain; soft-deleted/purge-protected resources documented separately. |
| AZ-19 | P1 | TODO | Estimate vs actual report | Provider `ActualCost` compared with pre-run estimate and variance explained. |
| AZ-20 | P1 | TODO | Rightsizing | CPU/RAM/usage evidence compared with D8s_v5 baseline and alternative sizing documented. |
| AZ-21 | P1 | TODO | Environment promotion model | lab/dev/preprod/prod GitOps promotion and approvals designed without requiring four paid environments. |
| AZ-22 | P2 | DEFERRED | Ansible Day-2 | Added only for operations not better governed by Terraform, Operators or GitOps. |

## CREATE Definition of Done

A paid CREATE is authorized only when all of the following are true:

1. supported Azure CLI;
2. providers registered;
3. quotas sufficient;
4. selected ARO version offered in region and compatible with selected RHOAI;
5. GitHub OIDC working;
6. Terraform remote state working;
7. Terraform plan retained/reviewed;
8. refreshed all-in cost estimate within budget with margin;
9. CREATE and DESTROY workflows present and tested in non-paid/dry-run paths;
10. TTL/hard-stop declared;
11. explicit human approval for the paid run.

## DESTROY Definition of Done

The destroy sequence must be idempotent and converge toward zero billable lab resources:

```text
capture inventory/cost window
  -> delete ARO
  -> verify ARO absent
  -> terraform plan -destroy
  -> protected approval
  -> apply destroy plan
  -> verify resource group/residual resources
  -> record final cost / residual soft-delete state
```

## Evidence ownership

Architecture/backlog decisions are retained here. Executable proof belongs in `zdmooc/TradeOps-GenAI-Integration`, including:

- Terraform and ARO lifecycle implementation;
- GitHub Actions workflows;
- GitOps manifests;
- RHOAI deployment contracts;
- test results;
- Azure provider/quota/preflight outputs;
- Cost Management/GreenOps evidence;
- create/destroy transcripts.

The master roadmap is satisfied only by real retained evidence from the runtime repository; documentation alone does not upgrade `OPENSHIFT_AZURE_DEPLOYMENT` or `RESILIENCE_FINOPS_GREENOPS_VERIFIED` to complete.