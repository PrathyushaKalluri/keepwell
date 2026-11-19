"""Keepwell simple model (v4, final). One engine for the pilot, the unit economics, the 5-year plan, the ask and the returns.
Everything is driven by one unit: the active retailer. Python mirror of keepwell_model.xlsx (build_model_v4.py)."""
CR, L = 1e7, 1e5
P = dict(  # ---- pilot, Vijayawada–Guntur, Mar–Oct 2026
    months=["Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct"],
    active=[12, 15, 20, 24, 28, 30, 32, 34],
    rev_per_retailer_month=19_500,   # ₹ net of GST, per active retailer per month (pilot)
    contrib_margin=0.26,             # after technician pay, parts cost, retailer commission, per-job costs
    cluster_team_month=1.0 * L,      # pilot cluster team: coordinator, dispatcher, field executive
    avg_job=1_580,                   # ₹ net per job (installs, service, repair, AMC, Protect)
)
U = dict(  # ---- one mature retailer and one mature cluster (2031)
    rev_per_retailer_month=30_000, contrib_margin=0.32, retailers_per_cluster=60, cluster_cost_year=0.18 * CR,
)
Y = dict(  # ---- 5-year plan, year 1 = Apr 2027–Mar 2028 (from the close)
    years=["Y1", "Y2", "Y3", "Y4", "Y5"], cal=["2027", "2028", "2029", "2030", "2031"],
    retailers_end=[200, 500, 1000, 1800, 3000], clusters_end=[4, 9, 18, 30, 50],
    rev_per_retailer_year=[3.0 * L, 3.2 * L, 3.4 * L, 3.5 * L, 3.6 * L],   # rises as Protect, AMC renewals and parts build
    contrib_margin=[0.28, 0.29, 0.30, 0.31, 0.32],
    cluster_cost_year=0.18 * CR, hq=[0.40 * CR, 0.8 * CR, 1.5 * CR, 2.5 * CR, 3.5 * CR],
    launch_per_cluster=0.20 * CR,    # set-up, parts stock, onboarding and training for a new cluster
    wc_share=0.10,                   # working capital: 10% of each year's revenue increase
    tax=0.25, start_retailers=34, start_clusters=1, start_cash=0.02 * CR, pilot_rev_run=34 * 19_500 * 12,
)
# ---- one retailer's month, opened up (slide 6). Sources: technicians ₹330–500 a job and retailer commission ≈ ₹1.7k a month (Step 6).
SPLIT = dict(technicians=4_900, parts=6_400, retailer_commission=1_700, other_per_job=1_430)   # pilot, per active retailer per month
LIFT = dict(protect=4_000, amc_renewals=2_600, installed_base_repairs=3_900)                   # added per retailer per month by year 5
LIFT_NOTES = dict(protect="2 plans a month × ₹2,000 (about 4% of the ~55 covered appliances a retailer sells; the pilot test reached 6%)",
                  amc_renewals="2 renewals a month × ₹1,299", installed_base_repairs="about 1.5 more repairs a month on appliances Keepwell installed")
MATURE_TEAM_MONTH = 1.5 * L   # a 60-retailer cluster adds a second field executive and a parts desk (= ₹18 L a year)

def retailer_month():
    rev = P["rev_per_retailer_month"]; cost = sum(SPLIT.values()); con = rev - cost
    assert abs(con - rev * P["contrib_margin"]) < 1, con
    mrev = rev + sum(LIFT.values()); assert mrev == U["rev_per_retailer_month"], mrev
    assert abs(MATURE_TEAM_MONTH * 12 - U["cluster_cost_year"]) < 1
    mcon = mrev * U["contrib_margin"]; last = P["active"][-1]
    return dict(rev=rev, cost=cost, con=con, jobs=rev / P["avg_job"], tech_per_job=SPLIT["technicians"] / (rev / P["avg_job"]),
                mature_rev=mrev, mature_con=mcon, oct_cluster=last * con - P["cluster_team_month"], oct_contrib=last * con,
                mature_cluster_month=U["retailers_per_cluster"] * mcon - MATURE_TEAM_MONTH, mature_contrib_month=U["retailers_per_cluster"] * mcon,
                mature_breakeven=MATURE_TEAM_MONTH / mcon)

D = dict(seed=2.5 * CR, pre=10.0 * CR, isafe=0.45 * CR, isafe_cap_post=6.0 * CR, pool_post=0.10,
         exit_ebitda_mult=15, exit_year=5, benchmark_val=9.0 * CR, score=89, benchmark_score=80)

def pilot():
    rows = []
    for m, a in zip(P["months"], P["active"]):
        rev = a * P["rev_per_retailer_month"]; con = rev * P["contrib_margin"]
        rows.append(dict(month=m, active=a, revenue=rev, contribution=con, team=P["cluster_team_month"], ebitda=con - P["cluster_team_month"], jobs=rev / P["avg_job"]))
    tot = {k: sum(r[k] for r in rows) for k in ("revenue", "contribution", "team", "ebitda", "jobs")}
    tot["retailer_months"] = sum(P["active"]); tot["contrib_per_retailer_month"] = P["rev_per_retailer_month"] * P["contrib_margin"]
    tot["breakeven_retailers"] = P["cluster_team_month"] / tot["contrib_per_retailer_month"]
    tot["first_positive_month"] = next(r["month"] for r in rows if r["ebitda"] > 0)
    tot["oct_run_rate_ebitda"] = rows[-1]["ebitda"]
    return rows, tot

