# S09_CORRECTION_REPORT

| Field | Value |
|---|---|
| Document ID | S09_CORRECTION_REPORT |
| Version | 1.0 |
| Status | SUBMITTED FOR GATE |
| Stage | S09 |
| Date | 2026-11-21 |
| Depends on | S09_REVIEW_REPORT; 03_DEFECT_LOG; IRAA_PROPOSAL_EN_MASTER v0.2 |

- **Scope:** every change made in S09, by file. Master: v0.1 → v0.2, 12,874 → 12,870 words. No requirement, work-package number or title, effort figure, margin, planning value or scope boundary was changed. The diff against f3265e8 is the complete record.

## 1. Master changes by section

| Section | Change | Defect |
|---|---|---|
| Front matter | v0.2, S09; note that metadata, notes and placeholders are removed before transfer | DEF-038 |
| 5 | Unreferenced "two further products" removed; vendor detail shortened to a pointer; parent-project sentence shortened | DEF-017, DEF-015 |
| 6 | Vendor gap scoped to the documentation read and "we found no"; auto-apply sentence removed (kept in Section 9); passage-first display labelled an untested design choice; benefits paragraph shortened | DEF-018, DEF-039, DEF-015 |
| 7 | Third objective: disclosure sentence rewritten; fifth objective: walk-through moved to Section 12 only; completion list: protocol, judgment and run files, licensable substitute collections; assumption restates both disclosure conditions; duplicate "not deployed" sentence removed | DEF-019, DEF-034, DEF-036, DEF-015 |
| 8 | Specifications 1–3: Holm-adjusted rule; specification 2: "no example found" rate reported without target; specification 3: editor defined, rule for both sizing outcomes; specification 5: manual-entry queries counted; specification 8: status and terms wording; planning paragraph: family-wise level, sample-size note, sizes per task and track; out-of-scope specification sentence removed; ISO/IEC 20000-1 reading stated; introduction shortened | DEF-009, DEF-022, DEF-032, DEF-035, DEF-039, DEF-026, DEF-015 |
| 9 | Introduction: resolved row selection stated, re-read date; Type/Outcome/Status cells bare form categories, qualifiers in Notes; PQAI row and paragraph from SRC-053 and SRC-091; ITONICS superlative removed; Brightidea claim scoped; Wazoku scope; SOLVENT from its abstract with published affiliations; patent embodiment wording; one closing differentiator paragraph replaces two per-vendor repetitions | DEF-012, DEF-013, DEF-014, DEF-016, DEF-024, DEF-039, DEF-015 |
| 11 | Evidence may be on substitute data | DEF-039 |
| 12 intro parts | R2 retrieval qualified; branch list replaced by pointer to Section 17 and activity 4; functions and exclusions point to Sections 7 and 8; ISO sentence removed; input-limit wording | DEF-020, DEF-015, DEF-023 |
| 12 activity 1 | Retention: sponsor data and derived collections deleted by default; public-source collections, judgments and runs handed over where licensed; risk ending shortened; "terms note" | DEF-034, DEF-015, DEF-039 |
| 12 activity 2 | CQADupStack narrative shortened; rule one: margin-shifted test, interval reported; CPMP cited for closed-testing order; EMA draft status stated; rule four: adjusted p-values decide, family listed, "inferior" defined; Clopper–Pearson limited to single proportions; paired score-type interval | DEF-015, DEF-009, DEF-010, DEF-033, DEF-031 |
| 12 activity 3 | Candidate-set wording; language sentence and risk ending moved to Section 17 pointer | DEF-021, DEF-015 |
| 12 activity 4 | OPS limits corrected; duplicate disclosure fallback removed; edited query confirmatory, unedited exploratory; manual route records exact text and clearance | DEF-011, DEF-015, DEF-032, DEF-035 |
| 12 activity 5 | Two duplicate sentences removed | DEF-015 |
| 12 activity 6 | 80% sample-size criterion per task and track; specification 3 options; union of ranks 11–50; "no supported difference" limited to secondary comparisons; risk ending shortened | DEF-030, DEF-022, DEF-039, DEF-033, DEF-015 |
| 12 activity 7 | Deletion limited to sponsor-derived data | DEF-034 |
| 13 | Introduction shortened; key tasks for external prior-art statements, queries and pools; "optionally edited"; manual entry records exact text | DEF-015, DEF-037, DEF-032, DEF-035 |
| 14, 15, 16, 20 | "S10" removed from running prose; Section 16 note on month columns | DEF-038, DEF-039 |
| 17 | Risk 9 refers to the selected configuration | DEF-039 |
| 19 | Status paragraph shortened; EMA draft guideline added to references | DEF-015, DEF-010 |

## 2. Register changes

| File | Change |
|---|---|
| `project/03_DEFECT_LOG.md` v2.0 | DEF-009 to DEF-039; DEF-003 and DEF-005 notes |
| `project/00_OPEN_ISSUES_REGISTER.md` v9.0 | ISS-014, ISS-029, ISS-032, ISS-049, ISS-053 progress; ISS-054 corrected for confirmation; ISS-055, ISS-056 added |
| `project/02_SOURCE_LOG.md` v8.0 | SRC-091, SRC-092 added; S09 depth notes on 14 entries; SRC-071 correction |
| `project/02_CLAIM_REGISTER.md` v8.0 | CLM-036, CLM-051 (corrected), CLM-060 |
| `project/S01_REVIEWER_CRITERIA_REGISTER.md` v9.0 | RF-001, RF-003, RF-004, QA-003, QA-005 statuses |
| `project/00_SKILL_REGISTER.md` v9.0 | SKL-010 |
| `project/00_STAGE_STATUS.md` v9.0 | S09 submitted; owner decisions table |

## 3. Not changed, by rule

Approved stage inputs (`DRAFT_SEC*`, S04–S07 files) keep their wording; their divergence from the master on the OPS limit and on retention is logged under DEF-002 and DEF-011/DEF-034 for alignment at S10. Section 13 and Section 16 effort figures are unchanged.
