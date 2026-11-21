# S05_EVALUATION_DESIGN

| Field | Value |
|---|---|
| Document ID | S05_EVALUATION_DESIGN |
| Version | 3.0 |
| Status | DRAFT |
| Stage | S10 |
| Date | 2026-11-21 |
| Depends on | S01_REQUIREMENTS_REGISTER §1, §1a; S04_ARCHITECTURE; S04_DATA_FLOWS_AND_INTERFACES DF-08; S04_ASSUMPTIONS_AND_STANDARDS §1; S05_DATA_AVAILABILITY_AND_SUBSTITUTES; S05_FEASIBILITY_AND_RISKS; CLM-025 to CLM-028; CLM-045; CLM-047 to CLM-050; CLM-059 to CLM-064; DEC-028; DEC-029; DEC-034; S07_CORRECTED_EVALUATION_METHODOLOGY |

- **S10 alignment (DEF-002, DEC-039):** wording aligned with the S09-corrected master (CP-1 always applied with disclosure clearance and query approval, DEC-035; EPO OPS thresholds as fair-use guidance, DEC-038; retention default, DEF-034). Content otherwise unchanged.
- **S07 corrections (DEC-031, DEC-034):** the four mandatory corrections are made in this version: ET-01b and ET-04 redefined and ET-12 added (ISS-043); §6 rewritten for non-inferiority, closed testing and Holm (ISS-042, ISS-045); PV-12 to PV-15 added; §8 targets MS-01 to MS-03 corrected. Reasoning and planning calculations: `stages/S07/S07_CORRECTED_EVALUATION_METHODOLOGY`. The CQADupStack licence (ISS-044) is not established; DS-01 and DS-02 stay unusable until the T2.1 licensing gate passes.
- **Status of content:** PROPOSED evaluation design. No test has been run, no dataset has been obtained and no result exists. Every value in §7 is a planning value (ASSUMPTION, AS-12) that the owner can change; every entry in §8 is a target, not a result.
- **Scope:** the narrowed Option B essential set (DEC-028). Tests for excluded options (FN-04 grouping, FN-07 summaries, mandatory CP-2) are not designed here; MS-07 and MS-09 stay conditional in the Section 8 draft.
- **IDs defined here:** ET (evaluation test), PV (planning value). Data candidates (DS), data requirements (DR), feasibility tests (FT) and risks (RSK) are defined in the two companion files.

## 1. Design rules

1. **Two data tracks, never pooled.** *Track S* uses sponsor data: exported submissions, sponsor-confirmed solution-example sources and sponsor assessors as judges. It runs only if ISS-002 and, for R2, ISS-003 are answered yes. *Track P* uses public or constructed substitute data and project judges. Every result table, file name and figure carries its track label. A Track P result is evidence about the method on that data only; it is never reported as performance on sponsor submissions (ISS-028, CLM-045).
2. **Protocol frozen before test data is seen.** Metrics, grade scales, configurations, significance procedure and acceptance targets are fixed in an evaluation protocol document before the test split is judged. Changes after that point are logged with a reason and reported.
3. **Development and test split by time.** Configuration choice, fusion weights and thresholds are tuned on the development split only. The test split is run once per configuration. This applies the realistic, time-ordered evaluation that S02 found avoids overestimation in duplicate retrieval (S02 matrix rows 2.3 and 6.4; SRC-010).
4. **Targets are relative to a baseline, and no superiority is promised.** No absolute performance level can be justified in advance: no public benchmark of need or challenge submissions was identified (CLM-025), and no comparator publishes accuracy figures (CLM-034). The primary criterion for each retrieval test is non-inferiority to a stated baseline within a pre-declared margin; superiority is tested second and reported, not required (§6; corrected in S07, ISS-045). Absolute floors are set after the pilot and before the test run (PV-11). Acceptance of the evaluation deliverables does not depend on the outcome (`S06_DELIVERABLES_AND_ACCEPTANCE`).
5. **The assistant's output is a ranked list for an assessor.** Metrics are chosen for what the assessor sees: graded quality near the top of the list, and whether anything useful appears in the part of the list a person will read.

