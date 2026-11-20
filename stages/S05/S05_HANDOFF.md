# S05_HANDOFF

| Field | Value |
|---|---|
| Document ID | S05_HANDOFF |
| Version | 1.0 |
| Status | APPROVED |
| Stage | S05 |
| Date | 2026-11-20 |
| Depends on | DEC-028; DEC-030; S05_EVALUATION_DESIGN; S05_DATA_AVAILABILITY_AND_SUBSTITUTES; S05_FEASIBILITY_AND_RISKS; S05_QC_REPORT |

- **Transition:** S05 → S06 Main Activities and Deliverables (Section 13 work packages). S06 starts only after the owner records the S05 gate decision and opens a new chat (DEC-024).

## What S05 produced

- **Evaluation design:** explicit tests for R1 (ET-01, ET-01b, ET-02), R2 as corrected by DEC-029 (ET-03 to ET-05, including a "no example found" test), R3 (ET-06, ET-07, model-based workflow tests) and R4 (ET-08, ET-09); response time (ET-10) and judging reliability (ET-11). Baselines: BM25, recency order, fingerprints; candidates: dense, hybrid, optional re-ranking.
- **Data:** sponsor data (Track S) and substitute data (Track P) are separate tracks, never pooled. Outcomes O-1 to O-4 state what each availability answer allows. No dataset is selected; DS-01 to DS-05 are candidates with open licence or structure checks. ISS-002 stays open with explicit assumption AS-09.
- **Targets:** every active Section 8 row has a target (MS-01 to MS-06, MS-08, MS-10; MS-10 new). Retrieval targets are relative to BM25; absolute floors follow the pilot. No result or performance figure exists.
- **Feasibility:** self-hostable candidates with verified licences and input limits; dense-index memory brackets; three patent services with documented access routes (RQ-14 closed); compute to be measured in FT-02. Risks RSK-01 to RSK-14 for Section 17.

## Gate outcome (DEC-031)

CONDITIONAL PASS. Mandatory corrections before the S07 evaluation-methodology freeze: ISS-042 (MS-03 non-inferiority), ISS-043 (pool versus corpus absence in ET-01b, ET-04), ISS-044 (original CQADupStack licence), ISS-045 (whether a higher score than BM25 should be the mandatory acceptance criterion for MS-01, MS-02). S06 may plan the work to make them but must not treat the affected targets as final.

## Owner decisions

**Still open after the S05 gate:** ISS-002 and ISS-003 (what data and R2 sources can be released), ISS-037 (R2/R4 boundary), ISS-033 (external disclosure), ISS-038 (substitute licences; build DS-05 or not).

**Before or during S06:** ISS-039 (planning values PV-01 to PV-11; AS-12 applies until then), ISS-040 (patent service), ISS-013 (effort envelope), ISS-018, ISS-034 to ISS-036. ISS-005, ISS-007 to ISS-010 remain open; AS-01 to AS-12 apply.

## Inputs for S06 (load only these)

| Path | Why |
|---|---|
| `CLAUDE.md`, `project/00_PROJECT_RULES.md`, `project/00_STAGE_STATUS.md`, `project/00_STAGE_GATE_PROTOCOL.md` (§7 S06 row), `project/03_STYLE_GUIDE.md` | Rules and gate |
| `project/00_DECISIONS_LOG.md` (DEC-012, DEC-028, DEC-030 and the S05 gate entry), `project/00_OPEN_ISSUES_REGISTER.md` (ISS-013, ISS-017, ISS-018, ISS-034 to ISS-036, ISS-038 to ISS-045) | Scope, effort envelope, open decisions |
| `stages/S04/S04_ARCHITECTURE.md` §2, §3, §7; `stages/S04/S04_SCOPE_OPTIONS.md` §6 | Functions and components to package |
| `stages/S05/S05_EVALUATION_DESIGN.md` §5 item 5, §7, §9 | Evaluation activities, judging-effort formula, planning values |
| `stages/S05/S05_FEASIBILITY_AND_RISKS.md` §3, §4 | Feasibility tests and risks that work packages must schedule |
| `stages/S05/S05_DATA_AVAILABILITY_AND_SUBSTITUTES.md` §3 | Outcome that applies at S06 start |
| `proposal/DRAFT_SEC08_FEATURES.md`; `project/S01_TRACEABILITY_MATRIX.md` Parts D, F, G | Specifications each work package must deliver evidence for |
| `project/00_SKILL_REGISTER.md` | Skill checkpoint |

## Session start (S06)

> Begin S06 under `CLAUDE.md`. Clone the repository, confirm that the S05 content commit recorded in `project/00_STAGE_STATUS.md` exists and that DEC-031 is recorded, and report any mismatch before anything else. Run `python3 stages/S05/qc/S05_QC_CHECK.py .`; it must pass.

## Carried forward

ISS-029 (full-text checks of A-depth claims, including CLM-047 to CLM-050, S08); ISS-041 (training-data and licence files, S07); ISS-030 to ISS-032 (Section 9, S08–S10); the timed assessor study noted in `S05_EVALUATION_DESIGN` §10 for Section 11.
