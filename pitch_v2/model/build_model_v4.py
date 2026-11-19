"""Build keepwell_model.xlsx (v4, simple) with live formulas. Mirrors simple_model.py; verify_model_v4.py checks it.
    <venv>/bin/python build_model_v4.py
Blue = inputs, black = formulas. One unit drives everything: the active retailer."""
import pathlib, json
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill
from openpyxl.utils import get_column_letter as C
import simple_model as S
OUT = pathlib.Path(__file__).parent.parent / "keepwell_model.xlsx"
F = "Arial"; BLUE = Font(name=F, color="0000FF"); BOLD = Font(name=F, bold=True); BLACK = Font(name=F)
INR = '#,##0;(#,##0);"-"'; PCT = '0.0%;(0.0%);"-"'; CRF = '#,##0.00,,,," Cr";(#,##0.00,,,," Cr");"-"'
wb = Workbook(); ws = wb.active; ws.title = "README"
for i, t in enumerate(["Keepwell financial model (v4, simple). One unit drives everything: the active retailer.",
    "Pilot: one cluster, Vijayawada–Guntur, Mar–Oct 2026 (monthly). Unit: one mature retailer and one mature cluster.",
    "Plan: 5 years from the March 2027 close. EBITDA is positive from year 1; the seed funds cluster launches and working capital.",
    "Deal: ₹2.5 Cr CCPS at ₹10 Cr pre-money (single close); cap table; exit at 15× year-5 EBITDA; IRR; VC-method ceiling; course scorecard.",
    "Blue cells are inputs. Python mirror: model/simple_model.py. Check: model/verify_model_v4.py."], 1):
    ws.cell(i, 1, t).font = BOLD if i == 1 else BLACK
ws.column_dimensions["A"].width = 130
# ---------------- Inputs
wi = wb.create_sheet("Inputs"); wi["A1"] = "Inputs (blue)"; wi["A1"].font = BOLD
REF = {}; r = 3
def inp(k, label, v, fmt=INR):
    global r
    wi.cell(r, 1, label); c = wi.cell(r, 2, v); c.font = BLUE; c.number_format = fmt; REF[k] = f"Inputs!$B${r}"; r += 1
inp("p_rev", "Pilot: revenue per active retailer per month (₹, net of GST)", S.P["rev_per_retailer_month"])
inp("p_cm", "Pilot: contribution margin", S.P["contrib_margin"], PCT)
inp("p_team", "Pilot: cluster team cost per month (₹)", S.P["cluster_team_month"])
inp("p_job", "Pilot: average revenue per job (₹)", S.P["avg_job"])
r += 1
inp("u_rev", "Mature retailer: revenue per month (₹)", S.U["rev_per_retailer_month"])
inp("u_cm", "Mature retailer: contribution margin", S.U["contrib_margin"], PCT)
inp("u_n", "Retailers per mature cluster", S.U["retailers_per_cluster"], '#,##0')
inp("u_cost", "Mature cluster team cost per year (₹)", S.U["cluster_cost_year"])
r += 1
inp("y_clcost", "Plan: cluster team cost per cluster-year (₹)", S.Y["cluster_cost_year"])
inp("y_launch", "Plan: launch cost per new cluster (₹): set-up, parts stock, onboarding, training", S.Y["launch_per_cluster"])
inp("y_wc", "Plan: working capital, share of each year's revenue increase", S.Y["wc_share"], PCT)
inp("y_tax", "Plan: tax rate on positive EBITDA", S.Y["tax"], PCT)
inp("y_r0", "Plan: retailers at the close", S.Y["start_retailers"], '#,##0')
inp("y_c0", "Plan: clusters at the close", S.Y["start_clusters"], '#,##0')
inp("y_cash0", "Plan: cash at the close (₹)", S.Y["start_cash"])
inp("y_prev", "Plan: pilot revenue run-rate before year 1 (₹/yr)", S.Y["pilot_rev_run"])
r += 1
inp("d_seed", "Seed amount (₹), single close", S.D["seed"]); inp("d_pre", "Seed pre-money (₹)", S.D["pre"])
inp("d_isafe", "Pre-seed iSAFE (₹)", S.D["isafe"]); inp("d_cap", "iSAFE post-money cap (₹)", S.D["isafe_cap_post"])
inp("d_pool", "ESOP pool, share of post-seed", S.D["pool_post"], PCT); inp("d_mult", "Exit multiple on year-5 EBITDA (×)", S.D["exit_ebitda_mult"], '0"×"')
inp("d_bval", "Course scorecard: benchmark pre-money (₹)", S.D["benchmark_val"]); inp("d_score", "Our fundability score (/100)", S.D["score"], '0')
inp("d_bscore", "Course benchmark score", S.D["benchmark_score"], '0')
wi.column_dimensions["A"].width = 78; wi.column_dimensions["B"].width = 18
# ---------------- Pilot (monthly)
wp = wb.create_sheet("Pilot"); wp["A1"] = "Pilot, one cluster, Vijayawada–Guntur, Mar–Oct 2026"; wp["A1"].font = BOLD
hdr = ["Month", "Active retailers", "Revenue (₹)", "Contribution (₹)", "Cluster team (₹)", "Cluster EBITDA (₹)", "Jobs"]
for j, h in enumerate(hdr, 1): wp.cell(3, j, h).font = BOLD
for i, (m, a) in enumerate(zip(S.P["months"], S.P["active"]), 4):
    wp.cell(i, 1, m); c = wp.cell(i, 2, a); c.font = BLUE
    wp.cell(i, 3, f"=B{i}*{REF['p_rev']}"); wp.cell(i, 4, f"=C{i}*{REF['p_cm']}"); wp.cell(i, 5, f"={REF['p_team']}")
    wp.cell(i, 6, f"=D{i}-E{i}"); wp.cell(i, 7, f"=C{i}/{REF['p_job']}")
    for j in (3, 4, 5, 6): wp.cell(i, j).number_format = INR
    wp.cell(i, 7).number_format = '#,##0'
