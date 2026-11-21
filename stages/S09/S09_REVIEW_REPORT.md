# S09_REVIEW_REPORT

| Field | Value |
|---|---|
| Document ID | S09_REVIEW_REPORT |
| Version | 1.0 |
| Status | SUBMITTED FOR GATE |
| Stage | S09 |
| Date | 2026-11-21 |
| Depends on | S09_PLAN; IRAA_PROPOSAL_EN_MASTER v0.1 (f3265e8) and v0.2; S09_ISOLATED_REVIEW_RECORD; 03_DEFECT_LOG; 02_SOURCE_LOG; REF-01; REF-02; REF-03; DEC-037 |

- **Recommended gate outcome:** CONDITIONAL PASS. The S09 exit criteria (gate protocol §7) are met for the Markdown master: isolated review completed with authorization; no Critical or Major defect open (two Critical and fourteen Major found and fixed); every RF item ADDRESSED, SCHEDULED for S10 or local finalization, or JUSTIFIED EXCEPTION. Conditions: owner confirmation of the Section 9 classifications (ISS-054); significance-level choice (ISS-055) and EMA check (ISS-053) before the protocol freeze; native-template inspection and length target (ISS-056).
- **Independence:** the review was done twice. (1) This stage thread, a fresh session that did not draft the master. (2) An isolated reviewer agent, a separate model instance launched from this session, given only the baseline master, a digest of REF-02 with the corrected requirements, the style guide and the criteria register. Neither is an external human reviewer; "independent" in this report means only this. The agent's findings and their disposition are in `S09_ISOLATED_REVIEW_RECORD`.

## 1. Form and table fidelity (DEC-037 priority a)

| Check | Result | Evidence |
|---|---|---|
| 20 sections, REF-02 titles and order | Pass | Scripted (S08 suite, re-run by S09 script) |
| REF-02 header rows verbatim in Sections 5, 9, 10, 11, 13, 14, 15, 16, 17, 20 | Pass | Scripted |
| Section 9 cells use the form's categories | Failed at baseline, fixed: "Industry product", "Open-source research and industry initiative", parenthetical commentary in Outcome and Status (DEF-016, DEF-013) | REF-02 §9 category lists |
| Section 12 activity headings = Section 13 = Section 16; seven frozen titles | Pass | Scripted |
| Stale owner-decision placeholder for a resolved issue | Failed at baseline, fixed (DEF-012) | DEC-037 |
| Working identifiers in proposal prose | "S10" in running prose of Sections 14–16 and 20 fixed (DEF-038); `[OPEN — S10]` placeholders kept by project convention | Scripted |

Transfer risks into the native Word template, which has not been inspected (ISS-021, ISS-056): the working front matter (metadata table, bold notes) must be removed; Section 12 has four unnumbered subheadings mirroring the form's prompts and a tool table, neither of which REF-02 shows; Sections 8 and 12 hold project tables (REF-02 asks Section 8 for a specifications table without a schema); Section 16 has 12 month columns while the duration is open; Section 13 key-task cells hold 60–90 words each. No exact formatting compliance is claimed.

## 2. Cross-section dependencies (priority: Sections 8, 12, 13, 16, 17)

Verified after correction: each Section 8 specification maps to a Section 12 method and a Section 13 activity (spec 1–3 to activities 2 and 6; spec 4 and 6 to activity 5; spec 5 to activity 4; spec 7 to activities 3 and 6; spec 8 to activities 5 and 6). Defects found and fixed: the query editor for specification 3 differed between Sections 8, 12 and 13 (DEF-032); Section 7 promised test collections that the retention default deleted (DEF-034); risk 9 tested "any configuration" while activity 6 tests the selected one (DEF-039); Section 13 key tasks omitted the external prior-art statements and pool judging, although S06 costs the judging in T6.3 (DEF-037). Effort figures (2,004 person-hours, provisional) are unchanged and identical in Sections 4, 13 and 16 (scripted); recomputation remains S10.

## 3. Primary-source verification (priority b)

Depth key: D = page read directly in this session; P = full-text extract through search; A = abstract or landing-page extract. All accessed 2026-11-21.

