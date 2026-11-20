# 02_SOURCE_LOG

| Field | Value |
|---|---|
| Document ID | 02_SOURCE_LOG |
| Version | 4.0 |
| Status | SUBMITTED FOR GATE |
| Stage | S04 |
| Date | 2026-11-20 |
| Depends on | REF-01; REF-02; REF-03; S02_LITERATURE_EVIDENCE_MATRIX; S03_COMPARABLE_SYSTEMS_MATRIX; S03_PRIOR_ART_REGISTER; S04_ASSUMPTIONS_AND_STANDARDS |

- **Rule:** Every source cited anywhere in the project is logged here before use. No citation from memory. Re-check this log before searching, to avoid repeated research.

## 1. Tier definitions

| Tier | Includes | Permitted use |
|---|---|---|
| T1 | Peer-reviewed publications, standards bodies' official pages, official technical documentation, patent-office records | Methods, capabilities, standards descriptions, prior art |
| T2 | Vendor product pages, vendor documentation, vendor white papers | Evidence of what a vendor states about its own product, labelled as such |
| T3 | Press, blogs, analyst summaries, preprints not yet peer reviewed (unless the preprint is the primary source of a method) | Context only; never sole support for capability, performance or comparator claims |

## 2. Project reference documents

| ID | Document | Nature | Authority |
|---|---|---|---|
| REF-01 | REQUIREMENTS_STATEMENT_EN_WORKING_V1 | Sanitized English working copy of the sponsor's statement of need | Source of product requirements; its claims are not independently verified |
| REF-02 | PROPOSAL_FORM_EN_WORKING_V1 | Sanitized English working copy of the official proposal form | Section order and table schemas; the original form governs formatting |
| REF-03 | REVIEWER_FEEDBACK_EN_V1 | Consolidated secondary reconstruction of reviewer concerns (DEC-011) | Working review criteria; superseded by original reviewer record if supplied |

## 3. External sources

- **Depth key:** A = abstract or landing page read; P = full-text excerpt read; B = bibliographic record only. Verified = Y means the statement used in S02 was found at that depth.
- **Accessed:** all entries 2026-11-20 unless stated.
- **S04 entries (SRC-064, SRC-065):** standards-body records for RQ-13; they describe each standard's scope and do not evidence any organization's conformity.
- **S03 entries (SRC-040 to SRC-063):** T2 rows evidence only what the vendor or project states about itself (C4, QA-005). Patent rows support prior-art statements, not legal conclusions.

