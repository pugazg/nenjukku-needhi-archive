# Nenjukku Needhi — English Translation Progress

## Authority

- Tamil source repository: `pugazg/kalaignar-autobiography` — **READ ONLY**
- Source path: `public/data/text/*.json`
- Batch 001 pinned source ref: `5c6b5ef8901044660e607d4649238d7c66cb648d`
- Latest observed source `main`: `bb0beaa0a18f97336b52319c1e7b15e62d81d1ed`
- `v1-ch04` source blob is identical at both refs: `1b55b986176d330fab4ce16eb70565ddd895ba48`
- Write repository: `pugazg/nenjukku-needhi-archive`
- Working branch: `main`

## Corpus

- Volume 1: 140 chapters
- Volume 2: 77 chapters
- Volume 3: 73 chapters
- Volume 4: 22 chapters
- Volume 5: 50 chapters
- Volume 6: 29 chapters
- Total: 391 chapters

## Project gates

- Translation plan: **COMPLETE FOR PRODUCTION**
- Two-pilot method review: **COMPLETE**
- Kalaignar Voice Guide: **LIVING / UPDATED THROUGH `v1-ch04`**
- Translation glossary: **LIVING / UPDATED THROUGH `v1-ch04` T3**
- Source-note convention: **DEFINED AND IN USE**
- Pilot `v1-ch01`: **APPROVED / CLOSED**
- Pilot `v1-ch02`: **APPROVED / CLOSED WITH 2 DOCUMENTED ACCEPTED SCHOLARLY UNCERTAINTIES**
- Pilot phase: **COMPLETE**
- Production translation: **OPEN**
- Active production batch: **Batch 001 — `v1-ch03`–`v1-ch07`**

## Production method

Normal production batch size is 5 chapters, but the batch is a management envelope. Process one chapter at a time through:

`source review → source notes → T1 → T2 → T3 → thought structure → terminology/cultural audit → post-freeze comparator if applicable → approval`

## Active Batch 001

| Chapter | Tamil title | Pages | Current status |
|---|---|---:|---|
| `v1-ch03` | `"சிவாய நம! ஓம் நமசிவாய"` | 30–36 | **APPROVED / CLOSED** |
| `v1-ch04` | `என்னுடைய அரசியல் அரிச்சுவடி` | 37–41 | **APPROVED / CLOSED** |
| `v1-ch05` | `நீதிக் கட்சியில் பல மாற்றங்கள்` | 42–45 | **SOURCE REVIEW NEXT** |
| `v1-ch06` | `தமிழ் காக்கும் போர் முனை` | 46–50 | not started |
| `v1-ch07` | `"நீங்களா 'மாணவ நேசன்' நடத்துகிறீர்கள்?"` | 51–55 | not started |

## `v1-ch03`

Final status: **APPROVED / CLOSED**.

- source review: PASS
- T1: PASS
- T2: PASS WITH REVISION
- T3: PASS WITH MINOR REVISION
- thought structure: PASS — 24/24 major movements preserved
- terminology/cultural consistency: PASS
- unresolved source holds: 0
- existing-English comparator at pinned ref: none

## `v1-ch04` — approved / closed

Durable files:

- translation: `data/books/nenjukku-needhi/translations/en/chapters/v1-ch04.json`
- source notes: `data/books/nenjukku-needhi/translations/en/source-notes/v1-ch04.json`
- T2 review: `data/books/nenjukku-needhi/translations/en/reviews/v1-ch04-t2.md`
- T3 review: `data/books/nenjukku-needhi/translations/en/reviews/v1-ch04-t3.md`
- thought-structure audit: `data/books/nenjukku-needhi/translations/en/reviews/v1-ch04-structure.md`
- final approval review: `data/books/nenjukku-needhi/translations/en/reviews/v1-ch04-approval.md`

Gate state:

- source review: **PASS**;
- T1: **PASS / COMPLETE**;
- T2: **PASS WITH REVISION / COMPLETE**;
- T3: **PASS WITH MINOR REVISION / COMPLETE — 10 source-checked revisions**;
- thought structure: **PASS — 20 / 20 major movements preserved**;
- terminology/cultural consistency: **PASS**;
- post-freeze comparator: **NONE at pinned source ref**;
- final approval: **PASS / APPROVED**;
- unresolved source holds: **0**;
- outstanding review items: **0**.

Final decisions include:

- `தென்னிந்திய நல உரிமைச் சங்கம்` → **South Indian Liberal Federation (SILF)** as disclosed proper-name normalisation;
- `முதல் மந்திரி` → **First Minister** for the 1920s Madras Presidency;
- `சட்டசபைத் தலைவர்` → **President of the Legislative Council** for that period;
- `இந்தியா மந்திரி` → **Secretary of State for India** when referring to Edwin Montagu;
- `Justice Party`, `Self-Respect Movement`, `rationalism`, `backward communities`, and `depressed communities/people` remain the context-sensitive historical working forms;
- `திராவிடப் பெருங்குடி` remains **great Dravidian community**;
- `விடிவெள்ளி` remains **morning star for the Dravidians**;
- `சொற்போர்` remains **verbal debates**;
- the `அரிச்சுவடி` → political-primer architecture remains intact;
- T3 removed translator-added `in their view` from the Home Rule comparison and changed pejorative-risk `schemes` to neutral `plans` for `திட்டங்கள்`;
- historical claims remain authored claims; external evidence is used only for terminology/proper-name/institutional normalisation.

## Batch 001 counters

- source files pinned: **5 / 5**
- full source reviews complete: **2 / 5**
- T1 complete: **2 / 5**
- T2 complete: **2 / 5**
- T3 complete: **2 / 5**
- thought-structure complete: **2 / 5**
- approved: **2 / 5**

## Infrastructure note

`schemas/chapter.json` is currently an empty one-byte legacy placeholder, so formal JSON-Schema execution is not available under current repository controls.

## Branch consolidation

The former working branch `translation/english-memoir` was merged into `main` via PR #1. All further translation work is performed directly on `main`; the old branch is not an active work surface.

## Next activity

Begin the complete source review for `v1-ch05` (`நீதிக் கட்சியில் பல மாற்றங்கள்`, pp. 42–45) before T1. Its first extraction unit begins with damaged `-ல்` after the repeated chapter heading, so the missing leading text must be investigated and documented rather than silently reconstructed.
