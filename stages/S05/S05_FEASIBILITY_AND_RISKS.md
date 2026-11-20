# S05_FEASIBILITY_AND_RISKS

| Field | Value |
|---|---|
| Document ID | S05_FEASIBILITY_AND_RISKS |
| Version | 1.0 |
| Status | APPROVED |
| Stage | S05 |
| Date | 2026-11-20 |
| Depends on | S04_ARCHITECTURE §3, §5; S04_ASSUMPTIONS_AND_STANDARDS §1; S05_EVALUATION_DESIGN; S05_DATA_AVAILABILITY_AND_SUBSTITUTES; RQ-14; RQ-15; CLM-036; CLM-051 to CLM-056; ISS-006; ISS-009; ISS-023; ISS-033; ISS-040; ISS-041 |

- **Purpose:** check that the essential set of narrowed Option B can be built and evaluated with verifiable, self-hostable components and accessible external sources; define early feasibility tests; list technical and data risks for Section 17.
- **Labels:** licence and limit statements are VERIFIED at documentation-page depth (A) and cite their source. Throughput, latency and hardware needs are not known and are not estimated: FT-02 measures them. Memory figures in §1.2 are arithmetic from stated dimensions (PROPOSED planning calculation, CLM-056).
- **IDs defined here:** FT (feasibility test), RSK (risk).

## 1. Models and tools (RQ-15)

### 1.1 Candidates for AC-04 and AC-05

All candidates can run on project-controlled hardware without sending submission text to a hosted service, which keeps AS-04 and AD-09 intact. Hosted embedding or re-ranking services are not evaluated while ISS-009 is open.

| Component | Candidate | Licence (stated on model or package page) | Stated input limit | Output | Languages | Source |
|---|---|---|---|---|---|---|
| Lexical index and baselines | Pyserini (Lucene-based) | Apache 2.0 per project licence badge (secondary listing; to be confirmed on the repository licence file in S07) | — | BM25 runs, evaluation scripts, prebuilt benchmark indexes | Analyzer-dependent | SRC-036, SRC-078 |
| Dense encoder D-1 | all-MiniLM-L6-v2 | Apache 2.0 | Text beyond 256 word pieces truncated | 384-dimensional vector | Intended as an English sentence and short-paragraph encoder | SRC-037 |
| Dense encoder D-2 | multilingual-e5-base | MIT | Text truncated at 512 tokens; inputs must start with "query: " or "passage: " | 768-dimensional vector; 12 layers | 100 languages inherited from XLM-RoBERTa | SRC-075 |
| Dense encoder D-3 | BGE-M3 | MIT | Up to 8,192 tokens | 1024-dimensional dense vector; also sparse and multi-vector outputs; weight file 2.27 GB | More than 100 languages | SRC-033, SRC-076 |
| Re-ranker RR | bge-reranker-v2-m3 | Apache 2.0 | Not read in S05 | Relevance score per query-passage pair; weight file 2.27 GB | Multilingual | SRC-077 |
| Vector search | Faiss with HNSW indexes | Library licence not re-read in S05 | — | Approximate nearest-neighbour search; a library, not a database (persistence and access control come from AC-03) | — | SRC-034, SRC-035 |

Practical requirement found: Pyserini needs a Java 21 runtime alongside Python because of its Lucene dependency (SRC-078). The reference environment (AS-11) must provide it.

Licence pages cover model weights and code. The terms of the data used to train each model were not assessed; S07 records them before a model is fixed (ISS-041, QA-010).

### 1.2 Memory for dense indexes at the PV-10 corpus sizes

A float32 vector index holds N × d × 4 bytes before index overhead. With passage segmentation, N is the number of passages, not records, so these figures are lower bounds per vector field.

| Vectors N | d = 384 (D-1) | d = 768 (D-2) | d = 1024 (D-3) |
|---|---|---|---|
| 10,000 | 15.36 MB | 30.72 MB | 40.96 MB |
| 100,000 | 153.6 MB | 307.2 MB | 409.6 MB |
| 1,000,000 | 1.536 GB | 3.072 GB | 4.096 GB |

At the two smaller sizes every candidate fits in the memory of an ordinary server. At one million vectors with D-3, memory becomes a design constraint (index compression or the smaller encoder). Encoding time for the corpus and query latency depend on hardware and are measured in FT-02, not estimated here.

## 2. External sources for R4 (RQ-14)

| Service | Coverage relevant to R4 | Access | Stated limits and terms | Source |
|---|---|---|---|---|
| EPO Open Patent Services (OPS) | Programmatic access to most of the EPO's data sets | Registration required | Free up to 4 GB of data per week; above that an annual subscription (EUR 2,800 on the current price page). Fair-use policy: as a rule all OPS services tolerate ten searches per minute per IP address, a threshold that may vary with operational circumstances, and OPS is not designed for downloading entire collections. Terms allow users to include the data in their own products | SRC-070, SRC-071, SRC-072, SRC-073 |
| USPTO PatentsView PatentSearch API | US patent data | API key requested through the PatentsView help centre; one key per user | 45 requests per minute per key. A third-party report states that the key-request link was removed in early 2026 (T3; not confirmed) | SRC-074, SRC-080 |
| Lens API | Patent and scholarly records | Access granted on request; token created in the user profile | Use subject to the Lens Terms of Use; quotas returned in response headers; numeric quotas and pricing not stated on the page read | SRC-081 |
| PQAI | Open-source prior-art search from plain-language descriptions, with an API | MIT-licensed code (CLM-036) | API terms not verified (open since S03) | SRC-053 |

