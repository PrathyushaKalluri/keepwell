"""Build keepwell_model.xlsx (Keepwell v2, Step 7) with live formulas.

    <venv>/bin/python build_model_v2.py      (needs openpyxl)
Mirrors plan_core.py exactly; verify_model.py compares the two after LibreOffice recalculation.
Colours: blue = input, black = formula, green = cross-sheet link. Scenario switch: Inputs!C2 (1 low, 2 base, 3 high).
"""
import pathlib
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment
from openpyxl.utils import get_column_letter as L
import plan_core as m

OUT = pathlib.Path(__file__).parent.parent / "keepwell_model.xlsx"
F = "Arial"
BLUE, BLACK, GREEN = Font(name=F, color="0000FF"), Font(name=F, color="000000"), Font(name=F, color="008000")
BOLD = Font(name=F, bold=True)
YEL = PatternFill("solid", fgColor="FFFF00")
INR = '#,##0;(#,##0);"-"'
PCT = '0.0%;(0.0%);"-"'
CR = '#,##0.00,,,," Cr";(#,##0.00,,,," Cr");"-"'

wb = Workbook()
# ---------------------------------------------------------------- README
ws = wb.active; ws.title = "README"
for i, t in enumerate([
    "Keepwell v2 financial model (Step 7). Illustrative case for the IIIT Hyderabad ESFS course pitch.",
    "BASE = Vijayawada–Guntur pilot actuals (Step 6, [Story], generated from ue_v2.py). Research inputs are tagged [R] with sources on the Inputs sheet.",
    "How to use: change Inputs!C2 (1 = LOW, 2 = BASE, 3 = HIGH). Blue cells are inputs; black are formulas; green link other sheets.",
    "LOW and HIGH set every input pessimistic/optimistic together (corner cases). Sensitivity sheet shows one-at-a-time swings.",
    "Sheets: Inputs → Shop (one mature shop, per year) → Cluster (one mature cluster) → Plan (8 years, layers, cash, exit) → Sensitivity.",
    "Python mirror: model/plan_core.py. Rebuild: model/build_model_v2.py. Check: model/verify_model.py.",
], start=1):
    ws.cell(i, 1, t).font = BOLD if i == 1 else BLACK
ws.column_dimensions["A"].width = 140

# ---------------------------------------------------------------- Inputs
wi = wb.create_sheet("Inputs")
wi["A1"] = "Inputs (blue). Live column = CHOOSE(scenario, Low, Base, High)"; wi["A1"].font = BOLD
wi["A2"] = "Scenario (1 LOW, 2 BASE, 3 HIGH)"; wi["C2"] = 2; wi["C2"].font = BLUE; wi["C2"].fill = YEL
hdr = ["Input", "Unit", "Low", "Base", "High", "Live", "Tag", "Source"]
for j, h in enumerate(hdr, 1):
    wi.cell(4, j, h).font = BOLD
REF = {}
r = 5
for k, ((lo, ba, hi), unit, tag, src) in m.I.items():
    wi.cell(r, 1, k); wi.cell(r, 2, unit)
    for j, x in enumerate((lo, ba, hi), 3):
        c = wi.cell(r, j, x); c.font = BLUE
    wi.cell(r, 6, f"=CHOOSE($C$2,C{r},D{r},E{r})").font = BLACK
    wi.cell(r, 7, tag); wi.cell(r, 8, src)
    fmt = PCT if (isinstance(ba, float) and ba < 1) else INR
    for j in (3, 4, 5, 6): wi.cell(r, j).number_format = fmt
    REF[k] = f"Inputs!$F${r}"; r += 1
for col, w in zip("ABCDEFGH", (26, 26, 12, 12, 12, 12, 14, 60)):
    wi.column_dimensions[col].width = w

# ---------------------------------------------------------------- Shop
wsh = wb.create_sheet("Shop")
wsh["A1"] = "One mature shop, per year (BASE pilot inputs via Inputs!F). Prices incl. GST are converted to net (÷1.18)."; wsh["A1"].font = BOLD
cols = ["Line", "Category mix", "Out-of-warranty share", "Events per unit-yr", "Ticket incl GST (₹)", "Parts share", "Parts margin",
        "Basis (1 = OOW units)", "Units in base", "Jobs / yr", "Net per job (₹)", "Contribution per job (₹)", "Revenue / yr (₹)", "Contribution / yr (₹)"]
