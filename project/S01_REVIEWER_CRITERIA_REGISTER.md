# S01_REVIEWER_CRITERIA_REGISTER

| Field | Value |
|---|---|
| Document ID | S01_REVIEWER_CRITERIA_REGISTER |
| Version | 8.0 |
| Status | APPROVED |
| Stage | S08 |
| Date | 2026-11-21 |
| Depends on | REF-03; DEC-011; S02 deliverables; S03 deliverables; S04 deliverables; S05 deliverables; S06 deliverables; S07 deliverables; S08 deliverables |

- **Source:** REF-03 (REVIEWER_FEEDBACK_EN_V1), a consolidated secondary reconstruction (DEC-011)
- **Evidence classes:** **RF** = reported reviewer criterion; **QA** = additional quality observation from the owner's handoff, not attributed to the proposal reviewer
- **Status labels:** `ADDRESSED` · `SCHEDULED` · `JUSTIFIED EXCEPTION` · `OPEN` (REF-03 §4.2). Each status cites an artifact.

The "Criterion (paraphrased)" column summarizes REF-03 in project terms. It is not reviewer wording.

## 1. Reported reviewer criteria

| ID | Area | Criterion (paraphrased) | Sections | Responsible stage(s) | S01 action | Status at S01 gate | Evidence / artifact |
|---|---|---|---|---|---|---|---|
| RF-001 | Formatting | Keep the official form's design; inserted text in regular-weight 12-point font; no arbitrary bold. | All | Local finalization | Rule recorded; Markdown limitation logged | SCHEDULED (master has no bold or decorative emphasis, scripted; typography at local finalization) | 03_STYLE_GUIDE §3; ISS-021; proposal/IRAA_PROPOSAL_EN_MASTER; S08_EDITORIAL_LOG Pass E; DEF-008 |
| RF-002 | Decoration and lists | No decorative dots, checkmarks or paragraph-opening bullets unless the form uses them. | All | S07–S08, local finalization | Rule added to style guide and gate. S07: Section 12 draft written as prose paragraphs with one tool table; no decorative bullets (scripted check) | ADDRESSED in Markdown (no paragraph-opening bullets in sections 1–20, scripted); native-template check at local finalization | 03_STYLE_GUIDE §3; 00_STAGE_GATE_PROTOCOL §5; proposal/DRAFT_SEC12_METHODOLOGY; proposal/IRAA_PROPOSAL_EN_MASTER; S08_EDITORIAL_LOG Pass E |
| RF-003 | Table integrity | Preserve table layouts, column labels, order and schema. | All tables | S08, local finalization | Table schemas recorded per section | ADDRESSED in Markdown (REF-02 header rows verbatim, scripted); native template not inspected, PENDING (ISS-021) | S01_REQUIREMENTS_REGISTER §4 (F-05 to F-20); 00_PROJECT_RULES §8; proposal/IRAA_PROPOSAL_EN_MASTER; S08_EDITORIAL_LOG Pass E; DEF-008 |
| RF-004 | Prose quality and technical ownership | Concise, specific, defensible writing the team can explain; no inflated or generic exposition. | All | Every stage; intensive S08–S09 | Style guide, pattern list and writing gate created and applied to S01 files | ADDRESSED for S08 (Pass C); S09 isolated review pending | 03_STYLE_GUIDE; 00_STAGE_GATE_PROTOCOL §5; S01_QC_REPORT §4; S02_QC_REPORT §4; proposal/IRAA_PROPOSAL_EN_MASTER; S08_EDITORIAL_LOG Pass E |
| RF-005 | Continuity roadmap | Current project is row 1 of Section 11; no preliminary row; later rows clearly prospective. | 11 | S04, S08 | Rule recorded; S04 draft has the current project as row 1 and three prospective rows | ADDRESSED (durations S10) | proposal/DRAFT_SEC11_CONTINUITY; 00_PROJECT_RULES §8; F-11; proposal/IRAA_PROPOSAL_EN_MASTER; S08_EDITORIAL_LOG Pass E Section 11 |
| RF-006 | Detailed methodology | Section 12 reproduces Section 13's numbered activities and explains each with concrete methods, inputs, tools, procedures, evaluation and outputs. | 12, 13 | S06–S07 | Cross-section rule FX-01 recorded. S06: WP1–WP7 identifiers and titles frozen for verbatim reuse in Section 12. S07: Section 12 working draft with one subsection per activity, numbers and titles verbatim, each covering procedures, inputs, methods and tools with status, validation, deliverables and acceptance, risks and fallbacks, and traceability | ADDRESSED (master Section 12 headings identical to Section 13 and 16, scripted; S09 review) | proposal/DRAFT_SEC12_METHODOLOGY; stages/S07/S07_WP_METHOD_TRACEABILITY §1; FX-01; proposal/IRAA_PROPOSAL_EN_MASTER; S08_EDITORIAL_LOG Pass E |
| RF-007 | Activity-plan structure | About six or seven coherent main activities, each with key tasks, tangible deliverable and defensible effort. | 13 | S06 | Gate criterion recorded; distinction from development stages fixed. S06: seven work packages, each with tasks, deliverables, acceptance evidence, dependencies and provisional person-hours with stated assumptions | ADDRESSED (effort provisional while ISS-013 is open) | S06_WORK_PACKAGES; S06_DELIVERABLES_AND_ACCEPTANCE; S06_DEPENDENCIES_AND_EFFORT; proposal/DRAFT_SEC13_ACTIVITIES |
| RF-008 | Team participation | No invented availability, assignments or shares; reconcile participation with total work. | 14, 13, 16 | S10 only | Deferred; local issue logged | SCHEDULED | ISS-025; FX-05 |
| RF-009 | Budget specificity | Itemized, defensible cost table derived from approved scope; reconciles to Section 16. | 15 | S10 only | Deferred; local issue logged | SCHEDULED | ISS-024; FX-03 |
| RF-010 | Gantt sequencing | Derive schedule and weights from final activities, dependencies, availability and costs; no early highlighting. | 16; 13–15 | S10 only | Deferred; rules recorded | SCHEDULED | FX-02, FX-04, FX-08 |
| RF-011 | Track versus maturity | Do not confuse funding track with technical maturity; reconcile title, prototype type, deliverables and classification. | 1, 5, 7, 8, 11, 13 | S04–S06 | S04: options A–D compared; Option B recommended; Section 5 provisionally selected; title pattern noted. S04.1: recommendation audited and narrowed; track-versus-maturity and four further distinctions made explicit; drafts marked provisional. S06: Section 13 activities limited to design, build and test of the laboratory prototype (DEC-028); live deployment and retraining placed in Section 11 | ADDRESSED (Sections 1, 5, 7, 11, 13 consistent in the master; ISS-016 provisional classification kept) | S04_SCOPE_OPTIONS §6; proposal/DRAFT_SEC05_CLASSIFICATION; proposal/DRAFT_SEC13_ACTIVITIES; ISS-016, FX-09; proposal/IRAA_PROPOSAL_EN_MASTER; S08_EDITORIAL_LOG Pass E |
| RF-012 | Superseded funding guidance | Former budget ceiling and mandatory training/consulting charges do not apply automatically; current rules need owner confirmation. | 13, 15, 16 | S10 only (S06 for training activity) | Issues logged; no cost lines carried forward. S06: no training activity and no carried-forward cost line in Section 13 | ADDRESSED for S08 (no default consulting or training line; costs S10) | ISS-018, ISS-024; proposal/DRAFT_SEC13_ACTIVITIES; proposal/IRAA_PROPOSAL_EN_MASTER; S08_EDITORIAL_LOG Pass E Section 15 |

