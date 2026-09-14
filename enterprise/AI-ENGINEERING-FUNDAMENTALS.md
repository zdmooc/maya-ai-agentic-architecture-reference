# AI Engineering Fundamentals Reference

Status: **DESIGNED — THEORETICAL FUNDAMENTALS COMPLETE / IMPLEMENTATION EVIDENCE SEPARATE**

This document fills the foundational AI-engineering theory layer that complements the enterprise architecture material in `ENTERPRISE-AI-THEORETICAL-DESIGN-I13-I20.md`.

It is intentionally vendor-neutral and architecture-oriented. It does not reproduce a book; it captures the concepts an AI Solution Architect should be able to explain, compare and use in architecture decisions.

## 1. AI engineering and application framing

AI engineering focuses on building applications from foundation models rather than training frontier models from scratch.

An architect must distinguish:

- traditional software engineering: mostly deterministic execution;
- ML engineering: train/evaluate/deploy task-specific predictive models;
- AI engineering: compose foundation models with prompts, context, retrieval, tools, workflows, agents, policies, evaluation and feedback;
- AI platform engineering: provide secure, observable, scalable model/data/runtime capabilities to multiple product teams.

A valid AI use case starts with a business outcome and measurable acceptance criteria. Before choosing a model, define users, task, risk, data, latency, availability, quality, cost, privacy, human-oversight and operational constraints.

Use-case progression should prefer the simplest sufficient pattern:

`deterministic software -> prompt-only -> RAG -> workflow -> agent -> fine-tuning`

## 2. Foundation-model fundamentals

### Training data

Model capability is strongly influenced by the distribution, quality, language, domain and recency of its training data. An architect cannot normally inspect all training data for a proprietary model, so model selection must treat provenance/transparency as a decision criterion.

Important distinctions:

- general-purpose vs domain-specific models;
- multilingual capability vs translated behavior;
- public/open-weight vs proprietary/API-only models;
- pretrained capability vs post-trained/aligned behavior.

### Architecture and model size

Most modern LLMs are based on transformer-family architectures. Model size influences capability, memory footprint, latency and serving cost, but larger is not automatically better for every task.

Architectural decisions must compare quality per task against latency, throughput, memory, cost, deployability and governance constraints.

### Post-training

Pretraining produces general language/modeling capability. Post-training adapts behavior using methods such as supervised fine-tuning and preference/alignment methods.

Architecturally, post-training affects instruction following, safety behavior, output style and domain/task performance, but does not remove the need for application-level guardrails and evaluation.

### Sampling and probabilistic generation

A generative model produces a probability distribution over possible next tokens. Generation is therefore probabilistic unless constrained by deterministic decoding or structured-output controls.

Key concepts:

- temperature controls randomness/concentration of token probabilities;
- top-k limits candidate tokens to the k most likely;
- top-p/nucleus sampling limits candidates to a cumulative probability mass;
- deterministic/low-randomness decoding improves repeatability but does not make model knowledge deterministic;
- seeds may improve reproducibility where providers support them, but provider/runtime changes can still alter outputs.

Use low-variance settings for extraction, classification and controlled workflows; allow more diversity only when the business task benefits from it.

### Test-time compute

Some models spend additional inference-time computation on reasoning or search. More test-time compute can improve quality on some tasks but increases latency and cost. It must therefore be governed as a quality/cost/SLA trade-off rather than enabled indiscriminately.

### Structured outputs

Prefer schemas, typed JSON, constrained decoding or function/tool contracts when downstream software depends on model output. Treat free-form text as untrusted input to deterministic systems.

### Probabilistic nature and uncertainty

A fluent answer is not proof of correctness. Architecture must distinguish generation confidence, retrieval evidence, deterministic facts and verified business data. For critical decisions, authoritative systems and deterministic policy remain the source of truth.

## 3. Evaluation methodology fundamentals

Evaluation is a system capability, not a final test step.

### Language-model metrics

Architect-level understanding should include:

- entropy: uncertainty of a probability distribution;
- cross-entropy: difference between predicted probability distribution and observed target sequence;
- perplexity: exponentiated average cross-entropy, useful for language-model fit/comparison under compatible tokenization/data conditions;
- exact match: strict equality where one correct output exists;
- functional correctness: whether generated code/action actually satisfies a test or contract;
- semantic similarity: embedding or model-based comparison where wording can vary.

No single metric is sufficient for an enterprise AI application.

### Embedding-based evaluation

Embeddings map content into vector spaces where semantic similarity can be estimated. They are useful for retrieval and approximate semantic evaluation but can miss factual, security or domain-specific errors.

### LLM/AI-as-judge

A model can score or compare outputs using a rubric. Advantages include scale and ability to evaluate open-ended answers. Risks include judge bias, position bias, self-preference, prompt sensitivity, inconsistency and shared failure modes with the model being evaluated.

Controls include explicit rubrics, reference answers where appropriate, randomized ordering, multiple judges or spot human review, calibration against human labels and versioning of judge model/prompt.

### Comparative evaluation

