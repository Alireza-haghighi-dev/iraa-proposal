# S06_WORK_PACKAGES

| Field | Value |
|---|---|
| Document ID | S06_WORK_PACKAGES |
| Version | 1.0 |
| Status | SUBMITTED FOR GATE |
| Stage | S06 |
| Date | 2026-11-21 |
| Depends on | DEC-012; DEC-028; DEC-031; S04_ARCHITECTURE; S04_SCOPE_OPTIONS; S04_ASSUMPTIONS_AND_STANDARDS; S05_EVALUATION_DESIGN; S05_FEASIBILITY_AND_RISKS; S05_DATA_AVAILABILITY_AND_SUBSTITUTES; DRAFT_SEC07_OBJECTIVES; DRAFT_SEC08_FEATURES |

- **Status of content:** every work package, task and deliverable is PROPOSED. Nothing has been built or tested. Person-hours are in `S06_DEPENDENCIES_AND_EFFORT` and are provisional (ISS-013 open).
- **Scope basis:** narrowed Option B, laboratory prototype, technology development, design + build + test (DEC-028). Funded functions: FN-01 to FN-03, FN-05, FN-06, FN-08, FN-09 with CP-5 and CP-6, FN-10 (logging only), FN-11, FN-12, and CP-1 while external disclosure is not authorized.
- **Frozen at the S06 gate:** WP identifiers and titles in §1. S07 (Section 12) and S10 (Sections 14 to 16) reuse them verbatim (RF-006, FX-01, FX-02). Tasks Tn.m and deliverables Dn.m may be refined in S07 without renumbering the work packages.
- **Not work packages:** the development stages S01–S10 of this proposal workflow (DEC-012).

## 1. Work-package register (frozen identifiers and titles)

| WP | Title | Objective | Type of work |
|---|---|---|---|
| WP1 | Prototype design specification and data-protection baseline | Fix the field map, assessment template, record state model, interfaces and data-handling rules that the build work packages implement, and assess the information security risks of the prototype's data flows | Design |
| WP2 | Evaluation protocol, test collections and evaluation harness | Produce the frozen evaluation protocol and judging guide, the versioned test collections for each data track, and the harness that computes the S05 metrics and significance tests | Design and build (evaluation tooling) |
| WP3 | Ingestion and retrieval for similar submissions and solution examples | Build the import, normalization, indexing and retrieval components that rank stored submissions for a new submission (R1) and items from registered solution-example sources for a submitted need (R2), with evidence passages | Build |
| WP4 | External prior-art retrieval with query approval | Build the connector framework, one patent-service connector, query construction and the approval of the exact query text before it leaves the controlled environment (R4) | Build |
| WP5 | Assessment record, review interface and approval controls | Build the assessment record, the evidence-first review screens, access control, audit log, report export and decision log, with the essential approval controls CP-5 and CP-6 (R3) | Build |
| WP6 | Prototype integration and evaluation | Integrate WP3 to WP5 into one release on the reference environment, carry out relevance judging, the single test run, the workflow and timing tests, and report results by data track | Integration and test |
| WP7 | Technical documentation and handover | Deliver the as-built design, deployment instructions, source code, component licence inventory, the updated security risk assessment and a handover demonstration | Documentation and transfer |

Seven work packages, as the reviewer criterion asks for about six or seven (RF-007). Build is split by requirement because R1/R2, R4 and R3 rest on different components (AC-01 to AC-05; AC-07; AC-09 to AC-13) and can be accepted separately. Evaluation tooling (WP2) is separate from the evaluation itself (WP6) because the protocol must be frozen and the harness checked (FT-01) before any test pool is judged (`S05_EVALUATION_DESIGN` §1, rule 2).

## 2. Tasks per work package

Effort per task is in `S06_DEPENDENCIES_AND_EFFORT` §3. "Conditional" tasks run only if the stated condition holds; they are not in the planning figure unless noted.

### WP1 — Prototype design specification and data-protection baseline

