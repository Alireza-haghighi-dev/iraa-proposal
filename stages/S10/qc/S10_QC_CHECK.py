#!/usr/bin/env python3
"""S10_QC_CHECK.py - reproducible checks for S10 (final integration), resumed on the approved S11 baseline (DEC-042).

Usage (from the repository root):  python3 stages/S10/qc/S10_QC_CHECK.py . [path/to/PROPOSAL_FORM_EN_WORKING_V1.md]

Cumulative: runs stages/S09/qc/S09_QC_CHECK.py and accepts only the S09 failures that
S10 supersedes, each re-checked here. Then checks: form structure (20 sections, order,
headings); official table header rows verbatim against REF-02 when the form file is given
(REF-02 is not in the repository; without it the embedded copy of the header rows is used);
Section 12 / 13 / 16 / WP title identity; Section 13 and 16 effort arithmetic; FX-02 to FX-05
(PENDING until owner inputs); formatting markers; working identifiers; OPS wording; disclosure
and R2 wording; DEF-002 alignment; superseded drafts; citations; effort recomputation in the
decision request; deliverables; safety scan. It does not judge meaning or writing quality.
Standard library only. Exit 0 = pass.
"""
import glob, os, re, subprocess, sys

ROOT = sys.argv[1] if len(sys.argv) > 1 else "."
FORM = sys.argv[2] if len(sys.argv) > 2 else None
res = []
def add(n, ok, d=""): res.append((n, "PASS" if ok else "FAIL", d))
def info(n, d): res.append((n, "INFO", d))
def pend(n, d): res.append((n, "PENDING", d))
def rd(*p):
    f = os.path.join(ROOT, *p)
    return open(f, encoding="utf-8").read() if os.path.isfile(f) else None

# ---- 0. Cumulative S11 run (DEC-042) ----------------------------------------------------
# The approved S11 suite runs S09 (with S08, S07 and the safety scan). It is called with IRAA_SKIP_S10
# so that it does not call this script back. Its pre-approval checks that the approval made obsolete
# are accepted by name below and replaced by the baseline checks in section 4.
env = dict(os.environ, IRAA_SKIP_S10="1")
s11 = subprocess.run([sys.executable, "-B", os.path.join(ROOT, "stages", "S11", "qc", "S11_QC_CHECK.py"), ROOT],
                     capture_output=True, text=True, env=env).stdout
m = re.search(r"SUMMARY\s+s11_checks=(\d+)\s+failed=(\d+)", s11)
info("S11 cumulative run", m.group(0) if m else "no summary")
ACC_S11 = {
    "Master v0.4, stage S11": "master v0.5 / S10 after approval",
    "Section 4 states six months, provisional": "Section 4 states the approved six months and 1,291 h",
    "Effort labelled provisional in Section 13": "figures approved (DEC-042); labels removed",
    "Section 16 months not yet marked": "months marked from the approved distribution (checked in section 4)",
    "Stage status records S11 submitted for the owner checkpoint": "stage status records S11 approved",
    "No S11 file claims approval of the revised baseline": "S11 approved by DEC-042",
}
ACC_DEEP = {  # earlier-stage checks reported inside the S11 suite's S09 line
    "Section 13: every effort cell marked provisional": "approved figures",
    "Section 16: months, cost and weight left for S10": "months now marked; cost and weight still open",
    "Section 11: durations S10, costs local": "stage 1 duration 6 (approved); later stages open; costs local",
    "ISS-013 updated and still open": "resolved by DEC-042", "ISS-018 updated and still open": "resolved by DEC-040/DEC-042",
    "ISS-049 registered and open": "resolved by DEC-042", "ISS-050 registered and open": "resolved by DEC-042",
}
bad = []
for l in [x for x in s11.splitlines() if x.startswith("FAIL")]:
    if "S09 suite: only S11-superseded failures" in l:
        det = l.split("[", 1)[1].rsplit("]", 1)[0] if "[" in l else ""
        bad += [d.strip() for d in det.split(" | ") if d.strip() and not any(k in d for k in ACC_DEEP)]
    elif not any(k in l for k in ACC_S11):
        bad.append(l)
add("S11 cumulative checks pass apart from the listed supersessions", not bad, " | ".join(bad)[:600])

