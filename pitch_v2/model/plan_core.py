"""Keepwell v2 Step 7 plan engine (Python mirror of keepwell_model.xlsx). Pilot actuals = BASE."""
SC = ("low", "base", "high")
I = {  # name: ((low, base, high), unit, tag, source)
 "units_month": ((60, 74, 90), "units/shop/month", "Story/R", "Step 6 pilot ledgers; R 30/60/120"),
 "auth_cov": ((0.30, 0.41, 0.50), "share of AC units", "Story", "Step 6 pilot"),
 "routing": ((0.50, 0.58, 0.70), "share", "Story", "Step 6 pilot"),
 "capture": ((0.08, 0.11, 0.15), "share of OOW events", "Story/R", "Step 6; R dealer-arranged 10-15%"),
 "leakage": ((0.15, 0.09, 0.05), "share", "Story", "Step 6 audit"),
 "amc_attach": ((0.02, 0.034, 0.05), "share of OOW base/yr", "Story/R", "Step 6; R 2-10%"),
 "years_base": ((4.5, 4.5, 4.5), "years of sales in active base", "Assumption", "Step 4"),
 "ac_install_net": ((700, 800, 900), "INR/install", "Story/R", "Step 6 sub-contract; R SERVIZ proxy"),
 "materials_net": ((1100, 1271, 1500), "INR/install net of GST", "R", "LG/Lloyd rate cards"),
 "materials_margin": ((0.15, 0.20, 0.25), "share", "Assumption", "UNKNOWN in R; pilot invoices"),
 "ac_install_payout": ((550, 500, 450), "INR/install", "Story", "Step 3"),
 "wm_install_net": ((250, 300, 350), "INR/install", "R", "RA"),
 "wm_install_payout": ((220, 200, 180), "INR", "Assumption", ""),
 "other_install_capture": ((0.25, 0.35, 0.45), "share", "Assumption", ""),
 "labour_payout": ((0.65, 0.60, 0.55), "share of labour", "R", "UC ~71%; agency 45-60%"),
 "parts_margin": ((0.15, 0.20, 0.30), "share", "Assumption", "R dealer 15-40%"),
 "comm_install": ((0.05, 0.05, 0.05), "share", "Story", "Step 6"),
 "comm_repair": ((0.08, 0.08, 0.08), "share", "Story", "Step 6"),
 "comm_amc": ((0.12, 0.12, 0.12), "share", "Story", "Step 6"),
 "rework": ((0.05, 0.04, 0.03), "share of net", "Story/R", "callbacks 6.5%"),
 "levy": ((0.02, 0.014, 0.01), "share of net", "R", "central Code ~1% + TS Act 21 1-2% on TS share of clusters"),
 "tech_cost": ((5, 2.5, 1.5), "INR/job", "R", "RB"),
 "insurance": ((4, 2.5, 2), "INR/job", "R", "RB"),
 "amc_visit_ac": ((450, 400, 350), "INR/visit", "R", "RB 300-480"),
 "amc_visit_ro": ((500, 450, 400), "INR/visit", "Assumption", ""),
 "shops_per_cluster": ((40, 50, 60), "shops", "Model", "00c density"),
 "cluster_fixed_m": ((210000, 190000, 170000), "INR/month", "Model", "00c mature team"),
 "floor_topup_y": ((600000, 450000, 250000), "INR/cluster/yr", "Model", "Step 6 pilot topup scaled"),
 "plan_jobs_m": ((60, 100, 150), "jobs/cluster/month", "Story", "Step 6 contract from Jan 2027"),
 "plan_contrib": ((120, 150, 200), "INR/job", "R", "SERVIZ proxy"),
 "plan_rev": ((600, 700, 800), "INR/job revenue", "R", "SERVIZ: brand pays 1000, centre keeps 700"),
 "shop_cac": ((18000, 14000, 9500), "INR/shop blended", "Story/Assumption", "warm 9.5k (pilot, AP/TS network) / cold 22k (R) / self-serve ~6k"),
 "shop_churn": ((0.20, 0.10, 0.06), "share of shops/yr replaced", "Assumption", "Step 6 retention gate 85%"),
 "pay_fee": ((0.010, 0.008, 0.005), "share of revenue", "R", "UPI 0% MDR; cards/gateway ~2%; blend"),
 "nwc_pct": ((0.10, 0.07, 0.05), "share of revenue growth", "Assumption", "B2B receivables, parts and refurbished stock, less AMC advances"),
 "tax_rate": ((0.25, 0.25, 0.25), "share of taxable profit", "R", "domestic company rate ~25%"),
 "start_cash": ((1800000, 1800000, 1800000), "INR", "Story", "Step 2 cash Nov 2026"),
 "hq_mult": ((1.2, 1.0, 0.85), "x HQ headcount path", "Assumption", "HQ built by headcount (Step 7 §7.4)"),
 "setup": ((350000, 300000, 250000), "INR/new cluster", "Assumption", "Step 2"),
 "wc": ((350000, 300000, 250000), "INR/new cluster", "Assumption", ""),
 "parts_stock": ((1000000, 1000000, 800000), "INR/new cluster from Y2", "R", "physical layers"),
 "layer_k": ((0.6, 1.0, 1.3), "x data-layer adoption", "Assumption", "00b"),
}
CAT = [  # category, mix, oow, [(events, ticket_incl_gst, parts_share, parts_margin_override or None, basis)], amc(price, visits, visit_key)
 ("AC", 0.30, 0.85, [(1.00, 550, 0.10, None, "inuse"), (0.40, 2300, 0.45, None, "oow"), (0.15, 1500, 0.45, None, "oow")], (1299, 2, "amc_visit_ac")),
 ("Refrigerator", 0.25, 0.91, [(0.08, 1500, 0.50, None, "oow"), (0.03, 199, 0.0, None, "inuse")], None),
 ("Washing machine", 0.15, 0.82, [(0.12, 1200, 0.45, None, "oow"), (0.05, 199, 0.0, None, "inuse")], None),
 ("Water purifier", 0.05, 0.80, [(1.50, 600, 0.50, 0.30, "inuse"), (0.15, 600, 0.40, None, "oow")], (2500, 3, "amc_visit_ro")),
]
CLUSTERS_END = [3, 5, 9, 14, 21, 30, 40, 52]
HQ = [1.0e7, 1.6e7, 2.6e7, 4.0e7, 6.0e7, 8.0e7, 10.5e7, 13.0e7]  # headcount build: founders+eng+finance -> regional leads, data team, compliance
LAYERS = [  # name, start_year, rev per mature cluster/yr, contribution share, kind
 ("Parts to other agencies (excl. own jobs)", 2, 2.0e6, 0.10, "ops"),
 ("Trade-in field arm", 2, 1.8e6, 0.57, "ops"),
 ("Install & claims verification", 3, 0.9e6, 0.80, "data"),
 ("Replacement leads & AMC renewals", 4, 0.67e6, 0.70, "data"),
 ("Refurbished appliances (avg over clusters; about half run it)", 5, 3.0e6, 0.12, "ops"),
 ("E-waste feeder to recyclers", 3, 0.25e6, 0.50, "ops"),
]
ENTERPRISE = [0, 0, 0, 0, 1.5e7, 3.0e7, 5.0e7, 8.0e7]
MAT = (0.25, 0.60, 0.90, 1.0)   # cluster maturity by age (opening yr, 2nd, 3rd, 4th+): shops sign and ramp over ~3 years
LRAMP = (0.4, 0.7, 1.0)  # layer ramp by layer age


