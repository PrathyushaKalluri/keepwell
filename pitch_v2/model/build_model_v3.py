"""Build keepwell_model.xlsx (Keepwell v3, Step 7 + 7b redesign) with live formulas.

    <venv>/bin/python build_model_v3.py [scenario 1-4]     (needs openpyxl)
Mirrors plan_v3.py exactly; verify_model_v3.py compares the two after LibreOffice recalculation.
Colours: blue = input, black = formula, green = cross-sheet link. Scenario switch: Inputs!C2 (1 LOW, 2 BASE, 3 HIGH, 4 STRESS).
"""
import pathlib, sys, json
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill
from openpyxl.utils import get_column_letter as CL_
import plan_core as m, plan_v3 as V

OUT = pathlib.Path(__file__).parent.parent / "keepwell_model.xlsx"
SCEN = int(sys.argv[1]) if len(sys.argv) > 1 else 2
F = "Arial"
BLUE, BLACK, GREEN = Font(name=F, color="0000FF"), Font(name=F, color="000000"), Font(name=F, color="008000")
BOLD = Font(name=F, bold=True)
YEL = PatternFill("solid", fgColor="FFFF00")
INR = '#,##0;(#,##0);"-"'
PCT = '0.0%;(0.0%);"-"'

LV = V.L
LEV = {  # lever inputs: (low, base, high, stress), unit, tag, source
 "protect_attach": ((0.05, LV["protect_attach"], LV["protect_attach"], 0.05), "share of covered units sold", "Assumption", "US ~30% (Warranty Week); no India rate published; 7b §7b.3"),
 "covered_share": ((0.75,) * 4, "share of units", "Model", "AC+fridge+WM+purifier mix (CAT)"),
 "protect_price": ((LV["protect_price"],) * 4, "INR incl GST", "R/derived", "Onsitego AC 2-yr ₹3,299; resQ ₹3,699; mix-weighted ~₹2,040"),
 "protect_comm": ((LV["protect_comm"],) * 4, "share of net", "R", "US stores keep 50-70% (Checkbook); we pay less"),
 "claims_ratio": ((0.45, LV["claims_ratio"], LV["claims_ratio"], 0.45), "share of net", "Derived", "own failure data ~27% at cost; 35% carried"),
 "protect_admin": ((LV["protect_admin"],) * 4, "share of net", "Assumption", ""),
 "reserve_share": ((LV["reserve_share"],) * 4, "share of expected claims on unearned plans", "Assumption", "ring-fenced claims reserve"),
 "parts_margin_mature": ((0.25, LV["parts_margin_mature"], LV["parts_margin_mature"], 0.25), "share", "R", "dealer/distributor margins 15-40%"),
 "repair_share_core": ((LV["repair_share_core"],) * 4, "share of core revenue", "Model", "plan_core shop rows"),
 "partner_from": ((LV["partner_from"],) * 4, "year", "Model", "first 6 clusters Keepwell-run"),
 "partner_fixed_m": ((LV["partner_fixed_m"],) * 4, "INR/partner cluster/month", "Assumption", "shop sales lead, QC, marketing"),
 "partner_fee": ((LV["partner_fee"],) * 4, "share of core revenue", "R/Assumption", "IFB 1,512 franchisees; Mr. Appliance royalty 5-7%"),
 "partner_open_floor": ((LV["partner_open_floor"],) * 4, "INR, opening year", "Assumption", "partner never loses money while ramping"),
 "partner_setup": ((LV["partner_setup"],) * 4, "INR/new partner cluster", "Assumption", ""),
 "partner_cac": ((LV["partner_cac"],) * 4, "INR/shop", "R", "cold rate ~22k"),
 "hq_scale": ((LV["hq_scale"],) * 4, "x Step 7 HQ path", "Assumption", "AI intake and dispatch"),
 "shops_per_cluster": ((60, 60, 60, 50), "shops", "Model", "00c density; stress 50"),
}
PATHS = {1: LV["clusters_end"], 2: LV["clusters_end"], 3: LV["clusters_end"], 4: V.STRESS["clusters_end"]}
OVR = {"comm_repair": LV["comm_repair"], "comm_amc": LV["comm_amc"]}

