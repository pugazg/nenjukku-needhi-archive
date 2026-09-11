# Nenjukku Needhi English Translation — HANDOVER

## LIVE MAIN IS AUTHORITATIVE

Continue in:

- writable repository: `pugazg/nenjukku-needhi-archive`
- branch: `main`

The source repository is strictly **READ ONLY**:

- `pugazg/kalaignar-autobiography`
- source path: `public/data/text/*.json`

Never create commits, branches, PRs, issues, metadata changes, or generated files in the source repository.

Fetch live `main` before doing any work and preserve newer durable work if the repository has advanced.

Last verified substantive work-state commit before these handover-only files:

`4f079480b2a944ee90d409b1c1400d4420ac8e5a`

## Source pin

Batch 001 source pin:

`5c6b5ef8901044660e607d4649238d7c66cb648d`

Latest observed source `main`:

`d6621b71256ae99b1c89b4f2091513dcc5f96626`

For `v1-ch07`, pinned/live source blob is byte-identical:

`13b1f1d06abeb762ed5f016818fa282b78ba7593`

## Translation philosophy

Core rule:

> We are not translating an autobiography about Kalaignar. We are translating Kalaignar telling his own story.

Preserve, in order:

1. factual fidelity;
2. intellectual/reasoning fidelity;
3. rhetorical fidelity;
4. voice;
5. natural English only after the above.

The Tamil JSON paragraph is an extraction/page unit, not automatically an authorial paragraph.

Never silently normalize source anomalies. Record page joins, OCR/spacing anomalies, non-authorial text, uncertain readings, quotations, verse, paragraph reconstruction, chronology tensions and other interventions in the chapter source notes.

Existing English is **never drafting authority**. It may only be checked after the independent English is frozen.

## Production workflow for one chapter

`P0 source review → T1 fresh translation → T2 Tamil-English/Kalaignar voice → T3 English-only literary review → thought-structure audit → terminology/cultural audit → post-freeze comparator check → final approval → closed`

Do not combine later gates merely to move faster unless explicitly authorized.

## Batch 001

Batch control:

`data/books/nenjukku-needhi/translations/en/batches/batch-001.md`

Chapters:

- `v1-ch03` — APPROVED / CLOSED
- `v1-ch04` — APPROVED / CLOSED
- `v1-ch05` — APPROVED / CLOSED
- `v1-ch06` — APPROVED / CLOSED
- `v1-ch07` — **T2 COMPLETE / T3 NEXT**

Current Batch 001 counters:

- source reviews: **5 / 5**
- T1: **5 / 5**
- T2: **5 / 5**
- T3: **4 / 5**
- thought structure: **4 / 5**
- terminology/cultural: **4 / 5**
- comparator checks: **4 / 5**
- approved chapters: **4 / 5**

Do **not** start `v1-ch08` until `v1-ch07` is fully approved/closed and Batch 001 is closed.

## Active chapter — v1-ch07

Tamil title:

`"நீங்களா 'மாணவ நேசன்' நடத்துகிறீர்கள்?"`

Working English title:

**Are You the One Who Runs 'Maanava Nesan'?**

Pages:

**51–55**

Pinned source:

- path: `public/data/text/v1-ch07.json`
- blob: `13b1f1d06abeb762ed5f016818fa282b78ba7593`

Durable files:

- source notes: `data/books/nenjukku-needhi/translations/en/source-notes/v1-ch07.json`
- translation: `data/books/nenjukku-needhi/translations/en/chapters/v1-ch07.json`
- T2 review: `data/books/nenjukku-needhi/translations/en/reviews/v1-ch07-t2.md`

Current gate state:

- P0 source review: **PASS / COMPLETE**
- T1 fresh translation: **PASS / COMPLETE**
- T2 source-and-Kalaignar-voice review: **PASS WITH REVISION / COMPLETE**
- T3: **NEXT**
- unresolved source holds: **0**
- blocking T2 issues: **0**
- existing-English comparator consulted: **NO**

## v1-ch07 P0 controls

The source review records and protects:

- repeated heading excluded from duplicate body prose;
- page-51 visual/extraction split `ஜி / ன்னா` reconstructed as Jinnah;
- anomalous `முஸ்லீம் வீக்கிற்கும்` translated only by secure contextual function as Muslim League;
- valid archaic `முடங்கல்` treated as letter/written communication;
- source sequence `அழகிரி சிற்றரசு` treated contextually as separate Alagiri and Chittarasu names;
- page-53/54 `செய்து கொண்- / டிருந்தது` joined across the page boundary;
- stray extraction backtick in the newspaper quotation ignored;
- `பள்ளிக்கூடத்திலிருத்த` translated only by secure schoolboy-meeting context;
- Gandhi–Jinnah dialogue preserved as direct speech;
- `Maanava Nesan` preserved as a visible handwritten publication;
- Bharathidasan spinning-wheel sarcasm preserved;
- `சிறுதுளி பெருவெள்ளம்` preserved as a compact proverb/image;
- `பொங்கல் மலர்` treated as a Pongal special issue, not a literal flower;
- demy-paper costs and the `labour and articles were free` joke preserved;
- practical copying burden preserved as the immediate narrative origin of `Murasoli`;
- `Murasoli` begins here as leaflet issues, not a weekly/monthly;
- Students' Federation remains generic; no unsupported expansion to AISF;
- delayed Communist reveal preserved;
- `Freedom – Peace – Equality` triad preserved;
- closing Federation-current / unknown-depth imagery preserved.

