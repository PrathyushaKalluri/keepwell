"""Build the KeepWell idea-submission deck (v2) on top of the official template PDF.

Usage: python build_deck_v2.py [template.pdf] [out.pdf]
Defaults resolve relative to the repo root.

Fixes vs v1: the free template slide is copied twice as independent pages
(v1 used doc.select([...,7,7,...]), which shares one content stream, so the
last two slides were drawn on top of each other).
"""
import math
import os
import sys

import pymupdf as fitz

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = sys.argv[1] if len(sys.argv) > 1 else os.path.join(ROOT, "Startup Buildathon _ Idea Submission Deck.pdf")
OUT = sys.argv[2] if len(sys.argv) > 2 else os.path.join(ROOT, "KeepWell Pitch Deck v2.pdf")

B, R, Y, G, D = "#4285F4", "#EA4335", "#FBBC04", "#34A853", "#202124"


def rgb(h):
    return tuple(int(h[i:i + 2], 16) / 255 for i in (1, 3, 5))


CSS = (
    "body{font-family:sans-serif;color:#202124;font-size:8.4pt;line-height:1.27}"
    "b{font-weight:bold} h4{margin:0 0 3px 0;font-size:9.8pt}"
    "ul{margin:2px 0 0 0;padding-left:11px} li{margin-bottom:2px}"
    ".s{font-size:7pt;color:#5f6368} .m{color:#5f6368}"
    "td,th{font-size:8pt;vertical-align:top;padding:2.2px 4px;text-align:left} th{color:#ffffff}"
)

# Template pages: 0 guidelines, 1 cover, 2 problem, 3 solution, 4 architecture,
# 5 tools, 6 models, 7 free slide, 8 thank you. Guidelines page is dropped.
tpl = fitz.open(SRC)
doc = fitz.open()
for i in (1, 2, 3, 4, 5, 6, 7, 7, 8):
    doc.insert_pdf(tpl, from_page=i, to_page=i)  # each insert is an independent page


def card(p, x, y, w, h, html, col=B, fill="#F8F9FA"):
    r = fitz.Rect(x, y, x + w, y + h)
    p.draw_rect(r, color=rgb("#DADCE0"), fill=rgb(fill), radius=0.04, width=0.7)
    p.draw_rect(fitz.Rect(x, y + 3, x + 3, y + h - 3), color=None, fill=rgb(col))
    spare, _ = p.insert_htmlbox(fitz.Rect(x + 8, y + 4, x + w - 5, y + h - 3), html, css=CSS, scale_low=1)
    assert spare >= 0, f"overflow in card: {html[:60]}"


def text(p, x, y, w, h, html, css=""):
    spare, _ = p.insert_htmlbox(fitz.Rect(x, y, x + w, y + h), html, css=CSS + css, scale_low=1)
    assert spare >= 0, f"overflow in text: {html[:60]}"


def clear(p):
    for r in p.search_for("Type here"):
        p.add_redact_annot(fitz.Rect(r.x0 - 1, r.y0 - 1, r.x1 + 14, r.y1 + 2), fill=(1, 1, 1))
    p.apply_redactions()


def title(p, t, sub):
    p.insert_text((39, 100), t, fontsize=18, fontname="hebo", color=rgb(D))
    p.insert_text((39, 117), sub, fontsize=11, fontname="helv", color=rgb("#3c4043"))


def table(header, rows, widths, head_col):
    h = f"<table style='width:100%' cellspacing='0'><tr style='background:{head_col}'>"
    h += "".join(f"<th width='{w}'>{c}</th>" for c, w in zip(header, widths))
    h += "</tr>"
    for i, r in enumerate(rows):
        bg = "#F8F9FA" if i % 2 == 0 else "#FFFFFF"
        h += f"<tr style='background:{bg}'>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>"
    return h + "</table>"


# ---------------------------------------------------------------- 1 cover
p = doc[0]
p.insert_text((135, 274), "KeepWell", fontsize=14, fontname="hebo", color=rgb(D))
p.insert_text((125, 308), "2", fontsize=12, fontname="helv", color=rgb(D))
text(p, 185, 330, 500, 64,
     "<span style='font-size:10pt'>Owner-run appliance repair agencies in India's Tier 2/3 cities take jobs "
     "through WhatsApp voice notes and phone calls. Technicians arrive without the model, part or repair "
     "history, so first visits fail, quotes get disputed, and households cannot prove warranty or keep a "
     "record of what they own.</span>")

