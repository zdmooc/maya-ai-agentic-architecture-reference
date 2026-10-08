# Blind benchmark case — DAAROPS (AA3)

**Case ID:** DAAROPS. **Data:** synthetic/reworded public-facing mission signal, no client secrets.

An architect / Platform Engineer is asked to assess a Kubernetes/OpenShift service in an enterprise setting. The priority is **Go operators**, CRD/controller-runtime, reconciliation, GitOps (Argo CD), Operator Lifecycle Manager and Day-2. The requester mentions a recent operator-focused recruiter discussion and expects a technically credible, evidence-based 12–15 minute demonstration.

Deliverable: extract FR/NFR, identify which existing MayaBank repositories already own the capabilities, assess existing code/tests/CI/runtime evidence against open PRs, explain real gaps, compare S1/S2/S3, draft one **PROPOSED** ADR, and propose a bounded demo/POC plan. Separate Kind and CRC/OpenShift proof; do not invent production or multi-node HA.

**Repository discovery entrypoint:** `zdmooc/cadrage_202682030`, main current revision. Do not assume any particular target repository before independently reading the portfolio. Read only allowlisted sources and current PRs; deny unauthorized tool calls.

Expected output: candidate JSON matching `solution-architect-agent/method/assessment.schema.json`. Record which sources and commits were actually inspected and what remained unavailable.

**Do not provide the model with** `evals/golden/daarops.json`, the evaluator results, or the reviewer decision.
