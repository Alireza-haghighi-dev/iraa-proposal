# 00_OPEN_ISSUES_REGISTER

| Field | Value |
|---|---|
| Document ID | 00_OPEN_ISSUES_REGISTER |
| Version | 5.0 |
| Status | APPROVED |
| Stage | S05 |
| Date | 2026-11-20 |
| Depends on | REF-01; REF-02; REF-03; S01_REQUIREMENTS_REGISTER; S02_RESEARCH_SYNTHESIS; S03_COMPARABLE_SYSTEMS_MATRIX; S03_PRIOR_ART_REGISTER; S04_SCOPE_OPTIONS; S04_ASSUMPTIONS_AND_STANDARDS; DEC-029; S05_EVALUATION_DESIGN; S05_DATA_AVAILABILITY_AND_SUBSTITUTES; S05_FEASIBILITY_AND_RISKS |

- **Type key:** **ODR** = OWNER DECISION REQUIRED; **OPEN** = information or evidence missing; **LOCAL** = local completion only, not researched in the working package
- **Blocking key:** The stage or gate that cannot close until the issue is resolved or an explicit assumption is approved

## A. Product scope and definition

| ID | Issue | Origin | Type | Blocks | Target | Status |
|---|---|---|---|---|---|---|
| ISS-001 | Development level of the current project: limited feasibility study / proof of concept versus a stronger prototype (laboratory, engineering, pilot or beta). Determines Sections 1, 5, 7, 8, 11 and 13 scope. S04: options A–D compared; Option B recommended. S04.1 audit: recommendation kept PROVISIONAL; Option B narrowed to essential functions plus owner-selectable options (S04_SCOPE_OPTIONS §4, §6). Decision still with the owner. DEC-028: narrowed Option B approved as the current planning scope; no live integration or production deployment committed. | RF-011, QA-003, F-01, F-05 | ODR | S04 gate | S04 | RESOLVED (DEC-028) for planning |
| ISS-004 | Scope of R1. S04.1 (DEC-029): comparing a new submission with stored submissions is the operative reading. Open point: whether the owner also wants the optional grouping or de-duplication of the stored collection (FN-04). Grouping is a PROPOSED addition, not a confirmed sponsor requirement. DEC-028: grouping excluded from the funded scope. | R1 | ODR | S04 gate (non-blocking for S05 if FN-04 is left out) | S04 | RESOLVED (DEC-028) |
| ISS-005 | Content of an "assessment". The source does not state the assessment criteria, categories, scores or decision outcomes that human assessors currently produce, nor which steps the assistant should support. S04: configurable template (AD-07) avoids guessing; fields still needed from the owner. | CTX-01, R3, Req. §4, §11 | OPEN | S04 gate | S04 | OPEN |
| ISS-003 | Sources of existing solution examples for R2 (corrected by DEC-029). Unresolved: which source categories count (sponsor records, external sources or both), whether any dataset is available to the project, permissions, and retrieval mechanisms. History: until S04.1 this issue concerned the existence of an "approved internal collection", wording now withdrawn from R2. S04: AS-02, rewritten in S04.1 (no source assumed; substitute data labelled). S05: R2 tests ET-03 to ET-05 run unchanged on any registered source; without a confirmed source R2 is tested on Track P only (DS-05). | R2, CLM-045 (CLM-012 superseded) | OPEN | S05 gate (the S04 gate proceeds on AS-02) | S04–S05 | OPEN |
| ISS-006 | External sources for R4: which patent and "solution example" sources are acceptable; access terms, licensing and cost. Jurisdiction-specific patent sources are deferred to owner-side completion. S04: AS-08; connector interface IF-03 is source-agnostic. S05: RQ-14 answered with three documented services (EPO OPS, PatentsView, Lens; CLM-051 to CLM-053); choice moved to ISS-040. | R4, DEC-009 | OPEN | S05 gate | S04–S05 | OPEN |
| ISS-007 | Language(s) of platform submissions and of any solution-example source. Not stated; must not be inferred. Activates or retires conditional RQ-07. S04: AS-06; language tag stored, no translation step (AD-12). S05: language decides between D-1 and the multilingual encoders D-2, D-3 (S05_EVALUATION_DESIGN §2). | C6, RQ-07 | ODR | S05 gate (the S04 gate proceeds on AS-06) | S04–S05 | OPEN |
| ISS-008 | Platform integration: whether the platform offers an API, database export or file export; read/write expectations for the assistant. The proposal must not assume an existing integration. S04: AS-03 (file export, read-only); adapter specified as IF-07. | Req. §4, §11 | OPEN | S05 gate (the S04 gate proceeds on AS-03) | S04–S05 | OPEN |
| ISS-009 | Data-handling restrictions: whether submission text may be processed by externally hosted AI services or must stay within sponsor-controlled infrastructure. S04: AS-04 (self-hosted default, AD-09); summaries off by default (AD-08). | C2 | ODR | S05 gate (the S04 gate proceeds on AS-04) | S04–S05 | OPEN |
| ISS-010 | Interpretation of C2: whether ISO/IEC 20000 and ISO/IEC 27001 mean alignment of the assistant's design, conformity with an existing certified management system, or certification; which controls are in scope. S04: standards scope verified (CLM-041, CLM-042); alignment-only interpretation proposed (CLM-043). | C2 | ODR | S05 gate (the S04 gate proceeds on CLM-043) | S04–S05 | OPEN |
| ISS-016 | Section 5 classification: project type, rationale (demand-driven versus documented need), maturity, execution stages, relationship to other projects. Depends on ISS-001. S04: provisional selection in proposal/DRAFT_SEC05_CLASSIFICATION. DEC-028: provisional classification adopted, subject to consistency review in S06/S08. | F-05, RF-011 | ODR | S04 gate (provisional), S06 (confirmed) | S04–S06 | PROVISIONALLY RESOLVED (DEC-028) |