| ID | Citation | DOI / URL | Type | Tier | Depth | Verified | Supports | Limitations |
|---|---|---|---|---|---|---|---|---|
| SRC-001 | Robertson, S. & Zaragoza, H. (2009). The Probabilistic Relevance Framework: BM25 and Beyond. Foundations and Trends in Information Retrieval 3(4), 333–389. | doi:10.1561/1500000019 | Monograph | T1 | A | Y | RQ-01, RQ-02 | Theory; no evaluation on need texts |
| SRC-002 | Thakur, N., Reimers, N., Rücklé, A., Srivastava, A. & Gurevych, I. (2021). BEIR: A Heterogeneous Benchmark for Zero-shot Evaluation of Information Retrieval Models. NeurIPS Datasets and Benchmarks. | doi:10.48550/arXiv.2104.08663 | Conference paper | T1 | A | Y | RQ-01, RQ-06 | Benchmark domains differ from submissions |
| SRC-003 | Reimers, N. & Gurevych, I. (2019). Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks. EMNLP-IJCNLP, 3982–3992. | doi:10.18653/v1/D19-1410 | Conference paper | T1 | A | Y | RQ-01 | STS-focused evaluation |
| SRC-004 | Karpukhin, V. et al. (2020). Dense Passage Retrieval for Open-Domain Question Answering. EMNLP, 6769–6781. | doi:10.18653/v1/2020.emnlp-main.550 | Conference paper | T1 | A | Y | RQ-01 | Requires in-domain training pairs |
| SRC-005 | Muennighoff, N., Tazi, N., Magne, L. & Reimers, N. (2023). MTEB: Massive Text Embedding Benchmark. EACL, 2014–2037. | doi:10.18653/v1/2023.eacl-main.148 | Conference paper | T1 | A | Y | RQ-01, RQ-06 | Leaderboard snapshot dates quickly |
| SRC-006 | Nogueira, R. & Cho, K. (2019). Passage Re-ranking with BERT. arXiv preprint. | doi:10.48550/arXiv.1901.04085 | Preprint (primary source of method) | T1 | A | Y | RQ-01 | Not peer reviewed; very large training set |
| SRC-007 | Cormack, G. V., Clarke, C. L. A. & Büttcher, S. (2009). Reciprocal Rank Fusion Outperforms Condorcet and Individual Rank Learning Methods. SIGIR, 758–759. | doi:10.1145/1571941.1572114 | Short paper | T1 | P | Y | RQ-01 | Two-page paper; TREC runs of 2009 |
| SRC-008 | Bruch, S., Gai, S. & Ingber, A. (2024). An Analysis of Fusion Functions for Hybrid Retrieval. ACM Transactions on Information Systems 42(1). | doi:10.1145/3596512 | Journal article | T1 | A | Y | RQ-01 | Authors affiliated with a vector-database vendor |
| SRC-009 | Sun, C., Lo, D., Khoo, S.-C. & Jiang, J. (2011). Towards More Accurate Retrieval of Duplicate Bug Reports. ASE, 253–262. | doi:10.1109/ASE.2011.6100061 | Conference paper | T1 | A | Y | RQ-02 | Software domain; structured fields |
| SRC-010 | Rakha, M. S., Bezemer, C.-P. & Hassan, A. E. (2018). Revisiting the Performance Evaluation of Automated Approaches for the Retrieval of Duplicate Issue Reports. IEEE Transactions on Software Engineering 44(12), 1245–1268. | https://sail.cs.queensu.ca/data/pdfs/TSE2017_RevisitingThePerformanceEvaluationOfAutomatedApproachesForTheRetrievalOfDuplicateIssueReports.pdf | Journal article (author copy) | T1 | A | Y | RQ-02, RQ-06 | DOI not retrieved in S02 |
| SRC-011 | Hoogeveen, D., Verspoor, K. M. & Baldwin, T. (2015). CQADupStack: A Benchmark Data Set for Community Question-Answering Research. ADCS, 3:1–3:8. | https://findanexpert.unimelb.edu.au/scholarlywork/1028211-cqadupstack--a-benchmark-data-set-for-community-question-answering-research | Conference paper | T1 | A | Y | RQ-02, RQ-06 | Duplicate labels assigned by forum users |
| SRC-012 | Broder, A. Z. (1997). On the Resemblance and Containment of Documents. Compression and Complexity of Sequences, 21–29. | https://www.cs.princeton.edu/courses/archive/spring13/cos598C/broder97resemblance.pdf | Conference paper (course copy) | T1 | P | Y | RQ-02 | Syntactic similarity only |
| SRC-013 | Westerski, A., Iglesias, C. A. & Espinosa Garcia, J. (2012). Idea Relationship Analysis in Open Innovation Crowdsourcing Systems. CollaborateCom 2012. | doi:10.4108/icst.collaboratecom.2012.250412 | Conference paper | T1 | A | Y | RQ-02 | Keyword similarity; 2012 data |
| SRC-014 | Just, J., Ströhle, T., Füller, J. & Hutter, K. (2024). AI-based novelty detection in crowdsourced idea spaces. Innovation: Organization & Management (online 2023). | doi:10.1080/14479338.2023.2215740 | Journal article | T1 | A | Y | RQ-03 | Publisher page not retrievable; abstract from indexing pages |
| SRC-015 | Just, J. (2024). Natural language processing for innovation search – Reviewing an emerging non-human innovation intermediary. Technovation 129, 102883. | doi:10.1016/j.technovation.2023.102883 | Review article | T1 | A | Y | RQ-03 | Count of problem–solution studies taken from review table excerpt |
| SRC-016 | Hope, T., Chan, J., Kittur, A. & Shahaf, D. (2017). Accelerating Innovation Through Analogy Mining. KDD, 235–243. | doi:10.1145/3097983.3098038 | Conference paper | T1 | A | Y | RQ-03 | Product descriptions; crowdsourced labels |
| SRC-017 | Bell, J. J., Pescher, C., Tellis, G. J. & Füller, J. (2024). Can AI Help in Ideation? A Theory-Based Model for Idea Screening in Crowdsourcing Contests. Marketing Science 43(1), 54–72. | doi:10.1287/mksc.2023.1434 | Journal article | T1 | A | Y | RQ-03, RQ-05 | Screening, not matching |
| SRC-018 | Lewis, P. et al. (2020). Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks. NeurIPS 33. | doi:10.48550/arXiv.2005.11401 | Conference paper | T1 | A | Y | RQ-03 | Open-domain QA benchmarks |
| SRC-019 | Shalaby, W. & Zadrozny, W. (2019). Patent retrieval: a literature review. Knowledge and Information Systems 61, 631–660. | doi:10.1007/s10115-018-1322-7 | Review article | T1 | A | Y | RQ-04 | Covers literature to 2018 |
| SRC-020 | Bekamiri, H., Hain, D. S. & Jurowetzki, R. (2024). PatentSBERTa: A deep NLP based hybrid model for patent distance and classification using augmented SBERT. Technological Forecasting and Social Change 206. | doi:10.48550/arXiv.2103.11933 | Journal article (preprint DOI cited) | T1 | A | Y | RQ-04 | Classification evaluation, not need-to-patent retrieval |
| SRC-021 | Amershi, S. et al. (2019). Guidelines for Human-AI Interaction. CHI 2019. | doi:10.1145/3290605.3300233 | Conference paper | T1 | A | Y | RQ-05 | Guidelines; no effect sizes |
| SRC-022 | Parasuraman, R. & Manzey, D. H. (2010). Complacency and Bias in Human Use of Automation: An Attentional Integration. Human Factors 52(3), 381–410. | doi:10.1177/0018720810376055 | Review article | T1 | A | Y | RQ-05 | Domains other than innovation management |
| SRC-023 | Goddard, K., Roudsari, A. & Wyatt, J. C. (2012). Automation bias: a systematic review of frequency, effect mediators, and mitigators. JAMIA 19(1), 121–127. | doi:10.1136/amiajnl-2011-000089 | Systematic review | T1 | A | Partial | RQ-05 | Mediators verified; mitigators not verified (full abstract page blocked) |
| SRC-024 | Buçinca, Z., Malaya, M. B. & Gajos, K. Z. (2021). To Trust or to Think: Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making. Proc. ACM HCI 5(CSCW1), Art. 188. | doi:10.1145/3449287 | Journal article | T1 | A | Y | RQ-05 | Lab study, non-expert participants |
| SRC-025 | Järvelin, K. & Kekäläinen, J. (2002). Cumulated Gain-Based Evaluation of IR Techniques. ACM TOIS 20(4), 422–446. | doi:10.1145/582415.582418 | Journal article | T1 | A | Y | RQ-06 | — |
| SRC-026 | Voorhees, E. M. (2000). Variations in relevance judgments and the measurement of retrieval effectiveness. Information Processing & Management 36(5), 697–716. | doi:10.1016/S0306-4573(00)00010-8 | Journal article | T1 | A | Y | RQ-06 | TREC-scale topic sets |
| SRC-027 | Cohen, J. (1960). A coefficient of agreement for nominal scales. Educational and Psychological Measurement 20, 37–46. | Bibliographic record via secondary sources; DOI not retrieved | Journal article | T1 | B | Y (bibliographic) | RQ-06 | Original not read |
| SRC-028 | Liu, N. F., Zhang, T. & Liang, P. (2023). Evaluating Verifiability in Generative Search Engines. Findings of EMNLP 2023, 7001–7025. | doi:10.18653/v1/2023.findings-emnlp.467 | Conference paper | T1 | P | Y | RQ-08 | Commercial systems as of 2023 |
| SRC-029 | Gao, T., Yen, H., Yu, J. & Chen, D. (2023). Enabling Large Language Models to Generate Text with Citations. EMNLP 2023, 6465–6488. | doi:10.18653/v1/2023.emnlp-main.398 | Conference paper | T1 | A | Y | RQ-08 | Benchmark tasks differ |
| SRC-030 | Ji, Z. et al. (2023). Survey of Hallucination in Natural Language Generation. ACM Computing Surveys. | doi:10.1145/3571730 | Survey | T1 | A | Y | RQ-08 | Scope statement only used |
| SRC-031 | Liu, N. F. et al. (2024). Lost in the Middle: How Language Models Use Long Contexts. TACL 12, 157–173. | doi:10.1162/tacl_a_00638 | Journal article | T1 | A | Y | RQ-08 | Models of 2023 |
| SRC-032 | Sun, W. et al. (2023). Is ChatGPT Good at Search? Investigating Large Language Models as Re-Ranking Agents. EMNLP 2023, 14918–14937. | doi:10.18653/v1/2023.emnlp-main.923 | Conference paper | T1 | A | Y | RQ-01 | Figures from arXiv v1 abstract |
| SRC-033 | Chen, J., Xiao, S., Zhang, P., Luo, K., Lian, D. & Liu, Z. (2024). M3-Embedding (BGE M3): Multi-Linguality, Multi-Functionality, Multi-Granularity Text Embeddings Through Self-Knowledge Distillation. arXiv preprint. | doi:10.48550/arXiv.2402.03216 | Preprint (primary source of model) | T1 | A | Y | RQ-01 (RQ-07 if activated) | Author-reported results |
| SRC-034 | Douze, M. et al. (2024). The Faiss library. arXiv preprint. | doi:10.48550/arXiv.2401.08281 | Preprint (primary source of library) | T1 | P | Y | RQ-15 preparation | Library scope only |
| SRC-035 | Malkov, Yu. A. & Yashunin, D. A. Efficient and Robust Approximate Nearest Neighbor Search Using Hierarchical Navigable Small World Graphs. IEEE TPAMI (IEEE Xplore document 8594636); arXiv:1603.09320. | doi:10.48550/arXiv.1603.09320 | Journal article | T1 | A | Y | RQ-15 preparation | Journal volume not retrieved |
| SRC-036 | Lin, J. et al. (2021). Pyserini: A Python Toolkit for Reproducible Information Retrieval Research with Sparse and Dense Representations. SIGIR 2021. | doi:10.1145/3404835.3463238 | Conference paper | T1 | A | Y | RQ-06 | Current version and licence not checked |
| SRC-037 | sentence-transformers. all-MiniLM-L6-v2 model card. Hugging Face. | https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2 | Official model documentation | T1 | A | Y | RQ-01 | Only embedding dimension and intended use verified |
| SRC-038 | Liu, T.-Y. (2009). Learning to Rank for Information Retrieval. Foundations and Trends in Information Retrieval 3(3), 225–331. | doi:10.1561/1500000016 | Monograph | T1 | A | Y | RQ-09 | — |
| SRC-039 | Settles, B. (2009). Active Learning Literature Survey. Computer Sciences Technical Report 1648, University of Wisconsin–Madison. | https://minds.wisc.edu/items/37538f44-36ae-413e-8967-e6c831e17a8e | Technical report | T1 | A | Y | RQ-09 | Not peer reviewed; widely used survey |
| SRC-040 | Wazoku Limited. "Automatically search for duplicate Ideas." Wazoku Knowledge base (no page date). | https://support.wazoku.com/automatically-search-for-duplicate-ideas | Vendor documentation | T2 | A | Y | RQ-10 | Vendor statement; matching method and fields not stated |
| SRC-041 | Wazoku Limited. "About Jen." Wazoku Knowledge base (no page date). | https://support.wazoku.com/about_jen | Vendor documentation | T2 | A | Y | RQ-10 | Vendor statement; model, data use and human-decision design not stated |
| SRC-042 | Innocentive (Wazoku). Home page: "In 2020, Wazoku acquired Innocentive." | https://www.innocentive.com/ | Vendor web page | T2 | A | Y | RQ-10, RQ-11 | Corporate history statement only |
| SRC-043 | Innocentive (Wazoku Crowd). Challenge page "Wazoku Inc: eRFP Challenge – Evaluation." | https://www.innocentive.com/challenges/wazoku-inc-erfp-challenge-evaluation/ | Vendor web page | T2 | A | Y | RQ-10 | Used only for: closed Challenges are evaluated by Seeker organizations |
| SRC-044 | ITONICS. "AI" product page (Prism). | https://itonics-innovation.com/ai | Vendor web page | T2 | A | Y | RQ-10 | Marketing page; no model or method named; performance figures excluded |
| SRC-045 | ITONICS. Innovation management demo page. | https://www.itonics-innovation.com/innovation-demo | Vendor web page | T2 | A | Y | RQ-10 | Marketing page; short statements only |
| SRC-046 | Brightidea. "Duplicate Checker on Post Submission." Brightidea Support Portal (no page date). | https://support.brightidea.com/hc/en-us/articles/205840267-Duplicate-Checker-on-Post-Submission | Vendor documentation | T2 | A | Y | RQ-10 | Method, fields and threshold not stated; scope limited to one Initiative |
| SRC-047 | Brightidea. AI features overview article, Brightidea Support Portal (no page date). | https://support.brightidea.com/hc/en-us/articles/16717011910163 | Vendor documentation | T2 | A | Y | RQ-10 | Page contains unfilled editorial placeholders; may be in revision |
| SRC-048 | Wellspring. "Scout" product page. | https://www.wellspring.com/scout | Vendor web page | T2 | A | Y | RQ-10 | Record counts are vendor-stated; AI method not described |
| SRC-049 | Wellspring. Technology evaluations page. | https://www.wellspring.com/technology-evaluations | Vendor web page | T2 | A | Y | RQ-10 | Speed figure has no method; excluded |
| SRC-050 | Wellspring. "Accolade: Idea Management Software." | https://www.wellspring.com/solutions/idea-management-software | Vendor web page | T2 | A | Y | RQ-10 | No AI or duplicate detection described |
| SRC-051 | IdeaScale. "Idea Duplicate Detection Tool." IdeaScale Support Center. | https://help.ideascale.com/idea-duplicate-detection-tool | Vendor documentation | T2 | A | Y | RQ-11 | Method, model and threshold not stated |
| SRC-052 | ServiceNow. "Predictive Intelligence for Innovation Management." Product documentation, Yokohama release, updated 2025-01-30. | https://docs.servicenow.com/bundle/sandiego-it-business-management/page/product/innovation-management/concept/predictive-intelligence-for-innovation.html | Vendor documentation | T2 | A | Y | RQ-11 | Training procedure on a linked page not read |
| SRC-053 | PQAI project. pqai repository README ("PQAI: Patent Quality Artificial Intelligence"). | https://github.com/pqaidevteam/pqai | Open-source project documentation | T2 | A | Y | RQ-11, RQ-12 | README read through a web mirror because the repository page was not reachable in this session; project self-description |
| SRC-054 | Zellner [initials not recorded] (2020). Enabling Shared Understanding of Novelty with an Open Prior-Art Search Engine. Abstract, JURIX 2020 workshop page, Carnegie Mellon University. | https://www.cmu.edu/epp/patents/events/jurix2020/abstracts/zellner-abstract.html | Workshop abstract | T3 | A | Y | RQ-11 | Used only for project origin; author name as shown in page address |
| SRC-055 | Chan, J., Chang, J. C., Hope, T., Shahaf, D. & Kittur, A. (2018). SOLVENT: A Mixed Initiative System for Finding Analogies between Research Papers. Proc. ACM Hum.-Comput. Interact. 2(CSCW), 31:1–31:21. | doi:10.1145/3274300 | Journal article | T1 | A | Y | RQ-11, RQ-12 | Research papers, not organizational submissions |
| SRC-056 | Hamilton, R. A. II, Moskowitz, P. A., Pickover, C. A. & Seaman, J. W. US 8,943,033 B2, "System and method for avoiding duplication of effort in drafting documents." Granted 2015-01-27. Google Patents record. | https://patents.google.com/patent/US8943033 | Patent record | T1 | A | Y | RQ-12 | Legal status is a database assumption; claims read as summarized on the record page |
| SRC-057 | Sager, B. M. & Kimberlin, W. L. (Reveal Networks Inc.). US 11,561,987 B1, "Platform for semantic search and dynamic reclassification." Granted 2023-01-24. Google Patents record. | https://patents.google.com/patent/US11561987 | Patent record | T1 | A | Y | RQ-12 | Claim 1 text not in the portion read; description sections used |
| SRC-058 | USPTO Official Gazette entry: US 12,461,922 B1, "Platform for semantic search and dynamic reclassification," assigned to Reveal Networks, Inc., 2025-11-04. | https://patentsgazette.uspto.gov/week44/OG/html/1540-1/US12461922-20251104.html | Patent-office record | T1 | A | Y | RQ-12 | Gazette claim only |
| SRC-059 | Canadian Patent Database record CA 2588160 (PCT/US2005/041749; WO 2006/055746), "Integrated idea management method and software with protection mechanism." | https://brevets-patents.ic.gc.ca/opic-cipo/cpd/eng/patent/2588160/summary.html | Patent-office record | T1 | A | Y | RQ-12 | Owner, inventors and status not shown on the page read |
| SRC-060 | EP 2765543 A1, "Method and system for matching technical needs to solutions." Google Patents record (search-result extract). | https://patents.google.com/patent/EP2765543A1/en | Patent record | T1 | B | Partial | RQ-12 | Record page failed to load; only title and claim-1 opening read in the extract (ISS-031) |
| SRC-061 | US 11,762,916 B1, "User interface for identifying unmet technical needs and/or technical problems." Google Patents record (search-result extract). | https://patents.google.com/patent/US11762916 | Patent record | T1 | B | Partial | RQ-12 | Record page failed to load; abstract extract only (ISS-031) |
| SRC-062 | Verma, M., Sharma, V. & Singh, V. (2025). A Hybrid AI Framework for Strategic Patent Portfolio Pruning: Integrating Learning-to-Rank and Market-Need Analysis for Technology Transfer Optimization. arXiv:2509.00958. | doi:10.48550/arXiv.2509.00958 | Preprint | T3 | P | Y | RQ-12 | Not peer reviewed; no quantitative evaluation |
| SRC-063 | Open Innovation Contests (16 Topics collected between 2015 and 2022). Dataset, Zenodo, version v1, published 2025-07-09. | https://zenodo.org/records/15854790 | Dataset record | T1 | A | Y | RQ-11 | Student-generated ideas, not organizational need or challenge submissions |
| SRC-064 | ISO/IEC 27001:2022 Information security, cybersecurity and privacy protection — Information security management systems — Requirements. Edition 3.0, published 2022-10-25, ISO/IEC JTC 1/SC 27. Publication record, IEC Webstore. | https://webstore.iec.ch/publication/79694 | Standards-body publication record | T1 | A | Y | RQ-13; CLM-041 | Abstract only; the standard's text and Annex A controls were not read. The iso.org record page returned client errors and was not used. |
| SRC-065 | ISO/IEC 20000-1:2018 Information technology — Service management — Part 1: Service management system requirements. Edition 3, 2018-09; reviewed and confirmed 2023; Amendment 1:2024. Publication record, ISO. | https://www.iso.org/standard/70636.html | Standards-body publication record | T1 | A | Y | RQ-13; CLM-042 | Abstract only; clause text not read |

## 4. Entry procedure (from S02)

1. Search; open and read the source itself, not only a search snippet.
2. Record full citation, DOI or stable URL, access date and tier.
3. Mark Verified = Y only when the specific statement used was found in the source text.
4. Record limitations relevant to this project (domain, language, data size, date, evaluation setting).
5. Link the entry to the RQ it informs and any CLM it supports.
