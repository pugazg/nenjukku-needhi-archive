# Nenjukku Needhi — English Translation Progress

## Authority

- Tamil source repository: `pugazg/kalaignar-autobiography` — **READ ONLY**
- Source path: `public/data/text/*.json`
- Batch 001 pinned source ref: `5c6b5ef8901044660e607d4649238d7c66cb648d`
- Latest observed source `main`: `bb0beaa0a18f97336b52319c1e7b15e62d81d1ed`
- `v1-ch04` source blob is identical at both refs: `1b55b986176d330fab4ce16eb70565ddd895ba48`
- Write repository: `pugazg/nenjukku-needhi-archive`
- Working branch: `translation/english-memoir`

## Corpus

- Volume 1: 140 chapters
- Volume 2: 77 chapters
- Volume 3: 73 chapters
- Volume 4: 22 chapters
- Volume 5: 50 chapters
- Volume 6: 29 chapters
- Total: 391 chapters

## Project gates

- Translation plan: **COMPLETE FOR PRODUCTION**
- Two-pilot method review: **COMPLETE**
- Kalaignar Voice Guide: **LIVING / UPDATED THROUGH `v1-ch03`**
- Translation glossary: **LIVING / UPDATED THROUGH `v1-ch03`**
- Source-note convention: **DEFINED AND IN USE**
- Pilot `v1-ch01`: **APPROVED / CLOSED**
- Pilot `v1-ch02`: **APPROVED / CLOSED WITH 2 DOCUMENTED ACCEPTED SCHOLARLY UNCERTAINTIES**
- Pilot phase: **COMPLETE**
- Production translation: **OPEN**
- Active production batch: **Batch 001 — `v1-ch03`–`v1-ch07`**

## Production method

Normal production batch size is 5 chapters, but the batch is a management envelope. Process one chapter at a time through:

`source review → source notes → T1 → T2 → T3 → thought structure → terminology/cultural audit → post-freeze comparator if applicable → approval`

## Active Batch 001

| Chapter | Tamil title | Pages | Current status |
|---|---|---:|---|
| `v1-ch03` | `"சிவாய நம! ஓம் நமசிவாய"` | 30–36 | **APPROVED / CLOSED** |
| `v1-ch04` | `என்னுடைய அரசியல் அரிச்சுவடி` | 37–41 | **SOURCE REVIEW COMPLETE / READY FOR T1** |
| `v1-ch05` | `நீதிக் கட்சியில் பல மாற்றங்கள்` | 42–45 | not started |
| `v1-ch06` | `தமிழ் காக்கும் போர் முனை` | 46–50 | not started |
| `v1-ch07` | `"நீங்களா 'மாணவ நேசன்' நடத்துகிறீர்கள்?"` | 51–55 | not started |

## `v1-ch03`

Final status: **APPROVED / CLOSED**.

- source review: PASS
- T1: PASS
- T2: PASS WITH REVISION
- T3: PASS WITH MINOR REVISION
- thought structure: PASS — 24/24 major movements preserved
- terminology/cultural consistency: PASS
- unresolved source holds: 0
- existing-English comparator at pinned ref: none

## `v1-ch04` source-review result

Durable source notes:

`data/books/nenjukku-needhi/translations/en/source-notes/v1-ch04.json`

Source review: **COMPLETE / READY FOR T1**.

Key findings:

- Source `main` advanced after the batch opened, but `v1-ch04` remains byte-identical at the pinned and live refs; Batch 001 therefore keeps its original source authority.
- The opening is damaged in both the pinned extraction and page-37 witness as `-ம் ஆண்டு`. Independent biographical evidence places this exact Tiruvarur High School admission episode in **1936**, matching the passage's age twelve. T1 may reconstruct `In 1936` only with the source intervention disclosed.
- `கர்ஸ்தூரி ஐயங்கார்` is the digital-source spelling; independent accounts identify the headmaster as **Kasthuri/Kasturi Iyengar**. English may normalise the personal name while preserving the note.
- Headmaster Iyengar's `நோக்கு` is the dated Brahmin-Tamil pronominal form already established in `v1-ch03`; it functions as `உனக்கு`, not `look`.
- `பங்கா` / `பியூன்` are period school vocabulary and should retain their colonial-era texture.
- The admission episode is deliberately told in third-person dramatic present and must remain so until the delayed `நானே தான்!` reveal.
- The boy's plea after `அதற்கு நான் என்ன செய்வது தம்பி?` has a missing opening quotation mark; it is securely reconstructed as direct speech.
- Contextual extraction defects are recorded for `விழுத்து`, the interrupting full stop in `அந்த ஆண்டு. அந்தப் பையன்`, `சுட்சியின்`, and `சட்டசயைத்`.
- `கலகலத்து நின்றது` is lexically valid in the sense of becoming shaky/losing strength and is not treated as corrupted text.
- `அரிச்சுவடி` is the governing metaphor: the Panagal Raja supplementary reader becomes Kalaignar's political primer.
- The chapter's structural movement is `school-admission drama → delayed self-reveal → Panagal Raja reader → political primer → Justice Party history → Self-Respect/Periyar/Anna connection`.
- Pages 38–41 contain dense historical assertions; translate Kalaignar's account faithfully rather than silently fact-correcting it.
- No non-authorial Wikisource maintenance material is present.
- unresolved source holds: **0**.
- T2 review items carried forward: movement terminology/register and historical-office vocabulary.

## Batch 001 counters

- source files pinned: **5 / 5**
- full source reviews complete: **2 / 5**
- T1 complete: **1 / 5**
- T2 complete: **1 / 5**
- T3 complete: **1 / 5**
- thought-structure complete: **1 / 5**
- approved: **1 / 5**

## Infrastructure note

`schemas/chapter.json` is currently an empty one-byte legacy placeholder, so formal JSON-Schema execution is not available under current repository controls.

## Next activity

Begin the fresh T1 translation of `v1-ch04` directly from the pinned Tamil and completed source notes. Preserve the third-person dramatic opening and delayed `நானே தான்!` reveal; reconstruct 1936 only as a documented source intervention; keep the `அரிச்சுவடி` political-primer metaphor; and do not turn the Justice Party history into detached encyclopedia prose.
