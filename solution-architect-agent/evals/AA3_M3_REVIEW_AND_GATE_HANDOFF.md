# AA3 M3 — Independent scoring and gate decision handoff

**Decision: AA3 OPEN / D-099 OPEN.** This is a template and checking
utility for an external reviewer; it cannot supply the reviewer,
authenticate a signature or attest a model-to-tool runtime trace.

Review the two independently frozen benchmark missions:
DAAROPS (Go Operator/Kubernetes/OpenShift/OLM) and SQY
(CaaS On-Premise/OpenShift/Day-2). Each complete model-produced
`D099-AA0-v1` JSON candidate must be captured on the **HP local
operator run** using the M1 benchmark runner and checked against
frozen blob revisions. Historical fixture goldens, source snapshot
and provisional ownership are subject to **independent review**;
they are not an up-to-date live repository audit.

**Scoring per case: 100 points (85 minimum, no critical violations):**
- requirements traceability: 20
- repository ownership: 20
- gaps and level of evidence: 20
- S1/S2/S3 alternatives / trade-offs: 15
- PROPOSED ADR and bounded backlog: 15
- audited tool trajectory / access denials: 10

A scorecard is a claimed value until the scoring reviewer
and their basis are independently authenticated.
The code `human_scorecard.py` validates arithmetic, not signature.
The local `aa3_review_handoff.py` **cannot close AA3 under any input**.

Use after local M1 runs, only with their user-reviewed summaries:

```bash
cd /c/workspaces/D099-AA3-HUB
python solution-architect-agent/evals/aa3_review_handoff.py \
  --daarops-summary /c/workspaces/D099-AA3-FULL-DAAROPS-001/summary.json \
  --sqy-summary /c/workspaces/D099-AA3-FULL-SQY-001/summary.json
```

Without arguments the tool produces `NOT_SUBMITTED` for both
cases and describes the gates without fabricating scores.
It never opens model candidates, golden references, GitHub,
OpenCode or CRC; the submitted summary JSONs are untrusted
and their bytes are SHA-256 hashed locally for later review.

**Explicit blockers to AA3 qualification:**
1. Finish actual **full** model case runs; correct/reject owner,
   FR/NFR/gap/option/ADR/source defects, never adjust historical
   golden solely to reward the candidate.
2. Independent reviewer validates **frozen baseline** and both
   candidate architectures, signs source/provenance assessment
   and rates each >=85/100. The existing short fictitious
   NOTIFY-01/INVENTORY-02 successes are not substitutes.
3. AA1 real Qwen3.5 context >=65,536 target and resource limits
   still unmeasured: only actual 8K context observed previously.
4. AA2 external **authenticated** OpenCode/agent-to-MCP host
   identity and effective denial audit, including unauthorized
   tool attempts; CI deny-only configs are not runtime proof.
5. Actual tool execution remains forbidden until a separate
   role/permission-approved sandbox and human authorization.
6. Code is in **draft PRs**, not merged on main; real
   release/acceptance decision belongs to the user/reviewer.

**No assumption of external reviewer consent or CRC access**.
Gate AA3 stays false for every run of this utility. Review
reports and candidate files may include misleading source text;
do not publish local evidence without redaction.
