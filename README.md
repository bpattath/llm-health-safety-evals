# LLM Health Safety Evals

**An open evaluation suite for LLM decision-support in low-resource health systems: grounding, multilingual safety, and epidemic-signal reliability.**

**Status: design phase complete — seeking seed funding to build.** This repository currently contains the design document, task taxonomy with drafted example items, and roadmap. Code and datasets will be developed here in the open.

## The problem

Large language models are being wired into health decision-making in low- and middle-income countries — as chat interfaces over health data, triage aids, and advisory tools — faster than anyone is checking whether they are safe in those contexts. Three gaps stand out:

1. **Grounding.** When an assistant is constrained to a verified health-data store, does that grounding actually hold under realistic queries from health officials — and how often do models fabricate statistics when the data is missing?
2. **Multilingual safety.** Safety behaviours (refusals, caveats, calibration) are measurably weaker outside English. Health staff in Kerala, India — the suite's deployment context — work in Malayalam and English–Malayalam code-switching. No evaluation exists for whether guardrails survive the languages of actual deployment.
3. **Epidemic-signal reliability.** After the 2025 collapse of global surveillance funding, AI assistants are becoming the interpretive layer over incomplete, degraded surveillance data. Can models interpret potential outbreak signals honestly — expressing calibrated uncertainty and declining to conclude when the evidence is insufficient?

This suite evaluates all three, and publishes everything — harness, task datasets, results across frontier and open-weight models — under open licences, so any team deploying LLMs into health systems can test before shipping.

## Deployment context

The suite is designed against **First Signal**, a climate–health early-warning platform for Kerala, India, developed with the [Nayaneethi Policy Collective](https://www.nayaneethi.com) (Wayanad, Kerala). Its planned user-facing layer is a grounded chat assistant for health officials ("Is risk rising in my district this week? Why?") backed by a provenance-first indicator store built from Copernicus climate data, HMIS facility reporting, IHIP/IDSP disease surveillance, and NFHS survey data. The platform itself is pre-prototype and fundraised separately; this evaluation suite is deliberately scoped to stand alone.

Kerala offers an unusually demanding test bed: a strong decentralised health system, monsoon-driven outbreak dynamics (the 2018 floods and subsequent leptospirosis surge), and repeated spillovers of a high-consequence pathogen (Nipah virus, 2018 and 2023) — exactly the conditions under which AI interpretive reliability matters most. Validation runs with Kerala health-system practitioners convened through Nayaneethi.

The tasks are not hypothetical — they mirror the queries, languages, data conditions, and stakes of this deployment — and the resulting benchmark is reusable by any team deploying LLMs into health systems, in any country.

## Contents

| Document | What it covers |
|---|---|
| [docs/DESIGN.md](docs/DESIGN.md) | Full design: motivation, the three evaluation tracks, methodology, metrics, models covered, ethics |
| [docs/TASK_TAXONOMY.md](docs/TASK_TAXONOMY.md) | Task taxonomy and drafted example evaluation items for each track |
| [ROADMAP.md](ROADMAP.md) | 10-week build plan and budget |

## Team and context

Led by Balasubramanyam Pattath (PhD economist / data scientist, Geneva Graduate Institute; native Malayalam speaker), consultant with the [Nayaneethi Policy Collective](https://www.nayaneethi.com) (Wayanad, Kerala), which hosts the First Signal initiative and supplies the local health-system networks, epidemiologist review, and Malayalam-speaking reviewers behind the evaluation items.

## Licensing

Code will be released under MIT; evaluation datasets under CC-BY-4.0. Documents in this repository are CC-BY-4.0.

## Contact

Issues and PRs welcome, or reach out via the [Nayaneethi Policy Collective](https://www.nayaneethi.com).
