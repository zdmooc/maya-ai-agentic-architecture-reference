# Iteration 6 Evidence — Governed RAG, Tool Boundary and Specialist Agents

Date: 2026-09-11

## Status

**IMPLEMENTED + TESTED. CI GREEN. ANALYSIS-ONLY AGENTIC BOUNDARY.**

Iteration 6 is implemented in the executable runtime repository `zdmooc/TradeOps-GenAI-Integration`. The architecture repository records the capability gate, evidence and explicit non-claims.

Final runtime HEAD:

`faa16245013155265ef1edb8e3f47ba1b9b77415`

GitHub Actions run:

`34648593641` — job `lint-test` — **SUCCESS**

## Runtime delta

I6 is exactly one commit ahead of the final I5 runtime HEAD `bca514ce35fab3e63ef16e487394fea576523d7b` and zero commits behind.

Git compare shows 22 changed files. I6 adds governed agent/RAG/tool capabilities while preserving the I1-I5 deterministic, backtest and ML engines.

## Real agent framework

The pre-I6 controller described itself as "LangGraph-style" but used a hand-written sequential function loop. I6 replaces that claim with an actual LangGraph `StateGraph` and pins:

`langgraph==1.2.11`

CI installed that exact version successfully on CPython 3.11.16.

The graph is:

`START -> Market -> Technical -> Pattern -> Macro -> Risk -> Fusion -> END`

Microsoft Agent Framework was reviewed as an alternative but is not added, avoiding two competing orchestration frameworks.

## Specialist agents and evidence states

Implemented specialist roles:

- Market Agent;
- Technical Agent;
- Pattern Agent;
- Macro Agent;
- Risk Agent;
- Fusion Agent.

Agents consume upstream evidence; they do not recompute deterministic indicators, patterns, sizing or hard-risk limits.

Every finding can emit:

- `SUPPORTED`;
- `UNKNOWN`;
- `DATA_STALE`;
- `CONFLICT`;
- `VETO`.

Fail-closed precedence is:

1. deterministic I3 risk `VETO`;
2. stale market evidence -> `DATA_STALE`;
3. specialist or governed-RAG conflict -> `CONFLICT`;
4. opposing directional evidence -> `CONFLICT`;
5. insufficient aligned evidence -> `UNKNOWN`;
6. aligned evidence plus deterministic risk ACCEPT -> `SUPPORTED`.

`SUPPORTED` remains analysis-only and is not an order approval.

## Execution boundary

`AgenticAssessment` hard-codes:

- `execution_allowed=false`;
- `decision_scope=ANALYSIS_ONLY`.

The JSON Schema also constrains these exact values.

The legacy `/agent/trade` path that could reach `APPROVE` and call the paper OMS is disabled with HTTP 409. The new `/agent/assessment` endpoint returns only evidence and assessment state. I7 owns the later executable fusion/HITL workflow.

## Governed RAG

The existing Qdrant-backed retrieval service remains reusable. Before passages enter agent context, I6 validates:

- approved `.md` / `.txt` source type;
- score range and minimum relevance threshold;
- non-empty bounded text;
- prompt-injection markers such as requests to ignore prior instructions, expose prompts, execute shell commands or bypass policy.

Unsafe retrieved instructions produce `CONFLICT`. No acceptable retrieval produces `UNKNOWN`.

A versioned I6 RAG corpus covers:

- deterministic risk policy;
- strategy governance;
- stale-data runbook;
- agent boundary ADR;
- evidence lineage.

## Governed tool boundary

The existing internal `/call` compatibility boundary is hardened with:

- server-side bearer-token authentication;
- server-assigned principals and scopes;
- explicit governed-tool allowlist;
- strict argument/type/enum validation;
- rejection of unknown fields;
- per-principal/tool sliding-window rate limits;
- bounded tool execution timeout;
- secret-like field redaction before audit payload persistence;
- separate general-agent and human-reviewer identities.

General-agent scopes:

- `market.read`;
- `risk.evaluate`;
- `workflow.read`.

