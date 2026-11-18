"""Keepwell v2: evidence-based unit economics and solution variants (Phase 0d, steps 2 to 5).

    python3 ue_v2.py            -> prints the tables used in steps/00_unit_economics.md
    python3 ue_v2.py --json     -> writes research/ue_v2_results.json

Every input below carries a tag and a source key. Source keys point to:
  RA = research/retail_install/parameters.csv     RB = research/supply_layers/parameters.csv
  RC = research/competitors_funding/*.csv          AR = pitch/archive/market_intel/raw/demand/parameters.csv
  DOC = founders' rough reference (used only where nothing better exists; tagged ASSUMPTION)
Prices that compete with unregistered local mechanics are customer prices INCLUDING 18% GST (net = /1.18).
Brand rate-card installation fees are quoted "+ GST", so they are already net.
"""
import json, math, sys, copy, pathlib

HERE = pathlib.Path(__file__).parent
S = ("low", "base", "high")

# value tuples are (low, base, high); "low" = the pessimistic case for Keepwell
P = {
    # ---- retailer (RA)
    "units_month": ((30, 60, 120), "ASSUMPTION", "RA units_per_month_independent_target_shop"),
    "ac_share_units": ((0.25, 0.30, 0.35), "ASSUMPTION", "RA (AC 25-35% of dealer units)"),
    "other_install_share_units": ((0.20, 0.25, 0.30), "DERIVED", "RA install shares WM 90%, geyser 100%, TV 55% x mix"),
    "installed_base": ((2000, 3000, 5500), "DERIVED", "~4.5 yrs of sales x survival"),
    "oow_share": ((0.75, 0.80, 0.85), "DERIVED", "AR share_out_of_comprehensive_warranty"),
    "paid_events_per_unit_yr": ((0.30, 0.45, 0.63), "DERIVED", "AR incidence weighted by unit mix (AC 1.55, fridge .11, WM .17, RO 1.65)"),
    "repair_capture": ((0.06, 0.12, 0.20), "SOURCE-BACKED PROXY", "AR channel_share_dealer_arranged 10-15% of AC service"),
    "retailer_cac": ((30000, 18000, 12000), "ASSUMPTION", "RA cac_per_retailer UNKNOWN; DOC 18k"),
    "retailer_churn_yr": ((0.35, 0.20, 0.10), "ASSUMPTION", "DOC"),
    # ---- out-of-warranty repair/service job (AR, RB)
    "oow_ticket_incl_gst": ((800, 1000, 1300), "DERIVED", "AR bills: AC service 550, gas 2300, repair 1200-1500; mix"),
    "parts_share": ((0.30, 0.35, 0.45), "DERIVED", "RB parts_share_of_repair_bill (applied to blended ticket)"),
    "parts_margin": ((0.10, 0.20, 0.30), "ASSUMPTION", "RB parts_margin UNKNOWN; dealer margin 15-40% proxy"),
    "labour_payout_share": ((0.70, 0.60, 0.55), "SOURCE-BACKED PROXY", "RB UC partner ~71% of gross; agency 45-60%"),
    "comm_repair": ((0.10, 0.08, 0.06), "ASSUMPTION", "retailer referral commission"),
    "rework_share": ((0.06, 0.04, 0.03), "ASSUMPTION", "AR rework 5-15% of jobs x partial cost"),
    "tech_cost_job": ((5, 2.5, 1.5), "DERIVED", "RB tech_cost_per_job"),
    "insurance_job": ((4, 2.5, 2), "DERIVED", "RB insurance_cost_per_job"),
    "levy_share": ((0.02, 0.01, 0.0), "FACT", "RB gig levy TS 1-2%, AP none"),
    # ---- AC installation as brand-authorised partner (RA, RC)
    "auth_brand_coverage": ((0.30, 0.50, 0.65), "ASSUMPTION", "share of retailer's AC units from brands that authorise us"),
    "install_routing": ((0.50, 0.70, 0.85), "ASSUMPTION", "share of those installs the retailer routes to us"),
    "ac_install_net": ((700, 900, 1199), "SOURCE-BACKED PROXY", "RA LG/Lloyd 1199+GST; RC SERVIZ brand pays 1000 / centre gets 700"),
    "materials_sale": ((800, 1500, 2500), "SOURCE-BACKED PROXY", "RA copper 950-1100/m, bracket 750"),
    "materials_margin": ((0.15, 0.25, 0.35), "ASSUMPTION", "UNKNOWN; dealer-supplied materials hint"),
    "ac_install_payout": ((550, 450, 400), "ASSUMPTION", "technician pay per AC install"),
    "other_install_net": ((200, 300, 400), "SOURCE-BACKED PROXY", "RA geyser 250-350; WM/TV UNKNOWN"),
    "other_install_capture": ((0.20, 0.35, 0.50), "ASSUMPTION", ""),
    "other_install_payout": ((180, 200, 220), "ASSUMPTION", ""),
    "comm_install": ((0.08, 0.05, 0.03), "ASSUMPTION", "DOC 5%"),
    # ---- AMC (RB)
    "amc_price_incl_gst": ((1099, 1299, 1599), "SOURCE-BACKED PROXY", "RB UC AC plan 1098-1298; brand AMCs 1500-6000"),
    "amc_month": ((2, 4, 7), "DERIVED", "RB attach 2-10% of OOW units/yr x retailer-referred share"),
    "amc_visit_cost": ((450, 350, 300), "DERIVED", "RB amc_cost_per_visit 300-480"),
    "amc_visits": ((2, 2, 2), "FACT", "RB"),
    "comm_amc": ((0.15, 0.12, 0.10), "ASSUMPTION", "EW-like counter commission"),
    # ---- technician (RB)
    "jobs_day": ((2.2, 2.8, 3.5), "SOURCE-BACKED PROXY", "RB UC 1.7/day avg; partners claim 70-80/mo; DOC 3.8"),
    "days": ((25, 25, 26), "ASSUMPTION", ""),
    "util": ((0.60, 0.70, 0.80), "ASSUMPTION", "RB seasonality-driven"),
    "income_floor": ((24000, 22000, 20000), "DERIVED", "RB Tier2/3 mechanic earns 10-25k (base 20k); floor to recruit"),
    "season_peak": ((2.0, 1.8, 1.4), "DERIVED", "RB AC Mar-Jun index; techs sized for blended peak"),
    # ---- cluster & company (DOC, RC)
    "cluster_fixed": ((200000, 165000, 140000), "ASSUMPTION", "DOC 1.65L (manager, dispatch, training, office, onboarding)"),
    "retailers_target": ((25, 30, 40), "ASSUMPTION", ""),
    "retailer_fee_month": ((1500, 2500, 4000), "ASSUMPTION", "variant C only: after-sales desk subscription"),
    "retailer_fee_adoption": ((0.3, 0.6, 0.8), "ASSUMPTION", "variant C only"),
    "agency_fee_share": ((0.15, 0.20, 0.25), "SOURCE-BACKED PROXY", "RC SERVIZ 30% of brand fee; UC keeps ~25-36%"),
    "agency_cluster_fixed": ((120000, 95000, 80000), "ASSUMPTION", "variant D: manager + care, no training/tools"),
    "partner_payout_uplift": ((0.08, 0.05, 0.03), "ASSUMPTION", "variant E: extra payout share to keep per-job partners loyal (no income floor)"),
    "filler_jobs_cluster": ((0, 150, 300), "SOURCE-BACKED PROXY", "variant E: brand/e-com paid jobs in the trough via 247around/SERVIZ-type networks"),
    "filler_contrib": ((100, 150, 200), "SOURCE-BACKED PROXY", "RC SERVIZ keeps 300 of 1000; we keep ~150 after cost"),
}