**Answer to RQ-14:** three services have documented access routes and stated limits (EPO OPS, PatentsView, Lens), which meets the RQ-14 criterion of at least two options with terms verified. Which one the prototype uses is an owner choice once ISS-006 and ISS-033 are answered (ISS-040). The connector interface (IF-03, AD-04) does not depend on the choice.

**Volume check.** ET-09 at PV-08 issues 30 statements × 3 formulations = 90 searches per track and stores up to 900 results per track. At ten searches per minute this is about nine minutes of query time per track, well inside every stated limit. Volume is not a feasibility constraint for the evaluation; access approval and terms are.

## 3. Feasibility tests (early in the funded project)

Each test retires a specific risk before the work that depends on it.

| ID | Test | Pass condition | Retires |
|---|---|---|---|
| FT-01 | Reproduce a published BM25 run on DS-02 through the harness | Same metric value as the published reference run within rounding | Harness errors (RSK-09) |
| FT-02 | Encode a corpus at each confirmed PV-10 size with D-1 to D-3 on the reference environment; time query encoding, search and re-ranking | Measured times recorded; the configuration set for ET-10 is limited to those that can meet PV-09 | Hardware and latency (RSK-11) |
| FT-03 | Connector smoke test against each candidate patent service with public test queries | Authenticated query, parsed results, provenance stored, rate-limit handling observed | External access (RSK-06) |
| FT-04 | Parse the sponsor export, if one is released, against the field map | Import report produced; rejected rows explained | Export format (RSK-01) |
| FT-05 | Pilot judging on development queries | Agreement and time per judgment measured; guide revised | Judging validity and effort (RSK-03, RSK-04) |

## 4. Technical and data risks (input to Section 17)

Likelihood and impact are qualitative judgements at S05, to be revised in S08 and S10 against the actual plan (FX-11).

| ID | Risk | Likelihood | Impact | Mitigation in the design | Trigger and fallback |
|---|---|---|---|---|---|
| RSK-01 | No sponsor export is released (ISS-002) | Unknown | All retrieval targets tested on substitute data only | Track P planned from the start (AS-09); proposal wording fixed by outcome O-4 | No answer by the start of E-2: proceed on Track P |
| RSK-02 | No solution-example source is confirmed for R2 (ISS-003) | Unknown | R2 untested on sponsor sources | FN-05 built against the evidence-source interface; DS-05 constructed substitute | Section 8 states MS-02 was tested on substitute data |
| RSK-03 | Assessor time is unavailable or short (ISS-012) | Medium | Fewer judged queries; wider intervals | Project judges with the same guide (AS-10); effort sized from FT-05 | Report underpowered comparisons as such (§6 of the evaluation design) |
| RSK-04 | Judges disagree beyond PV-05 | Medium | Comparisons not interpretable | Pilot, one guide revision, scale collapse rule | Report agreement; restrict claims to the collapsed scale |
| RSK-05 | Submissions are not in English (ISS-007) | Unknown | D-1 unusable; substitute data mismatched in language | D-2 and D-3 are multilingual; RQ-07 activation (AS-06) | Track P results reported as language-mismatched if no same-language substitute exists |
| RSK-06 | Patent-service access is refused, changed or withdrawn | Medium (PatentsView key issuance uncertain) | R4 automated retrieval unavailable | Three services identified; connector interface; cached results | AS-08: assessor-run searches with manual entry; MS-03 marked untested |
| RSK-07 | External disclosure of submission text is not authorized (ISS-033) | Unknown | No Track S R4 test | ET-09 runs on public need statements; CP-1 keeps approval of any query | R4 tested on Track P only |
| RSK-08 | Test sets too small to detect a difference | Medium | Inconclusive results | Sample-size check after the pilot; pre-declared comparisons only | Report "no supported difference", not an improvement |
| RSK-09 | Tuning leaks into the test split | Low with controls | Overstated results | Frozen protocol; time-based split; single test run; FT-01 | Logged deviation; re-run on a fresh time segment if available |
| RSK-10 | Long submissions exceed model input limits (256 or 512 tokens) | Medium | Text silently truncated | Passage segmentation (FN-02); D-3 for long inputs | Report truncation counts per corpus |
| RSK-11 | Reference hardware cannot meet PV-09 with the stronger configurations | Unknown until FT-02 | Slower or weaker configuration selected | FT-02 before selection; compact encoder; index compression | Owner revises PV-09 or hardware (S10) |
| RSK-12 | A substitute dataset's terms prohibit the intended use (ISS-038) | Unknown | Candidate unusable | Licence check before use; several candidates | Drop the candidate; choose another or construct (DS-05) |
| RSK-13 | Pooling misses relevant items found only by an unpooled method | Low to medium | Biased comparison | All configurations pooled, including B-REC; judged@10 and bpref reported | Additional judging round for low-coverage runs |
| RSK-14 | Optional functions re-enter the funded plan without a decision | Low | Effort grows without a requirement behind it | Scope fixed by DEC-028; MS-07 and MS-09 conditional | Owner decision required to add them |
