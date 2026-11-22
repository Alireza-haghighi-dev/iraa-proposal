# S10_QC_REPORT

| Field | Value |
|---|---|
| Document ID | S10_QC_REPORT |
| Version | 0.4 |
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
- **Native-form QC (DEC-043):** `python3 -I stages/S10/qc/S10_FORM_QC.py <blank form> proposal/IRAA_PROPOSAL_EN_FORM.docx proposal/IRAA_PROPOSAL_EN_MASTER.md` → 112 checks, 0 failures, 1 pending (Section 16 costs and weights). It compares header, footer, styles, numbering, settings and page setup; the 20 headings; for each of the 10 tables the properties, grid widths, header rows, merges and the order of original rows, and requires every added row to clone an adjacent row; then cross-checks Sections 12/13/16 titles, effort and months, Section 14 shares, Section 15 (no amounts), Sections 5, 9, 10, 11, 17 content, narrative formatting (12 pt, regular, no numbering), guidance removal, local placeholders and claim wording. The file was also validated against the OOXML schema and rendered to PDF (33 pages) for a visual check.
- **Negative test (form):** removing one vertical merge in Section 15 and adding a month-7 mark in Section 16 produced three failures; the test copy was deleted.
- **Not established by a structural PASS:** cost inputs, local completion, the signed original's formatting, S10b.
- **Correction pass (DEC-044):** form QC 121 checks, 0 failures, 1 pending (Section 16 costs and weights); corrected form SHA-256 848ba4df04aed44c86cb732ae841fcf9bcc7599496406036b1875f9fe92c2511; blank form SHA-256 8bc63dabdbddff9c8deb78fdd6ab336fde198f33f57b2652fb1a8d6c5fddc267. OOXML validation passed; rendered to PDF (37 pages) and Sections 8, 9, 13, 14, 15, 16 and 17 inspected.
- **Negative tests (correction pass):** a second Section 8 table (1 failure), a deleted original table (stops with FAIL), an altered specification cell (2 failures), a Section 13 cell at 10 pt (1 failure) and restored "await owner confirmation" wording (1 failure). Test copies deleted.
- **S10 suite:** 106 checks, 0 failures, 1 pending; includes the approved monthly totals and lead row.
