# Iteration 011 — Azure / ARO Enterprise Target Evidence

Status: **IMPLEMENTED + TESTED IN CI / LIVE AZURE-ARO DEPLOYMENT PENDING**

## Scope

Iteration 11 transposes the executable TradeOps/OpenShift architecture into an enterprise Azure target while preserving the deterministic, ML, agentic, risk and HITL contracts established by I1-I10.

The target is deliberately **ARO-first**, not AKS-first:

- Azure Red Hat OpenShift remains the container platform target;
- the I9 GitOps/OpenShift contracts and I10 RHOAI/KServe contracts are preserved;
- Azure provides enterprise landing-zone, identity, networking, secret-management and observability integrations;
- Microsoft Foundry is optional and cannot replace deterministic risk or HITL controls by default.

## Reuse decision

Reviewed reference repository:

`zdmooc/mayabank-azure-cloud-ai-platform`

Reviewed reference commit:

`dfe3909dc6904ac502aac857eb55f8ac2a0d1309`

Reused concepts:

- Landing Zone and hub-spoke principles;
- Microsoft Entra ID, RBAC and privileged-access posture;
- managed/workload identity patterns;
- Key Vault and private endpoint patterns;
- Azure Monitor / OpenTelemetry integration;
- FinOps / GreenOps tagging and destroy discipline;
- Microsoft Foundry architectural guidance.

Adapted decision:

- this program keeps Azure Red Hat OpenShift as its Azure runtime target rather than moving the executable baseline to AKS;
- Kafka-compatible messaging semantics remain architecture contracts unless a separate functional decision replaces them;
- RHOAI/KServe remains the primary self-managed AI-serving path, with Microsoft Foundry available as an optional managed integration.

## Runtime implementation

### Azure architecture document

`docs/20-azure-aro-enterprise-target.md`

It documents:

- ARO-first enterprise topology;
- private API and private ingress target;
- managed identities and workload identity;
- Key Vault RBAC/private networking;
- Azure Monitor and Log Analytics;
- optional Microsoft Foundry integration;
- FinOps/GreenOps and DR posture;
- explicit non-claims.

### Terraform foundation

Directory:

`infra/azure-enterprise/terraform/`

Pinned toolchain:

- Terraform `1.16.2`;
- `hashicorp/azurerm` `5.2.0`.

Foundation resources:

- resource group;
- ARO VNet `10.60.0.0/16`;
- master subnet `10.60.0.0/23`;
- worker subnet `10.60.2.0/23`;
- shared/private-endpoint subnet `10.60.4.0/24`;
- user-assigned managed identity;
- Key Vault;
- Key Vault private endpoint and private DNS integration;
- Log Analytics workspace;
- Azure Monitor Workspace.

The default Terraform foundation intentionally does **not** create an ARO cluster or Microsoft Foundry resources. Those resources can carry significant cost/quota implications and are reserved for explicit labs.

### Identity and secrets

The target uses:

- ARO managed identity at cluster provisioning time;
- workload identity/federated identity for application access;
- Key Vault with Azure RBAC;
- `Key Vault Secrets User` as the application secret-read role;
- purge protection;
- public network access disabled;
- private endpoint + private DNS.

No static ARO client secret is stored or accepted by the versioned create helper.

### ARO operational helpers

`scripts/i11_aro_preflight.sh`

- verifies Azure CLI availability;
- validates required environment variables;
- verifies `Microsoft.RedHatOpenShift` provider registration;
- verifies requested ARO version availability in the selected Azure region;
- executes `az aro validate` using managed identity mode.

`scripts/i11_aro_create.sh`

- executes explicit ARO creation only when the operator chooses to do so;
- uses `--enable-mi true`;
- uses private API visibility;
- uses private ingress visibility;
- accepts version/network/subnets from environment;
- does not use a static client secret.

`scripts/i11_aro_destroy.sh`

- provides explicit cluster deletion;
- warns that shared foundation resources and identities require separate review.

### Observability

The Azure target preserves the I8 OpenTelemetry contract and adds the Azure foundation for:

- Log Analytics;
- Azure Monitor Workspace;
- managed Prometheus / ARO monitoring integration when enabled;
- unchanged correlation and trace-context semantics across environments.

### Microsoft Foundry

Microsoft Foundry is documented as an optional managed AI integration for selected models, agents and tools.

It is not automatically provisioned by the default I11 Terraform foundation and is not allowed to bypass:

- deterministic I3 risk;
- I7 HITL;
- governed I6 tool access;
- I5/I10 model-qualification rules.

### FinOps / GreenOps

Required/versioned tagging includes:

