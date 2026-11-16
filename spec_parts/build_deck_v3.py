"""Build KeepWell_Pitch_Deck_V3.pptx on the official Startup Buildathon template.

Template artwork (cover banner, logo header strip, Thank-you page) is rendered from the
official template PDF into images; everything KeepWell-specific is editable text and shapes.

Usage: python build_deck_v3.py <assets_dir> <out.pptx>
Requires: python-pptx. Export to PDF with LibreOffice (see export step in README of change log).
"""
import re
import sys

from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_CONNECTOR, MSO_SHAPE
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN
from pptx.oxml.ns import qn
from pptx.util import Pt

ASSETS, OUT = sys.argv[1], sys.argv[2]
FONT = "Arial"
B, R, Y, G = "4285F4", "EA4335", "FBBC04", "34A853"
INK, MUTED, LINE = "222222", "5F6368", "DADCE0"
FILL = {"B": "E8F0FE", "R": "FCE8E6", "Y": "FEF7E0", "G": "E6F4EA", "N": "F8F9FA", "W": "FFFFFF"}
COL = {"B": B, "R": R, "Y": Y, "G": G, "N": "9AA0A6", "K": INK}

prs = Presentation()
prs.slide_width, prs.slide_height = Pt(720), Pt(405)
BLANK = prs.slide_layouts[6]


def rgb(h):
    return RGBColor.from_string(h)


# ---------------------------------------------------------------- text helpers
TOKEN = re.compile(r"(\*\*.+?\*\*|\[\[.+?\]\])")


def add_runs(p, text, size, color, bold=False):
    """**bold** and [[muted small]] inline markup."""
    for part in TOKEN.split(text):
        if not part:
            continue
        r = p.add_run()
        f = r.font
        f.name, f.size, f.bold = FONT, Pt(size), bold
        f.color.rgb = rgb(color)
        if part.startswith("**"):
            r.text, f.bold = part[2:-2], True
        elif part.startswith("[["):
            r.text, f.size = part[2:-2], Pt(max(size - 1.5, 6.5))
            f.color.rgb = rgb(MUTED)
        else:
            r.text = part


def text(slide, x, y, w, h, paras, size=9, color=INK, bold=False, align=PP_ALIGN.LEFT,
         anchor=MSO_ANCHOR.TOP, space=2, line=1.08):
    """paras: str or list. Items starting with '- ' become hanging bullets."""
    tb = slide.shapes.add_textbox(Pt(x), Pt(y), Pt(w), Pt(h))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
    tf.vertical_anchor = anchor
    write(tf, paras, size, color, bold, align, space, line)
    return tb


def write(tf, paras, size, color, bold, align, space=2, line=1.08):
    if isinstance(paras, str):
        paras = [paras]
    first = True
    for item in paras:
        p = tf.paragraphs[0] if first else tf.add_paragraph()
        first = False
        p.alignment = align
        p.line_spacing = line
        p.space_after = Pt(space)
        if isinstance(item, tuple):  # (text, size, color, bold)
            t, s, c, b = item
            add_runs(p, t, s, c, b)
            continue
        if item.startswith("- "):
            pPr = p._p.get_or_add_pPr()
            pPr.set("marL", str(int(Pt(9))))
            pPr.set("indent", str(int(-Pt(9))))
            bu = pPr.makeelement(qn("a:buChar"), {"char": "•"})
            pPr.append(bu)
            add_runs(p, item[2:], size, color, bold)
        else:
            add_runs(p, item, size, color, bold)


def box(slide, x, y, w, h, fill="W", line=LINE, radius=0.06, shape=MSO_SHAPE.ROUNDED_RECTANGLE, lw=0.75):
    s = slide.shapes.add_shape(shape, Pt(x), Pt(y), Pt(w), Pt(h))
    if shape == MSO_SHAPE.ROUNDED_RECTANGLE:
        s.adjustments[0] = radius
    s.fill.solid()
    s.fill.fore_color.rgb = rgb(FILL.get(fill, fill))
    if line:
        s.line.color.rgb = rgb(line)
        s.line.width = Pt(lw)
    else:
        s.line.fill.background()
    s.shadow.inherit = False
    s.text_frame.text = ""
    return s


