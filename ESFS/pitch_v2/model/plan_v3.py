"""Keepwell v3 plan: redesigned model on the plan_core engine (reviewer-corrected 20 Nov 2026).
Levers: (1) Keepwell Protect sold at the shop counter (repairs-only service contract), (2) commission moved from
repairs to Protect, (3) central parts buying, (4) partner clusters run by existing service-centre owners, (5) AI-lean HQ."""
import copy, plan_core as P

L = dict(
    protect_attach=0.08,      # share of covered-category units sold that take Protect (mature shop)
    covered_share=0.75,       # AC + fridge + WM + purifier share of units sold (CAT mix)
    attach_ramp=(0.4, 0.75, 1.0),  # by cluster age, on top of MAT (conservative double ramp)
    protect_price=2000,       # INR incl GST, avg 2-yr extension after brand warranty (derived market avg ~2,040)
    protect_comm=0.25,        # shop commission, paid and expensed at sale
    claims_ratio=0.35,        # repair claims at Keepwell's delivery cost, share of net price
    protect_admin=0.05,       # admin, processing, dispute handling
    reserve_share=1.0,        # share of expected claims on unearned plans held in a ring-fenced reserve
    comm_repair=0.03, comm_amc=0.08,
    parts_margin_mature=0.30, # central buying from cluster age 2
    repair_share_core=0.48,   # repairs as share of core revenue (from plan_core shop rows)
    partner_from=3,
    partner_fixed_m=100000,   # Keepwell cost per partner cluster/month: shop sales lead, QC audits, marketing
    partner_fee=0.10,         # of partner-cluster core revenue
    partner_open_floor=800000,# minimum fee guaranteed to a partner in its opening year
    partner_setup=150000,
    partner_cac=20000,        # shop CAC in partner clusters (mostly outside the warm AP/TS network)
    clusters_end=[3, 6, 11, 18, 28, 40, 55, 72],
    hq_scale=0.85,            # x Step 7 headcount path, then scaled with clusters (half fixed, half per cluster)
    shops_per_cluster=60,
)

