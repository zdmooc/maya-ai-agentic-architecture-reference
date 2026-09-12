# Iteration 009 — OpenShift Local / CRC and GitOps

Status: **IMPLEMENTED + TESTED IN CI / LIVE CRC DEPLOYMENT PENDING**

## Scope

Iteration 9 packages the I8 target runtime for OpenShift Local / CRC, adds resource and network guardrails, replaces the minimal historical Helm chart, and provides an Argo CD / Kustomize / Helm GitOps path.

Runtime repository: `zdmooc/TradeOps-GenAI-Integration`

Baseline before I9:

- I8 final HEAD: `90976dd60a9b80272e39db07ed027ae500f947c1`.

I9 commits:

- functional commit: `80ee9297a299133a63c7326b34bddf33d588bab5` — `feat(i9): package OpenShift CRC runtime and GitOps guardrails`;
- final corrective commit / I9 HEAD: `92e0718640e8a19f61df671c14a74e163a5af445` — `fix(i9): remove unused platform test import`.

Final runtime delta from I8:

- 2 commits ahead;
- 0 commits behind;
- 35 files changed.

## Runtime packaging decision

The previous chart only packaged three APIs and still represented the early demonstration architecture. I9 replaces that with a single target runtime package.

The target application slice is:

1. `market-data`;
2. `workflow-api`;
3. `genai-api`;
4. `rag-api`;
5. `agent-controller`;
6. `mcp-server`;
7. `risk-engine`;
8. `paper-oms`;
9. `notifier`.

The old `signal-engine` is deliberately excluded from the target deployment because it still contains the pre-I2 demonstration signal rule and is not part of the accepted deterministic/ML/agentic architecture.

## Unified OpenShift runtime image

`Dockerfile.openshift` builds one application image used by the nine workloads with different Python module commands.

Reasons:

- avoids storing many almost-identical Python images in the constrained CRC VM;
- keeps dependency and SBOM management simpler;
- preserves one application artifact lineage for the local platform lab.

The image:

- uses Python 3.11;
- installs the pinned runtime requirements;
- adds pinned RAG dependencies `sentence-transformers==6.0.1` and `qdrant-client==1.19.0`;
- copies services, RAG corpus, knowledge-base material and schemas;
- does not fix a container UID;
- applies group-0 permissions using `chgrp -R 0 /app` and `chmod -R g=u /app` so OpenShift restricted security can assign an arbitrary UID.

The OpenShift BuildConfig publishes `tradeops-runtime:i9` to the namespace ImageStream.

## Helm target

`infra/helm/tradeops` is upgraded to chart version `0.9.0`.

The chart now declares:

- all nine target application workloads;
- explicit CPU/memory requests and limits;
- startup/readiness/liveness HTTP probes for API workloads;
- `RuntimeDefault` seccomp behavior;
- `allowPrivilegeEscalation: false`;
- Linux capability drop `ALL`;
- ServiceAccount token automount disabled;
- secret references rather than committed passwords;
- OpenShift Routes for `agent-controller`, `workflow-api` and Grafana.

The historical three per-service deployment templates were removed in favor of one generated application-workload template.

## Stateful and observability dependencies

The CRC-local chart includes:

- PostgreSQL 16 with a PVC and versioned initialization SQL for workflows, orders and audit logs;
- Redpanda with a PVC as the local Kafka-compatible event backbone;
- Qdrant with a PVC for the local RAG demonstrator;
- OpenTelemetry Collector;
- Prometheus;
- Grafana with a Prometheus datasource.

The platform containers also define explicit resource requests/limits and readiness checks where appropriate.

## Resource governance

I9 adds:

- namespace `tradeops` with restricted Pod Security labels;
- `ResourceQuota`;
- `LimitRange`;
- CRC-specific quota overrides;
- small CRC PVC defaults in `values-crc.yaml`.

The values are demonstrator limits, not production capacity numbers.

## NetworkPolicy

The namespace starts fail-closed with a default-deny ingress/egress policy.

Explicit policies then allow:

- intra-namespace communication;
- DNS egress to the OpenShift DNS namespace;
- ingress from the OpenShift router to the externally exposed services;
- TCP/443 egress for market-data and GenAI components which may require external market/provider endpoints.

Standard Kubernetes NetworkPolicy does not provide FQDN-level filtering, so I9 does not claim domain-specific egress policy.

## Kyverno policy-as-code

I9 deliberately uses the current CEL policy family:

- `apiVersion: policies.kyverno.io/v1`;
- `kind: ValidatingPolicy`.

Three policies are versioned:

