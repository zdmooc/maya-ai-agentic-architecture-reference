# Iteration 008 — End-to-End Observability, Security and LLMOps

Status: **IMPLEMENTED + TESTED IN CI / DEPLOYMENT VALIDATION PENDING**

## Scope

Iteration 8 hardens the existing runtime rather than creating another observability or security stack. It reuses the existing Prometheus/Grafana baseline, replaces the OpenTelemetry placeholder, adds trace/correlation propagation, adds security and identity controls, and turns security/SBOM checks into CI gates.

Runtime repository: `zdmooc/TradeOps-GenAI-Integration`

Baseline before I8:

- I7 HEAD: `f2e8536da9dc5c0e63134d97c3052f7b00ba1d0a`

I8 commits:

- functional commit: `eea28b5d5317f3fd200de56ba882f9a6d93371d4` — `feat(i8): observability security and LLMOps hardening`;
- hardening/fix commit and final I8 HEAD: `90976dd60a9b80272e39db07ed027ae500f947c1` — `fix(i8): harden secret audit defaults`.

Runtime delta from I7 to final I8 HEAD:

- 2 commits ahead;
- 0 commits behind;
- 30 files changed.

## Implemented capabilities

### OpenTelemetry and correlation

- `services/common/otel.py` is no longer a placeholder;
- OpenTelemetry SDK and OTLP HTTP exporter are pinned in runtime dependencies;
- W3C `traceparent` propagation is implemented for service calls;
- `X-Correlation-ID` is propagated as an application-level lineage identifier;
- HTTP request tracing is integrated into the agent-controller and governed tool server paths;
- Kafka publish/consume helpers propagate trace and correlation context;
- structured logs can include correlation/trace context;
- decision fusion and deterministic risk evaluation emit business spans;
- LLM calls emit spans with provider/model/status/latency metadata without storing prompt content.

### Prometheus / Grafana / SLOs

- the existing Prometheus/Grafana stack is reused rather than duplicated;
- Prometheus scrape coverage is expanded beyond the original three APIs;
- business/security/LLM metrics are added, including decision outcomes, MCP policy outcomes, LLM request latency and estimated token/cost counters;
- an I8 Grafana dashboard is provisioned;
- Prometheus alert rules are added for service availability/error/latency and governed decision/tool behavior;
- an OpenTelemetry Collector configuration is added for local OTLP ingestion/export wiring.

### LLMOps

- LLM latency is measured;
- input/output token counts and cost are represented only as estimates when provider-native usage is unavailable;
- prompt/response bodies are not intentionally attached to spans;
- LLM observability does not grant execution authority and does not bypass the I3 risk veto or I7 HITL gate.

### Identity and authorization

- `services/security/identity.py` adds a reusable identity contract;
- local static bearer-token principals remain available for the demonstrator;
- OIDC/JWT-compatible verification supports issuer, audience, JWKS, expiry, roles and scopes;
- invalid audience, expired token and wrong-role paths fail closed;
- agent and reviewer roles remain distinct;
- governed MCP/tool scopes remain server-side and reviewer execution still requires explicit human approval.

### Secret and supply-chain hygiene

- tracked `.env` was removed from Git;
- `.gitignore` now prevents `.env` from being re-added;
- `.env.example` remains the documented template;
- weak default `POSTGRES_PASSWORD=tradeops` values were replaced with explicit local placeholders in Python/Helm configuration;
- `scripts/security_audit.py` rejects a tracked `.env`, private-key material and literal secret-like values in active source/config paths;
- historical `evidence-sample/` output and the scanner source itself are excluded only to avoid self/redacted-artifact false positives;
- a deterministic SPDX JSON SBOM is generated from the repository's pinned direct requirements;
- CI checks that the committed SBOM matches `requirements.txt`.

### Threat / abuse tests

- OIDC/JWT verification, audience/expiry/role failures and static-local compatibility are covered by tests;
- prompt-injection marker handling remains fail closed through the I6 RAG governance path;
- security scanner behavior is tested;
- SBOM determinism/completeness against pinned direct requirements is tested;
- trace/correlation propagation and observability behavior are covered by I8 tests.

## CI evidence

### First I8 run — expected hardening failure

GitHub Actions run: `34653286233`

Observed:

- dependency installation: PASS;
- Ruff: PASS;
- new security audit: FAIL;
- SBOM and Pytest were correctly skipped after the security gate failed.

The new scanner found:

- real weak defaults in active configuration (`POSTGRES_PASSWORD=tradeops`);
- false positives in historical redacted evidence;
- a self-match on the scanner's own private-key marker strings.

No security gate was disabled. Active weak defaults were corrected and exclusions were narrowed to the scanner itself plus historical `evidence-sample/` artifacts.

### Final I8 run

GitHub Actions run: `34654382558`

Job: `103443477579`

Final results:

- dependency installation: PASS;
- Ruff: **PASS** (`All checks passed!`);
- security audit: **PASS** (`SECURITY_AUDIT_PASS`);
- SBOM consistency gate: **PASS** (`SBOM_CHECK_PASS`);
- Pytest: **157 passed, 69 warnings in 15.78s**;
- overall job conclusion: **SUCCESS**.

Net test increase from I7: **12 passing tests** (145 -> 157).

The 69 warnings are non-blocking deprecation warnings already concentrated in Starlette/FastAPI and sklearn/SciPy compatibility paths; they are not I8 functional failures.

## Evidence classification

### IMPLEMENTED + TESTED

- trace/correlation context primitives;
- HTTP/Kafka propagation code;
- business/LLM instrumentation hooks;
- Prometheus metric definitions;
- JWT/OIDC-compatible validation logic;
- role/scope fail-closed tests;
- secret audit CI gate;
- deterministic direct-dependency SBOM and consistency gate;
- Grafana/Prometheus/Collector configuration files;
- prompt-injection regression test;
- full CI regression suite.

### DESIGNED / CONFIGURED, NOT DEPLOYMENT-VERIFIED IN I8

- OpenTelemetry Collector running as an actually observed end-to-end trace backend;
- Grafana dashboard rendering against live I8 traffic;
- alert firing/notification delivery in a running environment;
- production IdP/OIDC federation against a real external issuer;
- production secrets manager integration;
- production TLS/mTLS service mesh or PKI.

## Explicit non-claims

- I8 does **not** claim a production OpenTelemetry backend deployment or measured trace retention/throughput;
- I8 does **not** claim live federation with Entra ID, Keycloak, Okta or another production IdP;
- the OIDC code proves JWT validation mechanics, not a production IAM rollout;
- the SPDX file covers pinned direct Python requirements and is not claimed as a complete transitive container/image SBOM;
- the repository security scanner is a focused CI hygiene gate, not a replacement for enterprise secret-scanning/SAST platforms;
- prompt-injection marker detection is a deterministic defensive control, not comprehensive prompt-injection immunity;
- NetworkPolicy, cluster Policy-as-Code/Kyverno, image scanning and deployment-enforced controls remain I9 work;
- Phoenix is not added in I8; its ELv2 implications remain a deliberate review point before adoption;
- no automated real-money execution or live IG order routing is enabled;
- observability does not weaken the deterministic risk veto or mandatory human review boundary.

## Exit decision

Iteration 8 exit criteria are satisfied at the **code/CI evidence** level:

- correlation/trace primitives exist and are tested;
- dashboards/alerts/collector configuration exist;
- LLM/business/security metrics exist;
- identity/security/SBOM controls are CI-enforced;
- negative security tests pass;
- full regression CI is green.

Deployment validation of those observability/security configurations is intentionally deferred to the OpenShift/GitOps work in I9.