T = 12; wp.cell(T, 1, "Total, 8 months").font = BOLD
for j in range(2, 8):
    col = C(j); wp.cell(T, j, f"=SUM({col}4:{col}11)").number_format = INR if j < 7 else '#,##0'
wp.cell(T + 2, 1, "Contribution per active retailer per month (₹)"); wp.cell(T + 2, 2, f"={REF['p_rev']}*{REF['p_cm']}").number_format = INR
wp.cell(T + 3, 1, "Breakeven: active retailers that pay for the cluster team"); wp.cell(T + 3, 2, f"={REF['p_team']}/B{T+2}").number_format = '0.0'
wp.cell(T + 4, 1, "Contribution margin, pilot total"); wp.cell(T + 4, 2, f"=D{T}/C{T}").number_format = PCT
wp.column_dimensions["A"].width = 58
for j in range(2, 8): wp.column_dimensions[C(j)].width = 18
# ---------------- Unit
wu = wb.create_sheet("Unit"); wu["A1"] = "One mature retailer and one mature cluster"; wu["A1"].font = BOLD
U = [("Revenue per retailer per month (₹)", f"={REF['u_rev']}", INR), ("Contribution per retailer per month (₹)", f"=B3*{REF['u_cm']}", INR),
     ("Cluster revenue per year (₹)", f"=B3*12*{REF['u_n']}", INR), ("Cluster contribution per year (₹)", f"=B4*12*{REF['u_n']}", INR),
     ("Cluster team cost per year (₹)", f"={REF['u_cost']}", INR), ("Cluster EBITDA per year (₹)", "=B6-B7", INR), ("Cluster EBITDA margin", "=B8/B5", PCT),
     ("Breakeven retailers per cluster", f"=B7/(B4*12)", '0.0')]
for i, (lab, f, fmt) in enumerate(U, 3): wu.cell(i, 1, lab); c = wu.cell(i, 2, f); c.number_format = fmt
wu["A13"] = "One retailer's month, opened up (pilot → mature)"; wu["A13"].font = BOLD
RM = [("Pilot revenue per retailer per month (₹)", f"={REF['p_rev']}", None), ("  − technicians (≈ ₹400 a job)", S.SPLIT["technicians"], 1), ("  − parts", S.SPLIT["parts"], 1),
      ("  − retailer commission (5% installs, 8% repairs, 12% AMC, 25% Protect)", S.SPLIT["retailer_commission"], 1), ("  − travel, payments, AI desk, guarantee reserve", S.SPLIT["other_per_job"], 1),
      ("Result: contribution per retailer per month (₹)", "=B14-SUM(B15:B18)", None), ("Check: equals pilot margin × revenue (0 = OK)", f"=ROUND(B19-B14*{REF['p_cm']},0)", None),
      ("  + Protect plans (2 a month × ₹1,700 net)", S.LIFT["protect"], 1), ("  + AMC renewals (2 a month × ₹1,100 net)", S.LIFT["amc_renewals"], 1),
      ("  + repairs on the installed base (≈1.8 × ₹2,700)", S.LIFT["installed_base_repairs"], 1), ("Result: mature revenue per retailer per month (₹)", "=B14+SUM(B21:B23)", None),
      ("Check: equals the mature input (0 = OK)", f"=B24-{REF['u_rev']}", None),
      ("Pilot cluster, October: 34 retailers × contribution − ₹1.0 L team (₹)", f"=Pilot!B11*B19-{REF['p_team']}", None),
      ("Mature cluster per month: 60 × mature contribution − team (₹)", f"={REF['u_n']}*B4-B7/12", None)]
