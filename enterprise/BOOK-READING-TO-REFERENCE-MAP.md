# Book Reading -> Architecture Reference Map

Status: **LEARNING NAVIGATION**

This map keeps the two purposes separate:

- **Books**: understand concepts in depth.
- **Reference repository**: reuse architecture decisions, patterns and evidence criteria.

## Recommended reading sequence

### Foundation

1. Tome 1 — Architect role and end-to-end AI platform.
2. Tome 1 — ML fundamentals.
3. Tome 1 — Transformers and LLM lifecycle.
4. Tome 1 — tokens, embeddings, context.
5. Tome 1 — RAG vs fine-tuning/LoRA.

Then use the repository for the corresponding reusable architecture artifacts:

- `AI-ML-SOLUTION-ARCHITECTURE-LIFECYCLE.md`
- `AI-ENGINEERING-FUNDAMENTALS.md`
- `AI-ARCHITECTURE-PATTERN-CATALOG.md`
- `ENTERPRISE-RETRIEVAL-VECTOR-DATABASE-ARCHITECTURE.md`

### Agentic AI and integration

Read the learning chapters on agents, tool calling, MCP and enterprise SI integration, then use:

- `../architecture/AGENTIC-MCP-ARCHITECTURE.md`
- `AGENT-AUTONOMY-HITL-MODEL.md`
- `IDENTITY-PROPAGATION-MCP-IAM.md`
- `AI-SI-INTEGRATION-CONTRACTS.md`

### OpenShift AI / private AI platform

Read the RHOAI/OpenShift chapters, then use:

- `RHOAI-PLATFORM-DEEP-DIVE.md`
- `AI-PLATFORM-PHYSICAL-GPU-ARCHITECTURE.md`
- `DISTRIBUTED-TRAINING-FINETUNING-LIFECYCLE.md`
- I17 in `ENTERPRISE-AI-THEORETICAL-DESIGN-I13-I20.md`

### Production

Read the Vector DB, security, LLMOps, GPU sizing, DR and FinOps chapters/labs, then use:

- `ENTERPRISE-RETRIEVAL-VECTOR-DATABASE-ARCHITECTURE.md`
- `AI-ZERO-TRUST-SUPPLY-CHAIN-CONTROLS.md`
- `GENAI-SRE-SLO-ERROR-BUDGET.md`
- `AI-PLATFORM-HA-DR-MULTICLUSTER.md`
- `AI-FINOPS-GREENOPS-TELEMETRY.md`

## Learning-to-proof rule

Reading a chapter does not change repository maturity.

`read/understood != implemented != tested != deployed != verified`

Only code, tests, deployments, measurements and evidence packs move a capability beyond `DESIGNED`.