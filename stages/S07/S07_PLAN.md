# S07_PLAN

| Field | Value |
|---|---|
| Document ID | S07_PLAN |
| Version | 1.0 |
| Status | SUBMITTED FOR GATE |
| Stage | S07 |
| Date | 2026-11-21 |
| Depends on | DEC-033; DEC-034; S06_HANDOFF; 00_STAGE_GATE_PROTOCOL §7 (S07 row) |

- **Stage:** S07 — Detailed Technical Methodology (proposal Section 12).
- **Authorization:** S06 gate decision DEC-033 (CONDITIONAL PASS; S07 authorized in a new chat); owner instruction `START_STAGE S07` recorded as DEC-034.
- **Session start checks:** S06 content commit 03f56dd and approved baseline 2d46990 present in history; S06 QC script passes (869 checks, 0 failed). At first clone the S06 gate decision had not yet been recorded; the session stopped and reported it, and the owner recorded DEC-033 before work began.

## 1. Inputs (as listed in the S06 handoff)

`CLAUDE.md`; `project/00_PROJECT_RULES.md`, `00_STAGE_STATUS.md`, `00_STAGE_GATE_PROTOCOL.md`, `03_STYLE_GUIDE.md`, `00_DECISIONS_LOG.md`, `00_OPEN_ISSUES_REGISTER.md`, `02_SOURCE_LOG.md`, `02_CLAIM_REGISTER.md`, `00_SKILL_REGISTER.md`, `S01_REVIEWER_CRITERIA_REGISTER.md`, `S01_TRACEABILITY_MATRIX.md`; `stages/S06/S06_WORK_PACKAGES.md`, `S06_DELIVERABLES_AND_ACCEPTANCE.md`, `S06_HANDOFF.md`; `stages/S05/S05_EVALUATION_DESIGN.md`, `S05_FEASIBILITY_AND_RISKS.md` §1–§2, `S05_DATA_AVAILABILITY_AND_SUBSTITUTES.md` §4; `stages/S04/S04_ARCHITECTURE.md` §3–§5, `S04_DATA_FLOWS_AND_INTERFACES.md`; `proposal/DRAFT_SEC07_OBJECTIVES.md`, `DRAFT_SEC08_FEATURES.md`, `DRAFT_SEC13_ACTIVITIES.md`; REF-02 §12 (Claude Project).

## 2. Work steps

1. Resolve ISS-042 to ISS-045 and record the reasoning (`S07_CORRECTED_EVALUATION_METHODOLOGY`); write the corrected rows into `S05_EVALUATION_DESIGN` v2.0, `S05_DATA_AVAILABILITY_AND_SUBSTITUTES` v2.0 and `DRAFT_SEC08_FEATURES` v0.4.
2. Targeted source checks only: CQADupStack licence on the original distribution (ISS-044); Pyserini and Faiss licence files and current version (ISS-041); model-card training-data statements (ISS-041); sources for non-inferiority, multiplicity and binomial intervals.
3. Tool and version register with VERIFIED / PROPOSED status (`S07_TOOL_AND_VERSION_REGISTER`).
4. Section 12 working draft with one subsection per WP, titles verbatim (`proposal/DRAFT_SEC12_METHODOLOGY`); align the Section 13 draft where Section 12 adds a task.
5. WP-to-methodology traceability, Section 8 verification steps and consistency checks (`S07_WP_METHOD_TRACEABILITY`).
6. Living registers: decisions, issues, sources, claims, Skill checkpoint, traceability Parts G and I, reviewer criteria, stage status, README.
7. QC script (cumulative, adds S07 checks), QC report, handoff; commit and push as SUBMITTED FOR GATE (owner authorization in DEC-034).

## 3. Length budget

Section 12 draft: at most 5,500 words including the tool table (the form sets no limit; Section 12 must carry concrete procedures for seven activities). Other S07 files: as needed for the tables; handoff one page or less.

## 4. Out of scope

S08 drafting of other sections; personnel, effort, costs and schedule (S10); any implementation; use of any dataset; contact with any external service beyond reading public documentation pages.
