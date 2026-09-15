# AI Evaluation & Observability Tooling Options

Status: **DESIGNED — TOOLING OPTIONS / NO TOOL DEPLOYMENT CLAIM**

Purpose: make the evaluation and AI-observability layer concrete without turning the architecture reference into a product-specific implementation repository.

## 1. Architecture principle

Evaluation and observability are capabilities, not products. Tool choices may change while the logical contracts remain stable.

Required capabilities include:

- prompt/model/RAG/agent evaluation;
- golden datasets and regression gates;
- latency/TTFT/tokens/cost measurement;
- retrieval and citation quality;
- agent/tool-call traces;
- model/provider/version attribution;
- prompt and configuration version attribution;
- security/prompt-injection regression;
- promotion/rollback evidence.

## 2. Promptfoo option

Use case: **lightweight, CI-friendly evaluation candidate**.

Evaluate for:

- prompt/model comparison;
- regression suites;
- structured assertions;
- security/prompt-injection test cases;
- CI integration;
- cost/latency comparisons where supported.

Architecture rule: Promptfoo may implement part of I14 evaluation, but no architecture requirement depends on Promptfoo specifically.

## 3. Phoenix option

Use case: **AI observability/evaluation candidate** for traces and LLM/RAG analysis.

Evaluate for:

- OpenTelemetry-aligned traces where appropriate;
- request/model/provider attribution;
- retrieval spans;
- agent/tool spans;
- latency/token/cost analysis;
- evaluation linkage;
- debugging of RAG/agent behavior.

Architecture rule: Phoenix is an option, not a mandatory dependency. The common telemetry contract remains OpenTelemetry-first where practical.

## 4. Existing observability foundation

The reference architecture already assumes:

- OpenTelemetry for trace context and telemetry;
- Prometheus/Grafana for platform/application metrics;
- structured audit/evidence for governed AI;
- provider/model/prompt/config attribution;
- LLMOps and evaluation gates.

An AI-specific tool should complement rather than duplicate the entire observability stack.

## 5. Selection criteria

Choose evaluation/observability tooling based on:

1. OpenTelemetry interoperability;
2. model/provider neutrality;
3. RAG/agent trace support;
4. evaluation workflow fit;
5. CI/CD integration;
6. data privacy and retention;
7. deployment model (SaaS/self-hosted);
8. OpenShift/Kubernetes operability;
9. cost;
10. exportability/exit strategy.

## 6. Minimal evaluation chain

```text
Golden dataset
  -> candidate prompt/model/RAG/agent configuration
  -> deterministic checks
  -> retrieval/grounding checks
  -> security checks
  -> latency/cost checks
  -> optional calibrated judge/human review
  -> promotion decision
```

## 7. Telemetry model

Capture when available and appropriate:

- trace/correlation ID;
- application/use-case ID;
- model alias/provider/model version;
- prompt/config version;
- retrieval query and corpus/index version metadata;
- tool name and outcome;
- agent step/state;
- TTFT;
- total latency;
- input/output tokens;
- request/model cost;
- evaluation scores;
- error/fallback/degraded-mode status;
- human-review outcome when applicable.

Sensitive content must follow data-minimization, redaction and retention rules.

## 8. Repository decision

- **Promptfoo:** preferred candidate when a lightweight executable evaluation POC is required.
- **Phoenix:** preferred candidate to evaluate for AI-specific observability/tracing in a future concrete platform mission.
- **OpenTelemetry:** remains the common telemetry foundation.
- **Prometheus/Grafana:** remain the primary platform metrics baseline.

No tool is considered implemented until code/deployment/tests/evidence exist in an executable repository.