"""S10 register alignment (DEF-002). Applies exact, one-time replacements and bumps file metadata.
Applied once in S10 (already applied; re-running fails its assertions by design). Run from the repository root: python3 stages/S10/qc/S10_ALIGN.py ."""
import re, sys, pathlib
root = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else ".")
NOTE = "- **S10 alignment (DEF-002, DEC-039):** wording aligned with the S09-corrected master (CP-1 always applied with disclosure clearance and query approval, DEC-035; EPO OPS thresholds as fair-use guidance, DEC-038; retention default, DEF-034). Content otherwise unchanged."
EDITS = {
"stages/S04/S04_DATA_FLOWS_AND_INTERFACES.md": [
 ("Query text (assessor-approved where CP-1 applies)", "Query text that has passed CP-1: disclosure clearance and assessor approval of the exact text (DEC-035)"),
 ("Query sent (with approval if CP-1 applies)", "Query sent, with its CP-1 disclosure clearance and assessor approval"),
 ("edit and approve query (CP-1, if applied)", "edit and approve query (CP-1; sent only with disclosure clearance)"),
 ("Where CP-1 applies, the assessor sees the exact text that would be sent and may shorten or redact it, and only the approved text leaves the controlled environment. Whether this control is needed depends on the owner's answer to ISS-033.",
  "CP-1 applies to every external query (DEC-035): the text must have disclosure clearance (a public record, or a recorded sponsor authorization covering the record and field), and the assessor sees the exact text that would be sent, may shorten or redact it, and approves it. Only cleared and approved text leaves the controlled environment. Query approval does not authorize disclosure; ISS-033 decides only whether text derived from sponsor submissions can be cleared."),
 ("| Query text (approved text only, where CP-1 applies) | CP-1 if selected;", "| Query text (cleared and approved text only, CP-1) | CP-1 on every query (DEC-035);"),
],
"stages/S04/S04_ARCHITECTURE.md": [
 ("FN-04, FN-07 and CP-1 to CP-4 added only by owner selection", "FN-04, FN-07 and CP-2 to CP-4 added only by owner selection; CP-1 required for every external query (DEC-035)"),
],
"stages/S05/S05_EVALUATION_DESIGN.md": [
 ("the approving assessor (CP-1, while external disclosure is not authorized, DEC-028)", "the disclosure clearance and the approving assessor (CP-1, required for every external query, DEC-035)"),
 ("Share of external queries with a logged approval of the exact text sent;", "Share of external queries with both a logged approval of the exact text sent and a disclosure clearance; unrefused attempts to send confidential text without authorization;"),
 ("| MS-05 | 100% of external queries have a logged approval of the exact text sent (while CP-1 applies) |", "| MS-05 | 100% of external queries have both a logged assessor approval of the exact text sent and a disclosure clearance; 0 unrefused attempts to send confidential text without authorization; manual-entry queries reported separately (DEC-035; master Section 8 specification 5) |"),
],
"stages/S05/S05_FEASIBILITY_AND_RISKS.md": [
 ("Fair-use policy: as a rule all OPS services tolerate ten searches per minute per IP address, a threshold that may vary with operational circumstances, and OPS is not designed for downloading entire collections.",
  "Fair-use guidance, not guaranteed limits (DEC-038): the charter gives approximately 1 Mbit per second for OPS (its 10 search-related actions per minute apply to Espacenet and the Register); the OPS FAQ states that as a rule OPS services tolerate ten searches per minute per IP address, a threshold that may be higher or lower depending on operational circumstances, one request per second for family-related actions, and that OPS is not designed for downloading entire collections."),
],
"stages/S06/S06_DELIVERABLES_AND_ACCEPTANCE.md": [
 ("Every external call passes through CP-1 while it applies;", "Every external call passes through CP-1 (disclosure clearance and assessor approval of the exact text, DEC-035); confidential text with an approved query but no authorization is refused;"),
 ("AS-08 manual-entry path works with the same fields", "AS-08 manual-entry path works with the same fields and records the exact query text and the clearance relied on"),
 ("| MS-05 | ET-08 in D6.3 | Applies while CP-1 applies |", "| MS-05 | ET-08 in D6.3 | Applies to every external query (DEC-035) |"),
],
"stages/S06/S06_DEPENDENCIES_AND_EFFORT.md": [
 ("| Delete at project close; no copy outside the environment |", "| Delete imported sponsor data, collections derived from it and cached external results at project close; retain and hand over public-source collections, judgment files and run files where licences permit; no copy of sponsor data outside the environment (DEF-034) |"),
 ("| CP-1 applies; ET-09 on Track P |", "| CP-1 applies to every query; no sponsor-derived text sent without authorization; ET-09 on Track P |"),
],
"stages/S07/S07_TOOL_AND_VERSION_REGISTER.md": [
 ("fair-use guide value of ten searches per minute", "fair-use guidance (charter: approximately 1 Mbit per second for OPS; OPS FAQ: ten searches per minute per IP address as a rule, varying with operational circumstances; neither guaranteed, DEC-038)"),
],
"stages/S07/S07_WP_METHOD_TRACEABILITY.md": [
 ("ten searches per minute fair-use guide value (VERIFIED, CLM-051)", "fair-use guidance as recorded in CLM-051 (VERIFIED; not guaranteed limits, DEC-038)"),
 ("| 100% of queries have a logged approval of the exact text sent (while CP-1 applies) |", "| 100% of queries have both a logged approval of the exact text sent and a disclosure clearance; 0 unrefused attempts without authorization (DEC-035) |"),
],
"project/02_CLAIM_REGISTER.md": [
 ("higher or lower depending on operational circumstances; not a guaranteed limit, DEC-038)", "higher or lower depending on operational circumstances, and one request per second for family-related actions; not a guaranteed limit, DEC-038)"),
 ("S05_FEASIBILITY_AND_RISKS, S07_WP_METHOD_TRACEABILITY and DRAFT_SEC12 keep the old wording (aligned at S10, DEF-002)", "S10: S05_FEASIBILITY_AND_RISKS, S07 registers aligned; DRAFT_SEC12 superseded by the master (DEF-002); FAQ re-read 2026-11-21 in S10"),
],
"project/02_SOURCE_LOG.md": [
 ("threshold may be higher or lower |", "threshold may be higher or lower; S10 re-read 2026-11-21: also \"a threshold of one request per second for family-related actions\"; robot access welcomed within limits, bulk download by robots up to 1 Mbit/second |"),
],
}
def bump(text, superseded=False):
    def ver(m):
        v = m.group(1); major = int(v.split(".")[0]); return f"| Version | {major+1}.0 |"
    text = re.sub(r"\| Version \| ([0-9.]+) \|", ver, text, count=1)
    text = re.sub(r"\| Status \| [A-Z ]+ \|", "| Status | SUPERSEDED |" if superseded else "| Status | DRAFT |", text, count=1)
    text = re.sub(r"\| Stage \| [^|]+ \|", "| Stage | S10 |", text, count=1)
    text = re.sub(r"\| Date \| [^|]+ \|", "| Date | 2026-11-21 |", text, count=1)
    return text
def add_note(text, note):
    lines = text.split("\n"); i = next(k for k,l in enumerate(lines) if l.startswith("| Depends on"))
    lines.insert(i+2, note); return "\n".join(lines)
registers = {"project/02_CLAIM_REGISTER.md", "project/02_SOURCE_LOG.md"}
for f, edits in EDITS.items():
    p = root/f; t = p.read_text()
    for a,b in edits:
        assert t.count(a) == 1, (f, a[:70]); t = t.replace(a,b)
    if f not in registers:
        t = add_note(bump(t), NOTE)
    p.write_text(t)
for f in sorted((root/"proposal").glob("DRAFT_SEC*.md")):
    t = bump(f.read_text(), superseded=True)
    t = add_note(t, "- **SUPERSEDED (S10, DEC-039):** this draft is superseded by `proposal/IRAA_PROPOSAL_EN_MASTER`, which carries all S08–S10 corrections (including DEF-002 items). Kept unchanged below as the approved stage input; do not use it as proposal text.")
    f.write_text(t)
print("alignment applied")
