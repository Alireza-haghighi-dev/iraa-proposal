# 02_CLAIM_REGISTER

| Field | Value |
|---|---|
| Document ID | 02_CLAIM_REGISTER |
| Version | 3.0 |
| Status | SUBMITTED FOR GATE |
| Stage | S03 |
| Date | 2026-11-20 |
| Depends on | REF-01; REF-02; 02_SOURCE_LOG (SRC-001 to SRC-063); S03_COMPARABLE_SYSTEMS_MATRIX; S03_PRIOR_ART_REGISTER |

- **Purpose:** Tracks every claim that the proposal may rely on, its evidence and its permitted use. Seeded in S01 with claims in the reference documents that must not be used as verified facts.

## Status key

`VERIFIED` (supported by a logged source) · `VERIFIED (vendor statement)` / `VERIFIED IN PART (vendor statement)` (a T2 source confirms the vendor says this; not evidence that the feature works or performs) · `SOURCE CLAIM — UNVERIFIED` (stated in a reference document, not independently checked) · `HYPOTHESIS` (expected effect to be tested) · `PROPOSED` (team proposal) · `OPEN`

## Claims

| ID | Claim | Origin | Status | Permitted use now | Verification route | Target stage |
|---|---|---|---|---|---|---|
| CLM-001 | Wazoku provides innovation management and collection, assessment and prioritization of organizational challenges and ideas. | REF-01 §10 | VERIFIED IN PART (vendor statement): SRC-040, SRC-041, SRC-042; "prioritization" not separately confirmed | Section 9 as "the vendor documents …" | Re-check pages before submission (ISS-032) | S08 |
| CLM-002 | ITONICS provides innovation management, technology-trend analysis and opportunity identification. | REF-01 §10 | VERIFIED IN PART (vendor statement): SRC-044, SRC-045 | As CLM-001 | As CLM-001 | S08 |
| CLM-003 | Brightidea supports idea collection, evaluation and management of organizational innovation processes. | REF-01 §10 | VERIFIED IN PART (vendor statement): SRC-046, SRC-047 | As CLM-001 | As CLM-001 | S08 |
| CLM-004 | Wellspring supports technology discovery, commercialization-opportunity analysis and industry–research connections. | REF-01 §10 | VERIFIED IN PART (vendor statement): SRC-048, SRC-049, SRC-050; commercialization analysis and industry–research connections not confirmed | As CLM-001 | As CLM-001 | S08 |
| CLM-005 | Growth in platform records beyond the usual volume increases review time and causes an assessment backlog. | REF-01 §4 | SOURCE CLAIM — UNVERIFIED (no figures) | Problem statement attributed to the sponsor | Baseline data from owner (ISS-011, ISS-023) | S05 |
| CLM-006 | The assistant will improve review speed and accuracy, coordination and consistency of organization, and reduce errors. | REF-01 §6, §15 | HYPOTHESIS | Only as expected benefits to be tested | Evaluation design with baseline (QA-002) | S05 |
| CLM-007 | The solution may be applicable to other organizations with comparable workflows. | REF-01 §5 | HYPOTHESIS | Only as conditional future possibility | None in current project; Section 11 | S04 / S08 |
| CLM-008 | ISO/IEC 20000 and ISO/IEC 27001 apply as constraints. | REF-01 §8 | SOURCE CLAIM — scope unspecified | Name the standards; no conformity or certification claim | Owner clarification (ISS-010); official standards-body descriptions (T1) | S04 |
| CLM-009 | Form maturity mapping: feasibility ≈ TRL 3 or below; technology development ≈ TRL 4–6; product development ≈ TRL 7 or above. | REF-02 §5 | SOURCE CLAIM — sponsor form mapping, not validated for this project | Use the form's categories; do not claim a TRL as achieved | Owner decision on maturity (ISS-001) | S04 |
| CLM-010 | The illustration in the original statement depicts the product concept. | REF-01 §14 | Conceptual only | Must not be used as evidence of a working product | — | — |
| CLM-011 | Future stages could use prior assessments to improve subsequent analyses. | REF-01 §17 | PROPOSED (evaluator suggestion, future capability) | Section 11 future phase and extensibility design only; not current-project autonomous training | Design note in S04 | S04 |
| CLM-012 | An approved internal collection of solutions or precedents exists as a populated dataset that the assistant and this project can use. | Implied by the wording of REF-01 §7.2 (R2); not stated as fact | OPEN — not established | Must not be assumed in architecture, evaluation, objectives or proposal text | Owner clarification (ISS-003, ISS-002) | S04–S05 |
| CLM-013 | Across heterogeneous zero-shot benchmarks, BM25 remained competitive with neural retrievers; re-ranking and late-interaction models achieve the best average results at high computational cost. | SRC-002 | VERIFIED | Background for Sections 9 and 12; no transfer claim | Full-text check in S08 Pass A | S08 |
| CLM-014 | Dense retrievers trained on in-domain pairs outperformed BM25 by 9–19 points (top-20 accuracy) in open-domain QA. | SRC-004 | VERIFIED | Background only; conditional on training data (ISS-002) | As above | S08 |
| CLM-015 | No single text-embedding method dominates all tasks in MTEB. | SRC-005 | VERIFIED | Justifies comparing models in S05 | As above | S08 |
| CLM-016 | For lexical+semantic fusion, RRF is sensitive to its parameters and a tuned convex combination outperformed it with few labelled examples. | SRC-008; SRC-007 for RRF origin | VERIFIED | Justifies comparing fusion methods in S05 | As above | S08 |
| CLM-017 | Classical evaluation of duplicate-report retrieval overestimated performance by a median of 17–42% versus a realistic, time-ordered evaluation. | SRC-010 | VERIFIED | Justifies time-ordered evaluation design | As above | S05 |
| CLM-018 | Duplicate detection is a common technique in idea management systems; richer relationship types than "duplicate" have been proposed. | SRC-013 | VERIFIED | Background for R1 and Section 9 | As above | S08 |
| CLM-019 | A review of NLP for innovation search identified only three studies on problem–solution matching. | SRC-015 | VERIFIED | Supports the statement that direct evidence for R2-type matching is limited | Confirm count in full text | S08 |
| CLM-020 | Automation bias causes omission and commission errors, affects experts and is not prevented by training or instructions. | SRC-022 | VERIFIED | Justifies R3 design measures beyond a final approval click | As above | S08 |
| CLM-021 | Explanations did not reduce overreliance on AI in a controlled study; cognitive-forcing designs did. | SRC-024 | VERIFIED | Input to S04 review-screen design | As above | S04 |
| CLM-022 | In a 2023 audit, about 51.5% of sentences from generative search engines were fully supported by citations and 74.5% of citations supported their sentence. | SRC-028 | VERIFIED | Justifies citation checks for generated summaries | As above | S04 |
| CLM-023 | In crowdsourcing contests, a model could screen out weak ideas but could not mimic experts in selecting the best. | SRC-017 | VERIFIED | Supports human final authority (R3) | As above | S08 |
| CLM-024 | Automatic patent retrieval performance is judged around average; interactive assistance for professionals is advocated. | SRC-019 | VERIFIED | Background for R4 scope | As above | S08 |
| CLM-025 | No public benchmark of organizational need/challenge submissions was found in S02 or S03. Public idea datasets exist (SRC-063; the annotated dataset in SRC-013) but contain ideas, not need or challenge submissions. | S02 and S03 searches (S02_PLAN, S03_PLAN) | OPEN — negative search result | May be stated as "none identified in our search", not as "none exists"; idea datasets only as proxies | S05 evaluation design (ISS-028) | S05 |
| CLM-026 | Multi-stage retrieval (lexical and dense candidates, fusion, optional re-ranking) is a candidate design for R1 and R2. | S02_RESEARCH_SYNTHESIS §3 | PROPOSED | S04–S05 design input only | S05 evaluation | S05 |
| CLM-027 | A time-ordered, assessor-judged, graded test set with measured inter-assessor agreement is a candidate evaluation design. | S02_RESEARCH_SYNTHESIS §3 | PROPOSED | S05 design input only | S05 | S05 |
| CLM-028 | Evidence-first review screens with cognitive-forcing elements are a candidate design for R3. | S02_RESEARCH_SYNTHESIS §3 | PROPOSED | S04 design input only | S04 | S04 |
| CLM-029 | Wazoku documents an admin setting that shows links to potential duplicate Ideas while a user types a new Idea title; the matching method is not documented. | SRC-040 | VERIFIED (vendor statement) | Section 9 comparison | Re-check before submission (ISS-032) | S08 |
| CLM-030 | Wazoku's Jen assistant is documented to give an evaluation-support score for coherence, relevance to Challenge requirements and innovation, and to scout companies (scouting in English only). | SRC-041 | VERIFIED (vendor statement) | Section 9 comparison | As CLM-029 | S08 |
| CLM-031 | ITONICS documents AI duplicate detection, first-pass screening against jury criteria, patent clustering, and reviewer approval of AI changes with an optional auto-apply mode. | SRC-044, SRC-045 | VERIFIED (vendor statement) | Section 9 comparison; R3 design contrast | As CLM-029 | S08 |
| CLM-032 | Brightidea documents a submission-time Duplicate Checker scoped to one Initiative, a Scout app that searches the web for companies matching a described need, and bring-your-own-model options. | SRC-046, SRC-047 | VERIFIED (vendor statement) | Section 9 comparison | As CLM-029 | S08 |
| CLM-033 | Wellspring documents Scout search over patents, publications, grants and startups, and evaluation scorecards and stage-gate workflows in Accolade; no AI assessment or duplicate detection is described on the pages read. | SRC-048, SRC-049, SRC-050 | VERIFIED (vendor statement) | Section 9 comparison | As CLM-029 | S08 |
| CLM-034 | None of the comparator pages read discloses an accuracy evaluation of its similarity, scoring or scouting functions, and none describes checking a new submission against an approved collection of existing solutions or precedents. | S03 reading of SRC-040 to SRC-052 | OPEN — negative reading result | "Not documented in the vendor's public material as of 2026-11-20"; never "does not exist" | Re-check before submission | S08 |
| CLM-035 | IdeaScale documents duplicate flags with similarity percentages and an AI-generated explanation for moderators; ServiceNow documents a trained similarity solution using idea Title and Description. | SRC-051, SRC-052 | VERIFIED (vendor statement) | Section 9 background; S04 review-screen design input | As CLM-029 | S04 |
| CLM-036 | PQAI is an MIT-licensed open-source prior-art search engine that takes plain-language descriptions and uses ML models trained on past patent examination records; it offers an API. | SRC-053 (origin: SRC-054) | VERIFIED (project statement) | Section 9; candidate R4 component or baseline | Licence and API terms in RQ-14 | S04–S05 |
| CLM-037 | SOLVENT combined human annotation of problem and mechanism with a computational model and found more analogies than baseline IR approaches; experts judged the analogies useful. | SRC-055 | VERIFIED | Section 9; R2/R3 design background | Full-text check in S08 Pass A | S08 |
| CLM-038 | Patents describe parts of the intended product: overlap alerts against stored internal disclosures with inventor-controlled access (US 8,943,033 B2); matching logged needs to a solutions database including patent documents (US 11,561,987 B1 family); committee voting on submitted ideas (CA 2588160). | SRC-056 to SRC-059 | VERIFIED | Section 9 prior-art statements only | Office-register re-check if used (ISS-030) | S08 |
| CLM-039 | The S03 prior-art scan found no record combining R1, R2, R4 and mandatory human approval of assessment outcomes in one system. | S03_PRIOR_ART_REGISTER §4 | OPEN — negative search result | "None identified in our scan"; no patentability or freedom-to-operate statement | Professional search if the owner requires it (ISS-031) | S08 |
| CLM-040 | The intended product's distinguishing point is linking R1, R2 and R4 results to one assessment record approved by an assessor, with evidence shown for each result and a project-run evaluation. | S03_COMPARABLE_SYSTEMS_MATRIX §5; S03_SECTION9_COMPARISON | PROPOSED | Sections 6 and 9 as a design position; no superiority claim (QA-005) | S05 evaluation design | S05 |