## Authored chronology tensions — DO NOT CORRECT

1. The memoir says in **1939** M. N. Roy started `புரட்சி ஜனநாயகக் கட்சி`. T2 normalizes the historical entity name to **Radical Democratic Party**, but the memoir's **1939** date must remain unchanged.

2. Kalaignar describes himself as a thin **15-year-old** when the khadi-shirted organizer met him, and then says the meeting was four months before `Murasoli` began. External institutional chronology places `Murasoli`'s first issue on 10 August 1942, when Karunanidhi was eighteen. Preserve the memoir's wording; do not silently reconcile it.

## v1-ch07 T2 decisions already applied

T2 is complete and durable. Important applied decisions include:

- working title retained: **Are You the One Who Runs 'Maanava Nesan'?**
- `Maanava Nesan` retained as the working romanized publication title;
- **Indian National Congress** used for the historical entity;
- **Radical Democratic Party** used for M. N. Roy's party, while preserving Kalaignar's 1939 date;
- Gandhi–Jinnah direct dialogue retained;
- `Janab Jinnah`, `Gandhiji`, source-led honorific variation retained;
- Subhas at Tripuri: **stood for the presidency again**;
- Nehru **tried to dissuade him**;
- Rajendra Prasad sentence resolved conservatively as a Gandhi-favoured figure elected Congress president;
- British wartime-crisis sentence made natural without changing the argument;
- linked Congress Working Committee reference normalized consistently;
- `கவிக்குயில் சரோஜினி தேவி` retained as **the poet-songbird Sarojini Devi**;
- visitor's question has no added `really`;
- Bharathidasan's spinning-wheel sentence rebalanced to preserve repeated madness;
- **handwritten journal** used for the publication form, **copy/copies** for physical exemplars;
- **Little drops make a great flood** retained;
- **Pongal special issue** retained;
- **demy paper** retained;
- **The labour and the articles were free!** retained;
- `Murasoli` birth as **leaflet issues** retained;
- `பாசறை` rendered as **organizing camp** in the recruiter speech;
- Students' Federation kept generic;
- Congress students believed it **Congress-affiliated**;
- `பொதுமாணவர்கள்` clarified as unaffiliated students belonging to no party;
- closing wording now uses **The current of the Federation seemed ready to sweep us along with it**, preserving the linked water image.

## Living controls

Read and obey before continuing:

1. `docs/TRANSLATION_PLAN.md`
2. `docs/PILOT_METHOD_REVIEW.md`
3. `docs/KALAIGNAR_VOICE_GUIDE.md`
4. `docs/TRANSLATION_GLOSSARY.md`
5. `docs/TRANSLATION_PROGRESS.md`
6. `data/books/nenjukku-needhi/translations/en/batches/batch-001.md`
7. `data/books/nenjukku-needhi/translations/en/source-notes/v1-ch07.json`
8. `data/books/nenjukku-needhi/translations/en/chapters/v1-ch07.json`
9. `data/books/nenjukku-needhi/translations/en/reviews/v1-ch07-t2.md`

Voice Guide and glossary are updated through **v1-ch07 T2**.

## Immediate next activity — v1-ch07 T3

Perform **T3 English-only literary review**.

Method:

1. Read the revised English chapter as English first, without using Tamil to generate edits.
2. Identify only genuine literary/syntactic/cadence problems.
3. Recheck every proposed change against the pinned Tamil before accepting it.
4. Do not make changes merely because a smoother English sentence is possible.
5. Do not consult any existing-English comparator.
6. Record accepted/rejected decisions in:
   `data/books/nenjukku-needhi/translations/en/reviews/v1-ch07-t3.md`
7. Apply accepted source-checked T3 changes to:
   `data/books/nenjukku-needhi/translations/en/chapters/v1-ch07.json`
8. Update source notes, Batch 001, progress and manifest.
9. Stop with **thought-structure audit next**.

T3 must especially protect:

- macro-history → thin schoolboy scale shift;
- direct Gandhi–Jinnah and other quoted speech;
- authored chronology tensions;
- Subhas/Gandhi/Nehru political friction without textbook rewriting;
- Bharathidasan's sarcasm;
- material publishing details and humour;
- the causal chain `Maanava Nesan` copying burden → `Murasoli`;
- delayed Communist reveal;
- Freedom – Peace – Equality;
- final current / unknown-depth imagery.

## After T3

Remaining gates for `v1-ch07`:

1. thought-structure audit;
2. terminology/cultural-consistency audit;
3. post-freeze existing-English comparator availability check;
4. final approval review;
5. approve/close `v1-ch07`;
6. close Batch 001;
7. only then begin the next production batch.

## Infrastructure limitation

`schemas/chapter.json` is an empty one-byte legacy placeholder.

Do not claim formal JSON-Schema validation. Only claim syntactic JSON parseability and structural consistency under implemented repository controls.
