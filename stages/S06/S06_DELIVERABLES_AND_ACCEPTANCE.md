# S06_DELIVERABLES_AND_ACCEPTANCE

| Field | Value |
|---|---|
| Document ID | S06_DELIVERABLES_AND_ACCEPTANCE |
| Version | 1.0 |
| Status | APPROVED |
| Stage | S06 |
| Date | 2026-11-21 |
| Depends on | S06_WORK_PACKAGES; S05_EVALUATION_DESIGN; S05_FEASIBILITY_AND_RISKS; DRAFT_SEC08_FEATURES; DEC-031 |

- **Rule for acceptance evidence:** a deliverable is accepted on evidence that a third party can inspect: a document reviewed against a stated checklist, a test log with a pass criterion, a run file or a recorded measurement. Acceptance of a deliverable does not depend on a retrieval target being met. Retrieval targets (MS-01 to MS-03) are reported results; a "no supported difference" outcome is a valid evaluation result, not a failed deliverable (`S05_EVALUATION_DESIGN` §6).
- **Who accepts:** the owner, or a reviewer the owner designates, records acceptance. No named person is assumed (S10).
- **Affected targets:** MS-01 to MS-03 and the ET-01b and ET-04 definitions are not final until ISS-042 to ISS-045 are corrected in S07 (DEC-031). D2.1 is the deliverable that carries the corrected versions.

## 1. Deliverables and acceptance evidence

| ID | Deliverable | WP | Form | Acceptance evidence | Verification method |
|---|---|---|---|---|---|
| D1.1 | Prototype design specification: field map and IF-01, assessment template, record state model as a transition table, IF-02 to IF-08 (IF-07 specified only), reference environment | WP1 | Document | Every essential FN maps to at least one AC, one interface and one ET or unit test; the transition table enumerates every state, event and role used by ET-06; open owner inputs (ISS-005, ISS-034, ISS-035) are listed with the default applied | Checklist review; traceability check (T1.6) |
| D1.2 | Information security risk assessment of data flows (draft) | WP1 | Document | Each data flow DF-01 to DF-08 and each trust boundary has at least one identified risk, an assessed treatment and an owner-side decision point; external-query flow DF-04 records CP-1 | Checklist review against `S04_DATA_FLOWS_AND_INTERFACES` §4 |
| D1.3 | Data-handling and retention procedure | WP1 | Document | States what is stored, where, for how long and how it is deleted for imported submissions, test collections and cached external results; marks any rule still awaiting ISS-036 | Review |
| D2.1 | Evaluation protocol and judging guide (frozen version) | WP2 | Document | Freeze date recorded before any test pool is judged; contains metrics, grade scales, configurations, significance and correction procedure, PV values with their confirmation status, and the S07 corrections for ISS-042 to ISS-045; later changes logged with reason | Review; version history; freeze record |
| D2.2 | Versioned test collections per track, with licence record and, if built, DS-05 | WP2 | Data and manifest | Each collection has source, licence note, track label, split dates and checksum; no collection combines Track S and Track P; every substitute used passed T2.1 | Manifest check script |
| D2.3 | Evaluation harness with FT-01 reproduction note | WP2 | Software and note | FT-01 pass condition: the reproduced BM25 run matches the published reference value within rounding (`S05_FEASIBILITY_AND_RISKS` §3); metric scripts pass unit tests on hand-computed examples | Script output; unit-test log |
| D3.1 | Ingestion and normalization components (AC-01, AC-02) with source registry | WP3 | Software | Import of the field-mapped test file produces an import report listing rejected rows with reasons; every stored item carries source type, availability status and permission note; truncation counts reported per corpus | Unit and integration test log |
| D3.2 | Index layer and retrieval service (AC-04, AC-05) with all S05 configurations and display thresholds | WP3 | Software | Each configuration in `S05_EVALUATION_DESIGN` §2 that passed FT-02 produces a run file on the development split; each candidate is returned with an evidence passage; index and model versions stored | Run files; test log |
| D3.3 | Resource and latency measurement note (FT-02); FT-04 import report if an export is released | WP3 | Note | Measured encoding, search and re-ranking times recorded per configuration and confirmed corpus size; configuration set for ET-10 stated | Measurement log |
| D4.1 | Connector framework, patent connector, query construction and CP-1 approval | WP4 | Software | Every external call passes through CP-1 while it applies; logged text equals sent text; each stored result has source, retrieval date and terms note; AS-08 manual-entry path works with the same fields | Contract tests; CP-1 bypass tests |
| D4.2 | Connector smoke-test report (FT-03) | WP4 | Note | Authenticated query, parsed results, stored provenance and observed rate-limit handling for each connected service; if access is refused, the AS-08 fallback is recorded and MS-03 is marked untested | Test log |
| D5.1 | Assessment record service, access control, audit log, report and decision-log export (AC-09, AC-11 to AC-13) | WP5 | Software | Approved records carry model, index, connector and template versions; audit log holds one entry per transition; report export (IF-05) and decision-log export (IF-06) validate against D1.1 | Test log |
| D5.2 | Review interface (AC-10) | WP5 | Software | Screens show passage before score for R1, R2 and R4 items; source attribution fields visible; CP-1, approval and return actions available only to the assessor role | Scripted interface tests; checklist review |
| D5.3 | Approval-enforcement test suite (ET-06, ET-07) | WP5 | Software | Generated from the D1.1 transition table; covers every (state, event, role) combination, expired sessions, replayed requests and randomized sequences | Coverage report against the transition table |
| D6.1 | Integrated prototype release on the reference environment | WP6 | Software release | Release built from tagged sources by the deployment scripts on a clean environment; all WP3 to WP5 test suites pass on the release | Build log; test log |
| D6.2 | Pilot report and configuration selection record | WP6 | Document | Agreement (ET-11) and time per judgment reported; guide revision logged; PV-11 floors and the final query count fixed and dated before the test run; selection based on the development split only | Review; dates against D2.1 freeze record |
| D6.3 | Judgment files, run files and test logs | WP6 | Data | Raw and adjudicated judgments kept; single test run per configuration logged; ET-06 to ET-08 and ET-10 logs complete | Manifest check |
| D6.4 | Evaluation report by track | WP6 | Document | Every Section 8 row (MS-01 to MS-06, MS-08, MS-10) reported with its track, interval and pass or fail against the D2.1 criterion; results with an interval including zero stated as "no supported difference"; Track S and Track P never combined | Review; harness reproduces every reported figure from D6.3 |
| D7.1 | As-built design specification and deployment and operation instructions, with continuity notes | WP7 | Document | A person not involved in the build deploys D6.1 from the instructions on the reference environment | Deployment rehearsal record |
| D7.2 | Updated information security risk assessment; deletion record | WP7 | Document | D1.2 updated to the built system; deletion carried out as in D1.3 and recorded | Review; deletion record |
| D7.3 | Source code, configuration and component licence inventory | WP7 | Software and document | Every third-party component and model listed with version, licence and training-data terms (ISS-041); no Track S data in the package | Inventory check; repository scan |
| D7.4 | Handover demonstration and acceptance record | WP7 | Record | Demonstration covers R1, R2, R4 lists and the CP-5/CP-6 workflow on the release; acceptance or listed reservations recorded | Signed-off record (owner) |

