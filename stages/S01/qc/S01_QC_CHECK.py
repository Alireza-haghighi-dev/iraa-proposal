#!/usr/bin/env python3
"""S01_QC_CHECK.py - reproducible structural checks for the S01 deliverables.

Usage (from the repository root):  python3 stages/S01/qc/S01_QC_CHECK.py .
Checks the S01 deliverables in project/ and stages/S01/, and scans every
committed text file in the repository for credentials, identifying data and
unexpected file types.
Requires only the Python 3 standard library. Reads files; writes nothing.
Exit code 0 = all FAIL-capable checks passed; 1 = at least one failed.

Scope: structure, identifiers, coverage, metadata and pattern scans.
It does NOT check meaning, source fidelity or writing quality; those are
self-reported in S01_QC_REPORT.md and reserved for independent review.
"""
import glob, hashlib, os, re, sys

ROOT = sys.argv[1] if len(sys.argv) > 1 else "."
DELIV = sorted(glob.glob(os.path.join(ROOT, "project", "*.md")) +
               glob.glob(os.path.join(ROOT, "stages", "S01", "*.md")))
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
    "RQ": "S01_RESEARCH_QUESTIONS.md",
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
for k, n, w in [("RF", 12, 3), ("QA", 10, 3), ("F", 20, 2), ("FX", 12, 2), ("RQ", 15, 2)]:
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
                tag = "example usage (exempt)" if exempt else "FOUND IN TEXT"
                if exempt:
                    info("pattern scan", f"{f}:{n} '{p}' {tag}")
                else:
                    add("pattern scan", False, f"{f}:{n} '{p}' {tag}")
info("pattern list size", str(len(PATTERNS)))

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
    hits += re.findall(r"\+?\d[\d ()\-]{8,}\d", no_dates)
    hits += re.findall(r"https?://\S+", t)
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
