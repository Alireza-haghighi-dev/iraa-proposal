#!/usr/bin/env python3
"""Insert the English master into the sanitized native Word form (DEC-043).

Usage: python3 -I stages/S10/qc/S10_BUILD_FORM_DOCX.py <blank_form.docx> <master.md> <out.docx>

Rules implemented: the 20 headings, every table grid, column order, cell properties and merges are kept;
rows are added only by cloning an existing data row of the same table; template guidance is removed only
in sections whose content is now inserted; inserted narrative copies the form's own body paragraph format
(Calibri 12 pt, regular, no numbering); table cells keep the form's native cell format.
"""
import copy, re, sys
import docx
from docx.oxml.ns import qn

BASE, MASTER, OUT = sys.argv[1:4]
d = docx.Document(BASE)
body = d.element.body
W = lambda t: qn("w:" + t)

def text(el):
    return "".join(t.text or "" for t in el.iter(W("t")))

def is_heading(el):
    ps = el.find(W("pPr"))
    st = ps.find(W("pStyle")) if ps is not None else None
    return el.tag == W("p") and st is not None and st.get(W("val")) == "Heading1"

# ---- master sections -------------------------------------------------------------------
M = open(MASTER, encoding="utf-8").read()
M = M[M.find("## 1. Project title"):]
parts = re.split(r"^## (\d+)\. .*$", M, flags=re.M)
SEC = {int(parts[i]): parts[i + 1] for i in range(1, len(parts), 2)}
def clean(s):
    s = s.replace("[OPEN — S10]", "[OPEN]").replace("`", "")
    return re.sub(r"\s+", " ", s).strip()
def blocks(n):
    return [b.strip() for b in SEC[n].strip().split("\n\n") if b.strip()]
def table_rows(block):
    rows = [l for l in block.splitlines() if l.startswith("|") and not l.startswith("| ---") and not l.startswith("|---")]
    return [[clean(c) for c in r.strip().strip("|").split("|")] for r in rows[1:]]

# ---- templates ---------------------------------------------------------------------------
els = list(body.iterchildren())
heads = {int(re.match(r"(\d+)\.", text(e)).group(1)): e for e in els if is_heading(e)}
assert sorted(heads) == list(range(1, 21)), sorted(heads)
NARR = next(e for e in els if e.tag == W("p") and text(e) == "[PROJECT RATIONALE AND SIGNIFICANCE]")
NARR = copy.deepcopy(NARR)

def para(t):
    p = copy.deepcopy(NARR)
    runs = p.findall(W("r"))
    for r in runs[1:]: p.remove(r)
    tt = runs[0].find(W("t")); tt.text = t; tt.set("{http://www.w3.org/XML/1998/namespace}space", "preserve")
    return p

def section_elems(n):
    out, on = [], False
    for e in body.iterchildren():
        if e is heads[n]: on = True; continue
        if on and (is_heading(e) or e.tag == W("sectPr")): break
        if on: out.append(e)
    return out

def remove_paras(n, keep=lambda t: False):
    for e in section_elems(n):
        if e.tag == W("p") and text(e).strip() and not keep(text(e)):
            body.remove(e)

def insert_after(ref, items):
    for it in items:
        ref.addnext(it); ref = it
    return ref

def tables(n):
    return [e for e in section_elems(n) if e.tag == W("tbl")]

def set_cell(tc, t):
    ps = tc.findall(W("p"))
    for p in ps[1:]: tc.remove(p)
    p = ps[0]
    runs = p.findall(W("r"))
    if not runs:
        r = p.makeelement(W("r"), {}); p.append(r); runs = [r]
    for r in runs[1:]: p.remove(r)
    r = runs[0]
    for t_ in r.findall(W("t")) + r.findall(W("br")): r.remove(t_)
    te = r.makeelement(W("t"), {}); te.text = t
    te.set("{http://www.w3.org/XML/1998/namespace}space", "preserve"); r.append(te)

def cells(tr): return tr.findall(W("tc"))
def rows(tbl): return tbl.findall(W("tr"))

def clone_row_after(tr):
    new = copy.deepcopy(tr); tr.addnext(new); return new

ADDED = []  # (section, description) for the QC record

# ---- headings with inline fields ------------------------------------------------------------
def heading_replace(n, old, new):
    for t in heads[n].iter(W("t")):
        if old in (t.text or ""):
            t.text = t.text.replace(old, new); return
    raise AssertionError((n, old))
heading_replace(1, "[PROJECT TITLE]", clean(blocks(1)[0]))
heading_replace(4, "[MONTHS] months and [PERSON-HOURS] person-hours", "6 months and 1,291 person-hours")

