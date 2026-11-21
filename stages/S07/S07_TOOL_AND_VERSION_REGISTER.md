# S07_TOOL_AND_VERSION_REGISTER

| Field | Value |
|---|---|
| Document ID | S07_TOOL_AND_VERSION_REGISTER |
| Version | 2.0 |
| Status | DRAFT |
| Stage | S10 |
| Date | 2026-11-21 |
| Depends on | S05_FEASIBILITY_AND_RISKS §1; S04_ARCHITECTURE §3, §5; QA-010; ISS-040; ISS-041; SRC-033 to SRC-037; SRC-075 to SRC-078; SRC-086; CLM-054; CLM-055; CLM-058; CLM-063 |

- **S10 alignment (DEF-002, DEC-039):** wording aligned with the S09-corrected master (CP-1 always applied with disclosure clearance and query approval, DEC-035; EPO OPS thresholds as fair-use guidance, DEC-038; retention default, DEF-034). Content otherwise unchanged.
- **Purpose:** every tool, library, model and external service named in Section 12, with what has been verified about it and what is only proposed (REF-02 §12 rule; QA-010; S07 gate criterion).
- **Status key:** VERIFIED (SRC-###) = the stated property was found in the cited source at the depth recorded in `02_SOURCE_LOG`. PROPOSED = a team choice not checked against a source in this project; its licence and version are recorded in the D7.3 inventory before use. "Version" means the version to be pinned; no version is pinned before T1.5 (reference environment) and T3.3 (index layer).
- **Rule for pinning:** at T1.5 each component is pinned to an exact version, its licence file is read on the version pinned, and the result is entered in D1.1 §environment and later D7.3. A component whose licence or terms fail that check is replaced by the listed alternative or dropped, and the change is logged.

## 1. Retrieval and indexing (WP3)

| Component | Role in the prototype | Version status | Licence status | Other verified properties | Open items |
|---|---|---|---|---|---|
| Pyserini | B-LEX (BM25), passage-level lexical index, standard metric computation in the harness | 2.4.0 is the latest release on the package index, released 2026-08-27 (VERIFIED, SRC-078, re-read 2026-11-21); version to pin: PROPOSED at T1.5 | Apache-2.0 in the package metadata "License expression" field (VERIFIED, SRC-078); the repository licence file could not be retrieved in S07 | Requires Python ≥ 3.12 and a Java 21 runtime because of its Anserini dependency (VERIFIED, SRC-078) | Read the licence file of the pinned version at T1.5 |
| Faiss | Vector search for D-1 to D-3; exact search for evaluation runs, HNSW where FT-02 shows it is needed | Not checked; PROPOSED at T1.5 | MIT, licence file in the project repository (VERIFIED, SRC-086) | Library, not a database: persistence and access control come from AC-03 (SRC-034) | Whether filtered search by date is supported in the pinned version (otherwise over-fetch and filter, Section 12 activity 3) |
| all-MiniLM-L6-v2 (D-1) | English dense encoder, low resource | Model revision pinned at T1.5 (PROPOSED) | Apache 2.0 (VERIFIED, SRC-037) | 384 dimensions; input beyond 256 word pieces truncated (VERIFIED, SRC-037, CLM-054). The model card lists 33 training datasets totalling about 1.17 billion training tuples and states no terms for them (VERIFIED, SRC-037, CLM-063) | Training-data terms not assessed (ISS-041) |
| multilingual-e5-base (D-2) | Multilingual dense encoder | Pinned at T1.5 (PROPOSED) | MIT (VERIFIED, SRC-075) | 768 dimensions; 512-token truncation; inputs prefixed "query: " or "passage: " (VERIFIED, SRC-075) | Training-data terms not read (ISS-041) |
| BGE-M3 (D-3) | Long-input multilingual dense encoder | Pinned at T1.5 (PROPOSED) | MIT (VERIFIED, SRC-076) | 1,024 dimensions; inputs up to 8,192 tokens (VERIFIED, SRC-076). The model card names the MLDR training split and a linked fine-tuning data set but no terms for training data (VERIFIED, SRC-076, CLM-063) | Training-data terms not assessed (ISS-041) |
| bge-reranker-v2-m3 (RR) | Optional cross-encoder re-ranking of the top 50 | Pinned at T1.5 (PROPOSED) | Apache 2.0 (VERIFIED, SRC-077) | Input limit not read (SRC-077) | Input limit and training-data terms (ISS-041) |
| Encoder runtime library (candidate: sentence-transformers) | Loading D-1 to D-3 and RR, batching, normalization | PROPOSED | Not checked (PROPOSED) | — | Licence and version at T1.5 |

## 2. Services, storage and interface (WP4, WP5)

| Component | Role | Status | Notes |
|---|---|---|---|
| Python 3.12 runtime | Services AC-01 to AC-05, AC-07, AC-09, AC-11 to AC-14 | PROPOSED; set by the Pyserini requirement (VERIFIED, SRC-078) | One language for services and harness keeps the evaluation path identical to the product path |
| Java 21 runtime | Required by Pyserini | VERIFIED as a requirement (SRC-078) | Version pinned at T1.5 |
| Relational database (candidate: PostgreSQL) | AC-03 content store, AC-09 records, AC-13 audit log | PROPOSED; licence not checked | Chosen for transactions, row-level permissions and triggers that make the audit table insert-only for the application role |
| HTTP service framework (candidate: FastAPI) | IF-02, IF-04, IF-05, IF-06 endpoints | PROPOSED; licence not checked | Interfaces are specified in D1.1 independent of the framework |
| Server-rendered web interface | AC-10 review screens | PROPOSED | No client-side model inference |
| Password hashing (candidate: Argon2id through a maintained library) | AC-12 project-managed accounts (AS-05) | PROPOSED; library not checked | Sponsor identity federation is future work (IF-08) |
| JSON Schema validation | IF-05 and IF-06 export validation; IF-01 import validation | PROPOSED | Schemas are part of D1.1 |

## 3. External sources for R4 (WP4)

| Service | Status in S07 | Basis |
|---|---|---|
| EPO Open Patent Services | Recommended first connector, subject to owner decision ISS-040 | Registration route, free tier to 4 GB per week, fair-use guidance (charter: approximately 1 Mbit per second for OPS; OPS FAQ: ten searches per minute per IP address as a rule, varying with operational circumstances; neither guaranteed, DEC-038) and terms allowing inclusion in own products are documented (VERIFIED, CLM-051); the full terms were read only in part (SRC-073) |
| USPTO PatentsView PatentSearch API | Alternative | 45 requests per minute per key (VERIFIED, SRC-074); key issuance uncertain (T3 report, SRC-080, CLM-052 OPEN) |
| Lens API | Alternative | Access on request, quotas in response headers (VERIFIED, CLM-053); terms and plan not read |
| PQAI | Not recommended for the funded connector | MIT-licensed code (CLM-036); API terms not verified |

The connector framework (IF-03, AD-04) does not depend on the choice. Owner decision ISS-040 is needed before T4.2.

## 4. Evaluation and test tooling (WP2, WP5, WP6)

| Tool | Role | Status |
|---|---|---|
| Harness AC-14 (project code) | Run files, metric computation, paired bootstrap, sign-flip randomization tests, Holm adjustment, Clopper–Pearson intervals, per-track reports | PROPOSED; metric code unit-tested on hand-computed examples (D2.3); methods sourced (SRC-025, SRC-066, SRC-068, SRC-087, SRC-089, SRC-090) |
| Judging screen (part of AC-14) | Blind, randomized-order grading with time per judgment (FT-05) | PROPOSED |
| Numerical libraries (candidates: NumPy, SciPy) | Resampling and exact binomial intervals | PROPOSED; licences not checked |
| Property-based test generator (candidate: Hypothesis) | Randomized event sequences for ET-06 | PROPOSED; licence not checked |
| Browser automation (candidate: Playwright) | Scripted interface tests for D5.2 | PROPOSED; licence not checked |
| Container-based deployment scripts | D6.1 clean-environment build; D7.1 rehearsal | PROPOSED; tooling chosen at T1.5 |

## 5. Not used

No hosted embedding, re-ranking or generative service is used while ISS-009 is open (AD-09). No summary generator is built (FN-07 outside the funded scope, DEC-028). No model is fine-tuned or retrained (AD-10).
