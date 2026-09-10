# Roadmap: build plan, complete by 31 December 2026

*The core build is 10 weeks; weeks 11–14 are contingency buffer (reviewer availability, model-access delays, workshop scheduling), with everything shipped by end of December 2026.*

| Weeks | Milestone |
|---|---|
| 1–2 | Inspect-based harness (item schema, mock indicator-store fixtures, runner, extending the included 12-item pilot); freeze Track 1 item set |
| 3–5 | Dataset construction: draft full item sets for Tracks 2 and 3; epidemiologist review of scenarios; Malayalam variants drafted (project lead) and independently reviewed via the Nayaneethi network |
| 6–7 | Evaluation runs: frontier APIs (Anthropic, OpenAI, Google, Mistral) and open-weight models (Llama, Gemma, Mistral families); judge-rubric validation against human-scored subset |
| 8 | Analysis: metrics by model × track × language; failure galleries |
| 9 | Kerala validation: in-person annotation workshop in Kerala with health-system practitioners convened through the Nayaneethi Policy Collective (practitioner-adjudicated gold labels, item realism, failure-gallery review); public write-up + practitioner's guide |
| 10 | Release: datasets (CC-BY-4.0), harness (MIT), results tables; workshop submission; dissemination through the Nayaneethi network and the AI-safety community |

## Out of scope (this phase)

- The First Signal platform and assistant prototype itself (developed separately)
- Languages beyond English/Malayalam (the harness is built to make adding languages cheap)
- Live deployment monitoring (a natural phase 2 once the assistant exists)
