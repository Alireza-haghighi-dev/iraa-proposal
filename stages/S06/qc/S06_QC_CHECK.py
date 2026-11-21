#!/usr/bin/env python3
"""S06_QC_CHECK.py - reproducible structural checks for S06 (Main Activities, Deliverables and Work Packages).

Usage (from the repository root):  python3 stages/S06/qc/S06_QC_CHECK.py .
Cumulative: all S04, S04.1 and S05 checks (below) plus the S06 checks in section 8h.
The S05 check "S06 not started" is replaced by "S07 not started".
S05 description: all S04 and S04.1 checks plus the S05 checks in section 8g.
Original S04 description follows.
Checks the living documents in project/, the stage files in stages/S01/
to stages/S04/ and the proposal drafts in proposal/: all S03 checks, plus
S04 architecture identifiers, R3 checkpoints, traceability Part F, the
Section 5 and Section 11 draft schemas, Section 8 specification labels and
certification wording. It also scans every
committed text file in the repository for credentials, identifying data and
unexpected file types.
Requires only the Python 3 standard library. Reads files; writes nothing.
Exit code 0 = all FAIL-capable checks passed; 1 = at least one failed.

Scope: structure, identifiers, coverage, metadata and pattern scans.
It does NOT check meaning, source fidelity or writing quality; those are
self-reported in S03_QC_REPORT.md and reserved for independent review.
"""
import glob, hashlib, os, re, sys

ROOT = sys.argv[1] if len(sys.argv) > 1 else "."
DELIV = sorted(glob.glob(os.path.join(ROOT, "project", "*.md")) +
               glob.glob(os.path.join(ROOT, "stages", "S01", "*.md")) +
               glob.glob(os.path.join(ROOT, "stages", "S02", "*.md")) +
               glob.glob(os.path.join(ROOT, "stages", "S03", "*.md")) +
               glob.glob(os.path.join(ROOT, "stages", "S04", "*.md")) +
               glob.glob(os.path.join(ROOT, "stages", "S04.1", "*.md")) +
               glob.glob(os.path.join(ROOT, "stages", "S05", "*.md")) +
               glob.glob(os.path.join(ROOT, "stages", "S06", "*.md")) +
               glob.glob(os.path.join(ROOT, "proposal", "*.md")))
FILES = {os.path.basename(p): open(p, encoding="utf-8").read() for p in DELIV}
ALL = sorted(p for p in glob.glob(os.path.join(ROOT, "**", "*"), recursive=True)
             + glob.glob(os.path.join(ROOT, "**", ".*"), recursive=True)
             if os.path.isfile(p) and os.sep + ".git" + os.sep not in p + os.sep
             and not p.endswith(os.sep + ".git"))
results = []  # (check, PASS/FAIL/INFO, detail)

def add(name, ok, detail=""):
    results.append((name, "PASS" if ok else "FAIL", detail))

def info(name, detail):
    results.append((name, "INFO", detail))

def need(fname):
    if fname not in FILES:
        add(f"file present: {fname}", False, "missing")
        return ""
    return FILES[fname]

# 0. Inventory with SHA-256 so results can be tied to exact file versions
for f, t in FILES.items():
    info("sha256", f"{hashlib.sha256(t.encode('utf-8')).hexdigest()}  {f}")

# 1. Metadata header (00_PROJECT_RULES section 10)
FIELDS = ["Document ID", "Version", "Status", "Stage", "Date", "Depends on"]
STATUS = {"DRAFT", "SUBMITTED FOR GATE", "APPROVED", "SUPERSEDED"}
for f, t in FILES.items():
    m = re.search(r"\| Field \| Value \|\n\|---\|---\|\n((?:\|.*\|\n)+)", t)
    if not m:
        add("metadata header", False, f"{f}: no header table"); continue
    rows = [re.match(r"\|\s*(.*?)\s*\|\s*(.*?)\s*\|$", l).groups()
            for l in m.group(1).splitlines()]
    keys = [k for k, _ in rows]; vals = dict(rows)
    problems = []
    if keys != FIELDS: problems.append(f"fields {keys}")
    if vals.get("Document ID") != f[:-3]: problems.append("Document ID != file name")
    if not re.fullmatch(r"\d+\.\d+", vals.get("Version", "")): problems.append("version format")
    if vals.get("Status") not in STATUS: problems.append(f"status '{vals.get('Status')}'")
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", vals.get("Date", "")): problems.append("date format")
    if not vals.get("Depends on"): problems.append("empty Depends on")
    add("metadata header", not problems, f"{f}" + (": " + "; ".join(problems) if problems else ""))

# 2. Register definitions and duplicates
def defined(prefix, fname):
    return re.findall(r"^\|\s*(" + prefix + r"-\d+)\s*\|", need(fname), re.M)

REG = {
    "ISS": "00_OPEN_ISSUES_REGISTER.md", "DEC": "00_DECISIONS_LOG.md",
    "CLM": "02_CLAIM_REGISTER.md", "REF": "02_SOURCE_LOG.md",
    "SKL": "00_SKILL_REGISTER.md", "RF": "S01_REVIEWER_CRITERIA_REGISTER.md",
    "QA": "S01_REVIEWER_CRITERIA_REGISTER.md", "F": "S01_REQUIREMENTS_REGISTER.md",
    "FX": "S01_REQUIREMENTS_REGISTER.md", "CTX": "S01_REQUIREMENTS_REGISTER.md",
    "RQ": "S01_RESEARCH_QUESTIONS.md", "SRC": "02_SOURCE_LOG.md",
}
DEFS = {}
for k, fname in REG.items():
    if k == "RQ":  # RQs are defined in section 2 of the file
        text = need(fname)
        sec2 = text[text.find("## 2."):text.find("## 3.")]
        ids = re.findall(r"^\|\s*(RQ-\d+)\b", sec2, re.M)
    else:
        ids = defined(k, fname)
    DEFS[k] = set(ids)
    dups = sorted({i for i in ids if ids.count(i) > 1})
    add(f"no duplicate {k} definitions", not dups, ", ".join(dups) or f"{len(ids)} defined")

# 3. Required sets complete
def want(k, n, w):
    return {f"{k}-{i:0{w}d}" for i in range(1, n + 1)}
for k, n, w in [("RF", 12, 3), ("QA", 10, 3), ("F", 20, 2), ("FX", 12, 2), ("RQ", 15, 2), ("SRC", 81, 3), ("CLM", 57, 3), ("ISS", 48, 3)]:
    miss = sorted(want(k, n, w) - DEFS[k])
    add(f"complete set {k}", not miss, ", ".join(miss) or f"{n}/{n}")
req = need("S01_REQUIREMENTS_REGISTER.md")
for r in ["R1", "R2", "R3", "R4"]:
    add(f"requirement {r} registered", bool(re.search(r"^\| " + r + r" \|", req, re.M)))
CLASS = {"C1": "SC", "C2": "SC", "C3": "EA", "C4": "PG", "C5": "PG", "C6": "PG"}
for c, cls in CLASS.items():
    row = re.search(r"^\| " + c + r" \|.*$", req, re.M)
    ok = bool(row) and re.search(r"\|\s*" + cls + r"\b[^|]*\|", row.group(0)) is not None
    add(f"{c} registered with classification {cls}", ok)

