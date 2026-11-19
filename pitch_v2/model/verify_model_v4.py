import json, pathlib
from openpyxl import load_workbook
import simple_model as S
R = json.load(open(pathlib.Path(__file__).parent / "rows_v4.json"))
wb = load_workbook(pathlib.Path(__file__).parent.parent / "keepwell_model.xlsx", data_only=True)
pr, pt = S.pilot(); u = S.unit(); pl, need = S.plan(); d = S.deal(); bad = 0
def chk(a, b, lab):
    global bad
    if abs((a or 0) - b) > max(1, abs(b) * 1e-6): bad += 1; print("MISMATCH", lab, a, b)
p = wb["Pilot"]; t = R["pilot_total"]
chk(p.cell(t, 3).value, pt["revenue"], "pilot rev"); chk(p.cell(t, 4).value, pt["contribution"], "pilot con"); chk(p.cell(t, 6).value, pt["ebitda"], "pilot ebitda")
rm = S.retailer_month(); un = wb["Unit"]; chk(un["B19"].value, rm["con"], "retailer contribution"); chk(un["B20"].value, 0, "split check"); chk(un["B25"].value, 0, "lift check"); chk(un["B26"].value, rm["oct_cluster"], "oct cluster"); chk(un["B27"].value, rm["mature_cluster_month"], "mature cluster month"); chk(un["B8"].value, u["cluster_ebitda"], "cluster ebitda"); chk(un["B10"].value * 1000, u["breakeven"] * 1000, "breakeven")
pw = wb["Plan"]
for j, r in enumerate(pl):
    for k, key in (("Revenue (₹)", "revenue"), ("EBITDA (₹)", "ebitda"), ("Cumulative cash (₹)", "cum_cash")):
        chk(pw.cell(R["plan"][k], 3 + j).value, r[key], f"{key} Y{j+1}")
chk(pw.cell(R["peak"], 2).value, need, "peak")
dw = wb["Deal"]; chk(dw["B13"].value, d["ev"], "EV"); chk(dw["B16"].value * 1000, d["multiple"] * 1000, "multiple"); chk(dw["B19"].value, d["scorecard"], "scorecard")
print(f"checks done | mismatches {bad} | peak {need/1e7:.2f} Cr | Y1 EBITDA {pl[0]['ebitda']/1e7:.2f} Cr | EV {d['ev']/1e7:.0f} Cr | {d['multiple']:.1f}x")
