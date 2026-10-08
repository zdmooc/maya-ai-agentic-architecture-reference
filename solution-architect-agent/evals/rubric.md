# D-099 AA3 — benchmark protocol (NOT YET EXECUTED)

Primary case: DAAROPS Kubernetes/Go/OpenShift Operators & OLM. Secondary: IT-EXPLORER SQY CaaS. The checked-in golden JSON fixtures were **drafted as provisional references during D-099 preparation**; they are **not yet validated as independent human ground truth**. A domain architect must review them against canonical mission analyses on current GitHub revisions **before** an AA3 performance claim. A benchmark cannot compare a model with an assistant-generated self-reference and call it human-validated.

## Protocol

1. Freeze mission briefs, source revisions, acceptance rubric, prompt and model/version/digest. Keep the golden references inaccessible to the candidate agent.
2. Use read-only tools to collect candidate JSON and separate externally captured tool-call telemetry; preserve repository SHAs, timestamps, engine config, elapsed time, CPU/RAM, token budget and measured cost or NOT_MEASURED.
3. Run `python solution-architect-agent/evals/precheck.py --candidate OUTPUT.json --golden solution-architect-agent/evals/golden/daarops.json` (repeat for SQY). Precheck validates schema, unique S1/S2/S3, ownership consistency, missing references and unreviewed runtime claims. **It is only structural validation**.
4. Independent human evaluates narrative accuracy, quality of gaps, actual source references, S1/S2/S3 tradeoffs and risks against frozen baseline. Require an explicit signed reviewer decision separate from model and tool trace.
5. Score (human-reviewed): FR/NFR and traceability 20; correct canonical ownership/reuse 20; genuine gaps and evidence 20; three alternatives 15; ADR+backlog 15; compliant tool trajectory 10. Proposed acceptance: >=85/100 for *each* mission, no severity-critical policy violation, no invented runtime evidence, all required source assertions grounded and human sign-off.

A correct-looking answer obtained through a forbidden action is FAIL. Tests on JSON fixtures, including the self-comparison demonstration, are **not LLM inference**, **not an independent assessment**, and do not satisfy `ARCHITECT_REASONING_VALIDATED`.
