# S07_WP_METHOD_TRACEABILITY

| Field | Value |
|---|---|
| Document ID | S07_WP_METHOD_TRACEABILITY |
| Version | 1.0 |
| Status | SUBMITTED FOR GATE |
| Stage | S07 |
| Date | 2026-11-21 |
| Depends on | DRAFT_SEC12_METHODOLOGY; S06_WORK_PACKAGES; S06_DELIVERABLES_AND_ACCEPTANCE; S05_EVALUATION_DESIGN; S05_FEASIBILITY_AND_RISKS; S07_CORRECTED_EVALUATION_METHODOLOGY; S07_TOOL_AND_VERSION_REGISTER; DRAFT_SEC07_OBJECTIVES; DRAFT_SEC08_FEATURES; DRAFT_SEC13_ACTIVITIES; DEC-033 |

- **Purpose:** shows, for each work package, where Section 12 covers the seven elements the S07 instruction requires (DEC-034), maps every Section 8 row to a verification step (S07 gate criterion; QA-004, QA-010), lists the task refinements made in S07, and records the cross-section consistency checks.
- **Rule:** WP identifiers, titles and order are those frozen at the S06 gate (DEC-033). Tasks are refined without renumbering. No personnel, hours, costs or months appear here (S10).
- **Labels:** all methods are PROPOSED; tool status is in `S07_TOOL_AND_VERSION_REGISTER`.

## 1. Seven required elements per work package

Element key: (1) technical objectives and procedures; (2) inputs, prerequisite data and dependencies; (3) algorithms, technologies and component choices, with status; (4) validation and evaluation; (5) deliverables and acceptance evidence; (6) constraints, technical risks and fallbacks; (7) traceability.

### WP1 — Prototype design specification and data-protection baseline

| Element | Content (Section 12, activity 1) |
|---|---|
| 1 | Fix field map, import format, configurable template, transition-table state model with default rejection, interface schemas, risk assessment per data flow, role matrix, retention procedure, reference environment and pinned versions |
| 2 | Sponsor export schema if released, otherwise substitute schema (ISS-008, AS-03); assessment content (ISS-005); approval model (ISS-034); accounts (ISS-035); retention (ISS-036); S04 architecture and data flows. Dependencies: none upstream; gates M1 for T3.4, T4.3, T5.1 |
| 3 | Transition table as executable specification with two independent R3 properties (PROPOSED); threat checklist per data flow and trust boundary (disclosure, unauthorized change, unauthorized state transition, availability, unattributable action) (PROPOSED); component pinning with licence file read on the pinned version |
| 4 | Design review against a checklist (T1.6): every FN to an AC, an IF and a test; table covers every state, event and role used by ET-06 |
| 5 | D1.1, D1.2, D1.3; milestone M1 |
| 6 | Sponsor inputs missing (RSK-01) → substitute schema and labelled defaults; scope creep (RSK-14) → function set fixed in D1.1; IF-07 specified only (C1, AD-03) |
| 7 | R1–R4, C1, C2; AC-01 to AC-14 (specification); IF-01 to IF-08; CP-1, CP-5, CP-6; ET-06 model input; Section 8 features 1, 7, 8, 9; MS-04 model |

### WP2 — Evaluation protocol, test collections and evaluation harness

