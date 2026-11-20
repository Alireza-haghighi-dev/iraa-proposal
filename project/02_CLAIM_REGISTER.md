# 02_CLAIM_REGISTER

| Field | Value |
|---|---|
| Document ID | 02_CLAIM_REGISTER |
| Version | 1.2 |
| Status | APPROVED |
| Stage | S01 |
| Date | 2026-11-20 |
| Depends on | REF-01; REF-02; 02_SOURCE_LOG |

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
