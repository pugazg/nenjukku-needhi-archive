# Batch 003 — Volume 1 Chapters 13–17

Status: **OPEN / `v1-ch13` P0 SOURCE REVIEW NEXT**

Source repository: `pugazg/kalaignar-autobiography` — **READ ONLY**

Pinned source ref for Batch 003 opening:

`d6621b71256ae99b1c89b4f2091513dcc5f96626`

Previous Batch 002 source pin:

`d6621b71256ae99b1c89b4f2091513dcc5f96626`

The live source `main` has not advanced since Batch 002. Batch 003 nevertheless records the freshly fetched live source SHA as its own batch authority pin.

Write repository: `pugazg/nenjukku-needhi-archive`

Working branch: `main`

## Batch-size decision

Normal production batch size is **5 chapters**, reduced to 1–3 only for unusually long or difficult chapters.

Intake inspection for `v1-ch13`–`v1-ch17` found:

| ID | Tamil title | Pages | Extraction units | Approx. Tamil chars | Source blob SHA |
|---|---|---:|---:|---:|---|
| `v1-ch13` | `மாமனார் தந்த வரவேற்பு` | 76–80 | 5 | 9,331 | `80fc03e2092ab69b22879e65ab6887acc4284a55` |
| `v1-ch14` | `வாழ்வதற்கு வழி? நடிகனானேன் நான்!` | 81–84 | 4 | 7,261 | `1fa0f359d8da9cbeb2d9b03fa6244badbece89f6` |
| `v1-ch15` | `நண்பர்கள் முகம் வாடலாமா?` | 85–89 | 5 | 9,596 | `ceb2759588dfec6646a4ba53369fce02c0bd9c92` |
| `v1-ch16` | `கம்புகள்! குண்டாந்தடிகள்!` | 90–93 | 4 | 6,654 | `fd6793f228db38098aff1eddcfb7fefce3fff3d2` |
| `v1-ch17` | `குளிப்பது ஒரு குற்றமா?` | 94–98 | 5 | 8,473 | `eac5cc2193a40fc7c59c88f8d7a8eec65f0e8f66` |

All five are modest 4–5-page chapters. No intake-level length/difficulty signal requires a reduced span.

Therefore Batch 003 uses the standard **five-chapter span `v1-ch13`–`v1-ch17`**.

This intake inspection is **not** a P0 source review. It does not authorize translation decisions, source normalization, title-repeat handling, page-join reconstruction, or any other source intervention.

## Chapter queue

| ID | Tamil title | Pages | Current status |
|---|---|---:|---|
| `v1-ch13` | `மாமனார் தந்த வரவேற்பு` | 76–80 | **P0 SOURCE REVIEW NEXT** |
| `v1-ch14` | `வாழ்வதற்கு வழி? நடிகனானேன் நான்!` | 81–84 | **PINNED / QUEUED** |
| `v1-ch15` | `நண்பர்கள் முகம் வாடலாமா?` | 85–89 | **PINNED / QUEUED** |
| `v1-ch16` | `கம்புகள்! குண்டாந்தடிகள்!` | 90–93 | **PINNED / QUEUED** |
| `v1-ch17` | `குளிப்பது ஒரு குற்றமா?` | 94–98 | **PINNED / QUEUED** |

## Opening counters

- batch opened: **YES**
- source files pinned: **5 / 5**
- full source reviews complete: **0 / 5**
- T1 complete: **0 / 5**
- T2 complete: **0 / 5**
- T3 complete: **0 / 5**
- thought-structure complete: **0 / 5**
- terminology/cultural complete: **0 / 5**
- approved chapters: **0 / 5**
- unresolved source holds: **0**
- translations started: **0**

## Batch rule

- process chapters sequentially unless the user explicitly authorizes a batch-wide gate;
- P0 source review and source notes must complete before T1 for a chapter;
- source pixels/text at the pinned read-only source are controlling;
- document source anomalies; never silently normalize;
- existing English is not a production gate for `v1-ch02+`;
- do not start `v1-ch18` until Batch 003 is closed.

## Immediate next activity

Run **P0 source review for `v1-ch13` only**.

Source identity:

- ID: `v1-ch13`
- title: `மாமனார் தந்த வரவேற்பு`
- pages: **76–80**
- source path: `public/data/text/v1-ch13.json`
- source ref: `d6621b71256ae99b1c89b4f2091513dcc5f96626`
- source blob: `80fc03e2092ab69b22879e65ab6887acc4284a55`
- extraction units: **5**
- extraction strategy: `wordjoiner`

P0 must read the full pinned Tamil and record title repeats, page/source-unit joins, OCR or spacing anomalies, quotations, verse/song, chronology-sensitive claims, non-authorial material, duplicated source material, textual/semantic holds and paragraph-reconstruction needs.

Do **not** translate during P0.

## Infrastructure limitation

`schemas/chapter.json` remains a one-byte newline-only legacy placeholder.

Do not claim formal JSON-Schema validation.
