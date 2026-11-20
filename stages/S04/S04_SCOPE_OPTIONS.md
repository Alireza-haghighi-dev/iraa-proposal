# S04_SCOPE_OPTIONS

| Field | Value |
|---|---|
| Document ID | S04_SCOPE_OPTIONS |
| Version | 1.1 |
| Status | SUBMITTED FOR GATE |
| Stage | S04.1 |
| Date | 2026-11-20 |
| Depends on | ISS-001; ISS-016; RF-011; RF-012; QA-003; CLM-039; CLM-040; CLM-045; CLM-046; DEC-029; S04_ARCHITECTURE; S04_ASSUMPTIONS_AND_STANDARDS |

- **Purpose:** give the owner the options for ISS-001 (development level of the current project) with their consequences, and a recommendation. The decision remains OWNER DECISION REQUIRED.
- **S04.1 status:** the recommendation is PROVISIONAL. It was audited in S04.1 against the proposal form, the reviewer criteria and the defined deliverables (§6) and is not approved. OWNER DECISION REQUIRED (ISS-001, ISS-016).
- **Labels:** option descriptions and the recommendation are PROPOSED. Maturity bands and prototype names are the proposal form's own terms (REF-02 §1, §5); the form's TRL mapping has not been validated for this project.

## 1. What the decision has to reconcile

RF-011 asks that the funding track not be confused with technical maturity, and that title, prototype type, current deliverables and classification agree. QA-003 records that an earlier rewrite described a delivered assistant while the scope was a feasibility proof of concept. RF-012 records that earlier conditional guidance (a former budget ceiling and mandatory training or consulting charges) rested on an incorrect funding-track assumption and was superseded. REF-03 does not name the track. Whatever track the proposal is filed under, the Section 5 maturity selection here follows from what the project will actually deliver.

Three facts constrain the choice. No production system exists and none may be implied (REF-03 §4.9). R1-type duplicate suggestion is already a documented market feature, and vendors also document scouting for existing companies and technologies that match a described need (CLM-046), so neither R1 nor R2 alone separates the product from them; the design position in CLM-040 is to bring R1, R2 and R4 results for one submission into a single assessor-approved record, and it is a position to evaluate, not a claimed advantage. Four inputs that a live deployment would need are outside the team's control and unresolved: data access (ISS-002), the sources of solution examples for R2 (ISS-003), platform integration (ISS-008) and data-handling rules (ISS-009).

## 2. Options

| Option | Form maturity / prototype type | What exists at completion | Execution stages | Depends on |
|---|---|---|---|---|
| A. Feasibility study and proof of concept | Feasibility (form: roughly TRL 3 or below); experimental code, no prototype | Feasibility report; offline retrieval experiments for R1, R2 and R4 on a sanitized sample or proxy data; review-screen mock-up; architecture specification | Design, test | Proxy data at minimum |
| B. Laboratory prototype | Technology development (form: roughly TRL 4–6); laboratory prototype | Working assistant in a project-controlled or sponsor-provided isolated environment: the essential functions in §6 (`S04_ARCHITECTURE` §2), plus any optional functions the owner selects; offline evaluation on a time-ordered, assessor-judged test set; a structured assessor walk-through of the R3 workflow; test and evaluation reports | Design, build, test | Exported or proxy data; one external patent source with usable terms (ISS-006); assessor time for judgments (ISS-012) |
| C. Pilot prototype integrated with the platform | Technology development, upper band; pilot prototype | Option B plus a live adapter to the sponsor's platform, use by assessors on incoming submissions in parallel with the normal process, operational logging | Design, build, test | Platform API and write rules (ISS-008); data-handling decision (ISS-009); sponsor infrastructure and accounts (ISS-035); documented joint support from the intended user, which the form says more advanced prototypes may require (REF-02 §1) |
| D. Product development | Product development (form: roughly TRL 7 or above) | Operational system | Build, test | A validated prototype, which does not exist |

## 3. Assessment against the constraints

| Criterion | A | B | C | D |
|---|---|---|---|---|
| Consistent with "no implied production system" (REF-03 §4.9) | Yes | Yes | Yes, if the pilot is described as parallel use | No |
| Can test the CLM-040 design position (linked R1/R2/R4 record approved by an assessor) | Partly: retrieval quality only, workflow on a mock-up | Yes, in a controlled environment | Yes, with live submissions | — |
| Can test the essential R3 controls (CP-5, CP-6) with real software | No | Yes | Yes | — |
| Depends on unresolved external inputs | Low | Moderate: degrades to proxy data if ISS-002 is negative; R2 is tested on labelled substitute data if ISS-003 confirms no source | High: ISS-002, ISS-003, ISS-008, ISS-009, ISS-035 all must be resolved before the work can start | — |
| Risk of title, deliverables and classification drifting apart (RF-011) | Low, but Section 8 then lists user requirements rather than measurable specifications (REF-02 §8) | Low if Section 8 specifications are targets tested in the project (S05) | Moderate: pilot results depend on sponsor-side events | High |
| Gives the next phase a usable starting point (Section 11) | Specification only | Prototype with defined platform adapter interface (IF-07) | Pilot evidence | — |

Option D is excluded. Option C is the stronger demonstration but would make the funded plan conditional on four sponsor-side decisions that the proposal cannot assume. Option A is the lowest-risk choice, but it cannot show the assessor workflow working, which is where the product differs from documented comparators.

## 4. Recommendation (PROPOSED; PROVISIONAL; OWNER DECISION REQUIRED)

