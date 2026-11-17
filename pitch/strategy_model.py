"""Keepwell strategy rebuild: scenario model behind STRATEGY_REBUILD.md (version 2, after the investor red-team).

    python3 strategy_model.py            # prints every table used in the document

Strategies modelled month by month over 72 months on the red-team's harder assumptions:
  A. Verified service network: brands pay per resolved complaint; Keepwell pays agencies.
     REJECTED (thin middleman margin).
  B. Software-only triage API (3-year view).
  C. Agency-first, the old pitch (plan G figures from keepwell_model.xlsx). REJECTED.
  D. Keepwell Verify: brands pay per verified job on their own networks; administrators pay per claim.
  E. Keepwell Care: households buy an annual care plan from their local agency, paid upfront.
  E + D combined, lean and evidence-gated: the RECOMMENDATION.

Every input is an ASSUMPTION to validate with real buyers.
Illustrative case for the IIIT Hyderabad ESFS course pitch.
"""
from dataclasses import dataclass

L = 1e5          # Rs 1 lakh
CR = 1e7         # Rs 1 crore
MONTHS = 72

BASE = {
    # price and cost per resolved complaint, Strategy A
    "payer_price_per_resolved": 475,       # brand pays per RESOLVED complaint, not per visit
    "brand_cost_today_per_visit": 450,     # what a brand pays its partner per visit today (research range Rs 400-700)
    "brand_visits_per_complaint_today": 1.33,  # ~1 in 4 complaints needs a second visit (global first-time fix ~75%)
    "agency_payout_per_visit": 325,
    "revisit_rate_with_circuit": 0.15,     # prepared visits cut repeats from ~25% to ~15%; re-visits are paid by Keepwell
    "qa_ops_per_job": 10,                  # remote proof-pack review, partner-management tools
    "ai_msg_cost_per_job": 8,
    "payer_payment_days": 60,
    # volume, Strategy A
    "pilot_jobs": 250,                     # per payer per month during a 3-month pilot
    "brand_contract_jobs": 600,            # mid-tier brand, Tier 2/3 jobs in TS+AP a month
    "admin_contract_jobs": 400,            # administrator claim repairs in TS+AP a month
    "pilot_conversion": 0.70,              # expected share of pilots that convert (expected-value modelling)
    "payer_churn_per_year": 0.10,
    "brand_geo_multiplier": 2.0,           # south India, phased in months 19-30
    "admin_geo_multiplier": 1.5,
    "routed_jobs_per_agency": 60,
    "max_admins": 4,
    # other revenue lines
    "platform_fee_year": 8 * L,            # triage API on the payer's own intake; separately priced
    "platform_takeup": 0.50,               # expected share of converted payers who buy it
    "claims_licence_year": 30 * L,         # evidence-pack licence for one administrator
    "plan_attach_rate": 0.03, "plan_commission": 240,
    "desk_pro_price": 399, "desk_pro_uptake": 0.25,
    # people and overheads, Rs a month by period (months 1-12 include an enterprise sales lead from month 2)
    "team_cost": [(12, 15 * L), (24, 32 * L), (36, 48 * L), (48, 70 * L), (60, 95 * L), (72, 120 * L)],
    "other_opex_share": 0.18,
    # financing
    "invoice_discount_from_month": 19, "invoice_discount_share": 0.70, "invoice_discount_rate": 0.14,
}
INPUTS = dict(BASE)

# signed payers: (month, type). Brands first; the first administrator only at month 10 (6-12-month cycle)
PAYERS_FIRST = [(4, "brand"), (7, "brand"), (10, "admin")]
NEW_PAYERS = [(13, 0.5), (25, 0.7), (37, 0.9), (49, 1.0)]   # new payers a month from that month on


def team_cost(m):
    for upto, c in INPUTS["team_cost"]:
        if m <= upto:
            return c
    return INPUTS["team_cost"][-1][1]


def payer_list(m, delay=0):
    out = [(s + delay, t) for s, t in PAYERS_FIRST if s + delay <= m]
    acc = 0.0
    for mm in range(13 + delay, m + 1):
        rate = [r for start, r in NEW_PAYERS if mm >= start + delay][-1]
        acc += rate
        while acc >= 1:
            acc -= 1
            n_admin = sum(1 for _, t in out if t == "admin")
            t = "admin" if (len(out) % 3 == 0 and n_admin < INPUTS["max_admins"]) else "brand"
            out.append((mm, t))
    return out


def survive(start, m):
    age = m - start
    if age < 3:
        return 0.0
    return INPUTS["pilot_conversion"] * (1 - INPUTS["payer_churn_per_year"]) ** ((age - 3) / 12)


