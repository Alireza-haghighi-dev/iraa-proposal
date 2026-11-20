# DRAFT_SEC07_OBJECTIVES

| Field | Value |
|---|---|
| Document ID | DRAFT_SEC07_OBJECTIVES |
| Version | 0.1 |
| Status | SUBMITTED FOR GATE |
| Stage | S04 |
| Date | 2026-11-20 |
| Depends on | F-07; FX-06; R1–R4; C1; C3; ISS-001; ISS-002; ISS-003; ISS-004; ISS-005; S04_ARCHITECTURE; S04_ASSUMPTIONS_AND_STANDARDS |

- **Draft status:** provisional, written for Option B (ISS-001 open). Objectives name deliverables only; work-package numbers are added after S06 so that every objective maps to a scheduled activity (FX-06). Targets are set in S05; no figure appears here. Bracketed IDs are working references and are removed in S08.

## 7. Project objectives

The objective of the current project is to design, build and test a laboratory prototype of an assistant that prepares, for each submission to the sponsor's platform, an assessment record linking three kinds of related material, and that leaves every assessment decision with a human assessor. The prototype is evaluated in a controlled environment; it is not deployed on the live platform.

The first objective is a working similarity function for submissions already stored in the platform [R1]. For a new submission, the prototype ranks earlier stored submissions and shows the passages or fields that make each one similar. In a batch mode it proposes groups of stored submissions that may duplicate or overlap each other, which an assessor confirms or rejects. Both readings of the requirement are covered unless the sponsor limits it to one [ISS-004].

The second objective is retrieval of relevant solutions or precedents from the approved internal collection [R2]. The statement of need does not establish whether this collection exists in machine-readable form or whether the project may use it [ISS-003]. The prototype component is therefore built so that it works on any collection supplied in the import format; if the sponsor's collection is not available during the project, the component is tested on a substitute collection and reported as such.

The third objective is retrieval of external patents, and of solution examples where a usable source is identified, for each submission [R4]. The assessor reviews and may edit the search text before it is sent to any external service, and the results are stored in the assessment record with their source and retrieval date.

The fourth objective is a review and approval workflow in which no assessment outcome becomes final without an assessor's approval [R3]. The assessor labels each displayed candidate before submitting the record, accepts or rejects any generated summary, and approves the record under their own account. Approved records are exported as reports; changes after approval create a new version that needs approval again.

The fifth objective is an evaluation of the prototype that states how well it performs and under what conditions. Retrieval quality is measured on a test set ordered by submission date and judged by assessors; the workflow is tested against the approval rules; and a structured walk-through with assessors checks whether the review screens lead them to inspect the evidence. The metrics and targets are listed in Section 8.

At project completion the following will exist: the prototype software with its source code and deployment instructions; a design specification including the interface for a later connection to the platform; the evaluation data protocol and test set (or a description of the substitute data used); test and evaluation reports; an information security risk assessment of the prototype's data flows, prepared to support the sponsor's own processes; and a log of assessor decisions in a format that a later stage can use.

The project works under these assumptions. Stored submissions are supplied as a sanitized file export, or a public substitute collection is used and labelled as such [ISS-002]. The prototype reads exported data only and does not write to the platform [ISS-008]. Submission text is processed within the controlled environment unless the sponsor allows external AI services [ISS-009]. The content of an assessment is configured from information the sponsor provides [ISS-005]. Learning from past assessments and integration with the live platform are not objectives of this project; they are described in Section 11.