## 2. Additional quality observations

| ID | Observation (paraphrased) | Sections | Responsible stage(s) | S01 action | Status at S01 gate | Evidence / artifact |
|---|---|---|---|---|---|---|
| QA-001 | Earlier drafts disagree on work-package count and effort; their figures are not commitments. | 4, 13–16 | S06, S10 | No historical figures used; rule added. S06: all person-hours derived from task-level estimates and stated assumptions EH-01 to EH-10; none taken from earlier drafts | ADDRESSED (S06 figures; S10 recomputes) | 03_STYLE_GUIDE §2.8; S06_DEPENDENCIES_AND_EFFORT §1, §3 |
| QA-002 | Speed and accuracy benefits lack a measured baseline. | 6, 7, 8 | S05, S08 | Benefits registered as hypotheses; S05: evaluation measures retrieval quality and workflow conformance only, with an explicit no-baseline assumption for speed and accuracy (S05_EVALUATION_DESIGN §10) | ADDRESSED (benefits stated as untested expectations in Sections 6, 12 and 19) | CLM-006; ISS-011; S05_EVALUATION_DESIGN §1, §10; CLM-057; proposal/IRAA_PROPOSAL_EN_MASTER; S08_EDITORIAL_LOG Pass E |
| QA-003 | Delivered-assistant wording conflicted with feasibility/PoC scope. | 1, 5, 7, 8, 11 | S04 | S04: current-phase deliverables and future stages separated; drafts avoid delivered-assistant wording | OPEN (owner decision required on ISS-001) | S04_SCOPE_OPTIONS; S04_ARCHITECTURE §2; proposal/DRAFT_SEC07_OBJECTIVES |
| QA-004 | Measurable specifications, test criteria and data assumptions incomplete. | 8, 12, 13 | S05–S07 | S05: metric, test condition and target for every active MS row; data assumptions AS-09 to AS-12; data requirements and outcomes; MS-10 added. S07: every Section 8 row mapped to a verification step; MS-01 to MS-03 corrected (ISS-042, ISS-043, ISS-045) | ADDRESSED (S05 design; S07 verification steps and corrections) | proposal/DRAFT_SEC08_FEATURES v0.4; S05_EVALUATION_DESIGN v2.0 §4, §6, §8; stages/S07/S07_WP_METHOD_TRACEABILITY §3 |
| QA-005 | Comparators and claimed advantages lack source-specific verification. | 9 | S03, S08 | Eight Section 9 candidates verified from first-party or patent-office sources; each capability cell sourced or marked ND; vendor statements labelled; marketing figures excluded; no superiority claim | ADDRESSED with conditions (vendor statements only, no superiority claim; row selection ISS-030; vendor re-read ISS-032) | S03_COMPARABLE_SYSTEMS_MATRIX; S03_SECTION9_COMPARISON; CLM-001 to CLM-004, CLM-029 to CLM-040; ISS-030, ISS-032; proposal/IRAA_PROPOSAL_EN_MASTER; S08_EDITORIAL_LOG Pass E Section 9 |
| QA-006 | Team prior work undocumented; capacity unknown. | 10, 14 | S10 | Deferred; local issue logged | SCHEDULED | ISS-025 |
| QA-007 | Activity table lacks adequate tasks and deliverables. | 12, 13 | S06–S07 | Gate criteria require tasks, deliverables, acceptance evidence. S06: every activity has key tasks, named deliverables and acceptance evidence. S07: Section 12 expands every activity into concrete technical tasks with acceptance evidence | ADDRESSED (Sections 12 and 13 drafts) | S06_WORK_PACKAGES §2; S06_DELIVERABLES_AND_ACCEPTANCE §1; proposal/DRAFT_SEC12_METHODOLOGY |
| QA-008 | Gantt markings and costs populated before assumptions agreed. | 15, 16 | S10 | No schedule or cost content before S10 | SCHEDULED | DEC-001; RF-010 entry |
| QA-009 | Risks, dates, attachments and administrative fields incomplete. | 17–20 | S08, S10 | Risk split recorded; local fields logged | ADDRESSED for technical and data risks (Section 17); timeline, financial and administrative fields S10 | F-17; ISS-026; proposal/IRAA_PROPOSAL_EN_MASTER; S08_EDITORIAL_LOG Pass E Section 17 |
| QA-010 | Earlier comparative research and technology choices are leads, not verified evidence. | 8, 9, 12 | S02–S05 | No earlier technology choices inherited; S05: licences and input limits of candidate components verified at documentation depth; versions and training-data terms left for S07 (ISS-041). S07: tool and version register; Pyserini release and licence and Faiss licence verified; model-card training-data statements read; remaining terms at T1.5 pinning (ISS-041) | ADDRESSED for S07 scope (pinned versions and training-data terms scheduled at T1.5 and in D7.3) | stages/S07/S07_TOOL_AND_VERSION_REGISTER; SRC-078; SRC-086; CLM-063; ISS-041 |

## 3. Binding workflow implications from REF-03 §4 and where they are enforced

| REF-03 §4 item | Enforced by |
|---|---|
| 1. Create RF entries in S01 and keep RF/QA distinct | This register; DEC-011 |
| 2. Status labels with artifact references at each gate | 00_STAGE_GATE_PROTOCOL §4 |
| 3. Design Section 13 first, then Section 12 one-to-one | S06 before S07; FX-01 |
| 4. No identities, locations, local market claims, financial units or administrative details | DEC-009; 00_PROJECT_RULES §3 |
| 5. Sponsor form governs formatting and schemas | RF-001, RF-003; ISS-021 |
| 6. Scope question recorded as OWNER DECISION REQUIRED | ISS-001 |
| 7. Development stages are not work packages | DEC-012; 03_STYLE_GUIDE §6 |
| 8. Budget thresholds and eligibility are local decisions | ISS-024 |
| 9. Human authority mandatory; no implied deployment, measured performance or certification | R3; C2; C5; 03_STYLE_GUIDE §2.3 |
