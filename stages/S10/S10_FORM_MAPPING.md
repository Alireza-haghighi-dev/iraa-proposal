# S10_FORM_MAPPING

| Field | Value |
|---|---|
| Document ID | S10_FORM_MAPPING |
| Version | 0.3 |
| Status | DRAFT |
| Stage | S10 |
| Date | 2026-11-21 |
| Depends on | REF-02 (PROPOSAL_FORM_EN_WORKING_V1); proposal/IRAA_PROPOSAL_EN_MASTER v0.5; DEC-042; RF-001 to RF-003; DEC-039; ISS-021; ISS-056 |

- **Purpose:** maps every field and table of the official form to the master and states what remains before transfer into the native template.
- **Native template:** supplied by the owner on 2026-11-22 as a sanitized blank English working copy (DEC-043; SHA-256 in `qc/S10_FORM_QC_OUTPUT.txt`; not committed, as a reference document). The filled form `proposal/IRAA_PROPOSAL_EN_FORM.docx` is kept out of the public repository by the existing `*.docx` rule in `.gitignore` and is delivered to the owner directly (its SHA-256 is in the QC output); it is reproducible from the blank form and the master with `qc/S10_BUILD_FORM_DOCX.py`, and is checked cell by cell by `qc/S10_FORM_QC.py`. The working markdown master keeps the REF-02 column labels; the native form's own labels govern the Word file (§3).
- **Status codes:** COMPLETE (text final pending native insertion); OWNER (waits for `S10_OWNER_DECISION_REQUEST`); LOCAL (reserved for local completion, never filled here).

## 1. Section and table map

| Sec. | Form field or table (REF-02) | Master content | Status | Insertion note |
|---|---|---|---|---|
| 1 | Title text | Title naming maturity, execution stages and prototype type, following the form's own pattern | COMPLETE | Plain text in the title field |
| 2 | Team name | Placeholder | LOCAL | Naming rule is local |
| 3 | Team lead and contact | Placeholder | LOCAL | Personal data never entered here |
| 4 | Duration (months); total person-hours | 6 months; 1,291 person-hours (DEC-042) | COMPLETE | Equals Section 13 and the Section 16 month span |
| 5 | Classification table, 2 columns × 5 rows | Table kept; selection written after the options in each cell; justification below the table | COMPLETE | In the native form, mark the selection with the form's own mechanism (tick, highlight or deletion of unselected options) and remove the words "Provisional selection"; the classification is provisionally adopted (DEC-028, ISS-016) |
| 6 | Free text | Need, gap, literature basis, human-approval rationale | COMPLETE | Plain paragraphs |
| 7 | Free text | Five objectives, completion deliverables, assumptions | COMPLETE | Plain paragraphs |
| 8 | Free text; the form asks for measurable specifications in a table | Functional features table (No. / Feature / Requirement) and measurable specifications table (No. / Specification / Metric and test condition / Target) | COMPLETE | Both tables are project tables inside a free-text field, as the form invites for specifications; the features table could be turned into a numbered paragraph list if the reviewer reads it as a new form table (ISS-056) |
| 9 | Comparator table, 7 columns | Six rows; two patent records discussed after the table | COMPLETE (location column LOCAL) | Location descriptor part of column 4 is local |
| 10 | Team prior-work table, 7 columns | One placeholder row | OWNER / LOCAL | Only documented work; left blank if none (decision request item 10) |
| 11 | Continuity table, 5 columns | Four stages, current project first; row 1 duration 6 | OWNER (rows 2–4 durations); LOCAL (cost) | Later rows are estimates, not commitments |
| 12 | Free text; activity titles repeated from Section 13 | Introductory parts, seven numbered activities with exact Section 13 titles, limits of the method | COMPLETE | Unnumbered subheadings and the tool table are not in the form; at insertion either keep them as plain lines and a simple table or convert them to paragraphs (ISS-056). Numbered titles must stay verbatim |
| 13 | Activity table, 5 columns | Seven activities, deliverables, key tasks, approved effort (DEC-042) | COMPLETE | — |
| 14 | Team table, 6 columns | Placeholder row; four members planned (DEC-042) | OWNER / LOCAL | Name and qualifications local; responsibility, monthly hours and shares from request items 1–3 (formulas in S10_RESOURCE_CALCULATIONS); shares total 100% |
| 15 | Budget table, 6 columns | Placeholder row; four cost drivers named | OWNER / LOCAL | Unit cost and total are local in the form; item types and quantities from request items 4–6 |
| 16 | Gantt table, 17 columns (12 month columns) | Seven activities, approved effort, months 1–6 marked from the approved distribution; months 7–12 blank | COMPLETE except costs and weights | Cost cells local; weights from request items 4–5; mark months with the native form's own mechanism |
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

## 3. Native form: insertion record (DEC-043)

| Item | Native form | Treatment |
|---|---|---|
| Tables | 10 native tables (Sections 5, 9, 10, 11, 13, 14, 15, 16, 17, 20) | Count, grids, widths, table properties, header rows and merges unchanged; 20 data rows added by cloning adjacent rows (S9 3, S11 1, S13 2, S14 1, S16 2, S17 11; list in `qc/S10_FORM_ADDED_ROWS.txt`) |
| Section 5 | Checkbox cells | Seven selections marked [X]; justification paragraphs below the table |
| Section 8 | No native table | Features and measurable specifications inserted as numbered paragraphs, so no table is added; the form's guidance asks for a specification table, which the owner may approve as one addition (ISS-056) |
| Section 9 | Seven columns; three comparison fields | Six rows; six comparison fields (three cloned); patent prior-art paragraph after the fields |
| Section 11 | Labels Current phase, Future phase 1, 2 | Row Future phase 3 added |
| Section 12 | Free text | Subheadings as plain paragraphs (no heading style or bold); the tool table rendered as sentences (ISS-056) |
| Section 14 | Six columns, three rows | Fourth row added; neutral labels; planned hours and shares (DEC-043 item 7) |
| Section 15 | Fixed category rows with merges | Quantities and pending items only; no amounts or units |
| Section 16 | 17 columns, two header rows, 12 month columns | Seven activity rows; months 1–6 marked X; months 7–12 blank; costs and weights pending |
| Section 17 | Five category rows (Technical, Data / information, Schedule, Financial, Other) | 16 risks in that order; master renumbered to match |
| Column labels | Differ from REF-02 (for example "Implementation context", "Work assignment", "Cost weight (%)") | Native labels kept in the Word file; master keeps REF-02 labels as working text |
| Template guidance | Instruction paragraphs per section | Removed where content was inserted; kept where content is still open (general note in Section 1; Sections 2, 10, 14 local-entry note, 15, 16 cost notes, 20) |
| Header, footer and signature block, styles, numbering, page setup | — | Byte-equivalent after canonicalization (scripted) |
| Table cell type size | Native 10 pt cell format | Kept; the 12 pt rule is applied to narrative paragraphs |