for i, (lab, v, blue) in enumerate(RM, 14):
    wu.cell(i, 1, lab); c = wu.cell(i, 2, v); c.number_format = INR
    if blue: c.font = BLUE
wu["A30"] = "The 12 jobs behind ₹19,500 (pilot, per retailer per month; prices net of GST)"; wu["A30"].font = BOLD
for j, h in enumerate(["Job", "Jobs a month", "₹ per job", "₹ a month", "Why this price (market reference)"], 1): wu.cell(31, j, h).font = BOLD
for i, (job, n, pr, basis) in enumerate(S.JOB_MIX, 32):
    wu.cell(i, 1, job); c = wu.cell(i, 2, n); c.font = BLUE; c.number_format = '0.0'; c = wu.cell(i, 3, pr); c.font = BLUE; c.number_format = INR
    wu.cell(i, 4, f"=B{i}*C{i}").number_format = INR; wu.cell(i, 5, basis)
e = 32 + len(S.JOB_MIX); wu.cell(e, 1, "Total").font = BOLD; wu.cell(e, 2, f"=SUM(B32:B{e-1})").number_format = '0.0'; wu.cell(e, 4, f"=SUM(D32:D{e-1})").number_format = INR
wu.cell(e + 1, 1, "Average job (₹)"); wu.cell(e + 1, 4, f"=D{e}/B{e}").number_format = INR
wu.cell(e + 2, 1, "Check: equals pilot revenue per retailer (0 = OK)"); wu.cell(e + 2, 4, f"=D{e}-{REF['p_rev']}").number_format = INR
wu.column_dimensions["A"].width = 64; wu.column_dimensions["C"].width = 12; wu.column_dimensions["D"].width = 14; wu.column_dimensions["E"].width = 70; wu.column_dimensions["B"].width = 18
# ---------------- Plan
wl = wb.create_sheet("Plan"); wl["A1"] = "5-year plan (year 1 = Apr 2027–Mar 2028)"; wl["A1"].font = BOLD
for j, (y, cal) in enumerate(zip(S.Y["years"], S.Y["cal"]), 3): wl.cell(3, j, f"{y} ({cal})").font = BOLD
wl.cell(3, 2, "Start").font = BOLD
rows = ["Retailers (end of year)", "Clusters (end of year)", "Average active retailers", "Average clusters", "Revenue per retailer per year (₹)", "Contribution margin",
        "Revenue (₹)", "Contribution (₹)", "Cluster teams (₹)", "Head office (₹)", "EBITDA (₹)", "EBITDA margin", "Cluster launches (₹)", "Working capital (₹)", "Tax (₹)",
        "Cash flow (₹)", "Cumulative cash (₹)"]
RW = {k: i for i, k in enumerate(rows, 4)}
for k, i in RW.items(): wl.cell(i, 1, k)
wl.cell(RW["Retailers (end of year)"], 2, f"={REF['y_r0']}"); wl.cell(RW["Clusters (end of year)"], 2, f"={REF['y_c0']}")
wl.cell(RW["Revenue (₹)"], 2, f"={REF['y_prev']}"); wl.cell(RW["Cumulative cash (₹)"], 2, f"={REF['y_cash0']}")
for j in range(5):
    c, p = C(3 + j), C(2 + j); y = lambda k: f"{c}{RW[k]}"; yp = lambda k: f"{p}{RW[k]}"
    vals = {"Retailers (end of year)": S.Y["retailers_end"][j], "Clusters (end of year)": S.Y["clusters_end"][j],
            "Revenue per retailer per year (₹)": S.Y["rev_per_retailer_year"][j], "Contribution margin": S.Y["contrib_margin"][j], "Head office (₹)": S.Y["hq"][j]}
    for k, v in vals.items():
        cell = wl.cell(RW[k], 3 + j, v); cell.font = BLUE
    wl[y("Average active retailers")] = f"=({yp('Retailers (end of year)')}+{y('Retailers (end of year)')})/2"
    wl[y("Average clusters")] = f"=({yp('Clusters (end of year)')}+{y('Clusters (end of year)')})/2"
    wl[y("Revenue (₹)")] = f"={y('Average active retailers')}*{y('Revenue per retailer per year (₹)')}"
    wl[y("Contribution (₹)")] = f"={y('Revenue (₹)')}*{y('Contribution margin')}"
    wl[y("Cluster teams (₹)")] = f"={y('Average clusters')}*{REF['y_clcost']}"
    wl[y("EBITDA (₹)")] = f"={y('Contribution (₹)')}-{y('Cluster teams (₹)')}-{y('Head office (₹)')}"
    wl[y("EBITDA margin")] = f"={y('EBITDA (₹)')}/{y('Revenue (₹)')}"
    wl[y("Cluster launches (₹)")] = f"=({y('Clusters (end of year)')}-{yp('Clusters (end of year)')})*{REF['y_launch']}"
    wl[y("Working capital (₹)")] = f"=MAX(0,{y('Revenue (₹)')}-{yp('Revenue (₹)')})*{REF['y_wc']}"
    wl[y("Tax (₹)")] = f"=MAX(0,{y('EBITDA (₹)')})*{REF['y_tax']}"
    wl[y("Cash flow (₹)")] = f"={y('EBITDA (₹)')}-{y('Tax (₹)')}-{y('Cluster launches (₹)')}-{y('Working capital (₹)')}"
    wl[y("Cumulative cash (₹)")] = f"={yp('Cumulative cash (₹)')}+{y('Cash flow (₹)')}"
