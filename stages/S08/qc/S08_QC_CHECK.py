#!/usr/bin/env python3
"""S08_QC_CHECK.py - reproducible checks for S08 (integrated English master and editorial pass).

Usage (from the repository root):  python3 stages/S08/qc/S08_QC_CHECK.py .

Cumulative: runs stages/S07/qc/S07_QC_CHECK.py on the same tree and accepts only
two S07 failures that S08 legitimately supersedes, each re-checked here:
  (1) "S07: S08 not started" - S08 has started under DEC-036;
  (2) inflated-language hits in IRAA_PROPOSAL_EN_MASTER.md that fall inside the
      Section 19 reference list (titles of cited works, the same exemption the
      S07 script grants to 02_SOURCE_LOG citation rows).
Any other S07 failure fails this script. The S07 script also performs the
repository-wide credential, identifier and file-type scan.

S08 checks: 20 form sections in order; REF-02 table header rows verbatim;
Section 12/13/16 activity identity and effort sums; placeholders for reserved
fields; proposal-text form (no bold, no paragraph-opening bullets, no working
identifiers); ISS-052 disclosure wording; corrected methodology phrases;
withdrawn or prohibited claims; citation-to-reference and reference-to-source-log
traceability; register updates. It does NOT judge meaning or writing quality.
Standard library only. Reads files; writes nothing. Exit 0 = pass.
"""
import glob, os, re, subprocess, sys

ROOT = sys.argv[1] if len(sys.argv) > 1 else "."
res = []
def add(n, ok, d=""): res.append((n, "PASS" if ok else "FAIL", d))
def info(n, d): res.append((n, "INFO", d))
def rd(*p):
    f = os.path.join(ROOT, *p)
    return open(f, encoding="utf-8").read() if os.path.isfile(f) else None

# ---- 0. Cumulative S07 run -------------------------------------------------
master = rd("proposal", "IRAA_PROPOSAL_EN_MASTER.md") or ""
mlines = master.splitlines()
ref_start = next((i for i, l in enumerate(mlines) if l.startswith("References cited in this proposal")), None)
ref_end = next((i for i, l in enumerate(mlines) if l.startswith("## 20.")), None)
s7 = subprocess.run([sys.executable, os.path.join(ROOT, "stages", "S07", "qc", "S07_QC_CHECK.py"), ROOT],
                    capture_output=True, text=True)
s7fails = [l for l in s7.stdout.splitlines() if l.startswith("FAIL")]
m = re.search(r"SUMMARY\s+files=(\d+)\s+checks=(\d+)\s+failed=(\d+)", s7.stdout)
info("S07 cumulative run", m.group(0) if m else "no summary")
unexpected = []
for l in s7fails:
    if "S07: S08 not started" in l:
        info("S07 check superseded", "S08 not started -> S08 started under DEC-036")
        continue
    pm = re.search(r"IRAA_PROPOSAL_EN_MASTER\.md:(\d+) '(\w+)' FOUND IN TEXT", l)
    if pm and ref_start is not None and ref_end is not None and ref_start < int(pm.group(1)) - 1 < ref_end:
        info("S07 check superseded", f"citation title in Section 19 reference list, line {pm.group(1)} '{pm.group(2)}'")
        continue
    unexpected.append(l)
add("S07 cumulative checks pass apart from the two superseded checks", not unexpected, " | ".join(unexpected) or f"{len(s7fails)} superseded")

# ---- 1. Files and metadata --------------------------------------------------
NEED = [("proposal", "IRAA_PROPOSAL_EN_MASTER.md"), ("project", "03_DEFECT_LOG.md")] + \
       [("stages", "S08", f) for f in ["S08_PLAN.md", "S08_EDITORIAL_LOG.md", "S08_QC_REPORT.md",
                                       "S08_CHANGE_REPORT.md", "S08_HANDOFF.md"]]