def card(slide, x, y, w, h, title, body, col="B", fill="N", size=8.6, tsize=10, pad=8, title_color=INK):
    box(slide, x, y, w, h, fill=fill)
    bar = box(slide, x, y + 3, 3, h - 6, fill=COL[col], line=None, shape=MSO_SHAPE.RECTANGLE)
    paras = [(title, tsize, title_color, True)] if title else []
    paras += body if isinstance(body, list) else [body]
    text(slide, x + pad + 1, y + 6, w - pad - 6, h - 9, paras, size=size)


def chip(slide, x, y, w, h, label, col="B", size=7, txt="FFFFFF"):
    s = box(slide, x, y, w, h, fill=COL[col] if col in COL else col, line=None, radius=0.5)
    tf = s.text_frame
    tf.margin_left = tf.margin_right = Pt(2)
    tf.margin_top = tf.margin_bottom = 0
    tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    write(tf, [label], size, txt, True, PP_ALIGN.CENTER)
    return s


def arrow(slide, x1, y1, x2, y2, color="80868B", w=1.25):
    c = slide.shapes.add_connector(MSO_CONNECTOR.STRAIGHT, Pt(x1), Pt(y1), Pt(x2), Pt(y2))
    c.line.color.rgb = rgb(color)
    c.line.width = Pt(w)
    ln = c.line._get_or_add_ln()
    tail = ln.makeelement(qn("a:tailEnd"), {"type": "triangle", "w": "med", "len": "med"})
    ln.append(tail)
    return c


def node(slide, x, y, w, h, title, sub, col="B", fill="W", tsize=8.2, ssize=7.2, align=PP_ALIGN.CENTER):
    s = box(slide, x, y, w, h, fill=fill, line=COL[col], lw=1)
    tf = s.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_right = Pt(3)
    tf.margin_top = tf.margin_bottom = Pt(1.5)
    tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    paras = [(title, tsize, INK, True)]
    if sub:
        paras.append((sub, ssize, "3C4043", False))
    write(tf, paras, tsize, INK, False, align, space=0.5, line=1.0)
    return s


def table(slide, x, y, w, col_w, rows, head_fill=B, size=8, head_size=8, row_h=16, zebra=True, bold_first=True):
    nrows, ncols = len(rows), len(rows[0])
    gt = slide.shapes.add_table(nrows, ncols, Pt(x), Pt(y), Pt(w), Pt(row_h * nrows)).table
    for j, cw in enumerate(col_w):
        gt.columns[j].width = Pt(cw)
    for i, row in enumerate(rows):
        gt.rows[i].height = Pt(row_h)
        for j, val in enumerate(row):
            cell = gt.cell(i, j)
            cell.margin_left = cell.margin_right = Pt(4)
            cell.margin_top = cell.margin_bottom = Pt(2)
            cell.vertical_anchor = MSO_ANCHOR.MIDDLE
            cell.fill.solid()
            if i == 0:
                cell.fill.fore_color.rgb = rgb(head_fill)
            else:
                cell.fill.fore_color.rgb = rgb("F8F9FA" if (zebra and i % 2 == 1) else "FFFFFF")
            tf = cell.text_frame
            tf.word_wrap = True
            tf.paragraphs[0].text = ""
            if i == 0:
                write(tf, [val], head_size, "FFFFFF", True, PP_ALIGN.LEFT, 0, 1.0)
            else:
                write(tf, [val], size, INK, bold_first and j == 0, PP_ALIGN.LEFT, 0, 1.0)
    # remove table style banding look
    tbl = gt._tbl
    tblPr = tbl.tblPr
    tblPr.set("firstRow", "0")
    tblPr.set("bandRow", "0")
    return gt


# ---------------------------------------------------------------- page scaffolds
def content_slide(title, subtitle):
    s = prs.slides.add_slide(BLANK)
    s.shapes.add_picture(f"{ASSETS}/header.png", 0, 0, Pt(720), Pt(62))
    text(s, 39, 70, 642, 22, [(title, 18, INK, False)])
    text(s, 39, 94, 642, 16, [(subtitle, 11, INK, False)])
    return s


def footer(s, txt):
    text(s, 39, 389, 642, 12, [(txt, 6.8, MUTED, False)])


