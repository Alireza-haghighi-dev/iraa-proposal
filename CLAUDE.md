# CLAUDE.md

Entry point for every session on the Intelligent Requirements Assessment Assistant proposal. The full rules are in `project/00_PROJECT_RULES.md`; this file only says how to start and what must never happen.

## Start of session

1. Read `project/00_PROJECT_RULES.md` and `project/00_STAGE_STATUS.md`.
2. Read the latest handoff: `stages/S0X/S0X_HANDOFF.md` for the most recent stage.
3. Confirm that the approved baseline commit recorded in `00_STAGE_STATUS.md` exists in the repository history (and the stage tag, where one exists). Stop and report any mismatch.
4. Read only the inputs the handoff lists. The three reference documents (REF-01 to REF-03) are in the Claude Project, not in this repository.
5. Run the Skill checkpoint (`project/00_SKILL_REGISTER.md`).

## Never

- Start a stage without an owner approval recorded in `project/00_DECISIONS_LOG.md`.
- Push before the owner approves the stage, unless the owner has explicitly authorized pushing that stage's package as `SUBMITTED FOR GATE`.
- Commit the reference documents, credentials, personal or geographic identifiers (including the account name or repository URL), private infrastructure details or unrelated files. This repository is public.
- Invent facts, citations, results, team details or figures, or present targets, expected benefits, vendor descriptions or standards mentions as verified.
- Install or run a third-party Skill without owner authorization and a recorded security review.
- Quote RF items as reviewer wording; they are reported criteria (DEC-011).
- Confuse the development stages S01–S10 with the 6–7 funded work packages of proposal Section 13.

## Layout

| Path | Contents |
|---|---|
| `project/` | Living documents: rules, status, decisions, issues, registers, source and claim logs, style guide |
| `stages/S0X/` | Stage deliverables: plan, outputs, QC report and evidence, change report, handoff |
| `proposal/` | Section drafts and the English master (from S07/S08) |

## Writing

English only. Follow `project/03_STYLE_GUIDE.md` in every file: specific, evidenced, no promotional language, no filler. Revise content, not synonyms.

## Stage threads (DEC-023)

- The main Project conversation is the coordinator only: approvals, links, blockers, decisions.
- Each stage runs in one fresh thread: S01 — Research Foundation, S02 — Scientific Literature, S03 — Comparable Systems, S04 — Product Architecture, S05 — Feasibility and Evaluation, S06 — Work Packages, S07 — Technical Methodology, S08 — Proposal Drafting, S09 — Independent Review, S10 — Final Integration.
- A stage thread loads only the start-of-session files above. No earlier transcripts, full research reports or whole-repository reads unless a specific verification needs them.
- Focused subagents may be used when they materially cut context. Their sources enter the source log only with a DOI or URL and the supporting statement, and the stage thread spot-checks them.

Workflow commands (conventions, not slash commands):

- `START_STAGE SXX`: after the previous stage is approved, the coordinator records the approval (DEC entry, stage files set to `APPROVED`, commit, push, SHA in `00_STAGE_STATUS.md`). The owner then opens a new chat in the Claude Project and sends `START_STAGE SXX`; that chat runs the start-of-session steps. No scheduled tasks (DEC-024).
- `CLOSE_STAGE SXX`: finish deliverables, run the stage QC script and pre-commit safety scan, update living registers and the handoff, commit and push as `SUBMITTED FOR GATE`, record the commit SHA, report results and open issues to the coordinator, then stop.
