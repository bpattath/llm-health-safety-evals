#!/usr/bin/env python3
"""Regenerate docs/pilot-data.json for the static explorer.

Combines pilot/items.json with any pilot/results/raw_*.jsonl files.
Run after run_pilot.py; commit docs/pilot-data.json to publish.
"""
import json
from pathlib import Path

HERE = Path(__file__).parent
DOCS = HERE.parent / "docs"

items = json.loads((HERE / "items.json").read_text())
responses = {}
models = []
for raw in sorted((HERE / "results").glob("raw_*.jsonl")) if (HERE / "results").exists() else []:
    for line in raw.read_text().splitlines():
        rec = json.loads(line)
        model = rec["model"]
        if model not in models:
            models.append(model)
        responses.setdefault(rec["item"], {})[model] = {
            "response": rec["response"],
            "resolved_model": rec.get("resolved_model", model),
            "auto_flags": rec.get("auto_flags", []),
            "confirmed": rec.get("confirmed", None),
        }

out = {
    "system_prompt": items["system_prompt"],
    "items": items["items"],
    "models": models,
    "responses": responses,
}
(DOCS / "pilot-data.json").write_text(json.dumps(out, indent=1))
print("wrote", DOCS / "pilot-data.json", "-", len(items["items"]), "items,", len(models), "models")
