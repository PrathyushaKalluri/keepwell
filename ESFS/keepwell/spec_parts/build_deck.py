import fitz, sys
SRC="/Users/klprathyusha/Placement Preparation/google startup buildathon/Startup Buildathon _ Idea Submission Deck.pdf"
OUT=sys.argv[1]
B,R,Y,G,D="#4285F4","#EA4335","#FBBC04","#34A853","#202124"
def rgb(h): return tuple(int(h[i:i+2],16)/255 for i in (1,3,5))
doc=fitz.open(SRC); doc.select([1,2,3,4,5,6,7,7,8])
CSS="body{font-family:sans-serif;color:#202124;font-size:8.6pt;line-height:1.28} b{font-weight:bold} h4{margin:0 0 3px 0;font-size:10pt} ul{margin:2px 0 0 0;padding-left:11px} li{margin-bottom:2px} .s{font-size:7.2pt;color:#5f6368} .k{font-size:15pt;font-weight:bold} td,th{font-size:8.2pt;vertical-align:top;padding:2px 4px;text-align:left} th{color:#ffffff}"
def card(p,x,y,w,h,html,col=B,fill="#F8F9FA"):
    r=fitz.Rect(x,y,x+w,y+h)
    p.draw_rect(r,color=rgb("#DADCE0"),fill=rgb(fill),radius=0.04,width=0.7)
    p.draw_rect(fitz.Rect(x,y+3,x+3,y+h-3),color=None,fill=rgb(col))
    p.insert_htmlbox(fitz.Rect(x+8,y+4,x+w-5,y+h-3),html,css=CSS)
def text(p,x,y,w,h,html): p.insert_htmlbox(fitz.Rect(x,y,x+w,y+h),html,css=CSS)
def clear(p):
    for r in p.search_for("Type here"): p.add_redact_annot(r,fill=(1,1,1))
    p.apply_redactions()
def title(p,t,sub):
    p.insert_text((39,100),t,fontsize=18,fontname="hebo",color=rgb(D))
    p.insert_text((39,117),sub,fontsize=11,fontname="helv",color=rgb("#3c4043"))
# 0 cover
p=doc[0]
p.insert_text((135,274),"Keepwell",fontsize=14,fontname="hebo",color=rgb(D))
p.insert_text((125,308),"3  (Prathyusha Kalluri, Sri Charan Peri, Kavyanth Munagala - IIIT Hyderabad)",fontsize=11,fontname="helv",color=rgb(D))
text(p,185,330,495,60,"<span style='font-size:10.5pt'>Indian appliance repair agencies run on voice notes, phone calls and lost invoices, so first visits fail, warranties go unproven and households keep no record of what they own.</span>")
# 1 problem
p=doc[1]; clear(p)
card(p,39,134,206,128,"<h4>Agencies (owner-run, 2-10 technicians)</h4><ul><li>Arrive without model, serial or repair history, so the wrong part or a second visit</li><li>Complaints arrive as Hindi, Telugu or Tamil voice notes that never become records</li><li>Quotes are by phone, so price disputes and lost trust</li></ul>",B)
card(p,257,134,206,128,"<h4>Households</h4><ul><li>Invoices, warranty dates and past repairs are lost or on paper</li><li>No way to prove warranty or check if a quote is fair</li><li>Brand service is distrusted; local technicians are the default</li></ul>",R)
card(p,475,134,206,128,"<h4>Warranty and plan providers, OEMs</h4><ul><li>Claims are checked by hand with weak evidence</li><li>No visibility of repair quality in the unorganised channel</li><li>No clean record to price plans or spot repeat failures</li></ul>",G)
for i,(k,t,c) in enumerate([("55%","had a defective in-warranty high-value product",B),("21%","of those who acted got a refund or replacement",R),("76%","of AC owners avoid brand service",G)]):
    x=39+i*218
    p.insert_text((x,292),k,fontsize=20,fontname="hebo",color=rgb(c))
    text(p,x+52,274,150,28,f"<span style='font-size:8.6pt'>{t}</span>")
