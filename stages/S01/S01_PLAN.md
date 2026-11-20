# S01_PLAN

| Field | Value |
|---|---|
| Document ID | S01_PLAN |
| Version | 1.2 |
| Status | APPROVED |
| Stage | S01 |
| Date | 2026-11-20 |
| Depends on | REF-01; REF-02; REF-03; DEC-014 |

## 1. Inputs

| Input | Use |
|---|---|
| REF-01 REQUIREMENTS_STATEMENT_EN_WORKING_V1 | Product requirements, constraints and context |
| REF-02 PROPOSAL_FORM_EN_WORKING_V1 | Section obligations, table schemas, cross-section rules |
| REF-03 REVIEWER_FEEDBACK_EN_V1 | Reported reviewer criteria (RF) and quality observations (QA) |
| Owner decisions D1–D3, Corrections 1–5, workflow update | Recorded as DEC-001 to DEC-014 |

No external research was performed in S01. No Skill was used (SKL-001).

## 2. Execution steps

1. Extract every numbered item of REF-01 and classify it as requirement (R), constraint (C), context (CTX) or administrative/local.
2. Record each REF-02 section obligation (F-01 to F-20) and cross-section rule (FX-01 to FX-12), with completion class and drafting stage.
3. Register RF-001 to RF-012 and QA-001 to QA-010 with responsible stage, S01 action and gate status.
4. Define research questions for S02–S05 and check coverage against R1–R4 and C1–C5.
5. Build the source-to-section traceability matrix.
6. Set up the evidence system (source log, claim register) and seed unverified claims from the references.
7. Record decisions, open issues, style rules, gate protocol and Skill checkpoint.
8. Run QC checks; write QC report and handoff.

## 3. Deliverables and length budgets

| File | Budget | Purpose |
|---|---|---|
| S01_PLAN.md | ≤ 1 page | Inputs and execution plan |
| 00_PROJECT_RULES.md | ≤ 2 pages | Stable rules for fresh sessions |
| 00_STAGE_STATUS.md | ≤ 1 page | Current position |
| 00_STAGE_GATE_PROTOCOL.md | ≤ 3 pages | Gate checks |
| 00_DECISIONS_LOG.md | As needed | Decision record |
| 00_OPEN_ISSUES_REGISTER.md | As needed | Open issues |
| 00_SKILL_REGISTER.md | ≤ 1 page | Skill checkpoints |
| 02_SOURCE_LOG.md | As needed | Source records |
| 02_CLAIM_REGISTER.md | As needed | Claims and evidence status |
| 03_STYLE_GUIDE.md | ≤ 3 pages | Writing standard and glossary |
| S01_REQUIREMENTS_REGISTER.md | As needed | R, C, CTX, F, FX |
| S01_REVIEWER_CRITERIA_REGISTER.md | As needed | RF and QA compliance |
| S01_RESEARCH_QUESTIONS.md | ≤ 3 pages | RQ-01 to RQ-15 |
| S01_TRACEABILITY_MATRIX.md | As needed | Source → section map |
| S01_QC_REPORT.md | ≤ 2 pages | QC results |
| S01_HANDOFF.md | ≤ 1 page | Next-stage inputs and file tiers |
| S01_CHANGE_REPORT.md | ≤ 2 pages | v1.1 corrections (added after DEC-015) |
| S01_QC_CHECK.py, S01_QC_CHECK_OUTPUT.txt | — | Reproducible QC script and its output (added after DEC-015) |