# 4. Reference integrity: every referenced ID is defined
proposed = set(re.findall(r"\|\s*(DEC-\d+) \(proposed\)", need("00_DECISIONS_LOG.md")))
allt = "\n".join(FILES.values())
for k in REG:
    refs = set(re.findall(r"\b(" + k + r"-\d+)\b", allt))
    undef = sorted(refs - DEFS[k] - proposed)
    add(f"all {k} references defined", not undef, ", ".join(undef) or f"{len(refs)} referenced")
info("proposed (pending) decisions", ", ".join(sorted(proposed)) or "none")

# 5. RF / QA status labels
LABELS = ("ADDRESSED", "SCHEDULED", "JUSTIFIED EXCEPTION", "OPEN")
rv = need("S01_REVIEWER_CRITERIA_REGISTER.md")
for rid in sorted(DEFS["RF"] | DEFS["QA"]):
    row = re.search(r"^\| " + rid + r" \|.*$", rv, re.M).group(0)
    cells = [c.strip() for c in row.strip("|").split("|")]
    status = cells[-2] if len(cells) >= 2 else ""
    add("RF/QA status label", status.startswith(LABELS), f"{rid}: {status}")

# 6. RQ coverage of R1-R4 and C1-C5
rq = need("S01_RESEARCH_QUESTIONS.md")
cov = rq[rq.find("## 3."):]
for item in ["R1", "R2", "R3", "R4", "C1", "C2", "C3", "C4", "C5"]:
    row = re.search(r"^\| " + item + r"\b.*$", cov, re.M)
    add(f"RQ coverage {item}", bool(row) and "RQ-" in row.group(0))

# 7. Traceability Part A covers REF-01 sections 1-18
tm = need("S01_TRACEABILITY_MATRIX.md")
parta = tm[tm.find("## A."):tm.find("## B.")]
missing = [str(i) for i in range(1, 19) if not re.search(r"^\| §" + str(i) + r"(\.\d)? ", parta, re.M)]
add("traceability Part A covers REF-01 §1-§18", not missing, ", ".join(missing) or "18/18")
partb = tm[tm.find("## B."):tm.find("## C.")]
secs = [str(i) for i in range(1, 21) if not re.search(r"^\| " + str(i) + r" \|", partb, re.M)]
add("traceability Part B covers form sections 1-20", not secs, ", ".join(secs) or "20/20")

# 8. Inflated-language pattern scan. Hits are allowed only where the style
#    guide or gate protocol lists the words as examples.
PATTERNS = ["crucial", "paramount", "cutting-edge", "state-of-the-art", "revolutioni",
            "seamless", "leverag", "in today", "robust", "comprehensive", "game-chang",
            "delve", "holistic", "unlock"]
EXEMPT = {"03_STYLE_GUIDE.md", "00_STAGE_GATE_PROTOCOL.md"}
SCAN = dict(FILES)
for entry in ("CLAUDE.md", "README.md"):
    ep = os.path.join(ROOT, entry)
    if os.path.isfile(ep):
        SCAN[entry] = open(ep, encoding="utf-8").read()
for f, t in SCAN.items():
    for n, line in enumerate(t.splitlines(), 1):
        for p in PATTERNS:
            if p in line.lower():
                exempt = f in EXEMPT and ('"' in line or "“" in line or "|" in line)
                cite = f == "02_SOURCE_LOG.md" and line.startswith("| SRC-")
                exempt = exempt or cite
                tag = ("citation title (exempt)" if cite else "example usage (exempt)") if exempt else "FOUND IN TEXT"
                if exempt:
                    info("pattern scan", f"{f}:{n} '{p}' {tag}")
                else:
                    add("pattern scan", False, f"{f}:{n} '{p}' {tag}")
info("pattern list size", str(len(PATTERNS)))

# 8b. S02 source log integrity
slog = need("02_SOURCE_LOG.md")
SRCROWS = {}
for line in slog.splitlines():
    m = re.match(r"^\| (SRC-\d+) \|(.*)\|$", line)
    if m:
        cells = [c.strip() for c in m.group(2).split("|")]
        SRCROWS[m.group(1)] = cells
for sid, c in sorted(SRCROWS.items()):
    # columns after ID: citation, doi/url, type, tier, depth, verified, supports, limitations
    probs = []
    if len(c) != 8: probs.append(f"{len(c)} columns")
    else:
        if not (c[1].startswith("doi:10.") or c[1].startswith("https://") or "Bibliographic" in c[1]):
            probs.append("no DOI/URL")
        if c[3] not in ("T1", "T2", "T3"): probs.append(f"tier {c[3]}")
        if c[4] not in ("A", "P", "B"): probs.append(f"depth {c[4]}")
        if not (c[5].startswith("Y") or c[5].startswith("Partial")): probs.append(f"verified {c[5]}")
        if not c[6].startswith("RQ"): probs.append("no RQ link")
    add("source log row complete", not probs, sid + (": " + "; ".join(probs) if probs else ""))

# 8c. Evidence matrix: sources defined, no orphans, active RQs covered by T1 verified sources
mx = need("S02_LITERATURE_EVIDENCE_MATRIX.md")
msrc = set(re.findall(r"\bSRC-\d+\b", mx))
add("matrix sources all logged", msrc <= set(SRCROWS), ", ".join(sorted(msrc - set(SRCROWS))) or f"{len(msrc)} cited")
S03TXT = "\n".join(v for k, v in FILES.items() if k.startswith(("S03_", "S04_", "S05_", "DRAFT_")))
s3src = set(re.findall(r"\bSRC-\d+\b", S03TXT))
add("S03/S04 sources all logged", s3src <= set(SRCROWS), ", ".join(sorted(s3src - set(SRCROWS))) or f"{len(s3src)} cited")
orph = sorted(set(SRCROWS) - msrc - s3src)
add("no orphan sources in log", not orph, ", ".join(orph) or "all logged sources cited in S02 matrix or S03/S04/S05 deliverables")
S03ONLY = set(re.findall(r"\bSRC-\d+\b", "\n".join(v for k, v in FILES.items() if k.startswith("S03_"))))
S04ONLY = set(re.findall(r"\bSRC-\d+\b", "\n".join(v for k, v in FILES.items() if k.startswith(("S04_", "DRAFT_")))))
new = sorted(i for i in SRCROWS if 40 <= int(i[4:]) <= 63)
miss = [i for i in new if i not in S03ONLY]
add("every S03 source cited in an S03 deliverable", not miss, ", ".join(miss) or f"{len(new)} S03 sources")
new4 = sorted(i for i in SRCROWS if 64 <= int(i[4:]) <= 65)
miss4 = [i for i in new4 if i not in S04ONLY]
add("every S04 source cited in an S04 deliverable", not miss4, ", ".join(miss4) or f"{len(new4)} S04 sources")
S05ONLY = set(re.findall(r"\bSRC-\d+\b", "\n".join(v for k, v in FILES.items() if k.startswith(("S05_",)) and k != "S05_QC_REPORT.md")))
new5 = sorted(i for i in SRCROWS if int(i[4:]) >= 66)
miss5 = [i for i in new5 if i not in S05ONLY]
add("every S05 source cited in an S05 deliverable", not miss5, ", ".join(miss5) or f"{len(new5)} S05 sources")
add("RQ-13 has a verified T1 source", any("RQ-13" in c[6] and c[3] == "T1" and c[5].startswith("Y") for c in SRCROWS.values()))
for rq in ["RQ-01", "RQ-02", "RQ-03", "RQ-04", "RQ-05", "RQ-06", "RQ-08", "RQ-09"]:
    sec = re.search(r"^## " + rq + r"\b.*?(?=^## |\Z)", mx, re.M | re.S)
    ids = set(re.findall(r"\bSRC-\d+\b", sec.group(0))) if sec else set()
    good = [i for i in ids if i in SRCROWS and SRCROWS[i][3] == "T1" and SRCROWS[i][5].startswith("Y")]
    add(f"{rq} has a verified T1 source", bool(good), f"{len(good)} verified T1 of {len(ids)} cited")
