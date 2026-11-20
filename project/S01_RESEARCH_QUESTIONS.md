# S01_RESEARCH_QUESTIONS

| Field | Value |
|---|---|
| Document ID | S01_RESEARCH_QUESTIONS |
| Version | 2.0 |
| Status | SUBMITTED FOR GATE |
| Stage | S02 |
| Date | 2026-11-20 |
| Depends on | S01_REQUIREMENTS_REGISTER; DEC-002; S02_RESEARCH_SYNTHESIS |

## 1. Scope rules for research

- Research the final intended product and the methods it would use; do not research the sponsor, its location or local markets (DEC-009).
- Search terms listed below are **leads**, not evidence or design choices (QA-010).
- Every source used enters `02_SOURCE_LOG.md` before it is cited.
- A research question is closed when its "done when" condition is met or when a documented search finds no adequate evidence; the latter is recorded, not hidden.

## 2. Research questions

### S02 — Scientific and technical literature

| ID | Question | Drives | Sections | Evidence sought | Done when | Search leads |
|---|---|---|---|---|---|---|
| RQ-01 | Which text-representation and similarity methods are documented for short-to-medium free-text descriptions of needs, problems or ideas, and what are their reported strengths and limitations (lexical, dense embedding, hybrid, re-ranking)? | R1, R2 | 8, 12 | T1 surveys and empirical studies; official model documentation | Each method family has ≥1 T1 source with limitations stated | lexical retrieval BM25; sentence embeddings; hybrid retrieval; cross-encoder re-ranking; semantic textual similarity |
| RQ-02 | What does the literature report on duplicate and near-duplicate detection in user-submitted text collections, and how transferable are those results to need or challenge submissions? | R1 (ISS-004) | 8, 12 | T1 studies in comparable settings (idea management, community Q&A, issue trackers) | ≥2 T1 studies with setting, data and metric noted, plus a transferability note | duplicate question detection; duplicate bug report retrieval; idea similarity in innovation management |
| RQ-03 | How is retrieval from an internal collection of solutions or precedents typically designed and evaluated, including need–solution matching and grounding of generated summaries in retrieved items? | R2 | 8, 12 | T1 studies on retrieval-augmented generation and problem–solution matching | ≥2 T1 sources; grounding and citation risks stated | retrieval-augmented generation evaluation; problem–solution matching; case-based reasoning retrieval |
| RQ-04 | What methods are documented for retrieving patents and non-patent prior art from natural-language problem descriptions, and how are they evaluated? | R4 | 8, 9, 12 | T1 patent-retrieval studies and evaluation campaigns | ≥2 T1 sources; evaluation settings recorded | patent prior-art search; CLEF-IP; patent retrieval with embeddings |
| RQ-05 | Which human-in-the-loop decision-support design practices are evidenced for keeping humans in control: presentation of evidence, explanation, override, audit trail, and mitigation of automation bias? | R3 | 6, 8, 12, 17 | T1 human–AI interaction and decision-support research | ≥2 T1 sources; design implications listed | automation bias decision support; human–AI interaction guidelines; human oversight |
| RQ-06 | How can retrieval and similarity be evaluated reproducibly when labelled data is scarce: metrics, construction of small test collections, annotation protocols and inter-annotator agreement? | QA-002, QA-004, R1, R2, R4 | 8, 12, 13 | T1 IR evaluation methodology | Metric set and annotation procedure each supported by T1 sources | precision at k; nDCG; MRR; test collection construction; Cohen's kappa |
| RQ-07 *(conditional)* | If submissions are not exclusively in English, which multilingual or cross-lingual retrieval methods apply, and with what limitations? | ISS-007 | 8, 12 | T1 cross-lingual retrieval studies | Activated only if ISS-007 confirms non-English content | cross-lingual retrieval; multilingual sentence embeddings |
| RQ-08 | What reliability problems are reported when large language models summarize or structure documents for assessment support (unsupported statements, citation errors), and which mitigations are documented? | R2, R3, R4, RF-004 | 8, 12, 17 | T1 evaluation studies | ≥2 T1 sources; mitigations listed with evidence strength | LLM hallucination evaluation; attribution and citation accuracy; grounded generation |
| RQ-09 | What approaches allow a system to use recorded human decisions to improve later retrieval (relevance feedback, learning to rank, active learning), and what governance issues do they raise? | C3, C1 (future) | 11, 12 (extensibility only) | T1 overview sources | 1–2 T1 sources sufficient; informs extensibility design only | relevance feedback; learning to rank; active learning |

