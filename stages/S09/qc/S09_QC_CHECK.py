#!/usr/bin/env python3
"""S09_QC_CHECK.py - reproducible checks for S09 (independent critical review).

Usage (from the repository root):  python3 stages/S09/qc/S09_QC_CHECK.py .

Cumulative: runs stages/S08/qc/S08_QC_CHECK.py on the same tree (which itself runs
the S07 suite and the repository-wide safety scan) and accepts only the S08
failures that S09 legitimately supersedes, each re-checked below:
  (1) "S09 not started" - S09 started under DEC-037;
  (2) "Section 9: provisional selection flagged with ISS-030" - ISS-030 was
      resolved by DEC-037; the placeholder is now a defect (DEF-012) and must be absent;
  (3) "required wording present: 'lists as superseded'" - replaced by the accurate
      status statement (DEF-010), re-checked below;
  (4) "Stage status: S08 submitted ... or approved" - the stage status now records S09.
Any other S08 failure fails this script.

S09 checks: deliverables and metadata; master version; each corrected defect
(DEF-009 to DEF-026) checked by presence of the corrected wording and absence of
the defective wording; length not above the S08 baseline; registers updated.
It does NOT judge meaning or writing quality. Standard library only. Exit 0 = pass.
"""
import glob, os, re, subprocess, sys

ROOT = sys.argv[1] if len(sys.argv) > 1 else "."
res = []
def add(n, ok, d=""): res.append((n, "PASS" if ok else "FAIL", d))
def info(n, d): res.append((n, "INFO", d))
def rd(*p):
    f = os.path.join(ROOT, *p)
    return open(f, encoding="utf-8").read() if os.path.isfile(f) else None

# ---- 0. Cumulative S08 run ----------------------------------------------------------
s8 = subprocess.run([sys.executable, os.path.join(ROOT, "stages", "S08", "qc", "S08_QC_CHECK.py"), ROOT],
                    capture_output=True, text=True)
m = re.search(r"SUMMARY\s+s08_checks=(\d+)\s+failed=(\d+)", s8.stdout)
info("S08 cumulative run", m.group(0) if m else "no summary")
SUPERSEDED = {
    "S09 not started": "S09 started under DEC-037",
    "Section 9: provisional selection flagged with ISS-030": "ISS-030 resolved by DEC-037; placeholder removed (DEF-012)",
    "required wording present: 'lists as superseded'": "replaced by the draft-status statement (DEF-010)",
    "Stage status: S08 submitted": "stage status now records S09",
}
S09_SRC = {"SRC-091", "SRC-092"}
s9txt = "\n".join(open(p, encoding="utf-8").read() for p in glob.glob(os.path.join(ROOT, "stages", "S09", "*.md")))
unexpected = []
for l in [x for x in s8.stdout.splitlines() if x.startswith("FAIL")]:
    k = next((k for k in SUPERSEDED if k in l), None)
    if k:
        info("S08 check superseded", f"{k} -> {SUPERSEDED[k]}"); continue
    if "S07 cumulative checks pass apart from the two superseded checks" in l:
        # (5) S07 source-coverage checks only know S02-S07 deliverables; S09 sources are cited in S09 files.
        inner = re.findall(r"FAIL  ([^\[]+?)\s+\[([^\]]*)\]", l.split("[", 1)[1])
        bad = []
        for name, det in inner:
            ids = set(re.findall(r"SRC-\d+", det))
            if name.strip() in ("no orphan sources in log", "every S07 source cited in an S07 deliverable or the Section 12 draft") \
               and ids and ids <= S09_SRC and all(i in s9txt for i in ids):
                info("S07 check superseded", f"{name.strip()} -> {', '.join(sorted(ids))} are S09 sources cited in S09 deliverables")
            else:
                bad.append(f"{name.strip()} [{det}]")
        if bad: unexpected.append("S07: " + " | ".join(bad))
        continue
    unexpected.append(l)
