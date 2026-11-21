# S08_EDITORIAL_LOG

| Field | Value |
|---|---|
| Document ID | S08_EDITORIAL_LOG |
| Version | 1.0 |
| Status | SUBMITTED FOR GATE |
| Stage | S08 |
| Date | 2026-11-21 |
| Depends on | IRAA_PROPOSAL_EN_MASTER; S07_HANDOFF; DEC-035; ISS-029; ISS-030; ISS-052; 02_SOURCE_LOG; 02_CLAIM_REGISTER; 03_STYLE_GUIDE; S01_REVIEWER_CRITERIA_REGISTER |

- **Purpose:** record of editorial passes A to E applied once to the assembled master (no alternative full drafts were produced). Each pass states what was checked, how, and what changed.
- **Check classes:** *Scripted* checks are reproduced by `qc/S08_QC_CHECK.py`. *Self-reported* checks were performed by the drafting session by reading and are not independently verified (gate protocol §6).

## Pass A. Source fidelity of consequential claims (self-reported)

Scope: the sources named in the S07 handoff (SRC-066 to SRC-069, SRC-087, SRC-089, SRC-090) and the S02 sources whose statements the master relies on (ISS-029). No broad literature search was run. Page fetching required an approval that was not available in this session, so checks used search-result extracts of full-text copies or abstract pages; the depth reached is stated per row.

