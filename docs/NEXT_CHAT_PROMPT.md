# NEXT CHAT PROMPT — Nenjukku Needhi / Open Batch 004

Continue directly in `pugazg/nenjukku-needhi-archive`, branch `main`.

## LIVE MAIN IS AUTHORITATIVE

Fetch live writable `main` first and preserve newer durable work.

The source repository remains strictly **READ ONLY**:

`pugazg/kalaignar-autobiography`

Never modify the source repository.

## Durable production state

Batch 001: **CLOSED / 5 OF 5 APPROVED**

Batch 002: **CLOSED / 5 OF 5 APPROVED**

Batch 003: **CLOSED / 5 OF 5 APPROVED**

Batch 003 source pin:

`d6621b71256ae99b1c89b4f2091513dcc5f96626`

Batch 003 chapters:

- `v1-ch13` — APPROVED / CLOSED
- `v1-ch14` — APPROVED / CLOSED
- `v1-ch15` — APPROVED / CLOSED
- `v1-ch16` — APPROVED / CLOSED
- `v1-ch17` — APPROVED / CLOSED

Final Batch 003 counters:

- source reviews: **5 / 5**
- T1: **5 / 5**
- T2: **5 / 5**
- T3: **5 / 5**
- thought structure: **5 / 5**
- terminology/cultural: **5 / 5**
- approved: **5 / 5**
- independent English frozen: **5 / 5**
- unresolved source holds: **0**
- unresolved terminology holds: **0**
- outstanding review items: **0**

No active production batch currently exists.

## Batch 003 durable review highlights

- `v1-ch13`: T2 **9**, T3 **6**, structure **20/20**, terminology **PASS WITH ONE REVISION**
- `v1-ch14`: T2 **8**, T3 **5**, structure **16/16**, terminology **PASS WITH ONE REVISION**
- `v1-ch15`: T2 **7**, T3 **6**, structure **18/18**, terminology **PASS WITH ONE REVISION**
- `v1-ch16`: T2 **5**, T3 **5**, structure **16/16**, terminology **PASS WITHOUT REVISION**
- `v1-ch17`: T2 **7**, T3 **5**, structure **19/19**, terminology **PASS WITHOUT REVISION**

Terminology revisions:

- `v1-ch13`: **Children's Reform Association** continuity restored;
- `v1-ch14`: first-use **cheri settlement**;
- `v1-ch15`: **depressed communities** per period glossary policy;
- `v1-ch16`–`v1-ch17`: no terminology-stage chapter-text changes.

The `ஜன்னி` item in `v1-ch13` is resolved conservatively without asserting a modern diagnosis.

## Comparator policy

The source repository's `public/data/text-en/` directory contains only `v1-ch01.json` in the production source state already examined.

Comparator checking is **not a production gate for `v1-ch02` onward**. Do not search unofficial English translations.

## Immediate activity — open Batch 004 only

Start from `v1-ch18`.

1. Fetch live source-repository `main`.
2. Record that live source SHA as the Batch 004 source pin.
3. Inspect `v1-ch18` onward for chapter length/difficulty.
4. Under the normal policy, use a **five-chapter batch** unless one or more chapters are unusually long/difficult enough to justify reducing the span to 1–3.
5. Create:
   `data/books/nenjukku-needhi/translations/en/batches/batch-004.md`
6. Update:
   - `data/books/nenjukku-needhi/translations/en/manifest.json`
   - `docs/TRANSLATION_PROGRESS.md`
   - `docs/HANDOVER.md`
   - `docs/NEXT_CHAT_PROMPT.md`
7. Do **not** translate any chapter during Batch 004 opening.
8. Stop with `v1-ch18` **P0 source review next**.

## Mandatory method

`P0 source review → T1 → T2 → T3 → thought-structure audit → terminology/cultural audit → final approval → closed`

Existing English is never drafting authority.

## Infrastructure limitation

`schemas/chapter.json` remains a one-byte newline-only legacy placeholder.

Do not claim formal JSON-Schema validation.