def val(k, s):
    return P[k][0][S.index(s)]


def g(s):
    return {k: val(k, s) for k in P}


# ------------------------------------------------------------------ job economics
def oow_job(p):
    n = p["oow_ticket_incl_gst"] / 1.18
    parts = n * p["parts_share"]; labour = n - parts
    cost = parts * (1 - p["parts_margin"]) + labour * p["labour_payout_share"] + n * (p["comm_repair"] + p["rework_share"] + p["levy_share"]) + p["tech_cost_job"] + p["insurance_job"]
    return dict(price=p["oow_ticket_incl_gst"], net=round(n), contribution=round(n - cost), margin=round((n - cost) / n, 3), payout=round(labour * p["labour_payout_share"]))


def ac_install_job(p):
    n = p["ac_install_net"] + p["materials_sale"]
    cost = p["materials_sale"] * (1 - p["materials_margin"]) + p["ac_install_payout"] + p["ac_install_net"] * (p["comm_install"] + p["rework_share"] + p["levy_share"]) + p["tech_cost_job"] + p["insurance_job"]
    return dict(net=round(n), contribution=round(n - cost), margin=round((n - cost) / n, 3), payout=p["ac_install_payout"])


def other_install_job(p):
    n = p["other_install_net"]
    cost = p["other_install_payout"] + n * (p["comm_install"] + p["levy_share"]) + p["tech_cost_job"] + p["insurance_job"]
    return dict(net=round(n), contribution=round(n - cost), payout=p["other_install_payout"])


