# S10_HANDOFF

| Field | Value |
|---|---|
| Document ID | S10_HANDOFF |
| Version | 0.3 |
| Status | DRAFT |
| Stage | S10 |
| Date | 2026-11-21 |
| Depends on | DEC-039; S10_OWNER_DECISION_REQUEST; S10_UNRESOLVED_ITEMS; S10_QC_REPORT |

- **Finalization status (2026-11-22):** native-form insertion done (DEC-043): `proposal/IRAA_PROPOSAL_EN_FORM.docx` passes the structural form QC (112 checks, 0 failures; costs pending). Submitted for an owner gate on the insertion. S10 IN PROGRESS on the approved S11 baseline (DEC-042). Technical integration, Section 4, Section 13, Section 16 months and Section 11 row 1 complete; personnel, budget, Section 16 costs and weights, Section 10 and local fields outstanding; native template not inspected; S10b not authorized. **Not submission-ready.**
- **Interim commit:** recorded in the commit message and the coordinator report (a file cannot hold its own commit SHA).

## Done in this package

Master v0.3 with the OPS, statistical-level and citation corrections; DEF-002 register alignment; section drafts superseded; form mapping with the remaining template-insertion list; unresolved-items register; one owner-decision request with a recomputed provisional effort proposal (2,049 h); QC script and output.

## Next session or continuation

1. Read the owner's answers to `S10_OWNER_DECISION_REQUEST` v0.2 (items 1–9) and record them as a DEC entry, quoting only what the owner stated.
2. Fill Sections 10, 11 rows 2–4, 14, 15 (types and quantities; amounts local) and the Section 16 weights with the formulas in `S10_RESOURCE_CALCULATIONS`; update risk 14; remove the corresponding `[OPEN — S10]` markers.
3. Extend `qc/S10_QC_CHECK.py` so that FX-03 to FX-05 run instead of reporting PENDING; run it with the REF-02 path.
4. Update the consistency report, unresolved items, change report and this handoff; push as SUBMITTED FOR GATE; report; stop. S10b runs only with owner authorization.
