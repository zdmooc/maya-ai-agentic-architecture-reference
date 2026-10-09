# D-099 AA0 — Method integrity contract (iteration I1)

This is a **STATIC_DESIGN_CONTRACT**, not an executed architecture agent or
human-approved method. The stable twelve-stage method stays in
`method/stages.json`; `method/validate_workflow.py` checks mandatory
owner/stage order and four *authenticated human* gates (ADR, BUILD,
TEST_REVIEW, RUNTIME). A failure returns structured violations.

The validator neither calls a model nor asserts that runtime approvals are
enforced. This PR remains a draft until an independent architecture review.
Do not transfer gates to the agent, run code supplied by a retrieved
document, merge GitHub PRs automatically, or mutate any live cluster.

Test: `python -m unittest discover -s solution-architect-agent/tests -v`.
