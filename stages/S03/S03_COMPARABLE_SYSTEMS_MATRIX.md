# S03_COMPARABLE_SYSTEMS_MATRIX

| Field | Value |
|---|---|
| Document ID | S03_COMPARABLE_SYSTEMS_MATRIX |
| Version | 2.0 |
| Status | APPROVED |
| Stage | S04.1 |
| Date | 2026-11-20 |
| Depends on | S01_REQUIREMENTS_REGISTER; S01_RESEARCH_QUESTIONS (RQ-10, RQ-11); 02_SOURCE_LOG; 02_CLAIM_REGISTER; QA-005; RC-01 |

- **S04.1 status note (RC-01):** the S04 session set this file to APPROVED on the basis of an approval inferred from the wording of the owner's START_STAGE S04 instruction. That approval has not been recorded as an explicit owner decision, so the status was returned to SUBMITTED FOR GATE; the owner confirmed the approval in DEC-028 and the status is APPROVED. Reviewed S03 content: commit 6780335.
- **Reference point:** the final intended product, not the current-phase output (FX-10): an assistant that compares a submission with stored submissions (R1), checks whether relevant existing solution examples can be identified for the submitted need (R2, as corrected in S04.1, DEC-029), examines external patents and solution examples (R4), and leaves the final decision to an assessor (R3), designed for later extension (C1).
- **Evidence rule:** every vendor cell is a vendor statement (T2) found on the first-party page cited, read on 2026-11-20. It shows what the vendor says, not that the feature works as described or performs well (C4, QA-005).
- **Cell legend:** `VS` = VERIFIED as vendor statement (cited SRC). `ND` = not documented in the pages read; OPEN. ND does not mean the capability is absent. `S02` = evidence carried from S02 without re-research.

## 1. Named initiatives (RQ-10)

| Dimension (driver) | Wazoku | ITONICS | Brightidea | Wellspring |
|---|---|---|---|---|
| D1. Similar or duplicate submissions flagged (R1) | VS: admin setting shows links to potential duplicate Ideas while a user types the title of a new Idea (SRC-040). Fields compared and method: ND. | VS: AI "clusters similar ideas and flags duplicates" (SRC-045); "Duplicate hunt" before project approval and a uniqueness check before submission (SRC-044). Method: ND. | VS: Duplicate Checker shows possibly similar submissions while the form is filled in, limited to the same Initiative; admin toggle (SRC-046). Method, fields, threshold: ND. | ND on the Scout, evaluation and Accolade pages read (SRC-048, SRC-049, SRC-050). |
| D2. Match a submission to an internal collection of existing solutions or precedents (R2 as worded before S04.1; see the S04.1 note below the table) | ND. Jen searches platform content on request (SRC-041); no matching of a new Idea to a solution collection is described. | VS, partial: Prism links "external intelligence, internal portfolio data" and "highlights potential connections between related elements" (SRC-044). No precedent-matching workflow described. | ND (SRC-047). | ND on the pages read (SRC-048, SRC-050). |
| D3. Human decision and review controls (R3) | VS, partial: Jen's evaluation output is a score that "supports evaluation" (SRC-041). On the challenge marketplace, Seeker organizations evaluate closed Challenges (SRC-043). Final-decision design: ND. | VS: a reviewer can check each AI-proposed change or set it to auto-apply; human ratings shown next to AI evaluations, disagreement flagged for discussion; role-based access to AI features (SRC-044). | VS, partial: submitter reviews AI-drafted text before submitting; Scout company profiles reviewed before import (SRC-047). Assessment-decision controls: ND. | VS, partial: workflows for "approvals, reviews"; evaluation scorecards and Stage-Gate processes (SRC-050); built-in triage, technical-fit and market-readiness workflows (SRC-049). Who decides: ND. |
| D4. External patents and solution examples (R4) | VS, partial: Jen scouts companies and recommends organizations for Challenges (SRC-041); Wazoku acquired the Innocentive solver crowd in 2020 (SRC-042). Patent retrieval: ND. | VS: Prism can "cluster a competitor's recent patents" and AI agents "scan markets, patents, and startups" (SRC-044, SRC-045). Linking patents to a specific submission: ND. | VS, partial: Scout app searches the web for emerging-technology companies matching a described need; Project Room research covers "IP considerations" (SRC-047). Patent retrieval: ND. | VS: Scout searches patents (vendor states 90+ patent offices), publications, grants, startups and licensable technologies (SRC-048). Linking results to a submitted need: ND. |
| D5. AI-assisted evaluation or scoring | VS: Jen gives a score for coherence, relevance to Challenge requirements and innovation (SRC-041). | VS: Prism evaluates ideas against custom criteria and performs "first-pass screening" against the jury's criteria (SRC-044). | VS: ranking of Top Ideas by a proprietary formula over evaluation scores and engagement (SRC-047). Generated assessment: ND. | ND. |
| D6. Evidence shown with AI output (explanation, citations) | ND. | ND beyond paired human/AI ratings (SRC-044). | VS, partial: Scout returns "sourced" company profiles (SRC-047). | ND. |
| D7. Method or model disclosed | ND (SRC-040, SRC-041). | ND; models from "selected vendors", none named (SRC-044). | VS, partial: bring-your-own-model with named cloud model providers (SRC-047); retrieval method ND. | ND. |
| D8. Published accuracy or effectiveness evaluation | ND. | ND. | ND. | ND. A vendor speed figure exists (SRC-049) but has no method; excluded (§4). |
| D9. Data-control options | ND. | VS: no training on proprietary data without consent (SRC-044). | VS: bring-your-own-model keeps data "within your existing governance" (SRC-047). | ND. |

