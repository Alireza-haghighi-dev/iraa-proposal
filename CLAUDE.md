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

## After owner approval of a stage

Run the stage QC script and the pre-commit safety scan, commit to `main`, push, record the approved commit SHA in `00_STAGE_STATUS.md`, add a `S0X-approved` tag if the environment permits it, and report the links in chat.