for p in NEED:
    add(f"file present: {'/'.join(p)}", rd(*p) is not None)
FIELDS = ["Document ID", "Version", "Status", "Stage", "Date", "Depends on"]
for f in sorted(glob.glob(os.path.join(ROOT, "stages", "S08", "*.md"))):
    t = open(f, encoding="utf-8").read(); b = os.path.basename(f)
    mm = re.search(r"\| Field \| Value \|\n\|---\|---\|\n((?:\|.*\|\n)+)", t)
    rows = [re.match(r"\|\s*(.*?)\s*\|\s*(.*?)\s*\|$", x).groups() for x in mm.group(1).splitlines()] if mm else []
    v = dict(rows)
    ok = ([k for k, _ in rows] == FIELDS and v.get("Document ID") == b[:-3] and v.get("Stage") == "S08"
          and v.get("Status") == "SUBMITTED FOR GATE" and re.fullmatch(r"\d+\.\d+", v.get("Version", "")))
    add("S08 metadata header", bool(ok), b)
s9 = [x for x in glob.glob(os.path.join(ROOT, "stages", "S09", "*")) if not x.endswith(".gitkeep")]
add("S09 not started (stages/S09 holds no deliverables)", not s9, ", ".join(map(os.path.basename, s9)) or "empty")

# ---- 2. Sections and table schemas (REF-02) -------------------------------------
SECTIONS = ["Project title", "Team name", "Team lead and contact information", "Project duration and person-hours",
            "General project classification", "Necessity and significance", "Project objectives",
            "Main features and general/technical specifications", "Related research and comparable products",
            "Team’s prior research and relevant work", "Project continuity and future stages",
            "Detailed technical implementation method", "Activities and deliverables", "Implementation team",
            "Project budget", "Project Gantt schedule", "Project execution risks", "Completion date",
            "Other relevant remarks", "Attachments"]
heads = re.findall(r"^## (.+)$", master, re.M)
exp = [f"{i}. {s}" for i, s in enumerate(SECTIONS, 1)]
norm = lambda s: s.replace("'", "’")
add("20 form sections present in order, no other level-2 headings", [norm(h) for h in heads] == exp,
    f"{len(heads)} headings")
def sec(n):
    a = master.find(f"\n## {n}. "); b = master.find(f"\n## {n+1}. ") if n < 20 else len(master)
    return master[a:b] if a >= 0 else ""
SCHEMA = {
    5: "| Classification | Options / Selection |",
    9: "| No. | Research or product | Type | Executing organization / approved location descriptor | Outcome | Latest status | Notes / URL |",
    10: "| No. | Relevant research or product | Type | Approved organization descriptor | Outcome | Latest status | Notes |",
    11: "| Stage | Project title | Estimated duration (months) | Estimated cost (sponsor unit; local only) | High-level deliverable |",
    13: "| No. | Main activity | Activity deliverable(s) | Key tasks | Effort (person-hours) |",
    14: "| No. | Team member [local only] | Qualifications [local only] | Project responsibility | Monthly hours | Share of total effort (%) |",
    15: "| No. | Cost type | Item description | Quantity | Unit cost [local only] | Total [local only] |",
    16: "| No. | Main activity | Effort (person-hours) | " + " | ".join(f"Month {i}" for i in range(1, 13)) + " | Activity cost [local only] | Weight (%) |",
    17: "| No. | Risk category | Risk description | Mitigation |",
    20: "| Attachment category | Local completion status |"}
def tables(t):
    out, cur = [], []
    for l in t.splitlines():
        if l.startswith("|"): cur.append(l)
        elif cur: out.append(cur); cur = []
    if cur: out.append(cur)
    return out