## 2. Retrieval configurations and baselines (R1, R2)

AC-05 runs the same configurations on every registered corpus (AD-01, AD-02). Names below are candidates whose licences and input limits are verified in `S05_FEASIBILITY_AND_RISKS` §1; S07 confirms versions.

| ID | Configuration | Role | Basis |
|---|---|---|---|
| B-REC | Stored items in reverse date order, no ranking | Naive baseline: what an assessor sees by browsing recent records | Project choice; shows whether any ranking helps |
| B-LEX | BM25 over title and text fields (Pyserini) | Primary baseline for every retrieval test | SRC-001, SRC-036; S02 matrix 6.5 |
| B-FP | Near-duplicate fingerprints (shingle resemblance) | Baseline for the "duplicate" grade only | SRC-012; FN-02 already computes fingerprints |
| D-1 | Compact English sentence encoder (candidate: all-MiniLM-L6-v2) | Dense first stage, low resource | SRC-037; English only; input truncated beyond 256 word pieces (CLM-054) |
| D-2 | Multilingual encoder (candidate: multilingual-e5-base) | Dense first stage if ISS-007 reports non-English text; otherwise second dense candidate | SRC-075; 512-token limit (CLM-054) |
| D-3 | Long-input multilingual encoder (candidate: BGE-M3) | Dense first stage for long submissions | SRC-033, SRC-076; inputs up to 8,192 tokens (CLM-054) |
| H-RRF | Reciprocal rank fusion of B-LEX and the best dense run | Hybrid | SRC-007 |
| H-CC | Convex score combination of the same runs, weight tuned on the development split | Hybrid, compared with H-RRF | SRC-008 |
| RR | Cross-encoder re-ranking of the top 50 of the best hybrid (candidate: bge-reranker-v2-m3) | Optional second stage; kept only if it scores higher than its input run on the development split and meets the latency target | SRC-006, SRC-077; S02 synthesis §4 |

Long texts are split into passages by FN-02; the document score is the maximum passage score, and the best passage is the evidence span shown to the assessor (AD-05). Language handling follows ISS-007: if submissions are not in English, D-1 is dropped and RQ-07 is activated (AS-06).

## 3. Grade scales

Grades are defined in a judging guide with worked examples, revised once after the pilot (ET-11). Binary metrics treat grade ≥ 2 as relevant.

| Test | 3 | 2 | 1 | 0 |
|---|---|---|---|---|
| R1 (stored submission for a new submission) | Duplicate: the same need | Overlapping: part of the need is the same | Related: same topic area, different need | Unrelated |
| R2 (solution example for a submitted need) | Addresses the need as stated | Addresses part of the need | Related to the need, but does not address it | Unrelated |
| R4 (external patent or solution example) | — | Relevant prior art: describes a solution or a closely matching technique for the need | Marginal: shares a technical element only | Not relevant |

The R1 labels follow the relationship labels proposed in S02 (synthesis §3, item 3). Gains for nDCG are the grade values (linear gain).

## 4. Tests per requirement

### R1 — compare a new submission with stored submissions (operative reading, DEC-029)

| ID | Test | Data and procedure | Metrics | Spec |
|---|---|---|---|---|
| ET-01 | Similar-submission ranking quality | Sort the corpus by submission date. The last time segment supplies test queries (PV-01) and the segment before it development queries (PV-02); each query searches only items dated before it. Pool the top PV-03 items of every configuration in §2 and judge the pool on the R1 scale. Pool-absent queries (no item graded ≥ 2 in the judged pool) are kept and analysed in ET-01b and ET-12 | Primary: nDCG@10 (SRC-025). Secondary: Recall@20 of items graded ≥ 2; MRR of the first duplicate; P@5; bpref and judged@10 as completeness checks (SRC-068) | MS-01 |
| ET-01b | Behaviour on pool-absent queries (corrected S07, ISS-043) | For test queries whose judged pool contains no item graded ≥ 2, record the highest score shown and how often the top-ranked item scores above the display threshold chosen on the development split. Pool-absence does not show that the corpus holds no similar submission; ET-12 checks a sample at greater depth | Pool-based false-match rate at the display threshold | MS-01 (reported with it) |
| ET-02 | Harness reproduction | Run B-LEX on a public benchmark with published reference runs through Pyserini and compare with the reference result | Difference from reference run on the same metric | FT-01 |

