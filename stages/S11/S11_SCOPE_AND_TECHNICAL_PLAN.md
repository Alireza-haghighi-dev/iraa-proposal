# S11_SCOPE_AND_TECHNICAL_PLAN

| Field | Value |
|---|---|
| Document ID | S11_SCOPE_AND_TECHNICAL_PLAN |
| Version | 0.1 |
| Status | SUBMITTED FOR GATE |
| Stage | S11 |
| Date | 2026-11-21 |
| Depends on | DEC-028; DEC-035; DEC-040; DEC-041; S04_ARCHITECTURE; S05_EVALUATION_DESIGN; S06_WORK_PACKAGES; S07_CORRECTED_EVALUATION_METHODOLOGY; IRAA_PROPOSAL_EN_MASTER v0.3 |

- **Purpose:** scope-revision and simplification analysis (§1), revised technical implementation plan (§2), and the limits on simplification set by the sponsor, the form and the reviewer (§3). The canonical text is the master v0.4; this file records why each change was made.
- **Basis:** engineering judgment applied to the approved S04–S10 design; no new literature search. Every cut keeps R1–R4, the approval and disclosure controls, the data-protection baseline and a reproducible evaluation.
- **Status:** provisional until the owner checkpoint (DEC-041 item 8). Historical stage records S04–S07 are kept unchanged; where they differ from this file, this file and the master govern.

## 1. Simplification analysis

| Area | S04–S10 design | Problem for a six-month, four-member project | S11 decision | Requirement effect |
|---|---|---|---|---|
| Retrieval configurations | Nine: date-ordered list, BM25, fingerprint, three dense encoders, two fusion methods, optional re-ranker; configuration chosen on development data | Each configuration adds indexing, timing, pooled judging and analysis; selection adds a tuning step and a selection record | Three ranked configurations: BM25, one dense encoder, reciprocal rank fusion of the two, fixed in advance as the primary configuration. Fingerprints kept as a duplicate flag, not as a ranked configuration | R1, R2 kept; the question answered becomes "does adding semantic retrieval to BM25 help?" |
| Embedding models | all-MiniLM-L6-v2, multilingual-e5-base, BGE-M3 | Three encoders with overlapping purposes; English-only encoder useless if submissions are not English (ISS-007 open) | multilingual-e5-base only (licence and 512-token input verified, S07). BGE-M3 kept as a documented alternative for long texts (risk 7), not built | Language risk covered by the multilingual choice |
| Re-ranker and second fusion method | bge-reranker-v2-m3; convex score combination | Optional sophistication; extra latency and judging | Removed | None on R1–R4 |
| Parameter tuning | BM25 and fusion weights tuned on development data | Tuning effort and a leakage risk to control | BM25 toolkit defaults; RRF constant from Cormack et al. (2009); only display thresholds set on development data | Fewer moving parts; simpler integrity argument |
| Statistical design | Non-inferiority test per comparison with margin-shifted randomization tests, Holm family-wise adjustment, superiority second, sample-size target of 80% probability, one-sided/two-sided level question (ISS-055), specification 3 sizing decision (ISS-049) | Over-elaborate for small judged sets; the planned sizes could not reach the stated power, so the machinery would mostly produce "not established" | One primary comparison per requirement; two-sided 95% paired bootstrap interval read against the margin and against zero (not worse / better / worse / inconclusive); randomization p-value reported beside it; prior-art comparison reported as an estimate only. Removes Holm, margin-shifted tests and the level mismatch | Claims limited to what the interval supports; inconclusive results reported as such |
| Test sets and judging | 60 + 20 queries for R1; 60 + 20 need statements for R2; 30 separate statements for R4 with three formulations; pool depth 10 over nine configurations; deeper check on 10 queries to depth 50 or exhaustive below 200 items | Judging and construction dominated WP2 and WP6 (planning 140 h judging plus 60 h construction) | 50 + 10 queries for R1; 50 need statements written once, 40 + 10 for R2 and 30 of them reused for R4; two formulations for R4; pool depth 10 over three configurations; deeper check on 5 queries to rank 30; 20% double judging kept | Smaller sample, wider intervals, honestly reported |
| Corpus sizes and scale | 10,000 / 100,000 / 1,000,000 items; approximate search planned above exact-search limits | Industrial-scale assumption for a laboratory prototype | 10,000 and 100,000 items, exact search; larger collections stated as outside the tested range | Specification 7 tested at two sizes |
| Interface | Full review screens for three result types, query approval, template form | Largest single build task (140 h) | Lightweight server-rendered screens with the same rules: evidence passage before score, assessor-only actions, query-approval screen | R3 controls unchanged |
| Accounts and identity | Separate identity interface and account component | Re-implements what web frameworks provide | Framework's built-in authentication with the project's role checks | None |
| Approval tests | Generated exhaustive suite plus randomized property-based sequences | Randomized generator is extra tooling | Generated exhaustive suite over every state, event and role, with expired and replayed requests and re-approval; randomized sequences removed | Specification 4 tested exhaustively over the table |
| Second-approver setting | Configurable setting, off by default | Unrequested feature (approval model open, ISS-034) | Added as table rows only if the sponsor requires it | None |
| Documentation and validation | Separate design review, release checklist, acceptance, as-built update, continuity notes, each with review effort | Review counted inside several tasks and again in coordination | One review line per work package and one coordination line for the project (EH-10 check in S11_EFFORT_AND_SCHEDULE §3) | None |
| Deployment | Rehearsal by a person not involved in the build (ISS-051 open) | No such person was identified | A team member who did not write the deployment scripts performs the rehearsal on a clean instance | Activity 7 acceptance kept |
| Error analysis and correction | Implicit in the report | Owner's month 5 focus asks for it explicitly | Explicit error analysis and corrective development in WP6; corrected code not re-scored on the test split | Strengthens the evaluation's integrity |

