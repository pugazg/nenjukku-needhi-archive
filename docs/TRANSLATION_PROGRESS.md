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

- Translation plan: **UPDATED FROM TWO PILOTS / COMPLETE FOR PRODUCTION**
- Initial Kalaignar voice study (`v1-ch01`, `v1-ch02`): **COMPLETE**
- Two-pilot method review: **COMPLETE** — `docs/PILOT_METHOD_REVIEW.md`
- Kalaignar Voice Guide: **UPDATED THROUGH PILOT-2 / LIVING DOCUMENT**
- Translation glossary: **INITIALISED**
- Source-note convention: **DEFINED AND IN USE**
- Pilot `v1-ch01`: **APPROVED / CLOSED**
- Pilot `v1-ch02`: **APPROVED / CLOSED WITH 2 DOCUMENTED ACCEPTED SCHOLARLY UNCERTAINTIES**
- Pilot phase: **COMPLETE**
- Production translation: **OPEN**
- Active production batch: **Batch 001 — `v1-ch03`–`v1-ch07`**

## Mandatory chapter statuses

Use only these durable chapter states:

- `not-started`
- `source-review`
- `t1-in-progress`
- `t1-complete`
- `t2-voice-review`
- `t3-english-review`
- `thought-structure-review`
- `source-hold`
- `approved`

A chapter may be `approved` with a documented accepted scholarly uncertainty only when the uncertainty has been explicitly reviewed, its conservative final treatment is visible, and a dedicated editorial closure decision exists. Accepted uncertainty is not counted as an unresolved source hold.

## Pilot closure

### `v1-ch01` — `பிறந்த ஆண்டு`

Final status: **APPROVED / CLOSED**

Key durable lessons:

- preserve concrete idiom rather than abstracting it;
- preserve rhetorical contrast and ownership logic;
- preserve foundation imagery and deliberate political/emotional intensity;
- preserve Kalaignar's historical present;
- source OCR/extraction interventions must remain disclosed;
- existing English is a post-freeze comparator only.

### `v1-ch02` — `தந்தையின் துணிவு`

Final status: **APPROVED / CLOSED**

Gate results:

- T1: **PASS**;
- T2: **PASS WITH REVISION**;
- T3: **PASS**;
- thought-structure audit: **PASS**;
- non-authorial Wikisource notices: **EXCLUDED / PASS**;
- unresolved source holds: **0**;
- accepted scholarly uncertainties: **2**.

Accepted uncertainties:

1. `தரகுமூட்டை` — stable across available text witnesses; exact semantic force not securely established; final English retains `taragu-mootai`.
2. `முந்தானையால் கூட்டியே நின்று` — stable wording; exact object/syntactic force remains uncertain; final English retains a conservative rendering without supplying an unexpressed object.

Editorial closure: `data/books/nenjukku-needhi/translations/en/reviews/v1-ch02-editorial-closure.md`.

This closure does **not** claim the semantic questions have been solved. Stronger future evidence may reopen them through a documented revision.

## Production method

Normal production batch size: **5 chapters**.

A five-chapter batch is a management envelope. Process one chapter at a time through:

`source review → source notes → T1 → T2 → T3 → thought structure → terminology/cultural audit → post-freeze comparator if applicable → approval`

Do not bulk-translate five chapters merely because they belong to one batch. Do not start the sixth chapter until the active batch is closed.

## Active Batch 001 — `v1-ch03`–`v1-ch07`

Batch control: `data/books/nenjukku-needhi/translations/en/batches/batch-001.md`

Pinned source ref: `5c6b5ef8901044660e607d4649238d7c66cb648d`

| Chapter | Tamil title | Pages | Current status |
|---|---|---:|---|
| `v1-ch03` | `"சிவாய நம! ஓம் நமசிவாய"` | 30–36 | **SOURCE REVIEW COMPLETE / READY FOR T1** |
| `v1-ch04` | `என்னுடைய அரசியல் அரிச்சுவடி` | 37–41 | queued for source review |
| `v1-ch05` | `நீதிக் கட்சியில் பல மாற்றங்கள்` | 42–45 | queued for source review |
| `v1-ch06` | `தமிழ் காக்கும் போர் முனை` | 46–50 | queued for source review |
| `v1-ch07` | `"நீங்களா 'மாணவ நேசன்' நடத்துகிறீர்கள்?"` | 51–55 | queued for source review |

### `v1-ch03` source-review result

Source notes: `data/books/nenjukku-needhi/translations/en/source-notes/v1-ch03.json`

Recorded before translation:

- repeated chapter heading;
- multiple page/source-unit joins, including sentences split at `நாலு பெரிய மனிதர்கள் இருக்குமிடத்தில்`, `மதிமயங்கித்`, `அப்படிப்`, and `அடியெடுத்து வைத்ததே`;
- long quoted/oral Thirukkuvalai journey requires literary paragraph reconstruction while retaining repeated `இதோ` / `அதோ` demonstrative rhythm;
- contextual extraction anomaly `நாள் கூட` is recorded; context requires the first-person `நான்கூட` sense;
- low-level `வேணடுமென்ற` extraction defect recorded;
- caste/ritual vocabulary and Kalaignar's retrospective rationalist criticism require voice-sensitive handling;
- concrete political images — perfume on an unhealed wound, surgery, and the kicked ball — must remain concrete;
- `அரிநமோத்து சிந்தம்` is a lexical/semantic review item: T1 may preserve/transliterate it, but approval requires review;
- humour timing around the stolen hair-pot, Angalamman puja and curse-soil blowing back must be preserved;
- no non-authorial Wikisource maintenance unit is currently identified in the chapter body.

## Next activity

Begin a fresh T1 translation of `v1-ch03` directly from the pinned Tamil source and its completed source-note record. Do not consult any existing English as drafting authority. Preserve the chapter's movement from ritual childhood and comic anecdote into caste revolt, childhood theatre, nostalgia, superstition, rationalist reinterpretation and return to family/village memory.