def payer_jobs(start, kind, m):
    I = INPUTS
    age = m - start
    if age < 0:
        return 0.0
    if age < 3:
        return I["pilot_jobs"]
    base = I["brand_contract_jobs"] if kind == "brand" else I["admin_contract_jobs"]
    ramp = min(1.0, (age - 2) / 4)
    mult = I["brand_geo_multiplier"] if kind == "brand" else I["admin_geo_multiplier"]
    geo = 1 + (mult - 1) * min(1.0, max(0, m - 18) / 12)
    return base * ramp * survive(start, m) * geo


@dataclass
class Row:
    m: int; payers: int; jobs: float; agencies: float; gmv: float; net: float; other: float
    software: float; direct: float; opex: float; ebitda: float; receivables: float; cash_flow: float


def strategy_a(delay=0, months=MONTHS):
    I = INPUTS
    rows, prev_unfin = [], 0.0
    for m in range(1, months + 1):
        ps = payer_list(m, delay)
        jobs = sum(payer_jobs(s, k, m) for s, k in ps)
        visits = jobs * (1 + I["revisit_rate_with_circuit"])
        agencies = max(14, visits / I["routed_jobs_per_agency"] * 1.15)
        g = jobs * I["payer_price_per_resolved"]
        net = g - visits * I["agency_payout_per_visit"]               # re-visits are paid by us
        conv = sum(survive(s, m) for s, _ in ps)
        platform = conv * I["platform_takeup"] * I["platform_fee_year"] / 12
        admin_conv = sum(survive(s, m) for s, k in ps if k == "admin")
        claims = min(admin_conv, 1 if m < 33 else 2) * I["claims_licence_year"] / 12 if m >= 24 else 0
        plans = jobs * I["plan_attach_rate"] * I["plan_commission"] if m >= 20 else 0
        desk = agencies * I["desk_pro_uptake"] * I["desk_pro_price"]
        other = platform + claims + plans + desk
        direct = jobs * (I["qa_ops_per_job"] + I["ai_msg_cost_per_job"])
        opex = team_cost(m) * (1 + I["other_opex_share"])
        ebitda = net + other - direct - opex
        receivables = g * I["payer_payment_days"] / 30
        financed = receivables * I["invoice_discount_share"] if m >= I["invoice_discount_from_month"] else 0
        interest = financed * I["invoice_discount_rate"] / 12
        unfin = receivables - financed
        cf = ebitda - interest - (unfin - prev_unfin)
        prev_unfin = unfin
        rows.append(Row(m, len(ps), jobs, agencies, g, net, other, platform + claims, direct, opex, ebitda, receivables, cf))
    return rows


def yr(rows, f, y):
    return sum(f(r) for r in rows[(y - 1) * 12:y * 12]) / CR


def net_rev(r): return r.net + r.other
def gmv(r): return r.gmv + r.other


def peak_need(rows, a, b):
    cum, worst = 0.0, 0.0
    for r in rows[a - 1:b]:
        cum += r.cash_flow
        worst = min(worst, cum)
    return -worst / CR


