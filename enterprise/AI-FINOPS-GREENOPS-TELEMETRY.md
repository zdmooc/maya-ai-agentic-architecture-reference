# AI FinOps / GreenOps Telemetry & Unit Economics

Status: **DESIGNED — ARCHITECTURE REFERENCE / ENERGY-CARBON VALUES REQUIRE MEASUREMENT**

## Purpose

Deepen the operational FinOps/GreenOps layer for AI platforms. The goal is to connect infrastructure consumption, tokens, energy and business value without confusing estimates with measured evidence.

## Four counters

| Layer | Primary counters | Example decision |
|---|---|---|
| Infrastructure | GPU-h, vCPU-h, GiB-h, storage | right-size, pool, placement |
| AI | input/output tokens, requests, context, cache | prompt/RAG/model optimization |
| Energy | kWh, power, GPU energy | scheduling, power/capacity optimization |
| Business value | successful answers/incidents/documents | stop/continue, service tier |

## Unit economics

Useful units include:

- cost / successful request;
- cost / useful answer;
- cost / 1M tokens;
- cost / incident assisted/resolved;
- cost / 1000 documents/pages;
- cost / training run accepted;
- Wh / request or 1M tokens;
- gCO2e / request only when methodology is declared.

`cost_per_useful_answer = total_service_cost / accepted_or_successful_answers`

A lower GPU-hour price is not automatically better if it increases latency, retries, token use or failure rate.

## Allocation taxonomy

Every production workload should carry ownership and allocation metadata such as:

- product;
- business unit;
- cost center;
- environment;
- owner;
- model/runtime;
- service tier.

For shared platforms, decide explicitly how idle capacity, common services, licenses and DR capacity are allocated.

## GPU telemetry

Observe more than average utilization:

- accelerator utilization;
- HBM/VRAM used and pressure;
- power draw and energy counter where available;
- temperature and ECC/RAS signals;
- queue depth/wait time;
- model/runtime identity;
- tokens/s and successful requests;
- replica/pod/namespace attribution.

A GPU at high utilization can still deliver poor goodput if SLOs are missed or requests retry.

### Goodput

`GPU_goodput_efficiency = GPU_time_serving_SLO_compliant_work / GPU_time_allocated`

Use goodput rather than raw utilization when comparing configurations.

## Token telemetry

Track at least:

- system/prompt tokens;
- RAG/context tokens;
- user input tokens;
- generated output tokens;
- retries/aborted requests;
- prefix/semantic cache hit rate where applicable;
- tool-call count for agents.

Runaway context and agent loops are cost and security problems simultaneously.

## Serving optimization levers

Evaluate one change at a time and keep quality/SLO gates:

- model size/tier routing;
- quantization;
- continuous batching;
- context cap;
- RAG top-K and reranking;
- prompt compaction;
- prefix/semantic caching;
- replica count/autoscaling;
- scale-to-zero for non-critical workloads;
- GPU sharing only when isolation/performance permit.

## Training optimization levers

- queue/admission and priority;
- checkpoint frequency;
- mixed precision;
- LoRA/QLoRA vs full fine-tuning;
- data-loader/storage tuning;
- scheduling to available capacity;
- stopping failed/non-improving runs.

## Budgets and guardrails

Define budgets per product/team/environment for:

- GPU-hours;
- tokens;
- external provider spend;
- storage/log retention;
- training runs.

Possible automated controls:

- warn at budget threshold;
- cap context/output length;
- reject unowned production workloads;
- require approval for high-cost models/runs;
- stop runaway agent loops;
- enforce quotas through platform policy.

## Energy and carbon

Distinguish:

- measured accelerator/server energy;
- allocated datacenter energy;
- estimated cooling/PUE effects;
- grid/carbon-intensity assumptions;
- embodied/manufacturing impact if included.

Every carbon number must state boundary, period, data source and whether it is measured or estimated.

## FinOps/GreenOps decision rule

An optimization is accepted only if required quality, security and SLO gates remain satisfied.

Do not claim a configuration is greener solely because it uses fewer tokens if it causes more failed retries, longer runtime or lower useful outcome rate.

## Required evidence before `VERIFIED`

- workload ownership/tags;
- cost allocation model;
- token and GPU telemetry;
- quality/SLO correlation;
- baseline vs optimized comparison;
- explicit energy/carbon methodology;
- measured or clearly labeled estimated figures;
- dashboard/report reproducible from source metrics.