Reviewer scopes additionally include:

- `audit.read`;
- `paper.execute`.

`oms.place_order` requires both `paper.execute` and explicit `human_approved=true`. Tests prove that the general agent remains forbidden even if it submits `human_approved=true` itself.

No arbitrary shell tool exists in the allowlist; an attempted `shell.exec` is rejected as `TOOL_NOT_ALLOWED`.

## MCP protocol claim boundary

The official MCP Python SDK v2 was reviewed during I6, but it is not added to this runtime. The runtime already pins `uvicorn==0.30.6`, while the reviewed current MCP SDK line requires a newer Uvicorn on normal Python platforms. I6 therefore avoids an unrelated protocol-stack migration merely to claim the SDK.

The hardened `/call` interface is treated as a governed MCP-shaped compatibility boundary only.

I6 does **not** claim:

- official MCP protocol-conformance testing;
- a native Streamable HTTP MCP deployment;
- full MCP OAuth/resource-server implementation.

Any future native MCP migration must preserve the I6 authorization/policy layer and must not create an ungoverned second tool path.

## Versioned disagreement scenarios

`data/agentic/i6_disagreement_scenarios.json` is explicitly marked `SYNTHETIC_POLICY_TEST_ONLY` and contains:

- aligned LONG evidence -> `SUPPORTED/LONG`;
- technical/pattern disagreement -> `CONFLICT/UNKNOWN`;
- stale market data -> `DATA_STALE/UNKNOWN`;
- deterministic risk veto -> `VETO/NEUTRAL`.

These scenarios validate policy mechanics, not trading performance.

## CI evidence

Final CI on runtime commit `faa16245013155265ef1edb8e3f47ba1b9b77415`:

```text
ruff check .
All checks passed!

pytest -q
........................................................................ [ 64%]
.......................................                                  [100%]
111 passed, 69 warnings in 15.58s
```

I5 ended with 87 passing tests. I6 therefore contributes a net increase of 24 passing tests after replacing the seven legacy heuristic-agent tests with four governed API tests and adding dedicated specialist/RAG/tool-policy/API coverage.

I6 tests include:

- actual LangGraph graph execution;
- versioned disagreement scenarios;
- stale-data behavior;
- opposing-direction conflict;
- terminal deterministic risk veto;
- UNKNOWN fallback;
- RAG low-score rejection;
- RAG prompt-injection conflict;
- server-side token/scopes;
- missing-scope rejection;
- unknown-tool rejection;
- unknown-argument/type/enum/quantity rejection;
- explicit human approval for paper execution;
- proof that general-agent identity cannot self-escalate into `paper.execute`;
- rate limiting;
- recursive audit redaction;
- tool timeout fail-closed behavior.

The 69 warnings are non-blocking deprecation warnings from the existing Starlette/FastAPI/scikit-learn dependency lines; I6 introduces no CI failure.

## Explicit non-claims

I6 does **not** claim:

- executable I7 decision fusion;
- a complete Human-in-the-Loop approval workflow;
- automated real-money execution;
- production authentication/identity federation; the I6 static bearer-token mapping is a testable local boundary to be replaced by OIDC/RBAC in later security work;
- official MCP protocol conformance;
- cryptographic RAG document provenance;
- comprehensive defense against every possible prompt-injection technique;
- agent-generated deterministic indicators, patterns, market regime or risk calculations;
- real-market profitability or calibration beyond I5's explicitly synthetic qualification.

## I6 exit decision

The I6 capability gate is satisfied because:

- a real agent graph framework is executed in CI;
- all target specialist roles exist;
- UNKNOWN / DATA_STALE / CONFLICT / VETO behavior is explicit and tested;
- deterministic I3 VETO remains terminal;
- RAG evidence is governed before entering the agent context;
- tool access is authenticated, authorized, allowlisted, validated, rate-limited, time-bounded and audited with redaction;
- general agents cannot access the paper-order capability;
- disagreement and tool-abuse scenarios are versioned and green in the full repository CI.

Iteration 7 has not started.