## 2. Section 8 rows and the deliverable that evidences each

| Row | Evidenced by | Status at S06 |
|---|---|---|
| MS-01 | D6.4 (ET-01, ET-01b) on D3.2 | Target not final (ISS-043, ISS-045) |
| MS-02 | D6.4 (ET-03, ET-04) on D3.2; D2.2 for the source tested | Target not final (ISS-043, ISS-045) |
| MS-03 | D6.4 (ET-09) on D4.1 | Target not final (ISS-042) |
| MS-04 | D5.3 executed in D6.3 | Pass/fail target unchanged |
| MS-05 | ET-08 in D6.3 | Applies while CP-1 applies |
| MS-06 | ET-07 in D6.3 | Pass/fail target unchanged |
| MS-08 | ET-10 in D6.3; D3.3 | Planning value PV-09 awaiting ISS-039 |
| MS-10 | ET-05 in D6.3 | Pass/fail target unchanged |
| MS-07, MS-09 | None | Outside the funded scope (DEC-028) |

## 3. Milestones (decision points, not dates)

| ID | Milestone | Reached when | Gates |
|---|---|---|---|
| M1 | Design accepted | D1.1 to D1.3 accepted | Start of T3.4, T4.3, T5.1 final implementation |
| M2 | Protocol frozen | D2.1 frozen, D2.2 versioned, D2.3 passes FT-01 | Pilot judging (T6.2, T6.3 development pools) |
| M3 | Release integrated | D6.1 accepted | Test-pool judging and the single test run |
| M4 | Evaluation complete | D6.4 accepted | WP7 documentation of results |
| M5 | Handover | D7.4 recorded | Project close |
