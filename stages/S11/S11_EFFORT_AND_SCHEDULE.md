# S11_EFFORT_AND_SCHEDULE

| Field | Value |
|---|---|
| Document ID | S11_EFFORT_AND_SCHEDULE |
| Version | 0.1 |
| Status | SUBMITTED FOR GATE |
| Stage | S11 |
| Date | 2026-11-21 |
| Depends on | DEC-040; DEC-041; S11_SCOPE_AND_TECHNICAL_PLAN; S06_DEPENDENCIES_AND_EFFORT; qc/S11_EFFORT_MODEL.py |

- **Status:** PROVISIONAL. Hours, the lead/contributor split and the month allocation are proposals for the owner checkpoint (DEC-041 item 8). No availability, rate, cost or Gantt marking is final.
- **Source of every number:** `qc/S11_EFFORT_MODEL.py`, which holds the task list and month shares and regenerates the tables below; the QC script checks that the tables match it.
- **Nature of the estimates:** every task figure is an engineering judgment for the revised scope (S11_SCOPE_AND_TECHNICAL_PLAN), made at task level; no percentage was applied to the earlier figures and no productivity multiplier is used. Judging hours use the S06 formula (queries × pooled items × 1.27 × seconds ÷ 3,600) with the revised sizes: about 20 pooled items per query over three configurations, 45 s per item for retrieval judgments and 90 s for patent documents, all to be replaced by pilot values.
- **Split:** "Lead" is Member 1; "Contributors" are Members 2–4 combined. The split assigns architecture, the retrieval service core, the decision rule, the approval and disclosure enforcement, integration and adjudication to the lead, and specified, testable work (import, normalization, collections, harness code, screens, exports, generated tests, judging, documentation drafts, licence inventory, rehearsal) to contributors under the lead's review. This is an internal planning assumption (DEC-040 item 2) and does not appear in the proposal.

## 1. Task-level estimate