1. require CPU/memory requests and limits;
2. reject `:latest` container tags;
3. require disabled privilege escalation and `ALL` capability drop.

No legacy `kyverno.io/v1` `ClusterPolicy` is introduced.

The direct CRC deployment script detects whether the `ValidatingPolicy` CRD exists. Policies are only applied when Kyverno is already installed; I9 does not silently install an operator or mutate the cluster platform lifecycle.

## GitOps

The old example repository placeholder is removed.

`gitops/argocd` now contains:

- `AppProject` `tradeops`;
- `tradeops-platform` Application for the CRC Kustomize overlay;
- `tradeops-kyverno-policies` Application for CEL policies;
- `tradeops-runtime` Application for the Helm chart.

All sources point to the real `zdmooc/TradeOps-GenAI-Integration` repository and explicitly use `targetRevision: main`.

Sync waves separate platform guardrails, Kyverno policy and application runtime ordering.

## Operational scripts

I9 adds:

- `scripts/i9_crc_preflight.sh` — verifies CRC, `oc`, Helm, user/session and node state;
- `scripts/i9_crc_deploy.sh` — applies guardrails, creates runtime secrets from local environment variables, starts the OpenShift build and deploys either directly with Helm or through Argo CD;
- `scripts/i9_crc_verify.sh` — checks workload rollouts, StatefulSets, quota/LimitRange/NetworkPolicy/Routes and the exposed agent health endpoint; it also fails if the legacy `signal-engine` is deployed;
- `scripts/i9_image_scan.sh` — Trivy HIGH/CRITICAL image gate for an externally reachable image reference.

## CI platform validation

The CI pipeline now runs, in order:

1. dependency installation;
2. Ruff;
3. secret audit;
4. SBOM consistency check;
5. Helm lint using the CRC values;
6. Helm template rendering;
7. `scripts/i9_validate_platform.py`;
8. the full Pytest suite.

The I9 validator checks the target workload list, legacy-signal exclusion, resource/probe/security contracts, NetworkPolicies, current Kyverno API, Argo CD repository/path configuration, unified-image pinning and arbitrary-UID permissions.

## CI history

First I9 run:

- GitHub Actions run: `34681157466`;
- job: `103519925799`;
- dependency installation: PASS;
- Ruff: FAIL on one unused `Path` import in the new I9 test file;
- later gates correctly did not run;
- no lint or quality rule was disabled.

Corrective commit:

- `92e0718640e8a19f61df671c14a74e163a5af445`;
- removes only the unused import.

Final I9 run:

- GitHub Actions run: `34681213356`;
- job: `103520072644`;
- CPython 3.11.16;
- Ruff: **PASS**;
- security audit: **SECURITY_AUDIT_PASS**;
- SBOM: **SBOM_CHECK_PASS**;
- Helm lint: **1 chart linted, 0 failed**;
- Helm render: **PASS**;
- I9 platform validator: **I9_PLATFORM_VALIDATION_PASS**;
- Pytest: **167 passed, 69 warnings in 16.83s**;
- job conclusion: **SUCCESS**.

I8 ended at 157 tests, therefore I9 adds 10 passing tests.

## What CI proves

CI evidence proves that:

- the Helm chart parses and renders;
- the platform contracts remain versioned;
- expected workloads and guardrails are present;
- Kyverno manifests use the chosen current policy API;
- the security/SBOM gates still pass;
- I0-I8 regression tests remain green.

## Explicit non-claims

I9 does **not** claim that the user's local CRC cluster has already executed the deployment.

The following remain deployment evidence to capture on the actual CRC host:

- OpenShift BuildConfig successfully building the unified image inside CRC;
- all external platform images pulling successfully;
- PVC binding and actual disk consumption;
- all twelve Deployments and three StatefulSets reaching Ready;
- OpenShift Routes becoming reachable;
- live health verification through the Route;
- real OpenTelemetry trace delivery in the CRC deployment;
- actual Argo CD sync status when GitOps mode is selected;
- actual Kyverno admission decisions when Kyverno is installed;
- Trivy scan result for the built runtime image.

I9 also does not claim:

- production-grade HA for PostgreSQL, Redpanda, Qdrant, Prometheus or Grafana;
- mTLS between all services;
- FQDN-level egress policy;
- automated real-money trading or live IG order routing;
- OpenShift AI / KServe / vLLM serving, which belongs to I10.

## Exit decision

Iteration 9 is accepted as:

**IMPLEMENTED + TESTED IN CI / LIVE CRC DEPLOYMENT PENDING**.

The code, manifests, operational scripts and CI guardrails are ready for the local CRC execution lab, but deployment verification is intentionally not fabricated.