LABELS_M = ("VERIFIED", "OPEN", "PROPOSED", "ASSUMPTION")
for line in mx.splitlines():
    m = re.match(r"^\| ((?:\d+|I)\.\d+) \|", line)
    if m:
        last = [c.strip() for c in line.strip("|").split("|")][-1]
        add("matrix row label", last.startswith(LABELS_M), f"{m.group(1)}: {last}")

# 8d. S03 exit criteria (00_STAGE_GATE_PROTOCOL section 7)
cm = need("S03_COMPARABLE_SYSTEMS_MATRIX.md")
pa = need("S03_PRIOR_ART_REGISTER.md")
s9 = need("S03_SECTION9_COMPARISON.md")
for rq_id in ["RQ-10", "RQ-11", "RQ-12"]:
    good = [i for i, c in SRCROWS.items() if rq_id in c[6] and c[5].startswith("Y")]
    add(f"{rq_id} has a verified source", bool(good), f"{len(good)} verified")
sec1 = cm[cm.find("## 1."):cm.find("**REF-01")]
cells_bad = []
for line in sec1.splitlines():
    if re.match(r"^\| D\d\.", line):
        for cell in [c.strip() for c in line.strip("|").split("|")][1:]:
            if not (cell.startswith(("VS", "ND", "S02")) or "SRC-" in cell):
                cells_bad.append(line[:12] + ": " + cell[:30])
add("matrix section 1 cells sourced or ND", not cells_bad, "; ".join(cells_bad) or "all cells labelled")
sec2 = cm[cm.find("## 2."):cm.find("## 3.")]
bad2 = []
for line in sec2.splitlines():
    if line.startswith("| ") and not line.startswith(("| System", "|---")):
        for cell in [c.strip() for c in line.strip("|").split("|")][2:]:
            if not (cell.startswith(("VS", "ND", "S02", "VERIFIED", "—")) or "SRC-" in cell):
                bad2.append(cell[:30])
add("matrix section 2 cells sourced or ND", not bad2, "; ".join(bad2) or "all cells labelled")
HDR = "| No. | Research or product | Type | Executing organization / approved location descriptor | Outcome | Latest status | Notes / URL |"
add("Section 9 table uses the form header", HDR in s9)
rows9 = [l for l in s9.splitlines() if re.match(r"^\| \d+ \|", l)]
add("Section 9 has at least three comparators", len(rows9) >= 3, f"{len(rows9)} rows")
for l in rows9:
    cells = [c.strip() for c in l.strip("|").split("|")]
    ok = len(cells) == 7 and "[LOCAL COMPLETION ONLY]" in cells[3] and ("SRC-" in cells[6])
    add("Section 9 row: 7 cells, local placeholder, source", ok, cells[0] if cells else l[:10])
for l in pa.splitlines():
    m = re.match(r"^\| (PA-\d+|NP-\d+) \|", l)
    if m:
        add("prior-art row sourced", "SRC-" in l, m.group(1))
SUP = ["outperform", "superior to", "better than", "more accurate than", "best-in-class", "market-leading",
       "novel ", "unique ", "patentable", "first of its kind", "distinguishing point"]
for f, t in FILES.items():
    if not f.startswith(("S03_", "S04_", "S04.1_", "S05_", "DRAFT_")) or f in ("S03_QC_REPORT.md", "S04_QC_REPORT.md", "S04.1_QC_REPORT.md", "S05_QC_REPORT.md"):  # QC reports name the terms they scan for
        continue
    for n, line in enumerate(t.splitlines(), 1):
        low = line.lower()
        for w in SUP:
            if w in low:
                rule = ("do not" in low) or ("never" in low) or ("no superiority" in low) or ("no novelty" in low) or ("no longer framed" in low) or ("not a claimed" in low)
                if rule:
                    info("superiority scan", f"{f}:{n} '{w}' in a rule statement (exempt)")
                else:
                    add("superiority scan", False, f"{f}:{n} '{w}'")
info("superiority list size", str(len(SUP)))


# 8e. S04 checks (00_STAGE_GATE_PROTOCOL section 7, S04 row)
arch = need("S04_ARCHITECTURE.md"); dfi = need("S04_DATA_FLOWS_AND_INTERFACES.md")
asm = need("S04_ASSUMPTIONS_AND_STANDARDS.md"); sco = need("S04_SCOPE_OPTIONS.md")
S4DEF = {"FN": arch, "AC": arch, "CP": arch, "AD": arch, "IF": dfi, "DF": None, "AS": asm,
         "MS": need("DRAFT_SEC08_FEATURES.md")}
dfdef = set(re.findall(r"^### (DF-\d+)\b", dfi, re.M))
for k, text in S4DEF.items():
    ids = list(dfdef) if k == "DF" else re.findall(r"^\|\s*(" + k + r"-\d+)\s*\|", text, re.M)
    dups = sorted({i for i in ids if ids.count(i) > 1})
    add(f"no duplicate {k} definitions", not dups, ", ".join(dups) or f"{len(ids)} defined")
    refs = set(re.findall(r"\b(" + k + r"-\d+)\b", allt))
    # ranges written "CP-1 to CP-6" count as references to their endpoints only
    undef = sorted(refs - set(ids))
    add(f"all {k} references defined", not undef, ", ".join(undef) or f"{len(refs)} referenced")
cps = set(re.findall(r"^\| (CP-\d+) \|", arch, re.M))
add("R3 checkpoints CP-1 to CP-6 defined", cps == {f"CP-{i}" for i in range(1, 7)}, ", ".join(sorted(cps)))
add("approval rule: no transition into Approved outside CP-5", "No transition into Approved exists outside CP-5" in arch)
fnrows = [l for l in arch.splitlines() if re.match(r"^\| FN-\d+ \|", l)]
badfn = [l[:8] for l in fnrows if len([c for c in l.strip("|").split("|")]) != 5 or not l.strip("|").split("|")[3].strip()]
add("every FN row states current-project scope", not badfn and len(fnrows) >= 10, ", ".join(badfn) or f"{len(fnrows)} functions")
add("future-only and never-in-scope items stated", "Not in any phase" in arch)
add("scope options A-D present with recommendation", all(f"| {o}. " in sco for o in "ABCD") and "OWNER DECISION REQUIRED" in sco)
for a in [f"AS-{i:02d}" for i in range(1, 9)]:
    row = re.search(r"^\| " + a + r" \|.*$", asm, re.M)
    add(f"assumption {a} linked to an issue", bool(row) and "ISS-" in row.group(0))
