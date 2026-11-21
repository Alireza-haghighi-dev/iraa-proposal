# 00_STAGE_STATUS

| Field | Value |
|---|---|
| Document ID | 00_STAGE_STATUS |
| Version | 9.0 |
| Status | SUBMITTED FOR GATE |
| Stage | S09 |
| Date | 2026-11-21 |
| Depends on | 00_DECISIONS_LOG; 00_OPEN_ISSUES_REGISTER; S06_HANDOFF; DEC-031; DEC-032; DEC-033; DEC-034; DEC-035; S07_HANDOFF; DEC-036; S08_HANDOFF; DEC-037; S09_HANDOFF |

## Current position

| Item | Value |
|---|---|
| Current stage | S09 SUBMITTED FOR GATE (authorized by DEC-037); awaiting owner gate decision; S10 not started |
| Latest approved baseline | f3265e8192c207ec1f48c802ca7840f504e7b87c (S08 conditional-pass checkpoint; DEC-037) |
| Earlier baselines | S07 conditional-pass checkpoint 267712fa4838c4f69f2e8773efaa29e9e74f732a (DEC-035); S06 conditional-pass checkpoint 2d46990b966db528a39456d7457b23cf918b8f4d (DEC-033); S05 conditional-pass checkpoint 350ac4328908610e3c0fce678ead1eb77053dd69 (DEC-031); S05 content 83331af94aa058c486ad1150a0472178375e6cf1 (status record 5e75b5e); S03–S04.1 approved checkpoint 51daa1ac37c375736e086dfdec0f1e778966d8be (DEC-028); S04.1 content 4c3ddda872d2c8782a2994e1a122923104e371c7; S04 content ea246cef29c912dbd5a7b205b3a3a64f7f926597; S03 content 67803355fe0a9fd7ef9271718adb5f4b52459315 (approval confirmed in DEC-028); S02 961ae6ad31581eac633304d905cbab1761179b0b (DEC-022); S01 2b5f83c65749a4c697782216026a6291a91aa2a1 |
| Baseline identification | By commit SHA only (DEC-020). No Git tags exist in the repository |
| Planning scope | Narrowed Option B, laboratory prototype, technology development, design + build + test (DEC-028) |
| S05 content | 83331af94aa058c486ad1150a0472178375e6cf1 (approved, CONDITIONAL PASS, DEC-031) |
| S06 content | 03f56ddafbca86f52158827b1dc3bacf49852f62 (approved, CONDITIONAL PASS, DEC-033; status record f8bdb0e) |
| S07 content | b534b9afd356c19c7fa36e3b46d4b9f2db1d11f0 (approved, CONDITIONAL PASS, DEC-035; status record 6208f0a) |
| S08 content | f3434164baa1b4060c11831203d4deebfb8540f5 (approved, CONDITIONAL PASS, DEC-037; status record da66531) |
| S09 content | Recorded in the S09 handoff note to the coordinator after push (commit SHA reported in chat and in the follow-up status record) |
| Next stage | S10 — Team, Financial Planning, Schedule and Final Integration |
| S10 may start | No; requires the owner's S09 gate decision |

## Stage register

| Stage | Title | State | Gate decision |
|---|---|---|---|
| S01 | Research Foundation and Requirements Mapping | Approved; baseline commit 2b5f83c | CONDITIONAL PASS (DEC-015), then APPROVED (DEC-016) |
| S02 | Scientific and Technical Literature Research | Approved; content commit 34a7745 | APPROVED (DEC-022) |
| S03 | Comparable Systems and Prior-Art Analysis | Approved; content commit 6780335 | APPROVED (DEC-026, confirmed DEC-028) |
| S04 | Product Definition and Technical Architecture | Approved as corrected by S04.1 | APPROVED (DEC-028) |
| S04.1 | Consolidated correction and cross-stage audit (S01–S04) | Approved; content commit 4c3ddda | APPROVED (DEC-028) |
| S05 | Technical Feasibility and Evaluation Design | Approved; content commit 83331af | CONDITIONAL PASS (DEC-031); mandatory corrections ISS-042 to ISS-045 before the S07 freeze |
| S06 | Main Activities and Deliverables (Section 13 work packages) | Approved; content commit 03f56dd | CONDITIONAL PASS (DEC-033); WP1–WP7 identifiers and titles frozen; effort figures provisional scenarios only |
| S07 | Detailed Technical Methodology (Section 12) | Approved; content commit b534b9a | CONDITIONAL PASS (DEC-035); parameters and licensing decisions provisional; editorial correction ISS-052 due in S08 |
| S08 | Proposal Drafting and Intensive Editorial Pass | Approved; content commit f343416; English master `proposal/IRAA_PROPOSAL_EN_MASTER` accepted as working draft for review | CONDITIONAL PASS (DEC-037); Section 9 rows fixed (ISS-030); PQAI classification to S09 (ISS-054) |
| S09 | Independent Critical Review | SUBMITTED FOR GATE; master v0.2; 31 defects recorded (DEF-009 to DEF-039), no Critical or Major open | Pending |
| S10 | Team, Financial Planning, Schedule and Final Integration (incl. S10b independent audit) | Not started | — |

## Owner decisions due by stage

| Due before | Issue | Reference |
|---|---|---|
| WP2 start (T2.1, T2.3, T2.4) | Data availability; R2 sources and R2/R4 boundary; substitute licences; build DS-05 or not | ISS-002, ISS-003, ISS-037, ISS-038, ISS-044 |
| WP1 acceptance (D1.1 to D1.3) | Assessment content; approval model; accounts; retention | ISS-005, ISS-034, ISS-035, ISS-036 |
| Protocol freeze (T2.2) | Planning values, including PV-12 to PV-15; MS-03 non-inferiority parameters; ET-12 parameters; non-inferiority criterion against the current EMA guideline; significance level alignment | ISS-039, ISS-049, ISS-050, ISS-053, ISS-055 |
| WP4 (T4.2) | Patent service; external disclosure | ISS-040, ISS-033 |
| WP1 pinning (T1.5) | Language; integration; hosting; standards interpretation; training-data and licence terms of the pinned components (Section 12 branches on each answer) | ISS-007, ISS-008, ISS-009, ISS-010, ISS-041 |
| Test run (WP6) | MS-03 option after the pilot | ISS-049 |
| S09 gate | S09 review findings and corrections; confirmation of the corrected comparator classifications | DEC-037; ISS-054 |
| S10b | Authorization to run the independent audit | ISS-014 |
| Local finalization | Native-template inspection, length target, front matter and placeholder removal | ISS-021, ISS-056 |
| S10 | Effort envelope; person-hour convention; training activity; effort assumptions; sponsor-side hours; coordination confirmation; team assignments, availability, costs and duration (owner consultation, DEC-033) | ISS-013, ISS-017, ISS-018, ISS-025, ISS-046, ISS-047, ISS-048, ISS-050 (ET-12 effort), ISS-051 (deployment rehearsal) |

Full list: `00_OPEN_ISSUES_REGISTER.md`.

## Required inputs for the next session

See `stages/S09/S09_HANDOFF.md`, sections "Inputs for S10" and "Session start".