for j, h in enumerate(cols, 1):
    wsh.cell(3, j, h).font = BOLD
R = lambda k: REF[k].replace("Inputs!", "Inputs!")
row = 4
first = row
for cat, mix, oow, jobs, amc in m.CAT:
    for ev, tk, ps, pm, basis in jobs:
        wsh.cell(row, 1, f"{cat}: {'service' if tk < 700 and ps < 0.2 else 'repair/service'} (₹{tk})")
        for j, x in ((2, mix), (3, oow), (4, ev), (5, tk), (6, ps), (8, 1 if basis == "oow" else 0)):
            wsh.cell(row, j, x).font = BLUE
        g = wsh.cell(row, 7, pm if pm is not None else f"={REF['parts_margin']}"); g.font = BLUE if pm is not None else GREEN
        wsh.cell(row, 9, f"={REF['units_month']}*B{row}*12*{REF['years_base']}*0.9")
        wsh.cell(row, 10, f"=I{row}*IF(H{row}=1,C{row},1)*D{row}*{REF['capture']}*(1-{REF['leakage']})")
        wsh.cell(row, 11, f"=E{row}/1.18")
        wsh.cell(row, 12, f"=K{row}-K{row}*F{row}*(1-G{row})-K{row}*(1-F{row})*{REF['labour_payout']}-K{row}*({REF['comm_repair']}+{REF['rework']}+{REF['levy']})-{REF['tech_cost']}-{REF['insurance']}")
        wsh.cell(row, 13, f"=J{row}*K{row}"); wsh.cell(row, 14, f"=J{row}*L{row}")
        row += 1
    if amc:
        price, vis, vk = amc
        wsh.cell(row, 1, f"{cat}: AMC (₹{price}, {vis} visits)")
        for j, x in ((2, mix), (3, oow), (5, price)):
            wsh.cell(row, j, x).font = BLUE
        wsh.cell(row, 4, vis).font = BLUE
        wsh.cell(row, 9, f"={REF['units_month']}*B{row}*12*{REF['years_base']}*0.9")
        wsh.cell(row, 10, f"=I{row}*C{row}*{REF['amc_attach']}*(1-{REF['leakage']})")
        wsh.cell(row, 11, f"=E{row}/1.18")
        wsh.cell(row, 12, f"=K{row}-D{row}*{REF[vk]}-K{row}*({REF['comm_amc']}+{REF['levy']})-50-2*{REF['tech_cost']}")
        wsh.cell(row, 13, f"=J{row}*K{row}"); wsh.cell(row, 14, f"=J{row}*L{row}")
        row += 1
wsh.cell(row, 1, "AC install (brand-authorised, sub-contract)"); wsh.cell(row, 2, 0.30).font = BLUE
wsh.cell(row, 10, f"={REF['units_month']}*B{row}*12*{REF['auth_cov']}*{REF['routing']}")
wsh.cell(row, 11, f"={REF['ac_install_net']}+{REF['materials_net']}")
wsh.cell(row, 12, f"=K{row}-{REF['materials_net']}*(1-{REF['materials_margin']})-{REF['ac_install_payout']}-{REF['ac_install_net']}*({REF['comm_install']}+{REF['rework']}+{REF['levy']})-{REF['tech_cost']}-{REF['insurance']}")
wsh.cell(row, 13, f"=J{row}*K{row}"); wsh.cell(row, 14, f"=J{row}*L{row}"); row += 1
wsh.cell(row, 1, "Washing-machine install"); wsh.cell(row, 2, 0.15).font = BLUE
wsh.cell(row, 10, f"={REF['units_month']}*B{row}*12*0.9*{REF['other_install_capture']}")
wsh.cell(row, 11, f"={REF['wm_install_net']}")
wsh.cell(row, 12, f"=K{row}-{REF['wm_install_payout']}-K{row}*({REF['comm_install']}+{REF['levy']})-{REF['tech_cost']}-{REF['insurance']}")
wsh.cell(row, 13, f"=J{row}*K{row}"); wsh.cell(row, 14, f"=J{row}*L{row}"); last = row; row += 2
wsh.cell(row, 1, "TOTAL per mature shop per year").font = BOLD
wsh.cell(row, 10, f"=SUM(J{first}:J{last})"); wsh.cell(row, 13, f"=SUM(M{first}:M{last})"); wsh.cell(row, 14, f"=SUM(N{first}:N{last})")
SHOP_REV, SHOP_CON = f"Shop!$M${row}", f"Shop!$N${row}"
wsh.cell(row + 1, 1, "Contribution margin"); wsh.cell(row + 1, 14, f"=N{row}/M{row}").number_format = PCT
for rr in range(first, row + 1):
    for j in (9, 10): wsh.cell(rr, j).number_format = '#,##0.0'
    for j in (11, 12, 13, 14): wsh.cell(rr, j).number_format = INR
    for j in (2, 3, 6, 7): wsh.cell(rr, j).number_format = PCT
