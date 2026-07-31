#!/usr/bin/env python3
"""Operation Ochema — state snapshotter.

Computes a deterministic snapshot of the thesis's current state so the
dreaming phase can diff "now" vs "last run": file hashes, versions,
concept/confrontation/evidence counts, GAP count, LOG tail.

Usage:
    python3 ochema-snapshot.py            # print snapshot JSON to stdout
    python3 ochema-snapshot.py --write    # write meta/operation-state.json
"""
import json
import hashlib
import re
import sys
from pathlib import Path

ROOT = Path("/root/projects/ochema")
OBJ = ROOT / "the-occhema-object"

KEY_FILES = [
    "ochema.md",
    "ochemamath.md",
    "the-unified-formal-framework.md",
    "the-orchestration.md",
    "the-moment.md",
    "the-occhema-object/evidence/TREE.md",
    "the-occhema-object/confrontations/REGISTRY.md",
    "the-occhema-object/sections/07-falsification.md",
    "concepts/REGISTRY.md",
    "concepts/QUEUE.md",
    "the-occhema-object/updates/LOG.md",
]


def sha256(p: Path) -> str:
    h = hashlib.sha256()
    try:
        h.update(p.read_bytes())
    except FileNotFoundError:
        return "MISSING"
    return h.hexdigest()[:16]


def last_version() -> str:
    log = OBJ / "updates/LOG.md"
    try:
        text = log.read_text()
    except FileNotFoundError:
        return "none"
    vers = re.findall(r"## v(\d+\.\d+\.\d+)", text)
    return vers[-1] if vers else "none"


def count_md(path: str, pattern: str) -> int:
    p = ROOT / path
    try:
        return len(re.findall(pattern, p.read_text(), re.MULTILINE))
    except FileNotFoundError:
        return 0


def snapshot() -> dict:
    concepts = [d for d in (ROOT / "concepts").iterdir() if (ROOT / "concepts" / d).is_dir() and (ROOT / "concepts" / d / "core.md").exists()]
    confrontations = [f.stem for f in (OBJ / "confrontations").glob("*.md") if f.stem != "REGISTRY"]
    evidence = [f.stem for f in (OBJ / "evidence").glob("*.md") if f.stem != "TREE"]
    return {
        "timestamp": __import__("datetime").datetime.now().isoformat(timespec="seconds"),
        "version": last_version(),
        "files": {p: sha256(ROOT / p) for p in KEY_FILES},
        "counts": {
            "concepts": len(concepts),
            "concepts_with_essays": sum(1 for c in concepts if (ROOT / "concepts" / c / "essays").exists()),
            "confrontations": len(confrontations),
            "evidence_records": len(evidence),
            "gaps": count_md("the-occhema-object/evidence/TREE.md", r"^\d+\. \*\*L\d+"),
            "queued_concepts": count_md("concepts/QUEUE.md", r"PENDING"),
        },
        "cycle_state": {
            "last_cycle": None,
            "last_produced": [],
            "next_targets": [],
            "loop_status": "idle",
        },
        "log_tail": "\n".join((OBJ / "updates/LOG.md").read_text().splitlines()[-8:]) if (OBJ / "updates/LOG.md").exists() else "",
    }


if __name__ == "__main__":
    snap = snapshot()
    if "--write" in sys.argv:
        out = ROOT / "the-occhema-object/meta/operation-state.json"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(json.dumps(snap, indent=2))
        print(f"WROTE {out}")
    print(json.dumps(snap, indent=2))
