# S07_QC_REPORT

| Field | Value |
|---|---|
| Document ID | S07_QC_REPORT |
| Version | 1.0 |
| Status | SUBMITTED FOR GATE |
| Stage | S07 |
| Date | 2026-11-21 |
| Depends on | 00_STAGE_GATE_PROTOCOL; 03_STYLE_GUIDE; DEC-034; S07_PLAN; qc/S07_QC_CHECK.py; qc/S07_QC_CHECK_OUTPUT.txt |

- **Method key:** **Scripted** = reproducible with `python3 stages/S07/qc/S07_QC_CHECK.py .` from the repository root (standard library only; output delivered as `qc/S07_QC_CHECK_OUTPUT.txt`). **Self-reported** = performed by the drafting session by reading; not independently verified (gate protocol §6).

## 1. Scripted result

RESULT PASS: 1,097 checks, 0 failed, 102 information lines, 64 files (see the output file for the per-check list and SHA-256 of every deliverable). The script is cumulative: it re-runs every S04 to S06 check and adds section 8i for S07. Three S06 checks were adjusted because S07 legitimately changed approved content, and each adjustment is visible in the script: ISS-042, ISS-043 and ISS-045 may now carry "CORRECTED IN S07"; sources SRC-082 to SRC-090 are checked as S07 sources rather than S05 sources; the two GitHub repositories cited as sources (dataset author's scripts; Faiss) are added to the citation allowlist. The S06 script is expected to fail on the S07 tree (for example "S07 not started"); it remains valid for its own baseline.

## 2. Exit criteria (00_STAGE_GATE_PROTOCOL §7, S07 row)

| Criterion | Result | Method |
|---|---|---|
| Section 12 uses WP numbers and titles verbatim | Seven subsections; headings equal the Section 13 rows and the frozen WP register, in order | Scripted |
| Each tool or version verified or marked PROPOSED | Every row of the Section 12 tool table and of `S07_TOOL_AND_VERSION_REGISTER` carries a status; Pyserini release, requirements and licence and the Faiss licence verified with sources | Scripted (presence of labels); self-reported (fidelity of each label to its source) |
| Each Section 8 specification maps to a verification step | MS-01 to MS-10 and features 1, 2, 4, 5, 7, 8, 9 mapped in `S07_WP_METHOD_TRACEABILITY` §3 (MS-07, MS-09 marked not applicable) | Scripted |

## 3. Mandatory corrections (DEC-031) and S07 instruction (DEC-034)

| Item | Result | Method |
|---|---|---|
| ISS-042 MS-03 | Non-inferiority test with margin 0.10 in Section 8, evaluation design and Section 12; "never read as non-inferiority" stated; sample-size table recomputed | Scripted |
| ISS-043 absence | Pool-based metric names; lower-bound statement; old full-pool wording removed; ET-12 with Clopper–Pearson; three absence levels defined; bounds 0.308 and 0.168 recomputed | Scripted |
| ISS-044 CQADupStack | DS-01, DS-02 marked unusable; code and data licences distinguished; four-condition gate present; ISS-044 open | Scripted; the source reading is self-reported |
| ISS-045 BM25 | Section 8 MS-01, MS-02 require non-inferiority within 0.05 and say superiority is not required; old "Higher … than the BM25 baseline" wording absent; default-configuration rule and Holm present | Scripted |
| Seven elements per WP | Elements 1–7 present for WP1–WP7 in the traceability file; every deliverable and task referenced in its Section 12 activity; each activity names a validation step and a risk or open issue | Scripted (presence); self-reported (substance) |
| No personnel, hours, costs, schedule in Section 12 | None found | Scripted |
| No invented results | Result-language scan over Section 12 and S07 files | Scripted |
| Section 7 walk-through | Conditional in Section 7 v0.3 and Section 12 | Scripted |

## 4. Writing quality (03_STYLE_GUIDE; gate protocol §5)

| Check | Result | Method |
|---|---|---|
| Unmeasurable adjectives (REF-02 §12 gives two examples; the script scans for them and related words) and style-guide patterns | None in Section 12 body; repository-wide pattern scan passes | Scripted |
| Proposal-text form (RF-002) | Section 12 body is prose with one tool table; no bullet lists | Scripted |
| Specificity | Every Section 12 paragraph names a requirement, component, method, test, deliverable or issue | Self-reported |
| Template paragraphs | Activity subsections vary in structure (activity 1 leads with design scope, activity 2 with the licence gate, activity 5 with enforcement mechanics) | Self-reported |
| Length | Section 12 draft within the 5,500-word budget | Scripted |

## 5. Evidence

Nine sources added (SRC-082 to SRC-090) and one re-read (SRC-078), each with URL or DOI, tier, depth and the statement used. Two are T3 (SRC-079 from S05, SRC-085) and are used only as context for the conflicting-licence finding, never as sole support. SRC-087 is a clinical-trial guideline cited for a statistical principle, not for regulatory applicability; its replacement (SRC-088) is a draft whose text was not read. Holm and Clopper–Pearson are cited at abstract depth (A); their use is standard and full-text checks are scheduled for S08 Pass A. Self-reported.

## 6. Defects found and fixed during the stage

| # | Defect | Fix |
|---|---|---|
| 1 | First automated edit of `S05_EVALUATION_DESIGN` located the end of §8 by the first "MS-04" in the file, which lies earlier (ET-06 row); the guarded replacement aborted before writing | Search anchored after the start position; no file was damaged |
| 2 | Draft wording implied the EMA draft guideline retains the rule; only its status page was read | Sentence restricted to what was read |
| 3 | Source rows initially lacked an RQ link required by the source-log check; SRC-087 citation named a journal not verified | RQ links added; citation limited to the PMC copy |
| 4 | Section 12 activity 5 did not name D5.1 and D5.2 or an open issue; activity 4 omitted optional T4.6 | Sentences added |
| 5 | Risk IDs in Section 12 activities 1 and 3 did not match the S05 risk definitions | Corrected against `S05_FEASIBILITY_AND_RISKS` §4 |
| 6 | QC script constants with long digit runs tripped the identifying-data scan | Constants computed from the standard library instead |

## 7. Open points (none blocking the S07 gate)

| Severity | Point | Where it goes |
|---|---|---|
| Major (owner decision) | MS-03 non-inferiority is unlikely to be established at 30 need statements; parameters and post-pilot option needed | ISS-049 |
| Minor (owner decision) | ET-12 parameters and added judging effort | ISS-050; S10 |
| Minor | CQADupStack licence not established; T2.1 gate must pass before any use | ISS-044 |
| Minor | Patent service not chosen (EPO OPS recommended) | ISS-040 |
| Minor | Training-data terms of the candidate models and pinned versions | ISS-041; T1.5, D7.3 |
| Minor | Independent person for the deployment rehearsal | ISS-051; S10 |
| Note | Section 13 activity 6 effort does not yet include ET-12 judging | S10 (ISS-046, ISS-050) |
| Note | Statistical and licence sources read at abstract or landing-page depth | S08 Pass A; S09 |

## 8. Recommended gate outcome

CONDITIONAL PASS: the exit criteria and the four mandatory corrections are met in the working drafts; ISS-049 and ISS-050 need owner confirmation before the protocol freeze (T2.2), and ISS-044 remains a gate inside WP2, not a stage blocker. The owner decides the gate.
