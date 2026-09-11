# NEXT CHAT PROMPT — Nenjukku Needhi / v1-ch09 Terminology-Cultural Audit

Continue directly in `pugazg/nenjukku-needhi-archive`, branch `main`.

## LIVE MAIN IS AUTHORITATIVE

Fetch live `main` first and preserve newer durable work.

The source repository remains strictly **READ ONLY**:

`pugazg/kalaignar-autobiography`

Batch 002 source pin:

`d6621b71256ae99b1c89b4f2091513dcc5f96626`

## Comparator policy

The source repository's `public/data/text-en/` directory contains only `v1-ch01.json` at the Batch 002 pin. Comparator checking is **not a production gate for `v1-ch02` onward**.

## Batch 002 state

- source reviews: **5 / 5**
- T1: **5 / 5**
- T2: **5 / 5**
- T3: **5 / 5**
- thought structure: **5 / 5**
- terminology/cultural: **1 / 5**
- approved: **1 / 5**
- unresolved source holds: **0**

Structure results:

- `v1-ch08` — PASS — 18 / 18 — APPROVED / CLOSED
- `v1-ch09` — PASS — 20 / 20
- `v1-ch10` — PASS — 12 / 12
- `v1-ch11` — PASS — 12 / 12
- `v1-ch12` — PASS — 22 / 22

Across the new audits:

- reordered: **0**
- omitted: **0**
- invented: **0**
- chapter-text changes: **0**

## Active chapter

`v1-ch09` — **Troublemaker Narada Entered**

- pages: **60–64**
- source blob: `e3104c0f74478f25d0b15c4bb1ed12afd6420d21`
- source review: **PASS**
- T1: **PASS**
- T2: **PASS WITH REVISION — 12 grouped revisions**
- T3: **PASS WITH MINOR REVISION — 11 grouped revisions**
- thought structure: **PASS — 20 / 20**
- unresolved source holds: **0**
- next gate: **terminology/cultural**

Durable files:

- `data/books/nenjukku-needhi/translations/en/source-notes/v1-ch09.json`
- `data/books/nenjukku-needhi/translations/en/chapters/v1-ch09.json`
- `data/books/nenjukku-needhi/translations/en/reviews/v1-ch09-t2.md`
- `data/books/nenjukku-needhi/translations/en/reviews/v1-ch09-t3.md`
- `data/books/nenjukku-needhi/translations/en/reviews/v1-ch09-structure.md`

## Immediate activity — terminology/cultural audit only

Review the independent English against:

1. `docs/TRANSLATION_GLOSSARY.md`
2. `docs/KALAIGNAR_VOICE_GUIDE.md`
3. terminology precedents in approved chapters.

Give particular attention to:

- School Final / examination vocabulary;
- Kudi Arasu press / publication references;
- Periyar E. V. R.;
- Tirukkuvalai / Nagapattinam;
- Indirani / Indra / Narada / Dhruva / Kali / Ahalya;
- `Dhruvan` as the play title;
- Murasoli Maran;
- child-speech representation;
- sandal-paste / silver-bowl continuity from `v1-ch08`;
- election deposit terminology;
- educational-policy vocabulary;
- any culture-specific image that should remain source-led rather than normalized away.

Do not consult existing English.

Create:

`data/books/nenjukku-needhi/translations/en/reviews/v1-ch09-terminology.md`

If the audit passes, freeze the independent English and set the next gate to **final approval**.

## Infrastructure limitation

`schemas/chapter.json` remains a one-byte newline-only legacy placeholder. Do not claim formal JSON-Schema validation.