Pairwise ranking can be easier than absolute scoring but still requires randomized order and enough representative samples. Public benchmarks are signals, not application acceptance tests.

## 4. Evaluating AI systems and model selection

Evaluation criteria must derive from the application.

Typical dimensions:

- domain capability;
- factuality/grounding;
- instruction following;
- structured-output compliance;
- safety and policy adherence;
- retrieval quality;
- tool-use correctness;
- latency and throughput;
- context-window behavior;
- cost;
- privacy/residency;
- operational supportability.

### Model-selection workflow

1. Define application acceptance criteria.
2. Build a representative evaluation dataset.
3. Shortlist candidate models/providers.
4. Evaluate every important system component, not only final answer quality.
5. Compare quality, cost, latency, sovereignty and operations.
6. Decide API vs self-hosted/open-weight deployment.
7. Record the choice in an ADR and define fallback/re-evaluation triggers.

### Build vs buy / API vs self-host

API-hosted models reduce infrastructure burden and may provide leading quality. Private/self-hosted models offer stronger locality/control and potentially predictable economics at scale, but add GPU, serving, patching, model lifecycle and SRE responsibility.

The decision is workload-specific; there is no universal winner.

## 5. Prompt engineering fundamentals

### Prompt roles and context

Distinguish system/instruction context from user input and retrieved/tool data. Treat every external text source as potentially untrusted.

### Zero-shot and few-shot

- zero-shot: instruction without examples;
- few-shot/in-context learning: examples in the prompt demonstrate desired behavior without changing model weights.

Use examples when output format, edge cases or task semantics are difficult to express by instruction alone.

### Context efficiency

Longer context is not automatically better. Excess or irrelevant context increases cost/latency and can reduce answer quality. Context selection should be deliberate, ranked and bounded.

### Good prompt design

- state task and constraints clearly;
- supply authoritative context;
- separate data from instructions;
- decompose complex deterministic workflows into controlled steps;
- request structured output where appropriate;
- define abstention behavior;
- evaluate prompts on regression datasets;
- version prompts like code/configuration.

### Defensive prompt engineering

Threats include direct jailbreaks and indirect prompt injection in retrieved documents, web content or tool responses.

Controls include trust-boundary separation, instruction hierarchy, content sanitization where applicable, tool allowlists, deterministic authorization outside the model, output validation and negative regression tests.

## 6. RAG and agent fundamentals

### RAG

RAG injects external knowledge at request time instead of expecting model weights to contain current or enterprise-private knowledge.

Canonical path:

`query -> policy/ACL -> retrieval -> reranking -> context construction -> generation -> citation/verification`

Important design decisions:

- lexical, vector or hybrid retrieval;
- chunk strategy and metadata;
- embedding model;
- ACL filtering;
- reranking;
- context budget;
- freshness/versioning;
- citation and abstention;
- retrieval and generation evaluation separately.

RAG can extend beyond text to tables, images and multimodal content when extraction and citation quality are governed.

### Agents

An agent is useful when the model must select tools/actions or plan across uncertain multi-step tasks. Do not use an agent where a deterministic workflow is sufficient.

Agent architecture concepts:

- state and goals;
- tools and typed contracts;
- planning/orchestration;
- short/long-term memory where justified;
- stop conditions and budgets;
- human approval for sensitive actions;
- audit and traceability.

Failure modes include looping, tool misuse, hallucinated plans, stale memory, privilege escalation, context poisoning and excessive agency.

## 7. Fine-tuning fundamentals

Fine-tuning changes model behavior/weights. It is not the default solution for missing fresh factual knowledge.

### When fine-tuning can make sense

- stable domain/task behavior;
- consistent style/format;
- specialized instruction following;
- reducing prompt size through learned behavior;
- adapting smaller models for a narrow task.

### When not to fine-tune

Prefer RAG for frequently changing enterprise knowledge, citations and document-level access control. Prefer deterministic software for hard business rules.

### Core training concepts

Training adjusts parameters using backpropagation and gradient-based optimization. Full-parameter tuning is expensive; parameter-efficient methods update a small subset or adapters.

### Numerical precision and quantization

Weights/activations can use reduced precision to lower memory and improve serving/training efficiency, with possible quality trade-offs.

### PEFT / LoRA

LoRA-style methods add low-rank trainable adapters rather than updating all model parameters. They reduce compute/storage requirements and make task-specific variants easier to manage.

### Model merging / multi-task adaptation

Adaptations can sometimes be merged or combined, but interference and evaluation risk require explicit validation.

Every fine-tuned model requires dataset provenance, base-model version, training configuration, evaluation baseline/candidate comparison and rollback path.

## 8. Dataset engineering fundamentals

Model/application quality depends on data quality, coverage and representativeness.

### Curation

Define desired task/domain distribution, user populations, languages, edge cases, negative cases and safety scenarios.

### Quality, coverage and quantity

More data does not compensate for systematically wrong, duplicated or irrelevant data. Coverage must represent the production task and important failure modes.

### Acquisition and annotation

