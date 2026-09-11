# Nenjukku Needhi — English Translation Plan

## Authority boundary

- Source repository: `pugazg/kalaignar-autobiography`
- Source path: `public/data/text/*.json`
- Source repository is **READ ONLY** for this project. No commits, branches, edits, pull requests, issue changes, generated files, or metadata changes may be made there.
- Initial pinned source `main`: `5c6b5ef8901044660e607d4649238d7c66cb648d`.
- Write repository: `pugazg/nenjukku-needhi-archive` only.

The source pin records the starting corpus state. Before each production batch, live source metadata may be read again and any drift must be recorded in the archive; source changes must never be written back by this project.

## Governing translation principle

**We are not translating an autobiography about Kalaignar. We are translating Kalaignar telling his own story.**

The translation must preserve not only information but what Kalaignar's sentence is doing: argument, cadence, humour, affection, irony, political force, dramatic pacing, repetition, analogy, direct reader-address, and the movement between personal memory and public history.

### Four fidelity levels

1. **Factual fidelity** — retain every person, event, date, claim, image, quotation and narrative action present in the authorial Tamil.
2. **Intellectual fidelity** — preserve Kalaignar's route to a conclusion. Do not compress a chain of examples or reasoning merely because English could say it more briefly.
3. **Rhetorical fidelity** — questions remain questions; deliberate repetition remains repetition; accumulative lists keep their build; punchlines remain punchlines; contrasts and reversals remain visible.
4. **Voice fidelity** — the English should read like an accomplished political writer, dramatist and public speaker narrating his own life, not like an academic summary or a neutralised paraphrase.

Natural English matters, but never at the cost of these four levels.

## What the Tamil pilots reveal about Kalaignar's prose

The method is derived from direct reading and full pilot processing of `v1-ch01` (`பிறந்த ஆண்டு`) and `v1-ch02` (`தந்தையின் துணிவு`), not from copying any existing English benchmark.

Recurring characteristics to preserve:

- personal memory expands into social, Tamil, Indian and world history, then often returns to the personal;
- rhetorical questions frequently function as arguments or verdicts;
- repetition and parallel constructions build momentum;
- concrete scenes and analogies carry abstract political or philosophical thought;
- prose often has an oral/public-speaking quality and addresses the reader directly;
- humour can arrive immediately after grief, danger or political seriousness and must not be explained away;
- self-reference can combine pride, irony and self-mockery;
- affectionate and political epithets are part of the emotional language, not disposable metadata;
- embedded songs, proverbs, Tirukkural, quotations and sayings participate in the argument;
- apparent personal, cultural, religious or political tensions should be preserved rather than simplified into a cleaner ideological portrait.

See `docs/PILOT_METHOD_REVIEW.md` and `docs/KALAIGNAR_VOICE_GUIDE.md` for durable lessons from both pilots.

## Source-text problem: extraction units are not authorial paragraphs

`public/data/text/*.json` contains extracted digital text. Its `paragraphs` array is **not assumed to represent Kalaignar's authorial paragraphing**.

Known examples from the pilots:

- words can be split across source elements/page joins, e.g. `கேட்க-` followed by `லாம்` in `v1-ch02`;
- sentences can cross JSON element boundaries;
- chapter titles can be repeated at the beginning of the first source element;
- OCR/spacing artefacts can occur;
- contextual extraction anomalies can survive into more than one text witness;
- non-authorial Wikisource maintenance notices can appear inside the `paragraphs` array — `v1-ch02` contains two such duplicate-page/editorial notices.

Therefore:

> **Tamil JSON paragraph = source extraction unit, not necessarily an authorial paragraph.**

The translation pipeline must reconstruct readable literary units from the source while preserving traceability to the extraction units.

## Mandatory source notes

Every translated chapter must carry explicit source notes. Cleaning must never be silent.

Record, where applicable:

- `title_repeat` — chapter heading repeated inside body and treated as metadata rather than prose;
- `page_join` / `source_unit_join` — a word or sentence crosses source elements and has been joined for translation;
- `ocr_spacing` — an evident spacing/character artefact has been interpreted;
- `ocr_or_extraction_reading` — an extracted form is defective or anomalous and context is used to determine its function;
- `non_authorial_editorial` — Wikisource/editorial/interface material excluded from the literary translation;
- `duplicate_source` — duplicated source text/page material;
- `textual_reading_hold` — the source characters/words themselves are not secure;
- `semantic_interpretation_hold` — the visible wording is stable but its exact semantic/syntactic force remains uncertain;
- `accepted_scholarly_uncertainty` — after reasonable review, an unresolved semantic interpretation is intentionally preserved transparently through conservative wording/transliteration and a documented editorial closure decision;
- `verse_or_song` — embedded verse requires verse-aware translation;
- `quotation` — quoted material whose wording/attribution needs special handling;
- `paragraph_reconstruction` — English literary paragraphing differs from extraction-unit boundaries;
- any other source intervention that could affect scholarly traceability.

A note must identify what was observed and what action was taken. Source problems are documented only in `pugazg/nenjukku-needhi-archive`; they are never corrected in the source repository by this project.

### Accepted scholarly uncertainty

Accepted scholarly uncertainty is not a shortcut around a source hold. It may be used only when:

1. reasonable source/lexical review has been attempted;
2. the visible source wording is stable enough to preserve;
3. a confident English interpretation would require invention;
4. the final conservative treatment is visible in the translation and explained in source notes;
5. a dedicated editorial decision records why the uncertainty is accepted and how future stronger evidence may reopen it.

Once those conditions are satisfied, the item is no longer counted as an unresolved source hold. It remains permanently visible as an accepted uncertainty in the archival apparatus.

## Translation workflow

### P0 — Corpus inventory and source hygiene

