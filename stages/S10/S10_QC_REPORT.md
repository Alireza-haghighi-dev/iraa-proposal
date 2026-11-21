# S10_QC_REPORT

| Field | Value |
|---|---|
| Document ID | S10_QC_REPORT |
| Version | 0.2 |
| Status | DRAFT |
| Stage | S10 |
| Date | 2026-11-21 |
| Depends on | qc/S10_QC_CHECK.py; qc/S10_QC_CHECK_OUTPUT.txt; 00_STAGE_GATE_PROTOCOL §6 |

- **Command:** `python3 stages/S10/qc/S10_QC_CHECK.py . <path to PROPOSAL_FORM_EN_WORKING_V1.md>` (the form file is a Claude Project document, not in this repository; without the path the script uses its embedded copy of the header rows). Output: `qc/S10_QC_CHECK_OUTPUT.txt`.
- **Class:** all checks listed in the output are scripted (reproducible). Statements in `S10_CONSISTENCY_REPORT` marked "read" are self-reported.
- **Result:** see the SUMMARY line of the output. FX-02 runs and passes on the approved baseline; FX-03 to FX-05 are PENDING until the personnel and cost inputs arrive and are not counted as passes.
- **Cumulative:** the script runs the approved S11 suite (which runs S09, S08, S07 and the safety scan) and accepts by name only the pre-approval S11 conditions made obsolete by DEC-042 and the earlier-stage checks they replaced, each with its reason in the script.
- **Open defects:** DEF-005, DEF-008, DEF-025, DEF-028 (Minor or Note; owner or local decisions). No Critical or Major defect is open.
- **Not verified:** native Word layout (template unavailable); meaning and writing quality (S10b, not authorized).
- **Recommended outcome:** none yet; S10 continues after the owner's answers.
- **Negative test:** on a scratch copy, one Section 12 title and the OPS family-related clause were altered; the script reported both as FAIL (FX-01 and the OPS FAQ check) and the copy was deleted.
- **Negative test (resumption):** on a scratch copy, one Section 16 month mark was added to activity 7; the script reported the Gantt check as FAIL; the copy was deleted.