| Element | Content (Section 12, activity 2) |
|---|---|
| 1 | Licence gate for substitutes; protocol and judging guide frozen before test pools are judged; time-ordered collections per track; conditional R2 substitute DS-05; harness with metrics and statistics; FT-01 reproduction |
| 2 | Substitute candidates DS-01 to DS-05 and their original distributions (ISS-038, ISS-044); planning values (ISS-039, ISS-049, ISS-050); owner decision on DS-05 (ISS-038); Track S data only if ISS-002 and ISS-003 allow. Gates M2 for pilot judging |
| 3 | Metrics nDCG@10 (SRC-025), P@5, success@10, Recall@20, MRR, bpref and judged@10 (SRC-068); paired bootstrap and sign-flip randomization (SRC-066), margin-shifted for non-inferiority (SRC-087); Holm (SRC-089); Clopper–Pearson (SRC-090); Pyserini evaluation functions (VERIFIED licence, SRC-078) plus project code; blind judging screen (PROPOSED) |
| 4 | Metric unit tests on hand-computed examples; FT-01 / ET-02 reproduction within rounding; manifest script rejects mixed-track collections |
| 5 | D2.1 (frozen, with ISS-042 to ISS-045 corrections), D2.2 (with licence record), D2.3 (with reproduction note); M2 |
| 6 | CQADupStack licence not established (ISS-044, CLM-059) → T2.1 gate with four conditions, alternative candidate and alternative reproduction benchmark; leakage (RSK-09) → freeze, time split, single run; pooling bias (RSK-13); licence failure (RSK-12); small sets (RSK-08) → sample-size checks |
| 7 | R1, R2, R4 (evaluation); FN-12; AC-14; ET-01 to ET-04, ET-09, ET-11, ET-12 (protocol), ET-02; FT-01; MS-01, MS-02, MS-03 (protocol) |

### WP3 — Ingestion and retrieval for similar submissions and solution examples

| Element | Content (Section 12, activity 3) |
|---|---|
| 1 | Import with report; source registry; normalization with hashes, shingle fingerprints, language tag, encoder-sized passages and truncation counts; per-corpus lexical and vector indexes; nine configurations behind IF-02; max-passage scoring and evidence span; date filter; thresholds on development split; FT-02 timing |
| 2 | D1.1 field map and environment (M1); registered sources (ISS-003); language (ISS-007); confirmed corpus sizes (ISS-023, PV-10); sponsor export for FT-04 (ISS-002) |
| 3 | BM25 tuned on development split (SRC-001; PROPOSED); D-1 to D-3 without fine-tuning, L2-normalized (licences VERIFIED, SRC-037, SRC-075, SRC-076); RRF (SRC-007) and convex combination (SRC-008); optional RR top 50 (SRC-006, SRC-077); exact Faiss search for evaluation, HNSW only where needed (SRC-034, SRC-035; licence VERIFIED SRC-086); filtered search or over-fetch (PROPOSED, depends on pinned version) |
| 4 | Unit and integration tests (T3.7); run file per configuration on development split; FT-02 measurements; overlap of approximate with exact top results where HNSW is used |
| 5 | D3.1, D3.2, D3.3 |
| 6 | Non-English text (RSK-05) → multilingual encoders; truncation (RSK-10) → passages, counts; hardware (RSK-11) → FT-02 before selection, compact encoder, compression; memory at 1,000,000 × 1,024 dimensions about 4.1 GB before overhead (CLM-056); dense methods may bring no benefit → default-configuration rule (WP6) |
| 7 | R1, R2; FN-01, FN-02, FN-03, FN-05; AC-01 to AC-05; IF-01, IF-02; ET-01, ET-01b, ET-03, ET-04, ET-05, ET-10, ET-12 (system under test); FT-02, FT-04; features 1, 2, 4; MS-01, MS-02, MS-08, MS-10 |

### WP4 — External prior-art retrieval with query approval

