#!/usr/bin/env python3
"""S10_FORM_QC.py - structural and content QC of the filled native form against the sanitized blank form.

Usage: python3 -I stages/S10/qc/S10_FORM_QC.py <blank_form.docx> <filled.docx> <master.md>

The blank form is not stored in this public repository (DEC-043; reference documents stay out); its
SHA-256 is printed so the comparison can be repeated against the same file. Exit 0 = pass.
A structural PASS does not mean that financial inputs, local completion or S10b approval exist.
"""
import hashlib, re, sys, zipfile
import docx
from docx.oxml.ns import qn
from lxml import etree

BASE, OUT, MASTER = sys.argv[1:4]
W = lambda t: qn("w:" + t)
res = []
def add(n, ok, d=""): res.append((n, "PASS" if ok else "FAIL", d))
def info(n, d): res.append((n, "INFO", d))
def pend(n, d): res.append((n, "PENDING", d))
def text(el): return "".join(t.text or "" for t in el.iter(W("t")))
def is_heading(el):
    ps = el.find(W("pPr")); st = ps.find(W("pStyle")) if ps is not None else None
    return el.tag == W("p") and st is not None and st.get(W("val")) == "Heading1"

info("Blank form SHA-256", hashlib.sha256(open(BASE, "rb").read()).hexdigest())
info("Filled form SHA-256", hashlib.sha256(open(OUT, "rb").read()).hexdigest())
B, O = docx.Document(BASE), docx.Document(OUT)
bb, ob = list(B.element.body.iterchildren()), list(O.element.body.iterchildren())

# ---- 1. package parts other than the body are unchanged ------------------------------------
zb, zo = zipfile.ZipFile(BASE), zipfile.ZipFile(OUT)
for part in ["word/header1.xml", "word/footer1.xml", "word/styles.xml", "word/numbering.xml", "word/settings.xml",
             "word/fontTable.xml", "word/theme/theme1.xml"]:
    a = etree.tostring(etree.fromstring(zb.read(part)), method="c14n")
    c = etree.tostring(etree.fromstring(zo.read(part)), method="c14n")
    add("Unchanged part: %s" % part, a == c)
hr = zb.read("word/_rels/header1.xml.rels")
add("Header relationships: blank form has none; the writer omits the empty part", b"<Relationship " not in hr and
    ("word/_rels/header1.xml.rels" not in zo.namelist() or b"<Relationship " not in zo.read("word/_rels/header1.xml.rels")))
sb, so = B.element.body.find(W("sectPr")), O.element.body.find(W("sectPr"))
add("Section properties (page, margins, header/footer references) unchanged",
    etree.tostring(sb, method="c14n") == etree.tostring(so, method="c14n"))
add("Footer signature table present and unchanged", b"Signature" in zo.read("word/footer1.xml"))

# ---- 2. headings ----------------------------------------------------------------------------------
hb = [text(e) for e in bb if is_heading(e)]; ho = [text(e) for e in ob if is_heading(e)]
add("20 section headings, same order", len(hb) == len(ho) == 20 and
    [h.split(".")[0] for h in hb] == [h.split(".")[0] for h in ho] == [str(i) for i in range(1, 21)])
exp = [h.replace("[PROJECT TITLE]", "Design, Development and Testing of a Laboratory Prototype of an Intelligent Requirements Assessment Assistant")
        .replace("[MONTHS] months and [PERSON-HOURS] person-hours", "6 months and 1,291 person-hours") for h in hb]
add("Heading texts unchanged except the Section 1 title and Section 4 duration fields", ho == exp)
hx = lambda e: etree.tostring(e.find(W("pPr")), method="c14n")
add("Heading paragraph formatting unchanged", [hx(e) for e in bb if is_heading(e)] == [hx(e) for e in ob if is_heading(e)])

# ---- 3. tables: count, grid, properties, merges, rows ---------------------------------------------------
tb = [e for e in bb if e.tag == W("tbl")]; to_all = [e for e in ob if e.tag == W("tbl")]
def sec_of(body_list, tbl):
    n = None
    for e in body_list:
        if is_heading(e): n = int(text(e).split(".")[0])
        if e is tbl: return n