# ---- 1. Master structure ---------------------------------------------------------------
M = rd("proposal", "IRAA_PROPOSAL_EN_MASTER.md") or ""
body = M[M.find("## 1. Project title"):]
def sec(n):
    mm = re.search(r"^## %d\. .*?$(.*?)(?=^## \d+\. |\Z)" % n, body, re.M | re.S)
    return mm.group(1) if mm else ""
HEAD = ["Project title", "Team name", "Team lead and contact information", "Project duration and person-hours",
        "General project classification", "Necessity and significance", "Project objectives",
        "Main features and general/technical specifications", "Related research and comparable products",
        "Team's prior research and relevant work", "Project continuity and future stages",
        "Detailed technical implementation method", "Activities and deliverables", "Implementation team",
        "Project budget", "Project Gantt schedule", "Project execution risks", "Completion date",
        "Other relevant remarks", "Attachments"]
found = re.findall(r"^## (\d+)\. (.+)$", body, re.M)
add("20 sections in official order with form headings", [(int(a), b.strip()) for a, b in found] == list(enumerate(HEAD, 1)),
    str(found[:3]))
add("Master v0.5, stage S10, status DRAFT", "| Version | 0.5 |" in M and "| Stage | S10 |" in M and "| Status | DRAFT |" in M)
add("Master states it is not submission-ready", "Not submission-ready" in M)

# ---- 2. Official table header rows -----------------------------------------------------
EMB = {
 5: "| Classification | Options / Selection |",
 9: "| No. | Research or product | Type | Executing organization / approved location descriptor | Outcome | Latest status | Notes / URL |",
 10: "| No. | Relevant research or product | Type | Approved organization descriptor | Outcome | Latest status | Notes |",
 11: "| Stage | Project title | Estimated duration (months) | Estimated cost (sponsor unit; local only) | High-level deliverable |",
 13: "| No. | Main activity | Activity deliverable(s) | Key tasks | Effort (person-hours) |",
 14: "| No. | Team member [local only] | Qualifications [local only] | Project responsibility | Monthly hours | Share of total effort (%) |",
 15: "| No. | Cost type | Item description | Quantity | Unit cost [local only] | Total [local only] |",
 16: "| No. | Main activity | Effort (person-hours) | " + " | ".join("Month %d" % i for i in range(1, 13)) + " | Activity cost [local only] | Weight (%) |",
 17: "| No. | Risk category | Risk description | Mitigation |",
 20: "| Attachment category | Local completion status |",
}
src = "embedded copy"
if FORM and os.path.isfile(FORM):
    F = open(FORM, encoding="utf-8").read(); src = "REF-02 file"
    for n in EMB:
        fm = re.search(r"^## %d\. .*?$(.*?)(?=^## \d+\. |\Z)" % n, F, re.M | re.S)
        hdr = [l for l in fm.group(1).splitlines() if l.startswith("| ")][0] if fm else ""
        add("Embedded header for Section %d equals REF-02" % n, hdr.strip() == EMB[n])
info("Header source", src)
norm = lambda h: re.sub(r"\s*\|\s*", "|", h.strip())
for n, h in EMB.items():
    rows = [l for l in sec(n).splitlines() if l.startswith("| ")]
    add("Section %d table header verbatim" % n, bool(rows) and norm(rows[0]) == norm(h))
# column counts of data rows equal header column counts
for n, h in EMB.items():
    rows = [l for l in sec(n).splitlines() if l.startswith("| ") and not l.startswith("| ---")]
    k = h.count("|")
    add("Section %d rows keep the header's column count" % n, all(r.count("|") == k for r in rows))
# section 5 row labels
s5 = [l.split("|")[1].strip() for l in sec(5).splitlines() if l.startswith("| ") and not l.startswith("| ---")][1:]
add("Section 5 row labels unchanged", s5 == ["Project type", "Reason", "Maturity", "Execution", "Relationship"])
# only form-sanctioned extra tables: 8 (features, specifications) and 12 (tool table)
extra = {n: len([l for l in sec(n).splitlines() if l.startswith("| ---")]) for n in range(1, 21)}
expected = {5: 1, 8: 2, 9: 1, 10: 1, 11: 1, 12: 1, 13: 1, 14: 1, 15: 1, 16: 1, 17: 1, 20: 1}
add("Tables per section as mapped (8: two project tables; 12: one tool table)", all(extra[n] == expected.get(n, 0) for n in extra),
    str({n: v for n, v in extra.items() if v}))

