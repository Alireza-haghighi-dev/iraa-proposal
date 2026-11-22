# S10_CHANGE_REPORT

| Field | Value |
|---|---|
| Document ID | S10_CHANGE_REPORT |
| Version | 0.3 |
| Status | DRAFT |
| Stage | S10 |
| Date | 2026-11-21 |
| Depends on | DEC-039; 03_DEFECT_LOG; qc/S10_ALIGN.py |

| Change | Files | Reason |
|---|---|---|
| OPS rate-limit sentence rewritten: thresholds described as guidance values, not fixed limits; charter values (about 1 Mbit per second, 4 GB per week free, yearly subscription above) and FAQ values (ten searches per minute per IP address as a rule, one request per second for family-related actions, operational variation) attributed separately | Master §12 activity 4; CLM-051; SRC-072 | DEC-039 item 1; full FAQ and charter re-read 2026-11-21 (DEF-040) |
| Significance-level question stated in the text with both options | Master §12 activity 2 | DEC-039 item 1, flag unresolved experimental decisions (DEF-041, ISS-055) |
| Malkov and Yashunin cited as the 2020 TPAMI article with DOI; Rakha et al. confirmed without DOI | Master §12, §19; SRC-035; SRC-010 | DEF-029 |
| Tool-table status cells shortened without changing content | Master §12 | Offset added words (S09 reduction plan item) |
| CP-1, MS-05, D4.1, retention and OPS wording aligned with the master; files moved to a new major version, status DRAFT, stage S10 | S04_DATA_FLOWS_AND_INTERFACES, S04_ARCHITECTURE, S05_EVALUATION_DESIGN, S05_FEASIBILITY_AND_RISKS, S06_DELIVERABLES_AND_ACCEPTANCE, S06_DEPENDENCIES_AND_EFFORT, S07_TOOL_AND_VERSION_REGISTER, S07_WP_METHOD_TRACEABILITY | DEF-002 (applied by `qc/S10_ALIGN.py`) |
| Six section drafts marked SUPERSEDED by the master | proposal/DRAFT_SEC05 to DRAFT_SEC13 | DEF-002 (DRAFT_SEC12 carried the old OPS and retention wording) |
| Master v0.3, DRAFT; front matter states S10 status and not submission-ready | Master | DEC-039 item 5 |
| Registers: DEC-039; DEF-002 and DEF-029 fixed, DEF-040 and DEF-041 added; ISS notes; SKL-011; stage status | project/ | Record keeping |
| Body length 12,594 → 12,622 words (+28) | Master | Within the S10 allowance of 50 words |

## Resumption on the approved S11 baseline (DEC-042)

| Change | Files | Reason |
|---|---|---|
| Effort labels "(provisional)" removed; Section 4 = 6 months and 1,291 h; Section 11 row 1 = 6; Section 13 total note restated | Master v0.5 | DEC-042 items 1–3 |
| Section 16 months 1–6 marked from the approved month distribution; months 7–12 blank; explanatory note | Master §16 | DEC-042 item 4 (applied by `qc/S10_APPLY_S11_BASELINE.py`) |
| Risk 13 restated; risk 15 added for the technical lead's planned capacity | Master §17 | DEC-042 item 9 |
| Decision request v0.2 (nine remaining inputs); resource calculations with formulas for Sections 14–16 | S10_OWNER_DECISION_REQUEST, S10_RESOURCE_CALCULATIONS | DEC-042 next step |
| QC rebuilt on the approved baseline: runs the S11 suite (which runs S09, S08, S07) and checks FX-02, the Gantt marks, dependencies and the new documents; S11 suite skips its call back to S10 when run from it | qc/S10_QC_CHECK.py; stages/S11/qc/S11_QC_CHECK.py | Avoids circular suites |
| Registers: DEC-042; ISS-013, ISS-018, ISS-046, ISS-048, ISS-049, ISS-050, ISS-055, ISS-057 resolved; ISS-025, ISS-039, ISS-051 notes; S11 files APPROVED; stage status | project/; stages/S11 | Record keeping |

## Native-form insertion (DEC-043, 2026-11-22)

| Change | Files | Reason |
|---|---|---|
| Filled native form built from the master | proposal/IRAA_PROPOSAL_EN_FORM.docx; qc/S10_BUILD_FORM_DOCX.py | DEC-043 items 1–3 |
| Cell-by-cell structural and content QC against the blank form | qc/S10_FORM_QC.py; qc/S10_FORM_QC_OUTPUT.txt; qc/S10_FORM_ADDED_ROWS.txt | DEC-043 QC requirement |
| Master v0.6: Section 14 four member rows (526 h; 255 h each; shares 40.7/19.8/19.8/19.7; planned monthly averages); Section 15 personnel quantity and pending items; Section 17 reordered into the native form's categories with a sixteenth "Other" row; risk cross-references updated; Faiss row corrected to exact search (S11) | proposal/IRAA_PROPOSAL_EN_MASTER.md; qc/S10_FORM_ALIGN_MASTER.py | DEC-043 items 7–8; consistency |
| S11 month table and WP × month table recomputed with controlled rounding; the WP × month table now includes attributed coordination, so rows equal the approved WP totals and columns the month totals (month 1 team total 147, month 2 243; per-contributor values to one decimal) | stages/S11/qc/S11_EFFORT_MODEL.py; stages/S11/S11_EFFORT_AND_SCHEDULE.md | DEC-043 item 9; approved totals unchanged |
| Resource calculations: monthly averages 87.7 and 42.5 h; DEC-043 split | S10_RESOURCE_CALCULATIONS | DEC-043 item 7 |
| DEC-043; ISS-021, ISS-025, ISS-056 notes; stage status | project/ | Record keeping |
