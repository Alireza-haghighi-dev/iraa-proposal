# 00_STAGE_GATE_PROTOCOL

| Field | Value |
|---|---|
| Document ID | 00_STAGE_GATE_PROTOCOL |
| Version | 2.0 |
| Status | SUBMITTED FOR GATE |
| Stage | S02 |
| Date | 2026-11-20 |
| Depends on | 00_PROJECT_RULES; 03_STYLE_GUIDE; REF-03 |

## 1. Gate outcomes

- **PASS**: all checks in sections 2–6 satisfied.
- **CONDITIONAL PASS**: only non-blocking conditions remain; each is logged as an ISS entry with a target stage.
- **FAIL**: any blocking check fails. The stage is reworked before resubmission.

Only the owner decides the gate. The decision is recorded as a DEC entry. The next stage does not start without it.

## 2. Delivery completeness

- [ ] Defined inputs and a short execution plan (`S0X_PLAN.md`).
- [ ] Stage work products as named Markdown files carrying the metadata header defined in `00_PROJECT_RULES.md` §10.
- [ ] Updated `00_DECISIONS_LOG.md` and `00_OPEN_ISSUES_REGISTER.md`.
- [ ] Updated `02_SOURCE_LOG.md` and `02_CLAIM_REGISTER.md` where research occurred.
- [ ] `S0X_QC_REPORT.md` and `S0X_HANDOFF.md` (one page or less, listing exact inputs for the next stage).
- [ ] Skill checkpoint recorded in `00_SKILL_REGISTER.md`.
- [ ] `00_STAGE_STATUS.md` updated.
- [ ] Before any push: QC script and pre-commit safety scan passed. After approval: commit on `main`, pushed, approved commit SHA recorded in `00_STAGE_STATUS.md`; tag added where the environment permits (`00_PROJECT_RULES.md` §4, DEC-020).

## 3. Evidence checks

- [ ] Every factual statement carries a claim label (see `00_PROJECT_RULES.md` §6).
- [ ] Every external source has a DOI or URL, access date, tier and verification status in `02_SOURCE_LOG.md`.
- [ ] No citation from memory. Every cited item was retrieved and inspected during this project.
- [ ] Source tiers respected: **T1** peer-reviewed literature, standards bodies, official technical documentation, patent-office records; **T2** vendor documentation (valid only as evidence of what the vendor states); **T3** secondary or press material (never the sole support for a capability, performance or comparator statement).
- [ ] Numbers, capabilities and comparator statements re-checked against source text at the gate.
- [ ] Limitations that affect applicability (domain, language, data, date) are recorded.
- [ ] No target, expected benefit, vendor description or standards mention is presented as a demonstrated fact (C4, C5, QA-002).

## 4. Traceability and scope checks

- [ ] `S01_TRACEABILITY_MATRIX.md` updated; no R, C, F, FX, RF or QA item dropped.
- [ ] Every applicable RF and QA item carries one status from the reviewer document: `ADDRESSED`, `SCHEDULED`, `JUSTIFIED EXCEPTION` or `OPEN`, with an artifact reference.
- [ ] Current-project scope kept separate from future phases (C3, F-07, RF-005).
- [ ] Development stages (S01–S10) not conflated with Section 13 work packages (DEC-012).
- [ ] No team, personal, financial-commitment, jurisdiction-specific or local administrative content before S10; local fields remain `[LOCAL COMPLETION ONLY]`.

## 5. Writing-quality checks (every deliverable, every stage)

- [ ] **Specificity**: each substantive paragraph contains a project-specific element (an ID, component, method, metric, data condition or deliverable). A paragraph that would fit an unrelated proposal fails.
- [ ] **Qualifiers**: evaluative words ("robust", "comprehensive", "significant", "efficient") are backed by a stated criterion or source, or removed.
- [ ] **Patterns**: none of the patterns in `03_STYLE_GUIDE.md` §4 remain.
- [ ] **Revision quality**: fixes change content or structure; synonym substitution is not a fix; no editing aimed at AI detectors.
- [ ] **Terminology**: consistent with the glossary in `03_STYLE_GUIDE.md` §6.
- [ ] **Concision**: each deliverable within the length budget stated in its plan, or the excess justified.
- [ ] **Fidelity**: no requirement, obligation, number or technical meaning changed relative to the reference documents and the claim register.
- [ ] **Proposal-text form** (from S07): no decorative bullets, checkmarks or paragraph-opening bullets where the official form does not use them (RF-002).

## 6. QC report content

Checks run, method used for each, result, defects found and fixed, open defects with severity (Critical / Major / Minor / Note), and a recommended gate outcome.

Each check is classed as one of:

- **Scripted (reproducible)**: the script and its output are delivered with the stage package, and the owner can re-run it on the delivered files.
- **Self-reported**: performed by the drafting session by reading; not independently verified. Reported as such, never as verified.

A check may be called "verified" only when it is scripted and reproducible, or when an isolated reviewer has performed it (S09, S10b).

## 7. Stage-specific exit criteria

| Stage | Must be true before exit |
|---|---|
| S01 | R/C/CTX/F/FX registered; RF-001–RF-012 and QA-001–QA-010 registered with status; RQs mapped to stages and sections; evidence system set up; scope and data issues logged. |
| S02 | Each active RQ assigned to S02 has at least one verified T1 source or an explicit "no adequate evidence found" record; limitations stated per method family. |
| S03 | At least three Section 9 comparators; every capability cell sourced or marked "not documented"; no superiority claim without matched benchmark evidence (QA-005). |
| S04 | Current-phase boundary and future phases separated; R3 checkpoints defined; integration and data assumptions explicit; ISS-001 decided by owner; Section 5 provisionally selected (RF-011, QA-003). |
| S05 | Metrics, baselines, dataset needs, procedures and acceptance criteria defined and labelled as targets; ISS-002 resolved or an explicit assumption recorded (QA-002, QA-004). |
| S06 | 6–7 work packages with frozen IDs and titles, tasks, deliverables, acceptance evidence, dependencies and provisional person-hours with stated assumptions, within the ISS-013 envelope (RF-007, QA-001, QA-007). |
| S07 | Section 12 uses WP numbers and titles verbatim; each tool or version verified or marked PROPOSED; each Section 8 specification maps to a verification step (RF-006, QA-010). |
| S08 | Passes A–E logged; all draftable sections complete; local fields remain placeholders. |
| S09 | Isolated review completed (with authorization); no open Critical or Major defects; every RF item `ADDRESSED` or `JUSTIFIED EXCEPTION` for draftable sections. |
| S10 | FX-02 to FX-05 verified by script; S10b independent audit passed; local fields marked. |