def unit():
    c = U["rev_per_retailer_month"] * U["contrib_margin"]
    cl_rev = U["rev_per_retailer_month"] * 12 * U["retailers_per_cluster"]; cl_con = c * 12 * U["retailers_per_cluster"]
    return dict(contrib_per_retailer_month=c, cluster_revenue=cl_rev, cluster_contribution=cl_con, cluster_cost=U["cluster_cost_year"],
                cluster_ebitda=cl_con - U["cluster_cost_year"], cluster_margin=(cl_con - U["cluster_cost_year"]) / cl_rev,
                breakeven=U["cluster_cost_year"] / (c * 12))

def plan():
    out = []; r0, c0, cash, prev_rev = Y["start_retailers"], Y["start_clusters"], Y["start_cash"], Y["pilot_rev_run"]; trough = cash
    for i in range(5):
        r1, c1 = Y["retailers_end"][i], Y["clusters_end"][i]
        avg_r, avg_c = (r0 + r1) / 2, (c0 + c1) / 2
        rev = avg_r * Y["rev_per_retailer_year"][i]; con = rev * Y["contrib_margin"][i]
        clu = avg_c * Y["cluster_cost_year"]; hq = Y["hq"][i]; ebitda = con - clu - hq
        launch = (c1 - c0) * Y["launch_per_cluster"]; wc = max(0, rev - prev_rev) * Y["wc_share"]; tax = max(0, ebitda) * Y["tax"]
        cf = ebitda - tax - launch - wc; cash += cf; trough = min(trough, cash)
        out.append(dict(year=Y["years"][i], cal=Y["cal"][i], retailers=r1, clusters=c1, avg_retailers=avg_r, revenue=rev, contribution=con,
                        cluster_cost=clu, hq=hq, ebitda=ebitda, margin=ebitda / rev, launch=launch, wc=wc, tax=tax, cash_flow=cf, cum_cash=cash))
        r0, c0, prev_rev = r1, c1, rev
    return out, -trough

def deal():
    rows, need = plan()
    post = D["pre"] + D["seed"]; seed = D["seed"] / post
    isafe_pre = D["isafe"] / D["isafe_cap_post"]; pool_pre = D["pool_post"] / (1 - seed); f_pre = 1 - isafe_pre - pool_pre
    cap = {"Founders": f_pre * (1 - seed), "Pre-seed iSAFE": isafe_pre * (1 - seed), "ESOP pool": D["pool_post"], "Seed": seed}
    ev = rows[D["exit_year"] - 1]["ebitda"] * D["exit_ebitda_mult"]; val = ev * seed; mult = val / D["seed"]; irr = mult ** (1 / D["exit_year"]) - 1
    vc_ceiling = ev / (1.40 ** 5)
    scorecard = D["benchmark_val"] * D["score"] / D["benchmark_score"]
    return dict(post=post, cap=cap, ev=ev, ev_rev_mult=ev / rows[4]["revenue"], seed_value=val, multiple=mult, irr=irr, vc_ceiling=vc_ceiling,
                scorecard=scorecard, need=need, buffer=D["seed"] - need)

def conservative():
    """Revenue per retailer −10%, margin −2 points, rollout −25%, head office −15%."""
    import copy
    Y0 = copy.deepcopy(Y)
    try:
        Y["rev_per_retailer_year"] = [x * 0.9 for x in Y0["rev_per_retailer_year"]]; Y["contrib_margin"] = [m - 0.02 for m in Y0["contrib_margin"]]
        Y["retailers_end"] = [150, 350, 700, 1260, 2100]; Y["clusters_end"] = [3, 6, 12, 21, 35]; Y["hq"] = [h * 0.85 for h in Y0["hq"]]
        return plan()
    finally:
        Y.clear(); Y.update(Y0)

if __name__ == "__main__":
    print("retailer month", {k: round(v, 1) for k, v in retailer_month().items()})
    pr, pt = pilot(); u = unit(); pl, need = plan(); d = deal()
    print("PILOT"); [print(f" {r['month']} {r['active']:>3} rev {r['revenue']/L:5.2f}L con {r['contribution']/L:5.2f}L ebitda {r['ebitda']/L:+5.2f}L jobs {r['jobs']:.0f}") for r in pr]
    print(f" total rev {pt['revenue']/L:.1f}L con {pt['contribution']/L:.1f}L team {pt['team']/L:.1f}L EBITDA {pt['ebitda']/L:+.1f}L jobs {pt['jobs']:.0f} | contrib/retailer/month ₹{pt['contrib_per_retailer_month']:.0f} | breakeven {pt['breakeven_retailers']:.1f} | first + {pt['first_positive_month']} | Oct EBITDA {pt['oct_run_rate_ebitda']/L:.2f}L")
    print("UNIT", {k: round(v / L, 2) if v > 100 else round(v, 3) for k, v in u.items()})
    print("PLAN"); [print(f" {r['year']} {r['cal']} ret {r['retailers']} cl {r['clusters']} rev {r['revenue']/CR:6.2f} con {r['contribution']/CR:5.2f} clu {r['cluster_cost']/CR:4.2f} hq {r['hq']/CR:4.2f} EBITDA {r['ebitda']/CR:+6.2f} ({r['margin']:.1%}) launch {r['launch']/CR:4.2f} wc {r['wc']/CR:4.2f} tax {r['tax']/CR:4.2f} cf {r['cash_flow']/CR:+5.2f} cum {r['cum_cash']/CR:+5.2f}") for r in pl]
    print(f"peak need {need/CR:.2f} Cr | buffer {d['buffer']/CR:.2f}")
    print("DEAL", {k: (round(v / CR, 2) if isinstance(v, float) and v > 1e5 else (round(v, 3) if isinstance(v, float) else v)) for k, v in d.items() if k != "cap"}, {k: f"{v:.1%}" for k, v in d["cap"].items()})
