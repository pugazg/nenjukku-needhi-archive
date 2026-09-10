# Batch 001 — Volume 1 Chapters 3–7

Status: **OPEN / `v1-ch05` TERMINOLOGY-CULTURAL PASS / COMPARATOR CHECK NEXT**

Source repository: `pugazg/kalaignar-autobiography` — **READ ONLY**

Pinned source ref for batch opening: `5c6b5ef8901044660e607d4649238d7c66cb648d`

Latest source-main drift check during `v1-ch05` source review: `d6621b71256ae99b1c89b4f2091513dcc5f96626`; `v1-ch05` blob remains byte-identical at `220fb5271eac48c6988057d0d464d5950fd822a3`, so Batch 001 authority remains the opening pin.

Write repository: `pugazg/nenjukku-needhi-archive`

Working branch: `main`

## Batch rule

This five-chapter batch is a management envelope. Process one chapter at a time through its gates; do not bulk-translate all five in one iteration and do not start `v1-ch08` until Batch 001 is closed.

## Chapters

| ID | Tamil title | Pages | Source blob SHA | Current status |
|---|---|---:|---|---|
| `v1-ch03` | `"சிவாய நம! ஓம் நமசிவாய"` | 30–36 | `e7c0d550d68f8b30d9c48a22019e017f7034ff93` | **APPROVED / CLOSED** |
| `v1-ch04` | `என்னுடைய அரசியல் அரிச்சுவடி` | 37–41 | `1b55b986176d330fab4ce16eb70565ddd895ba48` | **APPROVED / CLOSED** |
| `v1-ch05` | `நீதிக் கட்சியில் பல மாற்றங்கள்` | 42–45 | `220fb5271eac48c6988057d0d464d5950fd822a3` | **TERMINOLOGY-CULTURAL PASS / COMPARATOR CHECK NEXT** |
| `v1-ch06` | `தமிழ் காக்கும் போர் முனை` | 46–50 | `8f93218b297262319d82f89274dbee3d1de803f5` | queued for source review |
| `v1-ch07` | `"நீங்களா 'மாணவ நேசன்' நடத்துகிறீர்கள்?"` | 51–55 | `13b1f1d06abeb762ed5f016818fa282b78ba7593` | queued for source review |

## `v1-ch03` closure

Durable files:

- translation: `../chapters/v1-ch03.json`
- source notes: `../source-notes/v1-ch03.json`
- T2 review: `../reviews/v1-ch03-t2.md`
- T3 review: `../reviews/v1-ch03-t3.md`
- thought-structure audit: `../reviews/v1-ch03-structure.md`
- final approval review: `../reviews/v1-ch03-approval.md`

Final status: **APPROVED / CLOSED** with source review, T1, T2, T3, thought structure and terminology/cultural gates passed; unresolved source holds `0`.

## `v1-ch04` closure

Durable files:

- translation: `../chapters/v1-ch04.json`
- source notes: `../source-notes/v1-ch04.json`
- T2 review: `../reviews/v1-ch04-t2.md`
- T3 review: `../reviews/v1-ch04-t3.md`
- thought-structure audit: `../reviews/v1-ch04-structure.md`
- final approval review: `../reviews/v1-ch04-approval.md`

Gate results:

- source review: **PASS**;
- fresh T1 translation: **PASS / COMPLETE**;
- T2 source-and-Kalaignar-voice review: **PASS WITH REVISION / COMPLETE**;
- T3 English-only review: **PASS WITH MINOR REVISION / COMPLETE — 10 source-checked revisions**;
- thought structure: **PASS — 20 / 20 major movements preserved**;
- terminology/cultural consistency: **PASS**;
- post-freeze existing-English comparator: **NONE at pinned ref**;
- final approval: **PASS / APPROVED**;
- unresolved source holds: **0**;
- outstanding review items: **0**.

## `v1-ch05` — terminology/cultural audit complete

Durable files:

- source notes: `../source-notes/v1-ch05.json`
- translation: `../chapters/v1-ch05.json`
- T2 review: `../reviews/v1-ch05-t2.md`
- T3 review: `../reviews/v1-ch05-t3.md`
- thought-structure audit: `../reviews/v1-ch05-structure.md`
- terminology/cultural audit: `../reviews/v1-ch05-terminology.md`

Gate state:

- source review: **PASS / COMPLETE**;
- fresh T1 translation: **PASS / COMPLETE**;
- T2 source-and-Kalaignar-voice review: **PASS WITH REVISION / COMPLETE**;
- T3 English-only literary review: **PASS WITH MINOR REVISION / COMPLETE — 15 source-checked revisions**;
- thought structure: **PASS / COMPLETE — 22 / 22 major movements preserved**;
- terminology/cultural consistency: **PASS WITH MINOR REVISION / COMPLETE — 2 revisions**;
- unresolved source holds: **0**;
- outstanding review items: **0**;
- existing-English comparator: **NOT CONSULTED**;
- next gate: **post-freeze comparator availability check**.

The terminology/cultural audit normalises `முனுசாமி நாயுடு` to **Munuswamy Naidu** and keeps **Gandhiji** consistent inside the linked Bose comparison. It confirms the existing period **First Minister / Premier** distinction, Panneerselvam/Khalifullah/Natarajan/Indian National Congress forms, `வடமொழி` → **Sanskrit**, `இறும்பூது` → **wonder**, **Leader of the Tamils**, and the culturally visible Navalar / Arignar / Perarignar / Muthamizh Kaavalar / Ammaiyar / Tamilavel epithets.

The audit deliberately retains collective **The Tamil**, chapter-specific **the pride of race**, and **Tamil chindu** as source-driven historical/cultural language. `இனம்` is not globally frozen; later occurrences remain context-dependent.

## Branch consolidation

PR #1 merged the former working branch `translation/english-memoir` into `main`. `main` is the sole active translation work surface. Future chapter commits and control updates go directly to `main`.

## Opening observations for remaining batch chapters

### `v1-ch06`

The opening source repeats the heading. The chapter is strongly oratorical, with descriptions of Pattukkottai Alagirisami, the Tamil volunteer march, repeated rhetorical images and quoted public speech. Source review must preserve speech cadence rather than flattening the passage into historical summary.

### `v1-ch07`

The opening contains the spacing/extraction form `ஜி ன்னாவிற்கும்` for Jinnah. The chapter begins in all-India political history and later moves into Kalaignar's student activity; source review must track the historical-to-personal pivot and inspect further spacing/name anomalies before T1.

## Current batch gate

- Batch opened: **YES**
- source files pinned: **5 / 5**
- full source reviews complete: **3 / 5** (`v1-ch03`, `v1-ch04`, `v1-ch05`)
- T1 complete: **3 / 5** (`v1-ch03`, `v1-ch04`, `v1-ch05`)
- T2 complete: **3 / 5** (`v1-ch03`, `v1-ch04`, `v1-ch05`)
- T3 complete: **3 / 5** (`v1-ch03`, `v1-ch04`, `v1-ch05`)
- thought-structure complete: **3 / 5** (`v1-ch03`, `v1-ch04`, `v1-ch05`)
- terminology/cultural complete: **3 / 5** (`v1-ch03`, `v1-ch04`, `v1-ch05`)
- approved chapters: **2 / 5** (`v1-ch03`, `v1-ch04`)
- next chapter activity: **post-freeze comparator availability check for `v1-ch05`**