# ---- 1 -------------------------------------------------------------------------------------------
remove_paras(1, keep=lambda t: t.startswith("Template guidance"))

# ---- 5: classification marks --------------------------------------------------------------------
t5 = tables(5)[0]
CHOSEN = ["Product / system", "Demand-driven", "Technology development", "Design", "Build", "Testing", "Independent project"]
marked = []
for tc in t5.iter(W("tc")):
    tx = text(tc)
    for c in CHOSEN:
        if tx.strip() == "[ ] " + c:
            for t in tc.iter(W("t")):
                if "[ ]" in (t.text or ""): t.text = t.text.replace("[ ]", "[X]", 1)
            marked.append(c)
assert sorted(marked) == sorted(CHOSEN), marked
remove_paras(5)
insert_after(t5, [para(clean(b)) for b in blocks(5) if not b.startswith("|")])

# ---- 6, 7: narrative only -------------------------------------------------------------------------
for n in (6, 7):
    remove_paras(n)
    insert_after(heads[n], [para(clean(b)) for b in blocks(n)])

# ---- 8: features and specifications as numbered paragraphs (no table added) -------------------------
remove_paras(8)
items = []
for b in blocks(8):
    if b.startswith("|"):
        rs = table_rows(b)
        if len(rs[0]) == 3:
            items += [para("Feature %s. %s (%s)." % (r[0], r[1].rstrip("."), r[2])) for r in rs]
        else:
            items += [para("Specification %s. %s. Metric and test condition: %s. Target: %s." % (r[0], r[1], r[2].rstrip("."), r[3].rstrip("."))) for r in rs]
    else:
        items.append(para(clean(b)))
insert_after(heads[8], items)

# ---- 9: comparators -----------------------------------------------------------------------------------
b9 = blocks(9)
t9 = tables(9)[0]
for e in section_elems(9):
    if e.tag == W("p") and text(e).strip() and not text(e).startswith("Comparison and distinguishing"):
        body.remove(e)
insert_after(heads[9], [para(clean(b9[0]))])
rs9 = table_rows(next(b for b in b9 if b.startswith("|")))
assert len(rs9) == 6
trs = rows(t9)
while len(rows(t9)) - 1 < len(rs9):
    clone_row_after(rows(t9)[-1]); ADDED.append((9, "data row %d" % (len(rows(t9)) - 1)))
for tr, r in zip(rows(t9)[1:], rs9):
    for tc, v in zip(cells(tr), r): set_cell(tc, v)
comp = [b for b in b9[1:] if not b.startswith("|")]
fields = [e for e in section_elems(9) if e.tag == W("p") and text(e).startswith("Comparison and distinguishing")]
assert len(fields) == 3
last = fields[-1]
for k in range(4, 7):
    new = copy.deepcopy(fields[0]); last.addnext(new); last = new; fields.append(new)
    ADDED.append((9, "comparison field for entry %d" % k))
for k, (f, txt) in enumerate(zip(fields, comp[:6]), 1):
    for r in f.findall(W("r"))[1:]: f.remove(r)
    f.find(W("r")).find(W("t")).text = "Comparison and distinguishing features relative to entry %d: %s" % (k, clean(txt))
insert_after(fields[-1], [para(clean(b)) for b in comp[6:]])

# ---- 11: roadmap ----------------------------------------------------------------------------------------
b11 = blocks(11)
remove_paras(11)
t11 = tables(11)[0]
insert_after(heads[11], [para(clean(b11[0]))])
rs11 = table_rows(b11[1])
assert len(rs11) == 4
new = clone_row_after(rows(t11)[-1]); ADDED.append((11, "row 'Future phase 3'"))
labels = ["Current phase", "Future phase 1", "Future phase 2", "Future phase 3"]
for tr, r, lab in zip(rows(t11)[1:], rs11, labels):
    vals = [lab] + r[1:]
    for tc, v in zip(cells(tr), vals): set_cell(tc, v)
insert_after(t11, [para(clean(b)) for b in b11[2:]])

# ---- 12: methodology (subheadings as plain paragraphs; tool table as sentences) ---------------------------
remove_paras(12)
items = []
for b in blocks(12):
    if b.startswith("### "):
        items.append(para(b[4:].strip()))
    elif b.startswith("|"):
        for r in table_rows(b):
            items.append(para("%s. Use: %s. Version: %s. Status: %s." % (r[0], r[1], r[2].rstrip("."), r[3].rstrip("."))))
    else:
        items.append(para(clean(b)))
insert_after(heads[12], items)

