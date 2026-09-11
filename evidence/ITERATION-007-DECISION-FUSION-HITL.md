# Iteration 7 Evidence — Deterministic Decision Fusion and Human-in-the-Loop

Date: 2026-09-11

## Status

**IMPLEMENTED + TESTED. CI GREEN. SHADOW/PAPER EXECUTION REQUIRES EXPLICIT HUMAN APPROVAL.**

Iteration 7 is implemented in `zdmooc/TradeOps-GenAI-Integration`. This architecture repository records the capability gate, evidence and explicit non-claims.

Final runtime HEAD:

`f2e8536da9dc5c0e63134d97c3052f7b00ba1d0a`

Functional I7 commit:

`ab6154b6cd9dbe60e6b30d893c5e7d3d57837d13`

Final GitHub Actions run:

`34650953035` — job `lint-test` — **SUCCESS**

## Runtime delta

I7 starts from I6 runtime HEAD `faa16245013155265ef1edb8e3f47ba1b9b77415`.

The functional commit adds the deterministic fusion/HITL implementation. A second test-only correction commit updates the I6 health expectation and adds end-to-end API coverage. Existing I1-I6 deterministic, replay, backtest, ML and agent engines remain intact.

## Deterministic decision fusion

I7 does not use majority voting. A proposal must pass explicit gates before it can even enter human review.

Required gates are:

- I6 assessment status is `SUPPORTED`;
- I3 deterministic risk status is `ACCEPT`;
- event freshness is within the configured threshold;
- evidence quality meets the policy minimum;
- market regime is explicitly allowlisted;
- reward/risk ratio meets the minimum;
- historical sample size is sufficient;
- historical expectancy in R is above the minimum;
- entry/stop/target geometry is valid for LONG or SHORT;
- any ML probability used as a gate is explicitly qualified as real-market calibrated.

Policy `i7-v1` defaults:

- minimum evidence quality: `0.70`;
- maximum freshness: `5000 ms`;
- minimum R/R: `2.0`;
- minimum historical expectancy: `0.05 R`;
- minimum historical sample: `30` trades;
- minimum qualified real-market calibrated probability: `0.55`;
- review TTL: `15 minutes`.

`POST_EVENT` is not in the default allowed-regime set.

A gate failure returns `NO_TRADE`. Passing every gate returns only `REVIEW_REQUIRED`; it never returns autonomous approval.

## Price geometry

LONG requires:

`stop < entry < every target`

SHORT requires:

`stop > entry > every target`

Invalid geometry fails closed before review.

## ML claim boundary

I5 currently has only `CALIBRATED_OUT_OF_SAMPLE_SYNTHETIC` evidence. I7 deliberately treats synthetic calibration and `SCORE_ONLY` output as non-decisive.

Only an explicitly qualified future status such as:

- `CALIBRATED_REAL_MARKET`;
- `CALIBRATED_OUT_OF_SAMPLE_REAL_MARKET`

can activate the ML probability gate.

Therefore I7 does not convert the I5 synthetic score into a trading probability claim.

## Evidence score

I7 calculates a deterministic evidence score from evidence quality, freshness, R/R and historical expectancy; qualified real-market ML can contribute only when its probability status is eligible.

The score is informational. It is not a substitute for the hard gates and cannot override deterministic risk.

## HITL state machine

Terminal no-trade path:

`NO_TRADE`

Review path:

`PENDING_REVIEW -> APPROVED | REJECTED | EXPIRED`

Approved execution path:

`APPROVED -> EXECUTED_SHADOW | EXECUTED_PAPER | EXPIRED`

Safety invariants:

- a `NO_TRADE` case cannot be reviewed;
- only an authenticated reviewer may approve/reject;
- a general agent cannot self-approve;
- review requires an explicit rationale;
- expired cases fail closed;
- deterministic risk must still be `ACCEPT` at review and execution;
- a case cannot be reviewed twice;
- a case cannot be executed twice;
- PAPER requires an order result containing an `order_id`;
- SHADOW records the approved decision without placing an order.

## API workflow

I7 adds:

- `POST /decision/propose` — agent identity only;
- `GET /decision/{proposal_id}` — agent or reviewer identity;
- `POST /decision/{proposal_id}/review` — reviewer identity only;
- `POST /decision/{proposal_id}/execute` — reviewer identity only after approval.

The service health mode is now `ANALYSIS_PLUS_HITL` with execution scope `SHADOW_OR_PAPER_AFTER_HUMAN_APPROVAL`.

The legacy `/agent/trade` autonomous path remains disabled.

## Persistence and lineage

I7 reuses the existing PostgreSQL `workflows` table instead of creating a parallel workflow database.

The complete I7 case is persisted under `payload.i7`; status, decision and reviewer remain available in the existing searchable columns.

Audit kinds are:

- `decision.proposed`;
- `decision.reviewed`;
- `decision.executed`.

For PAPER execution, `oms.place_order` now accepts the I7 proposal identifier as `workflow_id`. Tests prove that the returned paper order preserves the exact `proposal_id -> workflow_id` lineage.

## Identity boundary

I7 reuses the I6 local demonstrator identities:

- agent bearer token: proposal creation;
- reviewer bearer token: review and approved execution.

The agent identity still has no `paper.execute` privilege at the tool boundary. PAPER execution is invoked using the reviewer identity and `human_approved=true` only after the persisted I7 case reaches `APPROVED`.

Static bearer tokens remain a local test boundary; production OIDC/RBAC is not claimed and belongs to later security work.

## Versioned scenario evidence

`data/decision/i7_fusion_scenarios.json` is marked `SYNTHETIC_POLICY_TEST_ONLY` and includes:

- valid setup -> `REVIEW_REQUIRED` in SHADOW;
- deterministic risk veto -> `NO_TRADE`;
- stale data -> `NO_TRADE`;
- negative historical expectancy -> `NO_TRADE`;
- PAPER eligibility -> still human-approval-required with `execution_allowed=false` at proposal time.

These scenarios validate policy mechanics, not profitability.

## CI evidence

First I7 run on functional commit `ab6154b6cd9dbe60e6b30d893c5e7d3d57837d13`:

- run `34650643058`;
- Ruff: PASS;
- Pytest: `141 passed, 1 failed, 69 warnings`;
- the only failure was the obsolete I6 health assertion expecting `ANALYSIS_ONLY` after I7 legitimately changed the service mode to `ANALYSIS_PLUS_HITL`.

No fusion/HITL functional test failed in that run.

The correction commit `f2e8536da9dc5c0e63134d97c3052f7b00ba1d0a`:

- updates the health expectation to the I7 contract;
- adds API-level HITL tests for agent/reviewer authorization;
- proves SHADOW proposal -> review -> execution;
- proves a second execution is rejected;
- proves PAPER keeps proposal-to-order workflow lineage.

Final run `34650953035`:

```text
ruff check .
All checks passed!

pytest -q
........................................................................ [ 49%]
........................................................................ [ 99%]
.                                                                        [100%]
145 passed, 69 warnings in 16.83s
```

I6 ended with 111 passing tests. I7 therefore adds a net 34 passing tests.

## Explicit non-claims

I7 does **not** claim:

- automated real-money execution;
- live IG order execution;
- real-market calibrated ML probability;
- production OIDC/RBAC or identity federation;
- end-to-end OpenTelemetry tracing;
- production SLOs/dashboards/alerts;
- strategy profitability based on the synthetic policy fixtures;
- that evidence score can override hard risk or policy gates.

## I7 exit decision

The I7 capability gate is satisfied because:

- fusion is deterministic, evidence-aware and not majority voting;
- deterministic I3 risk remains authoritative;
- synthetic ML evidence is not mislabeled or promoted to a real-market probability;
- eligible cases require human review;
- rejection, expiration and duplicate execution fail closed;
- SHADOW is approval-gated but order-free;
- PAPER is approval-gated and passes through the governed tool boundary;
- proposal/reviewer/order lineage is preserved;
- the full repository CI is green with 145 tests and Ruff clean.

Iteration 8 has not started.