def cells(l): return [c.strip() for c in l.strip().strip("|").split("|")]
for n, h in SCHEMA.items():
    tb = tables(sec(n))
    ok = len(tb) == 1 and tb[0][0] == h and re.fullmatch(r"\|( --- \|)+", tb[0][1]) and \
         all(len(cells(r)) == len(cells(h)) for r in tb[0][2:]) and len(tb[0]) > 2
    add(f"Section {n}: one table, REF-02 header verbatim, every row has {len(cells(h))} cells", bool(ok))
s5 = tables(sec(5))[0][2:] if tables(sec(5)) else []
add("Section 5: five classification rows in form order",
    [cells(r)[0] for r in s5] == ["Project type", "Reason", "Maturity", "Execution", "Relationship"])
add("Section 9: at least three comparator rows", len(tables(sec(9))[0]) - 2 >= 3 if tables(sec(9)) else False)
add("Section 9: provisional selection flagged with ISS-030", "[OWNER DECISION REQUIRED — ISS-030]" in sec(9))
add("Sections 8 and 12 hold only project tables (no REF-02 schema exists)",
    len(tables(sec(8))) == 2 and len(tables(sec(12))) == 1)

# ---- 3. Activities, effort, titles ----------------------------------------------
d13 = rd("proposal", "DRAFT_SEC13_ACTIVITIES.md") or ""
frozen = [(int(cells(r)[0]), cells(r)[1], int(cells(r)[4])) for r in tables(d13)[-1][2:]]
r13 = [cells(r) for r in tables(sec(13))[0][2:]]
t13 = [(int(c[0]), c[1], int(re.match(r"(\d+)", c[4]).group(1))) for c in r13]
add("Section 13: seven activities identical to the frozen titles and figures", t13 == frozen, str([x[2] for x in t13]))
add("Section 13: every effort cell marked provisional", all("(provisional)" in c[4] for c in r13))
tot = sum(x[2] for x in t13)
add("Section 13 total = 2,004 and stated in Sections 4 and 13", tot == 2004 and "2,004" in sec(4) and "2,004" in sec(13), str(tot))
h12 = re.findall(r"^### (\d)\. (.+)$", sec(12), re.M)
add("Section 12 numbered headings = Section 13 numbers and titles", [(int(a), b) for a, b in h12] == [(a, b) for a, b, _ in t13])
r16 = [cells(r) for r in tables(sec(16))[0][2:]]
add("Section 16: numbers, titles and effort identical to Section 13",
    [(int(c[0]), c[1], int(re.match(r"(\d+)", c[2]).group(1))) for c in r16] == t13)
add("Section 16: months, cost and weight left for S10 / local completion",
    all(all(x == "[OPEN — S10]" for x in c[3:15]) and c[15] == "[LOCAL COMPLETION ONLY]" and c[16] == "[OPEN — S10]" for c in r16))
r11 = [cells(r) for r in tables(sec(11))[0][2:]]
add("Section 1 title = Section 11 row 1 title; row 1 is the current project",
    r11[0][0] == "1 (current project)" and r11[0][1] == sec(1).strip().splitlines()[-1].strip())
add("Section 11: durations S10, costs local", all(c[2] == "[OPEN — S10]" and c[3] == "[LOCAL COMPLETION ONLY]" for c in r11))
cats = {cells(r)[1] for r in tables(sec(17))[0][2:]}
add("Section 17: categories from the form's four risk types", cats <= {"Technical", "Information and data", "Timeline", "Financial"} and len(cats) == 4, str(sorted(cats)))
add("Arithmetic: 10^6 x 1,024 x 4 bytes rounds to 4.1 GB", round(1e6 * 1024 * 4 / 1e9, 1) == 4.1 and "4.1 GB" in sec(12))

# ---- 4. Reserved fields -----------------------------------------------------------
for n in (2, 3, 18):
    body = "\n".join(sec(n).strip().splitlines()[1:]).strip()
    add(f"Section {n}: local completion placeholder only", body == "[LOCAL COMPLETION ONLY]", body[:60])
