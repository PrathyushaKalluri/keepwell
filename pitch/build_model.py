import sys
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.comments import Comment
from openpyxl.utils import get_column_letter

OUT = sys.argv[1]
wb = Workbook()

F = "Arial"
BLUE = Font(name=F, size=10, color="0000FF")
BLACK = Font(name=F, size=10, color="000000")
GREEN = Font(name=F, size=10, color="008000")
BOLD = Font(name=F, size=10, bold=True)
TITLE = Font(name=F, size=14, bold=True)
HDR = Font(name=F, size=10, bold=True, color="FFFFFF")
HDR_FILL = PatternFill("solid", fgColor="1F3864")
SEC_FILL = PatternFill("solid", fgColor="D9E1F2")
YELLOW = PatternFill("solid", fgColor="FFFF00")
TOP = Border(top=Side(style="thin"))

NUM_L = '#,##0.0;(#,##0.0);"-"'      # ₹ lakh
NUM_0 = '#,##0;(#,##0);"-"'
NUM_RS = '"₹"#,##0;("₹"#,##0);"-"'
NUM_RS1 = '"₹"#,##0.0;("₹"#,##0.0);"-"'
PCT = '0.0%;(0.0%);"-"'
MULT = '0.0"x"'
NUM_CR = '#,##0.00;(#,##0.00);"-"'

YCOLS = ["C", "D", "E", "F", "G"]
YEARS = ["Y1 (Dec 26–Nov 27)", "Y2", "Y3", "Y4", "Y5"]

REF = {}  # key -> absolute ref on Assumptions


def style_all(ws):
    for row in ws.iter_rows():
        for c in row:
            if c.font is None or c.font.name != F:
                c.font = Font(name=F, size=c.font.size if c.font else 10, bold=c.font.bold if c.font else False,
                              color=c.font.color if c.font else None)


def header(ws, r, labels, start_col=1):
    for i, l in enumerate(labels):
        c = ws.cell(row=r, column=start_col + i, value=l)
        c.font = HDR
        c.fill = HDR_FILL
        c.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)


def section(ws, r, text, ncols=9):
    for col in range(1, ncols + 1):
        ws.cell(row=r, column=col).fill = SEC_FILL
    c = ws.cell(row=r, column=1, value=text)
    c.font = BOLD


# ---------------------------------------------------------------- Assumptions
A = wb.active
A.title = "Assumptions"
A["A1"] = "Keepwell — Assumptions (every input lives here)"
A["A1"].font = TITLE
A["A2"] = "Blue = input you can change · Yellow fill = still to be decided in a pitch step · Money in ₹ lakh (L) unless the unit says ₹. 1 Cr = 100 L."
A["A2"].font = Font(name=F, size=9, italic=True)
header(A, 4, ["Input", "Unit", "Value / Y1", "Y2", "Y3", "Y4", "Y5", "Tag", "Source / note (decided in step)"])
r = 5


def scalar(key, label, unit, val, fmt, tag, note, decide=True):
    global r
    A.cell(row=r, column=1, value=label).font = BLACK
    A.cell(row=r, column=2, value=unit).font = BLACK
    c = A.cell(row=r, column=3, value=val)
    c.font = BLUE
    c.number_format = fmt
    if decide:
        c.fill = YELLOW
    A.cell(row=r, column=8, value=tag).font = BLACK
    A.cell(row=r, column=9, value=note).font = BLACK
    REF[key] = f"Assumptions!$C${r}"
    r += 1


def yearly(key, label, unit, vals, fmt, tag, note, decide=True):
    global r
    A.cell(row=r, column=1, value=label).font = BLACK
    A.cell(row=r, column=2, value=unit).font = BLACK
    for i, v in enumerate(vals):
        c = A.cell(row=r, column=3 + i, value=v)
        c.font = BLUE
        c.number_format = fmt
        if decide:
            c.fill = YELLOW
    A.cell(row=r, column=8, value=tag).font = BLACK
    A.cell(row=r, column=9, value=note).font = BLACK
    REF[key] = r  # row number; column per year
    r += 1


def sec(text):
    global r
    r += 1
    section(A, r, text)
    r += 1


sec("1. General")
scalar("tax", "Corporate tax rate (on positive EBIT)", "%", 0.25, PCT, "Model", "Indian new-regime rate ~25%; loss carry-forward ignored for simplicity", False)
scalar("ctc_growth", "Annual salary increase", "%", 0.08, PCT, "Model", "Step 7")
scalar("agencies_now", "Paying/pilot agencies at start of Y1", "agencies", 5, NUM_0, "Story", "Step 2: 5-agency paid pilot (repo design: 3–5 agencies at ₹40 vs ₹100); Step 6 confirms")

sec("2. Market sizing (Step 4)")
scalar("techs", "Appliance/AC repair technicians in India (base)", "people", 250000, NUM_0, "Real+Model", "ICAP (govt): ~2,00,000 RAC service technicians, mostly informal; CEEW: skilled AC technician demand ~0.37M. Base 2.5L covers AC + fridge + washing machine")
scalar("techs_low", "Technicians — low case", "people", 200000, NUM_0, "Real", "ICAP estimate (RAC only)", False)
scalar("techs_high", "Technicians — high case", "people", 370000, NUM_0, "Real", "CEEW skilled AC technician requirement (repo)", False)
scalar("share_in_agencies", "Share of technicians working in agencies of 2–10 technicians", "%", 0.60, PCT, "DRAFT", "Assumption: rest are solo or brand/platform-employed. Validate in agency interviews (repo validate-first list)")
scalar("techs_per_agency", "Technicians per agency (average)", "people", 4, NUM_0, "DRAFT", "Repo persona: owner-run, 2–10 technicians")
scalar("nonmetro", "Share of agencies in Tier 2/3 (non-metro) towns", "%", 0.60, PCT, "Real+Model", "Blue Star: ~70% of sales non-metro (FY25); Redseer: Tier 2+ = 68% of incremental durables sales. 60% used for the installed base")
scalar("beachhead_share", "Telangana + Andhra Pradesh share of non-metro agencies", "%", 0.062, PCT, "Model", "Population share: TS ~3.8 Cr + AP ~5.3 Cr of ~147.7 Cr (UN WPP 2026)")
scalar("south_share", "Four southern states (TS, AP, KA, TN) share", "%", 0.16, PCT, "Model", "Population share ~23.6 Cr of ~147.7 Cr; southern appliance ownership above average, so conservative")
scalar("repair_jobs", "Appliance repair jobs per year, India", "jobs", 150000000, NUM_0, "Real", "Repo: ~150M appliances a year come in for repair (2017, single source). Cross-checked against ₹9,000 Cr ÷ average ticket")
scalar("avg_ticket", "Average repair bill", "₹/job", 600, NUM_RS, "DRAFT", "Visit charge ₹200–500 (case-comp research) plus parts. Used only for the cross-check")
scalar("local_share", "Share of repair jobs done by local (independent) providers", "%", 0.44, PCT, "Real", "LocalCircles: 44% use a local provider for AC servicing (up from 38%); 76% of AC owners avoid brand service")
scalar("fee_low", "Fee per verified fix — low test point (sizing only)", "₹", 40, NUM_RS, "Real", "Repo R1 test range ₹40–100. NOT a pricing decision (pricing deferred)", False)
scalar("fee_high", "Fee per verified fix — high test point (sizing only)", "₹", 100, NUM_RS, "Real", "Repo R1 test range ₹40–100. NOT a pricing decision", False)
scalar("repair_mkt_cr", "India appliance repair market", "₹ Cr/yr", 9000, NUM_0, "Real", "ICICI Direct citing UC DRHP (₹165–170bn install+repair+service FY25, ~half repairs); BlueWeave ~$981M (2023), 8.18% CAGR; Servify est. ~$1B", False)
scalar("devprot_cr", "Device-protection (plans) market, India", "₹ Cr/yr", 10340, NUM_0, "Real", "Servify estimate ~$1.1B (FY24) at ₹94/$ (repo FX). Extended warranty USD 3.6–4.4B is an upper bound (IMARC may include auto)", False)
scalar("appl_share", "Appliance share of device-protection market", "%", 0.30, PCT, "DRAFT", "Device protection is mostly smartphones; appliances assumed ~30% (validate with administrators, E7)")
scalar("plan_comm_low", "Plan commission — low", "%", 0.10, PCT, "Real", "Repo R3: 10–20%", False)
scalar("plan_comm_high", "Plan commission — high", "%", 0.20, PCT, "Real", "Repo R3: 10–20%", False)
scalar("parts_share_bill", "Parts share of the repair bill", "%", 0.35, PCT, "DRAFT", "No source in repo; assumption to validate with parts wholesalers")
scalar("parts_ref_low", "Parts referral — low", "%", 0.03, PCT, "Real", "Repo R4: 3–8%", False)
scalar("parts_ref_high", "Parts referral — high", "%", 0.08, PCT, "Real", "Repo R4: 3–8%", False)
scalar("ftf_global", "First-visit fix rate (global benchmark)", "%", 0.77, PCT, "Real", "Case-comp research: no India rate published; global ~77%", False)
scalar("tech_pay", "Technician pay", "₹/month", 19408, NUM_RS, "Real", "Indeed (case-comp research); field AC technicians ₹18–30k (repo, weak source)", False)
scalar("wasted_hours", "Technician time lost per wasted trip", "hours", 1.125, '0.00', "DRAFT", "Case-comp assumption: 45–90 minutes (midpoint)")
scalar("travel_cost", "Travel cost per wasted trip", "₹", 50, NUM_RS, "DRAFT", "Assumption: fuel/fare within town")
scalar("machines", "Fridges, washing machines and ACs in Indian homes", "machines", 270000000, NUM_0, "Real", "~335M households (Data for India 2024) × fridge ~50% + washing machine ~20% + AC ~10–13% (CLASP/BEE 2024; Ken Research 52/23/10) ≈ 268–285M")

