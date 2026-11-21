# S07_CORRECTED_EVALUATION_METHODOLOGY

| Field | Value |
|---|---|
| Document ID | S07_CORRECTED_EVALUATION_METHODOLOGY |
| Version | 1.0 |
| Status | APPROVED |
| Stage | S07 |
| Date | 2026-11-21 |
| Depends on | DEC-031; DEC-033; DEC-034; S05_EVALUATION_DESIGN; S05_DATA_AVAILABILITY_AND_SUBSTITUTES; S06_DELIVERABLES_AND_ACCEPTANCE; ISS-042; ISS-043; ISS-044; ISS-045; SRC-011; SRC-066; SRC-067; SRC-079; SRC-082 to SRC-090 |

- **Purpose:** the record of how S07 resolved the four mandatory corrections from the independent S05 audit (DEC-031) before the evaluation methodology is frozen. The corrected rows are written into `S05_EVALUATION_DESIGN` v2.0 and `proposal/DRAFT_SEC08_FEATURES` v0.4; this file gives the reasoning, the procedures and the planning calculations behind them. WP2 deliverable D2.1 carries the corrected versions (S06 handoff).
- **Status of content:** PROPOSED evaluation methodology. No test has been run and no result exists. Margins, sample sizes and depths below are planning values (ASSUMPTION, AS-12) awaiting owner confirmation (ISS-039, ISS-049, ISS-050). Sample-size figures are normal-approximation planning calculations (PROPOSED), recomputed by `qc/S07_QC_CHECK.py`.
- **New IDs:** ET-12, PV-12 to PV-15 (defined in `S05_EVALUATION_DESIGN` v2.0); ISS-049 to ISS-051.

## 1. Summary of the corrections

| Issue | Audit finding (DEC-031) | Resolution in S07 | Status after S07 |
|---|---|---|---|
| ISS-042 (MS-03) | "Not lower than unaided keyword queries" was to be read from a two-sided superiority test; a non-significant difference is not evidence of non-inferiority | Option chosen: a pre-declared non-inferiority test with margin PV-12 on the paired difference Q-C − Q-A in success@10; superiority tested second in a closed sequence; a sample-size check before the test run; "non-inferiority not established" reported when the interval crosses −PV-12 (§2) | Corrected in design; margin and R4 sample size need owner confirmation (ISS-049) |
| ISS-043 (ET-01b, ET-04) | "Nothing relevant" was defined from the judged pool and read as absence from the corpus | Three levels of absence defined (pool-absent, depth-checked, verified); metrics renamed as pool-based; the pool-based false-reassurance rate stated as a lower bound; new test ET-12 estimates how often pool-absent queries do have a relevant item deeper in the ranking or the source (§3) | Corrected in design; sample and depth need owner confirmation (ISS-050) |
| ISS-044 (CQADupStack) | The dataset licence had not been read on the original distribution; a code-repository or mirror licence was not sufficient | Licence check carried out on the original distribution and the authors' script repository; licence of the data not established; conflicting third-party statements recorded; licensing decision gate defined for WP2 T2.1 (§4) | Check done; **licence not established**; DS-01 and DS-02 stay unusable until the gate passes (ISS-044 remains open) |
| ISS-045 (BM25 criterion) | Statistically supported outperformance of BM25 was a mandatory acceptance criterion for MS-01 and MS-02 | Acceptance of the evaluation separated from the empirical outcome; MS-01 and MS-02 restated as non-inferiority to B-LEX within PV-07 plus the absolute floor PV-11, with superiority as a secondary, reported hypothesis; a default-configuration rule decides what the as-built prototype uses when non-inferiority is not shown (§5) | Corrected in design under the owner's S07 instruction (DEC-034) |

Multiplicity control for all confirmatory hypotheses is defined in §6. The changes to other files are listed in §7.

## 2. ISS-042: MS-03 as a non-inferiority comparison

### 2.1 Why the S05 wording was wrong

S05 stated the MS-03 target as "Q-C success@10 not lower than Q-A" and planned to test it with the two-sided paired randomization test of §6, which tests for a difference. A non-significant result of that test means only that a difference was not detected; with 30 need statements per track (PV-08) a real shortfall could easily go undetected. Regulatory guidance on comparative trials states the general rule: non-inferiority is shown when the two-sided 95% confidence interval for the difference lies entirely above −Δ, where Δ is a margin fixed in advance, and a margin chosen after seeing the data is a serious problem (SRC-087, CLM-060). The European Medicines Agency has published a draft guideline intended to replace that document (SRC-088); only its status page was read, not its text. The project cites the statistical principle, not regulatory applicability.