# the one supplementary table authorized for Section 8 (DEC-044) is checked separately in section 3b
supp = [t for t in to_all if sec_of(ob, t) == 8]
to = [t for t in to_all if sec_of(ob, t) != 8]
add("Original tables: 10 in the blank form, 10 preserved outside Section 8", len(tb) == len(to) == 10, "%d vs %d" % (len(tb), len(to)))
add("Exactly one supplementary table, in Section 8 (DEC-044); total tables 11", len(supp) == 1 and len(to_all) == 11, "%d supplementary" % len(supp))
add("Blank form has no table in Section 8", not any(sec_of(bb, t) == 8 for t in tb))
if len(to) != len(tb):   # table-by-table comparison is impossible; stop with a clear failure
    for n, s_, d_ in res: print("%-7s %s%s" % (s_, n, ("  [" + d_ + "]") if d_ else ""))
    print("\nSUMMARY  form_checks=%d  failed=%d  (stopped: original table count differs)" % (len(res), sum(1 for r in res if r[1] == "FAIL")))
    print("RESULT FAIL"); sys.exit(1)
SECS = [sec_of(bb, t) for t in tb]
add("Tables sit in the same sections", SECS == [sec_of(ob, t) for t in to], str(SECS))
def sig(tr):
    cells = []
    for tc in tr.findall(W("tc")):
        p = tc.find(W("tcPr"))
        g = p.find(W("gridSpan")) if p is not None else None
        v = p.find(W("vMerge")) if p is not None else None
        w = p.find(W("tcW")) if p is not None else None
        cells.append((g.get(W("val")) if g is not None else "1", (v.get(W("val")) or "cont") if v is not None else "",
                      w.get(W("w")) if w is not None else ""))
    trp = tr.find(W("trPr"))
    return (tuple(cells), etree.tostring(trp, method="c14n") if trp is not None else b"")
added_total = 0
HEADER_ROWS = {16: 2, 5: 0}  # Section 5 has no header row; its option cells are marked
for t_b, t_o, s in zip(tb, to, SECS):
    add("S%d: table properties unchanged" % s, etree.tostring(t_b.find(W("tblPr")), method="c14n") == etree.tostring(t_o.find(W("tblPr")), method="c14n"))
    gb = [g.get(W("w")) for g in t_b.find(W("tblGrid"))]; go = [g.get(W("w")) for g in t_o.find(W("tblGrid"))]
    add("S%d: grid columns and widths unchanged (%d columns)" % (s, len(gb)), gb == go)
    rb, ro = t_b.findall(W("tr")), t_o.findall(W("tr"))
    h = HEADER_ROWS.get(s, 1 if s != 20 else 0)
    add("S%d: header row text and structure unchanged" % s,
        all(text(a) == text(b) and sig(a) == sig(b) for a, b in zip(rb[:h], ro[:h])))
    # original rows must appear in order; each extra row must copy the structure of the row before it
    i = j = 0; extras = []; ok = True
    while j < len(ro):
        if i < len(rb) and sig(rb[i]) == sig(ro[j]): i += 1; j += 1
        else:
            if j == 0 or sig(ro[j]) != sig(ro[j - 1]): ok = False
            extras.append(j); j += 1
    ok = ok and i == len(rb)
    add("S%d: every original row kept in order; %d added row(s) cloned from an adjacent data row" % (s, len(extras)), ok)
    added_total += len(extras)
    # cell count per row equals the grid when spans are counted
    add("S%d: every row spans the full grid" % s, all(sum(int(c[0]) for c in sig(r)[0]) == len(go) for r in ro))
add("Added table rows = 20 (S9 3, S11 1, S13 2, S14 1, S16 2, S17 11)", added_total == 20,
    "added %d" % added_total)

# ---- 3b. supplementary Section 8 specification table --------------------------------------------------------
M0 = open(MASTER, encoding="utf-8").read()
mspec = [[re.sub(r"\s+", " ", c.replace("[OPEN — S10]", "[OPEN]")).strip() for c in l.strip().strip("|").split("|")]
         for l in [b for b in M0.split("## 8.")[1].split("## 9.")[0].split("\n\n") if b.startswith("| No. | Specification |")][0].splitlines()
         if l.startswith("|") and not l.startswith("| ---")]
