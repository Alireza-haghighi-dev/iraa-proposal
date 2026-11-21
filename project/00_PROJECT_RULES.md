# 00_PROJECT_RULES

| Field | Value |
|---|---|
| Document ID | 00_PROJECT_RULES |
| Version | 5.0 |
| Status | SUBMITTED FOR GATE |
| Stage | S06 |
| Date | 2026-11-21 |
| Depends on | 00_DECISIONS_LOG; 00_STAGE_GATE_PROTOCOL; 03_STYLE_GUIDE |

- **Purpose:** Full project rules. `CLAUDE.md` at the repository root is the short entry point and points here.

## 1. Objective

Produce an evidence-based, reviewer-ready English proposal for the Intelligent Requirements Assessment Assistant, following the official proposal form (20 sections, original table schemas) and the requirements statement. The English master is later translated and formatted locally by the owner.

## 2. Product baseline (DEC-002)

The sponsor's platform holds organizational, operational and technology **needs or challenges** submitted for assessment and for identification of possible solutions. They are not software requirements specifications. Product requirements are R1–R4 in `S01_REQUIREMENTS_REGISTER.md`. The C-series is classified there by authority: C1–C2 are sponsor-origin constraints on the product, C3 is evaluator advisory guidance, and C4–C6 are project governance rules that bind how this project works, not what the product must do. Source text and working interpretations are kept in separate columns; an interpretation never counts as a sponsor requirement. Human assessors keep final decision authority (R3).

## 3. Hard boundaries

