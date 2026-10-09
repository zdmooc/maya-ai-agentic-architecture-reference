"""D099 AA3: extract strict JSON candidate from OpenCode JSONL output.

This parses a model-produced artifact. Neither the candidate nor this trace
constitutes independent tool-authorization evidence or human review.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Iterable


class CandidateExtractionError(ValueError):
    """A candidate cannot be reconstructed safely."""


def extract(events: Iterable[dict[str, Any]]) -> dict[str, Any]:
    messages = []
    tokens = None
    event_types: dict[str, int] = {}
    for event in events:
        if not isinstance(event, dict):
            raise CandidateExtractionError("INVALID_EVENT")
        kind = event.get("type")
        if not isinstance(kind, str):
            raise CandidateExtractionError("INVALID_EVENT_TYPE")
        event_types[kind] = event_types.get(kind, 0) + 1
        part = event.get("part", {})
        if kind == "text" and isinstance(part, dict) and part.get("type") == "text":
            content = part.get("text")
            if isinstance(content, str):
                messages.append(content)
        if kind == "step_finish" and isinstance(part, dict):
            tokens = part.get("tokens")
    if not messages:
        raise CandidateExtractionError("NO_MODEL_TEXT")
    raw = "".join(messages).strip()
    if len(raw) > 200_000:
        raise CandidateExtractionError("TOO_MUCH_MODEL_TEXT")
    try:
        candidate = json.loads(raw)
    except (ValueError, UnicodeError) as exc:
        raise CandidateExtractionError("MODEL_TEXT_NOT_JSON_OBJECT") from exc
    if not isinstance(candidate, dict):
        raise CandidateExtractionError("MODEL_JSON_NOT_OBJECT")
    return {
        "candidate": candidate,
        "metadata": {
            "classification": "MODEL_OUTPUT_EXTRACTED_UNVERIFIED",
            "events": event_types,
            "reported_tokens": tokens,
            "independent_tool_audit": "NOT_PRESENT",
            "human_review": "NOT_PRESENT",
            "AA3_ARCHITECT_REASONING_VALIDATED": False,
        },
    }


def read_events(path: Path) -> list[dict[str, Any]]:
    if path.stat().st_size > 2_000_000:
        raise CandidateExtractionError("TRACE_TOO_LARGE")
    with path.open("r", encoding="utf-8") as fh:
        try:
            return [json.loads(line) for line in fh if line.strip()]
        except json.JSONDecodeError as exc:
            raise CandidateExtractionError("INVALID_JSONL") from exc


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--trace", type=Path, required=True)
    ap.add_argument("--candidate", type=Path, required=True)
    ap.add_argument("--metadata", type=Path, required=True)
    args = ap.parse_args()
    result = extract(read_events(args.trace))
    # Outputs must be new files in a scratch area. Never overwrite a result
    # from a prior run (including a golden/reference file).
    if args.candidate.resolve() == args.metadata.resolve():
        raise CandidateExtractionError("OUTPUT_COLLISION")
    with args.candidate.open("x", encoding="utf-8") as file:
        json.dump(result["candidate"], file, indent=2, ensure_ascii=False)
        file.write("\n")
    with args.metadata.open("x", encoding="utf-8") as file:
        json.dump(result["metadata"], file, indent=2, ensure_ascii=False)
        file.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
