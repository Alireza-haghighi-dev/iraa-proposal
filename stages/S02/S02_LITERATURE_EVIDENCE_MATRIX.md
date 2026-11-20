# S02_LITERATURE_EVIDENCE_MATRIX

| Field | Value |
|---|---|
| Document ID | S02_LITERATURE_EVIDENCE_MATRIX |
| Version | 1.0 |
| Status | SUBMITTED FOR GATE |
| Stage | S02 |
| Date | 2026-11-20 |
| Depends on | S01_RESEARCH_QUESTIONS; 02_SOURCE_LOG (SRC-001 to SRC-039); DEC-002 |

- **Reading the matrix:** each row is one finding from one or more logged sources. "Finding" paraphrases what the source states at the verification depth recorded in `02_SOURCE_LOG.md` (A = abstract or landing page read; P = full-text excerpt read; B = bibliographic record only). No row reports a result obtained by this project.
- **Applicability** rates transfer to this project's submissions (organizational, operational and technology needs or challenges, DEC-002): **Direct** (same kind of text and task), **Close** (similar user-submitted text, similar task), **Analogous** (different domain, same mechanism), **Low** (mechanism only).
- **Label** follows `00_PROJECT_RULES.md` §6. VERIFIED applies to the source's statement, never to its transfer to this project; transfer is always an ASSUMPTION until tested in S05.

## RQ-01 Text representation and similarity methods (R1, R2)

| # | Method family | Finding | Sources | Setting | Applicability | Limitations for this project | Compute / reproducibility | Label |
|---|---|---|---|---|---|---|---|---|
| 1.1 | Lexical (BM25, BM25F) | BM25 is the best-known ranking function of the probabilistic relevance framework; BM25F extends it to documents with several fields. | SRC-001 | Theory and review | Close: submissions are likely to have title and description fields (ASSUMPTION, ISS-008) | Exact-term matching misses paraphrase and synonyms | Inverted index; no training data; widely implemented (SRC-036) | VERIFIED |
| 1.2 | Lexical vs neural, zero-shot | Across 18 public datasets and 10 retrieval systems, BM25 remained competitive with the neural systems; re-ranking and late-interaction models had the best average zero-shot results at high computational cost; dense and sparse neural retrievers were more efficient but often underperformed. | SRC-002 | Heterogeneous benchmark, no in-domain training | Analogous: no benchmark of need/challenge submissions exists in BEIR | Benchmark domains differ from organizational needs; averages hide per-dataset variation | Open benchmark and code (SRC-002) | VERIFIED |
| 1.3 | Dense bi-encoder (sentence embeddings) | Siamese/triplet fine-tuning of BERT yields sentence embeddings comparable by cosine similarity; for 10,000 sentences, finding the most similar pair drops from about 65 hours (cross-encoding every pair) to about 5 seconds. | SRC-003 | STS and transfer tasks | Close | Short-text oriented; quality on longer descriptions not shown here | Embeddings computed once per text, then compared cheaply | VERIFIED |
| 1.4 | Dense retrieval trained in-domain | A dual-encoder trained on question–passage pairs outperformed a Lucene BM25 system by 9–19 percentage points in top-20 passage retrieval accuracy on open-domain QA. | SRC-004 | Open-domain QA with training pairs | Analogous | Gains depend on in-domain training pairs, which this project may not have (ISS-002) | Requires labelled pairs and GPU training | VERIFIED |
| 1.5 | Embedding model choice | Across 8 tasks, 58 datasets and 112 languages, no single embedding method dominated all tasks. | SRC-005 | Benchmark of 33 models | Analogous | Leaderboard rank does not predict performance on submissions | Open code and leaderboard | VERIFIED |
| 1.6 | Cross-encoder re-ranking | A BERT cross-encoder re-ranking BM25 candidates reached the top of the MS MARCO passage leaderboard, about 27% relative MRR@10 above the previous best; the design is two-stage (cheap retrieval, expensive re-ranking). | SRC-006 | Web passage ranking with large training set | Analogous | Fine-tuned on a very large labelled set; cost grows with candidate count | Code released by authors | VERIFIED |
| 1.7 | LLM as re-ranker | Instructed GPT-4 re-ranking matched or exceeded a fine-tuned monoT5-3B on TREC and BEIR subsets (average gains of 2.3–2.7 nDCG in the reported settings); a 440M-parameter model distilled from it outperformed a 3B supervised model on BEIR. The authors built a new test set to address data-contamination concerns. | SRC-032 | Benchmarks plus new test set | Analogous | Hosted-model use depends on ISS-009; contamination concern acknowledged by authors | Code released; inference cost per query | VERIFIED |
| 1.8 | Hybrid fusion (RRF) | Reciprocal Rank Fusion, an unsupervised rank-combination method, almost always improved on the best of the combined runs in the authors' experiments. | SRC-007 | TREC runs | Analogous | Evidence from 2009 runs; not tested on lexical+dense pairs in that paper | No training; one constant | VERIFIED |
| 1.9 | Hybrid fusion (score combination) | For lexical+semantic fusion, RRF was sensitive to its parameters; a convex combination of normalized scores outperformed RRF in- and out-of-domain and needed only a small set of labelled examples to tune its weight. | SRC-008 | Benchmarks | Analogous | Authors were affiliated with a vector-database vendor (disclosed for balance) | Needs a small labelled tuning set | VERIFIED |
| 1.10 | Multi-function embeddings | One model offers dense, sparse and multi-vector retrieval, more than 100 languages and inputs up to 8,192 tokens. | SRC-033 | Benchmarks reported by authors | Close (relevant to ISS-007 and long descriptions) | Author-reported results; not independently checked here | Larger model than MiniLM-class encoders | VERIFIED (source claim) |
| 1.11 | Compact encoder | `all-MiniLM-L6-v2` maps sentences and paragraphs to 384-dimensional vectors for clustering or semantic search. | SRC-037 | Official model card | Close | Training data and limits not verified from the official card in this stage | Small vectors; low storage | VERIFIED |