sec("3. Circuit pricing and usage (Step 7)")
scalar("jobs_month", "Jobs per agency per month", "jobs", 145, NUM_0, "Model", "Step 4 triangulation: 150M jobs × 44% local ÷ ~37,500 agencies ≈ 147/month; repo problem map: 100 (small) / 250 (mid). Pilot (Step 6) confirms")
scalar("paid_share", "Share of jobs that become a verified (billable) fix", "%", 0.82, PCT, "Story", "Pilot: 82% of routed jobs verified by the technician (Step 6)")
scalar("fee_fix", "Fee per verified fix", "₹", 40, NUM_RS, "DRAFT", "RECOMMENDED, not decided (Step 7). Pilot: value = 2x fee at ~₹43; ₹100 arm failed; interviews ₹30–50; repo R1 ₹40")
scalar("sub_month", "Optional Desk Pro add-on (owner reports, reminders, quote templates)", "₹/month", 399, NUM_RS, "DRAFT", "RECOMMENDED. Repo R2: optional ₹300–500/month; 3 of 18 interviewed owners prefer a flat fee")
scalar("desk_adopt", "Share of paying agencies taking Desk Pro", "%", 0.25, PCT, "DRAFT", "Assumption; E1 tests it")
scalar("free_days", "Free trial for new agencies", "days", 30, NUM_0, "DRAFT", "RECOMMENDED 30 (one-pager said 60): per-fix pricing already removes the risk, and the pilot reached 85% routing in 4 weeks")

sec("4. Cost to serve (Step 7)")
scalar("ai_job", "AI cost per job (LLM + voice), at 2027 prices", "₹/job", 4.5, NUM_RS1, "Model", "Repo CTE: job mix 50% simple / 35% parts / 15% warranty → Flash-2027 ₹5.10, Lite-cached ₹1.22; routed ~50/50 = ₹3.2 + Pro escalations ~₹0.3 + 25% margin ≈ ₹4.5. Pilot measured ₹3.1 at 2026 prices")
scalar("msg_job", "WhatsApp / telephony cost per job", "₹/job", 1.2, NUM_RS1, "Model", "Repo CTE §3: 3–8 utility msgs × ₹0.115 = ₹0.35–0.92 ex-GST; +18% GST and BSP markup (~₹0.15/msg) → ₹1.2", False)
scalar("support_month", "Support tooling per agency", "₹/agency/month", 100, NUM_RS, "DRAFT", "Helpdesk tools and calls only; support PEOPLE are in team cost (no double count)")

sec("5. Acquisition and retention (Step 7)")
scalar("cac", "Acquisition cash cost per new agency (excluding people)", "₹/agency", 1000, NUM_RS, "DRAFT", "Parts-wholesaler referral ₹500 + onboarding kit and travel ₹500. Field-sales salaries are in team cost; fully loaded CAC is calculated on the P&L")
scalar("rep_prod", "Paying agencies added per field-sales person per year", "agencies", 80, NUM_0, "DRAFT", "10 trials a month × 12 × ~67% converting (E1 target ≥ 70%)")
scalar("referral", "Referred agencies per year, as a share of agencies at start of year", "%", 0.10, PCT, "DRAFT", "Owners refer owners (technician and wholesaler networks)")
scalar("churn_m", "Monthly churn used for LTV (conservative, new-agency rate)", "%", 0.03, PCT, "DRAFT", "Unit economics use the year-1 rate, not the mature rate")

sec("6. Home Memory (Step 7)")
scalar("uniq_hh", "Share of jobs that add a new machine record", "%", 0.60, PCT, "DRAFT", "Repeat customers don't add records")
scalar("consent", "Household consent rate to keep the record", "%", 0.70, PCT, "DRAFT", "DPDP consent-first")

sec("7. Later product lines (Step 7)")
scalar("plan_start", "Service Plans start year", "year #", 2, NUM_0, "DRAFT", "Roadmap")
scalar("plan_attach", "Plans sold per record per year", "%", 0.02, PCT, "DRAFT", "Plan uptake is low single digits (repo); reminder-triggered offers")
scalar("plan_value", "Average plan value", "₹", 2000, NUM_RS, "Real", "Croma ZipCare AC AMC ₹1,999/yr (repo)")
scalar("plan_comm", "Keepwell commission on plan", "%", 0.15, PCT, "DRAFT", "One-pager 15%; repo 10–20%")
scalar("parts_start", "Parts Marketplace start year", "year #", 3, NUM_0, "Model", "Roadmap R4 comes after R3 claims (Step 1)")
scalar("parts_adopt", "Share of agencies buying parts through Keepwell", "%", 0.30, PCT, "DRAFT", "")
scalar("parts_gmv", "Parts bought per adopting agency", "₹/month", 20000, NUM_RS, "DRAFT", "")
scalar("parts_take", "Take rate on parts", "%", 0.05, PCT, "DRAFT", "Repo R4 3–8%; midpoint")
scalar("resale_start", "Resale & Recycling start year", "year #", 5, NUM_0, "Model", "R5 is the vision release (Step 1)")
scalar("resale_rate", "Resale/trade-in deals per 1,000 records per year", "deals", 4, NUM_0, "DRAFT", "")
scalar("resale_value", "Average resale deal value", "₹", 5000, NUM_RS, "Model", "Repo: scrap/exchange ₹800–5,000; refurb sells 50–70% below new. Blend of refurb and scrap")
scalar("resale_take", "Take rate on resale", "%", 0.04, PCT, "DRAFT", "One-pager ~4%")
scalar("data_value", "Claims-triage licence per administrator", "₹ L/yr", 40, NUM_L, "Real", "Repo problem map: ₹40–60L/yr licence + ₹25 per claim (low end used)")
scalar("credit_y1", "Google for Startups credits usable in Y1", "₹ L", 235, NUM_L, "Real", "AI tier: $250k in year 1 at ₹94/$ (Step 3)")
scalar("credit_y2", "Google for Startups credits usable in Y2", "₹ L", 94, NUM_L, "Real", "Up to $100k in year 2 at ₹94/$ (Step 3)")

sec("8. Yearly plan (Steps 6–8)")
yearly("data_contracts", "Claims-triage licences (Data Services)", "#", [0, 0, 1, 2, 4], NUM_0, "DRAFT", "R3 in year 2: LOI in Y2 (E7), first licence Y3")
yearly("churn_yr", "Monthly agency churn, by year", "%", [0.03, 0.03, 0.02, 0.015, 0.015], PCT, "DRAFT", "RECOMMENDED: 3% while new; falls as rate cards, customer histories and habits build up in Circuit (switching costs, Step 5). Series A gate ≥95% monthly")
yearly("hc_founders", "Headcount — founders", "people", [3, 3, 3, 3, 3], NUM_0, "Story", "Step 2")
yearly("hc_tech", "Headcount — product, AI, engineering", "people", [4, 6, 10, 14, 18], NUM_0, "Model", "Lean: covers the repo role list (AI lead, eval, SRE, security, platform, product). Revenue per employee benchmark in P&L")
yearly("hc_ops", "Headcount — agency success, field ops, support", "people", [3, 5, 12, 22, 32], NUM_0, "Model", "~1 per 80–120 agencies")
yearly("hc_sales", "Headcount — field sales (drives agency growth)", "people", [1, 3, 10, 18, 24], NUM_0, "Model", "Funded growth plan: seed funds Y1–Y2; Series A (~month 20) funds faster field sales from Y3. New agencies = field sales × productivity + referrals")
yearly("hc_ga", "Headcount — finance, HR, admin", "people", [1, 2, 3, 5, 7], NUM_0, "DRAFT", "Step 8")
yearly("brand", "Brand, events, content (excl. CAC)", "₹ L", [5, 10, 35, 60, 90], NUM_L, "Model", "Brand rises with the Series A rollout")
yearly("pmf", "PMF programme: pilots, focus groups, analytics, research", "₹ L", [25, 25, 15, 15, 15], NUM_L, "DRAFT", "Course M1: Stage 2 needs PMF money; E1–E8 (Step 6). Costed in Step 8")
yearly("infra", "Cloud, tools, model hosting (fixed)", "₹ L", [6, 12, 25, 45, 70], NUM_L, "Model", "Repo GSM §4.2: pilot all-in ₹12k–35k/month; eval runs ~₹2,300/night. Credits applied separately on the P&L")
yearly("compliance", "Compliance, legal, audit, IP (Y1 includes ₹8L seed transaction costs)", "₹ L", [16, 10, 15, 20, 30], NUM_L, "Model", "Step 8: Y1 = lawyer ₹4L + CA/CS ₹2.4L + valuer ₹0.5L + trademarks ₹0.6L + security review ₹0.5L + seed transaction costs ₹8L (course term sheet: company bears up to ₹12.5L)")
yearly("ga_other", "Office, travel, admin", "₹ L", [8, 14, 22, 32, 45], NUM_L, "DRAFT", "")
yearly("capex", "Capex (devices, field kits)", "₹ L", [5, 8, 12, 18, 25], NUM_L, "DRAFT", "Depreciated over 3 years")

sec("9. Salaries (Step 8)")
scalar("ctc_founders", "Founder salary", "₹ L/yr", 12, NUM_L, "Story", "Below market — skin in the game")
scalar("ctc_tech", "Avg cost per head — product/AI/eng", "₹ L/yr", 18, NUM_L, "DRAFT", "Hyderabad market")
scalar("ctc_ops", "Avg cost per head — ops/field/support", "₹ L/yr", 5, NUM_L, "DRAFT", "")
scalar("ctc_sales", "Avg cost per head — sales/partnerships", "₹ L/yr", 9, NUM_L, "DRAFT", "")
scalar("ctc_ga", "Avg cost per head — finance/HR/admin", "₹ L/yr", 10, NUM_L, "DRAFT", "")

sec("10. Cash and the raise (Steps 2 and 8)")
scalar("cash_open", "Cash in bank at start of Y1", "₹ L", 37, NUM_L, "Story", "Step 2: raised ₹45L (founders ₹15L + iSAFE ₹30L), spent ~₹8L since Oct 2026")
scalar("grants", "Grants counted in the funding gap", "₹ L", 0, NUM_L, "Model", "SISFS ₹20L applied via CIE-IIITH, not yet sanctioned: NOT counted (don't base survival on an unapproved grant). Upside buffer")
scalar("runway", "Runway the raise must fund", "months", 24, NUM_0, "Model", "Step 8: Series A gates reached ~month 15–18 + a 4–6 month Series A process")
scalar("eng_pmf", "Share of engineering cost that runs PMF experiments", "%", 0.50, PCT, "Model", "Use of funds by PURPOSE: AI lead (root-cause accuracy, E2), eval/data engineer (gates, measurement), speech/ML engineer (Telugu/Tamil, E4) = 3 of 6 roles. Backend, WhatsApp and SRE build the product")
scalar("contingency", "Contingency buffer", "%", 0.10, PCT, "Model", "Activity 1 used ~10%", False)
scalar("wc_pct", "Working capital (parts float, payment cycles) as % of revenue", "%", 0.05, PCT, "DRAFT", "")
scalar("round_to", "Round the ask up to the nearest", "₹ L", 25, NUM_L, "Model", "", False)

