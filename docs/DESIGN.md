# Design Document — LLM Health Safety Evals

*Version 0.1 — August 2026. Design phase; feedback welcome via issues.*

## 1. Motivation

LLM assistants are entering health systems in low- and middle-income countries with no context-appropriate safety evidence. The deployments moving fastest — chat interfaces over national health data, advisory tools for district health teams — are exactly the ones where failure is least visible and most costly: users have limited means to verify outputs, oversight is thin, and the populations affected are vulnerable.

Three published findings motivate the suite:

- **Safety behaviour degrades outside English.** Models refuse harmful requests in English yet comply with equivalent requests in lower-resource languages; accuracy and calibration also fall. The deployment languages this suite covers — Malayalam and English–Malayalam code-switching — sit squarely in this gap.
- **Retrieval grounding reduces but does not eliminate fabrication**, and grounding failures concentrate precisely where data is sparse — which, in post-2025 health systems, is most places.
- **Confidence communication shapes decisions.** For an official deciding whether to trigger a heat alert or escalate an outbreak investigation, a miscalibrated "certainly" is a different and worse failure than an honest "the data cannot tell us yet."

No public benchmark covers this deployment class. This suite is scoped to fill that gap and to be reusable beyond its origin project.

## 2. Deployment context

The suite is designed against the Evidence Lab, a climate–health early-warning platform for Kerala, India, developed with the Nayaneethi Policy Collective (Wayanad, Kerala) — currently pre-prototype and fundraised separately. Its planned user-facing layer is a grounded chat assistant for health officials, specified to answer questions like *"Is risk rising in my district this week? Why?"* by querying a provenance-first indicator store (Copernicus ERA5-Land climate data, HMIS facility reporting, IHIP/IDSP disease surveillance, NFHS survey data, community reports) and returning numbers with sources and uncertainty attached — never free-generating statistics.

Kerala supplies unusually demanding test conditions: monsoon-driven outbreak dynamics (the 2018 floods were followed by a major leptospirosis surge) and repeated spillovers of a high-consequence pathogen (Nipah virus, 2018 and 2023). A district health official interpreting an ambiguous fever cluster in a district with Nipah history is precisely the user whose AI assistant must not overclaim. Evaluation items and results are validated with Kerala health-system practitioners convened through Nayaneethi.

This context supplies the suite's realism: actual query patterns, actual languages (Malayalam, English–Malayalam code-switching), actual data-quality conditions (missing district-months, reporting artifacts, survey lags), and an actual decision cadence (weekly district health meetings, monsoon-season alert thresholds).

## 3. Evaluation tracks

### Track 1 — Grounding and hallucination

**Question:** When constrained to a verified data store, does grounding hold — and what happens at its edges?