def run(s="base", lv=None):
    lv = {**L, **(lv or {})}
    I0 = copy.deepcopy(P.I)
    def setv(k, val):
        t = list(P.I[k][0]); t[P.SC.index(s)] = val; P.I[k] = (tuple(t),) + P.I[k][1:]
    try:
        setv("comm_repair", lv["comm_repair"]); setv("comm_amc", lv["comm_amc"]); setv("shops_per_cluster", lv["shops_per_cluster"])
        _, rev0, con0 = P.shop(s)
        setv("parts_margin", lv["parts_margin_mature"]); _, rev1, con1 = P.shop(s)
        p = {k: P.v(k, s) for k in P.I}
    finally:
        P.I.clear(); P.I.update(I0)
    S = lv["shops_per_cluster"]; parts_gain = con1 - con0
    att_eff = lv["protect_attach"] * lv["covered_share"]
    units_yr = p["units_month"] * 12; net = lv["protect_price"] / 1.18
    plan_con_cl = p["plan_jobs_m"] * 12 * p["plan_contrib"]; plan_rev_cl = p["plan_jobs_m"] * 12 * p["plan_rev"]
    cl_fix = p["cluster_fixed_m"] * 12; k = p["layer_k"]
    cov_frac = att_eff * (2 / 4.5)            # share of the out-of-warranty repair base covered by Protect
    ends = [0, 0, 1] + lv["clusters_end"]; new = [0, 0, 1] + [ends[i + 3] - ends[i + 2] for i in range(8)]
    E = lambda t: ends[t + 2]; N = lambda t: new[t + 2]
    n_open = lambda oy: N(oy) if oy > 0 else 1
    own = lambda oy: oy < lv["partner_from"]; part = lambda oy: oy >= lv["partner_from"]
    out = []; cash = cash_nf = p["start_cash"]; trough = trough_nf = cash; pool = 0.0; prev_rev = 0.0
    sold = {}; U_prev = 0.0; R_prev = 0.0
    for t in range(1, 9):
        coh = [(oy, n_open(oy), t - oy) for oy in range(0, t + 1)]
        eqw = lambda f: sum(n * P.MAT[min(a, 3)] for oy, n, a in coh if f(oy))
        cnt = lambda f, c=lambda a: True: sum(n for oy, n, a in coh if f(oy) and c(a))
        eq = eqw(lambda oy: True); eq_own = eqw(own); eq_part = eqw(part)
        eq_parts = sum(n * P.MAT[min(a, 3)] for oy, n, a in coh if a >= 1)
        r = {"year": t, "clusters": E(t), "partner_clusters": cnt(part), "shops": E(t) * S, "eq": eq}
        core_gross = rev0 * S * eq
        lost_rev = core_gross * lv["repair_share_core"] * cov_frac          # covered repairs no longer billed
        r["Core service"] = core_gross - lost_rev
        r["Plan-seller fulfilment"] = plan_rev_cl * eq
        con = con0 * S * eq + parts_gain * S * eq_parts + plan_con_cl * eq - lost_rev * 0.17
        con -= p["floor_topup_y"] * eq_own
        fee = lv["partner_fee"] * rev0 * S * eq_part
        open_topup = sum(n * max(0.0, lv["partner_open_floor"] - lv["partner_fee"] * rev0 * S * P.MAT[0]) for oy, n, a in coh if part(oy) and a == 0)
        con -= fee + open_topup
        # Protect: sold at t, nothing delivered in t (brand warranty), recognised half in t+1 and half in t+2
        sold[t] = units_yr * S * att_eff * sum(n * P.MAT[min(a, 3)] * lv["attach_ramp"][min(a, 2)] for oy, n, a in coh)
        prot_rev = 0.5 * (sold.get(t - 1, 0) + sold.get(t - 2, 0)) * net
        r["Keepwell Protect"] = prot_rev
        con += prot_rev * (1 - lv["claims_ratio"] - lv["protect_admin"]) - sold[t] * net * lv["protect_comm"]
        U = (sold[t] + 0.5 * sold.get(t - 1, 0)) * net                    # unearned plan revenue
        Rz = U * lv["claims_ratio"] * lv["reserve_share"]                   # ring-fenced claims reserve
        float_in = (U - U_prev) - (Rz - R_prev); U_prev, R_prev = U, Rz
        data = 0.0
        for name, st, rv, cs, kind in P.LAYERS:
            val = rv * eq * P.LRAMP[min(t - st, 2)] * (k if kind == "data" else 1) if t >= st else 0.0
            r[name] = val; con += val * cs; data += val if kind == "data" else 0
        ent = P.ENTERPRISE[t - 1] * k; r["Brand data contracts"] = ent; con += ent * 0.75; data += ent
        keys = [x for x in r if x not in ("year", "clusters", "partner_clusters", "shops", "eq")]
        rev = sum(r[x] for x in keys); fees = rev * p["pay_fee"]
        fixed = cl_fix * (cnt(own, lambda a: a >= 1) + 0.5 * cnt(own, lambda a: a == 0)) \
              + lv["partner_fixed_m"] * 12 * (cnt(part, lambda a: a >= 1) + 0.5 * cnt(part, lambda a: a == 0))
        hq = P.HQ[t - 1] * lv["hq_scale"] * p["hq_mult"] * (0.5 + 0.5 * E(t) / P.CLUSTERS_END[t - 1])
        new_own = N(t) * S if own(t) else 0; new_part = N(t) * S if part(t) else 0
        cac = new_own * p["shop_cac"] + new_part * lv["partner_cac"] + E(t - 1) * S * p["shop_churn"] * p["shop_cac"]
        ebitda = con - fees - fixed - hq - cac
        nown = N(t) if own(t) else 0; npart = N(t) if part(t) else 0
        capex = nown * (p["setup"] + p["wc"] + (p["parts_stock"] if t >= 2 else 0)) + npart * (lv["partner_setup"] + p["wc"] + p["parts_stock"] * 0.5)
        dnwc = max(0.0, rev - prev_rev) * p["nwc_pct"]; prev_rev = rev
        dep = sum((N(oy) if own(oy) else 0) * p["setup"] / 3 + (N(oy) if part(oy) else 0) * lv["partner_setup"] / 3 for oy in range(max(1, t - 2), t + 1))
        taxable = ebitda - dep
        if taxable < 0: pool += -taxable; tax = 0.0
        else:
            use = min(pool, taxable); pool -= use; tax = (taxable - use) * p["tax_rate"]
        step = ebitda - tax - capex - dnwc
        cash += step + float_in; cash_nf += step; trough = min(trough, cash); trough_nf = min(trough_nf, cash_nf)
        r.update(revenue=rev, data_rev=data, contribution=con, fees=fees, cluster_fixed=fixed, hq=hq, cac=cac, ebitda=ebitda,
                 capex=capex, dnwc=dnwc, tax=tax, cash_cum=cash, cash_nofloat=cash_nf, protect_sold=sold[t], float_in=float_in,
                 unearned=U, reserve=Rz, partner_fee=fee + open_topup,
                 data_con=sum(r[n] * cs for n, st, rv, cs, kd in P.LAYERS if kd == "data") + ent * 0.75)
        out.append(r)
    # mature cluster economics (age 4+)
    plans = units_yr * att_eff
    prot_con_shop = plans * net * (1 - lv["claims_ratio"] - lv["protect_admin"] - lv["protect_comm"])
    lost = rev0 * lv["repair_share_core"] * cov_frac
    shop_con_m = con1 + prot_con_shop - lost * 0.17
    shop_rev_m = rev0 - lost + plans * net
    own_cl = dict(rev=shop_rev_m * S + plan_rev_cl, con=shop_con_m * S + plan_con_cl - p["floor_topup_y"], fix=cl_fix)
    part_cl = dict(rev=own_cl["rev"], con=shop_con_m * S + plan_con_cl - lv["partner_fee"] * rev0 * S, fix=lv["partner_fixed_m"] * 12)
    for c in (own_cl, part_cl): c["ebitda"] = c["con"] - c["fix"]; c["margin"] = c["ebitda"] / c["rev"]
    be = (cl_fix + p["floor_topup_y"] - plan_con_cl) / shop_con_m
    return out, dict(peak=-min(0, trough), peak_nofloat=-min(0, trough_nf)), dict(
        shop_rev=shop_rev_m, shop_con=shop_con_m, prot_con_shop=prot_con_shop, plans_shop=plans, own=own_cl, partner=part_cl,
        be_shops=be, core_rev_shop=rev0, core_con_shop=con1, partner_fee_mature=lv["partner_fee"] * rev0 * S)