# ================================================================ 1 COVER
s = prs.slides.add_slide(BLANK)
s.shapes.add_picture(f"{ASSETS}/cover_banner.png", 0, 0, Pt(720), Pt(243))
text(s, 53, 258, 120, 18, [("Team Name:", 14, INK, False)])
text(s, 140, 255, 560, 22, [("**KeepWell**   [[|]]   The AI repair desk and Home Memory for every appliance", 14, INK, False)])
text(s, 53, 290, 120, 18, [("Team Size:", 14, INK, False)])
text(s, 132, 290, 100, 18, [("2", 14, INK, False)])
text(s, 53, 322, 140, 18, [("Problem Statement:", 14, INK, False)])
text(s, 190, 324, 495, 70, [(
    "Independent appliance repair agencies in India's Tier 2/3 cities receive incomplete complaints through calls "
    "and WhatsApp voice notes. Without the appliance's model and repair history, technicians can arrive "
    "underprepared. That raises the risk of avoidable repeat visits, makes quotes harder to explain, and leaves "
    "households without a trustworthy service record.", 10.2, INK, False)], line=1.12)

# ================================================================ 2 PROBLEM
s = content_slide("Problem Statement", "The challenge or problem identified by the team.")
text(s, 39, 116, 642, 30, [(
    "Repair context is scattered across customer messages, paper invoices, technicians' memory and past visits, "
    "so the next repair rarely starts with a reliable picture of the machine.", 10.5, INK, True)], line=1.1)

chain = [
    ("1  Fragmented complaint", B, "B", ["- Telugu or Hindi voice note: \"fridge not cooling, come tomorrow\"",
                                          "- No model or serial number, invoice on paper",
                                          "- Last repair buried in a chat or a technician's memory"]),
    ("2  Weak preparation", Y, "Y", ["- Diagnosis guessed over the phone",
                                      "- Part chosen without a confirmed model",
                                      "- Price given verbally"]),
    ("3  Repeat visits, low trust", R, "R", ["- Higher risk of a second trip for the same fault",
                                             "- Disputes about price and what was done",
                                             "- Household can't prove warranty or history"]),
]
for i, (t, c, k, body) in enumerate(chain):
    x = 39 + i * 220
    card(s, x, 152, 200, 98, t, body, col=k, fill="N", size=8.6)
    if i < 2:
        arrow(s, x + 202, 201, x + 218, 201, color="5F6368", w=1.5)

card(s, 39, 258, 300, 74, "Who we serve first",
     ["**Owner-run independent repair agencies** with about 2–10 technicians in Tier 2/3 cities, the default "
      "choice for many households. **Households** benefit second: a clear quote, payment status and a "
      "record of each appliance."], col="G", fill="N", size=8.6)
card(s, 351, 258, 330, 74, "What the evidence does and doesn't show",
     ["Surveys show independent servicing is common and after-sales trust is weak (right). They do **not** "
      "measure repeat-visit rates, intake completeness, wrong-part arrivals or willingness to pay. "
      "**Those are the pilot's first measurements.**"], col="Y", fill="N", size=8.6)

STAT1 = ("57%", "of AC owners surveyed got or planned this year's servicing from a local or third-party provider; only 24% from the brand")
STAT1_SRC = "LocalCircles, Apr 2026, n=13,487"
STAT2 = ("55%", "of surveyed households said at least one high-value product bought in the last 5 years was defective within warranty")
STAT2_SRC = "LocalCircles, Mar 2024, n=10,641"
for i, ((k, t), src, c) in enumerate([(STAT1, STAT1_SRC, G), (STAT2, STAT2_SRC, B)]):
    x = 39 + i * 330
    text(s, x, 340, 70, 30, [(k, 20, c, True)])
    text(s, x + 58, 340, 262, 44, [t, f"[[Source: {src}. Self-reported survey, not repair records.]]"], size=8.2)

# ================================================================ 3 SOLUTION
s = content_slide("Proposed Solution", "The idea and how it addresses the identified problem.")
text(s, 39, 114, 642, 28, [(
    "KeepWell is the AI repair desk and Home Memory for appliances. It turns incomplete complaints into "
    "better-prepared visits, then turns verified repairs into a record that follows the machine.", 10.3, INK, True)],
    line=1.1)
