# S03_PRIOR_ART_REGISTER

| Field | Value |
|---|---|
| Document ID | S03_PRIOR_ART_REGISTER |
| Version | 2.0 |
| Status | SUBMITTED FOR GATE |
| Stage | S04.1 |
| Date | 2026-11-20 |
| Depends on | S01_RESEARCH_QUESTIONS (RQ-12); 02_SOURCE_LOG; DEC-009; RC-01 |

- **S04.1 status note (RC-01):** the S04 session set this file to APPROVED on the basis of an approval inferred from the wording of the owner's START_STAGE S04 instruction. That approval has not been recorded as an explicit owner decision, so the status is returned to SUBMITTED FOR GATE until the owner confirms it (DEC-028). Reviewed S03 content: commit 6780335.
- **Purpose:** documented answer to RQ-12: are there patents or published applications describing systems that match submitted needs against internal precedents and external prior art with human approval?
- **Nature of this search:** a technical prior-art scan to support Section 9. It is not a patentability, validity or freedom-to-operate search and supports no legal conclusion (CLM-039).

## 1. Search protocol

| Item | Value |
|---|---|
| Date | 2026-11-20 |
| Tool | Web search tool (standard and extended modes), then the fetch tool on each relevant record |
| Databases reached | Google Patents record pages; USPTO patent full-text (search-result extracts) and Official Gazette; Canadian Patent Database (CIPO). International and national-office records only; no jurisdiction-specific searches (DEC-009). |
| Query concepts | (a) matching technical needs or unmet needs to solutions; (b) ranking solutions to user-described technical problems; (c) duplicate or overlap detection for submitted ideas or invention disclosures; (d) idea management with reviewer evaluation; (e) the S02 lead EP 2765543 A1 |
| Inclusion rule | Record whose abstract, claims or description addresses at least one of R1, R2 or R4, with or without a human decision step (R3) |
| Verification | Bibliographic data and the statement used were read on the record page (depth A), except where §4 says otherwise |

## 2. Patent records found

| No. | Record | Owner (as listed) | Dates | Status (as listed) | What it describes | R1 | R2 | R3 | R4 | Source | Label |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PA-1 | US 8,943,033 B2, "System and method for avoiding duplication of effort in drafting documents" (family member US 9,727,934 B2) | International Business Machines Corp. (original assignee) | Priority and filing 2009-01-30; granted 2015-01-27 | Expired – fee related (database assumption) | Terms from a new invention disclosure are matched against stored internal disclosures; overlaps are alerted; confidential sections are released only after an inventor of record authorizes access | Yes (keyword-style term matching) | Partly (stored internal disclosures) | Yes (inventor authorization; counsel or arbitrator variants) | No | SRC-056 | VERIFIED (SRC-056) |
| PA-2 | US 11,561,987 B1, "Platform for semantic search and dynamic reclassification" (family: US 12,061,612 B1; US 12,461,922 B1) | Reveal Networks Inc. | Earliest priority 2013-05-23 (database assumption); filed 2022-06-24; granted 2023-01-24. US 12,461,922 B1 published 2025-11-04 | Active (database assumption) | A needs database and a solutions database; a matching engine compares "semantic signatures" built from the distribution of rare words; solutions may be crawled from expired or abandoned patents; the user is asked to confirm details when logging a need | Partly (signature similarity between documents) | Yes (needs matched to a solutions database) | Partly (user confirmation of need details; no assessment approval) | Yes (patent documents among solution sources) | SRC-057, SRC-058 | VERIFIED (SRC-057, SRC-058) |
| PA-3 | CA 2588160 (PCT/US2005/041749; WO 2006/055746), "Integrated idea management method and software with protection mechanism" | Not stated on the record page read | Date shown 2007-05-16 (type of date not stated) | Not stated on the record page read | Ideas submitted with category, description and designated review organization; committee members vote electronically, rate feasibility and set status; filter-based search only | No | No | Yes (committee vote and feasibility rating) | No | SRC-059 | VERIFIED (SRC-059); owner and status OPEN |
| PA-4 | EP 2765543 A1, "Method and system for matching technical needs to solutions" | Not retrieved | Not retrieved | Not retrieved | Claim 1 opening: a project description with at least one unmet technical need is received at an "innovation exchange network"; Figure 1 is described as a process for matching the unmet needs with an expert and obtaining proposed solutions | No | No | Partly (expert-proposed solutions) | Partly (external experts, not patents) | SRC-060 | Partial: title and claim-1 opening from a search-result extract only; record page failed to load (ISS-031) |
| PA-5 | US 11,762,916 B1, "User interface for identifying unmet technical needs and/or technical problems" | Not retrieved | Not retrieved | Not retrieved | Abstract: systems receive user input and automatically identify unmet technical needs or problems in areas of technology; the interface can analyze a user's technical capabilities | No | No | No | Partly (document analysis) | SRC-061 | Partial: abstract extract only (ISS-031) |

## 3. Non-patent prior art (research and open tools)

| No. | Item | Relevance | Source | Label |
|---|---|---|---|---|
| NP-1 | SOLVENT (Chan et al., 2018): human annotation of problem and mechanism plus a computational model to find analogous papers | Mixed-initiative matching of problems to existing solutions in other domains (R2, R3) | SRC-055 | VERIFIED |
| NP-2 | PQAI: open-source prior-art search from plain-language descriptions | Natural-language-to-patent retrieval (R4) | SRC-053, SRC-054 | VERIFIED (SRC-053) |
| NP-3 | Need–Seed framework (Verma et al., 2025): maps market needs to patent claims with three mandatory expert review gates | Need-to-patent matching with human gates; preprint with no quantitative evaluation | SRC-062 | T3, context only |
| NP-4 | Idea relationship analysis, analogy mining, AI idea screening (S02) | R1 and R3 background | SRC-013, SRC-016, SRC-017 | S02, VERIFIED |

## 4. Result and limitations

**Result (RQ-12).** The scan found prior art for individual elements: overlap detection against stored internal submissions with a human authorization step (PA-1), matching of logged needs against a solutions database that includes patent documents (PA-2), and committee-based idea evaluation (PA-3). No record found in this scan combines comparison with stored submissions (R1), checking an internal precedent collection (R2), external patent retrieval (R4) and mandatory human approval of the assessment outcome (R3) in one system. This is a statement about this scan only (CLM-039), not evidence that no such record exists.

**Limitations.**

1. The patent-database search interfaces were reached only through the web search tool; Boolean or classification-code searches in Espacenet, PATENTSCOPE or USPTO Patent Public Search were not run.
2. Google Patents record pages for EP 2765543 A1 and US 11,762,916 B1 returned server errors; USPTO full-text PDFs returned no machine-readable text. PA-4 and PA-5 rest on search-result extracts (ISS-031).
3. Legal status and priority dates shown by Google Patents are labelled by that database as assumptions.
4. Non-English and jurisdiction-specific patent literature were not searched (DEC-009).

**Recommendation (PROPOSED).** If the owner wants Section 9 to carry patent rows, re-check PA-1 and PA-2 on the issuing office's register before submission, or commission a professional search; decision recorded as part of ISS-030.
