# 03_DEFECT_LOG

| Field | Value |
|---|---|
| Document ID | 03_DEFECT_LOG |
| Version | 1.0 |
| Status | SUBMITTED FOR GATE |
| Stage | S08 |
| Date | 2026-11-21 |
| Depends on | 00_PROJECT_RULES §5; 00_STAGE_GATE_PROTOCOL §6; S08_EDITORIAL_LOG; DEC-035 |

- **Purpose:** defects found in proposal text or working registers from S08 onwards. Severity: Critical / Major / Minor / Note (gate protocol §6). A defect is closed only by a recorded fix or an owner decision.

| ID | Stage found | Location | Defect | Severity | Fix / disposition | Status |
|---|---|---|---|---|---|---|
| DEF-001 | S08 | Sections 7, 8 (feature 5, MS-05), 12 (intro, activity 4); S04_ARCHITECTURE CP-1 | Assessor query approval presented as the control that applies while external disclosure is not authorized; approval does not authorize disclosure (DEC-035, ISS-052) | Major | Master rewritten: confidential text is sent only with a disclosure clearance and an approved query; withdrawn phrasings checked absent by script; S04_ARCHITECTURE CP-1 row v2.0 | FIXED (S08) |
| DEF-002 | S08 | S04_DATA_FLOWS_AND_INTERFACES (IF-03, DF table, sequence note); S05_EVALUATION_DESIGN (MS-05 target, ET-08); S06_DELIVERABLES_AND_ACCEPTANCE (D4.1, MS-05 row); S06_DEPENDENCIES_AND_EFFORT (CP-1 notes) | Working registers keep the pre-DEC-035 conditional description of CP-1 and the conditional MS-05 | Minor | Governed by the S04_ARCHITECTURE CP-1 row and the master (stated in both); register wording aligned at S10 integration | OPEN |
| DEF-003 | S08 | CLM-017 (SRC-010) | "Median 17–42%" overestimation figure not found at the depth reached in Pass A | Minor | Figure not used in the master; qualitative statement only | FIXED (S08) |
| DEF-004 | S08 | CLM-019 (SRC-015) | Count of three problem–solution matching studies not confirmed | Minor | Claim not used in the master | FIXED (S08) |
| DEF-005 | S08 | Section 12 activity 2; SRC-087, SRC-088 | EMA lists CPMP/EWP/482/99 as superseded by the guideline on non-inferiority and equivalence comparisons | Minor | Master states the supersession; check of the criterion against the current guideline before the protocol freeze (ISS-053) | OPEN |
| DEF-006 | S08 | Section 5 (DRAFT_SEC05 v0.2) | Comparator counts referred to Section 9 although two of the five duplicate-suggestion products are not Section 9 rows | Minor | Counts restated against the Section 9 rows in the master | FIXED (S08) |
| DEF-007 | S08 | Section 9 row 5 (S03 row 5) | PQAI organization descriptor relied on a T3 source (SRC-054), which may not be the sole support for comparator statements | Note | Descriptor reduced to "PQAI open-source project" | FIXED (S08) |
| DEF-008 | S08 | Whole master | Native Word template not inspected; RF-001/RF-003 compliance shown in Markdown only | Note | Formatting pending local finalization (ISS-021); no pixel-level claim | OPEN |