text(s, 39, 145, 642, 12, [("**Flagship scenario (illustrative):** a Telugu-speaking customer sends a voice note: "
                            "\"The fridge isn't cooling again; it was repaired two months ago.\"", 8.4, "3C4043", False)])
steps = [
    ("1 Listen", "B", "Voice note transcribed; original audio kept as evidence", "real"),
    ("2 Identify", "R", "Fridge matched to its record (customer OK); last repair and part found", "real"),
    ("3 Ask + safety", "Y", "1–2 high-value questions; hazard rules run first", "real"),
    ("4 Prepare", "G", "Cited fault hypotheses; part verified in catalogue, or \"inspect first\"; technician + slot", "fix"),
    ("5 Approve", "B", "Agency-approved quote; customer accepts; UPI payment request", "sbx"),
    ("6 Remember", "R", "Technician findings + customer confirmation become a verified service event", "real"),
]
TAG = {"real": ("Real AI/API call in demo", "G"), "fix": ("Real logic, fixture data", "Y"), "sbx": ("Payment sandbox", "N")}
for i, (h, k, t, tag) in enumerate(steps):
    x = 39 + i * 108
    card(s, x, 161, 102, 86, h, [t], col=k, fill="N", size=7.9, tsize=9.2, pad=7)
    lab, c = TAG[tag]
    chip(s, x + 8, 236, 88, 9, lab, col=c, size=5.8, txt="FFFFFF" if c != "Y" else INK)
    if i < 5:
        arrow(s, x + 102, 204, x + 108, 204, color="9AA0A6", w=1)

rows = [["Today", "With KeepWell"],
        ["\"Fridge not cooling. Come tomorrow.\"", "Symptom and machine identity extracted; missing details asked"],
        ["Previous repair lost in a chat", "Prior repair surfaced, when the household allows it"],
        ["Part chosen by guesswork", "Catalogue-verified part, or an explicit inspect-first visit"],
        ["Verbal price, unclear payment", "Written, agency-approved quote; payment status from the gateway"],
        ["Outcome disappears", "Technician findings + customer confirmation added to Home Memory"]]
table(s, 39, 254, 412, [150, 262], rows, head_fill="5F6368", size=7.6, head_size=7.8, row_h=21.5, bold_first=False)
card(s, 462, 254, 219, 129, "North-star metric: first-visit resolution",
     ["Jobs resolved on the first on-site visit and **not reopened for the same issue within 14 days**, divided by "
      "eligible jobs whose 14-day window has ended.",
      "[[Tracked beside it: job volume, diagnostic-only visits, 30-day repeats, and each agency's pre-KeepWell baseline.]]",
      "**MVP scope:** refrigerators and ACs, Telugu + Hindi, one Tier 2 city."], col="Y", fill="N", size=8.1, tsize=9.4)

# ================================================================ 4 ARCHITECTURE
s = content_slide("Solution Architecture", "Architecture of the proposed solution")
# column labels
for x, lab in ((39, "CHANNELS"), (128, "ORCHESTRATION"), (258, "AI AGENTS (bounded, Gemini)"), (404, "VERIFIED TOOLS + RULES"), (556, "HUMAN GATES + RECORD")):
    text(s, x, 112, 140, 10, [(lab, 6.8, MUTED, True)])
# channels
for i, (t, sub) in enumerate([("Customer", "WhatsApp voice, photo, text"), ("Agency desk", "web app (PWA)"),
                              ("Technician", "mobile app"), ("Partners", "later: plans, OEMs")]):
    node(s, 39, 124 + i * 52, 78, 44, t, sub, col="N")
# orchestrator
node(s, 128, 124, 118, 92, "Workflow orchestrator",
     "Cloud Run + ADK. Job state machine, event log, retries, idempotent signed webhooks, per-job cost cap", col="K", fill="F1F3F4")
node(s, 128, 224, 118, 48, "Untrusted-input guard", "Model Armor + rules: customer text and manuals are data, not instructions", col="R", fill="FCE8E6", tsize=7.8, ssize=6.8)
node(s, 128, 280, 118, 52, "Human approval gates", "agency approves price; customer approves quote, booking, payment, sharing", col="R", fill="FCE8E6", tsize=7.8, ssize=6.8)
# AI
ai = [("Intake agent", "Transcribe + Flash-Lite: complaint, facts, 1–2 questions"),
      ("Appliance identity", "Document AI OCR / Gemini vision + exact SQL match"),
      ("Diagnostic agent", "3.8 Flash: ranked, cited hypotheses or abstain"),
      ("Preparation agent", "technician brief, part class, customer text"),
      ("Repair memory agent", "close-out draft; repeat-failure check")]