## RQ-02 Duplicate and near-duplicate detection (R1, ISS-004)

| # | Method family | Finding | Sources | Setting | Applicability | Limitations for this project | Compute / reproducibility | Label |
|---|---|---|---|---|---|---|---|---|
| 2.1 | Idea-management duplicates | Duplicate detection is a common way Idea Management Systems cope with large idea volumes; the authors argue for richer relationship types than "duplicate" and annotate idea datasets with them, using Lucene keyword similarity to surface candidates. | SRC-013 | Public idea-management datasets | **Direct** (closest setting found) | 2012 study; keyword similarity only; annotation scheme not validated across organizations | Lucene-based | VERIFIED |
| 2.2 | Retrieval-style duplicate search | Duplicate bug-report retrieval combined an extended BM25F with non-text fields (REP), tuned by supervised learning; on 209,058 Eclipse reports it reported recall@k of 37–71% and MAP of 47%. | SRC-009 | Software issue trackers | Close (user-submitted reports describing problems) | Different vocabulary; relies on structured fields | Needs labelled duplicates for tuning | VERIFIED |
| 2.3 | Evaluation pitfall | The classical evaluation of duplicate-retrieval approaches overestimated BM25F and REP performance by a median of 17–42% relative to a realistic evaluation; the authors recommend the realistic setup. | SRC-010 | Software issue trackers | Close (evaluation design) | Specific to time-ordered issue data, but the overestimation mechanism applies to any time-ordered submission stream | — | VERIFIED |
| 2.4 | Duplicate-question benchmark | CQADupStack provides 12 StackExchange subforums with user-marked duplicate questions, fixed train/test splits and baseline results. | SRC-011 | Community Q&A | Analogous | Duplicate labels come from forum users; label quality varies | Public dataset; usable as a proxy test set if ISS-002 blocks real data | VERIFIED |
| 2.5 | Near-duplicate (syntactic) | Resemblance (Jaccard over word shingles) and containment can be estimated from small fixed-size sketches computed in linear time. | SRC-012 | Web documents | Low to Close: finds re-submitted or copied text, not paraphrased needs | Syntactic only; misses rewording | Very cheap; no training | VERIFIED |

## RQ-03 Matching needs to solutions and internal precedents (R2)