pf = tm[tm.find("## F."):]
for item in ["R1", "R2", "R3", "R4", "C1 (SC)", "C2 (SC)", "C3 (EA)"]:
    row = re.search(r"^\| " + re.escape(item) + r" \|.*$", pf, re.M)
    add(f"traceability Part F row {item} has components", bool(row) and ("AC-" in row.group(0)))
s5 = need("DRAFT_SEC05_CLASSIFICATION.md")
add("Section 5 draft uses the form table", "| Classification | Options / Selection |" in s5 and
    all(r in s5 for r in ["| Project type |", "| Reason |", "| Maturity |", "| Execution |", "| Relationship |"]))
s11 = need("DRAFT_SEC11_CONTINUITY.md")
H11 = "| Stage | Project title | Estimated duration (months) | Estimated cost (sponsor unit; local only) | High-level deliverable |"
add("Section 11 draft uses the form header", H11 in s11)
r11 = [l for l in s11.splitlines() if re.match(r"^\| \d", l)]
add("Section 11 row 1 is the current project (RF-005)", bool(r11) and "current project" in r11[0])
add("Section 11 cost cells local only", r11 and all("[LOCAL COMPLETION ONLY]" in l for l in r11))
add("Section 11 durations not invented", r11 and all("[OPEN" in l.split("|")[3] for l in r11))
s8 = need("DRAFT_SEC08_FEATURES.md")
for l in s8.splitlines():
    m = re.match(r"^\| (MS-\d+) \|", l)
    if m:
        tgt = l.strip("|").split("|")[-1].strip()
        add("Section 8 target set in S05 (no row left as 'S05')", bool(tgt) and tgt != "S05", f"{m.group(1)}: {tgt}")
add("Section 8 separates measurable specifications from functional features",
    "Functional features" in s8 and "Measurable specifications" in s8)
CERT = ["certified", "certification", "compliant", "complies with", "conformity", "conforms to"]
for f, t in FILES.items():
    if not f.startswith(("S04_", "S04.1_", "S05_", "DRAFT_")) or f in ("S04_QC_REPORT.md", "S04.1_QC_REPORT.md", "S05_QC_REPORT.md"):
        continue
    for n, line in enumerate(t.splitlines(), 1):
        low = line.lower()
        for w in CERT:
            if w in low:
                neg = any(x in low for x in ("not certified", "no conformity", "cannot", "not proposed",
                          "not claimed", "is not", "not itself", "no certification", "claims conformity",
                          "conformity is claimed", "claimed as conforming", "certification, a conformity",
                          "or certification?", "certification status", "or certification", "is claimed", "versus certification", "versus actual certification", "certification scan"))
                if neg:
                    info("certification scan", f"{f}:{n} '{w}' negated or quoted (exempt)")
                else:
                    add("certification scan", False, f"{f}:{n} '{w}'")
info("certification list size", str(len(CERT)))

# 8f. S04.1 correction checks (DEC-029, RC-01)
req = need("S01_REQUIREMENTS_REGISTER.md")
add("S04.1: R2 corrected statement recorded with provenance",
    "Assess whether relevant existing solution examples can be identified for a submitted need." in req
    and "### 1a. Owner correction to R2" in req and "DEC-029" in req)
r2row = re.search(r"^\| R2 \|.*$", req, re.M).group(0)
add("S04.1: R2 row keeps identifier and marks old wording superseded", "superseded" in r2row.lower() and "ISS-037" in r2row)
r1row = re.search(r"^\| R1 \|.*$", req, re.M).group(0)
add("S04.1: R1 operative reading is new-versus-stored; grouping not a confirmed requirement",
    "new submission with stored submissions" in r1row and "not a confirmed sponsor requirement" in r1row)
WITHDRAWN = ["approved internal collection", "internal precedent", "precedent collection"]
OPERATIVE = ["S04_ARCHITECTURE.md", "S04_DATA_FLOWS_AND_INTERFACES.md", "S04_ASSUMPTIONS_AND_STANDARDS.md",
             "S04_SCOPE_OPTIONS.md", "DRAFT_SEC05_CLASSIFICATION.md", "DRAFT_SEC07_OBJECTIVES.md",
             "DRAFT_SEC08_FEATURES.md", "DRAFT_SEC11_CONTINUITY.md", "S02_RESEARCH_SYNTHESIS.md", "03_STYLE_GUIDE.md"]
HIST = ("no longer", "withdrawn", "assumed that", "superseded", "s04.1")
for f in OPERATIVE:
    for n, line in enumerate(need(f).splitlines(), 1):
        low = line.lower()
        for w in WITHDRAWN:
            if w in low:
                if any(h in low for h in HIST):
                    info("S04.1 withdrawn-wording scan", f"{f}:{n} '{w}' in a correction note (exempt)")
                else:
                    add("S04.1 withdrawn-wording scan", False, f"{f}:{n} '{w}'")
add("S04.1 withdrawn-wording scan completed", True, f"{len(OPERATIVE)} operative files")
dl = need("00_DECISIONS_LOG.md")
d26 = re.search(r"^\| DEC-026 \|.*$", dl, re.M).group(0)
add("S04.1: DEC-026 keeps INFERRED history and is not shown as an original owner decision", "nferred" in d26 and "| Owner (recorded" not in d26)
d29 = re.search(r"^\| DEC-029 \|.*$", dl, re.M)
add("S04.1: DEC-029 recorded as owner instruction", bool(d29) and "| Owner | ACTIVE |" in d29.group(0) and "does not approve S04" in d29.group(0))
add("S04.1: record correction RC-01 present", re.search(r"^\| RC-01 \|", dl, re.M) is not None)
d28 = re.search(r"^\| DEC-028 \|.*$", dl, re.M)
confirmed = bool(d28) and "S03 approval confirmed" in d28.group(0) and "| Owner | ACTIVE |" in d28.group(0)
s3app = [f for f, t in FILES.items() if f.startswith("S03_") and re.search(r"^\| Status \| APPROVED \|", t, re.M)]
s3n = len([f for f in FILES if f.startswith("S03_")])
add("S04.1: S03 status matches the decision record (APPROVED only after explicit confirmation)",
    (len(s3app) == s3n) if confirmed else (not s3app), f"confirmed={confirmed}; approved files={len(s3app)}/{s3n}")
st = need("00_STAGE_STATUS.md")
add("S04.1: stage status identifies baselines by SHA; no reliance on tags",
    "No Git tags" in st and "2b5f83c65749a4c697782216026a6291a91aa2a1" in st and "961ae6ad31581eac633304d905cbab1761179b0b" in st)
arch = need("S04_ARCHITECTURE.md")
cls = {}
for l in arch.splitlines():
    m = re.match(r"^\| (CP-\d) \| [^|]+ \| ([^|]+) \|", l)
    if m: cls[m.group(1)] = m.group(2).strip()
add("S04.1: CP-5 and CP-6 classed Essential", cls.get("CP-5", "").startswith("Essential") and cls.get("CP-6", "").startswith("Essential"), str(cls))
add("S04.1: CP-1 to CP-4 not classed Essential", all(not cls.get(f"CP-{i}", "Essential").startswith("Essential") for i in range(1, 5)))
for fn in ("FN-04", "FN-07"):
    row = re.search(r"^\| " + fn + r" \|.*$", arch, re.M).group(0)
    add(f"S04.1: {fn} not in the essential funded scope", ("OPTIONAL" in row) or ("EXCLUDED" in row))
