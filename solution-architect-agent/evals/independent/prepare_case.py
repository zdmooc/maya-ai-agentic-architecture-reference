"""D099 AA3 I5: assemble a synthetic, golden-blind evaluation packet offline."""
from __future__ import annotations
import hashlib
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "notification_case.json"
REFERENCE = ROOT / "notification_reference.review_only.json"
ALLOWED_SYNTHETIC = frozenset({"notification_case.json", "inventory_case.json"})


def case_path(name: str) -> Path:
    if name not in ALLOWED_SYNTHETIC:
        raise ValueError("UNAPPROVED_INDEPENDENT_FIXTURE")
    return ROOT / name


def assemble_case(name: str) -> tuple[dict[str, Any], dict[str, Any]]:
    selected = case_path(name)
    fixture = json.loads(selected.read_text(encoding="utf-8"))
    if fixture.get("origin") != "SYNTHETIC_FICTIONAL_NO_EXTERNAL_CLIENT_OR_REPOSITORY":
        raise ValueError("ONLY_SYNTHETIC_INDEPENDENT_CASE_ALLOWED")
    sources = fixture["sources"]
    if not isinstance(sources, list) or not sources:
        raise ValueError("CASE_SOURCE_REQUIRED")
    if not all(isinstance(s.get("id"), str) and s.get("text") for s in sources):
        raise ValueError("CASE_INVALID_SOURCE")
    if len(set(s["id"] for s in sources)) != len(sources):
        raise ValueError("CASE_DUPLICATE_SOURCE")
    mapping = fixture["repository_sources"]
    if any(source_id not in {s["id"] for s in sources}
           for source_id in mapping.values()):
        raise ValueError("CASE_UNKNOWN_REPO_SOURCE")
    packet = {
        "mission_id": fixture["mission_id"],
        "mission_title": fixture["mission_title"],
        "scenario": fixture["scenario"],
        "repository_sources": mapping,
        "sources": [
            {"id": s["id"], "text": s["text"],
             "sha256": hashlib.sha256(s["text"].encode("utf-8")).hexdigest()}
            for s in sources
        ],
    }
    # The blind model packet contains no reference/golden answer.
    return packet, {
        "status": "SYNTHETIC_BLIND_PACKET_STATIC_ONLY",
        "fixture_path": name,
        "fixture_sha256": hashlib.sha256(selected.read_bytes()).hexdigest(),
        "reference_exposed": False,
        "source_provenance": "FICTIONAL_FIXTURE_PIN_TO_COMMIT_BEFORE_MODEL_RUN",
        "model_invoked": False,
        "AA3_ARCHITECT_REASONING_VALIDATED": False,
    }


def assemble() -> tuple[dict[str, Any], dict[str, Any]]:
    """Compatibility with the original NOTIFY-01 fixture."""
    return assemble_case("notification_case.json")


if __name__ == "__main__":
    packet, metadata = assemble()
    print(json.dumps({
        "status": metadata["status"], "mission_id": packet["mission_id"],
        "source_ids": [x["id"] for x in packet["sources"]],
        "fixture_sha256": metadata["fixture_sha256"],
        "model_invoked": False,
    }, indent=2))
