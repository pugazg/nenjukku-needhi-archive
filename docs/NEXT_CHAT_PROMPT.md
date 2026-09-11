# NEXT CHAT PROMPT — Nenjukku Needhi / v1-ch13 P0 Source Review

Continue directly in `pugazg/nenjukku-needhi-archive`, branch `main`.

## LIVE MAIN IS AUTHORITATIVE

Fetch live writable `main` first and preserve newer durable work.

The source repository remains strictly **READ ONLY**:

`pugazg/kalaignar-autobiography`

Never modify the source repository.

## Batch 003 — OPEN

Source pin:

`d6621b71256ae99b1c89b4f2091513dcc5f96626`

Span:

`v1-ch13`–`v1-ch17`

Batch-size decision:

**standard five-chapter batch retained**

Intake metadata:

- `v1-ch13` — `மாமனார் தந்த வரவேற்பு` — pages 76–80 — 5 units — blob `80fc03e2092ab69b22879e65ab6887acc4284a55`
- `v1-ch14` — `வாழ்வதற்கு வழி? நடிகனானேன் நான்!` — pages 81–84 — 4 units — blob `1fa0f359d8da9cbeb2d9b03fa6244badbece89f6`
- `v1-ch15` — `நண்பர்கள் முகம் வாடலாமா?` — pages 85–89 — 5 units — blob `ceb2759588dfec6646a4ba53369fce02c0bd9c92`
- `v1-ch16` — `கம்புகள்! குண்டாந்தடிகள்!` — pages 90–93 — 4 units — blob `fd6793f228db38098aff1eddcfb7fefce3fff3d2`
- `v1-ch17` — `குளிப்பது ஒரு குற்றமா?` — pages 94–98 — 5 units — blob `eac5cc2193a40fc7c59c88f8d7a8eec65f0e8f66`

The live source `main` is unchanged from Batch 002, but Batch 003 independently pins the freshly fetched live SHA above.

Opening counters:

- source files pinned: **5 / 5**
- source reviews: **0 / 5**
- T1: **0 / 5**
- T2: **0 / 5**
- T3: **0 / 5**
- thought structure: **0 / 5**
- terminology/cultural: **0 / 5**
- approved: **0 / 5**
- translations started: **0**

## Comparator policy

The source repository's `public/data/text-en/` directory contains only `v1-ch01.json` at the relevant production source state.

Comparator checking is **not a production gate for `v1-ch02` onward**.

## Mandatory startup

Read completely before source-dependent work:

1. `docs/HANDOVER.md`
2. `docs/TRANSLATION_PLAN.md`
3. `docs/PILOT_METHOD_REVIEW.md`
4. `docs/KALAIGNAR_VOICE_GUIDE.md`
5. `docs/TRANSLATION_GLOSSARY.md`
6. `docs/TRANSLATION_PROGRESS.md`
7. `data/books/nenjukku-needhi/translations/en/manifest.json`
8. `data/books/nenjukku-needhi/translations/en/batches/batch-003.md`

## Immediate activity — P0 only

Active chapter:

`v1-ch13` — `மாமனார் தந்த வரவேற்பு`

Source identity:

- pages: **76–80**
- source path: `public/data/text/v1-ch13.json`
- source ref: `d6621b71256ae99b1c89b4f2091513dcc5f96626`
- source blob: `80fc03e2092ab69b22879e65ab6887acc4284a55`
- extraction units: **5**
- extraction strategy: `wordjoiner`

Read the **full pinned Tamil**.

Review and document:

- repeated title at source start, if any;
- source-unit/page joins and broken words;
- OCR/spacing/extraction anomalies;
- quotation/dialogue boundaries;
- verse/song or quoted literary material;
- names, dates and chronology-sensitive assertions;
- political/institutional names;
- non-authorial editorial material;
- duplicated source content;
- textual-reading holds;
- semantic-interpretation holds;
- paragraph-reconstruction needs;
- culture-specific material that will require careful T1 treatment.

Do not silently normalize the Tamil source.

Create:

`data/books/nenjukku-needhi/translations/en/source-notes/v1-ch13.json`

Then update:

- `data/books/nenjukku-needhi/translations/en/batches/batch-003.md`
- `data/books/nenjukku-needhi/translations/en/manifest.json`
- `docs/TRANSLATION_PROGRESS.md`
- `docs/HANDOVER.md`
- `docs/NEXT_CHAT_PROMPT.md`

Stop with **T1 fresh translation for `v1-ch13` next**.

Do **not** translate during P0.

## Infrastructure limitation

`schemas/chapter.json` remains a one-byte newline-only legacy placeholder.

Do not claim formal JSON-Schema validation.
