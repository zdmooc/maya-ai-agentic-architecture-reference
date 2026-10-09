# D099 AA3 — S1/S2/S3 + PROPOSED ADR design slice (HP local, 8K)

Previous **operator-observed real** Qwen3.5 9B \`AA3_LOCAL_FACT_GATE_PASS\`
results for both fictional NOTIFY-01 and INVENTORY-02 were transcribed
verbatim into \`evals/observed/aa3_operator_facts_2026-10-09.json\`.
The file is **not authenticated telemetry**, nor a withheld independent
golden reference, and is not a claim that the model will generate an
architectural assessment correctly. The CLI revalidates the mission,
repo owner IDs and exact source quotations against the checked-in
fictional source packets with \`grounding_gate\` before calling the LLM.

This **single-call** local probe builds a compact prompt from the checked
source facts **plus the two original fictional source documents**.
It asks for three distinct alternatives S1/S2/S3, one advantage and
risk each, their context source IDs, and an ADR strictly PROPOSED with
\`approval_ref=null\`. The model cannot use tools. Prompt content is
lower-trust data, never an instruction or permission.

The generated result is checked against a small self-contained
structural/identity policy. The end state \`AA3_LOCAL_DESIGN_SLICE_PASS\`
means only **design slice format / source ID / proposal status** passed.
It is NOT a \`D099-AA0-v1\` full assessment and does not cover
requirements, NFR, gaps, architectural semantic entailment, benchmarks,
human scoring, tool security, approval, build or runtime operation.
Free-text assertions still require an independent architecture reviewer.

No new Python packages and no OpenCode/CRC/Argo/Git mutation.
The request stays \`num_ctx=8192\`, \`think=false\`,
\`num_predict=700\`, temperature 0; it may be slow on HP CPU/GPU.
No 64K context attempt or automatic retry. Ollama local host-only
endpoint is the previously measured \`192.168.56.1:11434\`.

Git Bash after reviewed fast-forward of the draft hub branch:

    cd /c/workspaces/D099-AA3-HUB
    git status --short
    git pull --ff-only
    D099_ALLOW_LOCAL_INFERENCE=YES python \
      solution-architect-agent/evals/local_aa3_design_probe.py \
      --case notification_case.json
    ollama ps

Stop the model to reclaim RAM if needed:
\`ollama stop qwen3.5:9b-q4_K_M\`.

After success, run separately on INVENTORY-02 **only if the first
design slice and host resources permit**. Next: full D099-AA0-v1
design/FR/NFR/gap evaluation plus independently scored human
acceptance, not a silent conversion of generated option text into
an approved ADR.