# ---------------------------------------------------------------- 2 problem
p = doc[1]; clear(p)
text(p, 39, 128, 642, 20,
     "<span style='font-size:9.6pt'><b>Root cause:</b> no structured record of the job or the appliance exists "
     "anywhere, so every visit starts from zero.</span>")
card(p, 39, 150, 206, 118,
     "<h4>Repair agencies <span class='m' style='font-weight:normal;font-size:8pt'>(2-10 technicians)</span></h4><ul>"
     "<li>Technician arrives without model, serial or history: wrong part, second visit</li>"
     "<li>Complaints come as Hindi, Telugu or Tamil voice notes that never become records</li>"
     "<li>Quotes by phone lead to price disputes and lost trust</li></ul>", B)
card(p, 257, 150, 206, 118,
     "<h4>Households</h4><ul>"
     "<li>Invoices, warranty dates and past repairs are lost or on paper</li>"
     "<li>No way to prove warranty or check whether a quote is fair</li>"
     "<li>Brand service is costly and slow, so local technicians are the default</li></ul>", R)
card(p, 475, 150, 206, 118,
     "<h4>Plan providers and OEMs</h4><ul>"
     "<li>Claims are checked by hand with weak evidence</li>"
     "<li>No view of repair quality in the unorganised channel</li>"
     "<li>No clean data to price plans or spot repeat failures</li></ul>", G)
stats = [("55%", "of households had a high-value product turn out defective within warranty", B),
         ("21%", "of those who sought action got a refund or replacement", R),
         ("3 in 4", "AC owners did not use brand service this season", G)]
for i, (k, t, c) in enumerate(stats):
    x = 39 + i * 218
    p.insert_text((x, 296), k, fontsize=19, fontname="hebo", color=rgb(c))
    off = 70 if len(k) > 3 else 52
    text(p, x + off, 278, 206 - off, 30, f"<span style='font-size:8.2pt'>{t}</span>")
text(p, 39, 307, 642, 14,
     "<span class='s'>Sources: LocalCircles consumer surveys, India: defective-products survey 2022 (28,000+ responses); "
     "AC servicing survey 2026. Self-reported survey figures, not measured repair data.</span>")
card(p, 39, 324, 642, 50,
     "<b>Why Tier 2/3 first.</b> Durables sales grew 10% in Tier 3 cities vs 7% in Tier 1 (Q4 2024), with many "
     "first-time fridge and washing-machine buyers. Urban Company and OEM networks are metro-weighted, so owner-run "
     "agencies carry the load with WhatsApp and no software. "
     "<span class='s'>(Trade-press figure. No official count of repair agencies exists; the pilot will measure it.)</span>", Y)

# ---------------------------------------------------------------- 3 solution
p = doc[2]; clear(p)
text(p, 39, 128, 642, 32,
     "<span style='font-size:10.2pt'><b>KeepWell is an AI desk for repair agencies that lives in WhatsApp. It prepares "
     "every visit, and turns each finished job into a lasting Home Memory record of the appliance.</b></span>")
steps = [("1 Understand", "Customer sends a voice note or photo in Hindi, Telugu, Tamil, Kannada or Marathi", B),
         ("2 Identify", "Model, serial and invoice read from photos; warranty checked by rules", R),
         ("3 Triage", "Safety hard-stops first, then likely faults and parts, grounded in manuals", Y),
         ("4 Quote", "Priced from the agency's own rate card; the model never invents prices", G),
         ("5 Prepare", "Technician brief, parts list, route and time slot", B),
         ("6 Close out", "Technician's voice note becomes the job card; record saved with consent", R)]
for i, (h, t, c) in enumerate(steps):
    card(p, 39 + i * 108, 166, 102, 90, f"<h4 style='font-size:9pt'>{h}</h4><span style='font-size:7.9pt'>{t}</span>", c)
card(p, 39, 264, 205, 124,
     "<h4>What changes</h4><ul>"
     "<li><b>Agency:</b> right part on the first visit; quotes in minutes; a record for every job</li>"
     "<li><b>Household:</b> warranty proof and service history in one place; a quote they can check</li>"
     "<li><b>Partners (later):</b> evidence-backed claims</li></ul>", G)
card(p, 254, 264, 205, 124,
     "<h4>Rules built in</h4><ul>"
     "<li>AI proposes; a person approves price, warranty and safety decisions</li>"
     "<li>Asks a question instead of guessing when unsure</li>"
     "<li>Never auto-denies a claim</li>"
     "<li>No record kept without consent</li></ul>", B)
