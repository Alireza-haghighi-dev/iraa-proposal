# S04_PLAN

| Field | Value |
|---|---|
| Document ID | S04_PLAN |
| Version | 1.0 |
| Status | SUBMITTED FOR GATE |
| Stage | S04 |
| Date | 2026-11-20 |
| Depends on | S03_HANDOFF; DEC-026; DEC-027; 00_STAGE_GATE_PROTOCOL §7 (S04 row) |

## 1. Inputs

| Input | Use |
|---|---|
| Repository at commit 9a7a95e. Baselines 2b5f83c (S01), 34a7745 and 961ae6a (S02) and S03 content commit 6780335 all present in history; checked before work began. DEC-026 was missing and was recorded from the owner's instruction (see DEC-026). | Rules, registers, evidence |
| Inputs listed in `S03_HANDOFF.md` only: rules, status, gate protocol, style guide, requirements register, RQ-13 to RQ-15, decisions, open issues, the ten listed claims, S02 synthesis §3, S03 matrix §5, Skill register, traceability matrix | Design inputs and limits |
| REF-01 §7, §8, §11, §15, §17; REF-02 §1, §5, §7, §8, §11; REF-03 RF-005, RF-011, RF-012, QA-003, QA-004 (Claude Project) | Requirement wording, form schemas, reviewer criteria |

## 2. Execution steps

1. Record DEC-026 and DEC-027; Skill checkpoint (SKL-004).
2. RQ-13 only: retrieve the official ISO/IEC pages for ISO/IEC 27001 and ISO/IEC 20000-1 and log them. RQ-14 (patent data terms) and RQ-15 (deployment and compute) stay in S05 as planned; S04 designs interfaces that do not depend on their answers.
3. Write the scope-options analysis (Option A to D) and a recommendation for ISS-001, without deciding it.
4. Write the functional scope, component architecture, R3 checkpoints, interfaces and data flows, separating current-project and future capabilities.
5. Record assumptions for data, integration, deployment and access; keep unresolved items OPEN; write the standards-alignment analysis.
6. Draft proposal Sections 5, 7, 8 and the technical part of 11 under the recommended option, marked provisional.
7. Update living registers, add traceability Part F, run the S04 QC script and safety scan, write QC report and handoff, commit and push (DEC-027).

## 3. Search log

| RQ | Queries | Mode | Pages opened |
|---|---|---|---|
| RQ-13 | "ISO/IEC 20000-1:2018 service management system requirements iso.org"; "ISO/IEC 27001:2022 information security management systems requirements iso.org abstract" | Standard | iso.org record 70636 (SRC-065); IEC webstore record 79694 (SRC-064). The iso.org page for ISO/IEC 27001 returned a client error twice and was not used. |

## 4. Length budget

| Deliverable | Budget |
|---|---|
| S04_SCOPE_OPTIONS | ≤ 10 KB |
| S04_ARCHITECTURE | ≤ 24 KB |
| S04_DATA_FLOWS_AND_INTERFACES | ≤ 16 KB |
| S04_ASSUMPTIONS_AND_STANDARDS | ≤ 12 KB |
| Four proposal drafts | ≤ 16 KB together |
| S04_HANDOFF | One page |
