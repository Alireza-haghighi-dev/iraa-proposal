# S08_HANDOFF

| Field | Value |
|---|---|
| Document ID | S08_HANDOFF |
| Version | 1.0 |
| Status | SUBMITTED FOR GATE |
| Stage | S08 |
| Date | 2026-11-21 |
| Depends on | DEC-036; IRAA_PROPOSAL_EN_MASTER; S08_EDITORIAL_LOG; S08_QC_REPORT; 03_DEFECT_LOG |

- **Transition:** S08 → S09 Independent Critical Review. S09 starts only after the owner records the S08 gate decision, authorizes the isolated reviewer (ISS-014) and opens a new chat (DEC-024).

## What S08 produced

- **English master** `proposal/IRAA_PROPOSAL_EN_MASTER` v0.1: 20 sections in form order, REF-02 table headers verbatim, proposal prose without working identifiers, author–year citations with a reference list in Section 19. Sections 2, 3, 10, 14, 18 and the S10 cells of 4, 11, 15, 16 are placeholders.
- **Corrections applied:** ISS-052 (disclosure clearance and query approval are separate, both required; DEF-001, also S04 CP-1); Section 5 counts (DEF-006); Section 9 rows 1–6 as a provisional selection (ISS-030).
- **Pass A findings:** two S02 figures not confirmed and not used (DEF-003, DEF-004); EMA lists the CPMP non-inferiority guidance as superseded (ISS-053).

## Owner decisions

**At the S08 gate:** acceptance of the master; Section 9 rows (ISS-030; patent rows need ISS-031 if used). **For S09:** ISS-014 authorization. **Before the protocol freeze:** ISS-053 with ISS-039, ISS-049, ISS-050. **S10:** DEF-002 register alignment, effort recomputation including the ISS-052 controls and deeper-check judging, and the items in `00_STAGE_STATUS`.

## Inputs for S09

| Path | Why |
|---|---|
| `CLAUDE.md`, `project/00_PROJECT_RULES.md`, `00_STAGE_STATUS.md`, `00_STAGE_GATE_PROTOCOL.md` (§5, §7 S09 row), `03_STYLE_GUIDE.md` | Rules and gate |
| `proposal/IRAA_PROPOSAL_EN_MASTER.md` | Object of review |
| `stages/S08/S08_EDITORIAL_LOG.md`, `S08_QC_REPORT.md`, `project/03_DEFECT_LOG.md` | What was checked and what remains |
| `project/S01_REVIEWER_CRITERIA_REGISTER.md`, `02_CLAIM_REGISTER.md`, `02_SOURCE_LOG.md`, `00_OPEN_ISSUES_REGISTER.md` | Criteria, evidence, issues |

The isolated reviewer should not receive the S01–S08 drafting history beyond these files.

## Session start (S09)

> Begin S09 under `CLAUDE.md`. Clone the repository, confirm that the S08 gate decision and the S08 content commit are recorded in `project/00_STAGE_STATUS.md`, and report any mismatch before anything else. Run `python3 stages/S08/qc/S08_QC_CHECK.py .`; it must pass.