sec("11. Valuation (Step 9)")
scalar("irr", "Investor target IRR", "%", 0.35, PCT, "Real", "Course M4: seed VC 35–40%. 35% used because the horizon is 6 years (course M2: early VC horizon 5–8 years)")
scalar("horizon", "Years to exit", "years", 6, NUM_0, "Model", "Course M2: early VC 5–8 years; strategic acquirers (Step 9) buy once the record and claims lines are proven")
scalar("exit_mult", "Revenue multiple at exit", "x", 7, MULT, "Real", "Servify ~₹5,660 Cr valuation ÷ ₹781 Cr FY25 revenue ≈ 7.2x (repo); course SaaS 3–8x ARR")
scalar("later_dil", "Dilution from Series A and B before exit", "%", 0.32, PCT, "Model", "1 − (1 − 20% A) × (1 − 15% B), as in the cap table")
scalar("g6", "Revenue growth in Y6", "%", 0.60, PCT, "DRAFT", "Decelerating from Y5 growth of ~104%")
scalar("g7", "Revenue growth in Y7", "%", 0.40, PCT, "DRAFT", "Continues the deceleration")
scalar("comp1", "Comparable 1: Hisabkitab (AI accounting for small firms), seed, Jul 2026", "₹ Cr post-money", 20, NUM_CR, "Real", "Deal-tracker report; closest SMB vertical-AI seed comparable")
scalar("comp2", "Comparable 2: Unveilr AI (AI search agents), pre-seed, Oct 2026", "₹ Cr post-money", 16.7, NUM_CR, "Real", "Ascendants / SaaSRise; earlier stage than us")
scalar("comp3", "Comparable 3: Indian seed market midpoint", "₹ Cr post-money", 37.6, NUM_CR, "Real", "Kae Capital guide: seed post-money $2–8M; midpoint $4M at ₹94/$")
scalar("bench_score", "Scorecard benchmark score", "/100", 80, NUM_0, "Real", "Course M4 example", False)
scalar("our_score", "Keepwell fundability score", "/100", 76, NUM_0, "Model", "Step 11 self-score: Market 12/15, Product 22/30, Startup 35/45, X-factor 7/10")

sec("12. Cap table (Step 9)")
scalar("sh_f1", "Shares — Sri Charan Peri (CTO)", "shares", 450000, NUM_0, "Story", "Step 2: 30% of founder equity; ₹4.5L at ₹1 face value")
scalar("sh_f2", "Shares — Prathyusha Kalluri (CEO)", "shares", 600000, NUM_0, "Story", "Step 2: 40% of founder equity (team decision); ₹6L at ₹1 face value")
scalar("sh_f3", "Shares — Kavyanth Munagala (COO)", "shares", 450000, NUM_0, "Story", "Step 2: 30% of founder equity; ₹4.5L at ₹1 face value")
scalar("isafe_amt", "Pre-seed iSAFE amount (2 operator angels)", "₹ L", 30, NUM_L, "Story", "Step 2")
scalar("isafe_cap", "iSAFE post-money valuation cap", "₹ Cr", 10, NUM_CR, "Story", "Step 2; converts at seed")
scalar("isafe_disc", "iSAFE discount to seed price", "%", 0.20, PCT, "Story", "Applies only if it gives a lower price than the cap")
scalar("esop", "ESOP pool, % of post-seed fully diluted", "%", 0.10, PCT, "DRAFT", "Course: 5–15% pool")
scalar("dil_a", "Series A dilution", "%", 0.20, PCT, "DRAFT", "")
scalar("dil_b", "Series B dilution", "%", 0.15, PCT, "DRAFT", "")

sec("13. Pilot (Step 6) — 5 agencies, 4 weeks, Ramagundam–Peddapalli + Karimnagar")
scalar("p_jobs", "Pilot agency jobs per month (median)", "jobs", 125, NUM_0, "Story", "18 interviews: median 125 (range 60–260); Step 4 model 145")
scalar("p_routed", "Share of jobs routed through Circuit by week 4", "%", 0.85, PCT, "Story", "Ramp 45% → 85% over 4 weeks")
scalar("p_lost", "Requests agencies say they lose today (missed calls, unanswered voice notes)", "%", 0.125, PCT, "Story", "Interviews: about 1 in 8")
scalar("p_recovered", "Extra jobs captured by Circuit (share of monthly jobs)", "%", 0.08, PCT, "Story", "About two-thirds of the lost 12.5%")
scalar("p_margin", "Agency margin per job", "₹", 240, NUM_RS, "DRAFT", "₹600 average bill × ~40% margin")
scalar("p_ftf_before", "One-visit closure — agency's own baseline", "%", 0.71, PCT, "Story", "2 weeks of agency logs before go-live (repo primary metric)")
scalar("p_ftf_after", "One-visit closure — weeks 3–4 with Circuit", "%", 0.84, PCT, "Story", "Early; ~400 Circuit jobs")
scalar("p_admin_hrs", "Owner time saved per day (quoting, coordination)", "hours", 0.75, '0.00', "Story", "Owner self-report")
scalar("p_owner_rate", "Value of owner time", "₹/hour", 150, NUM_RS, "DRAFT", "Assumption")
scalar("p_verified", "Share of routed jobs the technician verified", "%", 0.82, PCT, "Story", "Close to the model's 80% billable share")
scalar("p_fee_a", "Fee arm A (3 agencies)", "₹/verified fix", 40, NUM_RS, "Real", "Repo pilot design", False)
scalar("p_fee_b", "Fee arm B (2 agencies)", "₹/verified fix", 100, NUM_RS, "Real", "Repo pilot design", False)

A.column_dimensions["A"].width = 58
A.column_dimensions["B"].width = 16
for col in "CDEFG":
    A.column_dimensions[col].width = 13
A.column_dimensions["H"].width = 9
A.column_dimensions["I"].width = 70
A.freeze_panes = "C5"


def y(key, i):
    """yearly input reference for year index i (0-4)"""
    return f"Assumptions!${YCOLS[i]}${REF[key]}"


def s(key):
    return REF[key]


# ---------------------------------------------------------------- Revenue Build
R = wb.create_sheet("Revenue Build")
R["A1"] = "Revenue build — agencies, jobs, records and six revenue lines (₹ lakh)"
R["A1"].font = TITLE
header(R, 3, ["Line", "Unit"] + YEARS)
rows = {}
rr = 4


def line(key, label, unit, fn, fmt=NUM_L, bold=False, green=False):
    global rr
    R.cell(row=rr, column=1, value=label).font = BOLD if bold else BLACK
    R.cell(row=rr, column=2, value=unit).font = BLACK
    for i in range(5):
        c = R.cell(row=rr, column=3 + i, value=fn(i))
        c.number_format = fmt
        c.font = GREEN if green else (BOLD if bold else BLACK)
        if bold:
            c.border = TOP
    rows[key] = rr
    rr += 1


def rc(key, i):
    return f"{YCOLS[i]}{rows[key]}"


def prev(key, i):
    return f"{YCOLS[i-1]}{rows[key]}"


line("yr", "Year number", "#", lambda i: i + 1, NUM_0)
section(R, rr, "Agencies", 7); rr += 1
line("ag_begin", "Paying agencies — start of year", "agencies",
     lambda i: f"={s('agencies_now')}" if i == 0 else 0, NUM_0)
line("new_ag", "New paying agencies (field sales × productivity + referrals)", "agencies",
     lambda i: f"={y('hc_sales', i)}*{s('rep_prod')}+{rc('ag_begin', i)}*{s('referral')}", NUM_0)
line("churn_y", "Annual churn rate", "%", lambda i: f"=1-(1-{y('churn_yr', i)})^12", PCT)
line("churned", "Agencies lost in year", "agencies",
     lambda i: f"={rc('ag_begin', i)}*{rc('churn_y', i)}+{rc('new_ag', i)}*{rc('churn_y', i)}/2", NUM_0)
line("ag_end", "Paying agencies — end of year", "agencies",
     lambda i: f"={rc('ag_begin', i)}+{rc('new_ag', i)}-{rc('churned', i)}", NUM_0, bold=True)
for i in range(1, 5):
    R[f"{YCOLS[i]}{rows['ag_begin']}"] = f"={YCOLS[i-1]}{rows['ag_end']}"
line("avg_ag", "Average agencies in year", "agencies", lambda i: f"=({rc('ag_begin', i)}+{rc('ag_end', i)})/2", NUM_0)
line("paid_ag", "Paid agency-years (after free trial)", "agency-yrs",
     lambda i: f"=MAX(0,{rc('avg_ag', i)}-{rc('new_ag', i)}*{s('free_days')}/365)", NUM_0)
line("paid_frac", "Paid share of agency time", "%", lambda i: f"=IF({rc('avg_ag', i)}=0,0,{rc('paid_ag', i)}/{rc('avg_ag', i)})", PCT)
line("jobs", "Jobs handled by Circuit", "jobs", lambda i: f"={rc('avg_ag', i)}*{s('jobs_month')}*12", NUM_0)
section(R, rr, "Home Memory", 7); rr += 1
line("rec_new", "New machine records created", "records", lambda i: f"={rc('jobs', i)}*{s('uniq_hh')}*{s('consent')}", NUM_0)
line("rec_cum", "Machine records — cumulative", "records",
     lambda i: f"={rc('rec_new', i)}" if i == 0 else 0, NUM_0)
for i in range(1, 5):
    R[f"{YCOLS[i]}{rows['rec_cum']}"] = f"={YCOLS[i-1]}{rows['rec_cum']}+{YCOLS[i]}{rows['rec_new']}"