STRESS = dict(protect_attach=0.05, claims_ratio=0.45, parts_margin_mature=0.25, shops_per_cluster=50, clusters_end=[3, 5, 9, 14, 21, 30, 40, 52])
LOWX = dict(protect_attach=0.05, claims_ratio=0.45, parts_margin_mature=0.25)

def show(s="base", lv=None, label=None):
    rows, pk, u = run(s, lv); o, pc = u["own"], u["partner"]
    print(f"== {label or s}: shop rev {u['shop_rev']/1e5:.2f}L con {u['shop_con']/1e3:.0f}k (Protect {u['prot_con_shop']/1e3:.0f}k, {u['plans_shop']:.0f} plans) | own cl rev {o['rev']/1e7:.2f}Cr EBITDA {o['ebitda']/1e5:.1f}L ({o['margin']:.1%}) | partner {pc['ebitda']/1e5:.1f}L ({pc['margin']:.1%}) | BE {u['be_shops']:.0f} | PEAK {pk['peak']/1e7:.1f}Cr (no float {pk['peak_nofloat']/1e7:.1f})")
    for r in rows:
        so = (r['ebitda'] - r['data_con']) / (r['revenue'] - r['data_rev'])
        print(f" Y{r['year']} cl {r['clusters']:>3} p{r['partner_clusters']:>2} shops {r['shops']:>5} rev {r['revenue']/1e7:6.1f} prot {r['Keepwell Protect']/1e7:4.1f} data {r['data_rev']/1e7:4.1f} hq {r['hq']/1e7:4.1f} EBITDA {r['ebitda']/1e7:5.1f} ({r['ebitda']/r['revenue']:6.1%}) svc-only {(r['ebitda']-r['data_con'])/1e7:5.1f} ({so:5.1%}) cash {r['cash_cum']/1e7:5.1f} nofloat {r['cash_nofloat']/1e7:5.1f} reserve {r['reserve']/1e7:4.1f}")
    return rows, pk, u

if __name__ == "__main__":
    show("base"); show("base", STRESS, "stress"); show("low", LOWX, "low")
