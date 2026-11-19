"""Keepwell round map, cap table and investor returns (Steps 8-9). Mirrors the Funding sheet in keepwell_model.xlsx."""
import plan_v3 as V
R = dict(
    isafe=0.45e7, isafe_cap_post=6.0e7, isafe_disc=0.20,
    seed=2.5e7, seed_pre=8.0e7, pool_post=0.10, t1=1.75e7, t2=0.75e7,   # tranche 2 at the month-9 gate (after the first AC season)
    r2=5.0e7, r2_pre=25.0e7,           # Round 2 (go-to-market), H2 2028
    r3=15.0e7, r3_pre=70.0e7,          # Round 3 (scaling), 2030
    split=(("Prathyusha (CEO)", 0.38), ("Kavyanth (COO)", 0.31), ("Sri Charan (CTO)", 0.31)),
    data_mult=7, op_mult=2.5,
)
def captable(r=R):
    post = r["seed_pre"] + r["seed"]
    seed = r["seed"] / post
    # post-money iSAFE: ownership = amount / post-money cap, on pre-money capitalisation (incl. pool)
    disc_price_pre = r["seed_pre"] * (1 - r["isafe_disc"])
    isafe_pre = max(r["isafe"] / r["isafe_cap_post"], r["isafe"] / disc_price_pre)
    pool_pre = r["pool_post"] / (1 - seed)
    f_pre = 1 - isafe_pre - pool_pre
    s = {"Founders": f_pre * (1 - seed), "Pre-seed iSAFE": isafe_pre * (1 - seed), "ESOP pool": pool_pre * (1 - seed), "Seed": seed}
    d2 = r["r2"] / (r["r2_pre"] + r["r2"]); d3 = r["r3"] / (r["r3_pre"] + r["r3"])
    a2 = {k: v * (1 - d2) for k, v in s.items()}; a2["Round 2 (GTM)"] = d2
    a3 = {k: v * (1 - d3) for k, v in a2.items()}; a3["Round 3 (Scaling)"] = d3
    return s, a2, a3, dict(seed_post=post, d2=d2, d3=d3, r2_post=r["r2_pre"] + r["r2"], r3_post=r["r3_pre"] + r["r3"])
def ev(row, r=R):
    return (row["revenue"] - row["data_rev"]) * r["op_mult"] + row["data_rev"] * r["data_mult"]
def returns(r=R):
    s, a2, a3, x = captable(r)
    out = {}
    for nm, sc, lv in (("BASE", "base", None), ("STRESS", "base", V.STRESS)):
        rows, pk, u = V.run(sc, lv)
        for yr in (5, 7, 8):
            e = ev(rows[yr - 1]); stake = a3["Seed"]; val = e * stake; mult = val / r["seed"]
            hold = yr - 0.5 + 0.5  # invested ~Feb 2027 (year 1 start); exit at end of year yr
            irr = mult ** (1 / hold) - 1
            out[(nm, yr)] = dict(ev=e, stake=stake, value=val, mult=mult, irr=irr)
    # VC method ceiling on seed post-money (5-yr exit, 35-40% IRR)
    vc = {}
    for nm in ("BASE", "STRESS"):
        e5 = out[(nm, 5)]["ev"]; ret = a3["Seed"] / s["Seed"]
        vc[nm] = {t: e5 * ret / ((1 + t) ** 5) for t in (0.35, 0.40)}
    return s, a2, a3, x, out, vc
if __name__ == "__main__":
    s, a2, a3, x, out, vc = returns()
    print("seed post", x["seed_post"] / 1e7, "d2", round(x["d2"], 4), "d3", round(x["d3"], 4))
    for nm, t in (("after seed", s), ("after R2", a2), ("after R3 / at exit", a3)):
        print(nm, {k: f"{v:.1%}" for k, v in t.items()})
    for k, v in R["split"]: print(" ", k, f"{s['Founders']*v:.1%} -> {a3['Founders']*v:.1%}")
    for k, v in out.items(): print(k, f"EV {v['ev']/1e7:.0f} Cr stake {v['stake']:.1%} value {v['value']/1e7:.1f} Cr {v['mult']:.1f}x IRR {v['irr']:.0%}")
    for k, v in vc.items(): print("VC-method max seed post", k, {t: round(p / 1e7, 1) for t, p in v.items()})
