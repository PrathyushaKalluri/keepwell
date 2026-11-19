"""Render the Keepwell seed deck from deck_content.py.

Usage: python build_deck.py <out_dir>
Writes Keepwell_Seed_Deck.pptx and Keepwell_Seed_Deck.html. The PDF is made from the pptx with LibreOffice.
"""
import sys, os, html
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from deck_content import MAIN, APPENDIX
from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.chart.data import CategoryChartData
from pptx.enum.chart import XL_CHART_TYPE, XL_LEGEND_POSITION, XL_LABEL_POSITION

OUT = sys.argv[1] if len(sys.argv) > 1 else "."
NAVY = RGBColor(0x14, 0x2B, 0x4C); TEAL = RGBColor(0x0E, 0x8C, 0x7F); AMBER = RGBColor(0xE8, 0x9A, 0x2E)
INK = RGBColor(0x1E, 0x23, 0x2B); GREY = RGBColor(0x5F, 0x6B, 0x7A); LIGHT = RGBColor(0xF2, 0xF5, 0xF8); WHITE = RGBColor(0xFF, 0xFF, 0xFF)
LINE = RGBColor(0xD5, 0xDC, 0xE4); RED = RGBColor(0xC0, 0x39, 0x2B)
FONT = "Arial"

prs = Presentation()
prs.slide_width = Inches(13.333); prs.slide_height = Inches(7.5)
BLANK = prs.slide_layouts[6]
W = 13.333


def box(sl, x, y, w, h, fill=None, line=None, shape=MSO_SHAPE.RECTANGLE):
    s = sl.shapes.add_shape(shape, Inches(x), Inches(y), Inches(w), Inches(h))
    if fill is None:
        s.fill.background()
    else:
        s.fill.solid(); s.fill.fore_color.rgb = fill
    if line is None:
        s.line.fill.background()
    else:
        s.line.color.rgb = line; s.line.width = Pt(1)
    s.shadow.inherit = False
    return s


def text(sl, x, y, w, h, t, size=14, bold=False, color=INK, align=PP_ALIGN.LEFT, anchor=MSO_ANCHOR.TOP, italic=False, shape=None):
    tb = shape if shape is not None else sl.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    tf = tb.text_frame; tf.word_wrap = True; tf.vertical_anchor = anchor
    tf.margin_left = tf.margin_right = Inches(0.05); tf.margin_top = tf.margin_bottom = Inches(0.03)
    lines = t if isinstance(t, list) else [t]
    for i, ln in enumerate(lines):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.alignment = align
        r = p.add_run(); r.text = ln
        r.font.name = FONT; r.font.size = Pt(size); r.font.bold = bold; r.font.italic = italic; r.font.color.rgb = color
    return tb


def bullets(sl, x, y, w, h, items, size=13, color=INK, gap=6):
    tb = sl.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    tf = tb.text_frame; tf.word_wrap = True
    for i, it in enumerate(items):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.space_after = Pt(gap)
        r = p.add_run(); r.text = "•  " + it
        r.font.name = FONT; r.font.size = Pt(size); r.font.color.rgb = color
    return tb


def frame(sl, d, num):
    box(sl, 0, 0, W, 0.08, fill=TEAL)
    text(sl, 0.6, 0.35, 8, 0.35, d["kicker"].upper(), size=11, bold=True, color=TEAL)
    text(sl, 0.6, 0.68, 12.1, 1.2, d["headline"], size=26 if len(d["headline"]) < 70 else 22, bold=True, color=NAVY)
    text(sl, 11.6, 7.05, 1.3, 0.3, str(num), size=9, color=GREY, align=PP_ALIGN.RIGHT)
    text(sl, 0.6, 7.05, 6, 0.3, "Keepwell · Seed 2026", size=9, color=GREY)
    if d.get("notes"):
        sl.notes_slide.notes_text_frame.text = d["notes"]


def stat_tile(sl, x, y, w, h, val, lab, fill=LIGHT, vcol=NAVY, vsize=26):
    box(sl, x, y, w, h, fill=fill)
    text(sl, x + 0.15, y + 0.12, w - 0.3, h * 0.5, val, size=vsize, bold=True, color=vcol)
    text(sl, x + 0.15, y + h * 0.52, w - 0.3, h * 0.45, lab, size=11, color=RGBColor(0xC9, 0xD6, 0xE6) if fill == NAVY else GREY)


def foot(sl, t):
    text(sl, 0.6, 6.62, 12.1, 0.4, t, size=9, color=GREY, italic=True)


def r_title(sl, d, n):
    box(sl, 0, 0, W, 7.5, fill=NAVY)
    box(sl, 0.6, 2.05, 0.12, 2.1, fill=TEAL)
    text(sl, 0.95, 1.35, 10, 0.4, d["kicker"].upper(), size=13, bold=True, color=AMBER)
    text(sl, 0.95, 1.95, 11, 1.2, d["headline"], size=60, bold=True, color=WHITE)
    text(sl, 0.95, 3.15, 11, 0.6, d["tagline"], size=26, color=WHITE)
    text(sl, 0.95, 3.85, 11, 0.5, d["sub"], size=16, color=RGBColor(0xB8, 0xC7, 0xD9))
    text(sl, 0.95, 6.4, 11.5, 0.4, d["names"], size=12, color=RGBColor(0xB8, 0xC7, 0xD9))
    sl.notes_slide.notes_text_frame.text = d["notes"]


def r_story(sl, d, n):
    frame(sl, d, n)
    bullets(sl, 0.6, 2.2, 7.0, 4.0, d["left"], size=15, gap=10)
    box(sl, 8.1, 2.25, 4.6, 3.3, fill=NAVY)
    text(sl, 8.35, 2.5, 4.1, 2.2, d["quote"], size=20, bold=True, color=WHITE, italic=True)
    text(sl, 8.35, 4.85, 4.1, 0.5, "— " + d["quote_by"], size=12, color=AMBER)


def r_stats(sl, d, n):
    frame(sl, d, n)
    text(sl, 0.6, 1.62, 12, 0.45, d["sub"], size=15, color=GREY)
    for i, (v, l) in enumerate(d["stats"]):
        stat_tile(sl, 0.6 + i * 4.1, 2.25, 3.9, 1.35, v, l, vsize=30)
    for i, (h, its) in enumerate(d["cols"]):
        x = 0.6 + i * 6.15
        text(sl, x, 3.85, 5.9, 0.35, h, size=14, bold=True, color=TEAL)
        bullets(sl, x, 4.25, 5.9, 2.3, its, size=12)
    foot(sl, d["foot"])


