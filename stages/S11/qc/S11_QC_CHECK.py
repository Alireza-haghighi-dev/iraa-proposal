#!/usr/bin/env python3
"""S11_QC_CHECK.py - reproducible checks for S11 (project right-sizing, six-month rebaseline).

Usage (from the repository root):  python3 stages/S11/qc/S11_QC_CHECK.py . [path/to/PROPOSAL_FORM_EN_WORKING_V1.md]

Cumulative: runs the S09 and S10 suites (S09 runs S08, S07 and the safety scan) and accepts
only failures caused by deliberate S11 design changes, each listed with its reason and
re-checked by an S11 check below. Then checks the master against the S11 model and scope,
the effort model's internal consistency and the generated tables, registers and deliverables.
It does not judge meaning or writing quality. Standard library only. Exit 0 = pass.
"""
import glob, importlib.util, io, os, re, subprocess, sys, contextlib
sys.dont_write_bytecode = True

ROOT = sys.argv[1] if len(sys.argv) > 1 else "."
FORM = sys.argv[2] if len(sys.argv) > 2 else None
res = []
def add(n, ok, d=""): res.append((n, "PASS" if ok else "FAIL", d))
def info(n, d): res.append((n, "INFO", d))
def rd(*p):
    f = os.path.join(ROOT, *p)
    return open(f, encoding="utf-8").read() if os.path.isfile(f) else None
def run(stage, extra=()):
    return subprocess.run([sys.executable, os.path.join(ROOT, "stages", stage, "qc", f"{stage}_QC_CHECK.py"), ROOT, *extra],
                          capture_output=True, text=True).stdout

# ---- 0. Cumulative runs with S11 supersessions ------------------------------------------
ACC_S08 = {  # failures of the S08 suite reported inside the S09 suite
 "Section 13: seven activities identical to the frozen titles and figures": "titles unchanged; figures replaced by the S11 provisional estimate (checked in §2)",
 "Section 13 total = 2,004": "total replaced by 1,291 (checked in §2)",
 "Arithmetic: 10^6 x 1,024 x 4 bytes": "one-million-item sentence removed with the larger corpus size (§1)",
 "Section 4: duration and total effort reserved for S10": "Section 4 states the planned six months and the provisional total (§2)",
 "'superiority tested second, not required'": "replaced by the interval rule; 'not required' wording re-checked (§1)",
 "'non-inferiority not established'": "replaced by 'inconclusive' (§1)",
}
ACC_S09 = {
 "Master is v0.2": "master v0.4 / S11",
 "S10 not started": "S10 started (DEC-039)",
 "Master not longer than the S08 baseline": "replaced by the S11 body-length rule",
 "DEF-009 decision rule": "Holm rule replaced by the interval rule (S11 scope §1)",
 "DEF-009 Section 8 specifications 1 to 3": "specifications 1-3 state the interval rule",
 "Isolated IR-02": "sample-size target replaced by expected interval width recorded before the test run",
 "Isolated IR-03": "specification 3 is an estimate only; no sizing decision remains",
 "Isolated IR-05": "unedited automatic query removed; two formulations",
 "Isolated IR-06": "no confirmatory family under the interval rule",
 "DEF-021 timing-check": "timing rule rewritten for two corpus sizes (checked in §1)",
 "DEF-022 Section 8 flags specification 3": "specification 3 states that 30 statements cannot support a claim (checked in §1)",
 "Stage status records S09": "stage status records S11",
}
ACC_S10 = {
 "Master v0.3, stage S10": "master v0.4 / S11",
 "Statistical level question stated": "level question removed by the interval-only rule (ISS-055 note)",
 "'superiority tested second, not required'": "see S08 entry",
 "Malkov and Yashunin": "approximate search and its reference removed with the larger corpus size",
 "Request S06 column equals Section 13": "S10 request item 1 superseded by the S11 checkpoint",
 "Proposed planning total = 2004 + 45": "S10 request item 1 superseded by the S11 checkpoint",
 "Stage status records S10 in progress": "stage status records S11 (S10 paused)",
}
def unexpected(lines, acc):
    return [l for l in lines if not any(k in l for k in acc)]
s9 = run("S09"); bad = []
for l in [x for x in s9.splitlines() if x.startswith("FAIL")]:
    if "S08 cumulative checks pass apart from the listed supersessions" in l:
        inner = re.findall(r"FAIL\s+(.+?)(?=\s+\[|\s+\||\]|$)", l.split("[", 1)[1] if "[" in l else "")
        bad += [i for i in inner if not any(k in i for k in ACC_S08)]
    elif not any(k in l for k in ACC_S09):
        bad.append(l)
add("S09 suite: only S11-superseded failures", not bad, " | ".join(bad)[:600])
s10 = run("S10", (FORM,) if FORM else ())
s10f = [x for x in s10.splitlines() if x.startswith("FAIL") and "S09 cumulative checks pass" not in x]
u10 = unexpected(s10f, ACC_S10)
add("S10 suite: only S11-superseded failures", not u10, " | ".join(u10)[:600])
for l in s10.splitlines():
    if l.startswith("PENDING"): info("S10 pending", l[8:120])