| # | Method family | Finding | Sources | Setting | Applicability | Limitations for this project | Compute / reproducibility | Label |
|---|---|---|---|---|---|---|---|---|
| 3.1 | Review of NLP in innovation search | A review of NLP for innovation search lists problem–solution matching among the practices NLP supports; the review's own table counts only three studies on problem–solution matching. | SRC-015 | Literature review | **Direct** | Small evidence base for the exact task | — | VERIFIED |
| 3.2 | Structural (purpose/mechanism) similarity | Learning separate purpose and mechanism representations from product descriptions found analogies with higher precision than standard similarity in the authors' experiments; the authors note that simpler IR similarity scales but misses structural similarity. | SRC-016 | Product descriptions, crowdsourced annotation | Close | Required crowdsourced annotation; product texts differ from organizational needs | Training on annotated data | VERIFIED |
| 3.3 | Retrieval-augmented generation | RAG combines a generator with a dense vector index; the authors note that retrieval-based memory can be inspected and updated, while provenance remains an open problem. | SRC-018 | Knowledge-intensive NLP benchmarks | Analogous | Benchmarks are open-domain QA, not precedent matching | Needs retriever plus generator | VERIFIED |
| 3.4 | AI screening of crowdsourced ideas | In 21 crowdsourcing contests (4,191 ideas), theory-based models could not mimic experts in choosing the best ideas, but a simple model could screen out ideas experts considered bad; the authors present a curve trading false negatives against ideas screened. | SRC-017 | Corporate crowdsourcing contests | Close (screening, not matching) | Screening quality judged against experts; not a solution-matching study | Replication files published by journal | VERIFIED |
| 3.5 | Semantic novelty of ideas | Doc2Vec, SBERT and GPT-3 Ada embeddings were used to compute the semantic distance of crowdsourced ideas to reference sets for novelty detection. | SRC-014 | Crowdsourced idea spaces | Close (inverse of duplicate detection) | Abstract-level verification only; quantitative results not checked | — | VERIFIED |

## RQ-04 Patent and prior-art retrieval (R4)

| # | Method family | Finding | Sources | Setting | Applicability | Limitations for this project | Compute / reproducibility | Label |
|---|---|---|---|---|---|---|---|---|
| 4.1 | Patent retrieval review | Patent retrieval underpins most patent-analysis tasks; the review judges automatic performance to be around average and argues for interactive tools that assist patent professionals. | SRC-019 | Literature review (to 2018) | Close | Predates current embedding models | — | VERIFIED |
| 4.2 | Domain-adapted sentence embeddings for patents | SBERT embeddings of patent claims, fine-tuned with an augmented in-domain approach, supported patent-to-patent similarity and a kNN classifier that predicted CPC subclasses (663 labels) with an F1 of 66%. | SRC-020 | Patent claims | Close (patent side of R4) | Measured on classification, not need-to-patent retrieval | Public model with 768-dimensional output (model card cited in SRC-020) | VERIFIED |
| 4.3 | Query–document mismatch | Need statements are short and non-technical, while patents are long and formal; no source in this stage measures retrieval from organizational need statements to patents. | — | — | — | Evidence gap (ISS-028) | — | OPEN |

## RQ-05 Human-in-the-loop decision support (R3)

| # | Topic | Finding | Sources | Setting | Applicability | Limitations for this project | Label |
|---|---|---|---|---|---|---|---|
| 5.1 | Interaction guidelines | Eighteen human–AI interaction guidelines were validated with 49 design practitioners testing them against 20 AI-infused products. | SRC-021 | Consumer and productivity products | Close (UI design of review screens) | Guidelines, not effect sizes | VERIFIED |
| 5.2 | Automation bias | Automation bias produces both omission and commission errors when aids are imperfect, occurs in naive and expert users, and is not prevented by training or instructions; complacency arises under multiple-task load. | SRC-022 | Review across aviation, medicine, process control | Close (assessors with backlog pressure, CTX-01) | Domains differ; mechanism transfers | VERIFIED |
| 5.3 | Mediators of automation bias | A systematic review found user factors (cognitive style, decision-support experience, task experience) and attitudes (trust, confidence) mediate automation bias. Mitigators are reported in the review but were not verified at abstract level in this stage. | SRC-023 | Mainly clinical decision support | Close | Mitigator details OPEN | VERIFIED (mediators); OPEN (mitigators) |
| 5.4 | Explanations and overreliance | Adding explanations did not reduce overreliance and may increase it; three cognitive-forcing designs reduced overreliance compared with simple explanation designs (N = 199); benefits were larger for people higher in need for cognition. | SRC-024 | Controlled experiment | Close | Lab task; effect on expert assessors untested | VERIFIED |
| 5.5 | Screening versus selection | Computational screening could remove clearly weak ideas but could not mimic experts in picking the best (see 3.4). | SRC-017 | Crowdsourcing contests | Close | — | VERIFIED |

## RQ-06 Evaluation with scarce labelled data (QA-002, QA-004)

