# S03_SECTION9_COMPARISON

| Field | Value |
|---|---|
| Document ID | S03_SECTION9_COMPARISON |
| Version | 1.0 |
| Status | SUBMITTED FOR GATE |
| Stage | S03 |
| Date | 2026-11-20 |
| Depends on | S03_COMPARABLE_SYSTEMS_MATRIX; S03_PRIOR_ART_REGISTER; F-09; FX-10; QA-005; REF-02 §9 |

- **Status of this text:** working input for S08, not proposal text. SRC and CLM identifiers stay visible until S08 Pass A converts them into the form's notes and URLs.
- **Table schema:** the seven columns of REF-02 §9, unchanged (RF-003). Location descriptors are not researched (DEC-009) and remain `[LOCAL COMPLETION ONLY]`.
- **Selection:** eight candidate rows; the form requires at least three. Final row selection is an owner decision (ISS-030). Recommended minimum set: rows 1–4 (the initiatives named in the requirements statement) plus row 5 or 6 as a research or open-tool comparator.

## 1. Working table

| No. | Research or product | Type | Executing organization / approved location descriptor | Outcome | Latest status | Notes / URL |
|---|---|---|---|---|---|---|
| 1 | Wazoku innovation platform (idea and challenge management; Jen AI assistant; Wazoku Crowd) | Industry product | Wazoku Limited / [LOCAL COMPLETION ONLY] | Commercial product | In progress (offered as of 2026-11-20; ASSUMPTION from current support pages) | Vendor statements: SRC-040, SRC-041, SRC-042. https://support.wazoku.com/about_jen |
| 2 | ITONICS Innovation OS (idea management, trend radar, Prism AI) | Industry product | ITONICS / [LOCAL COMPLETION ONLY] | Commercial product | In progress (ASSUMPTION, as row 1) | Vendor statements: SRC-044, SRC-045. https://itonics-innovation.com/ai |
| 3 | Brightidea innovation management (Duplicate Checker, Scout app, AI features) | Industry product | Brightidea Inc. / [LOCAL COMPLETION ONLY] | Commercial product | In progress (ASSUMPTION, as row 1) | Vendor statements: SRC-046, SRC-047. https://support.brightidea.com/hc/en-us/articles/205840267-Duplicate-Checker-on-Post-Submission |
| 4 | Wellspring Scout and Accolade (technology scouting; innovation and idea management) | Industry product | Wellspring / [LOCAL COMPLETION ONLY] | Commercial product | In progress (ASSUMPTION, as row 1) | Vendor statements: SRC-048, SRC-049, SRC-050. https://www.wellspring.com/scout |
| 5 | PQAI prior-art search engine | Open-source research and industry initiative | PQAI initiative (initiated by AT&T and a regional IP alliance per SRC-054) / [LOCAL COMPLETION ONLY] | Commercial product (closest form category for an operating public service with open code; S08 to confirm) | In progress (ASSUMPTION) | SRC-053, SRC-054 |
| 6 | SOLVENT: mixed-initiative system for finding analogies between research papers | Publication (peer-reviewed) | Research groups at university institutions (authors' affiliations per SRC-055) / [LOCAL COMPLETION ONLY] | Laboratory prototype (our classification) | Completed (published 2018) | SRC-055. doi:10.1145/3274300 |
| 7 | US 11,561,987 B1 and family: platform matching unmet needs to a solutions database by semantic signatures | Patent | Reveal Networks Inc. / [LOCAL COMPLETION ONLY] | Patent (no product claim made) | Completed (granted 2023-01-24; listed active) | SRC-057, SRC-058. https://patents.google.com/patent/US11561987 |
| 8 | US 8,943,033 B2: overlap alerts between new and stored invention disclosures with inventor-controlled access | Patent | International Business Machines Corp. / [LOCAL COMPLETION ONLY] | Patent (no product claim made) | Completed (granted 2015-01-27; listed expired) | SRC-056. https://patents.google.com/patent/US8943033 |

The form lists outcome types for products and research (feasibility report to commercial product); it has no "patent" outcome. Rows 7–8 use "Patent" as a placeholder for S08 to resolve with the owner (ISS-030).

## 2. Similarities and differences (draft prose for S08)

**Wazoku.** Like the intended assistant, Wazoku documents a duplicate check on new submissions and an AI score that supports evaluation against challenge requirements (SRC-040, SRC-041). Its external reach is a solver community and company scouting (SRC-041, SRC-042), not retrieval of patents linked to a submission. The documentation read does not say how duplicates are detected or how evaluation scores are produced, and no accuracy figures are published. The intended assistant differs in combining R1, R2 and R4 results in one assessment record that the assessor approves (R3); whether this improves assessment is a hypothesis for the evaluation (CLM-006).

**ITONICS.** ITONICS documents the closest AI scope: duplicate detection, first-pass screening against jury criteria, patent clustering and market scanning, with per-change reviewer approval (SRC-044, SRC-045). Two differences matter for this project. First, the vendor allows AI changes to be auto-applied, whereas R3 requires a human decision on every assessment outcome. Second, patent analysis is described for competitor and market monitoring, not for examining prior art for an individual submission (R4). Models and methods are not disclosed.

**Brightidea.** Brightidea's Duplicate Checker searches earlier submissions within the same initiative while a submitter fills in the form (SRC-046), and its Scout app searches the web for companies matching a described need (SRC-047). R2-type checking of an internal precedent collection is not described. Brightidea is the only named vendor to document bring-your-own-model options with named providers (SRC-047), which is relevant to the data-handling constraint (C2, ISS-009).

**Wellspring.** Wellspring's strength in the documentation read is external search: Scout covers patents, publications, grants and startups (SRC-048), and Accolade provides evaluation scorecards and stage-gate workflows (SRC-050). Duplicate detection and AI-assisted assessment are not described on the pages read. The intended assistant takes the opposite starting point: the submitted need, compared first with internal records and only then with external sources.

**PQAI.** PQAI retrieves patents and technical literature from a plain-language description using models trained on examination records, and is available as open code and an API (SRC-053). It covers one requirement (R4) and has no submission management or approval workflow. It is a candidate component or baseline for R4, subject to access terms (RQ-14, ISS-006), not a competing product.

**SOLVENT.** SOLVENT matched research problems to analogous mechanisms by combining human annotation with a computational model, and found more analogies than baseline retrieval (SRC-055). It supports the design choice of keeping humans in the matching loop, but it works on research papers with crowd annotation, not on organizational submissions.

**Patent prior art.** US 11,561,987 B1 describes matching logged needs against a solutions database that includes patent documents, using rare-word "semantic signatures" (SRC-057). US 8,943,033 B2 describes alerting a submitter to overlap with stored internal disclosures and releasing details only with inventor consent (SRC-056). Each covers part of R1, R2 or R4; neither describes an assessor approving an assessment outcome. These are prior-art references, not freedom-to-operate findings (CLM-039).

## 3. Rules carried into S08

1. Do not write that the assistant "outperforms" or is "more accurate than" any row; no matched benchmark exists (QA-005, CLM-034).
2. Describe vendor features as "the vendor documents …" and keep access dates (ISS-032).
3. Compare against the final intended product (FX-10); the current-phase scope (ISS-001) is stated in Sections 7 and 11, not here.
