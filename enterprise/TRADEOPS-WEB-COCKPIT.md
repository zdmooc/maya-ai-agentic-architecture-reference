# TradeOps Web Cockpit — architecture workstream

## Status

**IMPLEMENTED + TESTED IN CI / LIVE CRC DEPLOYMENT PENDING** as of 2026-09-13.

Executable runtime commit:

`17d47d33a663b78fd5e23518927929fe5e43b4ce`

TradeOps GitHub Actions CI **#92** (`34750050606`): **SUCCESS**. The run validated the React/TypeScript production build, security/SBOM, Helm lint/render, `I13_WEB_COCKPIT_VALIDATION_PASS`, the existing OpenShift/RHOAI/Azure contracts and **230 passing Pytest tests**.

The business Route remains `PLANNED` until real CRC runtime evidence exists:

`https://tradeops-ui-tradeops.apps-crc.testing`

## Purpose

Add a demonstrable Web IHM to the Agentic AI / trading reference architecture without creating a new backend architecture or bypassing the existing governance model.

The cockpit is a **cross-cutting demo capability** supporting the existing roadmap. It is not a new numbered I0-I12 capability and does not change the architectural control model.

Executable implementation belongs in:

`https://github.com/zdmooc/TradeOps-GenAI-Integration`

Implementation/evidence:

- `docs/27-tradeops-web-cockpit.md`
- `docs/28-demo-urls.md`
- `evidence/ITERATION-013-WEB-COCKPIT.md`
- `frontend/tradeops-ui/`

## Architecture position

```text
User / Browser
   -> TradeOps Web Cockpit
      -> same-origin reverse proxy
         -> Market Data API
         -> Workflow API
         -> Agent Controller
            -> deterministic engines
            -> Agent/RAG/MCP orchestration
            -> deterministic Risk Gate
            -> Human-in-the-Loop
            -> SHADOW / PAPER
      -> Grafana / OpenShift links for operational evidence
```

The cockpit visualizes and operates the existing governed architecture; it does not replace or weaken it.

## Implemented views

- Market Dashboard
- Signal Detail
- Agent Evidence
- Deterministic Risk Gate
- Human-in-the-Loop Review
- SHADOW/PAPER execution control
- Positions / Outcomes / Performance demonstration
- Audit / Provenance
- Platform / Demo Links

## Security and governance rules

1. The browser does not call MCP directly.
2. The browser does not connect directly to PostgreSQL, Kafka/Redpanda, Qdrant or internal execution services.
3. Risk veto remains authoritative.
4. No UI button can bypass Human-in-the-Loop.
5. SHADOW and PAPER are visually distinct.
6. Real-money execution is out of scope.
7. Synthetic, estimated and measured values are labelled distinctly.
8. Secrets/tokens are not embedded in frontend source or built image.
9. CRC static-demo Agent/Reviewer tokens remain memory-only in the browser and are backed by OpenShift Secrets on the services.
10. Grafana remains the SRE/technical observability interface; the cockpit is the business/demo interface.

## CRC status

Existing verified LIVE Routes:

- `https://agent-controller-tradeops.apps-crc.testing`
- `https://workflow-api-tradeops.apps-crc.testing`
- `https://grafana-tradeops.apps-crc.testing`

Implemented but not yet live-verified Route:

- `https://tradeops-ui-tradeops.apps-crc.testing`

The runtime repository already contains the `tradeops-ui` BuildConfig, ImageStream, Helm Deployment/Service/Route, NetworkPolicy changes and CRC deploy/verify logic.

## Remaining live exit criteria

Only runtime evidence remains before the cockpit can be called `DEPLOYED/VERIFIED` on CRC:

- build `tradeops-ui:i13-ui` with the OpenShift BuildConfig;
- Deployment Ready;
- Route reachable;
- `/healthz` reachable;
- proxied Agent Controller and Workflow API health reachable;
- one `REVIEW_REQUIRED -> human review -> SHADOW/PAPER` flow executed;
- audit visible;
- live evidence committed;
- demo URL catalog changed from `PLANNED` to `LIVE` only after those checks.

## Relation to Azure/ARO

The cockpit is proven first on CRC. Azure/ARO industrialization later deploys the **same frontend packaging** through the existing GitOps path, without changing business logic.

```text
prove locally -> package declaratively -> reconcile with GitOps -> deploy on enterprise target
```

No paid Azure resource is required for the cockpit CRC proof.
