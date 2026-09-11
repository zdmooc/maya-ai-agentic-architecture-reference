# Iteration 1 Evidence — Canonical Market Data and Replay

Date: 2026-09-11

## Status

**IMPLEMENTED + TESTED OFFLINE / CI GREEN. LIVE IG DEMO VALIDATION PENDING.**

Iteration 1 is implemented in the executable runtime repository `zdmooc/TradeOps-GenAI-Integration` rather than duplicated in this architecture repository.

Runtime commit:

`38a4f9637da31e8b96f0de8444a59c29a33bc9f3`

Commit message:

`feat(i1): canonical market data, IG adapters and deterministic replay`

GitHub Actions run:

`34642186132` — job `lint-test` — **SUCCESS**

## Implemented capabilities

### Canonical market model

`services/market_data/model.py`

Canonical `MarketEvent` includes:

- instrument;
- event and ingest timestamps normalized to UTC;
- source identity;
- bid / ask / last;
- computed spread and midpoint;
- market status;
- event type and resolution;
- optional source sequence;
- measured latency field;
- stale marker;
- event id and extensible metadata;
- deterministic deduplication key;
- JSON serialization/deserialization.

The contract is also versioned as `schemas/events/market.event.schema.json`.

### IG REST adapter

`services/market_data/ig_rest.py`

Implemented protocol mapping:

- IG Demo and Live base URLs are separated;
- session creation uses POST `/session` version 2;
- CST and X-SECURITY-TOKEN are captured from response headers;
- account id and Lightstreamer endpoint are read dynamically from the session response;
- historical data uses GET `/prices/{epic}` version 3;
- pagination is handled;
- historical OHLC/volume metadata is retained while the close prices are normalized to `MarketEvent`.

The implementation is unit-tested against deterministic mocked IG responses. No successful connection to a real IG account is claimed in this iteration.

### IG Lightstreamer adapter

`services/market_data/ig_streaming.py`

Implemented mapping:

- Lightstreamer endpoint is supplied by the IG session, not hard-coded;
- user is the active IG account id;
- password uses `CST-<token>|XST-<token>`;
- modern `PRICE:{account}:{epic}` subscription;
- `MERGE` mode with `Pricing` data adapter;
- fields used in I1: `BIDPRICE1`, `ASKPRICE1`, `TIMESTAMP`, `DLG_FLAG`;
- updates are normalized to canonical `MarketEvent`;
- observed ingest latency is calculated when an IG timestamp is present;
- connection/subscription lifecycle has an explicit disconnect path.

The Lightstreamer SDK import is lazy, allowing deterministic replay/unit tests without a live network dependency.

### Data-quality engine

`services/market_data/quality.py`

Explicit rejection reasons:

- `DUPLICATE`;
- `OUT_OF_ORDER`;
- `STALE`;
- `BAD_SPREAD`;
- `MISSING_PRICE`;
- `FUTURE_TIMESTAMP`.

The engine updates stream state only after an event is accepted, preventing rejected data from poisoning the high-water mark or deduplication state.

### Deterministic replay

`services/market_data/clock.py`
`services/market_data/replay.py`

Capabilities:

- deterministic clock;
- JSONL capture/load;
- stable replay ordering by event time and event id;
- deterministic quality evaluation;
- historical replay does not incorrectly fail staleness merely because captured data is old;
- accepted/rejected records are retained for evidence.

Versioned fixture:

`data/replay/sample_market_events.jsonl`

Replay demo:

`python scripts/demo_market_replay.py`

Observed local fixture result:

```text
accepted=2 rejected=0
2026-09-11T12:00:00+00:00 IX.D.DAX.IFM.IP bid=23500.0 ask=23501.0 spread=1.0
2026-09-11T12:00:01+00:00 IX.D.DAX.IFM.IP bid=23502.0 ask=23503.0 spread=1.0
```

## Test evidence

Dedicated I1 local test suite:

```text
5 passed
```

It covers:

1. canonical model round-trip and spread;
2. stale, invalid-spread, duplicate and out-of-order rejection;
3. deterministic replay ordering and repeatability;
4. IG REST authentication/header/historical normalization through `httpx.MockTransport`;
5. Lightstreamer subscription/update normalization through deterministic fakes.

Repository CI after push:

```text
ruff check .
All checks passed!

pytest -q
................... [100%]
19 passed, 3 warnings in 1.61s
```

The warnings are pre-existing deprecation warnings in Starlette/FastAPI paths and do not represent an I1 test failure.

The CI also successfully installed `lightstreamer-client-lib==2.2.3` under Python 3.11.

## Configuration and security boundary

`.env.example` now defines empty IG variables:

- `IG_ENV=demo`;
- `IG_API_KEY=`;
- `IG_IDENTIFIER=`;
- `IG_PASSWORD=`.

No real credential is committed. Demo must be validated before any live account use.

## Exit criteria assessment

| I1 criterion | Status | Evidence |
|---|---|---|
| Canonical `MarketEvent` | PASS | code + JSON Schema + tests |
| bid/ask/spread/status/timestamps/source/latency/staleness | PASS | canonical model + streaming adapter |
| IG REST auth/historical adapter | IMPLEMENTED / MOCK-TESTED | deterministic HTTP tests |
| IG Lightstreamer adapter | IMPLEMENTED / MOCK-TESTED | fake SDK/client tests |
| duplicate/out-of-order/bad-data handling | PASS | unit tests |
| event schema | PASS | JSON Schema |
| deterministic clock | PASS | code + replay test |
| reproducible replay | PASS | fixture + script + tests |
| stale/bad-data tests | PASS | tests |
| actual IG Demo REST authentication | PENDING | requires user IG demo credentials/network evidence |
| actual IG Lightstreamer stream | PENDING | requires authenticated IG demo session |
| real latency measurements | PENDING | requires live feed |

The roadmap exit evidence — **reproducible replay and stale/bad-data tests** — is satisfied. Live IG validation is deliberately tracked separately and is not fabricated.

## Non-claims

Iteration 1 does **not** claim:

- profitable signals;
- live IG connectivity;
- production-grade reconnect/session-renewal behavior;
- verified real-world market latency;
- technical indicators or pattern detection;
- backtesting profitability;
- ML probability or calibration;
- automated real-money execution.

These remain governed by later iterations.