wb = Workbook()
ws = wb.active; ws.title = "README"
for i, t in enumerate([
    "Keepwell v3 financial model (Step 7 + Step 7b redesign). Illustrative case for the IIIT Hyderabad ESFS course pitch.",
    "BASE = Vijayawada–Guntur pilot actuals (Step 6, [Story]) plus the five 7b levers: Keepwell Protect, commission shift, central parts, partner clusters, lean HQ.",
    "Scenario switch Inputs!C2: 1 LOW (all pilot inputs pessimistic + stress Protect), 2 BASE, 3 HIGH, 4 STRESS (planning case for Step 8).",
    "Blue = inputs; black = formulas; green = links to other sheets. Protect plan cash: expected claims on unearned plans are ring-fenced (Plan sheet).",
    "Sheets: Inputs → Shop (one mature shop) → Cluster (own and partner) → Plan (8 years, cohorts, Protect, cash, exit) → Sensitivity.",
    "Python mirror: model/plan_v3.py (on plan_core.py). Rebuild: model/build_model_v3.py. Check: model/verify_model_v3.py.",
], start=1):
    ws.cell(i, 1, t).font = BOLD if i == 1 else BLACK
ws.column_dimensions["A"].width = 150

wi = wb.create_sheet("Inputs")
wi["A1"] = "Inputs (blue). Live = CHOOSE(scenario, Low, Base, High, Stress)"; wi["A1"].font = BOLD
wi["A2"] = "Scenario (1 LOW, 2 BASE, 3 HIGH, 4 STRESS)"; wi["C2"] = SCEN; wi["C2"].font = BLUE; wi["C2"].fill = YEL
for j, h in enumerate(["Input", "Unit", "Low", "Base", "High", "Stress", "Live", "Tag", "Source"], 1):
    wi.cell(4, j, h).font = BOLD
REF = {}; r = 5
def add_input(k, vals, unit, tag, src):
    global r
    wi.cell(r, 1, k); wi.cell(r, 2, unit)
    for j, x in enumerate(vals, 3):
        wi.cell(r, j, x).font = BLUE
    wi.cell(r, 7, f"=CHOOSE($C$2,C{r},D{r},E{r},F{r})")
    wi.cell(r, 8, tag); wi.cell(r, 9, src)
    fmt = PCT if (isinstance(vals[1], float) and vals[1] < 1) else INR
    for j in range(3, 8): wi.cell(r, j).number_format = fmt
    REF[k] = f"Inputs!$G${r}"; r += 1
wi.cell(r, 1, "Pilot and engine inputs (Step 7)").font = BOLD; r += 1
for k, ((lo, ba, hi), unit, tag, src) in m.I.items():
    if k == "shops_per_cluster": continue
    if k in OVR: lo = ba = hi = OVR[k]; src = "7b lever 2: commission moved to Protect"
    add_input(k, (lo, ba, hi, ba), unit, tag, src)
r += 1; wi.cell(r, 1, "7b levers").font = BOLD; r += 1
for k, (vals, unit, tag, src) in LEV.items():
    add_input(k, vals, unit, tag, src)
r += 1; wi.cell(r, 1, "Cluster rollout path (clusters at end of year 1..8)").font = BOLD; r += 1
for j in range(8): wi.cell(r, 3 + j, f"Y{j+1}").font = BOLD
r += 1; PATH_ROW = {}
for sc, nm in ((1, "Low"), (2, "Base"), (3, "High"), (4, "Stress")):
    wi.cell(r, 1, f"Path {nm}")
    for j, x in enumerate(PATHS[sc]): wi.cell(r, 3 + j, x).font = BLUE
    PATH_ROW[sc] = r; r += 1
wi.cell(r, 1, "Path live")
for j in range(8):
    c = CL_(3 + j); wi.cell(r, 3 + j, f"=CHOOSE($C$2,{c}{PATH_ROW[1]},{c}{PATH_ROW[2]},{c}{PATH_ROW[3]},{c}{PATH_ROW[4]})")
PATH_LIVE = r; r += 1
wi.cell(r, 1, "Step 7 reference path (for HQ scaling)")
for j, x in enumerate(m.CLUSTERS_END): wi.cell(r, 3 + j, x).font = BLUE
PATH_REF = r
for col, w in zip("ABCDEFGHI", (28, 30, 12, 12, 12, 12, 12, 14, 60)):
    wi.column_dimensions[col].width = w