def amc_job(p):
    n = p["amc_price_incl_gst"] / 1.18
    cost = p["amc_visits"] * p["amc_visit_cost"] + n * (p["comm_amc"] + p["levy_share"]) + 50 + p["tech_cost_job"] * 2
    return dict(price=p["amc_price_incl_gst"], net=round(n), contribution=round(n - cost), margin=round((n - cost) / n, 3), payout=p["amc_visits"] * p["amc_visit_cost"])


# ------------------------------------------------------------------ variants: lines per retailer per month (steady state)
def lines(p, v):
    L = []
    if v == "E_HYBRID":
        p = dict(p); p["labour_payout_share"] = min(0.8, p["labour_payout_share"] + p["partner_payout_uplift"])
        p["ac_install_payout"] = p["ac_install_payout"] * (1 + p["partner_payout_uplift"]); p["amc_visit_cost"] *= (1 + p["partner_payout_uplift"])
    oow = p["installed_base"] * p["oow_share"] * p["paid_events_per_unit_yr"] / 12 * p["repair_capture"]
    if v in ("DOC_ON_EVIDENCE",):
        # founders' design priced on evidence: customer-paid installs by an UNAUTHORISED provider -> AC installs not contestable
        oi = p["units_month"] * p["other_install_share_units"] * p["other_install_capture"]
        L.append(("other installs", oi, other_install_job(p), 1))
        L.append(("OOW repair/service", oow, oow_job(p), 1))
        L.append(("AMC sold", p["amc_month"], amc_job(p), p["amc_visits"] / 12))
    if v in ("A_AUTHORISED", "C_DESK", "E_HYBRID"):
        ai = p["units_month"] * p["ac_share_units"] * p["auth_brand_coverage"] * p["install_routing"]
        oi = p["units_month"] * p["other_install_share_units"] * p["other_install_capture"]
        L.append(("AC installs (brand-authorised)", ai, ac_install_job(p), 1))
        L.append(("other installs", oi, other_install_job(p), 1))
        L.append(("OOW repair/service", oow, oow_job(p), 1))
        L.append(("AMC sold", p["amc_month"], amc_job(p), p["amc_visits"] / 12))
    if v in ("C_DESK", "E_HYBRID"):
        fee = p["retailer_fee_month"] * p["retailer_fee_adoption"]
        L.append(("retailer after-sales desk fee", 1, dict(net=round(fee), contribution=round(fee * 0.9)), 0))
    if v == "D_AGENCY":
        # asset-light: route retailer jobs to existing authorised centres / agencies, keep a fee on net value
        ai = p["units_month"] * p["ac_share_units"] * p["auth_brand_coverage"] * p["install_routing"]
        fee_inst = (p["ac_install_net"]) * p["agency_fee_share"] * 0.5      # ASC shares half our fee with retailer-led demand
        fee_oow = p["oow_ticket_incl_gst"] / 1.18 * p["agency_fee_share"]
        c_oow = fee_oow - p["oow_ticket_incl_gst"] / 1.18 * (p["comm_repair"] + 0.02) - p["tech_cost_job"]
        L.append(("AC installs routed to ASC", ai, dict(net=round(fee_inst), contribution=round(fee_inst - p["ac_install_net"] * p["comm_install"] - p["tech_cost_job"])), 0))
        L.append(("OOW jobs routed", oow, dict(net=round(fee_oow), contribution=round(c_oow)), 0))
        amc_fee = p["amc_price_incl_gst"] / 1.18 * (1 - p["comm_amc"]) - p["amc_visits"] * p["amc_visit_cost"] * 1.15
        L.append(("AMC sold (fulfilled by partner)", p["amc_month"], dict(net=round(p["amc_price_incl_gst"] / 1.18), contribution=round(amc_fee)), 0))
    return L


