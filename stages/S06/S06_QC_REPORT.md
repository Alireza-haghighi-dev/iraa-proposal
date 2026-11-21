# S06_QC_REPORT

| Field | Value |
|---|---|
| Document ID | S06_QC_REPORT |
| Version | 1.0 |
| Status | APPROVED |
| Stage | S06 |
| Date | 2026-11-21 |
| Depends on | 00_STAGE_GATE_PROTOCOL; S06_PLAN; qc/S06_QC_CHECK.py; qc/S06_QC_CHECK_OUTPUT.txt |

## 1. Scripted checks (reproducible)

`python3 stages/S06/qc/S06_QC_CHECK.py .` (Python 3 standard library; reads files only). The script is cumulative: every S04, S04.1 and S05 check, with the S05 check "S06 not started" replaced by "S07 not started", the complete-set check for ISS extended to ISS-048, plus the S06 checks in section 8h. Output: `qc/S06_QC_CHECK_OUTPUT.txt`.

**Result:** see the summary line at the end of the output file (RESULT PASS at the time of commit).

S06 checks added (section 8h): S06 deliverables present; 6 or 7 work packages with sequential, unique identifiers; Section 13 draft uses the form's column schema and repeats every WP number and title verbatim, in order; no development stage S01–S10 used as a work package (DEC-012); task and deliverable identifiers unique, every reference defined, every WP with tasks and at least one deliverable, every deliverable with acceptance evidence and a verification method; every non-conditional task has an effort row and conditional tasks stay out of the planning table; the judging hours recomputed from the S05 formula for the three scenarios; per-WP planning, low and high totals and the grand totals recomputed from the task table and EH-09; Section 13 efforts and total equal the planning figures; person-week conversion, the L-4 figure and the handoff figures recomputed; effort assumptions labelled with their owner issue; no claim that the ISS-013 envelope is met; R1–R4, the ten essential functions, all components except AC-06 and AC-08, all ET tests, FT-01 to FT-05 and RSK-01 to RSK-14 assigned; excluded items (FN-04, FN-07, AC-06, AC-08, CP-2 to CP-4) absent from funded tasks; Section 13 free of grouping, summaries, write-back, production deployment, cost, month and team content, with retraining mentioned only as excluded and the training decision stated; DEC-032 recorded without approving S06; ISS-042 to ISS-045 open, carried with an S06 note and an explicit S07 instruction each; ISS-013 and ISS-018 updated and open; result-language and withdrawn-R2-wording scans over S06 files; traceability Part H rows for R1 to R4; RF-007 status updated. The identifying-data, credential and file-inventory scans cover every repository text file and serve as the pre-commit safety scan.

A negative test was run on a scratch copy (one WP title changed in Section 13, one Section 13 effort changed, one task estimate changed): the script reported each change and the dependent totals as FAIL. The scratch copy was deleted.

## 2. Self-reported checks (performed by reading; not independently verified)

| Check | Method | Result |
|---|---|---|
| Scope fidelity to DEC-028 | Compared every task with the essential set and the exclusions | No live deployment, retraining, grouping, summaries or mandatory labelling in funded tasks; IF-07 specified only |
| R2 without an assumed source | Read WP3, WP2 and Section 13 text | Source registry and substitute DS-05 only; no internal solutions collection assumed |
| R4 disclosure | Read WP4 and Section 13 | CP-1 approval of exact text kept; ET-09 on public need statements under the default |
| No overlap or double counting | Each S05 step E-0 to E-6 and each FT mapped to exactly one task | E-0 → T2.2; E-1 → T2.5; E-2 → T2.3; E-3 → T6.2 and T6.3; E-4 → T6.4; E-5 → T6.3, T6.5; E-6 → T6.6. Workflow-test suite built once (T5.6) and executed once (T6.5) |
| Estimate realism | Read each task's basis | Plausible for a proficient practitioner using existing libraries (EH-02); these are judgements, labelled ASSUMPTION, not benchmarks |
| No invented team, money, dates or sponsor resources | Read all S06 files | None; assessor hours kept sponsor-side and open (ISS-047) |
| Style guide §4 patterns | Read S06 files and the Section 13 draft | No pattern found after the fix in §3 |
| Length budgets (S06_PLAN §4) | Line counts | Within budget (work packages 157, deliverables 65, effort 173, Section 13 31, handoff 52 lines) |

## 3. Defects found and fixed during the stage

| Severity | Defect | Fix |
|---|---|---|
| Minor | L-4 per-query saving stated as 0.9 h; recomputation at planning values gives 0.71 h | Corrected to "about 0.7 h" with the calculation shown; now checked by script |
| Minor | MS-row check in the first script draft required the deliverable ID at the start of the cell and failed on valid rows | Pattern widened to any deliverable ID in the row |
| Note | The Section 7 draft lists an assessor walk-through as part of the evaluation objective, while S06 makes it conditional on assessor time (T6.7) | Recorded for S07/S08 in `S06_HANDOFF` and `S06_WORK_PACKAGES` §5; Section 7 draft not edited in S06 |

## 4. Open items and limitations

| Severity | Item | Tracked |
|---|---|---|
| Note | Effort envelope not stated; figures are conditional and no ceiling is claimed as met | ISS-013 |
| Note | Judging brackets EH-06 to EH-08 are project judgements until the FT-05 pilot | ISS-046 |
| Note | Mandatory S05 corrections not made in S06 by design; MS-01 to MS-03, ET-01b and ET-04 not final | ISS-042 to ISS-045 (S07) |
| Note | Sponsor-side assessor hours and a separate coordination activity await owner decisions | ISS-047, ISS-048 |
| Note | No research in S06; source log and claim register unchanged | — |

No Critical or Major defect is open.

## 5. Gate checklist (00_STAGE_GATE_PROTOCOL)

| Item | Status |
|---|---|
| Plan, work products with metadata | Done |
| Decisions and issues updated | DEC-032; ISS-013, -017, -018, -034, -035, -036, -038, -039, -040, -042 to -045 updated; ISS-046 to ISS-048 added |
| Source log and claim register | Unchanged (no research) |
| Traceability | Part D updated; Part H added |
| RF/QA status | RF-007, QA-001, QA-007 ADDRESSED; RF-006, RF-011, RF-012 SCHEDULED with S06 artifacts |
| Skill checkpoint | SKL-007 (no Skill used) |
| Identifier scheme | Tn.m, Dn.m, M, EH and L added to `00_PROJECT_RULES` §5 |
| Stage status | Updated to SUBMITTED FOR GATE |
| S06 exit criterion | Met except "within the ISS-013 envelope", which cannot be shown while ISS-013 is open; conditional estimates and reductions provided instead |

**Recommended gate outcome:** CONDITIONAL PASS: the work-package structure, identifiers and titles can be frozen now; the effort figures stay provisional until ISS-013, ISS-039 and ISS-046 are decided and the FT-05 pilot values exist.
