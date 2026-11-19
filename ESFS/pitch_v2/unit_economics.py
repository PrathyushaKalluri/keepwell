"""Keepwell v2 unit-economics engine (Phase 0d).

    python3 unit_economics.py            -> prints every level for every parameter set and variant
    python3 unit_economics.py --json     -> also writes research/ue_results.json

Levels: job -> technician -> retailer -> cluster -> company (monthly simulation).
Parameter sets:
  DOC   = the founders' rough reference (pitch .md / figures PDF), reproduced only to check its logic.
  LOW/BASE/HIGH = evidence-based sets (filled from research/*/parameters.csv; see PARAM_SOURCES).
Solution variants are functions that transform a parameter set (Phase 0d step 5).
Standard library only.
"""
import json, math, sys, copy, pathlib

HERE = pathlib.Path(__file__).parent

# --------------------------------------------------------------------------- reference set (DOC)
DOC = dict(
    # job level
    install_fee=650, install_payout_share=0.72, install_consumables=30, install_other=0, install_ai_pay=8,
    repair_ticket=1150, repair_parts_price=700, repair_parts_cost=490, repair_labour_payout=300, repair_rework_share=0.03,
    repair_ai_pay=32, amc_price=1800, amc_visits=2, amc_visit_payout=300, amc_rework=100, amc_ai_pay=30, amc_other=300,
    comm_install=0.05, comm_repair=0.08, comm_amc=0.15,
    gst_on_price=0.0,                    # DOC prices are treated as net of GST
    # retailer level
    units_month=100, install_need=0.55, install_capture=0.45, installed_base=5000, events_per_unit=0.30,
    oow_share=0.75, repair_capture=0.15, amc_month=5, ramp_start=0.35, ramp_months=12,
    retailer_cac=18000, retailer_churn_year=0.20,
    # technician
    tech_jobs_day=3.8, tech_days=25, tech_util=0.80,
    # cluster
    cluster_fixed=165000, cluster_setup=300000, cluster_wc=300000, retailers_target=25, retailers_ramp_months=9,
    retailers_at_open=2, seasonality_amp=0.0,
    # company
    hq_month=[(6, 350000), (12, 500000), (24, 650000), (60, 900000)], cluster_open_months=[1, 7, 13],
    parts_wholesale_month=0, parts_wholesale_margin=0.14,
)


# --------------------------------------------------------------------------- level 1: job
def job_economics(p):
    inst_rev = p["install_fee"]
    inst_cost = inst_rev * p["install_payout_share"] + p["install_consumables"] + inst_rev * p["comm_install"] + p["install_ai_pay"] + p["install_other"]
    rep_rev = p["repair_ticket"]
    rep_cost = (p["repair_labour_payout"] + p["repair_parts_cost"] + rep_rev * p["comm_repair"] + rep_rev * p["repair_rework_share"] + p["repair_ai_pay"])
    amc_rev = p["amc_price"]
    amc_cost = p["amc_visits"] * p["amc_visit_payout"] + amc_rev * p["comm_amc"] + p["amc_rework"] + p["amc_ai_pay"] + p["amc_other"]
    out = {}
    for k, r, c in (("install", inst_rev, inst_cost), ("repair", rep_rev, rep_cost), ("amc", amc_rev, amc_cost)):
        out[k] = dict(revenue=round(r), direct_cost=round(c), contribution=round(r - c), margin=round((r - c) / r, 3) if r else 0)
    return out


# --------------------------------------------------------------------------- level 2: retailer (steady state, per month)
def retailer_month(p, ramp=1.0):
    j = job_economics(p)
    installs = p["units_month"] * p["install_need"] * p["install_capture"] * ramp
    repairs = p["installed_base"] * p["events_per_unit"] / 12 * p["oow_share"] * p["repair_capture"] * ramp
    amcs = p["amc_month"] * ramp
    rev = installs * j["install"]["revenue"] + repairs * j["repair"]["revenue"] + amcs * j["amc"]["revenue"]
    con = installs * j["install"]["contribution"] + repairs * j["repair"]["contribution"] + amcs * j["amc"]["contribution"]
    field_jobs = installs + repairs + amcs * p["amc_visits"] / 12 * 12 / 12  # AMC visits spread over the year (2 visits/plan/yr)
    retailer_comm = (installs * j["install"]["revenue"] * p["comm_install"] + repairs * j["repair"]["revenue"] * p["comm_repair"]
                     + amcs * j["amc"]["revenue"] * p["comm_amc"])
    return dict(installs=installs, repairs=repairs, amcs=amcs, field_jobs=field_jobs, revenue=rev, contribution=con,
                retailer_commission=retailer_comm)


