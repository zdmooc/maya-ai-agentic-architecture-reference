# Building Evolutionary Architectures — Architecture Alignment for AI

Status: **DESIGNED — ARCHITECTURE EXTRACTION COMPLETE / AUTOMATION EVIDENCE DEFERRED**

Source: *Building Evolutionary Architectures — 2nd Edition* — Neal Ford, Rebecca Parsons, Patrick Kua, Pramod Sadalage, O'Reilly, 2022.

Public references checked:
- O'Reilly book/TOC: https://www.oreilly.com/library/view/building-evolutionary-architectures/9781492097532/
- Thoughtworks book page: https://www.thoughtworks.com/insights/books/building-evolutionaryarchitectures-second-edition

Purpose: extract the principles that help an **AI Solution Architect / Enterprise AI Architect** build architectures that can change model, provider, prompt, index, tools, data and platform without uncontrolled degradation.

## 1. Core principle retained

An evolutionary architecture supports **guided, incremental change across multiple dimensions**.

For AI, those dimensions include:
- model/provider;
- prompt/context;
- corpus/index;
- tools/agents;
- data contracts;
- API/event contracts;
- runtime/platform;
- security/policy;
- cost/capacity;
- quality/evaluation;
- compliance/retention.

Change is expected. Architecture must make change safe and measurable.

## 2. Fitness functions

A fitness function protects an architectural characteristic by making it observable/testable.

For AI, examples include:
- no confidential request may route to an ineligible provider;
- every machine-consumed LLM response must validate against schema;
- RAG answers must meet citation/grounding thresholds;
- p95 latency must stay within budget;
- cost/useful-answer must stay below an agreed ceiling;
- critical tools must remain least-privilege;
- prompt/model/index changes must pass regression evaluation;
- forbidden provider-specific SDK coupling must not appear outside approved adapters;
- every deployable AI artifact must expose version/provenance metadata.

Created: `AI-ARCHITECTURE-FITNESS-FUNCTIONS.md`.

## 3. Fitness-function categories retained

Useful distinctions:
- **atomic vs holistic** — one component or end-to-end quality;
- **triggered vs continual vs temporal** — CI-time, runtime or periodic review;
- **static vs dynamic** — inspect structure/config or exercise running behavior;
- **automated vs manual** — machine-enforced or architecture/risk review;
- **intentional vs emergent** — explicitly designed or discovered through operations;
- **domain-specific vs cross-cutting** — payment correctness versus generic security/performance.

Not every architecture characteristic can or should be fully automated.

## 4. Automated architectural governance

The book's key contribution is governance through continuous evidence rather than document-only governance.

AI examples:
- CI rejects prompts/models/indexes that fail eval thresholds;
- policy tests reject illegal provider/data combinations;
- API/event contract tests block breaking changes;
- IaC/policy-as-code validates resource/security rules;
- load tests guard performance characteristics;
- SBOM/AI-BOM/license checks guard supply-chain requirements;
- deployment checks require rollback metadata and provenance.

Design Authority still owns exceptions and trade-offs; automation enforces repeatable rules.

## 5. Reversibility and provider change

Architectural decisions should be as reversible as practical.

For AI:
- use model aliases rather than hard-coded endpoint semantics;
- externalize enterprise knowledge from model weights where appropriate;
- version prompts/evals independently;
- isolate provider adapters;
- retain portable business contracts;
- keep authoritative policy outside the LLM;
- define exit/replacement triggers in ADRs.

Deliberate provider coupling is acceptable when its value exceeds exit risk and the decision is explicit.

## 6. Last responsible moment

Do not freeze uncertain technology choices earlier than necessary, but do not postpone high-risk architectural constraints such as:
- data residency;
- privacy/security;
- system-of-record ownership;
- SLOs;
- regulated human oversight;
- irreversible data/model licensing terms.

Use POCs to resolve uncertainty before the decision must become expensive to reverse.

## 7. Architecture for testability

AI architecture should expose seams that allow independent testing of:
- retrieval;
- model response;
- policy;
- tools;
- agent orchestration;
- business rules;
- provider routing;
- failure/fallback behavior.

A monolithic agent that hides all state/tool/model behavior is difficult to govern and evolve.

## 8. Incremental change

Prefer bounded changes:
- one model candidate;
- one prompt version;
- one retrieval strategy;
- one provider adapter;
- one tool contract;
- one policy change.

Evaluate before/after and retain rollback.

Avoid “big bang” AI platform migrations unless constraints require them.

## 9. Data evolution

AI data systems also evolve:
- document metadata schema;
- event schemas;
- embeddings;
- index format;
- retention/classification rules;
- training/eval datasets.

Fitness functions should protect compatibility, deletion lineage, provenance and rebuildability.

## 10. Coupling and bounded contexts

Architectural boundaries should reduce volatile coupling.

For AI:
- domain application owns business semantics;
- AI platform owns reusable cross-cutting capabilities;
- provider adapters isolate vendor volatility;
- tool contracts isolate agent from backend implementation;
- knowledge ingestion isolates source systems from retrieval implementation.

Reuse is effective when abstractions are stable enough; do not centralize highly volatile domain logic into a shared platform prematurely.

## 11. Anticorruption layer for AI providers

Where a cloud/model provider has proprietary semantics, use an adapter/anticorruption layer when portability matters.

The layer may normalize:
- model aliases;
- chat/completion/tool APIs;
- structured output;
- safety/policy metadata;
- usage/cost telemetry;
- errors/timeouts.

Do not hide genuinely provider-specific capabilities if the application intentionally relies on them; record the coupling in an ADR.

## 12. Sacrificial architecture principle

A prototype architecture may be intentionally disposable.

Rule:
- label it as sacrificial;
- do not let temporary shortcuts silently become production architecture;
- capture the assumptions/constraints that must change before production.

This maps directly to the `GENAI-PRODUCTION-MATURITY-MODEL.md`.

## 13. AI-specific evolutionary dimensions

The reference should continually test/protect:
1. quality/evaluation;
2. security/privacy;
3. Responsible AI/compliance;
4. latency/throughput;
5. reliability/resilience;
6. cost/FinOps;
7. provider portability;
8. data/knowledge correctness;
9. observability/auditability;
10. business value.

## 14. POC / automation policy

No mandatory implementation POC from this book.

Automation becomes useful when a concrete program wants to operationalize fitness functions in CI/GitOps/policy-as-code. Existing repositories (GitOps/OpenShift/TradeOps) can provide that runtime evidence later.

## 15. Interview outcomes

An AI Solution Architect should be able to answer:
- How do you prevent an AI architecture from degrading as models/providers change?
- What is an architecture fitness function?
- Which AI architecture properties can be automatically governed?
- How do you preserve reversibility without lowest-common-denominator design?
- When should a provider-specific capability be deliberately accepted?
- What is the last responsible moment for an AI architecture decision?
- How do you evolve schemas, prompts and indexes safely?

## 16. Conclusion

The main contribution is a stronger **continuous architecture governance model**. The repository now has an AI-specific fitness-function catalog that can later be automated selectively through CI, GitOps, policy-as-code and runtime SLO/evaluation gates.