for i, (t, sub) in enumerate(ai):
    node(s, 258, 124 + i * 42, 134, 36, t, sub, col="B", fill="E8F0FE", tsize=7.8, ssize=6.8)
# tools
tools = [("Safety rules", "hazard lexicon, escalate to person"),
         ("Consent + permissions", "who may see which record"),
         ("Warranty + price policy", "agency rate card, terms, GST"),
         ("Parts catalogue", "verified / unknown / incompatible"),
         ("Dispatch", "Maps Routes + Route Optimization"),
         ("UPI payment gateway", "payment link, signed webhook (sandbox)")]
for i, (t, sub) in enumerate(tools):
    node(s, 404, 124 + i * 35, 140, 30, t, sub, col="Y", fill="FEF7E0", tsize=7.6, ssize=6.6)
# record
node(s, 556, 124, 125, 74, "Appliance record",
     "Cloud SQL: machine ID, service timeline, evidence, consent, append-only audit. Files in Cloud Storage", col="G", fill="E6F4EA")
node(s, 556, 206, 125, 50, "Home Memory", "household view; technician-reported vs customer-verified events", col="G", fill="E6F4EA", tsize=7.8, ssize=6.8)
node(s, 556, 264, 125, 68, "Eval loop", "AI suggestion vs technician outcome; ADK evals, traces, release gates", col="R", fill="FCE8E6", tsize=7.8, ssize=6.8)
# arrows
for i in range(4):
    arrow(s, 117, 146 + i * 52, 128, 170 if i < 2 else 300)
arrow(s, 246, 165, 258, 165); arrow(s, 246, 200, 258, 230)
arrow(s, 392, 180, 404, 180); arrow(s, 392, 260, 404, 260)
arrow(s, 544, 160, 556, 160); arrow(s, 544, 250, 556, 230)
arrow(s, 618, 256, 618, 264)
# legend + notes
leg = [("B", "LLM capability"), ("Y", "Deterministic code / external API"), ("R", "Human or safety control"), ("G", "System of record")]
for i, (k, lab) in enumerate(leg):
    x = 39 + i * 132
    box(s, x, 340, 9, 9, fill=FILL[k], line=COL[k], lw=1)
    text(s, x + 13, 340, 115, 10, [(lab, 7.2, INK, False)])
text(s, 39, 354, 642, 34, [
    "**Rules that shape the design:** the vector index is never the source of truth for exact facts; no part is called "
    "compatible unless the catalogue says so; money, safety, consent and state changes never depend on a model alone.",
    "**Where it runs:** app, database and files in Mumbai (asia-south1). No Gemini model is offered on standard pay-as-you-go in Mumbai today, "
    "so the pilot calls Gemini's global endpoint with customer consent; in-India inference would need 3.5 Flash / Flash-Lite provisioned throughput. "
    "**Outside Google:** WhatsApp Cloud API, UPI payment gateway, parts suppliers."], size=7.4, line=1.05, space=1.5)

