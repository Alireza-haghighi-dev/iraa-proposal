# S04_ASSUMPTIONS_AND_STANDARDS

| Field | Value |
|---|---|
| Document ID | S04_ASSUMPTIONS_AND_STANDARDS |
| Version | 2.0 |
| Status | SUBMITTED FOR GATE |
| Stage | S05 |
| Date | 2026-11-20 |
| Depends on | C2; CLM-008; CLM-041; CLM-042; CLM-043; SRC-064; SRC-065; ISS-002; ISS-003; ISS-006 to ISS-010; ISS-023; ISS-033 to ISS-039; CLM-045; DEC-029; S05_EVALUATION_DESIGN; S05_DATA_AVAILABILITY_AND_SUBSTITUTES |

- **Purpose:** state the planning assumptions the architecture uses while owner decisions are open, and define what "alignment" with ISO/IEC 20000 and ISO/IEC 27001 can honestly mean for this project.
- **S05 addition:** AS-09 to AS-12 cover evaluation data, judges, the reference environment and the numeric planning values; AS-01 to AS-08 are unchanged.
- **Labels:** AS rows are ASSUMPTION; each stays in force only until the linked issue is decided. Standards descriptions are VERIFIED at landing-page depth (SRC-064, SRC-065); the alignment mapping is PROPOSED.

## 1. Planning assumptions

| ID | Assumption | Linked issue | If the assumption fails |
|---|---|---|---|
| AS-01 | Evaluation and prototype data come from a sanitized export of stored submissions; if none can be released, from a public proxy collection labelled as such | ISS-002, ISS-028 | Proxy only: Section 8 targets apply to proxy data, and the proposal says so |
| AS-02 | No solution-example source for R2 is treated as available until the owner confirms its category, format and permission to use it. FN-05 is built against the evidence-source interface and tested on labelled substitute data meanwhile; no substitute dataset is selected in S04 or S04.1 (revised S04.1, DEC-029) | ISS-003, ISS-037, CLM-045 | When a source is confirmed, it is registered and FN-05 is re-evaluated on it; no design change |
| AS-03 | The platform can produce a file export of submissions; no API is assumed; the prototype never writes to the platform | ISS-008 | No export at all: AS-01 proxy route; API available: IF-07 can move into scope only by owner decision |
| AS-04 | The prototype runs in an isolated, project-controlled or sponsor-provided environment with self-hosted retrieval models; no submission text goes to hosted AI services | ISS-009 | Hosted services allowed: AD-08 and hosted re-ranking become options, with the provider's terms recorded |
| AS-05 | Access uses project-managed test accounts with three roles (assessor, administrator, evaluator); no sponsor production accounts | ISS-035 | Sponsor accounts required: IF-08 federation becomes in scope |
| AS-06 | Submission language is unknown; S05 selects components that can be tested on the actual language once ISS-007 is answered | ISS-007, RQ-07 | Conditional RQ-07 is activated in S05 |
| AS-07 | Corpus size and submission rate are unknown; S05 sizes the prototype for ranges agreed with the owner | ISS-023, RQ-15 | Sizing revised |
| AS-08 | At least one patent source offers access terms that permit automated queries for this use; solution-example sources are added only if ISS-006 names one | ISS-006, RQ-14 | R4 is limited to assessor-run searches with results entered manually, and Section 8 records the limit |
| AS-09 | Until ISS-002 is answered, R1 method comparison and harness validation use public substitute data (candidates DS-01, DS-02, subject to the licence check) and R2 uses a constructed substitute (DS-05, subject to owner decision). All such results are labelled Track P (added S05) | ISS-002, ISS-038 | Sponsor data released: Track S added; Track P kept as a method check |
| AS-10 | If sponsor assessors cannot judge (ISS-012), project judges with domain knowledge apply the same judging guide; their results are labelled "project judges" (added S05) | ISS-012 | Assessors available: they judge Track S, and a shared subset calibrates project judges |
| AS-11 | Evaluation and timing run on one self-hosted reference environment (a single server with an optional single GPU and a Java 21 runtime); its exact specification is fixed in S06/S10 (added S05) | ISS-009, ISS-023 | Different environment: FT-02 and ET-10 repeated on it |
| AS-12 | The numeric planning values PV-01 to PV-11 in `S05_EVALUATION_DESIGN` §7 apply until the owner confirms or changes them (added S05) | ISS-039 | Values changed: protocol, judging budget and Section 8 targets updated before the protocol is frozen |

## 2. Questions the owner is asked to answer

These are the open points that change the design. None asks for team, personal or financial information.

| Issue | Question |
|---|---|
| ISS-003 | From which sources should existing solution examples be identified for a submitted need (sponsor-held records, external sources, or both)? Is any of them available to the project, under what permissions, and how can it be accessed? |
| ISS-004 | R1 covers comparison of new submissions with stored ones (FN-03). Do you also want the optional grouping of the stored collection (FN-04)? |
| ISS-005 | What fields and outcome codes does a completed assessment currently contain? |
| ISS-007 | In which language or languages are submissions and any solution-example source written? |
| ISS-008 | Can the platform export submissions to a file, and is there an API? |
| ISS-009 | May submission text be processed by externally hosted AI services, or must it stay in sponsor-controlled infrastructure? |
| ISS-010 | Does the C2 standards constraint mean design alignment, fitting into an existing certified management system, or certification? |
| ISS-033 | May assessor-approved query text be sent to external patent search services? |
| ISS-034 | Is one assessor's approval sufficient, or does the sponsor require a second approver? Which optional review controls (CP-1 to CP-4) should the prototype include? |
| ISS-037 | Should R2 cover only sponsor-held examples, or also external examples that R4 would otherwise return? |
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
