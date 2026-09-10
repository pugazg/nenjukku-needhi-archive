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
- Kalaignar Voice Guide: **LIVING / UPDATED THROUGH `v1-ch03`**
- Translation glossary: **LIVING / UPDATED THROUGH `v1-ch03`**
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
| `v1-ch04` | `என்னுடைய அரசியல் அரிச்சுவடி` | 37–41 | **T1 COMPLETE / T2 NEXT** |
| `v1-ch05` | `நீதிக் கட்சியில் பல மாற்றங்கள்` | 42–45 | not started |
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

## `v1-ch04` — fresh T1 complete

Durable files:

- translation: `data/books/nenjukku-needhi/translations/en/chapters/v1-ch04.json`
- source notes: `data/books/nenjukku-needhi/translations/en/source-notes/v1-ch04.json`

Gate state:

- source review: **PASS**;
- T1: **PASS / COMPLETE**;
- unresolved source holds: **0**;
- T2 review items remaining: **2** — movement terminology/register; historical-office vocabulary;
- next gate: **T2 source-and-Kalaignar-voice review**.

T1 decisions enforced:

- The damaged opening `-ம் ஆண்டு` is reconstructed as **1936** only through the already documented contextual evidence; the digital source is not represented as containing the missing numerals.
- The school-admission scene remains in third-person dramatic present until the delayed `நானே தான்!` reveal.
- `கர்ஸ்தூரி ஐயங்கார்` is rendered as `Kasthuri Iyengar`, with source spelling and the normalisation decision documented.
- Headmaster Iyengar's recurring dated Brahmin-Tamil `நோக்கு` is translated by function rather than as `look`.
- `punkah` and `peon` preserve the colonial-period school scene.
- The boy's missing opening quotation is reconstructed as continuing direct speech.
- `விழுத்து`, `சுட்சியின்`, `சட்டசயைத்` and the interrupted `அந்த ஆண்டு. அந்தப் பையன்` sequence are translated by context and remain disclosed.
- `அரிச்சுவடி` is retained as **primer** in both title and body; the Panagal Raja schoolbook is the autobiographical trigger for the Justice Party history that follows.
- The historical section preserves Kalaignar's rhetorical images rather than flattening them: removing fetters, Thiagarayar as the Dravidians' dawn-star entering unending sleep in nature's lap, the country shedding tears over the Raja of Panagal, the Justice Party left shaken, and the flame of rationalism carried by `Kudi Arasu`.
- Dense historical claims are translated as Kalaignar presents them; T1 does not silently fact-correct them.

## Batch 001 counters

- source files pinned: **5 / 5**
- full source reviews complete: **2 / 5**
- T1 complete: **2 / 5**
- T2 complete: **1 / 5**
- T3 complete: **1 / 5**
- thought-structure complete: **1 / 5**
- approved: **1 / 5**

## Infrastructure note

`schemas/chapter.json` is currently an empty one-byte legacy placeholder, so formal JSON-Schema execution is not available under current repository controls.

## Branch consolidation

The former working branch `translation/english-memoir` was merged into `main` via PR #1. All further translation work is performed directly on `main`; the old branch is not an active work surface.

## Next activity

Run the complete T2 Tamil-English source-and-Kalaignar-voice review for `v1-ch04`. Special focus: the `அரிச்சுவடி`/primer metaphor, third-person admission drama, movement terminology (`நீதிக் கட்சி`, `சுயமரியாதை`, `பகுத்தறிவு`, `திராவிடப் பெருங்குடி`, `தாழ்த்தப்பட்ட`), historical-office vocabulary, and whether the dense political chronology has become more encyclopedic or smoother than Kalaignar's own rhetorical sequence.