### 2.2 Corrected procedure

1. **Estimand.** Per need statement *i*, d_i = s_i(Q-C) − s_i(Q-A), where s_i is 1 if the top 10 contains at least one item graded 2 on the R4 scale and 0 otherwise. The estimand is the mean of d_i over the test need statements of one track and one patent service.
2. **Margin.** PV-12 = 0.10 absolute (ASSUMPTION; owner confirmation ISS-049): the assisted, assessor-edited query may find a relevant prior-art item for at most 10 fewer need statements in 100 than an unaided keyword query and still count as non-inferior. The margin is fixed in D2.1 before any R4 test result list is judged.
3. **Decision rule.** Non-inferiority is concluded when the lower limit of the two-sided 95% paired bootstrap interval (PV-06 resamples) for the mean of d_i is above −PV-12. The confirmatory p-value is a one-sided sign-flip randomization test of H0: mean(d) ≤ −PV-12, computed on d_i + PV-12. The sign-flip test assumes that the shifted differences are symmetric under H0; the bootstrap interval is reported alongside so that the two can be compared (PROPOSED).
4. **Superiority second.** Only if non-inferiority is concluded, superiority (lower limit above 0) is assessed. Testing superiority after non-inferiority in this order corresponds to a closed test procedure and needs no further multiplicity adjustment for that pair (SRC-087, CLM-060); the family-wide adjustment in §6 still applies.
5. **Reporting vocabulary.** "Non-inferior" (lower limit > −PV-12); "superior" (lower limit > 0); "non-inferiority not established" (interval contains −PV-12); "inferior" (upper limit < −PV-12). A non-significant superiority result is never reported as "not lower" or as equivalence.

### 2.3 Sample size: what 30 need statements can show

For a paired binary outcome, the variance of d_i is ψ − Δ², where ψ is the share of discordant need statements (one formulation succeeds, the other fails) and Δ is the true mean difference. With Δ = 0, a two-sided 5% level and 80% power, the normal approximation gives n ≈ 7.849 × ψ / PV-12² need statements (PROPOSED planning calculation, CLM-064).

| Discordant share ψ | n needed for PV-12 = 0.10 | Half-width of the 95% interval with n = 30 |
|---|---|---|
| 0.1 | 79 | 0.113 |
| 0.2 | 157 | 0.160 |
| 0.3 | 236 | 0.196 |

At PV-08 = 30, the interval half-width exceeds the margin for every discordance rate in the table, so non-inferiority would very probably not be established even if the two formulations performed identically. This is stated in the protocol instead of being discovered at the end. The method therefore adds an R4 development set of PV-13 = 10 need statements per track (ASSUMPTION; ISS-049), searched with all three formulations and judged during the pilot (T6.2), to estimate ψ. After the pilot, one of three owner choices is recorded in D2.1 before the test run: (a) raise PV-08 to the computed n within the judging budget; (b) keep PV-08 and report MS-03 as an estimate with its interval, stating in advance that non-inferiority is not expected to be established at that size; (c) change PV-12 with a written justification that does not use test data. ISS-049 records the choice.

### 2.4 Corrected MS-03 target

"Assessor-edited automatic queries (Q-C) non-inferior to unaided keyword queries (Q-A, the baseline) in success@10: lower limit of the 95% interval of the paired difference above −0.10 (margin to be confirmed); superiority tested second; reported per track and patent service, with 'non-inferiority not established' where the interval contains the margin."

## 3. ISS-043: absence of relevant items

### 3.1 Definitions

| Term | Definition | What it supports |
|---|---|---|
| Pool-absent query | A test query whose judged pool (top PV-03 items of every configuration in `S05_EVALUATION_DESIGN` §2) contains no item graded ≥ 2 | "No relevant item was found among the items any configuration ranked in its top PV-03." Nothing about the rest of the corpus |
| Depth-checked absent query | A pool-absent query for which the extended judging of ET-12 (ranks PV-03 + 1 to the PV-15 depth of every configuration) also finds no item graded ≥ 2 | Absence to that depth across all configurations; not corpus-wide absence |
| Verified absent query | A query for which every item in the searchable source dated before the query has been judged and none is graded ≥ 2 | Absence from the source. Feasible only for small sources (PV-15 size condition) |

