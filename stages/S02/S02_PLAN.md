# S02_PLAN

| Field | Value |
|---|---|
| Document ID | S02_PLAN |
| Version | 1.0 |
| Status | APPROVED |
| Stage | S02 |
| Date | 2026-11-20 |
| Depends on | S01_HANDOFF; S01_RESEARCH_QUESTIONS; DEC-019; DEC-021 |

## 1. Inputs

| Input | Use |
|---|---|
| S01 baseline, commit 2b5f83c (all 15 required files present at version 1.2; checked read-only before work began) | Rules, research questions, registers |
| RQ-01 to RQ-09 | Research scope; RQ-07 inactive (ISS-007) |
| REF-01 to REF-03 in the Claude Project | Consulted only to confirm requirement wording |

## 2. Execution steps

1. Skill checkpoint (SKL-002).
2. Search each research question with short, specific queries; open the landing page, abstract or full text of every candidate; log the statement used and its verification depth.
3. Verify authorship and bibliographic details where search snippets were ambiguous (three papers checked; one author list corrected before logging).
4. Build the evidence matrix by research question, with applicability to need/challenge submissions and limitations per finding.
5. Write the synthesis: requirement-level implications, candidate approaches labelled PROPOSED, computational notes, gaps.
6. Update the living registers; run the S02 QC script; write the QC report and handoff; commit and push (DEC-021).

## 3. Search log (supports CLM-025)

Queries were run with the web search tool on 2026-11-20. "Standard" and "extended" refer to the tool's search modes.

| RQ | Queries (summarized) | Mode |
|---|---|---|
| RQ-01 | BEIR zero-shot benchmark; Sentence-BERT; BM25 probabilistic relevance framework; Dense Passage Retrieval; MTEB; BERT passage re-ranking; reciprocal rank fusion; fusion functions for hybrid retrieval; LLM re-ranking agents; BGE M3 embedding; all-MiniLM-L6-v2 model card | Standard |
| RQ-02 | Duplicate issue-report evaluation; duplicate bug-report retrieval (BM25F/REP); CQADupStack; Broder resemblance and containment; idea-management duplicate detection; idea relationship analysis | Standard and extended |
| RQ-03 | Matching technology needs to solutions; NLP for innovation search review; novelty detection in crowdsourced ideas; analogy mining; AI idea screening in crowdsourcing; retrieval-augmented generation | Standard and extended |
| RQ-04 | Patent retrieval literature review; PatentSBERTa | Standard |
| RQ-05 | Human–AI interaction guidelines; complacency and automation bias; automation-bias systematic review; cognitive forcing functions | Standard |
| RQ-06 | Cumulated gain (nDCG); variations in relevance judgments; Cohen's kappa; Pyserini | Standard |
| RQ-08 | Verifiability of generative search engines; LLM citation generation (ALCE); hallucination survey; lost in the middle | Standard |
| RQ-09 | Learning to rank; active learning survey | Standard |
| Infrastructure | Faiss library; HNSW | Standard |

No search in this stage returned a public benchmark of organizational need or challenge submissions, nor a study measuring retrieval from need statements to patents. This is a statement about the searches above, not proof that none exists (CLM-025, ISS-028).

## 4. Deliverables and length budgets

| File | Budget | Purpose |
|---|---|---|
| S02_PLAN.md | ≤ 2 pages | Inputs, steps, search log |
| S02_LITERATURE_EVIDENCE_MATRIX.md | As needed | Findings by research question |
| S02_RESEARCH_SYNTHESIS.md | ≤ 4 pages | Implications, candidate approaches, gaps |
| S02_QC_REPORT.md | ≤ 2 pages | QC results |
| S02_HANDOFF.md | ≤ 1 page | Inputs for S03 |
| qc/S02_QC_CHECK.py, qc/S02_QC_CHECK_OUTPUT.txt | — | Reproducible checks |
| Living registers in `project/` | Updated | Sources, claims, decisions, issues, Skill register, status, traceability |