# ------------------------------------------------ Shop: two contribution columns (early parts margin, mature parts margin)
wsh = wb.create_sheet("Shop")
wsh["A1"] = "One shop, per year. Contribution at the opening-year parts margin (L/N) and with central parts buying (O/P)."; wsh["A1"].font = BOLD
cols = ["Line", "Category mix", "Out-of-warranty share", "Events per unit-yr", "Ticket incl GST (₹)", "Parts share", "Parts margin (opening)",
        "Basis (1 = OOW)", "Units in base", "Jobs / yr", "Net per job (₹)", "Contribution per job (₹)", "Revenue / yr (₹)", "Contribution / yr (₹)",
        "Contribution per job, central parts (₹)", "Contribution / yr, central parts (₹)"]
for j, h in enumerate(cols, 1): wsh.cell(3, j, h).font = BOLD
row = first = 4
for cat, mix, oow, jobs, amc in m.CAT:
    for ev, tk, ps, pm, basis in jobs:
        wsh.cell(row, 1, f"{cat}: service/repair (₹{tk})")
        for j, x in ((2, mix), (3, oow), (4, ev), (5, tk), (6, ps), (8, 1 if basis == "oow" else 0)):
            wsh.cell(row, j, x).font = BLUE
        g = wsh.cell(row, 7, pm if pm is not None else f"={REF['parts_margin']}"); g.font = BLUE if pm is not None else GREEN
        pm2 = str(pm) if pm is not None else REF["parts_margin_mature"]
        wsh.cell(row, 9, f"={REF['units_month']}*B{row}*12*{REF['years_base']}*0.9")
        wsh.cell(row, 10, f"=I{row}*IF(H{row}=1,C{row},1)*D{row}*{REF['capture']}*(1-{REF['leakage']})")
        wsh.cell(row, 11, f"=E{row}/1.18")
        tail = f"-K{row}*(1-F{row})*{REF['labour_payout']}-K{row}*({REF['comm_repair']}+{REF['rework']}+{REF['levy']})-{REF['tech_cost']}-{REF['insurance']}"
        wsh.cell(row, 12, f"=K{row}-K{row}*F{row}*(1-G{row})" + tail)
        wsh.cell(row, 15, f"=K{row}-K{row}*F{row}*(1-{pm2})" + tail)
        wsh.cell(row, 13, f"=J{row}*K{row}"); wsh.cell(row, 14, f"=J{row}*L{row}"); wsh.cell(row, 16, f"=J{row}*O{row}")
        row += 1
    if amc:
        price, vis, vk = amc
        wsh.cell(row, 1, f"{cat}: AMC (₹{price}, {vis} visits)")
        for j, x in ((2, mix), (3, oow), (5, price), (4, vis)):
            wsh.cell(row, j, x).font = BLUE
        wsh.cell(row, 9, f"={REF['units_month']}*B{row}*12*{REF['years_base']}*0.9")
        wsh.cell(row, 10, f"=I{row}*C{row}*{REF['amc_attach']}*(1-{REF['leakage']})")
        wsh.cell(row, 11, f"=E{row}/1.18")
        wsh.cell(row, 12, f"=K{row}-D{row}*{REF[vk]}-K{row}*({REF['comm_amc']}+{REF['levy']})-50-2*{REF['tech_cost']}")
        wsh.cell(row, 15, f"=L{row}")
        wsh.cell(row, 13, f"=J{row}*K{row}"); wsh.cell(row, 14, f"=J{row}*L{row}"); wsh.cell(row, 16, f"=J{row}*O{row}")
        row += 1
