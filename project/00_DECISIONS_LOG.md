# 00_DECISIONS_LOG

| Field | Value |
|---|---|
| Document ID | 00_DECISIONS_LOG |
| Version | 2.0 |
| Status | SUBMITTED FOR GATE |
| Stage | S02 |
| Date | 2026-11-20 |
| Depends on | Owner instructions as recorded in each entry |

- **Rule:** Entries are never deleted. A changed decision gets a new entry, and the old entry is marked SUPERSEDED with a pointer.

| ID | Date | Decision | Decided by | Status | Affects |
|---|---|---|---|---|---|
| DEC-001 | 2026-11-19 | The 10-stage development plan (S01–S10) is approved, with team, personal, final financial and schedule content deferred to S10. | Owner | ACTIVE | All stages |
| DEC-002 | 2026-11-19 | Research baseline: platform submissions are organizational, operational and technology needs or challenges submitted for assessment and identification of possible solutions, not software requirements specifications. | Owner (D1) | ACTIVE | R1–R4, RQ set, Sections 6–9, 12 |
| DEC-003 | 2026-11-19 | Long-term source of truth to be a private GitHub repository. | Owner (D2) | SUPERSEDED by DEC-010 | — |
| DEC-004 | 2026-11-19 | Reviewer feedback is supplied before substantive drafting; its criteria are integrated from S01. S09 verifies compliance rather than discovering criteria. | Owner (D3) | ACTIVE | All stages |
| DEC-005 | 2026-11-19 | No blanket policy against third-party Skills. A Skill checkpoint runs before each stage; no Skill is installed, run or trusted without explicit authorization and security review. Skill discovery is coordinated separately with the owner. | Owner (Correction 1) | ACTIVE | All stages |
| DEC-006 | 2026-11-19 | Natural, technically credible professional English is required in every deliverable from S01. S08 remains the intensive editorial stage. No synonym-swapping or AI-detector optimization. | Owner (Correction 2) | ACTIVE | All stages |
| DEC-007 | 2026-11-19 | An isolated critical-review context is used in S09 and after S10 integration (S10b), each subject to explicit authorization before execution. The reviewer uses the approved references, requirements, reviewer feedback and current deliverables, not the drafting conversation. | Owner (Correction 3) | ACTIVE | S09, S10 |
| DEC-008 | 2026-11-19 | Each stage uses a fresh session and durable handoff files; stable rules are kept concise. | Owner (Correction 4) | ACTIVE | All stages |
| DEC-009 | 2026-11-19 | Personally identifying, geographically identifying, jurisdiction-specific and locally restricted administrative information stays outside all working documents. Official-form fields requiring it remain local-completion placeholders. | Owner (Correction 5) | ACTIVE | All stages |
| DEC-010 | 2026-11-19 | Git and GitHub are removed from the workflow. The Claude Project with its reference documents is the working environment. Each stage ends with downloadable Markdown deliverables and is self-contained for a fresh session. Chat history is not the record of decisions. | Owner | PARTLY SUPERSEDED by DEC-017 (storage and handoff). Self-contained stages and files-as-record remain in force. | All stages |
| DEC-011 | 2026-11-19 | REVIEWER_FEEDBACK_EN_V1 is a consolidated secondary reconstruction. RF items are treated as reported reviewer criteria and QA items as additional quality observations; neither is presented as a direct quotation. | Owner | ACTIVE | Reviewer register, S08–S09 |
| DEC-012 | 2026-11-19 | The 10 development stages are kept distinct from the approximately 6–7 funded work packages in Section 13. | Owner | ACTIVE | S06–S08, Sections 12, 13, 16 |
| DEC-013 | 2026-11-19 | Writing-quality gates are mandatory at every stage; independent review is required for the final quality audit. | Owner | ACTIVE | All stages |
| DEC-014 | 2026-11-19 | Authorization to begin S01 using the three English reference documents. S02 does not start automatically. | Owner | ACTIVE | S01 |

| DEC-015 | 2026-11-20 | S01 gate: CONDITIONAL PASS. Conditions: (1) separate sponsor-origin constraints from project governance rules, keeping identifiers; (2) make QC checks reproducible or label them self-reported; (3) standardize document metadata; (4) define a practical handoff procedure for fresh Project sessions and the minimum file set for S02; (5) preserve research questions, reviewer mapping, verification rules and writing standards without unnecessary restructuring; (6) keep source text separate from interpretation and do not imply that a populated internal dataset exists. S02 not authorized until final approval. | Owner | ACTIVE | All S01 deliverables |

| DEC-016 | 2026-11-20 | Final approval of S01 after the DEC-015 corrections. S01 deliverables are APPROVED. S02 is not yet authorized. | Owner | ACTIVE | All S01 deliverables |
| DEC-017 | 2026-11-20 | GitHub-based storage adopted. The connected `iraa-proposal` repository is the persistent source of truth. Each approved stage is committed and pushed with an annotated `S0X-approved` tag; links are reported in chat. | Owner | ACTIVE (supersedes the storage and handoff parts of DEC-010) | All stages |
| DEC-018 | 2026-11-20 | Repository layout approved: `project/` (living documents), `stages/` (stage deliverables), `proposal/` (drafts). The repository is public. The three reference documents stay in the Claude Project and are not committed. No credentials, personal or geographic identifiers (including the account name or repository URL), private infrastructure details, unrelated files or unapproved material are committed. Nothing is pushed before stage approval. | Owner | ACTIVE | All stages |

| DEC-019 | 2026-11-20 | S02 authorized, subject to a read-only check that the required S01 files exist at the S01 baseline commit (check passed). | Owner | ACTIVE | S02 |
| DEC-020 | 2026-11-20 | The S01 baseline is commit 2b5f83c65749a4c697782216026a6291a91aa2a1. The tag push failure (HTTP 403) is not a blocker. Approved baselines are identified by commit SHA in `00_STAGE_STATUS.md`; a stage tag is added when the environment permits. | Owner | ACTIVE (closes ISS-027) | All stages |
| DEC-021 | 2026-11-20 | The owner authorized committing and pushing the finished S02 deliverables before the S02 gate decision. Pushed files carry status `SUBMITTED FOR GATE` until approved. This modifies the "no push before approval" rule of DEC-018 for S02. | Owner | ACTIVE | S02 |
| DEC-023 | 2026-11-20 | Fresh-thread stage workflow: the main Project conversation acts only as coordinator; each stage runs in one fresh thread that loads only `CLAUDE.md`, the stage status, the previous handoff and the registers it lists; workflow commands `START_STAGE` and `CLOSE_STAGE` defined in `CLAUDE.md`. Quality requirements unchanged. | Owner | ACTIVE | All later stages |

## Pending owner decision

| ID | Decision requested | Recommended |
|---|---|---|
| DEC-022 (proposed) | S02 gate outcome and authorization to begin S03 | Approve S02; begin S03 |