Track S uses exported submissions. Track P uses a public duplicate-question collection with post dates, if its licence check passes (DS-01, ISS-038); its "duplicate" labels were assigned by forum users (SRC-011 limitation), so Track P judges re-grade the pooled items on the R1 scale rather than relying on the original labels alone.

### R2 — assess whether relevant existing solution examples can be identified for a submitted need (corrected, DEC-029)

R2 is tested against whatever source is registered. No source is assumed. The test design is the same for a sponsor-held source and for an external source; the source type is a reported condition (ISS-037).

| ID | Test | Data and procedure | Metrics | Spec |
|---|---|---|---|---|
| ET-03 | Solution-example ranking quality | Queries: submissions (Track S) or need statements from the substitute set (Track P, DS-05). Corpus: each registered solution-example source, indexed separately (AD-01). Pool and judge on the R2 scale as in ET-01 | Primary: P@5 at grade ≥ 2 (share of the first five shown that address at least part of the need). Secondary: nDCG@10; Recall@20 | MS-02 |
| ET-04 | "Can be identified" signal (corrected S07, ISS-043) | R2 asks whether examples can be identified, so "none found" is a legitimate answer. Test queries include pool-absent needs: no item graded ≥ 2 in the judged pool, which is not the same as no relevant item in the source. The assistant shows "no example above threshold" when no candidate passes a threshold set on the development split | Pool-based false-reassurance rate (assistant reports none, but a grade ≥ 2 item exists in the pool), reported as a lower bound with the ET-12 estimate; false-alarm rate (assistant shows a candidate, none of the displayed items is graded ≥ 2) | MS-02 (reported with it) |
| ET-12 | Extended absence check (added S07, ISS-043) | For each retrieval test and track, a seeded random sample of PV-14 pool-absent queries (plus queries where the assistant reported none) is judged to the PV-15 depth of every configuration, or exhaustively when the source meets the PV-15 size condition | Share of sampled pool-absent queries with an item graded ≥ 2 found deeper, with Clopper–Pearson 95% interval (SRC-090); count of verified absent queries | MS-01, MS-02 (reported with them) |
| ET-05 | Source attribution and evidence display | Inspect every listed item in the R1, R2 and R4 result sets produced during ET-01, ET-03 and ET-09 | Share of listed items with source type, availability status, permission note and evidence passage | MS-10 |

If no R2 source is confirmed before the evaluation, ET-03 and ET-04 run on Track P only, and Section 8 states that MS-02 was tested on substitute data. Judges also record, for each R2 query, whether a relevant example exists among the judged items; the share of needs with at least one grade ≥ 2 example in the judged pool is a property of the source (a lower bound on the share in the whole source), reported separately from ranking quality so that a sparse source is not mistaken for a weak method.

### R3 — final human approval

R3 is tested as a workflow property, not statistically. The requirement is met only if no path exists to a final outcome without an assessor's approval.

| ID | Test | Procedure | Pass criterion | Spec |
|---|---|---|---|---|
| ET-06 | Approval enforcement | Model-based test of the AC-09 state machine: every (state, event, role) combination of Draft, In review, Submitted, Approved and Returned, attempted through IF-04 and directly against the service layer, including evaluator and administrator roles, expired sessions and replayed requests; plus randomized event sequences generated from the same model | No record reaches Approved, and no outcome field is written, without a CP-5 approval event bound to an authenticated assessor | MS-04 |
| ET-07 | Re-approval after change and record reproducibility | After approval, change each editable field once; check that a new Draft version is created and needs CP-5 again (CP-6). For every approved record, check that model, index, connector and template versions are stored (AD-11) and that the audit log holds one entry per transition | Every change produces a new version requiring approval; every approved record carries all four version fields | MS-04, MS-06 |

