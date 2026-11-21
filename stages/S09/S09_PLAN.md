# S09_PLAN

| Field | Value |
|---|---|
| Document ID | S09_PLAN |
| Version | 1.0 |
| Status | SUBMITTED FOR GATE |
| Stage | S09 |
| Date | 2026-11-21 |
| Depends on | DEC-037; S08_HANDOFF; 00_STAGE_GATE_PROTOCOL §5–§7; IRAA_PROPOSAL_EN_MASTER v0.1 (baseline f3265e8) |

- **Authorization:** DEC-037 item (4); owner instruction START_STAGE S09 (2026-11-21). S10 is not started.
- **Object of review:** `proposal/IRAA_PROPOSAL_EN_MASTER.md` at the approved baseline f3265e8 (v0.1; 12,874 words by Python whitespace split, the count used by the S09 script and close to the owner's figure; 12,750 by `wc -w`, which treats some Unicode spacing differently).

## Inputs

`CLAUDE.md`; `project/00_PROJECT_RULES.md`, `00_STAGE_STATUS.md`, `00_STAGE_GATE_PROTOCOL.md`, `03_STYLE_GUIDE.md`, `03_DEFECT_LOG.md`, `S01_REVIEWER_CRITERIA_REGISTER.md`, `02_CLAIM_REGISTER.md`, `02_SOURCE_LOG.md`, `00_OPEN_ISSUES_REGISTER.md`; `stages/S08/S08_HANDOFF.md`, `S08_EDITORIAL_LOG.md`, `S08_QC_REPORT.md`; REF-01 to REF-03 and the R2 correction note (Claude Project, read-only). `S07_CORRECTED_EVALUATION_METHODOLOGY` §2 and §6 were read for one specific check (the non-inferiority decision rule).

## Method

1. Start checks: baseline f3265e8 and S08 content f343416 present; DEC-037 recorded; S08 QC script passes (92 checks, 0 failures).
2. Two review passes. (a) Fresh-session review by this stage thread, which did not draft the master. (b) An isolated reviewer agent given only the baseline master, a form-and-requirements digest, the style guide and the reviewer criteria register, with no drafting history (S08 handoff rule). The agent is a separate model instance launched from this session; it is not an external human reviewer, and independence is limited accordingly.
3. Priority order (DEC-037): form and table fidelity; primary-source accuracy; concise English; template fit; comparator claims and classifications (ISS-054); EMA guidance status and statistics (ISS-053).
4. Primary-source re-reads of the consequential statements, with the depth reached recorded per source.
5. Defects recorded with severity, location, evidence, correction and whether required before S10. Critical and Major defects fixed in the master or marked unresolved.
6. Cumulative QC script `qc/S09_QC_CHECK.py` (runs S08, accepts only listed supersessions, adds S09 checks).

## Length budget

S09 deliverables: review report and correction report, each within about three pages; handoff one page. The master may not grow through corrections by more than the words needed; repetition is cut where it carries no additional technical content.

## Out of scope

Team, effort, costs, schedule, local administrative fields (S10, owner consultation); localization; inspection of the native Word template (not available in this session).
