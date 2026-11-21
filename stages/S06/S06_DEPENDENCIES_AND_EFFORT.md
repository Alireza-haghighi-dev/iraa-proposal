# S06_DEPENDENCIES_AND_EFFORT

| Field | Value |
|---|---|
| Document ID | S06_DEPENDENCIES_AND_EFFORT |
| Version | 2.0 |
| Status | DRAFT |
| Stage | S10 |
| Date | 2026-11-21 |
| Depends on | S06_WORK_PACKAGES; S06_DELIVERABLES_AND_ACCEPTANCE; S05_EVALUATION_DESIGN §5, §7, §9; S05_FEASIBILITY_AND_RISKS §3; S05_DATA_AVAILABILITY_AND_SUBSTITUTES §3; ISS-013; ISS-017; ISS-039 |

- **S10 alignment (DEF-002, DEC-039):** wording aligned with the S09-corrected master (CP-1 always applied with disclosure clearance and query approval, DEC-035; EPO OPS thresholds as fair-use guidance, DEC-038; retention default, DEF-034). Content otherwise unchanged.
- **Status of figures:** every person-hour figure is a provisional ASSUMPTION for planning (EH-01 to EH-10). No figure is taken from earlier drafts (QA-001). None is a commitment, a team allocation or a cost.
- **Effort envelope:** ISS-013 (duration and effort envelope) is open. S06 therefore gives conditional estimates and a list of reductions with their consequences (§6). It does not claim that any ceiling is met.
- **Unit:** person-hours of a proficient practitioner, independent of team size (REF-02 §13).

## 1. Effort-sizing assumptions (ASSUMPTION; owner confirmation ISS-046)

| ID | Assumption | Effect if wrong |
|---|---|---|
| EH-01 | Estimates are person-hours for one proficient practitioner. The form's example (two full-time people, two weeks, 180 person-hours) implies 45 hours per person-week; that factor is used only to express totals in person-weeks, and the convention itself awaits ISS-017 | Person-week figures change; person-hours do not |
| EH-02 | Build tasks use the open-source libraries named as candidates in S05 (Pyserini, Faiss, the D-1 to D-3 encoders, the RR re-ranker) rather than new implementations; no project code exists to reuse | If a candidate fails its licence or feasibility check, the affected task grows |
| EH-03 | The planning figure assumes the current data position, outcome O-4 (nothing released): retrieval tests on Track P only, judged by project judges (AS-09, AS-10) | Other outcomes add the work in §5 |
| EH-04 | DS-05 is built (T2.4), pending the owner decision under ISS-038 | Not built: −60 h and MS-02 untested under O-4 |
| EH-05 | Judging inputs from AS-12: per retrieval test and track, PV-01 = 60 test plus PV-02 = 20 development queries; PV-08 = 30 need statements for ET-09; PV-04 = 20% double judging | Values changed under ISS-039: recompute §4 |
| EH-06 | Unique pooled items per query for ET-01 and ET-03 (up to 90 with nine configurations at depth PV-03 = 10): 30 / 45 / 60 (low / planning / high). Per need statement for ET-09 (three formulations × 10): 20 / 25 / 30 | Replaced by the FT-05 pilot values |
| EH-07 | Seconds per judgment: 30 / 45 / 60 for R1 and R2 items; 60 / 90 / 120 for patent documents. Project judgement, not a sourced figure | Replaced by the FT-05 pilot values |
| EH-08 | Share of double-judged pairs sent to a third judge: 0.25 / 0.35 / 0.50 | Replaced by pilot agreement |
| EH-09 | Range for build, design and documentation tasks: 0.8 to 1.3 times the planning figure, reflecting unknown export format, field list and library behaviour | Wider range if ISS-005 or ISS-008 answers add fields or formats |
| EH-10 | Coordination and quality review are included in each task (design review T1.6, release checklist T6.1, acceptance T7.4); no separate management activity (ISS-048). No training activity (ISS-018) | A separate activity, if the sponsor requires one, is added to Section 13 and to the totals |

