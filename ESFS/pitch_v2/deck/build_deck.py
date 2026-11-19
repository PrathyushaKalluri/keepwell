"""Render the Keepwell seed deck (v2) from deck_content.py → Keepwell_Seed_Deck.pptx + .html (PDF via LibreOffice).
    <venv>/bin/python build_deck.py
"""
import sys, os, html, pathlib
HERE = pathlib.Path(__file__).parent; sys.path.insert(0, str(HERE))
from deck_content import MAIN, APPENDIX, NAMES
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.chart.data import CategoryChartData
from pptx.enum.chart import XL_CHART_TYPE, XL_LEGEND_POSITION, XL_LABEL_POSITION

NAVY = RGBColor(0x0E, 0x23, 0x40); TEAL = RGBColor(0x0F, 0x8C, 0x7A); AMBER = RGBColor(0xE0, 0x8A, 0x1E); INK = RGBColor(0x1E, 0x23, 0x2B)
GREY = RGBColor(0x5B, 0x66, 0x7C); LIGHT = RGBColor(0xF4, 0xF1, 0xEA); WHITE = RGBColor(0xFF, 0xFF, 0xFF); RED = RGBColor(0xC2, 0x41, 0x2D); TEALBG = RGBColor(0xE3, 0xF3, 0xEF)
PALE = RGBColor(0xB8, 0xC7, 0xD9); FONT = "Arial"; W = 13.333
prs = Presentation(); prs.slide_width = Inches(W); prs.slide_height = Inches(7.5); BLANK = prs.slide_layouts[6]

def box(sl, x, y, w, h, fill=None, line=None, shape=MSO_SHAPE.RECTANGLE):
    s = sl.shapes.add_shape(shape, Inches(x), Inches(y), Inches(w), Inches(h))
    if fill is None: s.fill.background()
    else: s.fill.solid(); s.fill.fore_color.rgb = fill
    if line is None: s.line.fill.background()
    else: s.line.color.rgb = line; s.line.width = Pt(1)
    s.shadow.inherit = False; return s
def text(sl, x, y, w, h, t, size=14, bold=False, color=INK, align=PP_ALIGN.LEFT, anchor=MSO_ANCHOR.TOP, italic=False, shape=None):
    tb = shape if shape is not None else sl.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    tf = tb.text_frame; tf.word_wrap = True; tf.vertical_anchor = anchor
    tf.margin_left = tf.margin_right = Inches(0.06); tf.margin_top = tf.margin_bottom = Inches(0.03)
    for i, ln in enumerate(t if isinstance(t, list) else [t]):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph(); p.alignment = align
        r = p.add_run(); r.text = ln; f = r.font; f.name = FONT; f.size = Pt(size); f.bold = bold; f.italic = italic; f.color.rgb = color
    return tb
def bullets(sl, x, y, w, h, items, size=13, color=INK, gap=6, mark="•  "):
    tb = sl.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h)); tf = tb.text_frame; tf.word_wrap = True
    for i, it in enumerate(items):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph(); p.space_after = Pt(gap)
        r = p.add_run(); r.text = mark + it; r.font.name = FONT; r.font.size = Pt(size); r.font.color.rgb = color
    return tb
def frame(sl, d, n):
    box(sl, 0, 0, W, 0.08, fill=TEAL)
    text(sl, 0.6, 0.32, 12, 0.35, d["kicker"].upper(), size=11, bold=True, color=TEAL)
    text(sl, 0.6, 0.62, 12.1, 1.0, d["headline"], size=27 if len(d["headline"]) < 62 else 23, bold=True, color=NAVY)
    text(sl, 11.6, 7.08, 1.2, 0.3, str(n), size=9, color=GREY, align=PP_ALIGN.RIGHT)
    text(sl, 0.6, 7.08, 8, 0.3, "Keepwell · Seed 2026 · illustrative case, IIIT Hyderabad ESFS", size=9, color=GREY)
    if d.get("notes"): sl.notes_slide.notes_text_frame.text = d["notes"]
def foot(sl, t): text(sl, 0.6, 6.7, 12.1, 0.35, t, size=9, color=GREY, italic=True)
def tile(sl, x, y, w, h, v, l, fill=LIGHT, vc=NAVY, vs=26, lc=GREY):
    box(sl, x, y, w, h, fill=fill); text(sl, x + 0.15, y + 0.1, w - 0.3, h * 0.5, v, size=vs, bold=True, color=vc)
    text(sl, x + 0.15, y + h * 0.5, w - 0.3, h * 0.5, l, size=11, color=lc)