wsh.cell(row, 1, "AC install (brand-authorised, sub-contract)"); wsh.cell(row, 2, 0.30).font = BLUE
wsh.cell(row, 10, f"={REF['units_month']}*B{row}*12*{REF['auth_cov']}*{REF['routing']}")
wsh.cell(row, 11, f"={REF['ac_install_net']}+{REF['materials_net']}")
wsh.cell(row, 12, f"=K{row}-{REF['materials_net']}*(1-{REF['materials_margin']})-{REF['ac_install_payout']}-{REF['ac_install_net']}*({REF['comm_install']}+{REF['rework']}+{REF['levy']})-{REF['tech_cost']}-{REF['insurance']}")
wsh.cell(row, 15, f"=L{row}")
wsh.cell(row, 13, f"=J{row}*K{row}"); wsh.cell(row, 14, f"=J{row}*L{row}"); wsh.cell(row, 16, f"=J{row}*O{row}"); row += 1
wsh.cell(row, 1, "Washing-machine install"); wsh.cell(row, 2, 0.15).font = BLUE
wsh.cell(row, 10, f"={REF['units_month']}*B{row}*12*0.9*{REF['other_install_capture']}")
wsh.cell(row, 11, f"={REF['wm_install_net']}")
wsh.cell(row, 12, f"=K{row}-{REF['wm_install_payout']}-K{row}*({REF['comm_install']}+{REF['levy']})-{REF['tech_cost']}-{REF['insurance']}")
wsh.cell(row, 15, f"=L{row}")
wsh.cell(row, 13, f"=J{row}*K{row}"); wsh.cell(row, 14, f"=J{row}*L{row}"); wsh.cell(row, 16, f"=J{row}*O{row}"); last = row; row += 2
TOT = row
wsh.cell(row, 1, "TOTAL core service per mature shop per year").font = BOLD
for c in "JMNP": wsh[f"{c}{row}"] = f"=SUM({c}{first}:{c}{last})"
SHOP_REV, SHOP_CON0, SHOP_CON1 = f"Shop!$M${TOT}", f"Shop!$N${TOT}", f"Shop!$P${TOT}"
row += 2
wsh.cell(row, 1, "Keepwell Protect per mature shop").font = BOLD; row += 1
NET = f"({REF['protect_price']}/1.18)"
prot = [
    ("Plans sold per year", f"={REF['units_month']}*12*{REF['covered_share']}*{REF['protect_attach']}", '#,##0.0'),
    ("Net price per plan (₹)", f"={NET}", INR),
    ("Contribution per plan (₹): net × (1 − commission − claims − admin)", f"={NET}*(1-{REF['protect_comm']}-{REF['claims_ratio']}-{REF['protect_admin']})", INR),
    ("Protect contribution per shop (₹)", f"=B{row}*B{row+2}", INR),
    ("Lost repair revenue (covered repairs no longer billed) (₹)", f"={SHOP_REV}*{REF['repair_share_core']}*{REF['covered_share']}*{REF['protect_attach']}*(2/4.5)", INR),
    ("Mature shop revenue incl. Protect (₹)", f"={SHOP_REV}-B{row+4}+B{row}*B{row+1}", INR),
    ("Mature shop contribution incl. Protect and central parts (₹)", f"={SHOP_CON1}+B{row+3}-B{row+4}*0.17", INR),
]
PR = {}
for i, (lab, f, fmt) in enumerate(prot):
    wsh.cell(row + i, 1, lab); c = wsh.cell(row + i, 2, f); c.number_format = fmt
    PR[i] = f"Shop!$B${row+i}"
for rr in range(first, TOT + 1):
    for j in (9, 10): wsh.cell(rr, j).number_format = '#,##0.0'
    for j in (11, 12, 13, 14, 15, 16): wsh.cell(rr, j).number_format = INR
    for j in (2, 3, 6, 7): wsh.cell(rr, j).number_format = PCT
wsh.column_dimensions["A"].width = 62
for j in range(2, 17): wsh.column_dimensions[CL_(j)].width = 14

# ------------------------------------------------ Cluster
wc = wb.create_sheet("Cluster")
wc["A1"] = "One mature cluster (age 4+), per year"; wc["A1"].font = BOLD
wc["B2"] = "Keepwell-run"; wc["C2"] = "Partner-run"; wc["B2"].font = wc["C2"].font = BOLD
S = REF["shops_per_cluster"]
PLANREV = f"{REF['plan_jobs_m']}*12*{REF['plan_rev']}"; PLANCON = f"{REF['plan_jobs_m']}*12*{REF['plan_contrib']}"
rowsC = [
    ("Shops per cluster", f"={S}", f"={S}", '#,##0'),
    ("Revenue (₹)", f"={PR[5]}*B3+{PLANREV}", "=B4", INR),
    ("Shop contribution (₹)", f"={PR[6]}*B3", f"={PR[6]}*C3", INR),
    ("Plan-seller fulfilment contribution (₹)", f"={PLANCON}", f"={PLANCON}", INR),
    ("Off-season floor (own) / partner fee (partner) (₹)", f"=-{REF['floor_topup_y']}", f"=-{REF['partner_fee']}*{SHOP_REV}*C3", INR),
    ("Cluster contribution (₹)", "=B5+B6+B7", "=C5+C6+C7", INR),
    ("Keepwell fixed cost for the cluster (₹)", f"=-{REF['cluster_fixed_m']}*12", f"=-{REF['partner_fixed_m']}*12", INR),
    ("Cluster EBITDA (₹)", "=B8+B9", "=C8+C9", INR),
    ("Cluster EBITDA margin", "=B10/B4", "=C10/C4", PCT),
    ("Breakeven shops (Keepwell-run)", f"=({REF['cluster_fixed_m']}*12+{REF['floor_topup_y']}-B6)/{PR[6]}", "", '#,##0.0'),
]
for i, (lab, fb, fc, fmt) in enumerate(rowsC, 3):
    wc.cell(i, 1, lab)
    for j, f in ((2, fb), (3, fc)):
        if f: c = wc.cell(i, j, f); c.number_format = fmt