def retailer(p, v):
    L = lines(p, v)
    rev = sum(q * j["net"] for _, q, j, _ in L)
    con = sum(q * j["contribution"] for _, q, j, _ in L)
    visits = sum(q * f for _, q, j, f in L)
    payouts = sum(q * j.get("payout", 0) for _, q, j, f in L if f)
    return dict(lines=[(n, round(q, 2), j["net"], j["contribution"]) for n, q, j, _ in L], revenue=round(rev), contribution=round(con),
                visits=round(visits, 2), payouts=round(payouts))


def cluster(p, v, n=None):
    n = n or p["retailers_target"]
    r = retailer(p, v)
    fixed = p["agency_cluster_fixed"] if v == "D_AGENCY" else p["cluster_fixed"]
    cap = p["jobs_day"] * p["days"] * p["util"]
    visits = n * r["visits"]
    techs = math.ceil(visits * p["season_peak"] / (p["jobs_day"] * p["days"])) if visits else 0
    earned = (n * r["payouts"] / techs) if techs else 0
    topup = techs * max(0, p["income_floor"] - earned) if v not in ("D_AGENCY", "E_HYBRID") else 0
    filler = p["filler_jobs_cluster"] * p["filler_contrib"] if v == "E_HYBRID" else 0
    con = n * r["contribution"] - topup + filler
    per_ret = r["contribution"] - (topup / n if n else 0) + (filler / n if n else 0)
    be = fixed / per_ret if per_ret > 0 else None
    return dict(retailers=n, revenue=round(n * r["revenue"]), contribution=round(con), fixed=fixed, ebitda=round(con - fixed),
                technicians=techs, tech_income_avg=round(earned), income_topup=round(topup), visits_month=round(visits),
                breakeven_retailers=math.ceil(be) if be else None, contribution_per_retailer_net=round(per_ret),
                margin=round(con / (n * r["revenue"]), 3) if r["revenue"] else 0)


def returns(p, v):
    c = cluster(p, v)
    cpr = c["contribution_per_retailer_net"]
    if cpr <= 0:
        return dict(payback_months=None, ltv_3yr=0, ltv_cac=0)
    ramp = lambda m: min(1.0, 0.35 + 0.65 * (m - 1) / 11)
    cum, m = -p["retailer_cac"], 0
    while cum < 0 and m < 120:
        m += 1; cum += cpr * ramp(m) * (1 - p["retailer_churn_yr"] / 12) ** m
    ltv = sum(cpr * ramp(k) * (1 - p["retailer_churn_yr"] / 12) ** k for k in range(1, 37))
    return dict(payback_months=m if cum >= 0 else None, ltv_3yr=round(ltv), ltv_cac=round(ltv / p["retailer_cac"], 1))


VARIANTS = {
    "DOC_ON_EVIDENCE": "Founders' design re-priced on evidence (unauthorised: no in-warranty AC installs)",
    "A_AUTHORISED": "Brand-authorised installation partner + OOW repair + AMC, employed/contracted techs",
    "C_DESK": "A + retailer pays an after-sales desk subscription",
    "D_AGENCY": "Asset-light: route retailer demand to existing ASCs/agencies for a fee",
    "E_HYBRID": "C + certified partner technicians paid per job (no salary floor) + brand-paid filler jobs in the trough",
}