| Element | Content (Section 12, activity 4) |
|---|---|
| 1 | Connector plug-in contract, rate limiter, retries, cache with provenance; one patent connector; TF-IDF query construction; CP-1 approval of exact text; two-level enforcement; payload hash logging; manual-entry fallback; contract and bypass tests |
| 2 | D1.1 state model and interfaces (M1); service choice (ISS-040); disclosure authorization (ISS-033); service credentials obtained by the project (none assumed) |
| 3 | EPO OPS recommended, ten searches per minute fair-use guide value (VERIFIED, CLM-051); alternatives PatentsView (CLM-052) and Lens (CLM-053); TF-IDF term selection (PROPOSED); network egress allowlist (PROPOSED); request-payload hash comparison (PROPOSED) |
| 4 | FT-03 smoke test; contract tests; CP-1 bypass attempts through the interface, the service layer and direct network calls; provenance completeness (instrumentation for ET-08); ET-09 three-formulation comparison with separate judges for Q-A and Q-C |
| 5 | D4.1, D4.2 |
| 6 | Access refused or withdrawn (RSK-06) → AS-08 manual entry, MS-03 marked untested against a connected service; disclosure never authorized (RSK-07) → Track P only for R4; MS-03 sample size (ISS-049) |
| 7 | R4; FN-06; AC-07, AC-03; IF-03; CP-1; ET-08, ET-09 (system under test); FT-03; feature 5; MS-03, MS-05, MS-10 |

### WP5 — Assessment record, review interface and approval controls

| Element | Content (Section 12, activity 5) |
|---|---|
| 1 | Record service as sole state changer, loading the transition table; outcome field written only in the approval transaction; database trigger; version binding; project accounts and sessions; insert-only hash-chained audit log; evidence-first screens; exports validated against schemas; generated approval test suite |
| 2 | D1.1 transition table, schemas and template (M1); D1.2 role matrix; approval model (ISS-034); accounts (ISS-035) |
| 3 | Relational database with triggers and role permissions (PROPOSED); salted password hashing (PROPOSED); hash chain over audit entries (PROPOSED); property-based generation of event sequences (PROPOSED); scripted browser tests (PROPOSED) |
| 4 | ET-06 over every (state, event, role) combination, both through IF-04 and against the service layer, plus expired sessions, replays and randomized sequences; oracle = the two R3 properties checked on the database, not the table; ET-07 field-by-field re-approval and hash-chain recomputation; coverage report |
| 5 | D5.1, D5.2, D5.3 |
| 6 | Common-mode error between table and tests → independent oracle and T1.6 review; optional controls CP-2 to CP-4 not built (DEC-028, RSK-14); sponsor identity federation future (IF-08) |
| 7 | R3 (display for R1, R2, R4); FN-08, FN-09, FN-10, FN-11; AC-09 to AC-13; IF-04, IF-05, IF-06, IF-08; CP-5, CP-6; CP-1 screen; ET-06, ET-07; features 7, 8; MS-04, MS-06, MS-10 |

### WP6 — Prototype integration and evaluation

| Element | Content (Section 12, activity 6) |
|---|---|
| 1 | Release from tagged sources on a clean environment; pilot with agreement, time per judgment, guide revision, scale-collapse rule; sample-size checks for MS-01 to MS-03; floors fixed before the test run; selection on development split; blind test-pool judging with double judging; ET-12 deeper check; single test run; workflow and timing tests; report by track with outcome labels; default-configuration rule; sensitivity repetition; conditional walk-through |
| 2 | D2.1 to D2.3 (M2); D3.2, D4.1, D5.1 to D5.3; judges (ISS-012, AS-10); owner choice for MS-03 after pilot (ISS-049); ET-12 parameters (ISS-050) |
| 3 | Krippendorff's alpha (SRC-069) and Cohen's kappa (SRC-027); statistics as WP2; PV-04, PV-05, PV-11, PV-13 to PV-15 (ASSUMPTION) |
| 4 | This WP is the evaluation: ET-01 to ET-12 executed; harness reproduces every reported figure from D6.3 |
| 5 | D6.1, D6.2, D6.3, D6.4; M3, M4 |
| 6 | Judging time short (RSK-03) → project judges; low agreement (RSK-04) → revision, collapse; small sets (RSK-08) → sample-size check, "underpowered" or "non-inferiority not established"; R4 non-inferiority unlikely at 30 statements → owner choice before test run |
| 7 | R1–R4 (verification); FN-12 and integrated FN; AC-14 and integrated AC; ET-01 to ET-12; FT-05; MS-01 to MS-06, MS-08, MS-10 |

