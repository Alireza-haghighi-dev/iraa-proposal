# S03_PLAN

| Field | Value |
|---|---|
| Document ID | S03_PLAN |
| Version | 1.0 |
| Status | SUBMITTED FOR GATE |
| Stage | S03 |
| Date | 2026-11-20 |
| Depends on | S02_HANDOFF; S01_RESEARCH_QUESTIONS; DEC-022; DEC-024; DEC-025 |

## 1. Inputs

| Input | Use |
|---|---|
| Repository at commit 961ae6a (S02 approved; content commit 34a7745 and S01 baseline 2b5f83c both present in history; checked before work began) | Rules, registers, S02 leads |
| RQ-10, RQ-11, RQ-12 | S03 scope |
| CLM-001 to CLM-004 (vendor descriptions from REF-01 §10) | Claims to verify |
| S02 matrix "Leads recorded for S03" | EP 2765543 A1; contest-platform lead from SRC-017 |
| REF-01 §10 and REF-02 §9 in the Claude Project | Wording of the four named initiatives; Section 9 table schema |

## 2. Execution steps

1. Skill checkpoint (SKL-003).
2. For each named vendor, locate first-party help-centre or product pages that describe similarity or duplicate detection, AI-assisted evaluation, external technology or patent scouting, and human review. Open each page and record only what it states.
3. Extend to further comparators (RQ-11): two additional idea-management products with documented similar-idea features, one open-source patent prior-art search engine, and one peer-reviewed research system. S02 research systems (SRC-013, SRC-014, SRC-016, SRC-017) are reused, not re-researched.
4. Run the RQ-12 patent search through the web search tool, then open the patent-office or patent-database record for each relevant hit.
5. Build the capability matrix, prior-art register and Section 9 working table; separate vendor statements, marketing claims and undocumented capabilities.
6. Update living registers; run the S03 QC script; write QC report and handoff; commit and push as `SUBMITTED FOR GATE` (DEC-025).

## 3. Search log

All searches were run with the web search tool on 2026-11-20; pages were then opened with the fetch tool. "Standard" and "extended" are the tool's search modes.

| RQ | Queries (summarized) | Mode | Pages opened |
|---|---|---|---|
| RQ-10 | Wazoku duplicate/similar ideas; Wazoku support duplicate; Wazoku AI evaluation; Wazoku Crowd/Innocentive; Brightidea duplicate detection; Brightidea AI features; Brightidea Scout; ITONICS AI similarity/duplicate detection; Wellspring Scout; Wellspring Accolade evaluation; Wellspring AI | Standard | SRC-040 to SRC-050 |
| RQ-11 | IdeaScale duplicate detection; ServiceNow innovation predictive intelligence; PQAI open-source prior-art search; SOLVENT mixed-initiative analogy search; public idea or challenge datasets (CLM-025 re-check) | Standard and extended | SRC-051 to SRC-055, SRC-062, SRC-063 |
| RQ-12 | EP 2765543 A1 matching technical needs to solutions; "innovation exchange network" unmet technical need; matching unmet needs to solutions database; ranking technical solutions to described problems; idea management duplicate detection patent; overlap with prior invention disclosures | Standard and extended | SRC-056 to SRC-061 |

Retrieval limits met during the search are recorded in `S03_PRIOR_ART_REGISTER.md` §4 and ISS-031.

## 4. Deliverables and length budgets

| File | Budget | Purpose |
|---|---|---|
| S03_PLAN.md | ≤ 2 pages | Inputs, steps, search log |
| S03_COMPARABLE_SYSTEMS_MATRIX.md | As needed | Capability matrix, claim verification, implications |
| S03_PRIOR_ART_REGISTER.md | ≤ 4 pages | RQ-12 search protocol and results |
| S03_SECTION9_COMPARISON.md | ≤ 4 pages | Section 9 working table and differentiators (input to S08) |
| S03_QC_REPORT.md | ≤ 2 pages | QC results |
| S03_HANDOFF.md | ≤ 1 page | Inputs for S04 |
| qc/S03_QC_CHECK.py, qc/S03_QC_CHECK_OUTPUT.txt | — | Reproducible checks |
| Living registers in `project/` | Updated | Sources, claims, decisions, issues, Skill register, status, research questions, reviewer criteria, traceability |
