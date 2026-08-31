# Roadmap: build plan, complete by 31 December 2026

*Contingent on seed funding for build time, expert honoraria, API credits, and compute. The core build is 10 weeks; weeks 11–14 are contingency buffer (reviewer availability, model-access delays, workshop scheduling), with everything shipped by end of December 2026.*

| Weeks | Milestone |
|---|---|
| 1–2 | Inspect-based harness (item schema, mock indicator-store fixtures, runner, extending the included 12-item pilot); freeze Track 1 item set |
| 3–5 | Dataset construction: draft full item sets for Tracks 2 and 3; epidemiologist review of scenarios; Malayalam variants drafted (project lead) and independently reviewed via the Nayaneethi network |
| 6–7 | Evaluation runs: frontier APIs (Anthropic, OpenAI, Google, Mistral) and open-weight models (Llama, Gemma, Mistral families); judge-rubric validation against human-scored subset |
| 8 | Analysis: metrics by model × track × language; failure galleries |
| 9 | Kerala validation: in-person annotation workshop in Kerala with health-system practitioners convened through the Nayaneethi Policy Collective (practitioner-adjudicated gold labels, item realism, failure-gallery review); public write-up + practitioner's guide |
| 10 | Release: datasets (CC-BY-4.0), harness (MIT), results tables; workshop submission; dissemination through the Nayaneethi network and the AI-safety community |

## Indicative budget

| Item | Amount (USD) |
|---|---|
| Dedicated build time (~140 hours over 10–14 weeks, deliverable-bound; roughly half the lead's consulting day rate, with the balance contributed) | 5,600 |
| Economy round-trip flight, Geneva to Kochi | 1,000 |
| Accommodation, per diem and local transport for the validation week | 450 |
| Native-speaker and epidemiologist review honoraria (via the Nayaneethi network) | 800 |
| API credits for evaluation runs (frontier models) | 2,000 |
| Rented GPU compute for open-weight and Indic-language model evaluation | 850 |
| Development subscriptions (3 months) | 700 |
| **Total** | **11,400** |

If travel becomes infeasible, the annotation workshop runs remotely at no additional cost, reducing the total to 9,950.

## Out of scope (this phase)

- The First Signal platform and assistant prototype itself (separately fundraised)
- Languages beyond English/Malayalam (the harness is built to make adding languages cheap)
- Live deployment monitoring (a natural phase 2 once the assistant exists)
