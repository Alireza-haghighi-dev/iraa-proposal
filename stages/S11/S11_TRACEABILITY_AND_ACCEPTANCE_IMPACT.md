# S11_TRACEABILITY_AND_ACCEPTANCE_IMPACT

| Field | Value |
|---|---|
| Document ID | S11_TRACEABILITY_AND_ACCEPTANCE_IMPACT |
| Version | 0.1 |
| Status | APPROVED |
| Stage | S11 |
| Date | 2026-11-21 |
| Depends on | S01_TRACEABILITY_MATRIX; S07_WP_METHOD_TRACEABILITY; S11_SCOPE_AND_TECHNICAL_PLAN; IRAA_PROPOSAL_EN_MASTER v0.4 |

## 1. Requirements

| Requirement | Delivered by | Verified by (master Section 8) | S11 change | Still satisfied? |
|---|---|---|---|---|
| R1 compare new submissions with stored ones (identical or related) | WP3 import, hashes and fingerprints, three ranked configurations, evidence passages | Specification 1 (nDCG@10, 50 test queries); specification 8 | Configurations 9 → 3; queries 60 → 50; interval rule | Yes |
| R2 assess whether relevant existing solution examples can be identified | WP3 on each registered source; WP2 constructed substitute if no source is confirmed | Specification 2 (P@5, 40 test statements per source; "no example found" lower bound) | Statements written once and shared with R4; deeper check smaller | Yes, on substitute data unless a source is confirmed |
| R3 final human approval and re-approval | WP1 transition table; WP5 record service, trigger, audit chain, screens; generated suite | Specifications 4 and 6 | Randomized sequences and second-approver setting removed; exhaustive generated suite kept | Yes, unchanged in strength |
| R4 external patent and solution evidence, subject to authorization | WP4 connector, query construction, clearance plus approval, manual fallback | Specifications 3 and 5; specification 8 | Two query formulations instead of three; result reported as an estimate | Yes; disclosure controls unchanged |
| Information security constraint | WP1 risk assessment, roles, retention; WP5 audit; WP7 deletion | Specification 5; design review | None | Yes |
| Extensibility constraint | Import, retrieval and connector interfaces; adapter specified | Design review | Identity interface replaced by framework authentication | Yes |

## 2. Section 8 specifications and acceptance criteria

| No. | Before S11 | After S11 | Impact on acceptance |
|---|---|---|---|
| 1 | Non-inferiority test (margin 0.05, margin-shifted randomization, Holm), superiority second; floor | Interval rule against the margin and zero; randomization p reported; floor; "inconclusive" outcome | Same target meaning (not required to beat BM25); claims now limited to what the interval shows |
| 2 | As 1, per source; "no example found" lower bound | As 1, per source; lower bound kept | As 1 |
| 3 | Non-inferiority at margin 0.10 if sized after the pilot, otherwise estimate | Estimate with interval only | No inferential claim; removes an unreachable target |
| 4 | Zero bypasses; generated plus randomized tests | Zero bypasses; generated exhaustive tests | Criterion unchanged |
| 5 | 100% both conditions; zero unrefused attempts | Unchanged | Unchanged |
| 6 | 100% versions stored | Unchanged | Unchanged |
| 7 | ≤ 5 s at agreed sizes (three brackets) | ≤ 5 s at 10,000 and 100,000 items | Larger collections stated as outside the tested range |
| 8 | 100% attribution | Unchanged | Unchanged |

## 3. Work packages, deliverables and Sections 12–16

| WP | Title (unchanged) | Deliverables changed | Section 12 | Section 13 effort | Section 16 |
|---|---|---|---|---|---|
| WP1 | Prototype design specification and data-protection baseline | Vertical prototype added to the key tasks | Activity 1 updated | 150 (provisional) | Effort updated; months open |
| WP2 | Evaluation protocol, test collections and evaluation harness | "Significance procedure" → "decision rule"; one need-statement set | Activity 2 rewritten | 168 | As above |
| WP3 | Ingestion and retrieval for similar submissions and solution examples | Duplicate flag explicit; two corpus sizes | Activity 3 rewritten | 210 | As above |
| WP4 | External prior-art retrieval with query approval | None | Two formulations | 138 | As above |
| WP5 | Assessment record, review interface and approval controls | "Lightweight" screens | Activity 5 trimmed | 226 | As above |
| WP6 | Prototype integration and evaluation | Configuration selection record removed; error analysis added | Activity 6 rewritten | 267 | As above |
| WP7 | Technical documentation and handover | Reproducibility check added | Activity 7 updated | 132 | As above |

Titles in Sections 12, 13 and 16 are identical to the frozen WP titles (scripted check). Section 16 months, costs and weights stay open until the checkpoint.

## 4. Records superseded in part

S05_EVALUATION_DESIGN (planning values, MS-01 to MS-03 rules), S06_DEPENDENCIES_AND_EFFORT (task figures), S06_WORK_PACKAGES (tasks T2.4, T3.4, T6.4) and S07_CORRECTED_EVALUATION_METHODOLOGY (§§2, 6) remain the approved historical record; where they differ, the master v0.4 and this stage govern, pending the owner checkpoint.
