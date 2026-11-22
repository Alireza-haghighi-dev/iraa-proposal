"""Aligns the master with the native-form insertion (owner instruction 2026-11-22, DEC-043): Section 14 member
rows, Section 15 rows, Section 17 order and categories as in the native form, risk cross-references, the
Faiss row (exact search only, S11). Applied once; re-running fails its assertions by design."""
import sys, pathlib, re
p = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else ".") / "proposal/IRAA_PROPOSAL_EN_MASTER.md"
s = p.read_text()
def sub(a, b):
    global s; assert s.count(a) == 1, a[:60]; s = s.replace(a, b)
sub("| Version | 0.5 |", "| Version | 0.6 |")
sub("DEC-042 |\n", "DEC-042; DEC-043 |\n")
sub("| Faiss (Douze et al., 2024) | Exact and approximate vector search |", "| Faiss (Douze et al., 2024) | Exact vector search |")
# Section 14
sub("| [OPEN — S10] | [LOCAL COMPLETION ONLY] | [LOCAL COMPLETION ONLY] | [OPEN — S10] | [OPEN — S10] | [OPEN — S10] |\n\nTeam composition, responsibilities, monthly hours and shares will be set from verified availability; shares will total 100% of the Section 13 effort.",
 "| 1 | Member 1 [LOCAL COMPLETION ONLY] | [LOCAL COMPLETION ONLY] | Technical lead: architecture, design decisions, retrieval and approval-control implementation, integration, technical review and acceptance of all activities | 87.7 (planned) | 40.7 |\n"
 "| 2 | Member 2 [LOCAL COMPLETION ONLY] | [LOCAL COMPLETION ONLY] | Project contributor: specified implementation, testing, judging and documentation tasks in activities 1 to 7, under the technical lead's direction and review [activity assignment OPEN] | 42.5 (planned) | 19.8 |\n"
 "| 3 | Member 3 [LOCAL COMPLETION ONLY] | [LOCAL COMPLETION ONLY] | Project contributor: as for Member 2 [activity assignment OPEN] | 42.5 (planned) | 19.8 |\n"
 "| 4 | Member 4 [LOCAL COMPLETION ONLY] | [LOCAL COMPLETION ONLY] | Project contributor: as for Member 2 [activity assignment OPEN] | 42.5 (planned) | 19.7 |\n\n"
 "Shares are planned person-hours divided by the 1,291 person-hours of Section 13: 526 hours for the technical lead and 255 hours for each contributor; they are rounded to one decimal so that the column totals 100.0%. Monthly hours are the planned six-month averages of these totals; they are planning figures, not confirmed availability. The technical lead's planned load is highest in months 3 and 4, at about 105 to 110 hours (Section 17, risk 13).")
# Section 15
sub("| [OPEN — S10] | [OPEN — S10] | [OPEN — S10] | [OPEN — S10] | [LOCAL COMPLETION ONLY] | [LOCAL COMPLETION ONLY] |\n\nThe cost table",
 "| 1 | Personnel | Project team: technical lead 526 person-hours; three contributors, 255 person-hours each | 1,291 person-hours | [LOCAL COMPLETION ONLY] | [LOCAL COMPLETION ONLY] |\n"
 "| 2 | Ancillary costs | Patent-service access above the free access tier, only if measured query volume requires it [pending owner approval] | [OPEN — S10] | [LOCAL COMPLETION ONLY] | [LOCAL COMPLETION ONLY] |\n"
 "| 3 | Capital items | Reference evaluation environment: existing equipment, purchase or rental [pending owner decision] | [OPEN — S10] | [LOCAL COMPLETION ONLY] | [LOCAL COMPLETION ONLY] |\n\nThe cost table")
# Section 17: native-form order and categories
rows = {int(l.split("|")[1]): l for l in s.splitlines() if re.match(r"\| \d+ \| (Technical|Information and data|Timeline|Financial) \|", l)}
assert sorted(rows) == list(range(1, 16))
order = [5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 11, 12, 15, 13, 14]
cat = {"Information and data": "Data / information", "Timeline": "Schedule"}
new = []
for i, old in enumerate(order, 1):
    c = rows[old].split("|"); c[1] = " %d " % i; c[2] = " %s " % cat.get(c[2].strip(), c[2].strip()); new.append("|".join(c))
new.append("| 16 | Other | No further execution risk identified at the proposal stage | Not applicable |")
block = "\n".join(rows[k] for k in range(1, 16))
# rows are contiguous but not in numeric order in the file (15 after 14); replace the whole block in file order
filerows = [l for l in s.splitlines() if re.match(r"\| \d+ \| (Technical|Information and data|Timeline|Financial) \|", l)]
sub("\n".join(filerows), "\n".join(new))
sub("| No. | Risk category | Risk description | Mitigation |", "| No. | Risk category | Risk description | Mitigation |")  # header kept
# cross-references
sub("(Section 17, risks 1 to 5; activity 4 for the disclosure rule)", "(Section 17, risks 1 and 7 to 10; activity 4 for the disclosure rule)")
sub("Section 17 (risks 6 to 9)", "Section 17 (risks 2 to 5)")
sub("Section 17 (risks 10 and 12)", "Section 17 (risks 6 and 12)")
p.write_text(s); print("aligned")
