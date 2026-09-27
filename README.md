# Opportunity Intelligence and Evidence-Assisted Proposal Platform

**Confidential client engagement · Architecture, AI-assisted delivery and reliability engineering**

I led the architecture and delivery of a connected workflow that moves from public opportunity discovery to a capability-statement draft a person can inspect, edit and export. The work combined product scoping, AI-assisted implementation, independent review, adversarial testing and controlled integration across two applications.

## The challenge

Business-development and proposal teams search fragmented portals, interpret opportunity requirements and look for credible evidence of prior capability. Each handoff creates risk: a missed match, a stale record, an unsupported statement or a technical failure mistaken for “nothing found.”

The goal was not simply to add AI. It was to make the workflow faster to navigate while keeping its decisions and failure states visible to the people responsible for the final submission.

## The solution

### Tool 1 — Opportunity discovery

Portal-specific adapters collect and normalize opportunities from multiple public sources. Configured English and Spanish terms support case- and accent-insensitive matching. Full UNDP detail-page text can provide matching context beyond the short display description. Discovery timestamps and matched keywords are written through a validated, header-name-driven Google Sheet contract.

### Tool 2 — Evidence-assisted proposal preparation

A read-only opportunity browser provides search, filters, sorting and pagination. Users can see why an opportunity matched, select one, manually obtain and upload its terms of reference (ToR), review the extracted requirements, retrieve relevant passages from a capability library and generate an editable draft for human review and DOCX export.

## End-to-end workflow

Public portals → adapter-based discovery → validated Sheet contract → opportunity browser → ToR upload and review → capability-library retrieval → editable draft → human review → DOCX output.

The [architecture diagram](ARCHITECTURE.md) shows the integration boundary between the tools and the separate evidence-library path.

## Engineering decisions that mattered

| Decision | User value |
|---|---|
| Validate and write by header name | Reordered Sheet columns cannot silently move values into the wrong fields. |
| Keep discovery time separate from deadline | “Newly discovered” has a real meaning instead of borrowing an unrelated date. |
| Distinguish source failure from an empty result | An unavailable portal cannot quietly masquerade as “no opportunities found.” |
| Match against full source text where available | Relevant terms deep in an opportunity description are not lost to display truncation. |
| Preserve last-known-good evidence during supported update failures | One bad document or incomplete write does not automatically destroy searchable evidence. |
| Report source files, indexed documents and search chunks separately | Users can see incomplete coverage instead of relying on a misleading total. |

## Delivery approach

I translated product goals into explicit contracts, split implementation into bounded tasks, used AI coding tools to accelerate delivery, and reviewed the resulting behavior independently. High-risk assumptions were challenged with focused regression tests, including reordered headers, long descriptions, partial index writes, unavailable source libraries and malformed optional data.

This is the kind of work I bring to an MVP: clear scope, explicit acceptance criteria, fast implementation, evidence-based review and honest release boundaries.

## Current boundaries

The workflow is delivered, but generated text, extracted requirements and source references still require human verification. ToR download remains manual. Deterministic evidence-quote verification and a generic **Evidence Studio** product are planned next-stage work. No unverified claims are made here about time savings, bid wins, adoption or commercial impact.

## Explore the case study

- [Detailed case study](CASE_STUDY.md)
- [Architecture and workflow](ARCHITECTURE.md)
- [One-page portfolio summary](portfolio/PORTFOLIO_ONE_PAGER.pdf) and [editable Word version](portfolio/PORTFOLIO_ONE_PAGER.docx)
- [Synthetic demonstration materials](examples/SYNTHETIC_DEMO.md)
- [Concise Spanish summary](SPANISH_SUMMARY.md)

**Discuss a scoped AI-assisted MVP:** Armando Elizalde · armando21elizalde@gmail.com · [LinkedIn](https://www.linkedin.com/in/elizaltech/)

All examples are synthetic. Client identity, private source code, operational links and client documents are withheld.

## Portfolio application

This repository also contains a standalone Streamlit presentation of the case study. It exposes only the anonymized material above and a downloadable copy of the one-page PDF.

Run it locally with:

```powershell
python -m pip install -r requirements.txt
python -m streamlit run streamlit_app.py
```

The intended deployment is a public Streamlit application backed by a private repository. Do not add client documents, application source repositories, credentials, live data, operational URLs or private deployment configuration to this project.