fn05 = re.search(r"^\| FN-05 \|.*$", arch, re.M).group(0)
add("S04.1: FN-05 uses the evidence-source interface and labelled substitute data", "evidence-source interface" in fn05 and "substitute" in fn05)
add("S04.1: architecture separates actual availability from proposed substitutes",
    "Actual availability to the project" in arch and "Substitute if unavailable (PROPOSED)" in arch)
s5 = need("DRAFT_SEC05_CLASSIFICATION.md")
add("S04.1: Section 5 selections marked provisional",
    s5.count("Provisional selection:") == 5 and not re.search(r"\. Selected:", s5))
sco = need("S04_SCOPE_OPTIONS.md")
add("S04.1: scope audit section with the five distinctions; owner decision recorded where made",
    ("PROVISIONAL" in sco or "DEC-028" in sco) and "## 6. S04.1 audit" in sco and
    all(k in sco for k in ["funding track versus technological maturity", "Current funded deliverables versus future",
                           "Proposed architecture versus implemented", "Prototype evaluation versus live",
                           "Proposed standards alignment versus certification"]))
cr = need("02_CLAIM_REGISTER.md")
badc = []
for l in cr.splitlines():
    m = re.match(r"^\| (CLM-\d+) \|", l)
    if m:
        cells = [c.strip() for c in l.strip("|").split("|")]
        if len(cells) != 8: badc.append(m.group(1) + f" ({len(cells)} cells)")
        elif cells[3].startswith("VERIFIED") and "SRC-" not in cells[7]: badc.append(m.group(1) + " (VERIFIED without depth)")
add("S04.1: every claim row has an evidence-depth cell; VERIFIED claims cite depth", not badc, ", ".join(badc) or "all rows")
add("S04.1: CLM-012 superseded by CLM-045", re.search(r"^\| CLM-012 \|.*SUPERSEDED by CLM-045", cr, re.M) is not None)
for f in ["S04.1_CORRECTION_MATRIX.md", "S04.1_CHANGE_REPORT.md", "S04.1_QC_REPORT.md", "S04.1_HANDOFF.md",
          "S04.1_R2_REFERENCE_CORRECTION_NOTE.md"]:
    add(f"S04.1 deliverable present: {f}", f in FILES)
# 8g. S05 checks (00_STAGE_GATE_PROTOCOL section 7, S05 row; DEC-030)
s7dir = [os.path.basename(p) for p in glob.glob(os.path.join(ROOT, "stages", "S07", "*")) if not p.endswith(".gitkeep")]
add("S06: S07 not started (stages/S07 holds no deliverables)", not s7dir, ", ".join(s7dir) or "empty")
for f in ["S05_PLAN.md", "S05_EVALUATION_DESIGN.md", "S05_DATA_AVAILABILITY_AND_SUBSTITUTES.md",
          "S05_FEASIBILITY_AND_RISKS.md", "S05_QC_REPORT.md", "S05_HANDOFF.md"]:
    add(f"S05 deliverable present: {f}", f in FILES)
ev = need("S05_EVALUATION_DESIGN.md"); da = need("S05_DATA_AVAILABILITY_AND_SUBSTITUTES.md")
fe = need("S05_FEASIBILITY_AND_RISKS.md")
S5DEF = {"ET": ev, "PV": ev, "DR": da, "DS": da, "FT": fe, "RSK": fe}
for k, text in S5DEF.items():
    ids = re.findall(r"^\|\s*(" + k + r"-\d+[a-z]?)\s*\|", text, re.M)
    dups = sorted({i for i in ids if ids.count(i) > 1})
    add(f"no duplicate {k} definitions", not dups, ", ".join(dups) or f"{len(ids)} defined")
    refs = set(re.findall(r"\b(" + k + r"-\d+[a-z]?)\b", allt))
    undef = sorted(refs - set(ids))
    add(f"all {k} references defined", not undef, ", ".join(undef) or f"{len(refs)} referenced")
# explicit tests for R1-R4: each requirement heading exists and its section defines at least one ET row
for r in ["R1", "R2", "R3", "R4"]:
    i = ev.find("### " + r + " ")
    seg = ev[i:ev.find("\n### ", i + 4)] if i >= 0 else ""
    ets = re.findall(r"^\| (ET-\d+[a-z]?) \|", seg, re.M)
    add(f"S05: explicit test(s) for {r}", bool(ets), ", ".join(ets) or "none")
add("S05: R2 section uses the corrected statement (DEC-029)",
    "assess whether relevant existing solution examples can be identified for a submitted need" in ev
    and "No source is assumed" in ev)
# sponsor versus substitute data separated
add("S05: Track S and Track P defined and never pooled",
    "*Track S*" in ev and "*Track P*" in ev and "never pooled" in ev and "A combined average across tracks is not computed" in da)
add("S05: no substitute dataset selected; every DS row has a licence or access cell and open checks",
    "none selected" in da.lower() and all(len([c for c in l.strip("|").split("|")]) == 6
                                         for l in da.splitlines() if re.match(r"^\| DS-\d+ \|", l)))
# planning values labelled as assumptions and linked to an owner issue
add("S05: planning values labelled ASSUMPTION with owner issue", "ASSUMPTION, AS-12" in ev and "ISS-039" in ev)
for a in [f"AS-{i:02d}" for i in range(9, 13)]:
    row = re.search(r"^\| " + a + r" \|.*$", asm, re.M)
    add(f"assumption {a} linked to an issue", bool(row) and "ISS-" in row.group(0))
# targets: every essential MS row has a target; conditional rows say they are not set
s8rows = {m.group(1): l for l in s8.splitlines() for m in [re.match(r"^\| (MS-\d+) \|", l)] if m}
add("S05: MS-01 to MS-10 present in Section 8", set(s8rows) == {f"MS-{i:02d}" for i in range(1, 11)}, ", ".join(sorted(s8rows)))
for ms in ("MS-07", "MS-09"):
    add(f"S05: {ms} kept conditional (not set)", "Not set" in s8rows.get(ms, ""))
for ms in ("MS-01", "MS-02", "MS-03"):
    add(f"S05: {ms} target is relative to a baseline", ("baseline" in s8rows.get(ms, "").lower()) or ("not lower than" in s8rows.get(ms, "").lower()))
add("S05: Section 8 states targets are untested", "All targets are untested" in s8)
# no performance results: result verbs only in negated or rule context
RES = [r"\bachiev(es|ed)\b", r"\boutperform(s|ed)?\b", r"\bdemonstrated\b", r"\bwe (found|measured|observed)\b"]
for f in [x for x in FILES if x.startswith("S05_") and x != "S05_QC_REPORT.md"] + ["DRAFT_SEC08_FEATURES.md"]:
    for n, line in enumerate(FILES.get(f, "").splitlines(), 1):
        for pat in RES:
            if re.search(pat, line, re.I):
                add("S05 result-language scan", False, f"{f}:{n} {pat}")
add("S05 result-language scan completed", True)
# memory arithmetic in S05_FEASIBILITY_AND_RISKS 1.2 is recomputed
def fmt(b):
    return (f"{b/1e9:.3f} GB" if b >= 1e9 else (f"{b/1e6:.2f} MB" if b < 1e8 else f"{b/1e6:.1f} MB"))
