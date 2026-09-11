# NEXT CHAT PROMPT — Nenjukku Needhi / Open Batch 002

Continue directly in `pugazg/nenjukku-needhi-archive`, branch `main`.

## LIVE MAIN IS AUTHORITATIVE

Fetch live `main` first and preserve newer durable work.

The source repository is strictly **READ ONLY**:

`pugazg/kalaignar-autobiography`

Never modify it.

## Durable state

Batch 001 (`v1-ch03`–`v1-ch07`) is **CLOSED**.

All five chapters are **APPROVED / CLOSED**.

Batch 001 final counters:

- source reviews: **5 / 5**
- T1: **5 / 5**
- T2: **5 / 5**
- T3: **5 / 5**
- thought structure: **5 / 5**
- terminology/cultural: **5 / 5**
- comparator checks: **5 / 5**
- approvals: **5 / 5**
- unresolved source holds: **0**
- outstanding review items: **0**

Batch 001 source pin:

`5c6b5ef8901044660e607d4649238d7c66cb648d`

Latest observed source `main` at closure:

`d6621b71256ae99b1c89b4f2091513dcc5f96626`

There is currently **no active production batch**.

`v1-ch08` has **not** been started.

## Mandatory startup reading

Read completely before changing anything:

1. `docs/HANDOVER.md`
2. `docs/TRANSLATION_PLAN.md`
3. `docs/PILOT_METHOD_REVIEW.md`
4. `docs/KALAIGNAR_VOICE_GUIDE.md`
5. `docs/TRANSLATION_GLOSSARY.md`
6. `docs/TRANSLATION_PROGRESS.md`
7. `data/books/nenjukku-needhi/translations/en/manifest.json`
8. `data/books/nenjukku-needhi/translations/en/batches/batch-001.md`

## Immediate next activity — open Batch 002 only

Do **not** begin `v1-ch08` T1 in this activity.

1. Fetch live source `main` from the read-only source repository.
2. Treat that live source state as the candidate Batch 002 opening pin; record any drift from Batch 001.
3. Inspect `v1-ch08` onward enough to determine chapter size/difficulty and select the Batch 002 span.
   - normal size: **5 chapters**;
   - reduce to **1–3** only for unusually long/difficult material.
4. Fetch and pin the selected source chapter blobs.
5. Create:
   `data/books/nenjukku-needhi/translations/en/batches/batch-002.md`
6. Update:
   - `data/books/nenjukku-needhi/translations/en/manifest.json`
   - `docs/TRANSLATION_PROGRESS.md`
   - `docs/HANDOVER.md`
   - `docs/NEXT_CHAT_PROMPT.md`
7. Stop with **`v1-ch08` P0 source review next**.

## Method constraints

- source repository remains READ ONLY;
- existing English is never drafting authority;
- process chapters sequentially inside the batch;
- P0/source notes must complete before T1;
- do not silently normalize source anomalies or authored chronology;
- do not claim formal JSON-Schema validation while `schemas/chapter.json` remains a one-byte legacy placeholder.