if __name__ == "__main__":
    out = {}
    print("JOB LEVEL")
    for s in S:
        p = g(s)
        print(f" {s:5} OOW {oow_job(p)} | AC install {ac_install_job(p)} | other install {other_install_job(p)} | AMC {amc_job(p)}")
    for v, d in VARIANTS.items():
        print(f"\n=== {v}: {d}")
        out[v] = {}
        for s in S:
            p = g(s); r = retailer(p, v); c = cluster(p, v); u = returns(p, v)
            out[v][s] = dict(retailer=r, cluster=c, returns=u, cluster_table=[cluster(p, v, n) for n in (15, 20, 25, 30, 40, 50)])
            print(f" {s:5} retailer/mo rev {r['revenue']:>7,} contrib {r['contribution']:>6,} visits {r['visits']} | cluster@{c['retailers']}: "
                  f"rev {c['revenue']:,} contrib {c['contribution']:,} EBITDA {c['ebitda']:,} techs {c['technicians']} income {c['tech_income_avg']:,} "
                  f"topup {c['income_topup']:,} BE {c['breakeven_retailers']} | payback {u['payback_months']} LTV:CAC {u['ltv_cac']}")
        print("   lines(base):", retailer(g('base'), v)["lines"])
    if "--json" in sys.argv:
        json.dump(dict(params={k: dict(zip(S, v[0]), tag=v[1], source=v[2]) for k, v in P.items()}, results=out),
                  open(HERE / "research/ue_v2_results.json", "w"), indent=1)


# ------------------------------------------------------------------ company (monthly) for capital need
HQ = [(6, 400000), (12, 550000), (24, 700000), (36, 900000), (60, 1200000)]  # ASSUMPTION: founders on lean pay, eng, finance, training lead


def company(s, v="E_HYBRID", months=24, opens=(1, 7, 13), setup=300000, wc=300000, ramp_m=12):
    p = g(s); r = retailer(p, v); c_full = cluster(p, v)
    tgt = p["retailers_target"]; cash = trough = 0; rows = []
    for m in range(1, months + 1):
        rev = con = fixed = cac = 0
        for om in [o for o in opens if o <= m]:
            age = m - om + 1
            if age == 1: cash -= setup
            if age <= 6: cash -= wc / 6
            n = min(tgt, 2 + (tgt - 2) * (age - 1) / (ramp_m - 1))
            n_prev = min(tgt, 2 + (tgt - 2) * (age - 2) / (ramp_m - 1)) if age > 1 else 0
            cac += (n - n_prev) * p["retailer_cac"]
            ramp = min(1.0, 0.35 + 0.65 * (max(1, age / 2) - 1) / 11)
            share = c_full["contribution"] / c_full["revenue"] if c_full["revenue"] else 0
            rv = n * r["revenue"] * ramp
            rev += rv; con += rv * share
            fixed += p["cluster_fixed"] if age > 1 else p["cluster_fixed"] * 0.6
        hq = next(x for lim, x in HQ if m <= lim)
        e = con - fixed - hq - cac; cash += e; trough = min(trough, cash)
        rows.append(dict(m=m, rev=rev, ebitda=e, cash=cash))
    y = lambda a, b, k: round(sum(x[k] for x in rows[a:b]))
    return dict(y1_rev=y(0, 12, "rev"), y2_rev=y(12, 24, "rev") if months >= 24 else None, y1_ebitda=y(0, 12, "ebitda"),
                y2_ebitda=y(12, 24, "ebitda") if months >= 24 else None, peak_need=round(-trough), run_rate_end=round(rows[-1]["rev"] * 12),
                retailers_end=len([o for o in opens if o <= months]) * tgt)


if __name__ == "__main__" and "--company" in sys.argv:
    for v in ("A_AUTHORISED", "E_HYBRID"):
        for s in S:
            print(v, s, company(s, v))
    print("E base, 5 clusters by m19:", company("base", "E_HYBRID", 24, (1, 5, 9, 14, 19)))


