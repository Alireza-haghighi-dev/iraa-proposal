#!/usr/bin/env python3
"""S10_QC_CHECK.py - reproducible checks for S10 (final integration), interim phase.

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

# ---- 0. Cumulative S09 run ------------------------------------------------------------
s9 = subprocess.run([sys.executable, os.path.join(ROOT, "stages", "S09", "qc", "S09_QC_CHECK.py"), ROOT],
                    capture_output=True, text=True)
m = re.search(r"SUMMARY\s+s09_checks=(\d+)\s+failed=(\d+)", s9.stdout)
info("S09 cumulative run", m.group(0) if m else "no summary")
SUPERSEDED = {
    "Master is v0.2, stage S09": "master v0.3 / S10 (checked below)",
    "S10 not started": "S10 started under DEC-039",
    "Master not longer than the S08 baseline": "replaced by the S10 body-length rule below",
    "Stage status records S09 submitted for gate": "stage status records S10 in progress (checked below)",
}
s9fail = [l for l in s9.stdout.splitlines() if l.startswith("FAIL")]
unexpected = [l for l in s9fail if not any(k in l for k in SUPERSEDED)]
add("S09 cumulative checks pass apart from the listed supersessions", not unexpected, " | ".join(unexpected)[:600])
for l in s9fail:
    if l not in unexpected: info("superseded S09 condition", l[6:120])

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
add("Master v0.3, stage S10, status DRAFT", "| Version | 0.3 |" in M and "| Stage | S10 |" in M and "| Status | DRAFT |" in M)
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
tot = re.search(r"Total effort \(provisional\): ([\d,]+) person-hours", sec(13))
add("Section 13 efforts sum to stated total", None not in e13 and tot and sum(e13) == num(tot.group(1)), "%s vs %s" % (sum(x or 0 for x in e13), tot.group(1) if tot else None))
add("Section 16 efforts equal Section 13 row by row", e16 == e13)
owner_done = "[OPEN — S10]" not in sec(14) + sec(15) + sec(16)
if owner_done:
    add("FX-02 Section 16 hours = Section 13 total", sum(e16) == sum(e13))
else:
    pend("FX-02 to FX-05 (hours, costs, weights, shares)", "await owner inputs; Sections 14-16 still hold placeholders")
add("Effort marked provisional while owner inputs are open", owner_done or "(provisional)" in sec(13))

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
add("Statistical level question stated (0.025 per family or 0.05 with 90% intervals)", "0.025 per family" in low and "90% intervals" in low)
for ph in ["approval of a query does not authorize disclosure", "query approval never substitutes for disclosure clearance",
           "checks whether relevant existing solution examples can be identified for a submitted need",
           "superiority tested second, not required", "has not been confirmed"]:
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
add("Malkov and Yashunin: journal record and DOI", "42(4), 824–836" in refs and "10.1109/TPAMI.2018.2889473" in refs)
cites = set(re.findall(r"\(([A-Z][A-Za-z\-]+)(?: et al\.| and [A-Z][A-Za-z\-]+)?,? (\d{4})\)", body))
cites |= set(re.findall(r"([A-Z][A-Za-z\-]+)(?: et al\.)? \((\d{4})\)", sec(6) + sec(9) + sec(12)))
missing = sorted({(a, y) for a, y in cites if not re.search(r"^%s.*\(%s\)" % (re.escape(a), y), refs, re.M)
                  and a not in ("ISO", "CPMP", "Section")})
add("Every author-year citation has a reference entry", not missing, str(missing))

# ---- 9. Effort recomputation in the decision request ---------------------------------------------
R = rd("stages", "S10", "S10_OWNER_DECISION_REQUEST.md") or ""
RT = R.split("| No. | Main activity | S06 planning | Proposed planning |")[-1]
add_low, add_pl, add_hi = 20*80*30/3600, 20*120*45/3600, 20*160*60/3600
q_low, q_pl, q_hi = 30*2*6/60, 30*2*10/60, 30*2*15/60
calc = [(round(add_low), round(add_pl), round(add_hi)), (round(q_low), round(q_pl), round(q_hi)), (4, 5, 7)]
tl, tp, th = (sum(c[i] for c in calc) for i in range(3))
add("Addition rows recompute (13/30/53, 6/10/15, 4/5/7)", calc == [(13, 30, 53), (6, 10, 15), (4, 5, 7)])
add("Added totals 23/45/75 stated", "| Total added | | | %d | %d | %d |" % (tl, tp, th) in R)
prop = [int(l.split("|")[4]) for l in RT.splitlines() if re.match(r"\| [1-7] \| ", l)]
s06 = [int(l.split("|")[3]) for l in RT.splitlines() if re.match(r"\| [1-7] \| ", l)]
add("Request S06 column equals Section 13 provisional figures", s06 == e13)
add("Proposed planning total = 2004 + 45 = 2049", sum(prop) == sum(e13) + tp == 2049 and "| Total | | 2004 | 2049 |" in R)
add("Proposed range 1,577 to 2,745 (S06 1,554 / 2,670 + additions)", "1,577 to 2,745" in R and 1554 + tl == 1577 and 2670 + th == 2745)
add("Person-weeks at 45 h: about 45.5", round(2049 / 45, 1) == 45.5 and "45.5 person-weeks" in R)

# ---- 10. Deliverables, records, safety ------------------------------------------------------------
for f in ["S10_PLAN", "S10_FORM_MAPPING", "S10_OWNER_DECISION_REQUEST", "S10_UNRESOLVED_ITEMS", "S10_CONSISTENCY_REPORT",
          "S10_CHANGE_REPORT", "S10_QC_REPORT", "S10_HANDOFF"]:
    t = rd("stages", "S10", f + ".md")
    add("Deliverable %s present with metadata" % f, bool(t) and "| Document ID | %s |" % f in t)
DL = rd("project", "00_DECISIONS_LOG.md") or ""
add("DEC-039 recorded", "| DEC-039 |" in DL)
ST = rd("project", "00_STAGE_STATUS.md") or ""
add("Stage status records S10 in progress, awaiting owner inputs", "S10 in progress" in ST)
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
