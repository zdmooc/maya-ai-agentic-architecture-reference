# TradeOps Web Cockpit — architecture workstream

## Status

**DEPLOYED LIVE ON CRC / PLATFORM VERIFIED / END-TO-END HITL LIVE PROOF PENDING** as of 2026-09-13.

Executable runtime implementation:

`https://github.com/zdmooc/TradeOps-GenAI-Integration`

The business Route is now LIVE and verified on real CRC:

`https://tradeops-ui-tradeops.apps-crc.testing`

Deployment/evidence source:

`TradeOps-GenAI-Integration/evidence/graduation/live/ui/20260913/README.md`

The live platform proof covers the OpenShift build, published image, Deployment Ready, Service, Route, UI health, same-origin proxy health to Market/Workflow/Agent, and `I9_CRC_VERIFY_PASS`.

The complete interactive business proof `REVIEW_REQUIRED -> APPROVE/REJECT -> SHADOW/PAPER -> audit` remains a separate final live-functional step and is not yet claimed as demonstrated.

## Purpose

Add a demonstrable Web IHM to the Agentic AI / trading reference architecture without creating a new backend architecture or bypassing the existing governance model.

The cockpit is a **cross-cutting demo capability** supporting the existing roadmap. It is not a new numbered I0-I12 capability and does not change the architectural control model.

Executable implementation belongs in:

`https://github.com/zdmooc/TradeOps-GenAI-Integration`

Implementation/evidence:

- `docs/27-tradeops-web-cockpit.md`
- `docs/28-demo-urls.md`
- `evidence/ITERATION-013-WEB-COCKPIT.md`
- `evidence/graduation/live/ui/20260913/README.md`
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

Verified LIVE Routes:

- `https://agent-controller-tradeops.apps-crc.testing`
- `https://workflow-api-tradeops.apps-crc.testing`
- `https://grafana-tradeops.apps-crc.testing`
- `https://tradeops-ui-tradeops.apps-crc.testing`

The runtime repository contains the `tradeops-ui` BuildConfig, ImageStream, Helm Deployment/Service/Route, NetworkPolicy controls and CRC deploy/verify logic.

Live CRC proof on 2026-09-13 verified:

- `tradeops-ui-1` OpenShift build `Complete`;
- ImageStreamTag `tradeops-ui:i13-ui` published;
- Helm release `tradeops` deployed, revision `5`;
- Deployment `tradeops-ui` Ready `1/1`;
- Route reachable;
- `/` and `/healthz` HTTP 200;
- proxied Market, Workflow and Agent health HTTP 200;
- `scripts/i9_crc_verify.sh` ended with `I9_CRC_VERIFY_PASS`.

## Remaining live functional proof

The deployment itself is live and verified. Remaining evidence is limited to the governed business flow:

- create a proposal and observe `REVIEW_REQUIRED`;
- perform explicit human `APPROVE` or `REJECT`;
- for an approved proposal, execute only `SHADOW` or `PAPER`;
- verify the audit record.

This remaining cockpit evidence is not an I12 graduation blocker.

## Relation to Azure/ARO

The cockpit is proven first on CRC. Azure/ARO industrialization later deploys the **same frontend packaging** through the existing GitOps path, without changing business logic.

```text
prove locally -> package declaratively -> reconcile with GitOps -> deploy on enterprise target
```

No paid Azure resource is required for the cockpit CRC proof.

The I12 graduation blockers remain unchanged:

- `OPENSHIFT_AZURE_DEPLOYMENT`;
- `RESILIENCE_FINOPS_GREENOPS_VERIFIED`.