### R4 — external patents and solution examples

| ID | Test | Data and procedure | Metrics | Spec |
|---|---|---|---|---|
| ET-08 | Disclosure control and provenance | For every external query issued during ET-09, check the logged query text against the text actually sent, the disclosure clearance and the approving assessor (CP-1, required for every external query, DEC-035), and the stored source, retrieval date and terms note of each result | Share of external queries with both a logged approval of the exact text sent and a disclosure clearance; unrefused attempts to send confidential text without authorization; share of results with complete provenance | MS-05, MS-10 |
| ET-09 | Relevance by query formulation | Need statements (PV-08; PV-13 development statements for the pilot) are searched in one patent service selected from `S05_FEASIBILITY_AND_RISKS` §2 with three formulations: Q-A, a keyword query written by a judge without assistance (baseline representing manual searching, CTX-02); Q-B, an automatically generated query; Q-C, Q-B after assessor editing at CP-1. Pool the top 10 of each formulation and judge on the R4 scale | Primary: success@10 (at least one grade-2 item in the top 10). Secondary: P@10 at grade 2 | MS-03 |

Track S queries use submission text only if ISS-033 authorizes it. Otherwise ET-09 runs on Track P need statements, which are public text, so the R4 evaluation does not depend on the disclosure decision. No estimate of R4 performance can be given in advance: no study of retrieval from need statements to patents was found (S02 synthesis §5; ISS-028).

### Response time and judging reliability

| ID | Test | Procedure | Metric | Spec |
|---|---|---|---|---|
| ET-10 | Response time | On the reference environment (AS-11), at each corpus size in PV-10 that the owner confirms, open each test query and time the display of R1 and R2 results with the selected configuration | 95th-percentile time from opening a submission to display | MS-08 |
| ET-11 | Judging reliability | A share of query-item pairs (PV-04) is judged independently by two judges. Agreement on the ordinal scale is reported with Krippendorff's alpha (SRC-069) and, for the binary relevant/not-relevant split, Cohen's kappa (SRC-027). Disagreements are adjudicated by a third judge; raw and adjudicated judgments are both kept | Agreement statistic per test and track | Evaluation validity, not a product specification |

## 5. Assessor validation

The judgments are the measuring instrument, so they are validated before any configuration is compared.

1. **Who judges.** Track S: sponsor assessors (ISS-012). Track P, or Track S if assessors are unavailable: project judges with domain knowledge, working from the same guide; results are labelled "project judges" (AS-10).
2. **Pilot.** Development queries are judged first (FT-05). The pilot measures agreement and time per judgment, and the guide is revised once. If agreement stays below PV-05 after one revision, the R1 and R2 scales are collapsed to three levels (merging grades 3 and 2) and the change is reported.
3. **Calibration across judge groups.** If both sponsor assessors and project judges take part, a shared subset is judged by both groups and the agreement between groups is reported, so that Track P results judged by project judges can be read against assessor judgments.
4. **Sensitivity.** Configuration comparisons are repeated with each judge's own judgments on the double-judged subset. S02 found that system rankings stayed stable despite assessor disagreement on TREC-scale topic sets, with smaller sets possibly less stable (matrix row 6.2, SRC-026); the repetition checks whether that holds here.
5. **Effort.** Judging hours = test queries × mean pooled items per query × (1 + PV-04) × seconds per judgment ÷ 3,600, summed over tests and tracks. Pooled items per query and seconds per judgment are unknown until FT-05; S06 sizes the judging activity from this formula with the pilot values, not from a guess.

## 6. Statistical analysis (rewritten in S07; ISS-042, ISS-045)