wc.column_dimensions["A"].width = 54; wc.column_dimensions["B"].width = 18; wc.column_dimensions["C"].width = 18

# ------------------------------------------------ Plan
wp = wb.create_sheet("Plan")
wp["A1"] = "8-year plan (Year 1 = 2027). Columns B,C = years −2,−1; D = year 0 (pilot, 2026); E..L = years 1..8."; wp["A1"].font = BOLD
yc = {t: CL_(4 + t) for t in range(-2, 9)}
wp.cell(3, 1, "Year").font = BOLD
for t in range(-2, 9): wp.cell(3, 4 + t, t).font = BOLD
RW = {}; nxt = [4]
def put(key, label, fn, fmt=INR, years=range(1, 9), zero_before=True):
    rr = nxt[0]; nxt[0] += 1; RW[key] = rr
    wp.cell(rr, 1, label)
    if zero_before:
        for t in range(-2, min(years)):
            wp.cell(rr, 4 + t, 0).number_format = fmt
    for t in years:
        c = wp.cell(rr, 4 + t, fn(t)); c.number_format = fmt
    return rr
def gap(): nxt[0] += 1
y = lambda key, t: f"{yc[t]}{RW[key]}"
put("E", "Clusters (end of year)", lambda t: (1 if t == 0 else f"=Inputs!{CL_(2 + t)}{PATH_LIVE}"), '#,##0', range(0, 9))
put("N", "New clusters opened", lambda t: f"={y('E',t)}-{y('E',t-1)}", '#,##0', range(-1, 9))
wp.cell(RW["N"], 2, 0)
put("No", "New Keepwell-run clusters", lambda t: f"=IF({yc[t]}$3<{REF['partner_from']},{y('N',t)},0)", '#,##0', range(-1, 9))
wp.cell(RW["No"], 2, 0)
put("Np", "New partner clusters", lambda t: f"={y('N',t)}-{y('No',t)}", '#,##0', range(-1, 9))
wp.cell(RW["Np"], 2, 0)
put("Eo", "Keepwell-run clusters (end of year)", lambda t: f"={y('No',t)}" + (f"+{y('Eo',t-1)}" if t > -1 else ""), '#,##0', range(-1, 9))
wp.cell(RW["Eo"], 2, 0)
put("Ep", "Partner clusters (end of year)", lambda t: f"={y('E',t)}-{y('Eo',t)}", '#,##0', range(0, 9))
put("Sh", "Shops (end of year)", lambda t: f"={y('E',t)}*{S}", '#,##0', range(0, 9))
M0, M1, M2, M3 = m.MAT; R0, R1, R2 = LV["attach_ramp"]
def eqf(nk, ek, t):
    return f"={y(nk,t)}*{M0}+{y(nk,t-1)}*{M1}+{y(nk,t-2)}*{M2}+{y(ek,t-3) if t-3>=-1 else 0}*{M3}"
put("eq", "Mature-cluster equivalents (ramp 25/60/90/100%)", lambda t: eqf("N", "E", t) if t >= 2 else f"={y('N',t)}*{M0}+{y('N',t-1)}*{M1}+{y('N',t-2)}*{M2}", '#,##0.00')
put("eqo", "… of which Keepwell-run", lambda t: (eqf("No", "Eo", t) if t >= 2 else f"={y('No',t)}*{M0}+{y('No',t-1)}*{M1}+{y('No',t-2)}*{M2}"), '#,##0.00')
put("eqp", "… of which partner", lambda t: f"={y('eq',t)}-{y('eqo',t)}", '#,##0.00')
put("eqa", "Equivalents aged 1+ (get central parts margin)", lambda t: f"={y('eq',t)}-{y('N',t)}*{M0}", '#,##0.00')
put("att", "Protect-weighted equivalents (maturity × attach ramp)",
    lambda t: f"={y('N',t)}*{M0*R0}+{y('N',t-1)}*{M1*R1}+{y('N',t-2)}*{M2*R2}+" + (f"{y('E',t-3)}*{M3*R2}" if t - 3 >= -1 else "0"), '#,##0.00')
