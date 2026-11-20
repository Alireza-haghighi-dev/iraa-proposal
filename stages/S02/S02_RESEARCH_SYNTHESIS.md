# S02_RESEARCH_SYNTHESIS

| Field | Value |
|---|---|
| Document ID | S02_RESEARCH_SYNTHESIS |
| Version | 2.0 |
| Status | SUBMITTED FOR GATE |
| Stage | S04.1 |
| Date | 2026-11-20 |
| Depends on | S02_LITERATURE_EVIDENCE_MATRIX; 02_SOURCE_LOG; 02_CLAIM_REGISTER; S01_REQUIREMENTS_REGISTER; DEC-029 |

- **S04.1 revision:** only the R2 row of §2 changed, to follow the corrected R2 (DEC-029). The evidence, the other rows and the conclusions approved under DEC-022 are unchanged.
- **Purpose:** state what the S02 evidence means for R1–R4 and what it does not settle. Matrix rows are cited as M-x.y (for example, M-1.2).
- **Status of statements:** findings are VERIFIED at the depth recorded in the source log. Everything under "Candidate approaches" is PROPOSED input to S04–S05, not a design decision. Transfer of any finding to the sponsor's submissions is an ASSUMPTION until the S05 evaluation tests it.

## 1. Main findings

**No single retrieval method is a safe default.** BM25 held up as a strong zero-shot baseline across heterogeneous benchmarks, while dense retrievers were cheaper than re-rankers but often weaker out of domain (M-1.2). Dense retrievers clearly outperformed BM25 when trained on in-domain pairs (M-1.4), and no embedding model led every task in MTEB (M-1.5). For this project the deciding variable is therefore whether labelled sponsor data exists (ISS-002). Without it, the evidence favours comparing lexical, dense and hybrid retrieval on a purpose-built test set rather than choosing one method from benchmark tables.

**Combining lexical and dense retrieval is well motivated, but the fusion method matters.** Reciprocal Rank Fusion needs no training and improved on its inputs in the original experiments (M-1.8). A later analysis of lexical-plus-semantic fusion found RRF sensitive to its parameters and a tuned convex combination better, with only a small labelled set needed for tuning (M-1.9). Both results come from public benchmarks; neither has been tested on need or challenge texts.

**Re-ranking improves ranking quality at a predictable cost.** Cross-encoder re-ranking of a short candidate list reached top benchmark results (M-1.6), and instructed LLMs can re-rank competitively (M-1.7). The cost grows with the number of candidates scored, and the hosted-LLM option depends on the data-handling decision (ISS-009).

**The closest domain evidence is thin.** Only one study found addresses duplicate detection inside idea-management systems directly; it used keyword similarity and argued that "duplicate" is too coarse a relationship (M-2.1). A review of NLP for innovation search counts three studies on problem–solution matching (M-3.1). Most transferable evidence therefore comes from neighbouring tasks: duplicate bug reports (M-2.2), duplicate questions (M-2.4) and analogy search over product descriptions (M-3.2).

**Evaluation design can inflate results.** In duplicate-report retrieval, a classical evaluation setup overestimated performance by a median of 17–42% compared with a time-ordered, realistic setup (M-2.3). Assessor judgments vary widely, although system rankings tend to stay stable (M-6.2). Both points bear directly on QA-002 and QA-004.

**Human review does not neutralize automation errors by itself.** Automation bias produces omission and commission errors, affects experts and is not prevented by training or instructions (M-5.2). Explanations did not reduce overreliance in a controlled study, while cognitive-forcing designs did (M-5.4). R3 (final human approval) is necessary but not sufficient. The review interface has to make the assessor engage with the evidence, and the evaluation has to check for overreliance.

**Generated summaries need citation checks.** Audits of generative search found that a substantial share of generated sentences lacked full citation support and that some citations did not support their sentence (M-8.1, M-8.2). Information placed mid-prompt is used less reliably (M-8.3). Any LLM component that summarizes precedents or patents for assessors needs an explicit citation and grounding check.

**Computational screening complements experts rather than replacing them.** In corporate crowdsourcing contests, a model could screen out clearly weak ideas but could not reproduce experts' choice of the best ideas (M-3.4).

## 2. Requirement-level implications