- Unit of analysis: the query. Each comparison uses per-query paired differences between two configurations (or two R4 formulations) on the same queries and judgments.
- Confirmatory comparisons are pre-declared: the selected configuration against B-LEX for MS-01 and for MS-02 on each registered source, and Q-C against Q-A for MS-03 on each connected patent service. B-LEX parameters are tuned on the development split over a grid fixed in the protocol.
- Each confirmatory comparison is a closed sequence. Non-inferiority first: the lower limit of the two-sided 95% paired bootstrap interval (PV-06) of the mean difference must lie above minus the margin (PV-07 for MS-01 and MS-02; PV-12 for MS-03); the confirmatory p-value is a one-sided sign-flip randomization test on the differences shifted by the margin. Superiority second, only if non-inferiority holds (lower limit above zero; two-sided randomization test). A non-significant superiority test is never read as non-inferiority (SRC-087, CLM-060). In a comparison over TREC runs, the randomization, bootstrap and t tests showed little practical difference, while the Wilcoxon and sign tests were less able to detect significance and could produce false detections (CLM-047, SRC-066); the Wilcoxon and sign tests are therefore not used.
- Multiple comparisons: Holm step-down procedure over the confirmatory family of each track at a family-wise level of 0.05 (SRC-089, CLM-061). The comparison of RR with its input run is decided on the development split and reported on the test split as secondary, with an unadjusted interval.
- Sample size: error rates in retrieval comparisons depend on the number of topics and on the size of the observed difference (CLM-048, SRC-067). After the pilot, the standard deviation of per-query differences on the development split (MS-01, MS-02) and the discordant share on the PV-13 development statements (MS-03) are used to check whether the planned query counts give an interval half-width no larger than the margin. If not, the query count is raised within the judging budget, the owner choice of ISS-049 is applied, or the result is reported as underpowered. Planning calculations: `S07_CORRECTED_EVALUATION_METHODOLOGY` §2.3, §5.2.
- Incomplete judgments: unjudged items count as not relevant; judged@10 is reported for every run, and bpref is reported as a check of sensitivity to missing judgments because standard measures degrade under substantially incomplete judgments (CLM-049, SRC-068). Pooling all configurations, including B-REC, reduces the chance that a new configuration is penalized for retrieving unjudged items. Absence of relevant items is stated at the level actually checked: pool, depth or verified (ET-12).
- Reporting: mean, per-query distribution, confidence interval and adjusted p-value for each comparison, by track, with one of the outcome labels "superior", "non-inferior", "non-inferiority not established", "inferior" or "below floor". A difference whose interval includes zero is reported as "no supported difference", never as an improvement.

## 7. Planning values (ASSUMPTION, AS-12; owner confirmation ISS-039)

| ID | Item | Planning value | Why this value | Changed when |
|---|---|---|---|---|
| PV-01 | Test queries per retrieval test and track (ET-01, ET-03) | 60 | Starting point for the sample-size check in §6 | Pilot variance or judging budget requires it |
| PV-02 | Development queries per test and track | 20 | Enough for the pilot and threshold tuning without using test queries | Pilot shows unstable thresholds |
| PV-03 | Pool depth per configuration | 10 | Matches the primary metric cut-off | Judged@10 of the selected run falls below the level fixed in the protocol |
| PV-04 | Double-judged share of query-item pairs | 20% | Provides the agreement estimate (ET-11) at one fifth of the extra cost of full double judging | Agreement is low or judges are scarce |
| PV-05 | Minimum agreement before comparing configurations | Krippendorff's alpha ≥ 0.67 on the ordinal scale | Project threshold for proceeding; not taken from a source | Owner or judges set another value before the pilot |
| PV-06 | Significance level; resamples | 0.05, two-sided; 10,000 permutations and bootstrap samples | Conventional level; resample count keeps Monte Carlo error small relative to 0.05 | — |
| PV-07 | Minimum difference of interest, nDCG@10 or P@5 | 0.05 absolute | Smallest difference treated as worth reporting to assessors | Owner sets another value |
| PV-08 | R4 need statements per track (ET-09) | 30, each searched with three formulations | Bounded by judging cost (90 result lists) | Judging budget |
| PV-09 | Response-time target (ET-10) | 95th percentile ≤ 5 s | Project planning value for interactive use; no sponsor figure exists | Owner sets another value |
| PV-10 | Corpus sizes for sizing and timing | 10,000; 100,000; 1,000,000 items | Brackets for an unknown corpus size (ISS-023, AS-07) | ISS-023 answered |
| PV-11 | Absolute floors for MS-01 to MS-03 | Not set now; fixed after the pilot and before the test run | No defensible prior value (rule 4) | — |
| PV-12 | Non-inferiority margin for MS-03 (success@10, Q-C − Q-A) | 0.10 absolute | Largest shortfall (10 need statements in 100) treated as acceptable for an assisted query; project judgement (added S07) | Owner sets another value before the protocol freeze (ISS-049) |
| PV-13 | R4 development need statements per track, for the pilot estimate of the discordant share | 10, each searched with three formulations | Needed to check the MS-03 sample size before the test run (added S07) | Owner decision (ISS-049) |
| PV-14 | Pool-absent queries sampled per retrieval test and track for ET-12 | 10 | Bounded by judging cost; precision stated in advance (added S07) | Owner decision (ISS-050) |
| PV-15 | ET-12 extended judging depth and size condition | Ranks 11 to 50 of every configuration; exhaustive judging if the source holds at most 200 items dated before the query | Deeper than the primary pool at bounded cost (added S07) | Owner decision (ISS-050) |