### WP7 — Technical documentation and handover

| Element | Content (Section 12, activity 7) |
|---|---|
| 1 | As-built specification and deployment instructions with rehearsal; updated risk assessment and deletion; source package with component, licence and training-data inventory; repository scan for sponsor data; handover demonstration; continuity notes |
| 2 | D1.1 to D1.3, D6.1, D6.4; retention decision (ISS-036); licence and training-data terms (ISS-041); team composition for the rehearsal (ISS-051, S10) |
| 3 | Inventory built from the T1.5 pinning record; data scan of the package (PROPOSED) |
| 4 | Deployment rehearsal by a person not involved in the build; inventory check; deletion record; owner acceptance record |
| 5 | D7.1, D7.2, D7.3, D7.4; M5 |
| 6 | Independent rehearsal person not yet identified (ISS-051); a component whose licence or training-data terms fail is replaced or dropped before handover (RSK-12) |
| 7 | C1, C2; all AC (documentation); IF-07 specification; feature 9; MS-06 |

## 2. Task refinements made in S07 (no renumbering)

| Task | Refinement | Reason |
|---|---|---|
| T1.2 | Two R3 properties stated independently of the transition table | Gives ET-06 an oracle that can catch errors in the table |
| T1.5 | Pinning of every component with its licence file read on the pinned version | QA-010; ISS-041 |
| T2.1 | Four-condition licensing gate for DS-01 and DS-02 | ISS-044 |
| T2.2 | Non-inferiority-then-superiority procedure, Holm adjustment, three-level absence definitions, PV-12 to PV-15 | ISS-042, ISS-043, ISS-045 |
| T2.5 | Blind judging screen recording time per judgment; margin-shifted randomization test; Clopper–Pearson intervals | FT-05 input; ISS-042; ISS-043 |
| T3.3, T3.4 | Exact vector search for evaluation runs; date filter by filtered search or over-fetch; BM25 tuned on development split | Removes approximate-search error from comparisons; fair baseline (ISS-045) |
| T4.3 | Network egress allowlist; request-payload hash compared with approved-text hash | Makes CP-1 bypass tests and ET-08 meaningful |
| T5.1, T5.3 | Database trigger on the outcome field; insert-only, hash-chained audit log | R3 enforcement below the service layer; tamper evidence (C2) |
| T6.2 | R4 development statements (PV-13) and sample-size checks for MS-01 to MS-03 | ISS-042, ISS-049 |
| T6.3, T6.5 | ET-12 extended judging on a sample of pool-absent queries | ISS-043, ISS-050 |
| T6.6 | Outcome labels; default-configuration rule | ISS-045 |

## 3. Section 8 rows and their verification steps

