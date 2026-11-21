# S11_CHANGE_REPORT

| Field | Value |
|---|---|
| Document ID | S11_CHANGE_REPORT |
| Version | 0.1 |
| Status | APPROVED |
| Stage | S11 |
| Date | 2026-11-21 |
| Depends on | DEC-040; DEC-041; qc/S11_MASTER_REVISION.py; qc/S11_EFFORT_MODEL.py |

| Change | Where | Basis |
|---|---|---|
| Configuration set reduced to BM25, one multilingual encoder and reciprocal rank fusion (primary, fixed in advance); fingerprints as duplicate flag; no tuning of ranking parameters | Master §12 (logic, test design, tool table, activity 3), §13 activity 3, §17 risks 6–9 | S11_SCOPE §1 |
| Evaluation decision rule: two-sided 95% paired bootstrap interval read against the margin and zero; randomization p beside it; prior art as an estimate; Holm, margin-shifted tests and the 0.10 margin removed; "inconclusive" outcome | Master §8 specifications 1–3 and note; §12 activities 2 and 6; limits of the method | S11_SCOPE §1; ISS-049, ISS-055 notes |
| Test sets: 50 + 10 queries (R1); 50 need statements written once, 40 + 10 for R2 and 30 reused for R4; two R4 formulations; deeper check 5 queries to rank 30 | Master §8, §12 activities 2, 4, 6 | ISS-039, ISS-050 notes |
| Corpus sizes 10,000 and 100,000, exact search only; one-million-item statement removed | Master §8 specification 7, §12 activity 3, §17 risk 8 | S11_SCOPE §1 |
| Lightweight interface; framework authentication; randomized test generator and second-approver setting removed | Master §12 activities 1 and 5, §13 activity 5 | S11_SCOPE §1 |
| First-month end-to-end prototype; error analysis and corrective development; final reproducibility check; rehearsal by a member who did not write the deployment scripts | Master §12 activities 1, 6, 7; §13 activities 1, 6, 7 | DEC-041 items 2 and 4; ISS-051 note |
| Provisional effort 1,291 h (WP1 150, WP2 168, WP3 210, WP4 138, WP5 226, WP6 267, WP7 132); six months planned | Master §§4, 13, 16 | S11_EFFORT_AND_SCHEDULE; pending checkpoint |
| References no longer cited removed (Bruch et al., Holm, Malkov and Yashunin, Nogueira and Cho; two model cards) | Master §19 | Citation check |
| Risk 11 and 13 mitigations updated for the six-month plan | Master §17 | S11 model |
| DEC-040, DEC-041; ISS-057; ISS-013, ISS-025, ISS-039, ISS-049, ISS-050, ISS-051, ISS-055 notes; stage status | project/ | Record keeping |

Unchanged: WP identifiers and titles; the 20 sections and every official table header; R1–R4 wording; disclosure and approval controls; data-protection baseline; Section 9 comparators; local placeholders. Historical S04–S07 records are not edited; S11_TRACEABILITY_AND_ACCEPTANCE_IMPACT §4 states where they are superseded in part.
