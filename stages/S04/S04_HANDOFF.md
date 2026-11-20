# S04_HANDOFF

| Field | Value |
|---|---|
| Document ID | S04_HANDOFF |
| Version | 1.0 |
| Status | SUBMITTED FOR GATE |
| Stage | S04 |
| Date | 2026-11-20 |
| Depends on | All S04 deliverables; DEC-026; DEC-027 |

- **Transition:** S04 Product Definition and Technical Architecture → S05 Technical Feasibility and Evaluation Design. S05 starts only after DEC-028 is recorded, including the owner's decision on ISS-001.

## What S04 established

- **Scope:** four options compared; Option B (laboratory prototype, technology development, design + build + test) recommended, with three conditions (proxy data, proxy internal collection, read-only toward the platform). OWNER DECISION REQUIRED (ISS-001).
- **Design:** 12 functions (FN), 14 components (AC), 8 interfaces (IF), 8 data flows (DF), 12 design choices (AD), all PROPOSED. R3 enforced through six checkpoints (CP-1 to CP-6); no path to Approved outside CP-5.
- **Assumptions:** AS-01 to AS-08 cover data, internal collection, integration, deployment, access, language, scale and external sources; each tied to an open issue. New issues ISS-033 to ISS-036.
- **Standards:** SRC-064, SRC-065; both standards apply to an organization's management system; alignment only (CLM-041 to CLM-043).
- **Drafts:** `proposal/` Sections 5, 7, 8 (with MS-01 to MS-09) and technical Section 11, provisional on ISS-001.

## Owner decisions requested at the S04 gate

ISS-001 (scope), ISS-016 (Section 5), ISS-004 (R1 scope), ISS-005 (assessment content); confirmation of DEC-026. Answers to ISS-003, ISS-007 to ISS-010 and ISS-033 are wanted before or during S05; until then AS-01 to AS-08 apply.

## Inputs for S05 (load only these)

| Path | Why |
|---|---|
| `CLAUDE.md`, `project/00_PROJECT_RULES.md`, `project/00_STAGE_STATUS.md`, `project/00_STAGE_GATE_PROTOCOL.md`, `project/03_STYLE_GUIDE.md` | Rules and gate |
| `project/00_DECISIONS_LOG.md` (DEC-028), `project/00_OPEN_ISSUES_REGISTER.md` (ISS-002, ISS-003, ISS-006, ISS-007, ISS-009, ISS-011, ISS-012, ISS-023, ISS-028, ISS-033) | Decisions and data issues |
| `project/S01_RESEARCH_QUESTIONS.md` (RQ-06, RQ-07, RQ-14, RQ-15) | S05 research scope |
| `project/02_CLAIM_REGISTER.md` (CLM-026, CLM-027, CLM-036, CLM-044) | Evaluation and component inputs |
| `stages/S02/S02_RESEARCH_SYNTHESIS.md` §3–§5 | Evaluation design leads |
| `stages/S04/S04_ARCHITECTURE.md` §2, §4, §5; `stages/S04/S04_DATA_FLOWS_AND_INTERFACES.md` DF-08; `stages/S04/S04_ASSUMPTIONS_AND_STANDARDS.md` §1 | Design to evaluate |
| `proposal/DRAFT_SEC08_FEATURES.md` | MS rows needing metrics and targets |
| `project/00_SKILL_REGISTER.md`, `project/S01_TRACEABILITY_MATRIX.md` (Part D: specification column) | Skill checkpoint; traceability |

## Session start (S05)

> Begin S05 under `CLAUDE.md`. Attach and clone the repository, confirm the baseline commit recorded in `project/00_STAGE_STATUS.md` and that DEC-028 is recorded, and report any mismatch before doing anything else.

## Carried forward

ISS-030 to ISS-032 (Section 9, S08–S10); ISS-029 (full-text checks, S08); re-cut of the Section 5, 7, 8 and 11 drafts if the owner does not choose Option B.
