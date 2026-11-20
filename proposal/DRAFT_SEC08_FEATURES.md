# DRAFT_SEC08_FEATURES

| Field | Value |
|---|---|
| Document ID | DRAFT_SEC08_FEATURES |
| Version | 0.2 |
| Status | APPROVED |
| Stage | S04.1 |
| Date | 2026-11-20 |
| Depends on | F-08; R1–R4; C1; C2; QA-002; QA-004; ISS-001; ISS-003; ISS-009; ISS-010; ISS-037; DEC-029; S04_ARCHITECTURE; S04_DATA_FLOWS_AND_INTERFACES; S04_ASSUMPTIONS_AND_STANDARDS |

- **Draft status:** narrowed Option B, approved as the current planning scope (DEC-028). Feature numbers 3 and 6 were removed with grouping and summaries; the remaining numbers are kept until S08 renumbers. MS-07 and MS-09 apply only if a later decision brings summaries or mandatory labelling back into scope. The form asks design and prototyping projects for a table of measurable specifications and a separation between measurable specifications and functional features (REF-02 §8). The form gives no column schema for this table; the columns below are this project's. Metric choice, values and test conditions for MS-rows marked "S05" are set in S05; until then they are OPEN. MS-04 to MS-06 are pass/fail targets derived from R3 and the design, still to be tested.

## 8. Main features and general/technical specifications

The deliverable is a laboratory prototype of an assistant that supports assessors of platform submissions. It imports stored submissions from export files, connects to whichever solution-example sources the sponsor confirms, and prepares one assessment record per submission. The record links three result lists: earlier submissions similar to the new one, existing solution examples that may address it, and external patents or solution examples. Every listed item states its source. Each listed item is shown with the passages that connect it to the submission, before any score or summary. The assessor completes the assessment fields and approves the record; the prototype cannot approve a record or write an outcome by itself.

Functional features (observable, verified by demonstration and workflow tests):

| No. | Feature | Requirement |
| --- | --- | --- |
| 1 | Import of exported submissions and solution-example items, each tagged with its source and availability status, with an import report listing rejected rows | R1, R2 |
| 2 | Ranked list of earlier similar submissions for a new submission, with the matching passages or fields | R1 |
| 4 | Ranked existing solution examples for a submitted need, with supporting passages and the source of each item; any confirmed source can be connected through the import format or a connector | R2 |
| 5 | External patent search for a submission, with results stored together with source, date and terms note; assessor approval of the exact query text before any submission text leaves the environment, unless external disclosure is otherwise authorized | R4 |
| 7 | Assessment record with configurable assessment fields, approval history, a log of assessor decisions (no automatic retraining) and the versions of all models and indexes used; report export | R3, C3 |
| 8 | Role-based access and an append-only log of approvals and external queries | R3, C2 |
| 9 | Defined interfaces for adding external sources, retrieval models and assessment templates, and for a later platform connection | C1 |

Measurable specifications (targets to be tested; none is a measured result):

| No. | Specification | Metric and test condition | Target |
| --- | --- | --- | --- |
| MS-01 | Similar-submission retrieval quality | Ranking metric on a test set ordered by submission date, judged by assessors on a graded scale | S05 |
| MS-02 | Solution-example relevance | Relevance of top-ranked examples judged by assessors; on a confirmed source or on labelled substitute data, stated with the result | S05 |
| MS-03 | External prior-art relevance | Share of relevant items among top-ranked results on a judged sample | S05 |
| MS-04 | Approval enforcement | Workflow test of all state transitions: records reaching "approved" without an assessor approval event | 0 |
| MS-05 | External disclosure control (only if query approval is required) | Share of external queries with a logged assessor approval of the exact text sent | 100% |
| MS-06 | Record reproducibility | Share of approved records that store model, index, connector and template versions | 100% |
| MS-07 | Summary grounding (only if the summary feature is enabled) | Share of summary sentences supported by their cited passage, by automatic check and manual audit | S05 |
| MS-08 | Response time | Time from opening a submission to display of R1 and R2 results, at the corpus size agreed for testing | S05 |
| MS-09 | Evidence inspection (only if per-candidate labelling is selected) | Rate at which assessors keep the system's top candidate unchanged, compared with their judgments in the evaluation set | S05 |

The prototype is designed to support alignment with ISO/IEC 27001 and ISO/IEC 20000-1 through role-based access, audit logging, versioned components and a risk assessment of its data flows. It is not certified, and no conformity with either standard is claimed. Both standards set requirements for an organization's management system; which controls apply depends on the sponsor's scope, which has not been specified.
