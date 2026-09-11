# Batch 002 — Volume 1 Chapters 8–12

Status: **OPEN / `v1-ch08` SOURCE REVIEW NEXT**

Source repository: `pugazg/kalaignar-autobiography` — **READ ONLY**

Pinned source ref for Batch 002 opening:

`d6621b71256ae99b1c89b4f2091513dcc5f96626`

Previous Batch 001 source pin:

`5c6b5ef8901044660e607d4649238d7c66cb648d`

Repository-level source `main` advanced between the two batch pins, but the selected `v1-ch08`–`v1-ch12` chapter blobs are unchanged from the Batch 001 pin. Batch 002 nevertheless uses the live source `main` at opening as its own authority pin, per project policy.

Write repository: `pugazg/nenjukku-needhi-archive`

Working branch: `main`

## Batch-size decision

Normal production batch size is **5 chapters**, reduced to 1–3 only for unusually long or difficult chapters.

Intake inspection for `v1-ch08`–`v1-ch12` found:

| ID | Tamil title | Pages | Extraction units | Approx. Tamil chars | Source blob SHA |
|---|---|---:|---:|---:|---|
| `v1-ch08` | `தமிழ் மாணவர் மன்றம்` | 56–59 | 4 | 7,940 | `e041c90234656a6b9fbd4650d607c3ba0b53e5e8` |
| `v1-ch09` | `கலகக்கார நாரதர் புகுந்தார்.` | 60–64 | 5 | 9,233 | `e3104c0f74478f25d0b15c4bb1ed12afd6420d21` |
| `v1-ch10` | `நண்பன் நடித்த நாடகம்` | 65–67 | 3 | 4,929 | `38f3e3efcd8c48a7c3df70c3b5e36b02d813261f` |
| `v1-ch11` | `இளம் எழுத்தாளர்` | 68–70 | 3 | 4,088 | `31e7fcb1770db1a19caaa9725b9b5709f7250454` |
| `v1-ch12` | `"எடுக்கவோ, கோக்கவோ?"` | 71–75 | 5 | 9,125 | `df9bfe3fb369783e68c5166b7068323909d6f4f9` |

These are all modest 3–5-page chapters with no intake-level length signal requiring a reduced batch. Therefore Batch 002 uses the standard **five-chapter span `v1-ch08`–`v1-ch12`**.

This intake inspection is **not** a P0 source review. It does not authorize translation decisions or source normalization.

## Chapter queue

| ID | Tamil title | Pages | Current status |
|---|---|---:|---|
| `v1-ch08` | `தமிழ் மாணவர் மன்றம்` | 56–59 | **P0 SOURCE REVIEW NEXT** |
| `v1-ch09` | `கலகக்கார நாரதர் புகுந்தார்.` | 60–64 | **PINNED / QUEUED** |
| `v1-ch10` | `நண்பன் நடித்த நாடகம்` | 65–67 | **PINNED / QUEUED** |
| `v1-ch11` | `இளம் எழுத்தாளர்` | 68–70 | **PINNED / QUEUED** |
| `v1-ch12` | `"எடுக்கவோ, கோக்கவோ?"` | 71–75 | **PINNED / QUEUED** |

## Batch rule

This batch is a management envelope.

- process one chapter at a time;
- P0 source review and source notes must complete before T1 for that chapter;
- finish required gates before materially moving to the next chapter;
- do not start `v1-ch13` until Batch 002 is closed;
- source repository remains strictly read-only;
- existing English is never drafting authority.

## Opening counters

- batch opened: **YES**
- source files pinned: **5 / 5**
- full source reviews complete: **0 / 5**
- T1 complete: **0 / 5**
- T2 complete: **0 / 5**
- T3 complete: **0 / 5**
- thought-structure complete: **0 / 5**
- terminology/cultural complete: **0 / 5**
- comparator checks complete: **0 / 5**
- approved chapters: **0 / 5**

## Immediate next activity

Run the complete **P0 source review for `v1-ch08` — `தமிழ் மாணவர் மன்றம்`, pages 56–59**.

Use:

- source ref: `d6621b71256ae99b1c89b4f2091513dcc5f96626`
- source path: `public/data/text/v1-ch08.json`
- source blob: `e041c90234656a6b9fbd4650d607c3ba0b53e5e8`
- extraction units: **4**
- source strategy: `wordjoiner`

The first extraction unit begins with the chapter title, but whether/how that repeated heading is excluded must be decided and documented during P0 rather than assumed from intake inspection.

Stop after P0 with **T1 next**. Do not translate during the P0 activity.

## Infrastructure limitation

`schemas/chapter.json` remains a one-byte newline-only legacy placeholder.

Do not claim formal JSON-Schema validation.