add("S08 cumulative checks pass apart from the listed supersessions", not unexpected, " | ".join(unexpected))
for l in s8.stdout.splitlines():
    if l.startswith("INFO  S07"): info("via S08", l[6:])

# ---- 1. Deliverables and metadata ---------------------------------------------------------
NEED = ["S09_PLAN.md", "S09_REVIEW_REPORT.md", "S09_CORRECTION_REPORT.md", "S09_QC_REPORT.md", "S09_HANDOFF.md"]
for f in NEED:
    add(f"file present: stages/S09/{f}", rd("stages", "S09", f) is not None)
add("isolated review record present", rd("stages", "S09", "S09_ISOLATED_REVIEW_RECORD.md") is not None)
FIELDS = ["Document ID", "Version", "Status", "Stage", "Date", "Depends on"]
def meta(t):
    mm = re.search(r"\| Field \| Value \|\n\|---\|---\|\n((?:\|.*\|\n)+)", t or "")
    rows = [re.match(r"\|\s*(.*?)\s*\|\s*(.*?)\s*\|$", x).groups() for x in mm.group(1).splitlines()] if mm else []
    return rows
for f in sorted(glob.glob(os.path.join(ROOT, "stages", "S09", "*.md"))):
    rows = meta(open(f, encoding="utf-8").read()); v = dict(rows); b = os.path.basename(f)
    ok = ([k for k, _ in rows] == FIELDS and v.get("Document ID") == b[:-3] and v.get("Stage") == "S09"
          and v.get("Status") in ("SUBMITTED FOR GATE", "APPROVED") and re.fullmatch(r"\d+\.\d+", v.get("Version", "")))
    add("S09 metadata header", bool(ok), b)
master = rd("proposal", "IRAA_PROPOSAL_EN_MASTER.md") or ""
mv = dict(meta(master))
add("Master is v0.2, stage S09", mv.get("Version") == "0.2" and mv.get("Stage") == "S09", f"{mv.get('Version')} {mv.get('Stage')}")
s10 = [x for x in glob.glob(os.path.join(ROOT, "stages", "S10", "*")) if not x.endswith(".gitkeep")]
add("S10 not started (stages/S10 holds no deliverables)", not s10, ", ".join(map(os.path.basename, s10)) or "empty")

# ---- 2. Proposal text corrections ------------------------------------------------------------
def sec(n):
    a = master.find(f"\n## {n}. "); b = master.find(f"\n## {n+1}. ") if n < 20 else len(master)
    return master[a:b] if a >= 0 else ""
mlines = master.splitlines()
rs = next((i for i, l in enumerate(mlines) if l.startswith("References cited in this proposal")), None)
re_ = next((i for i, l in enumerate(mlines) if l.startswith("## 20.")), None)
body = master[master.find("\n## 1. "):]
refblock = "\n".join(mlines[rs:re_]) if rs else ""
low = body.replace(refblock, "").lower()
def cells(l): return [c.strip() for c in l.strip().strip("|").split("|")]
s9rows = [cells(l) for l in sec(9).splitlines() if re.match(r"^\| \d+ \|", l)]

add("DEF-009 decision rule: adjusted p-values decide, intervals reported unadjusted",
    "adjusted p-values decide" in low and "intervals are reported unadjusted" in low)
add("DEF-009 old interval-only decision wording absent from Sections 8 and 12",
    "lower limit of the 95% interval of the paired difference above" not in low
    and "non-inferiority is concluded only when the lower limit" not in low)
add("DEF-009 Section 8 specifications 1 to 3 state the Holm-adjusted rule",
    "holm-adjusted" in sec(8).lower() and sec(8).count("same decision rule") == 2)
add("DEF-010 EMA status: draft reference and absence of an adopted version stated",
    "EMA/301654/2025" in sec(12) and "no adopted version or legal effective date" in sec(12)
    and "states that it is superseded" in sec(12))
