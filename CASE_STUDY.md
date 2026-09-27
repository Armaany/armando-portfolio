# Opportunity Intelligence and Evidence-Assisted Proposal Platform

## Initial problem and constraints

This confidential engagement connected two related activities: finding relevant opportunities and preparing a capability statement against an opportunity’s requirements. Analysts need a useful shortlist; proposal writers need credible source material; reviewers need to understand the basis of a draft. A successful handoff must preserve meaning as information moves between these tasks.

The platform had to accommodate multiple portal structures, bilingual matching, a shared Sheet contract, document extraction and an evolving evidence library. External sources and individual files could fail independently. AI-assisted extraction and drafting also required explicit review boundaries because fluent output is not proof of factual support.

## Discovery and scope decisions

The architectural scope separates discovery from proposal preparation. Tool 1 owns collection and Sheet writes. Tool 2 consumes the shared data in read-only mode and owns the preparation workflow. This makes the Sheet an explicit integration boundary rather than an incidental export.

The delivered workflow supports selecting an opportunity, followed by a manual ToR upload. Selection is intentionally not an automatic document-fetch operation: the user remains aware of which source document is being analyzed. A structured summary and detailed review precede retrieval and drafting.

## My role and AI-assisted delivery method

Led the architecture, AI-assisted implementation workflow, independent code review, testing, integration and delivery control for an end-to-end opportunity intelligence and document-generation platform.

My workflow used specifications and architecture decisions to define bounded implementation work, including delegation to AI-assisted implementation. I then reviewed whether the resulting behavior met the intended contract. Adversarial cases challenged optimistic assumptions; debugging and focused regression coverage supported integration and controlled delivery.

The engineering judgment is visible in boundaries that constrain implementation: a timestamp means discovery time, a fetch failure must not become an empty result, and an index update must not casually discard useful evidence. These rules are more consequential than the volume of generated code.

## Tool 1 design

Portal-specific adapters sit behind a common collection workflow. Enabled adapters are run with isolated exception handling, so a failure in one does not prevent collection from later sources. Records are deduplicated and checked against configured sector and geography criteria before storage.

Keyword normalization handles case and accents, supporting configured English and Spanish terms. Full UNDP detail-page text can supply matching context beyond a short display description. The same matching-text choice is used for filtering and for reporting matched keywords, helping keep the reason shown to a user aligned with the filtering decision. Detail retrieval can fail; full enrichment is therefore conditional rather than guaranteed for every record.

The orchestrator stamps discovery time when it processes an opportunity. This separates freshness from the deadline. Transient full-text matching fields are removed before storage rather than being appended to the shared contract.

## Tool 2 design

The opportunity browser reads the Sheet export and validates its headers. Search, filters, sorting and pagination support triage. Matched keywords make a row’s inclusion more understandable, but they are evidence of a keyword match rather than proof of business fit.

One opportunity can be selected for capability-statement preparation. The user obtains the ToR and uploads a PDF or DOCX. The extraction stage structures its contents, and “ToR at a glance” summarizes extracted fields before the detailed source review. The summary presentation normalizes existing extracted values; it does not independently verify the extraction.

Retrieval queries a Chroma index and applies metadata filters to candidate passages. Selected evidence is provided as context to a language-model-assisted draft generator. The review interface supports editing before document export. Source references and a constrained prompt help review, but neither establishes deterministic factual verification.

## Data contract between the tools

The integration uses a validated 14-column Sheet contract. Header names are normalized before lookup. Required columns must be present and duplicates are rejected; writing and reading use names rather than relying on fixed column positions. Unknown extra columns are handled without moving canonical values into the wrong fields.

| Information group | Meaning carried between tools |
|---|---|
| Identity and context | Portal, opportunity title, organization, geography and opportunity link |
| Timing and commercial context | Deadline and contract value, where available |
| Assessment | Summary, relevance, bid recommendation, risk flags and review status |
| Discovery explanation | Discovery timestamp and matched keywords |

These are contract concepts, not copied live rows. Discovery timestamps use explicit timezone semantics; matched keywords use a structured serialized list. The browser tolerates absent or malformed optional display values without converting them into unsupported facts.

The Sheet is a practical integration boundary. Its tradeoff is that schema changes need coordination and the consumer depends on export availability. Read-only consumption describes Tool 2’s behavior; it does not establish the security configuration of the underlying Sheet.

## Failure-handling improvements