| Source | Statement used in the master | Depth reached in S08 | Result | Action in the master |
|---|---|---|---|---|
| SRC-002 (BEIR) | 18 heterogeneous datasets; BM25 a robust baseline; re-ranking and late-interaction best on average at high computational cost | A (NeurIPS and arXiv abstracts) | Confirmed | Used in Sections 6 and 12; "robust" paraphrased as "competitive" |
| SRC-005 (MTEB) | No single text-embedding method dominates across all tasks; 8 task types | A (abstract) | Confirmed | Used in Sections 6 and 12 |
| SRC-010 (Rakha et al.) | Classical evaluation overestimates performance compared with a realistic evaluation using all reports available | A (abstract on an author page) | Qualitative statement confirmed; the "median 17–42%" figure in CLM-017 was not found in the extracts read | Figure not used; qualitative statement only |
| SRC-015 (Just, 2024) | Count of three problem–solution matching studies (CLM-019) | A (abstract: 167 articles, 18 practices) | Count not confirmed | CLM-019 not used in the master |
| SRC-022 (Parasuraman and Manzey) | Automation bias: omission and commission errors; naive and expert participants; not prevented by training or instructions | A (publisher abstract and author copy extract) | Confirmed | Used in Section 6 |
| SRC-066 (Smucker et al.) | Randomization, bootstrap and t tests agree closely; Wilcoxon and sign tests poor at detecting significance and prone to false detections | P (extract of the authors' institutional full text, abstract and recommendations) | Confirmed; the authors also recommend the randomization test where applicable | Used in Section 12, activity 2 |
| SRC-067 (Voorhees and Buckley) | Error rates depend on the number of topics and the observed difference | A (NIST abstract) | Confirmed | Used in Section 12, activity 6 |
| SRC-068 (Buckley and Voorhees) | Standard measures not robust to substantially incomplete judgments; new measure (bpref) correlated with existing measures under complete judgments | P (extract of the full text) and A (NIST abstract) | Confirmed | Used in Section 12, activity 2 |
| SRC-069 (Hayes and Krippendorff) | Krippendorff's alpha proposed as the standard reliability measure | A (publisher abstract; author manuscript extract) | Confirmed; the 0.67 threshold is not from this source | Section 12 labels 0.67 as a project planning value |
| SRC-087 (CPMP/EWP/482/99) | Non-inferiority shown when the two-sided 95% interval lies entirely to the right of −Δ | P (PMC full-text extract) | Confirmed. New finding: the EMA guideline page states that this guidance is superseded by the guideline on non-inferiority and equivalence comparisons in clinical trials (SRC-088 recorded it as a draft in consultation) | Section 12 cites CPMP (2000) as the source of the criterion, states that EMA lists it as superseded, and requires a check against the current guideline before the protocol freeze (ISS-053) |
| SRC-089 (Holm) | Sequentially rejective procedure with a prescribed multiple level of significance | P (extract of the article's first page) | Confirmed | Used in Section 12, activity 2 |
| SRC-090 (Clopper and Pearson) | Confidence limits for a binomial proportion | Not re-checked (A from S07) | Unchanged | Method citation only; no figure from the source |

Not re-checked in S08 (unchanged depth; ISS-029 remains open for S09): vendor pages SRC-040 to SRC-050 (Section 9; ISS-032 asks for a re-read before submission), model cards SRC-037 and SRC-075 to SRC-077, EPO documentation SRC-070 to SRC-073, Pyserini SRC-078, Faiss SRC-086, and the method sources SRC-001, SRC-006 to SRC-008, SRC-012, SRC-025, SRC-026, SRC-027 (bibliographic only), SRC-034, SRC-035, SRC-036, SRC-055. Their statements in the master are the same statements recorded in S02 to S07.

Quantitative statements in the master and their basis: margins 0.05 and 0.10, 60 test queries, 30 need statements, ten development statements, 20% double judging, ten sampled pool-absent queries, depth 50, 200-item exhaustive limit, alpha 0.67, 5-second response time and corpus brackets are planning values (labelled as such); 4.1 GB is arithmetic (10^6 × 1,024 × 4 bytes; recomputed by the S08 script); 256 word pieces, 512 tokens and 8,192 tokens are model-card statements (S05/S07); Pyserini 2.4.0, Python 3.12 and Java 21 are package-page statements (S07); ten searches per minute is the EPO fair-use charter statement (S05); 2,004 person-hours and the activity figures are the S06 provisional estimates (recomputed by the S08 script).

## Pass B. Assembly map (scripted structure, self-reported content)

| Section | Source of the text | Change in assembly |
|---|---|---|
| 1 | Section 11 row 1 title (DRAFT_SEC11, DEC-028) | Title entered |
| 2, 3, 18 | REF-02 | `[LOCAL COMPLETION ONLY]` |
| 4 | DRAFT_SEC13 total | Duration and final effort `[OPEN — S10]`; provisional figure referenced |
| 5 | DRAFT_SEC05 v0.2 | Comparator counts restated against the Section 9 rows (three in Section 9 plus two further products for duplicate suggestion; three in Section 9 for scouting); TRL mapping attributed to the sponsor form |
| 6 | New in S08, from REF-01 §4–§7, §15, CLM-005, CLM-006, CLM-013, CLM-015, CLM-017 (qualitative), CLM-020, CLM-025, CLM-031, CLM-034, CLM-046 | Drafted |
| 7 | DRAFT_SEC07 v0.3 | ISS-052 correction (third objective); IDs removed |
| 8 | DRAFT_SEC08 v0.4 | ISS-052 correction (feature 4, specification 5); renumbered (mapping below); MS-07 and MS-09 moved to one sentence as out-of-scope; planning values paragraph added |
| 9 | S03_SECTION9_COMPARISON v2.0 | Rows 1–6 as provisional selection (ISS-030); patent rows 7–8 described in prose only; PQAI organization descriptor reduced to what T2 evidence supports (the T3 origin statement dropped) |
| 10, 14, 15 | REF-02 | Placeholders; Section 15 names four cost items the method creates, without quantities or amounts |
| 11 | DRAFT_SEC11 v0.2 | Duration cells `[OPEN — S10]`; wording edits |
| 12 | DRAFT_SEC12 v0.1 | ISS-052 correction (intro branches, activity 1 disclosure status, activity 4 rewritten); bracketed IDs removed; author–year citations added; CPMP supersession note; alpha 0.67 labelled |
| 13 | DRAFT_SEC13 v0.2 | Activity 1 and 4 key tasks and activity 4 deliverable name disclosure clearance; effort cells marked provisional; IDs removed |
| 16 | Section 13 | Titles and provisional effort copied; months, costs and weights `[OPEN — S10]` / local |
| 17 | S05_FEASIBILITY_AND_RISKS RSK-01 to RSK-14 | 14 rows in the form's four columns; timeline and financial rows point to S10 |
| 19 | New | Status-of-statements paragraph; reference list (every entry traceable to 02_SOURCE_LOG) |
| 20 | REF-02 attachment categories | Status column `[LOCAL COMPLETION ONLY]` |

**Identifier mapping (Section 8).** Features: 1 = old 1; 2 = old 2; 3 = old 4; 4 = old 5; 5 = old 7; 6 = old 8; 7 = old 9. Specifications: 1 = MS-01; 2 = MS-02; 3 = MS-03; 4 = MS-04; 5 = MS-05; 6 = MS-06; 7 = MS-08; 8 = MS-10. MS-07 and MS-09 remain defined in `S05_EVALUATION_DESIGN` and are not part of the funded scope. Requirement references: "Requirement 1" to "Requirement 4" = R1 to R4; "information security constraint" = C2; "extensibility constraint" = C1; "evaluator guidance on later learning" = C3.

**Table structures (scripted).** Every table in Sections 5, 9, 10, 11, 13, 14, 15, 16, 17 and 20 keeps the REF-02 header row verbatim, including column order, and no column or row label was added or removed. Sections 8 and 12 contain project tables; REF-02 asks Section 8 for a table of measurable specifications without giving a schema, and gives Section 12 no table. The native Word template was not inspected; layout and typography are pending local finalization (ISS-021).

## Pass C. Language and argument (self-reported)

Applied once to the assembled text, with `03_STYLE_GUIDE` §4 patterns as diagnostics. Representative changes, all of which keep the technical meaning:

| Pattern found | Example before | After |
|---|---|---|
| Working IDs in prose | "…stored in the platform [R1]." | IDs removed; the requirement named in words where needed |
| Unexplained jargon for a proposal reader | "Track P", "Track S" | "substitute-data track", "sponsor-data track" |
| Source evaluative word repeated as the project's own | "robust baseline" | "competitive baseline", attributed |
| Ambiguous authority for a threshold | "if alpha stays below 0.67 [PV-05]" | "…0.67 is a planning value set by the project" |
| Unattributed method choice | "paired bootstrap, sign-flip randomization test" | Reason given with Smucker et al. (2007) |
| Benefit wording | Section 6 not yet drafted | Benefits stated once as the sponsor's expectations and as untested |
| Long nominal phrases | "the R1 display threshold and the R2 'no example above threshold' signal" | "the display threshold for similar submissions and the 'no example above threshold' signal for solution examples" |

The scripted inflated-language scan (S07 pattern list) finds no hit in the master text; one hit is the title of a cited paper in Section 19 and is recorded as a citation-title exemption by the S08 script.

## Pass D. Cross-section consistency and traceability

| Check | Method | Result |
|---|---|---|
| Section 12 activity headings = Section 13 titles = Section 16 titles, numbers 1–7, in order; same as the frozen S06 titles | Scripted | Pass |
| Section 13 effort = Section 16 effort = 2,004 (provisional) and Section 4 reference | Scripted | Pass |
| Section 1 title = Section 11 row 1 title | Scripted | Pass |
| Section 11 row 1 is the current project; later rows prospective | Scripted (row 1 label) and self-reported (wording) | Pass |
| Disclosure rule (ISS-052) stated in Sections 7, 8 (feature 4, specification 5), 12 (intro and activity 4), 13 (activity 4), 17 (risk 3); withdrawn phrasings absent | Scripted phrase checks; self-reported reading | Pass |
| Corrected S07 methodology: non-inferiority first, superiority "not required", "non-inferiority not established", margins 0.05/0.10 as planning values, pool-based absence, Holm, BM25 default rule | Scripted phrase checks; self-reported reading | Pass |
| Corrected R2: no approved internal collection assumed; source of every example stated | Scripted (withdrawn phrases absent) | Pass |
| Requirements traceability: R1 → Sections 7, 8 (features 1–2, spec 1), 12 (activities 3, 6); R2 → 7, 8 (features 1, 3, spec 2), 12 (2, 3, 6); R3 → 7, 8 (features 5–6, spec 4), 12 (1, 5); R4 → 7, 8 (feature 4, specs 3, 5), 12 (4); C1 → 8 (feature 7), 12; C2 → 8, 12 (1, 5), 19; C3 → 8 (feature 5), 11, 12 | Self-reported | Complete |
| Citations: every author–year citation in the body has a Section 19 entry; every DOI or URL in Section 19 appears in 02_SOURCE_LOG | Scripted | Pass |
| No team identities, allocations, final hours, rates, budgets, dates or local administrative details | Scripted placeholder checks; self-reported reading | Pass |
| No certification, proven accuracy, patentability, measured performance or superiority claim | Scripted word scan with negation context; self-reported reading | Pass |
| No promise of sponsor data, assessors, infrastructure or integration | Self-reported reading; Section 19 states each as a sponsor decision | Pass |

Effort note: the ISS-052 correction adds a disclosure-status field and a second check before the connector (activities 1, 4, 5). This is small relative to the activity estimates; the effect is left to the S10 recomputation and the provisional figures are unchanged.

## Pass E. Reviewer-focused completeness check (self-reported)

| Criterion | Status for the master | Note |
|---|---|---|
| RF-001 font and emphasis | SCHEDULED (local finalization) | No bold or decorative emphasis in inserted text (scripted); typography applied in the native template |
| RF-002 decoration and lists | ADDRESSED in Markdown | No paragraph-opening bullets in sections 1–20 (scripted); native-template check pending |
| RF-003 table integrity | ADDRESSED in Markdown; native template PENDING | REF-02 header rows verbatim (scripted); pixel-level layout not claimed |
| RF-004 prose quality | ADDRESSED for S08; S09 isolated review pending | Pass C |
| RF-005 continuity | ADDRESSED (durations S10) | Row 1 current project |
| RF-006 Section 12 mirrors Section 13 | ADDRESSED | Pass D |
| RF-007 activity plan | ADDRESSED (effort provisional) | Unchanged from S06/S07 |
| RF-008 to RF-010 team, budget, Gantt | SCHEDULED S10 | Placeholders only |
| RF-011 track versus maturity | ADDRESSED | Sections 1, 5, 7, 11 consistent |
| RF-012 superseded cost guidance | ADDRESSED | No default consulting or training line |
| QA-002 benefits as hypotheses | ADDRESSED | Sections 6, 12 limits, 19 |
| QA-005 comparators | ADDRESSED with conditions | Vendor statements only; no superiority claim; row selection ISS-030; vendor re-read ISS-032 |
| QA-009 risks and remaining fields | ADDRESSED for technical and data risks; timeline, financial and administrative fields S10 | Section 17 |

Draftable sections complete: 1, 5 to 9, 11 to 13, 17, 19. Partly draftable and filled as far as allowed: 4, 15, 16, 20. Reserved: 2, 3, 10, 14, 18 (local or S10).