| Task | Content | Inputs | Output |
|---|---|---|---|
| T1.1 | Field map and import-file specification (IF-01) from the sponsor export schema if released, otherwise from the substitute schema; configurable assessment template (AD-07) with the fields the owner supplies (ISS-005), or a placeholder template if none are supplied | ISS-002, ISS-005, ISS-008, AS-03 | D1.1 §field map, §template |
| T1.2 | Record state model: states Draft, In review, Submitted, Approved, Returned; events and roles; CP-5, CP-6 and CP-1 rules; optional second approver as a setting (AD-06, ISS-034). Written as an executable transition table so that ET-06 can generate its test cases from it | S04_ARCHITECTURE §4 | D1.1 §state model |
| T1.3 | Interface specifications IF-02 to IF-06 and IF-08; IF-07 platform adapter specified, not implemented (C1, AD-03) | S04_DATA_FLOWS_AND_INTERFACES | D1.1 §interfaces |
| T1.4 | Information security risk assessment of data flows DF-01 to DF-08 and their trust boundaries; role and permission matrix (AS-05, ISS-035); retention and deletion procedure for imported data and cached external results (ISS-036) | S04_ASSUMPTIONS_AND_STANDARDS §3 | D1.2, D1.3 |
| T1.5 | Reference environment specification for evaluation and timing (AS-11): hardware class, operating system, runtime; cost is settled in S10 | S05_FEASIBILITY_AND_RISKS §1.2 | D1.1 §environment |
| T1.6 | Design review against the essential function set; check that every FN in scope maps to a component, an interface and a test | Traceability Part H | Review record in D1.1 |

### WP2 — Evaluation protocol, test collections and evaluation harness

| Task | Content | Inputs | Output |
|---|---|---|---|
| T2.1 | Licence and terms checks of substitute candidates on their original distributions (DS-01 to DS-04; ISS-038, ISS-044); selection record; a candidate that fails is dropped | S05_DATA_AVAILABILITY_AND_SUBSTITUTES §4 | D2.2 §licence record |
| T2.2 | Evaluation protocol (E-0) and judging guide with worked examples: metrics, grade scales, configurations, significance procedure, multiple-comparison correction, targets; incorporates the corrections for ISS-042 to ISS-045 as settled in S07; PV values as confirmed (ISS-039) | S05_EVALUATION_DESIGN; S07 Section 12 | D2.1 |
| T2.3 | Test collections per track (E-2): time-ordered development and test splits, query selection, versioning with source, licence note, track label and split dates | DR-01 to DR-03; outcome O-1 to O-4 | D2.2 |
| T2.4 | Conditional (owner decision, ISS-038): construct the R2 substitute DS-05, with need statements written by project judges and a public solution-description source with permissive terms. Included in the planning figure because without it MS-02 cannot be tested under outcome O-4 | ISS-003, ISS-038 | D2.2 §DS-05 |
| T2.5 | Evaluation harness AC-14 (E-1, FN-12): run-file handling, metric scripts (nDCG@10, P@5, Recall@20, MRR, bpref, judged@10, success@10), paired randomization test and bootstrap interval, per-track reporting that never pools tracks | S05_EVALUATION_DESIGN §4, §6 | D2.3 |
| T2.6 | FT-01 / ET-02: reproduce a published BM25 run on DS-02 through the harness (conditional on the DS-02 licence check passing; otherwise another benchmark with published reference runs and a permissive licence) | FT-01 | D2.3 §reproduction note |

### WP3 — Ingestion and retrieval for similar submissions and solution examples

| Task | Content | Inputs | Output |
|---|---|---|---|
| T3.1 | Ingestion adapter AC-01 (FN-01): parse IF-01 files, validate against the field map, import report with rejected rows; source registry in AC-03 with source type, availability status and permission note | D1.1 | D3.1 |
| T3.2 | Normalization pipeline AC-02 (FN-02): cleaning, exact-copy hashing, shingle fingerprints (used by B-FP), language tag, passage segmentation with truncation counts (RSK-10) | D1.1 | D3.1 |
| T3.3 | Index layer AC-04: one lexical and one vector index per registered corpus, index version stored (AD-01, AD-11) | D3.1 | D3.2 |
| T3.4 | Retrieval service AC-05 behind IF-02 (FN-03, FN-05): configurations B-REC, B-LEX, B-FP, D-1 to D-3, H-RRF, H-CC and optional RR; maximum-passage scoring; evidence span shown per candidate (AD-05) | S05_EVALUATION_DESIGN §2 | D3.2 |
| T3.5 | Display thresholds: R1 display threshold (ET-01b) and the R2 "no example above threshold" signal (ET-04), both set on the development split only | ET-01b, ET-04 | D3.2 |
| T3.6 | FT-02: encode corpora at each confirmed PV-10 size with D-1 to D-3; time encoding, search and re-ranking on the reference environment; restrict the ET-10 configuration set to those that can meet PV-09 | D1.1 §environment | D3.3 |
| T3.7 | Unit and integration tests of AC-01 to AC-05 | — | Test suite in D3.2 |
| T3.8 | Conditional (sponsor export released): FT-04, parse the sponsor export against the field map | ISS-002 | Import report in D3.3 |

### WP4 — External prior-art retrieval with query approval

