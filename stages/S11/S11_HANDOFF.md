# S11_HANDOFF

| Field | Value |
|---|---|
| Document ID | S11_HANDOFF |
| Version | 0.1 |
| Status | APPROVED |
| Stage | S11 |
| Date | 2026-11-21 |
| Depends on | DEC-041; S11_EFFORT_AND_SCHEDULE; S11_SCOPE_AND_TECHNICAL_PLAN; S11_QC_REPORT; S10_HANDOFF |

- **Status:** S11 APPROVED (DEC-042). Scope, 1,291 h, WP split, six months and the month distribution are frozen. Not submission-ready.
- **Owner decisions at the checkpoint:** (1) approve or amend the revised scope; (2) approve the 1,291 h and its WP split; (3) Section 13 effort convention, full figure or without coordination (ISS-057); (4) confirm the revised planning values (ISS-039, ISS-049, ISS-050, ISS-055 notes); (5) state whether the technical lead can give about 110 h in months 3–4 (about 27 h per week), or choose the 90 h or 80 h adjustment in S11_EFFORT_AND_SCHEDULE §5; (6) rehearsal arrangement (ISS-051).

## Resuming S10 after approval

1. Record the checkpoint decision as a DEC entry.
2. Remove "(provisional)" only where the owner approved the figures; mark the Section 16 months from the approved month allocation (WP × month table) and compute weights once costs are known.
3. Complete Sections 14 and 15 from the remaining S10 decision-request items (rates, non-personnel items, cost rules, member responsibilities and hours; fourth member's details); S10 item 1 is superseded by this checkpoint.
4. Extend `stages/S10/qc/S10_QC_CHECK.py` so FX-02 to FX-05 run; run S11 and S10 QC; update S10 deliverables; push S10 as SUBMITTED FOR GATE.
