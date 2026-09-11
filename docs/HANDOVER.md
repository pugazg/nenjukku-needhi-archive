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

Source pin: `d6621b71256ae99b1c89b4f2091513dcc5f96626`

Span: **`v1-ch08`–`v1-ch12`**

At the user's explicit instruction, fresh T1 translation was completed across the entire active batch after P0/source review was completed for every chapter.

- source reviews: **5 / 5**
- T1: **5 / 5**
- T2: **0 / 5**
- unresolved source holds: **0**
- existing-English comparator consulted: **NO**

T1 chapters:

- `v1-ch08` — **Tamil Students' Association**
- `v1-ch09` — **Troublemaker Narada Entered**
- `v1-ch10` — **The Drama My Friend Acted Out**
- `v1-ch11` — **The Young Writer**
- `v1-ch12` — **"Shall I Pick Them Up, or String Them?"**

The batch-wide T1 preserves source-led joins, verse/drama lineation, direct speech, political and organizational distinctions, authored chronology, humour, self-irony, exam-failure reflection, and the embedded 1944 Murasoli leaflet. No prior English was consulted.

## Immediate next activity — v1-ch08 T2

Perform the T2 Tamil-English source-and-Kalaignar-voice review for `v1-ch08` only. Subsequent review gates remain sequential unless the user explicitly authorizes another batch-wide gate.

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