# ---- 1. Master scope ---------------------------------------------------------------------
M = rd("proposal", "IRAA_PROPOSAL_EN_MASTER.md") or ""
body = M[M.find("## 1. Project title"):]; low = body.lower()
def sec(n):
    mm = re.search(r"^## %d\. .*?$(.*?)(?=^## \d+\. |\Z)" % n, body, re.M | re.S)
    return mm.group(1) if mm else ""
add("Master v0.4, stage S11, front matter states S11 status", "| Version | 0.4 |" in M and "| Stage | S11 |" in M and "**S11 status:**" in M)
for gone in ["re-rank", "convex", "holm", "margin-shifted", "minilm", "property-based", "1,000,000", "selected configuration",
             "three dense", "date-ordered", "0.10", "superiority test", "family-wise", "non-inferiority not established"]:
    txt = low.split("## 19.")[0] if gone != "re-rank" else low.split("## 19.")[0].replace("re-ranking and late-interaction models", "")
    add("Removed element absent from proposal text: '%s'" % gone, gone not in txt)
for need in ["reciprocal rank fusion", "fixed in advance as the primary configuration", "inconclusive", "lower bound of the interval",
             "error analysis", "two formulations", "10,000 and 100,000", "did not write the deployment scripts",
             "reproducibility check", "being better than bm25 is not required", "not re-scored on the test split",
             "30 statements are too few to support one", "no ranking parameter is tuned", "small end-to-end prototype"]:
    add("Required S11 wording: '%s'" % need, need in low)
for ph in ["approval of a query does not authorize disclosure", "query approval never substitutes for disclosure clearance",
           "checks whether relevant existing solution examples can be identified for a submitted need",
           "two separate conditions must both be met", "no transition into approved exists except the approval event"]:
    add("Preserved control wording: '%s'" % ph[:55], ph in low)
add("Proposal text has no internal capability or training statements",
    not re.search(r"\bintern\b|\binterns\b|junior|under (?:the lead's )?supervision|member [1-4]|capabilit(?:y|ies) of (?:the )?team", low)
    and low.count("training") == sum(low.count(k) for k in ("no training or learning activity", "training pairs", "training-data", "training or instructions", "retraining", "consulting, training or other line")))
refs = sec(19)
for r in ["Bruch,", "Holm,", "Malkov,", "Nogueira,", "all-MiniLM", "bge-reranker"]:
    add("Uncited reference removed: %s" % r, r not in refs)
cited = set(re.findall(r"\(([A-Z][\w\-]+)(?: et al\.| and [A-Z][\w\-]+)?, (\d{4})\)", body))
entries = [l for l in refs.splitlines() if re.match(r"^[A-Z][\w\-]+.*\(\d{4}\)", l)]
orph = [e[:30] for e in entries if not any(e.startswith(a) and "(%s)" % y in e for a, y in cited)
        and not e.startswith(("ISO/IEC", "CPMP", "European"))]
add("No uncited reference entries", not orph, str(orph))
w3 = len(subprocess.run(["git", "-C", ROOT, "show", "106329d:proposal/IRAA_PROPOSAL_EN_MASTER.md"], capture_output=True, text=True)
         .stdout.split("## 1. Project title", 1)[-1].split())
add("Body not longer than master v0.3", len(body.split()) <= w3, "%d vs %d" % (len(body.split()), w3))

# ---- 2. Effort: master versus model -----------------------------------------------------------
spec = importlib.util.spec_from_file_location("m", os.path.join(ROOT, "stages", "S11", "qc", "S11_EFFORT_MODEL.py"))
mod = importlib.util.module_from_spec(spec); buf = io.StringIO()
with contextlib.redirect_stdout(buf): spec.loader.exec_module(mod)
gen = buf.getvalue()
wp = [mod.RL[w] + mod.RC[w] for w in range(1, 8)]
num = lambda s: int(re.match(r"[\d,]+", s).group(0).replace(",", ""))
e13 = [num(l.split("|")[5].strip()) for l in sec(13).splitlines() if re.match(r"\| [1-7] \|", l)]
e16 = [num(l.split("|")[3].strip()) for l in sec(16).splitlines() if re.match(r"\| [1-7] \|", l)]
add("Section 13 effort = model WP totals", e13 == wp, "%s vs %s" % (e13, wp))
add("Section 16 effort = Section 13", e16 == e13)
tot = sum(wp)
add("Model total 1,291 = lead 526 + contributors 765", tot == 1291 and mod.TL == 526 and mod.TC == 765)
add("Total stated in Sections 4, 13 and 16", all("1,291 person-hours" in sec(n) for n in (4, 13, 16)))
add("Section 4 states six months, provisional", "6 months (planned" in sec(4) and "provisional" in sec(4))
add("Effort labelled provisional in Section 13 (seven rows and the total)", sec(13).count("(provisional)") == 8)
t13 = [l.split("|")[2].strip() for l in sec(13).splitlines() if re.match(r"\| [1-7] \|", l)]
add("Section 13 titles = model titles = Section 12 numbered titles", t13 == [mod.TITLES[w] for w in range(1, 8)]
    == [b.strip() for a, b in re.findall(r"^### (\d)\. (.+)$", sec(12), re.M)])