gap()
put("core", "Core service revenue (after lost covered repairs) (₹)", lambda t: f"={SHOP_REV}*{S}*{y('eq',t)}*(1-{REF['repair_share_core']}*{REF['covered_share']}*{REF['protect_attach']}*(2/4.5))")
put("plan", "Plan-seller fulfilment revenue (₹)", lambda t: f"={PLANREV}*{y('eq',t)}")
put("sold", "Protect plans sold", lambda t: f"={REF['units_month']}*12*{S}*{REF['covered_share']}*{REF['protect_attach']}*{y('att',t)}", '#,##0', range(-1, 9))
wp.cell(RW["sold"], 2, 0)
put("prot", "Keepwell Protect revenue (half in each of 2 covered years) (₹)", lambda t: f"=0.5*({y('sold',t-1)}+{y('sold',t-2)})*{NET}")
L0 = nxt[0]; LROWS = []
for i, (name, st, rv, cs, kind) in enumerate(m.LAYERS):
    rr = nxt[0]; nxt[0] += 1; LROWS.append(rr)
    wp.cell(rr, 1, f"{name} (₹)")
    wp.cell(rr, 14, st).font = BLUE; wp.cell(rr, 15, rv).font = BLUE; wp.cell(rr, 16, cs).font = BLUE; wp.cell(rr, 17, 1 if kind == "data" else 0).font = BLUE
    for t in range(1, 9):
        wp.cell(rr, 4 + t, f"=IF({yc[t]}$3>=$N{rr},$O{rr}*{y('eq',t)}*CHOOSE(MIN({yc[t]}$3-$N{rr},2)+1,{m.LRAMP[0]},{m.LRAMP[1]},{m.LRAMP[2]})*IF($Q{rr}=1,{REF['layer_k']},1),0)").number_format = INR
for j, h in zip((14, 15, 16, 17), ("Start year", "Revenue per mature cluster (₹/yr)", "Contribution share", "Data layer (1)")):
    wp.cell(L0 - 1, j, h).font = BOLD
LEND = nxt[0] - 1
put("entb", "Brand data contracts, BASE path (₹) [Assumption]", lambda t: m.ENTERPRISE[t - 1])
for t in range(1, 9): wp.cell(RW["entb"], 4 + t).font = BLUE
put("ent", "Brand data contracts × adoption (₹)", lambda t: f"={y('entb',t)}*{REF['layer_k']}")
gap()
put("rev", "TOTAL REVENUE (₹)", lambda t: f"={y('core',t)}+{y('plan',t)}+{y('prot',t)}+SUM({yc[t]}{L0}:{yc[t]}{LEND})+{y('ent',t)}")
put("data", "of which data layers (₹)", lambda t: "=" + "+".join(f"{yc[t]}{rr}" for rr, l in zip(LROWS, m.LAYERS) if l[4] == "data") + f"+{y('ent',t)}")
LOST = f"{SHOP_REV}*{S}*{{eq}}*{REF['repair_share_core']}*{REF['covered_share']}*{REF['protect_attach']}*(2/4.5)"
put("con_core", "Core + plan-seller contribution, after floor (own) and lost repairs (₹)",
    lambda t: f"={SHOP_CON0}*{S}*{y('eq',t)}+({SHOP_CON1}-{SHOP_CON0})*{S}*{y('eqa',t)}+{PLANCON}*{y('eq',t)}-{LOST.format(eq=y('eq',t))}*0.17-{REF['floor_topup_y']}*{y('eqo',t)}")
put("pfee", "Partner fees incl. opening-year floor (₹)",
    lambda t: f"=-{REF['partner_fee']}*{SHOP_REV}*{S}*{y('eqp',t)}-{y('Np',t)}*MAX(0,{REF['partner_open_floor']}-{REF['partner_fee']}*{SHOP_REV}*{S}*{M0})")
put("pcon", "Protect contribution: recognised × (1 − claims − admin) − commission on plans sold (₹)",
    lambda t: f"={y('prot',t)}*(1-{REF['claims_ratio']}-{REF['protect_admin']})-{y('sold',t)}*{NET}*{REF['protect_comm']}")