def rounds(rows, bank=0.21, grants=0.10, contingency=0.15):
    """Step A funds runway to month 15 (seed planned at ~12, 3-month buffer); the seed funds to month 34."""
    step_a = max(0.0, peak_need(rows, 1, 15) * (1 + contingency) - bank - grants)
    step_a = -(-step_a * 4 // 1) / 4                      # round up to Rs 0.25 Cr
    total = peak_need(rows, 1, 34) * (1 + contingency) - bank - grants
    seed = max(0.0, -(-(total - step_a) * 2 // 1) / 2)     # round up to Rs 0.5 Cr
    return step_a, seed


def irr(rows, seed, pre, exit_year=6, gmv_multiple=2.5, later_dilution=0.68):
    g6 = yr(rows, gmv, 6)
    g = g6 if exit_year == 6 else g6 * 1.25 ** (exit_year - 6)   # beyond Y6: +25% a year
    exit_val = g * gmv_multiple
    moic = exit_val * (seed / (pre + seed) * later_dilution) / seed
    return exit_val, moic, moic ** (1 / (exit_year - 1)) - 1      # seed closes at the end of year 1


def run(overrides=None, delay=0):
    INPUTS.clear(); INPUTS.update(BASE); INPUTS.update(overrides or {})
    try:
        return strategy_a(delay)
    finally:
        INPUTS.clear(); INPUTS.update(BASE)


# ------------------------------------------------------------------ Strategy D: Circuit + Verify for brand service networks
D_BASE = {
    "fee_per_verified_job": 20,        # brand pays per job verified through Circuit on ITS OWN partner network
    "brand_jobs_per_year": 400000,     # mid-tier brand: national warranty + installation + paid service jobs a year
    "admin_fee_per_claim": 40,         # administrator pays per claim evidence pack
    "admin_claims_per_year": 150000,   # appliance claims handled by one administrator a year
    "setup_fee": 5 * L,                # one-off integration fee per payer
    "rollout_months": 12,              # pilot region (~6% of jobs) to national
    "pilot_share": 0.06,
    "conversion": 0.70, "churn_per_year": 0.08,
    "ai_cost_per_job": 5,              # AI + messaging (agency partners use it free)
    "base_team": [(12, 14 * L), (24, 26 * L), (36, 36 * L), (48, 46 * L), (60, 56 * L), (72, 66 * L)],
    "cs_per_live_payer": 1.2 * L,      # implementation + customer success per live payer a month
    "other_opex_share": 0.18,
    "payment_days": 60,
}
D = dict(D_BASE)
D_FIRST = [(4, "brand"), (7, "brand"), (10, "admin")]
D_NEW = [(13, 0.4), (25, 0.5), (37, 0.5), (49, 0.5)]


def d_payers(m, delay=0):
    out = [(s + delay, t) for s, t in D_FIRST if s + delay <= m]
    acc = 0.0
    for mm in range(13 + delay, m + 1):
        acc += [r for st, r in D_NEW if mm >= st + delay][-1]
        while acc >= 1:
            acc -= 1
            n_admin = sum(1 for _, t in out if t == "admin")
            out.append((mm, "admin" if (len(out) % 4 == 0 and n_admin < 6) else "brand"))
    return out


def d_live(start, m):
    age = m - start
    if age < 0: return 0.0, 0.0
    if age < 3: return 1.0, D["pilot_share"]                       # pilot: one region
    w = D["conversion"] * (1 - D["churn_per_year"]) ** ((age - 3) / 12)
    share = D["pilot_share"] + (1 - D["pilot_share"]) * min(1.0, (age - 3) / D["rollout_months"])
    return w, share


def strategy_d(delay=0, months=MONTHS):
    rows, prev_rec = [], 0.0
    for m in range(1, months + 1):
        ps = d_payers(m, delay)
        rev = jobs = setup = live = 0.0
        for s, k in ps:
            w, share = d_live(s, m)
            live += w
            if k == "brand":
                j = D["brand_jobs_per_year"] / 12 * share * w
                rev += j * D["fee_per_verified_job"]
            else:
                j = D["admin_claims_per_year"] / 12 * share * w
                rev += j * D["admin_fee_per_claim"]
            jobs += j
            if m - s == 3: setup += D["setup_fee"] * D["conversion"]
        rev += setup
        cogs = jobs * D["ai_cost_per_job"]
        base = [c for upto, c in D["base_team"] if m <= upto][0] if m <= D["base_team"][-1][0] else D["base_team"][-1][1]
        opex = (base + live * D["cs_per_live_payer"]) * (1 + D["other_opex_share"])
        ebitda = rev - cogs - opex
        rec = rev * D["payment_days"] / 30
        cf = ebitda - (rec - prev_rec); prev_rec = rec
        rows.append(Row(m, len(ps), jobs, 0, rev, rev, 0, rev, cogs, opex, ebitda, rec, cf))
    return rows


def run_d(overrides=None, delay=0):
    D.clear(); D.update(D_BASE); D.update(overrides or {})
    try:
        return strategy_d(delay)
    finally:
        D.clear(); D.update(D_BASE)


def irr_rev(rows, seed, pre, exit_year=6, multiple=6, later_dilution=0.68):
    r6 = yr(rows, net_rev, 6)
    r = r6 if exit_year == 6 else r6 * 1.25 ** (exit_year - 6)
    ev = r * multiple
    moic = ev * (seed / (pre + seed) * later_dilution) / seed
    return ev, moic, moic ** (1 / (exit_year - 1)) - 1


# ------------------------------------------------------------------ Strategy E: Keepwell Care plans sold through agencies
E_BASE = {
    "plan_price": 1499,                # annual home care plan: 2 preventive services + labour-free repairs + priority + record
    "attach_rate": 0.04,               # share of an agency's monthly jobs that buy a plan (after a 2-month ramp)
    "jobs_per_agency": 125,            # observed median in the 18 interviews (illustrative)
    "agency_commission_new": 250, "agency_commission_renewal": 100,
    "delivery_cost_per_plan_year": 800,  # 2 preventive visits x Rs 300 + ~0.5 labour repair x Rs 300 + Rs 50 ops/AI
    "renewal_rate": 0.55,
    "agency_adds": [(3, 0), (12, 6), (24, 18), (36, 36), (48, 50), (60, 60), (72, 60)],  # new agencies a month (field reps)
    "agency_churn_month": 0.02,
    "acq_cash_per_agency": 2000,
    "team": [(12, 14 * L), (24, 28 * L), (36, 42 * L), (48, 55 * L), (60, 68 * L), (72, 80 * L)],
    "other_opex_share": 0.18,
}
E = dict(E_BASE)


def strategy_e(months=MONTHS, delay=0):
    agencies, cohorts, rows = 14.0, [], []      # cohorts: (month sold, plans) for renewals and ratable revenue
    ages = []                                    # agency cohorts for attach ramp: (month joined, count)
    ages.append((-2, 14.0))
    for m in range(1, months + 1):
        add = [a for upto, a in E["agency_adds"] if m <= upto][0] if m <= E["agency_adds"][-1][0] else E["agency_adds"][-1][1]
        if m <= delay: add = 0
        ages = [(j, c * (1 - E["agency_churn_month"])) for j, c in ages]
        if add: ages.append((m, add))
        agencies = sum(c for _, c in ages)
        live_selling = sum(c * min(1.0, max(0, m - j) / 2) for j, c in ages)  # 2-month ramp
        new_plans = live_selling * E["jobs_per_agency"] * E["attach_rate"] if m > delay else 0
        renewals = sum(n * E["renewal_rate"] for sm, n in cohorts if m - sm == 12)
        sold = new_plans + renewals
        cohorts.append((m, sold))
        active = sum(n for sm, n in cohorts if 0 <= m - sm < 12)
        revenue = active * E["plan_price"] / 12                          # ratable
        cash_in = sold * E["plan_price"]                                  # paid upfront
        commission = new_plans * E["agency_commission_new"] + renewals * E["agency_commission_renewal"]
        delivery = active * E["delivery_cost_per_plan_year"] / 12
        direct = commission + delivery
        team = [c for upto, c in E["team"] if m <= upto][0] if m <= E["team"][-1][0] else E["team"][-1][1]
        opex = team * (1 + E["other_opex_share"]) + add * E["acq_cash_per_agency"]
        ebitda = revenue - direct - opex
        cf = cash_in - direct - opex                                      # deferred revenue funds growth
        r = Row(m, int(agencies), active, agencies, revenue, revenue, 0, 0, direct, opex, ebitda, 0, cf)
        r.plans_sold = sold
        rows.append(r)
    return rows


def run_e(overrides=None, delay=0):
    E.clear(); E.update(E_BASE); E.update(overrides or {})
    try:
        return strategy_e(delay=delay)
    finally:
        E.clear(); E.update(E_BASE)


# ------------------------------------------------------------------ Combined platform: E (households via agencies) + D (brands/admins)
def combined(e_over=None, d_over=None, d_delay=6, shared_saving=0.70):
    """One company: E's team runs the agency network; D adds its revenue, AI cost and customer success, and
    only (1 - shared_saving) of D's base team, because engineering and the record are shared.
    D starts d_delay months later (brands are sold once the network and record show results)."""
    Er, Dr = run_e(e_over), run_d(d_over, d_delay)
    out = []
    for e, d in zip(Er, Dr):
        rev = e.gmv + d.gmv
        d_base = [c for upto, c in D_BASE["base_team"] if d.m <= upto][0] if d.m <= D_BASE["base_team"][-1][0] else D_BASE["base_team"][-1][1]
        d_cs = d.opex - d_base * (1 + D_BASE["other_opex_share"])
        opex = e.opex + d_cs + d_base * (1 - shared_saving) * (1 + D_BASE["other_opex_share"])
        direct = e.direct + d.direct
        ebitda = rev - direct - opex
        cf = e.cash_flow + (d.cash_flow - (d.ebitda - (d.gmv - d.direct - d.opex))) if False else None
        # cash: E cash basis + D accrual less its receivable build, with the shared-cost adjustment
        d_cf_adj = d.cash_flow + (d.opex - d_cs - d_base * (1 - shared_saving) * (1 + D_BASE["other_opex_share"]))
        out.append(Row(e.m, d.payers, e.jobs, e.agencies, rev, rev, 0, d.gmv, direct, opex, ebitda, d.receivables,
                       e.cash_flow + d_cf_adj))
    return out


def strategy_b():
    """Software-only: Rs 25 L ACV; first contract month 9, then one every 3 months, every 1.5 after the seed."""
    out, n = [], 0.0
    for m in range(1, 37):
        if m >= 9:
            n += 1 if m == 9 else (1 / 3 if m <= 12 else 1 / 1.5)
        rev = int(n) * 25 * L / 12
        t = 11 * L if m <= 12 else 24 * L if m <= 24 else 36 * L
        out.append((rev, rev * 0.75 - t * 1.18))
    return ([sum(x[0] for x in out[i * 12:(i + 1) * 12]) / CR for i in range(3)],
            [sum(x[1] for x in out[i * 12:(i + 1) * 12]) / CR for i in range(3)])


C_ANNUAL = {"revenue": [0.20, 0.85, 3.64], "ebitda": [-1.78, -2.15, -2.77]}


def f2(xs, d=2): return " / ".join(f"{x:.{d}f}" for x in xs)


if __name__ == "__main__":
    A = run()
    I = BASE
    revisit_cost = I["revisit_rate_with_circuit"] * I["agency_payout_per_visit"]
    net_job = I["payer_price_per_resolved"] - I["agency_payout_per_visit"] - revisit_cost
    contrib = net_job - I["qa_ops_per_job"] - I["ai_msg_cost_per_job"]
    brand_today = I["brand_cost_today_per_visit"] * I["brand_visits_per_complaint_today"]
    print("== Per resolved complaint (Rs)")
    print(f"  Brand pays today ~{brand_today:.0f} ({I['brand_cost_today_per_visit']} x {I['brand_visits_per_complaint_today']} visits); "
          f"with Keepwell {I['payer_price_per_resolved']} -> saves {brand_today - I['payer_price_per_resolved']:.0f} "
          f"({(brand_today - I['payer_price_per_resolved'])/brand_today*100:.0f}%)")
    print(f"  Agency paid {I['agency_payout_per_visit']} per visit | re-visit cost on us {revisit_cost:.0f} | "
          f"Keepwell net {net_job:.0f} ({net_job/I['payer_price_per_resolved']*100:.1f}% of price) | contribution {contrib:.0f}")

    print("\n== Year 1..6 (Rs Cr)  [A from this model; B and C over 3 years]")
    print(f"  A net revenue   {f2([yr(A, net_rev, y) for y in range(1, 7)])}")
    print(f"  A GMV           {f2([yr(A, gmv, y) for y in range(1, 7)])}")
    print(f"  A EBITDA        {f2([yr(A, lambda r: r.ebitda, y) for y in range(1, 7)])}")
    print("  A software share of net revenue: " + " / ".join(
        f"{yr(A, lambda r: r.software, y) / max(1e-9, yr(A, net_rev, y)) * 100:.0f}%" for y in range(1, 7)))
    br, be = strategy_b()
    print(f"  B revenue (Y1-3) {f2(br)} | EBITDA {f2(be)}")
    print(f"  C revenue (Y1-3) {f2(C_ANNUAL['revenue'])} | EBITDA {f2(C_ANNUAL['ebitda'])}")

    print("\n== Strategy A by half-year")
    print("  month | payers | resolved jobs/mo | agencies | net rev/mo L | EBITDA/mo L | receivables L")
    for r in A:
        if r.m % 6 == 0:
            print(f"  {r.m:5d} | {r.payers:6d} | {r.jobs:16.0f} | {r.agencies:8.0f} | {net_rev(r)/L:12.1f} | {r.ebitda/L:11.1f} | {r.receivables/L:8.1f}")
    first_pos = next((r.m for r in A if r.ebitda > 0), None)
    recs = lambda upto: sum(r.jobs for r in A[:upto]) / 1e5
    print(f"  EBITDA positive from month {first_pos} | verified records: m24 {recs(24):.1f} L, m36 {recs(36):.1f} L, m72 {recs(72):.1f} L")
    for mm in (12, 24, 30, 36):
        r = A[mm - 1]
        print(f"  run-rate month {mm}: net Rs {net_rev(r)*12/CR:.2f} Cr | GMV Rs {gmv(r)*12/CR:.2f} Cr | payers signed {r.payers}")

    step_a, seed = rounds(A)
    print("\n== Rounds (15% contingency; less Rs 21 L cash and Rs 10 L grant)")
    print(f"  Step A (runway to month 15): Rs {step_a:.2f} Cr | Seed at ~month 12 (runway to month 34): Rs {seed:.1f} Cr")
    na = rounds(run({"invoice_discount_share": 0.0}))
    print(f"  Without invoice discounting: Step A Rs {na[0]:.2f} Cr | Seed Rs {na[1]:.1f} Cr")

    pre = 20
    print(f"\n== Investor return on the seed: Rs {seed:.1f} Cr at Rs {pre} Cr pre ({seed/(pre+seed)*100:.0f}% stake), exit valued on GMV")
    for ey in (6, 7):
        for mult in (2.0, 2.5, 3.0):
            ev, moic, r = irr(A, seed, pre, ey, mult)
            print(f"  exit year {ey}, {mult:.1f}x GMV: exit Rs {ev:.0f} Cr -> {moic:.1f}x, IRR {r*100:.0f}%")

    # ---------------- Strategy D
    DD = run_d()
    print("\n================ STRATEGY D: Circuit + Verify for brand service networks ================")
    print(f"  per brand at full national rollout: {D_BASE['brand_jobs_per_year']:,} jobs x Rs {D_BASE['fee_per_verified_job']} = Rs {D_BASE['brand_jobs_per_year']*D_BASE['fee_per_verified_job']/CR:.2f} Cr a year")
    print(f"  per administrator: {D_BASE['admin_claims_per_year']:,} claims x Rs {D_BASE['admin_fee_per_claim']} = Rs {D_BASE['admin_claims_per_year']*D_BASE['admin_fee_per_claim']/CR:.2f} Cr a year")
    print(f"  D revenue  {f2([yr(DD, net_rev, y) for y in range(1, 7)])}")
    print(f"  D EBITDA   {f2([yr(DD, lambda r: r.ebitda, y) for y in range(1, 7)])}")
    print(f"  D gross margin Y3: {(1 - yr(DD, lambda r: r.direct, 3)/yr(DD, net_rev, 3))*100:.0f}%")
    print("  month | payers signed | verified jobs/mo | revenue/mo L | EBITDA/mo L")
    for r in DD:
        if r.m % 6 == 0:
            print(f"  {r.m:5d} | {r.payers:13d} | {r.jobs:16.0f} | {r.gmv/L:12.1f} | {r.ebitda/L:11.1f}")
    fp = next((r.m for r in DD if r.ebitda > 0), None)
    print(f"  EBITDA positive from month {fp} | verified jobs (records) m24 {sum(r.jobs for r in DD[:24])/1e5:.1f} L, m36 {sum(r.jobs for r in DD[:36])/1e5:.1f} L")
    for mm in (12, 18, 24, 30, 36):
        print(f"  run-rate month {mm}: Rs {DD[mm-1].gmv*12/CR:.2f} Cr")
    sa_d, sd_d = rounds(DD)
    print(f"  Rounds: Step A (to month 15) Rs {sa_d:.2f} Cr | seed (to month 34) Rs {sd_d:.1f} Cr")
    preD = 25
    print(f"  Investor return, seed Rs {sd_d:.1f} Cr at Rs {preD} Cr pre ({sd_d/(preD+sd_d)*100:.0f}% stake), exit on revenue:")
    for ey in (6, 7):
        for mult in (5, 6, 8):
            ev, moic, r = irr_rev(DD, sd_d, preD, ey, mult)
            print(f"    exit year {ey}, {mult}x revenue: exit Rs {ev:.0f} Cr -> {moic:.1f}x, IRR {r*100:.0f}%")
    print("  Stress tests D: revenue Y1/Y2/Y3 | Y6 | Step A + seed")
    for name, ov, d in [("Base", {}, 0), ("Fee Rs 12 per job", {"fee_per_verified_job": 12}, 0),
                        ("Half the jobs per brand (2 lakh)", {"brand_jobs_per_year": 200000}, 0),
                        ("Rollout takes 24 months", {"rollout_months": 24}, 0),
                        ("Conversion 50%", {"conversion": 0.5}, 0), ("Pilots 3 months late", {}, 3),
                        ("COMBINED: Rs 15 + 2.5 lakh jobs + 50% conv + 18-mo rollout",
                         {"fee_per_verified_job": 15, "brand_jobs_per_year": 250000, "conversion": 0.5, "rollout_months": 18}, 0)]:
        R = run_d(ov, d); a_, s_ = rounds(R)
        print(f"    {name:58s} {f2([yr(R, net_rev, k) for k in (1, 2, 3)])} | {yr(R, net_rev, 6):5.1f} | {a_:.2f} + {s_:.1f}")

    # ---------------- Strategy E
    EE = run_e()
    c = E_BASE
    contrib_new = c["plan_price"] - c["agency_commission_new"] - c["delivery_cost_per_plan_year"]
    contrib_ren = c["plan_price"] - c["agency_commission_renewal"] - c["delivery_cost_per_plan_year"]
    print("\n================ STRATEGY E: Keepwell Care plans sold through partner agencies ================")
    print(f"  per plan: Rs {c['plan_price']} | agency commission {c['agency_commission_new']} (renewal {c['agency_commission_renewal']}) | delivery {c['delivery_cost_per_plan_year']} -> contribution Rs {contrib_new} new, Rs {contrib_ren} renewal")
    per_ag = c["jobs_per_agency"] * c["attach_rate"] * 12
    print(f"  per agency: {per_ag:.0f} new plans a year -> Rs {per_ag*c['plan_price']/L:.2f} L plan revenue; agency earns Rs {per_ag*c['agency_commission_new']/L:.2f} L commission + Rs {per_ag*600/L:.2f} L for service visits")
    print(f"  E revenue  {f2([yr(EE, net_rev, y) for y in range(1, 7)])}")
    print(f"  E EBITDA   {f2([yr(EE, lambda r: r.ebitda, y) for y in range(1, 7)])}")
    print("  month | agencies | active plans | revenue/mo L | EBITDA/mo L")
    for r in EE:
        if r.m % 6 == 0:
            print(f"  {r.m:5d} | {r.agencies:8.0f} | {r.jobs:12.0f} | {r.gmv/L:12.1f} | {r.ebitda/L:11.1f}")
    fp = next((r.m for r in EE if r.ebitda > 0), None)
    print(f"  EBITDA positive from month {fp}")
    sa_e, sd_e = rounds(EE)
    print(f"  Rounds (cash basis, plans paid upfront): Step A Rs {sa_e:.2f} Cr | seed Rs {sd_e:.1f} Cr")
    preE = 20
    for ey in (6, 7):
        for mult in (2, 3, 4):
            ev, moic, r_ = irr_rev(EE, sd_e, preE, ey, mult)
            print(f"    seed Rs {sd_e:.1f} Cr at Rs {preE} Cr pre | exit year {ey}, {mult}x revenue: Rs {ev:.0f} Cr -> {moic:.1f}x, IRR {r_*100:.0f}%")
    print("  Stress tests E: revenue Y1/Y2/Y3 | Y6 | Step A + seed")
    for name, ov in [("Base", {}), ("Attach 2.5%", {"attach_rate": 0.025}), ("Price Rs 999", {"plan_price": 999, "delivery_cost_per_plan_year": 650}),
                     ("Renewal 40%", {"renewal_rate": 0.40}), ("Delivery cost Rs 1,000", {"delivery_cost_per_plan_year": 1000}),
                     ("Half the agency growth", {"agency_adds": [(3, 0), (12, 3), (24, 9), (36, 18), (48, 25), (60, 30), (72, 30)]}),
                     ("COMBINED: attach 2.5% + renewal 40% + delivery Rs 1,000", {"attach_rate": 0.025, "renewal_rate": 0.40, "delivery_cost_per_plan_year": 1000})]:
        R = run_e(ov); a_, s_ = rounds(R)
        print(f"    {name:58s} {f2([yr(R, net_rev, k) for k in (1, 2, 3)])} | {yr(R, net_rev, 6):5.1f} | {a_:.2f} + {s_:.1f} | EBITDA+ m{next((r.m for r in R if r.ebitda > 0), '-')}")

    # ---------------- Combined
    CC = combined()
    print("\n================ COMBINED PLATFORM: Keepwell Care (E) + Verify for brands/admins (D) ================")
    print(f"  revenue  {f2([yr(CC, net_rev, y) for y in range(1, 7)])}")
    print(f"    of which households (E) {f2([yr(EE, net_rev, y) for y in range(1, 7)])}")
    print(f"  EBITDA   {f2([yr(CC, lambda r: r.ebitda, y) for y in range(1, 7)])}")
    fpc = next((r.m for r in CC if r.ebitda > 0), None)
    print(f"  EBITDA positive from month {fpc}")
    for mm in (12, 18, 24, 30, 36):
        print(f"  run-rate month {mm}: Rs {CC[mm-1].gmv*12/CR:.2f} Cr | agencies {CC[mm-1].agencies:.0f} | active plans {CC[mm-1].jobs:.0f} | B2B payers signed {CC[mm-1].payers}")
    sa_c, sd_c = rounds(CC)
    print(f"  Rounds: Step A (to month 15) Rs {sa_c:.2f} Cr | seed (to month 34) Rs {sd_c:.1f} Cr")
    preC = 20
    for ey in (6, 7):
        for mult in (3, 4, 5):
            ev, moic, r_ = irr_rev(CC, sd_c, preC, ey, mult)
            print(f"    seed Rs {sd_c:.1f} Cr at Rs {preC} Cr pre ({sd_c/(preC+sd_c)*100:.0f}%) | exit year {ey}, {mult}x revenue: Rs {ev:.0f} Cr -> {moic:.1f}x, IRR {r_*100:.0f}%")
    print("  Stress tests combined: revenue Y1/Y2/Y3 | Y6 | Step A + seed | EBITDA+ month")
    for name, eo, do in [("Base", {}, {}), ("Attach 2.5%", {"attach_rate": 0.025}, {}),
                         ("Brand fee Rs 12, half jobs", {}, {"fee_per_verified_job": 12, "brand_jobs_per_year": 200000}),
                         ("Half the agency growth", {"agency_adds": [(3, 0), (12, 3), (24, 9), (36, 18), (48, 25), (60, 30), (72, 30)]}, {}),
                         ("COMBINED DOWNSIDE (all three)", {"attach_rate": 0.025, "agency_adds": [(3, 0), (12, 3), (24, 9), (36, 18), (48, 25), (60, 30), (72, 30)]},
                          {"fee_per_verified_job": 12, "brand_jobs_per_year": 200000})]:
        R = combined(eo, do); a_, s_ = rounds(R)
        print(f"    {name:34s} {f2([yr(R, net_rev, k) for k in (1, 2, 3)])} | {yr(R, net_rev, 6):5.1f} | {a_:.2f} + {s_:.1f} | m{next((r.m for r in R if r.ebitda > 0), '-')}")

    # ---------------- Lean, evidence-gated version of the combined platform (the recommendation)
    lean_e = {"team": [(12, 11 * L), (24, 20 * L), (36, 30 * L), (48, 40 * L), (60, 50 * L), (72, 60 * L)]}
    lean_d = {"base_team": [(12, 0), (24, 8 * L), (36, 14 * L), (48, 20 * L), (60, 26 * L), (72, 30 * L)], "cs_per_live_payer": 1.0 * L}
    LC = combined(lean_e, lean_d, shared_saving=0.0)
    print("\n================ RECOMMENDED: lean, evidence-gated combined platform ================")
    print(f"  revenue  {f2([yr(LC, net_rev, y) for y in range(1, 7)])}")
    print(f"  EBITDA   {f2([yr(LC, lambda r: r.ebitda, y) for y in range(1, 7)])}")
    fpl = next((r.m for r in LC if r.ebitda > 0), None)
    print(f"  EBITDA positive from month {fpl}")
    for mm in (6, 12, 18, 24, 30, 36):
        r = LC[mm-1]
        print(f"  month {mm}: run-rate Rs {r.gmv*12/CR:.2f} Cr | agencies {r.agencies:.0f} | active plans {r.jobs:.0f} | B2B payers signed {r.payers} | EBITDA/mo Rs {r.ebitda/L:.1f} L")
    sa_l, sd_l = rounds(LC)
    print(f"  Rounds: Step A (to month 15) Rs {sa_l:.2f} Cr | seed (to month 34) Rs {sd_l:.1f} Cr")
    for preL in (15, 20):
        for ey in (6, 7):
            for mult in (3, 4, 5):
                ev, moic, r_ = irr_rev(LC, sd_l, preL, ey, mult)
                print(f"    seed Rs {sd_l:.1f} Cr at Rs {preL} Cr pre ({sd_l/(preL+sd_l)*100:.0f}%) | exit year {ey}, {mult}x revenue: Rs {ev:.0f} Cr -> {moic:.1f}x, IRR {r_*100:.0f}%")
    print("  Stress tests (lean): revenue Y1/Y2/Y3 | Y6 | Step A + seed | EBITDA+ month")
    for name, eo, do in [("Base", {}, {}), ("Attach 2.5%", {"attach_rate": 0.025}, {}),
                         ("Brand fee Rs 12, half jobs", {}, {"fee_per_verified_job": 12, "brand_jobs_per_year": 200000}),
                         ("Half the agency growth", {"agency_adds": [(3, 0), (12, 3), (24, 9), (36, 18), (48, 25), (60, 30), (72, 30)]}, {}),
                         ("COMBINED DOWNSIDE (all three)", {"attach_rate": 0.025, "agency_adds": [(3, 0), (12, 3), (24, 9), (36, 18), (48, 25), (60, 30), (72, 30)]},
                          {"fee_per_verified_job": 12, "brand_jobs_per_year": 200000})]:
        eo2 = dict(lean_e); eo2.update(eo); do2 = dict(lean_d); do2.update(do)
        R = combined(eo2, do2, shared_saving=0.0); a_, s_ = rounds(R)
        print(f"    {name:34s} {f2([yr(R, net_rev, k) for k in (1, 2, 3)])} | {yr(R, net_rev, 6):5.1f} | {a_:.2f} + {s_:.1f} | m{next((r.m for r in R if r.ebitda > 0), '-')}")

    print("\n== Stress tests A: net revenue Y1/Y2/Y3 | Y6 | Step A + seed need (Rs Cr)")
    cases = [
        ("Base case", {}, 0),
        ("Price Rs 425 per resolved job", {"payer_price_per_resolved": 425}, 0),
        ("Half the volume per payer", {"brand_contract_jobs": 300, "admin_contract_jobs": 200}, 0),
        ("Re-visits stay at 25%", {"revisit_rate_with_circuit": 0.25}, 0),
        ("No platform fee", {"platform_fee_year": 0}, 0),
        ("First pilots 3 months late", {}, 3),
        ("Pilot conversion 50%", {"pilot_conversion": 0.5}, 0),
        ("COMBINED: Rs 425 + half volume + 50% conversion",
         {"payer_price_per_resolved": 425, "brand_contract_jobs": 300, "admin_contract_jobs": 200, "pilot_conversion": 0.5}, 0),
    ]
    for name, ov, d in cases:
        R = run(ov, d)
        sa, sd = rounds(R)
        print(f"  {name:48s} {f2([yr(R, net_rev, k) for k in (1, 2, 3)])} | {yr(R, net_rev, 6):5.1f} | {sa:.2f} + {sd:.1f}")
