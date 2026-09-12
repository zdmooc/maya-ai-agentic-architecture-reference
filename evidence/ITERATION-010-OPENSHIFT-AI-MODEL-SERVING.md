# Iteration 010 — OpenShift AI model serving

## Status

**IMPLEMENTED + TESTED IN CI / LIVE RHOAI DEPLOYMENT AND MEASURED PERFORMANCE PENDING**

Iteration 10 adds the governed model-serving layer for the TradeOps reference architecture. The implementation targets Red Hat OpenShift AI 3.4 and keeps deployment evidence distinct from manifest/CI evidence.

Runtime repository: `zdmooc/TradeOps-GenAI-Integration`

Runtime commit / I10 HEAD:

`316a6a0f1cf09b35b4594d8f2061f206ee31f45c`

Parent I9 HEAD:

`92e0718640e8a19f61df671c14a74e163a5af445`

Runtime delta from I9: one commit ahead, zero behind, 24 changed files.

## Architecture decision

I10 separates two serving classes:

1. **Signal-quality ML serving** — CPU-first custom runtime for the I5 calibrated classifier contract.
2. **LLM serving** — GPU-oriented KServe/vLLM reference using the platform-provided `vllm-runtime`.

The repository does not build a second unmanaged vLLM stack and does not deploy a parallel hand-built MLflow control plane. The target lifecycle uses the OpenShift AI managed MLflow operator and Kubernetes project/RBAC integration.

## Signal-quality online contract

I10 introduces `services/model_serving/` with:

- `SignalQualityServingService`;
- canonical I5 feature-order enforcement;
- rejection of missing or extra features;
- rejection of NaN/infinite feature values;
- validation of `predict_proba` output shape and bounds;
- qualification metadata returned with every prediction;
- explicit LAB versus PRODUCTION serving modes.

The online request uses exactly the existing I5 feature contract:

- RSI;
- MACD histogram;
- ATR percentage;
- ADX;
- EMA slope;
- VWAP distance percentage;
- volatility percentage;
- volume z-score;
- structure score;
- pattern score;
- relative strength;
- session code;
- distance to level in ATR units;
- regime code;
- spread in basis points;
- latency in milliseconds;
- data-quality score.

## Production-qualification guard

I10 intentionally refuses to turn the I5 synthetic calibration into a production probability claim.

`MODEL_SERVING_MODE=PRODUCTION` is accepted only with:

`MODEL_QUALIFICATION=CALIBRATED_OUT_OF_SAMPLE_REAL_MARKET`

The existing I5 status `CALIBRATED_OUT_OF_SAMPLE_SYNTHETIC` therefore remains lab-only.

This is a fail-closed control rather than a documentation convention.

## Serving API

The model-serving FastAPI surface exposes:

- `GET /health/live`;
- `GET /health/ready`;
- `POST /v1/models/{model_name}:predict`;
- `GET /metrics`.

The readiness endpoint becomes successful only after the model is loaded. Unknown model names fail with HTTP 404; invalid feature contracts fail with HTTP 422; absent/unloadable model state fails readiness and serving availability.

Prometheus metrics include:

- `tradeops_model_requests_total{status}`;
- `tradeops_model_request_seconds`.

## OpenShift AI resources

I10 versions the RHOAI target in `infra/openshift-ai/VERSION` and adds:

- `tradeops-ai` namespace;
- service account `tradeops-model-serving`;
- namespaced RoleBinding to `mlflow-operator-mlflow-integration`;
- OpenShift `ImageStream` and binary `BuildConfig` for `tradeops-ai-runtime:i10`;
- custom KServe `ServingRuntime` for the TradeOps signal-quality service;
- KServe `InferenceService` `tradeops-signal-quality`;
- monitoring `PrometheusRule`;
- Kustomize composition.

The `InferenceService` is configured with:

- RawDeployment mode;
- `minReplicas: 2`;
- `maxReplicas: 4`;
- explicit CPU/memory requests and limits;
- explicit service-account identity;
- model URI and qualification supplied through a runtime Secret, not committed to Git;
- MLflow Kubernetes namespaced integration environment settings.

## MLflow lifecycle

The target lifecycle is:

1. train/evaluate using the point-in-time I5 feature contract;
2. log experiment evidence;
3. register/version the model in MLflow;
4. attach qualification metadata;
5. select an explicit model URI;
6. inject the model URI and qualification as runtime Secret values;
7. load through the MLflow SDK;
8. become Ready only after successful load;
9. serve predictions through KServe;
10. collect request/error/latency evidence.

No production MLflow workspace or production model version is claimed by CI.

## vLLM reference

`infra/openshift-ai/examples/inferenceservice-vllm.yaml` provides a deliberately non-executable-until-configured reference for LLM serving:

