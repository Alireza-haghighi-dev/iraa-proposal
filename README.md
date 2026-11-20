# iraa-proposal

Working repository for an English technical proposal: the **Intelligent Requirements Assessment Assistant**, a decision-support tool that would help human assessors review organizational, operational and technology needs or challenges submitted to a platform. It would check new submissions against stored ones, against an approved internal collection of precedents (whose availability is still unresolved), and against external patents and solution examples. Human assessors keep final approval.

This repository contains proposal-development records, not software. No product exists yet, and nothing here reports measured performance.

## Status

| Stage | Title | State |
|---|---|---|
| S01 | Research Foundation and Requirements Mapping | Approved (`S01-approved`) |
| S02–S10 | Literature research through final integration | Not started |

Current position: `project/00_STAGE_STATUS.md`.

## Layout

| Path | Contents |
|---|---|
| `CLAUDE.md` | Session entry point and hard rules |
| `project/` | Living documents: project rules, stage status, gate protocol, decisions, open issues, Skill register, source log, claim register, style guide, requirements, reviewer criteria, research questions, traceability |
| `stages/S01/` … `stages/S10/` | Stage deliverables: plan, QC report and evidence, change report, handoff |
| `proposal/` | Proposal section drafts and the English master (from S07/S08) |

The sponsor's reference documents are not part of this repository. Administrative, team, personal and locally restricted information is completed outside it.

## Quality check

From the repository root: `python3 stages/S01/qc/S01_QC_CHECK.py .` (Python 3 standard library only).