if supp:
    st = supp[0]
    srows = [[text(c).strip() for c in r.findall(W("tc"))] for r in st.findall(W("tr"))]
    add("S8 table: header No. / Specification / Metric and test condition / Target and 8 rows identical to the master", srows == mspec and len(srows) == 9)
    n13 = [t for t in tb if sec_of(bb, t) == 13][0]
    add("S8 table: table properties copied from the native Section 13 table", etree.tostring(st.find(W("tblPr")), method="c14n") == etree.tostring(n13.find(W("tblPr")), method="c14n"))
    gw = [int(g.get(W("w"))) for g in st.find(W("tblGrid"))]
    add("S8 table: four columns spanning the native table width", len(gw) == 4 and sum(gw) == sum(int(g.get(W("w"))) for g in n13.find(W("tblGrid")))
        and all(len(r.findall(W("tc"))) == 4 for r in st.findall(W("tr"))))
    add("S8: specification paragraphs replaced, not duplicated", not any(re.match(r"Specification [1-8]\. ", text(e)) for e in ob if e.tag == W("p")))

# ---- 4. content cross-checks ------------------------------------------------------------------------------
def rows_text(t, skip=1): return [[text(c).strip() for c in r.findall(W("tc"))] for r in t.findall(W("tr"))[skip:]]
T = dict(zip(SECS, to))
t13 = rows_text(T[13])
eff13 = [int(r[4].replace(",", "")) for r in t13[:-1]]
add("S13: seven activities with effort 150/168/210/138/226/267/132", eff13 == [150, 168, 210, 138, 226, 267, 132])
add("S13: TOTAL = 1,291 = sum", t13[-1][-1] == "1,291" and sum(eff13) == 1291)
titles13 = [r[1] for r in t13[:-1]]
t16 = rows_text(T[16], skip=2)
add("S16: titles identical to S13", [r[1] for r in t16[:-1]] == titles13)
add("S16: effort identical to S13 row by row; TOTAL 1,291", [int(r[2]) for r in t16[:-1]] == eff13 and t16[-1][1] == "1,291")
add("S16: months 7-12 blank in every activity row", all(all(c == "" for c in r[9:15]) for r in t16[:-1]))
add("S16: every activity scheduled within months 1-6", all("X" in r[3:9] for r in t16[:-1]))
M = open(MASTER, encoding="utf-8").read()
mg = [[c.strip() for c in l.strip().strip("|").split("|")][3:9] for l in M.split("## 16.")[1].split("## 17.")[0].splitlines() if re.match(r"\| [1-7] \|", l)]
add("S16: month marks identical to the master (approved S11 distribution)", [r[3:9] for r in t16[:-1]] == mg)
pend("S16: activity costs and cost weights", "await the approved personnel-rate allocation and non-personnel amounts (DEC-043 item 8)")
bodytext = [text(e) for e in ob if e.tag == W("p")]
s12 = bodytext[[k for k, t in enumerate(bodytext) if t.startswith("12. ")][0]:[k for k, t in enumerate(bodytext) if t.startswith("13. ")][0]]
t12 = [t[3:] for t in s12 if re.match(r"^[1-7]\. ", t)]
add("S12: numbered activity titles identical to S13, in order", t12 == titles13)
t14 = rows_text(T[14])
sh = [float(r[5]) for r in t14]
add("S14: four member rows with neutral placeholders", len(t14) == 4 and all("LOCAL COMPLETION ONLY" in r[1] and "LOCAL COMPLETION ONLY" in r[2] for r in t14))
add("S14: participation 40.7 + 19.8 + 19.8 + 19.7 = 100.0 (526 h and 3 x 255 h of 1,291 h)", abs(sum(sh) - 100) < 1e-9 and 526 + 3 * 255 == 1291
    and [round(100 * x / 1291, 1) for x in (526, 255)] == [40.7, 19.8])
add("S14: monthly hours are planned averages (526/6, 255/6)", t14[0][4].startswith("87.7") and all(r[4].startswith("42.5") for r in t14[1:])
    and round(526 / 6, 1) == 87.7 and 255 / 6 == 42.5)