| Task | Content | Inputs | Output |
|---|---|---|---|
| T4.1 | Connector framework AC-07 behind IF-03 (FN-06): plug-in contract, rate-limit handling, cache, provenance per result (source, retrieval date, terms note) (AD-04) | D1.1 | D4.1 |
| T4.2 | Connector for the patent service chosen under ISS-040; FT-03 smoke test with public test queries | ISS-040; S05_FEASIBILITY_AND_RISKS §2 | D4.1, D4.2 |
| T4.3 | Query construction (formulation Q-B) from submission text; assessor editing and approval of the exact text (CP-1) through IF-04; exact sent text logged to AC-13 | D1.1 §state model | D4.1 |
| T4.4 | Fallback under AS-08: manual entry of assessor-run search results with the same provenance fields | AS-08, RSK-06 | D4.1 |
| T4.5 | Tests: connector contract tests, CP-1 bypass attempts, provenance completeness (instrumentation used by ET-08) | — | Test suite in D4.1 |
| T4.6 | Optional: a second patent-service connector, if ISS-040 selects more than one | ISS-040 | D4.1 |

### WP5 — Assessment record, review interface and approval controls

| Task | Content | Inputs | Output |
|---|---|---|---|
| T5.1 | Assessment record service AC-09 (FN-08, FN-09): schema, the T1.2 state machine, versioning, CP-5 and CP-6 enforcement, optional second approver; the only component that changes record state | D1.1 | D5.1 |
| T5.2 | Access control AC-12 (FN-11) with project-managed accounts and the roles assessor, administrator and evaluator (AS-05); permission check on every IF-04 call | D1.2 role matrix | D5.1 |
| T5.3 | Append-only audit and provenance log AC-13: record events, approvals, external queries, component versions | — | D5.1 |
| T5.4 | Review interface AC-10: evidence-first candidate lists for R1, R2 and R4 (passage before score, AD-05), source attribution per item (MS-10), CP-1 query-approval screen, assessment template form, approval and return actions | D1.1 | D5.2 |
| T5.5 | Report generator AC-11 (IF-05) and decision-log export (FN-10, IF-06); no retraining (AD-10) | — | D5.1 |
| T5.6 | Model-based and randomized test suite for ET-06 and ET-07, generated from the T1.2 transition table | D1.1 §state model | D5.3 |

### WP6 — Prototype integration and evaluation

| Task | Content | Inputs | Output |
|---|---|---|---|
| T6.1 | Integrate WP3, WP4 and WP5 into one versioned release on the reference environment; deployment scripts; release checklist | D3.2, D4.1, D5.1, D5.2 | D6.1 |
| T6.2 | Pilot (E-3, FT-05) analysis: agreement and time per judgment, one guide revision, sample-size check against PV-07, absolute floors PV-11 fixed before the test run | D2.1, D2.2 | D6.2 |
| T6.3 | Relevance judging of development and test pools for ET-01, ET-03 and ET-09, with double judging of PV-04 and third-judge adjudication (ET-11). Sized by the formula in `S06_DEPENDENCIES_AND_EFFORT` §4 | D2.1, D2.2, D6.1 | Judgment files in D6.3 |
| T6.4 | Tuning on the development split and configuration selection record (E-4) | D6.2 | D6.2 §selection |
| T6.5 | Single test run (E-5); workflow tests ET-06 to ET-08; attribution check ET-05; timing ET-10 at each confirmed corpus size | D6.1, D5.3 | Run files and test logs in D6.3 |
| T6.6 | Analysis and evaluation report by track (E-6): per-query distributions, intervals, p-values, agreement, sensitivity repetition; "no supported difference" where the interval includes zero | D6.3 | D6.4 |
| T6.7 | Conditional (assessor time available, ISS-012): structured walk-through of the review screens with assessors; qualitative findings only | D6.1 | Walk-through note in D6.4 |

### WP7 — Technical documentation and handover

| Task | Content | Inputs | Output |
|---|---|---|---|
| T7.1 | As-built design specification (update of D1.1) and deployment and operation instructions for the reference environment | D1.1, D6.1 | D7.1 |
| T7.2 | Update of the information security risk assessment to the built prototype; execution of the retention and deletion procedure at project close (ISS-036) | D1.2, D1.3 | D7.2 |
| T7.3 | Source code and configuration package; inventory of third-party components and models with licence and training-data terms (ISS-041) | D6.1 | D7.3 |
| T7.4 | Handover demonstration on the reference environment and acceptance record | D7.1 to D7.3, D6.4 | D7.4 |
| T7.5 | Continuity notes for Section 11: decision-log format, IF-07 specification and the limits found in evaluation | D1.1, D6.4 | D7.1 §continuity |

## 3. Essential funded work versus optional and future development

