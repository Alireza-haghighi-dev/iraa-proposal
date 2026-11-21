# S10_OWNER_DECISION_REQUEST

| Field | Value |
|---|---|
| Document ID | S10_OWNER_DECISION_REQUEST |
| Version | 0.1 |
| Status | DRAFT |
| Stage | S10 |
| Date | 2026-11-21 |
| Depends on | DEC-033; DEC-039; S06_DEPENDENCIES_AND_EFFORT; REF-02 §§4, 11, 13–16; ISS-013, ISS-017, ISS-018, ISS-025, ISS-046 to ISS-048, ISS-050, ISS-051 |

- **Purpose:** the single owner-decision request of S10 (DEC-039 item 3). Sections 4, 11 (durations), 13 (final effort), 14, 15 and 16 are completed only from the answers. Nothing below is assumed.
- **How to answer:** reply by item number. "Default" means the option S10 would apply if you confirm it; no default is applied without your confirmation.
- **Local fields:** names, qualifications, currency amounts, dates and contact details stay local. Where a calculation needs rates, relative values are enough.

## A. Effort basis (Sections 4, 13)

| No. | Decision | Options | Default proposed |
|---|---|---|---|
| 1 | Total effort basis | (a) Accept the recomputed provisional figure in §1 below (2,049 h); (b) set an effort envelope, and S10 applies the reductions L-1 to L-5 to fit it; (c) another figure with a stated reason | (a) |
| 2 | Person-hour convention | Month = 4 weeks; full-time = 45 h per week (implied by the form's Section 13 example) or another weekly figure | 4 weeks; weekly figure from you |
| 3 | Sponsor assessor hours | Recorded outside the funded effort, or included in Section 13 | Outside (no assessor time is assumed) |
| 4 | Coordination and training | Coordination stays inside the seven activities; no training activity, unless a sponsor rule requires either | Both as stated |

## B. Team (Section 14)

| No. | Decision | What is needed |
|---|---|---|
| 5 | Members listed | Three core members only, or also the potential collaborator (only if committed) |
| 6 | Per member | A neutral label (Member 1, 2, 3), the activities they lead or support, and average monthly hours available for the project. Qualifications stay local |
| 7 | Independent deployment rehearsal (activity 7 acceptance) | Who performs it: the collaborator, an owner-designated reviewer, or a core member not involved in the build |

## C. Duration and schedule (Sections 4, 11, 16, 18)

| No. | Decision | What is needed |
|---|---|---|
| 8 | Project duration | Number of months, or "derive from team hours". The form's Gantt has 12 month columns; if more than 12, state the native template's rule |
| 9 | Later stages (Section 11) | Estimated durations for stages 2–4, or leave them for local completion |

## D. Costs (Sections 15, 16)

| No. | Decision | What is needed |
|---|---|---|
| 10 | Personnel rate structure | One hourly rate for all members, or relative rates per member (for example 1.0 / 1.0 / 0.8). Amounts stay local |
| 11 | Non-personnel items | For each, include or rule out: reference evaluation environment (existing equipment / purchase / rental); patent-service access (free tier expected); any other item. Give a quantity and, if weights must include it, its cost relative to one personnel hour |
| 12 | Sponsor cost rules | Any allowable-cost categories or ceiling that apply (yes or no; details may stay local). Superseded training or consulting lines are not included (RF-012) |

## E. Other

| No. | Decision | What is needed |
|---|---|---|
| 13 | Section 10 prior work | Documented relevant work (type, outcome, status, public link), or "none": the table stays blank |
| 14 | Native template | Upload a sanitized copy of the original Word form if available; otherwise template insertion stays a local task and the proposal is not marked submission-ready |

## 1. Recomputed provisional effort for item 1

The S06 planning figures (2,004 h; range 1,554–2,670 h) do not include three tasks that S07–S09 added. S10 proposes these additions; they are project estimates, not measured values, and are replaced by pilot values where the method says so.

| Addition | Activity | Basis | Low | Planning | High |
|---|---|---|---|---|---|
| Deeper relevance check (ET-12) judging | 6 | 10 queries × 2 retrieval tasks × substitute track = 20 queries; 80 / 120 / 160 unique items per query at ranks 11–50; 30 / 45 / 60 s per judgment (EH-07) | 13 | 30 | 53 |
| Writing unaided and edited external queries | 6 | 30 need statements × 2 formulations; 6 / 10 / 15 minutes each | 6 | 10 | 15 |
| Manual-entry query and clearance logging | 4 | Extension of T4.4; EH-09 range | 4 | 5 | 7 |
| Total added | | | 23 | 45 | 75 |

| No. | Main activity | S06 planning | Proposed planning |
|---|---|---|---|
| 1 | Prototype design specification and data-protection baseline | 210 | 210 |
| 2 | Evaluation protocol, test collections and evaluation harness | 290 | 290 |
| 3 | Ingestion and retrieval for similar submissions and solution examples | 380 | 380 |
| 4 | External prior-art retrieval with query approval | 210 | 215 |
| 5 | Assessment record, review interface and approval controls | 400 | 400 |
| 6 | Prototype integration and evaluation | 374 | 414 |
| 7 | Technical documentation and handover | 140 | 140 |
| Total | | 2004 | 2049 |

Proposed range: 1,577 to 2,745 h. At 45 h per person-week the planning figure is about 45.5 person-weeks. Arithmetic is recomputed by `qc/S10_QC_CHECK.py`.
