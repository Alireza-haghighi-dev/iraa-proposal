# S01_REQUIREMENTS_REGISTER

| Field | Value |
|---|---|
| Document ID | S01_REQUIREMENTS_REGISTER |
| Version | 1.2 |
| Status | APPROVED |
| Stage | S01 |
| Date | 2026-11-20 |
| Depends on | REF-01; REF-02; DEC-002 |

## 1. Product requirements (from REF-01 §7)

REF-01 lists four "essential requirements" without priority order. They are carried as mandatory. The "Source text" column reproduces REF-01 word for word. Everything in the "Working interpretation" column is this project's reading under DEC-002, not source text, and may change when the linked open issues are resolved.

| ID | Source text (REF-01, verbatim) | Source | Class | Working interpretation (not source text) | Unresolved points | Verification approach (to be defined in S05) | Sections |
|---|---|---|---|---|---|---|---|
| R1 | Assess similarities among requirements already stored in the platform. | REF-01 §7.1 | Functional | Identify stored submissions that describe the same or a closely related need or challenge. | New-versus-stored comparison, grouping of the stored collection, or both (ISS-004). Similarity criteria not defined. Whether the project can access stored records is open (ISS-002, ISS-008). | Retrieval and duplicate-detection metrics on a labelled test set | 7, 8, 12, 13 |
| R2 | Check whether relevant existing solutions or precedents are available in an approved internal collection. | REF-01 §7.2 | Functional | Where an approved collection is available to the assistant, retrieve items from it that may address a submission and present them to the assessor. | REF-01 does not establish that the collection exists as a populated, machine-readable dataset, what it contains, who approves it, or whether the project may use it (ISS-003, ISS-002). No design or claim may assume these. | Retrieval relevance judged by assessors, conditional on ISS-003 and ISS-002 | 7, 8, 12, 13 |
| R3 | Require final human approval of assessments and processing outcomes. | REF-01 §7.3 | Governance / functional | The assistant proposes; an assessor approves, edits or rejects. No outcome is final without assessor approval. | What an "assessment" contains (ISS-005). | Workflow test showing that no outcome is finalized without an approval record | 6, 7, 8, 12, 13, 17 |
| R4 | Examine relevant external patents and solution examples for submitted requirements. | REF-01 §7.4 | Functional | Retrieve external prior art (patents and documented solution examples) related to a submission for assessor review. | Acceptable sources, licensing and access (ISS-006). "Solution examples" not defined. | Retrieval relevance on a sample, judged by assessors | 7, 8, 9, 12, 13 |

## 2. C-series: constraints, advisory guidance and project governance rules

The C-series mixes items of different authority. Identifiers are kept unchanged for traceability; the **Classification** column states what each item is and whom it binds.

| Classification | Meaning | Binds |
|---|---|---|
| **SC** — Sponsor-origin constraint | Stated as a constraint in the body of the sponsor's statement of need (REF-01) | The proposed product |
| **EA** — Evaluator advisory | Recommendation recorded in the statement's evaluator section | Scope of the current project (advisory) |
| **PG** — Project governance rule | Evidence-handling or confidentiality rule from the owner's working-copy annotations and restrictions, adopted by this project | How this project researches and writes; **not** a technical requirement on the product |