def v(k, s): return I[k][0][SC.index(s)]


def shop(s):
    p = {k: v(k, s) for k in I}
    u = p["units_month"]; rows = []
    for cat, mix, oow, jobs, amc in CAT:
        base = u * mix * 12 * p["years_base"] * 0.9
        for ev, tk, ps, pm, basis in jobs:
            n = base * (oow if basis == "oow" else 1) * ev * p["capture"] * (1 - p["leakage"])
            net = tk / 1.18; parts = net * ps; lab = net - parts
            pmg = pm if pm is not None else p["parts_margin"]
            c = net - parts * (1 - pmg) - lab * p["labour_payout"] - net * (p["comm_repair"] + p["rework"] + p["levy"]) - p["tech_cost"] - p["insurance"]
            rows.append((f"{cat} service/repair", n, net, c))
        if amc:
            price, vis, vk = amc; n = base * oow * p["amc_attach"] * (1 - p["leakage"]); net = price / 1.18
            c = net - vis * p[vk] - net * (p["comm_amc"] + p["levy"]) - 50 - 2 * p["tech_cost"]
            rows.append((f"{cat} AMC", n, net, c))
    n = u * 0.30 * 12 * p["auth_cov"] * p["routing"]; net = p["ac_install_net"] + p["materials_net"]
    c = net - p["materials_net"] * (1 - p["materials_margin"]) - p["ac_install_payout"] - p["ac_install_net"] * (p["comm_install"] + p["rework"] + p["levy"]) - p["tech_cost"] - p["insurance"]
    rows.append(("AC install (authorised)", n, net, c))
    n = u * 0.15 * 12 * 0.9 * p["other_install_capture"]; net = p["wm_install_net"]
    c = net - p["wm_install_payout"] - net * (p["comm_install"] + p["levy"]) - p["tech_cost"] - p["insurance"]
    rows.append(("WM install", n, net, c))
    return rows, sum(r[1] * r[2] for r in rows), sum(r[1] * r[3] for r in rows)