add("Section 16 months not yet marked", sec(16).count("[OPEN — S10]") >= 7 * 12)

# ---- 3. Model properties -------------------------------------------------------------------------
mL, mC = mod.mL, mod.mC
team = [mL[i] + mC[i] for i in range(6)]
add("Month 1 is the lightest month", team[0] == min(team), str([round(x) for x in team]))
add("Workload rises from month 1 to month 4", team[0] < team[1] < team[3] and team[0] < team[2])
add("Lead peak at most 110 h per month", max(mL) <= 110, str(round(max(mL))))
add("Month 6 holds corrective work (T6.5 or T7.5)", any(t[0] in ("T6.5", "T7.5") and t[5][5] > 0 for t in mod.T))
add("EH-10: one review line per WP, one coordination line", sorted(t[0] for t in mod.T if t[0].startswith("R")) == ["R%d" % i for i in range(1, 8)]
    and not any("coordination" in t[2].lower() for t in mod.T))
add("Every task's month shares sum to 1", all(abs(sum(t[5]) - 1) < 1e-9 for t in mod.T))
D = rd("stages", "S11", "S11_EFFORT_AND_SCHEDULE.md") or ""
tables = gen.split("\nPEAK")[0].strip().split("\n\n")
add("S11_EFFORT_AND_SCHEDULE tables match the model output", all(t.strip() in D for t in tables))
tbuf = subprocess.run([sys.executable, os.path.join(ROOT, "stages", "S11", "qc", "S11_EFFORT_MODEL.py"), "--tasks"], capture_output=True, text=True).stdout
add("Task table matches the model", tbuf.split("\n\n")[-1].strip() in D)
lead = [round(x) for x in mL]
add("Availability table matches model (lead 72 / 108 / 74; total 526)", lead[0] == 72 and max(lead) == 108 and lead[5] == 74 and "526 h" in D)
add("Shortfall at 80 h stated (480 < 526, 46 h)", "480 < 526 (short by 46 h)" in D and 6 * 80 == 480 and 526 - 480 == 46)

# ---- 4. Registers and deliverables ---------------------------------------------------------------
DL = rd("project", "00_DECISIONS_LOG.md") or ""
add("DEC-040 and DEC-041 recorded", "| DEC-040 |" in DL and "| DEC-041 |" in DL)
IS = rd("project", "00_OPEN_ISSUES_REGISTER.md") or ""
add("ISS-057 (Section 13 effort convention) registered", "| ISS-057 |" in IS)
ST = rd("project", "00_STAGE_STATUS.md") or ""
add("Stage status records S11 submitted for the owner checkpoint", "S11 corrective stage (DEC-041) submitted for the owner checkpoint" in ST)
for f in ["S11_PLAN", "S11_SCOPE_AND_TECHNICAL_PLAN", "S11_EFFORT_AND_SCHEDULE", "S11_TRACEABILITY_AND_ACCEPTANCE_IMPACT",
          "S11_CHANGE_REPORT", "S11_QC_REPORT", "S11_HANDOFF"]:
    t = rd("stages", "S11", f + ".md")
    add("Deliverable %s present with metadata" % f, bool(t) and "| Document ID | %s |" % f in t)
add("No S11 file claims approval of the revised baseline", not re.search(r"\| Status \| APPROVED \|", "\n".join(
    open(f).read() for f in glob.glob(os.path.join(ROOT, "stages", "S11", "*.md")))))
allmd = "\n".join(open(f, encoding="utf-8").read() for f in glob.glob(os.path.join(ROOT, "**", "*.md"), recursive=True))
add("Safety: no account name, repository URL, e-mail or phone", not re.search(r"github\.com/[A-Za-z0-9-]+/iraa|@[a-z0-9-]+\.(com|org|ir)\b|\+\d{2}[ \d]{8,}", allmd, re.I))
add("No Persian text", not re.search(r"[؀-ۿ]", allmd))

for n, s, d in res:
    print("%-7s %s%s" % (s, n, ("  [" + d + "]") if d else ""))
nf = sum(1 for r in res if r[1] == "FAIL")
print("\nSUMMARY  s11_checks=%d  failed=%d  info=%d" % (sum(1 for r in res if r[1] in ("PASS", "FAIL")), nf, sum(1 for r in res if r[1] == "INFO")))
print("RESULT", "PASS" if nf == 0 else "FAIL")
sys.exit(1 if nf else 0)
