# 00_STAGE_STATUS

| Field | Value |
|---|---|
| Document ID | 00_STAGE_STATUS |
| Version | 5.0 |
| Status | SUBMITTED FOR GATE |
| Stage | S05 |
| Date | 2026-11-20 |
| Depends on | 00_DECISIONS_LOG; 00_OPEN_ISSUES_REGISTER; S05_HANDOFF |

## Current position

| Item | Value |
|---|---|
| Current stage | S05 submitted for gate (DEC-030); awaiting owner gate decision |
| Latest approved baseline | 51daa1ac37c375736e086dfdec0f1e778966d8be (S03, S04 and S04.1 approved checkpoint; DEC-028) |
| Earlier baselines | S04.1 content 4c3ddda872d2c8782a2994e1a122923104e371c7; S04 content ea246cef29c912dbd5a7b205b3a3a64f7f926597; S03 content 67803355fe0a9fd7ef9271718adb5f4b52459315 (approval confirmed in DEC-028); S02 961ae6ad31581eac633304d905cbab1761179b0b (DEC-022); S01 2b5f83c65749a4c697782216026a6291a91aa2a1 |
| Baseline identification | By commit SHA only (DEC-020). No Git tags exist in the repository |
| Planning scope | Narrowed Option B, laboratory prototype, technology development, design + build + test (DEC-028) |
| S05 submitted content | 83331af94aa058c486ad1150a0472178375e6cf1 (SUBMITTED FOR GATE; DEC-030) |
| Next stage | S06 — Main Activities and Deliverables |
| S06 may start | No: requires the owner's S05 gate decision recorded in the decisions log |

## Stage register

| Stage | Title | State | Gate decision |
|---|---|---|---|
| S01 | Research Foundation and Requirements Mapping | Approved; baseline commit 2b5f83c | CONDITIONAL PASS (DEC-015), then APPROVED (DEC-016) |
| S02 | Scientific and Technical Literature Research | Approved; content commit 34a7745 | APPROVED (DEC-022) |
| S03 | Comparable Systems and Prior-Art Analysis | Approved; content commit 6780335 | APPROVED (DEC-026, confirmed DEC-028) |
| S04 | Product Definition and Technical Architecture | Approved as corrected by S04.1 | APPROVED (DEC-028) |
| S04.1 | Consolidated correction and cross-stage audit (S01–S04) | Approved; content commit 4c3ddda | APPROVED (DEC-028) |
| S05 | Technical Feasibility and Evaluation Design | Submitted for gate; content commit 83331af | Pending |
| S06 | Main Activities and Deliverables (Section 13 work packages) | Not started | — |
| S07 | Detailed Technical Methodology (Section 12) | Not started | — |
| S08 | Proposal Drafting and Intensive Editorial Pass | Not started | — |
| S09 | Independent Critical Review | Not started | — |
| S10 | Team, Financial Planning, Schedule and Final Integration (incl. S10b independent audit) | Not started | — |

## Owner decisions due by stage

| Due before | Issue | Reference |
|---|---|---|
| S05 gate | Data availability; R2 sources and R2/R4 boundary; external query disclosure; substitute licences and the constructed R2 set | ISS-002, ISS-003, ISS-037, ISS-033, ISS-038 |
| S06 | Duration and effort envelope; training activity; approval model; accounts; retention; planning values; patent service | ISS-013, ISS-018, ISS-034, ISS-035, ISS-036, ISS-039, ISS-040 |
| S06–S07 | Assessment content; language; integration; hosting; standards interpretation | ISS-005, ISS-007, ISS-008, ISS-009, ISS-010 |
| S07 | Training-data and licence-file checks | ISS-041 |
| S08 | Section 9 row selection | ISS-030 |
| S09 | Authorization to run the independent reviewer | ISS-014 |

Full list: `00_OPEN_ISSUES_REGISTER.md`.

## Required inputs for the next session

See `stages/S05/S05_HANDOFF.md`, sections "Inputs for S06" and "Session start".
