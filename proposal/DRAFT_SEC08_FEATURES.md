# DRAFT_SEC08_FEATURES

| Field | Value |
|---|---|
| Document ID | DRAFT_SEC08_FEATURES |
| Version | 0.3 |
| Status | SUBMITTED FOR GATE |
| Stage | S05 |
| Date | 2026-11-20 |
| Depends on | F-08; R1–R4; C1; C2; QA-002; QA-004; ISS-001; ISS-003; ISS-009; ISS-010; ISS-037; DEC-029; S04_ARCHITECTURE; S04_DATA_FLOWS_AND_INTERFACES; S04_ASSUMPTIONS_AND_STANDARDS; S05_EVALUATION_DESIGN; ISS-039 |

- **Draft status:** narrowed Option B, approved as the current planning scope (DEC-028). Feature numbers 3 and 6 were removed with grouping and summaries; the remaining numbers are kept until S08 renumbers. MS-07 and MS-09 apply only if a later decision brings summaries or mandatory labelling back into scope. The form asks design and prototyping projects for a table of measurable specifications and a separation between measurable specifications and functional features (REF-02 §8). The form gives no column schema for this table; the columns below are this project's. S05 set the metric, test condition and target of every active row (`stages/S05/S05_EVALUATION_DESIGN` §4, §8). All targets are untested. Retrieval targets are stated relative to a lexical baseline because no defensible absolute value exists before evaluation; absolute floors are fixed after a pilot (PV-11). Numeric planning values (PV-07, PV-09) await owner confirmation (ISS-039). Every result will be reported with the data track behind it: sponsor data (Track S) or substitute data (Track P). MS-10 was added in S05 to make source and evidence attribution testable.

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
| MS-01 | Similar-submission retrieval quality | nDCG@10 on a test set ordered by submission date, graded by judges on a four-level scale; compared with a BM25 baseline by a paired randomization test | Higher nDCG@10 than the BM25 baseline, with the 95% interval of the difference above zero; absolute floor fixed after the pilot |
| MS-02 | Solution-example relevance | Share of the first five examples shown that address at least part of the need (P@5), judged per registered source; source type stated with the result; rate of wrongly reporting "no example found" also reported | Higher P@5 than the BM25 baseline on each source, same criterion; absolute floor fixed after the pilot |
| MS-03 | External prior-art relevance | Share of need statements with at least one relevant patent in the top 10 (success@10), for assessor-edited automatic queries compared with unaided keyword queries, on a judged sample | Not lower than unaided keyword queries |
| MS-04 | Approval enforcement | Workflow test of all state transitions and roles: records reaching "approved" without an assessor approval event; changes to approved records that bypass re-approval | 0 |
| MS-05 | External disclosure control (only if query approval is required) | Share of external queries with a logged assessor approval of the exact text sent | 100% |
| MS-06 | Record reproducibility | Share of approved records that store model, index, connector and template versions | 100% |
| MS-07 | Summary grounding (only if the summary feature is enabled) | Share of summary sentences supported by their cited passage, by automatic check and manual audit | Not set: feature outside the funded scope |
| MS-08 | Response time | 95th-percentile time from opening a submission to display of R1 and R2 results, at each corpus size agreed for testing, on the reference environment | ≤ 5 s (planning value, to be confirmed) |
| MS-09 | Evidence inspection (only if per-candidate labelling is selected) | Rate at which assessors keep the system's top candidate unchanged, compared with their judgments in the evaluation set | Not set: control outside the funded scope |
| MS-10 | Source and evidence attribution | Share of listed items (similar submissions, solution examples, external results) that show source type, availability status, terms note and an evidence passage | 100% |

The prototype is designed to support alignment with ISO/IEC 27001 and ISO/IEC 20000-1 through role-based access, audit logging, versioned components and a risk assessment of its data flows. It is not certified, and no conformity with either standard is claimed. Both standards set requirements for an organization's management system; which controls apply depends on the sponsor's scope, which has not been specified.