## B. Data and evaluation

| ID | Issue | Origin | Type | Blocks | Target | Status |
|---|---|---|---|---|---|---|
| ISS-002 | Data availability for evaluation: whether historical submissions, past assessments and any solution-example source confirmed under ISS-003, or a sanitized sample of them, can be used in the project. If not, evaluation must rely on a constructed or public proxy collection, and the proposal must say so. S05: data requirements DR-01 to DR-06, sponsor request and outcomes O-1 to O-4 defined (S05_DATA_AVAILABILITY_AND_SUBSTITUTES); explicit assumption AS-09 recorded, which meets the S05 exit condition without resolving the issue. | QA-002, QA-004, QA-010 | ODR | S05 gate | S05 | OPEN (explicit assumption AS-09 recorded) |
| ISS-011 | Baseline performance: current review time per submission, backlog size, and any error or rework measure. No figures are supplied. Without them, speed and accuracy benefits remain hypotheses. S05: explicit assumption: no baseline is available, so the evaluation measures retrieval quality and workflow conformance only; speed and accuracy benefits stay hypotheses (S05_EVALUATION_DESIGN §10). | CTX-01, C5, QA-002 | OPEN | S05 gate (an explicit "no baseline" assumption is acceptable) | S05 | OPEN (explicit no-baseline assumption recorded) |
| ISS-012 | Ground truth: who can judge relevance or similarity for test cases, and how much assessor time is available for annotation. S05: judging protocol, pilot, calibration and effort formula defined (S05_EVALUATION_DESIGN §5); fallback AS-10. Assessor hours still needed from the owner. | QA-004, RQ-06 | OPEN | S05 gate | S05 | OPEN |
| ISS-023 | Scale: number of stored records, submission rate and typical text length. Needed for compute sizing and evaluation sample design. The source gives no figures. S05: sizing brackets PV-10 and memory arithmetic (S05_FEASIBILITY_AND_RISKS §1.2); actual figures still needed. | CTX-03, Req. §5 | OPEN | S05 gate (ranges acceptable) | S05 | OPEN (ranges recorded) |

