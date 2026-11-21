# S11_QC_REPORT

| Field | Value |
|---|---|
| Document ID | S11_QC_REPORT |
| Version | 0.1 |
| Status | APPROVED |
| Stage | S11 |
| Date | 2026-11-21 |
| Depends on | qc/S11_QC_CHECK.py; qc/S11_QC_CHECK_OUTPUT.txt; qc/S11_EFFORT_MODEL.py; 00_STAGE_GATE_PROTOCOL §6 |

- **Command:** `python3 stages/S11/qc/S11_QC_CHECK.py . <path to PROPOSAL_FORM_EN_WORKING_V1.md>`; output in `qc/S11_QC_CHECK_OUTPUT.txt`. Result: 76 checks, 0 failures; FX-02 to FX-05 remain pending (owner inputs).
- **Cumulative:** runs the S09 suite (with S08, S07 and the safety scan inside it) and the S10 suite. Failures caused by deliberate S11 design changes are accepted only by name, each with its reason in the script and a replacing S11 check (25 accepted conditions are defined: 6 for S08, 12 for S09, 7 for S10).
- **Scripted checks:** removed elements absent and S11 wording present in the master; control wording preserved; no internal capability or training statements in the proposal text; reference list without uncited entries; body length not above v0.3; Section 13 and 16 effort equal to the model; titles identical across Sections 12, 13, 16 and the model; month 1 lightest; lead peak ≤ 110 h; corrective work in month 6; one review line per work package and one coordination line (EH-10); every table in S11_EFFORT_AND_SCHEDULE regenerated from the model; registers and deliverables.
- **Negative test:** on a scratch copy, one Section 13 figure and the rehearsal wording were altered; the script reported four failures (both cumulative suites, the S11 wording check and the Section 16 equality check). The copy was deleted.
- **Register repair:** S10 notes had been appended after the OPEN status of 14 issues (S10 and S11 notes), which broke the S06/S07 "still open" checks; the notes were moved into the timing column and the status cells restored to OPEN.
- **Self-reported, not scripted:** the engineering judgments behind each task figure; the technical adequacy of the reduced scope (S11_SCOPE_AND_TECHNICAL_PLAN §3 gives the reasoning). An independent check would be part of S10b, which is not authorized.
- **Recommended outcome:** owner checkpoint (DEC-041 item 8).
