"""Monthly cash profile from the annual plan_v3 output (seasonality overlay). Used by Step 8.
Contribution and Protect sales follow the AC-led season; people and fixed costs are flat; parts stock and working capital
build Feb-Apr; new clusters open half in January and half in July. Financing is added separately."""
import plan_v3 as V
SEASON = [0.06, 0.07, 0.10, 0.12, 0.13, 0.11, 0.08, 0.07, 0.07, 0.07, 0.06, 0.06]   # sums to 1.00
WC = [0.10, 0.25, 0.30, 0.20, 0.05, 0.0, 0.05, 0.05, 0.0, 0.0, 0.0, 0.0]               # growth WC build
CAPEX = [0.5, 0, 0, 0, 0, 0, 0.5, 0, 0, 0, 0, 0]
def months(s="base", lv=None, start_cash=None):
    rows, pk, u = V.run(s, lv)
    cash = rows[0]["cash_cum"] - (rows[0]["ebitda"] - rows[0]["tax"] - rows[0]["capex"] - rows[0]["dnwc"] + rows[0]["float_in"])  # opening
    if start_cash is not None: cash = start_cash
    out = []
    for r in rows:
        flat = r["cluster_fixed"] + r["hq"] + r["cac"] + r["fees"] + r["tax"]
        for mo in range(12):
            cf = r["contribution"] * SEASON[mo] - flat / 12 - r["dnwc"] * WC[mo] - r["capex"] * CAPEX[mo] + r["float_in"] * SEASON[mo]
            cash += cf; out.append(cash)
    return out
if __name__ == "__main__":
    for nm, s, d in (("BASE", "base", None), ("STRESS", "base", V.STRESS), ("LOW", "low", V.LOWX), ("STRESS hold3", "base", {**V.STRESS, "clusters_end": [3]*8}), ("LOW hold3", "low", {**V.LOWX, "clusters_end": [3]*8})):
        m = months(s, d)
        tro = min(range(len(m)), key=lambda i: m[i])
        print(f"{nm:13s} trough {m[tro]/1e7:6.2f} at month {tro+1} | m15 {m[14]/1e7:5.2f} m21 {m[20]/1e7:5.2f} m24 {m[23]/1e7:5.2f} m30 {m[29]/1e7:5.2f} m36 {m[35]/1e7:5.2f} m42 {m[41]/1e7:5.2f} m45 {m[44]/1e7:5.2f} m48 {m[47]/1e7:5.2f}")