for k, i in RW.items():
    for j in range(2, 8):
        wl.cell(i, j).number_format = PCT if "margin" in k.lower() else ('#,##0' if ("Retailers" in k or "Clusters" in k or "Average" in k) else CRF)
pk = RW["Cumulative cash (₹)"] + 2
wl.cell(pk, 1, "Peak cash need (₹)").font = BOLD; wl.cell(pk, 2, f"=-MIN(0,MIN(C{RW['Cumulative cash (₹)']}:G{RW['Cumulative cash (₹)']}))").number_format = CRF
wl.cell(pk + 1, 1, "Seed (₹)"); wl.cell(pk + 1, 2, f"={REF['d_seed']}").number_format = CRF
wl.cell(pk + 2, 1, "Buffer after the peak (₹)"); wl.cell(pk + 2, 2, f"=B{pk+1}-B{pk}").number_format = CRF
wl.column_dimensions["A"].width = 40
for j in range(2, 8): wl.column_dimensions[C(j)].width = 16
# ---------------- Deal
wd = wb.create_sheet("Deal"); wd["A1"] = "The deal, cap table and the investor's return"; wd["A1"].font = BOLD
E = RW["EBITDA (₹)"]; RV = RW["Revenue (₹)"]
DL = [("Post-money (₹)", f"={REF['d_pre']}+{REF['d_seed']}", CRF), ("Seed ownership", f"={REF['d_seed']}/B3", PCT),
      ("iSAFE share of pre-money capitalisation (at the cap)", f"={REF['d_isafe']}/{REF['d_cap']}", PCT),
      ("ESOP pool share of pre-money capitalisation", f"={REF['d_pool']}/(1-B4)", PCT), ("Founders share of pre-money", "=1-B5-B6", PCT),
      ("Founders after seed", "=B7*(1-B4)", PCT), ("iSAFE after seed", "=B5*(1-B4)", PCT), ("ESOP after seed", f"={REF['d_pool']}", PCT), ("Seed after seed", "=B4", PCT),
      ("Check: cap table sums to 100%", "=B8+B9+B10+B11", PCT),
      ("Exit enterprise value: year-5 EBITDA × multiple (₹)", f"=Plan!G{E}*{REF['d_mult']}", CRF), ("… as a multiple of year-5 revenue", f"=B13/Plan!G{RV}", '0.0"×"'),
      ("Seed stake value at exit (₹)", "=B13*B4", CRF), ("Money multiple", f"=B15/{REF['d_seed']}", '0.0"×"'), ("IRR over 5 years", "=B16^(1/5)-1", PCT),
      ("VC method: max post-money for a 40% IRR over 5 years (₹)", "=B13/1.4^5", CRF),
      ("Course scorecard pre-money: benchmark × score ÷ benchmark score (₹)", f"={REF['d_bval']}*{REF['d_score']}/{REF['d_bscore']}", CRF)]
for i, (lab, f, fmt) in enumerate(DL, 3): wd.cell(i, 1, lab); c = wd.cell(i, 2, f); c.number_format = fmt
wd.column_dimensions["A"].width = 66; wd.column_dimensions["B"].width = 18
wb.save(OUT)
json.dump(dict(plan=RW, pilot_total=T, peak=pk), open(pathlib.Path(__file__).parent / "rows_v4.json", "w"))
print("saved", OUT)