t15 = rows_text(T[15])
add("S15: no amounts or currency entered", not re.search(r"\d[\d,.]*\s*(?:€|\$|EUR|USD|IRR|rial|toman)", " ".join(sum(t15, [])), re.I)
    and all(r[-1] in ("", "[open]") for r in t15))
add("S15: personnel quantity 1,291 person-hours", t15[0][3] == "1,291 person-hours")
t9 = rows_text(T[9])
add("S9: six comparator rows in the seven original columns", len(t9) == 6 and all(len(r) == 7 and r[1] for r in t9))
cf = [t for t in bodytext if t.startswith("Comparison and distinguishing features relative to entry")]
add("S9: six comparison fields, none left as a placeholder", len(cf) == 6 and not any("[TO BE COMPLETED]" in t for t in cf))
t10 = rows_text(T[10])
add("S10: prior-work table left blank (no invented team work)", all(all(c == "" for c in r[1:]) for r in t10))
t17 = rows_text(T[17])
add("S17: 16 risks numbered 1-16 in the form's category order", [r[0] for r in t17] == [str(i) for i in range(1, 17)]
    and [r[1] for r in t17] == ["Technical"] * 6 + ["Data / information"] * 4 + ["Schedule"] * 3 + ["Financial"] * 2 + ["Other"])
t11 = rows_text(T[11])
add("S11: current phase first, 6 months; later durations open", t11[0][0] == "Current phase" and t11[0][2] == "6" and all(r[2] == "[OPEN]" for r in t11[1:]))
t5 = " ".join(text(c) for c in T[5].iter(W("tc")))
add("S5: seven selections marked, nothing else", t5.count("[X]") == 7 and all(("[X] " + c) in t5 for c in
    ["Product / system", "Demand-driven", "Technology development", "Design", "Build", "Testing", "Independent project"]))

# ---- 5. formatting of inserted narrative ------------------------------------------------------------------
heads_idx = [k for k, e in enumerate(ob) if is_heading(e)]
bad_fmt = []
for e in ob:
    if e.tag != W("p") or is_heading(e) or not text(e).strip(): continue
    if e.find(".//" + W("numPr")) is not None: bad_fmt.append("numbering: " + text(e)[:40])
    for r in e.findall(W("r")):
        rp = r.find(W("rPr"))
        if rp is None: continue
        b = rp.find(W("b")); sz = rp.find(W("sz"))
        if b is not None and b.get(W("val")) not in ("0", "false"): bad_fmt.append("bold: " + text(e)[:40])
        if sz is not None and sz.get(W("val")) != "24": bad_fmt.append("size: " + text(e)[:40])
add("Narrative paragraphs: regular weight, 12 pt, no list numbering", not bad_fmt, "; ".join(bad_fmt[:5]))
alltext = "\n".join(text(e) for e in O.element.body.iter(W("p")))
# table typography (DEC-044): inserted data-cell text 12 pt and regular in Sections 8, 11, 13, 14, 15, 17
# (No. column and the form's own row labels excluded); Sections 9 and 16 keep the native 10 pt (reported conflict)
TT = {8: supp[0] if supp else None}
TT.update({s_: t_ for s_, t_ in zip(SECS, to)})
badc = []
for s_, skip, size in [(8, {0}, "24"), (11, {0}, "24"), (13, {0}, "24"), (14, {0}, "24"), (15, {0, 1}, "24"), (17, {0, 1}, "24"), (9, {0}, "20"), (16, {0}, "20")]:
    t_ = TT.get(s_)
    hdr = 2 if s_ == 16 else 1
    for tr in t_.findall(W("tr"))[hdr:]:
        for ci, tc in enumerate(tr.findall(W("tc"))):
            if ci in skip: continue
            for r in tc.iter(W("r")):
                if not text(r).strip(): continue
                rp = r.find(W("rPr")); sz = rp.find(W("sz")) if rp is not None else None; b = rp.find(W("b")) if rp is not None else None
                if sz is None or sz.get(W("val")) != size: badc.append("S%d size %s" % (s_, sz.get(W("val")) if sz is not None else None))
                if b is not None and b.get(W("val")) not in ("0", "false"): badc.append("S%d bold" % s_)
