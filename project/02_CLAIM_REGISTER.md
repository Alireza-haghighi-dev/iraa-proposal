# 02_CLAIM_REGISTER

| Field | Value |
|---|---|
| Document ID | 02_CLAIM_REGISTER |
| Version | 2.0 |
| Status | APPROVED |
| Stage | S02 |
| Date | 2026-11-20 |
| Depends on | REF-01; REF-02; 02_SOURCE_LOG; 02_SOURCE_LOG (SRC-001 to SRC-039) |

- **Purpose:** Tracks every claim that the proposal may rely on, its evidence and its permitted use. Seeded in S01 with claims in the reference documents that must not be used as verified facts.

## Status key

`VERIFIED` (supported by a logged source) · `SOURCE CLAIM — UNVERIFIED` (stated in a reference document, not independently checked) · `HYPOTHESIS` (expected effect to be tested) · `PROPOSED` (team proposal) · `OPEN`

## Claims

| ID | Claim | Origin | Status | Permitted use now | Verification route | Target stage |
|---|---|---|---|---|---|---|
| CLM-001 | Wazoku provides innovation management and collection, assessment and prioritization of organizational challenges and ideas. | REF-01 §10 | SOURCE CLAIM — UNVERIFIED | Candidate comparator only | Vendor primary documentation (T2), labelled as vendor statement | S03 |
| CLM-002 | ITONICS provides innovation management, technology-trend analysis and opportunity identification. | REF-01 §10 | SOURCE CLAIM — UNVERIFIED | Candidate comparator only | As CLM-001 | S03 |
| CLM-003 | Brightidea supports idea collection, evaluation and management of organizational innovation processes. | REF-01 §10 | SOURCE CLAIM — UNVERIFIED | Candidate comparator only | As CLM-001 | S03 |
| CLM-004 | Wellspring supports technology discovery, commercialization-opportunity analysis and industry–research connections. | REF-01 §10 | SOURCE CLAIM — UNVERIFIED | Candidate comparator only | As CLM-001 | S03 |
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
| CLM-025 | No public benchmark of organizational need/challenge submissions was found in S02. | S02 searches (documented in S02_PLAN) | OPEN — negative search result | May be stated as "none identified in our search", not as "none exists" | Re-check in S03 | S03 |
| CLM-026 | Multi-stage retrieval (lexical and dense candidates, fusion, optional re-ranking) is a candidate design for R1 and R2. | S02_RESEARCH_SYNTHESIS §3 | PROPOSED | S04–S05 design input only | S05 evaluation | S05 |
| CLM-027 | A time-ordered, assessor-judged, graded test set with measured inter-assessor agreement is a candidate evaluation design. | S02_RESEARCH_SYNTHESIS §3 | PROPOSED | S05 design input only | S05 | S05 |
| CLM-028 | Evidence-first review screens with cognitive-forcing elements are a candidate design for R3. | S02_RESEARCH_SYNTHESIS §3 | PROPOSED | S04 design input only | S04 | S04 |