# --------------------------------------------------------------------------- level 3: technician
def technician(p):
    jobs = p["tech_jobs_day"] * p["tech_days"] * p["tech_util"]
    j = job_economics(p)
    pay_inst = p["install_fee"] * p["install_payout_share"]
    pay_rep = p["repair_labour_payout"]
    rm = retailer_month(p)
    mix_inst = rm["installs"] / max(rm["installs"] + rm["repairs"], 1e-9)
    avg_pay = mix_inst * pay_inst + (1 - mix_inst) * pay_rep
    return dict(jobs_month=round(jobs, 1), avg_payout=round(avg_pay), income_month=round(jobs * avg_pay))


# --------------------------------------------------------------------------- level 4: cluster
def cluster(p, n_retailers=None):
    rm = retailer_month(p)
    n = n_retailers or p["retailers_target"]
    con = n * rm["contribution"]
    be = p["cluster_fixed"] / rm["contribution"] if rm["contribution"] > 0 else float("inf")
    jobs_day = n * (rm["installs"] + rm["repairs"] + rm["amcs"] * p["amc_visits"] / 12) / 26
    techs = math.ceil(n * (rm["installs"] + rm["repairs"] + rm["amcs"] * p["amc_visits"] / 12) / (p["tech_jobs_day"] * p["tech_days"] * p["tech_util"]))
    return dict(retailers=n, contribution=round(con), fixed=p["cluster_fixed"], ebitda=round(con - p["cluster_fixed"]),
                breakeven_retailers=math.ceil(be) if be != float("inf") else None, breakeven_exact=round(be, 2) if be != float("inf") else None,
                jobs_day=round(jobs_day, 1), technicians=techs)


def unit_returns(p):
    rm = retailer_month(p)
    payback_ss = p["retailer_cac"] / rm["contribution"] if rm["contribution"] > 0 else None
    # ramped payback
    cum, m = -p["retailer_cac"], 0
    while cum < 0 and m < 120:
        m += 1
        ramp = min(1.0, p["ramp_start"] + (1 - p["ramp_start"]) * (m - 1) / max(p["ramp_months"] - 1, 1))
        cum += retailer_month(p, ramp)["contribution"] * (1 - p["retailer_churn_year"] / 12) ** m
    life_m = 12 / p["retailer_churn_year"] if p["retailer_churn_year"] else 120
    ltv3 = sum(retailer_month(p, min(1.0, p["ramp_start"] + (1 - p["ramp_start"]) * (k - 1) / max(p["ramp_months"] - 1, 1)))["contribution"]
               * (1 - p["retailer_churn_year"] / 12) ** k for k in range(1, 37))
    return dict(payback_steady_months=round(payback_ss, 1) if payback_ss else None, payback_ramped_months=m if cum >= 0 else None,
                expected_life_months=round(life_m), ltv_3yr=round(ltv3), ltv_cac_3yr=round(ltv3 / p["retailer_cac"], 1))


