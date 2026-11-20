# iraa-proposal

Working repository for an English technical proposal: the **Intelligent Requirements Assessment Assistant**, a decision-support tool that would help human assessors review organizational, operational and technology needs or challenges submitted to a platform. It would check new submissions against stored ones, against an approved internal collection of precedents (whose availability is still unresolved), and against external patents and solution examples. Human assessors keep final approval.

This repository contains proposal-development records, not software. No product exists yet, and nothing here reports measured performance.

## Status

| Stage | Title | State |
|---|---|---|
| S01 | Research Foundation and Requirements Mapping | Approved (baseline commit `2b5f83c`) |
| S02 | Scientific and Technical Literature Research | Approved (commit `34a7745`) |
| S03–S10 | Comparable systems through final integration | Not started |

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

From the repository root, each stage has its own check, for example `python3 stages/S02/qc/S02_QC_CHECK.py .` (Python 3 standard library only). The S01 check validates the S01 baseline and is run against that commit.
