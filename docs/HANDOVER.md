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

`P0 source review → T1 fresh translation → T2 Tamil-English/Kalaignar voice → T3 English-only literary review → thought-structure audit → terminology/cultural audit → final approval → closed`

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
- T2: **5 / 5**
- T3: **5 / 5**
- thought structure: **5 / 5**
- terminology/cultural: **5 / 5**
- approved: **1 / 5**
- unresolved source holds: **0**
- existing-English comparator consulted: **NO**

`v1-ch08` — **Tamil Students' Association — APPROVED / CLOSED**

- T1: **PASS / COMPLETE**
- T2: **PASS WITH REVISION / COMPLETE**
- accepted grouped T2 revisions: **18**
- T3: **PASS WITH MINOR REVISION / COMPLETE**
- accepted grouped T3 revisions: **19**
- thought structure: **PASS / COMPLETE — 18 / 18 major movements**
- reordered / omitted / invented: **0 / 0 / 0**
- terminology/cultural: **PASS WITH ONE REVISION / COMPLETE**
- terminology revision: **sandalwood bowl → sandal-paste bowl**
- unresolved terminology holds: **0**
- unresolved source holds: **0**
- independent English: **FROZEN**
- comparator gate: **NOT APPLICABLE for v1-ch02+**
- final approval: **PASS / APPROVED / CLOSED**
- approval review: `data/books/nenjukku-needhi/translations/en/reviews/v1-ch08-approval.md`
- next gate: **CLOSED**

T2 preserves the exact `தமிழ் வாழ்க! இந்தி வளர்க` slogan, authored 1941/1942 chronology, Bharathidasan verse and historical present, while strengthening Kalaignar's Congress-Communist dominance metaphor, fee arithmetic, wrist-chain materiality, theft-scene internal questions, Chettiar Bank wording, maternal colloquial affection and guilty humour. The mother/wife two-theft parallel remains intact.

The remaining Batch 002 chapters have now completed T2, T3, thought structure and terminology/cultural review:

- `v1-ch09` — **T2 PASS — 12 / T3 PASS — 11 / STRUCTURE PASS — 20 / 20 / TERMINOLOGY PASS WITH ONE REVISION — FINAL APPROVAL NEXT**
- `v1-ch10` — **T2 PASS — 7 / T3 PASS — 10 / STRUCTURE PASS — 12 / 12 / TERMINOLOGY PASS WITH ONE REVISION — FINAL APPROVAL QUEUED**
- `v1-ch11` — **T2 PASS — 7 / T3 PASS — 7 / STRUCTURE PASS — 12 / 12 / TERMINOLOGY PASS WITHOUT REVISION — FINAL APPROVAL QUEUED**
- `v1-ch12` — **T2 PASS — 13 / T3 PASS — 12 / STRUCTURE PASS — 22 / 22 / TERMINOLOGY PASS WITHOUT REVISION — FINAL APPROVAL QUEUED**

Batch 002 T2, T3, thought structure and terminology/cultural are all **5 / 5 COMPLETE**. Across the new terminology audits: **2 source-supported chapter revisions total**, **0 unresolved terminology holds**, **0 unresolved source holds**, and independent English is **frozen 5 / 5**.

## Comparator policy

At the Batch 002 source pin, `pugazg/kalaignar-autobiography/public/data/text-en/` contains only `v1-ch01.json`. The historical `v1-ch01` comparison remains archived, but comparator availability/absence is no longer a production gate for later chapters.

## Immediate next activity — v1-ch09 final approval

Run the **final approval review** for `v1-ch09` only. Verify P0, T1, T2, T3, thought structure, terminology/cultural consistency, frozen independent English, zero unresolved holds and syntactic JSON parseability. If all pass, approve and close `v1-ch09`. Stop before beginning `v1-ch10` final approval.

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