card(p, 469, 264, 212, 124,
     "<h4>Roadmap and goal metric</h4><ul>"
     "<li><b>Phase 1:</b> agency AI desk (Tier 2/3)</li>"
     "<li><b>Phase 2:</b> Home Memory, plan/AMC offers, parts</li>"
     "<li><b>Phase 3:</b> claims triage for plan providers and OEMs (Tier 1)</li></ul>"
     "<b>Goal:</b> verified first-time-right jobs per active agency per month.", Y)

# ---------------------------------------------------------------- 4 architecture
p = doc[3]; clear(p)


def node(x, y, w, h, t, c, fill=None):
    p.draw_rect(fitz.Rect(x, y, x + w, y + h), color=rgb(c), fill=rgb(fill or "#FFFFFF"), radius=0.12, width=1)
    spare, _ = p.insert_htmlbox(fitz.Rect(x + 3, y + 2, x + w - 3, y + h - 1), t,
                                css=CSS + "body{text-align:center;font-size:7.6pt;line-height:1.2}", scale_low=1)
    assert spare >= 0, f"overflow in node: {t[:40]}"


def arrow(x1, y1, x2, y2):
    col = rgb("#80868B")
    p.draw_line((x1, y1), (x2, y2), color=col, width=1)
    a = math.atan2(y2 - y1, x2 - x1)
    for s in (0.45, -0.45):
        p.draw_line((x2, y2), (x2 - 6 * math.cos(a - s), y2 - 6 * math.sin(a - s)), color=col, width=1)


for x, lbl in ((39, "CHANNELS"), (175, "ORCHESTRATION"), (365, "INTELLIGENCE"), (555, "DATA AND OPS")):
    p.insert_text((x, 134), lbl, fontsize=6.5, fontname="hebo", color=rgb("#5f6368"))
node(39, 140, 100, 52, "<b>Customer</b><br>WhatsApp voice note, photo, text", B)
node(39, 205, 100, 52, "<b>Agency and technician</b><br>WhatsApp + light web app (PWA)", B)
node(39, 270, 100, 52, "<b>Plan provider, OEM</b><br>claims console (Phase 3)", B)
node(175, 140, 150, 100, "<b>KeepWell orchestrator</b><br>Cloud Run API + <b>ADK agents</b><br>"
     "intake, identify, triage, quote, brief and close-out agents; retries and per-job cost cap", G, "#E6F4EA")
node(175, 252, 150, 70, "<b>Human approval gates</b><br>quote, warranty decision, safety release, data sharing", R, "#FCE8E6")
node(365, 138, 150, 50, "<b>Gemini on Vertex AI</b><br>3.8 Flash + 3.5 Flash-Lite: voice, vision, extraction, drafting", B, "#E8F0FE")
node(365, 196, 150, 44, "<b>Rules engine (code)</b><br>warranty, pricing, safety hard-stops, consent", Y, "#FEF7E0")
node(365, 248, 150, 44, "<b>Grounded retrieval</b><br>manuals + fault codes in Postgres pgvector, text-embedding-005", B, "#E8F0FE")
node(365, 300, 150, 40, "<b>Google Maps Platform</b><br>Routes + Route Optimization", G, "#E6F4EA")
node(555, 138, 126, 60, "<b>Cloud SQL (Postgres)</b><br>jobs, appliances, Home Memory, audit log", B)
node(555, 206, 126, 50, "<b>Cloud Storage</b><br>voice, photos, invoices, with consent and retention", B)
node(555, 264, 126, 50, "<b>Pub/Sub + Cloud Tasks</b><br>events, reminders, retries", B)
node(555, 322, 126, 46, "<b>Evals + monitoring</b><br>ADK evals, Gen AI Evaluation, Cloud Logging", R, "#FCE8E6")
for y in (166, 231, 296):
    arrow(139, y, 175, 190 if y < 250 else 285)
arrow(325, 190, 365, 165); arrow(325, 200, 365, 218); arrow(325, 215, 365, 270); arrow(325, 235, 365, 318)
arrow(515, 165, 555, 168); arrow(515, 218, 555, 230); arrow(515, 270, 555, 288)
text(p, 39, 346, 505, 46,
     "<span class='s'><b>Design choices.</b> Hosted in Mumbai (asia-south1). Prices, warranty verdicts and safety stops "
     "come from code, not the model. pgvector keeps retrieval portable and in-region. AI Studio is used for prototyping and "
     "Vertex AI for production. WhatsApp Cloud API is the only non-Google component.</span>")

