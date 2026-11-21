# S07_HANDOFF

| Field | Value |
|---|---|
| Document ID | S07_HANDOFF |
| Version | 1.0 |
| Status | APPROVED |
| Stage | S07 |
| Date | 2026-11-21 |
| Depends on | DEC-033; DEC-034; DRAFT_SEC12_METHODOLOGY; S07_CORRECTED_EVALUATION_METHODOLOGY; S07_TOOL_AND_VERSION_REGISTER; S07_WP_METHOD_TRACEABILITY; S07_QC_REPORT |

- **Transition:** S07 → S08 Proposal Drafting and Intensive Editorial Pass. S08 starts only after the owner records the S07 gate decision and opens a new chat (DEC-024).

## What S07 produced

- **Section 12 working draft** (`proposal/DRAFT_SEC12_METHODOLOGY` v0.1): method logic, what the project controls, scope, sources and a tool table with status, then one subsection per activity, titles verbatim from Section 13 (WP1–WP7).
- **Corrected evaluation methodology:** ISS-042 (MS-03 as a non-inferiority test, margin 0.10), ISS-043 (pool-based absence, ET-12 deeper check) and ISS-045 (BM25 as a non-inferiority reference within 0.05, superiority not required, default-configuration rule, Holm) corrected in `S05_EVALUATION_DESIGN` v2.0 and Section 8 v0.4. ISS-044: CQADupStack data licence not established; DS-01 and DS-02 unusable until the T2.1 gate passes.
- **Tool register** (Pyserini 2.4.0 and licence, Faiss licence verified; everything else PROPOSED), **traceability** (seven elements per WP; Section 8 rows to verification steps), Section 13 v0.2 (activity 6 tasks aligned; effort unchanged).

## Owner decisions

**At the S07 gate:** acceptance of Section 12 and the corrected methodology. **Before the protocol freeze (T2.2):** ISS-049 (MS-03 margin and R4 sample size; at 30 statements non-inferiority is unlikely to be established), ISS-050 (ET-12 parameters), ISS-039 (PV values). **Before WP2 / WP4 / T1.5:** ISS-044 (licensing gate), ISS-040 (patent service; EPO OPS recommended), ISS-041, ISS-007 to ISS-010. **S10:** ISS-050 effort, ISS-051 rehearsal person, and the items in `00_STAGE_STATUS`.

## Instructions for S08

- **Mandatory (DEC-035, ISS-052):** reword every passage that treats assessor query approval (CP-1) as sufficient for external transmission. Both disclosure authorization (ISS-033) and query approval are required before any confidential text leaves the controlled environment; without authorization, only public need statements or text the authorization covers may be sent. Affected: Section 7 third objective, Section 8 feature 5 and MS-05, Section 12 activity 4 and intro, `S04_ARCHITECTURE` CP-1 row.
- **Critical reviewer requirement (DEC-035, RF-003):** preserve the official form's 20 sections and original table structures in the English master.
- Keep all open experimental parameters and licensing decisions provisional (ISS-039, ISS-041, ISS-044, ISS-049, ISS-050).
- Draft the remaining draftable sections into the English master; carry Section 12 into it with an editorial pass (Passes A–E), removing bracketed working IDs and keeping every claim label's meaning.
- Do not change WP titles or the corrected targets; keep "not required" for superiority and "non-inferiority not established" wording.
- Full-text checks (Pass A) for SRC-066 to SRC-069, SRC-087, SRC-089, SRC-090 and S02 sources (ISS-029).
- Section 9 row selection needs ISS-030.

## Inputs for S08

| Path | Why |
|---|---|
| `CLAUDE.md`, `project/00_PROJECT_RULES.md`, `00_STAGE_STATUS.md`, `00_STAGE_GATE_PROTOCOL.md` (§5, §7 S08 row), `03_STYLE_GUIDE.md` | Rules and gate |
| `project/00_DECISIONS_LOG.md` (DEC-028, DEC-033, DEC-034, DEC-035), `00_OPEN_ISSUES_REGISTER.md`, `02_CLAIM_REGISTER.md`, `02_SOURCE_LOG.md`, `S01_REVIEWER_CRITERIA_REGISTER.md` | Decisions, issues, evidence, criteria |
| `proposal/` (all drafts) | Sections to integrate |
| `stages/S07/S07_WP_METHOD_TRACEABILITY.md` §4; `stages/S03/S03_SECTION9_COMPARISON.md` | Consistency checks; Section 9 |

## Session start (S08)

> Begin S08 under `CLAUDE.md`. Clone the repository, confirm that the S07 content commit recorded in `project/00_STAGE_STATUS.md` exists and that the S07 gate decision is recorded, and report any mismatch before anything else. Run `python3 stages/S07/qc/S07_QC_CHECK.py .`; it must pass.