Kept without reduction: disclosure clearance and assessor query approval with bypass tests at the service and network levels; insert-only audit log with hash chain; outcome-field database trigger; versioning and re-approval; information security risk assessment and retention procedure; licence gate for substitute data; frozen protocol, time-ordered split and single test run; blind judging with double judging and adjudication; source and evidence attribution; reproduction of a published BM25 run; final reproducibility check.

## 2. Revised technical implementation plan

| WP | Main components and methods | Reused components (licence status) | Built by the project |
|---|---|---|---|
| WP1 | Field map, transition table with two approval properties, interface specifications, risk assessment, retention procedure, reference environment; first-month end-to-end prototype | Pyserini (Apache-2.0, verified), Faiss (MIT, verified), multilingual-e5-base (licence verified), relational database and web framework (licences recorded before use) | Specifications; environment scripts; prototype slice |
| WP2 | Licence check; protocol and judging guide; time-ordered collections; one need-statement set; harness | Toolkit evaluation functions; established statistical libraries where they provide the procedure | success@10, judged@10, interval and test wrappers, manifests, judging screen |
| WP3 | Import and validation; normalization; hashes and shingle fingerprints; passage splitting; lexical and exact vector indexes; three configurations; thresholds; timing at two sizes | Pyserini BM25; Faiss exact search; pretrained encoder without fine-tuning | Import adapter, source registry, retrieval service with date filter and evidence passages |
| WP4 | Connector contract, cache with provenance, rate limiter; one patent-service connector; TF-IDF query construction; disclosure clearance and query approval; manual-entry fallback; bypass tests | Patent service API (EPO OPS recommended; owner decision) | Connector, query flow, enforcement and tests |
| WP5 | Record service with transition table, versioning and database trigger; roles; audit log with hash chain; lightweight screens; exports; generated approval suite | Web framework authentication; database roles and triggers | Record service, screens, exports, test generator |
| WP6 | Integration release and deployment scripts; pilot; test judging; single test run; workflow tests; interval analysis; error analysis and correction; report | Harness from WP2 | Release, judgments, analysis, report |
| WP7 | As-built specification and instructions; risk assessment update and deletion; inventory; rehearsal; defect resolution and reproducibility check; demonstration and acceptance | Automated dependency and licence listing | Documentation, package, acceptance record |

The architecture of S04 is unchanged in structure (import, normalization, indexes, retrieval service, connector, record service, audit log, review interface, exports, harness); only the number of configurations, the scale and the interface depth are reduced.

## 3. Limits on simplification

| Source | Requirement that limits cuts | Consequence |
|---|---|---|
| Sponsor statement (R1–R4) | New-versus-stored comparison; solution-example identification without an assumed database; final human approval; external patent and solution evidence | No requirement is dropped; R2 needs the constructed substitute set unless a sponsor source is confirmed |
| DEC-028, DEC-035 | Approval and re-approval controls; no confidential text sent without disclosure authorization and query approval | Enforcement and bypass tests are not reduced |
| Sponsor constraints (information security, extensibility) | Risk assessment, access control, audit log; defined interfaces | Kept; the platform adapter stays specified only |
| Form (REF-02 §§8, 12, 13) | Measurable specifications in a table; Section 12 repeats the Section 13 activities with concrete methods; every activity has a tangible output and an effort figure | Specifications 1–8 kept with revised test conditions; seven activities unchanged |
| Reviewer criteria RF-003, RF-006, RF-007, RF-010 | Official tables unchanged; Section 12 = Section 13; six or seven activities; schedule derived from effort and capacity | WP identifiers and titles unchanged; Gantt months entered only after the checkpoint |
| Scientific integrity (QA-002, QA-004) | Benefits stated as hypotheses; testable criteria with data conditions | Interval rule and "inconclusive" outcome added; no claim beyond the sample |