# ================================================================ 5 TOOLS
s = content_slide("Google AI Tools", "Google AI Studio, Google Antigravity and Google Agent Skills (used or planned to be used).")
text(s, 39, 113, 642, 14, [("From prototype to a measured, end-to-end repair workflow. All three are planned for the build; none has produced results yet.", 9.2, "3C4043", False)])
tools = [
    ("Google AI Studio", "B", "Design and evaluate the intelligence",
     ["- Prototype complaint understanding, label/invoice reading, grounded triage and technician briefs",
      "- Run candidate models on the same labelled cases, schema and rubric",
      "- Stress-test Telugu/Hindi code-switching, blurred labels, missing history"],
     "Versioned prompts, JSON schemas, first gold cases, model comparison sheet",
     "Same cases re-run per model; synthetic data only on free-tier keys"),
    ("Google Antigravity", "R", "Build and test the working product",
     ["- Build the agency desk, household page, Cloud Run backend, event workflow, WhatsApp intake",
      "- Implement tool calls, business rules, approval gates and the appliance record",
      "- Generate and run regression tests; we review every diff"],
     "One demonstrable complaint-to-repair-history workflow",
     "Tests and eval suite pass in CI before each demo build"),
    ("Google Agent Skills", "G", "Raise implementation quality",
     ["- Use Google's published developer skills for Cloud, ADK, Gemini API and deployment",
      "- Write separate KeepWell domain skills: repair vocabulary, safety escalation, service evidence, tone",
      "- Developer skills are build-time guidance, not runtime agents"],
     "Reviewable SKILL.md files in the repo, reused by the eval runner",
     "Skill-guided code reviewed; domain skills checked by a technician"),
]
for i, (name, k, role, task, deliv, proof) in enumerate(tools):
    x = 39 + i * 218
    box(s, x, 132, 206, 216, fill="N")
    box(s, x, 135, 3, 210, fill=COL[k], line=None, shape=MSO_SHAPE.RECTANGLE)
    text(s, x + 10, 138, 190, 30, [(name, 11, INK, True), (role, 8.6, COL[k], True)], space=1)
    text(s, x + 10, 168, 190, 10, [("TASK", 6.8, MUTED, True)])
    text(s, x + 10, 178, 190, 92, task, size=8.1, space=2)
    text(s, x + 10, 272, 190, 10, [("DELIVERABLE", 6.8, MUTED, True)])
    text(s, x + 10, 282, 190, 30, [deliv], size=8.1)
    text(s, x + 10, 312, 190, 10, [("PROOF", 6.8, MUTED, True)])
    text(s, x + 10, 322, 190, 26, [proof], size=8.1)
card(s, 39, 354, 642, 32, None,
     ["**Runtime (what customers touch):** Agent Development Kit (ADK) agents on Cloud Run · selected Gemini models · Cloud SQL + "
      "Cloud Storage · Document AI · Maps Platform · authenticated adapters for WhatsApp and the payment gateway. "
      "**Measured with:** assertions, expert rubrics, tool-trajectory checks, traces, real cost per workflow."],
     col="Y", fill="N", size=7.9)

# ================================================================ 6 MODELS
s = content_slide("Google AI Models", "Google AI model(s) used or planned for the proposed solution.")
text(s, 39, 113, 642, 14, [("Different intelligence for different repair decisions. Each is a candidate to benchmark on our cases, not a guaranteed winner.", 9.2, "3C4043", False)])
bands = [
    ("LISTEN", "B", "Gemini 3.5 Transcribe", "Code-switched Telugu/Hindi voice notes (both supported); custom repair vocabulary",
     "Critical-term recall, word error rate by language", "Flash-Lite audio input; tap/typed intake"),
    ("UNDERSTAND", "R", "Gemini 3.5 Flash-Lite", "Intent, appliance facts, missing fields, one follow-up question",
     "Field precision/recall, schema validity, abstention", "Escalate to 3.8 Flash"),
    ("READ", "Y", "Document AI Enterprise OCR vs Gemini vision", "Model/serial plate, invoice date and seller (OCR reads Telugu, Hindi; runs in Mumbai)",
     "Exact match on critical fields; low-confidence → ask", "Customer or technician types it"),
    ("REASON", "G", "Gemini 3.8 Flash", "Ranked fault hypotheses from history + cited manual excerpts",
     "Grounded claims, usefulness, uncertainty, tool correctness", "Inspect-first; human triage"),
    ("REMEMBER", "B", "Gemini Embedding 2 vs text-embedding-005", "Find manual sections and similar past repairs; Embedding 2 also embeds photos",
     "Retrieval recall@5, citation validity, cost", "SQL filters + keyword search"),
]
hdr = ["Stage", "Candidate", "Job", "Evaluated on", "Fallback"]
xs = [39, 108, 228, 400, 562]
ws = [66, 118, 170, 160, 119]
for x, w, h in zip(xs, ws, hdr):
    text(s, x + 2, 131, w, 10, [(h.upper(), 6.8, MUTED, True)])
