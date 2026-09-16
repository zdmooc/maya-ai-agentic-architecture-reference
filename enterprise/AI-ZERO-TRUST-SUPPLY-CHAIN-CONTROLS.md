# AI Zero Trust & Supply Chain Controls

Status: **DESIGNED — ARCHITECTURE REFERENCE / PRODUCT VERSIONS MUST BE REVALIDATED**

## Purpose

Deepen the AI security architecture from policy principles to platform controls spanning users, workloads, models, RAG data, tool gateways, containers and deployment supply chain.

## Security premise

The LLM is never a security boundary. Model output, retrieved text and tool-call arguments are untrusted inputs that require deterministic validation.

## Trust planes

Protect separately:

- human identity;
- workload identity;
- network path;
- code and dependencies;
- container/runtime image;
- model artifact;
- dataset/corpus/index;
- agent/tool capability;
- secrets/keys;
- human approval record.

## Human vs workload identity

Use different identities and permissions:

`user OIDC/MFA -> application principal -> policy -> service account/workload identity -> backend credential`

Avoid shared local accounts, default ServiceAccounts and permanent broad administrator credentials.

## Network Zero Trust

Baseline:

- default-deny ingress/egress where practical;
- explicit service-to-service allowlists;
- mTLS/service identity where risk warrants it;
- restricted model/provider egress;
- separated admin and workload paths;
- audited break-glass procedure.

Encryption alone is not network Zero Trust; destination and identity restrictions matter.

## Supply-chain path

`commit -> review -> build -> SBOM -> vulnerability scan -> provenance/attestation -> sign -> policy admission -> deploy immutable digest`

Minimum blocking gates may include:

- secret detection;
- branch/review policy;
- dependency/license policy;
- SBOM availability;
- critical vulnerability threshold;
- provenance/build identity;
- signature verification;
- immutable digest promotion.

## AI-BOM extension

Software SBOM is necessary but insufficient. Record an AI-BOM linking:

- application/service;
- container/runtime digest;
- model/base/adapters and hashes;
- tokenizer;
- prompt/system instruction version;
- dataset/corpus version;
- embedding model;
- vector index version;
- tool/MCP registry version;
- policies/guardrails;
- licenses/owners/provenance.

## Model artifact controls

Validate:

- trusted source;
- immutable digest/hash;
- license/usage rights;
- malware/unsafe serialization risk where relevant;
- approved registry path;
- promotion state;
- signature/attestation when supported;
- rollback target.

## RAG controls

Protect against:

- unauthorized retrieval;
- poisoned documents;
- indirect prompt injection;
- stale/retired source versions;
- tenant crossover;
- hidden sensitive metadata.

Use provenance, ingestion approval, pre-retrieval ACL, source/version citations and deletion/rebuild lineage.

## Agent / MCP controls

For every tool:

- narrow schema;
- allowlist;
- explicit scope;
- resource/tenant restrictions;
- timeout/rate limit;
- idempotency for side effects;
- audit/redaction;
- HITL for privileged actions;
- post-condition verification.

Never expose unrestricted shell, arbitrary SQL, unrestricted URL fetch or generic cluster-admin mutation to a general-purpose agent.

## Platform enforcement

Possible OpenShift/platform control layers include:

- RBAC;
- SCC/pod security;
- NetworkPolicy;
- admission/policy-as-code;
- runtime/container security tooling;
- software trust/signature tooling;
- external secret management;
- OpenShift AI guardrail/governance components.

Named products and versions are implementation choices and must be checked against the actual supported platform release.

## Audit evidence

For sensitive actions capture:

- user/principal;
- workload identity;
- model/prompt/tool versions;
- policy decision;
- approval record if required;
- target and arguments, redacted as needed;
- resulting side effect;
- post-condition verification;
- trace/correlation ID.

## Red-team scenarios

Minimum regression set:

- direct prompt injection;
- indirect injection in document/tool output;
- poisoned RAG document;
- ACL bypass attempt;
- unauthorized tool call;
- privilege escalation;
- token/credential replay;
- tool argument injection;
- malicious tool result;
- excessive agency;
- HITL bypass;
- secret/data exfiltration;
- unbounded consumption/agent loop.

## Required evidence before `VERIFIED`

- threat model and trust boundaries;
- least-privilege RBAC tests;
- NetworkPolicy/egress tests;
- SBOM/provenance/signature evidence;
- negative admission test;
- RAG ACL and poisoning tests;
- agent/tool authorization and HITL tests;
- correlated audit trail.