## 2. Dependencies and sequencing

Relative order only. Calendar months, overlap with team availability and weights are set in S10 (RF-010).

| WP or task | Depends on | Type | Reason |
|---|---|---|---|
| WP1 | Owner answers where available (§7); defaults AS-01 to AS-12 otherwise | Start | Design fixes what WP3 to WP5 implement |
| T2.1, T2.3, T2.5 | None (start with WP1) | Parallel start | Licence checks and harness do not need the prototype |
| T2.2 freeze | S07 corrections for ISS-042 to ISS-045; ISS-039 | Finish-to-start | Protocol cannot freeze with uncorrected targets (DEC-031) |
| T2.6 (FT-01) | T2.1 (DS-02 licence), T2.5 | Finish-to-start | Harness errors retired before any comparison (RSK-09) |
| T3.1, T3.2 | T1.1 | Finish-to-start | Field map |
| T3.4 | T1.3 (IF-02), T3.3 | Finish-to-start | Interface and indexes |
| T3.6 (FT-02) | T1.5, T3.3, T3.4 | Finish-to-start | Must precede configuration selection (T6.4) and ET-10 |
| T4.2 (FT-03) | T4.1, ISS-040 | Finish-to-start | Service choice |
| T4.3 | T1.2, T5.1 (record API for CP-1) | Partial overlap | CP-1 is enforced by AC-09 |
| T5.1, T5.6 | T1.2 | Finish-to-start | Transition table |
| T5.4 | T5.1, T3.4, T4.3 (candidate and query data) | Partial overlap | Screens consume IF-02, IF-03 and IF-04 |
| T6.1 | D3.2, D4.1, D5.1, D5.2 | Finish-to-start | Integration |
| T6.3 development pools, T6.2 | M2 (D2.1 to D2.3), D3.2 runs on the development split | Finish-to-start | Pilot needs frozen guide and pooled runs |
| T6.4 | T6.2, T3.6 | Finish-to-start | Selection on development data within the FT-02 limits |
| T6.3 test pools, T6.5 | M3 (D6.1), T6.4, PV-11 fixed | Finish-to-start | Single test run on the selected configuration |
| T6.6 | T6.3, T6.5 | Finish-to-start | Analysis |
| WP7 | T6.6 (D6.4), D1.1 to D1.3 | Finish-to-start for T7.1, T7.4; T7.3 may start at M3 | As-built documentation |

**Longest chain (planning figures):** T1.1 → T3.1 → T3.3 → T3.4 → T6.1 → T6.4 → T6.3 test pools → T6.5 → T6.6 → T7.1 → T7.4. WP2 runs alongside WP1 and WP3 but M2 must be reached before pilot judging; the S07 corrections and ISS-039 are therefore on the path to M2. Feasibility tests are placed before the work they protect: FT-01 before M2, FT-02 before T6.4, FT-03 before T4.3 is relied on, FT-04 at T3.1 if an export arrives, FT-05 at T6.2.

## 3. Provisional person-hours per task (planning figure)

