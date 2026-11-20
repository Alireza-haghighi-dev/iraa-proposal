# S01_CHANGE_REPORT

| Field | Value |
|---|---|
| Document ID | S01_CHANGE_REPORT |
| Version | 1.1 |
| Status | APPROVED |
| Stage | S01 |
| Date | 2026-11-20 |
| Depends on | DEC-015; DEC-016; DEC-017; DEC-018; S01 package v1.0 (2026-11-19) |

## 1. Summary

The S01 gate was granted a CONDITIONAL PASS (DEC-015) with six conditions. This report states what changed for each condition and why. All 16 v1.0 files changed, because condition 3 (metadata) touches every header; content changes are limited to the files named below. Three files are new.

## 2. Changes by condition

| # | Condition | What changed | Files | Why |
|---|---|---|---|---|
| 1 | Separate sponsor constraints from governance rules | C-series given a Classification column: C1–C2 **SC** (sponsor-origin constraint), C3 **EA** (evaluator advisory), C4–C6 **PG** (project governance rule, binds the project's work, not the product). Origin column now states where each item comes from, including working-copy annotations. Identifiers unchanged. Dependent references labelled. | S01_REQUIREMENTS_REGISTER §2; 00_PROJECT_RULES §2, §5; S01_RESEARCH_QUESTIONS §3; S01_TRACEABILITY_MATRIX A–B | v1.0 implied that evidence-handling and confidentiality rules were sponsor technical requirements (DEF-S01-01, DEF-S01-08) |
| 2 | Reproducible QC evidence or self-reported label | QC script and its output delivered. Report split into scripted (reproducible) and self-reported checks. "No defects" claim withdrawn; nine defects recorded. Gate protocol now defines both classes and restricts the word "verified". | S01_QC_REPORT (rewritten); S01_QC_CHECK.py (new); S01_QC_CHECK_OUTPUT.txt (new); 00_STAGE_GATE_PROTOCOL §6 | v1.0 claimed scripted validation without evidence, and part of it had been done manually (DEF-S01-02, DEF-S01-03) |
| 3 | Standardize metadata | One six-field header in every file: Document ID, Version, Status, Stage, Date, Depends on. Status vocabulary fixed. Former extra header fields moved to a short note list below the table. Standard defined once. | All files; 00_PROJECT_RULES §10 (new) | Headers varied by file (DEF-S01-04) |
| 4 | Handoff procedure without Git | Owner and session steps defined: generated files are downloads, not Project knowledge; owner replaces files in the Project keeping names; new session checks presence and versions before work. Handoff lists Tier A (session start, 11 files), Tier B (before S02 gate, 3 files) and Tier C (archive only) with versions, plus a suggested first message. | 00_PROJECT_RULES §4 (replaced); S01_HANDOFF (rewritten); 00_STAGE_STATUS | v1.0 assumed the files would be available to a fresh session (DEF-S01-05) |
| 5 | Preserve research questions, mapping, rules, writing standard | RQ-01 to RQ-15, RF/QA rows and statuses, source tiers and verification rules, and the style guide's rules and pattern list are unchanged in substance. | — | Condition required no restructuring |
| 6 | Source text versus interpretation; no implied dataset | R1–R4 columns renamed "Source text (REF-01, verbatim)" and "Working interpretation (not source text)". R2 interpretation made conditional on the collection being available. ISS-003 now covers whether the collection exists at all; ISS-002 qualified. CLM-012 added. Glossary entry rewritten. C2 quoted verbatim. | S01_REQUIREMENTS_REGISTER §1; 00_OPEN_ISSUES_REGISTER; 02_CLAIM_REGISTER; 03_STYLE_GUIDE §6; S01_TRACEABILITY_MATRIX A | v1.0 R2 wording implied a populated collection (DEF-S01-06, DEF-S01-07) |

## 3. Other updates

| File | Change |
|---|---|
| 00_DECISIONS_LOG | DEC-015 recorded (conditional pass and conditions); DEC-016 proposed (final approval, start S02) |
| 00_STAGE_STATUS | S01 state set to conditional pass, corrections delivered |
| S01_PLAN | Deliverables table lists the three new files |

## 4. File versions in this package

| File | v1.0 → v1.1 | Content change beyond header |
|---|---|---|
| 00_PROJECT_RULES | 1.1 | Yes (§2, §4, §5, §10) |
| 00_STAGE_STATUS | 1.1 | Yes |
| 00_STAGE_GATE_PROTOCOL | 1.1 | Yes (§2, §6) |
| 00_DECISIONS_LOG | 1.1 | Yes |
| 00_OPEN_ISSUES_REGISTER | 1.1 | Yes (ISS-002, ISS-003) |
| 00_SKILL_REGISTER | 1.1 | Header only |
| 02_SOURCE_LOG | 1.1 | Header only |
| 02_CLAIM_REGISTER | 1.1 | Yes (CLM-012) |
| 03_STYLE_GUIDE | 1.1 | Yes (glossary entry) |
| S01_REQUIREMENTS_REGISTER | 1.1 | Yes (§1, §2) |
| S01_REVIEWER_CRITERIA_REGISTER | 1.1 | Header only |
| S01_RESEARCH_QUESTIONS | 1.1 | Yes (§3 labels only) |
| S01_TRACEABILITY_MATRIX | 1.1 | Yes (labels, R2 row) |
| S01_PLAN | 1.1 | Yes (table) |
| S01_QC_REPORT | 1.1 | Rewritten |
| S01_HANDOFF | 1.1 | Rewritten |
| S01_CHANGE_REPORT | 1.0 (new) | — |
| S01_QC_CHECK.py | new | — |
| S01_QC_CHECK_OUTPUT.txt | new | — |

## 5. Version 1.2: approval and GitHub publication

After the owner approved the corrected stage (DEC-016) and switched storage to GitHub (DEC-017, DEC-018), the following changes were made before the first commit. The technical substance of S01 is unchanged.

| Change | Files | Why |
|---|---|---|
| All S01 files set to `APPROVED`, version 1.2 (this report 1.1) | All | DEC-016 |
| DEC-016, DEC-017, DEC-018 recorded; DEC-010 marked partly superseded; DEC-019 proposed (start S02) | project/00_DECISIONS_LOG | Owner decisions of 2026-11-20 |
| Handoff procedure rewritten for the repository; hard boundaries 10–11 added (public repository, no push before approval); stage delivery and metadata notes updated | project/00_PROJECT_RULES §3, §4, §9, §10 | DEC-017, DEC-018 |
| Gate checklist item for commit, tag and push after approval | project/00_STAGE_GATE_PROTOCOL §2 | DEC-017 |
| Stage status set to approved and published | project/00_STAGE_STATUS | DEC-016 |
| Upload tiers replaced with repository paths and a session-start check against the tag | stages/S01/S01_HANDOFF | DEC-017 |
| QC script adapted to the repository layout; credential scan, file-inventory check and entry-file scan added; report updated | stages/S01/qc/S01_QC_CHECK.py; stages/S01/S01_QC_REPORT | Pre-commit safety requirement |
| `CLAUDE.md`, `README.md`, `.gitignore` added; empty `stages/S02` to `stages/S10` and `proposal/` folders created | Repository root | DEC-018 |

**File placement (DEC-018).** Living documents are in `project/`: the nine `00_`, `02_` and `03_` files and the four S01 registers (requirements, reviewer criteria, research questions, traceability). Stage-only files are in `stages/S01/`: plan, QC report, change report, handoff and `qc/`.

**Not committed.** The three reference documents (kept in the Claude Project), the downloadable zip packages, and any URL or account name.

