# S05_PLAN

| Field | Value |
|---|---|
| Document ID | S05_PLAN |
| Version | 1.0 |
| Status | SUBMITTED FOR GATE |
| Stage | S05 |
| Date | 2026-11-20 |
| Depends on | DEC-028; DEC-029; DEC-030; S04.1_HANDOFF; S04.1_R2_REFERENCE_CORRECTION_NOTE; 00_STAGE_GATE_PROTOCOL §7 (S05 row) |

- **Objective:** define how the narrowed Option B prototype (DEC-028) will be tested: metrics, baselines, test sets, judging procedure, acceptance targets, data routes and resource feasibility, with explicit tests for R1, R2 (corrected, DEC-029), R3 and R4. Nothing is built or measured in S05.
- **Exit criterion (gate protocol §7):** metrics, baselines, dataset needs, procedures and acceptance criteria defined and labelled as targets; ISS-002 resolved or an explicit assumption recorded (QA-002, QA-004).

## 1. Start-of-session checks

| Check | Result |
|---|---|
| Baseline SHAs in `00_STAGE_STATUS.md` present in history | All six present (51daa1a, 4c3ddda, ea246ce, 6780335, 961ae6a, 2b5f83c) |
| DEC-028 recorded; settles RC-01 and ISS-001 | Yes |
| `S04.1_QC_CHECK.py` on the start commit a595df1 | PASS (542 checks, 0 failed) |
| R2 operative meaning | Corrected statement (DEC-029; `S04.1_R2_REFERENCE_CORRECTION_NOTE`). No approved internal solutions collection is assumed anywhere in S05 |

## 2. Inputs (loaded as listed in the S04.1 handoff)

Rules, status, gate protocol, style guide; DEC-028, DEC-029, RC-01; ISS-002, ISS-003, ISS-006, ISS-007, ISS-009, ISS-011, ISS-012, ISS-023, ISS-028, ISS-033, ISS-037; requirements register §1, §1a; RQ-06, RQ-07, RQ-14, RQ-15; CLM-025 to CLM-028, CLM-036, CLM-044, CLM-045; S02 synthesis §3–§5 and evidence matrix rows 6.1–6.6; S04 architecture §1, §2, §4, §5; DF-08; assumptions §1; scope §6; Section 8 draft; Skill register; traceability Part F.

## 3. Work steps

1. Targeted research, only where S02 left gaps: significance testing, topic-set size, incomplete judgments and agreement statistics (RQ-06); patent data services and their terms (RQ-14); model licences and input limits (RQ-15); licence status of public substitute data. Every source is logged before use.
2. Evaluation design per requirement (`S05_EVALUATION_DESIGN`).
3. Data routes, sponsor data request and substitute candidates (`S05_DATA_AVAILABILITY_AND_SUBSTITUTES`).
4. Model, tool and external-source feasibility; feasibility tests; implementation risks (`S05_FEASIBILITY_AND_RISKS`).
5. Section 8 targets (`proposal/DRAFT_SEC08_FEATURES` v0.3).
6. Register updates, cumulative QC script, QC report, handoff; commit and push as SUBMITTED FOR GATE (DEC-030).

## 4. Length budgets

| Deliverable | Budget |
|---|---|
| S05_EVALUATION_DESIGN | ≤ 260 lines |
| S05_DATA_AVAILABILITY_AND_SUBSTITUTES | ≤ 120 lines |
| S05_FEASIBILITY_AND_RISKS | ≤ 140 lines |
| S05_HANDOFF | One page |

## 5. Out of scope

S06 work packages and effort; Section 12 prose; any implementation; any numeric performance expectation; team, cost and schedule content (S10).
