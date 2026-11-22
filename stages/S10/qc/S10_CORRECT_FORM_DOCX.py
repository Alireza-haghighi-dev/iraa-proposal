#!/usr/bin/env python3
"""Targeted corrections to the filled native form (owner correction pass, 2026-11-22, DEC-044).

Usage: python3 -I stages/S10/qc/S10_CORRECT_FORM_DOCX.py <filled.docx> <master.md> <out.docx>

Works on a copy of the filled form; does not rebuild it. Changes, and nothing else:
 1. removes the leftover general template note ("Template guidance: remove instructional text ...");
 2. applies the approval-status wording corrections of S10_STATUS_WORDING.SUBS;
 3. replaces the eight "Specification N." paragraphs of Section 8 with one supplementary table
    (No. / Specification / Metric and test condition / Target), whose table properties and header-row
    properties are copied from the native Section 13 table and whose text comes from the master;
 4. sets inserted text in the data rows of the Section 8, 11, 13, 14, 15 and 17 tables to 12 pt (Section 9 keeps
    10 pt: reported conflict); shortens three cost cells and the Section 14 monthly-hours cells; keeps header rows
    with the next row; the No. column,
    the form's own row labels (Section 15 cost categories, Section 17 risk types, Section 11 phase labels, TOTAL),
    header rows, Section 5 and Section 20 template text and the Section 16 Gantt keep the native 10 pt;
 5. updates the document title metadata.
"""
import copy, os, re, sys
sys.dont_write_bytecode = True
import docx
from docx.oxml.ns import qn
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from S10_STATUS_WORDING import SUBS

SRC, MASTER, OUT = sys.argv[1:4]
d = docx.Document(SRC)
body = d.element.body
W = lambda t: qn("w:" + t)
def text(el): return "".join(t.text or "" for t in el.iter(W("t")))
def is_heading(el):
    ps = el.find(W("pPr")); st = ps.find(W("pStyle")) if ps is not None else None
    return el.tag == W("p") and st is not None and st.get(W("val")) == "Heading1"
def section_of(el):
    n = None
    for e in body.iterchildren():
        if is_heading(e): n = int(text(e).split(".")[0])
        if e is el: return n
LOG = []

# 1. leftover general template note
note = [p for p in body.findall(W("p")) if text(p).startswith("Template guidance: remove instructional text")]
assert len(note) == 1
body.remove(note[0]); LOG.append("Section 1: removed the general template note")

# 2. approval-status wording
for a, b in SUBS:
    hits = [p for p in body.iter(W("p")) if a in text(p)]
    assert len(hits) == 1, a[:50]
    ts = hits[0].findall(".//" + W("t"))
    assert len(ts) == 1, "paragraph has several runs"
    ts[0].text = ts[0].text.replace(a, b)
    LOG.append("Section %s: approval-status wording: '%s...'" % (section_of(hits[0]) or "?", a[:45]))

# 3. Section 8 specification table
M = open(MASTER, encoding="utf-8").read()
s8 = M.split("## 8.")[1].split("## 9.")[0]
spec_block = [b for b in s8.split("\n\n") if b.startswith("| No. | Specification |")][0]
clean = lambda c: re.sub(r"\s+", " ", c.replace("[OPEN — S10]", "[OPEN]")).strip()
rows = [[clean(c) for c in l.strip().strip("|").split("|")] for l in spec_block.splitlines()
        if l.startswith("|") and not l.startswith("| ---")]
header, data = rows[0], rows[1:]
assert header == ["No.", "Specification", "Metric and test condition", "Target"] and len(data) == 8
paras = [p for p in body.findall(W("p")) if re.match(r"Specification [1-8]\. ", text(p))]
assert len(paras) == 8
kids = list(body.iterchildren())
assert [kids.index(p) for p in paras] == list(range(kids.index(paras[0]), kids.index(paras[0]) + 8)), "not contiguous"
native = [t for t in body.findall(W("tbl")) if section_of(t) == 13][0]
GRID = [537, 1900, 3700, 2880]                      # dxa; sums to the native Section 13 width (9,017)
assert sum(GRID) == sum(int(g.get(W("w"))) for g in native.find(W("tblGrid")))
tbl = body.makeelement(W("tbl"), {})
tbl.append(copy.deepcopy(native.find(W("tblPr"))))
grid = tbl.makeelement(W("tblGrid"), {})
for g in GRID:
    gc = grid.makeelement(W("gridCol"), {W("w"): str(g)}); grid.append(gc)
