# AI Engineering — Official Book/Repo Alignment

Status: **DESIGNED — CHAPTER-BY-CHAPTER ALIGNMENT COMPLETE / POCs DEMAND-DRIVEN**

Purpose: verify that `maya-ai-agentic-architecture-reference` covers the architectural and engineering fundamentals exposed by Chip Huyen's *AI Engineering* and its official repository `chiphuyen/aie-book`, without copying the book or treating the repository as implementation evidence.

Official reference checked:

- https://github.com/chiphuyen/aie-book
- `ToC.md`
- `chapter-summaries.md`
- `resources.md`
- `prompt-examples.md`

This document is a mapping and gap-closure reference. It is not a reproduction of the book.

## Executive conclusion

After alignment, the reference repository covers the ten major areas of the book at **AI Solution Architect / AI Platform Architect theory level**.

The main gaps found during the audit were not enterprise-architecture gaps. They were foundational details that needed to be made explicit: LM -> LLM -> foundation-model evolution, scaling-law concepts, public benchmark limitations, fine-tuning memory composition, agent memory/evaluation, prompt leakage/reverse-prompt risks, and explicit/implicit feedback limitations.

These are captured below as architecture knowledge. They do **not** create mandatory new POCs.

---

## Chapter 1 — Building AI applications with foundation models

**Status: COVERED after supplement**

Existing coverage:

- AI Engineering vs ML Engineering;
- business-first use-case framing;
- measurable acceptance criteria;
- simplest-sufficient-pattern rule;
- Enterprise AI architecture/design authority in I15.

Additional fundamentals retained from the official structure:

- language model -> large language model -> foundation model is an evolution in scale, training approach, modality and reusable capabilities;
- self-supervision enables learning from large unlabeled corpora;
- foundation models can support coding, writing, conversational interfaces, information aggregation, knowledge management, document processing, multimodal generation and workflow automation;
- a use case must be evaluated before implementation: business value, feasibility, quality target, risk, data, latency, cost, privacy, maintenance and human oversight;
- planning includes expectation setting, milestones, operational ownership and maintenance, not only model selection;
- AI Engineering sits between model/platform capabilities and application/product engineering.

Architect interview rule: be able to explain **why AI is justified**, not only how to deploy it.

Future POC: none by default. Activate only when a mission requests product framing, use-case portfolio or AI transformation governance.

---

## Chapter 2 — Understanding foundation models

**Status: COVERED after supplement**

Existing coverage:

- training-data quality/domain/language;
- transformer-family architecture;
- model size;
- SFT/post-training;
- sampling, temperature, top-k, top-p;
- test-time compute;
- structured outputs;
- probabilistic behavior.

Additional fundamentals:

### Scaling dimensions

A large model is characterized not only by parameter count but also by training-token volume and compute budget. More parameters alone do not guarantee compute-optimal training.

Architectural implication:

`quality target + data availability + training/inference budget + latency + memory + governance -> model class decision`

### Scaling laws

Scaling laws describe empirical relationships among model size, training data and compute. They are planning tools, not guarantees. For application architects, their importance is mainly to understand why bigger models cost more and why smaller well-adapted models can sometimes be preferable.

### Transformer limitations

Transformers provide powerful parallel sequence modeling but introduce context, compute and memory costs. Long context is not free and should not replace retrieval, summarization or deliberate context construction.

### Post-training distinction

- SFT teaches target behavior/examples;
- preference optimization aligns outputs toward preferred behavior;
- post-training does not replace application-level policy, security or evaluation.

Future POC: only if a role requires model adaptation, private-model selection or model-platform engineering.

---

## Chapter 3 — Evaluation methodology

**Status: COVERED**

Existing coverage:

- entropy;
- cross-entropy;
- perplexity;
- exact/functional correctness;
- semantic similarity and embeddings;
- AI-as-judge;
- pairwise/comparative evaluation.

Additional fundamentals:

- bits-per-character and bits-per-byte are alternate normalized language-model measures useful in compatible comparison contexts;
- human evaluation remains important for sanity checks and high-impact subjective criteria;
- AI judges must themselves be versioned, calibrated and evaluated;
- judge scores from different models/prompts are not automatically comparable;
- exact evaluation should be preferred whenever a deterministic contract exists.

Architect rule:

`exact tests first -> deterministic domain metrics -> retrieval metrics -> calibrated subjective/LLM judge -> human review where needed`

Future POC: model/evaluation benchmark only when a mission needs GenAIOps/evaluation evidence.

---

## Chapter 4 — Evaluating AI systems and model selection

