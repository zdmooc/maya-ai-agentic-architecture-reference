# D099 AA3 — Human scorecard arithmetic, review not attestation

Independent human rubric remains **20+20+20+15+15+10 = 100** and
requires >=85 **per case** without critical policy violation.
`evals/human_scorecard.py` checks score-field integrity, legal
ranges, total, declared independent source review and declared
external tool-trajectory review. It does **not** verify reviewer
identity, signatures, audits or provenance; a fabricated JSON declaring
human review is not proof of independent approval.

CI tests deliberately use a fully passing *synthetic* scorecard to
demonstrate that even 100/100 **cannot** promote
`AA3_ARCHITECT_REASONING_VALIDATED`.

Actual AA3 requires an independently reviewed blind reference for
at least two approved distinct cases, qualified model and tool trace,
verified reviewer authentication, actual sign-off and no critical
policy violations. The fictional NOTIFY-01 exercise is preparatory;
it does not replace both genuine acceptance cases.