wsh.column_dimensions["A"].width = 44
for j in range(2, 15): wsh.column_dimensions[L(j)].width = 14

# ---------------------------------------------------------------- Cluster
wc = wb.create_sheet("Cluster")
wc["A1"] = "One mature cluster, per year"; wc["A1"].font = BOLD
lines = [
    ("Shops per cluster", f"={REF['shops_per_cluster']}", '#,##0'),
    ("Revenue: shops + plan-seller jobs (₹)", f"={SHOP_REV}*B3+{REF['plan_jobs_m']}*12*{REF['plan_rev']}", INR),
    ("Shop contribution (₹)", f"={SHOP_CON}*B3", INR),
    ("Off-season floor top-up for core technicians (₹)", f"=-{REF['floor_topup_y']}", INR),
    ("Plan-seller fulfilment contribution (₹)", f"={REF['plan_jobs_m']}*12*{REF['plan_contrib']}", INR),
    ("Cluster contribution (₹)", "=B5+B6+B7", INR),
    ("Cluster fixed costs (₹)", f"=-{REF['cluster_fixed_m']}*12", INR),
    ("Cluster EBITDA (₹)", "=B8+B9", INR),
    ("Cluster EBITDA margin", "=B10/B4", PCT),
    ("Breakeven shops per cluster", f"=({REF['cluster_fixed_m']}*12+{REF['floor_topup_y']}-B7)/{SHOP_CON}", '#,##0.0'),
]
for i, (lab, f, fmt) in enumerate(lines, 3):
    wc.cell(i, 1, lab); c = wc.cell(i, 2, f); c.number_format = fmt
    c.font = GREEN if "Inputs!" in f or "Shop!" in f else BLACK
wc.column_dimensions["A"].width = 52; wc.column_dimensions["B"].width = 18
CL = {"S": "Cluster!$B$3", "rev": "Cluster!$B$4", "con": "Cluster!$B$8", "fix": "-Cluster!$B$9"}

# ---------------------------------------------------------------- Plan
wp = wb.create_sheet("Plan")
wp["A1"] = "8-year plan (Year 1 = 2027). Columns: B,C = years -2,-1 (zeros); D = year 0 (pilot, 2026); E..L = years 1..8."; wp["A1"].font = BOLD
yc = {t: L(4 + t) for t in range(-2, 9)}  # B=-2, C=-1, D=0, E=1 ... L=8
wp.cell(3, 1, "Year").font = BOLD
for t in range(-2, 9): wp.cell(3, 4 + t, t).font = BOLD
rowmap = {}
def put(r, label, vals_or_fn, fmt=INR, font=BLACK, years=range(1, 9)):
    wp.cell(r, 1, label); rowmap[label] = r
    for t in years:
        v = vals_or_fn(t) if callable(vals_or_fn) else vals_or_fn[t]
        c = wp.cell(r, 4 + t, v); c.number_format = fmt; c.font = font
put(4, "Clusters (end of year)", {-2: 0, -1: 0, 0: 1, **{t: m.CLUSTERS_END[t - 1] for t in range(1, 9)}}, '#,##0', BLUE, range(-2, 9))
put(5, "New clusters opened", lambda t: f"={yc[t]}4-{yc[t-1]}4", '#,##0', BLACK, range(-1, 9))
wp.cell(5, 2, 0)
put(6, "Shops (end of year)", lambda t: f"={yc[t]}4*{CL['S']}", '#,##0', BLACK, range(0, 9))
put(7, "Mature-cluster equivalents (ramp 25% / 60% / 90% / 100%)",
    lambda t: f"={yc[t]}5*{m.MAT[0]}+{yc[t-1]}5*{m.MAT[1]}+{yc[t-2]}5*{m.MAT[2]}+" + (f"{yc[t-3]}4*{m.MAT[3]}" if t >= 1 else "0"), '#,##0.00')