bad = []
for n in (10_000, 100_000, 1_000_000):
    row = re.search(r"^\| " + f"{n:,}" + r" \|(.*)\|$", fe, re.M)
    cells = [c.strip() for c in row.group(1).split("|")] if row else []
    for d, cell in zip((384, 768, 1024), cells):
        if fmt(n * d * 4) != cell: bad.append(f"{n}x{d}: {cell} != {fmt(n * d * 4)}")
    if len(cells) != 3: bad.append(f"row {n} missing")
add("S05: dense-index memory table matches N x d x 4 bytes", not bad, "; ".join(bad) or "9 cells")
# R4 volume arithmetic: 30 statements x 3 formulations = 90 searches, 900 results, ~9 minutes at 10/min
add("S05: R4 volume arithmetic consistent with PV-08", "30 statements × 3 formulations = 90 searches" in fe
    and "up to 900 results" in fe and "about nine minutes" in fe and "| PV-08 |" in ev and "| 30, each searched with three formulations |" in ev)
# every S05 source used is logged with T1 or flagged T3; T3 never sole support
t3 = {s for s, c in SRCROWS.items() if c[3] == "T3"}
for cid in ("CLM-051", "CLM-053", "CLM-054"):
    row = re.search(r"^\| " + cid + r" \|.*$", need("02_CLAIM_REGISTER.md"), re.M).group(0)
    srcs = set(re.findall(r"SRC-\d+", row.split("|")[3]))
    add(f"S05: {cid} not supported by T3 sources alone", bool(srcs - t3), ", ".join(sorted(srcs)))
c52 = re.search(r"^\| CLM-052 \|.*$", need("02_CLAIM_REGISTER.md"), re.M).group(0)
add("S05: T3-only statement in CLM-052 kept OPEN", "OPEN (T3 only)" in c52)
# DEC-030 recorded as owner instruction that does not approve S05
d30 = re.search(r"^\| DEC-030 \|.*$", dl, re.M)
add("S05: DEC-030 recorded; does not approve S05", bool(d30) and "| Owner | ACTIVE |" in d30.group(0) and "does not approve S05" in d30.group(0))
# exit criterion: ISS-002 resolved or explicit assumption recorded
i2 = re.search(r"^\| ISS-002 \|.*$", need("00_OPEN_ISSUES_REGISTER.md"), re.M).group(0)
add("S05 exit: ISS-002 resolved or explicit assumption recorded", "AS-09" in i2 and "explicit assumption" in i2)
# withdrawn R2 wording must not appear in S05 deliverables
for f in [x for x in FILES if x.startswith("S05_")]:
    for n, line in enumerate(FILES[f].splitlines(), 1):
        for w in WITHDRAWN:
            if w in line.lower():
                add("S05 withdrawn-wording scan", False, f"{f}:{n} '{w}'")
add("S05 withdrawn-wording scan completed", True)
# traceability Part G covers R1-R4
pg = tm[tm.find("## G."):] if "## G." in tm else ""
for r in ["R1", "R2", "R3", "R4"]:
    row = re.search(r"^\| " + r + r" \|.*$", pg, re.M)
    add(f"traceability Part G row {r} has ET and MS", bool(row) and "ET-" in row.group(0) and "MS-" in row.group(0))

# 8h. S06 checks (00_STAGE_GATE_PROTOCOL section 7, S06 row; DEC-032)
import math
for f in ["S06_PLAN.md", "S06_WORK_PACKAGES.md", "S06_DELIVERABLES_AND_ACCEPTANCE.md",
          "S06_DEPENDENCIES_AND_EFFORT.md", "S06_QC_REPORT.md", "S06_HANDOFF.md", "DRAFT_SEC13_ACTIVITIES.md"]:
    add(f"S06 deliverable present: {f}", f in FILES)
wp = need("S06_WORK_PACKAGES.md"); da6 = need("S06_DELIVERABLES_AND_ACCEPTANCE.md")
ef = need("S06_DEPENDENCIES_AND_EFFORT.md"); s13 = need("DRAFT_SEC13_ACTIVITIES.md")
ho6 = need("S06_HANDOFF.md")
def sect(t, start, stop):
    i = t.find(start); j = t.find(stop, i + len(start)) if i >= 0 else -1
    return t[i:j if j > 0 else len(t)] if i >= 0 else ""
# work-package register: 6-7 packages, frozen IDs and titles
reg = sect(wp, "## 1.", "## 2.")
WPS = re.findall(r"^\| (WP\d+) \| ([^|]+?) \|", reg, re.M)
ids = [w for w, _ in WPS]; TITLE = dict(WPS)
add("S06: 6 or 7 work packages registered", 6 <= len(WPS) <= 7, f"{len(WPS)}")
add("S06: WP identifiers sequential and unique", ids == [f"WP{i}" for i in range(1, len(ids) + 1)], ", ".join(ids))
for w, title in WPS:
    add(f"S06: {w} has objective and type cells", re.search(r"^\| " + w + r" \|[^|]+\|\s*\S[^|]+\|\s*\S[^|]*\|$", reg, re.M) is not None)
# Section 13 draft repeats numbers and titles verbatim, in the form schema
add("S06: Section 13 table uses the form schema",
    "| No. | Main activity | Activity deliverable(s) | Key tasks | Effort (person-hours) |" in s13)
S13 = {int(m.group(1)): [c.strip() for c in m.group(2).split("|")]
       for m in re.finditer(r"^\| (\d) \|(.*)\|$", s13, re.M)}
add("S06: Section 13 rows = WP count", len(S13) == len(WPS), f"{len(S13)}")
for i, (w, title) in enumerate(WPS, 1):
    row = S13.get(i, [])
    add(f"S06: Section 13 row {i} title = {w} title", bool(row) and row[0] == title, row[0] if row else "missing")
    add(f"S06: Section 13 row {i} has deliverables, tasks and effort", len(row) == 4 and all(row[:3]) and re.fullmatch(r"\d+", row[3] or "") is not None)
# no development stage appears as an activity (DEC-012)
stagehits = [f"row {i}" for i, row in S13.items() if re.search(r"\bS(0\d|10)(\.\d)?\b", " ".join(row))]
stagehits += [w for w, t_ in WPS if re.search(r"\bS(0\d|10)\b", t_)]
add("S06: no development stage used as a work package", not stagehits, ", ".join(stagehits) or "none")
# tasks per work package
tsec = sect(wp, "## 2.", "## 3.")
TASKS = re.findall(r"^\| (T(\d+)\.(\d+)) \|", tsec, re.M)
tids = [t_[0] for t_ in TASKS]
add("S06: no duplicate task IDs", len(tids) == len(set(tids)), f"{len(tids)} tasks")
for i in range(1, len(WPS) + 1):
    n = [t_ for t_ in TASKS if int(t_[1]) == i]
    add(f"S06: WP{i} has tasks and a heading", bool(n) and f"### WP{i} — {TITLE.get(f'WP{i}', '?')}" in tsec, f"{len(n)} tasks")
trefs = set(re.findall(r"\b(T\d+\.\d+)\b", allt))
add("S06: every task reference defined", not (trefs - set(tids)), ", ".join(sorted(trefs - set(tids))) or f"{len(trefs)} referenced")
# deliverables: each WP has at least one, each has acceptance evidence and verification
DROWS = {m.group(1): [c.strip() for c in m.group(2).split("|")]
         for m in re.finditer(r"^\| (D\d+\.\d+) \|(.*)\|$", sect(da6, "## 1.", "## 2."), re.M)}