| # | Topic | Finding | Sources | Applicability | Limitations for this project | Label |
|---|---|---|---|---|---|---|
| 6.1 | Graded relevance metrics | Cumulated-gain measures (including the normalized form, nDCG) credit systems for placing highly relevant documents early under graded relevance judgments. | SRC-025 | Direct (ranked suggestion lists) | Needs graded judgments from assessors (ISS-012) | VERIFIED |
| 6.2 | Assessor disagreement | Individual relevance assessments vary widely; in NIST's study, comparative rankings of systems remained stable despite those differences. | SRC-026 | Direct (small assessor pool) | Stability shown for TREC-scale topic sets; small test sets may be less stable | VERIFIED |
| 6.3 | Agreement statistic | Cohen's kappa measures chance-corrected agreement between two raters on nominal categories. | SRC-027 | Direct | Bibliographic verification only; interpretation thresholds not adopted here | VERIFIED (bibliographic) |
| 6.4 | Realistic duplicate evaluation | Time-ordered, realistic evaluation avoids the overestimation seen with classical setups (see 2.3). | SRC-010 | Close | — | VERIFIED |
| 6.5 | Reproducible baselines | Pyserini packages sparse, dense and hybrid first-stage retrieval with queries, relevance judgments, prebuilt indexes and evaluation scripts for common test collections. | SRC-036 | Direct (baseline tooling) | Version and licence to be verified in S05 (QA-010) | VERIFIED |
| 6.6 | Proxy benchmarks | BEIR, MTEB and CQADupStack provide public data and code for comparing methods before any sponsor data is available. | SRC-002, SRC-005, SRC-011 | Analogous | Proxy results do not predict performance on submissions | VERIFIED |

## RQ-07 Multilingual retrieval (conditional)

Not activated. ISS-007 is unresolved. SRC-033 and SRC-005 are logged because they also bear on RQ-01; no cross-lingual research was carried out.

## RQ-08 Reliability of LLM-generated summaries and citations (R2, R3, R4, RF-004)

| # | Topic | Finding | Sources | Applicability | Limitations for this project | Label |
|---|---|---|---|---|---|---|
| 8.1 | Citation verifiability | In a human audit of four generative search engines, about 51.5% of generated sentences were fully supported by citations and 74.5% of citations supported their sentence; citation quality correlated inversely with fluency and perceived utility. | SRC-028 | Close (assistant summaries citing precedents or patents) | Commercial systems in 2023; newer systems untested here | VERIFIED |
| 8.2 | Citation benchmark | On the ALCE benchmark, even the best models lacked complete citation support about half the time on ELI5; automatic citation metrics correlated with human judgments. | SRC-029 | Close | Benchmark tasks differ | VERIFIED |
| 8.3 | Long-context position effect | Language models used information at the start or end of the input better than information in the middle, and performance fell as inputs grew longer. | SRC-031 | Close (many retrieved items in one prompt) | Models tested in 2023 | VERIFIED |
| 8.4 | Hallucination taxonomy | A survey covers hallucination metrics and mitigation methods across summarization, dialogue, generative QA, data-to-text and translation. | SRC-030 | Analogous | Abstract-level only | VERIFIED |

## RQ-09 Learning from recorded assessor decisions (C3 future, C1)

| # | Topic | Finding | Sources | Applicability | Limitations for this project | Label |
|---|---|---|---|---|---|---|
| 9.1 | Learning to rank | Learning-to-rank builds a ranking model from training data; approaches divide into pointwise, pairwise and listwise. | SRC-038 | Close (future use of assessor decisions as training data) | Future capability only (C3) | VERIFIED |
| 9.2 | Active learning | An active learner asks an oracle, such as a human annotator, to label chosen instances, aiming at accuracy with fewer labels. | SRC-039 | Close (annotation budget, ISS-012) | Could serve S05 test-set construction; adoption is a design decision | VERIFIED |

## Infrastructure evidence (supports RQ-01, RQ-15 preparation)

| # | Component | Finding | Sources | Label |
|---|---|---|---|---|
| I.1 | Approximate nearest-neighbour search | HNSW builds a multi-layer proximity graph incrementally and reports logarithmic complexity scaling. | SRC-035 | VERIFIED |
| I.2 | Vector search library | Faiss is a library of vector indexing and search methods; it is not a database and provides no concurrent writes, sharding or transactions. | SRC-034 | VERIFIED |

## Leads recorded for S03 (not evidence)

| Lead | Why relevant | Next step |
|---|---|---|
| A published European patent application titled "Method and system for matching technical needs to solutions" (EP2765543A1) | Possible prior art for RQ-12 | Retrieve and verify the record in S03 |
| Corporate crowdsourcing platform whose contest data underlies SRC-017 | Possible comparator for RQ-11 | Verify from primary sources in S03 |