| ID | Text | Source and origin | Classification | Notes | Sections |
|---|---|---|---|---|---|
| C1 | "The assistant should be extensible to support user-requested enhancements in later stages." | REF-01 §8, statement body | SC | Design for adding functions without rebuilding the core. Specific enhancements are not named. | 8, 11, 12 |
| C2 | "ISO/IEC 20000 and ISO/IEC 27001 are mentioned as constraints; the specific applicable controls and scope of conformity have not been specified." | REF-01 §8. The standards mention is sponsor-origin; the second clause reads as a working-copy annotation. | SC (scope unresolved) | Treat as proposed alignment until ISS-009 and ISS-010 are resolved. No conformity or certification claim (REF-03 §4.9). | 8, 12, 17 |
| C3 | The evaluator suggests enabling future stages to improve analyses using prior assessments; this is not a requirement for autonomous self-training in the current project. (Paraphrase of REF-01 §17.) | REF-01 §17, initial evaluator analysis; the second sentence reads as a working-copy annotation | EA | Current design may record assessor decisions so the capability can be added later (C1). No self-training in the current project. | 7, 11 |
| C4 | Descriptions of related programs (Wazoku, ITONICS, Brightidea, Wellspring) require independent verification before use as comparative evidence. | REF-01 §10 closing note and external collaboration restrictions; working-copy annotation, not attributable to the sponsor's original statement on available evidence | PG | Governs evidence handling for Section 9 (CLM-001 to CLM-004). | 9 |
| C5 | Expected benefits (speed, accuracy, coordination, consistency, fewer errors) are not measured outcomes; no monetary estimate is supplied. | REF-01 §6 and §15 qualifying sentences; working-copy annotation | PG | Governs how benefits are written: hypotheses only (CLM-006, QA-002). The benefits themselves are sponsor expectations (CTX-07). | 6, 7, 8 |
| C6 | Use only the English working representation; no identifying or sponsor-only details; preserve section numbering; mark absent information OPEN; do not treat draft metrics, standards mentions or vendor descriptions as verified. | External collaboration restrictions in REF-01 and REF-02; owner-imposed | PG | Confidentiality and process rule; reinforced by DEC-009. | All |

## 3. Context facts (not requirements)

| ID | Fact as stated in source | Source | Use |
|---|---|---|---|
| CTX-01 | Record volume beyond the usual level lengthens reviews and creates an assessment backlog. | REF-01 §4 | Problem statement (Section 6); unquantified (CLM-005) |
| CTX-02 | Reviews are currently performed by human personnel. | REF-01 §9 | Baseline workflow (Sections 6, 8) |
| CTX-03 | Immediate need is the sponsoring organization; possible applicability to comparable organizations if usefulness is shown; no numerical demand estimate. | REF-01 §5 | Sections 6, 11 (CLM-007) |
| CTX-04 | Application domain: ICT. | REF-01 §1 | Classification context |
| CTX-05 | Keywords: assistant; intelligent; requirement review; requirement processing; intelligent assessment. | REF-01 §13 | Search terms for S02–S03; Section 1 wording |
| CTX-06 | Source title: "Intelligent Assistant for Requirements Review". | REF-01 title | ISS-015 |
| CTX-07 | Proposed solution: an intelligent assistant supporting more effective and accurate assessment of submissions. | REF-01 §11 | Section 6; "accurate" requires a metric (C5) |
| CTX-08 | Long-term concept: an assistant able to support the full assessment workflow. | REF-01 §15 | Section 11 future phases only |

Administrative items in REF-01 (§2 sponsor, §3 representative, §12 support mechanism, §16 preparer, §18 central evaluator, empty) are local-completion or owner items: ISS-019, ISS-026.

## 4. Proposal-form obligations by section (REF-02)

Completion class: **D** = draftable in the English package; **P** = partly draftable, remainder local or S10; **L** = local completion only; **S10** = completed only in S10.