def landbar(sl, t, y=6.0):
    box(sl, 0.6, y, 12.1, 0.58, fill=TEAL); text(sl, 0.8, y, 11.7, 0.58, t, size=15, bold=True, color=WHITE, anchor=MSO_ANCHOR.MIDDLE)

def r_title(sl, d, n):
    box(sl, 0, 0, W, 7.5, fill=NAVY); box(sl, 0.6, 2.05, 0.12, 2.3, fill=TEAL)
    text(sl, 0.95, 1.35, 10, 0.4, d["kicker"].upper(), size=14, bold=True, color=AMBER)
    text(sl, 0.95, 1.9, 11, 1.2, d["headline"], size=64, bold=True, color=WHITE)
    text(sl, 0.95, 3.15, 11.5, 0.6, d["tagline"], size=26, color=WHITE)
    text(sl, 0.95, 3.9, 11.5, 0.5, d["sub"], size=16, color=PALE)
    text(sl, 0.95, 6.35, 11.8, 0.4, NAMES, size=12, color=PALE)
    text(sl, 0.95, 6.75, 11.8, 0.4, "Illustrative case for the IIIT Hyderabad ESFS course · founder histories, pilot and financials are [Story]", size=10, color=PALE, italic=True)
    sl.notes_slide.notes_text_frame.text = d["notes"]
def r_problem(sl, d, n):
    frame(sl, d, n); bullets(sl, 0.6, 1.75, 7.3, 2.9, d["story"], size=15, gap=9)
    box(sl, 8.2, 1.85, 4.5, 2.5, fill=NAVY); text(sl, 8.45, 2.05, 4.0, 1.4, d["quote"], size=22, bold=True, italic=True, color=WHITE)
    text(sl, 8.45, 3.55, 4.0, 0.7, "— " + d["quote_by"], size=11, color=AMBER)
    for i, (v, l) in enumerate(d["stats"]): tile(sl, 0.6 + i * 3.05, 4.85, 2.9, 1.65, v, l, vs=28)
    foot(sl, d["foot"])
