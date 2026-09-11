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

Current counters:

- source reviews: **5 / 5**
- T1: **5 / 5**
- T2: **1 / 5**
- T3: **0 / 5**
- unresolved source holds: **0**
- existing-English comparator consulted: **NO**

`v1-ch08` — **Tamil Students' Association**

- T1: **PASS / COMPLETE**
- T2: **PASS WITH REVISION / COMPLETE**
- accepted grouped T2 revisions: **18**
- unresolved source holds: **0**
- blocking T2 issues: **0**
- next gate: **T3**

T2 preserves the exact `தமிழ் வாழ்க! இந்தி வளர்க` slogan, authored 1941/1942 chronology, Bharathidasan verse and historical present, while strengthening Kalaignar's Congress-Communist dominance metaphor, fee arithmetic, wrist-chain materiality, theft-scene internal questions, Chettiar Bank wording, maternal colloquial affection and guilty humour. The mother/wife two-theft parallel remains intact.

The remaining Batch 002 chapters `v1-ch09`–`v1-ch12` remain **T1 COMPLETE / T2 QUEUED**.

## Immediate next activity — v1-ch08 T3

Run the **T3 English-only literary review** of `v1-ch08`. Read the revised English first without consulting Tamil; then recheck every proposed fluency change against the pinned Tamil before accepting it. Do not consult existing English.

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