section(R, rr, "Revenue (₹ lakh)", 7); rr += 1
line("rev_sub", "Circuit — Desk Pro add-on", "₹ L", lambda i: f"={rc('paid_ag', i)}*{s('desk_adopt')}*{s('sub_month')}*12/100000")
line("rev_fix", "Circuit — per verified fix", "₹ L",
     lambda i: f"={rc('jobs', i)}*{s('paid_share')}*{s('fee_fix')}*{rc('paid_frac', i)}/100000")
line("rev_plan", "Service Plans — commission", "₹ L",
     lambda i: f"=IF({rc('yr', i)}>={s('plan_start')},{rc('rec_cum', i)}*{s('plan_attach')}*{s('plan_value')}*{s('plan_comm')}/100000,0)")
line("rev_parts", "Parts Marketplace — take", "₹ L",
     lambda i: f"=IF({rc('yr', i)}>={s('parts_start')},{rc('avg_ag', i)}*{s('parts_adopt')}*{s('parts_gmv')}*12*{s('parts_take')}/100000,0)")
line("rev_resale", "Resale & Recycling — take", "₹ L",
     lambda i: f"=IF({rc('yr', i)}>={s('resale_start')},{rc('rec_cum', i)}/1000*{s('resale_rate')}*{s('resale_value')}*{s('resale_take')}/100000,0)")
line("rev_data", "Data Services — claims-triage licences", "₹ L", lambda i: f"={y('data_contracts', i)}*{s('data_value')}")
line("rev_total", "Total revenue", "₹ L",
     lambda i: f"=SUM({YCOLS[i]}{rows['rev_sub']}:{YCOLS[i]}{rows['rev_data']})", bold=True)
line("rev_circuit_share", "Circuit share of revenue", "%",
     lambda i: f"=IF({rc('rev_total', i)}=0,0,({rc('rev_sub', i)}+{rc('rev_fix', i)})/{rc('rev_total', i)})", PCT)
line("growth", "Revenue growth", "%",
     lambda i: "" if i == 0 else f"=IF({prev('rev_total', i)}=0,0,{rc('rev_total', i)}/{prev('rev_total', i)}-1)", PCT)
R.column_dimensions["A"].width = 46
R.column_dimensions["B"].width = 12
for col in YCOLS:
    R.column_dimensions[col].width = 17
R.freeze_panes = "C4"
RB = rows.copy()


def rb(key, i):
    return f"'Revenue Build'!{YCOLS[i]}{RB[key]}"


# ---------------------------------------------------------------- P&L
P = wb.create_sheet("P&L and Cash")
P["A1"] = "5-year P&L and cash (₹ lakh)"
P["A1"].font = TITLE
header(P, 3, ["Line", "Unit"] + YEARS)
rows = {}
rr = 4
R_ws = R


def pline(key, label, unit, fn, fmt=NUM_L, bold=False, green=False):
    global rr
    P.cell(row=rr, column=1, value=label).font = BOLD if bold else BLACK
    P.cell(row=rr, column=2, value=unit).font = BLACK
    for i in range(5):
        v = fn(i)
        c = P.cell(row=rr, column=3 + i, value=v)
        c.number_format = fmt
        c.font = GREEN if green else (BOLD if bold else BLACK)
        if bold:
            c.border = TOP
    rows[key] = rr
    rr += 1


def pc(key, i):
    return f"{YCOLS[i]}{rows[key]}"


pline("yr", "Year number", "#", lambda i: f"={rb('yr', i)}", NUM_0, green=True)
section(P, rr, "Revenue", 7); rr += 1
pline("rev", "Total revenue", "₹ L", lambda i: f"={rb('rev_total', i)}", green=True)
section(P, rr, "Cost of revenue", 7); rr += 1
pline("cogs_ai", "AI cost (Gemini, voice)", "₹ L", lambda i: f"={rb('jobs', i)}*{s('ai_job')}/100000")
pline("cogs_msg", "WhatsApp messaging", "₹ L", lambda i: f"={rb('jobs', i)}*{s('msg_job')}/100000")
pline("cogs_sup", "Agency support", "₹ L", lambda i: f"={rb('avg_ag', i)}*{s('support_month')}*12/100000")
pline("cogs", "Total cost of revenue", "₹ L", lambda i: f"={pc('cogs_ai', i)}+{pc('cogs_msg', i)}+{pc('cogs_sup', i)}", bold=True)
pline("gp", "Gross profit", "₹ L", lambda i: f"={pc('rev', i)}-{pc('cogs', i)}", bold=True)
pline("gm", "Gross margin", "%", lambda i: f"=IF({pc('rev', i)}=0,0,{pc('gp', i)}/{pc('rev', i)})", PCT)
section(P, rr, "Team cost (headcount × cost per head, salaries grow yearly)", 7); rr += 1
for k, lab in [("founders", "Founders"), ("tech", "Product, AI, engineering"), ("ops", "Agency success, field ops, support"),
               ("sales", "Field sales"), ("ga", "Finance, HR, admin")]:
    pline("t_" + k, "Team — " + lab, "₹ L",
          lambda i, k=k: f"={y('hc_' + k, i)}*{s('ctc_' + k)}*(1+{s('ctc_growth')})^({pc('yr', i)}-1)")
pline("team", "Total team cost", "₹ L", lambda i: f"=SUM({YCOLS[i]}{rows['t_founders']}:{YCOLS[i]}{rows['t_ga']})", bold=True)
pline("headcount", "Total headcount", "people",
      lambda i: "=" + "+".join(y('hc_' + k, i) for k in ["founders", "tech", "ops", "sales", "ga"]), NUM_0)
section(P, rr, "Other operating expenses (SG&A)", 7); rr += 1
pline("mkt_cac", "Agency acquisition cash (new agencies × non-people CAC)", "₹ L", lambda i: f"={rb('new_ag', i)}*{s('cac')}/100000")
pline("mkt_brand", "Brand, events, content", "₹ L", lambda i: f"={y('brand', i)}", green=True)
pline("pmf", "PMF programme (pilots, focus groups, analytics)", "₹ L", lambda i: f"={y('pmf', i)}", green=True)
pline("infra", "Cloud, tools, hosting", "₹ L", lambda i: f"={y('infra', i)}", green=True)
pline("compl", "Compliance, legal, audit, IP", "₹ L", lambda i: f"={y('compliance', i)}", green=True)
pline("ga_o", "Office, travel, admin", "₹ L", lambda i: f"={y('ga_other', i)}", green=True)
pline("credits", "Less: Google for Startups credits (AI + cloud only)", "₹ L",
      lambda i: (f"=-MIN({pc('cogs_ai', i)}+{pc('infra', i)},{s('credit_y1')})" if i == 0 else (f"=-MIN({pc('cogs_ai', i)}+{pc('infra', i)},{s('credit_y2')})" if i == 1 else 0)))
pline("opex", "Total operating expenses (team + SG&A)", "₹ L",
      lambda i: f"={pc('team', i)}+SUM({YCOLS[i]}{rows['mkt_cac']}:{YCOLS[i]}{rows['credits']})", bold=True)
section(P, rr, "Profit", 7); rr += 1
pline("ebitda", "EBITDA", "₹ L", lambda i: f"={pc('gp', i)}-{pc('opex', i)}", bold=True)
pline("ebitda_m", "EBITDA margin", "%", lambda i: f"=IF({pc('rev', i)}=0,0,{pc('ebitda', i)}/{pc('rev', i)})", PCT)
pline("capex", "Capex", "₹ L", lambda i: f"={y('capex', i)}", green=True)
pline("da", "Depreciation and amortisation (3-yr straight line)", "₹ L",
      lambda i: "=(" + "+".join(f"{YCOLS[j]}{rr - 1}" for j in range(max(0, i - 2), i + 1)) + ")/3")
pline("ebit", "EBIT", "₹ L", lambda i: f"={pc('ebitda', i)}-{pc('da', i)}", bold=True)
pline("taxp", "Tax", "₹ L", lambda i: f"=MAX(0,{pc('ebit', i)})*{s('tax')}")
pline("ni", "Net income", "₹ L", lambda i: f"={pc('ebit', i)}-{pc('taxp', i)}", bold=True)
section(P, rr, "Cash", 7); rr += 1
pline("dwc", "Increase in working capital", "₹ L",
      lambda i: f"={pc('rev', i)}*{s('wc_pct')}" if i == 0 else f"=({pc('rev', i)}-{YCOLS[i-1]}{rows['rev']})*{s('wc_pct')}")
pline("fcf", "Free cash flow (negative = burn)", "₹ L",
      lambda i: f"={pc('ebitda', i)}-{pc('capex', i)}-{pc('taxp', i)}-{pc('dwc', i)}", bold=True)
pline("burn_m", "Average monthly burn", "₹ L/month", lambda i: f"=MAX(0,-{pc('fcf', i)})/12")
pline("cash_open", "Opening cash", "₹ L", lambda i: f"={s('cash_open')}" if i == 0 else "")
pline("grants", "Grants received", "₹ L", lambda i: f"={s('grants')}" if i == 0 else 0)
pline("seed", "Seed raise (from Funding Need)", "₹ L", lambda i: "='Funding Need'!$C$22" if i == 0 else 0, green=True)
pline("cash_close", "Closing cash (before Series A)", "₹ L",
      lambda i: f"={pc('cash_open', i)}+{pc('grants', i)}+{pc('seed', i)}+{pc('fcf', i)}", bold=True)
for i in range(1, 5):
    P[f"{YCOLS[i]}{rows['cash_open']}"] = f"={YCOLS[i-1]}{rows['cash_close']}"
pline("ebitda_pos", "EBITDA positive? (1 = yes)", "flag", lambda i: f"=IF({pc('ebitda', i)}>0,1,0)", NUM_0)
pline("cac_full", "Fully loaded CAC per new agency (field sales + acquisition + brand)", "₹",
      lambda i: f"=IF({rb('new_ag', i)}=0,0,({pc('t_sales', i)}+{pc('mkt_cac', i)}+{pc('mkt_brand', i)})*100000/{rb('new_ag', i)})", NUM_RS)
