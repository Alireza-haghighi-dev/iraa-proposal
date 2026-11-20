# 00_SKILL_REGISTER

| Field | Value |
|---|---|
| Document ID | 00_SKILL_REGISTER |
| Version | 2.0 |
| Status | SUBMITTED FOR GATE |
| Stage | S02 |
| Date | 2026-11-20 |
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

## 3. Forward notes for the S02 checkpoint

| Candidate | Origin | Possible use in S02 | Concerns to evaluate |
|---|---|---|---|
| deep-research | Built-in (Anthropic) | Parallel literature search across RQ-01 to RQ-09 | Uses subagents (requires owner authorization); produces narrative reports that would need conversion into SRC/CLM records; risk of sources not individually inspected |
| pdf-reading | Built-in (Anthropic) | Reading open-access papers retrieved as PDFs | Low risk; check that extracted figures are verified against the page |
| Third-party research or citation-verification Skills | To be proposed by owner | Citation checking, structured extraction | Full security review required before any use |

No Skill was used in S02. For S03, the same candidates apply; patent-database access may raise new needs (RQ-12).
