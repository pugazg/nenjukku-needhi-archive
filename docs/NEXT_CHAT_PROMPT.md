# NEXT CHAT PROMPT — Nenjukku Needhi / Open Batch 003

Continue directly in `pugazg/nenjukku-needhi-archive`, branch `main`.

## LIVE MAIN IS AUTHORITATIVE

Fetch live writable `main` first and preserve newer durable work.

Source repository remains strictly **READ ONLY**:

`pugazg/kalaignar-autobiography`

Never modify the source repository.

## Durable production state

Batch 001: **CLOSED / 5 OF 5 APPROVED**

Batch 002: **CLOSED / 5 OF 5 APPROVED**

Batch 002 source pin:

`d6621b71256ae99b1c89b4f2091513dcc5f96626`

Batch 002 chapters:

- `v1-ch08` — APPROVED / CLOSED
- `v1-ch09` — APPROVED / CLOSED
- `v1-ch10` — APPROVED / CLOSED
- `v1-ch11` — APPROVED / CLOSED
- `v1-ch12` — APPROVED / CLOSED

Final Batch 002 counters:

- source reviews: **5 / 5**
- T1: **5 / 5**
- T2: **5 / 5**
- T3: **5 / 5**
- thought structure: **5 / 5**
- terminology/cultural: **5 / 5**
- approved: **5 / 5**
- unresolved source holds: **0**
- unresolved terminology holds: **0**
- outstanding review items: **0**

No active production batch currently exists.

## Comparator policy

At the Batch 002 source pin, the source repository's `public/data/text-en/` directory contains only `v1-ch01.json`.

Comparator checking is **not a production gate for `v1-ch02` onward**. Preserve the historical `v1-ch01` comparator record, but do not create per-chapter absence checks or search unofficial English versions.

## Immediate activity — open Batch 003 only

Start from `v1-ch13`.

1. Fetch live source-repository `main`.
2. Record that live source SHA as the Batch 003 source pin.
3. Inspect `v1-ch13` onward for chapter length/difficulty.
4. Under the normal policy, use a **five-chapter batch** unless one or more chapters are unusually long/difficult enough to justify reducing the span to 1–3.
5. Create:
   `data/books/nenjukku-needhi/translations/en/batches/batch-003.md`
6. Update:
   - `data/books/nenjukku-needhi/translations/en/manifest.json`
   - `docs/TRANSLATION_PROGRESS.md`
   - `docs/HANDOVER.md`
   - `docs/NEXT_CHAT_PROMPT.md`
7. Do **not** translate any chapter during Batch 003 opening.
8. Stop with `v1-ch13` **P0 source review next**.

## Mandatory method

Production workflow:

`P0 source review → T1 → T2 → T3 → thought-structure audit → terminology/cultural audit → final approval → closed`

Existing English is never drafting authority.

## Infrastructure limitation

`schemas/chapter.json` remains a one-byte newline-only legacy placeholder.

Do not claim formal JSON-Schema validation.