# ---- 3. Titles: WP / 13 / 12 / 16 -------------------------------------------------------
WP = rd("stages", "S06", "S06_WORK_PACKAGES.md") or ""
wp = [r.split("|")[2].strip() for r in WP.splitlines() if re.match(r"\| WP[1-7] \| [A-Z]", r)][:7]
def tbl(n, col):
    return [l.split("|")[col].strip() for l in sec(n).splitlines() if re.match(r"\| \d+ \|", l)]
t13 = tbl(13, 2); t16 = tbl(16, 2)
t12 = [b.strip() for a, b in re.findall(r"^### (\d)\. (.+)$", sec(12), re.M)]
add("Seven frozen WP titles found in S06", len(wp) == 7)
add("Section 13 titles equal frozen WP titles, in order", t13 == wp)
add("Section 12 numbered titles equal Section 13 (FX-01)", t12 == t13)
add("Section 16 titles equal Section 13", t16 == t13)

# ---- 4. Effort arithmetic -----------------------------------------------------------------
num = lambda s: int(re.match(r"[\d,]+", s).group(0).replace(",", "")) if re.match(r"[\d,]+", s) else None
e13 = [num(x) for x in tbl(13, 5)]; e16 = [num(x) for x in tbl(16, 3)]
tot = re.search(r"Total effort: ([\d,]+) person-hours", sec(13))
add("Section 13 efforts sum to stated total", None not in e13 and tot and sum(e13) == num(tot.group(1)), "%s vs %s" % (sum(x or 0 for x in e13), tot.group(1) if tot else None))
add("Section 16 efforts equal Section 13 row by row", e16 == e13)
pend("FX-03 to FX-05 (costs, weights, shares)", "await personnel and cost inputs; Sections 14, 15 and the Section 16 cost columns still hold placeholders")
add("FX-02 Section 16 hours = Section 13 total = 1,291 (DEC-042)", sum(e16) == sum(e13) == 1291)
add("No effort cell still marked provisional", "(provisional)" not in sec(13) + sec(16))

# ---- 5. Formatting and identifiers ------------------------------------------------------------
add("No bold, bullets or decorative marks in proposal text", not re.search(r"\*\*|^\s*[-*•] |✓|✔|☐|☑", body, re.M))
ids = re.findall(r"\b(?:ISS|SRC|CLM|DEC|DEF|MS|ET|PV|AS|EH|FN|CP|AC|IF|DF|RF|QA|WP|RSK|DS|FT)-\d+", body)
add("No working identifiers in proposal text", not ids, str(sorted(set(ids)))[:200])
w9 = len(re.sub(r"\s+", " ", subprocess.run(["git", "-C", ROOT, "show", "c8470d6:proposal/IRAA_PROPOSAL_EN_MASTER.md"],
          capture_output=True, text=True).stdout.split("## 1. Project title", 1)[-1]).split())
wb = len(body.split())
add("Body length within S09 body + 50 words (S10 corrections allowance)", w9 and wb <= w9 + 50, "%d vs S09 %d" % (wb, w9))

# ---- 6. Technical corrections -------------------------------------------------------------------
low = body.lower()
a4 = sec(12).split("### 4.")[1].split("### 5.")[0].lower() if "### 4." in sec(12) else ""
add("OPS: thresholds called guidance values, not fixed limits", "guidance values, not fixed limits" in a4)
add("OPS: charter values (1 Mbit per second; 4 GB per week)", "1 mbit per second" in a4 and "4 gb per week" in a4)
add("OPS: FAQ values (ten per minute per IP as a rule; family-related one per second; operational variation)",
    "ten searches per minute per ip address as a rule" in a4 and "one request per second for family-related actions" in a4
    and "depending on operational circumstances" in a4)
add("OPS: Espacenet/Register charter value not attributed to OPS", "10 search-related actions" not in low)
for ph in ["approval of a query does not authorize disclosure", "query approval never substitutes for disclosure clearance",
           "checks whether relevant existing solution examples can be identified for a submitted need",
           "being better than bm25 is not required", "has not been confirmed"]:
    add("Required wording present: '%s'" % ph[:60], ph in low)
