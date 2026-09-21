# APZOK Vastu Chat — CSV Content Instructions

## Goal

Maintain and extend the Vastu Chat collections:
- VastuKnowledge
- VastuVocabulary
- VastuChatFlows

Read the existing backend and master CSV files before creating or
updating data. Produce import-ready CSV files compatible with the
actual backend.

## 1. Understand the existing implementation first

Inspect:
- Collection schemas and validators
- Language registry
- Question matching and search indexing
- Answer selection and verdict handling
- Conversation state and follow-up handling
- Remedy eligibility, ordering, and cross-row linking
- Publication and translation review checks
- Existing CSV headers and representative JSON values

Use the repository's current implementation as the source of truth.
Do not invent field names, JSON structures, enum values, or capabilities.

If requested behavior is unsupported, explain the gap.
Do not silently change the backend to make content fit.

## 2. Preserve existing data

Before editing:
- Identify the latest authoritative master CSV for each collection.
- Preserve existing record IDs, topic IDs, remedy IDs, and flow IDs.
- Preserve all existing questions, answers, translations, conditions,
  steps, limitations, source notes, and relationships.
- Avoid duplicate records and duplicate aliases.
- Do not replace full masters with files containing only new rows.

For each update, report records added, changed, and unchanged.
Explain any intentional deletion.

## 3. Collection responsibilities

### VastuKnowledge

Store the actual topic content:
- Questions and supported variations
- Short and detailed answers
- Qualified verdicts where appropriate
- Suggestions and remedies
- Steps and limitations
- Conditions such as construction stage
- Language content
- Explicit relationships to other topics

Follow the existing topic-per-row structure.
Store translations inside the existing language structure.

### VastuVocabulary

Store searchable question aliases and topic mappings.

Follow the current language-per-topic row structure.
Every vocabulary record must reference an existing topic.

Include natural questions, common spelling variations, and relevant
synonyms supported by the matcher.

Do not add misleading aliases solely to increase matches.
Do not use English text as a substitute for an untranslated language.

Generate search fields using the repository's existing indexing
functions. Do not invent search keys or version numbers manually.

### VastuChatFlows

Store reusable conversation messages and controls supported by
the backend.

Preserve existing flow IDs and action contracts.
Do not create a flow expecting new behavior unless the engine
actually handles it.

## 4. Write natural questions and useful answers

Cover relevant forms when the stored guidance supports them:
- Where should something be placed?
- Is my existing arrangement correct?
- Can I build or place something here?
- It is already built. What can I do?
- What can I do without changing the structure?
- Explain more.
- Show suggestions.

Keep important distinctions:
- Room location versus direction faced
- Under versus beside versus above
- Planned versus existing construction
- Positive versus negative statements
- Different compass directions

Do not merge questions that need different answers.

For yes/no questions, use the backend's verdict structure when
supported. Start with a qualified answer such as:
- Yes, according to the stored traditional guidance...
- No, this arrangement is generally discouraged in that guidance...
- This may need improvement...
- More information is needed...

Do not force a yes/no answer to an ambiguous question.
Do not add a yes/no opening to a “where” or “how” question unnecessarily.

Distinguish traditional Vastu beliefs from established facts.
Do not promise health, wealth, marriage, or other guaranteed outcomes.
Do not invent remedies or source references.

## 5. Handle any supported remedy count

Do not assume every topic has exactly two remedies.

A topic may contain zero, one, two, six, or more remedies, within
the limits enforced by the backend.

Each remedy must:
- Have a stable unique ID
- Apply to the actual situation
- Contain distinct useful guidance
- Include steps and limitations where appropriate
- Use supported eligibility conditions
- Have corresponding language content when available

Do not add filler remedies to reach a target count.
Do not duplicate the same remedy with different wording.

Check that Next, Read more, and All suggestions work for the full
eligible remedy list, including the final-item behavior.

## 6. Cross-row remedies

Use the existing explicit linking mechanism.

Only share a remedy when it is relevant to the receiving topic.
Follow all reciprocal-link requirements enforced by the backend.

Preserve:
- Source topic and remedy identity
- Language availability
- Review and publication requirements
- Construction-stage and other conditions
- Deduplication and ordering

A shared word such as “kitchen” is not enough to justify sharing.
Never transfer advice that changes meaning in the receiving context.

## 7. Matching priorities

Preserve the engine's existing ranking:
1. Exact question or alias match
2. Supported equivalent phrasing
3. Relevant related candidates requiring clarification
4. Honest no-match response when necessary

Treat matching scores as retrieval scores, not accuracy guarantees.
Never claim 80–100% correctness merely from a similarity score.

Search questions, answers, and remedy content only through mechanisms
supported by the current backend.

## 8. Languages

Read supported language codes from the backend registry.

For each translation:
- Preserve the original meaning and conditions.
- Use natural grammar and the correct script.
- Translate answers, remedy steps, limitations, and user-facing labels.
- Keep technical IDs unchanged.
- Do not claim human or native-speaker review unless it occurred.

Keep incomplete translations explicitly marked as missing.
Keep placeholder vocabulary inactive.
Do not mark untranslated content as complete.

If a language is unsupported, report the backend work required
instead of adding an unusable language code.

## 9. Publication

Treat the CMS publication status and custom contentStatus as
separate fields.

Follow all actual backend eligibility checks, including review,
test-only, translation, and activation flags.

Do not publish content simply to bypass those checks.
Preserve draft status for incomplete material.
State what remains necessary before release.

## 10. CSV formatting

