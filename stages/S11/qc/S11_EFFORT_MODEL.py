#!/usr/bin/env python3
"""S11 effort and six-month capacity model (provisional; engineering judgment, not measured data).

Each task: (id, WP, description, lead hours, contributor hours, month shares M1..M6).
Coordination and review are counted ONCE (EH-10 check): each WP has one review line; team
coordination is one cross-cutting line distributed by month and then attributed to WPs in
proportion to their task hours in that month. Run: python3 stages/S11/qc/S11_EFFORT_MODEL.py
Prints the markdown tables used in S11_EFFORT_AND_SCHEDULE and exits 0 if internal sums agree.
"""
T = [
# WP1 Prototype design specification and data-protection baseline
("T1.1",1,"Field map, import format, substitute schema, configurable assessment template",6,14,(1,0,0,0,0,0)),
("T1.2",1,"Record state model as a transition table with the two approval properties",14,4,(1,0,0,0,0,0)),
("T1.3",1,"Interface specifications (retrieval, connector, record and export, identity); platform adapter specified only",12,6,(.7,.3,0,0,0,0)),
("T1.4",1,"Information security risk assessment per data flow, role matrix, retention procedure",10,16,(.5,.5,0,0,0,0)),
("T1.5",1,"Development and reference environment; library selection, pinning and licence check; small vertical prototype (import, BM25, display)",12,20,(1,0,0,0,0,0)),
("R1",1,"Technical review of WP1 outputs (design review)",8,4,(.6,.4,0,0,0,0)),
# WP2 Evaluation protocol, test collections and evaluation harness
("T2.1",2,"Licence check of two or three substitute candidates on their original distributions",4,8,(1,0,0,0,0,0)),
("T2.2",2,"Evaluation protocol and judging guide (grade scales, decision rule, sample sizes); freeze before test judging",18,6,(.2,.5,.3,0,0,0)),
("T2.3",2,"Substitute collection for similar submissions: time-ordered split, 60 queries, manifest",4,20,(0,.6,.4,0,0,0)),
("T2.4",2,"50 public need statements used for both solution-example and prior-art evaluation; source indexing",4,26,(0,.5,.5,0,0,0)),
("T2.5",2,"Harness: toolkit metrics plus project code for success@10, judged@10, paired bootstrap, randomization test, Clopper-Pearson, agreement; unit tests",12,26,(0,.5,.5,0,0,0)),
("T2.6",2,"Reproduction of a published BM25 run",2,8,(0,0,1,0,0,0)),
("R2",2,"Technical review of WP2 outputs",8,2,(.2,.4,.4,0,0,0)),
# WP3 Ingestion and retrieval for similar submissions and solution examples
("T3.1",3,"Import adapter (delimited, JSON Lines), validation, import report, source registry",4,26,(0,1,0,0,0,0)),
("T3.2",3,"Normalization, exact hashes, shingle near-duplicate fingerprints, passage splitting, language tag",6,22,(0,1,0,0,0,0)),
("T3.3",3,"Lexical index and exact vector index per collection, with index versions",8,16,(0,.7,.3,0,0,0)),
("T3.4",3,"Retrieval service: BM25, one dense encoder, reciprocal rank fusion, date filter, evidence passage",28,18,(0,.6,.4,0,0,0)),
("T3.5",3,"Display threshold and 'no example above threshold' signal on development data",6,4,(0,0,1,0,0,0)),
("T3.6",3,"Encoding and search timing at two corpus sizes",4,8,(0,0,0,.5,.5,0)),
("T3.7",3,"Unit and integration tests",4,20,(0,.5,.5,0,0,0)),
("R3",3,"Technical review and integration of WP3 outputs",12,2,(0,.4,.4,.2,0,0)),
# WP4 External prior-art retrieval with query approval
("T4.1",4,"Connector contract, result cache with provenance, rate limiter, retries",12,16,(0,0,.8,.2,0,0)),
("T4.2",4,"One patent-service connector with smoke test",6,18,(0,0,.7,.3,0,0)),
("T4.3",4,"Query construction, disclosure clearance, assessor approval of exact text, payload-hash logging",18,10,(0,0,.5,.5,0,0)),
("T4.4",4,"Manual-entry fallback recording query text and clearance",2,10,(0,0,0,1,0,0)),
("T4.5",4,"Contract and bypass tests for both conditions",8,14,(0,0,0,1,0,0)),
("R4",4,"Technical review of WP4 outputs",8,2,(0,0,.5,.5,0,0)),
# WP5 Assessment record, review interface and approval controls
("T5.1",5,"Record service: transition table, versioning, approval binding, outcome-field database trigger",30,14,(0,.2,.4,.4,0,0)),
("T5.2",5,"Accounts and roles using the framework's authentication; permission checks",4,14,(0,0,.5,.5,0,0)),
("T5.3",5,"Insert-only audit log with hash chain",6,10,(0,0,0,1,0,0)),
("T5.4",5,"Lightweight server-rendered review interface: evidence-first lists, query approval, template form, approve and return",10,50,(0,0,.3,.7,0,0)),
("T5.5",5,"Exports: schema-validated JSON record, readable report, decision log",2,16,(0,0,0,1,0,0)),
("T5.6",5,"Generated approval-enforcement suite (every state, event and role; expired and replayed requests; re-approval; hash chain)",10,24,(0,0,0,1,0,0)),
("R5",5,"Technical review of WP5 outputs",12,2,(0,0,.4,.6,0,0)),
# WP6 Prototype integration and evaluation
("T6.1",6,"Integrated release on the reference environment; deployment scripts; system-level tests",22,18,(0,0,0,.4,.6,0)),
("T6.2",6,"Pilot judging on development queries; one guide revision; agreement; sample-size check",8,14,(0,0,0,.5,.5,0)),
("T6.3",6,"Test-pool judging with 20% double judging; deeper check; unaided and edited external queries",8,61,(0,0,0,0,1,0)),
("T6.4",6,"Single test run; approval, disclosure, attribution and response-time tests",6,14,(0,0,0,0,1,0)),
("T6.5",6,"Analysis with intervals; error analysis; corrective development",24,24,(0,0,0,0,.6,.4)),
("T6.6",6,"Evaluation report by data track",12,10,(0,0,0,0,.3,.7)),
("R6",6,"Technical review of WP6 outputs",10,2,(0,0,0,.1,.5,.4)),
# WP7 Technical documentation and handover
("T7.1",7,"As-built design specification; deployment and operation instructions",10,18,(0,0,0,0,.3,.7)),
("T7.2",7,"Risk assessment update; deletion of project data with record",4,8,(0,0,0,0,0,1)),
("T7.3",7,"Code package, component and licence inventory, sponsor-data scan",2,10,(0,0,0,0,0,1)),
("T7.4",7,"Deployment rehearsal by a member not involved in the deployment scripts; fixes",4,10,(0,0,0,0,0,1)),
("T7.5",7,"Defect resolution and final reproducibility check from stored run and judgment files",12,14,(0,0,0,0,0,1)),
("T7.6",7,"Handover demonstration, acceptance record, continuity notes",6,6,(0,0,0,0,0,1)),
("R7",7,"Technical review of WP7 outputs",6,2,(0,0,0,0,.3,.7)),
]
# Team coordination, counted once: weekly one-hour meeting of four members over 26 weeks (104 h, lead 26, contributors 78)
# plus task briefing by the lead, two hours a week (52 h). Month 1 is shorter in productive load but meetings run every week.
COORD_L, COORD_C = 26 + 52, 78
CMON = (1/6,)*6
TITLES = {1:"Prototype design specification and data-protection baseline",2:"Evaluation protocol, test collections and evaluation harness",
3:"Ingestion and retrieval for similar submissions and solution examples",4:"External prior-art retrieval with query approval",
5:"Assessment record, review interface and approval controls",6:"Prototype integration and evaluation",7:"Technical documentation and handover"}
OLD = {1:210,2:290,3:380,4:215,5:400,6:414,7:140}