S05 used "established by judging the full pool" for ET-04. That wording is replaced: judging the full pool establishes pool-absence only.

### 3.2 Corrected ET-01b and ET-04 metrics

- **ET-01b, renamed "Behaviour on pool-absent queries".** Metric: *pool-based false-match rate*, the share of pool-absent test queries for which the top candidate scores above the R1 display threshold. Each displayed candidate is itself in the pool and judged, so the statement "this displayed item is not relevant" is verified; the qualifier "pool-based" refers to the set of queries on which the rate is computed.
- **ET-04.** *Pool-based false-reassurance rate*: the assistant reports "no example above threshold" while the pool contains an item graded ≥ 2. Every such case is a verified error, but queries where both the pool and the assistant report nothing are counted as correct only relative to the pool. The pool-based rate is therefore a **lower bound** on the true false-reassurance rate, and is reported with that label. *False-alarm rate* (a candidate is shown and no displayed item is graded ≥ 2) is item-verified and keeps its name.
- **Source property (R2).** "Share of needs with at least one grade ≥ 2 example" is renamed "share of needs with at least one grade ≥ 2 example in the judged pool" and reported as a lower bound on the share in the source.

### 3.3 ET-12: extended absence check (new test)

1. **Sample.** For each retrieval test (ET-01, ET-03) and track, draw a simple random sample of PV-14 = 10 test queries (ASSUMPTION; ISS-050) from the pool-absent queries, plus any queries for which the assistant reported "no example above threshold". The sample is drawn by a seeded script after test-pool judging and before any analysis; if fewer queries qualify, all are taken.
2. **Extended judging.** Judge the union of ranks PV-03 + 1 to 50 of every configuration (PV-15 depth; ASSUMPTION; ISS-050), de-duplicated, blind to configuration and in random order. If the searchable source holds at most 200 items dated before the query (PV-15 size condition), judge all of them instead, which makes the query "verified absent" or not.
3. **Estimate.** Let x be the number of sampled pool-absent queries for which extended judging finds an item graded ≥ 2. Report x / m with the Clopper–Pearson exact 95% interval (SRC-090, CLM-062). This estimates the share of pool-absent queries that are not absent to the checked depth. It is itself a lower bound on corpus-level non-absence unless judging was exhaustive.
4. **Precision stated in advance.** If x = 0, the upper 95% limit is 1 − 0.025^(1/m): 0.308 for m = 10 and 0.168 for m = 20 (PROPOSED arithmetic, CLM-062). A sample of 10 can therefore only show that the pool missed relevant items in a large share of pool-absent queries; it cannot show that the pool is close to complete. The protocol states this, and the owner may raise PV-14 (ISS-050).
5. **Use.** If x > 0, the false-reassurance rate is reported as a pool-based lower bound together with the ET-12 estimate; the evaluation report does not adjust it by modelling. Corpus-level absence is claimed only for "verified absent" queries.
6. **Effort.** Extended judging hours = Σ over sampled queries of (de-duplicated items judged × seconds per judgment) ÷ 3,600. The number of de-duplicated items per query depends on overlap between configurations and is measured in the pilot; ET-12 hours are not yet in the S06 planning figure and are added in S10 (ISS-050, ISS-046).

### 3.4 Corrected wording for Section 8

MS-02 metric column: "rate of wrongly reporting 'no example found', measured against the judged pool (a lower bound) and checked at greater depth on a sample of queries". MS-01 keeps ET-01b as "reported with it", now named as above.

## 4. ISS-044: CQADupStack licence

### 4.1 Check carried out (2026-11-21)

