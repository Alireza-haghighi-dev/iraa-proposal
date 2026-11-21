# S10_FORM_MAPPING

| Field | Value |
|---|---|
| Document ID | S10_FORM_MAPPING |
| Version | 0.1 |
| Status | DRAFT |
| Stage | S10 |
| Date | 2026-11-21 |
| Depends on | REF-02 (PROPOSAL_FORM_EN_WORKING_V1); proposal/IRAA_PROPOSAL_EN_MASTER v0.3; RF-001 to RF-003; DEC-039; ISS-021; ISS-056 |

- **Purpose:** maps every field and table of the official form to the master and states what remains before transfer into the native template.
- **Native template:** not available in this session. The only form available is the English working representation REF-02, which reproduces the 20 sections and the logical table schemas but not the page design. No claim of Word-layout compliance is made (DEC-039 item 2). Table header rows below are checked verbatim against REF-02 by `qc/S10_QC_CHECK.py`.
- **Status codes:** COMPLETE (text final pending native insertion); OWNER (waits for `S10_OWNER_DECISION_REQUEST`); LOCAL (reserved for local completion, never filled here).

## 1. Section and table map

| Sec. | Form field or table (REF-02) | Master content | Status | Insertion note |
|---|---|---|---|---|
| 1 | Title text | Title naming maturity, execution stages and prototype type, following the form's own pattern | COMPLETE | Plain text in the title field |
| 2 | Team name | Placeholder | LOCAL | Naming rule is local |
| 3 | Team lead and contact | Placeholder | LOCAL | Personal data never entered here |
| 4 | Duration (months); total person-hours | Placeholders; provisional 2,004 h cited | OWNER | Filled from items 1–3 of the decision request; must equal Section 13 and the Section 16 month span |
| 5 | Classification table, 2 columns × 5 rows | Table kept; selection written after the options in each cell; justification below the table | COMPLETE | In the native form, mark the selection with the form's own mechanism (tick, highlight or deletion of unselected options) and remove the words "Provisional selection"; the classification is provisionally adopted (DEC-028, ISS-016) |
| 6 | Free text | Need, gap, literature basis, human-approval rationale | COMPLETE | Plain paragraphs |
| 7 | Free text | Five objectives, completion deliverables, assumptions | COMPLETE | Plain paragraphs |
| 8 | Free text; the form asks for measurable specifications in a table | Functional features table (No. / Feature / Requirement) and measurable specifications table (No. / Specification / Metric and test condition / Target) | COMPLETE | Both tables are project tables inside a free-text field, as the form invites for specifications; the features table could be turned into a numbered paragraph list if the reviewer reads it as a new form table (ISS-056) |
| 9 | Comparator table, 7 columns | Six rows; two patent records discussed after the table | COMPLETE (location column LOCAL) | Location descriptor part of column 4 is local |
| 10 | Team prior-work table, 7 columns | One placeholder row | OWNER / LOCAL | Only documented work; left blank if none (decision request item 10) |
| 11 | Continuity table, 5 columns | Four stages, current project first | OWNER (durations); LOCAL (cost) | Row 1 duration = Section 4; later rows are estimates, not commitments |
| 12 | Free text; activity titles repeated from Section 13 | Introductory parts, seven numbered activities with exact Section 13 titles, limits of the method | COMPLETE | Unnumbered subheadings and the tool table are not in the form; at insertion either keep them as plain lines and a simple table or convert them to paragraphs (ISS-056). Numbered titles must stay verbatim |
| 13 | Activity table, 5 columns | Seven activities, deliverables, key tasks, provisional effort | OWNER (effort) | Effort figures final only after decision request items 2–5 |
| 14 | Team table, 6 columns | Placeholder row | OWNER / LOCAL | Name and qualifications local; responsibility, monthly hours and share from item 1; shares total 100% |
| 15 | Budget table, 6 columns | Placeholder row; four cost drivers named | OWNER / LOCAL | Unit cost and total are local in the form; item types and quantities from items 6–8 |
| 16 | Gantt table, 17 columns (12 month columns) | Seven activities with titles and provisional effort; month cells open | OWNER | Months from items 1 and 3; cost cells local; weights from item 7. A duration above 12 months does not fit the 12 month columns of REF-02 and needs the native template's rule (item 3) |
| 17 | Risk table, 4 columns | Fourteen risks | COMPLETE except three schedule and cost mitigations marked open | Updated after owner inputs |
| 18 | Completion date | Placeholder | LOCAL | Must agree with Section 4 duration and start date |
| 19 | Free text | Claim-status statement and reference list | COMPLETE | References as plain paragraphs |
| 20 | Attachment table, 2 columns | Eight categories, all local | LOCAL | — |

## 2. Remaining template-insertion work (local finalization)

1. Obtain the native Word template and compare section order, headings and every table header with REF-02; record any difference before inserting text.
2. Remove the master's metadata table, front-matter notes and every bracketed working placeholder.
3. Insert text in regular-weight 12-point type (RF-001); no added bullets, ticks or bold (RF-002); paragraph lists in Sections 7 and 8 stay as sentences.
4. Keep every official table's columns, order and labels (RF-003); add rows only where the form's table is designed to take them.
5. Decide the Section 12 subheadings and tool table and the Section 8 features table (ISS-056); apply the S09 reduction plan (`S09_REVIEW_REPORT` §5) only if a length rule applies.
6. Fill local fields: Sections 2, 3, 18, 20, the location part of Section 9 column 4, Section 14 names and qualifications, Section 15 unit costs and totals, Section 16 activity costs, Section 11 costs.
7. Localization is a separate post-S10 process; the English master stays the source text.