| Task | WP | Work | Lead (h) | Contributors (h) | Months |
|---|---|---|---|---|---|
| T1.1 | WP1 | Field map, import format, substitute schema, configurable assessment template | 6 | 14 | M1 |
| T1.2 | WP1 | Record state model as a transition table with the two approval properties | 14 | 4 | M1 |
| T1.3 | WP1 | Interface specifications (retrieval, connector, record and export, identity); platform adapter specified only | 12 | 6 | M1, M2 |
| T1.4 | WP1 | Information security risk assessment per data flow, role matrix, retention procedure | 10 | 16 | M1, M2 |
| T1.5 | WP1 | Development and reference environment; library selection, pinning and licence check; small vertical prototype (import, BM25, display) | 12 | 20 | M1 |
| R1 | WP1 | Technical review of WP1 outputs (design review) | 8 | 4 | M1, M2 |
| T2.1 | WP2 | Licence check of two or three substitute candidates on their original distributions | 4 | 8 | M1 |
| T2.2 | WP2 | Evaluation protocol and judging guide (grade scales, decision rule, sample sizes); freeze before test judging | 18 | 6 | M1, M2, M3 |
| T2.3 | WP2 | Substitute collection for similar submissions: time-ordered split, 60 queries, manifest | 4 | 20 | M2, M3 |
| T2.4 | WP2 | 50 public need statements used for both solution-example and prior-art evaluation; source indexing | 4 | 26 | M2, M3 |
| T2.5 | WP2 | Harness: toolkit metrics plus project code for success@10, judged@10, paired bootstrap, randomization test, Clopper-Pearson, agreement; unit tests | 12 | 26 | M2, M3 |
| T2.6 | WP2 | Reproduction of a published BM25 run | 2 | 8 | M3 |
| R2 | WP2 | Technical review of WP2 outputs | 8 | 2 | M1, M2, M3 |
| T3.1 | WP3 | Import adapter (delimited, JSON Lines), validation, import report, source registry | 4 | 26 | M2 |
| T3.2 | WP3 | Normalization, exact hashes, shingle near-duplicate fingerprints, passage splitting, language tag | 6 | 22 | M2 |
| T3.3 | WP3 | Lexical index and exact vector index per collection, with index versions | 8 | 16 | M2, M3 |
| T3.4 | WP3 | Retrieval service: BM25, one dense encoder, reciprocal rank fusion, date filter, evidence passage | 28 | 18 | M2, M3 |
| T3.5 | WP3 | Display threshold and 'no example above threshold' signal on development data | 6 | 4 | M3 |
| T3.6 | WP3 | Encoding and search timing at two corpus sizes | 4 | 8 | M4, M5 |
| T3.7 | WP3 | Unit and integration tests | 4 | 20 | M2, M3 |
| R3 | WP3 | Technical review and integration of WP3 outputs | 12 | 2 | M2, M3, M4 |
| T4.1 | WP4 | Connector contract, result cache with provenance, rate limiter, retries | 12 | 16 | M3, M4 |
| T4.2 | WP4 | One patent-service connector with smoke test | 6 | 18 | M3, M4 |
| T4.3 | WP4 | Query construction, disclosure clearance, assessor approval of exact text, payload-hash logging | 18 | 10 | M3, M4 |
| T4.4 | WP4 | Manual-entry fallback recording query text and clearance | 2 | 10 | M4 |
| T4.5 | WP4 | Contract and bypass tests for both conditions | 8 | 14 | M4 |
| R4 | WP4 | Technical review of WP4 outputs | 8 | 2 | M3, M4 |
| T5.1 | WP5 | Record service: transition table, versioning, approval binding, outcome-field database trigger | 30 | 14 | M2, M3, M4 |
| T5.2 | WP5 | Accounts and roles using the framework's authentication; permission checks | 4 | 14 | M3, M4 |
| T5.3 | WP5 | Insert-only audit log with hash chain | 6 | 10 | M4 |
| T5.4 | WP5 | Lightweight server-rendered review interface: evidence-first lists, query approval, template form, approve and return | 10 | 50 | M3, M4 |
| T5.5 | WP5 | Exports: schema-validated JSON record, readable report, decision log | 2 | 16 | M4 |
| T5.6 | WP5 | Generated approval-enforcement suite (every state, event and role; expired and replayed requests; re-approval; hash chain) | 10 | 24 | M4 |
| R5 | WP5 | Technical review of WP5 outputs | 12 | 2 | M3, M4 |
| T6.1 | WP6 | Integrated release on the reference environment; deployment scripts; system-level tests | 22 | 18 | M4, M5 |
| T6.2 | WP6 | Pilot judging on development queries; one guide revision; agreement; sample-size check | 8 | 14 | M4, M5 |
| T6.3 | WP6 | Test-pool judging with 20% double judging; deeper check; unaided and edited external queries | 8 | 61 | M5 |
| T6.4 | WP6 | Single test run; approval, disclosure, attribution and response-time tests | 6 | 14 | M5 |
| T6.5 | WP6 | Analysis with intervals; error analysis; corrective development | 24 | 24 | M5, M6 |
| T6.6 | WP6 | Evaluation report by data track | 12 | 10 | M5, M6 |
| R6 | WP6 | Technical review of WP6 outputs | 10 | 2 | M4, M5, M6 |
| T7.1 | WP7 | As-built design specification; deployment and operation instructions | 10 | 18 | M5, M6 |
| T7.2 | WP7 | Risk assessment update; deletion of project data with record | 4 | 8 | M6 |
| T7.3 | WP7 | Code package, component and licence inventory, sponsor-data scan | 2 | 10 | M6 |
| T7.4 | WP7 | Deployment rehearsal by a member not involved in the deployment scripts; fixes | 4 | 10 | M6 |
| T7.5 | WP7 | Defect resolution and final reproducibility check from stored run and judgment files | 12 | 14 | M6 |
| T7.6 | WP7 | Handover demonstration, acceptance record, continuity notes | 6 | 6 | M6 |
| R7 | WP7 | Technical review of WP7 outputs | 6 | 2 | M5, M6 |
| C | All | Team coordination: weekly one-hour meeting of four members over 26 weeks; task briefing by the lead, 2 h per week | 78 | 78 | M1–M6 |
| Total | | | 526 | 765 | |