for bad in ["certified", "proven", "patentable", "guarantee", "state-of-the-art", "will reduce", "outperforms"]:
    add("Prohibited claim wording absent: '%s'" % bad, not re.search(r"\b%s\b" % bad, low.split("## 19.")[0]) or (bad == "certified" and "not certified" in low and low.count("certified") == low.count("not certified")))

# ---- 7. Register alignment (DEF-002) -----------------------------------------------------------
old = [r"while CP-1 applies", r"where CP-1 applies", r"CP-1 if selected", r"if CP-1 applies", r"CP-1, if applied",
       r"fair-use guide value of ten", r"Delete at project close; no copy outside the environment"]
live = [f for f in glob.glob(os.path.join(ROOT, "stages", "S0[4-7]", "*.md")) + glob.glob(os.path.join(ROOT, "project", "*.md"))
        if not re.search(r"(QC_REPORT|HANDOFF|CHANGE_REPORT|PLAN|CORRECTION_MATRIX|R2_REFERENCE)", f)]
hits = [(os.path.relpath(f, ROOT), p) for f in live for p in old
        if re.search(p, open(f, encoding="utf-8").read()) and "03_DEFECT_LOG" not in f and "00_DECISIONS_LOG" not in f]
add("DEF-002: outdated CP-1, OPS and retention wording absent from live registers", not hits, str(hits)[:300])
drafts = glob.glob(os.path.join(ROOT, "proposal", "DRAFT_SEC*.md"))
add("Section drafts marked SUPERSEDED", drafts and all("| Status | SUPERSEDED |" in open(f).read() for f in drafts))
D = rd("project", "03_DEFECT_LOG.md") or ""
for d in ["DEF-002", "DEF-029", "DEF-040", "DEF-041"]:
    row = next((l for l in D.splitlines() if l.startswith("| %s " % d)), "")
    add("%s recorded as FIXED" % d, "FIXED" in row.split("|")[-2] if row else False)

# ---- 8. Citations -------------------------------------------------------------------------------
refs = sec(19)
add("Removed references stay removed (S11)", not any(r in refs for r in ("Malkov,", "Holm,", "Bruch,", "Nogueira,")))
cites = set(re.findall(r"\(([A-Z][A-Za-z\-]+)(?: et al\.| and [A-Z][A-Za-z\-]+)?,? (\d{4})\)", body))
cites |= set(re.findall(r"([A-Z][A-Za-z\-]+)(?: et al\.)? \((\d{4})\)", sec(6) + sec(9) + sec(12)))
missing = sorted({(a, y) for a, y in cites if not re.search(r"^%s.*\(%s\)" % (re.escape(a), y), refs, re.M)
                  and a not in ("ISO", "CPMP", "Section")})
add("Every author-year citation has a reference entry", not missing, str(missing))

# ---- 9. Approved S11 baseline (DEC-042) -------------------------------------------------------------
import importlib.util, io, contextlib
sys.dont_write_bytecode = True
sp = importlib.util.spec_from_file_location("m", os.path.join(ROOT, "stages", "S11", "qc", "S11_EFFORT_MODEL.py"))
mod = importlib.util.module_from_spec(sp)
with contextlib.redirect_stdout(io.StringIO()): sp.loader.exec_module(mod)
APPROVED = [150, 168, 210, 138, 226, 267, 132]
add("Section 13 effort = DEC-042 approved figures = model", e13 == APPROVED == [mod.RL[w] + mod.RC[w] for w in range(1, 8)])
add("Section 4: 6 months and 1,291 person-hours", "Duration: 6 months. Total effort: 1,291 person-hours." in sec(4))
s11row = next((l for l in sec(11).splitlines() if l.startswith("| 1 (current project)")), "")
add("Section 11 stage 1 duration = 6", s11row.split("|")[3].strip() == "6" if s11row else False)
grow = {int(l.split("|")[1]): [c.strip() for c in l.split("|")[4:16]] for l in sec(16).splitlines() if re.match(r"\| [1-7] \|", l)}
ok = True
for w in range(1, 8):
    hrs = [sum((t[3] + t[4]) * t[5][mm] for t in mod.T if t[1] == w) for mm in range(6)]
    ok &= grow.get(w, [None])[:6] == ["X" if h > 0 else "" for h in hrs] and all(c == "" for c in grow[w][6:])
