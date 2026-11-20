# 03_STYLE_GUIDE

| Field | Value |
|---|---|
| Document ID | 03_STYLE_GUIDE |
| Version | 1.2 |
| Status | APPROVED |
| Stage | S01 |
| Date | 2026-11-20 |
| Depends on | REF-03 (RF-001 to RF-004); DEC-006; DEC-013 |

- **Applies to:** Every deliverable at every stage (DEC-006, DEC-013); proposal text additionally from S07
- **Related criteria:** RF-002, RF-004, QA-002, QA-005

## 1. Purpose

A reviewer should be able to ask the proposing team about any sentence and get a technical answer. Text that sounds polished but cannot be defended in that conversation fails this guide (RF-004).

## 2. Core rules

1. **Say something specific.** Each substantive paragraph names at least one concrete element of this project: a requirement ID, a component, a method, a dataset condition, a metric, a deliverable or a constraint.
2. **Back every evaluative word.** "Accurate", "efficient", "scalable" or "robust" needs a criterion ("precision@5 of at least X on test set Y, target") or a source. Otherwise delete it.
3. **Keep the claim status visible.** Write targets as targets ("the evaluation will test whether…"), assumptions as assumptions, and verified facts with their source. Expected benefits from the requirements statement are hypotheses (C5).
4. **Prefer the plain verb.** "The assistant ranks stored submissions by similarity", not "the assistant enables the facilitation of similarity-based ranking".
5. **One idea per sentence where the idea is technical.** Long sentences are acceptable when they carry a single chain of reasoning.
6. **Name the actor.** Use active voice when someone or something performs the action; the assessor, the retrieval component, the evaluation script.
7. **Define once, then reuse.** Introduce a term with its definition, then use the same term throughout (§6).
8. **No inherited figures.** Numbers from earlier drafts are not reused without justification (QA-001).

## 3. Proposal-text form (from S07; supports RF-001 to RF-003)

- Narrative sections are written as prose paragraphs.
- No decorative dots, checkmarks or paragraph-opening bullets unless the official form uses them (RF-002).
- No arbitrary bold or emphasis in inserted text (RF-001).
- Tables keep the form's columns, labels and order (RF-003).
- Working registers (this project's governance files) may use tables and lists; they are not proposal text.

## 4. Patterns to remove

Treat these as diagnostics. The fix is to replace them with specific content, not to rephrase them.

| Pattern | Example of the problem | What to do instead |
|---|---|---|
| Generic opening | "In today's rapidly evolving landscape…" | Start with the project-specific point |
| Importance assertion | "plays a crucial role", "is of paramount importance" | State the consequence and its evidence |
| Stock triplet | "efficient, scalable and robust" | Keep one property and give its criterion |
| Unattributed authority | "studies show", "it is widely recognized" | Cite the source (SRC-###) or remove |
| Echo summary | Final sentence restating the paragraph | Delete, or add the next logical step |
| Template paragraphs | Several paragraphs with identical structure | Vary structure according to content |
| Hedge stacking | "may potentially help to possibly reduce" | One accurate qualifier |
| Inflated benefit | "will revolutionize assessment" | Hypothesis with a measurable test |
| Unearned superiority | "outperforms existing tools" | Only with matched benchmark evidence (QA-005) |
| Nominalization chains | "the implementation of the evaluation of…" | Use the verb |
| Empty transitions | "Furthermore", "Moreover" opening most paragraphs | Let the logic connect sentences |

## 5. Revision method

1. Identify what the sentence must communicate.
2. Check whether the claim is supported; if not, label or remove it.
3. Rewrite for the reader who will question it.
4. Re-check fidelity against the source and the claim register.

Synonym substitution and rhythm-only edits are not revisions. Editing is never aimed at AI-detection tools (DEC-006).

## 6. Glossary (controlled terms)

| Term | Meaning in this project | Avoid |
|---|---|---|
| Submission | A need or challenge entered into the sponsor's platform for assessment (DEC-002). The requirements statement calls these "requirements". | "Requirement" for submissions in our own prose, except when quoting the form or source titles |
| Project requirement | An R or C item in `S01_REQUIREMENTS_REGISTER.md` | — |
| Assessment | The review of a submission by the sponsor's staff, leading to an outcome. Content not yet defined (ISS-005). | Implying the assistant makes the assessment |
| Assessor | A sponsor staff member who reviews submissions and gives final approval (R3) | "Reviewer" (reserved below) |
| Proposal reviewer | The person evaluating this proposal; source of RF items | "Reviewer" without qualifier where ambiguous |
| Assistant | The proposed software that supports assessors | "AI system" as a vague label; "autonomous" |
| Internal collection | The "approved internal collection" named in R2. Its existence as a populated, accessible dataset, its contents and its availability to the project are unresolved (ISS-003, ISS-002, CLM-012). | "Knowledge base" unless defined |
| External prior art | Patents and solution examples from outside the sponsor (R4) | — |
| Development stage | S01–S10 of this proposal-writing workflow | Using "stage" for work packages |
| Work package (WP) | One of the ~6–7 funded main activities in Section 13 | "Stage", "phase" |
| Continuity phase | A row of the Section 11 table. In proposal text use the form's own label "Stage". | Confusing with development stages |
| Target | A value the evaluation will test; not a result | "Achieves", "delivers" for untested values |