## 2. Work-package totals

| WP | Title | Technical lead | Contributors | Total | Earlier provisional (S10) |
|---|---|---|---|---|---|
| WP1 | Prototype design specification and data-protection baseline | 74 | 76 | 150 | 210 |
| WP2 | Evaluation protocol, test collections and evaluation harness | 62 | 106 | 168 | 290 |
| WP3 | Ingestion and retrieval for similar submissions and solution examples | 83 | 127 | 210 | 380 |
| WP4 | External prior-art retrieval with query approval | 61 | 77 | 138 | 215 |
| WP5 | Assessment record, review interface and approval controls | 85 | 141 | 226 | 400 |
| WP6 | Prototype integration and evaluation | 107 | 160 | 267 | 414 |
| WP7 | Technical documentation and handover | 54 | 78 | 132 | 140 |
| Total | | 526 | 765 | 1291 | 2049 |

Coordination (line C) is attributed to work packages in proportion to their task hours in each month, so that Section 13 carries all hours without an eighth work package (DEC-033 item 4).

## 3. EH-10 double-counting check

| Effort type | Where counted in S11 | Not counted again in |
|---|---|---|
| Technical review of outputs | Lines R1–R7 only (80 h: lead 64, contributors 16) | Task lines, which exclude review; the S06 design review T1.6 is merged into R1 and the S06 acceptance task into T7.6 |
| Team coordination and task briefing | Line C only (156 h: lead 78, contributors 78) | Task lines and review lines |
| Integration | T3.4 (service), T6.1 (release) | Review lines |
| Rework | Corrective development in T6.5 and defect resolution in T7.5 | No separate allowance or multiplier |

S06 estimates included coordination and review inside each task (EH-10). S11 task figures exclude both, and both appear once. Total review plus coordination: 236 h (18% of 1,291 h), stated rather than hidden in task figures. Whether Section 13 shows these hours is ISS-057.

## 4. Six-month workload model

| Month | Technical lead (h) | Contributors combined (h) | Per contributor if shared equally (h) | Team total (h) |
|---|---|---|---|---|
| 1 | 72 | 75 | 25 | 148 |
| 2 | 93 | 150 | 50 | 242 |
| 3 | 108 | 144 | 48 | 252 |
| 4 | 105 | 169 | 56 | 274 |
| 5 | 74 | 134 | 45 | 208 |
| 6 | 74 | 92 | 31 | 167 |
| Total | 526 | 765 | 255 | 1291 |

Hours per work package and month (team total):

| WP | M1 | M2 | M3 | M4 | M5 | M6 |
|---|---|---|---|---|---|---|
| WP1 | 103 | 23 |  |  |  |  |
| WP2 | 19 | 64 | 65 |  |  |  |
| WP3 |  | 120 | 53 | 9 | 6 |  |
| WP4 |  |  | 58 | 66 |  |  |
| WP5 |  | 9 | 50 | 145 |  |  |
| WP6 |  |  |  | 28 | 165 | 39 |
| WP7 |  |  |  |  | 11 | 101 |

| Month | Owner's focus (DEC-041 item 2) | Planned work |
|---|---|---|
| 1 | Lighter start: specifications, environment, formats, libraries, vertical prototype, evaluation procedures | WP1 nearly complete; licence check and protocol drafting start; end-to-end prototype; team total 148 h, the lightest month |
| 2 | Ingestion, normalization, duplicates, BM25, initial semantic retrieval, early tests | WP3 import, normalization, indexes, BM25 and dense retrieval; WP2 collections and harness; record-service skeleton |
| 3 | R1 and R2 integration, evidence handling, external search, core record and workflow | Retrieval service completed with fusion, thresholds, evidence passages; connector and query flow; record service; harness reproduction run |
| 4 | Integrated workflow, approval and re-approval, interface, traceability, access control, audit, system tests | Review interface, audit log, exports, generated approval suite, bypass tests; integration release starts; pilot judging; timing |
| 5 | Functional verification, retrieval evaluation, error analysis, reliability and security checks, corrective development, reporting | Test judging and single test run; workflow tests; interval analysis; error analysis; corrective development; report drafting |
| 6 | Defects, reproducibility, demonstration, documentation, rehearsal, handover | Defect resolution, reproducibility check, as-built documentation, deletion record, rehearsal, demonstration and acceptance |

