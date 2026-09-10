# v1-ch04 — Final Approval Review

Status: **COMPLETE / APPROVED**

Chapter: `../chapters/v1-ch04.json`

Source notes: `../source-notes/v1-ch04.json`

T2: `v1-ch04-t2.md`

T3: `v1-ch04-t3.md`

Thought structure: `v1-ch04-structure.md`

## Gate summary

- source review: **PASS**;
- T1 fresh Tamil translation: **PASS**;
- T2 Kalaignar-voice review: **PASS WITH REVISION**;
- T3 English-only literary review: **PASS WITH MINOR REVISION — 10 source-checked revisions**;
- thought-structure audit: **PASS — 20 / 20 major movements preserved**;
- unresolved source holds: **0**;
- outstanding lexical review items: **0**;
- non-authorial exclusions required: **0**;
- independent English frozen after T3: **YES**;
- existing-English comparator at pinned source ref: **NONE** (`public/data/text-en/v1-ch04.json` is absent);
- terminology/cultural-language consistency: **PASS**.

## Terminology / cultural consistency

The final chapter follows the living glossary and Voice Guide principles:

- `அரிச்சுவடி` remains **primer**, preserving the chapter's central movement from schoolbook to political education;
- `தென்னிந்திய நல உரிமைச் சங்கம்` is rendered by the historically attested proper name **South Indian Liberal Federation** and the intervention is disclosed;
- `நீதிக் கட்சி` / `ஜஸ்டிஸ் கட்சி` remains **Justice Party**;
- `முதல் மந்திரி` remains the period title **First Minister**, not modernised to Chief Minister;
- `சட்டசபைத் தலைவர்` is rendered as **President of the Legislative Council** for the 1920s Madras Presidency context;
- `இந்தியா மந்திரி` in the Montagu passage is rendered by the attested official English title **Secretary of State for India**, rather than literal `India Minister`; this is documented as institutional normalisation;
- `சுயமரியாதை இயக்கம்` remains **Self-Respect Movement** and `பகுத்தறிவு` remains **rationalism**;
- `தாழ்த்தப்பட்ட` / `பின்னடைந்த` social vocabulary retains the historical register as **depressed** / **backward** communities according to context;
- `திராவிடப் பெருங்குடி` remains **great Dravidian community**, preserving Kalaignar's collective image rather than replacing it with a modern bureaucratic category;
- `விடிவெள்ளி`, `இயற்கையின் மடியில் நீங்காத் துயில்`, `நாடு கண்ணீர் வடித்தது`, `பகுத்தறிவுச் சுடர்`, and `சூறாவளி வேகத்தில்` remain concrete metaphors rather than being neutralised;
- `சொற்போர்` remains **verbal debates**, retaining contest/oratorical force.

## T3 integrity check

T3 made ten limited revisions. The most important fidelity correction removed the translator-added hedge `in their view` from the Home Rule comparison; Kalaignar's Tamil makes that political assertion directly. `schemes` was also replaced by neutral `plans` for `திட்டங்கள்`.

Other T3 changes naturalised English without changing content: the peon's failed attempt to stop the boy, Kamalalayam swirling through the headmaster's mind, `top marks`, party-formation syntax, newspaper-name syntax, Panagal Raja's `tenure`, and the Justice Party `stood shaken` formulation.

No chronology, named person, political claim, rhetorical turn or metaphor was added or removed by T3.

## Thought-structure result

The 20-movement structure passes intact:

`school authority breached → descending-exam predicament → suicide threat → Kamalalayam danger → victory → delayed 'It was I myself!' reveal → Panagal Raja book → political primer → Justice Party formation/press → representation argument → Nair/elections → ministry → Panagal administration loops back to primer → labour confrontation → elections/leadership deaths → party shaken → Periyar/Self-Respect → organiser network → Anna as student speaker → Periyar–Justice Party convergence`.

The long historical passage therefore remains autobiographical in function rather than becoming an inserted encyclopedia article.

## Source / comparator controls

- controlling Tamil remains the pinned read-only source blob `1b55b986176d330fab4ce16eb70565ddd895ba48`;
- latest observed source-main drift remained byte-identical for this chapter;
- the damaged opening year reconstruction `1936` remains explicitly disclosed rather than silently attributed to surviving source pixels/text;
- no pre-existing English `v1-ch04` exists at the pinned source ref, so no post-freeze wording was adopted from an earlier translation.

## Machine-readable record check

The chapter remains stored in the same structured JSON form used by the approved pilot/production translations, with:

- unique id `v1-ch04`;
- language `en`;
- volume `1`;
- Tamil and English titles;
- page range `37–41`;
- pinned read-only source provenance;
- source-note linkage;
- translation notes;
- ordered paragraph array;
- T2/T3/structure/approval provenance links.

Formal repository JSON-Schema validation cannot currently be claimed because `schemas/chapter.json` remains an empty one-byte legacy placeholder. This is a repository-infrastructure limitation, not a chapter-content failure. Approval records machine-readable structural consistency under the controls actually implemented in the repository.

## Final decision

`v1-ch04` — **APPROVED / CLOSED**.

There are no unresolved meaning-affecting source issues and no remaining translation-review items.

Next production activity: begin the complete source review for `v1-ch05` (`நீதிக் கட்சியில் பல மாற்றங்கள்`, pp. 42–45) before any T1 translation. Its damaged opening `-ல்` must be treated as source evidence requiring review rather than silently reconstructed.
