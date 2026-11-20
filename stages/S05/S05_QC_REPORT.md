# S05_QC_REPORT

| Field | Value |
|---|---|
| Document ID | S05_QC_REPORT |
| Version | 1.0 |
| Status | APPROVED |
| Stage | S05 |
| Date | 2026-11-20 |
| Depends on | 00_STAGE_GATE_PROTOCOL; S05_PLAN; qc/S05_QC_CHECK.py; qc/S05_QC_CHECK_OUTPUT.txt |

## 1. Scripted checks (reproducible)

`python3 stages/S05/qc/S05_QC_CHECK.py .` (Python 3 standard library; reads files only). The script is cumulative: every S04 and S04.1 check, with the S04.1 check "S05 not started" replaced by "S06 not started", plus the S05 checks in section 8g. Output: `qc/S05_QC_CHECK_OUTPUT.txt`.

**Result:** see the summary line at the end of the output file (RESULT PASS at the time of commit).

S05 checks added (section 8g): S05 deliverables present; ET, PV, DR, DS, FT and RSK identifiers unique and every reference defined; at least one explicit test under each of R1, R2, R3 and R4; the R2 section uses the corrected statement (DEC-029) and assumes no source; Track S and Track P defined and never pooled; no substitute dataset selected and every DS row carries licence and open-check cells; planning values labelled ASSUMPTION and linked to ISS-039; AS-09 to AS-12 linked to issues; MS-01 to MS-10 present, MS-07 and MS-09 kept conditional, MS-01 to MS-03 relative to a baseline; result-language scan (achieved, outperform, demonstrated, "we found/measured/observed") over S05 files and the Section 8 draft; dense-index memory table recomputed from N × d × 4 bytes; R4 volume arithmetic consistent with PV-08; claims CLM-051, CLM-053, CLM-054 not supported by T3 sources alone, and the T3-only statement in CLM-052 kept OPEN; DEC-030 recorded without approving S05; ISS-002 carries an explicit assumption (S05 exit criterion); withdrawn R2 wording absent from S05 files; traceability Part G rows for R1 to R4. Existing scans were extended to S05 files: superiority, certification, inflated language, source-log integrity and "every S05 source cited in an S05 deliverable". The identifying-data, credential and file-inventory scans cover every repository text file and serve as the pre-commit safety scan.

## 2. Self-reported checks (performed by reading; not independently verified)

| Check | Method | Result |
|---|---|---|
| Fidelity of source statements | Each statement in S05 deliverables and CLM-047 to CLM-055 compared with the extract or page read during the session | Consistent after the fixes in §3; depth recorded as A, with search-result extracts flagged in the source log |
| No invented data, results, permissions | Read all S05 files for dataset names, figures and permission statements | No dataset selected; no performance figure; all numbers are planning values (PV, labelled), stated limits from sources, or arithmetic |
| R2 interpretation | Read R2 sections against `S04.1_R2_REFERENCE_CORRECTION_NOTE` | Corrected meaning used; source type is a reported condition; R2/R4 boundary left to ISS-037 |
| Consistency with DEC-028 scope | Compared tests with the essential set | No test for FN-04, FN-07 or mandatory CP-2; MS-07 and MS-09 not set |
| Style guide §4 patterns | Read S05 files | Two scan findings fixed (§3); no further pattern found by reading |
| Length budgets (S05_PLAN §4) | Line counts | Within budget (see output inventory) |

## 3. Defects found and fixed during the stage

| Severity | Defect | Fix |
|---|---|---|
| Minor | An unbacked evaluative qualifier in CLM-049 and in the evaluation design (inflated-language scan) | Reworded to the specific property (sensitivity to missing judgments) |
| Minor | "better than" in Section 8 targets (superiority scan) | Targets restated as "higher [metric] than the BM25 baseline" |
| Minor | Source-log rows for SRC-066 to SRC-072 and SRC-078 implied direct page reading where only search-result extracts were read | Limitations cells now say "via search-result extract" |
| Minor | OPS fair-use threshold stated without the source's own qualifier | Qualifier added ("may vary with operational circumstances") |
| Note | Inherited source checks only covered S04 files | Extended to S05 (orphan check and per-stage citation check) |

## 4. Open items and limitations

| Severity | Item | Tracked |
|---|---|---|
| Note | All S05 sources are at A depth; several read through search-result extracts. Full-text checks before proposal use | ISS-029 |
| Note | SRC-063 record and the EPO OPS landing page could not be fetched; SRC-063 structure and licence unverified | ISS-038 |
| Note | Licence of CQADupStack on its original distribution not read; third-party statement only (T3) | ISS-038 |
| Note | Model training-data terms and Pyserini/Faiss licence files not read | ISS-041 |
| Note | Planning values PV-01 to PV-11 are project choices awaiting owner confirmation | ISS-039 |

No Critical or Major defect is open.

## 5. Gate checklist (00_STAGE_GATE_PROTOCOL)

| Item | Status |
|---|---|
| Plan, work products with metadata | Done |
| Decisions and issues updated | DEC-030; ISS-002, -003, -006, -007, -011, -012, -023, -028, -033, -037 updated; ISS-038 to ISS-041 added |
| Source log and claim register | SRC-066 to SRC-081; CLM-047 to CLM-057; CLM-026 to CLM-028, CLM-036, CLM-045 updated |
| Traceability | Part G added; Part E rows for RQ-06, RQ-14, RQ-15 |
| RF/QA status | QA-002 and QA-004 ADDRESSED (design); QA-010 SCHEDULED for S07 |
| Skill checkpoint | SKL-006 (no Skill used) |
| Stage status | Updated; content commit 83331af recorded |
| S05 exit criterion | Metrics, baselines, dataset needs, procedures and acceptance criteria defined and labelled as targets; ISS-002 carries explicit assumption AS-09 |

**Recommended gate outcome:** PASS, with the owner decisions listed in `S05_HANDOFF` taken at or after the gate. None of them blocks S06 because AS-01 to AS-12 cover each one.
