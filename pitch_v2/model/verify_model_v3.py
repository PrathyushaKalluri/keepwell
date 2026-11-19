"""Compare recalculated keepwell_model.xlsx with plan_v3.py for the scenario set in Inputs!C2."""
import json, pathlib
from openpyxl import load_workbook
import plan_v3 as V
P = json.load(open(pathlib.Path(__file__).parent / "plan_rows_v3.json"))
wb = load_workbook(pathlib.Path(__file__).parent.parent / "keepwell_model.xlsx", data_only=True)
sc = wb["Inputs"]["C2"].value
args = {1: ("low", V.LOWX), 2: ("base", {}), 3: ("high", {}), 4: ("base", V.STRESS)}[sc]
rows, pk, u = V.run(*args); ws = wb["Plan"]; bad = 0
for t in range(1, 9):
    for key, k2 in (("rev", "revenue"), ("data", "data_rev"), ("con", "contribution"), ("ebitda", "ebitda"), ("cum", "cash_cum"), ("cumnf", "cash_nofloat"), ("Rz", "reserve")):
        x = ws.cell(P[key], 4 + t).value; y = rows[t - 1][k2]
        if abs((x or 0) - y) > max(1, abs(y) * 1e-6): bad += 1; print("MISMATCH", key, t, x, y)
c = wb["Cluster"]
for lab, xv, yv in (("own EBITDA", c["B10"].value, u["own"]["ebitda"]), ("partner EBITDA", c["C10"].value, u["partner"]["ebitda"]), ("BE", c["B12"].value, u["be_shops"])):
    if abs(xv - yv) > max(1, abs(yv) * 1e-6): bad += 1; print("MISMATCH", lab, xv, yv)
print(f"scenario {sc}: peak xlsx {ws.cell(P['peak'],5).value/1e7:.2f} py {pk['peak']/1e7:.2f} | nofloat {ws.cell(P['peak']+1,5).value/1e7:.2f} py {pk['peak_nofloat']/1e7:.2f} | Y7 EBITDA {rows[6]['ebitda']/1e7:.2f} | EV7 {ws.cell(P['ev'],5).value/1e7:.1f} EV8 {ws.cell(P['ev']+1,5).value/1e7:.1f} | mismatches {bad}")

import rounds as RD
s_, a2, a3, x, out, vc = RD.returns()
f = wb["Funding"]; F = P["funding"]
nm = {1: None, 2: "BASE", 3: None, 4: "STRESS"}[sc]
chk = [(f.cell(F["ct"] + 1, 2).value, s_["Founders"]), (f.cell(F["ct"] + 4, 4).value, a3["Seed"]), (f.cell(F["ct"] + 5, 4).value, a3["Round 2 (GTM)"])]
if nm:
    for j, yr in ((2, 5), (3, 7), (4, 8)):
        chk.append((f.cell(F["rt"] + 1, j).value, out[(nm, yr)]["ev"]))
    chk.append((f.cell(F["vm"] + 2, 3).value, vc[nm][0.40]))
fb = sum(1 for a, b in chk if abs(a - b) > max(1e-6, abs(b) * 1e-6))
print(f"Funding sheet checks: {len(chk)} | mismatches {fb}")