### S03 — Comparable systems and prior art

| ID | Question | Drives | Sections | Evidence sought | Done when | Search leads |
|---|---|---|---|---|---|---|
| RQ-10 | What do Wazoku, ITONICS, Brightidea and Wellspring state in their own primary documentation about similarity or duplicate detection, AI-assisted evaluation, external technology or patent scouting, and human review? | C4, QA-005 | 9 | T2 vendor documentation, labelled as vendor statements | Each capability cell sourced or marked "not documented" | Vendor documentation and product pages |
| RQ-11 | Which further products or research systems are comparable to the final intended product (open-innovation and challenge platforms, patent analytics tools, research prototypes)? | F-09, FX-10 | 9 | T1 research systems; T2 products | ≥3 verified comparators in total for Section 9 | open innovation platform AI; technology scouting software; patent landscaping tools |
| RQ-12 | Are there patents or published applications describing systems that match submitted needs against internal precedents and external prior art with human approval? | F-09, R4 | 9 | T1 patent-office records | Documented search with query, database and date; results or "none found" recorded | Patent database search (international databases only; jurisdiction-specific searches deferred, DEC-009) |

### S04–S05 — Architecture, feasibility and evaluation inputs

| ID | Question | Drives | Sections | Evidence sought | Done when | Search leads |
|---|---|---|---|---|---|---|
| RQ-13 | What do the official standards bodies publicly state about the scope of ISO/IEC 27001 and ISO/IEC 20000-1 (current editions), and which design obligations could reasonably be proposed as alignment? | C2, ISS-010 | 8, 12, 17 | T1 official ISO/IEC pages | Current editions and scopes verified; mapping labelled PROPOSED | ISO official catalogue pages |
| RQ-14 | Which external patent and prior-art data sources could the assistant use for R4, and what are their access methods, terms of use and limits? | R4, ISS-006 | 8, 12, 15 | T1 official data-provider documentation | ≥2 options with terms verified, or a documented constraint | Official patent-office data services; open scholarly metadata services |
| RQ-15 | What deployment options (self-hosted open-weight models versus hosted APIs) fit the data-handling constraint, and what compute does each require at the expected scale? | ISS-009, ISS-023, C2 | 8, 12, 15, 17 | T1 official model and platform documentation | Options compared with verified licence and resource figures | Model cards and licences; provider data-processing terms |

## 3. Coverage check

Classification of C-series items (SC, EA, PG) follows S01_REQUIREMENTS_REGISTER §2. PG items are covered here because they govern how evidence is gathered, not because they are product requirements.

| Item (classification) | Research questions |
|---|---|
| R1 | RQ-01, RQ-02, RQ-06 |
| R2 | RQ-01, RQ-03, RQ-06, RQ-08 |
| R3 | RQ-05, RQ-08 |
| R4 | RQ-04, RQ-06, RQ-08, RQ-12, RQ-14 |
| C1 (SC) | RQ-09 |
| C2 (SC) | RQ-13, RQ-15 |
| C3 (EA) | RQ-09 |
| C4 (PG) | RQ-10 |
| C5 (PG) | RQ-06 |
| C6 (PG) | Confidentiality and process rule; no research question |

## 4. Status after S02

| RQ | Status | Evidence |
|---|---|---|
| RQ-01 | Closed for S02 | S02 matrix rows 1.1–1.11 |
| RQ-02 | Closed for S02 | Rows 2.1–2.5 |
| RQ-03 | Partially closed; thin direct evidence | Rows 3.1–3.5 |
| RQ-04 | Partially closed; need-to-patent gap (ISS-028) | Rows 4.1–4.3 |
| RQ-05 | Closed for S02; mitigator detail open | Rows 5.1–5.5 |
| RQ-06 | Closed for S02 | Rows 6.1–6.6 |
| RQ-07 | Not activated (ISS-007) | — |
| RQ-08 | Closed for S02 | Rows 8.1–8.4 |
| RQ-09 | Closed for S02 | Rows 9.1–9.2 |
| RQ-10 to RQ-15 | Not started | S03–S05 |