for i, (st, k, model, job, ev, fb) in enumerate(bands):
    y = 143 + i * 31
    box(s, 39, y, 642, 27, fill="N")
    chip(s, 43, y + 7, 60, 13, st, col=k, size=7, txt="FFFFFF" if k != "Y" else INK)
    text(s, 110, y + 3, 116, 22, [(model, 8.2, INK, True)], anchor=MSO_ANCHOR.MIDDLE, line=1.0)
    for x, w, t in ((230, 166, job), (402, 156, ev), (564, 115, fb)):
        text(s, x, y + 3, w, 22, [(t, 7.7, INK, False)], anchor=MSO_ANCHOR.MIDDLE, line=1.0)
text(s, 43, 299, 638, 14, [("**Later, only if the pilot shows demand:** Gemini 3.8 Live (GA; audio sessions about 15 min) for real-time technician help; Gemma on-device for offline use. "
                            "**Classical ML, not LLMs:** parts-demand forecasts, technician ranking, repeat-failure anomaly detection.", 7.5, "3C4043", False)], line=1.0)
card(s, 39, 320, 316, 66, "No LLM for these decisions",
     ["Price and GST maths · consent and access · payment confirmation (gateway webhook only) · exact part "
      "compatibility (catalogue) · technician slots (Route Optimization) · job state changes (state machine)."],
     col="R", fill="N", size=8, tsize=9.2)
card(s, 365, 320, 316, 66, "Selection rule",
     ["Pick the simplest model that meets the quality gate at acceptable latency, cost and data-processing terms. "
      "Record benchmark results before claiming a model is better or cheaper. Endpoint region verified per model."],
     col="G", fill="N", size=8, tsize=9.2)

# ================================================================ 7 BUSINESS
s = content_slide("Business Model and Market", "B2B pricing per technician, with larger contracts as customers grow.")
card(s, 39, 114, 196, 128, "1  Who pays",
     ["- **Owner-run agencies** (2–10 technicians): the pilot customer",
      "- **Service centres and brand-authorised networks** (10–100+ technicians)",
      "- **Brands and plan providers:** claims evidence and job routing (Phase 3)",
      "- **Households:** free. Their Home Memory keeps them with the agency"],
     col="G", fill="N", size=7.9, tsize=9.6)
rows = [["Plan", "Price", "For"],
        ["Starter", "₹1,499 / technician / month", "Owner-run agencies. 60 AI-handled jobs per technician, then ₹10 a job"],
        ["Pro", "₹2,499 / technician / month", "Service centres: route optimisation, parts, multi-branch, analytics"],
        ["Enterprise", "Annual contract", "Brands, plan providers: ₹30–100 per claim, ₹100–250 per routed job"]]
text(s, 245, 114, 270, 12, [("**2  Pricing (to test; first 60 days free)**", 9.6, INK, False)])
table(s, 245, 129, 270, [52, 86, 132], rows, head_fill=B, size=7.3, head_size=7.6, row_h=28)
card(s, 525, 114, 156, 128, "3  What the market pays",
     ["- Indian WhatsApp AI tools: ₹1,000–17,000 / month",
      "- US field-service software: about $245–500 per technician / month",
      "- US AI call answering for home services: from about $449 / month",
      "- A wasted service visit costs an Indian service business about ₹350–500"],
     col="Y", fill="N", size=7.4, tsize=9.2)
card(s, 39, 250, 196, 104, "4  One technician on Starter",
     ["**₹1,499** in each month",
      "**₹90–600** running cost (≤60 jobs × ₹1.50–₹10: AI, WhatsApp, cloud)",
      "**₹900–1,410** left for support, sales, team",
      "Pays for itself if it avoids **3–4 wasted visits** a month."],
     col="B", fill="N", size=7.9, tsize=9.6)
card(s, 245, 250, 236, 104, "5  How it grows (targets, not forecasts)",
     ["- **300 agencies** × 5 technicians on Starter ≈ **₹2.7 Cr a year**",
      "- **40 service centres** × 20 technicians on Pro ≈ **₹2.4 Cr a year**",
      "- **One plan provider** at 10,000 claims a month × ₹30–100 ≈ **₹36 lakh–1.2 Cr a year**",
      "Agencies prove the product; networks and brands bring the larger contracts."],
     col="G", fill="N", size=7.9, tsize=9.6)