- workload;
- environment;
- cost center;
- data classification;
- managed-by;
- architecture stage.

The default lab limits automatic IaC to foundation resources. Expensive ARO/Foundry labs require explicit creation and explicit teardown.

## CI changes

I11 extends the existing CI with:

- `hashicorp/setup-terraform@v3`;
- Terraform `1.16.2`;
- `terraform fmt -check -recursive`;
- `terraform init -backend=false -input=false`;
- `terraform validate -no-color`;
- `scripts/i11_validate_azure_target.py`;
- twelve new platform tests.

Existing I8/I9/I10 quality, security, SBOM, Helm and platform gates remain enabled.

## Runtime commit history

Functional commit:

`740422080621f6847e65b0fd1e8dad68f3fc0064`

AzureRM 5 schema correction:

`d0f13aad8d6d041cdaad2d39c13ae58b0fb97ae4`

Final Terraform-format correction / I11 runtime HEAD:

`9c5beab73074608be1c941540267ebb3826bfe4b`

Delta from I10:

- 3 commits ahead;
- 0 commits behind;
- 12 files changed.

## CI hardening history

### First I11 run

GitHub Actions run:

`34682484768`

Job:

`103523547953`

The run passed:

- Python/Terraform setup;
- dependency installation;
- Ruff;
- security audit;
- SBOM check;
- Helm lint/render;
- I9 validator;
- I10 validator;
- Terraform formatting;
- Terraform initialization with AzureRM 5.2.0.

`terraform validate` then correctly failed against the actual AzureRM 5.2.0 schema for `azurerm_private_dns_zone_virtual_network_link`:

- `private_dns_zone_id` was required;
- the previous `resource_group_name` and `private_dns_zone_name` arguments were no longer valid for that resource schema.

No provider version was downgraded and no validation gate was disabled. The configuration was corrected to the current provider schema.

### Second I11 run

GitHub Actions run:

`34682589327`

Job:

`103523838050`

The AzureRM schema correction was present, but `terraform fmt -check -recursive` rejected the changed block's noncanonical alignment. No formatting gate was disabled. The file was reformatted canonically.

### Final I11 run

GitHub Actions run:

`34682673257`

Job:

`103524074997`

Commit:

`9c5beab73074608be1c941540267ebb3826bfe4b`

Result: **SUCCESS**.

Verified gates:

- CPython 3.11.16 setup: PASS;
- Terraform 1.16.2 setup: PASS;
- dependency installation: PASS;
- Ruff: PASS;
- security audit: `SECURITY_AUDIT_PASS`;
- SBOM consistency: `SBOM_CHECK_PASS`;
- Helm lint/render: PASS;
- I9 platform validator: `I9_PLATFORM_VALIDATION_PASS`;
- I10 serving validator: `I10_AI_SERVING_VALIDATION_PASS`;
- Terraform formatting: PASS;
- Terraform initialization: PASS;
- signed `hashicorp/azurerm v5.2.0` installation: PASS;
- Terraform validation: `Success! The configuration is valid.`;
- I11 Azure target validator: `I11_AZURE_TARGET_VALIDATION_PASS`;
- full Pytest: **196 passed, 69 warnings in 15.08s**.

I10 ended at 184 tests, so I11 adds **12 passing tests**.

The 69 warnings are pre-existing Starlette/FastAPI and I5 sklearn/scipy deprecation warnings.

## What CI proves

CI proves that:

- the Terraform files are canonically formatted;
- Terraform can initialize the exact pinned AzureRM provider;
- the foundation configuration validates against the real AzureRM 5.2.0 schema;
- the Key Vault/network/identity/observability contracts are versioned and tested;
- the ARO create contract remains private and managed-identity based;
- static ARO client-secret usage is rejected by project tests/validator;
- I0-I10 regression tests remain green.

## Explicit non-claims

I11 does **not** claim:

- a Terraform apply against an Azure subscription;
- a running ARO cluster;
- live ARO managed-identity/workload-identity federation;
- live Key Vault secret access;
- validated enterprise DNS, firewall, VPN or ExpressRoute routing;
- Azure Monitor ingestion from a live ARO cluster;
- a Microsoft Foundry resource/project/model deployment;
- measured Azure cost or carbon results;
- measured multi-region RTO/RPO or DR failover;
- automated real-money execution or live IG order routing.

## Exit state

I11 status is:

**IMPLEMENTED + TESTED IN CI / LIVE AZURE-ARO DEPLOYMENT PENDING**

The next program iteration is I12 Excellence graduation. I12 must not convert any pending live-evidence item into a claim without actual evidence.
