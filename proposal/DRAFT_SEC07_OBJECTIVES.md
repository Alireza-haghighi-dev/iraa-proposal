# DRAFT_SEC07_OBJECTIVES

| Field | Value |
|---|---|
| Document ID | DRAFT_SEC07_OBJECTIVES |
| Version | 0.3 |
| Status | APPROVED |
| Stage | S06 |
| Date | 2026-11-21 |
| Depends on | F-07; FX-06; R1–R4; C1; C3; ISS-001; ISS-002; ISS-003; ISS-004; ISS-005; ISS-012; ISS-037; DEC-029; DEC-033; AS-10; S04_ARCHITECTURE; S04_ASSUMPTIONS_AND_STANDARDS |

- **Draft status:** PROVISIONAL, written for the narrowed Option B (ISS-001 open; `S04_SCOPE_OPTIONS` §6). Revised in S04.1 for the corrected R2 and for optional functions. Objectives name deliverables only; work-package numbers are added after S06 so that every objective maps to a scheduled activity (FX-06); the mapping is in `S06_WORK_PACKAGES` §5. S06 gate (DEC-033): the walk-through and judging sentences were corrected so that no sponsor assessor availability is promised. Targets are set in S05; no figure appears here. Bracketed IDs are working references and are removed in S08.

## 7. Project objectives

The objective of the current project is to design, build and test a laboratory prototype of an assistant that prepares, for each submission to the sponsor's platform, an assessment record linking three kinds of related material, and that leaves every assessment decision with a human assessor. The prototype is evaluated in a controlled environment; it is not deployed on the live platform.

The first objective is a similarity function that compares each new submission with the submissions already stored in the platform [R1]. The prototype ranks earlier stored submissions and shows the passages or fields that make each one similar. Grouping the whole stored collection into likely duplicates is not part of the current project [DEC-028].

The second objective is a function that checks whether relevant existing solution examples can be identified for a submitted need [R2]. Which sources these examples should come from, and whether any of them can be made available to the project, has not been settled [ISS-003, ISS-037]. The function is therefore built so that a source can be connected without changing the rest of the prototype, and every example it shows states where it came from. If no source is confirmed during the project, the function is tested on substitute data and the results are reported as substitute-data results.

The third objective is retrieval of external patents, and of solution examples where a usable source is identified, for each submission [R4]. The results are stored in the assessment record with their source and retrieval date. No confidential submission text is sent to an external service without the required authorization; until that authorization is defined, the assessor reviews and approves the exact search text before it is sent [ISS-033, DEC-028].

The fourth objective is a review and approval workflow in which no assessment outcome becomes final without an assessor's approval [R3]. The assessor approves the record under their own account; a change after approval creates a new version that needs approval again; approved records are exported as reports. Mandatory labelling of each displayed candidate and generated summaries are not part of the current project [DEC-028].

The fifth objective is an evaluation of the prototype that states how well it performs and under what conditions. Retrieval quality is measured on a test set ordered by submission date and judged on a written grading guide by sponsor assessors if they can take part, and otherwise by project judges, with the judging group stated in every result [ISS-012, AS-10]. The workflow is tested against the approval rules. Sponsor assessor availability has not been confirmed; if assessors can take part, a structured walk-through of the review screens records how they use them, and the evaluation does not depend on it [T6.7]. The metrics and targets are listed in Section 8.

At project completion the following will exist: the prototype software with its source code and deployment instructions; a design specification including the interface for a later connection to the platform; the evaluation data protocol and test set, with any substitute data identified as such; test and evaluation reports; an information security risk assessment of the prototype's data flows, prepared to support the sponsor's own processes; and a log of assessor decisions in a format that a later stage can use.

The project works under these assumptions. Stored submissions are supplied as a sanitized file export, or a public substitute collection is used and labelled as such [ISS-002]. The prototype reads exported data only and does not write to the platform [ISS-008]. Submission text is processed within the controlled environment unless the sponsor allows external AI services [ISS-009]. The content of an assessment is configured from information the sponsor provides [ISS-005]. Learning from past assessments and integration with the live platform are not objectives of this project; they are described in Section 11.
