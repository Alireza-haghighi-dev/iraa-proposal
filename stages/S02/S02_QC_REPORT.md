# S02_QC_REPORT

| Field | Value |
|---|---|
| Document ID | S02_QC_REPORT |
| Version | 1.0 |
| Status | SUBMITTED FOR GATE |
| Stage | S02 |
| Date | 2026-11-20 |
| Depends on | All S02 deliverables; updated living documents; S02_QC_CHECK.py; S02_QC_CHECK_OUTPUT.txt |

- **Performed by:** the drafting session. Nothing here is independently verified; independent review is reserved for S09 and S10b (DEC-007).
- **Recommended outcome:** PASS, with the open items in §5 carried forward.

## 1. Check classes

As defined in `00_STAGE_GATE_PROTOCOL.md` §6: **scripted** checks are reproducible with `python3 stages/S02/qc/S02_QC_CHECK.py .` from the repository root (output and SHA-256 file hashes in `stages/S02/qc/S02_QC_CHECK_OUTPUT.txt`); **self-reported** checks were done by reading.

## 2. Scripted checks

Final run: **PASS** (counts in the output file's SUMMARY line).

| # | Check | Result |
|---|---|---|
| S1 | Metadata header on every file in `project/`, `stages/S01/`, `stages/S02/` | Pass |
| S2–S5 | No duplicate definitions; complete sets (RF, QA, F, FX, RQ, SRC-001 to SRC-039); C-series classification; every referenced identifier defined (DEC-022 reported as pending) | Pass |
| S6–S8 | RF/QA status labels; RQ coverage of R1–R4 and C1–C5; traceability coverage of REF-01 §1–§18 and form sections 1–20 | Pass |
| S9 | Source-log rows complete: DOI or URL (or explicit bibliographic note), tier, depth, verification status, RQ link | Pass (39 rows) |
| S10 | Evidence matrix: every cited source is logged; no logged source is uncited; each active RQ (01–06, 08, 09) has at least one verified T1 source; every matrix row carries a label | Pass |
| S11 | Inflated-language scan, including `CLAUDE.md` and `README.md`. Hits allowed only as style-guide or gate-protocol examples, or inside citation titles in the source log | Pass (one citation-title hit, listed in the output) |
| S12 | Identifying-data scan: e-mail addresses, phone-like digit runs (dates, hashes, commit SHAs and DOIs removed first), repository or session URLs, local file paths | Pass |
| S13 | Credential scan and file inventory (no reference documents, only expected file types) | Pass |

Limits: the script checks structure, identifiers, coverage and surface patterns. It does not check whether a finding faithfully represents its source.

## 3. Self-reported checks

| # | Check | Method | Result |
|---|---|---|---|
| M1 | Every matrix finding matches the text retrieved for its source | Compared each row with the retrieved abstract, landing page or excerpt | Pass |
| M2 | Every number in the matrix appears in the source text retrieved | Checked: 65 h / 5 s (SRC-003); 9–19 points (SRC-004); 8 tasks, 58 datasets, 112 languages, 33 models (SRC-005); 27% MRR@10 (SRC-006); 2.3–2.7 nDCG, 440M vs 3B (SRC-032); 100+ languages, 8,192 tokens (SRC-033); 384 dimensions (SRC-037); 209,058 reports, 37–71%, 47% (SRC-009); 17–42% (SRC-010); 12 subforums (SRC-011); three studies (SRC-015); 21 contests, 4,191 ideas (SRC-017); 663 labels, F1 66% (SRC-020); 18 guidelines, 49 practitioners, 20 products (SRC-021); N = 199 (SRC-024); 51.5% and 74.5% (SRC-028); about 50% (SRC-029) | Pass |
| M3 | Bibliographic details | Authors, venue and DOI read from publisher, ACL Anthology, arXiv or indexing pages. Three author lists checked separately; one corrected before logging (DEF-S02-01) | Pass |
| M4 | Transfer kept separate from evidence | Applicability column and synthesis label transfer as ASSUMPTION; candidate approaches labelled PROPOSED | Pass |
| M5 | No tools, versions or architecture chosen | Synthesis §3 lists candidates only | Pass |
| M6 | Writing quality | Synthesis and matrix read against `03_STYLE_GUIDE.md`: each paragraph cites matrix rows; adjectives either removed or attributed | Pass after DEF-S02-02 |
| M7 | Balance and disclosure | Vendor affiliation disclosed for SRC-008; negative findings (thin direct evidence, gaps) reported | Pass |

## 4. Defects

| ID | Severity | Finding | Action | Status |
|---|---|---|---|---|
| DEF-S02-01 | Minor | The expected author list for the idea-relationship paper (SRC-013) was wrong | Verified on the publisher page before logging: Westerski, Iglesias, Espinosa Garcia | Fixed |
| DEF-S02-02 | Minor | Our own text repeated a source's evaluative adjective for BM25 (matrix 1.2, CLM-013) | Replaced with a description of what was found | Fixed |
| DEF-S02-03 | Note | The QC script flagged digit runs in DOIs and commit SHAs, and its own path pattern | Script adjusted; adjustments visible in the script | Closed |
| DEF-S02-04 | Minor | Mitigators of automation bias (SRC-023) could not be verified; the abstract page was blocked | Mediators only reported; mitigators marked OPEN in matrix row 5.3 | Open |

## 5. Limitations and carried items

- Most sources are verified at abstract or landing-page depth (A). Any quantitative claim reused in the proposal needs a full-text check in S08 Pass A.
- Direct evidence for the sponsor's task is thin (matrix 3.1); no benchmark of need/challenge submissions was found (ISS-028).
- RQ-07 remains inactive pending ISS-007.
- The S01 QC script validates the S01 baseline; run it against commit 2b5f83c, not the current tree, because S02 adds files with citation URLs.