add("S06: deliverable IDs defined", bool(DROWS), f"{len(DROWS)}")
for i in range(1, len(WPS) + 1):
    d = [k for k, v in DROWS.items() if v[1] == f"WP{i}"]
    add(f"S06: WP{i} has at least one deliverable", bool(d), ", ".join(d))
for k, v in DROWS.items():
    add(f"S06: {k} prefix matches its WP and has acceptance evidence", k.split(".")[0][1:] == v[1][2:] and len(v) == 5 and all(v))
drefs = set(re.findall(r"\b(D\d+\.\d+)\b", allt))
add("S06: every deliverable reference defined", not (drefs - set(DROWS)), ", ".join(sorted(drefs - set(DROWS))) or f"{len(drefs)} referenced")
add("S06: acceptance does not depend on outperforming BM25", "Acceptance of a deliverable does not depend on a retrieval target being met" in da6)
# person-hours: task table sums, ranges, judging formula, Section 13 match
th = {m.group(2): (m.group(1), int(m.group(3))) for m in re.finditer(r"^\| (WP\d) \| (T\d+\.\d+) \| (\d+) \|", ef, re.M)}
cond = {"T3.8", "T4.6", "T6.7"}
miss = sorted(set(tids) - set(th) - cond)
add("S06: every non-conditional task has an effort row", not miss, ", ".join(miss) or f"{len(th)} rows")
add("S06: conditional tasks not in the planning table", not (cond & set(th)), ", ".join(sorted(cond & set(th))) or "none")
for k, (w, h) in th.items():
    if w != "WP" + k[1:].split(".")[0]: add("S06: task row in its own WP", False, k)
def jh(q, p, s, a, d=0.20):
    return math.ceil(q * p * (1 + d + d * a) * s / 3600)
SC = {"low": (30, 30, 20, 60, 0.25), "plan": (45, 45, 25, 90, 0.35), "high": (60, 60, 30, 120, 0.50)}
J = {}
for k, (p12, s12, p4, s4, a) in SC.items():
    J[k] = (jh(80, p12, s12, a), jh(80, p12, s12, a), jh(30, p4, s4, a))
jt = sect(ef, "## 4.", "## 5.")
for name, idx in (("ET-01", 0), ("ET-03", 1), ("ET-09", 2)):
    row = re.search(r"^\| " + name + r"[^|]*\| (\d+) \| (\d+) \| (\d+) \| (\d+) \|", jt, re.M)
    got = tuple(int(x) for x in row.groups()[1:]) if row else None
    add(f"S06: judging hours {name} recomputed", got == (J["low"][idx], J["plan"][idx], J["high"][idx]), f"{got} vs {(J['low'][idx], J['plan'][idx], J['high'][idx])}")
JT = {k: sum(v) for k, v in J.items()}
row = re.search(r"^\| Total \| — \| (\d+) \| (\d+) \| (\d+) \|", jt, re.M)
add("S06: judging totals recomputed", row is not None and tuple(map(int, row.groups())) == (JT["low"], JT["plan"], JT["high"]), str(JT))
add("S06: T6.3 planning hours = planning judging total", th.get("T6.3", ("", 0))[1] == JT["plan"])
tot = sect(ef, "### Totals per work package", "## 4.")
grand = [0, 0, 0]
for i in range(1, len(WPS) + 1):
    w = f"WP{i}"
    plan = sum(h for k, (ww, h) in th.items() if ww == w)
    nonj = sum(h for k, (ww, h) in th.items() if ww == w and k != "T6.3")
    jl, jhh = (JT["low"], JT["high"]) if w == "WP6" else (0, 0)
    exp = (plan, round(0.8 * nonj) + jl, round(1.3 * nonj) + jhh)
    row = re.search(r"^\| " + w + r" \| (\d+) \| (\d+) \| (\d+) \|", tot, re.M)
    got = tuple(map(int, row.groups())) if row else None
    add(f"S06: {w} totals recomputed (plan, low, high)", got == exp, f"{got} vs {exp}")
    grand = [g + e for g, e in zip(grand, exp)]
    add(f"S06: Section 13 effort for activity {i} = planning figure", S13.get(i, [""] * 4)[3] == str(plan))
row = re.search(r"^\| Total \| (\d+) \| (\d+) \| (\d+) \|", tot, re.M)
add("S06: grand totals recomputed", row is not None and list(map(int, row.groups())) == grand, f"{grand}")
add("S06: Section 13 total stated", f"Total effort (provisional): {grand[0]:,} person-hours" in s13)
add("S06: person-week conversion (EH-01, 45 h)", f"about {grand[0] / 45:.1f} person-weeks" in ef)
pp = 45 * (1 + 0.20 + 0.20 * 0.35) * 45 / 3600
add("S06: L-4 per-query figure", f"About {pp:.1f} h per removed query" in ef, f"{pp:.3f}")
add("S06: handoff figures match", f"{grand[0]:,} person-hours planning figure (range {grand[1]:,}–{grand[2]:,})" in ho6
    and f"({JT['low']} / {JT['plan']} / {JT['high']} h)" in ho6)
# effort labelled; envelope not claimed
add("S06: effort assumptions labelled ASSUMPTION with owner issue", "ASSUMPTION; owner confirmation ISS-046" in ef)
add("S06: no claim that the ISS-013 envelope is met", "It does not claim that any ceiling is met" in ef and "conditional" in s13)
for n, line in enumerate((s13 + "\n" + wp + "\n" + ef).splitlines(), 1):
    if re.search(r"within the (ISS-013 )?envelope|envelope (is|has been) met", line, re.I) and not re.search(r"\bnot\b|\bno\b|cannot", line, re.I):
        add("S06: envelope-claim scan", False, line[:80])
add("S06: envelope-claim scan completed", True)
# traceability per work package: R1-R4, essential FN, AC, ET, FT, MS
trs = sect(wp, "## 4.", "## 5.")
for item in ["R1", "R2", "R3", "R4"]:
    add(f"S06: {item} traced to a WP", re.search(r"\b" + item + r"\b", trs) is not None)
build = tsec + trs
for fn in ["FN-01", "FN-02", "FN-03", "FN-05", "FN-06", "FN-08", "FN-09", "FN-10", "FN-11", "FN-12"]:
    add(f"S06: essential {fn} assigned", fn in tsec)
for ac in [f"AC-{i:02d}" for i in range(1, 15) if i not in (6, 8)]:
    add(f"S06: {ac} built or specified in a WP", ac in build)
for x in ["FN-04", "FN-07", "AC-06", "AC-08", "CP-2", "CP-3", "CP-4"]:
    hit = [l for l in tsec.splitlines() if x in l]
    add(f"S06: excluded {x} not a funded task", not hit, "; ".join(h[:40] for h in hit) or "absent from tasks")
for et in ["ET-01", "ET-01b", "ET-02", "ET-03", "ET-04", "ET-05", "ET-06", "ET-07", "ET-08", "ET-09", "ET-10", "ET-11"]:
    add(f"S06: {et} scheduled", re.search(r"\b" + et + r"\b", trs) is not None)
for ft in [f"FT-{i:02d}" for i in range(1, 6)]:
    add(f"S06: {ft} scheduled in a task", ft in tsec)
