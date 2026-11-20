# 00_OPEN_ISSUES_REGISTER

| Field | Value |
|---|---|
| Document ID | 00_OPEN_ISSUES_REGISTER |
| Version | 2.0 |
| Status | SUBMITTED FOR GATE |
| Stage | S02 |
| Date | 2026-11-20 |
| Depends on | REF-01; REF-02; REF-03; S01_REQUIREMENTS_REGISTER; S02_RESEARCH_SYNTHESIS |

- **Type key:** **ODR** = OWNER DECISION REQUIRED; **OPEN** = information or evidence missing; **LOCAL** = local completion only, not researched in the working package
- **Blocking key:** The stage or gate that cannot close until the issue is resolved or an explicit assumption is approved

## A. Product scope and definition

| ID | Issue | Origin | Type | Blocks | Target | Status |
|---|---|---|---|---|---|---|
| ISS-001 | Development level of the current project: limited feasibility study / proof of concept versus a stronger prototype (laboratory, engineering, pilot or beta). Determines Sections 1, 5, 7, 8, 11 and 13 scope. | RF-011, QA-003, F-01, F-05 | ODR | S04 gate | S04 | OPEN |
| ISS-004 | Scope of R1. "Similarities among requirements already stored" can mean (a) comparing a new submission against stored ones, (b) grouping or de-duplicating the stored collection, or both. | R1 | ODR | S04 gate (non-blocking for S02, which covers both) | S04 | OPEN |
| ISS-005 | Content of an "assessment". The source does not state the assessment criteria, categories, scores or decision outcomes that human assessors currently produce, nor which steps the assistant should support. | CTX-01, R3, Req. §4, §11 | OPEN | S04 gate | S04 | OPEN |
| ISS-003 | Existence and nature of the "approved internal collection" named in R2. REF-01 does not establish that it exists as a populated, machine-readable dataset. Unknown: whether it exists in that form, its content type, format, size, approval owner and access method. | R2, CLM-012 | OPEN | S04 gate | S04 | OPEN |
| ISS-006 | External sources for R4: which patent and "solution example" sources are acceptable; access terms, licensing and cost. Jurisdiction-specific patent sources are deferred to owner-side completion. | R4, DEC-009 | OPEN | S05 gate | S04–S05 | OPEN |
| ISS-007 | Language(s) of platform submissions and of the internal collection. Not stated; must not be inferred. Activates or retires conditional RQ-07. | C6, RQ-07 | ODR | S04 gate | S04 | OPEN |
| ISS-008 | Platform integration: whether the platform offers an API, database export or file export; read/write expectations for the assistant. The proposal must not assume an existing integration. | Req. §4, §11 | OPEN | S04 gate | S04 | OPEN |
| ISS-009 | Data-handling restrictions: whether submission text may be processed by externally hosted AI services or must stay within sponsor-controlled infrastructure. | C2 | ODR | S04 gate | S04 | OPEN |
| ISS-010 | Interpretation of C2: whether ISO/IEC 20000 and ISO/IEC 27001 mean alignment of the assistant's design, conformity with an existing certified management system, or certification; which controls are in scope. | C2 | ODR | S04 gate | S04 | OPEN |
| ISS-016 | Section 5 classification: project type, rationale (demand-driven versus documented need), maturity, execution stages, relationship to other projects. Depends on ISS-001. | F-05, RF-011 | ODR | S04 gate (provisional), S06 (confirmed) | S04–S06 | OPEN |

## B. Data and evaluation

| ID | Issue | Origin | Type | Blocks | Target | Status |
|---|---|---|---|---|---|---|
| ISS-002 | Data availability for evaluation: whether historical submissions, past assessments and the internal collection (if it exists, ISS-003), or a sanitized sample of them, can be used in the project. If not, evaluation must rely on a constructed or public proxy collection, and the proposal must say so. | QA-002, QA-004, QA-010 | ODR | S05 gate | S05 | OPEN |
| ISS-011 | Baseline performance: current review time per submission, backlog size, and any error or rework measure. No figures are supplied. Without them, speed and accuracy benefits remain hypotheses. | CTX-01, C5, QA-002 | OPEN | S05 gate (an explicit "no baseline" assumption is acceptable) | S05 | OPEN |
| ISS-012 | Ground truth: who can judge relevance or similarity for test cases, and how much assessor time is available for annotation. | QA-004, RQ-06 | OPEN | S05 gate | S05 | OPEN |
| ISS-023 | Scale: number of stored records, submission rate and typical text length. Needed for compute sizing and evaluation sample design. The source gives no figures. | CTX-03, Req. §5 | OPEN | S05 gate (ranges acceptable) | S05 | OPEN |

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
| ISS-028 | No public benchmark of organizational need/challenge submissions and no study of retrieval from need statements to patents were found. Every performance figure must come from the project's own evaluation or be labelled as a proxy result. | S02 matrix rows 4.3; synthesis §5; CLM-025 | OPEN | S05 gate (evaluation design must address it) | S05 | OPEN |

## Closed issues

| ID | Issue | Resolution | Closed by |
|---|---|---|---|
| ISS-027 | The `S01-approved` tag could not be pushed (HTTP 403 from the session's git proxy). | Owner designated commit 2b5f83c65749a4c697782216026a6291a91aa2a1 as the immutable S01 baseline. | DEC-020 |
