# S08_HANDOFF

| Field | Value |
|---|---|
| Document ID | S08_HANDOFF |
| Version | 1.0 |
| Status | APPROVED |
| Stage | S08 |
| Date | 2026-11-21 |
| Depends on | DEC-036; IRAA_PROPOSAL_EN_MASTER; S08_EDITORIAL_LOG; S08_QC_REPORT; 03_DEFECT_LOG |

- **Transition:** S08 → S09 Independent Critical Review. S08 approved with CONDITIONAL PASS and S09 authorized (DEC-037, ISS-014); S09 runs in a new chat (DEC-024). The master is a working draft for independent review, not a submission-ready document.
- **Gate directions for S09 (DEC-037):** review priorities in this order: (a) original form and table fidelity; (b) scientific accuracy and primary-source verification; (c) natural, concise professional English; (d) feasibility of fitting the content into the original proposal template; (e) comparative claims and competitor classifications, including correction of the PQAI categorization (ISS-054); (f) current EMA guidance status and statistical interpretation (ISS-053). Section 9 keeps rows 1–6; the two patent records stay as labelled prior-art discussion, not rows (ISS-030 resolved). Team assignments, person-hours, costs, schedule and local administrative information are not finalized in S09.

## What S08 produced

- **English master** `proposal/IRAA_PROPOSAL_EN_MASTER` v0.1: 20 sections in form order, REF-02 table headers verbatim, proposal prose without working identifiers, author–year citations with a reference list in Section 19. Sections 2, 3, 10, 14, 18 and the S10 cells of 4, 11, 15, 16 are placeholders.
- **Corrections applied:** ISS-052 (disclosure clearance and query approval are separate, both required; DEF-001, also S04 CP-1); Section 5 counts (DEF-006); Section 9 rows 1–6 as a provisional selection (ISS-030).
- **Pass A findings:** two S02 figures not confirmed and not used (DEF-003, DEF-004); EMA lists the CPMP non-inferiority guidance as superseded (ISS-053).

## Owner decisions

**Decided at the S08 gate (DEC-037):** master accepted as working draft; Section 9 rows 1–6 (ISS-030); S09 authorized (ISS-014). **At the S09 gate:** review findings, ISS-054. **S10b:** independent-audit authorization (ISS-014). **Before the protocol freeze:** ISS-053 with ISS-039, ISS-049, ISS-050. **S10:** DEF-002 register alignment, effort recomputation including the ISS-052 controls and deeper-check judging, and the items in `00_STAGE_STATUS`.

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