- KServe `InferenceService`;
- runtime `vllm-runtime`;
- model format `vLLM`;
- two-replica HA floor and four-replica ceiling;
- one NVIDIA GPU request/limit per replica;
- explicit memory/CPU resources;
- `--max-model-len=4096`;
- `--gpu-memory-utilization=0.90`;
- intentional `s3://REPLACE-ME/...` storage placeholder.

The placeholder prevents the repository from pretending that an approved production LLM and storage path already exist.

## SLO contract

The initial Prometheus rules define engineering targets, not measured achievements:

- serving-unavailable responses trigger a critical alert;
- error ratio above 1 percent over ten minutes triggers a warning;
- p95 latency above 250 ms over ten minutes triggers a warning.

These thresholds remain provisional until target-cluster load tests provide empirical baselines.

## Capacity model

`scripts/i10_capacity_plan.py` estimates an initial replica count from:

- peak requests/second;
- measured p95 service time;
- safe concurrency per replica;
- target utilization.

It applies a two-replica minimum and emits:

`status=CAPACITY_ESTIMATE_NOT_BENCHMARK_EVIDENCE`

The calculator is a planning aid, not benchmark evidence.

## Operational scripts

I10 adds:

- `scripts/i10_rhoai_preflight.sh` — verifies login, DataScienceCluster, KServe CRDs, KServe managed state, MLflow Operator managed state and MLflow integration RBAC;
- `scripts/i10_rhoai_deploy.sh` — creates namespace/RBAC/build resources, creates the model-serving Secret from local environment values, builds the runtime image and applies the ServingRuntime, InferenceService and SLO rules;
- `scripts/i10_rhoai_verify.sh` — waits for InferenceService Ready, checks serving/monitoring/RBAC objects and prints the resolved inference URL;
- `scripts/i10_capacity_plan.py` — initial deterministic capacity estimator;
- `scripts/i10_validate_ai_serving.py` — CI contract validator for I10 manifests and policy assumptions.

## CI evidence

GitHub Actions run:

`34681817517`

Job:

`103521706237`

Commit:

`316a6a0f1cf09b35b4594d8f2061f206ee31f45c`

Result: **SUCCESS**.

Verified gates:

- CPython 3.11.16 dependency installation: PASS;
- Ruff: `All checks passed!`;
- security audit: `SECURITY_AUDIT_PASS`;
- SBOM consistency: `SBOM_CHECK_PASS`;
- I9 Helm lint: PASS, one chart linted / zero failed;
- I9 Helm render: PASS;
- I9 platform validator: `I9_PLATFORM_VALIDATION_PASS`;
- I10 serving validator: `I10_AI_SERVING_VALIDATION_PASS`;
- full Pytest: **184 passed, 69 warnings in 13.26s**.

I9 ended at 167 tests. I10 therefore adds **17 passing tests**.

The 69 warnings are the existing Starlette/FastAPI and I5 sklearn/scipy deprecation warnings; no I10 functional failure occurred.

## I10 tests

I10 adds tests for:

- canonical online feature ordering;
- missing feature rejection;
- extra feature rejection;
- non-finite feature rejection;
- PRODUCTION rejection of synthetic qualification;
- acceptance of explicit real-market qualification;
- health/readiness and predict API;
- unknown-model rejection;
- Prometheus metrics exposure;
- versioned RHOAI target;
- KServe HA and bounded scaling contract;
- MLflow Kubernetes integration contract;
- vLLM GPU/reference configuration;
- two-replica capacity floor;
- deterministic capacity scaling;
- invalid-capacity-input rejection;
- operational-script presence.

## What CI proves

CI evidence proves that:

- the custom signal-quality serving code executes under tests;
- feature-contract and qualification gates fail closed;
- the API contract and metrics are executable;
- I10 manifests contain the expected KServe, MLflow RBAC, HA, resources, probes, SLO and vLLM contracts;
- I0-I9 regression tests remain green.

## Explicit non-claims

I10 does **not** claim:

- that RHOAI 3.4 has been installed or executed on the user's local CRC cluster;
- that the custom ServingRuntime or InferenceService has reached Ready on a live cluster;
- that a real RHOAI MLflow workspace/model version has been created;
- that the vLLM example has loaded a real LLM;
- any measured GPU throughput, token/s, cold-start, warm-start, p50/p95/p99 latency or saturation;
- node-level HA, anti-affinity, GPU failover or storage DR validation;
- that the I5 synthetic model is a real-market calibrated probability model;
- automated real-money execution or live IG order routing;
- I11 Azure/ARO implementation.

## Exit state

I10 is **implemented and CI-tested**, but its original graduation condition requires measured deployment evidence. Therefore the accurate status remains:

**IMPLEMENTED + TESTED IN CI / LIVE RHOAI DEPLOYMENT AND MEASURED PERFORMANCE PENDING**

The next live evidence step is to execute the versioned preflight/deploy/verify flow on an eligible RHOAI cluster and capture model load time, cold/warm p50/p95/p99 latency, throughput, resource saturation and replica-failure recovery.