pline("rev_per_head", "Revenue per employee", "₹ L", lambda i: f"=IF({pc('headcount', i)}=0,0,{pc('rev', i)}/{pc('headcount', i)})")
P.cell(row=rr + 1, column=1, value="Break-even year (first year EBITDA > 0)").font = BOLD
P.cell(row=rr + 1, column=3,
       value=f'=IFERROR("Y"&MATCH(1,C{rows["ebitda_pos"]}:G{rows["ebitda_pos"]},0),"Beyond Y5")').font = BOLD
P.cell(row=rr + 2, column=1, value="Lowest closing cash in 5 years (negative = Series A needed)").font = BOLD
c = P.cell(row=rr + 2, column=3, value=f"=MIN(C{rows['cash_close']}:G{rows['cash_close']})")
c.font = BOLD
c.number_format = NUM_L
P.column_dimensions["A"].width = 52
P.column_dimensions["B"].width = 12
for col in YCOLS:
    P.column_dimensions[col].width = 17
P.freeze_panes = "C4"
PL = rows.copy()
PL_BE = rr + 1


def pl(key, i):
    return f"'P&L and Cash'!{YCOLS[i]}{PL[key]}"


# ---------------------------------------------------------------- Unit Economics
U = wb.create_sheet("Unit Economics")
U["A1"] = "Unit economics — one paying agency, steady state (₹ per month)"
U["A1"].font = TITLE
header(U, 3, ["Metric", "Value", "How it's calculated"])
urows = {}
ur = 4


def uline(key, label, formula, fmt, how, bold=False):
    global ur
    U.cell(row=ur, column=1, value=label).font = BOLD if bold else BLACK
    c = U.cell(row=ur, column=2, value=formula)
    c.number_format = fmt
    c.font = BOLD if bold else BLACK
    U.cell(row=ur, column=3, value=how).font = BLACK
    urows[key] = ur
    ur += 1


def ub(key):
    return f"B{urows[key]}"


uline("jobs", "Jobs per month", f"={s('jobs_month')}", NUM_0, "Step 4 triangulation")
uline("rev_sub", "Desk Pro revenue (average across agencies)", f"={s('sub_month')}*{s('desk_adopt')}", NUM_RS, "Add-on price × share taking it")
uline("rev_fix", "Per-fix revenue", f"={ub('jobs')}*{s('paid_share')}*{s('fee_fix')}", NUM_RS, "Jobs × verified share × fee")
uline("arpa", "Revenue per agency (ARPA)", f"={ub('rev_sub')}+{ub('rev_fix')}", NUM_RS, "What one agency pays us per month", True)
uline("var", "AI + messaging cost", f"={ub('jobs')}*({s('ai_job')}+{s('msg_job')})", NUM_RS, "Jobs × cost per job (2027 prices, before credits)")
uline("sup", "Support tooling", f"={s('support_month')}", NUM_RS, "People are in team cost")
uline("contrib", "Contribution per agency", f"={ub('arpa')}-{ub('var')}-{ub('sup')}", NUM_RS, "ARPA − cost to serve", True)
uline("cm", "Contribution margin", f"=IF({ub('arpa')}=0,0,{ub('contrib')}/{ub('arpa')})", PCT, "Contribution ÷ ARPA")
uline("cac", "Fully loaded CAC (Y3, at scale)", f"='P&L and Cash'!E{PL['cac_full']}", NUM_RS, "Field sales + acquisition cash + brand ÷ new agencies (P&L)")
uline("payback", "CAC payback (months, including free trial)",
      f"=IF({ub('contrib')}<=0,\"Never\",{ub('cac')}/{ub('contrib')}+{s('free_days')}/30)", '0.0', "CAC ÷ monthly contribution + free months. Gate ≤ 6 (Step 6)")
uline("life", "Expected agency lifetime (months)", f"=IF({s('churn_m')}=0,0,1/{s('churn_m')})", '0.0', "1 ÷ monthly churn")
uline("ltv", "Lifetime value (LTV), Circuit only", f"={ub('contrib')}*{ub('life')}", NUM_RS, "Contribution × lifetime (excludes plans, parts, claims)", True)
uline("ltv_cac", "LTV : CAC", f"=IF({ub('cac')}=0,0,{ub('ltv')}/{ub('cac')})", MULT, "Healthy if > 3x", True)
uline("rev_job", "Revenue per job", f"=IF({ub('jobs')}=0,0,{ub('arpa')}/{ub('jobs')})", NUM_RS1, "ARPA ÷ jobs")
uline("cost_job", "Cost to serve per job", f"=IF({ub('jobs')}=0,0,({ub('var')}+{ub('sup')})/{ub('jobs')})", NUM_RS1, "")
uline("take", "Our fee as a share of the agency's bill", f"=IF({s('avg_ticket')}=0,0,{s('fee_fix')}/{s('avg_ticket')})", PCT, "vs Urban Company keeping 28.3%")
uline("be_jobs", "Jobs per month to cover cost to serve",
      f"=IFERROR({ub('sup')}/({s('paid_share')}*{s('fee_fix')}-{s('ai_job')}-{s('msg_job')}+IF({ub('jobs')}=0,0,{ub('rev_sub')}/{ub('jobs')})),0)",
      '0.0', "Break-even volume per agency")
ur += 1
U.cell(row=ur, column=1, value="Company level").font = BOLD
ur += 1
uline("be_year", "Break-even year (EBITDA > 0)", f"='P&L and Cash'!C{PL_BE}", "@", "From P&L")
uline("other_rev_ag", "Platform revenue per agency per year, Y5 (plans, parts, resale, claims)", f"=IF({pl('rev', 4)}=0,0,({pl('rev', 4)}-'Revenue Build'!G{RB['rev_sub']}-'Revenue Build'!G{RB['rev_fix']})*100000/'Revenue Build'!G{RB['avg_ag']})", NUM_RS, "From Revenue Build")
uline("be_agencies", "Agencies needed to break even on the Y5 cost base", f"=IFERROR(({pl('opex', 4)}+{pl('cogs', 4)}-{pl('cogs', 4)})*100000/({ub('contrib')}*12+{ub('other_rev_ag')}),0)", NUM_0, "Y5 operating cost ÷ (Circuit contribution + platform revenue per agency)")
uline("y5_rev", "Y5 revenue (₹ L)", f"={pl('rev', 4)}", NUM_L, "From P&L")
uline("y5_ebitda", "Y5 EBITDA margin", f"={pl('ebitda_m', 4)}", PCT, "From P&L")
U.column_dimensions["A"].width = 44
U.column_dimensions["B"].width = 16
U.column_dimensions["C"].width = 50


# ---------------------------------------------------------------- Market
M = wb.create_sheet("Market", 2)
M["A1"] = "Market sizing — bottom-up from technicians and jobs (Step 4)"
M["A1"].font = TITLE
M["A2"] = "No official count of repair agencies exists (repo). We count technicians (ICAP/CEEW), convert to agencies, and cross-check against repair jobs and ₹."
M["A2"].font = Font(name=F, size=9, italic=True)
def mrow(r, label, f, fmt, how, bold=False):
    M.cell(row=r, column=1, value=label).font = BOLD if bold else BLACK
    c = M.cell(row=r, column=2, value=f); c.number_format = fmt; c.font = BOLD if bold else BLACK
    M.cell(row=r, column=3, value=how).font = BLACK
header(M, 4, ["A. Agencies (supply side)", "Value", "How"])
mrow(5, "Technicians (base)", f"={s('techs')}", NUM_0, "ICAP ~2L RAC + other appliances")
mrow(6, "× share in 2–10 technician agencies", f"={s('share_in_agencies')}", PCT, "Assumption")
mrow(7, "÷ technicians per agency", f"={s('techs_per_agency')}", NUM_0, "Repo persona")
mrow(8, "TAM — repair agencies in India", "=B5*B6/B7", NUM_0, "All agencies Circuit could serve", True)
mrow(9, "   low case", f"={s('techs_low')}*0.5/5", NUM_0, "2L technicians, 50% in agencies, 5 per agency")
mrow(10, "   high case", f"={s('techs_high')}*0.7/4", NUM_0, "3.7L technicians, 70% in agencies, 4 per agency")
mrow(11, "SAM — agencies in Tier 2/3 towns (all India)", f"=B8*{s('nonmetro')}", NUM_0, "Our segment; national within 5 years", True)
mrow(12, "Beachhead — Tier 2/3 agencies in Telangana + Andhra Pradesh", f"=B11*{s('beachhead_share')}", NUM_0, "Years 1–2")
mrow(13, "Next ring — Tier 2/3 agencies in the four southern states", f"=B11*{s('south_share')}", NUM_0, "Years 2–3")
mrow(14, "SOM — paying agencies planned by Y5", f"='Revenue Build'!G{RB['ag_end']}", NUM_0, "From the plan (Steps 6–8)", True)
mrow(15, "SOM as share of SAM", "=IF(B11=0,0,B14/B11)", PCT, "Sanity limit: ≤ 20% in 5 years", True)
mrow(16, "Series A gate (~120 agencies) as share of beachhead", "=IF(B12=0,0,120/B12)", PCT, "One-pager milestone")

header(M, 18, ["B. Cross-check (demand side)", "Value", "How"])
mrow(19, "Repair jobs per year, India", f"={s('repair_jobs')}", NUM_0, "Repo (2017, single source)")
mrow(20, "Implied jobs from ₹ market ÷ average ticket", f"={s('repair_mkt_cr')}*10000000/{s('avg_ticket')}", NUM_0, "Should be close to the row above")
mrow(21, "Jobs done by local agencies", f"=B19*{s('local_share')}", NUM_0, "LocalCircles 44%")
mrow(22, "Implied jobs per agency per month", "=IF(B8=0,0,B21/B8/12)", NUM_0, "Repo problem map: 100 (small) – 250 (mid)", True)

header(M, 24, ["C. Revenue pools Keepwell can earn (₹ Cr/yr)", "Low", "High"])
def prow(r, label, lo, hi, how):
    M.cell(row=r, column=1, value=label).font = BLACK
    for col, f in (("B", lo), ("C", hi)):
        M[f"{col}{r}"] = f; M[f"{col}{r}"].number_format = NUM_0
    M.cell(row=r, column=4, value=how).font = BLACK