tbl.append(grid)
ntr = native.findall(W("tr"))
def make_row(proto_tr, values, size):
    tr = copy.deepcopy(proto_tr)
    proto_tc = tr.findall(W("tc"))[0]
    for tc in tr.findall(W("tc")): tr.remove(tc)
    for g, v in zip(GRID, values):
        tc = copy.deepcopy(proto_tc)
        tcw = tc.find(W("tcPr")).find(W("tcW")); tcw.set(W("w"), str(round(g / sum(GRID) * 5000))); tcw.set(W("type"), "pct")
        for p in tc.findall(W("p"))[1:]: tc.remove(p)
        p = tc.find(W("p")); runs = p.findall(W("r"))
        for r in runs[1:]: p.remove(r)
        r = runs[0]
        for t in r.findall(W("t")): r.remove(t)
        rp = r.find(W("rPr"))
        if size:
            for tag in ("sz", "szCs"):
                e = rp.find(W(tag))
                if e is None: e = rp.makeelement(W(tag), {}); rp.append(e)
                e.set(W("val"), size)
        t = r.makeelement(W("t"), {}); t.text = v; t.set("{http://www.w3.org/XML/1998/namespace}space", "preserve"); r.append(t)
        tr.append(tc)
    return tr
tbl.append(make_row(ntr[0], header, None))           # native header format (bold, 10 pt)
for r in data:
    tbl.append(make_row(ntr[1], r, "24"))
paras[0].addprevious(tbl)
for p in paras: body.remove(p)
LOG.append("Section 8: eight specification paragraphs replaced by one supplementary table (4 columns, 8 data rows)")

# 4a. short cell texts where 12 pt would break words inside fixed narrow columns (meaning kept; explained
#     in the paragraph below each table): Section 14 monthly hours, Section 15 unit-cost and total cells
def set_text(tc, v):
    ts = tc.findall(".//" + W("t")); ts[0].text = v
    for t in ts[1:]: t.text = ""
for t in body.findall(W("tbl")):
    s = section_of(t)
    if s == 14:
        for tr in t.findall(W("tr"))[1:]:
            tc = tr.findall(W("tc"))[4]; old = text(tc)
            assert old.endswith(" (planned)"); set_text(tc, old.replace(" (planned)", ""))
        LOG.append("Section 14 table: monthly-hours cells shortened to the figure (planned averages are explained below the table)")
    if s == 15:
        n = 0
        for tc in t.iter(W("tc")):
            if text(tc) in ("[pending approved rate]", "[pending approved costs]"): set_text(tc, "[open]"); n += 1
        assert n == 3
        LOG.append("Section 15 table: three cost cells shortened to '[open]' (fits the 1,077-twip column at 12 pt)")

# 4b. keep each table's header row on the same page as the first data row (paragraph keep-with-next;
#     no row, cell or table property is changed)
for t in body.findall(W("tbl")):
    s = section_of(t)
    if s not in (8, 9, 11, 13, 14, 15, 17): continue
    for p in t.findall(W("tr"))[0].iter(W("p")):
        ppr = p.find(W("pPr"))
        if ppr is None: ppr = p.makeelement(W("pPr"), {}); p.insert(0, ppr)
        if ppr.find(W("keepNext")) is None:
            k = ppr.makeelement(W("keepNext"), {})
            ps = ppr.find(W("pStyle")); (ps.addnext(k) if ps is not None else ppr.insert(0, k))
    LOG.append("Section %d table: header row kept with the first data row" % s)

# 4c. 12 pt inserted text in data rows of the text tables. Section 9 keeps the native 10 pt: its fixed
#     columns of 750 to 1,246 twips (cell margins 0) cannot hold 12 pt words such as "Industry" or
#     "Commercial" without breaking them inside the word (reported conflict).
HEADER_ROWS = {8: 1, 11: 1, 13: 1, 14: 1, 15: 1, 17: 1}
for t in body.findall(W("tbl")):
    s = section_of(t)
    if s not in HEADER_ROWS: continue
    n = 0
    skip = {0, 1} if s in (15, 17) else {0}          # numbering and the form's own row labels keep the native format
    for tr in t.findall(W("tr"))[HEADER_ROWS[s]:]:
        for ci, tc in enumerate(tr.findall(W("tc"))):
          if ci in skip: continue
          for r in tc.iter(W("r")):
            if not text(r).strip(): continue
            rp = r.find(W("rPr"))
            if rp is None: rp = r.makeelement(W("rPr"), {}); r.insert(0, rp)
            for tag in ("sz", "szCs"):
                e = rp.find(W(tag))
                if e is None: e = rp.makeelement(W(tag), {}); rp.append(e)
                e.set(W("val"), "24")
            n += 1
    LOG.append("Section %d table: %d data-row runs set to regular 12 pt" % (s, n))

d.core_properties.title = "Intelligent Requirements Assessment Assistant - proposal, English working copy, corrected (not submission-ready)"
d.save(OUT)
with open(OUT + ".log.txt", "w") as f: f.write("\n".join(LOG) + "\n")
print("\n".join(LOG))