**Option B, a laboratory prototype under "technology development", with design, build and test execution stages.** It is the highest level the project can reach without assuming a platform integration, live data or sponsor infrastructure that REF-01 does not establish.

The recommendation holds with three explicit conditions, which Sections 7, 8 and 17 must repeat:

1. If sponsor data cannot be used (ISS-002), the prototype is evaluated on a sanitized or public proxy collection and every result is labelled as a proxy result (ISS-028).
2. Until the owner confirms at least one solution-example source for R2 (ISS-003, ISS-037, CLM-045), FN-05 is built against the evidence-source interface and tested on labelled substitute data. R2 is then described as a function that has been tested on substitute data and is ready for a confirmed source, not as a working R2 service on sponsor data. No substitute dataset is named until S05.
3. The prototype is read-only toward the platform: it imports exported records and never writes outcomes back (AD-03). Live integration is Section 11 row 2.

If the owner prefers Option A, the architecture in `S04_ARCHITECTURE` remains the target design, FN-08 to FN-11 become a specified mock-up, and the Section 5, 7, 8 and 11 drafts are re-cut. If the owner prefers Option C, the owner must first supply the decisions on ISS-008, ISS-009 and ISS-035 and confirm that documented joint support from the intended user can be attached.

## 5. Consequences for later stages

| Stage | Consequence of Option B |
|---|---|
| S05 | Measurable specifications in Section 8 become test targets with conditions (proxy versus sponsor data); RQ-14 must confirm at least one patent source; RQ-15 sizes a self-hosted deployment (AD-09) |
| S06 | Work packages cover design, build and evaluation of a prototype; the platform adapter is specified (IF-07) but not built |
| S08 | Title pattern "Design, Development and Testing of a Laboratory Prototype of …" (REF-02 §1 example); ISS-015 |
| S10 | Duration and cost of Section 11 row 1 come from Sections 13 to 16 |

## 6. S04.1 audit of the recommendation (PROVISIONAL)

The audit compared Option B with the proposal form (REF-02 §1, §5, §7, §8, §11), the reviewer criteria (RF-005, RF-011, QA-003, QA-004, QA-010) and the deliverables defined in S04. It did not re-open Options A, C or D.

**Distinctions the proposal must keep explicit**

| Distinction | Position in the S04 package after correction | Where it is stated |
|---|---|---|
| Administrative funding track versus technological maturity | The funding track is not named in the reference documents. The maturity selection follows from the deliverable alone, as the form requires; the track neither sets nor limits it (RF-011) | §1; `proposal/DRAFT_SEC05_CLASSIFICATION` |
| Current funded deliverables versus future product capabilities | Funded: the essential set below and any options the owner selects. Future: platform adapter implementation, write-back, learning from decisions, adaptation for other organizations (Section 11 rows 2–4) | `S04_ARCHITECTURE` §2; `proposal/DRAFT_SEC07_OBJECTIVES`; `proposal/DRAFT_SEC11_CONTINUITY` |
| Proposed architecture versus implemented functionality | Nothing is implemented. Every FN, AC, IF, DF and AD item is PROPOSED; the drafts use future or conditional wording for the prototype | `S04_ARCHITECTURE` status note |
| Prototype evaluation versus live platform integration | Option B evaluates offline on exported or substitute data and never writes to the platform (AD-03). Live use belongs to Option C or Section 11 row 2 | §4 condition 3 |
| Proposed standards alignment versus certification | Design features that support the sponsor's own alignment; no certification or conformity claim (CLM-043) | `S04_ASSUMPTIONS_AND_STANDARDS` §3; Section 8 draft |

**Findings**

1. *Scope breadth.* As submitted, Option B committed all twelve functions and all six R3 checkpoints as current deliverables. Two functions (FN-04 grouping, FN-07 summaries) and four checkpoints (CP-1 to CP-4) are not required by R1–R4 as corrected. Committing them would widen the funded plan without a sponsor requirement behind them. Corrected: they are now owner-selectable options.
2. *R2 dependency.* Condition 2 assumed that an approved internal collection might exist. Corrected to the evidence-source interface with labelled substitute data (DEC-029).
3. *Classification wording.* The Section 5 and Section 11 drafts wrote the Option B selections as if chosen. Corrected: each selection is marked provisional pending ISS-001 and ISS-016.
4. *Form fit.* Option B matches the form's "technology development" band and its laboratory-prototype example, and it gives Section 8 a table of measurable specifications as the form asks for design and prototyping projects. The form's TRL mapping is the sponsor's and is not validated for this project (CLM-009); no TRL is claimed as achieved.
5. *Evidence of readiness.* No component, dataset or evaluation result exists. The recommendation is a judgement about what is reachable without sponsor-side inputs (CLM-044, PROPOSED), not evidence that the prototype will meet its targets.

**Option B, narrowed (PROVISIONAL)**

| Set | Functions and controls | Basis |
|---|---|---|
| Essential (current project) | FN-01, FN-02, FN-03 (R1), FN-05 (R2), FN-06 (R4), FN-08, FN-09 with CP-5 and CP-6 (R3), FN-11, FN-12 | R1–R4 as corrected; R3; evaluation needed for Section 8 targets |
| Recommended, low cost | FN-10 decision logging (export only, no retraining) | Supports C3 (advisory) and C1 |
| Owner-selectable options | FN-04 with CP-4 (ISS-004); FN-07 with CP-3 (ISS-009); CP-1 (ISS-033); CP-2 (ISS-034) | Not required by R1–R4; each adds effort to the funded plan |

The recommendation stays at Option B with this narrowed scope. It becomes the planning basis for S05 only after the owner records a decision on ISS-001 in DEC-028.
