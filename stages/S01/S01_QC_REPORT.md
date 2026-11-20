# S01_QC_REPORT

| Field | Value |
|---|---|
| Document ID | S01_QC_REPORT |
| Version | 1.2 |
| Status | APPROVED |
| Stage | S01 |
| Date | 2026-11-20 |
| Depends on | All S01 deliverables v1.2; S01_QC_CHECK.py; S01_QC_CHECK_OUTPUT.txt; DEC-015; DEC-016 |

- **Performed by:** the drafting session. No check in this report is independently verified; independent review is reserved for S09 and S10b (DEC-007).
- **Outcome:** S01 approved by the owner (DEC-016). Version 1.2 adds the GitHub layout and handoff; the final scripted run below was made on the repository contents committed under tag `S01-approved`.

## 1. How to read this report

Each check is classed as defined in `00_STAGE_GATE_PROTOCOL.md` §6:

- **Scripted (reproducible):** run by `stages/S01/qc/S01_QC_CHECK.py`. Full output is in `stages/S01/qc/S01_QC_CHECK_OUTPUT.txt`, which also lists the SHA-256 hash of every S01 Markdown deliverable, so the results can be tied to the committed versions. To re-run from the repository root: `python3 stages/S01/qc/S01_QC_CHECK.py .` (Python 3 standard library only). Because this report and the output file are themselves checked, the output reflects the files as committed.
- **Self-reported:** performed by reading. Not verified by script or by an independent reviewer.

## 2. Scripted checks

Result of the final run: **PASS** (counts in `S01_QC_CHECK_OUTPUT.txt`, SUMMARY line).

| # | Check | What the script tests | Result |
|---|---|---|---|
| S1 | Metadata header | Every Markdown file has the six-field header in standard order; Document ID matches file name; version, status vocabulary and date format valid; dependencies present | Pass |
| S2 | No duplicate definitions | ISS, DEC, CLM, REF, SKL, RF, QA, F, FX, CTX, RQ each defined once in their register | Pass |
| S3 | Complete sets | RF-001–012, QA-001–010, F-01–20, FX-01–12, RQ-01–15, R1–R4 | Pass |
| S4 | C-series classification | C1, C2 = SC; C3 = EA; C4, C5, C6 = PG | Pass |
| S5 | Reference integrity | Every identifier referenced in any file is defined (DEC-016 reported separately as a pending proposal) | Pass |
| S6 | RF/QA status labels | Every RF and QA row uses one of ADDRESSED, SCHEDULED, JUSTIFIED EXCEPTION, OPEN | Pass |
| S7 | Research coverage | R1–R4 and C1–C5 each map to at least one RQ | Pass |
| S8 | Traceability coverage | Part A covers REF-01 §1–§18; Part B covers form sections 1–20 | Pass |
| S9 | Inflated-language scan | 14 listed terms in the S01 deliverables, `CLAUDE.md` and `README.md`. Hits are permitted only as listed examples in the style guide and gate protocol; each hit is printed with file and line | Pass (all hits are listed examples) |
| S10 | Identifying-data scan | Every committed text file: e-mail addresses, phone-like digit runs (ISO dates removed first) and URLs | Pass (none found) |
| S11 | Credential scan | Every committed text file: common token formats, private-key headers, assigned passwords or keys | Pass (none found) |
| S12 | File inventory | Only `.md`, `.py`, `.txt`, `.gitkeep`, `.gitignore` files; no reference documents; `CLAUDE.md`, `README.md`, `.gitignore` present | Pass |

**Limits of the script.** It checks structure, identifiers, coverage and surface patterns. It does not check meaning, fidelity to the source documents, accuracy of interpretations or writing quality.

## 3. Self-reported checks

| # | Check | Method | Result |
|---|---|---|---|
| M1 | R1–R4 source text matches REF-01 §7 word for word | Read REF-01 §7 and compared each line | Pass |
| M2 | C1 and C2 quoted text matches REF-01 §8 | Same method; C2 corrected in v1.1 (DEF-S01-07) | Pass after correction |
| M3 | C-series authority correctly assigned | Read origin of each item in REF-01 (statement body, evaluator section, working-copy annotation, collaboration restrictions) | Pass; assignment of the C2 second clause and C3 second sentence to working-copy annotation is a reading, flagged as such in the register |
| M4 | Interpretations separated from source text; no implied internal dataset | Read R1–R4 rows, glossary, traceability, issues | Pass after correction (DEF-S01-06; CLM-012 added) |
| M5 | RF/QA paraphrases faithful to REF-03 and not presented as quotations | Compared each row with REF-03 §2–§3 | Pass |
| M6 | No scope decision made by assumption | Checked ISS-001, ISS-016 and related text | Pass |
| M7 | Development stages kept distinct from work packages | Checked rules, glossary, gate criteria | Pass |
| M8 | Writing quality: specificity, unsupported qualifiers, terminology | Read changed sections against `03_STYLE_GUIDE.md` | Pass; "requirement" retained only in source text and form titles |
| M9 | No restructuring beyond the six corrections | Compared v1.1 with v1.0 by section | Pass; see `S01_CHANGE_REPORT.md` |
| M10 | Pre-commit review of staged files | Listed every staged path and searched for the repository owner's account name and the repository URL, which the script cannot check without containing them | Pass; see `S01_CHANGE_REPORT.md` §5 |

## 4. Defects (reassessed)

The v1.0 report stated "no defects". That was incorrect. The defects below were found at the owner's gate review or on reassessment.

| ID | Severity | Finding in v1.0 | Correction in v1.1 | Status |
|---|---|---|---|---|
| DEF-S01-01 | Major | C4–C6 presented alongside C1–C2 as constraints, implying sponsor-imposed product requirements | C-series classified SC / EA / PG with origin and authority; identifiers kept | Fixed |
| DEF-S01-02 | Major | QC report described checks as scripted and successful, but neither script nor output was delivered. The v1.0 identifying-data heuristic flagged every file (it matched dates); the resolution was a manual search, reported as if scripted. | Script and output delivered; checks classed scripted or self-reported; date exclusion built into the script | Fixed |
| DEF-S01-03 | Minor | Pattern scan reported as 13 terms; the script used 14 | Count now printed by the script | Fixed |
| DEF-S01-04 | Minor | Inconsistent header fields across files | Metadata standard (`00_PROJECT_RULES.md` §10) applied to all files; checked by S1 | Fixed |
| DEF-S01-05 | Major | Handoff listed inputs but assumed they would be available to a fresh session | Handoff procedure (`00_PROJECT_RULES.md` §4) and tiered file list with versions | Fixed |
| DEF-S01-06 | Major | R2 interpretation ("retrieve items from the sponsor-approved collection") implied that a populated collection exists | Interpretation made conditional; ISS-003 widened to existence; CLM-012 added; glossary updated | Fixed |
| DEF-S01-07 | Minor | C2 shown as source text but abbreviated ("the specific" omitted) | Quoted verbatim | Fixed |
| DEF-S01-08 | Minor | C3 (evaluator suggestion) presented as a constraint | Classified EA (advisory) | Fixed |
| DEF-S01-09 | Note | File count stated as 15 in a draft of v1.0, corrected to 16 before delivery | No action needed | Closed |

Open defects: none known. This statement is self-reported.

## 5. Remaining limitations

- No check in this report has been performed by an isolated reviewer.
- The repository is public (DEC-018); everything committed is published.
- REF-03 cannot be compared with the original reviewer record (ISS-020).
- Typography and table layout under RF-001 and RF-003 cannot be verified in Markdown (ISS-021).