**S04.1 re-reading of D2 and D4 (no new research).** Row D2 tested the withdrawn reading of R2 (an approved internal collection). Under the corrected R2, the question is whether a product identifies existing solution examples for a described need. Read that way, the D4 cells already record vendor statements that qualify: Wazoku's Jen scouts companies (SRC-041), Brightidea's Scout app searches for companies matching a described need (SRC-047) and Wellspring Scout searches patents, startups and licensable technologies (SRC-048). None of the pages read attaches those results to the assessment of an individual submission (CLM-046).

**REF-01 §10 wording against the evidence (CLM-001 to CLM-004):**

| Claim | What the vendor pages support | What remains unverified | New status |
|---|---|---|---|
| CLM-001 Wazoku | Challenge-based idea collection, duplicate suggestion, AI-supported evaluation score (SRC-040, SRC-041); external solver crowd (SRC-042) | "Prioritization" as a distinct function | VERIFIED IN PART (vendor statement) |
| CLM-002 ITONICS | Idea management with similarity detection and AI evaluation; trend radar and market or patent scouting (SRC-044, SRC-045) | "Opportunity identification" beyond the vendor's generated "market opportunity elements" | VERIFIED IN PART (vendor statement) |
| CLM-003 Brightidea | Idea collection with duplicate checking; evaluation scores used in ranking (SRC-046, SRC-047) | Process-management depth not examined | VERIFIED IN PART (vendor statement) |
| CLM-004 Wellspring | Technology discovery across patents, publications, grants and startups (SRC-048); evaluation workflows (SRC-049, SRC-050) | "Commercialization-opportunity analysis" and "industry–research connections" not examined on a first-party page | VERIFIED IN PART (vendor statement) |

## 2. Further comparators (RQ-11)

| System | Type | D1 (R1) | D2 (R2) | D3 (R3) | D4 (R4) | D7 method | D8 evaluation |
|---|---|---|---|---|---|---|---|
| IdeaScale duplicate detection | Commercial idea-management feature | VS: flags potential duplicates in the campaign while title or description is typed; moderators see similarity percentages and a side-by-side view with an AI-generated explanation of why ideas were flagged (SRC-051) | ND | VS, partial: comparison supports "a quick, informed decision"; no merge-approval step described (SRC-051) | ND | ND ("AI analysis") | ND |
| ServiceNow Innovation Management, Predictive Intelligence | Commercial platform feature | VS: trained "Similarity" solution suggests related ideas from Title and Description during submission and in the portal (SRC-052) | ND | ND | ND | VS, partial: supervised similarity solution that must be trained (SRC-052) | ND |
| PQAI | Open-source prior-art search engine | — | — | ND | VS: takes a plain-language invention description and returns similar patents and other technical literature; ML models trained on past patent examination records; MIT licence; API (SRC-053). Initiated by AT&T and a regional IP alliance (SRC-054, T3) | VS, partial: architecture and code public (SRC-053) | ND in the pages read |
| SOLVENT (Chan et al., 2018) | Peer-reviewed research system | — | VERIFIED (SRC-055): human annotations of purpose and mechanism used to find analogous research papers | VERIFIED (SRC-055): mixed-initiative design; experts judged usefulness | — | VERIFIED (SRC-055) | VERIFIED (SRC-055): found more analogies than baseline IR approaches |
| Idea-relationship analysis (SRC-013); novelty detection in idea spaces (SRC-014); analogy mining (SRC-016); AI idea screening (SRC-017) | Research | S02: duplicate detection is common in idea management; richer relation types proposed (CLM-018) | S02: problem–solution matching evidence is thin (CLM-019) | S02: model screened out weak ideas but did not match experts in picking the best (CLM-023) | — | S02 | S02 |

