# Batch 001 — Volume 1 Chapters 3–7

Status: **OPEN / `v1-ch03` APPROVED**

Source repository: `pugazg/kalaignar-autobiography` — **READ ONLY**

Pinned source ref for batch opening: `5c6b5ef8901044660e607d4649238d7c66cb648d`

Write repository: `pugazg/nenjukku-needhi-archive`

Working branch: `translation/english-memoir`

## Batch rule

This five-chapter batch is a management envelope. Process one chapter at a time through its gates; do not bulk-translate all five in one iteration and do not start `v1-ch08` until Batch 001 is closed.

## Chapters

| ID | Tamil title | Pages | Source blob SHA | Current status |
|---|---|---:|---|---|
| `v1-ch03` | `"சிவாய நம! ஓம் நமசிவாய"` | 30–36 | `e7c0d550d68f8b30d9c48a22019e017f7034ff93` | **APPROVED / CLOSED** |
| `v1-ch04` | `என்னுடைய அரசியல் அரிச்சுவடி` | 37–41 | `1b55b986176d330fab4ce16eb70565ddd895ba48` | **NEXT — SOURCE REVIEW** |
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

Gate results:

- source review: **PASS**;
- T1 fresh translation: **PASS**;
- T2 source-and-Kalaignar-voice review: **PASS WITH REVISION**;
- T3 English-only literary review: **PASS WITH MINOR REVISION**;
- thought-structure audit: **PASS — 24 / 24 major movements preserved**;
- terminology/cultural consistency: **PASS**;
- unresolved source holds: **0**;
- outstanding lexical review items: **0**;
- existing-English comparator: **NONE at pinned source ref**;
- final status: **APPROVED / CLOSED**.

Important durable lessons from the chapter include the dated Brahmin-Tamil `நோக்கு` = `உனக்கு` reading; the functional treatment of `அரிநமோத்து சிந்தம்` as an old education-initiation formula without speculative doctrinal translation; preservation of caste hierarchy and political metaphors; and retention of the long `இதோ` / `அதோ` spoken homecoming catalogue.

The repository's `schemas/chapter.json` remains an empty legacy placeholder, so formal JSON-Schema execution is not currently available. Approval records machine-readable structural consistency under the repository's implemented controls rather than claiming a nonexistent schema run.

## Opening observations for remaining batch chapters

### `v1-ch04`

The first extraction unit repeats the heading and immediately begins with the fragment `-ம் ஆண்டு` before the Thiruvarur High School scene. This appears to be a damaged/missing year expression and must be reviewed rather than silently supplied. The chapter also contains extended dialogue and the transition from school admission anecdote to Panagal Raja/Justice Party political education.

### `v1-ch05`

The first extraction unit repeats the heading and begins with `-ல்` before the Justice Party leadership change, indicating a damaged/missing year or preceding token at the start. The chapter carries political chronology and anti-Hindi agitation material where tense, dates and quoted exchanges require source-sensitive handling.

### `v1-ch06`

The opening source repeats the heading. The chapter is strongly oratorical, with descriptions of Pattukkottai Alagirisami, the Tamil volunteer march, repeated rhetorical images and quoted public speech. Source review must preserve speech cadence rather than flattening the passage into historical summary.

### `v1-ch07`

The opening contains the spacing/extraction form `ஜி ன்னாவிற்கும்` for Jinnah. The chapter begins in all-India political history and later moves into Kalaignar's student activity; source review must track the historical-to-personal pivot and inspect further spacing/name anomalies before T1.

## Current batch gate

- Batch opened: **YES**
- source files pinned: **5 / 5**
- full source reviews complete: **1 / 5** (`v1-ch03`)
- T1 complete: **1 / 5** (`v1-ch03`)
- T2 complete: **1 / 5** (`v1-ch03`)
- T3 complete: **1 / 5** (`v1-ch03`)
- thought-structure complete: **1 / 5** (`v1-ch03`)
- approved chapters: **1 / 5** (`v1-ch03`)
- next chapter activity: **complete source review for `v1-ch04`**
