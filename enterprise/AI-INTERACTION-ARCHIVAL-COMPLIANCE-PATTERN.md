# AI Interaction Archival & Compliance Pattern

Status: **DESIGNED — REFERENCE COMPLIANCE PATTERN**

Purpose: define how an enterprise AI solution can retain enough evidence for audit, incident investigation and regulatory needs without retaining excessive sensitive content by default.

## 1. Principle

Operational telemetry and evidentiary archival are different concerns.

- telemetry answers: performance, errors, traces, capacity, cost;
- archival answers: who asked what, what governed evidence/model/policy was used, what answer/action resulted, who approved it, and whether the record must be retained.

Do not assume that full raw prompts, retrieved context and outputs should always be stored.

## 2. Minimum interaction evidence

Retain, subject to policy:

- correlation/interaction ID;
- timestamp;
- user/application/service identity reference;
- use case / tenant / business domain;
- model alias/version/provider;
- prompt/template version;
- knowledge corpus/index version;
- tool calls and tool-result hashes/references where applicable;
- policy/guardrail decisions;
- answer/action status;
- HITL decision, approver and timestamp where applicable;
- source/citation references;
- latency/cost metadata;
- evaluation/feedback status;
- retention class.

## 3. Content-retention classes

### Class A — Metadata only

Use when full content is unnecessary or too sensitive.

Example: request ID, actor, versions, policy result, status, source IDs, hashes.

### Class B — Redacted interaction

Store prompt/output after removing or tokenizing PII/secrets/sensitive fields.

Use for quality investigations where semantic content is needed but raw data is not justified.

### Class C — Full governed interaction

Use only when legal, regulatory, security or business requirements justify it.

Requires stronger access, encryption, retention and deletion controls.

### Class D — Immutable/legal hold copy

Use only under explicit legal/regulatory process. Normal deletion schedules may be suspended under authorized legal hold.

## 4. Retention decision factors

- data classification;
- regulatory obligation;
- contractual requirement;
- incident/audit need;
- model-risk requirement;
- human-decision accountability;
- business criticality;
- privacy minimization;
- right-to-erasure/deletion constraints;
- source-system retention alignment;
- storage/cost implications.

## 5. Architecture flow

`AI request -> runtime trace -> classification/redaction -> archival policy -> encrypted evidence store -> retention/deletion/legal-hold lifecycle`

The archive is not the live model context store and is not automatically fed back into training/RAG.

## 6. Security controls

- encryption in transit/at rest;
- least-privilege access;
- separate audit/reviewer roles where required;
- immutable/tamper-evident storage where justified;
- access logging;
- tenant/domain segregation;
- secret/credential suppression;
- PII redaction/tokenization;
- export/download controls;
- incident alerting on unauthorized archive access.

## 7. Privacy controls

- collect only justified evidence;
- define purpose for each retained field;
- avoid indefinite retention;
- define deletion propagation;
- separate identity reference from content where possible;
- support lawful access/deletion workflows where applicable;
- document processors/providers and regions;
- do not reuse archived interactions for training without separate purpose/legal/governance approval.

## 8. AI-specific lineage

A retained decision should be reconstructable to the extent policy requires:

`interaction -> model -> prompt -> dataset/corpus/index -> retrieved sources -> tools -> policies -> output -> human decision`

Hashes/references may be preferable to copying sensitive payloads.

## 9. HITL and high-impact actions

For payment, entitlement, production remediation or other high-impact actions, retain at minimum:

- proposed action;
- evidence/source references;
- deterministic policy result;
- approval/rejection identity;
- timestamp;
- executed command/event reference;
- outcome/failure status.

The archive must distinguish model recommendation from human or deterministic final decision.

## 10. Deletion and index implications

If archived material also appears in RAG/index stores, deletion policy must address every derived representation:

- source document;
- extracted text;
- chunks;
- embeddings;
- vector index;
- caches;
- archive copies where deletion is legally permitted;
- backups according to backup-expiry policy.

## 11. Audit retrieval

Authorized audit/investigation queries should support:

- by interaction/correlation ID;
- by user/application/use case;
- by model/prompt/index version;
- by policy decision;
- by time range;
- by HITL decision;
- by incident/reference ID.

Avoid unrestricted semantic search over sensitive archives unless explicitly authorized and governed.

## 12. Evidence versus observability retention

Example separation:

- high-cardinality operational traces: short/medium retention;
- aggregated metrics: longer retention;
- regulated decision evidence: policy-defined retention;
- raw sensitive prompt content: minimum justified retention;
- legal hold: exceptional retention governed separately.

## 13. Architecture review questions

1. Why is each field retained?
2. Is full prompt/context necessary?
3. What is redacted before persistence?
4. Who can retrieve the evidence?
5. Where is it stored geographically?
6. What is the retention period?
7. How is deletion propagated?
8. What happens under legal hold?
9. Can the decision be reconstructed without storing unnecessary raw data?
10. Is archive data excluded from automatic training/reuse?

## 14. POC trigger

No mandatory POC. Build evidence only if a mission requires regulated GenAI, auditability, legal hold, banking/insurance AI decision traceability or compliance validation.