text(p,39,306,642,34,"<span class='s'>Source: LocalCircles consumer polls (India). These are consumer survey figures, not measured repair data.</span>")
card(p,39,332,642,56,"<b>Why Tier 2/3 first.</b> Durables sales in Tier 3 cities grew 10% vs 7% in Tier 1 (Q4 2024); first-time fridge and washing-machine buyers drive Tier 2 demand; organised repair is thin in small towns, so owner-run agencies and local technicians carry the load. <span class='s'>(Trade-press sources; we found no official agency count.)</span>",Y)
# 2 solution
p=doc[2]; clear(p)
text(p,39,132,642,30,"<span style='font-size:10.5pt'><b>Keepwell is an AI desk for repair agencies that lives in WhatsApp, and turns every job into a lasting Home Memory record for the appliance.</b></span>")
steps=[("1 Understand","Customer sends voice note or photo; Hindi, Telugu, Tamil, Kannada, Marathi",B),("2 Check","Model, serial, invoice read from photos; warranty checked by rules",R),("3 Triage","Safety hard-stops, then likely faults and parts, grounded in manuals",Y),("4 Quote","Price from the agency's rate card by code, never invented by the model",G),("5 Prepare","Technician brief, route and schedule",B),("6 Close out","Voice notes become the job card; record saved with consent",R)]
for i,(h,t,c) in enumerate(steps):
    x=39+i*108
    card(p,x,170,102,92,f"<h4 style='font-size:9pt'>{h}</h4><span style='font-size:8pt'>{t}</span>",c)
card(p,39,272,205,116,"<h4>Rules we build in</h4><ul><li>Model proposes; a human approves money, warranty and safety</li><li>Abstains and asks when unsure</li><li>Never auto-denies a claim</li><li>Consent before any record is kept</li></ul>",B)
card(p,254,272,205,116,"<h4>Build order</h4><ul><li><b>A Prepared Visit</b>: agency AI desk (Tier 2/3 first)</li><li><b>B Home Memory</b> and plan/AMC offers</li><li><b>C Claims triage</b> for plan providers and OEMs (Tier 1)</li><li>E Circular resale and recycling (vision)</li></ul>",G)
card(p,469,272,212,116,"<h4>Goal metric</h4><b>Verified first-time-right jobs per active agency per month.</b><br><br><span style='font-size:8pt'>Guardrails: safety misses, cost per job, human override rate, language accuracy gap. Targets to be set from the paid pilot.</span>",Y)
# 3 architecture
p=doc[3]; clear(p)
def node(x,y,w,h,t,c,fill=None):
    p.draw_rect(fitz.Rect(x,y,x+w,y+h),color=rgb(c),fill=rgb(fill or "#FFFFFF"),radius=0.12,width=1)
    p.insert_htmlbox(fitz.Rect(x+3,y+2,x+w-3,y+h-1),t,css=CSS+"body{text-align:center;font-size:7.8pt;line-height:1.2}")
def arrow(x1,y1,x2,y2):
    p.draw_line((x1,y1),(x2,y2),color=rgb("#80868B"),width=1); 
    import math; a=math.atan2(y2-y1,x2-x1)
    for s in (0.45,-0.45): p.draw_line((x2,y2),(x2-6*math.cos(a-s),y2-6*math.sin(a-s)),color=rgb("#80868B"),width=1)