def r_insight(sl, d, n):
    frame(sl, d, n)
    for i, (k, q) in enumerate(d["points"]):
        y = 2.2 + i * 1.15
        box(sl, 0.6, y, 1.6, 0.95, fill=NAVY)
        text(sl, 0.6, y, 1.6, 0.95, k, size=15, bold=True, color=WHITE, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
        text(sl, 2.35, y + 0.12, 4.9, 0.8, q, size=13, italic=True, color=INK)
    text(sl, 7.7, 2.2, 5, 0.4, d["right_head"], size=14, bold=True, color=TEAL)
    for i, (v, l) in enumerate(d["right"]):
        stat_tile(sl, 7.7, 2.7 + i * 1.0, 5.0, 0.88, v, l, vsize=20)
    box(sl, 0.6, 5.85, 12.1, 0.62, fill=TEAL)
    text(sl, 0.8, 5.85, 11.7, 0.62, d["land"], size=16, bold=True, color=WHITE, anchor=MSO_ANCHOR.MIDDLE)


def r_lifecycle(sl, d, n):
    frame(sl, d, n)
    text(sl, 0.6, 1.5, 12, 0.45, d["sub"], size=15, color=GREY)
    sw = 12.1 / len(d["stages"])
    for i, st in enumerate(d["stages"]):
        s = box(sl, 0.6 + i * sw, 2.1, sw - 0.05, 0.7, fill=TEAL if st == "Repaired" else NAVY, shape=MSO_SHAPE.CHEVRON)
        text(sl, 0, 0, 0, 0, st, size=12, bold=True, color=WHITE, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE, shape=s)
    box(sl, 0.6, 2.95, 12.1, 0.38, fill=AMBER)
    text(sl, 0.6, 2.95, 12.1, 0.38, "One living record per machine — the Keepwell record", size=12, bold=True, color=WHITE, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    for i, (rel, prod, desc) in enumerate(d["products"]):
        col, row = i % 3, i // 3
        x, y = 0.6 + col * 4.07, 3.6 + row * 1.45
        box(sl, x, y, 3.95, 1.3, fill=LIGHT)
        text(sl, x + 0.15, y + 0.08, 3.6, 0.3, rel, size=10, bold=True, color=TEAL)
        text(sl, x + 0.15, y + 0.36, 3.6, 0.4, prod, size=15, bold=True, color=NAVY)
        text(sl, x + 0.15, y + 0.78, 3.6, 0.5, desc, size=11, color=GREY)


def r_flow(sl, d, n):
    frame(sl, d, n)
    k = len(d["steps"]); cw = 12.1 / k
    for i, (nm, desc) in enumerate(d["steps"]):
        x = 0.6 + i * cw
        fill = TEAL if nm in ("Root cause", "Verify") else (AMBER if nm == "Safety" else NAVY)
        s = box(sl, x, 1.95, cw - 0.1, 0.75, fill=fill, shape=MSO_SHAPE.CHEVRON if i else MSO_SHAPE.PENTAGON)
        text(sl, 0, 0, 0, 0, nm, size=12, bold=True, color=WHITE, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE, shape=s)
        text(sl, x, 2.85, cw - 0.12, 2.8, desc, size=11, color=INK)
    box(sl, 0.6, 5.75, 12.1, 0.7, fill=LIGHT)
    text(sl, 0.8, 5.75, 11.7, 0.7, d["principle"], size=16, bold=True, color=NAVY, anchor=MSO_ANCHOR.MIDDLE, align=PP_ALIGN.CENTER)


def r_traction(sl, d, n):
    frame(sl, d, n)
    k = len(d["stats"]); tw = 12.1 / k
    for i, (v, l) in enumerate(d["stats"]):
        stat_tile(sl, 0.6 + i * tw, 1.65, tw - 0.12, 1.2, v, l, vsize=22)
    c = d["chart"]
    cd = CategoryChartData(); cd.categories = c["cats"]; cd.add_series("Top-3 accuracy %", c["vals"]); cd.add_series("Gate", [c["target"]] * len(c["cats"]))
    gf = sl.shapes.add_chart(XL_CHART_TYPE.LINE_MARKERS, Inches(0.6), Inches(3.05), Inches(7.2), Inches(3.4), cd)
    ch = gf.chart; ch.has_legend = True; ch.legend.position = XL_LEGEND_POSITION.BOTTOM; ch.legend.include_in_layout = False
    ch.has_title = True; ch.chart_title.text_frame.text = c["title"]
    ch.chart_title.text_frame.paragraphs[0].runs[0].font.size = Pt(12)
    ch.font.size = Pt(10); ch.font.name = FONT
    va = ch.value_axis; va.minimum_scale = 50; va.maximum_scale = 80; va.has_major_gridlines = True
    s0 = ch.series[0]; s0.format.line.color.rgb = TEAL; s0.format.line.width = Pt(3)
    s0.smooth = False; pl = ch.plots[0]
    s1 = ch.series[1]; s1.format.line.color.rgb = AMBER; s1.format.line.dash_style = 4
    s0.data_labels.show_value = True; s0.data_labels.position = XL_LABEL_POSITION.ABOVE; s0.data_labels.font.size = Pt(10)
    box(sl, 8.2, 3.15, 4.5, 2.0, fill=NAVY)
    text(sl, 8.4, 3.3, 4.1, 1.8, ["The learning loop, visible:", "every verified fix improves the next ranking."], size=15, bold=True, color=WHITE)
    box(sl, 8.2, 5.3, 4.5, 1.15, fill=None, line=AMBER)
    text(sl, 8.35, 5.35, 4.2, 1.05, d["honest"], size=12, color=INK)
    foot(sl, d["foot"])


def r_flywheel(sl, d, n):
    frame(sl, d, n)
    import math
    cx, cy, r = 3.55, 4.25, 1.75
    box(sl, cx - 1.0, cy - 0.5, 2.0, 1.0, fill=TEAL, shape=MSO_SHAPE.OVAL)
    text(sl, cx - 1.0, cy - 0.5, 2.0, 1.0, "Mistri Gyan + the record", size=11, bold=True, color=WHITE, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    k = len(d["wheel"])
    for i, nm in enumerate(d["wheel"]):
        a = -math.pi / 2 + 2 * math.pi * i / k
        x, y = cx + r * math.cos(a) * 1.3 - 0.85, cy + r * math.sin(a) - 0.32
        s = box(sl, x, y, 1.7, 0.64, fill=NAVY, shape=MSO_SHAPE.ROUNDED_RECTANGLE)
        text(sl, 0, 0, 0, 0, nm, size=10, bold=True, color=WHITE, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE, shape=s)
    text(sl, 7.3, 1.95, 5.4, 0.35, "A rival can copy in a quarter", size=13, bold=True, color=GREY)
    bullets(sl, 7.3, 2.3, 5.4, 1.6, d["copy"], size=11, color=GREY, gap=2)
    text(sl, 7.3, 3.95, 5.4, 0.35, "A rival cannot copy", size=13, bold=True, color=TEAL)
    bullets(sl, 7.3, 4.3, 5.4, 2.3, d["nocopy"], size=12, gap=3)


def r_tiles(sl, d, n):
    frame(sl, d, n)
    for i, (h, t) in enumerate(d["tiles"]):
        col, row = i % 2, i // 2
        x, y = 0.6 + col * 6.15, 2.0 + row * 2.25
        box(sl, x, y, 5.95, 2.05, fill=LIGHT)
        box(sl, x, y, 0.1, 2.05, fill=TEAL)
        text(sl, x + 0.3, y + 0.25, 5.4, 0.7, h, size=26, bold=True, color=NAVY)
        text(sl, x + 0.3, y + 1.05, 5.4, 0.9, t, size=14, color=INK)


def r_market(sl, d, n):
    frame(sl, d, n)
    k = len(d["funnel"])
    for i, (lab, v) in enumerate(d["funnel"]):
        w = 6.8 - i * 1.2; x = 0.6 + (6.8 - w) / 2; y = 1.95 + i * 1.05
        box(sl, x, y, w, 0.92, fill=[NAVY, RGBColor(0x2A, 0x4F, 0x7A), TEAL, AMBER][i])
        text(sl, x, y + 0.02, w, 0.5, v, size=22, bold=True, color=WHITE, align=PP_ALIGN.CENTER)
        text(sl, x, y + 0.5, w, 0.4, lab, size=10, color=WHITE, align=PP_ALIGN.CENTER)
    for i, (lab, v) in enumerate(d["pools"]):
        y = 2.0 + i * 2.0
        box(sl, 7.9, y, 4.8, 1.8, fill=LIGHT)
        text(sl, 8.1, y + 0.2, 4.4, 0.7, v, size=24, bold=True, color=NAVY if i == 0 else TEAL)
        text(sl, 8.1, y + 0.95, 4.4, 0.8, lab, size=13, color=GREY)
    foot(sl, d["foot"])


def r_compete(sl, d, n):
    frame(sl, d, n)
    X0, Y0, S = 0.9, 1.95, 4.5
    box(sl, X0, Y0, S, S, fill=LIGHT)
    box(sl, X0 + S / 2, Y0, S / 2, S / 2, fill=RGBColor(0xDD, 0xF1, 0xEE))
    text(sl, X0, Y0 + S + 0.05, S / 2, 0.3, "← " + d["xlab"][0], size=9, color=GREY)
    text(sl, X0 + S / 2, Y0 + S + 0.05, S / 2, 0.3, d["xlab"][1] + " →", size=9, color=GREY, align=PP_ALIGN.RIGHT)
    text(sl, X0 - 0.35, Y0, 0.3, S, "", size=9)
    text(sl, X0 + 0.05, Y0 + 0.05, S, 0.3, "↑ " + d["ylab"][1], size=9, color=GREY)
    text(sl, X0 + 0.05, Y0 + S - 0.32, S, 0.3, "↓ " + d["ylab"][0], size=9, color=GREY)
    for nm, x, y in d["dots"]:
        px, py = X0 + x * S, Y0 + (1 - y) * S
        kw = nm == "Keepwell"
        sz = 0.34 if kw else 0.2
        box(sl, px - sz / 2, py - sz / 2, sz, sz, fill=TEAL if kw else NAVY, shape=MSO_SHAPE.OVAL)
        text(sl, px + 0.12, py - 0.17, 1.8, 0.3, nm, size=12 if kw else 9, bold=kw, color=TEAL if kw else INK)
    tbl = sl.shapes.add_table(len(d["rows"]) + 1, 2, Inches(6.0), Inches(2.0), Inches(6.7), Inches(3.8)).table
    tbl.columns[0].width = Inches(2.2); tbl.columns[1].width = Inches(4.5)
    for j, h in enumerate(["Player", "Why they're not us"]):
        c = tbl.cell(0, j); c.text = h
    for i, (a, b) in enumerate(d["rows"]):
        tbl.cell(i + 1, 0).text = a; tbl.cell(i + 1, 1).text = b
    style_table(tbl, 11)


def style_table(tbl, size=11):
    for r_i, row in enumerate(tbl.rows):
        for c in row.cells:
            c.fill.solid(); c.fill.fore_color.rgb = NAVY if r_i == 0 else (LIGHT if r_i % 2 else WHITE)
            for p in c.text_frame.paragraphs:
                for r in p.runs:
                    r.font.name = FONT; r.font.size = Pt(size); r.font.bold = r_i == 0
                    r.font.color.rgb = WHITE if r_i == 0 else INK
            c.margin_left = c.margin_right = Inches(0.08)


def r_bizmodel(sl, d, n):
    frame(sl, d, n)
    for i, (k, v) in enumerate(d["ladder"]):
        y = 1.95 + i * 0.66
        box(sl, 0.6, y, 1.3, 0.56, fill=NAVY if i == 0 else RGBColor(0x2A, 0x4F, 0x7A))
        text(sl, 0.6, y, 1.3, 0.56, k, size=11, bold=True, color=WHITE, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
        text(sl, 2.0, y + 0.08, 4.6, 0.5, v, size=12, color=INK)
    box(sl, 7.0, 1.95, 5.7, 1.55, fill=TEAL)
    text(sl, 7.2, 2.0, 1.8, 1.4, d["compare"][0], size=40, bold=True, color=WHITE, anchor=MSO_ANCHOR.MIDDLE)
    text(sl, 8.9, 2.1, 3.7, 1.35, d["compare"][1], size=13, color=WHITE, anchor=MSO_ANCHOR.MIDDLE)
    for i, (v, l) in enumerate(d["stats"]):
        col, row = i % 2, i // 2
        stat_tile(sl, 7.0 + col * 2.9, 3.7 + row * 1.25, 2.8, 1.12, v, l, vsize=22)
    foot(sl, d["foot"])


def r_plan(sl, d, n):
    frame(sl, d, n)
    cd = CategoryChartData(); cd.categories = d["years"]
    cd.add_series("Revenue (₹ Cr)", d["revenue"])
    gf = sl.shapes.add_chart(XL_CHART_TYPE.COLUMN_CLUSTERED, Inches(0.6), Inches(2.05), Inches(7.4), Inches(3.6), cd)
    ch = gf.chart; ch.has_legend = True; ch.legend.position = XL_LEGEND_POSITION.BOTTOM; ch.legend.include_in_layout = False
    ch.font.size = Pt(10); ch.font.name = FONT
    ch.series[0].format.fill.solid(); ch.series[0].format.fill.fore_color.rgb = NAVY
    ch.has_legend = False
    pl = ch.plots[0]; pl.has_data_labels = True; pl.data_labels.number_format = '0.0'; pl.data_labels.number_format_is_linked = False
    pl.data_labels.font.size = Pt(9)
    text(sl, 0.6, 1.65, 7.4, 0.3, "Paying agencies: " + " → ".join(f"{a:,}" for a in d["agencies"]), size=11, bold=True, color=TEAL)
    text(sl, 0.6, 5.7, 1.6, 0.35, "EBITDA (₹ Cr)", size=10, bold=True, color=GREY)
    for i, (yr, e) in enumerate(zip(d["years"], d["ebitda"])):
        x = 2.15 + i * 1.17
        box(sl, x, 5.68, 1.1, 0.42, fill=TEAL if e >= 0 else RGBColor(0xF6, 0xE0, 0xDD))
        text(sl, x, 5.68, 1.1, 0.42, f"{yr}  {e:+.1f}", size=11, bold=True, color=WHITE if e >= 0 else RED, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    for i, (v, l) in enumerate(d["stats"]):
        stat_tile(sl, 8.3, 1.9 + i * 1.13, 4.4, 1.02, v, l, vsize=20)
    foot(sl, d["foot"])


def r_team(sl, d, n):
    frame(sl, d, n)
    for i, (nm, role, line) in enumerate(d["people"]):
        x = 0.6 + i * 4.07
        box(sl, x, 1.9, 3.95, 2.35, fill=LIGHT)
        box(sl, x, 1.9, 3.95, 0.08, fill=TEAL)
        text(sl, x + 0.2, 2.05, 3.6, 0.4, nm, size=17, bold=True, color=NAVY)
        text(sl, x + 0.2, 2.45, 3.6, 0.3, role, size=12, bold=True, color=TEAL)
        text(sl, x + 0.2, 2.8, 3.6, 1.4, line, size=11, color=INK)
    text(sl, 0.6, 4.4, 12.1, 0.5, d["advisors"], size=11, color=GREY)
    text(sl, 0.6, 4.95, 12.1, 0.35, "Already backing us", size=13, bold=True, color=TEAL)
    k = len(d["backers"]); bw = 12.1 / k
    for i, b in enumerate(d["backers"]):
        last = i == k - 1
        box(sl, 0.6 + i * bw, 5.35, bw - 0.1, 0.9, fill=AMBER if last else NAVY)
        text(sl, 0.6 + i * bw, 5.35, bw - 0.1, 0.9, b, size=10, bold=True, color=WHITE, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    foot(sl, d["foot"])


def r_trust(sl, d, n):
    frame(sl, d, n)
    for i, (h, t) in enumerate(d["tiers"]):
        x = 0.6 + i * 4.07
        box(sl, x, 1.95, 3.95, 1.4, fill=[TEAL, NAVY, AMBER][i])
        text(sl, x + 0.2, 2.05, 3.6, 0.5, h, size=18, bold=True, color=WHITE)
        text(sl, x + 0.2, 2.6, 3.6, 0.7, t, size=12, color=WHITE)
    bullets(sl, 0.6, 3.65, 12.1, 2.9, d["points"], size=14, gap=10)


def r_ask(sl, d, n):
    frame(sl, d, n)
    for i, (v, l) in enumerate(d["terms"]):
        stat_tile(sl, 0.6 + i * 3.05, 1.85, 2.9, 1.05, v, l, fill=NAVY, vcol=WHITE, vsize=24)
    text(sl, 0.6, 3.1, 6, 0.35, "Use of funds", size=13, bold=True, color=TEAL)
    for i, (lab, pct) in enumerate(d["uof"]):
        y = 3.5 + i * 0.5
        text(sl, 0.6, y, 2.9, 0.4, lab, size=11, color=INK)
        box(sl, 3.5, y + 0.07, max(0.05, 3.0 * pct / 40), 0.3, fill=[NAVY, RGBColor(0x2A, 0x4F, 0x7A), TEAL, AMBER, GREY][i])
        text(sl, 3.55 + 3.0 * pct / 40, y, 0.7, 0.4, f"{pct}%", size=11, bold=True, color=INK)
    text(sl, 7.3, 3.1, 5.4, 0.35, "Milestones this buys (Series A gates)", size=13, bold=True, color=TEAL)
    bullets(sl, 7.3, 3.5, 5.4, 2.3, d["milestones"], size=12, gap=4)
    text(sl, 7.3, 5.55, 5.4, 0.4, d["extra"], size=11, italic=True, color=GREY)
    box(sl, 0.6, 6.15, 12.1, 0.55, fill=TEAL)
    text(sl, 0.8, 6.15, 11.7, 0.55, d["close"], size=16, bold=True, color=WHITE, anchor=MSO_ANCHOR.MIDDLE, align=PP_ALIGN.CENTER)


def r_table(sl, d, n):
    frame(sl, d, n)
    cols, rows = d["cols"], d["rows"]
    tbl = sl.shapes.add_table(len(rows) + 1, len(cols), Inches(0.6), Inches(1.7), Inches(12.1), Inches(0.42 * (len(rows) + 1))).table
    for j, h in enumerate(cols):
        tbl.cell(0, j).text = h
    for i, r in enumerate(rows):
        for j, v in enumerate(r):
            tbl.cell(i + 1, j).text = v
    style_table(tbl, 11 if len(rows) < 8 else 10)


R = dict(title=r_title, story=r_story, stats=r_stats, insight=r_insight, lifecycle=r_lifecycle, flow=r_flow, traction=r_traction,
         flywheel=r_flywheel, tiles=r_tiles, market=r_market, compete=r_compete, bizmodel=r_bizmodel, plan=r_plan, team=r_team,
         trust=r_trust, ask=r_ask, table=r_table)

n = 0
for d in MAIN:
    n += 1; R[d["type"]](prs.slides.add_slide(BLANK), d, n)
# appendix divider
n += 1
sl = prs.slides.add_slide(BLANK); box(sl, 0, 0, W, 7.5, fill=NAVY)
text(sl, 0.95, 3.0, 11, 1.0, "Appendix", size=48, bold=True, color=WHITE)
text(sl, 0.95, 4.0, 11, 0.6, "Backup for Q&A — the workings behind every number", size=18, color=RGBColor(0xB8, 0xC7, 0xD9))
for d in APPENDIX:
    n += 1; R[d["type"]](prs.slides.add_slide(BLANK), d, n)
pptx_path = os.path.join(OUT, "Keepwell_Seed_Deck.pptx")
prs.save(pptx_path)
print("saved", pptx_path, n, "slides")

# ------------------------------------------------------------------ HTML (animated web deck)
E = html.escape


def h_items(items, cls="b"):
    return "".join(f'<li class="a" style="--d:{0.15 + i * 0.08:.2f}s">{E(t)}</li>' for i, t in enumerate(items))


def h_stat(v, l, i, cls=""):
    return f'<div class="stat a {cls}" style="--d:{0.1 + i * 0.08:.2f}s"><b>{E(v)}</b><span>{E(l)}</span></div>'


def h_line_chart(c):
    vals, cats = c["vals"], c["cats"]; lo, hi = 50, 80; Wc, Hc, P = 520, 240, 40
    xs = [P + i * (Wc - 2 * P) / (len(vals) - 1) for i in range(len(vals))]
    ys = [Hc - P - (v - lo) / (hi - lo) * (Hc - 2 * P) for v in vals]
    ty = Hc - P - (c["target"] - lo) / (hi - lo) * (Hc - 2 * P)
    path = " ".join(f"{'M' if i == 0 else 'L'}{x:.0f},{y:.0f}" for i, (x, y) in enumerate(zip(xs, ys)))
    pts = "".join(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="6" class="dot"/><text x="{x:.0f}" y="{y - 14:.0f}" class="lbl">{v}%</text>' for x, y, v in zip(xs, ys, vals))
    xl = "".join(f'<text x="{x:.0f}" y="{Hc - 12}" class="ax">{E(ct)}</text>' for x, ct in zip(xs, cats))
    return (f'<svg viewBox="0 0 {Wc} {Hc}" class="chart a" style="--d:.3s"><text x="{P}" y="20" class="ct">{E(c["title"])}</text>'
            f'<line x1="{P}" x2="{Wc - P}" y1="{ty:.0f}" y2="{ty:.0f}" class="gate"/><text x="{P + 6}" y="{ty - 6:.0f}" class="gl" style="text-anchor:start">gate {c["target"]}%</text>'
            f'<path d="{path}" class="ln"/>{pts}{xl}</svg>')


def h_bar_chart(years, rev, eb):
    Wc, Hc, P = 560, 300, 40; mx = max(rev); mn = min(eb); rng = mx - mn
    zero = P + mx / rng * (Hc - 2 * P); bw = (Wc - 2 * P) / len(years)
    out = [f'<svg viewBox="0 0 {Wc} {Hc}" class="chart a" style="--d:.25s"><line x1="{P}" x2="{Wc - P}" y1="{zero:.0f}" y2="{zero:.0f}" class="zero"/>']
    for i, (yr, r, e) in enumerate(zip(years, rev, eb)):
        x = P + i * bw + 8; w = bw / 2 - 10
        rh = r / rng * (Hc - 2 * P); eh = abs(e) / rng * (Hc - 2 * P)
        out.append(f'<rect x="{x:.0f}" y="{zero - rh:.0f}" width="{w:.0f}" height="{max(rh, 1):.0f}" class="rv grow" style="--d:{0.3 + i * 0.1:.2f}s"/>')
        ey = zero - eh if e >= 0 else zero
        out.append(f'<rect x="{x + w + 4:.0f}" y="{ey:.0f}" width="{w:.0f}" height="{max(eh, 1):.0f}" class="eb {"pos" if e >= 0 else "neg"} grow" style="--d:{0.35 + i * 0.1:.2f}s"/>')
        out.append(f'<text x="{x + w / 2:.0f}" y="{zero - rh - 6:.0f}" class="lbl">{r:.1f}</text>')
        out.append(f'<text x="{x + w * 1.5 + 4:.0f}" y="{(ey - 6) if e >= 0 else (ey + eh + 14):.0f}" class="lbl s">{e:+.1f}</text>')
        out.append(f'<text x="{x + w:.0f}" y="{Hc - 8}" class="ax">{yr}</text>')
    out.append('<text x="40" y="18" class="ct">Revenue vs EBITDA (₹ Cr)</text></svg>')
    return "".join(out)


def h_slide(d, num, total):
    t = d["type"]; k = E(d.get("kicker", "")); hd = E(d.get("headline", ""))
    head = f'<div class="kick a" style="--d:0s">{k}</div><h2 class="a" style="--d:.05s">{hd}</h2>' if t != "title" else ""
    body = ""
    if t == "title":
        return (f'<section class="slide title" data-n="{num}"><div class="bar a"></div><div class="kick a" style="--d:.1s">{k}</div>'
                f'<h1 class="a" style="--d:.2s">{hd}</h1><p class="tag a" style="--d:.35s">{E(d["tagline"])}</p>'
                f'<p class="sub a" style="--d:.5s">{E(d["sub"])}</p><p class="names a" style="--d:.65s">{E(d["names"])}</p></section>')
    if t == "story":
        body = f'<div class="g2"><ul class="big">{h_items(d["left"])}</ul><blockquote class="a" style="--d:.5s">{E(d["quote"])}<cite>— {E(d["quote_by"])}</cite></blockquote></div>'
    elif t == "stats":
        body = (f'<p class="lead a" style="--d:.1s">{E(d["sub"])}</p><div class="stats">' + "".join(h_stat(v, l, i, "xl") for i, (v, l) in enumerate(d["stats"])) + '</div><div class="g2">'
                + "".join(f'<div><h3 class="a" style="--d:.4s">{E(h)}</h3><ul>{h_items(it)}</ul></div>' for h, it in d["cols"]) + f'</div><p class="foot">{E(d["foot"])}</p>')
    elif t == "insight":
        body = ('<div class="g2"><div>' + "".join(f'<div class="pt a" style="--d:{0.15 + i * 0.1:.2f}s"><b>{E(a)}</b><i>{E(b)}</i></div>' for i, (a, b) in enumerate(d["points"]))
                + f'</div><div><h3>{E(d["right_head"])}</h3><div class="stats col">' + "".join(h_stat(v, l, i) for i, (v, l) in enumerate(d["right"])) + f'</div></div></div><div class="land a" style="--d:.7s">{E(d["land"])}</div>')
    elif t == "lifecycle":
        body = (f'<p class="lead a">{E(d["sub"])}</p><div class="chev">' + "".join(f'<span class="a {"hl" if s == "Repaired" else ""}" style="--d:{0.1 + i * 0.07:.2f}s">{E(s)}</span>' for i, s in enumerate(d["stages"]))
                + '</div><div class="rec a" style="--d:.65s">One living record per machine — the Keepwell record</div><div class="cards">'
                + "".join(f'<div class="card a" style="--d:{0.75 + i * 0.07:.2f}s"><small>{E(r)}</small><b>{E(p)}</b><span>{E(x)}</span></div>' for i, (r, p, x) in enumerate(d["products"])) + '</div>')
    elif t == "flow":
        body = ('<div class="flow">' + "".join(f'<div class="step a {"hl" if nm in ("Root cause", "Verify") else ("warn" if nm == "Safety" else "")}" style="--d:{0.1 + i * 0.12:.2f}s"><b>{E(nm)}</b><span>{E(ds)}</span></div>' for i, (nm, ds) in enumerate(d["steps"]))
                + f'</div><div class="land a" style="--d:1s">{E(d["principle"])}</div>')
    elif t == "traction":
        body = ('<div class="stats">' + "".join(h_stat(v, l, i) for i, (v, l) in enumerate(d["stats"])) + '</div><div class="g2">' + h_line_chart(d["chart"])
                + f'<div><div class="callout a" style="--d:.5s">The learning loop, visible: every verified fix improves the next ranking.</div><div class="honest a" style="--d:.7s">{E(d["honest"])}</div></div></div><p class="foot">{E(d["foot"])}</p>')
    elif t == "flywheel":
        body = ('<div class="g2"><div class="wheel">' + "".join(f'<span class="a" style="--d:{0.1 + i * 0.1:.2f}s;--i:{i}">{E(w)}</span>' for i, w in enumerate(d["wheel"]))
                + f'<em class="a" style="--d:.9s">Mistri Gyan + the record</em></div><div><h3 class="muted">A rival can copy in a quarter</h3><ul class="muted">{h_items(d["copy"])}</ul><h3>A rival cannot copy</h3><ul>{h_items(d["nocopy"])}</ul></div></div>')
    elif t == "tiles":
        body = '<div class="tiles">' + "".join(f'<div class="tile a" style="--d:{0.1 + i * 0.12:.2f}s"><b>{E(h)}</b><span>{E(x)}</span></div>' for i, (h, x) in enumerate(d["tiles"])) + '</div>'
    elif t == "market":
        body = ('<div class="g2"><div class="funnel">' + "".join(f'<div class="f a" style="--d:{0.1 + i * 0.15:.2f}s;--w:{100 - i * 18}%"><b>{E(v)}</b><span>{E(l)}</span></div>' for i, (l, v) in enumerate(d["funnel"]))
                + '</div><div class="stats col">' + "".join(h_stat(v, l, i + 4, "xl") for i, (l, v) in enumerate(d["pools"])) + f'</div></div><p class="foot">{E(d["foot"])}</p>')
    elif t == "compete":
        dots = "".join(f'<i class="a {"me" if nm == "Keepwell" else ""}" style="--d:{0.2 + i * 0.07:.2f}s;left:{x * 100:.0f}%;bottom:{y * 100:.0f}%"><u>{E(nm)}</u></i>' for i, (nm, x, y) in enumerate(d["dots"]))
        rows = "".join(f'<tr class="a" style="--d:{0.4 + i * 0.07:.2f}s"><td>{E(a)}</td><td>{E(b)}</td></tr>' for i, (a, b) in enumerate(d["rows"]))
        body = (f'<div class="g2"><div class="map"><div class="q"></div>{dots}<small class="xl">← {E(d["xlab"][0])}</small><small class="xr">{E(d["xlab"][1])} →</small>'
                f'<small class="yt">↑ {E(d["ylab"][1])}</small><small class="yb">↓ {E(d["ylab"][0])}</small></div><table><tr><th>Player</th><th>Why they\'re not us</th></tr>{rows}</table></div>')
    elif t == "bizmodel":
        body = ('<div class="g2"><div class="ladder">' + "".join(f'<div class="a" style="--d:{0.1 + i * 0.1:.2f}s"><b>{E(a)}</b><span>{E(b)}</span></div>' for i, (a, b) in enumerate(d["ladder"]))
                + f'</div><div><div class="cmp a" style="--d:.5s"><b>{E(d["compare"][0])}</b><span>{E(d["compare"][1])}</span></div><div class="stats g">'
                + "".join(h_stat(v, l, i + 6) for i, (v, l) in enumerate(d["stats"])) + f'</div></div></div><p class="foot">{E(d["foot"])}</p>')
    elif t == "plan":
        body = (f'<div class="g2"><div><p class="agn a">Paying agencies: {" → ".join(f"{a:,}" for a in d["agencies"])}</p>{h_bar_chart(d["years"], d["revenue"], d["ebitda"])}</div><div class="stats col">'
                + "".join(h_stat(v, l, i + 3) for i, (v, l) in enumerate(d["stats"])) + f'</div></div><p class="foot">{E(d["foot"])}</p>')
    elif t == "team":
        body = ('<div class="cards three">' + "".join(f'<div class="card a" style="--d:{0.1 + i * 0.12:.2f}s"><b>{E(nm)}</b><small>{E(r)}</small><span>{E(l)}</span></div>' for i, (nm, r, l) in enumerate(d["people"]))
                + f'</div><p class="muted a" style="--d:.5s">{E(d["advisors"])}</p><h3>Already backing us</h3><div class="chips">'
                + "".join(f'<span class="a {"hl" if i == len(d["backers"]) - 1 else ""}" style="--d:{0.6 + i * 0.07:.2f}s">{E(b)}</span>' for i, b in enumerate(d["backers"])) + f'</div><p class="foot">{E(d["foot"])}</p>')
    elif t == "trust":
        body = ('<div class="tiers">' + "".join(f'<div class="a t{i}" style="--d:{0.1 + i * 0.12:.2f}s"><b>{E(h)}</b><span>{E(x)}</span></div>' for i, (h, x) in enumerate(d["tiers"])) + f'</div><ul class="big">{h_items(d["points"])}</ul>')
    elif t == "ask":
        uof = "".join(f'<div class="u a" style="--d:{0.4 + i * 0.08:.2f}s"><span>{E(l)}</span><i style="--p:{p * 2.4}%"></i><b>{p}%</b></div>' for i, (l, p) in enumerate(d["uof"]))
        body = ('<div class="stats">' + "".join(h_stat(v, l, i, "inv") for i, (v, l) in enumerate(d["terms"])) + f'</div><div class="g2"><div><h3>Use of funds</h3>{uof}</div><div><h3>Milestones this buys</h3><ul>{h_items(d["milestones"])}</ul><p class="muted">{E(d["extra"])}</p></div></div>'
                f'<div class="land a" style="--d:1.1s">{E(d["close"])}</div>')
    elif t == "table":
        th = "".join(f"<th>{E(c)}</th>" for c in d["cols"])
        trs = "".join("<tr>" + "".join(f"<td>{E(v)}</td>" for v in r) + "</tr>" for r in d["rows"])
        body = f'<table class="apx a" style="--d:.15s"><tr>{th}</tr>{trs}</table>'
    notes = f'<aside class="notes">{E(d.get("notes", ""))}</aside>' if d.get("notes") else ""
    return f'<section class="slide t-{t}" data-n="{num}">{head}{body}<div class="pg">Keepwell · Seed 2026 <span>{num} / {total}</span></div>{notes}</section>'


slides = MAIN + [dict(type="divider")] + APPENDIX
total = len(slides)
parts = []
for i, d in enumerate(slides, 1):
    if d["type"] == "divider":
        parts.append(f'<section class="slide title" data-n="{i}"><h1 class="a">Appendix</h1><p class="tag a" style="--d:.2s">Backup for Q&amp;A — the workings behind every number</p></section>')
    else:
        parts.append(h_slide(d, i, total))

CSS = r"""
:root{--navy:#142B4C;--teal:#0E8C7F;--amber:#E89A2E;--ink:#1E232B;--grey:#5F6B7A;--light:#F2F5F8;--line:#D5DCE4;--bg:#E9EDF2;--card:#fff}
:root[data-theme="dark"]{--ink:#E8EDF3;--grey:#9AA7B6;--light:#1C2A3D;--line:#2B3B52;--bg:#0B1220;--card:#121C2C}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){--ink:#E8EDF3;--grey:#9AA7B6;--light:#1C2A3D;--line:#2B3B52;--bg:#0B1220;--card:#121C2C}}
*{box-sizing:border-box}html,body{margin:0;height:100%;background:var(--bg);font-family:Inter,Arial,Helvetica,sans-serif;color:var(--ink);overflow:hidden}
#stage{position:absolute;left:50%;top:50%;width:1280px;height:720px;transform-origin:center;}
.slide{position:absolute;inset:0;background:var(--card);padding:44px 58px 40px;opacity:0;pointer-events:none;transition:opacity .45s ease;border-radius:10px;box-shadow:0 10px 40px rgba(0,0,0,.18);overflow:hidden}
.slide::before{content:"";position:absolute;left:0;top:0;right:0;height:7px;background:var(--teal)}
.slide.on{opacity:1;pointer-events:auto}
.a{opacity:0;transform:translateY(14px);transition:opacity .55s ease,transform .55s ease;transition-delay:var(--d,0s)}
.on .a{opacity:1;transform:none}
.grow{transform-origin:bottom;transform:scaleY(0);transition:transform .7s cubic-bezier(.2,.8,.2,1);transition-delay:var(--d,0s);transform-box:fill-box}
.on .grow{transform:scaleY(1)}
.kick{color:var(--teal);font-weight:700;letter-spacing:.12em;font-size:13px;text-transform:uppercase}
h2{color:var(--navy);font-size:34px;line-height:1.15;margin:8px 0 18px;max-width:1120px}
:root[data-theme="dark"] h2{color:#CFE0F5}@media (prefers-color-scheme:dark){:root:not([data-theme="light"]) h2{color:#CFE0F5}}
h3{color:var(--teal);font-size:17px;margin:6px 0 8px}
.lead{color:var(--grey);font-size:19px;margin:-8px 0 16px}
ul{margin:0;padding-left:20px}li{margin:0 0 8px;font-size:16px;line-height:1.35}ul.big li{font-size:19px;margin-bottom:14px}
.g2{display:grid;grid-template-columns:1.25fr 1fr;gap:34px;align-items:start}
.stats{display:flex;gap:14px;margin-bottom:18px}.stats.col{flex-direction:column}.stats.g{display:grid;grid-template-columns:1fr 1fr}
.stat{background:var(--light);padding:14px 16px;flex:1;border-radius:8px;border-left:4px solid var(--teal)}
.stat b{display:block;font-size:28px;color:var(--navy)}.stat.xl b{font-size:38px}.stat span{color:var(--grey);font-size:14px}
:root[data-theme="dark"] .stat b{color:#CFE0F5}@media (prefers-color-scheme:dark){:root:not([data-theme="light"]) .stat b{color:#CFE0F5}}
.stat.inv{background:var(--navy);border-left-color:var(--amber)}.stat.inv b{color:#fff}.stat.inv span{color:#B8C7D9}
.foot{position:absolute;left:58px;right:58px;bottom:34px;color:var(--grey);font-size:12px;font-style:italic;margin:0}
.pg{position:absolute;left:58px;right:58px;bottom:12px;color:var(--grey);font-size:11px;display:flex;justify-content:space-between}
.notes{display:none}
.title{background:var(--navy)!important;color:#fff;padding:120px 90px}.title::before{display:none}
.title .bar{position:absolute;left:62px;top:205px;width:10px;height:180px;background:var(--teal)}
.title h1{font-size:96px;margin:10px 0 0;color:#fff}.title .tag{font-size:34px;margin:6px 0}.title .sub{font-size:21px;color:#B8C7D9}
.title .names{position:absolute;bottom:52px;color:#B8C7D9;font-size:15px}.title .kick{color:var(--amber)}
blockquote{background:var(--navy);color:#fff;margin:0;padding:30px;border-radius:8px;font-size:25px;font-weight:700;font-style:italic;line-height:1.3}
blockquote cite{display:block;margin-top:18px;color:var(--amber);font-size:15px;font-style:normal;font-weight:400}
.pt{display:flex;gap:14px;align-items:center;margin-bottom:14px}.pt b{background:var(--navy);color:#fff;min-width:130px;text-align:center;padding:20px 8px;border-radius:6px;font-size:18px}.pt i{font-size:17px}
.land{position:absolute;left:58px;right:58px;bottom:62px;background:var(--teal);color:#fff;font-weight:700;font-size:21px;padding:14px 22px;border-radius:8px;text-align:center}
.chev{display:flex;gap:4px;margin-top:6px}.chev span{flex:1;background:var(--navy);color:#fff;text-align:center;padding:14px 6px;font-weight:700;clip-path:polygon(0 0,88% 0,100% 50%,88% 100%,0 100%,12% 50%)}
.chev span.hl,.step.hl{background:var(--teal)}.step.warn{background:var(--amber)}
.rec{background:var(--amber);color:#fff;text-align:center;font-weight:700;padding:8px;margin:8px 0 16px;border-radius:4px}
.cards{display:grid;grid-template-columns:repeat(3,1fr);gap:12px}.card{background:var(--light);padding:14px 16px;border-radius:8px;border-top:4px solid var(--teal)}
.card small{display:block;color:var(--teal);font-weight:700}.card b{display:block;font-size:20px;margin:4px 0;color:var(--navy)}.card span{color:var(--grey);font-size:14px}
:root[data-theme="dark"] .card b{color:#CFE0F5}@media (prefers-color-scheme:dark){:root:not([data-theme="light"]) .card b{color:#CFE0F5}}
.cards.three .card{min-height:200px}.cards.three .card span{color:var(--ink);font-size:15px;display:block;margin-top:8px}
.flow{display:grid;grid-template-columns:repeat(7,1fr);gap:8px}.step{background:var(--navy);color:#fff;border-radius:8px;padding:14px 12px;min-height:300px}
.step b{display:block;font-size:17px;margin-bottom:10px}.step span{font-size:14px;line-height:1.35}
.chart{width:100%;height:auto;background:var(--light);border-radius:8px}.chart .ct{fill:var(--grey);font-size:14px;font-weight:700}
.chart .ln{fill:none;stroke:var(--teal);stroke-width:4;stroke-dasharray:900;stroke-dashoffset:900;transition:stroke-dashoffset 1.4s ease .4s}.on .chart .ln{stroke-dashoffset:0}
.chart .dot{fill:var(--teal)}.chart .lbl{fill:var(--ink);font-size:13px;text-anchor:middle;font-weight:700}.chart .lbl.s{font-size:11px}.chart .ax{fill:var(--grey);font-size:13px;text-anchor:middle}
.chart .gate{stroke:var(--amber);stroke-dasharray:6 5;stroke-width:2}.chart .gl{fill:var(--amber);font-size:12px;text-anchor:end}
.chart .rv{fill:var(--navy)}.chart .eb.neg{fill:#C0392B}.chart .eb.pos{fill:var(--teal)}.chart .zero{stroke:var(--line)}
:root[data-theme="dark"] .chart .rv{fill:#6E95C9}@media (prefers-color-scheme:dark){:root:not([data-theme="light"]) .chart .rv{fill:#6E95C9}}
.callout{background:var(--navy);color:#fff;padding:22px;border-radius:8px;font-size:20px;font-weight:700}
.honest{margin-top:14px;border:2px solid var(--amber);padding:14px;border-radius:8px;font-size:16px}
.wheel{position:relative;height:440px}.wheel span{position:absolute;left:50%;top:50%;width:160px;margin:-28px 0 0 -80px;background:var(--navy);color:#fff;border-radius:10px;padding:10px;text-align:center;font-size:13px;font-weight:700;
transform:rotate(calc(var(--i)*51.43deg)) translateY(-185px) rotate(calc(var(--i)*-51.43deg))}
.on .wheel span{transform:rotate(calc(var(--i)*51.43deg)) translateY(-185px) rotate(calc(var(--i)*-51.43deg))}
.wheel em{position:absolute;left:50%;top:50%;width:170px;height:90px;margin:-45px 0 0 -85px;background:var(--teal);color:#fff;border-radius:50%;display:flex;align-items:center;justify-content:center;text-align:center;font-style:normal;font-weight:700;font-size:14px;padding:10px}
.muted,.muted li{color:var(--grey)}
.tiles{display:grid;grid-template-columns:1fr 1fr;gap:18px}.tile{background:var(--light);border-left:8px solid var(--teal);padding:26px;border-radius:8px;min-height:190px}
.tile b{display:block;font-size:36px;color:var(--navy);margin-bottom:12px}.tile span{font-size:19px}
:root[data-theme="dark"] .tile b{color:#CFE0F5}@media (prefers-color-scheme:dark){:root:not([data-theme="light"]) .tile b{color:#CFE0F5}}
.funnel .f{width:var(--w);margin:0 auto 10px;background:var(--navy);color:#fff;text-align:center;padding:12px;border-radius:6px}.funnel .f:nth-child(2){background:#2A4F7A}.funnel .f:nth-child(3){background:var(--teal)}.funnel .f:nth-child(4){background:var(--amber)}
.funnel b{display:block;font-size:28px}.funnel span{font-size:13px}
.map{position:relative;height:430px;background:var(--light);border-radius:8px;margin:0 14px 24px}.map .q{position:absolute;right:0;top:0;width:50%;height:50%;background:rgba(14,140,127,.14);border-radius:0 8px 0 0}
.map i{position:absolute;width:14px;height:14px;margin:0 0 -7px -7px;border-radius:50%;background:var(--navy)}.map i u{position:absolute;left:18px;top:-3px;white-space:nowrap;text-decoration:none;font-size:13px;font-style:normal}
.map i.me{width:26px;height:26px;margin:0 0 -13px -13px;background:var(--teal);box-shadow:0 0 0 8px rgba(14,140,127,.25)}.map i.me u{font-weight:800;color:var(--teal);font-size:17px;left:-100px;top:30px}
.map small{position:absolute;font-size:12px;color:var(--grey)}.map .xl{left:0;bottom:-20px}.map .xr{right:0;bottom:-20px}.map .yt{left:8px;top:6px}.map .yb{left:8px;bottom:6px}
table{border-collapse:collapse;width:100%;font-size:15px}th{background:var(--navy);color:#fff;text-align:left;padding:9px 10px}td{padding:9px 10px;border-bottom:1px solid var(--line)}
tr:nth-child(even) td{background:var(--light)}table.apx{font-size:15px}
.ladder div{display:flex;gap:14px;align-items:center;margin-bottom:10px}.ladder b{background:var(--navy);color:#fff;min-width:96px;text-align:center;padding:12px 6px;border-radius:6px}.ladder span{font-size:16px}
.cmp{background:var(--teal);color:#fff;border-radius:8px;padding:18px;display:flex;gap:18px;align-items:center;margin-bottom:14px}.cmp b{font-size:52px}.cmp span{font-size:16px}
.agn{color:var(--teal);font-weight:700;margin:0 0 8px}
.chips{display:flex;gap:8px;flex-wrap:wrap}.chips span{background:var(--navy);color:#fff;padding:12px 14px;border-radius:6px;font-weight:700;font-size:13px}.chips span.hl{background:var(--amber)}
.tiers{display:grid;grid-template-columns:repeat(3,1fr);gap:14px;margin-bottom:24px}.tiers div{padding:20px;border-radius:8px;color:#fff}.tiers .t0{background:var(--teal)}.tiers .t1{background:var(--navy)}.tiers .t2{background:var(--amber)}
.tiers b{display:block;font-size:22px;margin-bottom:6px}
.u{display:grid;grid-template-columns:230px 1fr 50px;align-items:center;gap:10px;margin-bottom:9px;font-size:15px}.u i{display:block;height:20px;width:var(--p);background:var(--teal);border-radius:3px}
#hud{position:fixed;right:14px;bottom:10px;font:12px Arial;color:var(--grey);display:flex;gap:10px;align-items:center;z-index:5}
#hud button{background:var(--card);border:1px solid var(--line);color:var(--ink);border-radius:6px;padding:6px 10px;cursor:pointer}
#prog{position:fixed;left:0;top:0;height:4px;background:var(--amber);z-index:6;transition:width .3s}
#np{position:fixed;left:16px;right:16px;bottom:46px;background:var(--card);border:1px solid var(--line);padding:12px;border-radius:8px;font-size:14px;display:none;z-index:6}
@media print{html,body{overflow:visible;background:#fff}#stage{position:static;transform:none!important;width:auto;height:auto}
.slide{position:relative;opacity:1!important;page-break-after:always;width:1280px;height:720px;box-shadow:none;border-radius:0}.a,.grow{opacity:1!important;transform:none!important}#hud,#prog,#np{display:none}}
"""
JS = r"""
const S=[...document.querySelectorAll('.slide')];let i=0;const st=document.getElementById('stage');
function fit(){const s=Math.min(innerWidth/1300,innerHeight/740);st.style.transform=`translate(-50%,-50%) scale(${s})`}
function go(n){i=Math.max(0,Math.min(S.length-1,n));S.forEach((s,k)=>s.classList.toggle('on',k===i));document.getElementById('ct').textContent=(i+1)+' / '+S.length;
document.getElementById('prog').style.width=((i+1)/S.length*100)+'%';const nt=S[i].querySelector('.notes');document.getElementById('np').textContent=nt?nt.textContent:'(no notes)';
try{history.replaceState(null,'','#'+(i+1))}catch(e){}}
addEventListener('keydown',e=>{if(['ArrowRight','PageDown',' ','Enter'].includes(e.key)){e.preventDefault();go(i+1)}if(['ArrowLeft','PageUp','Backspace'].includes(e.key)){e.preventDefault();go(i-1)}
if(e.key==='Home')go(0);if(e.key==='End')go(S.length-1);if(e.key==='n'){const p=document.getElementById('np');p.style.display=p.style.display==='block'?'none':'block'}});
let x0=null;addEventListener('touchstart',e=>x0=e.touches[0].clientX);addEventListener('touchend',e=>{if(x0===null)return;const dx=e.changedTouches[0].clientX-x0;if(Math.abs(dx)>40)go(i+(dx<0?1:-1));x0=null});
document.getElementById('nx').onclick=()=>go(i+1);document.getElementById('pv').onclick=()=>go(i-1);
document.getElementById('th').onclick=()=>{const r=document.documentElement;r.dataset.theme=(r.dataset.theme==='dark')?'light':'dark'};
document.getElementById('nb').onclick=()=>{const p=document.getElementById('np');p.style.display=p.style.display==='block'?'none':'block'};
addEventListener('resize',fit);fit();go((parseInt(location.hash.slice(1))||1)-1);
"""
doc = f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Keepwell Seed Deck</title><style>{CSS}</style></head><body><div id="prog"></div><div id="stage">{''.join(parts)}</div>
<div id="np"></div><div id="hud"><button id="pv" aria-label="Previous">‹</button><span id="ct"></span><button id="nx" aria-label="Next">›</button><button id="nb">Notes (N)</button><button id="th">Theme</button></div>
<script>{JS}</script></body></html>"""
html_path = os.path.join(OUT, "Keepwell_Seed_Deck.html")
open(html_path, "w").write(doc)
print("saved", html_path, total, "slides")
