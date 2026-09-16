# Enterprise AI / SI Integration Contracts

Status: **DESIGNED — ARCHITECTURE REFERENCE / NO PRODUCTION INTEGRATION CLAIM**

## Purpose

Complete the enterprise integration layer between AI/agents and existing information systems. The goal is to avoid direct, privileged, ad-hoc connections from LLMs to enterprise backends.

## Core rule

For every AI integration, document five things:

1. contract;
2. identity;
3. authorization;
4. failure behavior;
5. audit evidence.

If one is missing, the integration is not production-ready.

## Four integration families

| Pattern | Typical use | Key risks |
|---|---|---|
| Synchronous API | interactive lookup/action | timeout, cascade failure, authz |
| Event-driven | decoupled/long-running processing | ordering, duplicates, replay, DLQ |
| Data/CDC | knowledge/index refresh | consistency, schema evolution, lag |
| Tool/Agent | controlled action in SI | excessive agency, privilege, audit |

## Contract-first architecture

Use explicit, versioned contracts:

- OpenAPI for HTTP APIs;
- AsyncAPI and/or schema-registry contracts for events;
- CloudEvents-style envelopes where useful for event metadata;
- typed MCP tool schemas for agentic capabilities.

Each contract defines schema, semantics, versioning, timeout/TTL, security, retry/idempotency and correlation identifiers.

## API Gateway vs AI Gateway

An API Gateway primarily protects enterprise APIs. An AI Gateway adds AI-specific controls.

| Control | API Gateway | AI Gateway |
|---|---|---|
| AuthN/AuthZ | OIDC/OAuth2/mTLS | consumes identity + AI policy |
| Quota | RPS/bandwidth | tokens/model/provider/budget |
| Routing | service/version/region | model/provider/fallback |
| Validation | payload/OpenAPI | prompt/tool schema/model policy |
| Security | WAF/TLS/IP | prompt injection, DLP, model egress |
| Observability | HTTP latency/errors | TTFT/tokens/tool calls/model |

The same product may implement both, but keep the responsibilities logically distinct.

## Identity propagation

Separate human identity from workload identity.

`user OIDC -> application principal -> policy decision -> dedicated workload identity -> backend-specific credential`

Do not forward one broad administrator token across every tool/backend.

Each integration adapter should have its own audience, scopes, secrets and least-privilege permissions.

## Kafka / event-driven AI

Define explicitly:

- event type/version;
- stable business key;
- partition key and ordering expectation;
- consumer group;
- retention;
- retry strategy;
- DLQ;
- replay procedure;
- idempotency key;
- correlation and causation IDs.

### Exactly-once caution

Do not promise end-to-end exactly-once across `Kafka -> agent -> external API -> database` unless every side effect participates in a proven transactional design.

Prefer:

- idempotent consumers;
- deduplication store;
- outbox/inbox patterns;
- deterministic business keys;
- replay-safe handlers.

## IBM MQ / payment systems

For payment/operations scenarios, expose narrow, governed capabilities such as:

- read queue depth/status;
- read channel/queue-manager health;
- inspect synthetic/non-sensitive DLQ metadata;
- retrieve a payment status by controlled identifier;
- request a remediation draft.

Do not expose unrestricted MQ administration or blind message replay to an agent. Sensitive operations require deterministic policy and human approval.

## ITSM / CMDB

Separate read and write capabilities:

- read incident;
- read CI/service relationship;
- create draft comment/change;
- create/update incident only with approved scope;
- production change requires explicit workflow/HITL.

CMDB context is evidence, not authorization. The fact that an agent found a CI relationship does not give it permission to change that CI.

## Git / GitOps remediation

Prefer change-by-PR for configuration remediation:

`agent diagnosis -> proposed patch -> policy -> human review -> PR -> CI/policy checks -> merge -> GitOps reconcile -> post-condition verification`

This creates reviewability, rollback and traceability instead of direct mutation.

## Secrets and workload identity

Use external secret management and short-lived/workload credentials where possible. Do not place enterprise API keys in prompts, tool descriptions or generic `.env` files committed to source control.

## Observability contract

Propagate at least:

- trace ID;
- correlation/business ID;
- actor/principal;
- tool/API/event name;
- policy decision;
- target environment/resource;
- outcome;
- redacted error details.

A single incident should be traceable across AI request, tool call, Kafka/MQ event, ITSM ticket and Git change.

## Failure behavior

For each adapter define:

- timeout;
- retryability;
- circuit breaker;
- fallback/degraded mode;
- stale-data behavior;
- partial-success semantics;
- compensation/manual recovery;
- fail-closed behavior for sensitive actions.

## Required evidence before `VERIFIED`

- versioned API/event/tool schemas;
- least-privilege identity tests;
- unauthorized-call negative tests;
- idempotency/replay tests;
- DLQ/recovery evidence;
- trace correlation across systems;
- HITL evidence for privileged actions;
- post-condition verification after any write.