put(9, "Core service revenue (₹)", lambda t: f"={SHOP_REV}*{CL['S']}*{yc[t]}7")
put(10, "Plan-seller fulfilment revenue (₹)", lambda t: f"={REF['plan_jobs_m']}*12*{REF['plan_rev']}*{yc[t]}7")
r0 = 11
LROWS = []
for i, (name, st, rv, cs, kind) in enumerate(m.LAYERS):
    rr = r0 + i
    wp.cell(rr, 1, f"{name} (₹)")
    wp.cell(rr, 14, st).font = BLUE; wp.cell(rr, 15, rv).font = BLUE; wp.cell(rr, 16, cs).font = BLUE; wp.cell(rr, 17, 1 if kind == "data" else 0).font = BLUE
    for t in range(1, 9):
        f = (f"=IF({yc[t]}$3>=$N{rr},$O{rr}*{yc[t]}$7*CHOOSE(MIN({yc[t]}$3-$N{rr},2)+1,{m.LRAMP[0]},{m.LRAMP[1]},{m.LRAMP[2]})"
             f"*IF($Q{rr}=1,{REF['layer_k']},1),0)")
        wp.cell(rr, 4 + t, f).number_format = INR
    LROWS.append(rr)
for j, h in zip((14, 15, 16, 17), ("Start year", "Revenue per mature cluster (₹/yr) [Assumption, 00b scaled]", "Contribution share", "Data layer (1)")):
    wp.cell(r0 - 1, j, h).font = BOLD
re_ = r0 + len(m.LAYERS)
wp.cell(re_, 1, "Brand data contracts, BASE (₹) [Assumption]")
for t in range(1, 9): wp.cell(re_, 4 + t, m.ENTERPRISE[t - 1]).font = BLUE
wp.cell(re_ + 1, 1, "Brand data contracts × adoption (₹)")
for t in range(1, 9): wp.cell(re_ + 1, 4 + t, f"={yc[t]}{re_}*{REF['layer_k']}").number_format = INR
REV = re_ + 3
put(REV, "TOTAL REVENUE (₹)", lambda t: f"={yc[t]}9+{yc[t]}10+SUM({yc[t]}{r0}:{yc[t]}{re_-1})+{yc[t]}{re_+1}")
put(REV + 1, "of which data layers (₹)", lambda t: "=" + "+".join(f"{yc[t]}{rr}" for rr, l in zip(LROWS, m.LAYERS) if l[4] == "data") + f"+{yc[t]}{re_+1}")
put(REV + 2, "Contribution (₹)", lambda t: f"={CL['con']}*{yc[t]}7+SUMPRODUCT({yc[t]}{r0}:{yc[t]}{re_-1},$P{r0}:$P{re_-1})+{yc[t]}{re_+1}*0.75")
put(REV + 3, "Contribution margin", lambda t: f"={yc[t]}{REV+2}/{yc[t]}{REV}", PCT)
put(REV + 4, "Payment and gateway fees (₹)", lambda t: f"=-{yc[t]}{REV}*{REF['pay_fee']}")
put(REV + 5, "Cluster fixed costs (₹)", lambda t: f"=-{CL['fix']}*({yc[t-1]}4+0.5*{yc[t]}5)")
put(REV + 6, "HQ costs, BASE headcount path (₹) [Assumption]", {t: m.HQ[t - 1] for t in range(1, 9)}, INR, BLUE)
put(REV + 7, "HQ costs × multiplier (₹)", lambda t: f"=-{yc[t]}{REV+6}*{REF['hq_mult']}")
put(REV + 8, "Shop acquisition: new shops + churn replacement (₹)", lambda t: f"=-(({yc[t]}4-{yc[t-1]}4)*{CL['S']}+{yc[t-1]}4*{CL['S']}*{REF['shop_churn']})*{REF['shop_cac']}")
put(REV + 9, "EBITDA (₹)", lambda t: f"={yc[t]}{REV+2}+{yc[t]}{REV+4}+{yc[t]}{REV+5}+{yc[t]}{REV+7}+{yc[t]}{REV+8}")
put(REV + 10, "EBITDA margin", lambda t: f"={yc[t]}{REV+9}/{yc[t]}{REV}", PCT)
put(REV + 12, "Cluster set-up, WC and parts stock (₹)", lambda t: f"=-{yc[t]}5*({REF['setup']}+{REF['wc']}+IF({yc[t]}3>=2,{REF['parts_stock']},0))")
put(REV + 13, "Working capital for growth (₹)", lambda t: f"=-MAX(0,{yc[t]}{REV}-{yc[t-1]}{REV})*{REF['nwc_pct']}")
put(REV + 14, "Taxable profit (EBITDA − set-up depreciation) (₹)", lambda t: f"={yc[t]}{REV+9}-{yc[t]}5*{REF['setup']}/3")
put(REV + 15, "Tax-loss pool, end of year (₹)", lambda t: f"=MAX(0,{yc[t-1]}{REV+15}-{yc[t]}{REV+14})")
put(REV + 16, "Tax (₹)", lambda t: f"=-MAX(0,{yc[t]}{REV+14}-{yc[t-1]}{REV+15})*{REF['tax_rate']}")
put(REV + 17, "Cash flow before financing (₹)", lambda t: f"={yc[t]}{REV+9}+{yc[t]}{REV+12}+{yc[t]}{REV+13}+{yc[t]}{REV+16}")
put(REV + 18, "Cumulative cash, incl. ₹18 L opening (₹)", lambda t: f"={yc[t]}{REV+17}+" + (f"{yc[t-1]}{REV+18}" if t > 1 else REF['start_cash']))
wp.cell(REV + 20, 1, "PEAK FUNDING NEED (₹)").font = BOLD
wp.cell(REV + 20, 5, f"=-MIN(0,MIN(E{REV+18}:L{REV+18}))").number_format = INR
wp.cell(REV + 22, 1, "Exit value check (operator revenue × 2.5 + data revenue × 7)").font = BOLD
for t, col in ((7, "K"), (8, "L")):
    wp.cell(REV + 23 + (t - 7), 1, f"Year {t} EV (₹)")
    wp.cell(REV + 23 + (t - 7), 5, f"=({col}{REV}-{col}{REV+1})*2.5+{col}{REV+1}*7").number_format = INR
