# S06_PLAN

| Field | Value |
|---|---|
| Document ID | S06_PLAN |
| Version | 1.0 |
| Status | SUBMITTED FOR GATE |
| Stage | S06 |
| Date | 2026-11-21 |
| Depends on | DEC-012; DEC-028; DEC-031; DEC-032; S05_HANDOFF; 00_STAGE_GATE_PROTOCOL §7 (S06 row) |

- **Objective:** define the 6–7 funded work packages of proposal Section 13 for the narrowed Option B laboratory prototype (DEC-028): frozen identifiers and titles, objectives, tasks, deliverables, acceptance evidence, dependencies and provisional person-hours with stated assumptions, traced to R1–R4, architecture components, S05 tests and Section 8 rows. Nothing is built, measured, staffed, costed or scheduled in calendar terms in S06.
- **Exit criterion (gate protocol §7):** 6–7 work packages with frozen IDs and titles, tasks, deliverables, acceptance evidence, dependencies and provisional person-hours with stated assumptions, within the ISS-013 envelope (RF-007, QA-001, QA-007). ISS-013 is still open, so S06 cannot show that an envelope is met; the estimates are conditional and the gap is reported (`S06_DEPENDENCIES_AND_EFFORT` §6).
- **Distinction kept throughout:** WP1–WP7 are funded project activities. S01–S10 are the stages of this proposal-writing workflow (DEC-012). No S-stage appears as a work package.

## 1. Start-of-session checks

| Check | Result |
|---|---|
| S05 gate decision recorded explicitly | DEC-031, decided by Owner, status ACTIVE: CONDITIONAL PASS, S06 authorized |
| Approved baseline in `00_STAGE_STATUS.md` present in history | 350ac43 (DEC-031 checkpoint) and S05 content 83331af present; status record 37d18d9 is the start commit |
| `python3 stages/S05/qc/S05_QC_CHECK.py .` on the start commit | PASS (638 checks, 0 failed) |
| Mandatory S05 corrections | ISS-042 to ISS-045 open; carried into WP2 task T2.2 and into explicit S07 instructions (`S06_HANDOFF`) |

## 2. Inputs (as listed in the S05 handoff)

Rules, status, gate protocol, style guide; DEC-012, DEC-028, DEC-029, DEC-030, DEC-031; ISS-002, ISS-003, ISS-005, ISS-013, ISS-017, ISS-018, ISS-033 to ISS-045; `S04_ARCHITECTURE` §2, §3, §4, §7; `S04_SCOPE_OPTIONS` §6; `S04_ASSUMPTIONS_AND_STANDARDS` §1 (AS-01 to AS-12); `S05_EVALUATION_DESIGN` §1 to §9; `S05_FEASIBILITY_AND_RISKS` §3, §4; `S05_DATA_AVAILABILITY_AND_SUBSTITUTES` §1, §3, §4; `proposal/DRAFT_SEC07_OBJECTIVES`; `proposal/DRAFT_SEC08_FEATURES`; traceability Parts D, F, G; reviewer register rows RF-006, RF-007, RF-011, RF-012, QA-001, QA-007; REF-02 Sections 12, 13 and 16 (Claude Project). No earlier transcripts were loaded.

## 3. Work steps

1. Package the essential function set (FN-01 to FN-03, FN-05, FN-06, FN-08 to FN-12, CP-1, CP-5, CP-6) and the evaluation sequence E-0 to E-6 into work packages with no shared tasks (`S06_WORK_PACKAGES`).
2. Define deliverables and the evidence that accepts each (`S06_DELIVERABLES_AND_ACCEPTANCE`).
3. Order the work, list owner decisions by the task that needs them, and size every task in person-hours with stated assumptions; size relevance judging from the S05 formula (`S06_DEPENDENCIES_AND_EFFORT`).
4. Draft Section 13 in the form's table schema (`proposal/DRAFT_SEC13_ACTIVITIES`).
5. Traceability Part H; register updates; cumulative QC script; QC report; handoff with S07 instructions; commit and push as SUBMITTED FOR GATE (DEC-032).

No external research is needed: S06 plans from approved S04 and S05 material. The source log and claim register are therefore unchanged.

## 4. Length budgets

| Deliverable | Budget |
|---|---|
| S06_WORK_PACKAGES | ≤ 200 lines |
| S06_DELIVERABLES_AND_ACCEPTANCE | ≤ 120 lines |
| S06_DEPENDENCIES_AND_EFFORT | ≤ 220 lines |
| DRAFT_SEC13_ACTIVITIES | ≤ 60 lines |
| S06_HANDOFF | One page |

## 5. Out of scope

Section 12 prose (S07); tool versions (S07); team members, monthly hours and shares (S10, Section 14); hourly rates and costs (S10, Section 15); calendar months and weights (S10, Section 16); the corrections ISS-042 to ISS-045 themselves (S07); any implementation or measurement.
