# S06_HANDOFF

| Field | Value |
|---|---|
| Document ID | S06_HANDOFF |
| Version | 1.0 |
| Status | APPROVED |
| Stage | S06 |
| Date | 2026-11-21 |
| Depends on | DEC-031; DEC-032; S06_WORK_PACKAGES; S06_DELIVERABLES_AND_ACCEPTANCE; S06_DEPENDENCIES_AND_EFFORT; S06_QC_REPORT |

- **Transition:** S06 → S07 Detailed Technical Methodology (Section 12). Gate: CONDITIONAL PASS (DEC-033); WP identifiers and titles frozen; effort figures are provisional scenarios, not staffing or budget commitments. S07 starts in a new chat (DEC-024).

## What S06 produced

- **Seven work packages** with frozen identifiers and titles: WP1 Prototype design specification and data-protection baseline; WP2 Evaluation protocol, test collections and evaluation harness; WP3 Ingestion and retrieval for similar submissions and solution examples; WP4 External prior-art retrieval with query approval; WP5 Assessment record, review interface and approval controls; WP6 Prototype integration and evaluation; WP7 Technical documentation and handover. Tasks T1.1 to T7.5, deliverables D1.1 to D7.4, milestones M1 to M5.
- **Effort:** 2,004 person-hours planning figure (range 1,554–2,670) under outcome O-4, with assumptions EH-01 to EH-10 and judging sized from the S05 formula (63 / 140 / 247 h). ISS-013 is open, so no envelope is claimed as met; reductions L-1 to L-5 are listed with their consequences.
- **Section 13 working draft** in the form schema (`proposal/DRAFT_SEC13_ACTIVITIES` v0.1). Traceability Part H.

## Mandatory corrections for S07 (DEC-031; carried, not yet made)

S07 must make these corrections in the evaluation methodology and in `proposal/DRAFT_SEC08_FEATURES` before the freeze, and WP2 deliverable D2.1 must carry the corrected versions:

1. **ISS-042 (MS-03):** replace "not lower than unaided keyword queries" tested by the superiority test with either a pre-declared non-inferiority test (stated margin, one-sided interval of Q-C minus Q-A success@10 above minus the margin) or a target that claims no non-inferiority. State which.
2. **ISS-043 (ET-01b, ET-04):** define absence as "no item graded ≥ 2 in the judged pool"; rename or qualify the false-match and false-reassurance rates as pool-based; where corpus-level absence is claimed, add an estimation method (for example additional judging beyond the pool for a sample of "none" queries) or drop the claim.
3. **ISS-044 (CQADupStack):** read the licence on the original distribution, separately from any code-repository Apache 2.0 statement; record the source in the source log at T1 or T2. DS-01 and DS-02 stay unusable until then (WP2 T2.1 depends on it).
4. **ISS-045 (BM25 criterion):** decide, with the owner if needed, whether MS-01 and MS-02 require a statistically supported improvement over B-LEX or use B-LEX as a reported reference with acceptance defined otherwise (non-inferiority plus absolute floors). Record the reasoning. S06 acceptance evidence already does not depend on this answer.

## Other instructions for S07

- Use WP1–WP7 numbers and titles verbatim in Section 12 (RF-006, FX-01); one Section 12 subsection per work package, with methods, inputs, tools, procedures, evaluation and outputs. Tasks may be refined; WP titles may not change without an owner decision.
- Verify or mark PROPOSED every tool and version (QA-010; ISS-041). Map each Section 8 row to a verification step using `S06_DELIVERABLES_AND_ACCEPTANCE` §2.
- The Section 7 walk-through correction was made at the gate (DEC-033, draft v0.3); keep Section 12 consistent with it and promise no assessor availability.
- Coordination stays cross-cutting within WP1–WP7; no eighth work package (DEC-033, ISS-048).

## Owner decisions

**At the S06 gate:** acceptance of WP1–WP7; ISS-048 (separate coordination activity). **Before WP2 work:** ISS-002, ISS-003, ISS-037, ISS-038 (build DS-05?), ISS-044. **Before S10:** ISS-013, ISS-017, ISS-018, ISS-046, ISS-047. Others as listed in `S06_DEPENDENCIES_AND_EFFORT` §7.

## Inputs for S07 (load only these)

| Path | Why |
|---|---|
| `CLAUDE.md`, `project/00_PROJECT_RULES.md`, `project/00_STAGE_STATUS.md`, `project/00_STAGE_GATE_PROTOCOL.md` (§7 S07 row), `project/03_STYLE_GUIDE.md` | Rules and gate |
| `project/00_DECISIONS_LOG.md` (DEC-028, DEC-031, DEC-032, S06 gate entry), `project/00_OPEN_ISSUES_REGISTER.md` (ISS-007 to ISS-010, ISS-033, ISS-038 to ISS-045) | Scope and corrections |
| `stages/S06/S06_WORK_PACKAGES.md`, `stages/S06/S06_DELIVERABLES_AND_ACCEPTANCE.md` | Section 12 structure |
| `stages/S05/S05_EVALUATION_DESIGN.md` §1 to §9; `stages/S05/S05_FEASIBILITY_AND_RISKS.md` §1, §2 | Methods and tools to verify |
| `stages/S04/S04_ARCHITECTURE.md` §3 to §5; `stages/S04/S04_DATA_FLOWS_AND_INTERFACES.md` | Components and interfaces |
| `proposal/DRAFT_SEC08_FEATURES.md`, `proposal/DRAFT_SEC13_ACTIVITIES.md`; `project/02_SOURCE_LOG.md`; `project/02_CLAIM_REGISTER.md` | Sections to align; evidence |

## Session start (S07)

> Begin S07 under `CLAUDE.md`. Clone the repository, confirm that the S06 content commit recorded in `project/00_STAGE_STATUS.md` exists and that the S06 gate decision is recorded, and report any mismatch before anything else. Run `python3 stages/S06/qc/S06_QC_CHECK.py .`; it must pass.