For all source chapter JSON files, record:

- source path and blob SHA;
- chapter ID, volume, Tamil title and page range;
- extraction-unit count;
- detected source anomalies;
- readiness/hold state.

Automatic detection may flag likely anomalies, but exclusions or reconstructions must be reviewed in context.

### P1 — Kalaignar Voice Guide

Maintain `docs/KALAIGNAR_VOICE_GUIDE.md` as a living, evidence-based style guide derived from Tamil chapters. It records translation decisions about rhetoric, political vocabulary, kinship/honorific language, humour, oral cadence, metaphor, verse, quotation and culturally loaded terms.

### P2 — T1 meaning translation

Translate directly from Tamil. Account for all authorial content. Preserve chronology, speakers, references, historical assertions and quoted material. Do not consult an existing English translation as the drafting authority.

### P3 — T2 Kalaignar-voice pass

Compare Tamil and English and ask:

- Did an argument get shortened?
- Did a question become a statement?
- Did repetition disappear?
- Did humour turn into explanation?
- Did affection become bureaucratic formality?
- Did anger or political force become neutral?
- Did a concrete image become abstraction?
- Did spoken/oratorical prose become academic English?
- Did an unfamiliar cultural term acquire an English meaning not established by evidence?

Revise to restore the author's rhetorical action.

### P4 — T3 independent English read

Read the English without using the Tamil as a crutch. It must function as English prose. Any fluency change must then be checked against the Tamil before acceptance. Do not smooth away a documented source uncertainty merely to make the English look finished.

### P5 — Thought-structure audit

Record the chapter's narrative/argument architecture at a high level and verify that the English follows the same intellectual journey. This is a structural fidelity check, not a summary substituted for translation.

### P6 — Terminology and cultural-language audit

Apply the living glossary consistently. Do not flatten culturally or politically meaningful Tamil vocabulary merely for convenience. Decide case by case whether to translate, transliterate, gloss on first occurrence, or preserve an established political epithet.

### Existing-English policy

The source repository's `public/data/text-en/` directory contains only `v1-ch01.json` at the Batch 002 source pin. Therefore existing-English comparison is **not a recurring production gate** for `v1-ch02` onward.

The historical `v1-ch01` comparator review remains part of the archive as provenance. Do not create per-chapter comparator-absence checks or search unofficial English versions merely to satisfy a workflow gate.

### P7 — Chapter approval

A chapter can be marked `approved` only when:

- all authorial Tamil is represented;
- all exclusions/reconstructions are documented in source notes;
- no unresolved source hold remains;
- any accepted scholarly uncertainty has a dedicated editorial closure record;
- T1, T2, T3 and thought-structure checks pass;
- terminology is consistent;
- JSON/schema validation passes.

## Poetry, songs and quotations

Embedded verse is not to be flattened into prose. Preserve lineation where recoverable, imagery, satire, address and rhetorical force. Rhyme is secondary to meaning and tone.

When Kalaignar quotes or renders another figure, translate the formulation present in Kalaignar's Tamil rather than silently replacing it with a modern canonical English quotation. External wording may be noted separately if useful, but it must not overwrite Kalaignar's framing.

Compressed, dialectal, archaic or semantically uncertain verse must not be forced into confident explanatory English. Conservative wording or transliteration with explicit notes is preferable to invention.

## Historical/factual assertions

Translation is not fact correction.

- If Kalaignar makes a historically contestable assertion, translate it faithfully.
- If the digital source appears corrupt, create a source note/hold.
- If an expression is unusual but intelligible, do not modernise it merely because a smoother alternative exists.

## Output layout

Primary translation layer:

```text
data/books/nenjukku-needhi/translations/en/
├── chapters/
│   ├── v1-ch01.json
│   ├── v1-ch02.json
│   └── ...
├── source-notes/
│   ├── v1-ch01.json
│   ├── v1-ch02.json
│   └── ...
├── reviews/
│   └── ...
├── alignment/
│   └── ...
└── manifest.json
```

Project controls:

```text
docs/
├── TRANSLATION_PLAN.md
├── PILOT_METHOD_REVIEW.md
├── KALAIGNAR_VOICE_GUIDE.md
├── TRANSLATION_GLOSSARY.md
└── TRANSLATION_PROGRESS.md
```

## Production strategy

Pilot phase:

1. `v1-ch01` — philosophy, politics, history, rhetoric and the self-to-world-to-self movement — **APPROVED / CLOSED**.
2. `v1-ch02` — family history, village culture, satire, grief, embedded song, religion, labour and humour — **APPROVED / CLOSED WITH 2 DOCUMENTED ACCEPTED SCHOLARLY UNCERTAINTIES**.

The pilot phase is complete.

Normal production batch size is **5 chapters**, reduced to 1–3 for unusually long or difficult chapters.

A five-chapter batch is a **management envelope**, not a requirement to translate all five chapters in one giant iteration. Within a batch:

- process one chapter at a time;
- complete source review and source notes before T1 for that chapter;
- make durable, reviewable commits as gates complete;
- finish the chapter's required gates before moving materially into the next chapter;
- do not start a sixth chapter until the current five-chapter batch is closed;
- record any reduction in batch size and its reason.

Batch 001 is `v1-ch03`–`v1-ch07`.

## Final corpus gate

Before release, verify:

- 391 expected source chapters accounted for;
- 391 English chapter records, unless a source hold is explicitly documented;
- no duplicate chapter IDs;
- titles translated;
- all authorial source content represented through translation/alignment;
- all source interventions documented;
- no unresolved meaning-affecting holds;
- all accepted scholarly uncertainties explicitly inventoried;
- terminology consistency across all six volumes;
- valid machine-readable manifests and chapter JSON.