add("Section 16 month marks = approved month distribution; months 7-12 empty", ok)
add("Every activity scheduled in at least one month; month 1 and month 6 used", all("X" in grow[w] for w in grow)
    and any(grow[w][0] == "X" for w in grow) and any(grow[w][5] == "X" for w in grow))
dep = {2: 1, 3: 1, 4: 3, 5: 1, 6: 3, 7: 6}   # activity: predecessor whose first month must not be later
first = {w: grow[w].index("X") for w in grow}
add("Dependency order: no activity starts before its predecessor starts", all(first[w] >= first[d] for w, d in dep.items()))
add("Capacity risk (lead about 110 h per month) recorded in Section 17", "about 110 hours per month" in sec(17))
add("Weights and activity costs still open (await costs)", sec(16).count("[OPEN — S10]") == 7 and sec(16).count("[LOCAL COMPLETION ONLY]") == 7)
R = rd("stages", "S10", "S10_OWNER_DECISION_REQUEST.md") or ""
add("Decision request v0.2 issued on the approved baseline", "| Version | 0.2 |" in R and "DEC-042" in R)
C = rd("stages", "S10", "S10_RESOURCE_CALCULATIONS.md") or ""
wl = round(100 * 526 / 1291, 1)
add("Resource calculations: lead share 40.7% and contributor share 59.3% of 1,291 h", wl == 40.7 and "40.7%" in C and "59.3%" in C)
hw = [round(100 * x / 1291, 1) for x in APPROVED]
add("Resource calculations: hour-share weights listed and summing to 100% within rounding", all(("%.1f" % x) in C for x in hw) and abs(sum(hw) - 100) <= 0.2)

# ---- 10. Deliverables, records, safety ------------------------------------------------------------
for f in ["S10_PLAN", "S10_FORM_MAPPING", "S10_OWNER_DECISION_REQUEST", "S10_UNRESOLVED_ITEMS", "S10_CONSISTENCY_REPORT", "S10_RESOURCE_CALCULATIONS",
          "S10_CHANGE_REPORT", "S10_QC_REPORT", "S10_HANDOFF"]:
    t = rd("stages", "S10", f + ".md")
    add("Deliverable %s present with metadata" % f, bool(t) and "| Document ID | %s |" % f in t)
DL = rd("project", "00_DECISIONS_LOG.md") or ""
add("DEC-039 recorded", "| DEC-039 |" in DL)
ST = rd("project", "00_STAGE_STATUS.md") or ""
add("Stage status records S11 approved and S10 resumed", "S11 approved (DEC-042); S10 resumed" in ST)
add("DEC-042 recorded", "| DEC-042 |" in DL)
add("Skill checkpoint recorded for S10", "| SKL-011 | S10 |" in (rd("project", "00_SKILL_REGISTER.md") or ""))
allmd = "\n".join(open(f, encoding="utf-8").read() for f in glob.glob(os.path.join(ROOT, "**", "*.md"), recursive=True))
add("Safety: no account name, repository URL, e-mail or phone", not re.search(r"github\.com/[A-Za-z0-9-]+/iraa|@[a-z0-9-]+\.(com|org|ir)\b|\+\d{2}[ \d]{8,}", allmd, re.I))
add("No Persian text in repository", not re.search(r"[؀-ۿ]", allmd))
add("Submission readiness not claimed", not re.search(r"submission-ready\s*(?:status)?\s*[:=]?\s*(yes|true)|is submission-ready", allmd, re.I))

for n, s, d in res:
    print("%-7s %s%s" % (s, n, ("  [" + d + "]") if d else ""))
nf = sum(1 for r in res if r[1] == "FAIL")
print("\nSUMMARY  s10_checks=%d  failed=%d  pending=%d  info=%d" % (
    sum(1 for r in res if r[1] in ("PASS", "FAIL")), nf, sum(1 for r in res if r[1] == "PENDING"), sum(1 for r in res if r[1] == "INFO")))
print("RESULT", "PASS" if nf == 0 else "FAIL")
sys.exit(1 if nf else 0)