Track source, license/usage rights, consent where applicable, owner, annotation instructions, reviewer process and quality checks.

### Augmentation and synthesis

Synthetic data can increase coverage or generate difficult cases but can amplify model bias/errors. Keep synthetic provenance explicit and validate against real-domain expectations.

### Distillation

A stronger teacher model can generate labels/signals for a smaller student model. Distillation trades teacher cost for potentially cheaper specialized inference, but inherits teacher limitations unless carefully evaluated.

### Processing

Typical controlled pipeline:

`inspect -> classify -> deduplicate -> clean/filter -> normalize -> split -> format -> version -> register`

Protect train/evaluation separation to avoid leakage.

## 9. Inference optimization fundamentals

Optimization is multi-dimensional: latency, throughput, quality, availability, memory and cost.

### Key metrics

- time to first token (TTFT);
- inter-token latency / tokens per second;
- end-to-end latency p50/p95/p99;
- requests/tokens per second;
- concurrent sequences;
- queue time;
- GPU/CPU utilization;
- VRAM/RAM usage;
- cache hit rate;
- cost per request/useful answer.

### Accelerators

GPU/accelerator choice depends on model size, precision, memory bandwidth, concurrency and economics. GPU utilization alone does not prove efficient service.

### Model optimization

Techniques include smaller model selection, quantization, distillation and task-specific adaptation, always evaluated for quality regression.

### Service optimization

Architectural levers include batching, continuous batching where supported, KV/prefix/semantic caches, autoscaling, routing, context compression, request prioritization and fallback.

Optimization must be benchmarked against representative workload; estimates are not runtime evidence.

## 10. AI engineering architecture and user feedback

A mature application typically evolves through these layers:

`business use case -> context -> guardrails -> model gateway/router -> cache -> model/RAG/agents/tools -> deterministic controls/HITL -> observability/evaluation -> feedback -> controlled improvement`

### Context enhancement

Use authoritative state, retrieved evidence and tool results to reduce reliance on model memory.

### Guardrails

Guardrails exist before, during and after model execution: identity/authorization, data policy, prompt/tool policy, output validation, business-rule enforcement and human approval.

### Model router and AI gateway

The gateway centralizes authentication, quotas, budgets, PII controls, auditing and provider abstraction. The router selects among eligible models based on quality, policy, cost, latency, availability and data-placement constraints.

### Caching

Caching can reduce cost/latency but must account for identity, policy, data freshness, prompt/model/index versions and sensitive-data isolation.

### Monitoring and observability

Trace the complete request across API, retrieval, model, agent/tool, policy and business decision layers. Do not log sensitive prompt/context content by default.

### Pipeline orchestration

Version and coordinate prompts, datasets, indexes, models, policies and evaluation gates. Promotion requires evidence, not just successful deployment.

### User feedback

Explicit ratings alone are incomplete. Capture structured corrections and operational signals, triage root causes and convert accepted feedback into regression/evaluation data. Feedback must not automatically retrain or alter production behavior without governance.

## 11. Architecture decision checklist

For every new AI use case, an architect should be able to answer:

1. What business outcome is being improved?
2. Why is AI required rather than deterministic software/search?
3. What model capability is required?
4. Prompt-only, RAG, workflow, agent or fine-tuning — and why?
5. What data enters model context and who is entitled to it?
6. How is the system evaluated before release?
7. What is the authoritative source of truth?
8. What can the model/tool change and what requires HITL?
9. What are SLO, latency, availability and cost limits?
10. Which provider/deployment locations are eligible?
11. How are model/prompt/data/index/tool versions traced?
12. How are rollback, incident response and provider outage handled?
13. How is feedback converted into controlled improvement?
14. Which claims are measured versus estimated?

## 12. Mapping to the reference repository

| Fundamentals area | Primary repository coverage |
|---|---|
| AI application framing | Architecture Vision, I15 |
| Foundation-model theory | this document + I18 model/vendor strategy |
| Evaluation methodology | this document + I5/I14 |
| Model/system selection | this document + I18 |
| Prompt engineering | this document + I13/I16 |
| RAG | I6 + I13 |
| Agents/tools/MCP | I6/I7 + I16 |
| Fine-tuning theory | this document + I17 future workload class |
| Dataset engineering | this document + I13/I14 |
| Inference optimization | I10 + I17 |
| AI architecture/gateway/cache | I16/I18 |
| Observability/feedback | I8 + I14 |

## 13. POCs remain demand-driven

This fundamentals layer does **not** create a new mandatory implementation sequence.

Potential POCs are activated only when useful:

- model/evaluation mission -> model benchmark + evaluation pipeline;
- prompt/GenAI application mission -> prompt registry/regression lab;
- RAG mission -> I13/I14;
- fine-tuning/LLM platform mission -> LoRA comparison lab under I17;
- inference/platform mission -> I17 serving benchmark;
- AI security/gateway mission -> I16;
- hybrid/model-provider mission -> I18.

Until activated, these remain architecture/theory knowledge, not implementation claims.