# ---- 13: activities ---------------------------------------------------------------------------------------
b13 = blocks(13)
remove_paras(13)
t13 = tables(13)[0]
insert_after(heads[13], [para(clean(b13[0]))])
rs13 = table_rows(b13[1])
assert len(rs13) == 7
total13 = rows(t13)[-1]
while len(rows(t13)) - 2 < 7:
    clone_row_after(rows(t13)[-2]); ADDED.append((13, "data row %d" % (len(rows(t13)) - 2)))
for tr, r in zip(rows(t13)[1:-1], rs13):
    for tc, v in zip(cells(tr), r): set_cell(tc, v)
set_cell(cells(rows(t13)[-1])[-1], "1,291")
insert_after(t13, [para(clean(b)) for b in b13[2:]])

# ---- 14: team -----------------------------------------------------------------------------------------------
b14 = blocks(14)
remove_paras(14, keep=lambda t: t.startswith("Enter confirmed team-member names"))
t14 = tables(14)[0]
rs14 = table_rows(b14[0])
assert len(rs14) == 4
clone_row_after(rows(t14)[-1]); ADDED.append((14, "row 4 (neutral placeholder for the fourth member)"))
for tr, r in zip(rows(t14)[1:], rs14):
    for tc, v in zip(cells(tr), r): set_cell(tc, v)
insert_after(t14, [para(clean(b)) for b in b14[1:]])

# ---- 15: costs (guidance kept: costs unresolved) ----------------------------------------------------------
b15 = blocks(15)
t15 = tables(15)[0]
r15 = rows(t15)
set_cell(cells(r15[1])[2], "Project team: technical lead 526 person-hours; three contributors, 255 person-hours each")
set_cell(cells(r15[1])[3], "1,291 person-hours")
for k in (4, 5): set_cell(cells(r15[1])[k], "[pending approved rate]")
set_cell(cells(r15[2])[2], "Other approved personnel: none planned")
set_cell(cells(r15[3])[2], "None planned")
set_cell(cells(r15[6])[2], "Patent-service access above the free access tier, only if measured query volume requires it [pending owner approval]")
set_cell(cells(r15[12])[2], "Reference evaluation environment: existing equipment, purchase or rental [pending owner decision]")
set_cell(cells(r15[-1])[-1], "[pending approved costs]")
insert_after(t15, [para(clean(b)) for b in b15[1:]])

# ---- 16: Gantt ------------------------------------------------------------------------------------------------
b16 = blocks(16)
remove_paras(16, keep=lambda t: t.startswith(("Assign approved personnel", "Calculate each activity", "Final checks")))
t16 = tables(16)[0]
rs16 = table_rows(b16[0])
assert len(rs16) == 7
while len(rows(t16)) - 3 < 7:
    clone_row_after(rows(t16)[-2]); ADDED.append((16, "data row %d" % (len(rows(t16)) - 3)))
for tr, r in zip(rows(t16)[2:-1], rs16):
    vals = r[:3] + r[3:15] + ["[pending]", "[pending]"]
    for tc, v in zip(cells(tr), vals): set_cell(tc, v)
tot = cells(rows(t16)[-1])
set_cell(tot[1], "1,291"); set_cell(tot[3], "[pending]")
insert_after(t16, [para(clean(b)) for b in b16[1:]])

# ---- 17: risks in the form's category order -------------------------------------------------------------------
remove_paras(17)
t17 = tables(17)[0]
rs17 = table_rows(blocks(17)[0])
assert len(rs17) == 16
cats = ["Technical", "Data / information", "Schedule", "Financial", "Other"]
proto = {text(cells(tr)[1]).strip(): tr for tr in rows(t17)[1:]}
assert sorted(proto) == sorted(cats)
for c in cats:
    mine = [r for r in rs17 if r[1] == c]
    anchor = proto[c]
    for k in range(1, len(mine)):
        anchor = clone_row_after(anchor); ADDED.append((17, "additional '%s' row" % c))
for tr, r in zip(rows(t17)[1:], rs17):
    for tc, v in zip(cells(tr), r): set_cell(tc, v)

# ---- 19: remarks and references -------------------------------------------------------------------------------
remove_paras(19)
items = []
for b in blocks(19):
    for line in b.splitlines():
        if line.strip(): items.append(para(clean(line)))
insert_after(heads[19], items)

d.core_properties.title = "Intelligent Requirements Assessment Assistant - proposal, English working copy (not submission-ready)"
d.core_properties.subject = "Filled from the English master; local fields, costs and weights open"
d.save(OUT)
with open(OUT + ".added.txt", "w") as f:
    for s, desc in ADDED: f.write("Section %d: %s\n" % (s, desc))
print("written", OUT, "rows/fields added:", len(ADDED))