| ID | Section | Mandatory content | Table | Class | Drafting stage |
|---|---|---|---|---|---|
| F-01 | 1 Project title | Subject, maturity stage, execution stage(s), prototype type | No | D (depends on ISS-001) | S08, final S10 |
| F-02 | 2 Team name | Name communicating the team's field | No | L | Local |
| F-03 | 3 Team lead and contact | Personal contact information | No | L | Local |
| F-04 | 4 Duration and person-hours | Months; total person-hours | No | S10 | S10 |
| F-05 | 5 General classification | Type, rationale, maturity, execution stages, relationship; parent project if any | Yes, 5 rows | D (depends on ISS-001, ISS-016) | S04 provisional, S08 |
| F-06 | 6 Necessity and significance | Why the final product matters; the gap; how it may be addressed. Funded-phase justification belongs in Section 11. | No | D | S08 |
| F-07 | 7 Objectives | Current-project objectives, scope, assumptions; only Gantt-scheduled deliverables; what exists at completion | No | D | S08 |
| F-08 | 8 Features and specifications | Key deliverable features; measurable specifications in a table for design/prototype projects; user requirements for feasibility projects; measurable versus functional separated | Table for measurable specs | D | S05 inputs, S08 |
| F-09 | 9 Related research and products | At least three comparators against the final intended product; type, executing organization, outcome, status, URL. Location fields for external or local markets reserved for local completion. | Yes, 7 columns | P | S03, S08 |
| F-10 | 10 Team prior work | Documented relevant work only; blank if none | Yes, 7 columns | S10 / L | S10 |
| F-11 | 11 Continuity and future stages | Current project as row 1; tentative title, duration, cost, deliverable per stage; future stages are plans | Yes, 5 columns | P (titles and deliverables draftable; durations S10; cost local) | S04, S08, S10 |
| F-12 | 12 Technical method | Problem-solving logic; requirement and constraint handling; research sources; tools; development and test methods; exact Section 13 activity titles expanded; verified or "proposed" details; no unmeasurable adjectives | No | D | S07 |
| F-13 | 13 Activities and deliverables | Main activities, each with assessable tangible output, key tasks, person-hour estimate for a proficient practitioner; reviewer preference six or seven | Yes, 5 columns | D (effort provisional until S10) | S06 |
| F-14 | 14 Implementation team | Qualification, responsibility, monthly hours, share of total effort; shares total 100% | Yes, 6 columns | S10 / L | S10 |
| F-15 | 15 Budget | Staff cost from person-hours and justified rate; consumables, operating, capital items; illustrative form lines not assumed valid | Yes, 6 columns | S10 / L | S10 |
| F-16 | 16 Gantt schedule | Same activity titles and efforts as Section 13; months from Section 14 availability and dependencies; per-activity cost; weights total 100% | Yes, 17 columns (12 months) | S10 | S10 |
| F-17 | 17 Execution risks | Technical, data, timeline, financial risks from the actual plan, with realistic mitigations; no untested assurances | Yes, 4 columns | P (technical and data S08; timeline and financial S10) | S08, S10 |
| F-18 | 18 Completion date | Date | No | L | Local |
| F-19 | 19 Other remarks | Optional | No | D (optional) | S08 |
| F-20 | 20 Attachments | Completed proposal, statement of need, resumes, other categories | Yes, 2 columns | L | Local / S10 |

## 5. Cross-section rules

| ID | Rule | Source | Checked at |
|---|---|---|---|
| FX-01 | Section 12 repeats Section 13 activity numbers and titles exactly, one-to-one. | REF-02 §12; RF-006 | S07, S09, S10 |
| FX-02 | Sum of Section 16 person-hours equals Section 13 total. | REF-02 §16 | S10 (script) |
| FX-03 | Sum of Section 16 activity costs equals Section 15 total. | REF-02 §16 | S10 (script) |
| FX-04 | Section 16 weight = activity cost ÷ total cost; weights total 100%. | REF-02 §16 | S10 (script) |
| FX-05 | Section 14 shares of total effort total 100%. | REF-02 §14 | S10 (script) |
| FX-06 | Section 7 objectives cover only deliverables in the current Gantt; longer-term ambitions go to Section 11. | REF-02 §7 | S08, S09 |
| FX-07 | Section 6 justifies the final product; justification of the funded phase is in Section 11. | REF-02 §6 | S08, S09 |
| FX-08 | Section 16 months follow Section 14 availability and activity dependencies. | REF-02 §16; RF-010 | S10 |
| FX-09 | Section 1 title is consistent with Section 5 maturity and execution stages and the prototype type. | REF-02 §1, §5; RF-011 | S08, S10 |
| FX-10 | Section 9 compares the final intended product, not only the current-phase output. | REF-02 §9 | S03, S08 |
| FX-11 | Section 17 risks derive from the actual activities, personnel, budget and schedule. | REF-02 §17 | S08, S10 |
| FX-12 | Section 4 duration and person-hours match Sections 13 and 16. | REF-02 §4 | S10 (script) |