# --------------------------------------------------------------------------- level 5: company (monthly)
def company(p, months=24):
    rows, cash, trough = [], 0.0, 0.0
    clusters = []  # list of open month
    for m in range(1, months + 1):
        if m in p["cluster_open_months"]:
            clusters.append(m)
            cash -= p["cluster_setup"]
        rev = con = fixed = 0.0
        retailers = 0
        for om in clusters:
            age = m - om + 1
            n = min(p["retailers_target"], p["retailers_at_open"] + (p["retailers_target"] - p["retailers_at_open"]) * (age - 1) / max(p["retailers_ramp_months"] - 1, 1))
            # cohort ramp approximated by average retailer age
            avg_age = max(1, age / 2)
            ramp = min(1.0, p["ramp_start"] + (1 - p["ramp_start"]) * (avg_age - 1) / max(p["ramp_months"] - 1, 1))
            season = 1 + p["seasonality_amp"] * math.cos(2 * math.pi * ((m + 9) % 12 - 4) / 12)  # peak ~May
            rm = retailer_month(p, ramp * season)
            rev += n * rm["revenue"]; con += n * rm["contribution"]
            fixed += p["cluster_fixed"] if age > 1 else p["cluster_fixed"] * 0.55
            retailers += n
            if age <= 6:
                cash -= p["cluster_wc"] / 6
            if age >= 9 and p["parts_wholesale_month"]:
                rev += p["parts_wholesale_month"]; con += p["parts_wholesale_month"] * p["parts_wholesale_margin"]
        new_ret = sum(1 for om in clusters if 1 <= m - om + 1 <= p["retailers_ramp_months"]) * (p["retailers_target"] - p["retailers_at_open"]) / p["retailers_ramp_months"]
        cac = new_ret * p["retailer_cac"]
        hq = next(v for lim, v in p["hq_month"] if m <= lim)
        ebitda = con - fixed - hq - cac
        cash += ebitda
        trough = min(trough, cash)
        rows.append(dict(month=m, clusters=len(clusters), retailers=round(retailers), revenue=round(rev), contribution=round(con),
                         cluster_fixed=round(fixed), hq=hq, cac=round(cac), ebitda=round(ebitda), cash=round(cash)))
    y = lambda a, b, k: sum(r[k] for r in rows[a:b])
    summ = dict(y1_revenue=round(y(0, 12, "revenue")), y2_revenue=round(y(12, 24, "revenue")) if months >= 24 else None,
                y1_ebitda=round(y(0, 12, "ebitda")), y2_ebitda=round(y(12, 24, "ebitda")) if months >= 24 else None,
                peak_funding_need=round(-trough), retailers_end=rows[-1]["retailers"], run_rate_end=rows[-1]["revenue"] * 12)
    return rows, summ


def full(p, label):
    return dict(label=label, job=job_economics(p), retailer={k: round(v, 2) for k, v in retailer_month(p).items()},
                technician=technician(p), cluster=cluster(p), returns=unit_returns(p),
                cluster_table=[cluster(p, n) for n in (15, 21, 22, 25, 35, 40)], company=company(p)[1])


def fmt(r):
    j = r["job"]; rm = r["retailer"]; c = r["cluster"]; u = r["returns"]; co = r["company"]
    L = [f"\n=== {r['label']}",
         "job: " + " | ".join(f"{k} rev {v['revenue']} contrib {v['contribution']} ({v['margin']:.0%})" for k, v in j.items()),
         f"retailer/month: installs {rm['installs']:.1f}, repairs {rm['repairs']:.1f}, AMC {rm['amcs']:.1f} -> revenue {rm['revenue']:,.0f}, contribution {rm['contribution']:,.0f}, retailer earns {rm['retailer_commission']:,.0f}",
         f"technician: {r['technician']}",
         f"cluster@{c['retailers']}: contribution {c['contribution']:,} - fixed {c['fixed']:,} = {c['ebitda']:,}; breakeven {c['breakeven_exact']} -> {c['breakeven_retailers']} retailers; {c['jobs_day']} jobs/day; {c['technicians']} techs",
         f"returns: {u}",
         f"company 24m: {co}"]
    return "\n".join(L)


if __name__ == "__main__":
    res = [full(DOC, "DOC reference (founders' rough model, reproduced)")]
    fixed = copy.deepcopy(DOC)
    print("\n".join(fmt(r) for r in res))
    if "--json" in sys.argv:
        (HERE / "research").mkdir(exist_ok=True)
        json.dump(res, open(HERE / "research/ue_results.json", "w"), indent=1)