put("lcon", "Layer and brand-data contribution (₹)", lambda t: f"=SUMPRODUCT({yc[t]}{L0}:{yc[t]}{LEND},$P{L0}:$P{LEND})+{y('ent',t)}*0.75")
put("dcon", "of which data contribution (₹)", lambda t: f"=SUMPRODUCT({yc[t]}{L0}:{yc[t]}{LEND},$P{L0}:$P{LEND},$Q{L0}:$Q{LEND})+{y('ent',t)}*0.75")
put("con", "CONTRIBUTION (₹)", lambda t: f"={y('con_core',t)}+{y('pfee',t)}+{y('pcon',t)}+{y('lcon',t)}")
put("conm", "Contribution margin", lambda t: f"={y('con',t)}/{y('rev',t)}", PCT)
put("fees", "Payment and gateway fees (₹)", lambda t: f"=-{y('rev',t)}*{REF['pay_fee']}")
put("fix", "Cluster fixed costs: own team / partner support (₹)",
    lambda t: f"=-{REF['cluster_fixed_m']}*12*({y('Eo',t-1)}+0.5*{y('No',t)})-{REF['partner_fixed_m']}*12*({y('Ep',t-1)}+0.5*{y('Np',t)})")
put("hqb", "HQ, Step 7 headcount path (₹) [Assumption]", lambda t: m.HQ[t - 1])
for t in range(1, 9): wp.cell(RW["hqb"], 4 + t).font = BLUE
put("hq", "HQ × scale × multiplier × (½ fixed + ½ per cluster vs Step 7 path) (₹)",
    lambda t: f"=-{y('hqb',t)}*{REF['hq_scale']}*{REF['hq_mult']}*(0.5+0.5*{y('E',t)}/Inputs!{CL_(2+t)}{PATH_REF})")
put("cac", "Shop acquisition: new shops (own / partner rates) + churn replacement (₹)",
    lambda t: f"=-({y('No',t)}*{S}*{REF['shop_cac']}+{y('Np',t)}*{S}*{REF['partner_cac']}+{y('E',t-1)}*{S}*{REF['shop_churn']}*{REF['shop_cac']})")
put("ebitda", "EBITDA (₹)", lambda t: f"={y('con',t)}+{y('fees',t)}+{y('fix',t)}+{y('hq',t)}+{y('cac',t)}")
put("ebm", "EBITDA margin", lambda t: f"={y('ebitda',t)}/{y('rev',t)}", PCT)
put("svc", "Service-only EBITDA (excl. data contribution) (₹)", lambda t: f"={y('ebitda',t)}-{y('dcon',t)}")
gap()
put("capex", "Cluster set-up, WC and parts stock (₹)",
    lambda t: f"=-{y('No',t)}*({REF['setup']}+{REF['wc']}+IF({yc[t]}3>=2,{REF['parts_stock']},0))-{y('Np',t)}*({REF['partner_setup']}+{REF['wc']}+{REF['parts_stock']}*0.5)")
put("dnwc", "Working capital for growth (₹)", lambda t: f"=-MAX(0,{y('rev',t)}-{y('rev',t-1)})*{REF['nwc_pct']}")
def depf(t):
    yrs = [oy for oy in range(max(1, t - 2), t + 1)]
    return "=" + "+".join(f"{y('No',oy)}*{REF['setup']}/3+{y('Np',oy)}*{REF['partner_setup']}/3" for oy in yrs)
put("dep", "Depreciation of set-up, 3 years (₹)", depf)
put("taxable", "Taxable profit (₹)", lambda t: f"={y('ebitda',t)}-{y('dep',t)}")
put("pool", "Tax-loss pool, end of year (₹)", lambda t: f"=MAX(0,{y('pool',t-1)}-{y('taxable',t)})")
put("tax", "Tax (₹)", lambda t: f"=-MAX(0,{y('taxable',t)}-{y('pool',t-1)})*{REF['tax_rate']}")
put("U", "Unearned Protect revenue, end of year (₹)", lambda t: f"=({y('sold',t)}+0.5*{y('sold',t-1)})*{NET}")
put("Rz", "Ring-fenced claims reserve (₹)", lambda t: f"={y('U',t)}*{REF['claims_ratio']}*{REF['reserve_share']}")
put("flt", "Usable plan cash: Δ unearned − Δ reserve (₹)", lambda t: f"=({y('U',t)}-{y('U',t-1)})-({y('Rz',t)}-{y('Rz',t-1)})")
put("cf", "Cash flow before financing (₹)", lambda t: f"={y('ebitda',t)}+{y('capex',t)}+{y('dnwc',t)}+{y('tax',t)}+{y('flt',t)}")
put("cum", "Cumulative cash, incl. ₹18 L opening (₹)", lambda t: f"={y('cf',t)}+" + (y('cum', t - 1) if t > 1 else REF['start_cash']))
put("cumnf", "Cumulative cash without any plan cash (₹)", lambda t: f"={y('cf',t)}-{y('flt',t)}+" + (y('cumnf', t - 1) if t > 1 else REF['start_cash']))
gap()
PK = nxt[0]
wp.cell(PK, 1, "PEAK FUNDING NEED (₹)").font = BOLD
wp.cell(PK, 5, f"=-MIN(0,MIN(E{RW['cum']}:L{RW['cum']}))").number_format = INR
wp.cell(PK + 1, 1, "Peak need without any plan cash (₹)")
wp.cell(PK + 1, 5, f"=-MIN(0,MIN(E{RW['cumnf']}:L{RW['cumnf']}))").number_format = INR
wp.cell(PK + 3, 1, "Exit value check (operator revenue × 2.5 + data revenue × 7)").font = BOLD
for i, (t, col) in enumerate(((7, "K"), (8, "L"))):
    wp.cell(PK + 4 + i, 1, f"Year {t} EV (₹)")
    wp.cell(PK + 4 + i, 5, f"=({col}{RW['rev']}-{col}{RW['data']})*2.5+{col}{RW['data']}*7").number_format = INR