add("Table data cells: 12 pt regular in Sections 8, 11, 13, 14, 15, 17; native 10 pt in Sections 9 and 16", not badc, str(sorted(set(badc)))[:200])
kn = all(p.find(W("pPr")) is not None and p.find(W("pPr")).find(W("keepNext")) is not None
         for s_ in (8, 9, 11, 13, 14, 15, 17) for p in TT[s_].findall(W("tr"))[0].iter(W("p")))
add("Header rows kept with the first data row (keep-with-next)", kn)
add("No bullet or decorative glyphs", not re.search(r"[•▪◦✓✔☐☑►■]", alltext))

# ---- 6. guidance removed where content is inserted; local fields kept ---------------------------------------
gb = {}
cur = None
for e in bb:
    if is_heading(e): cur = int(text(e).split(".")[0]); continue
    if e.tag == W("p") and text(e).strip(): gb.setdefault(cur, []).append(text(e))
KEEP = {2: 1, 10: 5, 14: 1, 15: 4, 16: 3, 20: 4}
left = [(s, t[:50]) for s, ts in gb.items() for t in ts if t in alltext.split("\n") and not t.startswith("Comparison and distinguishing")]
expected_left = sum(KEEP.values())
add("Template guidance removed in implemented sections, including the general note (kept only in 2, 10, 14 local note, 15, 16 cost notes, 20)",
    sorted(set(s for s, _ in left)) == sorted(KEEP) and len(left) == expected_left, str(left)[:300])
for ph in ["[TEAM NAME]", "[TO BE COMPLETED LOCALLY]", "[YYYY-MM-DD]"]:
    add("Local placeholder kept: %s" % ph, ph in alltext)
for gone in ["[PROJECT RATIONALE AND SIGNIFICANCE]", "[CURRENT-PHASE OBJECTIVES]", "[FEATURES AND MEASURABLE SPECIFICATIONS]",
             "[DETAILED METHODOLOGY BY WORK PACKAGE]", "[ADDITIONAL VERIFIED INFORMATION, IF ANY]", "[PROJECT TITLE]", "[MONTHS]"]:
    add("Content placeholder replaced: %s" % gone, gone not in alltext)

# ---- 7. claims and sensitive content ---------------------------------------------------------------------------
low = alltext.lower(); low_nr = low.split("references cited in this proposal")[0]
for ph in ["checks whether relevant existing solution examples can be identified for a submitted need",
           "approval of a query does not authorize disclosure", "no transition into approved exists except the approval event",
           "being better than bm25 is not required"]:
    add("Required wording present: '%s'" % ph[:55], ph in low)
add("Approval-status wording: test sizes, margin and corpus sizes stated as fixed; response time, floors, agreement open",
    "are fixed for this project" in low and "remain to be confirmed before the evaluation protocol is frozen" in low
    and "await owner confirmation" not in low and "the planning sizes" not in low and "margin is 0.05, a planning value" not in low)
for w in ["certified", "proven", "patentable", "guarantee", "outperforms", "state-of-the-art", "will reduce"]:
    hits = re.findall(r"(.{4})\b%s\b" % w, low_nr)
    add("Prohibited claim wording absent: '%s'" % w, all(h == "not " for h in hits), str(hits))
add("No working identifiers (DEC-, ISS-, S10 markers) in the form", not re.search(r"\b(?:DEC|ISS|SRC|CLM|DEF)-\d+|OPEN — S10", alltext))
add("No Persian text, e-mail address or phone number", not re.search(r"[؀-ۿ]|@[a-z0-9-]+\.[a-z]{2,}|\+\d{2}[ \d]{8,}", alltext, re.I))
core = zo.read("docProps/core.xml").decode()
add("Document metadata carries no author name", not re.search(r"<dc:creator>[^<]+</dc:creator>|<cp:lastModifiedBy>[^<]+</cp:lastModifiedBy>", core))

for n, s, d in res: print("%-7s %s%s" % (s, n, ("  [" + d + "]") if d else ""))
nf = sum(1 for r in res if r[1] == "FAIL")
print("\nSUMMARY  form_checks=%d  failed=%d  pending=%d" % (sum(1 for r in res if r[1] in ("PASS", "FAIL")), nf, sum(1 for r in res if r[1] == "PENDING")))
print("RESULT", "PASS" if nf == 0 else "FAIL")
sys.exit(1 if nf else 0)
