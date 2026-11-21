# 00_STAGE_STATUS

| Field | Value |
|---|---|
| Document ID | 00_STAGE_STATUS |
| Version | 6.0 |
| Status | SUBMITTED FOR GATE |
| Stage | S06 |
| Date | 2026-11-21 |
| Depends on | 00_DECISIONS_LOG; 00_OPEN_ISSUES_REGISTER; S06_HANDOFF; DEC-031; DEC-032 |

## Current position

| Item | Value |
|---|---|
| Current stage | S06 submitted for gate (DEC-032); awaiting owner gate decision |
| Latest approved baseline | 350ac4328908610e3c0fce678ead1eb77053dd69 (S05 conditional-pass checkpoint; DEC-031) |
| Earlier baselines | S05 content 83331af94aa058c486ad1150a0472178375e6cf1 (status record 5e75b5e); S03–S04.1 approved checkpoint 51daa1ac37c375736e086dfdec0f1e778966d8be (DEC-028); S04.1 content 4c3ddda872d2c8782a2994e1a122923104e371c7; S04 content ea246cef29c912dbd5a7b205b3a3a64f7f926597; S03 content 67803355fe0a9fd7ef9271718adb5f4b52459315 (approval confirmed in DEC-028); S02 961ae6ad31581eac633304d905cbab1761179b0b (DEC-022); S01 2b5f83c65749a4c697782216026a6291a91aa2a1 |
| Baseline identification | By commit SHA only (DEC-020). No Git tags exist in the repository |
| Planning scope | Narrowed Option B, laboratory prototype, technology development, design + build + test (DEC-028) |
| S05 content | 83331af94aa058c486ad1150a0472178375e6cf1 (approved, CONDITIONAL PASS, DEC-031) |
| S06 content | Submitted for gate; commit SHA reported to the coordinator and recorded here by the gate decision |
| Next stage | S07 — Detailed Technical Methodology (Section 12) |
| S07 may start | No: requires the owner's S06 gate decision (DEC-024) |

## Stage register

| Stage | Title | State | Gate decision |
|---|---|---|---|
| S01 | Research Foundation and Requirements Mapping | Approved; baseline commit 2b5f83c | CONDITIONAL PASS (DEC-015), then APPROVED (DEC-016) |
| S02 | Scientific and Technical Literature Research | Approved; content commit 34a7745 | APPROVED (DEC-022) |
| S03 | Comparable Systems and Prior-Art Analysis | Approved; content commit 6780335 | APPROVED (DEC-026, confirmed DEC-028) |
| S04 | Product Definition and Technical Architecture | Approved as corrected by S04.1 | APPROVED (DEC-028) |
| S04.1 | Consolidated correction and cross-stage audit (S01–S04) | Approved; content commit 4c3ddda | APPROVED (DEC-028) |
| S05 | Technical Feasibility and Evaluation Design | Approved; content commit 83331af | CONDITIONAL PASS (DEC-031); mandatory corrections ISS-042 to ISS-045 before the S07 freeze |
| S06 | Main Activities and Deliverables (Section 13 work packages) | Submitted for gate (DEC-032) | Pending |
| S07 | Detailed Technical Methodology (Section 12) | Not started | — |
| S08 | Proposal Drafting and Intensive Editorial Pass | Not started | — |
| S09 | Independent Critical Review | Not started | — |
| S10 | Team, Financial Planning, Schedule and Final Integration (incl. S10b independent audit) | Not started | — |

## Owner decisions due by stage

| Due before | Issue | Reference |
|---|---|---|
| S06 gate | Acceptance of WP1–WP7 and their frozen titles; separate coordination activity or not | DEC-032; ISS-048 |
| S07 evaluation-methodology freeze | Mandatory S05 corrections | ISS-042, ISS-043, ISS-044, ISS-045 |
| WP2 start (T2.1, T2.3, T2.4) | Data availability; R2 sources and R2/R4 boundary; substitute licences; build DS-05 or not | ISS-002, ISS-003, ISS-037, ISS-038, ISS-044 |
| WP1 acceptance (D1.1 to D1.3) | Assessment content; approval model; accounts; retention | ISS-005, ISS-034, ISS-035, ISS-036 |
| Protocol freeze (T2.2) | Planning values | ISS-039 |
| WP4 (T4.2) | Patent service; external disclosure | ISS-040, ISS-033 |
| S07 | Language; integration; hosting; standards interpretation; training-data and licence files | ISS-007, ISS-008, ISS-009, ISS-010, ISS-041 |
| S08 | Section 9 row selection | ISS-030 |
| S09 | Authorization to run the independent reviewer | ISS-014 |
| S10 | Effort envelope; person-hour convention; training activity; effort assumptions; sponsor-side hours | ISS-013, ISS-017, ISS-018, ISS-046, ISS-047 |

Full list: `00_OPEN_ISSUES_REGISTER.md`.

## Required inputs for the next session

See `stages/S06/S06_HANDOFF.md`, sections "Inputs for S07" and "Session start".
