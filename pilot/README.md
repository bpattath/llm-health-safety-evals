# Pilot: 12-item grounding & epidemic-signal run

A runnable, dependency-free pilot of the suite's Track 1 (grounding) and Track 3
(epidemic-signal) items, in English. It exists to demonstrate the harness design
and produce first indicative results; the funded build replaces it with a full
[Inspect](https://inspect.aisi.org.uk/)-based harness, 60–100 items per track,
Malayalam variants, and cross-family LLM-judge scoring.

## Run

```bash
export ANTHROPIC_API_KEY=...        # and/or OPENAI_API_KEY
python3 pilot/run_pilot.py --models anthropic:claude-sonnet-4-5 openai:gpt-4o
```

Outputs land in `pilot/results/`: raw responses per model (JSONL) and a draft
results table. Estimated cost: well under $2 per model.

## Scoring honesty

The runner applies **heuristic** automatic flags only (possible fabricated
numbers, confident conclusions where the data cannot support one, missed
premise corrections, dropped data-quality caveats). Every flag is reviewed by a
human before results are published; published tables state the exact dated model
identifiers, temperature, and configs used.