card(s, 491, 250, 190, 104, "6  What the pilot must prove",
     ["- Agencies keep paying ₹1,499 per technician after 60 days",
      "- Usage fits in 60 jobs per technician",
      "- First-visit resolution beats their baseline",
      "- One service centre or brand agrees to pilot Pro or Enterprise"],
     col="R", fill="N", size=7.9, tsize=9.6)
text(s, 39, 360, 642, 28, [
    "**Competition:** Urban Company (consumer booking), Servify (warranty programmes for brands), field-service software (tickets, dispatch). "
    "KeepWell works for the independent agency, in its language, and keeps each machine's verified repair history. **Key risk:** a repeat visit can earn an agency a second fee.",
    "[[Benchmarks from vendor and comparison sites (Nov 2026) and one practitioner estimate for visit cost; all KeepWell figures are assumptions to test. Running cost excludes payment fees and support.]]"],
    size=7.4, space=1)

# ================================================================ 8 EVALUATION
s = content_slide("Trust, Evaluation and Validation", "How we will measure quality, safety and business impact.")
card(s, 39, 114, 222, 236, "One gold case, end to end",
     ["**Input:** Telugu voice note, fridge not cooling, model unknown.",
      "**Expected:** keep the symptom, ask for the label photo, propose an inspect-first visit, claim no part.",
      "**Bad output:** \"Replace compressor XYZ; that will fix it.\"",
      "**Failure:** invented diagnosis and part with no model evidence.",
      "**Fix:** hard catalogue gate on part claims; more abstention examples; rerun the same case.",
      "**Result:** [[to be measured. We have not run this yet; the demo will show real before/after assertions, scores, traces and cost.]]",
      "**Learning loop:** AI suggestion → technician findings → customer confirms or disputes → error analysis → rule, retrieval or prompt fix → rerun holdout + regressions."],
     col="B", fill="N", size=8, tsize=9.6)
card(s, 271, 114, 200, 236, "Three evaluation layers",
     ["**1 Assertions:** valid schema, real IDs, no invented compatible part, hazard escalated, no quote or payment action without approval.",
      "**2 Rubrics (0–4, anchored, human-reviewed):** evidence, decision, uncertainty, technician detail, customer language.",
      "**3 Trajectory + outcome:** right tools in the right order (ADK tool_trajectory_avg_score, IN_ORDER), approvals at the right points, latency, cost, and real first-visit and 14/30-day repeat rates.",
      "**Gold set:** 100 adjudicated cases (25 intake, 25 triage/safety, 15 parts/dispatch, 10 quote/payment, 15 repair/repeat, "
      "10 Home Memory); ≥20 code-switched, ≥20 adversarial; untouched holdout. Synthetic first, clearly labelled."],
     col="G", fill="N", size=7.8, tsize=9.6)
rows = [["Provisional release gate", "Target"],
        ["Schema-valid outputs", "≥ 99%"],
        ["Safety escalation recall (hazard suite)", "100%"],
        ["Invented \"verified compatible\" part", "0"],
        ["Critical field precision", "≥ 95%"],
        ["Grounded factual claims", "≥ 98%"],
        ["Correct next state (holdout)", "≥ 95%"],
        ["Rubric ≥ 3/4 on every critical dimension", "≥ 85%"]]
table(s, 481, 114, 200, [148, 52], rows, head_fill=R, size=7.6, head_size=7.8, row_h=21)
text(s, 481, 285, 200, 64, [
    "[[Targets to refine with technicians. Not yet tested. A small gold set cannot prove rare-event safety; any critical "
    "policy failure blocks release regardless of averages.]]"], size=7.6)
card(s, 39, 356, 642, 30, None,
     ["**Validation plan:** interview 15–20 agencies → record each agency's baseline first-visit rate → paid pilot at ₹1,499 per technician → "
      "decide on more cities from pilot data. **Today:** spec, eval design and synthetic cases. No pilot, accuracy or cost results yet."],
     col="Y", fill="N", size=7.9)

# ================================================================ 9 THANK YOU
s = prs.slides.add_slide(BLANK)
s.shapes.add_picture(f"{ASSETS}/thankyou.jpg", 0, 0, Pt(720), Pt(405))

prs.save(OUT)
print("saved", OUT)
