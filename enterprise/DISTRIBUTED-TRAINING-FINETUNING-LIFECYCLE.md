# Distributed Training, Fine-Tuning & Model Lifecycle

Status: **DESIGNED — ARCHITECTURE REFERENCE / NO GPU TRAINING CLAIM**

## Purpose

Complete the reference for the model-building side of an enterprise AI platform: pipelines, experiment tracking, queue/admission, distributed training, checkpointing, SFT/LoRA/QLoRA, evaluation, registry and promotion.

## Decision rule

Use the least invasive technique that can meet the requirement:

`prompting -> RAG -> PEFT/LoRA -> full fine-tuning -> continued pretraining -> training from scratch`

Knowledge freshness is usually a RAG problem. Fine-tuning is primarily justified when behavior, format, task specialization or stable capabilities must change.

## Lifecycle

`dataset -> validation -> train/adapt -> checkpoint -> evaluate -> experiment tracking -> registry -> approval -> canary -> production -> monitor -> rollback/retire`

Every promoted model must be traceable to its dataset, code commit, training configuration, runtime image, metrics and approval decision.

## Pipeline responsibilities

Keep concerns separate:

- **Pipeline engine**: orchestrates reproducible steps.
- **Experiment tracker**: parameters, metrics, runs and comparisons.
- **Object storage**: datasets, checkpoints and model artifacts.
- **Model registry**: model/version metadata, lineage, approval state and discoverability.
- **Queue/admission layer**: resource fairness and capacity control.
- **Git**: source, configuration, review, policy and release references.

## Dataset governance

Minimum controls:

- explicit schema;
- immutable dataset version and checksum;
- train/validation/test split;
- leakage and near-duplicate checks;
- PII/secrets/legal-use review;
- language/domain coverage;
- owner and retention policy;
- frozen test set for comparable evaluation.

## SFT / LoRA / QLoRA

### SFT

Supervised Fine-Tuning modifies model behavior using labeled/instruction examples. It has higher compute/storage cost and stronger lifecycle obligations.

### LoRA

Low-Rank Adaptation keeps the base model frozen and trains small adapter matrices. Benefits include smaller trainable state and faster iteration, but the adapter must remain compatible with its exact base-model version.

### QLoRA

QLoRA reduces training memory by quantizing the base model during adaptation while training low-rank adapters. Validate quality, backend/runtime support and merge/serving strategy.

## Distributed training

Architecture must define:

- job API/operator/runtime;
- GPU/node count and topology;
- collective communication backend;
- queue/admission policy;
- checkpoint frequency/location;
- restart/preemption behavior;
- data feed path;
- observability and cost attribution.

### Parallelism

- Data Parallel: replicate model, partition batches.
- Tensor Parallel: split tensor operations across accelerators.
- Pipeline Parallel: split model stages.
- FSDP/ZeRO-like sharding: shard parameters/gradients/optimizer state.
- Expert Parallel: route MoE experts across devices.

Each pattern has different communication and memory behavior. Benchmark the target model/runtime/topology.

## Kueue/admission concepts

Queue/admission controls the right to consume scarce resources; it does not create GPU capacity.

Define:

- workload classes;
- ResourceFlavor/node class where applicable;
- cluster-level quota pools;
- namespace/local queues;
- priority/preemption policy;
- fair sharing between teams/environments.

## Checkpointing and recovery

Checkpoints must live outside ephemeral compute and support an explicit restart process.

Measure:

- checkpoint write time;
- checkpoint size;
- restore time;
- lost work window;
- recovery RTO after pod/node interruption.

For long jobs, checkpointing is part of availability architecture, not an implementation detail.

## Evaluation and promotion

Compare baseline and candidate on a frozen set. Promotion gates should include the dimensions relevant to the use case:

- task quality;
- safety/security regressions;
- latency/throughput;
- memory footprint;
- token/compute cost;
- robustness;
- explainability/fairness where applicable.

A candidate that improves one score but violates security, latency or cost gates is not approved.

## Release identity

A deployable model release should identify:

- base model/version/digest;
- adapter/model artifact digest;
- tokenizer;
- dataset version;
- training code commit;
- hyperparameters;
- training runtime/container digest;
- evaluation dataset/version;
- evaluation result;
- approval state.

## Failure drills

At minimum test:

- GPU OOM;
- dataset/schema corruption;
- job interruption;
- lost worker/node;
- checkpoint restore;
- registry unavailable;
- candidate regression;
- rollback to last approved model.

## Required evidence before `VERIFIED`

- executable pipeline or training job;
- captured lineage;
- reproducible evaluation;
- queue/admission evidence where used;
- checkpoint/restart evidence;
- registry promotion evidence;
- serving/rollback evidence for the approved candidate.