## C. Planning and administration

| ID | Issue | Origin | Type | Blocks | Target | Status |
|---|---|---|---|---|---|---|
| ISS-013 | Provisional duration and effort envelope for work-package sizing (not a budget commitment). | QA-001, RF-010 | ODR | S06 start | Before S06 | OPEN |
| ISS-018 | Whether any training or learning activity belongs in Section 13. RF-012 states that earlier mandatory training/consulting charges were superseded; nothing is included automatically. | F-13, RF-012 | ODR | S06 gate | Before S06 | OPEN |
| ISS-014 | Authorization to run the isolated reviewer in S09 and S10b. | DEC-007 | ODR | S09 start | Before S09 | OPEN |
| ISS-015 | Final project title wording. The source uses "Intelligent Assistant for Requirements Review"; the project name is "Intelligent Requirements Assessment Assistant". The form title must also state maturity, execution stage and prototype type. Depends on ISS-001. | F-01, CTX-06 | ODR | S08 gate (draft), S10 (final) | S08–S10 | OPEN |
| ISS-017 | Person-hour convention. The form's Section 13 example (two full-time people, two weeks, 180 person-hours) implies 45 h per person-week; its Section 14 example (20 h/week ≈ 80 h/month) implies 4 weeks per month. The convention used for conversion must be confirmed. | F-13, F-14 | ODR | S10 | S10 (also note in S06 assumptions) | OPEN |
| ISS-019 | Beneficiary support mechanism (requirements statement §12): no option selected. | Req. §12 | ODR / LOCAL | S10 | S10 | OPEN |
| ISS-024 | Allowable cost categories, thresholds and cost units. Superseded earlier guidance must not be reused. | RF-009, RF-012 | LOCAL | S10 | S10 | OPEN |
| ISS-025 | Team composition, qualifications, monthly capacity, prior work evidence. | RF-008, QA-006, F-10, F-14 | LOCAL | S10 | S10 | OPEN |
| ISS-026 | Administrative fields: team name, team lead contact, completion date, attachments, sponsor and representative identity. | F-02, F-03, F-18, F-20, Req. §2, §3, §16 | LOCAL | — | Local completion | OPEN |

## D. Source control and formatting

| ID | Issue | Origin | Type | Blocks | Target | Status |
|---|---|---|---|---|---|---|
| ISS-020 | REVIEWER_FEEDBACK_EN_V1 is a secondary reconstruction; the original reviewer record and prior drafts have not been compared line by line. Reconcile if sanitized primary material becomes available. | Reviewer doc §5 | OPEN | None | Any | OPEN |
| ISS-021 | RF-001 (regular 12-point font, no arbitrary bold) and RF-003 (table layout) cannot be fully enforced in Markdown. Markdown drafts preserve schemas; typography is applied at local finalization. | RF-001, RF-003 | LOCAL | None | Local finalization | OPEN |
| ISS-022 | The requirements statement's illustration (§14) was omitted from the working copy and is described as conceptual. It must not be used as evidence of a working product. | Req. §14 | OPEN (informational) | None | S08 | OPEN |

## E. Issues raised in S02

| ID | Issue | Origin | Type | Blocks | Target | Status |
|---|---|---|---|---|---|---|
| ISS-028 | No public benchmark of organizational need/challenge submissions and no study of retrieval from need statements to patents were found. Every performance figure must come from the project's own evaluation or be labelled as a proxy result. S03 re-check: idea datasets exist (SRC-063, SRC-013) as possible proxies; no comparator publishes accuracy figures either (CLM-034). S05: addressed in design: Track S and Track P separation, baseline-relative targets and labelling rules (S05_EVALUATION_DESIGN §1; CLM-057). Stays open until results exist. | S02 matrix rows 4.3; synthesis §5; CLM-025; S03 matrix §3 | OPEN | S05 gate (evaluation design must address it) | S05 | ADDRESSED IN DESIGN; OPEN for results |
| ISS-029 | S02 research limitations awaiting independent verification: most sources checked at abstract or landing-page depth; mitigators of automation bias (SRC-023) unverified; CLM-025 is a negative search result. | S02_QC_REPORT §4–§5; DEC-022 | OPEN | S08 gate (Pass A full-text checks) and S09 (isolated review) | S08–S09 | OPEN |

