# Nenjukku Needhi — English Translation Progress

## Authority

- Tamil source repository: `pugazg/kalaignar-autobiography` — **READ ONLY**
- Source path: `public/data/text/*.json`
- Batch 001 pinned source ref: `5c6b5ef8901044660e607d4649238d7c66cb648d`
- Latest observed source `main`: `d6621b71256ae99b1c89b4f2091513dcc5f96626`
- `v1-ch05` source blob is identical at the Batch 001 pin and live source main: `220fb5271eac48c6988057d0d464d5950fd822a3`
- Write repository: `pugazg/nenjukku-needhi-archive`
- Working branch: `main`

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
- Kalaignar Voice Guide: **LIVING / UPDATED THROUGH `v1-ch05` T2**
- Translation glossary: **LIVING / UPDATED THROUGH `v1-ch05` T2**
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
| `v1-ch04` | `என்னுடைய அரசியல் அரிச்சுவடி` | 37–41 | **APPROVED / CLOSED** |
| `v1-ch05` | `நீதிக் கட்சியில் பல மாற்றங்கள்` | 42–45 | **T3 COMPLETE / THOUGHT STRUCTURE NEXT** |
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

## `v1-ch04` — approved / closed

Durable files:

- translation: `data/books/nenjukku-needhi/translations/en/chapters/v1-ch04.json`
- source notes: `data/books/nenjukku-needhi/translations/en/source-notes/v1-ch04.json`
- T2 review: `data/books/nenjukku-needhi/translations/en/reviews/v1-ch04-t2.md`
- T3 review: `data/books/nenjukku-needhi/translations/en/reviews/v1-ch04-t3.md`
- thought-structure audit: `data/books/nenjukku-needhi/translations/en/reviews/v1-ch04-structure.md`
- final approval review: `data/books/nenjukku-needhi/translations/en/reviews/v1-ch04-approval.md`

Gate state:

- source review: **PASS**;
- T1: **PASS / COMPLETE**;
- T2: **PASS WITH REVISION / COMPLETE**;
- T3: **PASS WITH MINOR REVISION / COMPLETE — 10 source-checked revisions**;
- thought structure: **PASS — 20 / 20 major movements preserved**;
- terminology/cultural consistency: **PASS**;
- post-freeze comparator: **NONE at pinned source ref**;
- final approval: **PASS / APPROVED**;
- unresolved source holds: **0**;
- outstanding review items: **0**.

## `v1-ch05` — T3 complete

Durable files:

- source notes: `data/books/nenjukku-needhi/translations/en/source-notes/v1-ch05.json`
- translation: `data/books/nenjukku-needhi/translations/en/chapters/v1-ch05.json`
- T2 review: `data/books/nenjukku-needhi/translations/en/reviews/v1-ch05-t2.md`
- T3 review: `data/books/nenjukku-needhi/translations/en/reviews/v1-ch05-t3.md`

Gate state:

- source review: **PASS / COMPLETE**;
- T1: **PASS / COMPLETE**;
- T2: **PASS WITH REVISION / COMPLETE**;
- T3: **PASS WITH MINOR REVISION / COMPLETE — 15 source-checked revisions**;
- unresolved source holds: **0**;
- outstanding T3 review items: **0**;
- next gate: **thought-structure audit**.

T3 preserved all T2 source and terminology decisions while improving only genuine English-language roughness. Accepted revisions include the Tanjore-conference syntax, `took office as ministers`, compulsory-Hindi legislation `was enacted`, `organized agitations`, the red-flame sentence, `at heart` for `உள்ளூர`, the Panneerselvam-response syntax, the Maraimalai Adigal consolation sentence, the fourteen-year pivot, Nehru `to rest`, the public-money resolution, the Annadurai before-fame fragment, `came under severe challenge`, the reported criticism of Periyar, and `Short in stature!`.

T3 explicitly retained source-driven unusual English where smoothing would erase Kalaignar's action: `letter for letter` in the Tamil-mediated Voltaire quotation; `became corpses within the prison walls`; collective `The Tamil`; the blood-dipped flag flown until it touches the sky; `How the man speaks!`; the clipped `It was written. It was said.`; and the separate pomegranate-pearl, sluice, Courtallam-waterfall and Tamil-`chindu` images.

## Batch 001 counters

- source files pinned: **5 / 5**
- full source reviews complete: **3 / 5**
- T1 complete: **3 / 5**
- T2 complete: **3 / 5**
- T3 complete: **3 / 5**
- thought-structure complete: **2 / 5**
- approved: **2 / 5**

## Infrastructure note

`schemas/chapter.json` is currently an empty one-byte legacy placeholder, so formal JSON-Schema execution is not available under current repository controls.

## Branch consolidation

The former working branch `translation/english-memoir` was merged into `main` via PR #1. All further translation work is performed directly on `main`; the old branch is not an active work surface.

## Next activity

Run the complete **thought-structure audit** for `v1-ch05`, checking that the English follows the same narrative and argumentative movement as the pinned Tamil. Do not consult any pre-existing English comparator until the independent translation has passed thought structure.