prow(25, "Circuit fee pool — TAM (all repair jobs × fee)", f"=B19*{s('fee_low')}/10000000", f"=B19*{s('fee_high')}/10000000", "R1 at ₹40 and ₹100 test points")
prow(26, "Circuit fee pool — SAM (local-agency jobs in Tier 2/3)", f"=B21*{s('nonmetro')}*{s('fee_low')}/10000000", f"=B21*{s('nonmetro')}*{s('fee_high')}/10000000", "Our segment")
prow(27, "Service Plans commission pool (R3), appliances only", f"={s('devprot_cr')}*{s('appl_share')}*{s('plan_comm_low')}", f"={s('devprot_cr')}*{s('appl_share')}*{s('plan_comm_high')}", "Device protection ~₹10,340 Cr × ~30% appliances × 10–20%")
prow(28, "Parts referral pool (R4)", f"={s('repair_mkt_cr')}*{s('parts_share_bill')}*{s('parts_ref_low')}", f"={s('repair_mkt_cr')}*{s('parts_share_bill')}*{s('parts_ref_high')}", "Repair ₹ × parts share × 3–8%")
prow(29, "Keepwell earnable pool — TAM (rows 25 + 27 + 28)", "=B25+B27+B28", "=C25+C27+C28", "Claims triage, resale and data not sized (no India data)")
for col in "BC":
    M[f"{col}29"].font = BOLD
M["A30"] = "Earnable pool in USD million (₹94/$)"; M["B30"] = "=B29*10/94"; M["C30"] = "=C29*10/94"
for col in "BC":
    M[f"{col}30"].number_format = NUM_0

header(M, 32, ["D. Problem scale (for the problem slide)", "Value", "How"])
mrow(33, "Repeat visits per year (global first-visit fix 77%)", f"=B19*(1-{s('ftf_global')})", NUM_0, "No India rate exists; global benchmark")
mrow(34, "Cost per wasted trip (₹)", f"={s('tech_pay')}/200*{s('wasted_hours')}+{s('travel_cost')}", NUM_RS, "Pay ÷ 200 hours × time lost + travel")
mrow(35, "Cost of wasted trips per year (₹ Cr)", "=B33*B34/10000000", NUM_0, "The waste Circuit attacks", True)
mrow(36, "Machines in Indian homes with no shared record", f"={s('machines')}", NUM_0, "Home Memory's raw material")
M.column_dimensions["A"].width = 58
M.column_dimensions["B"].width = 18
M.column_dimensions["C"].width = 52
M.column_dimensions["D"].width = 50

# ---------------------------------------------------------------- Pilot
PT = wb.create_sheet("Pilot")
PT["A1"] = "Pilot economics — value to one agency vs our fee (₹ per agency per month, Step 6)"
PT["A1"].font = TITLE
PT["A2"] = "Pilot figures are Story (assumed for the pitch), built on the repo's pilot design. This tab tests the repo's #1 risk: does the agency get more value than it pays?"
PT["A2"].font = Font(name=F, size=9, italic=True)
header(PT, 4, ["Line", "Value", "How"])
prows = [
    (5, "Jobs per month", f"={s('p_jobs')}", NUM_0, "Median pilot agency"),
    (6, "Jobs routed through Circuit", f"=B5*{s('p_routed')}", NUM_0, "Week-4 share"),
    (7, "1. Recovered jobs (would have been lost)", f"=B5*{s('p_recovered')}", '0.0', "Missed calls / voice notes now captured"),
    (8, "   value: recovered jobs × agency margin", f"=B7*{s('p_margin')}", NUM_RS, ""),
    (9, "2. Repeat trips avoided", f"=B6*({s('p_ftf_after')}-{s('p_ftf_before')})", '0.0', "Routed jobs × one-visit improvement"),
    (10, "   value: trips × cost per wasted trip", f"=B9*Market!B34", NUM_RS, "Cost per trip from Market tab"),
    (11, "3. Owner time saved", f"={s('p_admin_hrs')}*26*{s('p_owner_rate')}", NUM_RS, "Hours/day × 26 days × ₹/hour"),
    (12, "Total value to the agency", "=B8+B10+B11", NUM_RS, ""),
    (13, "Verified fixes (billable)", f"=B6*{s('p_verified')}", '0.0', ""),
    (14, "Fee at arm A", f"=B13*{s('p_fee_a')}", NUM_RS, "₹40 per verified fix"),
    (15, "Fee at arm B", f"=B13*{s('p_fee_b')}", NUM_RS, "₹100 per verified fix"),
    (16, "Value ÷ fee, arm A", "=IF(B14=0,0,B12/B14)", MULT, "Want ≥ 2x for an easy yes"),
    (17, "Value ÷ fee, arm B", "=IF(B15=0,0,B12/B15)", MULT, "Below 1x means the agency loses money"),
    (18, "Fee per verified fix where value = 2x fee", "=IF(B13=0,0,B12/2/B13)", NUM_RS, "Input for the Step 7 pricing decision (not a decision)"),
]
for r, lab, f, fmt, how in prows:
    PT.cell(row=r, column=1, value=lab).font = BOLD if r in (12, 16, 17, 18) else BLACK
    c = PT.cell(row=r, column=2, value=f); c.number_format = fmt; c.font = BOLD if r in (12, 16, 17, 18) else BLACK
    PT.cell(row=r, column=3, value=how).font = BLACK
PT.column_dimensions["A"].width = 50
PT.column_dimensions["B"].width = 16
PT.column_dimensions["C"].width = 60

# ---------------------------------------------------------------- Sensitivity
SE = wb.create_sheet("Sensitivity")
SE["A1"] = "Sensitivity — LTV:CAC when each driver moves ±20% (Step 7)"
SE["A1"].font = TITLE
SE["A2"] = "Each row changes one driver and keeps the rest at base. Contribution = Desk Pro + jobs × verified × fee − jobs × (AI + messaging) − support; LTV = contribution ÷ churn."
SE["A2"].font = Font(name=F, size=9, italic=True)
header(SE, 4, ["Driver", "Base value", "LTV:CAC at −20%", "LTV:CAC at +20%", "Swing"])
J=s('jobs_month'); V=s('paid_share'); FE=s('fee_fix'); AI=s('ai_job'); MS=s('msg_job'); SU=s('support_month'); SB=s('sub_month'); DA=s('desk_adopt'); CH=s('churn_m')
CAC="'Unit Economics'!B" + str(urows['cac'])
def ltvcac(j=J, v=V, fe=FE, ai=AI, ms=MS, ch=CH, cac=CAC):
    return f"=IFERROR((({SB}*{DA}+{j}*{v}*{fe}-{j}*({ai}+{ms})-{SU})/{ch})/{cac},0)"
drivers = [
    ("Fee per verified fix", FE, NUM_RS, lambda m: ltvcac(fe=f"({FE}*{m})")),
    ("Jobs per agency per month", J, NUM_0, lambda m: ltvcac(j=f"({J}*{m})")),
    ("Verified share", V, PCT, lambda m: ltvcac(v=f"MIN(1,{V}*{m})")),
    ("Monthly churn", CH, PCT, lambda m: ltvcac(ch=f"({CH}*{m})")),
    ("Fully loaded CAC", CAC, NUM_RS, lambda m: ltvcac(cac=f"({CAC}*{m})")),
    ("AI cost per job", AI, NUM_RS1, lambda m: ltvcac(ai=f"({AI}*{m})")),
    ("Messaging cost per job", MS, NUM_RS1, lambda m: ltvcac(ms=f"({MS}*{m})")),
]
SE["A5"] = "Base case"; SE["C5"] = ltvcac(); SE["D5"] = ltvcac(); SE["C5"].number_format = MULT; SE["D5"].number_format = MULT
for i, (lab, ref, fmt, fn) in enumerate(drivers):
    r = 6 + i
    SE.cell(row=r, column=1, value=lab).font = BLACK
    SE.cell(row=r, column=2, value="=" + ref).number_format = fmt
    SE.cell(row=r, column=3, value=fn("0.8")).number_format = MULT
    SE.cell(row=r, column=4, value=fn("1.2")).number_format = MULT
    SE.cell(row=r, column=5, value=f"=ABS(D{r}-C{r})").number_format = MULT
SE["A14"] = "Read: the biggest swings are the drivers to prove first (they map to experiments E1, E2, E5 in Step 6)."
SE["A14"].font = Font(name=F, size=9, italic=True)
SE.column_dimensions["A"].width = 34
for col in "BCDE":
    SE.column_dimensions[col].width = 18

# ---------------------------------------------------------------- Funding Need
FN = wb.create_sheet("Funding Need")
FN["A1"] = "Funding need → the ask (₹ lakh), course M1 lanes"
FN["A1"].font = TITLE
FN["A2"] = "Runway window = Y1 + the share of Y2 needed to reach the runway months. Every number links to the P&L."
FN["A2"].font = Font(name=F, size=9, italic=True)
header(FN, 4, ["M1 funding lane", "What it pays for", "₹ L in runway window", "Use of funds %"])
w2 = f"(({s('runway')}-12)/12)"


def win(key):
    return f"({pl(key, 0)}+{pl(key, 1)}*{w2})"


lanes = [
    ("Discover product–market fit", "Experiments E1–E8: AI lead, eval/data and speech engineers; agency success team; pilots, golden sets, lexicons, research; AI cost per job",
     f"={win('t_tech')}*{s('eng_pmf')}+{win('pmf')}+{win('t_ops')}+{win('cogs')}"),
    ("Build the product", "Platform: backend, WhatsApp and SRE engineers; repo Foundations; cloud and hosting; devices",
     f"={win('t_tech')}*(1-{s('eng_pmf')})+{win('infra')}+{win('capex')}"),
    ("Build the team and company", "Founders, finance/HR/admin, office, compliance, legal, seed transaction costs",
     f"={win('t_founders')}+{win('t_ga')}+{win('ga_o')}+{win('compl')}"),
    ("Marketing and sales", "Field sales, agency acquisition, brand",
     f"={win('t_sales')}+{win('mkt_cac')}+{win('mkt_brand')}"),
    ("Working capital", "Parts float and payment cycles", f"={win('dwc')}"),
]
fr = 5
for name, what, f in lanes:
    FN.cell(row=fr, column=1, value=name).font = BLACK
    FN.cell(row=fr, column=2, value=what).font = BLACK
    c = FN.cell(row=fr, column=3, value=f)
    c.number_format = NUM_L
    c.font = GREEN
    c2 = FN.cell(row=fr, column=4, value=f"=IF($C$10=0,0,C{fr}/$C$10)")
    c2.number_format = PCT
    fr += 1