wp.column_dimensions["A"].width = 78
for j in range(2, 18): wp.column_dimensions[CL_(j)].width = 15
PLAN = dict(RW, peak=PK, ev=PK + 4)

# ------------------------------------------------ Sensitivity (values from plan_v3)
wsn = wb.create_sheet("Sensitivity")
wsn["A1"] = "One-at-a-time sensitivity on BASE (values from model/plan_v3.py at build time; rebuild to refresh)"; wsn["A1"].font = BOLD
for j, h in enumerate(["Change", "Year-7 EBITDA (₹ Cr)", "Year-8 EBITDA %", "Peak funding need (₹ Cr)", "First EBITDA-positive year"], 1):
    wsn.cell(3, j, h).font = BOLD
cases = [("BASE", {}), ("Protect attach 5%", dict(protect_attach=0.05)), ("Protect attach 0% (no Protect)", dict(protect_attach=0.0)),
         ("Protect attach 12%", dict(protect_attach=0.12)), ("Claims 45%", dict(claims_ratio=0.45)), ("Claims 55%", dict(claims_ratio=0.55)),
         ("Shop commission on Protect 40%", dict(protect_comm=0.40)), ("Parts margin stays 20%", dict(parts_margin_mature=0.20)),
         ("Partner fee 12%", dict(partner_fee=0.12)), ("No partners (all Keepwell-run)", dict(partner_from=99)),
         ("50 shops per cluster", dict(shops_per_cluster=50)), ("Step 7 rollout (52 clusters by Y8)", dict(clusters_end=m.CLUSTERS_END)),
         ("HQ at 1.0× Step 7 path", dict(hq_scale=1.0)), ("STRESS (planning case)", V.STRESS)]
for i, (lab, d) in enumerate(cases, 4):
    rr_, pk, uu = V.run("base", d)
    fp = next((x["year"] for x in rr_ if x["ebitda"] > 0), "never")
    vals = (lab, round(rr_[6]["ebitda"] / 1e7, 2), round(rr_[7]["ebitda"] / rr_[7]["revenue"], 3), round(pk["peak"] / 1e7, 2), fp)
    for j, x in enumerate(vals, 1):
        c = wsn.cell(i, j, x)
        if j == 3: c.number_format = PCT
rr_, pk, uu = V.run("low", V.LOWX); wsn.cell(4 + len(cases), 1, "LOW (all pilot inputs pessimistic)")
wsn.cell(4 + len(cases), 2, round(rr_[6]["ebitda"] / 1e7, 2)); wsn.cell(4 + len(cases), 3, round(rr_[7]["ebitda"] / rr_[7]["revenue"], 3)).number_format = PCT
wsn.cell(4 + len(cases), 4, round(pk["peak"] / 1e7, 2)); wsn.cell(4 + len(cases), 5, next((x["year"] for x in rr_ if x["ebitda"] > 0), "never"))
wsn.column_dimensions["A"].width = 40
for c_ in "BCDE": wsn.column_dimensions[c_].width = 24

wb.save(OUT)
json.dump(PLAN, open(pathlib.Path(__file__).parent / "plan_rows_v3.json", "w"))
print("saved", OUT, "scenario", SCEN)