1. English only.
2. No personal, geographic, jurisdiction-specific or locally restricted administrative information in any working file. Form fields reserved for local completion stay as `[LOCAL COMPLETION ONLY]`.
3. Do not invent facts, citations, results, performance figures, team qualifications, financial figures or implementation status. Mark gaps `OPEN` or `OWNER DECISION REQUIRED`.
4. Do not present targets, expected benefits, vendor descriptions or standards mentions as verified facts.
5. RF items are *reported reviewer criteria*; QA items are *additional quality observations*. Neither is quoted as reviewer wording (DEC-011).
6. The 10 development stages (S01–S10) are not the 6–7 funded work packages of Section 13 (DEC-012).
7. Team, personal data, final financial figures, Sections 14–16 commitments and administrative completion are handled in S10 only.
8. No third-party Skill is installed or run without explicit owner authorization and a recorded security review (DEC-005).
9. No stage starts without a recorded owner approval in `00_DECISIONS_LOG.md`. An approval read into the wording of another instruction is recorded as INFERRED and does not count as an explicit decision until the owner confirms it (S04.1, RC-01).
10. The repository is public. Never commit the three reference documents, credentials, personal or geographic identifiers (including the repository owner's account name or repository URL), private infrastructure details, unrelated files or unapproved material (DEC-018).
11. Nothing is pushed before the owner approves the stage, unless the owner explicitly authorizes pushing a stage package as `SUBMITTED FOR GATE` (as for S02, DEC-021).

## 4. Session handoff procedure (GitHub; DEC-017)

The `iraa-proposal` repository is the persistent source of truth. The three reference documents (REF-01 to REF-03) remain in the Claude Project and are never committed.

**Repository layout (DEC-018):**

| Path | Contents |
|---|---|
| `CLAUDE.md`, `README.md` | Entry point and repository overview |
| `project/` | Living documents: rules, status, gate protocol, decisions, issues, Skill register, source log, claim register, style guide and the registers created in S01. One current copy each; Git history and stage tags hold earlier states. |
| `stages/S0X/` | Stage-specific deliverables: plan, stage work products, QC report and evidence, change report, handoff |
| `proposal/` | Section drafts and the English master (from S07/S08) |

**During a stage:**
1. Work in a local clone. Do not push.
2. Deliver the stage package to the owner as downloads for review.

**After owner approval:**
1. Record the approval as a DEC entry and set the approved files to `APPROVED`.
2. Run the stage QC script and the pre-commit safety scan; both must pass.
3. Commit to `main` and push. Record the approved commit SHA in `00_STAGE_STATUS.md` (DEC-020). Add an annotated `S0X-approved` tag only if the environment permits pushing tags.
4. Report the repository, stage-folder and tag links to the owner in chat (not in committed files).

**Starting a new stage (fresh session):**
1. Attach and clone the repository; `CLAUDE.md` loads automatically.
2. Read this file, `project/00_STAGE_STATUS.md` and the previous handoff.
3. Confirm that the approved baseline commit recorded in `00_STAGE_STATUS.md` exists in the repository history; if not, stop and report.
4. Read only the inputs the handoff lists, plus the reference documents in the Claude Project as needed.
5. Run the Skill checkpoint and record it in `00_SKILL_REGISTER.md`.
6. Do not reconstruct decisions from chat history; the repository files are the record.

## 5. Identifier scheme

| Prefix | Meaning | Defined in |
|---|---|---|
| R / C | Product requirement / C-series item, classified SC, EA or PG | S01_REQUIREMENTS_REGISTER |
| CTX | Context fact from the requirements statement (not a requirement) | S01_REQUIREMENTS_REGISTER |
| F / FX | Proposal-form section obligation / cross-section rule | S01_REQUIREMENTS_REGISTER |
| RF / QA | Reported reviewer criterion / additional quality observation | S01_REVIEWER_CRITERIA_REGISTER |
| RQ | Research question | S01_RESEARCH_QUESTIONS |
| REF / SRC | Project reference document / external source | 02_SOURCE_LOG |
| CLM | Claim requiring evidence | 02_CLAIM_REGISTER |
| DEC / ISS | Decision / open issue | 00_DECISIONS_LOG / 00_OPEN_ISSUES_REGISTER |
| RC | Correction to the decision record itself (original entry kept) | 00_DECISIONS_LOG |
| SKL | Skill evaluation | 00_SKILL_REGISTER |
| WP | Funded work package for Section 13 (frozen at S06) | S06 deliverables |
| DEF | Defect | 03_DEFECT_LOG (from S08) |
| FN / AC / CP / AD | Product function / architecture component / R3 checkpoint / architecture design choice (PROPOSED) | S04_ARCHITECTURE |
| IF / DF | Interface / data flow (PROPOSED) | S04_DATA_FLOWS_AND_INTERFACES |
| AS | Planning assumption, valid until the linked issue is decided | S04_ASSUMPTIONS_AND_STANDARDS |
| MS | Measurable specification row for Section 8 (targets set in S05) | proposal/DRAFT_SEC08_FEATURES |
| ET / PV | Evaluation test / numeric planning value (ASSUMPTION, AS-12) | S05_EVALUATION_DESIGN |
| DR / DS | Data requirement / substitute dataset candidate | S05_DATA_AVAILABILITY_AND_SUBSTITUTES |
| FT / RSK | Feasibility test / technical or data risk (input to Section 17) | S05_FEASIBILITY_AND_RISKS |
| Tn.m / Dn.m / M | Task / deliverable within work package n / milestone (decision point, no date) | S06_WORK_PACKAGES; S06_DELIVERABLES_AND_ACCEPTANCE |
| EH / L | Effort-sizing assumption (ASSUMPTION) / effort-reduction option if the ISS-013 envelope is lower | S06_DEPENDENCIES_AND_EFFORT |

## 6. Claim labels

`VERIFIED (SRC-###)`, `PROPOSED`, `ASSUMPTION`, `OPEN`, `OWNER DECISION REQUIRED`. Every factual statement in a deliverable carries one, or sits in a register row that carries one.

## 7. Writing standard

Apply `03_STYLE_GUIDE.md` to every deliverable at every stage. Short form: say something specific to this project in every paragraph; back evaluative words with a criterion or a source; no promotional language, filler, or template-shaped paragraphs; revise by changing content, not by swapping synonyms.

## 8. Form invariants

- 20 sections, original order and table schemas (RF-003).
- Section 12 repeats Section 13 activity numbers and titles exactly (RF-006, FX-01).
- Section 13 person-hours = Section 16 person-hours; Section 15 total = Section 16 cost total; Section 16 weights and Section 14 shares each total 100% (FX-02 to FX-05).
- Section 11 row 1 is the current project; later rows are prospective (RF-005).

## 9. Stage delivery

Every stage ends with Markdown files: stage outputs, updated decisions and open issues, evidence records where research occurred, a QC report and a handoff of one page or less. They are reviewed as downloads before approval and committed, tagged and pushed after approval (§4). Gate rules: `00_STAGE_GATE_PROTOCOL.md`.

## 10. Document metadata standard

Every Markdown deliverable starts with the title line and this six-row table, in this order and with these field names:

| Field | Content |
|---|---|
| Document ID | File name without extension |
| Version | Major.minor. Minor increments for corrections within a stage; major increments when a later stage revises the file |
| Status | One of: `DRAFT`, `SUBMITTED FOR GATE`, `APPROVED` (accepted at a stage gate), `SUPERSEDED` |
| Stage | Stage that produced this version |
| Date | Date of this version (YYYY-MM-DD) |
| Depends on | Documents or decisions this file relies on, by ID |

Other context (keys, purpose, rules) goes in a short note list directly below the table, not in the table. The version history is recorded in stage change reports and Git history, not inside each file. `CLAUDE.md` and `README.md` are repository entry files and carry no metadata table.