| Source | What it states | Tier | Bearing on the licence of the data |
|---|---|---|---|
| Original distribution page of the dataset authors (SRC-082) | The retrieved page content contains no licence or terms-of-use statement and no attribution requirement; the sections headed "The Data" and "The Script" were not returned in readable form | T1 | Licence of the data **not established** from the original distribution |
| Authors' script repository README (SRC-083) | Scripts for manipulating the data; the data are twelve StackExchange subforums from the data dump released on 26 September 2014; "For licensing information please see the LICENCE file"; the LICENCE file itself could not be retrieved | T1 | The repository licence governs the scripts at least; whether it covers the data is not stated in the README |
| Stack Exchange statement on its data dump (SRC-084) | All community-contributed content on Stack Exchange is licensed under CC BY-SA 3.0; attribution is required | T2 (licensor's own statement) | The underlying posts were released under CC BY-SA 3.0 at the time of the 2014 dump; this does not by itself fix the terms of the authors' derived dataset or of their annotations |
| Third-party mirror, dataset card (SRC-079) | Apache 2.0, stated by the uploader | T3 | Not authoritative; Apache 2.0 is a software licence and is not evidence of the data licence |
| Third-party mirror of the BEIR-packaged version (SRC-085) | CC BY-NC-SA 4.0, stated by the uploader | T3 | Not authoritative; conflicts with SRC-079, and a non-commercial term would matter for later stages |

**Finding:** the licence of the original CQADupStack data cannot be established from the sources reachable in this session. The code licence (whatever the LICENCE file of the script repository says) and the data licence are separate questions, and two third-party mirrors give contradictory statements. DS-01 and DS-02 therefore remain **unusable**. ISS-044 stays OPEN (CLM-059).

### 4.2 Licensing decision gate (WP2 T2.1, before any use of DS-01 or DS-02)

DS-01 or DS-02 may be downloaded for evaluation use, indexed, judged or used in FT-01 only when all four conditions hold and are recorded in the D2.2 licence record:

1. **Data licence identified on the original distribution**: a licence or terms statement for the data (not the scripts) from the dataset authors' distribution, for example a licence file inside the distributed archive, or a written statement from the authors. Opening the archive only to read its licence file is part of T2.1 and is not use of the data.
2. **Compatibility with the planned use**: the terms permit research evaluation, re-grading of pooled items on the R1 scale and retention of judgment files for the project period; share-alike and attribution obligations are written into D2.2 and the D7.3 inventory.
3. **Consistency with the upstream licence**: the stated terms are compatible with the CC BY-SA 3.0 terms of the underlying posts (SRC-084), or the difference is explained by the source.
4. **Owner decision recorded** (OWNER DECISION REQUIRED, ISS-044). The project does not give a legal opinion; if the owner requires one, it is obtained outside the project.

If the gate does not pass before T2.3, Track P for R1 uses another candidate that passes T2.1 (DS-03 or DS-04, each with its own licence check, ISS-038), and FT-01 (ET-02) uses another benchmark with published reference runs and a licence that passes T2.1. No benchmark is named here because none has been licence-checked.

## 5. ISS-045: the role of BM25 in MS-01 and MS-02

### 5.1 Reasoning

Three points decide the question.

1. **Acceptance of the work and the empirical outcome are different things.** S06 already accepts deliverables on inspectable evidence and treats "no supported difference" as a valid result (`S06_DELIVERABLES_AND_ACCEPTANCE`, rule above §1). Keeping outperformance of BM25 as the Section 8 target would contradict that rule and would present an untested empirical outcome as the expected state of the prototype.
2. **No evidence supports a promise of superiority in this setting.** Multi-stage retrieval is a PROPOSED candidate design (CLM-026), no benchmark of need or challenge submissions was found (CLM-025), and no comparator publishes accuracy figures (CLM-034). A target that requires superiority would be a guarantee the project cannot justify (03_STYLE_GUIDE §4, "unearned superiority").
3. **The useful product question is whether a non-lexical configuration is acceptable, and when it should be the default.** A dense or hybrid configuration costs more to run (FT-02) and adds components to maintain. It is worth adopting only if it is not materially worse than B-LEX on the judged test set, and it is clearly preferable only if it is better. Both questions can be answered with pre-declared tests on the same paired data.

The owner's S07 instruction directs exactly this separation (DEC-034).

### 5.2 Corrected procedure

1. **Estimand.** Per test query, d_i = nDCG@10 (MS-01) or P@5 at grade ≥ 2 (MS-02) of the selected configuration minus that of B-LEX on the same judgments. B-LEX parameters are tuned on the development split over a grid fixed in D2.1, so the baseline is not weakened by default settings (PROPOSED).
2. **Non-inferiority first.** Margin δ_R = PV-07 (0.05 absolute), the smallest difference S05 already treats as worth reporting. Non-inferiority is concluded when the lower limit of the two-sided 95% paired bootstrap interval is above −PV-07; confirmatory p-value from the shifted sign-flip randomization test, as in §2.2.
3. **Superiority second**, only if non-inferiority holds (closed sequence, SRC-087).
4. **Absolute floor.** PV-11, fixed after the pilot and before the test run, as in S05.
5. **Sample-size check.** With Δ = 0, 80% power and margin 0.05, the planning approximation gives n ≈ 7.849 × σ² / 0.05², where σ is the standard deviation of d_i: 32 queries for σ = 0.10, 71 for σ = 0.15 and 126 for σ = 0.20 (PROPOSED planning calculation, CLM-064). With PV-01 = 60 test queries, the interval half-width stays at or below 0.05 only if σ ≤ about 0.198. After the pilot, σ is estimated on the development split and the query count is raised within the judging budget, or the result is reported as underpowered (S05 §6 rule, unchanged).
6. **Outcome categories** as in §2.2, item 5, plus "below floor" when the absolute floor is not met.
7. **Default-configuration rule.** The release (D6.1) uses the configuration selected on the development split. If, on the test split of a track, the selected configuration is not concluded non-inferior to B-LEX or falls below the floor, the evaluation report (D6.4) states this, and the as-built specification (D7.1) sets B-LEX as the default retrieval configuration for corpora of that kind, keeping the other configuration available as an option. When only Track P exists, the rule applies to Track P and D7.1 says that the default was chosen on substitute data.

### 5.3 Corrected targets

- **MS-01:** "nDCG@10 not lower than the BM25 baseline by more than 0.05 (lower limit of the 95% interval of the paired difference above −0.05) and at or above the absolute floor fixed after the pilot; superiority over BM25 tested second and reported, not required."
- **MS-02:** the same rule on P@5 at grade ≥ 2, per registered source; source type stated; pool-based false-reassurance rate (lower bound) and the ET-12 estimate reported with it.

## 6. Multiplicity control

S05 left the correction method to the protocol. The protocol (D2.1) uses the Holm step-down procedure (SRC-089, CLM-061) over the confirmatory family of each track, at a family-wise level of 0.05. The family consists of the non-inferiority and superiority hypotheses for MS-01, for MS-02 on each registered source, and for MS-03 on each connected patent service. Holm controls the family-wise error rate for any dependence between the tests; including both members of each non-inferiority/superiority pair makes it conservative, which is accepted for simplicity. Adjusted p-values decide; confidence intervals are reported unadjusted and labelled as such.

Two changes from S05 follow. The comparison of RR with its input run is moved out of the confirmatory family: RR is kept or dropped on the development split, so its test-split comparison is reported as secondary, with an unadjusted interval. Comparisons between tracks are never made (S05 rule 1).

## 7. Changes made to other files

| File | Change |
|---|---|
| `stages/S05/S05_EVALUATION_DESIGN.md` → v2.0 | ET-01b and ET-04 redefined (§3.2); ET-12 added; §6 rewritten for non-inferiority, closed testing and Holm; PV-12 to PV-15 added; §8 targets MS-01 to MS-03 corrected; gate note updated |
| `stages/S05/S05_DATA_AVAILABILITY_AND_SUBSTITUTES.md` → v2.0 | DS-01 and DS-02 licence cells record the S07 check and the gate |
| `proposal/DRAFT_SEC08_FEATURES.md` → v0.4 | MS-01 to MS-03 metric and target cells corrected; gate note updated |
| `proposal/DRAFT_SEC13_ACTIVITIES.md` → v0.2 | Activity 6 key tasks name the deeper absence check; effort unchanged pending S10 |
| `project/S01_TRACEABILITY_MATRIX.md` | Part G rows R1, R2, R4 corrected; Part I added |

## 8. Owner decisions arising

| Issue | Decision | Needed before |
|---|---|---|
| ISS-049 | Confirm PV-12 (MS-03 margin) and PV-13 (R4 development statements); after the pilot, choose option (a), (b) or (c) of §2.3 | D2.1 freeze (T2.2); choice before the test run |
| ISS-050 | Confirm PV-14 and PV-15 for ET-12, and accept the added judging effort | D2.1 freeze; effort in S10 |
| ISS-044 | Licensing decision gate for DS-01 and DS-02 (§4.2) | WP2 T2.1, before T2.3 and T2.6 |
| ISS-039 | Confirm PV-07 as both the minimum difference of interest and the non-inferiority margin for MS-01 and MS-02 | D2.1 freeze |
