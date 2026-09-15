# AI Gateway Implementation Options

Status: **DESIGNED — OPTION ANALYSIS / NO PRODUCT DEPLOYMENT CLAIM**

Purpose: make the AI Gateway decision concrete while preserving vendor neutrality.

## 1. Required logical capabilities

The enterprise AI Gateway should provide or integrate with:

- authentication and authorization;
- application/tenant identity;
- model aliases;
- multi-provider routing;
- provider allowlists;
- data-classification and residency-aware routing;
- quotas and rate limits;
- timeout and retry policy;
- budget/cost controls;
- fallback policy;
- structured telemetry;
- prompt/output policy hooks;
- audit/provenance metadata;
- secret isolation;
- provider-specific adapters behind a stable application contract.

Applications should call a stable enterprise contract rather than hard-code OpenAI, Azure, AWS, Google, Anthropic, Mistral or another provider directly.

## 2. LiteLLM option

Use case: **pragmatic executable gateway / lab / integration baseline**.

Strengths to evaluate:

- broad provider abstraction;
- model aliases/routing;
- budget and usage controls;
- relatively low barrier to executable proof;
- useful for validating the logical gateway contract.

Architecture caution:

- using LiteLLM does not remove the need for enterprise IAM, network, policy, audit and operational controls around it;
- product features and interfaces must be version-pinned and verified before any production recommendation.

Portfolio rule: LiteLLM may be selected for a concrete POC when an executable multi-provider gateway is required.

## 3. Envoy AI Gateway option

Use case: **enterprise/reference architecture candidate when an Envoy/Kubernetes-native gateway model is appropriate**.

Evaluate:

- integration with existing gateway/network architecture;
- Kubernetes/OpenShift fit;
- routing/policy extensibility;
- security and observability integration;
- operational maturity and version support at decision time.

Portfolio rule: treat Envoy AI Gateway as an architecture option, not as a claimed deployed capability unless runtime evidence exists.

## 4. Managed-cloud gateway option

A cloud provider may offer managed model routing, policy or AI gateway capabilities. These can be suitable when:

- cloud placement is already mandated;
- data residency and security requirements are satisfied;
- provider lock-in is accepted through an ADR;
- the managed capability materially reduces operations burden.

The application contract must remain portable where business requirements demand reversibility.

## 5. Selection criteria

Score candidate gateways against:

1. security/IAM integration;
2. model/provider coverage;
3. policy extensibility;
4. data residency controls;
5. routing/fallback features;
6. rate/quota/budget controls;
7. telemetry and audit;
8. OpenShift/Kubernetes operability;
9. HA/resilience model;
10. latency overhead;
11. cost;
12. portability and exit strategy;
13. community/vendor support;
14. upgrade/rollback complexity.

## 6. Recommended decision pattern

```text
Application
   -> Enterprise AI contract
   -> AI Gateway
      -> policy / identity / quota / budget
      -> model alias
      -> provider eligibility
      -> route/fallback
   -> approved model provider or private serving
```

## 7. Current repository decision

No universal product is mandated.

- **Architecture contract:** mandatory.
- **Provider abstraction:** mandatory where portability is an NFR.
- **LiteLLM:** preferred candidate for a lightweight executable POC.
- **Envoy AI Gateway:** enterprise/reference candidate to evaluate when mission context justifies it.
- **Managed gateway:** valid when cloud/provider constraints make it the best trade-off.

Any product selection must produce an ADR and runtime evidence before being described as implemented.