add("DEF-010 EMA draft guideline listed in Section 19", "EMA/301654/2025" in refblock)
add("DEF-011/DEC-038 EPO: charter and OPS FAQ both stated, FAQ value conditional",
    "1 mbit per second" in low and "ten searches per minute per ip address as a rule" in low and "depending on operational circumstances" in low)
add("DEF-012 Section 9: no ISS-030 placeholder and no 'provisional selection'",
    "ISS-030" not in sec(9) and "provisional selection" not in sec(9).lower())
add("DEF-012 no owner-decision placeholder remains for a resolved issue", "[OWNER DECISION REQUIRED" not in body)
pq = next((r for r in s9rows if "PQAI" in r[1]), [])
add("DEF-013 PQAI row: Type 'Industry project', bare Outcome; collaborative initiative and paid tiers in Notes",
    bool(pq) and pq[2] == "Industry project" and pq[4] == "Commercial product"
    and "collaborative initiative" in pq[6].lower() and "paid API tiers" in pq[6])
add("Isolated IR-10: Section 9 Outcome and Status cells hold bare form categories",
    bool(s9rows) and all(r[4] in ("Commercial product", "Laboratory prototype") and r[5] in ("In progress", "Completed") for r in s9rows))
# Isolated-review corrections
add("Isolated IR-02: sample-size check uses 80% probability, not half-width = margin",
    "80% probability of concluding non-inferiority" in body and "half-width is no larger than the margin" not in body)
add("Isolated IR-03: specification 3 has a rule for both outcomes of the sizing decision",
    "Otherwise: paired difference reported with its 95% interval and no non-inferiority claim" in sec(8)
    and "expected rather than exceptional" not in body)
add("Isolated IR-04: interval for paired binary outcome named; Clopper-Pearson limited to single proportions",
    "score-type interval for paired proportions" in body and "intervals for single proportions" in body)
add("Isolated IR-05: editor of the confirmatory query defined; unedited query exploratory",
    "acting in the assessor role" in sec(12) and "unedited automatic query is reported as exploratory" in sec(12)
    and "by a project judge in the assessor role" in sec(8))
add("Isolated IR-06: confirmatory family listed; 'inferior' defined",
    "confirmatory family of a track consists of" in body and '"Inferior" means' in body)
add("Isolated IR-07: retention keeps handover collections",
    "retained and handed over where their licences permit" in sec(12) and "substitute test collections whose licences permit handover" in sec(7))
add("Isolated IR-08: manual route records exact query text and is counted in specification 5",
    "records in the prototype the exact query text" in sec(12) and "manual-entry queries counted" in sec(8))
add("Isolated IR-09: Section 7 assumption restates both conditions", "external AI services" not in body)
add("Isolated IR-15: no 'S10' in running prose outside placeholders",
    not re.search(r"S10(?! *\])", re.sub(r"\[OPEN — S10\]", "", body)))
add("Isolated IR-26: single term 'terms note'", "permission note" not in body)
add("DEF-014 superlatives removed or scoped",
    "largest set" not in low and "the only one of the four" not in low
    and "of the pages read for the four named vendors" in low)
add("DEF-016 Section 9 Type entries use form source categories (industry project / publication)",
    bool(s9rows) and all(r[2].startswith(("Industry project", "Publication")) for r in s9rows), str([r[2] for r in s9rows]))
add("DEF-017 unreferenced 'two further idea-management products' absent", "two further idea-management products" not in low)
add("DEF-018 universal vendor claim scoped", "no vendor publishes" not in low and "in the vendor documentation we read" in low)
add("DEF-019 circular authorization sentence replaced",
    "or text the authorization covers" not in low and "only text within its scope may be sent" in low)