An empty list is meaningful only when a source fetch succeeds and finds nothing. Typed failures preserve that distinction for handled adapter errors. The orchestrator can report a source failure and continue with other adapters.

Handled portal errors construct messages from controlled fields instead of embedding raw request URLs, headers or underlying exception text. Tests use secret-like sentinels to check that those strings do not reach the safe representation. This is a bounded error-handling control, not proof that every logging path is safe. Debug traces and production logs remain excluded from the portfolio.

The opportunity browser also treats malformed optional values defensively. Qualitative relevance labels remain visible rather than being lost because a field is not numeric. Selection copy tells users to obtain and upload the ToR, avoiding an implication that selecting a row has downloaded a document.

## Indexing-reliability improvements

The indexer reconciles source documents using content hashes and index configuration. Unchanged material can be skipped. A changed document is extracted and its replacement prepared before old evidence is removed. New generations are written and checked before exact old-generation identifiers are deleted.

On supported write failures, rollback targets the partial new generation while preserving old evidence. Recovery outcomes are surfaced, including failed cleanup; the design does not assume rollback always succeeds. A missing or empty source library is handled conservatively so that a temporary source problem does not silently erase a non-empty index.

The interface distinguishes source documents, indexed documents and searchable chunks. It also presents individual failed documents with controlled failure categories. Removing directory paths from a filename improves operational presentation, but does not anonymize the filename itself. Public recordings therefore require entirely synthetic source filenames.

Generation is blocked when the index is unavailable, empty or being updated. A preserved non-empty index can still support generation when the library is missing, with a warning that it may be stale. Availability and freshness are separate properties.

## Product and UX decisions

The inspected code and regression coverage show attention to the decisions users actually make: finding a relevant row, understanding its match, selecting an opportunity, checking extracted requirements and reviewing the draft. Search and pagination limit browsing burden; explicit selection language makes the next action clear; count labels distinguish files from indexed passages.

These changes reduce browsing burden and make the next action explicit. Formal usability measurement remains future work.

## Testing and review discipline

Focused tests cover integration contracts, defensive parsing, adapter failure behavior, full-text matching and evidence preservation. High-value cases simulate reordered headers, long descriptions, partial writes, unavailable libraries and malformed status details. Such tests examine failures that a successful demonstration alone would miss.

The portfolio highlights the failure classes covered by the implementation without presenting unverified performance, adoption or live-availability claims.

## Important defects and release evidence

| Defect class covered by regression tests | Potential consequence | Engineering response |
|---|---|---|
| Column position assumptions | Values land under the wrong headers | Validate normalized names and project writes by header name |
| Matching only a short description | A relevant keyword deep in the detail text is missed | Use full detail text for matching when available |
| Fetch errors reported as empty results | Analysts believe no opportunities exist | Distinguish typed failures from successful empty results |
| Qualitative relevance treated only as a number | Useful relevance information disappears | Preserve readable qualitative labels |
| Destructive replacement before a successful index write | Existing evidence becomes unavailable | Prepare and verify replacements; preserve old generations on supported failures |
| Chunk totals presented as document totals | Evidence coverage appears misleadingly large | Report source, indexed-document and chunk counts separately |

These defect classes are protected by focused regression tests. Release chronology is intentionally omitted because it is not needed to demonstrate the underlying engineering decisions.

## Outcomes and lessons learned

The result is a connected discovery-to-document workflow with explicit checkpoints and observable failure states. Its practical value is that an analyst can pass a selected opportunity into preparation, and a reviewer can work from structured requirements and retrieved capability passages. No time-saving percentage, revenue effect or bid-win claim is supported by this review.

Three lessons transfer to other AI-assisted MVPs. First, shared data contracts deserve the same attention as visible features. Second, failure states need product language: “empty,” “unavailable,” “partial” and “stale” imply different user actions. Third, preserving evidence and showing references are valuable foundations, but verification must be implemented separately rather than inferred from a grounded prompt.

## Next phases

Deterministic evidence-quote verification is planned next-stage work: the intended direction is to check proposed quotations against source evidence and surface unsupported claims. A generic Evidence Studio product is also planned; it is not a completed commercial offering.

Other candidate work includes completing retrieval and evidence-integrity controls, evaluating representative synthetic cases, and completing an in-app discovery trigger. Automatic ToR downloading, guaranteed accuracy, fully verified citations and enterprise compliance certifications are outside the delivered scope.
