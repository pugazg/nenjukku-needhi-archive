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
- Pilot `v1-ch02`: **SOURCE NOTES COMPLETE / READY FOR T1**
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
| `v1-ch02` | `தந்தையின் துணிவு` | family/village narrative, humour, grief, religion, agriculture, embedded songs | `source-review` complete; `ready-for-t1` |

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

The post-freeze comparator contributed one adopted phrase-level choice only: “Do the small not own them too?” All other fresh translation decisions remain governed by Tamil-source fidelity.

## `v1-ch02` readiness

Source notes: `data/books/nenjukku-needhi/translations/en/source-notes/v1-ch02.json`

Recorded before translation:

- repeated chapter heading;
- `கேட்க-` + `லாம்` page/source-unit join;
- later `விடு-` continuation;
- paragraph reconstruction requirement;
- embedded satirical songs require verse-aware translation;
- sharp tonal movement among grief, social criticism, devotion, agriculture, affection and humour;
- final two source units are non-authorial Wikisource maintenance notices and are explicitly excluded from memoir translation.

## Next activity

Begin fresh T1 translation of `v1-ch02` directly from Tamil, using its source-note exclusions and verse handling from the start. Do not consult any existing English as drafting authority. Preserve the chapter's tonal shifts and keep the embedded satirical songs as verse rather than flattening them into prose.
