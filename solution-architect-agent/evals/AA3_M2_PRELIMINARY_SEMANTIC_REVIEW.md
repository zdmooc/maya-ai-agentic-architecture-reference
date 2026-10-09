# AA3 M2 — preliminary semantic warning pass (offline)

The existing Qwen3.5 8K short design-slice tests obtained
`AA3_LOCAL_DESIGN_SLICE_PASS` for both fictitious NOTIFY-01 and INVENTORY-02.
This **only validated JSON format, source IDs, option count and ADR status**.

`aa3_semantic_review_watchlist.py` is a **bounded lexical watchlist**
built from the user's real observed outputs. It flags:
- **NOTIFY-01 S1** unbounded retries violating mandatory N2 bounded delivery;
- **NOTIFY-01 S3** largely adding consent acceptance testing instead
  of another end-to-end delivery design;
- **INVENTORY-02 S1** evidence-free absolute consistency guarantee;
- **INVENTORY-02 S2** unmeasured high-throughput claim;
- **INVENTORY-02 S3** unreviewed ordering/atomicity/replay failure paths.

This is not an automatic semantic judge. A flag can require more
nuanced review; no flags could simply mean the watchlist missed a
different weakness. Both cases remain **NOT_SCORED**.

Read-only offline usage after pulling PR #4:

```bash
python solution-architect-agent/evals/aa3_semantic_review_watchlist.py --case NOTIFY-01
python solution-architect-agent/evals/aa3_semantic_review_watchlist.py --case INVENTORY-02
```

Next full benchmark has two genuinely distinct frozen *public mission*
cases DAAROPS/SQY, not additional reruns of the same short example.
Compare actual candidates with `precheck.py`, source pins and the
human scorecard. Never score 85/100 without an independent human.
Real model-to-MCP host audit remains unproved. No new repo, no CRC.
