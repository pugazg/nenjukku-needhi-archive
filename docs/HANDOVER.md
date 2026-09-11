# Nenjukku Needhi English Translation — HANDOVER

## LIVE MAIN IS AUTHORITATIVE

Continue in:

- writable repository: `pugazg/nenjukku-needhi-archive`
- branch: `main`

Fetch live `main` first and preserve newer durable work.

The source repository is strictly **READ ONLY**:

- `pugazg/kalaignar-autobiography`
- source path: `public/data/text/*.json`

Never modify the source repository.

## Translation philosophy

> We are not translating an autobiography about Kalaignar. We are translating Kalaignar telling his own story.

Preserve factual fidelity, intellectual/reasoning fidelity, rhetorical fidelity and voice before optimizing for natural English.

Existing English is **never drafting authority**.

## Production workflow

`P0 source review → T1 fresh translation → T2 Tamil-English/Kalaignar voice → T3 English-only literary review → thought-structure audit → terminology/cultural audit → post-freeze comparator check → final approval → closed`

Process chapters sequentially within the active batch.

## Batch 001 — CLOSED

`v1-ch03`–`v1-ch07` are all **APPROVED / CLOSED**.

Batch 001 source pin:

`5c6b5ef8901044660e607d4649238d7c66cb648d`

Final counters: all chapter gates **5 / 5**, unresolved source holds **0**, outstanding review items **0**.

## Batch 002 — OPEN

Batch control:

`data/books/nenjukku-needhi/translations/en/batches/batch-002.md`

Source pin:

`d6621b71256ae99b1c89b4f2091513dcc5f96626`

The source repository `main` advanced since Batch 001, but the selected `v1-ch08`–`v1-ch12` blobs are unchanged from the older pin. The current source `main` is nevertheless the Batch 002 authority pin.

Batch span: **`v1-ch08`–`v1-ch12`**.

The standard five-chapter size is retained because all five intake units are modest 3–5-page chapters; no reduction is justified.

Chapters:

- `v1-ch08` — `தமிழ் மாணவர் மன்றம்` — pp. 56–59 — blob `e041c90234656a6b9fbd4650d607c3ba0b53e5e8` — **P0 NEXT**
- `v1-ch09` — `கலகக்கார நாரதர் புகுந்தார்.` — pp. 60–64 — blob `e3104c0f74478f25d0b15c4bb1ed12afd6420d21` — QUEUED
- `v1-ch10` — `நண்பன் நடித்த நாடகம்` — pp. 65–67 — blob `38f3e3efcd8c48a7c3df70c3b5e36b02d813261f` — QUEUED
- `v1-ch11` — `இளம் எழுத்தாளர்` — pp. 68–70 — blob `31e7fcb1770db1a19caaa9725b9b5709f7250454` — QUEUED
- `v1-ch12` — `"எடுக்கவோ, கோக்கவோ?"` — pp. 71–75 — blob `df9bfe3fb369783e68c5166b7068323909d6f4f9` — QUEUED

Opening counters:

- source files pinned: **5 / 5**
- source reviews: **0 / 5**
- T1: **0 / 5**
- T2: **0 / 5**
- T3: **0 / 5**
- thought structure: **0 / 5**
- terminology/cultural: **0 / 5**
- comparator checks: **0 / 5**
- approvals: **0 / 5**

## Immediate next activity — v1-ch08 P0

Perform the complete P0 source review for:

- ID: `v1-ch08`
- Tamil title: `தமிழ் மாணவர் மன்றம்`
- pages: **56–59**
- source ref: `d6621b71256ae99b1c89b4f2091513dcc5f96626`
- source path: `public/data/text/v1-ch08.json`
- source blob: `e041c90234656a6b9fbd4650d607c3ba0b53e5e8`
- extraction units: **4**
- extraction strategy: `wordjoiner`

The intake inspection shows that the first extraction unit begins with the chapter title. Treat that only as an intake flag; decide and document the actual title-repeat handling during P0.

P0 must:

1. read the full pinned Tamil chapter;
2. identify title repeats, page/source-unit joins, OCR/spacing anomalies, quotations, verse/song, chronology-sensitive assertions, non-authorial material and any meaning-affecting uncertainty;
3. create `data/books/nenjukku-needhi/translations/en/source-notes/v1-ch08.json`;
4. update Batch 002, progress and manifest;
5. stop with **T1 next**.

Do **not** translate during P0.

## Mandatory controls

Read before P0:

1. `docs/HANDOVER.md`
2. `docs/TRANSLATION_PLAN.md`
3. `docs/PILOT_METHOD_REVIEW.md`
4. `docs/KALAIGNAR_VOICE_GUIDE.md`
5. `docs/TRANSLATION_GLOSSARY.md`
6. `docs/TRANSLATION_PROGRESS.md`
7. `data/books/nenjukku-needhi/translations/en/manifest.json`
8. `data/books/nenjukku-needhi/translations/en/batches/batch-002.md`

## Infrastructure limitation

`schemas/chapter.json` is a one-byte newline-only legacy placeholder.

Do not claim formal JSON-Schema validation.