| Item | Classification | Where it would go | Basis |
|---|---|---|---|
| WP1 to WP7 tasks not marked conditional or optional | Essential funded work | Section 13 | DEC-028 essential set; R1–R4 |
| T2.4 DS-05 construction | Conditional, in planning figure | WP2 | ISS-038 owner decision; needed for MS-02 under O-4 |
| T3.8 FT-04, T6.7 walk-through | Conditional, not in planning figure | WP3, WP6 | ISS-002, ISS-012 |
| T4.6 second patent connector | Optional, not in planning figure | WP4 | ISS-040 |
| FN-04 grouping with CP-4; FN-07 summaries with CP-3; mandatory CP-2 labelling (MS-07, MS-09) | Excluded from funded scope | Owner decision needed to add (RSK-14) | DEC-028 |
| IF-07 implementation, write-back, sponsor identity federation (IF-08 federated) | Future | Section 11 row 2 | AD-03, AS-05 |
| Learning from logged decisions; automatic retraining | Future | Section 11 row 3 | AD-10, C3 |
| Live-platform deployment, production operation | Future | Section 11 | DEC-028 |
| Timed assessor task study (speed, workload, decision accuracy) | Future | Section 11 | S05_EVALUATION_DESIGN §10 |
| Training or learning activity | Not included | Inserted mid-plan only if required (ISS-018) | RF-012; REF-02 §13 |

## 4. Traceability per work package

| WP | Requirements | Functions | Components | Interfaces / checkpoints | S05 tests and feasibility tests | Section 8 rows | Risks scheduled |
|---|---|---|---|---|---|---|---|
| WP1 | R1–R4, C1, C2 | All essential FN (specification) | AC-01 to AC-14 (specification) | IF-01 to IF-08; CP-1, CP-5, CP-6 | ET-06 model input | Features 1, 7, 8, 9; MS-04 (model) | RSK-01, RSK-14 |
| WP2 | R1, R2, R4 (evaluation) | FN-12 | AC-14 | — | ET-01 to ET-04, ET-09, ET-11 (protocol); ET-02; FT-01 | MS-01, MS-02, MS-03 (protocol) | RSK-02, RSK-08, RSK-09, RSK-12, RSK-13 |
| WP3 | R1, R2 | FN-01, FN-02, FN-03, FN-05 | AC-01 to AC-05 | IF-01, IF-02 | ET-01, ET-01b, ET-03, ET-04, ET-05, ET-10 (system under test); FT-02, FT-04 | Features 1, 2, 4; MS-01, MS-02, MS-08, MS-10 | RSK-05, RSK-10, RSK-11 |
| WP4 | R4 | FN-06 | AC-07, AC-03 | IF-03; CP-1 | ET-08, ET-09 (system under test); FT-03 | Feature 5; MS-03, MS-05, MS-10 | RSK-06, RSK-07 |
| WP5 | R3; display for R1, R2, R4 | FN-08, FN-09, FN-10, FN-11 | AC-09 to AC-13 | IF-04, IF-05, IF-06, IF-08; CP-5, CP-6; CP-1 screen | ET-06, ET-07 (suite) | Features 7, 8; MS-04, MS-06, MS-10 | RSK-14 |
| WP6 | R1–R4 (verification) | FN-12 and all integrated FN | AC-14 and integrated AC | All in release | ET-01 to ET-11 (execution); FT-05 | MS-01 to MS-06, MS-08, MS-10 | RSK-03, RSK-04, RSK-08, RSK-13 |
| WP7 | C1, C2 | — | All (documentation) | IF-07 specification handover | — | Feature 9; MS-06 | RSK-12 (licence inventory) |

## 5. Section 7 objectives and completion deliverables mapped to work packages

| Section 7 draft element | Work packages |
|---|---|
| First objective: similarity function (R1) | WP3, evaluated in WP6 |
| Second objective: solution-example identification (R2) | WP3; WP2 (T2.4 substitute); evaluated in WP6 |
| Third objective: external prior-art retrieval (R4) | WP4, evaluated in WP6 |
| Fourth objective: review and approval workflow (R3) | WP1 (state model), WP5, tested in WP6 |
| Fifth objective: evaluation | WP2, WP6 |
| Completion: prototype software, source code, deployment instructions | WP6 (release), WP7 |
| Completion: design specification including the platform interface | WP1, WP7 |
| Completion: evaluation data protocol and test set | WP2 |
| Completion: test and evaluation reports | WP6 |
| Completion: information security risk assessment | WP1, WP7 |
| Completion: log of assessor decisions in a reusable format | WP5 (export), WP7 (format note) |

The Section 7 draft names a structured walk-through with assessors as part of the fifth objective. In S06 it is conditional on assessor time (T6.7, ISS-012); S08 must make the Section 7 sentence conditional to match.