PH = re.compile(r"^\[(OPEN — S10|LOCAL COMPLETION ONLY)\]$")
for n in (10, 14, 15):
    rows = [cells(r) for r in tables(sec(n))[0][2:]]
    add(f"Section {n}: table rows hold placeholders only", all(PH.match(x) for r in rows for x in r))
add("Section 20: every status cell is local completion", all(cells(r)[1].startswith("[LOCAL COMPLETION ONLY]") for r in tables(sec(20))[0][2:]))
add("Section 4: duration and total effort reserved for S10", sec(4).count("[OPEN — S10]") == 2)

# ---- 5. Proposal-text form ------------------------------------------------------------
start = master.find("\n## 1. ")
body = master[start:]
blines = body.splitlines()
refblock = "\n".join(mlines[ref_start:ref_end]) if ref_start else ""
nonref = body.replace(refblock, "") if refblock else body
add("No bold or emphasis markup in proposal text", "**" not in body and not re.search(r"(?<![\w*])_[^_\s][^_]*_(?!\w)", body))
add("No paragraph-opening bullets in proposal text", not [l for l in blines if re.match(r"^\s*([-*•✓]|\d+\))\s", l)])
WID = re.compile(r"\b(R[1-4]|C[1-6]|MS-\d+|SRC-\d+|CLM-\d+|DEC-\d+|WP\d|T\d\.\d|D\d\.\d|FN-\d+|AC-\d+|CP-\d+|AD-\d+|IF-\d+|DF-\d+|PV-\d+|ET-\d+|RSK-\d+|AS-\d+|RF-\d+|QA-\d+|FX-\d+|F-\d+|EH-\d+|L-\d+|DS-\d+|DR-\d+|FT-\d+|RQ-\d+)\b")
hits = sorted({h for h in WID.findall(body)})
add("No working identifiers in proposal text", not hits, ", ".join(hits))
iss = re.findall(r"ISS-\d+", body); allowed = re.findall(r"\[OWNER DECISION REQUIRED — (ISS-\d+)\]", body)
add("ISS identifiers appear only inside owner-decision placeholders", sorted(iss) == sorted(allowed), ", ".join(iss))
add("No Persian or Arabic script anywhere in the repository Markdown",
    not any(re.search(r"[؀-ۿ]", open(p, encoding="utf-8").read())
            for p in glob.glob(os.path.join(ROOT, "**", "*.md"), recursive=True)))

# ---- 6. Mandatory corrections and prohibited claims ---------------------------------------
low = nonref.lower()
for ph in ["approval of a query does not authorize disclosure", "query approval never substitutes for disclosure clearance",
           "two separate conditions", "superiority tested second, not required", "non-inferiority not established",
           "is not required to be better than the bm25 baseline", "planning value", "lower bound",
           "makes bm25 the default configuration", "lists as superseded",
           "results on substitute data are reported as such"]:
    add(f"required wording present: '{ph}'", ph in low)
for ph in ["while external disclosure is not authorized", "unless external disclosure is otherwise authorized",
           "only if query approval is required", "approved internal collection", "internal precedent", "knowledge base",
           "outperform", "proven ", "guarantee", "state-of-the-art", "will revolution", "more accurate than",
           "conforms to iso", "compliant with iso", "iso-certified", "iso certified"]:
    add(f"withdrawn or prohibited wording absent: '{ph}'", ph not in low)
for word, neg in [("certif", r"\b(not|no)\b"), ("patentab", r"\bno\b"), ("freedom-to-operate", r"\b(not|no)\b")]:
    bad = [l for l in nonref.splitlines() if word in l.lower() and not re.search(neg, l.lower())]
    add(f"every '{word}' statement is negated", not bad, " | ".join(b[:80] for b in bad))
add("Section 12 effort-free: no person-hours or personnel in Section 12", not re.search(r"person-hours|\bhours\b", sec(12).replace("judging hours", "")))