# ---------------------------------------------------------------- 5 tools
p = doc[4]; clear(p)
card(p, 39, 134, 206, 170,
     "<h4>Google AI Studio</h4><b>Planned use</b><ul>"
     "<li>Prototype and tune each prompt: intake, label reading, quote text, close-out</li>"
     "<li>Test structured JSON output on real Indian-language voice notes and invoice photos</li>"
     "<li>Compare 3.8 Flash and 3.5 Flash-Lite on our golden set before fixing the model split</li>"
     "<li>Get API keys and ship the first working demo</li></ul>", B)
card(p, 257, 134, 206, 170,
     "<h4>Google Antigravity</h4><b>Planned use</b><ul>"
     "<li>Agent-driven build of the backend, WhatsApp webhook and agency web app during the two-day City Buildathon</li>"
     "<li>Agents write and run tests against our eval cases while we review the diffs</li>"
     "<li>One workspace for spec, prompts and code</li></ul>", R)
card(p, 475, 134, 206, 170,
     "<h4>Google Agent Skills</h4><b>Planned use</b><ul>"
     "<li>Package repair know-how as reusable skills: warranty rules, safety hard-stop checklist, "
     "Hindi/Telugu/Tamil appliance glossary, quote format</li>"
     "<li>Agents load a skill only when needed, keeping prompts short and cheap</li>"
     "<li>The eval runner reuses the same skills</li></ul>", G)
card(p, 39, 314, 642, 46,
     "<b>Also in the stack:</b> Agent Development Kit (agents, evals, A2A/MCP), Vertex AI, Cloud Run, Cloud SQL, "
     "Cloud Storage, Pub/Sub, Cloud Tasks, Google Maps Platform. The product spec and eval cases are drafted; "
     "the build happens in the City Buildathon.", Y)

# ---------------------------------------------------------------- 6 models
p = doc[5]; clear(p)
rows = [
    ("Gemini 3.8 Flash", "Fault hypotheses, quote and technician-brief drafting, job close-out",
     "Stable; strongest reasoning per rupee in the Flash tier; structured JSON output"),
    ("Gemini 3.5 Flash-Lite", "Language ID, routing, label and invoice extraction, voice-note transcription, reminders",
     "Cheapest stable tier and no 2027 price rise; routing work here cuts AI cost per job by about half"),
    ("Gemini 3.5 Flash (Vertex AI, India)", "The Flash tasks above, when a partner requires in-country processing",
     "Google's in-country ML processing commitment for India"),
    ("Gemini audio input; Chirp 3 as fallback", "Hindi, Telugu, Tamil, Kannada and Marathi voice notes: transcribe, then extract",
     "Audio at 32 tokens/sec is about 10x cheaper than Chirp 3; Chirp 3 Telugu/Tamil are preview and US/EU only"),
    ("text-embedding-005; Gemini Embedding 2 later", "Retrieval over manuals, fault codes and plan terms; later, photo search of parts and labels",
     "Negligible cost; multimodal embedding when photo search is added"),
    ("Gemini 3.8 Live (later)", "Live voice calls with technicians and customers",
     "Live API sessions are capped (about 15 min of audio), so not in release 1"),
]
text(p, 39, 130, 642, 222, table(("Model", "Used for", "Why this model"), rows, ("25%", "37%", "38%"), B))
text(p, 39, 352, 642, 40,
     "<span class='s'>Modelled cost per job (AI + WhatsApp + cloud) is about Rs 1.5-5.5 at 2026 prices and up to about "
     "Rs 10 after 3.8 Flash prices double on 1 Jan 2027; token counts are assumptions to be measured. Gemini 4 Hydrogen will "
     "be evaluated once its India region is confirmed. Model names and regions to be re-checked before launch.</span>")

# ---------------------------------------------------------------- 7 business model and market
p = doc[6]
title(p, "Business Model and Market", "Who pays, how much, and why the unit economics work.")
rows = [("1 Per-fix AI desk fee", "Agency", "Rs 40 per completed job card; pilot also tests Rs 100", "Phase 1"),
        ("2 Plan / AMC commission", "Plan provider", "10-20% of plans sold via Home Memory", "Phase 2"),
        ("3 Parts referral", "Verified parts sellers", "3-8% of matched orders", "Phase 2"),
        ("4 Claims triage", "Warranty administrators, OEMs", "Rs 30-100 per claim", "Phase 3"),
        ("5 Service lead routing", "OEMs, plan providers", "Rs 100-250 per completed job", "Phase 3")]
text(p, 39, 126, 642, 118, table(("Revenue stream", "Who pays", "Pricing (to be tested)", "Phase"), rows,
                                  ("23%", "25%", "42%", "10%"), G))