| Requirement | What the evidence supports | What remains unsettled |
|---|---|---|
| R1 Similarity among stored submissions | Retrieval-style duplicate search with lexical, dense and hybrid candidates (M-1.x, M-2.2); syntactic near-duplicate detection for re-submitted text (M-2.5); richer relationship labels than duplicate/not-duplicate (M-2.1) | Which interpretation of R1 applies (ISS-004); availability of labelled pairs (ISS-002) |
| R2 Existing solution examples for a submitted need (corrected S04.1) | Retrieval over a document collection with optional grounded summaries (M-3.3); structural purpose/mechanism matching as a research option (M-3.2); direct evidence for need-to-solution matching is thin (M-3.1). These methods apply to whichever source is chosen | Which sources count and whether any is available to the project (ISS-003, ISS-037, CLM-045); grounding quality on sponsor texts (M-8.x) |
| R3 Human approval | Interaction guidelines (M-5.1); automation-bias mechanisms and the effect of cognitive forcing (M-5.2, M-5.4) | Which assessor decisions the assistant supports (ISS-005); mitigator details from SRC-023 (OPEN) |
| R4 External patents and solution examples | Patent retrieval is hard and best supported interactively (M-4.1); domain-adapted patent embeddings exist (M-4.2) | No evidence on retrieval from organizational need statements to patents (M-4.3, ISS-028); data sources and licences (ISS-006, RQ-14) |

## 3. Candidate approaches for S04–S05 (PROPOSED)

These follow from the evidence above. S04 and S05 will accept, adapt or reject them.

1. **Multi-stage retrieval as the evaluation frame.** First-stage candidates from BM25 and from one compact and one larger embedding model, a fusion step (RRF and convex combination compared) and an optional cross-encoder re-ranker. The baselines are built with reproducible tooling (M-6.5). Rationale: M-1.2, M-1.6, M-1.8, M-1.9.
2. **A purpose-built, time-ordered test set.** Pairs judged by assessors on a graded scale, with agreement measured between at least two judges and evaluation that respects submission order. Rationale: M-2.3, M-6.1 to M-6.3. If sponsor data is unavailable, a public proxy (for example CQADupStack) is used and labelled as a proxy (M-6.6).
3. **Relationship labels beyond binary duplicates** (for example duplicate, overlapping, related, unrelated), defined with assessors. Rationale: M-2.1.
4. **Evidence-first review screens.** Retrieved items are shown with source passages before any generated summary, and the assessor records a decision and reason. Rationale: M-5.2, M-5.4, M-8.1.
5. **Citation checks for any generated text.** Each summary sentence must cite a retrieved item, with automatic support checking and a rejection path. Rationale: M-8.1 to M-8.3.
6. **Logging of assessor decisions** so that learning-to-rank or active learning can be added in a later phase without changing the current scope. Rationale: M-9.1, M-9.2, C1, C3.

## 4. Computational and reproducibility notes (verified facts only)

- Bi-encoder embeddings are computed once per text and compared cheaply; cross-encoding every pair is orders of magnitude slower (M-1.3).
- Re-rankers and late-interaction models carry high computational cost relative to first-stage retrievers (M-1.2).
- A compact sentence encoder produces 384-dimensional vectors (M-1.11); a multi-function model accepts inputs up to 8,192 tokens and more than 100 languages (M-1.10).
- Approximate nearest-neighbour search with HNSW scales logarithmically (I.1). Faiss is a search library rather than a database (I.2), so persistence, concurrent updates and access control must come from elsewhere in the architecture.
- Public benchmarks with released code (BEIR, MTEB, CQADupStack) and the Pyserini toolkit allow baseline results to be reproduced before sponsor data is available (M-6.5, M-6.6).

Hardware sizing, latency targets and licence checks are deferred to RQ-15 and S05 (QA-010).

## 5. Evidence gaps

| Gap | Consequence | Recorded as |
|---|---|---|
| No public benchmark of organizational need/challenge submissions | All performance figures in the proposal must come from the project's own evaluation or be labelled as proxy results | ISS-028 |
| No study of retrieval from need statements to patents | R4 performance cannot be estimated in advance; S05 must design a small judged sample | ISS-028 |
| Mitigator details of automation bias not verified (SRC-023) | Review-screen design relies on M-5.4 until verified | Matrix row 5.3 |
| Most sources verified at abstract level | Quantitative claims reused in the proposal need full-text checks in S08 Pass A | 02_SOURCE_LOG depth column |

## 6. Research-question status after S02

| RQ | Status | Basis |
|---|---|---|
| RQ-01 | Closed for S02 | 11 findings, 10 sources |
| RQ-02 | Closed for S02 | 5 findings; one direct-domain source |
| RQ-03 | Partially closed | Thin direct evidence (M-3.1); carried to S04 as a design risk |
| RQ-04 | Partially closed | Gap M-4.3 carried to S05 (ISS-028) |
| RQ-05 | Closed for S02, with one open detail | Mitigator details (M-5.3) |
| RQ-06 | Closed for S02 | 6 findings |
| RQ-07 | Not activated | ISS-007 |
| RQ-08 | Closed for S02 | 4 findings |
| RQ-09 | Closed for S02 | 2 findings; future capability only |