node(39,140,100,52,"<b>Customer</b><br>WhatsApp voice, photo, text",B)
node(39,205,100,52,"<b>Agency, technician</b><br>WhatsApp + light web app (PWA)",B)
node(39,270,100,52,"<b>Plan provider, OEM</b><br>claims console (Phase 2)",B)
node(175,140,150,100,"<b>Keepwell orchestrator</b><br>Cloud Run API + <b>ADK agents</b><br>idempotent events, retries, per-job cost guard",G,"#E6F4EA")
node(175,252,150,70,"<b>Human approval gates</b><br>quote, warranty, safety release, data sharing",R,"#FCE8E6")
node(365,138,150,50,"<b>Gemini Flash / Flash-Lite</b><br>voice, vision, extraction, quote and brief text, close-out",B,"#E8F0FE")
node(365,196,150,44,"<b>Rules engine (code)</b><br>warranty, pricing, safety hard-stop, consent",Y,"#FEF7E0")
node(365,248,150,44,"<b>Grounded retrieval</b><br>manuals + fault codes: Postgres pgvector, text-embedding-005",B,"#E8F0FE")
node(365,300,150,40,"<b>Google Maps Routes / Route Optimization</b><br>travel time, schedule",G,"#E6F4EA")
node(555,138,126,60,"<b>Cloud SQL (Postgres)</b><br>jobs, appliances, Home Memory, audit log",B)
node(555,206,126,50,"<b>Cloud Storage</b><br>voice, photos, invoices (consent, retention)",B)
node(555,264,126,50,"<b>Pub/Sub + Cloud Tasks</b><br>events, reminders, retries",B)
node(555,322,126,46,"<b>Evals + monitoring</b><br>ADK evals, Gen AI Evaluation, logs",R,"#FCE8E6")
for y in (166,231,296): arrow(139,y,175,190 if y<250 else 285)
arrow(325,190,365,165); arrow(325,200,365,218); arrow(325,215,365,270); arrow(325,235,365,318)
arrow(515,165,555,168); arrow(515,218,555,230); arrow(515,270,555,288)
text(p,39,338,500,50,"<span class='s'>Design choices: Mumbai (asia-south1) first; pgvector instead of a managed retrieval product so retrieval is portable and region-pinned; Gemini calls through Vertex AI where a model is available in-region, AI Studio for prototyping. WhatsApp Cloud API is the non-Google channel. Model names and Mumbai availability will be confirmed before we lock.</span>")
# 4 tools
p=doc[4]; clear(p)
card(p,39,134,206,200,"<h4>Google AI Studio</h4><b>Planned use</b><ul><li>Prototype and tune each system prompt (intake, label reading, quote text, close-out)</li><li>Test structured-output JSON schemas on real Indian-language voice notes and invoice photos</li><li>Compare Flash vs Flash-Lite on our golden set before we pick models</li><li>Generate API keys and the first working demo</li></ul>",B)
card(p,257,134,206,200,"<h4>Google Antigravity</h4><b>Planned use</b><ul><li>Agent-driven build of the backend, WhatsApp webhook and agency web app during the 48-hour City Buildathon</li><li>Agents write and run tests against our eval cases while we review diffs</li><li>Keeps the spec, prompts and code in one workspace</li></ul>",R)
card(p,475,134,206,200,"<h4>Google Agent Skills</h4><b>Planned use</b><ul><li>Package repair knowledge as reusable skills: warranty rules, safety hard-stop checklist, Hindi/Telugu/Tamil appliance glossary, quote format</li><li>Agents load a skill only when needed, keeping prompts short and cheap</li><li>Same skills are reused by the eval runner</li></ul>",G)
card(p,39,342,642,46,"<b>Also in the stack:</b> Agent Development Kit (agents, evals, A2A/MCP), Vertex AI, Cloud Run, Cloud SQL, Cloud Storage, Pub/Sub, Google Maps Platform. <span class='s'>We have not yet confirmed which of these tools the team has already used; this slide states planned use.</span>",Y)
# 5 models
p=doc[5]; clear(p)
rows=[("Gemini 3.8 Flash (Mumbai in-region Flash variant to be confirmed)","Intake extraction, label and invoice reading, diagnosis hypotheses, quote and brief text, job close-out","Best cost per job at acceptable quality; structured JSON output"),
("Gemini 3.5 Flash-Lite","Language ID, routing, safety second-reader, reminders","Cheapest tier; cuts AI cost about 46-52% vs Flash on our model"),
("Gemini audio understanding; Chirp 3 (consented, US/EU regions only)","Hindi and regional voice notes: transcribe, then extract","Audio about 32 tokens/sec; Chirp 3 only where the customer consents"),
("Gemini 3.8 Live","Later: live voice calls with technicians and customers","Preview; audio sessions limited to 15 minutes, so not in release 1"),
("text-embedding-005 (Gemini Embedding 2 later)","Retrieval over manuals, fault codes, plan terms","India-listed embedding; negligible cost"),
("Gemini Pro tier (opt-in, redacted)","Hard claim summaries only","No Pro model in Mumbai, so out-of-region and consent-gated")]
html="<table width='100%' cellspacing='0'><tr style='background:#4285F4'><th width='27%'>Model</th><th width='38%'>Used for</th><th>Why</th></tr>"
for i,(a,b,c) in enumerate(rows):
    bg="#F8F9FA" if i%2==0 else "#FFFFFF"
    html+=f"<tr style='background:{bg}'><td><b>{a}</b></td><td>{b}</td><td>{c}</td></tr>"