for ms in ["MS-01", "MS-02", "MS-03", "MS-04", "MS-05", "MS-06", "MS-08", "MS-10"]:
    add(f"S06: {ms} evidenced by a deliverable", re.search(r"^\| " + ms + r" \|[^|]*\bD\d+\.\d+", sect(da6, "## 2.", "## 3."), re.M) is not None)
for rsk in [f"RSK-{i:02d}" for i in range(1, 15)]:
    add(f"S06: {rsk} referenced in S06 planning", rsk in wp + ef)
# scope exclusions and invented content in the Section 13 draft
low13 = s13.lower()
for w in ["cluster", "grouping", "summar", "write-back", "production deployment"]:
    add(f"S06: Section 13 excludes '{w}'", w not in low13)
rt = [l for l in s13.splitlines() if "retrain" in l.lower() and "not" not in l.lower()]
add("S06: Section 13 mentions retraining only as excluded", not rt)
fin = re.findall(r"[$€£¥]|\bhourly rate\b|\bmonth \d|\bteam member\b", s13, re.I)
add("S06: Section 13 has no cost, month or team content", not fin, ", ".join(fin) or "none")
add("S06: training activity stated as not included (ISS-018)", "no training or learning activity is included" in low13)
# DEC-032, issues and carryover
d32 = re.search(r"^\| DEC-032 \|.*$", dl, re.M)
add("S06: DEC-032 recorded; does not approve S06", bool(d32) and "| Owner | ACTIVE |" in d32.group(0) and "does not approve S06" in d32.group(0))
isr = need("00_OPEN_ISSUES_REGISTER.md")
for iss in ["ISS-042", "ISS-043", "ISS-044", "ISS-045"]:
    row = re.search(r"^\| " + iss + r" \|.*$", isr, re.M)
    add(f"S06: {iss} carried with S06 note and open", bool(row) and "S06:" in row.group(0) and row.group(0).rstrip(" |").endswith("OPEN"))
    add(f"S06: {iss} has an explicit S07 instruction in the handoff", f"**{iss}" in ho6)
for iss in ["ISS-013", "ISS-018"]:
    row = re.search(r"^\| " + iss + r" \|.*$", isr, re.M)
    add(f"S06: {iss} updated and still open", bool(row) and "S06:" in row.group(0) and "| OPEN |" in row.group(0))
# result language and withdrawn R2 wording in S06 files
for f in [x for x in FILES if x.startswith("S06_") and x != "S06_QC_REPORT.md"] + ["DRAFT_SEC13_ACTIVITIES.md"]:
    for n, line in enumerate(FILES.get(f, "").splitlines(), 1):
        for pat in RES:
            if re.search(pat, line, re.I):
                add("S06 result-language scan", False, f"{f}:{n} {pat}")
        for w in WITHDRAWN:
            if w in line.lower():
                add("S06 withdrawn-wording scan", False, f"{f}:{n} '{w}'")
add("S06 result-language and withdrawn-wording scans completed", True)
# traceability Part H
ph = tm[tm.find("## H."):] if "## H." in tm else ""
for r in ["R1", "R2", "R3", "R4"]:
    row = re.search(r"^\| " + r + r" \|.*$", ph, re.M)
    add(f"traceability Part H row {r} has WP, D and MS", bool(row) and "WP" in row.group(0) and re.search(r"D\d\.\d", row.group(0)) is not None and "MS-" in row.group(0))
# RF-007 status
rf7 = re.search(r"^\| RF-007 \|.*$", rv, re.M).group(0)
add("S06: RF-007 status updated with artifact", "S06_WORK_PACKAGES" in rf7)


# 9. Identifying-data scan over every repository text file
#    (e-mail, phone-like digit runs with ISO dates removed, URLs)
def rel(p): return os.path.relpath(p, ROOT)
TEXT_EXT = (".md", ".py", ".txt", ".gitignore", ".gitkeep")
for p in ALL:
    if not p.endswith(TEXT_EXT): continue
    t = open(p, encoding="utf-8").read()
    hits = re.findall(r"[\w.+-]+@[\w-]+\.[\w.]+", t)
    no_dates = re.sub(r"\d{4}-\d{2}-\d{2}", " ", t)  # ISO dates are not phone numbers
    no_dates = re.sub(r"\b[0-9a-f]{64}\b", " ", no_dates)  # SHA-256 hashes neither
    no_dates = re.sub(r"\b[0-9a-f]{40}\b", " ", no_dates)  # nor Git commit SHAs
    no_dates = re.sub(r"(?:doi:)?10\.\d{4,9}/\S+", " ", no_dates)  # nor DOIs
    no_dates = re.sub(r"https?://\S+", " ", no_dates)  # URLs are checked separately below
    hits += re.findall(r"\+?\d[\d ()\-]{8,}\d", no_dates)
    # Citation URLs are permitted; repository, session and local paths are not.
    # Third-party GitHub projects cited as sources are allowlisted by owner name.
    GH_OK = ("github.com/pqaidevteam/",)
    hits += [u for u in re.findall(r"https?://\S+", t)
             if ("github.com" in u and not u.startswith(tuple("https://" + g for g in GH_OK)))
             or "claude.ai" in u or "iraa-proposal" in u]
    LOCAL = "/" + "home/|/" + "mnt/"  # built to avoid matching this line itself
    hits += re.findall("(?:" + LOCAL + r")\S+", t)
    add("identifying-data scan", not hits, rel(p) + (": " + ", ".join(hits) if hits else ""))

# 10. Credential scan over every repository text file
SECRET = [r"gh[pousr]_[A-Za-z0-9]{20,}", r"github_pat_[A-Za-z0-9_]{20,}",
          r"AKIA[0-9A-Z]{16}", r"-----BEGIN [A-Z ]*PRIVATE KEY-----",
          r"(?i)(password|passwd|secret|api[_-]?key|token)\s*[:=]\s*['\"][^'\"]{6,}"]
for p in ALL:
    if not p.endswith(TEXT_EXT): continue
    t = open(p, encoding="utf-8").read()
    hits = [m.group(0)[:12] + "..." for s in SECRET for m in re.finditer(s, t)]
    add("credential scan", not hits, rel(p) + (": " + ", ".join(hits) if hits else ""))

# 11. File inventory: only expected file types; no reference documents
ALLOWED = (".md", ".py", ".txt", ".gitkeep", ".gitignore")
REFS = ("REQUIREMENTS_STATEMENT_EN_WORKING_V1", "PROPOSAL_FORM_EN_WORKING_V1",
        "REVIEWER_FEEDBACK_EN_V1")
for p in ALL:
    name = os.path.basename(p)
    ok = name.endswith(ALLOWED) and not any(name.startswith(r) for r in REFS)
    add("file inventory", ok, rel(p))
for entry in ("CLAUDE.md", "README.md", ".gitignore"):
    add(f"entry file present: {entry}", os.path.isfile(os.path.join(ROOT, entry)))

# Report
fails = [r for r in results if r[1] == "FAIL"]
for name, status, detail in results:
    print(f"{status:4}  {name}" + (f"  [{detail}]" if detail else ""))
print(f"\nSUMMARY  files={len(FILES)}  checks={sum(r[1] != 'INFO' for r in results)}  "
      f"failed={len(fails)}  info={sum(r[1] == 'INFO' for r in results)}")
print("RESULT", "FAIL" if fails else "PASS")
sys.exit(1 if fails else 0)
