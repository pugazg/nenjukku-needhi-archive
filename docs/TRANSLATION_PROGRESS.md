# Nenjukku Needhi — English Translation Progress

## Authority

- Tamil source repository: `pugazg/kalaignar-autobiography` — **READ ONLY**
- Source path: `public/data/text/*.json`
- Initial source pin: `5c6b5ef8901044660e607d4649238d7c66cb648d`
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

## Gates

- Translation plan: **COMPLETE**
- Initial Kalaignar voice study (`v1-ch01`, `v1-ch02`): **COMPLETE**
- Kalaignar Voice Guide: **UPDATED WITH PILOT-1 LESSONS / LIVING DOCUMENT**
- Translation glossary: **INITIALISED**
- Source-note convention: **DEFINED AND IN USE**
- Corpus-wide source inventory: **NOT STARTED**
- Pilot `v1-ch01`: **APPROVED / CLOSED**
- Pilot `v1-ch02`: **T1 COMPLETE / T2 SOURCE+VOICE REVIEW NEXT**
- Production translation: **BLOCKED UNTIL `v1-ch02` PILOT COMPLETES AND METHOD IS REVIEWED**

## Mandatory chapter statuses

Use only these durable states:

- `not-started`
- `source-review`
- `t1-in-progress`
- `t1-complete`
- `t2-voice-review`
- `t3-english-review`
- `thought-structure-review`
- `source-hold`
- `approved`

A chapter must not be called `approved` unless all required source notes are recorded and all fidelity gates pass.

## Pilot queue

| Chapter | Tamil title | Purpose | Status |
|---|---|---|---|
| `v1-ch01` | `பிறந்த ஆண்டு` | philosophy, rhetoric, self ↔ history, political/historical cadence | **APPROVED / CLOSED** |
| `v1-ch02` | `தந்தையின் துணிவு` | family/village narrative, humour, grief, religion, agriculture, embedded songs | **T1 COMPLETE** |

## `v1-ch01` closure

Durable files:

- translation: `data/books/nenjukku-needhi/translations/en/chapters/v1-ch01.json`
- source notes: `data/books/nenjukku-needhi/translations/en/source-notes/v1-ch01.json`
- T2 review: `data/books/nenjukku-needhi/translations/en/reviews/v1-ch01-t2.md`
- T3 review: `data/books/nenjukku-needhi/translations/en/reviews/v1-ch01-t3.md`
- thought-structure audit: `data/books/nenjukku-needhi/translations/en/reviews/v1-ch01-structure.md`
- post-freeze existing-English comparison: `data/books/nenjukku-needhi/translations/en/reviews/v1-ch01-existing-comparison.md`

Gate results:

- T1 fresh Tamil translation: **PASS**;
- T2 Kalaignar-voice review: **PASS WITH REVISION**;
- T3 English-only read: **PASS WITH MINOR REVISION**;
- thought-structure audit: **PASS**;
- existing-English comparison: **PASS**;
- unresolved source holds: **0**;
- final status: **APPROVED**.

Key durable lessons from Pilot 1:

- preserve concrete idiom rather than abstracting it (`உயிர் எமக்கு வெல்லமல்ல` retains its jaggery image);
- preserve the `பெரிய / சின்ன` contrast and ownership logic;
- preserve foundation imagery in `கால்கோள்`;
- preserve deliberate intensity such as `வெறித்தனமான பக்தி`;
- preserve Kalaignar's historical present in live political passages;
- source OCR/extraction interventions must remain disclosed in source notes;
- existing English may influence a phrase only after the fresh translation is frozen and the adoption is explicitly justified.

## `v1-ch02` — T1 complete

Durable files:

- fresh T1 translation: `data/books/nenjukku-needhi/translations/en/chapters/v1-ch02.json`
- source notes: `data/books/nenjukku-needhi/translations/en/source-notes/v1-ch02.json`

T1 decisions already enforced:

- repeated heading excluded from body and represented as metadata;
- `கேட்க-` + `லாம்` and `விடு-` + `மல்லவா?` reconstructed as source-unit joins and disclosed;
- anomalous extracted `பார் போக்குவது?` translated contextually as the question of who will relieve the orphaned infant's hunger and explicitly noted;
- Muthuvelar's satirical songs retained as verse blocks, not prose summaries;
- culturally loaded terms such as `thali`, `manthirikar`, `Appa` and `Amma` retained or lightly glossed where useful;
- the Tirukkural verse and Kalaignar's subsequent gruel/nectar image remain linked;
- the chapter's shifts among grief, satire, religious devotion, agricultural domesticity, affection and humour are preserved rather than normalised;
- the final two Wikisource maintenance notices are excluded as non-authorial material.

Open T2/source issue:

- several lexical readings in the long `ஏலேலோ` satire (`தரகுமூட்டை`, `போகசாலை`, and the sequence around `முந்தானையால் கூட்டியே நின்று`) remain source-review items. T1 translates them conservatively but the chapter cannot be approved until they are reviewed.

## Next activity

Run the complete T2 source-and-Kalaignar-voice review for `v1-ch02`, with special attention to the embedded songs, rural/cultural vocabulary, humour, and whether any T1 phrasing over-explains or softens Kalaignar. Resolve or explicitly hold the long-song lexical uncertainties before T3.