add("DEF-020 R2 retrieval assumption qualified", "where a solution-example source can be imported as a collection" in low)
add("DEF-021 timing-check wording", "removed from the timing test" not in low and "removed from the candidate configuration set" in low)
add("DEF-022 Section 8 flags specification 3 sample-size limitation", "planned 30 need statements" in sec(8))
add("DEF-023 model input limits wording matches the tool table", "their input limits where stated" in low)
add("DEF-024 SOLVENT described as in its abstract", "finds more analogies than baseline information-retrieval approaches" in sec(9))
add("DEF-026 ISO/IEC 20000 reading stated", "reads the latter as iso/iec 20000-1" in low)
add("DEF-015 alignment sentence appears once (Section 8 only)", low.count("designed to support alignment") == 1, str(low.count("designed to support alignment")))
add("DEF-015 assessor walk-through described once (Section 12)", low.count("structured walk-through") == 1)
# Disclosure rule still complete after edits (ISS-052)
for ph in ["approval of a query does not authorize disclosure", "query approval never substitutes for disclosure clearance",
           "two separate conditions", "every query, in either case, still requires the assessor's approval"]:
    add(f"disclosure rule wording present: '{ph}'", ph in low)
add("No working identifiers or ISS references in proposal text",
    not re.search(r"\b(ISS-\d+|DEF-\d+|SRC-\d+|CLM-\d+|MS-\d+|DEC-\d+)\b", body))
wc = len(master.split())
add("Master not longer than the S08 baseline (12,874 words; DEC-038 EPO refinement allowance to 12,900)", wc <= 12900, str(wc))
add("Every Section 9 URL and new reference logged (projectpq.ai, EMA status page)",
    all(u in (rd("project", "02_SOURCE_LOG.md") or "") for u in ["https://projectpq.ai/",
        "https://www.ema.europa.eu/en/non-inferiority-equivalence-comparisons-clinical-trials-scientific-guideline"]))

# ---- 3. Registers -----------------------------------------------------------------------------
df = rd("project", "03_DEFECT_LOG.md") or ""
add("Defect log: DEF-009 to DEF-039 present", all(re.search(rf"^\| DEF-0{i:02d} \|", df, re.M) for i in range(9, 40)))
open_cm = [l for l in df.splitlines() if re.match(r"^\| DEF-\d+ \|", l) and ("| Critical |" in l or "| Major |" in l) and "| OPEN" in l]
add("No open Critical or Major defect", not open_cm, " | ".join(l[:40] for l in open_cm))
oi = rd("project", "00_OPEN_ISSUES_REGISTER.md") or ""
add("ISS-055 and ISS-056 registered", re.search(r"^\| ISS-055 \|", oi, re.M) and re.search(r"^\| ISS-056 \|", oi, re.M))
i54 = next((l for l in oi.splitlines() if l.startswith("| ISS-054 |")), "")
add("ISS-054 carries the S09 correction for owner confirmation", "S09" in i54)
st = rd("project", "00_STAGE_STATUS.md") or ""
add("Stage status records S09 submitted for gate", "| Stage | S09 |" in st and ("S09 SUBMITTED FOR GATE" in st or "S09 approved with CONDITIONAL PASS (DEC-038)" in st))
ho = rd("stages", "S09", "S09_HANDOFF.md") or ""
add("Handoff lists owner decisions and S10 inputs", "## Owner decisions" in ho and "## Inputs for S10" in ho)
sk = rd("project", "00_SKILL_REGISTER.md") or ""
add("Skill checkpoint recorded for S09", re.search(r"^\| SKL-010 \| S09 \|", sk, re.M) is not None)

for n, s, d in res:
    print(f"{s:5} {n}" + (f"  [{d}]" if d else ""))
fails = sum(1 for _, s, _ in res if s == "FAIL")
print(f"\nSUMMARY  s09_checks={len([r for r in res if r[1] != 'INFO'])}  failed={fails}  info={len([r for r in res if r[1] == 'INFO'])}")
print("RESULT " + ("PASS" if fails == 0 else "FAIL"))
sys.exit(1 if fails else 0)
