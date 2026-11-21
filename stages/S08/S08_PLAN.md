# S08_PLAN

| Field | Value |
|---|---|
| Document ID | S08_PLAN |
| Version | 1.0 |
| Status | APPROVED |
| Stage | S08 |
| Date | 2026-11-21 |
| Depends on | DEC-035; S07_HANDOFF; 00_STAGE_GATE_PROTOCOL §7 (S08 row) |

- **Authorization:** DEC-035 (S08 authorized; started by owner instruction START_STAGE S08, 2026-11-21).
- **Start checks:** baseline 267712f and S07 content b534b9a present in history; S07 QC script passed (1,097 checks, 0 failures) before any change.

## Scope

1. Assemble the English master `proposal/IRAA_PROPOSAL_EN_MASTER` with the 20 form sections in order and the REF-02 table schemas unchanged.
2. Apply passes A to E once to the assembled text (`S08_EDITORIAL_LOG`); no alternative full drafts.
3. Apply the mandatory corrections: ISS-052 disclosure rule; corrected R2; S07 methodology and open planning values; Section 9 as a provisional selection (ISS-030); no team, effort, cost, schedule or local details beyond placeholders.
4. Update affected registers; create `03_DEFECT_LOG`; QC script `qc/S08_QC_CHECK.py` (cumulative through S07, plus S08 checks); QC report, change report, handoff.

## Out of scope

New literature search; architecture or scope changes; Persian text; Sections 14 to 16 content; S09.

## Length budget

Master: proposal text of about 12,000 words, most of it Section 12 (carried from S07 at similar length). Stage records: editorial log, QC report and change report about two pages each; handoff one page.
