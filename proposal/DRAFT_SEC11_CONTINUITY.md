# DRAFT_SEC11_CONTINUITY

| Field | Value |
|---|---|
| Document ID | DRAFT_SEC11_CONTINUITY |
| Version | 1.0 |
| Status | SUPERSEDED |
| Stage | S10 |
| Date | 2026-11-21 |
| Depends on | F-11; RF-005; FX-07; C1; C3; CTX-03; CTX-08; CLM-011; ISS-001; DEC-029; S04_SCOPE_OPTIONS; S04_ARCHITECTURE |

- **SUPERSEDED (S10, DEC-039):** this draft is superseded by `proposal/IRAA_PROPOSAL_EN_MASTER`, which carries all S08–S10 corrections (including DEF-002 items). Kept unchanged below as the approved stage input; do not use it as proposal text.
- **Draft status:** technical part only; row 1 follows the planning scope approved in DEC-028 (narrowed Option B). Row 1 is the current project (RF-005). Durations are completed in S10 from Sections 13 to 16; cost cells are local completion. Later rows are prospective and conditional on the results of earlier rows and on sponsor decisions.

## 11. Project continuity and future stages

The current project ends with a laboratory prototype evaluated in a controlled environment. Three further stages would be needed to reach an assistant in operational use. Each depends on the results of the stage before it and on decisions the sponsor has not yet taken, so these rows are plans rather than commitments. The justification for funding the first stage now is that the sponsor's open questions on data, integration and data handling do not block a laboratory prototype, while the prototype's evaluation gives the sponsor measured evidence before committing to integration.

| Stage | Project title | Estimated duration (months) | Estimated cost (sponsor unit; local only) | High-level deliverable |
| --- | --- | --- | --- | --- |
| 1 (current project) | Design, Development and Testing of a Laboratory Prototype of an Intelligent Requirements Assessment Assistant | [OPEN — S10] | [LOCAL COMPLETION ONLY] | Laboratory prototype covering similarity search against stored submissions, identification of existing solution examples, external patent retrieval and assessor approval; evaluation and test reports; platform adapter specification |
| 2 | Pilot Integration of the Assessment Assistant with the Submission Platform | [OPEN — S10] | [LOCAL COMPLETION ONLY] | Pilot prototype connected to the platform through the specified adapter, used by assessors on incoming submissions in parallel with the existing process; pilot evaluation report |
| 3 | Operational Release with Learning from Approved Assessments | [OPEN — S10] | [LOCAL COMPLETION ONLY] | Operational version on sponsor infrastructure with write-back of approved outcomes, ranking improved from logged assessor decisions under assessor oversight, and support for further assessment steps |
| 4 | Adaptation for Organizations with Comparable Assessment Workflows | [OPEN — S10] | [LOCAL COMPLETION ONLY] | Configurable version and deployment guide for other organizations, if stages 2 and 3 show the assistant is useful |

Stage 2 depends on the sponsor providing a platform interface, accounts and a decision on whether submission text may leave its infrastructure. Stage 3 adds the capability suggested in the initial evaluation, improving later analyses from prior assessments; the current project prepares for it only by logging assessor decisions, and no stage removes the requirement for final human approval. Stage 4 follows the statement of need's note that other organizations with comparable workflows might use the solution if its usefulness is shown; no demand estimate exists for it.