## 5. Minimum availability required

| Role | Month 1 | Months 2–4 | Months 5–6 | Total over six months |
|---|---|---|---|---|
| Technical lead | 72 h (about 18 h per week) | up to 108 h in month 3 (about 27 h per week) | 74 h (about 19 h per week) | 526 h |
| Each contributor, if work is shared equally | 25 h (about 6 h per week) | up to 56 h in month 4 (about 14 h per week) | 45 h, then 31 h | 255 h |
| Contributors combined, if not equal | 75 h | up to 169 h in month 4 | 134 h, then 92 h | 765 h |

Weeks are converted at four weeks per month, the form's own example (ISS-017). These are the hours the plan needs; actual availability has not been stated and is not assumed.

Feasibility against possible lead limits (the binding constraint):

| Lead availability per month | Months over the limit | Six-month total available versus needed | Smallest adjustment |
|---|---|---|---|
| 110 h or more | None | 660 ≥ 526 | None; months 5–6 leave about 35 h per month of lead reserve for integration problems |
| 90 h | Months 2, 3, 4 exceed by 3, 18, 15 h (36 h) | 540 ≥ 526 | Move about 36 lead hours into months 1, 5 and 6 by giving contributors the lead share of the connector smoke test and the account set-up (T4.2, T5.2), starting deployment scripts (T6.1) earlier, and holding part of the WP4 and WP5 reviews until month 5; or extend by two weeks |
| 80 h | Months 2–4 exceed by 66 h | 480 < 526 (short by 46 h) | Not feasible in six months without reducing the lead's share: either a seven-month schedule, or about 46 lead hours delegated with additional review risk; no scope cut is proposed because the remaining scope is already the minimum that meets R1–R4 with a defensible evaluation |

Contributor hours are not binding: if the three contributors together can give 170 h in month 4 (about 14 h per week each), the plan fits.

## 6. Differences from the earlier 2,049-hour estimate

| WP | Earlier | S11 | Main reasons |
|---|---|---|---|
| WP1 | 210 | 150 | Fewer interface specifications (identity from the framework, adapter one page); risk assessment templated per data flow; vertical prototype added (+32 h) |
| WP2 | 290 | 168 | One need-statement set for R2 and R4; smaller collections; statistics reduced to intervals with established libraries; fewer candidates in the licence check |
| WP3 | 380 | 210 | Three configurations instead of nine; no tuning; one encoder; two corpus sizes; exact search only |
| WP4 | 215 | 138 | Simpler cache and limiter; two query formulations; enforcement and bypass tests kept in full |
| WP5 | 400 | 226 | Lightweight screens (140 → 60 h); framework authentication; randomized test generator and second-approver setting removed; record service, trigger, audit chain and generated suite kept |
| WP6 | 414 | 267 | Judging 180 → 69 h with smaller sets and three pooled configurations; no configuration selection; error analysis and corrective development added |
| WP7 | 140 | 132 | Defect resolution and final reproducibility check added (+26 h) offset by automated licence listing |
| Total | 2,049 | 1,291 | Net reduction 758 h. The S11 total also contains 236 h of review and coordination stated as separate lines (in S06 they sat inside task figures) and new work the earlier plan lacked: the vertical prototype, explicit error analysis and corrective development, and the final reproducibility check |

The four-member structure does not reduce total effort; it adds the review and coordination lines and determines the calendar through the lead's monthly hours.
