"""Render the Keepwell seed deck (v4, 12 slides) from deck_content.py → Keepwell_Seed_Deck.pptx + .html (PDF via LibreOffice).
    <venv>/bin/python build_deck.py
"""
import sys, html, pathlib
HERE = pathlib.Path(__file__).parent; sys.path.insert(0, str(HERE))
from deck_content import SLIDES
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
    text(sl, 0.6, 7.08, 8, 0.3, "Keepwell · Seed round 2026 · Confidential", size=9, color=GREY)
    if d.get("notes"): sl.notes_slide.notes_text_frame.text = d["notes"]
def foot(sl, t): text(sl, 0.6, 6.7, 12.1, 0.35, t, size=9, color=GREY, italic=True)
def tile(sl, x, y, w, h, v, l, fill=LIGHT, vc=NAVY, vs=26, lc=GREY):
    box(sl, x, y, w, h, fill=fill); text(sl, x + 0.15, y + 0.1, w - 0.3, h * 0.5, v, size=vs, bold=True, color=vc)
    text(sl, x + 0.15, y + h * 0.5, w - 0.3, h * 0.5, l, size=11, color=lc)
def landbar(sl, t, y=6.0):
    box(sl, 0.6, y, 12.1, 0.58, fill=TEAL); text(sl, 0.8, y, 11.7, 0.58, t, size=15, bold=True, color=WHITE, anchor=MSO_ANCHOR.MIDDLE)


SOFT = RGBColor(0xF6, 0xF8, 0xFA); C3 = [TEAL, AMBER, RGBColor(0x26, 0x37, 0x5A)]
def result(sl, t, y=6.2):
    text(sl, 0.6, y, 12.1, 0.55, t, size=13, bold=True, color=NAVY)
