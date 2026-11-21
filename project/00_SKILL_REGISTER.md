# 00_SKILL_REGISTER

| Field | Value |
|---|---|
| Document ID | 00_SKILL_REGISTER |
| Version | 8.0 |
| Status | SUBMITTED FOR GATE |
| Stage | S08 |
| Date | 2026-11-21 |
| Depends on | DEC-005 |

## 1. Checkpoint procedure (run at the start of every stage)

1. **Need**: name the specific quality gap a Skill would close in this stage. No gap means "no Skill".
2. **Candidates**: list candidates and origin (built-in Anthropic, organization-provided, third-party). Discovery and initial selection are coordinated with the owner.
3. **Security review** (any non-built-in Skill): publisher and repository provenance; pinned version or commit; full reading of SKILL.md and every script; check for network calls, telemetry, credential access, writes outside the workspace and obfuscated code; licence; dry run on non-project dummy data.
4. **Fitness**: does the output fit the evidence format (SRC/CLM IDs, claim labels) and the writing standard, or would it need rewriting?
5. **Decision**: ADOPT / REJECT / DEFER, with reason. Execution requires an owner authorization DEC entry.

## 2. Evaluations

| ID | Stage | Need identified | Candidates considered | Security review | Decision | Authorization |
|---|---|---|---|---|---|---|
| SKL-001 | S01 | None. S01 is extraction and structuring from three short reference documents; no external research. | None | Not applicable | No Skill used | Not required |
| SKL-002 | S02 | Systematic literature search with per-source verification | Catalog search for research or citation Skills: no results. Built-in `deep-research` evaluated. Built-in `pdf-reading` available. | Not applicable (no third-party Skill) | `deep-research` DEFERRED: it delegates searches to subagents and returns narrative reports, while S02 requires each source to be opened and logged individually. Direct web search used instead. `pdf-reading` not needed: abstracts and landing pages were sufficient at the recorded depth. | Not required |
| SKL-003 | S03 | Reading vendor help pages and patent records one by one, with per-statement verification | Catalog search (patent search, prior art, competitive analysis, citation verification): no results. Built-in `deep-research` and `pdf-reading` re-evaluated. | Not applicable (no third-party Skill) | `deep-research` DEFERRED for the S02 reason: subagent narrative output does not meet the per-source logging rule. `pdf-reading` not used: the USPTO PDFs returned no machine-readable text through the fetch tool, so the Skill could not help without file access. Direct search and fetch used. | Not required |
| SKL-004 | S04 | None requiring a Skill. S04 is design and drafting from loaded registers, plus two standards-body pages for RQ-13. | Catalog search (software architecture, system design, technical proposal, architecture diagram, requirements traceability): no results. Built-in `docs` considered and rejected: deliverables must be versioned Markdown in the repository. Built-in `dataviz` not applicable: diagrams are Mermaid source in Markdown, not charts. `deep-research` not needed (two sources). | Not applicable (no third-party Skill) | No Skill used | Not required |
| SKL-005 | S04.1 | None requiring a Skill. S04.1 corrects existing Markdown registers and drafts from loaded files; no new research. | Built-in `docs` not applicable (repository Markdown is the canonical format); `deep-research` not applicable (no search). | Not applicable (no third-party Skill) | No Skill used | Not required |
| SKL-006 | S05 | Reading official service, model and licence pages one by one for RQ-14 and RQ-15, with per-statement logging | Built-in `deep-research` re-evaluated; built-in `pdf-reading` considered for licence documents; `dataviz` and `docs` not applicable (repository Markdown, no charts) | Not applicable (no third-party Skill) | No Skill used. `deep-research` DEFERRED for the S02 reason (subagent narrative output does not meet the per-source logging rule). `pdf-reading` not needed: the pages read were HTML. Direct search and fetch used; two pages (SRC-063 record, EPO OPS landing page) were not reachable by fetch and were handled by search-result extracts or left OPEN | Not required |
| SKL-007 | S06 | None requiring a Skill. S06 plans work packages from approved S04 and S05 Markdown files; no external research, no charts, no non-Markdown output. | Built-in `docs` not applicable (repository Markdown is the canonical format); `xlsx` considered for the effort table and rejected (the QC script recomputes the figures from Markdown); `deep-research` not applicable (no search) | Not applicable (no third-party Skill) | No Skill used | Not required |
| SKL-008 | S07 | Reading a small number of licence, package and guideline pages one by one (ISS-041, ISS-044, statistical sources), and drafting Section 12 as repository Markdown | Built-in `pdf-reading` (licence or guideline documents as PDF); built-in `deep-research`; built-in `docs` (document output); `dataviz` (no charts needed) | Not applicable (no third-party Skill) | No Skill used. The pages needed were HTML and were read with the web tools, so `pdf-reading` was not needed; `deep-research` DEFERRED for the S02 reason (subagent narrative output does not meet the per-source logging rule, and fewer than ten sources were needed); `docs` not applicable because the repository Markdown is the canonical format and the owner reviews drafts there | Not required |
| SKL-009 | S08 | Assembling and editing repository Markdown; a small number of targeted source checks (Pass A) | Built-in `docs` (shareable review copy), `pdf-reading` (full-text PDFs), `deep-research` | Not applicable (no third-party Skill) | No Skill used. Repository Markdown is canonical and the owner reviews it there, so `docs` was not used; Pass A needed only targeted search extracts, so `deep-research` was not applicable; page fetching required approval that was unavailable, so `pdf-reading` could not be applied to downloaded files | Not required |

## 3. Forward notes

| Candidate | Origin | Possible use in S02 | Concerns to evaluate |
|---|---|---|---|
| deep-research | Built-in (Anthropic) | Parallel literature search across RQ-01 to RQ-09 | Uses subagents (requires owner authorization); produces narrative reports that would need conversion into SRC/CLM records; risk of sources not individually inspected |
| pdf-reading | Built-in (Anthropic) | Reading open-access papers retrieved as PDFs | Low risk; check that extracted figures are verified against the page |
| Third-party research or citation-verification Skills | To be proposed by owner | Citation checking, structured extraction | Full security review required before any use |

No Skill was used in S02 to S08. A shareable review copy of the English master (`docs`) can be made on owner request; the repository stays canonical.