def plan(s):
    p = {k: v(k, s) for k in I}
    _, shop_rev, shop_con = shop(s)
    S = p["shops_per_cluster"]
    plan_rev_cl = p["plan_jobs_m"] * 12 * p["plan_rev"]
    cl_rev = shop_rev * S + plan_rev_cl
    cl_con = shop_con * S - p["floor_topup_y"] + p["plan_jobs_m"] * 12 * p["plan_contrib"]
    cl_fix = p["cluster_fixed_m"] * 12
    ends = [0, 0, 1] + CLUSTERS_END            # index t+2 = end of year t (year 0 = pilot)
    new = [0, 0, 1] + [ends[i + 3] - ends[i + 2] for i in range(8)]
    E = lambda t: ends[t + 2]; N = lambda t: new[t + 2]
    out = []; cash = p["start_cash"]; trough = cash; loss_pool = 0.0; prev_rev = 0.0
    for t in range(1, 9):
        eq = N(t) * MAT[0] + N(t - 1) * MAT[1] + N(t - 2) * MAT[2] + E(t - 3) * MAT[3]
        r = {"year": t, "clusters": E(t), "shops": E(t) * S, "eq": eq}
        r["Core service"] = shop_rev * S * eq; r["Plan-seller fulfilment"] = plan_rev_cl * eq
        con = cl_con * eq; data = 0.0; core_con = con
        for name, st, rv, cs, kind in LAYERS:
            if t >= st:
                f = LRAMP[min(t - st, 2)] * (p["layer_k"] if kind == "data" else 1)
                val = rv * eq * f
            else:
                val = 0.0
            r[name] = val; con += val * cs; data += val if kind == "data" else 0
        ent = ENTERPRISE[t - 1] * p["layer_k"]; r["Brand data contracts"] = ent; con += ent * 0.75; data += ent
        keys = [k for k in r if k not in ("year", "clusters", "shops", "eq")]
        rev = sum(r[k] for k in keys)
        fees = rev * p["pay_fee"]
        fixed = cl_fix * (E(t - 1) + 0.5 * N(t))
        hq = HQ[t - 1] * p["hq_mult"]
        new_shops = (E(t) - E(t - 1)) * S; churn_shops = E(t - 1) * S * p["shop_churn"]
        cac = (new_shops + churn_shops) * p["shop_cac"]
        ebitda = con - fees - fixed - hq - cac
        core_ebitda = core_con - rev * 0 - fees * (r["Core service"] + r["Plan-seller fulfilment"]) / rev - fixed - hq - cac
        capex = N(t) * (p["setup"] + p["wc"] + (p["parts_stock"] if t >= 2 else 0))
        dnwc = max(0.0, rev - prev_rev) * p["nwc_pct"]; prev_rev = rev
        taxable = ebitda - N(t) * p["setup"] / 3          # rough depreciation of setup
        if taxable < 0: loss_pool += -taxable; tax = 0.0
        else:
            use = min(loss_pool, taxable); loss_pool -= use; tax = (taxable - use) * p["tax_rate"]
        cash += ebitda - tax - capex - dnwc; trough = min(trough, cash)
        r.update(revenue=rev, data_rev=data, contribution=con, fees=fees, cluster_fixed=fixed, hq=hq, cac=cac, ebitda=ebitda,
                 core_ebitda=core_ebitda, capex=capex, dnwc=dnwc, tax=tax, cash_cum=cash)
        out.append(r)
    be = (cl_fix + p["floor_topup_y"] - p["plan_jobs_m"] * 12 * p["plan_contrib"]) / shop_con
    return out, -min(0, trough), dict(shop_rev=shop_rev, shop_con=shop_con, cl_rev=cl_rev, cl_con=cl_con, cl_fix=cl_fix,
                                      cl_ebitda=cl_con - cl_fix, be_shops=be)


if __name__ == "__main__":
    for s in SC:
        rows, peak, u = plan(s)
        print(f"\n== {s}: shop rev {u['shop_rev']/1e5:.2f}L con {u['shop_con']/1e5:.2f}L | cluster rev {u['cl_rev']/1e7:.2f}Cr con {u['cl_con']/1e5:.1f}L fixed {u['cl_fix']/1e5:.1f}L EBITDA {u['cl_ebitda']/1e5:.1f}L | BE shops {u['be_shops']:.0f} | peak need {peak/1e7:.1f} Cr")
        for r in rows:
            print(f"Y{r['year']} cl {r['clusters']:>3} shops {r['shops']:>5} rev {r['revenue']/1e7:6.1f} data {r['data_rev']/1e7:4.1f} contrib {r['contribution']/r['revenue']:.0%} EBITDA {r['ebitda']/1e7:6.1f} ({r['ebitda']/r['revenue']:.0%}) coreEBITDA {r['core_ebitda']/1e7:6.1f} tax {r['tax']/1e7:4.1f} cash {r['cash_cum']/1e7:6.1f}")
