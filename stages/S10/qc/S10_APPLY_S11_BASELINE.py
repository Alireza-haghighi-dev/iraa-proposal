"""Applies the owner-approved S11 baseline (DEC-042) to the master: approved effort, six months,
Gantt month marks from the approved month distribution (qc/S11_EFFORT_MODEL.py), capacity risk.
Applied once; re-running fails its assertions by design."""
import sys, pathlib, importlib.util, io, contextlib
sys.dont_write_bytecode = True
root = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else ".")
spec = importlib.util.spec_from_file_location("m", root / "stages/S11/qc/S11_EFFORT_MODEL.py")
mod = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()): spec.loader.exec_module(mod)
p = root / "proposal/IRAA_PROPOSAL_EN_MASTER.md"; L = p.read_text().split("\n")
def para(prefix, new):
    idx = [i for i, l in enumerate(L) if l.startswith(prefix)]; assert len(idx) == 1, prefix[:50]; L[idx[0]] = new
def sub(a, b, n=1):
    s = "\n".join(L); assert s.count(a) == n, (a[:60], s.count(a)); L[:] = s.replace(a, b).split("\n")
sub("| Version | 0.4 |", "| Version | 0.5 |"); sub("| Stage | S11 |", "| Stage | S10 |")
sub("S11_SCOPE_AND_TECHNICAL_PLAN; S11_EFFORT_AND_SCHEDULE |", "S11_SCOPE_AND_TECHNICAL_PLAN; S11_EFFORT_AND_SCHEDULE; DEC-042 |")
para("- **S11 status:**", "- **Baseline status:** the S11 scope, the 1,291 person-hour effort, the six-month duration and the month distribution were approved by the owner (DEC-042) and are frozen. Section 16 month marks follow the approved distribution. Sections 14 and 15, Section 16 costs and weights, the team details and all financial values wait for owner inputs (`stages/S10/S10_OWNER_DECISION_REQUEST`, v0.2). The technical lead's planned monthly hours are a scheduling assumption, not a confirmed availability. Not submission-ready.")
para("Duration: 6 months (planned;", "Duration: 6 months. Total effort: 1,291 person-hours.")
sub("| 1 (current project) | Design, Development and Testing of a Laboratory Prototype of an Intelligent Requirements Assessment Assistant | [OPEN — S10] |",
    "| 1 (current project) | Design, Development and Testing of a Laboratory Prototype of an Intelligent Requirements Assessment Assistant | 6 |")
sub(" (provisional) |", " |", n=14)
para("Total effort (provisional): 1,291 person-hours.", "Total effort: 1,291 person-hours. The figures are task estimates that include technical review and team coordination, which are not counted elsewhere. They assume that no sponsor data is released and that retrieval is evaluated on substitute data judged by project judges; judging hours are checked against the pilot, and any change is recorded with its reason. If sponsor data or assessor time becomes available, the additional work is planned separately, and assessor hours are recorded apart from project effort unless the owner decides otherwise. No training or learning activity is included.")
# Gantt: mark months with planned hours; months 7-12 left blank (six-month project)
for w in range(1, 8):
    hrs = [sum((t[3] + t[4]) * t[5][m] for t in mod.T if t[1] == w) for m in range(6)]
    marks = ["X" if h > 0 else "" for h in hrs] + [""] * 6
    old = next(l for l in L if l.startswith("| %d | %s |" % (w, mod.TITLES[w])) and l.count("|") == 18)
    cells = old.split("|"); assert cells[4].strip() == "[OPEN — S10]"
    for m in range(12): cells[4 + m] = " %s " % marks[m] if marks[m] else " "
    L[L.index(old)] = "|".join(cells)
para("Activity numbers, titles and provisional effort are identical to Section 13", "Activity numbers, titles and effort are identical to Section 13 (total 1,291 person-hours). The project runs for six months, so months 7 to 12 are not used. An X marks each month in which the activity has planned work; the month distribution follows the task dependencies, with a lighter first month and the main evaluation in month 5. Activity costs and weights will be entered from the Section 15 costs; weights will total 100%.")
para("| 13 | Financial |", "| 13 | Financial | Judging or corrective work takes longer than the planned hours | Judging hours are checked against the pilot before the test run; the funded function set is fixed in the design specification; changes to effort are recorded with their reason |")
i = next(k for k, l in enumerate(L) if l.startswith("| 14 | Financial |"))
L.insert(i + 1, "| 15 | Timeline | The technical lead's available hours in months 3 and 4 fall below the planned load of about 110 hours per month | Specified tasks are handed to contributors with review, deployment scripts start earlier and part of the reviews moves to month 5; if this is not enough, the schedule is extended and the change is recorded |")
p.write_text("\n".join(L)); print("baseline applied")