FN["A10"] = "Gross spend in runway window"; FN["A10"].font = BOLD
FN["C10"] = "=SUM(C5:C9)"; FN["C10"].number_format = NUM_L; FN["C10"].font = BOLD; FN["C10"].border = TOP
FN["D10"] = "=SUM(D5:D9)"; FN["D10"].number_format = PCT; FN["D10"].font = BOLD; FN["D10"].border = TOP
calc = [
    (12, "Add: contingency", f"=C10*{s('contingency')}"),
    (13, "Total cash needed", "=C10+C12"),
    (14, "Less: revenue earned in runway window", f"=-({pl('rev', 0)}+{pl('rev', 1)}*{w2})"),
    (15, "Net cash burn", "=C13+C14"),
    (16, "Less: cash in bank", f"=-{s('cash_open')}"),
    (17, "Less: grants (non-dilutive)", f"=-{s('grants')}"),
    (18, "External funding gap", "=C15+C16+C17"),
]
for row, lab, f in calc:
    FN.cell(row=row, column=1, value=lab).font = BOLD if row in (13, 15, 18) else BLACK
    c = FN.cell(row=row, column=3, value=f)
    c.number_format = NUM_L
    c.font = BOLD if row in (13, 15, 18) else BLACK
FN["A20"] = "THE ASK — Step 8 recommendation (pending team lock)"; FN["A20"].font = Font(name=F, size=14, bold=True, color="C00000")
FN["A21"] = "Derived from the costed requirement list in steps/08_funding_needs_and_ask.md (24-month runway). Final once Step 8 is locked."
FN["A21"].font = Font(name=F, size=9, italic=True, color="C00000")
FN["A22"] = "Seed raise (gap rounded up)"; FN["A22"].font = BOLD
FN["C22"] = f"=CEILING(MAX(0,C18),{s('round_to')})"; FN["C22"].number_format = NUM_L; FN["C22"].font = BOLD
FN["C22"].fill = YELLOW
FN["D22"] = "₹ lakh"
FN["A23"] = "Seed raise in ₹ crore"; FN["C23"] = "=C22/100"; FN["C23"].number_format = NUM_CR
FN["A24"] = "Headroom over the gap"; FN["C24"] = "=C22-C18"; FN["C24"].number_format = NUM_L
FN["A26"] = "Milestones this buys (Step 8)"; FN["A26"].font = BOLD
FN["A27"] = "Paying agencies at end of runway (approx.)"
FN["C27"] = f"={rb('ag_end', 0)}+({rb('ag_end', 1)}-{rb('ag_end', 0)})*{w2}"; FN["C27"].number_format = NUM_0
FN["A28"] = "Machine records at end of runway (approx.)"
FN["C28"] = f"={rb('rec_cum', 0)}+({rb('rec_cum', 1)}-{rb('rec_cum', 0)})*{w2}"; FN["C28"].number_format = NUM_0
FN["A29"] = "Annualised revenue run-rate at end of runway (₹ L, approx.)"
FN["C29"] = f"={rb('ag_end', 1)}*'Unit Economics'!B{urows['arpa']}*12/100000+{pl('rev', 1)}-{rb('rev_sub', 1)}-{rb('rev_fix', 1)}"; FN["C29"].number_format = NUM_L
FN["A30"] = "Cash left at end of runway (₹ L)"
FN["C30"] = f"={pl('cash_close', 1)}"; FN["C30"].number_format = NUM_L
FN.column_dimensions["A"].width = 44
FN.column_dimensions["B"].width = 64
FN.column_dimensions["C"].width = 22
FN.column_dimensions["D"].width = 16

# ---------------------------------------------------------------- Valuation
V = wb.create_sheet("Valuation")
V["A1"] = "Valuation — three course methods (₹ crore, Step 9)"
V["A1"].font = TITLE
V["A2"] = "A pre-revenue seed is priced against comparable seed rounds (Methods 1–2) and checked against the investor's required return (Method 3). Methods give POST-money; pre-money = post − investment."
V["A2"].font = Font(name=F, size=9, italic=True)
V["A4"] = "Investment — the seed ask (₹ Cr)"; V["A4"].font = BOLD
V["B4"] = "='Funding Need'!C23"; V["B4"].number_format = NUM_CR; V["B4"].font = GREEN
header(V, 6, ["Revenue path (₹ Cr)", "Value", "Note"])
for i in range(5):
    V.cell(row=7 + i, column=1, value=f"Y{i+1} revenue")
    c = V.cell(row=7 + i, column=2, value=f"='P&L and Cash'!{YCOLS[i]}{PL['rev']}/100"); c.number_format = NUM_CR; c.font = GREEN
V["A12"] = "Y6 revenue"; V["B12"] = f"=B11*(1+{s('g6')})"; V["B12"].number_format = NUM_CR; V["C12"] = "Extension beyond the 5-year model"
V["A13"] = "Y7 revenue"; V["B13"] = f"=B12*(1+{s('g7')})"; V["B13"].number_format = NUM_CR
header(V, 15, ["Method 1 — Comparable seed rounds", "Post-money", "Note"])
V["A16"] = "Hisabkitab (AI for small firms), seed"; V["B16"] = f"={s('comp1')}"
V["A17"] = "Unveilr AI, pre-seed"; V["B17"] = f"={s('comp2')}"
V["A18"] = "Indian seed market midpoint"; V["B18"] = f"={s('comp3')}"
V["A19"] = "Average comparable post-money"; V["B19"] = "=AVERAGE(B16:B18)"; V["A19"].font = BOLD
V["A20"] = "Implied pre-money"; V["B20"] = "=B19-B4"
for r in range(16, 21):
    V[f"B{r}"].number_format = NUM_CR
header(V, 22, ["Method 2 — Scorecard", "Value", "Note"])
V["A23"] = "Baseline valuation (Method 1 average)"; V["B23"] = "=B19"; V["B23"].number_format = NUM_CR
V["A24"] = "Benchmark score"; V["B24"] = f"={s('bench_score')}"
V["A25"] = "Keepwell score (Step 11)"; V["B25"] = f"={s('our_score')}"
V["A26"] = "Adjusted post-money"; V["B26"] = "=IF(B24=0,0,B23*B25/B24)"; V["B26"].number_format = NUM_CR; V["A26"].font = BOLD
V["C26"] = "Course M4: reference valuation × (our score ÷ benchmark score)"
V["A27"] = "Implied pre-money"; V["B27"] = "=B26-B4"; V["B27"].number_format = NUM_CR
header(V, 29, ["Method 3 — Target return (VC method)", "Value", "Note"])
V["A30"] = "Target IRR"; V["B30"] = f"={s('irr')}"; V["B30"].number_format = PCT
V["A31"] = "Years to exit"; V["B31"] = f"={s('horizon')}"
V["A32"] = "Future value the investor needs"; V["B32"] = "=B4*(1+B30)^B31"; V["B32"].number_format = NUM_CR; V["C32"] = "Investment × (1 + IRR)^years"
V["A33"] = "Revenue in exit year"; V["B33"] = "=INDEX(B7:B13,MIN(7,B31))"; V["B33"].number_format = NUM_CR
V["A34"] = "Exit multiple"; V["B34"] = f"={s('exit_mult')}"; V["B34"].number_format = MULT
V["A35"] = "Exit value"; V["B35"] = "=B33*B34"; V["B35"].number_format = NUM_CR
V["A36"] = "Ownership needed at exit"; V["B36"] = "=IF(B35=0,0,B32/B35)"; V["B36"].number_format = PCT
V["A37"] = "Ownership needed today (after Series A and B dilution)"; V["B37"] = f"=B36/(1-{s('later_dil')})"; V["B37"].number_format = PCT
V["A38"] = "Post-money"; V["B38"] = "=IF(B37=0,0,B4/B37)"; V["B38"].number_format = NUM_CR; V["A38"].font = BOLD
V["C38"] = "Investment ÷ ownership. Course slides call this 'pre-money'; strictly it is post-money"
V["A39"] = "Implied pre-money"; V["B39"] = "=B38-B4"; V["B39"].number_format = NUM_CR
V["A40"] = "Pre-money we pitch (₹ Cr)"; V["A40"].font = BOLD
V["B40"] = "=ROUND(B49-B4,0)"; V["B40"].number_format = NUM_CR; V["B40"].font = BOLD; V["B40"].fill = YELLOW
V["C40"] = "Average post-money of the three methods − investment, rounded. Negotiation anchor (Step 9)"
V["A41"] = "Post-money (₹ Cr)"; V["B41"] = "=B40+B4"; V["B41"].number_format = NUM_CR
V["A42"] = "Seed investor stake"; V["A42"].font = BOLD
V["B42"] = "=IF(B41=0,0,B4/B41)"; V["B42"].number_format = PCT; V["B42"].font = BOLD
V["C42"] = "Indian seed norm: 15–25% dilution (Kae Capital)"
header(V, 44, ["Summary — post-money by method", "₹ Cr", ""])
V["A45"] = "Comparable"; V["B45"] = "=B19"
V["A46"] = "Scorecard"; V["B46"] = "=B26"
V["A47"] = "VC method"; V["B47"] = "=B38"
V["A48"] = "Low"; V["B48"] = "=MIN(B45:B47)"
V["A49"] = "Average"; V["B49"] = "=AVERAGE(B45:B47)"
V["A50"] = "High"; V["B50"] = "=MAX(B45:B47)"
for r in range(45, 51):
    V[f"B{r}"].number_format = NUM_CR
header(V, 52, ["VC-method check at the pitched price", "Value", "Note"])
V["A53"] = "Investor's stake after Series A and B"; V["B53"] = f"=B42*(1-{s('later_dil')})"; V["B53"].number_format = PCT
V["A54"] = "Investor's value at exit"; V["B54"] = "=B53*B35"; V["B54"].number_format = NUM_CR
V["A55"] = "Multiple on money"; V["B55"] = "=IF(B4=0,0,B54/B4)"; V["B55"].number_format = MULT
V["A56"] = "Implied IRR"; V["B56"] = "=IF(B4=0,0,(B54/B4)^(1/B31)-1)"; V["B56"].number_format = PCT
V["C56"] = "Compare with the 35–40% seed target (course M4)"
V.column_dimensions["A"].width = 52
V.column_dimensions["B"].width = 18
V.column_dimensions["C"].width = 80