## 8. Acceptance targets (for the Section 8 table)

| Spec | Target (to be tested; not a result) |
|---|---|
| MS-01 | Selected configuration not lower than B-LEX by more than PV-07 on nDCG@10 (lower limit of the 95% interval of the paired difference above −PV-07) and at or above the absolute floor (PV-11); superiority over B-LEX tested second and reported, not required; reported per track with ET-01b and ET-12 (corrected S07, ISS-045) |
| MS-02 | The same rule on P@5 at grade ≥ 2 on each registered source; pool-based false-reassurance rate (lower bound) and the ET-12 estimate reported; source type of each corpus stated (corrected S07, ISS-043, ISS-045) |
| MS-03 | Q-C non-inferior to Q-A in success@10 with margin PV-12 (lower limit of the 95% interval of the paired difference above −PV-12); superiority tested second; reported per track and per patent service, with "non-inferiority not established" where the interval contains the margin (corrected S07, ISS-042) |
| MS-04 | 0 records reach Approved without a CP-5 event; 0 changes to an approved record escape CP-6 |
| MS-05 | 100% of external queries have both a logged assessor approval of the exact text sent and a disclosure clearance; 0 unrefused attempts to send confidential text without authorization; manual-entry queries reported separately (DEC-035; master Section 8 specification 5) |
| MS-06 | 100% of approved records store model, index, connector and template versions |
| MS-08 | 95th-percentile display time within PV-09 at each confirmed corpus size |
| MS-10 | 100% of listed items carry source type, availability status, permission note and an evidence passage |

## 9. Evaluation sequence and outputs (input to S06)

| Step | Content | Output |
|---|---|---|
| E-0 | Write and freeze the evaluation protocol and judging guide | Protocol document |
| E-1 | Build the harness (AC-14, FN-12); run FT-01 | Harness; reproduction note |
| E-2 | Obtain data per track (`S05_DATA_AVAILABILITY_AND_SUBSTITUTES` §3); build splits | Versioned test collections |
| E-3 | Pilot judging on development queries (FT-05); revise guide | Pilot report with agreement and time per judgment |
| E-4 | Tune on development split; select configuration | Selection record |
| E-5 | Judge test pools; single test run; extended absence check ET-12; workflow tests ET-06 to ET-08; timing ET-10 | Judgments, run files, test logs |
| E-6 | Analysis and evaluation report, by track | Evaluation report feeding Section 8 and Section 17 |

## 10. What this evaluation cannot show

It does not measure assessment speed, assessor workload or decision accuracy in live use. No baseline review time or error rate has been supplied (ISS-011), so the expected benefits in REF-01 remain hypotheses (C5, CLM-006). A timed task study with assessors would be needed for that; it is not in the funded scope and is noted for Section 11. Track P results do not predict Track S results.
