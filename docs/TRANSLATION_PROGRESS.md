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
- Kalaignar Voice Guide: **UPDATED THROUGH `v1-ch03` T2 / LIVING DOCUMENT**
- Translation glossary: **UPDATED THROUGH `v1-ch03` T2 / LIVING DOCUMENT**
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

Final status: **APPROVED / CLOSED**.

### `v1-ch02` — `தந்தையின் துணிவு`

Final status: **APPROVED / CLOSED**.

- T1: PASS
- T2: PASS WITH REVISION
- T3: PASS
- thought-structure: PASS
- unresolved source holds: 0
- accepted scholarly uncertainties: 2 (`தரகுமூட்டை`; `முந்தானையால் கூட்டியே நின்று`)

Editorial closure: `data/books/nenjukku-needhi/translations/en/reviews/v1-ch02-editorial-closure.md`.

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
| `v1-ch03` | `"சிவாய நம! ஓம் நமசிவாய"` | 30–36 | **APPROVED / CLOSED** |
| `v1-ch04` | `என்னுடைய அரசியல் அரிச்சுவடி` | 37–41 | **NEXT — SOURCE REVIEW** |
| `v1-ch05` | `நீதிக் கட்சியில் பல மாற்றங்கள்` | 42–45 | queued for source review |
| `v1-ch06` | `தமிழ் காக்கும் போர் முனை` | 46–50 | queued for source review |
| `v1-ch07` | `"நீங்களா 'மாணவ நேசன்' நடத்துகிறீர்கள்?"` | 51–55 | queued for source review |

### `v1-ch03` — approved / closed

Durable files:

- translation: `data/books/nenjukku-needhi/translations/en/chapters/v1-ch03.json`
- source notes: `data/books/nenjukku-needhi/translations/en/source-notes/v1-ch03.json`
- T2 review: `data/books/nenjukku-needhi/translations/en/reviews/v1-ch03-t2.md`
- T3 review: `data/books/nenjukku-needhi/translations/en/reviews/v1-ch03-t3.md`
- thought-structure audit: `data/books/nenjukku-needhi/translations/en/reviews/v1-ch03-structure.md`
- approval review: `data/books/nenjukku-needhi/translations/en/reviews/v1-ch03-approval.md`

Final gate state:

- source review: **PASS**;
- T1: **PASS**;
- T2: **PASS WITH REVISION**;
- T3: **PASS WITH MINOR REVISION**;
- thought structure: **PASS — 24 / 24 major movements preserved**;
- terminology/cultural consistency: **PASS**;
- unresolved source holds: **0**;
- lexical review items remaining: **0**;
- existing-English comparator: **NONE at pinned source ref**;
- final status: **APPROVED / CLOSED**.

Key durable findings:

- `அரிநமோத்து சிந்தம்` is functionally resolved as an old education-initiation formula; the final English retains `Arinamothu Sindham` with only that minimal gloss;
- Postmaster Iyer's `நோக்கு` is dated Brahmin Tamil for `உனக்கு` (`for/to you`), not `look`;
- caste hierarchy and the wound/punugu, surgery and kicked-ball political images remain concrete and forceful;
- the long `இதோ` / `அதோ` homecoming remains a spoken guided-memory catalogue rather than a compressed summary;
- culture-specific `உச்சிமோந்து` remains the affectionate act of smelling the crown of the head;
- T3 restored natural English while retaining Kalaignar's concrete rain-of-kisses image and other rhetorical beats.

### Machine-readable infrastructure note

`schemas/chapter.json` in the repository is currently an empty one-byte legacy placeholder. Formal JSON-Schema execution therefore cannot be claimed for `v1-ch03` or the earlier translation records. The approval review records structural consistency under the repository's currently implemented controls. A future schema implementation can validate the corpus without changing literary approval status.

## Batch 001 counters

- source files pinned: **5 / 5**
- full source reviews complete: **1 / 5**
- T1 complete: **1 / 5**
- T2 complete: **1 / 5**
- T3 complete: **1 / 5**
- thought-structure complete: **1 / 5**
- approved: **1 / 5**

## Next activity

Run the complete source review for `v1-ch04` (`என்னுடைய அரசியல் அரிச்சுவடி`) before any T1 translation. Resolve or explicitly hold the damaged opening `-ம் ஆண்டு` expression; inspect the extended school-admission dialogue, Panagal Raja material, Justice Party political chronology, and any extraction/page joins or non-authorial material before translation begins.