for t in T: assert abs(sum(t[5]) - 1) < 1e-9, t[0]
mL = [sum(t[3]*t[5][m] for t in T) + COORD_L*CMON[m] for m in range(6)]
mC = [sum(t[4]*t[5][m] for t in T) + COORD_C*CMON[m] for m in range(6)]
# attribute coordination to WPs by their share of task hours in each month
wpL = {w:0.0 for w in TITLES}; wpC = {w:0.0 for w in TITLES}
for m in range(6):
    tot = sum((t[3]+t[4])*t[5][m] for t in T)
    for t in T:
        sh = (t[3]+t[4])*t[5][m]/tot
        wpL[t[1]] += t[3]*t[5][m] + COORD_L*CMON[m]*sh
        wpC[t[1]] += t[4]*t[5][m] + COORD_C*CMON[m]*sh
# round per WP so that WP totals add to the overall totals
def rnd(d, target):
    r = {k: int(v) for k, v in d.items()}; rem = target - sum(r.values())
    for k in sorted(d, key=lambda k: d[k]-int(d[k]), reverse=True)[:rem]: r[k] += 1
    return r
TL = round(sum(mL)); TC = round(sum(mC))
RL = rnd(wpL, TL); RC = rnd(wpC, TC)
out = []
out.append("| WP | Title | Technical lead | Contributors | Total | Earlier provisional (S10) |")
out.append("|---|---|---|---|---|---|")
for w in TITLES:
    out.append(f"| WP{w} | {TITLES[w]} | {RL[w]} | {RC[w]} | {RL[w]+RC[w]} | {OLD[w]} |")