## F. Issues raised in S03

| ID | Issue | Origin | Type | Blocks | Target | Status |
|---|---|---|---|---|---|---|
| ISS-030 | Final choice of Section 9 rows from the eight candidates in S03_SECTION9_COMPARISON (minimum three), including whether patent rows are used and how the form's outcome column is filled for them. | F-09, QA-005, S03_SECTION9_COMPARISON | ODR | S08 gate | S08 | OPEN |
| ISS-031 | RQ-12 was a web-search-based scan, not a professional patent search. EP 2765543 A1 and US 11,762,916 B1 rest on search-result extracts because their record pages failed to load (SRC-060, SRC-061). Re-check on the issuing office's register, or commission a professional search if the owner requires it. | RQ-12, CLM-039, S03_PRIOR_ART_REGISTER §4 | OPEN | S08 gate (only if patent rows are used) | S08 | OPEN |
| ISS-032 | Vendor capability statements reflect public pages read on 2026-11-20; one page (SRC-047) contains editorial placeholders. Re-check every Section 9 vendor statement shortly before submission. | QA-005, CLM-029 to CLM-035 | OPEN | S10 (final integration) | S08–S10 | OPEN |

## G. Issues raised in S04

| ID | Issue | Origin | Type | Blocks | Target | Status |
|---|---|---|---|---|---|---|
| ISS-033 | R4 requires sending query text derived from a submission to external search services. Whether assessor-approved query text may leave the controlled environment, and which services are acceptable, is not decided. DEC-028: no confidential submission text may go to external services without the required authorization; CP-1 applies until that authorization is defined. S05: R4 evaluation (ET-09) runs on public need statements, so it does not depend on this decision; Track S R4 testing does. | R4, ISS-009, DF-04 | ODR | S05 gate (R4 evaluation design) | S05 | OPEN |
| ISS-034 | Approval model under R3: whether one assessor's approval is sufficient or a second approver is required, which roles may approve, and which optional review controls (CP-1 to CP-4) the owner wants beyond the essential ones (CP-5, CP-6). DEC-028: CP-2 (mandatory labelling) and CP-3 (summaries) outside the essential funded scope; CP-5 and CP-6 kept. Single versus second approver and approving roles remain open. | R3, CP-5, AD-06; S04.1 | ODR | S06 gate | S05–S06 | OPEN (in part) |
| ISS-035 | Access permissions for the prototype: which roles need accounts and whether the sponsor's identity system must be used. | AS-05, IF-08 | ODR | S06 gate | S05–S06 | OPEN |
| ISS-036 | Retention and deletion of imported submissions and cached external results in the prototype environment, during and after the project. | AC-03, C2 | ODR | S06 gate | S05–S06 | OPEN |

## H. Issues raised in S04.1

| ID | Issue | Origin | Type | Blocks | Target | Status |
|---|---|---|---|---|---|---|
| ISS-037 | Boundary between R2 and R4. After the DEC-029 correction, R2 (existing solution examples for a submitted need) and R4 (external patents and solution examples) can overlap. Unresolved: whether R2 covers sponsor-held records only, external examples as well, or both, and how results are kept apart in the assessment record. The architecture keeps both behind one evidence-source interface with a source-type tag, so either answer fits without redesign. S05: R2 test design is identical for sponsor-held and external sources; source type is a reported condition (ET-03, ET-05). | R2, R4, DEC-029 | ODR | S05 gate (evaluation design for R2) | S05 | OPEN |


## I. Issues raised in S05 and at the S05 gate