card(p, 39, 248, 205, 140,
     "<h4>Unit economics (modelled)</h4><ul>"
     "<li>Cost per job Rs 1.5-5.5 now; up to about Rs 10 at 2027 Flash prices</li>"
     "<li>Gross margin on variable cost: 76-96% at Rs 40, 90-98% at Rs 100</li>"
     "<li>R1 alone: 3 jobs a day = about Rs 36,000 a year per agency; 1,000 agencies = about Rs 3.6 Cr</li></ul>"
     "<span class='s'>Assumptions, not forecasts. Jobs per agency is unmeasured.</span>", B)
card(p, 254, 248, 205, 140,
     "<h4>Go-to-market</h4><ul>"
     "<li>Start with 15-20 agencies in 1-2 Tier 2 cities; sell per fix, no monthly seat fee</li>"
     "<li>Grow through agency referrals and parts distributors in 5-10 Tier 2/3 cities</li>"
     "<li>Move into Tier 1 once agencies bring household records that plan providers and OEMs want</li></ul>", Y)
card(p, 469, 248, 212, 140,
     "<h4>Competition and moat</h4><ul>"
     "<li><b>Urban Company:</b> metro consumer marketplace</li>"
     "<li><b>Servify:</b> B2B warranty/OEM, metro-led</li>"
     "<li><b>ServiceOnDoors:</b> service marketplace</li>"
     "<li><b>Field-service SaaS:</b> English-first, generic</li></ul>"
     "None is a vernacular, WhatsApp-first desk for agencies. <b>Moat:</b> agency job data, linked appliance records, "
     "vernacular voice data.", R)

# ---------------------------------------------------------------- 8 trust, evaluation, next steps
p = doc[7]
title(p, "Trust, Evaluation and Next Steps", "How we keep it safe, measure quality and prove demand.")
card(p, 39, 128, 206, 208,
     "<h4>Responsible AI</h4><ul>"
     "<li>A person approves every quote, warranty decision, safety release and data share</li>"
     "<li>Coded safety hard-stops for gas, refrigerant and high voltage that the AI cannot override; "
     "the list will be reviewed by electricians and gas-safety experts</li>"
     "<li>Consent ledger, redaction and retention limits for voice and photos, built for the DPDP Act 2023 and Rules 2025</li>"
     "<li>Customer content is treated as data, never as instructions (prompt-injection defence)</li>"
     "<li>Complaint help is an evidence pack, not legal advice</li></ul>", R)
card(p, 254, 128, 206, 208,
     "<h4>Evaluation</h4><ul>"
     "<li>Golden datasets per feature and per language: Hindi, Telugu, Tamil, Kannada, Marathi</li>"
     "<li>Three layers: hard-rule assertions, rubric scoring, agent-trajectory checks</li>"
     "<li>ADK evals and Vertex Gen AI Evaluation run in CI</li>"
     "<li>Release blocked on any safety false-accept or a drop in field-extraction accuracy</li>"
     "<li>LLM judge calibrated against human labels</li>"
     "<li>Eval results shown live in the demo</li></ul>", B)
card(p, 469, 128, 212, 208,
     "<h4>Next steps (validation first)</h4><ul>"
     "<li><b>Interviews:</b> 15-20 agencies in 1-2 Tier 2 cities</li>"
     "<li><b>Paid pilot:</b> Rs 40 vs Rs 100 per fix</li>"
     "<li><b>Measure:</b> revisit rate, quote time, cost per job, jobs per agency</li>"
     "<li><b>Voice:</b> accuracy tests on real field recordings in each language</li>"
     "<li><b>Partners:</b> two administrator or OEM interviews before building claims triage</li>"
     "<li><b>Compliance:</b> confirm plan-selling and licensing rules</li></ul>"
     "", G)
card(p, 39, 342, 642, 46,
     "<b>Milestones.</b> <b>Now:</b> working prototype at the City Buildathon. <b>Months 0-6:</b> agency interviews and "
     "paid pilot (per-fix fee). <b>Months 6-12:</b> 5-10 Tier 2/3 cities; Home Memory, plans and parts. <b>Year 2:</b> "
     "claims triage with 1-2 plan-provider or OEM partners in Tier 1. "
     "<span class='s'>No pilot data yet; all figures in this deck are modelled assumptions to be tested.</span>", Y)

doc.save(OUT, garbage=4, deflate=True)
print("saved", OUT, os.path.getsize(OUT) // 1024, "KB")
