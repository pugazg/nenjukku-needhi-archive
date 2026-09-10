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
- Kalaignar Voice Guide: **INITIAL VERSION COMPLETE / LIVING DOCUMENT**
- Translation glossary: **INITIALISED**
- Source-note convention: **DEFINED AND IN USE**
- Corpus-wide source inventory: **NOT STARTED**
- Pilot `v1-ch01`: **T1 COMPLETE / T2 VOICE REVIEW IN PROGRESS**
- Pilot `v1-ch02`: **SOURCE NOTES COMPLETE / READY FOR T1**
- Production translation: **BLOCKED UNTIL BOTH PILOTS COMPLETE AND METHOD REVIEWED**

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
| `v1-ch01` | `பிறந்த ஆண்டு` | philosophy, rhetoric, self ↔ history, political/historical cadence | `t2-voice-review` |
| `v1-ch02` | `தந்தையின் துணிவு` | family/village narrative, humour, grief, religion, agriculture, embedded songs | `source-review` complete; `ready-for-t1` |

## Durable pilot files

### `v1-ch01`

- T1 translation: `data/books/nenjukku-needhi/translations/en/chapters/v1-ch01.json`
- source notes: `data/books/nenjukku-needhi/translations/en/source-notes/v1-ch01.json`
- T2 review: `data/books/nenjukku-needhi/translations/en/reviews/v1-ch01-t2.md`

Current T2 findings include:

- preserve the `பெரிய` / `சின்ன` rhetorical contrast more closely;
- restore the concrete `வெல்லம்` (jaggery) image in `உயிர் எமக்கு வெல்லமல்ல` rather than retaining only abstract sweetness;
- restore the foundation-laying force of `கால்கோள் விழா`;
- review whether `வெறித்தனமான பக்தி` was softened too much in T1;
- remove an external historical normalisation in “our Presidency” and return to the source wording `நம்முடைய மாநிலம்`.

### `v1-ch02`

- source notes: `data/books/nenjukku-needhi/translations/en/source-notes/v1-ch02.json`

Recorded before translation:

- repeated chapter heading;
- `கேட்க-` + `லாம்` page/source-unit join;
- later `விடு-` continuation;
- paragraph reconstruction requirement;
- embedded satirical songs require verse-aware translation;
- sharp tonal movement among grief, social criticism, devotion, agriculture, affection and humour;
- final two source units are non-authorial Wikisource maintenance notices and are explicitly excluded from memoir translation.

## Next activity

Finish the complete T2 Tamil-English voice review for `v1-ch01`, apply the reviewed corrections as one coherent revision, then run T3 English-only reading and thought-structure audit. After that, compare the frozen new translation with any pre-existing English rendering only as an independent comparator.

Then begin fresh T1 translation of `v1-ch02`, using its source-note exclusions and verse handling from the start.
