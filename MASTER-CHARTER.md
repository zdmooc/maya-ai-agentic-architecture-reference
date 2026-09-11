# Master Charter

## Mission

Build a demonstrable portfolio for the role **AI Solution Architect — Agentic AI & Real-Time Trading Systems** while keeping the architecture transferable to banking, payments, insurance, fraud, risk, cybersecurity, IT supervision and other real-time decision domains.

Trading is the demanding reference domain, not the purpose of the architecture.

## Outcomes

The program must demonstrate the ability to move from business need to architecture, implementation choices, controls, deployment, evidence and Architecture Review Board communication across:

- real-time/event-driven systems;
- deterministic quantitative engines;
- ML/MLOps;
- GenAI/LLMOps;
- multi-agent orchestration;
- RAG and MCP;
- security, governance and Human-in-the-Loop;
- OpenShift/GitOps;
- Azure enterprise architecture;
- observability/SRE, resilience, FinOps and GreenOps.

## Non-negotiable architecture principles

1. **Deterministic calculations remain deterministic.** Price, indicators, patterns, sizing and hard risk rules are not delegated to an LLM.
2. **ML estimates are measurable.** A score is not labelled a probability until calibration is demonstrated out-of-sample.
3. **Risk has veto power.** No model or agent can bypass deterministic policy/risk controls.
4. **No naïve multi-source price averaging.** Source identity, timestamp, latency, spread, staleness and quality are explicit data.
5. **Execution venue is authoritative for execution.** If an operation targets IG, IG data is the execution reference; other feeds are corroborating context.
6. **Agents orchestrate governed capabilities.** They synthesize evidence, call allowlisted tools, surface uncertainty and request human intervention.
7. **MCP is a security boundary, not a shortcut.** Authentication, authorization, input/output validation, timeouts, rate limits, audit and secret redaction are mandatory.
8. **Evidence precedes claims.** DESIGNED, IMPLEMENTED, TESTED, DEPLOYED and VERIFIED have distinct meanings.
9. **Architecture remains portable.** OpenShift/ARO and Azure managed services may optimize deployment without coupling domain logic to a single provider.
10. **Reuse before reinvention.** Existing personal repositories and mature public projects are reused, adapted or referenced deliberately rather than copied.

## Repository roles

### This repository

Owns architecture vision, capability map, target state, ADR direction, reuse decisions, roadmap, evidence index and enterprise transposability.

### TradeOps-GenAI-Integration

Primary candidate for executable trading integration. Reuse the event-driven services, workflow, RAG, MCP facade, paper OMS and audit concepts. Replace or substantially strengthen demo signal/risk logic, observability and production packaging.

### Other repositories

Remain specialist sources of reusable patterns. They are not merged wholesale into this repository.

## Financial safety scope

Initial scope:

`analysis -> signal -> replay/backtest -> paper/shadow -> Human-in-the-Loop`

Automated real-money execution is explicitly out of scope until a later architecture decision backed by controls, test evidence and operational governance.

## Evidence model

Every significant capability must eventually provide:

- architecture decision/ADR;
- code/configuration or external reference;
- automated tests where applicable;
- runtime/deployment evidence where claimed;
- metrics and traceability;
- known limitations;
- an interview-ready explanation of trade-offs.

## Iteration definition of done

Each technical iteration follows:

`ANALYSE -> AUDIT -> ARCHITECTURE -> REUSE DECISION -> IMPLEMENT -> TEST -> EVIDENCE -> DOCUMENT -> COMMIT -> BILAN -> STOP`

The next iteration starts only after the current state is coherent and recoverable from Git.