out.append(f"| Total | | {TL} | {TC} | {TL+TC} | {sum(OLD.values())} |")
out.append("")
out.append("| Month | Technical lead (h) | Contributors combined (h) | Per contributor if shared equally (h) | Team total (h) |")
out.append("|---|---|---|---|---|")
for m in range(6):
    out.append(f"| {m+1} | {round(mL[m])} | {round(mC[m])} | {round(mC[m]/3)} | {round(mL[m]+mC[m])} |")
out.append(f"| Total | {TL} | {TC} | {round(TC/3)} | {TL+TC} |")
out.append("")
out.append("| WP | " + " | ".join(f"M{m+1}" for m in range(6)) + " |")
out.append("|---|" + "---|"*6)
for w in TITLES:
    row = [sum((t[3]+t[4])*t[5][m] for t in T if t[1]==w) for m in range(6)]
    out.append(f"| WP{w} | " + " | ".join(str(round(x)) if x >= .5 else "" for x in row) + " |")
print("\n".join(out))
print(f"\nPEAK lead={max(round(x) for x in mL)} contributors_each={max(round(x/3) for x in mC)} month1_team={round(mL[0]+mC[0])} "
      f"task_lead={sum(t[3] for t in T)} task_contrib={sum(t[4] for t in T)} coord={COORD_L+COORD_C} review={sum(t[3]+t[4] for t in T if t[0].startswith('R'))}")

if __name__ == "__main__" and "--tasks" in __import__("sys").argv:
    print("\n| Task | WP | Work | Lead (h) | Contributors (h) | Months |")
    print("|---|---|---|---|---|---|")
    for t in T:
        ms = ", ".join(f"M{m+1}" for m in range(6) if t[5][m] > 0)
        print(f"| {t[0]} | WP{t[1]} | {t[2]} | {t[3]} | {t[4]} | {ms} |")
    print(f"| C | All | Team coordination: weekly one-hour meeting of four members over 26 weeks; task briefing by the lead, 2 h per week | {COORD_L} | {COORD_C} | M1–M6 |")
    print(f"| Total | | | {sum(t[3] for t in T)+COORD_L} | {sum(t[4] for t in T)+COORD_C} | |")
