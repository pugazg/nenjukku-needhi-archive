# Batch 001 — Volume 1 Chapters 3–7

Status: **OPEN / `v1-ch04` T2 COMPLETE**

Source repository: `pugazg/kalaignar-autobiography` — **READ ONLY**

Pinned source ref for batch opening: `5c6b5ef8901044660e607d4649238d7c66cb648d`

Latest source-main drift check during `v1-ch04` review: `bb0beaa0a18f97336b52319c1e7b15e62d81d1ed`; `v1-ch04` blob remains byte-identical at `1b55b986176d330fab4ce16eb70565ddd895ba48`, so Batch 001 authority remains the opening pin.

Write repository: `pugazg/nenjukku-needhi-archive`

Working branch: `main`

## Batch rule

This five-chapter batch is a management envelope. Process one chapter at a time through its gates; do not bulk-translate all five in one iteration and do not start `v1-ch08` until Batch 001 is closed.

## Chapters

| ID | Tamil title | Pages | Source blob SHA | Current status |
|---|---|---:|---|---|
| `v1-ch03` | `"சிவாய நம! ஓம் நமசிவாய"` | 30–36 | `e7c0d550d68f8b30d9c48a22019e017f7034ff93` | **APPROVED / CLOSED** |
| `v1-ch04` | `என்னுடைய அரசியல் அரிச்சுவடி` | 37–41 | `1b55b986176d330fab4ce16eb70565ddd895ba48` | **T2 COMPLETE / T3 NEXT** |
| `v1-ch05` | `நீதிக் கட்சியில் பல மாற்றங்கள்` | 42–45 | `220fb5271eac48c6988057d0d464d5950fd822a3` | queued for source review |
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

## `v1-ch04` durable state

Source notes: `../source-notes/v1-ch04.json`

Fresh T1/T2 translation: `../chapters/v1-ch04.json`

T2 review: `../reviews/v1-ch04-t2.md`

Gate results:

- source review: **PASS**;
- fresh T1 translation: **PASS / COMPLETE**;
- T2 source-and-Kalaignar-voice review: **PASS WITH REVISION / COMPLETE**;
- unresolved source holds: **0**;
- outstanding T2 review items: **0**;
- next gate: **T3 English-only review**.

T2 controls enforced:

- `தென்னிந்திய நல உரிமைச் சங்கம்` is normalised to the historically attested English proper name **South Indian Liberal Federation (SILF)**, with the intervention documented;
- `முதல் மந்திரி` remains the period title **First Minister**, not modernised to Chief Minister;
- `சட்டசபைத் தலைவர்` is rendered as **President of the Legislative Council**, matching the 1920s Madras Presidency institution rather than the modern Legislative Assembly;
- Justice Party, Self-Respect Movement, rationalism, backward communities and depressed communities/people are frozen as context-sensitive historical working forms;
- `திராவிடப் பெருங்குடி` remains **great Dravidian community**, preserving Kalaignar's collective imagery rather than replacing it with a bureaucratic non-Brahmin label;
- `விடிவெள்ளி` is corrected from the redundant `morning star of dawn` to **morning star for the Dravidians**;
- `சொற்போர்` retains oral/debate energy as **verbal debates**;
- the `அரிச்சுவடி` → political-primer architecture remains intact;
- historical assertions remain authored claims and are not silently fact-corrected.

## Branch consolidation

PR #1 merged the former working branch `translation/english-memoir` into `main`. `main` is now the sole active translation work surface. Future chapter commits and control updates go directly to `main`.

## Opening observations for remaining batch chapters

### `v1-ch05`

The first extraction unit repeats the heading and begins with `-ல்` before the Justice Party leadership change, indicating damaged/missing leading text. The chapter carries political chronology and anti-Hindi agitation material where tense, dates and quoted exchanges require source-sensitive handling.

### `v1-ch06`

The opening source repeats the heading. The chapter is strongly oratorical, with descriptions of Pattukkottai Alagirisami, the Tamil volunteer march, repeated rhetorical images and quoted public speech. Source review must preserve speech cadence rather than flattening the passage into historical summary.

### `v1-ch07`

The opening contains the spacing/extraction form `ஜி ன்னாவிற்கும்` for Jinnah. The chapter begins in all-India political history and later moves into Kalaignar's student activity; source review must track the historical-to-personal pivot and inspect further spacing/name anomalies before T1.

## Current batch gate

- Batch opened: **YES**
- source files pinned: **5 / 5**
- full source reviews complete: **2 / 5** (`v1-ch03`, `v1-ch04`)
- T1 complete: **2 / 5** (`v1-ch03`, `v1-ch04`)
- T2 complete: **2 / 5** (`v1-ch03`, `v1-ch04`)
- T3 complete: **1 / 5** (`v1-ch03`)
- thought-structure complete: **1 / 5** (`v1-ch03`)
- approved chapters: **1 / 5** (`v1-ch03`)
- next chapter activity: **T3 English-only review for `v1-ch04`**
