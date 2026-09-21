# Kitchen batch 1 — change and validation report

## Deliverables and source-of-truth limitation

The repository supplied two authoritative masters: `VastuKnowledge_Master.csv` and `VastuVocabulary_Master.csv`. Their complete, append-only derivatives are `1_VastuKnowledge_Master.csv` and `1_VastuVocabulary_Master.csv` in this directory. The repository contains no backend source, validator, language registry, pending-batch files, or `VastuChatFlows_Master.csv` in the working tree or Git history. Consequently, no ChatFlows file was fabricated: its exact header, schema, flow IDs, and action contracts cannot be established from the available source of truth. No flow change is required by the new topic rows.

## Ten distinct draft topics added

1. `kitchen_house_location` — kitchen location within the house.
2. `kitchen_cooking_platform` — cooking platform/stove position and the cook's facing direction.
3. `kitchen_sink_stove_relationship` — sink-to-stove arrangement.
4. `kitchen_window_ventilation` — windows and ventilation openings.
5. `kitchen_drainage_planning` — floor and sink drainage planning.
6. `kitchen_overhead_tank` — overhead tank above the kitchen.
7. `kitchen_underground_tank` — underground tank beneath the kitchen.
8. `kitchen_bedroom_above` — bedroom/cooking-zone vertical alignment.
9. `kitchen_bathroom_above` — bathroom/toilet above the kitchen.
10. `kitchen_exhaust_outlet` — chimney/hood duct and outlet planning.

The five existing concepts and their 115 vocabulary rows are unchanged. The ten additions do not duplicate the existing toilet-door alignment, open-plan kitchen, under-stair kitchen, kitchen mandir, or kitchen-entrance concepts. The new batch also keeps room location, facing direction, adjacency, and vertical relationships separate. No rows or IDs were deleted or altered.

## Counts and coverage

| Collection | Original | Added | Output total | Changed | Unchanged |
|---|---:|---:|---:|---:|---:|
| VastuKnowledge | 5 | 10 | 15 | 0 | 5 |
| VastuVocabulary | 115 | 230 | 345 | 0 | 115 |

Each new topic has one English vocabulary row plus inactive rows for all 22 other registry codes evidenced by the existing masters: `en`, `kn`, `hi`, `ta`, `te`, `ml`, `bn`, `mr`, `gu`, `ur`, `pa`, `or`, `as`, `mai`, `sat`, `ks`, `ne`, `sd`, `doi`, `kok`, `mni`, `brx`, and `sa`.

New English content is present for 10/10 topics. The other 220 new language-topic entries are deliberately empty, `isActive=false`, and represented as `translationStatus=missing` in Knowledge. No English placeholders were put into those languages. The requested translations therefore remain an explicit release gap. Native-speaker review, editorial review, and identifiable-source review also remain pending. All new collection rows use `DRAFT`; existing publication states are preserved.

## Remedies and behavior represented

Each topic currently has two distinct, situation-specific draft suggestions (20 total), with stable IDs, ordered steps, limitations, and corresponding English content. This count follows the guidance available in the authored draft and is not a runtime quota. The standard existing display contract is retained (`remediesPerReply=1`, `allRemediesPreviewCount=3`), and default remedy IDs preserve the declared order. No cross-row remedies were asserted without backend validation.

## Validation performed

`validate_batch.py` parses both source and output CSVs, parses all JSON-bearing fields, checks exact headers, append-only preservation, counts, unique collection IDs/topic IDs, the 23-code language set, 23 vocabulary rows per new topic, inactive missing-language rows, topic references, remedy IDs and language links, default-remedy ordering, and duplicate normalized aliases within and against the existing master. It also simulates exact alias lookup, ordered remedy navigation through the final item, missing-language fallback, and unknown-question no-match behavior from the declared records.

Backend schema validators and engine tests could not be run because no backend or tests are present. Live Wix/Android behavior was not tested. These draft files must not be described as publication-ready until the missing translations, reviews, source review, and unavailable backend validation are completed.

## Import guidance

Do not import these files into production yet. After the pending work and backend validation, use the numbered complete masters as replacement/import sources according to the CMS's documented upsert process, keyed by the existing collection `ID` (and checked by `topicId`/`conceptId`). Do not append the complete file blindly to a populated collection, because it includes every existing row. Preserve DRAFT status until all release checks pass.