| ID | Issue | Origin | Type | Blocks | Target | Status |
|---|---|---|---|---|---|---|
| ISS-038 | Substitute data: licence of CQADupStack on its original distribution and presence of post dates (DS-01, DS-02); structure, licence and language of the open innovation contest dataset (DS-03, record not reachable in S05); availability of the annotated idea-relationship data (DS-04); owner decision whether to build the constructed R2 substitute DS-05 and from which public source. | S05_DATA_AVAILABILITY_AND_SUBSTITUTES §4; RSK-12 | OPEN / ODR (DS-05) | Evaluation protocol freeze (E-0) | S06–S07 | OPEN |
| ISS-039 | Owner confirmation of the numeric planning values PV-01 to PV-11 (query counts, pool depth, agreement threshold, minimum difference, latency target, corpus brackets). | S05_EVALUATION_DESIGN §7; AS-12 | ODR | S06 effort sizing (non-blocking: AS-12 applies) | S06 | OPEN |
| ISS-040 | Choice of patent service(s) for R4: EPO OPS, PatentsView (key issuance uncertain, SRC-080), Lens (terms and plan not read) or PQAI (API terms not verified). | S05_FEASIBILITY_AND_RISKS §2; ISS-006; RSK-06 | ODR | S07 (tool selection) | S06–S07 | OPEN |
| ISS-041 | Training-data terms of the candidate models and the repository licence files of Pyserini and Faiss were not read; to be recorded before versions are fixed. | S05_FEASIBILITY_AND_RISKS §1.1; QA-010 | OPEN | S07 gate | S07 | OPEN |
| ISS-042 | Mandatory correction (DEC-031, item 1): MS-03 currently reads "not lower than unaided keyword queries", tested with the §6 superiority test. A non-significant difference is not evidence of non-inferiority. Correct by either a pre-declared non-inferiority test with a stated margin or a restated target that does not claim non-inferiority. | DEC-031; S05_EVALUATION_DESIGN §4 (ET-09), §8; DRAFT_SEC08_FEATURES MS-03 | OPEN (mandatory correction) | S07 evaluation-methodology freeze | S06–S07 | OPEN |
| ISS-043 | Mandatory correction (DEC-031, item 2): ET-01b and ET-04 define "nothing relevant" from the judged pool. A pool without a grade ≥ 2 item does not show that the corpus holds none. Correct the definitions, metric names (false-reassurance, false-match) and reporting so that pool-based absence is stated as such, and add a method for estimating corpus-level absence where it is claimed. | DEC-031; S05_EVALUATION_DESIGN §4; CLM-049 | OPEN (mandatory correction) | S07 evaluation-methodology freeze | S06–S07 | OPEN |
| ISS-044 | Mandatory correction (DEC-031, item 3): verify the licence of the original CQADupStack dataset on its own distribution, separately from the Apache 2.0 licence of any code repository or third-party mirror (SRC-079 is T3 and not sufficient). DS-01 and DS-02 stay unusable until this is done. Extends ISS-038. | DEC-031; S05_DATA_AVAILABILITY_AND_SUBSTITUTES §4; ISS-038 | OPEN (mandatory correction) | S07 evaluation-methodology freeze | S06–S07 | OPEN |
| ISS-045 | Mandatory correction (DEC-031, item 4): reassess whether MS-01 and MS-02 should require statistically supported outperformance of BM25 as a mandatory acceptance criterion, or whether BM25 should serve as a reported reference with acceptance defined otherwise (for example non-inferiority plus absolute floors). Record the reasoning and any owner decision. | DEC-031; S05_EVALUATION_DESIGN §1 rule 4, §8; CLM-057 | OPEN (mandatory correction; may need an owner decision) | S07 evaluation-methodology freeze | S06–S07 | OPEN |

## Closed issues

| ID | Issue | Resolution | Closed by |
|---|---|---|---|
| ISS-027 | The `S01-approved` tag could not be pushed (HTTP 403 from the session's git proxy). | Owner designated commit 2b5f83c65749a4c697782216026a6291a91aa2a1 as the immutable S01 baseline. | DEC-020 |
