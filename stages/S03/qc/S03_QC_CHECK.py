#!/usr/bin/env python3
"""S03_QC_CHECK.py - reproducible structural checks for the S03 deliverables.

Usage (from the repository root):  python3 stages/S03/qc/S03_QC_CHECK.py .
Checks the living documents in project/ and the stage files in stages/S01/
to stages/S03/, the source log, the S02 evidence matrix, the S03 comparator
matrix, prior-art register and Section 9 working table, and scans every
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
               glob.glob(os.path.join(ROOT, "stages", "S03", "*.md")))
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
for k, n, w in [("RF", 12, 3), ("QA", 10, 3), ("F", 20, 2), ("FX", 12, 2), ("RQ", 15, 2), ("SRC", 63, 3), ("CLM", 40, 3), ("ISS", 32, 3)]:
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
S03TXT = "\n".join(v for k, v in FILES.items() if k.startswith("S03_"))
s3src = set(re.findall(r"\bSRC-\d+\b", S03TXT))
add("S03 sources all logged", s3src <= set(SRCROWS), ", ".join(sorted(s3src - set(SRCROWS))) or f"{len(s3src)} cited")
orph = sorted(set(SRCROWS) - msrc - s3src)
add("no orphan sources in log", not orph, ", ".join(orph) or "all logged sources cited in S02 matrix or S03 deliverables")
new = sorted(i for i in SRCROWS if int(i[4:]) >= 40)
miss = [i for i in new if i not in s3src]
add("every S03 source cited in an S03 deliverable", not miss, ", ".join(miss) or f"{len(new)} new sources")
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
SUP = ["outperform", "superior to", "better than", "more accurate than", "best-in-class", "market-leading"]
for f, t in FILES.items():
    if not f.startswith("S03_") or f == "S03_QC_REPORT.md":  # the QC report names the terms it scans for
        continue
    for n, line in enumerate(t.splitlines(), 1):
        low = line.lower()
        for w in SUP:
            if w in low:
                rule = ("do not" in low) or ("never" in low) or ("no superiority" in low)
                if rule:
                    info("superiority scan", f"{f}:{n} '{w}' in a rule statement (exempt)")
                else:
                    add("superiority scan", False, f"{f}:{n} '{w}'")
info("superiority list size", str(len(SUP)))

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
