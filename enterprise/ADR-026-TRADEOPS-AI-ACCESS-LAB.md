# ADR-026 — TradeOps AI Access lab: Shared Identity -> Kong -> LiteLLM -> Model

**Status:** ACCEPTED FOR D-090 LAB / RUNTIME EVIDENCE PENDING  
**Date:** 2026-10-03  
**Scope:** G0 of the D-090 AI Platform execution wave.

## Context

The common L2 foundation is already proven for Shared OIDC and Shared OpenTelemetry. API Management has already demonstrated the pattern Shared OIDC -> Kong -> protected API + traces -> Shared OTel on CRC.

The next uncertainty is not the L2 foundation. It is whether the primary AI runtime, `TradeOps-GenAI-Integration`, can consume a real model through a governed AI access boundary and later be reused by a second consumer without prematurely creating another generic platform repository.

The current TradeOps LLM adapter always delegates to `MockLLM`; configuration can therefore label a provider/model that was never called. D-090 makes this the first AI runtime gap to close.

## Drivers

- reuse already-proven Shared Identity and Shared OTel;
- keep authentication/authorization deterministic and outside prompt semantics;
- preserve a provider-neutral application contract;
- expose model aliases, quota/budget and routing controls without embedding provider credentials in TradeOps;
- make actual executed provider/model observable;
- prove reuse before extraction.

## Options considered

### A — TradeOps calls a model provider directly

Rejected for the D-090 target because provider credentials and policy would remain application-owned and the reusable gateway contract would not be proven.

### B — TradeOps -> Kong -> LiteLLM -> model

Selected for the lab. Kong reuses the proven gateway/JWT boundary. LiteLLM is the lightweight executable AI routing candidate already identified by this reference repository.

### C — Envoy AI Gateway

Retained as an enterprise/reference option. Not selected for this first executable proof because it adds a second gateway technology before the basic multi-consumer contract is proven.

### D — Managed cloud AI gateway

Deferred to G9 / Azure AI. It remains a valid G5 platformization option.

## Decision

For G1-G4 use:

```text
TradeOps workload
  -> Shared Keycloak/RHBK client_credentials
  -> JWT
  -> Kong
       - authenticate/authorize workload
       - derive consumer server-side
       - never trust client-supplied consumer identity
  -> LiteLLM
       - model alias/routing
       - model allowlist
       - quota/budget policy
  -> approved real model
  -> Shared OpenTelemetry + AI-specific telemetry
```

Ownership during G1-G4:

- Shared Platform L2 owns OIDC/identity contract, OTel, secrets/GitOps/quality conventions.
- API Management remains the reference implementation for Kong/OIDC/OTel patterns.
- TradeOps temporarily owns the AI Access lab assets and integration code.
- LiteLLM is `DEDICATED_FOR_TEST` until G5.
- ODM becomes the second consumer in G3.
- No independent `maya-ai-platform` repository is created before G5.

## Security and identity

- workload identity is obtained through client credentials for the lab;
- Kong validates issuer/audience/scope according to the shared contract;
- consumer identity is derived from authenticated claims/server mapping;
- no `X-Consumer-Id` or equivalent client-controlled header is authoritative;
- provider credentials/LiteLLM keys are never exposed to consumers;
- model authorization and quotas fail closed;
- deterministic Risk Gate and HITL remain authoritative for TradeOps business actions.

## Observability

Client configuration may identify the requested alias, but telemetry must distinguish:

- requested model alias;
- model reported by the executed gateway/provider response;
- gateway/provider boundary actually called;
- authenticated consumer identity when returned by the trusted gateway;
- latency;
- token usage when provider-reported, otherwise explicitly estimated;
- cost when methodology/configuration is declared.

A configured provider/model name is not runtime evidence.

## Technical debt

During G3-G4, ODM consumes a capability hosted by TradeOps. This is deliberate temporary hosting, not an independent enterprise platform claim.

Exit gate: G5.

## Evidence required

G1:
- non-mock request path implemented;
- deterministic unit tests with a fake OpenAI-compatible gateway;
- observed real-model call before `DEPLOYED × SINGLE_CONSUMER` is claimed.

G2:
- auth negative tests;
- allowlist/quota policy tests;
- telemetry test proving response-reported model is used rather than configuration-only labels.

G3:
- ODM uses the same gateway contract.

G4:
- distinct identities/policies for TradeOps and ODM;
- cross-consumer negative tests.

## Revisit triggers

Revisit at G5 after G3/G4 evidence. Options are:

1. keep the capability hosted with TradeOps;
2. extract a small specialized AI platform;
3. adopt a managed provider capability.

The decision must be based on observed reuse and operational evidence, not repository ambition.
