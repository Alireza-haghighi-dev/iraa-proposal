# S04_ASSUMPTIONS_AND_STANDARDS

| Field | Value |
|---|---|
| Document ID | S04_ASSUMPTIONS_AND_STANDARDS |
| Version | 1.0 |
| Status | SUBMITTED FOR GATE |
| Stage | S04 |
| Date | 2026-11-20 |
| Depends on | C2; CLM-008; CLM-041; CLM-042; CLM-043; SRC-064; SRC-065; ISS-002; ISS-003; ISS-006 to ISS-010; ISS-023; ISS-033 to ISS-036 |

- **Purpose:** state the planning assumptions the architecture uses while owner decisions are open, and define what "alignment" with ISO/IEC 20000 and ISO/IEC 27001 can honestly mean for this project.
- **Labels:** AS rows are ASSUMPTION; each stays in force only until the linked issue is decided. Standards descriptions are VERIFIED at landing-page depth (SRC-064, SRC-065); the alignment mapping is PROPOSED.

## 1. Planning assumptions

| ID | Assumption | Linked issue | If the assumption fails |
|---|---|---|---|
| AS-01 | Evaluation and prototype data come from a sanitized export of stored submissions; if none can be released, from a public proxy collection labelled as such | ISS-002, ISS-028 | Proxy only: Section 8 targets apply to proxy data, and the proposal says so |
| AS-02 | The internal collection is treated as unavailable until the owner confirms its existence, format and permission to use it; FN-05 is built and tested on a proxy collection meanwhile | ISS-003, CLM-012 | If it exists and is released, FN-05 is re-evaluated on it; no other design change |
| AS-03 | The platform can produce a file export of submissions; no API is assumed; the prototype never writes to the platform | ISS-008 | No export at all: AS-01 proxy route; API available: IF-07 can move into scope only by owner decision |
| AS-04 | The prototype runs in an isolated, project-controlled or sponsor-provided environment with self-hosted retrieval models; no submission text goes to hosted AI services | ISS-009 | Hosted services allowed: AD-08 and hosted re-ranking become options, with the provider's terms recorded |
| AS-05 | Access uses project-managed test accounts with three roles (assessor, administrator, evaluator); no sponsor production accounts | ISS-035 | Sponsor accounts required: IF-08 federation becomes in scope |
| AS-06 | Submission language is unknown; S05 selects components that can be tested on the actual language once ISS-007 is answered | ISS-007, RQ-07 | Conditional RQ-07 is activated in S05 |
| AS-07 | Corpus size and submission rate are unknown; S05 sizes the prototype for ranges agreed with the owner | ISS-023, RQ-15 | Sizing revised |
| AS-08 | At least one patent source offers access terms that permit automated queries for this use; solution-example sources are added only if ISS-006 names one | ISS-006, RQ-14 | R4 is limited to assessor-run searches with results entered manually, and Section 8 records the limit |

## 2. Questions the owner is asked to answer

These are the open points that change the design. None asks for team, personal or financial information.

| Issue | Question |
|---|---|
| ISS-003 | Does an approved collection of solutions or precedents exist in machine-readable form, and may the project use it or a sample? |
| ISS-004 | Should R1 cover new-versus-stored search, grouping of the stored collection, or both? (Recommended: both, FN-03 and FN-04) |
| ISS-005 | What fields and outcome codes does a completed assessment currently contain? |
| ISS-007 | In which language or languages are submissions and the internal collection written? |
| ISS-008 | Can the platform export submissions to a file, and is there an API? |
| ISS-009 | May submission text be processed by externally hosted AI services, or must it stay in sponsor-controlled infrastructure? |
| ISS-010 | Does the C2 standards constraint mean design alignment, fitting into an existing certified management system, or certification? |
| ISS-033 | May assessor-approved query text be sent to external patent search services? |
| ISS-034 | Is one assessor's approval sufficient, or does the sponsor require a second approver? |
| ISS-035 | Which roles need accounts in the prototype, and must they use the sponsor's identity system? |
| ISS-036 | How long may imported submissions and cached external results be kept in the prototype environment, and how are they deleted at project end? |

## 3. ISO/IEC 27001 and ISO/IEC 20000-1: proposed alignment

**What the standards are (VERIFIED, landing-page depth).** ISO/IEC 27001:2022 (edition 3, published 2022-10) specifies requirements for establishing, implementing, maintaining and continually improving an information security management system within the context of the organization, including requirements for assessing and treating information security risks; the requirements are intended for all organizations, and excluding any requirement in Clauses 4 to 10 is not acceptable when an organization claims conformity (SRC-064; CLM-041). ISO/IEC 20000-1:2018 (edition 3, reviewed and confirmed in 2023, with Amendment 1:2024) specifies requirements for an organization to establish, implement, maintain and continually improve a service management system, covering the planning, design, transition, delivery and improvement of services (SRC-065; CLM-042).

**What follows for this project (PROPOSED interpretation, CLM-043).** Both standards set requirements for an organization's management system. A software prototype is not itself the object of conformity or certification. The proposal therefore cannot claim that the assistant is certified or compliant, and REF-01 confirms that the applicable controls and scope of conformity were not specified (C2). What the project can offer is design features that would make it easier for the sponsor to bring the assistant into the scope of its own management systems, if it has them (ISS-010). The proposal text should use "designed to support alignment with" and name the features.

The first row and the last two rows use terms from the verified scope text. The middle rows are the project's own PROPOSED reading of information-security concerns relevant to this prototype; they are not quoted from either standard.

| Area addressed | Proposed design feature | Component |
|---|---|---|
| ISO/IEC 27001: information security risk assessment and treatment | An information security risk assessment of the prototype's data flows and trust boundaries, delivered as a project document for the sponsor's own risk process | `S04_DATA_FLOWS_AND_INTERFACES` §4; S06 deliverable |
| Access to submission content (project reading) | Role-based access on every record operation; self-hosted default; assessor-approved external queries | AC-12, AD-09, CP-1 |
| Integrity and accountability of records (project reading) | Append-only audit log; approval bound to user identity; record versioning | AC-13, CP-5, CP-6 |
| Information sent to external parties (project reading) | Connector terms recorded per source; hosted services only after ISS-009 | AC-07, AD-08 |
| ISO/IEC 20000-1: transition and delivery of services | Versioned models, indexes and templates recorded in each record; documented release procedure for the prototype | AD-11 |
| ISO/IEC 20000-1: improvement of services | Decision log and evaluation harness provide measurable inputs for later service review | FN-10, FN-12 |

Not proposed: certification, a conformity statement, an Annex A control mapping (the control list was not retrieved in this project), or any statement about the sponsor's current certification status, which is unknown.