| Statement in the master | Source | Depth | Result |
|---|---|---|---|
| CPMP points to consider: status | SRC-092 (EMA page) | D | Page carries a "superseded" notice |
| Replacement guideline status | SRC-088 (EMA page) | D | Draft, consultation 13/11/2025–31/05/2026, no adopted version or legal effective date: baseline wording misleading (DEF-010) |
| OPS rate limit "ten searches per minute" | SRC-071 (full fair-use charter) | D | Wrong service: limit applies to Espacenet and Register; OPS ~1 Mbit/s and 4 GB/week free, yearly flat rate above (DEF-011). Isolated agent reached the same finding independently |
| PQAI self-description, organization, offer | SRC-053 (repository), SRC-091 (project site) | D | MIT licence; models trained on past patent examination records; "collaborative initiative" of four named organizations; paid API tiers |
| SOLVENT result | SRC-055 (NSF public-access copy) | A | "Finds more analogies than baseline information-retrieval approaches"; baseline description of the method inaccurate (DEF-024) |
| Duplicate-report evaluation bias | SRC-010 (author PDF) | P | Qualitative statement confirmed; the 17–42% figure (DEF-003) found but not used |
| Automation bias | SRC-022 (PubMed and author-copy abstracts) | A | Confirmed |
| Significance tests in IR | SRC-066 (authors' PDF) | P | Confirmed |
| Vendor capabilities, Section 9 rows 1–4 | SRC-040, -041, -044, -046, -047, -048 | D | All statements confirmed; ITONICS "largest set" and Brightidea "only one" are not supportable as worded (DEF-014) |
| Pyserini 2.4.0, Python ≥ 3.12, Java 21, Apache-2.0 | SRC-078 | (agent) A | Confirmed by the isolated agent |
| Patent records US 11,561,987 B1, US 8,943,033 B2 | SRC-057, SRC-056 | (agent) A | Hold; the first only at description level (DEF-039) |

Not re-checked in S09 (depth unchanged, recorded in ISS-029): SRC-001, SRC-002, SRC-005 to SRC-008, SRC-012, SRC-025, SRC-026, SRC-034 to SRC-036, model cards SRC-037 and SRC-075 to SRC-077, SRC-089, SRC-090. None of their master statements was found doubtful by either review.

## 4. Statistics, R2 and disclosure (priorities e, f; owner items 6–7)

Statistics. The baseline stated two decision rules that can disagree: an unadjusted 95% interval decided non-inferiority, while Holm was said to control the family-wise error; the approved S07 §6 rule is that adjusted p-values decide (DEF-009, Critical). The sample-size check accepted a design with about a 50% chance of success at zero true difference (DEF-030, Critical). Specification 3 had a target the method itself expected to be untestable (DEF-022), no paired-binary interval method (DEF-031), no listed confirmatory family and an undefined "inferior" label (DEF-033). All fixed; the margins (0.05, 0.10) remain planning values awaiting owner confirmation. A remaining inconsistency between the one-sided family-wise 0.05 and two-sided 95% intervals is an owner decision before the freeze (DEF-025, ISS-055). EMA status: the master now states the draft status accurately and uses CPMP (2000) only for the closed-testing order (DEF-010; ISS-053 open).

R2. No assumed internal collection anywhere (scripted absence of withdrawn wording). One overgeneralization fixed: R2 retrieval was described as local-collection retrieval although a source may be reachable only externally (DEF-020).

Disclosure. The two-condition rule is complete in Sections 7, 8, 12, 13 and 17 after three fixes: a circular sentence (DEF-019), a Section 7 assumption that restated only the sponsor condition (DEF-036), and the manual-entry fallback, which did not record the exact query text (DEF-035).

## 5. Prose and length (priorities c, d)

Baseline 12,874 words (Python whitespace split); after corrections 12,870. About 550 words of corrections were offset by cutting repetition (vendor gap stated in Sections 5, 6 and 9; the ISO sentence three times; the assessor walk-through twice; the disclosure fallback four times; Section 12 risk endings repeating Section 17; the Section 13 introduction repeating Section 7). Unscoped universal claims were corrected (DEF-014, DEF-017, DEF-018). The remaining prose is specific; the main weakness is density in Section 12 (4,974 words, 39% of the text).

No page limit is known, and none is assumed. If the native template or sponsor guidance requires a shorter text (ISS-056), the following cuts keep every method, metric, rule, fallback and citation:

| Location | Cut | Approx. words |
|---|---|---|
| Section 12 activity 5 | Move implementation detail (password hashing, database role, hash chain, trigger) to the activity 1 design specification; keep the enforcement rule and its test | 120 |
| Section 12 activities 2–3 | Move file formats, judging-screen behaviour, normalization and vector-filter detail to the protocol and design specification | 220 |
| Section 12 tool table | Shorten status cells to "verified: licence, input limit; open: training-data terms" | 80 |
| Section 9 | Vendor paragraphs to capabilities and documented limits, about 60 words each | 150 |
| Sections 8, 17 | Shorten feature and mitigation cells to their operative clause | 230 |
| Section 7 | Merge objectives 1–4 into one paragraph each of two sentences | 120 |
| Section 6 | Fold the two literature paragraphs into one | 80 |

Total about 1,000 words (8%). Section 16 placeholder cells (about 250 words) disappear when S10 fills the schedule.

## 6. Reviewer criteria status after S09

RF-001 SCHEDULED (local finalization); RF-002 ADDRESSED in Markdown; RF-003 ADDRESSED in Markdown, native template PENDING; RF-004 ADDRESSED for S09; RF-005, RF-006, RF-007, RF-011, RF-012 ADDRESSED; RF-008 to RF-010 SCHEDULED for S10. QA-003 corrected to ADDRESSED (DEF-027); QA-005 ADDRESSED. Register: `project/S01_REVIEWER_CRITERIA_REGISTER.md`.

## 7. Defect summary

31 defects recorded (DEF-009 to DEF-039): Critical 2, Major 14, Minor 14, Note 1. Open: DEF-025, DEF-028 (Minor; owner decisions), DEF-029 (Note; S10 citation pass), with DEF-002 and DEF-005 from S08 and DEF-008 unchanged. One isolated finding was rejected: IR-14 (training-placement advice "not in the form") is a false positive, because REF-02 Section 13 does contain that advice and the digest given to the agent omitted it.