| WP | Task | Hours | Basis |
|---|---|---|---|
| WP1 | T1.1 | 40 | Field map for one export or substitute schema, plus a configurable template |
| WP1 | T1.2 | 40 | Five states, three roles, CP-1, CP-5, CP-6, second-approver setting, as a transition table |
| WP1 | T1.3 | 50 | Seven interface specifications (IF-02 to IF-08) |
| WP1 | T1.4 | 50 | Eight data flows; role matrix; retention procedure |
| WP1 | T1.5 | 15 | One environment description |
| WP1 | T1.6 | 15 | One review and traceability pass |
| WP2 | T2.1 | 24 | Up to four candidates, original distributions |
| WP2 | T2.2 | 60 | Protocol and guide with worked examples for three grade scales |
| WP2 | T2.3 | 50 | Splits, query selection and manifests per track |
| WP2 | T2.4 | 60 | Conditional (EH-04): at least PV-01 + PV-02 need statements and source indexing |
| WP2 | T2.5 | 80 | Seven metrics, two resampling procedures, per-track reporting |
| WP2 | T2.6 | 16 | One reproduction run |
| WP3 | T3.1 | 60 | Parser, validation, import report, source registry |
| WP3 | T3.2 | 60 | Five normalization steps |
| WP3 | T3.3 | 50 | Lexical and vector index per corpus, versioning |
| WP3 | T3.4 | 110 | Nine configurations, fusion, passage scoring, evidence spans |
| WP3 | T3.5 | 20 | Two thresholds on the development split |
| WP3 | T3.6 | 40 | Three encoders × up to three corpus sizes |
| WP3 | T3.7 | 40 | Tests for five components |
| WP4 | T4.1 | 60 | Plug-in contract, cache, rate limits, provenance |
| WP4 | T4.2 | 50 | One service connector and FT-03 |
| WP4 | T4.3 | 50 | Query generation, edit and approval flow, exact-text logging |
| WP4 | T4.4 | 20 | Manual-entry path |
| WP4 | T4.5 | 30 | Contract and bypass tests |
| WP5 | T5.1 | 90 | Record service with state machine and versioning |
| WP5 | T5.2 | 40 | Three roles, project accounts |
| WP5 | T5.3 | 30 | Append-only log |
| WP5 | T5.4 | 140 | Candidate lists for three result types, query approval, template form, approval actions |
| WP5 | T5.5 | 40 | Two export formats |
| WP5 | T5.6 | 60 | Generated and randomized suite |
| WP6 | T6.1 | 60 | Integration, deployment scripts, release checklist |
| WP6 | T6.2 | 24 | Pilot analysis and sample-size check |
| WP6 | T6.3 | 140 | Formula, §4, planning scenario |
| WP6 | T6.4 | 40 | Tuning and selection |
| WP6 | T6.5 | 50 | Test run, ET-05 to ET-08, ET-10 |
| WP6 | T6.6 | 60 | Analysis and report by track |
| WP7 | T7.1 | 50 | As-built specification, deployment instructions |
| WP7 | T7.2 | 30 | Risk assessment update, deletion |
| WP7 | T7.3 | 30 | Code package, licence inventory |
| WP7 | T7.4 | 20 | Demonstration, acceptance record |
| WP7 | T7.5 | 10 | Continuity notes |

### Totals per work package

| WP | Planning figure | Low | High |
|---|---|---|---|
| WP1 | 210 | 168 | 273 |
| WP2 | 290 | 232 | 377 |
| WP3 | 380 | 304 | 494 |
| WP4 | 210 | 168 | 273 |
| WP5 | 400 | 320 | 520 |
| WP6 | 374 | 250 | 551 |
| WP7 | 140 | 112 | 182 |
| Total | 2004 | 1554 | 2670 |

Low and high apply EH-09 to every task except T6.3, whose range comes from the low and high judging scenarios in §4 (63 and 247 hours). At EH-01's conversion factor the planning total is about 44.5 person-weeks. The planning figure is the one carried into the Section 13 draft; S10 replaces it once ISS-013, ISS-039 and the FT-05 pilot values are known.

## 4. Relevance-judging effort (T6.3)

Formula, from `S05_EVALUATION_DESIGN` §5 item 5 with adjudication added (ET-11):

Hours = queries × pooled items per query × (1 + d + d × a) × seconds per judgment ÷ 3,600, where d = PV-04 (0.20) and a = adjudicated share (EH-08). Each test is rounded up to a whole hour.

| Test (Track P) | Queries | Low | Planning | High |
|---|---|---|---|---|
| ET-01 (R1) | 80 | 25 | 58 | 104 |
| ET-03 (R2, DS-05) | 80 | 25 | 58 | 104 |
| ET-09 (R4) | 30 | 13 | 24 | 39 |
| Total | — | 63 | 140 | 247 |

Inputs per scenario are EH-05 to EH-08. After the FT-05 pilot, the measured pooled-item count, time per judgment and agreement replace EH-06 to EH-08, and the figure in Section 13 is recomputed with the same formula.