# ---------------------------------------------------------------- Cap Table
C = wb.create_sheet("Cap Table")
C["A1"] = "Cap table and dilution path"
C["A1"].font = TITLE
C["A3"] = "Seed investor stake"; C["B3"] = "=Valuation!B42"; C["B3"].number_format = PCT; C["B3"].font = GREEN
C["A4"] = "ESOP pool target (post-seed)"; C["B4"] = f"={s('esop')}"; C["B4"].number_format = PCT
C["A5"] = "Existing shares (founders + converted iSAFE)"; C["B5"] = "=SUM(B10:B13)"; C["B5"].number_format = NUM_0
C["A6"] = "Post-seed fully diluted shares"; C["B6"] = "=IF(1-B3-B4<=0,0,B5/(1-B3-B4))"; C["B6"].number_format = NUM_0
C["A7"] = "Seed price per share (₹)"; C["B7"] = "=IF(B6=0,0,Valuation!B41*10000000/B6)"; C["B7"].number_format = '"₹"#,##0.00'
header(C, 9, ["Holder", "Shares pre-seed", "% pre-seed", "Shares post-seed", "% post-seed", "% post-Series A", "% post-Series B"])
holders = [("Sri Charan Peri (founder)", "sh_f1"), ("Prathyusha Kalluri (founder)", "sh_f2"),
           ("Kavyanth Munagala (founder)", "sh_f3"), ("Pre-seed angels (iSAFE, as converted)", None)]
cr = 10
for name, key in holders:
    C.cell(row=cr, column=1, value=name).font = BLACK
    if key:
        C.cell(row=cr, column=2, value=f"={s(key)}").number_format = NUM_0
    else:
        C.cell(row=cr, column=2, value="=ROUND(SUM(B10:B12)*I4/(1-I4),0)").number_format = NUM_0
    cr += 1
C["H3"] = "iSAFE conversion"; C["H3"].font = BOLD
C["H4"] = "Ownership at cap (amount ÷ post-money cap)"
C["I4"] = f"=IF({s('isafe_cap')}=0,0,{s('isafe_amt')}/({s('isafe_cap')}*100))"; C["I4"].number_format = PCT
C["H5"] = "Cap price per share (₹)"
C["I5"] = f"=IF(B13=0,0,{s('isafe_amt')}*100000/B13)"; C["I5"].number_format = '"₹"#,##0.00'
C["H6"] = "Discounted seed price (₹)"
C["I6"] = f"=B7*(1-{s('isafe_disc')})"; C["I6"].number_format = '"₹"#,##0.00'
C["H7"] = "Cap binds? (cap price ≤ discounted price)"
C["I7"] = '=IF(I5<=I6,"Yes — cap used","No — use discount (re-check)")'
C.column_dimensions["H"].width = 42
C.column_dimensions["I"].width = 18
C.cell(row=14, column=1, value="ESOP pool").font = BLACK
C["B14"] = 0
C.cell(row=15, column=1, value="Seed investor").font = BLACK
C["B15"] = 0
C.cell(row=16, column=1, value="Series A investor").font = BLACK
C.cell(row=17, column=1, value="Series B investor").font = BLACK
for rr_ in range(10, 16):
    C[f"C{rr_}"] = f"=IF(SUM($B$10:$B$15)=0,0,B{rr_}/SUM($B$10:$B$15))"
    C[f"D{rr_}"] = f"=B{rr_}" if rr_ <= 13 else ("=$B$4*$B$6" if rr_ == 14 else "=$B$3*$B$6")
    C[f"E{rr_}"] = f"=IF($D$18=0,0,D{rr_}/$D$18)"
    C[f"F{rr_}"] = f"=E{rr_}*(1-{s('dil_a')})"
    C[f"G{rr_}"] = f"=F{rr_}*(1-{s('dil_b')})"
C["F16"] = f"={s('dil_a')}"
C["G16"] = f"=F16*(1-{s('dil_b')})"
C["G17"] = f"={s('dil_b')}"
C["A18"] = "Total"; C["A18"].font = BOLD
for col in "BCDEFG":
    C[f"{col}18"] = f"=SUM({col}10:{col}17)"
    C[f"{col}18"].font = BOLD
    C[f"{col}18"].border = TOP
for rr_ in range(10, 19):
    for col in "BD":
        C[f"{col}{rr_}"].number_format = NUM_0
    for col in "CEFG":
        C[f"{col}{rr_}"].number_format = PCT
C["A20"] = "Founders combined"; C["A20"].font = BOLD
for col in "CEFG":
    C[f"{col}20"] = f"=SUM({col}10:{col}12)"
    C[f"{col}20"].number_format = PCT
    C[f"{col}20"].font = BOLD
C["A22"] = "Check: seed shares × price = investment (₹ Cr)"
C["B22"] = "=D15*B7/10000000"; C["B22"].number_format = NUM_CR
C.column_dimensions["A"].width = 40
for col in "BCDEFG":
    C.column_dimensions[col].width = 17

# ---------------------------------------------------------------- Checks
K = wb.create_sheet("Checks")
K["A1"] = "Model checks (all should read OK)"
K["A1"].font = TITLE
header(K, 3, ["Check", "Value", "Result"])
checks = [
    ("Use of funds sums to 100%", "='Funding Need'!D10", "=IF(ABS(B4-1)<0.0001,\"OK\",\"CHECK\")", PCT),
    ("Ask ≥ funding gap", "='Funding Need'!C22-'Funding Need'!C18", "=IF(B5>=0,\"OK\",\"CHECK\")", NUM_L),
    ("Cap table post-seed sums to 100%", "='Cap Table'!E18", "=IF(ABS(B6-1)<0.0001,\"OK\",\"CHECK\")", PCT),
    ("Cap table post-Series B sums to 100%", "='Cap Table'!G18", "=IF(ABS(B7-1)<0.0001,\"OK\",\"CHECK\")", PCT),
    ("Seed shares × price = investment", "='Cap Table'!B22-Valuation!B4", "=IF(ABS(B8)<0.001,\"OK\",\"CHECK\")", NUM_CR),
    ("iSAFE converts at its cap (not the discount)", "='Cap Table'!I5", "=IF('Cap Table'!I5<='Cap Table'!I6,\"OK\",\"CHECK\")", '"₹"#,##0.00'),
    ("SOM is under 20% of SAM", "=Market!B15", "=IF(B10<=0.2,\"OK\",\"CHECK (Step 4)\")", PCT),
    ("Cash never negative before Series A (else plan Series A)", f"='P&L and Cash'!C{PL_BE + 1}",
     "=IF(B11>=0,\"OK\",\"Series A needed after runway (expected)\")", NUM_L),
]
for i, (lab, f, res, fmt) in enumerate(checks):
    rr_ = 4 + i
    K.cell(row=rr_, column=1, value=lab).font = BLACK
    c = K.cell(row=rr_, column=2, value=f)
    c.number_format = fmt
    c.font = GREEN
    K.cell(row=rr_, column=3, value=res).font = BOLD
K.column_dimensions["A"].width = 56
K.column_dimensions["B"].width = 16
K.column_dimensions["C"].width = 18

# ---------------------------------------------------------------- README (first)
RM = wb.create_sheet("README", 0)
RM["A1"] = "Keepwell — financial model (seed pitch)"
RM["A1"].font = TITLE
lines = [
    "Status: STRUCTURE BUILT, NUMBERS ARE DRAFT PLACEHOLDERS. Each input gets locked in its pitch step (see Pitch Bible).",
    "Ask, valuation and seed price: Step 8–9 recommendations (24-month runway, ₹4.5 Cr at ₹18 Cr pre-money), pending team lock.",
    "",
    "How to use",
    "1. Change only blue cells on the Assumptions tab. Yellow-filled cells are still to be decided.",
    "2. Every other tab is formulas. Black = calculation, green = link to another tab.",
    "3. Money is in ₹ lakh (L) unless a unit says ₹ or ₹ Cr. 1 Cr = 100 L.",
    "4. Tags: Real = case comp / research; Story = assumed backstory or pilot; Model = modelling choice; DRAFT = placeholder.",
    "",
    "Tabs and the pitch step that fills them",
    "Assumptions — every input (Steps 2–9)",
    "Revenue Build — agencies, jobs, machine records, six revenue lines (Steps 4, 6, 7)",
    "P&L and Cash — gross margin, SG&A, EBITDA, D&A, EBIT, burn, runway, break-even (Step 7)",
    "Unit Economics — ARPA, cost to serve, contribution, CAC, payback, LTV, LTV:CAC (Step 7)",
    "Funding Need — 18-month budget by course M1 lanes → gap → the ask → use of funds (Step 8)",
    "Market — TAM/SAM/SOM in agencies and ₹ (Step 4)",
    "Pilot — value to an agency vs our fee at ₹40 and ₹100 (Step 6)",
    "Sensitivity — LTV:CAC when each driver moves ±20% (Step 7)",
    "Valuation — Comparable, Scorecard, VC method → pre-money we pitch (Step 9)",
    "Cap Table — founders, pre-seed, ESOP, seed, Series A, Series B (Step 9)",
    "Checks — reconciliation tests (all should read OK)",
    "",
    "Example of an input row (Assumptions): 'Fee per verified fix | ₹ | 40 | DRAFT | Repo/one-pager: ₹40, test ₹100'",
    "Sensitivity tab added in Step 7 (driver swings on LTV:CAC).",
]
for i, t in enumerate(lines):
    c = RM.cell(row=3 + i, column=1, value=t)
    c.font = BOLD if t in ("How to use", "Tabs and the pitch step that fills them") else BLACK
RM["A3"].font = Font(name=F, size=10, bold=True, color="C00000")
RM.column_dimensions["A"].width = 120

for ws in wb.worksheets:
    for row in ws.iter_rows():
        for c in row:
            f = c.font
            c.font = Font(name=F, size=f.size or 10, bold=f.bold, italic=f.italic, color=f.color)
    ws.sheet_view.showGridLines = False

wb.save(OUT)
print("saved", OUT)
