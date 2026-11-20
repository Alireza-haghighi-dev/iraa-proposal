# S04_SCOPE_OPTIONS

| Field | Value |
|---|---|
| Document ID | S04_SCOPE_OPTIONS |
| Version | 1.0 |
| Status | SUBMITTED FOR GATE |
| Stage | S04 |
| Date | 2026-11-20 |
| Depends on | ISS-001; ISS-016; RF-011; RF-012; QA-003; CLM-039; CLM-040; S04_ARCHITECTURE; S04_ASSUMPTIONS_AND_STANDARDS |

- **Purpose:** give the owner the options for ISS-001 (development level of the current project) with their consequences, and a recommendation. The decision remains OWNER DECISION REQUIRED.
- **Labels:** option descriptions and the recommendation are PROPOSED. Maturity bands and prototype names are the proposal form's own terms (REF-02 §1, §5); the form's TRL mapping has not been validated for this project.

## 1. What the decision has to reconcile

RF-011 asks that the funding track not be confused with technical maturity, and that title, prototype type, current deliverables and classification agree. QA-003 records that an earlier rewrite described a delivered assistant while the scope was a feasibility proof of concept. RF-012 records that earlier conditional guidance (a former budget ceiling and mandatory training or consulting charges) rested on an incorrect funding-track assumption and was superseded. REF-03 does not name the track. Whatever track the proposal is filed under, the Section 5 maturity selection here follows from what the project will actually deliver.

Three facts constrain the choice. No production system exists and none may be implied (REF-03 §4.9). R1-type duplicate suggestion is already a documented market feature, so a project that demonstrates R1 alone shows little that is new; the design position in CLM-040 rests on linking R1, R2 and R4 results to one approved assessment record. Four inputs that a live deployment would need are outside the team's control and unresolved: data access (ISS-002), the internal collection (ISS-003), platform integration (ISS-008) and data-handling rules (ISS-009).

## 2. Options

| Option | Form maturity / prototype type | What exists at completion | Execution stages | Depends on |
|---|---|---|---|---|
| A. Feasibility study and proof of concept | Feasibility (form: roughly TRL 3 or below); experimental code, no prototype | Feasibility report; offline retrieval experiments for R1, R2 and R4 on a sanitized sample or proxy data; review-screen mock-up; architecture specification | Design, test | Proxy data at minimum |
| B. Laboratory prototype | Technology development (form: roughly TRL 4–6); laboratory prototype | Working assistant in a project-controlled or sponsor-provided isolated environment: FN-01 to FN-12 in `S04_ARCHITECTURE` §2; offline evaluation on a time-ordered, assessor-judged test set; a structured assessor walk-through of the R3 workflow; test and evaluation reports | Design, build, test | Exported or proxy data; one external patent source with usable terms (ISS-006); assessor time for judgments (ISS-012) |
| C. Pilot prototype integrated with the platform | Technology development, upper band; pilot prototype | Option B plus a live adapter to the sponsor's platform, use by assessors on incoming submissions in parallel with the normal process, operational logging | Design, build, test | Platform API and write rules (ISS-008); data-handling decision (ISS-009); sponsor infrastructure and accounts (ISS-035); documented joint support from the intended user, which the form says more advanced prototypes may require (REF-02 §1) |
| D. Product development | Product development (form: roughly TRL 7 or above) | Operational system | Build, test | A validated prototype, which does not exist |

## 3. Assessment against the constraints

| Criterion | A | B | C | D |
|---|---|---|---|---|
| Consistent with "no implied production system" (REF-03 §4.9) | Yes | Yes | Yes, if the pilot is described as parallel use | No |
| Can test the CLM-040 design position (linked R1/R2/R4 record approved by an assessor) | Partly: retrieval quality only, workflow on a mock-up | Yes, in a controlled environment | Yes, with live submissions | — |
| Can test R3 checkpoints CP-1 to CP-6 with real software | No | Yes | Yes | — |
| Depends on unresolved external inputs | Low | Moderate: degrades to proxy data if ISS-002 is negative; R2 runs on a proxy collection if ISS-003 is negative | High: ISS-002, ISS-003, ISS-008, ISS-009, ISS-035 all must be resolved before the work can start | — |
| Risk of title, deliverables and classification drifting apart (RF-011) | Low, but Section 8 then lists user requirements rather than measurable specifications (REF-02 §8) | Low if Section 8 specifications are targets tested in the project (S05) | Moderate: pilot results depend on sponsor-side events | High |
| Gives the next phase a usable starting point (Section 11) | Specification only | Prototype with defined platform adapter interface (IF-07) | Pilot evidence | — |

Option D is excluded. Option C is the stronger demonstration but would make the funded plan conditional on four sponsor-side decisions that the proposal cannot assume. Option A is the lowest-risk choice, but it cannot show the assessor workflow working, which is where the product differs from documented comparators.

## 4. Recommendation (PROPOSED; OWNER DECISION REQUIRED)

**Option B, a laboratory prototype under "technology development", with design, build and test execution stages.** It is the highest level the project can reach without assuming a platform integration, live data or sponsor infrastructure that REF-01 does not establish.

The recommendation holds with three explicit conditions, which Sections 7, 8 and 17 must repeat:

1. If sponsor data cannot be used (ISS-002), the prototype is evaluated on a sanitized or public proxy collection and every result is labelled as a proxy result (ISS-028).
2. If the approved internal collection does not exist in usable form (ISS-003, CLM-012), FN-05 is built and tested against a proxy collection, and R2 is described as a component ready for the sponsor's collection, not as a working R2 service.
3. The prototype is read-only toward the platform: it imports exported records and never writes outcomes back (AD-03). Live integration is Section 11 row 2.

If the owner prefers Option A, the architecture in `S04_ARCHITECTURE` remains the target design, FN-08 to FN-11 become a specified mock-up, and the Section 5, 7, 8 and 11 drafts are re-cut. If the owner prefers Option C, the owner must first supply the decisions on ISS-008, ISS-009 and ISS-035 and confirm that documented joint support from the intended user can be attached.

## 5. Consequences for later stages

| Stage | Consequence of Option B |
|---|---|
| S05 | Measurable specifications in Section 8 become test targets with conditions (proxy versus sponsor data); RQ-14 must confirm at least one patent source; RQ-15 sizes a self-hosted deployment (AD-09) |
| S06 | Work packages cover design, build and evaluation of a prototype; the platform adapter is specified (IF-07) but not built |
| S08 | Title pattern "Design, Development and Testing of a Laboratory Prototype of …" (REF-02 §1 example); ISS-015 |
| S10 | Duration and cost of Section 11 row 1 come from Sections 13 to 16 |