The S02 lead "corporate crowdsourcing platform whose contest data underlies SRC-017" was not resolved: the SRC-017 abstract read in S02 does not name the platform, and no first-party source was found. It is dropped as a comparator.

## 3. Findings

| No. | Finding | Label |
|---|---|---|
| 3.1 | Submission-time duplicate suggestion is documented by three of the four named vendors (Wazoku, ITONICS, Brightidea; not found on the Wellspring pages read) and by IdeaScale and ServiceNow. Only ServiceNow names the input fields and the model type; only IdeaScale shows an explanation to moderators. | VERIFIED (SRC-040, SRC-044 to SRC-046, SRC-051, SRC-052), vendor statements |
| 3.2 | *Revised S04.1.* Three named vendors document scouting for existing companies, technologies or patents that match a described need, which falls under the corrected R2. None of the pages read links scouting results to the assessment record of a specific submission. (The S03 finding about an "approved collection of existing solutions or precedents" tested a reading of R2 that DEC-029 withdrew.) | VERIFIED as vendor statements (SRC-041, SRC-047, SRC-048); linkage OPEN (CLM-046) |
| 3.3 | External technology and patent search exists as a separate scouting module (Wellspring Scout, ITONICS Prism, Brightidea Scout app); none of the pages read links scouting results to the assessment record of a specific submission. | VERIFIED for the modules (SRC-044, SRC-047, SRC-048); linkage OPEN |
| 3.4 | AI scoring of ideas is documented by Wazoku and ITONICS; ITONICS documents per-change reviewer approval and an auto-apply option. An auto-apply option would conflict with R3 if applied to assessment outcomes. | VERIFIED (SRC-041, SRC-044); conflict statement is our reading of R3, PROPOSED |
| 3.5 | No comparator page read reports a measured accuracy of its similarity, scoring or scouting functions. Superiority statements against any comparator are therefore unsupported (QA-005). | OPEN (CLM-034) |
| 3.6 | PQAI shows that natural-language-to-patent retrieval can be integrated through an open API and self-deployed code; its training data are patent examination records, not need or challenge submissions. | VERIFIED (SRC-053); transfer to submissions is an ASSUMPTION to test (ISS-028) |
| 3.7 | Public idea datasets exist (SRC-063: about 620 student-generated ideas; SRC-013 annotated relationships in an idea dataset from an online public system), but no public benchmark of organizational need or challenge submissions was found in S03 either. | VERIFIED for the datasets; benchmark absence OPEN (CLM-025) |

## 4. Marketing claims recorded but not used

| Claim (paraphrased) | Source | Reason excluded |
|---|---|---|
| Customers reduced evaluation time by 40% | SRC-049 | No baseline, sample or method stated |
| AI flags the 15–20% of projects that are stalling | SRC-044 | No method or validation stated |
| Scout record counts (400M+ records, 145M+ publications, 2M+ startups) | SRC-048 | Vendor-stated volumes; may be cited only as "the vendor states", never as coverage evidence |
| Solver network size and success rates | Press and encyclopedia pages seen during search, not logged | Not first-party; not needed for Section 9 |

## 5. Implications for S04–S05 (PROPOSED)

| No. | Implication | Feeds |
|---|---|---|
| 5.1 | *Revised S04.1.* R1 is a documented market feature, and solution scouting (corrected R2) is documented as a separate module. The design position is to bring R1, R2 and R4 results for one submission into a single assessor-approved record with the evidence shown for each result (CLM-040). It is a position to evaluate, not a claimed advantage. | Section 6, 9; S04 |
| 5.2 | Show the reason for each similarity flag (matched passages or fields), as IdeaScale describes, and keep the decision with the assessor; no auto-apply path for assessment outcomes. | R3; S04 review-screen design; CLM-028 |
| 5.3 | Treat external search as a source connector (patents first, using an API such as PQAI's or an official patent-office service), with results stored against the submission. Access terms are ISS-006 and RQ-14. | R4; S04–S05 |
| 5.4 | Because comparators publish no accuracy figures, the proposal can differ by stating how the assistant will be measured (time-ordered, assessor-judged test set; CLM-027), not by claiming better results. | QA-002, QA-005; S05 |