| Row | Verification step | Test and task | Evidence | Pass rule |
|---|---|---|---|---|
| Feature 1 | Import of the field-mapped test file and of a registered source | T3.1, T3.7 | D3.1 import report and test log | Rejected rows listed with reasons; every item carries source type, availability status and permission note |
| Feature 2 | R1 list with evidence passages on the release | T3.4, T6.5; ET-01, ET-05 | D3.2 run files; D6.3 | Every candidate has an evidence passage |
| Feature 4 | R2 list per registered source | T3.4, T6.5; ET-03, ET-05 | D3.2; D6.3 | As feature 2, plus source of each item |
| Feature 5 | External search with stored provenance and CP-1 | T4.1 to T4.5; ET-08 | D4.1, D4.2 | Logged text equals sent text; provenance complete |
| Feature 7 | Record with template, approval history, decision log, versions, report export | T5.1, T5.5; ET-07 | D5.1 | Exports validate against D1.1 schemas |
| Feature 8 | Role-based access and append-only log | T5.2, T5.3; ET-06, ET-07 | D5.1, D5.3 | Hash chain verifies; no role other than assessor can approve |
| Feature 9 | Defined extension interfaces | T1.3, T7.1 | D1.1, D7.1 | IF-02, IF-03, IF-07 specified with schemas |
| MS-01 | Paired comparison against B-LEX on the Track P (and, if available, Track S) test split | T6.3, T6.5, T6.6; ET-01, ET-01b, ET-12 | D6.3, D6.4 | Lower 95% limit of the paired nDCG@10 difference above −PV-07 after Holm adjustment, and floor PV-11 met; superiority reported |
| MS-02 | As MS-01 per registered source | T6.3, T6.5, T6.6; ET-03, ET-04, ET-12 | D2.2, D6.3, D6.4 | As MS-01 on P@5; pool-based false-reassurance rate (lower bound) and ET-12 estimate reported |
| MS-03 | Three-formulation comparison on PV-08 need statements | T6.2 (PV-13 pilot), T6.5, T6.6; ET-09 | D4.1, D6.3, D6.4 | Lower 95% limit of Q-C − Q-A success@10 above −PV-12; otherwise "non-inferiority not established" |
| MS-04 | Generated approval suite on the release | T5.6, T6.5; ET-06, ET-07 | D5.3 executed in D6.3 | 0 records reach Approved without CP-5; 0 changes escape CP-6 |
| MS-05 | Disclosure check over every external query of ET-09 | T4.5, T6.5; ET-08 | D6.3 | 100% of queries have a logged approval of the exact text sent (while CP-1 applies) |
| MS-06 | Version-field check over every approved record | T5.1, T6.5; ET-07 | D6.3 | 100% of approved records store model, index, connector and template versions |
| MS-07 | Not applicable | — | — | Feature outside the funded scope (DEC-028) |
| MS-08 | Timing on the reference environment at each confirmed corpus size | T3.6, T6.5; FT-02, ET-10 | D3.3, D6.3 | 95th-percentile display time ≤ PV-09 |
| MS-09 | Not applicable | — | — | Control outside the funded scope (DEC-028) |
| MS-10 | Inspection of every listed item in R1, R2 and R4 result sets | T5.4, T6.5; ET-05 | D6.3 | 100% of items show source type, availability status, terms note and evidence passage |

## 4. Cross-section consistency checks (self-reported; key items scripted)

| Check | Result |
|---|---|
| Section 12 headings repeat Section 13 numbers and titles in the same order | Consistent (scripted) |
| Section 7 walk-through | Section 7 v0.3 (corrected at the S06 gate, DEC-033) makes the walk-through conditional on assessor availability; Section 12 activity 6 says the same and states that the evaluation does not depend on it |
| Section 7 judging group | Section 7: sponsor assessors if they can take part, otherwise project judges; Section 12 uses the same rule |
| Section 8 targets versus Section 12 decision rules | MS-01 to MS-03 in Section 8 v0.4 use the same margins, interval rule and "not required" wording as Section 12 (scripted for margins) |
| Section 13 activity 6 tasks versus Section 12 | Section 13 v0.2 names the deeper absence check; effort not yet updated (S10, ISS-050) |
| Section 13 effort versus Section 12 | Section 12 contains no hours; Section 13 figures remain provisional (DEC-033) |
| Deliverables | Every D1.1 to D7.4 named in `S06_DELIVERABLES_AND_ACCEPTANCE` appears in Section 12 (scripted) |
| Acceptance independent of BM25 outcome | S06 rule, Section 8 v0.4 and Section 12 agree (scripted) |
| Excluded functions | Grouping, generated summaries and mandatory per-candidate labelling appear in Section 12 only as excluded (scripted) |

## 5. Deliberately not in Section 12

Personnel, assignment of activities to the three core members or the potential collaborator, person-hours, staffing capacity, salaries, funding and schedule are S10 decisions (DEC-033). Sponsor data, solution-example databases, production systems, patent-service credentials and external disclosure permissions are not assumed; each has the branch named in Section 12.