## 5. Conditional work not in the planning figure

| Condition | Added work | Hours | Funded or sponsor-side |
|---|---|---|---|
| Sponsor export released (ISS-002) | T3.8 FT-04 | 16 | Funded |
| ISS-040 selects a second patent service | T4.6 | 30 | Funded |
| Assessor time available (ISS-012) | T6.7 walk-through, project side | 24 | Funded; assessor hours are sponsor-side |
| Outcome O-3: export, no assessor time | Track S ET-01 judged by project judges; Track S analysis | 58 (25–104) + 20 | Funded |
| Outcome O-1 or O-2: export and assessors | Track S ET-01 (and ET-03 under O-1) judged by sponsor assessors; calibration subset (§5 item 3 of the evaluation design) | 58 per test (25–104); calibration size not set | Sponsor-side, not in Section 13 unless the owner decides otherwise (ISS-047); project analysis +20 per track is funded |
| ISS-033 authorizes Track S R4 queries | Track S ET-09 judging | 24 (13–39) | Judged by whoever judges Track S |
| Owner decides not to build DS-05 | Remove T2.4 | −60 | MS-02 untested under O-4 |

## 6. Effort envelope (ISS-013 open)

No ceiling has been stated, so none can be shown to be met. If the owner sets an envelope below the planning total, these reductions are available. Each has a consequence that the proposal must then state.

| ID | Reduction | Hours saved (approx.) | Consequence |
|---|---|---|---|
| L-1 | Drop D-3 and RR from the configuration set | 30 in T3.4, 10 in T3.6, fewer pooled items in T6.3 | Long submissions rely on passage segmentation only (RSK-10); no re-ranking result |
| L-2 | Drop H-CC, keep H-RRF | 10 | One hybrid method compared instead of two |
| L-3 | Reduce review screens to the minimum for CP-1, CP-5, CP-6 and evidence display | 40 in T5.4 | Less convenient review; MS-10 unaffected |
| L-4 | Lower PV-01 (owner change under ISS-039) | About 0.7 h per removed query per retrieval test at planning values (45 items × 1.27 × 45 s) | Wider intervals; higher chance of an underpowered result (RSK-08) |
| L-5 | Do not build DS-05 (EH-04) | 60 plus 58 judging | R2 untested unless a sponsor source is confirmed |

An envelope above the planning total needs no change; the remaining margin covers the conditional work in §5.

## 7. Owner decisions by the task that needs them

| Issue | Needed by | Default applied until decided |
|---|---|---|
| ISS-013 effort envelope | S10 (Sections 14 to 16); §6 reductions | Planning figure, conditional |
| ISS-002, ISS-003, ISS-012 data, R2 sources, assessor time | T2.3 | Outcome O-4 (AS-09, AS-10) |
| ISS-005 assessment fields | T1.1 | Placeholder template (AD-07) |
| ISS-034 approval model; ISS-035 accounts | T1.2, T5.2 | AD-06 single approver with optional second; AS-05 |
| ISS-036 retention | T1.4, T7.2 | Delete imported sponsor data, collections derived from it and cached external results at project close; retain and hand over public-source collections, judgment files and run files where licences permit; no copy of sponsor data outside the environment (DEF-034) |
| ISS-038, ISS-044 substitute licences; DS-05 | T2.1, T2.4, T2.6 | Candidate unusable until checked; DS-05 assumed built (EH-04) |
| ISS-039 planning values | T2.2 freeze | AS-12 |
| ISS-040 patent service | T4.2 | None: T4.2 cannot start; AS-08 fallback if no service is chosen |
| ISS-033 external disclosure | Track S part of T6.3, T6.5 | CP-1 applies to every query; no sponsor-derived text sent without authorization; ET-09 on Track P |
| ISS-018 training activity | Section 13 final form | None included |
| ISS-046 to ISS-048 (S06) | S10 | EH-01 to EH-10 |