text(p,39,132,642,230,html+"</table>")
text(p,39,362,642,30,"<span class='s'>Modelled AI cost is about Rs 1.5-5.5 per job on 2026 prices (assumed token counts, to be measured). Flash prices double on 1 Jan 2027, so the Rs 40 per-fix fee is tested at 2027 prices. Model names and regional availability to be re-checked before launch.</span>")
# 6 business
p=doc[6]; title(p,"Business Model and Market","Who pays, how, and why the unit economics work.")
rows=[("R1 Per-fix AI desk fee","Agency","Rs 40 per completed job card (test Rs 100)","Phase 1"),
("R3 Plan / AMC commission","Plan provider, agency","10-20% of plan sold via Home Memory","Phase 1.5-2"),
("R4 Parts referral","Parts sellers","3-8% of matched orders","Phase 1.5"),
("R5 Claims triage","Warranty administrators, OEMs","Rs 30-100 per claim","Phase 2"),
("R6 Service lead routing","OEMs, plan providers","Rs 100-250 per completed job","Phase 2"),
("R8 Data and insights","OEMs, administrators","Contract; consent-first","Phase 3")]
html="<table width='100%' cellspacing='0'><tr style='background:#34A853'><th width='27%'>Revenue stream</th><th width='24%'>Payer</th><th width='33%'>Model</th><th>Phase</th></tr>"
for i,r in enumerate(rows):
    bg="#F8F9FA" if i%2==0 else "#FFFFFF"
    html+=f"<tr style='background:{bg}'>"+"".join(f"<td>{c}</td>" for c in r)+"</tr>"
text(p,39,130,642,150,html+"</table>")
card(p,39,284,205,104,"<h4>Unit economics (modelled)</h4>Variable cost Rs 1.5-5.5 per job; gross margin about 76-94% at Rs 40, 90-98% at Rs 100. Worst case is a warranty claim on 2027 prices.",B)
card(p,254,284,205,104,"<h4>Illustrative scale</h4>One agency at 3 jobs a day earns us about Rs 36,000 a year. 1,000 agencies is about Rs 3.6 Cr; the stacked ceiling is about Rs 110 Cr a year. <span class='s'>All assumptions, not forecasts.</span>",G)
card(p,469,284,212,104,"<h4>Go-to-market</h4>Tier 2/3 city agencies first (least software, least competition from Urban Company and OEM networks), then Tier 1 where plan sellers and OEMs sit.",Y)
# 7 responsible AI, eval, validation
p=doc[7]; title(p,"Trust, Evaluation and Next Steps","How we keep it safe, measure quality and prove demand.")
card(p,39,130,206,258,"<h4>Responsible AI</h4><ul><li>Human approves quotes, warranty decisions, safety releases and data sharing</li><li>Deterministic safety hard-stops the AI cannot clear (gas, refrigerant, high voltage); list to be reviewed by electricians and gas-safety experts</li><li>Consent ledger, redaction and retention for voice and photos (DPDP Act and Rules; lawyer review of roles)</li><li>Complaint help is an evidence pack, not legal advice</li><li>Prompt-injection defences: customer content treated as data</li></ul>",R)
card(p,254,130,206,258,"<h4>Evaluation</h4><ul><li>Golden datasets per feature and language (Hindi, Telugu, Tamil, Kannada, Marathi)</li><li>Three layers: assertions (hard rules), rubric scoring, agent-trajectory checks</li><li>ADK evals and Vertex Gen AI Evaluation in CI; release gates on safety false-accepts and field accuracy</li><li>LLM judge calibrated against human labels</li><li>Before/after eval results shown live in the demo</li></ul>",B)
card(p,469,130,212,258,"<h4>Next steps (validation first)</h4><ul><li>Interview 15-20 agencies in 1-2 Tier 2 cities</li><li>Paid pilot at Rs 40 and Rs 100 per fix; measure cost per job and revisit rate</li><li>Vernacular voice accuracy tests on real recordings</li><li>Two administrator or OEM interviews before building claims triage</li><li>Confirm plan-selling and licensing rules</li></ul><span class='s'>No pilot data yet; figures here are modelled assumptions.</span><br><br><b>Team:</b> Prathyusha Kalluri, Sri Charan Peri, Kavyanth Munagala (IIIT Hyderabad)",G)
doc.save(OUT,garbage=4,deflate=True)