Evaluated behaviours:
- **Faithful retrieval:** answerable queries must return the stored value, with provenance.
- **Honest refusal on missing data:** structurally identical queries whose answer is absent from the store must produce "the data does not cover that," not a fabricated value.
- **Quality caveats:** values flagged as low-quality or partial must carry that caveat into the answer.
- **False-premise correction:** queries presupposing a wrong fact ("Why did malaria cases double in X?" when they fell) must correct the premise rather than confabulate an explanation.
- **No silent extrapolation:** requests for aggregates the store cannot support (national figures from three regions' data) must be declined or explicitly scoped.

### Track 2 — Multilingual safety and calibration (Malayalam)

**Question:** Do guardrails, escalation behaviour, and calibration survive translation into the languages of deployment?

Evaluated behaviours, always as **matched cross-language sets** (same item in English, Malayalam, and English–Malayalam code-switching — the registers Kerala health staff actually use):
- **Guardrail parity:** clinical-overreach probes (requests for diagnosis or prescription that should be escalated to a clinician) must be handled identically across languages.
- **Refusal consistency:** unsafe-advice requests (e.g., self-medication dosing) must be refused with equal reliability in every language.
- **Calibration parity:** the hedging and uncertainty language attached to identical underlying evidence must convey the same confidence across languages.
- **Terminology fidelity:** clinical and epidemiological terms (pre-eclampsia, leptospirosis, rapid diagnostic test) must survive translation without meaning drift.

Malayalam items are drafted by the project lead (a native speaker) and independently reviewed by Malayalam-speaking health practitioners through the Nayaneethi network. The harness is built so further languages can be added cheaply by other teams.

### Track 3 — Epidemic-signal reliability under degraded data

**Question:** Given incomplete, degraded surveillance data — the post-2025 norm — can models interpret potential outbreak signals honestly?

Evaluated behaviours, on synthetic but realistic scenarios (a fever cluster after monsoon flooding in a district with Nipah spillover history; a post-flood leptospirosis surge against seasonal baselines; arbovirus season onset; data gaps from facility outages):
- **Signal vs. noise:** distinguishing genuine anomalies from seasonal base rates.
- **Artifact awareness:** considering reporting artifacts (a new facility joining the system, a backlog upload) as candidate explanations for apparent spikes.
- **Calibrated uncertainty:** quantifying and communicating what the missing data means for confidence in any conclusion.
- **Declining under pressure:** holding "the evidence is insufficient" even when the user demands a yes/no answer now.
- **Proportionate action:** recommending verification steps (targeted data checks, community confirmation) rather than premature mass alerts — or premature reassurance.

This track is the suite's biosecurity-relevant layer: AI systems are becoming the interpretive layer over whatever surveillance data remains, and their reliability on exactly these tasks determines whether they narrow or widen the world's outbreak-detection gap.

## 4. Methodology

- **Harness:** a lightweight, open eval harness (Python) executing items against a mock indicator store with controlled data conditions; every item specifies its data fixture, prompt(s), language variants, and scoring rubric.
- **Scoring:** deterministic checks where possible (did the answer contain the fabricated value? was the refusal produced?), rubric-based LLM-judge scoring for graded behaviours (uncertainty language, proportionality), with a human-validated subset to measure judge agreement. All judge prompts and rubrics published.
- **Metrics:** fabrication rate on unanswerable items; premise-correction rate; cross-language guardrail parity (refusal/escalation deltas); calibration error on confidence-elicitation items; artifact-consideration rate; decline-under-pressure rate.
- **Models:** frontier APIs (Anthropic, OpenAI, Google, Mistral) and open-weight models (Llama, Gemma, Mistral families) — the latter because resource-constrained deployments disproportionately use them.
- **Reporting:** a public results table by model × track × language, with qualitative failure galleries.

## 5. Dataset construction

Items are synthetic, constructed from public data patterns (HMIS/IHIP indicator structures, NFHS indicators, ERA5 climate values) — no real patient data, no PII, no operational surveillance data. Epidemiological plausibility is reviewed by public-health experts from the Nayaneethi network; language variants by native speakers, paid honoraria. Items and results are validated in workshops with Kerala health-system practitioners convened through Nayaneethi.

## 6. Ethics and dual-use

The suite evaluates *defensive* reliability: whether models serve health decision-makers honestly. It contains no pathogen-enhancement, synthesis, or other hazardous-knowledge content; scenario design deliberately stays at the epidemiological-operations level (case counts, reporting, alerts). Item review includes a dual-use check before release.

## 7. Outputs and licensing

1. Open-source eval harness (MIT) and task datasets (CC-BY-4.0) in this repository.
2. Results write-up across evaluated models, published openly; submission to a relevant workshop venue.
3. A short practitioner's guide: what to test before deploying an LLM assistant into a health system.

## 8. Status and funding

Design phase is complete (this document, the [task taxonomy](TASK_TAXONOMY.md), and the [roadmap](../ROADMAP.md)). Build is pending seed funding for evaluation compute, API credits, expert honoraria, and dedicated build time. The parent Evidence Lab platform (Nayaneethi Policy Collective) is fundraised separately; this evaluation layer is deliberately scoped to stand alone and be reusable by others.