**Status: COVERED after supplement**

Existing coverage:

- domain capability;
- generation/instruction following;
- factuality/grounding;
- safety;
- latency/throughput/cost;
- build vs buy;
- API vs self-host;
- private evaluation dataset;
- evaluation pipeline.

Additional fundamentals:

### Public benchmark limitations

Public benchmarks can help reject weak candidates, but they should not select the production model by themselves because:

- benchmark data can leak into training data;
- aggregate leaderboards may hide application-specific weaknesses;
- benchmark weighting may not match business priorities;
- provider/model versions change.

The production decision should therefore use a private, representative evaluation set plus operational constraints.

### Evaluation components

Evaluate the components separately where possible:

`retrieval -> prompt/context -> model -> tools -> policy -> final answer/action`

This makes root-cause analysis possible.

Future POC: private model leaderboard if required by a mission or provider-selection decision.

---

## Chapter 5 — Prompt engineering

**Status: COVERED after supplement**

Existing coverage:

- zero/few-shot;
- system/user roles;
- context efficiency;
- explicit instructions;
- decomposition;
- structured output;
- prompt versioning;
- prompt injection/jailbreak defenses.

Additional fundamentals:

- prompts are versioned application assets, not ad-hoc strings;
- iteration must be driven by evaluation data rather than subjective preference;
- proprietary system prompts can leak and must not be treated as secrets or security boundaries;
- reverse-prompt/reconstruction risk should be considered for sensitive internal instructions;
- information extraction is best constrained by schemas and deterministic validation;
- prompt-management tools are useful only if they integrate with evaluation, versioning and promotion controls.

### Practical prompt archetypes identified in the official repository

Useful future lab categories, without copying third-party prompts:

- financial assistant;
- task classifier/router;
- enterprise data classification;
- governed text-to-SQL;
- product ideation;
- content moderation/safety.

Future POC: prompt-regression lab only when targeting a GenAI application mission.

---

## Chapter 6 — RAG and agents

**Status: STRONG / COVERED**

Existing repository strength:

- governed RAG;
- ACL/filtering;
- hybrid retrieval concepts;
- reranking;
- citations/abstention;
- LangGraph agents;
- MCP-shaped tool boundary;
- HITL;
- deterministic risk/policy override prevention;
- agent failure modes.

Additional fundamentals:

### Retrieval families

- lexical/term retrieval such as BM25 is an important baseline;
- vector retrieval uses embeddings and approximate nearest-neighbor indexes;
- hybrid retrieval combines lexical and semantic signals;
- reranking trades extra latency/cost for better top-k relevance.

### Agent memory

Memory should be separated conceptually into:

- transient working/context memory;
- durable task/user/application state;
- retrieved external knowledge;
- audit/evidence history.

Do not let untrusted conversational memory silently become authoritative business state.

### Agent evaluation

Evaluate tool selection, argument correctness, planning success, stop conditions, loop behavior, policy compliance and final task outcome separately.

Future POC: already represented by I6/I7 and I13. No new POC unless a mission asks for a different domain.

---

## Chapter 7 — Fine-tuning

**Status: THEORY COVERED / POC DEFERRED**

Existing coverage:

- when to fine-tune / when not to;
- RAG vs fine-tuning;
- backpropagation;
- precision/quantization;
- PEFT/LoRA;
- model merging;
- evaluation and provenance.

Additional fundamentals:

### Training-memory composition

Fine-tuning memory is not only model weights. Capacity planning must consider, depending on method/runtime:

- weights;
- gradients;
- optimizer states;
- activations;
- temporary buffers/runtime overhead.

This is why full fine-tuning can require much more accelerator memory than inference.

### PEFT decision

PEFT/LoRA reduces trainable-parameter and storage cost. Quantized-base approaches such as QLoRA can further reduce memory, but quality and runtime compatibility must be evaluated.

### Multi-task/model merging

Combining adaptations can reduce the number of deployed variants but may introduce interference. Treat merging as a candidate requiring regression evaluation, not as a free composition mechanism.

Future POC: one LoRA/PEFT comparison only when a mission requires model adaptation/private AI.

---

## Chapter 8 — Dataset engineering

**Status: COVERED**

Existing coverage:

- quality;
- coverage;
- quantity;
- acquisition/annotation;
- synthetic data;
- distillation;
- inspection;
- deduplication;
- cleaning/filtering;
- formatting/versioning;
- leakage protection.

Additional architectural rules:

- dataset size must be justified by task coverage and marginal quality gain, not by volume alone;
- annotation guidelines are versioned assets;
- synthetic data must preserve provenance and must not contaminate evaluation sets;
- training, validation and evaluation datasets require explicit separation and lineage;
- data rights/license, retention, residency and deletion obligations belong in the dataset contract.

Future POC: dataset-engineering lab only for fine-tuning/evaluation/data-platform missions.

---

## Chapter 9 — Inference optimization

**Status: STRONG / COVERED**

Existing coverage:

- TTFT;
- tokens/s;
- p50/p95/p99;
- queue/concurrency;
- GPU/VRAM;
- quantization/distillation;
- batching/continuous batching;
- caches;
- routing;
- context compression;
- autoscaling/fallback;
- OpenShift AI/KServe/vLLM capacity architecture.

Additional fundamentals:

### Prefill and decode

Inference has different phases. Prompt/context processing and autoregressive token generation stress hardware differently. Capacity planning should not collapse everything into one average latency number.

### Memory and bandwidth

Model weights, KV cache and concurrent sequence state compete for accelerator memory. Memory bandwidth can be as important as raw compute for generation workloads.

### Accelerator decision

Select accelerators based on supported precision, memory capacity/bandwidth, model/runtime compatibility, concurrency, availability, operational support and total cost rather than brand alone.

Future POC: I17 benchmark only when hardware or a client mission justifies measured evidence.

---

## Chapter 10 — AI engineering architecture and user feedback

**Status: STRONG / COVERED after supplement**

Existing coverage:

- context enhancement;
- guardrails;
- AI Gateway;
- Model Router;
- caching;
- agents;
- monitoring/observability;
- pipeline orchestration;
- feedback loop;
- FinOps/GreenOps;
- enterprise governance.

Additional fundamentals:

### Feedback types

- explicit feedback: rating, correction, accept/reject, reason code;
- implicit feedback: abandonment, retry, edit, escalation, task completion;
- conversational feedback: corrections and objections expressed naturally in dialogue;
- operational feedback: incident, policy veto, fallback, tool failure, latency breach.

### Feedback limitations

Engagement is not automatically quality. Feedback can be sparse, biased toward extreme experiences, manipulated, role-dependent or delayed. It must therefore be interpreted with product/domain context.

### Controlled feedback lifecycle

`capture -> classify -> triage -> label -> root cause -> candidate change -> offline evaluation -> controlled promotion`

Never allow raw user feedback to mutate prompts, knowledge bases or models directly in production without governance.

Future POC: I14 feedback loop when requested.

---

# Practical alignment with the official GitHub repository

The official repository currently provides four especially useful resource types:

1. detailed table of contents and chapter summaries;
2. curated reading/research resources;
3. real-world prompt examples;
4. study notes/community material.

The official repository explicitly states that the book is **not a tutorial book** and does not contain large amounts of code. Therefore our reference should not attempt to manufacture code for every chapter merely to look complete.

Our differentiation is intentional:

`AI Engineering fundamentals`
`+ Enterprise Architecture / Design Authority`
`+ Agentic AI / MCP / HITL`
`+ OpenShift / OpenShift AI / KServe / vLLM`
`+ Hybrid Multi-Cloud`
`+ Security / Responsible AI / AI-BOM`
`+ Banking / Payments / MQ / Kafka`
`+ FinOps / GreenOps / SRE`

---

# Final coverage matrix

| Book area | Repository status | Primary location | Runtime POC |
|---|---|---|---|
| AI application framing | COVERED | Fundamentals + I15 | optional |
| Foundation models | COVERED | Fundamentals + this alignment | optional |
| Evaluation methodology | COVERED | Fundamentals + I5/I14 | demand-driven |
| AI-system/model evaluation | COVERED | Fundamentals + I14/I18 | demand-driven |
| Prompt engineering | COVERED | Fundamentals + I13/I16 | demand-driven |
| RAG | STRONG | I6 + I13 | existing / extend on demand |
| Agents/tools/memory | STRONG | I6/I7 + this alignment | existing / extend on demand |
| Fine-tuning | THEORY COVERED | Fundamentals + I17 | deferred |
| Dataset engineering | COVERED | Fundamentals + I13/I14 | deferred |
| Inference optimization | STRONG | I10 + I17 | benchmark deferred |
| Architecture/gateway/cache | STRONG | I16/I18 | deferred |
| Feedback | COVERED | I14 + this alignment | deferred |

## Decision

There is no reason to create a new repository for this book.

`maya-ai-agentic-architecture-reference` remains the source of truth. The book and its official GitHub repository are external learning/reference sources. New executable work is triggered only by a concrete mission, interview, business use case or platform requirement.