Use:
- UTF-8 encoding
- Existing exact headers
- Valid CSV quoting
- Valid JSON inside JSON fields
- Correct arrays, booleans, numbers, and strings

Avoid:
- Double-encoded JSON
- Arrays stored as strings inside arrays
- Broken quotes or truncated content
- Accidental field renaming
- Duplicate IDs
- Spreadsheet formulas in content cells

Respect current field-size and record-size limits.

## 11. Validation

Before delivery:
- Parse every CSV.
- Parse every embedded JSON field.
- Run the repository's schema validators.
- Check unique IDs and valid topic references.
- Check vocabulary mappings and language consistency.
- Check remedy references and cross-row eligibility.
- Compare against the original masters for accidental data loss.
- Run relevant engine tests using the generated records.

Include tests for:
- Exact questions
- Equivalent phrasing
- Ambiguous questions
- Changed direction or spatial relationship
- Existing versus planned construction
- Cross-row remedies
- Different remedy counts
- Missing translations
- Duplicate prevention
- End of suggestions

Use the actual implementation to determine expected results.
Report tests that could not be run.
Do not claim live Wix or Android testing from local tests alone.

## 12. Deliverables

Provide complete updated masters:
- VastuKnowledge_Master.csv
- VastuVocabulary_Master.csv
- VastuChatFlows_Master.csv

Also provide:
- A short change report
- Row counts by collection and language
- Validation results
- Remaining draft or translation gaps
- Import instructions that avoid duplicate records

Never claim that all languages or content are complete unless
the generated files actually contain and validate that content.

## Supported languages — complete coverage

Prepare content for all 23 supported languages:

| Code | Language |
|------|----------|
| en | English |
| kn | Kannada |
| hi | Hindi |
| ta | Tamil |
| te | Telugu |
| ml | Malayalam |
| bn | Bengali |
| mr | Marathi |
| gu | Gujarati |
| ur | Urdu |
| pa | Punjabi |
| or | Odia |
| as | Assamese |
| mai | Maithili |
| sat | Santali |
| ks | Kashmiri |
| ne | Nepali |
| sd | Sindhi |
| doi | Dogri |
| kok | Konkani |
| mni | Manipuri / Meitei |
| brx | Bodo |
| sa | Sanskrit |

Verify these codes against the current backend registry before editing.
This list covers English and the 22 scheduled Indian languages;
it does not represent every language spoken in India.

Translate complete user-facing content:
- Questions and meaningful question variations
- Short and detailed answers
- Qualified yes/no verdicts
- Suggestions and remedies
- Every remedy step and limitation
- Options, button labels, and clarification messages
- Fallback and end-of-suggestions messages

Preserve meaning, conditions, grammar, and appropriate script.
Keep internal IDs and action values unchanged.
Do not substitute English text and label it as a completed translation.
Record missing translations honestly and keep their vocabulary inactive.
Do not claim native-speaker review unless it occurred.

## Comprehensive content collection

For each requested topic, gather and organize relevant guidance from
the existing approved dataset and identifiable sources.

Cover applicable situations:
- New construction
- Existing construction
- Renovation
- Rented homes or restricted structural changes
- Different locations and facing directions
- Limited space
- Alternative arrangements
- Unclear or missing information

Include only situations supported by the source material.
Separate traditional preferences from practical building guidance.
Preserve disagreements between traditions rather than inventing
one universally correct answer.

Never invent source citations, remedies, guarantees, or missing facts.
Document sources and unresolved gaps using supported schema fields
or a separate content report.

## Remedies, suggestions, and options — no arbitrary content quota

Do not restrict every topic to two, six, or another fixed number.

Include every distinct, relevant, supported remedy or suggestion
available for that topic. Some topics may legitimately have none.

Do not add repetitive or weak suggestions merely to increase quantity.

For each remedy, preserve:
- Stable ID
- Applicable conditions
- Summary
- Full explanation
- Ordered steps
- Limitations
- Supported alternatives
- Translations
- Source relationship

For options and buttons:
- Use actions already supported by the backend.
- Translate labels while preserving internal action values.
- Ask for clarification when different options lead to different answers.
- Do not create buttons with no working action.

“No arbitrary content quota” does not mean unlimited storage or
unlimited response size.

Inspect actual backend limits for records, remedies, steps, search
indexes, response items, and buttons.

If complete content exceeds a limit:
1. Report the exact limit and affected content.
2. Preserve all content in the master source.
3. Use supported topic splitting, related records, or pagination.
4. If necessary, propose the specific backend update required.

Never silently truncate content or claim unlimited support.

## Prepare complete, import-ready CSV masters

Produce:
1. VastuKnowledge_Master.csv
2. VastuVocabulary_Master.csv
3. VastuChatFlows_Master.csv

Preserve all existing records and stable IDs.
Use exact current headers, field types, JSON structures, and enum values.

Maintain:
- Knowledge: one row per topic, with language content inside its
  supported language structure.
- Vocabulary: one row per topic per language, following the current
  schema; incomplete language rows remain inactive.
- ChatFlows: one row per supported flow ID, following the current
  localized flow structure.

For example, five topics across 23 languages normally require
115 vocabulary rows, including any explicitly inactive pending rows.

Use UTF-8 CSV with correctly escaped JSON.
Validate every row, reference, language entry, remedy, and action.
Check that CSV export and re-import preserve the full content.

Deliver a coverage report showing:
- Topics and row counts
- Available and missing languages
- Remedy counts per topic
- Translation and review status
- Validation results
- Any technical limits or unfinished work

Do not describe the files as complete or ready for publication
when content, translations, or required checks remain unfinished.