def r_tiles(sl, d, n):
    frame(sl, d, n)
    for i, (h, b) in enumerate(d["tiles"]):
        x = 0.6 + (i % 2) * 6.15; y = 1.8 + (i // 2) * 2.0
        box(sl, x, y, 5.95, 1.8, fill=LIGHT); box(sl, x, y, 0.1, 1.8, fill=AMBER)
        text(sl, x + 0.3, y + 0.15, 5.5, 0.4, h, size=18, bold=True, color=NAVY); text(sl, x + 0.3, y + 0.62, 5.5, 1.1, b, size=13)
    landbar(sl, d["land"])
def r_solution(sl, d, n):
    frame(sl, d, n)
    for i, (h, b) in enumerate(d["offers"]):
        x = 0.6 + i * 3.05; box(sl, x, 1.8, 2.9, 2.0, fill=NAVY if i == 2 else LIGHT)
        c = WHITE if i == 2 else NAVY; text(sl, x + 0.15, 1.95, 2.6, 0.7, h, size=17, bold=True, color=c)
        text(sl, x + 0.15, 2.7, 2.6, 1.0, b, size=12, color=PALE if i == 2 else INK)
    text(sl, 0.6, 4.05, 12, 0.35, "THE JOURNEY: FOUR PHASES, ONE RECORD", size=11, bold=True, color=TEAL)
    for i, (h, b) in enumerate(d["phases"]):
        s = box(sl, 0.6 + i * 3.05, 4.45, 3.0, 0.95, fill=TEAL if i == 0 else NAVY, shape=MSO_SHAPE.CHEVRON)
        text(sl, 0, 0, 0, 0, [h, b], size=11, bold=True, color=WHITE, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE, shape=s)
    landbar(sl, d["land"], 5.75)
def r_flow(sl, d, n):
    frame(sl, d, n)
    for i, (h, b) in enumerate(d["steps"]):
        x = 0.6 + i * 2.03; box(sl, x, 1.9, 1.9, 3.2, fill=TEALBG if i == 5 else LIGHT, line=TEAL if i == 5 else None)
        box(sl, x + 0.12, 2.05, 0.5, 0.5, fill=NAVY, shape=MSO_SHAPE.OVAL); text(sl, x + 0.12, 2.05, 0.5, 0.5, str(i + 1), size=14, bold=True, color=WHITE, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
        text(sl, x + 0.12, 2.7, 1.7, 0.45, h, size=16, bold=True, color=NAVY); text(sl, x + 0.12, 3.2, 1.7, 1.8, b, size=12)
    landbar(sl, d["principle"], 5.5)
def r_traction(sl, d, n):
    frame(sl, d, n)
    for i, (v, l) in enumerate(d["stats"]): tile(sl, 0.6 + i * 2.45, 1.75, 2.3, 1.55, v, l, fill=NAVY if i == 4 else LIGHT, vc=WHITE if i == 4 else NAVY, lc=PALE if i == 4 else GREY, vs=28)
    text(sl, 0.6, 3.55, 6, 0.35, "WHAT WORKED", size=12, bold=True, color=TEAL); bullets(sl, 0.6, 3.95, 5.9, 2.5, d["hits"], size=13, mark="✓  ")
    text(sl, 6.8, 3.55, 6, 0.35, "WHAT WE MISSED, AND FIXED", size=12, bold=True, color=RED); bullets(sl, 6.8, 3.95, 5.9, 2.5, d["misses"], size=13, mark="✗  ")
    foot(sl, d["foot"])
def r_unit(sl, d, n):
    frame(sl, d, n)
    for i, (h, rows) in enumerate(d["cols"]):
        x = 0.6 + i * 4.1; box(sl, x, 1.7, 3.9, 0.5, fill=NAVY); text(sl, x + 0.15, 1.7, 3.6, 0.5, h, size=15, bold=True, color=WHITE, anchor=MSO_ANCHOR.MIDDLE)
        for j, (k, v) in enumerate(rows):
            y = 2.25 + j * 0.47; last = j == len(rows) - 1 or (i == 2 and j == 3)
            box(sl, x, y, 3.9, 0.44, fill=TEALBG if last else LIGHT)
            text(sl, x + 0.12, y, 2.3, 0.44, k, size=12, bold=last, anchor=MSO_ANCHOR.MIDDLE)
            text(sl, x + 2.2, y, 1.6, 0.44, v, size=13, bold=True, color=TEAL if last else NAVY, align=PP_ALIGN.RIGHT, anchor=MSO_ANCHOR.MIDDLE)
    text(sl, 0.6, 5.2, 12.1, 0.6, d["lines"], size=11, color=GREY); landbar(sl, d["land"], 5.95)
def r_market(sl, d, n):
    frame(sl, d, n)
    for i, (k, v, l, f) in enumerate(d["bars"]):
        y = 1.85 + i * 1.08; wbar = max(0.35, 8.0 * f ** 0.5)
        text(sl, 0.6, y, 1.6, 0.85, k, size=15, bold=True, color=NAVY, anchor=MSO_ANCHOR.MIDDLE)
        box(sl, 2.2, y + 0.08, wbar, 0.7, fill=[NAVY, RGBColor(0x26, 0x37, 0x5A), TEAL, AMBER][i])
        text(sl, 2.3 + wbar, y, 3.2, 0.85, v, size=20, bold=True, color=NAVY, anchor=MSO_ANCHOR.MIDDLE)
        text(sl, 2.3 + wbar + 2.2 if wbar < 5 else 2.35, y + (0 if wbar < 5 else 0.85), 5.5, 0.85, l, size=12, color=GREY if wbar < 5 else GREY, anchor=MSO_ANCHOR.MIDDLE)
    foot(sl, d["foot"])
def r_compete(sl, d, n):
    frame(sl, d, n)
    hdr = ["Player", "What they do", "Why not the independent shop"]; ws = [2.6, 3.0, 3.6]; x0 = 0.6
    for j, h in enumerate(hdr): box(sl, x0 + sum(ws[:j]), 1.7, ws[j] - 0.04, 0.42, fill=NAVY); text(sl, x0 + sum(ws[:j]) + 0.08, 1.7, ws[j] - 0.2, 0.42, h, size=11, bold=True, color=WHITE, anchor=MSO_ANCHOR.MIDDLE)
    for i, row in enumerate(d["rows"]):
        y = 2.16 + i * 0.6
        for j, c in enumerate(row):
            box(sl, x0 + sum(ws[:j]), y, ws[j] - 0.04, 0.56, fill=LIGHT); text(sl, x0 + sum(ws[:j]) + 0.08, y, ws[j] - 0.2, 0.56, c, size=11, bold=j == 0, anchor=MSO_ANCHOR.MIDDLE)
    text(sl, 10.05, 1.7, 2.7, 0.42, "OUR FOUR MOATS", size=11, bold=True, color=TEAL)
    for i, (h, b) in enumerate(d["moats"]):
        y = 2.16 + i * 1.08; box(sl, 10.05, y, 2.65, 1.0, fill=TEALBG, line=TEAL)
        text(sl, 10.15, y + 0.05, 2.45, 0.45, h, size=12, bold=True, color=NAVY); text(sl, 10.15, y + 0.48, 2.45, 0.5, b, size=10)
def r_team(sl, d, n):
    frame(sl, d, n)
    for i, (nm, role, bg, owns) in enumerate(d["people"]):
        x = 0.6 + i * 4.1; box(sl, x, 1.7, 3.9, 3.25, fill=LIGHT)
        box(sl, x + 0.2, 1.9, 0.9, 0.9, fill=NAVY, shape=MSO_SHAPE.OVAL); text(sl, x + 0.2, 1.9, 0.9, 0.9, "".join(w[0] for w in nm.split()[:2]), size=20, bold=True, color=WHITE, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
        text(sl, x + 1.25, 1.9, 2.6, 0.45, nm, size=16, bold=True, color=NAVY); text(sl, x + 1.25, 2.33, 2.6, 0.4, role, size=13, bold=True, color=TEAL)
        text(sl, x + 0.2, 2.95, 3.5, 1.4, bg, size=11); text(sl, x + 0.2, 4.4, 3.5, 0.5, "Owns: " + owns, size=11, bold=True, color=GREY)
    text(sl, 0.6, 5.1, 12.1, 0.6, d["advisors"], size=12); landbar(sl, d["gap"], 5.8); foot(sl, d["foot"])
def r_plan(sl, d, n):
    frame(sl, d, n)
    cd = CategoryChartData(); cd.categories = d["years"]; cd.add_series("Revenue (₹ Cr)", d["rev"]); cd.add_series("EBITDA (₹ Cr)", d["ebitda"])
    gf = sl.shapes.add_chart(XL_CHART_TYPE.COLUMN_CLUSTERED, Inches(0.6), Inches(1.6), Inches(12.1), Inches(3.1), cd); ch = gf.chart
    ch.has_legend = True; ch.legend.position = XL_LEGEND_POSITION.TOP; ch.legend.include_in_layout = False; ch.legend.font.size = Pt(11)
    for s_, c in zip(ch.series, (NAVY, TEAL)):
        s_.format.fill.solid(); s_.format.fill.fore_color.rgb = c
        s_.data_labels.show_value = True; s_.data_labels.font.size = Pt(10); s_.data_labels.number_format = '0.0;-0.0'; s_.data_labels.number_format_is_linked = False; s_.data_labels.position = XL_LABEL_POSITION.OUTSIDE_END
    ch.value_axis.has_major_gridlines = False; ch.value_axis.tick_labels.font.size = Pt(10); ch.category_axis.tick_labels.font.size = Pt(11)
    for i, (h, a, b) in enumerate(d["rounds"]):
        x = 0.6 + i * 3.05; box(sl, x, 4.85, 2.95, 1.75, fill=NAVY if i == 0 else LIGHT)
        c = WHITE if i == 0 else NAVY; text(sl, x + 0.15, 4.95, 2.7, 0.35, h, size=12, bold=True, color=AMBER if i == 0 else TEAL)
        text(sl, x + 0.15, 5.3, 2.7, 0.5, a, size=22, bold=True, color=c); text(sl, x + 0.15, 5.85, 2.7, 0.7, b, size=11, color=PALE if i == 0 else INK)
    foot(sl, d["foot"])
def r_ask(sl, d, n):
    box(sl, 0, 0, W, 7.5, fill=NAVY); text(sl, 0.6, 0.32, 12, 0.35, d["kicker"].upper(), size=11, bold=True, color=AMBER)
    text(sl, 0.6, 0.62, 12, 0.9, d["headline"], size=30, bold=True, color=WHITE)
    for i, (v, l) in enumerate(d["terms"]): tile(sl, 0.6 + i * 2.1, 1.75, 1.95, 1.45, v, l, fill=RGBColor(0x1B, 0x3A, 0x66), vc=WHITE, lc=PALE, vs=20)
    text(sl, 0.6, 3.45, 6, 0.35, "USE OF FUNDS (COURSE M1 NEED COLUMNS)", size=11, bold=True, color=AMBER)
    for i, (l, p) in enumerate(d["uof"]):
        y = 3.85 + i * 0.5; text(sl, 0.6, y, 3.4, 0.42, l, size=12, color=WHITE, anchor=MSO_ANCHOR.MIDDLE)
        box(sl, 4.0, y + 0.08, 2.0 * p / 30, 0.28, fill=TEAL); text(sl, 4.05 + 2.0 * p / 30, y, 0.8, 0.42, f"{p}%", size=12, bold=True, color=WHITE, anchor=MSO_ANCHOR.MIDDLE)
    box(sl, 7.0, 1.75, 5.7, 4.15, fill=RGBColor(0x1B, 0x3A, 0x66)); text(sl, 7.2, 1.85, 5.3, 0.4, "MILESTONES BY MONTH 18 (JUN 2028) → ROUND 2", size=11, bold=True, color=AMBER)
    bullets(sl, 7.2, 2.3, 5.3, 3.5, d["milestones"], size=14, color=WHITE, gap=9, mark="◆  ")
    text(sl, 0.6, 6.45, 12.1, 0.5, d["help"], size=12, color=PALE); text(sl, 11.6, 7.08, 1.2, 0.3, str(n), size=9, color=PALE, align=PP_ALIGN.RIGHT)
    sl.notes_slide.notes_text_frame.text = d["notes"]
def r_table(sl, d, n):
    frame(sl, d, n); t = d["table"]; cols = len(t[0]); cw = 12.1 / cols
    for i, row in enumerate(t):
        for j, c in enumerate(row):
            y = 1.75 + i * 0.66; box(sl, 0.6 + j * cw, y, cw - 0.04, 0.62, fill=NAVY if i == 0 else LIGHT)
            text(sl, 0.68 + j * cw, y, cw - 0.2, 0.62, c, size=12 if i else 12, bold=(i == 0 or j == 0), color=WHITE if i == 0 else INK, anchor=MSO_ANCHOR.MIDDLE)
R = {k[2:]: v for k, v in globals().items() if k.startswith("r_")}
for i, d in enumerate(MAIN + APPENDIX, 1):
    sl = prs.slides.add_slide(BLANK); R[d["type"]](sl, d, i)
out = HERE / "Keepwell_Seed_Deck.pptx"; prs.save(out); print("saved", out)

# ---------------- HTML version (same content; arrow keys to navigate)
E = html.escape
def hs(d, n):
    k = f'<div class="k">{E(d["kicker"])}</div>'; h = f'<h1>{E(d["headline"])}</h1>'; t = d["type"]; b = ""
    if t == "title":
        return f'<section class="s dark"><div class="k">{E(d["kicker"])}</div><h1 class="big">{E(d["headline"])}</h1><p class="tag">{E(d["tagline"])}</p><p class="sub">{E(d["sub"])}</p><p class="names">{E(NAMES)}</p></section>'
    if t == "problem":
        b = '<div class="two"><ul>' + "".join(f"<li>{E(x)}</li>" for x in d["story"]) + f'</ul><blockquote>{E(d["quote"])}<cite>— {E(d["quote_by"])}</cite></blockquote></div><div class="tiles">' + "".join(f'<div class="tile"><b>{E(v)}</b><span>{E(l)}</span></div>' for v, l in d["stats"]) + f'</div><p class="foot">{E(d["foot"])}</p>'
    elif t == "tiles":
        b = '<div class="grid2">' + "".join(f'<div class="card"><b>{E(a)}</b><span>{E(c)}</span></div>' for a, c in d["tiles"]) + f'</div><div class="land">{E(d["land"])}</div>'
    elif t == "solution":
        b = '<div class="tiles">' + "".join(f'<div class="tile{" hi" if i == 2 else ""}"><b class="sm">{E(a)}</b><span>{E(c)}</span></div>' for i, (a, c) in enumerate(d["offers"])) + '</div><div class="chev">' + "".join(f'<div><b>{E(a)}</b><span>{E(c)}</span></div>' for a, c in d["phases"]) + f'</div><div class="land">{E(d["land"])}</div>'
    elif t == "flow":
        b = '<div class="flow">' + "".join(f'<div><i>{i+1}</i><b>{E(a)}</b><span>{E(c)}</span></div>' for i, (a, c) in enumerate(d["steps"])) + f'</div><div class="land">{E(d["principle"])}</div>'
    elif t == "traction":
        b = '<div class="tiles t5">' + "".join(f'<div class="tile"><b>{E(v)}</b><span>{E(l)}</span></div>' for v, l in d["stats"]) + '</div><div class="two"><div><h3 class="ok">What worked</h3><ul>' + "".join(f"<li>{E(x)}</li>" for x in d["hits"]) + '</ul></div><div><h3 class="bad">What we missed, and fixed</h3><ul>' + "".join(f"<li>{E(x)}</li>" for x in d["misses"]) + f'</ul></div></div><p class="foot">{E(d["foot"])}</p>'
    elif t == "unit":
        b = '<div class="cols3">' + "".join(f'<table><tr><th colspan=2>{E(h0)}</th></tr>' + "".join(f"<tr><td>{E(a)}</td><td>{E(c)}</td></tr>" for a, c in rows) + "</table>" for h0, rows in d["cols"]) + f'</div><p class="sub2">{E(d["lines"])}</p><div class="land">{E(d["land"])}</div>'
    elif t == "market":
        b = '<div class="mk">' + "".join(f'<div class="mrow"><b>{E(a)}</b><i style="width:{max(4, 70*f**0.5):.0f}%"></i><strong>{E(v)}</strong><span>{E(l)}</span></div>' for a, v, l, f in d["bars"]) + f'</div><p class="foot">{E(d["foot"])}</p>'
    elif t == "compete":
        b = '<div class="cmp"><table><tr><th>Player</th><th>What they do</th><th>Why not the independent shop</th></tr>' + "".join("<tr>" + "".join(f"<td>{E(c)}</td>" for c in r) + "</tr>" for r in d["rows"]) + '</table><div class="moats"><h3>Our four moats</h3>' + "".join(f'<div><b>{E(a)}</b><span>{E(c)}</span></div>' for a, c in d["moats"]) + "</div></div>"
    elif t == "team":
        b = '<div class="cols3">' + "".join(f'<div class="card"><b>{E(a)}</b><em>{E(r)}</em><span>{E(c)}</span><small>Owns: {E(o)}</small></div>' for a, r, c, o in d["people"]) + f'</div><p class="sub2">{E(d["advisors"])}</p><div class="land">{E(d["gap"])}</div><p class="foot">{E(d["foot"])}</p>'
    elif t == "plan":
        mx = max(d["rev"]); bars = "".join(f'<div class="bc"><div class="bv">{r:.1f}</div><div class="bar" style="height:{r/mx*100:.0f}%"></div><div class="be {"neg" if e < 0 else ""}">{e:+.1f}</div><div class="by">{y}</div></div>' for y, r, e in zip(d["years"], d["rev"], d["ebitda"]))
        b = f'<div class="chart">{bars}</div><p class="sub2">Bars: revenue (₹ Cr). Below each bar: EBITDA (₹ Cr).</p><div class="tiles">' + "".join(f'<div class="tile{" hi" if i == 0 else ""}"><em>{E(a)}</em><b>{E(v)}</b><span>{E(c)}</span></div>' for i, (a, v, c) in enumerate(d["rounds"])) + f'</div><p class="foot">{E(d["foot"])}</p>'
    elif t == "ask":
        b = '<div class="two"><div><div class="tiles t3">' + "".join(f'<div class="tile hi"><b>{E(v)}</b><span>{E(l)}</span></div>' for v, l in d["terms"]) + '</div><h3>Use of funds</h3>' + "".join(f'<div class="uof"><span>{E(l)}</span><i style="width:{p*2}%"></i><b>{p}%</b></div>' for l, p in d["uof"]) + '</div><div class="ms"><h3>Milestones by month 18 → Round 2</h3><ul>' + "".join(f"<li>{E(x)}</li>" for x in d["milestones"]) + f'</ul></div></div><p class="sub2">{E(d["help"])}</p>'
        return f'<section class="s dark">{k}{h}{b}</section>'
    elif t == "table":
        tt = d["table"]; b = "<table class='wide'>" + "".join("<tr>" + "".join((f"<th>{E(c)}</th>" if i == 0 else f"<td>{E(c)}</td>") for c in r) + "</tr>" for i, r in enumerate(tt)) + "</table>"
    return f'<section class="s">{k}{h}{b}<div class="pn">{n}</div></section>'
CSS = """
:root{--navy:#0E2340;--teal:#0F8C7A;--amber:#E08A1E;--ink:#1E232B;--grey:#5B667C;--light:#F4F1EA;--tealbg:#E3F3EF;--red:#C2412D}
*{box-sizing:border-box}html,body{margin:0;background:#0A1322;font-family:Inter,Arial,sans-serif;color:var(--ink)}
#deck{position:fixed;inset:0;display:grid;place-items:center}
.s{display:none;width:1280px;height:720px;background:#FAF7F1;padding:44px 56px;position:relative;overflow:hidden;border-top:6px solid var(--teal)}
.s.on{display:block}.s.dark{background:var(--navy);color:#fff;border-top-color:var(--amber)}
.k{font:700 13px Arial;letter-spacing:.14em;text-transform:uppercase;color:var(--teal)}.dark .k{color:var(--amber)}
h1{font:700 32px/1.15 Georgia,serif;color:var(--navy);margin:8px 0 20px}.dark h1{color:#fff}h1.big{font-size:84px;margin-top:120px}
.tag{font-size:28px;margin:0}.sub{font-size:18px;color:#B8C7D9}.names{position:absolute;bottom:40px;color:#B8C7D9;font-size:15px}
ul{margin:0;padding-left:20px;font-size:17px;line-height:1.5}h3{font:700 14px Arial;letter-spacing:.1em;text-transform:uppercase;color:var(--teal)}h3.ok{color:var(--teal)}h3.bad{color:var(--red)}.dark h3{color:var(--amber)}
.two{display:grid;grid-template-columns:1.5fr 1fr;gap:28px}.two blockquote{margin:0;background:var(--navy);color:#fff;font:italic 700 24px Georgia;padding:24px;border-radius:12px}cite{display:block;margin-top:14px;font:600 13px Arial;color:var(--amber)}
.tiles{display:grid;grid-template-columns:repeat(4,1fr);gap:14px;margin-top:20px}.tiles.t5{grid-template-columns:repeat(5,1fr)}.tiles.t3{grid-template-columns:repeat(3,1fr);margin-top:0}
.tile{background:var(--light);border-radius:12px;padding:14px 16px}.tile b{display:block;font:700 30px Georgia;color:var(--navy)}.tile b.sm{font-size:20px}.tile span{font-size:13px;color:var(--grey)}.tile em{font-style:normal;font:700 12px Arial;color:var(--teal);text-transform:uppercase}
.tile.hi{background:var(--navy)}.tile.hi b{color:#fff}.tile.hi span{color:#B8C7D9}.tile.hi em{color:var(--amber)}.dark .tile.hi{background:#1B3A66}
.grid2{display:grid;grid-template-columns:1fr 1fr;gap:16px}.card{background:var(--light);border-left:6px solid var(--amber);border-radius:10px;padding:16px 20px}.card b{display:block;font:700 20px Arial;color:var(--navy)}.card span{font-size:15px}.card em{display:block;color:var(--teal);font-style:normal;font-weight:700}.card small{display:block;margin-top:8px;color:var(--grey);font-weight:700}
.land{position:absolute;left:56px;right:56px;bottom:56px;background:var(--teal);color:#fff;font:700 18px Arial;padding:14px 20px;border-radius:10px}
.chev{display:grid;grid-template-columns:repeat(4,1fr);gap:6px;margin-top:22px}.chev div{background:var(--navy);color:#fff;padding:12px;clip-path:polygon(0 0,92% 0,100% 50%,92% 100%,0 100%,8% 50%);text-align:center}.chev div:first-child{background:var(--teal)}.chev b{display:block}.chev span{font-size:12px}
.flow{display:grid;grid-template-columns:repeat(6,1fr);gap:10px}.flow div{background:var(--light);border-radius:12px;padding:14px;min-height:260px}.flow div:last-child{background:var(--tealbg);border:2px solid var(--teal)}.flow i{display:grid;place-items:center;width:36px;height:36px;border-radius:50%;background:var(--navy);color:#fff;font-style:normal;font-weight:700}.flow b{display:block;font-size:18px;color:var(--navy);margin:10px 0 6px}.flow span{font-size:14px}
.cols3{display:grid;grid-template-columns:repeat(3,1fr);gap:16px}table{border-collapse:collapse;width:100%;font-size:14px}th{background:var(--navy);color:#fff;text-align:left;padding:8px 10px}td{background:var(--light);padding:7px 10px;border-bottom:3px solid #FAF7F1}td:last-child{font-weight:700;color:var(--navy)}
table.wide td{font-size:15px}.sub2{font-size:13px;color:var(--grey);margin-top:14px}.dark .sub2{color:#B8C7D9}
.mk .mrow{display:grid;grid-template-columns:120px 1fr;align-items:center;margin:10px 0}.mrow b{font-size:18px;color:var(--navy)}.mrow i{display:block;height:44px;background:var(--navy);border-radius:6px}.mrow:nth-child(3) i{background:var(--teal)}.mrow:nth-child(4) i{background:var(--amber)}.mrow strong{grid-column:2;font:700 22px Georgia;color:var(--navy)}.mrow span{grid-column:2;font-size:13px;color:var(--grey)}
.cmp{display:grid;grid-template-columns:3fr 1fr;gap:16px}.moats div{background:var(--tealbg);border:1px solid var(--teal);border-radius:10px;padding:10px;margin-bottom:8px}.moats b{display:block;color:var(--navy)}.moats span{font-size:12px}
.chart{display:flex;align-items:flex-end;gap:18px;height:250px;border-bottom:2px solid #CFC7B8;padding-top:20px}.bc{flex:1;height:100%;display:flex;flex-direction:column;justify-content:flex-end;align-items:center}.bar{width:70%;background:var(--navy);border-radius:6px 6px 0 0}.bv{font-weight:700;color:var(--navy)}.be{font-weight:700;color:var(--teal);margin-top:4px}.be.neg{color:var(--red)}.by{font-size:12px;color:var(--grey)}
.uof{display:grid;grid-template-columns:260px 1fr 50px;align-items:center;gap:8px;margin:6px 0;font-size:14px}.uof i{height:14px;background:var(--teal);border-radius:4px}.ms{background:#1B3A66;border-radius:12px;padding:16px 22px}.ms li{margin-bottom:8px}
.foot{position:absolute;left:56px;right:56px;bottom:16px;font-size:11px;color:var(--grey);font-style:italic}.pn{position:absolute;right:24px;bottom:14px;font-size:12px;color:var(--grey)}
.help{position:fixed;left:12px;bottom:8px;color:#55637E;font:12px Arial}
"""
JS = "const S=[...document.querySelectorAll('.s')];let i=Math.max(0,(parseInt(location.hash.slice(1))||1)-1);function r(){S.forEach((s,k)=>s.classList.toggle('on',k===i));history.replaceState(null,'','#'+(i+1));const sc=Math.min(innerWidth/1280,innerHeight/720)*.98;document.getElementById('deck').style.transform='scale('+sc+')'}addEventListener('keydown',e=>{if(['ArrowRight',' ','PageDown'].includes(e.key))i=Math.min(S.length-1,i+1);if(['ArrowLeft','PageUp'].includes(e.key))i=Math.max(0,i-1);r()});addEventListener('click',()=>{i=Math.min(S.length-1,i+1);r()});addEventListener('resize',r);r();"
H = f'<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Keepwell Seed Deck</title><style>{CSS}</style></head><body><div id="deck">' + "".join(hs(d, i) for i, d in enumerate(MAIN + APPENDIX, 1)) + f'</div><div class="help">→ / click next · ← back · slides 13–15 are the appendix</div><script>{JS}</script></body></html>'
(HERE / "Keepwell_Seed_Deck.html").write_text(H); print("saved html")
