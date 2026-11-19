"""Compare recalculated keepwell_model.xlsx (BASE) with plan_core.py."""
import json, pathlib
from openpyxl import load_workbook
import plan_core as m
P = json.load(open(pathlib.Path(__file__).parent / "plan_rows.json"))
wb = load_workbook(pathlib.Path(__file__).parent.parent / "keepwell_model.xlsx", data_only=True)
ws = wb["Plan"]; rows, peak, u = m.plan("base"); bad = 0
for t in range(1, 9):
    col = 4 + t
    for key, pk in (("rev", "revenue"), ("data", "data_rev"), ("con", "contribution"), ("ebitda", "ebitda"), ("cum", "cash_cum")):
        x = ws.cell(P[key], col).value; y = rows[t - 1][pk]
        if abs((x or 0) - y) > max(1, abs(y) * 1e-6): bad += 1; print("MISMATCH", key, t, x, y)
xp = ws.cell(P["peak"], 5).value
print("peak xlsx", round(xp / 1e7, 2), "python", round(peak / 1e7, 2), "| cluster BE", round(wb["Cluster"]["B12"].value, 1), round(u["be_shops"], 1))
print("Y7 EV", round(ws.cell(P["ev"], 5).value / 1e7, 1), "Y8 EV", round(ws.cell(P["ev"] + 1, 5).value / 1e7, 1), "| mismatches:", bad)