def r_title(sl, d, n):
    box(sl, 0, 0, W, 0.08, fill=TEAL)
    box(sl, 0.6, 0.7, 0.62, 0.62, fill=TEAL, shape=MSO_SHAPE.ROUNDED_RECTANGLE); text(sl, 1.35, 0.72, 4, 0.6, "keepwell", size=26, bold=True, color=NAVY, anchor=MSO_ANCHOR.MIDDLE)
    text(sl, 0.6, 1.9, 12, 1.4, d["headline"], size=40, bold=True, color=NAVY)
    text(sl, 0.6, 3.25, 12, 0.6, d["tagline"], size=20, color=GREY)
    for i, (ini, nm, role) in enumerate(d["people"]):
        x = 0.6 + i * 4.1; box(sl, x, 4.4, 3.9, 1.2, fill=SOFT, shape=MSO_SHAPE.ROUNDED_RECTANGLE)
        box(sl, x + 0.18, 4.65, 0.7, 0.7, fill=C3[i], shape=MSO_SHAPE.OVAL); text(sl, x + 0.18, 4.65, 0.7, 0.7, ini, size=15, bold=True, color=WHITE, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
        text(sl, x + 1.0, 4.52, 2.8, 0.4, nm, size=14, bold=True, color=NAVY); text(sl, x + 1.0, 4.9, 2.8, 0.7, role, size=10, color=GREY)
    text(sl, 0.6, 6.85, 8, 0.35, d["foot"], size=11, color=GREY)
    sl.notes_slide.notes_text_frame.text = d["notes"]
def r_cards(sl, d, n):
    frame(sl, d, n)
    for i, (h, a, b) in enumerate(d["cards"]):
        x = 0.6 + i * 4.1; box(sl, x, 1.75, 3.9, 3.6, fill=WHITE, line=RGBColor(0xDD, 0xE3, 0xEA)); box(sl, x, 1.75, 3.9, 0.08, fill=C3[i])
        text(sl, x + 0.2, 1.95, 3.5, 0.6, h, size=24, bold=True, color=C3[i]); text(sl, x + 0.2, 2.7, 3.5, 1.0, a, size=14, bold=True, color=INK); text(sl, x + 0.2, 3.65, 3.5, 1.6, b, size=12, color=GREY)
    result(sl, d["result"], 5.6); foot(sl, d["foot"])
def r_answer(sl, d, n):
    frame(sl, d, n)
    box(sl, 0.6, 1.6, 12.1, 1.05, fill=NAVY); box(sl, 0.6, 1.6, 0.1, 1.05, fill=AMBER)
    text(sl, 0.85, 1.66, 11.7, 0.3, "OUR VISION", size=10, bold=True, color=AMBER); text(sl, 0.85, 1.93, 11.7, 0.7, d["vision"], size=14, bold=True, color=WHITE)
    for i, (k, h, b) in enumerate(d["steps"]):
        x = 0.6 + i * 4.1; box(sl, x, 2.95, 3.9, 2.55, fill=WHITE, line=RGBColor(0xDD, 0xE3, 0xEA)); box(sl, x, 2.95, 0.08, 2.55, fill=C3[i])
        text(sl, x + 0.25, 3.1, 3.5, 0.3, k.upper(), size=10, bold=True, color=C3[i]); text(sl, x + 0.25, 3.45, 3.5, 0.5, h, size=20, bold=True, color=NAVY); text(sl, x + 0.25, 4.0, 3.5, 1.5, b, size=12, color=INK)
        if i < 2: box(sl, x + 3.93, 4.1, 0.14, 0.2, fill=GREY, shape=MSO_SHAPE.RIGHT_ARROW)
    result(sl, d["land"], 5.75)
def r_lifecycle(sl, d, n):
    frame(sl, d, n)
    col = {"serve": TEAL, "supply": AMBER, "circ": RGBColor(0x26, 0x37, 0x5A)}
    W5, H5, X0, Y0, GX = 2.3, 1.22, 0.6, 1.6, 0.15
    pos = {0: (0, 0), 1: (1, 0), 2: (2, 0), 3: (3, 0), 4: (4, 0), 5: (4, 1), 6: (3, 1), 7: (4, 2), 8: (3, 2), 9: (2, 2)}
    def xy(i): c, r = pos[i]; return X0 + c * (W5 + GX), Y0 + r * (H5 + 0.42)
    for i, (h, b, k) in enumerate(d["stages"]):
        x, y = xy(i); box(sl, x, y, W5, H5, fill=WHITE, line=col[k]); box(sl, x, y, W5, 0.07, fill=col[k])
        text(sl, x + 0.08, y + 0.1, W5 - 0.16, 0.32, h, size=12, bold=True, color=NAVY)
        text(sl, x + 0.08, y + 0.42, W5 - 0.16, 0.78, b, size=9.5, color=INK)
    def arrow(x, y, w, h, shape, fill=GREY):
        s_ = box(sl, x, y, w, h, fill=fill, shape=shape); return s_
    for i in range(4):
        x, y = xy(i); arrow(x + W5 + 0.01, y + H5 / 2 - 0.08, GX - 0.02, 0.16, MSO_SHAPE.RIGHT_ARROW)
    x4, y4 = xy(4); box(sl, x4 + 0.35, y4 + H5 + 0.04, W5 - 0.7, 0.34, fill=NAVY, shape=MSO_SHAPE.ROUNDED_RECTANGLE)
    text(sl, x4 + 0.35, y4 + H5 + 0.04, W5 - 0.7, 0.34, "Worth repairing?", size=10, bold=True, color=WHITE, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    x5, y5 = xy(5); arrow(x5 - GX + 0.01, y5 + H5 / 2 - 0.08, GX - 0.02, 0.16, MSO_SHAPE.LEFT_ARROW, TEAL)
    x6, y6 = xy(6); arrow(x6 + W5 / 2 - 0.08, y6 - 0.42, 0.16, 0.4, MSO_SHAPE.UP_ARROW, TEAL)
    text(sl, x6 + W5 / 2 + 0.1, y6 - 0.4, 2.2, 0.35, "fixed → back in use", size=9, bold=True, color=TEAL)
    text(sl, x4 + 0.0, y4 + H5 + 0.04, 0.35, 0.34, "yes ↓", size=9, bold=True, color=TEAL)
    x7, y7 = xy(7); arrow(x5 + W5 + 0.04, y4 + H5 + 0.2, 0.14, y7 + 0.3 - (y4 + H5 + 0.2), MSO_SHAPE.DOWN_ARROW, RED)
    text(sl, x5 + W5 - 0.45, y7 - 0.36, 0.45, 0.3, "no", size=9, bold=True, color=RED)
    for i in (7, 8):
        x, y = xy(i); arrow(x - GX + 0.01, y + H5 / 2 - 0.08, GX - 0.02, 0.16, MSO_SHAPE.LEFT_ARROW)
    text(sl, X0, Y0 + H5 + 0.5, 2 * W5 + GX, 1.2, ["SERVE · now   SUPPLY · from year 2   CIRCULATE · from year 3", "Repairable → parts → repaired → back in use.", "Not worth repairing → trade-in → refurbished (sold again) or recycled."], size=10, color=GREY)
    box(sl, X0, 6.2, 12.1, 0.42, fill=NAVY); text(sl, X0 + 0.15, 6.2, 11.8, 0.42, d["spine"], size=11, bold=True, color=WHITE, anchor=MSO_ANCHOR.MIDDLE)


def r_traction(sl, d, n):
    frame(sl, d, n)
    for i, (v, l) in enumerate(d["tiles"]):
        x = 0.6 + (i % 3) * 2.75; y = 1.65 + (i // 3) * 1.7; box(sl, x, y, 2.6, 1.55, fill=SOFT); box(sl, x, y, 0.07, 1.55, fill=[TEAL, AMBER, NAVY, TEAL, AMBER, NAVY][i])
        text(sl, x + 0.2, y + 0.1, 2.3, 0.6, v, size=26, bold=True, color=NAVY); text(sl, x + 0.2, y + 0.75, 2.3, 0.8, l, size=10.5, color=GREY)
    c = d["chart"]; cd = CategoryChartData(); cd.categories = c["months"]; cd.add_series("Contribution (₹ L)", c["contribution"]); cd.add_series("Cluster team (₹ L)", [c["team"]] * len(c["months"]))
    gf = sl.shapes.add_chart(XL_CHART_TYPE.COLUMN_CLUSTERED, Inches(8.95), Inches(1.65), Inches(3.75), Inches(3.25), cd); ch = gf.chart
    ch.has_title = True; ch.chart_title.text_frame.text = "Monthly contribution vs team cost (₹ L)"; ch.chart_title.text_frame.paragraphs[0].runs[0].font.size = Pt(10)
    ch.has_legend = True; ch.legend.position = XL_LEGEND_POSITION.BOTTOM; ch.legend.include_in_layout = False; ch.legend.font.size = Pt(9)
    s0, s1 = ch.series; s0.format.fill.solid(); s0.format.fill.fore_color.rgb = TEAL; s1.format.fill.solid(); s1.format.fill.fore_color.rgb = RGBColor(0xC9, 0xD1, 0xDB)
    ch.value_axis.has_major_gridlines = False; ch.value_axis.tick_labels.font.size = Pt(9); ch.category_axis.tick_labels.font.size = Pt(9)
    result(sl, d["result"], 5.25)
def r_chain(sl, d, n):
    frame(sl, d, n)
    for i, (h, v, l, s) in enumerate(d["chain"]):
        x = 0.6 + i * 3.08; box(sl, x, 1.8, 2.85, 3.0, fill=NAVY if i == 3 else SOFT)
        c1 = WHITE if i == 3 else NAVY
        text(sl, x + 0.2, 1.95, 2.5, 0.35, h.upper(), size=10, bold=True, color=AMBER if i == 3 else TEAL); text(sl, x + 0.2, 2.35, 2.5, 0.7, v, size=30, bold=True, color=c1)
        text(sl, x + 0.2, 3.1, 2.5, 0.5, l, size=12, color=PALE if i == 3 else GREY); text(sl, x + 0.2, 3.75, 2.5, 0.9, s, size=12, bold=True, color=WHITE if i == 3 else INK)
        if i < 3: box(sl, x + 2.87, 3.15, 0.19, 0.25, fill=GREY, shape=MSO_SHAPE.RIGHT_ARROW)
    landbar(sl, d["result"], 5.3)
def r_bridge(sl, d, n):
    frame(sl, d, n); y = 1.62; rh = 0.56
    for i, (op, v, lab, sub) in enumerate(d["rows"]):
        tot = op == "="; last = i == len(d["rows"]) - 1
        box(sl, 0.6, y, 7.5, rh - 0.06, fill=NAVY if last else (TEALBG if tot else SOFT))
        text(sl, 0.65, y, 0.4, rh - 0.06, op, size=20, bold=True, color=WHITE if last else (TEAL if tot else GREY), anchor=MSO_ANCHOR.MIDDLE, align=PP_ALIGN.CENTER)
        text(sl, 1.05, y, 1.6, rh - 0.06, v, size=18, bold=True, color=WHITE if last else NAVY, anchor=MSO_ANCHOR.MIDDLE, align=PP_ALIGN.RIGHT)
        text(sl, 2.75, y + 0.02, 5.3, 0.27, lab, size=11.5, bold=True, color=WHITE if last else INK)
        text(sl, 2.75, y + 0.25, 5.3, 0.25, sub, size=9.5, color=PALE if last else GREY)
        y += rh
    c = d["chart"]; cd = CategoryChartData(); cd.categories = [f"{m}\n{r}" for m, r in zip(c["months"], c["retailers"])]
    cd.add_series("Contribution (₹ L)", c["contribution"]); cd.add_series("Cluster team (₹ L)", [c["team"]] * len(c["months"]))
    gf = sl.shapes.add_chart(XL_CHART_TYPE.COLUMN_CLUSTERED, Inches(8.35), Inches(1.6), Inches(4.4), Inches(3.75), cd); ch = gf.chart
    ch.has_title = True; ch.chart_title.text_frame.text = "What the cluster kept each month vs its ₹1.0 L team cost (under each month: active retailers)"; ch.chart_title.text_frame.paragraphs[0].runs[0].font.size = Pt(10)
    ch.has_legend = True; ch.legend.position = XL_LEGEND_POSITION.BOTTOM; ch.legend.include_in_layout = False; ch.legend.font.size = Pt(9)
    s0, s1 = ch.series; s0.format.fill.solid(); s0.format.fill.fore_color.rgb = TEAL; s1.format.fill.solid(); s1.format.fill.fore_color.rgb = RGBColor(0xC9, 0xD1, 0xDB)
    s0.data_labels.show_value = True; s0.data_labels.font.size = Pt(8); s0.data_labels.number_format = '"₹"0.00" L"'; s0.data_labels.number_format_is_linked = False
    ch.value_axis.has_major_gridlines = False; ch.value_axis.tick_labels.font.size = Pt(9); ch.category_axis.tick_labels.font.size = Pt(8)
    text(sl, 8.4, 5.4, 4.3, 0.3, "Mar–Apr kept less than the team cost: loss months (−₹39k, −₹24k). Profit from May, at 20 retailers.", size=10, bold=True, color=TEAL)
    landbar(sl, d["result"], 5.85)
def r_retailer(sl, d, n):
    frame(sl, d, n)
    # strip: the 12 jobs behind ₹19,500
    cw = 1.62
    for i, (cnt, what, price, sub) in enumerate(d["jobs"]):
        x = 0.6 + i * (cw + 0.06); box(sl, x, 1.5, cw, 0.92, fill=SOFT)
        text(sl, x + 0.06, 1.52, cw - 0.1, 0.32, f"{cnt} {what}", size=10, bold=True, color=NAVY)
        text(sl, x + 0.06, 1.8, cw - 0.1, 0.3, price, size=12, bold=True, color=TEAL); text(sl, x + 0.06, 2.08, cw - 0.1, 0.3, sub, size=8.5, color=GREY)
    jt = d["jobs_total"]; x = 0.6 + 6 * (cw + 0.06); box(sl, x, 1.5, 12.7 - x, 0.92, fill=NAVY)
    text(sl, x + 0.08, 1.52, 12.6 - x, 0.3, "= " + jt[0], size=10, bold=True, color=PALE); text(sl, x + 0.08, 1.78, 12.6 - x, 0.36, jt[1], size=17, bold=True, color=WHITE)
    text(sl, x + 0.08, 2.1, 12.6 - x, 0.3, jt[2], size=9, bold=True, color=AMBER)
    for i, (h, rows) in enumerate(d["panels"]):
        x = 0.6 + i * 4.1; wpn = 3.9; box(sl, x, 2.55, wpn, 0.36, fill=NAVY if i == 2 else TEAL)
        text(sl, x + 0.12, 2.55, wpn - 0.2, 0.36, h.upper(), size=10, bold=True, color=WHITE, anchor=MSO_ANCHOR.MIDDLE)
        y = 2.95
        for k, (lab, v, kind) in enumerate(rows):
            hgt = 0.45; fill = TEALBG if kind == "total" else SOFT
            if i == 2 and kind == "total" and k == len(rows) - 1: fill = NAVY
            box(sl, x, y, wpn, hgt - 0.04, fill=fill); dark = fill == NAVY
            col = WHITE if dark else (RED if kind == "minus" else (TEAL if kind in ("plus", "total") else NAVY))
            text(sl, x + 0.1, y, 2.6, hgt - 0.04, lab, size=9, bold=kind == "total", color=WHITE if dark else INK, anchor=MSO_ANCHOR.MIDDLE)
            text(sl, x + 2.65, y, 1.17, hgt - 0.04, v, size=13 if kind == "total" else 12, bold=True, color=col, anchor=MSO_ANCHOR.MIDDLE, align=PP_ALIGN.RIGHT)
            y += hgt
        if i < 2: box(sl, x + wpn + 0.03, 4.1, 0.14, 0.25, fill=GREY, shape=MSO_SHAPE.RIGHT_ARROW)
    landbar(sl, d["result"], 5.75); foot(sl, d["foot"])
def r_cols3(sl, d, n):
    frame(sl, d, n)
    for i, (h, sub, items) in enumerate(d["cols"]):
        x = 0.6 + i * 4.1; box(sl, x, 1.65, 3.9, 4.0, fill=WHITE, line=RGBColor(0xDD, 0xE3, 0xEA)); box(sl, x, 1.65, 3.9, 0.08, fill=C3[i])
        text(sl, x + 0.2, 1.82, 3.5, 0.35, h.upper(), size=11, bold=True, color=C3[i]); text(sl, x + 0.2, 2.15, 3.5, 0.4, sub, size=12, bold=True, color=NAVY)
        bullets(sl, x + 0.2, 2.65, 3.55, 3.0, items, size=11, gap=5)
    result(sl, d["result"], 5.85)
def r_finplan(sl, d, n):
    frame(sl, d, n)
    hdr = ["", *d["years"]]; rows = [("Retailers (end of year)", d["retailers"]), ("Clusters", d["clusters"]), ("Revenue (₹ Cr)", [f"{v:.1f}" for v in d["revenue"]]),
                                    ("EBITDA (₹ Cr)", [f"+{v:.2f}" if v < 1 else f"+{v:.1f}" for v in d["ebitda"]]), ("EBITDA margin", d["margin"])]
    cw = [2.35] + [1.07] * 5
    for j, h in enumerate(hdr):
        x = 0.6 + sum(cw[:j]); box(sl, x, 1.65, cw[j] - 0.04, 0.4, fill=NAVY); text(sl, x + 0.08, 1.65, cw[j] - 0.15, 0.4, h, size=11, bold=True, color=WHITE, anchor=MSO_ANCHOR.MIDDLE, align=PP_ALIGN.LEFT if j == 0 else PP_ALIGN.RIGHT)
    for i, (lab, vals) in enumerate(rows):
        y = 2.09 + i * 0.47; hl = lab.startswith("EBITDA")
        for j, v in enumerate([lab, *vals]):
            x = 0.6 + sum(cw[:j]); box(sl, x, y, cw[j] - 0.04, 0.43, fill=TEALBG if hl else SOFT)
            text(sl, x + 0.08, y, cw[j] - 0.15, 0.43, v, size=11.5, bold=(j == 0 or hl), color=TEAL if (hl and j) else INK, anchor=MSO_ANCHOR.MIDDLE, align=PP_ALIGN.LEFT if j == 0 else PP_ALIGN.RIGHT)
    cd = CategoryChartData(); cd.categories = d["years"]; cd.add_series("Revenue (₹ Cr)", d["revenue"]); cd.add_series("EBITDA (₹ Cr)", d["ebitda"])
    gf = sl.shapes.add_chart(XL_CHART_TYPE.COLUMN_CLUSTERED, Inches(8.5), Inches(1.6), Inches(4.2), Inches(2.9), cd); ch = gf.chart
    ch.has_title = False; ch.has_legend = True; ch.legend.position = XL_LEGEND_POSITION.BOTTOM; ch.legend.include_in_layout = False; ch.legend.font.size = Pt(9)
    for s_, c in zip(ch.series, (NAVY, TEAL)): s_.format.fill.solid(); s_.format.fill.fore_color.rgb = c
    ch.value_axis.has_major_gridlines = False; ch.value_axis.tick_labels.font.size = Pt(9); ch.category_axis.tick_labels.font.size = Pt(9)
    landbar(sl, d["result"], 4.75); foot(sl, d["foot"])
def r_market(sl, d, n):
    frame(sl, d, n)
    for i, (v, l) in enumerate(d["tiles"]):
        x = 0.6 + (i % 3) * 4.1; y = 1.7 + (i // 3) * 1.65; box(sl, x, y, 3.9, 1.5, fill=SOFT); box(sl, x, y, 0.07, 1.5, fill=[NAVY, NAVY, TEAL, TEAL, AMBER, AMBER][i])
        text(sl, x + 0.22, y + 0.12, 3.5, 0.6, v, size=26, bold=True, color=NAVY); text(sl, x + 0.22, y + 0.8, 3.5, 0.6, l, size=12, color=GREY)
    result(sl, d["result"], 5.15); foot(sl, d["foot"])
def r_matrix(sl, d, n):
    frame(sl, d, n); cols = ["", *d["cols"]]; cw = [2.5] + [1.6] * 6
    for j, h in enumerate(cols):
        x = 0.6 + sum(cw[:j]); box(sl, x, 1.6, cw[j] - 0.04, 0.6, fill=NAVY); text(sl, x + 0.06, 1.6, cw[j] - 0.12, 0.6, h, size=9.5, bold=True, color=WHITE, anchor=MSO_ANCHOR.MIDDLE, align=PP_ALIGN.CENTER if j else PP_ALIGN.LEFT)
    for i, (nm, vals) in enumerate(d["rows"]):
        y = 2.24 + i * 0.46; us = i == 0
        for j, v in enumerate([nm, *vals]):
            x = 0.6 + sum(cw[:j]); box(sl, x, y, cw[j] - 0.04, 0.42, fill=TEALBG if us else SOFT)
            col = TEAL if v == "✓" else (AMBER if v == "Part" else (GREY if v == "−" else NAVY))
            text(sl, x + 0.06, y, cw[j] - 0.12, 0.42, v, size=11 if j else 11, bold=(j == 0 or v == "✓"), color=col, anchor=MSO_ANCHOR.MIDDLE, align=PP_ALIGN.CENTER if j else PP_ALIGN.LEFT)
    result(sl, d["result"], 5.6); foot(sl, d["foot"])
def r_team(sl, d, n):
    frame(sl, d, n)
    for i, (nm, role, bg, net) in enumerate(d["people"]):
        x = 0.6 + i * 4.1; box(sl, x, 1.7, 3.9, 3.0, fill=SOFT)
        box(sl, x + 0.2, 1.9, 0.8, 0.8, fill=C3[i], shape=MSO_SHAPE.OVAL); text(sl, x + 0.2, 1.9, 0.8, 0.8, "".join(w[0] for w in nm.split()[:2]), size=16, bold=True, color=WHITE, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
        text(sl, x + 1.15, 1.92, 2.7, 0.4, nm, size=15, bold=True, color=NAVY); text(sl, x + 1.15, 2.3, 2.7, 0.35, role, size=12, bold=True, color=C3[i])
        text(sl, x + 0.2, 2.9, 3.5, 0.5, net, size=20, bold=True, color=AMBER); text(sl, x + 0.2, 3.45, 3.5, 1.2, bg, size=11, color=INK)
    text(sl, 0.6, 4.9, 12.1, 0.6, d["advisors"], size=11, color=GREY); landbar(sl, d["result"], 5.65)
def r_ask(sl, d, n):
    box(sl, 0, 0, W, 7.5, fill=RGBColor(0x14, 0x4E, 0x7A)); text(sl, 0.6, 0.32, 12, 0.35, d["kicker"].upper(), size=11, bold=True, color=AMBER)
    text(sl, 0.6, 0.62, 12, 0.8, d["headline"], size=30, bold=True, color=WHITE)
    t = d["table"]; cw = [2.3, 0.8, 1.0, 3.3, 4.7]
    for i, row in enumerate(t):
        y = 1.6 + i * 0.62 if i else 1.6
        for j, v in enumerate(row):
            x = 0.6 + sum(cw[:j]); h = 0.42 if i == 0 else 0.58; yy = 1.6 if i == 0 else 2.06 + (i - 1) * 0.62
            box(sl, x, yy, cw[j] - 0.04, h, fill=RGBColor(0x0E, 0x23, 0x40) if i == 0 else RGBColor(0x1E, 0x5E, 0x8E))
            text(sl, x + 0.07, yy, cw[j] - 0.14, h, v, size=10 if i else 10, bold=(i == 0 or j == 0), color=AMBER if i == 0 else WHITE, anchor=MSO_ANCHOR.MIDDLE)
    for i, (v, l) in enumerate(d["terms"]):
        x = 0.6 + i * 4.1; box(sl, x, 4.15, 3.9, 1.2, fill=RGBColor(0x0E, 0x23, 0x40))
        text(sl, x + 0.2, 4.2, 3.5, 0.6, v, size=26, bold=True, color=WHITE); text(sl, x + 0.2, 4.82, 3.5, 0.5, l, size=11, color=PALE)
    text(sl, 0.6, 5.6, 12.1, 0.7, d["result"], size=13, bold=True, color=WHITE)
    text(sl, 11.6, 7.08, 1.2, 0.3, str(n), size=9, color=PALE, align=PP_ALIGN.RIGHT); sl.notes_slide.notes_text_frame.text = d["notes"]
R = {k[2:]: v for k, v in globals().items() if k.startswith("r_")}
for i, d in enumerate(SLIDES, 1):
    sl = prs.slides.add_slide(BLANK); R[d["type"]](sl, d, i)
prs.save(HERE / "Keepwell_Seed_Deck.pptx"); print("saved pptx")
