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
- Kalaignar Voice Guide: **UPDATED THROUGH PILOT-2 / LIVING DOCUMENT**
- Translation glossary: **INITIALISED**
- Source-note convention: **DEFINED AND IN USE**
- Corpus-wide source inventory: **NOT STARTED**
- Pilot `v1-ch01`: **APPROVED / CLOSED**
- Pilot `v1-ch02`: **T1 PASS / T2 PASS WITH REVISION / T3 PASS / THOUGHT-STRUCTURE PASS / SOURCE HOLD (2 SEMANTIC INTERPRETATIONS)**
- Production translation: **BLOCKED UNTIL `v1-ch02` PILOT IS EDITORIALLY CLOSED AND METHOD IS REVIEWED**

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
| `v1-ch02` | `தந்தையின் துணிவு` | family/village narrative, humour, grief, religion, agriculture, embedded songs | **SOURCE HOLD — ALL NON-SOURCE GATES COMPLETE** |

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

## `v1-ch02` — all translation/structure gates complete; semantic source hold remains

Durable files:

- translation: `data/books/nenjukku-needhi/translations/en/chapters/v1-ch02.json`
- source notes: `data/books/nenjukku-needhi/translations/en/source-notes/v1-ch02.json`
- T2 review: `data/books/nenjukku-needhi/translations/en/reviews/v1-ch02-t2.md`
- source-witness decision: `data/books/nenjukku-needhi/translations/en/reviews/v1-ch02-source-witness.md`
- T3 review: `data/books/nenjukku-needhi/translations/en/reviews/v1-ch02-t3.md`
- thought-structure audit: `data/books/nenjukku-needhi/translations/en/reviews/v1-ch02-structure.md`

Gate results:

- T1 fresh Tamil translation: **PASS**;
- T2 complete Tamil–English source-and-voice review: **PASS WITH REVISION**;
- non-authorial Wikisource notices: **EXCLUDED / PASS**;
- source-unit joins and contextual extraction anomalies: **DOCUMENTED / PASS**;
- embedded verse handling: **PASS WITH REVISION**;
- T3 English-only read: **PASS**;
- thought-structure audit: **PASS**;
- structural omissions/additions: **0**;
- final approval: **BLOCKED BY 2 SEMANTIC INTERPRETATION HOLDS**.

### Resolved during T2

- `போகசாலை` — independently supported as sleeping hall/bedchamber; T1's `pleasure-house` was corrected.
- `ஊடியும் கலந்துமே வந்தேன்` — restored to its lovers' quarrel/feigned-sulking then reunion sense rather than generic `dallied`.
- Kalaignar-voice corrections were applied across the orphan-infant, social-satire, devotion, Anjugam-praise, agricultural, birth and burglary passages.

### Exact remaining holds — 2

The pinned chapter extraction and the separately retained page-level text witness agree on the visible text. The remaining problem is **semantic interpretation**, not an unstable character reading.

1. `தரகுமூட்டை` — exact semantic force of the stable compound remains uncertain. The English retains provisional `taragu-mootai` rather than inventing a confident paraphrase.
2. `முந்தானையால் கூட்டியே நின்று` — exact object/syntactic force remains uncertain. The English remains conservative and supplies no unexpressed object.

A trustworthy page-image rendering of the relevant printed page was not available through the interfaces used in the witness review, so no visual-glyph verification is claimed. These isolated holds did not prevent T3 or the thought-structure audit, but they continue to block `approved` status.

## Pilot-2 structural result

The English preserves the chapter's complete movement:

`orphaned Muthuvel → human foster care → father's talents → protest/social satire → Kalaignar's self-comparison → fearless critic / intense believer → marriages and bereavement → Anjugam → working agricultural household → coconut humour → childlessness / Kural → Kalaignar's birth → burglary / thali humour → father's philosophy of theft`

## Next activity

Make the editorial closure decision for the two isolated semantic interpretation holds. Preferred order:

1. seek any stronger visual/lexical/printed evidence if newly accessible;
2. if none is available, decide explicitly whether documented transliteration/conservative rendering is acceptable as the final scholarly treatment;
3. if accepted, record the editorial acceptance, clear the two holds, mark `v1-ch02` approved, review the two-pilot method, and only then open the first five-chapter production batch.

Do not guess a smoother meaning merely to achieve closure.