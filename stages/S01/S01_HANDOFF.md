# S01_HANDOFF

| Field | Value |
|---|---|
| Document ID | S01_HANDOFF |
| Version | 1.2 |
| Status | APPROVED |
| Stage | S01 |
| Date | 2026-11-20 |
| Depends on | All S01 deliverables v1.2; DEC-015; DEC-016; DEC-017; DEC-018 |

- **Transition:** S01 Research Foundation → S02 Scientific and Technical Literature Research. S01 approved (DEC-016) and published as tag `S01-approved`. S02 starts only after owner authorization (DEC-019, proposed).

## What S01 established

- **Requirements:** R1–R4, with REF-01 source text kept separate from working interpretations. C-series classified by authority: C1–C2 sponsor-origin constraints (SC), C3 evaluator advisory (EA), C4–C6 project governance rules (PG). Eight context facts, 20 form obligations (F), 12 cross-section rules (FX).
- **Reviewer criteria:** RF-001 to RF-012 and QA-001 to QA-010 with status and artifact references. RF-011 and QA-003 are OPEN pending the scope decision; the rest are SCHEDULED.
- **Research:** RQ-01 to RQ-09 for S02 (RQ-07 conditional on ISS-007); RQ-10 to RQ-15 for S03–S05.
- **Evidence:** tiers T1–T3, source log, claim register (CLM-001 to CLM-012). CLM-012 records that the existence of a populated internal collection is not established.

## Inputs for S02

The repository at tag `S01-approved` is the source. The three reference documents are in the Claude Project, not in the repository.

| Needed | Path | Version |
|---|---|---|
| At session start | `CLAUDE.md` | — |
| At session start | `project/00_PROJECT_RULES.md` | 1.2 |
| At session start | `project/00_STAGE_STATUS.md` | 1.2 |
| At session start | `project/00_STAGE_GATE_PROTOCOL.md` | 1.2 |
| At session start | `project/00_DECISIONS_LOG.md` | 1.2 |
| At session start | `project/00_OPEN_ISSUES_REGISTER.md` | 1.2 |
| At session start | `project/00_SKILL_REGISTER.md` | 1.2 |
| At session start | `project/02_SOURCE_LOG.md` | 1.2 |
| At session start | `project/02_CLAIM_REGISTER.md` | 1.2 |
| At session start | `project/03_STYLE_GUIDE.md` | 1.2 |
| At session start | `project/S01_RESEARCH_QUESTIONS.md` | 1.2 |
| At session start | `stages/S01/S01_HANDOFF.md` | 1.2 |
| Before the S02 gate (S02 updates them) | `project/S01_REQUIREMENTS_REGISTER.md`, `project/S01_REVIEWER_CRITERIA_REGISTER.md`, `project/S01_TRACEABILITY_MATRIX.md` | 1.2 |
| Not needed by S02 | `stages/S01/S01_PLAN.md`, `S01_QC_REPORT.md`, `S01_CHANGE_REPORT.md`, `qc/` | — |

## Session start (S02)

Suggested first message for the new session:

> Begin S02 under `CLAUDE.md`. Attach and clone the `iraa-proposal` repository, confirm that tag `S01-approved` is the latest approved tag and matches `project/00_STAGE_STATUS.md`, and report any mismatch before doing anything else.

S02 outputs go to `stages/S02/`; updated living registers stay in `project/`.

## Carried forward

- No open issue blocks S02.
- Leave RQ-07 inactive unless the owner confirms non-English submissions (ISS-007).
- Owner decisions due later: ISS-001 and ISS-016 (S04 gate), ISS-002 and ISS-003 (S04–S05), ISS-013 and ISS-018 (before S06), ISS-014 (before S09).

## S02 first actions

1. Run the Skill checkpoint (candidates in `project/00_SKILL_REGISTER.md` §3); any use requires owner authorization.
2. Search, read and log sources per RQ; record limitations and transferability to need/challenge submissions.
3. Produce `stages/S02/S02_LITERATURE_EVIDENCE_MATRIX.md` and the standard stage files.
4. Choose no tools or architecture; S02 supplies evidence for S04–S05.