wp.column_dimensions["A"].width = 60
for j in range(2, 18): wp.column_dimensions[L(j)].width = 15
PLAN = dict(rev=REV, data=REV + 1, con=REV + 2, ebitda=REV + 9, cum=REV + 18, peak=REV + 20, ev=REV + 23, col0=4)

# ---------------------------------------------------------------- Sensitivity (values from plan_core, labelled)
wsn = wb.create_sheet("Sensitivity")
wsn["A1"] = "One-at-a-time sensitivity on BASE (values computed by model/plan_core.py at build time; rebuild to refresh)"; wsn["A1"].font = BOLD
for j, h in enumerate(["Input", "Swing", "Breakeven shops/cluster", "Year-7 EBITDA (₹ Cr)", "Peak funding need (₹ Cr)"], 1):
    wsn.cell(3, j, h).font = BOLD
rows_b, peak_b, u_b = m.plan("base")
wsn.cell(4, 1, "BASE"); wsn.cell(4, 3, round(u_b["be_shops"], 1)); wsn.cell(4, 4, round(rows_b[6]["ebitda"] / 1e7, 2)); wsn.cell(4, 5, round(peak_b / 1e7, 2))
res = []
for k in m.I:
    for s in ("low", "high"):
        orig = m.I[k]; vals = list(orig[0]); vals[1] = vals[0 if s == "low" else 2]; m.I[k] = (tuple(vals),) + orig[1:]
        rr_, pk, uu = m.plan("base"); m.I[k] = orig
        res.append((k, s, uu["be_shops"], rr_[6]["ebitda"] / 1e7, pk / 1e7))
res.sort(key=lambda x: x[3])
for i, (k, s, be, eb, pk) in enumerate(res[:24], 5):
    wsn.cell(i, 1, k); wsn.cell(i, 2, s); wsn.cell(i, 3, round(be, 1)); wsn.cell(i, 4, round(eb, 2)); wsn.cell(i, 5, round(pk, 2))
wsn.column_dimensions["A"].width = 26
for c_ in "BCDE": wsn.column_dimensions[c_].width = 22

wb.save(OUT)
import json
json.dump(PLAN, open(pathlib.Path(__file__).parent / "plan_rows.json", "w"))
print("saved", OUT)