# ------------------------------------------------------------------ Gate-1 redesign: F = AC-first, B2B-paid, retailer as demand source (after red team)
FAIR = dict(auth_brand_coverage=0.35, install_routing=0.65, ac_install_net=800, materials_margin=0.20, ac_install_payout=500,
            amc_visit_cost=400, retailer_cac=22000, retailer_churn_yr=0.25)   # red-team "middle case" inputs, used as the honest BASE


def variant_F(s="base", leakage=0.10, plan_jobs=100, plan_contrib=150, trough_floor=15000, core_share=0.5, retailers=None):
    """AC-only: authorised/sub-contracted installs + OOW AC service/repair + AMC, no desk fee, no other installs.
    Plan-seller (Onsitego/Zopper-type) fulfilment jobs contracted per cluster; partner techs per job with a trough floor for a core half."""
    p = g(s)
    if s == "base": p.update(FAIR)
    p = dict(p)
    p["materials_sale"] = p["materials_sale"] / 1.18          # materials net of GST
    ai = p["units_month"] * p["ac_share_units"] * p["auth_brand_coverage"] * p["install_routing"]
    oow = p["installed_base"] * p["ac_share_units"] / 0.30 * p["oow_share"] * p["paid_events_per_unit_yr"] / 12 * p["repair_capture"] * (1 - leakage)
    amc = p["amc_month"] * (1 - leakage)
    L = [("AC installs", ai, ac_install_job(p)), ("OOW AC service/repair", oow, oow_job(p)), ("AMC sold", amc, amc_job(p))]
    rev = sum(q * j["net"] for _, q, j in L); con = sum(q * j["contribution"] for _, q, j in L)
    visits = ai + oow + amc * 2 / 12
    n = retailers or p["retailers_target"]
    techs = math.ceil(n * visits * p["season_peak"] / (p["jobs_day"] * p["days"]))
    payouts = n * (ai * p["ac_install_payout"] + oow * oow_job(p)["payout"] + amc * 2 / 12 * p["amc_visit_cost"])
    trough_earn = payouts / techs * 0.6 if techs else 0
    topup = math.ceil(techs * core_share) * max(0, trough_floor - trough_earn) * 5 / 12   # 5 trough months, averaged
    plan = plan_jobs * plan_contrib
    c_con = n * con - topup + plan
    per = c_con / n
    be = p["cluster_fixed"] / per if per > 0 else None
    return dict(case=s, lines=[(a, round(q, 1), j["net"], j["contribution"]) for a, q, j in L], retailer_rev=round(rev), retailer_contrib=round(con),
                cluster_retailers=n, cluster_contrib=round(c_con), cluster_ebitda=round(c_con - p["cluster_fixed"]), techs=techs,
                avg_tech_income=round(payouts / techs) if techs else 0, topup=round(topup), plan_contrib=plan,
                per_retailer_all_in=round(per), breakeven=math.ceil(be) if be else None)


if __name__ == "__main__" and "--F" in sys.argv:
    for s in S: print(variant_F(s))
    print("F base, no plan-seller contract:", variant_F("base", plan_jobs=0))
    print("F base, zero authorisation:", (lambda: (FAIR.__setitem__('auth_brand_coverage', 0.0), variant_F('base'), FAIR.__setitem__('auth_brand_coverage', 0.35))[1])())
    print("F base at 40 retailers:", variant_F("base", retailers=40))


# ------------------------------------------------------------------ Gate-1 follow-up: AC-only vs multi-appliance (same fair inputs)
# per-category job types: (events per out-of-warranty unit-yr, ticket incl GST, parts share, parts margin) -- AR incidence & bills, RB parts
CAT = {
    "AC":              dict(mix=0.30, oow=0.85, jobs=[(1.00, 550, 0.10, 0.20), (0.40, 2300, 0.45, 0.20), (0.15, 1500, 0.45, 0.20)],
                            install=("auth", None), amc=(1299, 2, 400), season=1.8),
    "Refrigerator":    dict(mix=0.25, oow=0.91, jobs=[(0.08, 1500, 0.50, 0.20), (0.03, 199, 0.0, 0.0)], install=None, amc=None, season=1.2),
    "Washing machine": dict(mix=0.15, oow=0.82, jobs=[(0.12, 1200, 0.45, 0.20), (0.05, 199, 0.0, 0.0)], install=("other", 300), amc=None, season=1.0),
    "Water purifier":  dict(mix=0.05, oow=0.80, jobs=[(1.50, 600, 0.50, 0.30), (0.15, 600, 0.40, 0.20)], install=None, amc=(2500, 3, 450), season=1.1),
    "Geyser":          dict(mix=0.05, oow=0.80, jobs=[(0.10, 800, 0.45, 0.20)], install=("other", 300), amc=None, season=0.7),
}


