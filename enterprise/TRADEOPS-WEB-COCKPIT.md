# TradeOps Web Cockpit — architecture workstream

## Purpose

Add a demonstrable Web IHM to the Agentic AI / trading reference architecture without creating a new backend architecture or bypassing the existing governance model.

The cockpit is a **cross-cutting demo capability** supporting the existing roadmap. It is not a new numbered iteration and it does not change the I0-I12 capability model.

Executable implementation belongs in:

`https://github.com/zdmooc/TradeOps-GenAI-Integration`

Implementation backlog:

`docs/27-tradeops-web-cockpit.md`

Demo URL catalog:

`docs/28-demo-urls.md`

## Architecture position

```text
User / Browser
   -> TradeOps Web Cockpit
      -> Agent Controller / Workflow API
         -> deterministic engines
         -> Agent/RAG/MCP orchestration
         -> deterministic risk gate
         -> Human-in-the-Loop
         -> SHADOW / PAPER
      -> Grafana / OpenShift links for operational evidence
```

The cockpit must visualize the architecture; it must not replace or weaken it.

## User value

The demo must allow an interviewer, architect or operator to see in one place:

- market context and data freshness;
- technical/pattern/regime evidence;
- ML score and qualification status;
- specialized agent evidence;
- conflict / stale / unknown states;
- deterministic risk ACCEPT/VETO;
- fusion result;
- REVIEW_REQUIRED state;
- explicit human decision;
- SHADOW/PAPER outcome;
- PnL/outcome history with provenance;
- audit and operational observability links.

## Security and governance rules

1. The browser does not call MCP directly.
2. The browser does not connect directly to PostgreSQL, Kafka/Redpanda, Qdrant or internal execution services.
3. Risk veto remains authoritative.
4. No UI button can bypass Human-in-the-Loop.
5. SHADOW and PAPER are visually distinct.
6. Real-money execution is out of scope.
7. Synthetic, estimated and measured values must be labelled distinctly.
8. Secrets/tokens are never embedded in frontend source or browser-visible configuration.
9. The UI must use the same identity/audit/correlation model as the backend.
10. Grafana remains the SRE/technical observability interface; the cockpit is the business/demo interface.

## Target views

- Market Dashboard
- Signal Detail
- Agent Evidence
- Deterministic Risk Gate
- Human-in-the-Loop Review
- Positions / Outcomes / Performance
- Audit / Provenance
- Platform / Demo Links

## CRC target

Planned business UI Route:

`https://tradeops-ui-tradeops.apps-crc.testing`

Current state: **PLANNED / NOT YET DEPLOYED**.

Verified existing CRC demo Routes remain:

- `https://agent-controller-tradeops.apps-crc.testing`
- `https://workflow-api-tradeops.apps-crc.testing`
- `https://grafana-tradeops.apps-crc.testing`

## Exit criteria

The cockpit can be considered part of the demonstrable architecture only after:

- React/TypeScript frontend builds in CI;
- OpenShift image/deployment/service/route are healthy;
- UI calls Agent Controller and Workflow API through controlled same-origin endpoints;
- one complete REVIEW_REQUIRED -> human review -> SHADOW/PAPER flow is demonstrated;
- no direct exposure of MCP/database/event-bus internals is introduced;
- demo URLs are catalogued with LIVE/INTERNAL/PLANNED status;
- evidence is captured on CRC;
- the same packaging can later be reconciled by Argo CD on ARO without changing business logic.

## Relation to Azure/ARO

The cockpit should be proven first on CRC. Azure/ARO industrialization then deploys the same frontend through the existing GitOps path.

This preserves the program rule:

```text
prove locally -> package declaratively -> reconcile with GitOps -> deploy on enterprise target
```

No paid Azure resource is required to complete the cockpit implementation and CRC evidence.