# ---- 7. Citations and references ------------------------------------------------------------
refs = [l for l in mlines[ref_start + 1:ref_end] if l.strip()] if ref_start else []
cites = set()
for grp in re.findall(r"\(([^()]*?\d{4}[a-z]?)\)", nonref):
    for part in grp.split(";"):
        mm = re.match(r"\s*([A-Z][\w/\-’]+)(?:,? et al\.| and [A-Z][\w\-]+)?,? (\d{4})", part.strip())
        if mm: cites.add((mm.group(1), mm.group(2)))
for mm in re.finditer(r"\b([A-Z][\w\-]+)(?: et al\.| and [A-Z][\w\-]+)? \((\d{4})\)", nonref):
    cites.add((mm.group(1), mm.group(2)))
missing = sorted(f"{a} {y}" for a, y in cites if not any(r.startswith(a) and y in r for r in refs))
add("Every author-year citation has a Section 19 reference", not missing and len(cites) >= 20, f"{len(cites)} citations; missing: {', '.join(missing)}")
src = rd("project", "02_SOURCE_LOG.md") or ""
links = set(re.findall(r"https?://[^\s;]+", refblock + "\n" + sec(9)))
unlogged = []
for u in links:
    u = u.rstrip(".,)")
    key = ("doi:" + u.split("doi.org/")[1]) if "doi.org/" in u else u
    if key not in src and key.replace("https://www.", "https://") not in src and u.replace("https://", "https://www.") not in src:
        unlogged.append(u)
add("Every reference DOI or URL (Section 19 and Section 9) is logged in 02_SOURCE_LOG", not unlogged, ", ".join(sorted(unlogged)))
info("reference entries", str(len(refs)))

# ---- 8. Registers and propagation ------------------------------------------------------------
st = rd("project", "00_STAGE_STATUS.md") or ""; dl = rd("project", "00_DECISIONS_LOG.md") or ""
oi = rd("project", "00_OPEN_ISSUES_REGISTER.md") or ""; df = rd("project", "03_DEFECT_LOG.md") or ""
ar = rd("stages", "S04", "S04_ARCHITECTURE.md") or ""; ho = rd("stages", "S08", "S08_HANDOFF.md") or ""
add("Stage status: S08 SUBMITTED FOR GATE under DEC-036", "| Stage | S08 |" in st and "S08 SUBMITTED FOR GATE (DEC-036)" in st)
add("Decisions log: DEC-036 recorded", re.search(r"^\| DEC-036 \|", dl, re.M) is not None)
iss52 = next((l for l in oi.splitlines() if l.startswith("| ISS-052 |")), "")
add("ISS-052 marked resolved in the master, pending gate", "RESOLVED in the master" in iss52)
add("ISS-053 (EMA guideline supersession) registered", re.search(r"^\| ISS-053 \|", oi, re.M) is not None)
add("Defect log: DEF-001 to DEF-008 present", all(re.search(rf"^\| DEF-00{i} \|", df, re.M) for i in range(1, 9)))
cp1 = next((l for l in ar.splitlines() if l.startswith("| CP-1 |")), "")
add("S04_ARCHITECTURE CP-1 row carries the DEC-035 rule", "Approval never substitutes for clearance" in cp1 and "DEC-035" in cp1)
add("Handoff lists inputs and session start for S09", "## Inputs for S09" in ho and "## Session start (S09)" in ho)

# ---- Report ------------------------------------------------------------------------------------
for n, s, d in res:
    print(f"{s:5} {n}" + (f"  [{d}]" if d else ""))
fails = sum(1 for _, s, _ in res if s == "FAIL")
print(f"\nSUMMARY  s08_checks={len([r for r in res if r[1] != 'INFO'])}  failed={fails}  info={len([r for r in res if r[1] == 'INFO'])}")
print("RESULT " + ("PASS" if fails == 0 else "FAIL"))
sys.exit(1 if fails else 0)