def variant_G(cats, units=80, s="base", leakage=0.10, amc_attach_yr=0.03, plan_jobs=100, plan_contrib=150,
              trough_floor=15000, core_share=0.5, retailers=30, years_base=4.5):
    p = g(s); p.update(FAIR); p["materials_sale"] = p["materials_sale"] / 1.18
    rev = con = visits = payouts = 0.0; peakw = 0.0; detail = {}
    for c in cats:
        d = CAT[c]; u = units * d["mix"]; base = u * 12 * years_base * 0.9
        r = k = v = pay = 0.0
        for ev, tk, ps, pm in d["jobs"]:
            q = base * d["oow"] * ev / 12 * p["repair_capture"] * (1 - leakage)
            pj = dict(p, oow_ticket_incl_gst=tk, parts_share=ps, parts_margin=pm); j = oow_job(pj)
            r += q * j["net"]; k += q * j["contribution"]; v += q; pay += q * j["payout"]
        if d["install"]:
            if d["install"][0] == "auth":
                q = u * p["auth_brand_coverage"] * p["install_routing"]; j = ac_install_job(p); pp = p["ac_install_payout"]
            else:
                q = u * 0.9 * p["other_install_capture"]; j = other_install_job(dict(p, other_install_net=d["install"][1])); pp = p["other_install_payout"]
            r += q * j["net"]; k += q * j["contribution"]; v += q; pay += q * pp
        if d["amc"]:
            price, vis, vc = d["amc"]; q = base * d["oow"] * amc_attach_yr / 12 * (1 - leakage)
            j = amc_job(dict(p, amc_price_incl_gst=price, amc_visits=vis, amc_visit_cost=vc))
            r += q * j["net"]; k += q * j["contribution"]; v += q * vis / 12 * 12 / 12; pay += q * vis * vc / 12 * 12 / 12
        detail[c] = dict(revenue=round(r), contribution=round(k), visits=round(v, 1))
        rev += r; con += k; visits += v; payouts += pay; peakw += v * d["season"]
    peak_idx = peakw / visits if visits else 1
    techs = math.ceil(retailers * visits * peak_idx / (p["jobs_day"] * p["days"]))
    trough_earn = retailers * payouts / techs * (2 - peak_idx) if techs else 0   # off-season month earnings
    topup = math.ceil(techs * core_share) * max(0, trough_floor - trough_earn) * 5 / 12
    c_con = retailers * con - topup + plan_jobs * plan_contrib
    per = c_con / retailers
    return dict(cats=cats, units=units, per_retailer_revenue=round(rev), per_retailer_contrib=round(con), visits=round(visits, 1),
                peak_index=round(peak_idx, 2), techs=techs, avg_tech_income=round(retailers * payouts / techs) if techs else 0, topup=round(topup),
                per_retailer_all_in=round(per), breakeven=math.ceil(p["cluster_fixed"] / per) if per > 0 else None,
                cluster_ebitda_30=round(c_con - p["cluster_fixed"]), detail=detail)


if __name__ == "__main__" and "--G" in sys.argv:
    ALL = ["AC", "Refrigerator", "Washing machine", "Water purifier", "Geyser"]
    for cats in (["AC"], ["AC", "Washing machine", "Refrigerator"], ["AC", "Water purifier"], ["AC", "Washing machine", "Refrigerator", "Water purifier"], ALL):
        for un in (60, 80, 100):
            r = variant_G(cats, un); r.pop("detail") if un != 80 else None
            print(r)
