"""Build the Tier 2/3 appliance after-sales market-intelligence datasets and dashboard.

    python3 build_market_intel.py

Reads the research agents' raw files in raw/ (geo, osm, retail, competitors, demand),
runs the bottom-up demand model (LOW/BASE/HIGH), joins supply and competition,
scores cities and states, writes data/*.csv and dashboard/index.html.
Standard library only. Nothing here is fabricated: missing values stay blank/UNKNOWN.
"""
import csv, json, math, re, difflib, pathlib, collections, datetime

ROOT = pathlib.Path(__file__).parent
RAW, OUT, DASH = ROOT / "raw", ROOT / "data", ROOT / "dashboard"
OUT.mkdir(exist_ok=True); DASH.mkdir(exist_ok=True)
TODAY = datetime.date.today().isoformat()
SC = ("low", "base", "high")
CATS = ("AC", "Refrigerator", "Washing machine", "Water purifier")


def rd(p):
    p = RAW / p
    return list(csv.DictReader(open(p, encoding="utf-8"))) if p.exists() else []


def wr(name, rows, cols=None):
    cols = cols or (list(rows[0].keys()) if rows else [])
    with open(OUT / name, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=cols, extrasaction="ignore"); w.writeheader(); w.writerows(rows)
    return len(rows)


def fnum(x):
    try: return float(str(x).replace(",", ""))
    except Exception: return None


# ---------------------------------------------------------------- parameters
PAR = {}
for r in rd("demand/parameters.csv"):
    PAR[(r["parameter"], r["category"])] = {s: fnum(r[s]) for s in SC} | {"label": r["label"], "source": r["source"], "url": r["url"]}


def P(name, cat, s):
    return PAR[(name, cat)][s]


# ---------------------------------------------------------------- geography
cities_all = rd("geo/cities_raw.csv")
SB = {r["name_std"]: r for r in rd("geo/state_baseline.csv")}
units = [c for c in cities_all if c["count_unit"] == "1"]
for c in units:
    c["pop_2011"] = int(float(c["pop_2011"]))
    c["lat"], c["lon"] = fnum(c["lat"]), fnum(c["lon"])
    c["core"] = c["eligible_t2t3_core"] == "1"
    c["small"] = c["eligible_small_town"] == "1"
by_id = {c["city_id"]: c for c in units}

# ---------------------------------------------------------------- ownership (state NFHS-5 scaled to 2026 national level)
own = collections.defaultdict(dict)
for r in rd("demand/ownership_by_state.csv"):
    if r["label"] == "FACT" or (r["state"] != "India" and r["urban_rate"]):
        v = fnum(r["urban_rate"])
        if v is not None:
            own[r["state"]].setdefault(r["category"], v / 100)
NAT_NFHS = {"Refrigerator": own["India"]["refrigerator"], "Washing machine": own["India"]["washing machine"],
            "AC": own["India"]["air conditioner/cooler"], "Water purifier": 0.128}
NFHS_KEY = {"Refrigerator": "refrigerator", "Washing machine": "washing machine", "AC": "air conditioner/cooler", "Water purifier": "water purifier"}
NAT_PARAM = {"AC": "AC (AC only)", "Refrigerator": "Refrigerator", "Washing machine": "Washing machine", "Water purifier": "Water purifier (electric)"}
STATE_ALIAS = {"Delhi": "Delhi (NCT)"}


def own_rate(state, cat, s):
    st = own.get(STATE_ALIAS.get(state, state), {})
    base = st.get(NFHS_KEY[cat])
    src = "state NFHS-5"
    if base is None:
        base, src = NAT_NFHS[cat], "national NFHS-5 (no state row)"
    scaled = base * P("urban_ownership_rate_national", NAT_PARAM[cat], s) / NAT_NFHS[cat]
    return min(scaled, 0.95), src


# ---------------------------------------------------------------- demand model
BILL = {  # (job type, INR param name, category key)
    "AC": [("service", "routine_service_frequency", "AC", "inuse", "bill_routine_service", "AC"),
           ("gas refill", "refrigerant_refill_incidence", "AC", "oow", "bill_gas_refill", "AC"),
           ("repair", "repair_incidence_non_gas", "AC", "oow", "bill_repair_typical", "AC")],
    "Refrigerator": [("repair", "repair_incidence", "Refrigerator", "oow", "bill_repair_typical", "Refrigerator"),
                     ("service", "routine_service_frequency", "Refrigerator", "inuse", "bill_visit_or_inspection", "All")],
    "Washing machine": [("repair", "repair_incidence", "Washing machine", "oow", "bill_repair_typical", "Washing machine"),
                        ("service", "routine_service_frequency", "Washing machine", "inuse", "bill_visit_or_inspection", "All")],
    "Water purifier": [("service/filter", "routine_service_frequency", "Water purifier", "inuse", "bill_service_or_filter", "Water purifier"),
                       ("repair", "repair_incidence_non_filter", "Water purifier", "oow", "bill_service_or_filter", "Water purifier")],
}
OOW_CAT = {"AC": "AC", "Refrigerator": "Refrigerator", "Washing machine": "Washing machine", "Water purifier": "Water purifier"}


def households(c):
    sb = SB[c["state"]]
    g = fnum(sb["urban_growth_factor_2011_2026"]) or 1.0
    hh = fnum(sb["census2011_avg_urban_hh_size"]) or 4.5
    pop26 = c["pop_2011"] * g
    return pop26, pop26 / hh


est_rows = []
for c in units:
    pop26, hh = households(c)
    c["pop_2026_est"], c["hh_2026_est"] = round(pop26), round(hh)
    c["est"] = {}
    for s in SC:
        tot = {"installed": 0, "oow": 0, "jobs": 0, "value": 0}
        for cat in CATS:
            rate, src = own_rate(c["state"], cat, s)
            machines = hh * rate * P("tier23_ownership_vs_national_urban", "Index", s) * P("machines_per_owning_hh", cat, s)
            inuse = machines * P("share_still_in_use", "All", s)
            oow = inuse * P("share_out_of_comprehensive_warranty", OOW_CAT[cat], s)
            jobs = val = 0
            for _, fp, fc, basis, bp, bc in BILL[cat]:
                n = (inuse if basis == "inuse" else oow) * P(fp, fc, s)
                jobs += n; val += n * P(bp, bc, s)
            acc = P("channel_share_dealer_arranged", "AC", s)
            est_rows.append({"city_id": c["city_id"], "city": c["city"], "state": c["state"], "scenario": s.upper(), "category": cat,
                             "households_2026_est": round(hh), "ownership_rate": round(rate, 4), "ownership_source": src,
                             "installed_units": round(machines), "out_of_warranty_in_use": round(oow),
                             "annual_service_requests": round(jobs), "daily_requests_365": round(jobs / 365, 1),
                             "daily_requests_300_operating_days": round(jobs / 300, 1),
                             "annual_value_inr": round(val), "retailer_accessible_requests": round(jobs * acc),
                             "label": "DERIVED ESTIMATE"})
            c.setdefault("own_src", src)
            tot["installed"] += machines; tot["oow"] += oow; tot["jobs"] += jobs; tot["value"] += val
            c["est"].setdefault(s, {})[cat] = {"installed": machines, "oow": oow, "jobs": jobs, "value": val}
        tot["accessible_jobs"] = tot["jobs"] * P("channel_share_dealer_arranged", "AC", s)
        tot["accessible_value"] = tot["value"] * P("channel_share_dealer_arranged", "AC", s)
        c["est"][s]["total"] = tot

# ---------------------------------------------------------------- city name matching (retail, competitor claims)
def norm(x):
    x = x.lower()
    x = re.sub(r"\(.*?\)|u\.a\.|\bua\b|m\.corp\.|\bcorporation\b|\bcity\b|\bcantonment\b|\bm\.?cl\.?\b", " ", x)
    return re.sub(r"[^a-z]", "", x)


ALIAS = {"hanamkonda": "warangal", "kazipet": "warangal", "bellary": "ballari", "belgavi": "belgaum", "belagavi": "belgaum",
         "mysuru": "mysore", "hubballi": "hublidharwad", "hubli": "hublidharwad", "dharwad": "hublidharwad", "broadwayhubli": "hublidharwad",
         "chikkamangalur": "chikmagalur", "chikkamagaluru": "chikmagalur", "vizag": "visakhapatnam", "trichy": "tiruchirappalli",
         "tiruchirapalli": "tiruchirappalli", "calicut": "kozhikode", "trivandrum": "thiruvananthapuram", "cochin": "kochi",
         "ernakulam": "kochi", "gurugram": "gurgaon", "newdelhi": "delhi", "nandyala": "nandyal", "jagityala": "jagtial",
         "bhuvanagiri": "bhongir", "tumakuru": "tumkur", "shivamogga": "shimoga", "mangaluru": "mangalore", "davangere": "davanagere",
         "bengaluru": "bangalore", "pondicherry": "puducherry", "rajamahendravaram": "rajahmundry", "kalaburagi": "gulbarga",
         "vijayapura": "bijapur", "ballari": "bellary", "prayagraj": "allahabad", "aurangabad": "aurangabad", "chhatrapatisambhajinagar": "aurangabad",
         "tuticorin": "thoothukkudi", "thoothukudi": "thoothukkudi", "tanjore": "thanjavur", "burdwan": "barddhaman", "singanallur": "coimbatore", "gandhipuramcoimbatore": "coimbatore", "trichyroadcoimbatore": "coimbatore", "sundarapuram": "coimbatore", "palayamkottai": "tirunelveli", "maduraimain": "madurai", "katpadi": "vellore", "tilakwadibelagavi": "belgaum", "hubligokulroad": "hublidharwad", "kuvempunagar": "mysore", "jaipyr": "jaipur", "panjim": "panaji", "bhilai": "durgbhilainagar", "kakkanad": "kochi", "edappally": "kochi", "kadavanthara": "kochi", "pattom": "thiruvananthapuram", "kazhakoottam": "thiruvananthapuram", "kanchipuram": "kancheepuram", "nellore": "nellore", "kurnool": "kurnool",
         "ongole": "ongole", "vadodara": "vadodara", "baroda": "vadodara", "mumbai": "greatermumbai", "kolkata": "kolkata", "chennai": "chennai"}
idx = collections.defaultdict(dict)  # state -> norm name -> count-unit city_id
for c in cities_all:
    key = norm(c["city"]); cid = c["city_id"] if c["count_unit"] == "1" else (c["parent_ua_id"] or c["city_id"])
    idx[c["state"]].setdefault(key, cid)
    idx[c["state"]].setdefault(norm(c["unit_name_census"]), cid)


def match_city(name, state):
    state = re.sub(r"\s*\(.*\)", "", state or "").strip()
    if state in ("Delhi",): state = "NCT of Delhi" if "NCT of Delhi" in idx else state
    k = norm(name); k = ALIAS.get(k, k)
    pools = [idx[state]] if state in idx else list(idx.values())
    for pool in pools:
        if k in pool: return pool[k]
    for pool in pools:
        m = difflib.get_close_matches(k, pool.keys(), n=1, cutoff=0.86)
        if m: return pool[m[0]]
    return None


# ---------------------------------------------------------------- retail
retailers = rd("retail/retailers.csv")
rcc = rd("retail/retailer_city_counts.csv")
outlets = rd("retail/retailer_outlets.csv")
city_chain = collections.defaultdict(lambda: collections.Counter())
unmatched_retail = collections.Counter()
state_level = collections.Counter()
for r in rcc:
    if r["city"].upper().startswith("ALL"):
        r["matched_city_id"] = "STATE-LEVEL"; state_level[re.sub(r"\s*\(.*\)", "", r["state"])] += int(fnum(re.sub(r"[^0-9.]", "", r["outlet_count"].split(" ")[0]) or 0) or 0); continue
    cid = match_city(r["city"].lstrip("- ").strip(), r["state"])
    n = int(fnum(r["outlet_count"]) or 0)
    r["matched_city_id"] = cid or ""
    if cid and cid in by_id:
        city_chain[cid][r["retailer"]] += n
    else:
        unmatched_retail[re.sub(r"\s*\(.*\)", "", r["state"])] += n
for o in outlets:
    o["matched_city_id"] = match_city(o["city"], o["state"]) or ""
for c in units:
    cc = city_chain.get(c["city_id"], {})
    c["chain_outlets"] = sum(cc.values()); c["chains"] = sorted(cc)

# ---------------------------------------------------------------- OSM supply
osm = rd("osm/osm_points.csv")
RET_CLS = {"retail_appliance", "retail_electronics_general"}
REP_CLS = {"repair_appliance", "repair_electronics_general", "authorised_service_centre"}
geo_units = [c for c in units if c["lat"] is not None]


def hav(a, b, c, d):
    p = math.pi / 180
    x = math.sin((c - a) * p / 2) ** 2 + math.cos(a * p) * math.cos(c * p) * math.sin((d - b) * p / 2) ** 2
    return 12742 * math.asin(math.sqrt(x))


grid = collections.defaultdict(list)
for c in geo_units:
    grid[(int(c["lat"] * 4), int(c["lon"] * 4))].append(c)
for c in units:
    c["osm"] = collections.Counter()
osm_kept = []
for p in osm:
    la, lo = fnum(p.get("lat")), fnum(p.get("lon"))
    if la is None or lo is None: continue
    best, bd = None, 1e9
    gi, gj = int(la * 4), int(lo * 4)
    for di in (-1, 0, 1):
        for dj in (-1, 0, 1):
            for c in grid.get((gi + di, gj + dj), []):
                d = hav(la, lo, c["lat"], c["lon"])
                if d < bd: best, bd = c, d
    radius = 2 + 2.5 * math.sqrt(best["pop_2011"] / 1e5) if best else 0
    p["city_id"] = best["city_id"] if best and bd <= radius else ""
    p["dist_km"] = round(bd, 2) if best else ""
    if p["city_id"]:
        by_id[p["city_id"]]["osm"][p["class"]] += 1
    osm_kept.append(p)
for c in units:
    o = c["osm"]
    c["osm_retail"] = sum(o[k] for k in RET_CLS); c["osm_retail_appliance"] = o["retail_appliance"]
    c["osm_repair"] = sum(o[k] for k in REP_CLS); c["osm_repair_appliance"] = o["repair_appliance"]
    c["osm_asc"] = o["authorised_service_centre"]; c["osm_electrician"] = o["electrician"]

# ---------------------------------------------------------------- competitors
claims = rd("competitors/competitor_city_claims.csv")
comp = collections.defaultdict(collections.Counter)
comp_names = collections.defaultdict(list)
for r in claims:
    cid = match_city(r["city"], r["state"])
    r["city_id"] = cid or ""
    if cid:
        comp[cid][r["status"]] += 1
        if r["status"] in ("VERIFIED ACTIVE", "PUBLICLY CLAIMED"):
            comp_names[cid].append(f'{r["company"]} ({"verified" if r["status"]=="VERIFIED ACTIVE" else "claimed"})')
for c in units:
    k = comp.get(c["city_id"])
    c["comp_checked"] = bool(k)
    c["comp_verified"] = k["VERIFIED ACTIVE"] if k else None
    c["comp_claimed"] = k["PUBLICLY CLAIMED"] if k else None
    c["comp_list"] = "; ".join(comp_names.get(c["city_id"], []))

# ---------------------------------------------------------------- scoring
core = [c for c in units if c["core"]]


def pct_rank(vals):
    srt = sorted(vals)
    n = len(srt)
    return lambda v: (sum(1 for x in srt if x < v) + 0.5 * sum(1 for x in srt if x == v)) / n if n else 0


B = lambda c: c["est"]["base"]["total"]
r_value = pct_rank([B(c)["value"] for c in core])
r_acc = pct_rank([B(c)["accessible_value"] for c in core])
r_ret = pct_rank([c["chain_outlets"] + 0.5 * c["osm_retail_appliance"] for c in core])
r_rep = pct_rank([c["osm_repair"] for c in core])
tick = lambda c: B(c)["value"] / B(c)["jobs"] if B(c)["jobs"] else 0
r_tick = pct_rank([tick(c) for c in core])
dens = lambda c: c["osm_repair"] / max(c["hh_2026_est"], 1) * 1e5
r_dens = pct_rank([dens(c) for c in core])
maxcomp = max([(c["comp_verified"] or 0) + (c["comp_claimed"] or 0) for c in core] + [1])

WEIGHTS = {"default": (25, 25, 20, 15, 15), "demand-heavy": (15, 40, 20, 10, 15),
           "supply-heavy": (20, 20, 35, 10, 15), "equal": (20, 20, 20, 20, 20)}

for c in core + [c for c in units if not c["core"]]:
    e = B(c)
    c["conf_pts"] = (c["chain_outlets"] > 0) + (c["osm_retail"] + c["osm_repair"] >= 5) + c["comp_checked"] + (c["own_src"] == "state NFHS-5")
    c["confidence"] = "HIGH" if c["conf_pts"] >= 3 and c["chain_outlets"] > 0 else ("MEDIUM" if c["conf_pts"] >= 2 else "LOW")
    if not c["core"]:
        continue
    f_ret = r_ret(c["chain_outlets"] + 0.5 * c["osm_retail_appliance"]) if (c["chain_outlets"] + c["osm_retail_appliance"]) else 0.0
    f_dem = r_acc(e["accessible_value"])
    f_ful = r_rep(c["osm_repair"]) if c["osm_repair"] else 0.0
    if c["comp_checked"] and c["osm_repair"] >= 3:
        f_unmet = 0.5 * (1 - ((c["comp_verified"] or 0) + (c["comp_claimed"] or 0)) / maxcomp) + 0.5 * (1 - r_dens(dens(c)))
    elif c["comp_checked"]:
        f_unmet = 0.5 * (1 - ((c["comp_verified"] or 0) + (c["comp_claimed"] or 0)) / maxcomp) * 0.6
    else:
        f_unmet = 0.15  # no evidence either way: not rewarded
    f_eco = r_tick(tick(c))
    c["factors"] = dict(retailer_access=f_ret, monetizable_demand=f_dem, fulfilment=f_ful, unmet_demand=f_unmet, unit_economics=f_eco)
    adj = {"HIGH": 1.0, "MEDIUM": 0.85, "LOW": 0.7}[c["confidence"]]
    for wn, w in WEIGHTS.items():
        raw = sum(wi * fi for wi, fi in zip(w, c["factors"].values()))
        c[f"entry_{wn}"] = round(raw * adj, 1)
    c["entry_raw"] = round(sum(wi * fi for wi, fi in zip(WEIGHTS["default"], c["factors"].values())), 1)
    c["market_score"] = round(100 * (0.7 * r_value(e["value"]) + 0.3 * r_ret(c["chain_outlets"] + 0.5 * c["osm_retail_appliance"])), 1)
    c["opp_per_100k_hh"] = round(e["value"] / max(c["hh_2026_est"], 1) * 1e5)

ranked = sorted(core, key=lambda c: -c["entry_default"])
for i, c in enumerate(ranked): c["rank_entry"] = i + 1
for i, c in enumerate(sorted(core, key=lambda c: -c["market_score"])): c["rank_market"] = i + 1
for wn in WEIGHTS:
    for i, c in enumerate(sorted(core, key=lambda c: -c[f"entry_{wn}"])): c[f"rank_{wn}"] = i + 1
n = len(core)
for c in core:
    sat = c["comp_checked"] and ((c["comp_verified"] or 0) >= 3 or (c["comp_verified"] or 0) + (c["comp_claimed"] or 0) >= 8)
    if c["confidence"] == "LOW" and c["chain_outlets"] == 0:
        cl = "INSUFFICIENT DATA"
    elif sat:
        cl = "COMPETITIVE / SATURATED"
    elif c["rank_entry"] <= 0.15 * n and c["confidence"] != "LOW" and c["chain_outlets"] >= 2 and c["osm_repair"] >= 3:
        cl = "HIGH OPPORTUNITY"
    elif c["rank_entry"] <= 0.4 * n:
        cl = "PROMISING BUT UNVERIFIED"
    else:
        cl = "LOW COMMERCIAL ATTRACTIVENESS"
    c["class"] = cl
    adv, risk = [], []
    if c["chain_outlets"]: adv.append(f'{c["chain_outlets"]} verified chain outlets ({", ".join(x.split(" (")[0] for x in c["chains"][:3])})')
    if c["osm_repair"]: adv.append(f'{c["osm_repair"]} mapped repair/service points (OSM)')
    adv.append(f'~₹{B(c)["value"]/1e7:.1f} Cr/yr est. repair+service spend (BASE)')
    if not c["chain_outlets"]: risk.append("no verified chain outlets found")
    if c["osm_repair"] < 3: risk.append("repair supply not verifiable from open data")
    if c["comp_checked"] and (c["comp_verified"] or 0): risk.append(f'{c["comp_verified"]} competitors verified active')
    if not c["comp_checked"]: risk.append("competitor presence not checked")
    c["advantages"], c["risks"] = "; ".join(adv), "; ".join(risk)

# ---------------------------------------------------------------- states
states = []
for st, sb in SB.items():
    cs = [c for c in core if c["state"] == st]
    allc = [c for c in units if c["state"] == st]
    agg = lambda s, k: sum(c["est"][s]["total"][k] for c in cs)
    hh = sum(c["hh_2026_est"] for c in cs)
    chk = [c for c in cs if c["comp_checked"]]
    top5 = sorted([c["entry_default"] for c in cs], reverse=True)[:5]
    row = {"state": st, "eligible_cities": len(cs), "tier2_cities": sum(c["tier_pop"] == "Tier 2" for c in cs),
           "tier3_cities": sum(c["tier_pop"] == "Tier 3" for c in cs), "small_towns_50k_100k": sum(c["small"] for c in allc),
           "eligible_pop_2011": sum(c["pop_2011"] for c in cs), "eligible_pop_2026_est": sum(c["pop_2026_est"] for c in cs),
           "eligible_households_2026_est": hh,
           "verified_chain_outlets_in_eligible_cities": sum(c["chain_outlets"] for c in cs),
           "chain_outlets_unmatched_or_smaller_towns": unmatched_retail.get(st, 0),
           "chain_outlets_state_level_only": state_level.get(st, 0),
           "regional_chains_present": len({x for c in cs for x in c["chains"]}),
           "osm_retail_points": sum(c["osm_retail"] for c in cs), "osm_appliance_retail_points": sum(c["osm_retail_appliance"] for c in cs),
           "osm_repair_points_listed": sum(c["osm_repair"] for c in cs), "osm_authorised_service_centres": sum(c["osm_asc"] for c in cs),
           "verified_operating_repair_agencies": "UNKNOWN (no verification run)",
           "retail_outlets_per_100k_hh": round(sum(c["chain_outlets"] for c in cs) / hh * 1e5, 2) if hh else None,
           "installed_base_base": round(agg("base", "installed")), "oow_installed_base_low": round(agg("low", "oow")),
           "oow_installed_base_base": round(agg("base", "oow")), "oow_installed_base_high": round(agg("high", "oow")),
           "annual_repair_requests_low": round(agg("low", "jobs")), "annual_repair_requests_base": round(agg("base", "jobs")),
           "annual_repair_requests_high": round(agg("high", "jobs")), "annual_value_inr_cr_base": round(agg("base", "value") / 1e7, 1),
           "retailer_accessible_value_inr_cr_base": round(agg("base", "accessible_value") / 1e7, 1),
           "cities_competitor_checked": len(chk),
           "avg_competitors_present_in_checked": round(sum((c["comp_verified"] or 0) + (c["comp_claimed"] or 0) for c in chk) / len(chk), 1) if chk else None,
           "entry_score_top5_avg": round(sum(top5) / len(top5), 1) if top5 else 0,
           "ownership_source": cs[0]["own_src"] if cs else "",
           "high_conf_cities": sum(c["confidence"] == "HIGH" for c in cs), "med_conf_cities": sum(c["confidence"] == "MEDIUM" for c in cs),
           "low_conf_cities": sum(c["confidence"] == "LOW" for c in cs)}
    row["data_completeness"] = round((row["high_conf_cities"] + 0.5 * row["med_conf_cities"]) / len(cs), 2) if cs else 0
    row["competitive_intensity"] = ("UNKNOWN" if not chk else "HIGH" if row["avg_competitors_present_in_checked"] >= 6 else "MEDIUM" if row["avg_competitors_present_in_checked"] >= 3 else "LOW")
    states.append(row)
mx = max(s["annual_value_inr_cr_base"] for s in states) or 1
for s in states:
    s["market_size_score"] = round(100 * math.sqrt(s["annual_value_inr_cr_base"] / mx), 1)
    s["startup_entry_score"] = round(s["entry_score_top5_avg"] * (0.7 + 0.3 * s["data_completeness"]), 1)
for i, s in enumerate(sorted(states, key=lambda s: -s["annual_value_inr_cr_base"])): s["rank_market"] = i + 1
for i, s in enumerate(sorted(states, key=lambda s: -s["startup_entry_score"])): s["rank_entry"] = i + 1
# alternative tier definition: HRA Y/Z cities >=100k, non-metro
alt = collections.Counter(c["state"] for c in units if c["tier_hra"].startswith(("Y", "Z")) and c["pop_2011"] >= 100000 and c["metro_satellite"] != "1")
for i, (st, k) in enumerate(alt.most_common()):
    for s in states:
        if s["state"] == st: s["eligible_cities_hra_def"] = k; s["rank_count_hra_def"] = i + 1
pr = sorted(states, key=lambda s: -s["eligible_cities"])
for i, s in enumerate(pr): s["rank_count_pop_def"] = i + 1

# ---------------------------------------------------------------- economics (Python mirror of the dashboard simulator)
tot = lambda s, k: sum(c["est"][s]["total"][k] for c in core)
AVG_BILL = {s: round(tot(s, "value") / tot(s, "jobs")) for s in SC}
ECON = {
    "retailers": (20, 50, 100), "referrals_per_retailer_month": (10, 30, 60), "referral_to_booking": (0.30, 0.50, 0.70),
    "booking_to_paid": (0.70, 0.85, 0.92), "avg_bill": (AVG_BILL["low"], AVG_BILL["base"], AVG_BILL["high"]),
    "parts_share_of_bill": (0.30, 0.40, 0.45), "parts_cost_share": (0.95, 0.88, 0.80), "agency_payout_share_of_labour": (0.85, 0.75, 0.65),
    "retailer_commission_share": (0.12, 0.08, 0.05), "booking_fee": (0, 49, 99), "support_per_job": (55, 43, 35),
    "travel_coord_per_job": (30, 20, 10), "payment_fee_share": (0.02, 0.01, 0.005), "refund_rework_share": (0.05, 0.03, 0.02),
    "fixed_costs_month": (1200000, 800000, 600000)}


def econ(i):
    g = {k: v[i] for k, v in ECON.items()}
    jobs = g["retailers"] * g["referrals_per_retailer_month"] * g["referral_to_booking"] * g["booking_to_paid"]
    bill = g["avg_bill"]; parts = bill * g["parts_share_of_bill"]; labour = bill - parts
    rev_job = labour * (1 - g["agency_payout_share_of_labour"]) + parts * (1 - g["parts_cost_share"]) + g["booking_fee"]
    var_job = bill * (g["retailer_commission_share"] + g["payment_fee_share"] + g["refund_rework_share"]) + g["support_per_job"] + g["travel_coord_per_job"]
    contrib = rev_job - var_job
    be = g["fixed_costs_month"] / contrib if contrib > 0 else None
    per_ret = g["referrals_per_retailer_month"] * g["referral_to_booking"] * g["booking_to_paid"]
    return {"scenario": SC[i].upper(), "leads": round(g["retailers"] * g["referrals_per_retailer_month"]), "paid_jobs_month": round(jobs),
            "gtv_month": round(jobs * (bill + g["booking_fee"])), "revenue_per_job": round(rev_job), "variable_cost_per_job": round(var_job),
            "contribution_per_job": round(contrib), "contribution_margin_on_revenue": round(contrib / rev_job, 3) if rev_job else None,
            "monthly_contribution": round(jobs * contrib), "fixed_costs_month": g["fixed_costs_month"],
            "operating_profit_month": round(jobs * contrib - g["fixed_costs_month"]),
            "break_even_jobs_month": round(be) if be else "never (negative contribution)",
            "retailers_needed": round(be / per_ret) if be else "never"}


ECON_OUT = [econ(i) for i in range(3)]

# ---------------------------------------------------------------- write CSVs
city_cols = ["city_id", "city", "state", "district", "unit_type", "tier_pop", "tier_hra", "metro_satellite", "pop_2011", "pop_2026_est", "hh_2026_est",
             "lat", "lon", "chain_outlets", "chains_present", "osm_retail", "osm_retail_appliance", "osm_repair", "osm_repair_appliance", "osm_asc",
             "comp_checked", "comp_verified", "comp_claimed", "competitors_present", "jobs_low", "jobs_base", "jobs_high", "value_cr_base",
             "accessible_value_cr_base", "confidence", "class"]
city_rows = []
for c in units:
    if not (c["core"] or c["small"]): continue
    e = c["est"]
    city_rows.append({**{k: c.get(k) for k in city_cols}, "chains_present": "; ".join(c["chains"]), "competitors_present": c["comp_list"],
                      "jobs_low": round(e["low"]["total"]["jobs"]), "jobs_base": round(e["base"]["total"]["jobs"]), "jobs_high": round(e["high"]["total"]["jobs"]),
                      "value_cr_base": round(e["base"]["total"]["value"] / 1e7, 2), "accessible_value_cr_base": round(e["base"]["total"]["accessible_value"] / 1e7, 2),
                      "segment": "Tier 2/3 core" if c["core"] else "small town 50k-100k", "class": c.get("class", "small town (not scored)")})
counts = {}
counts["cities.csv"] = wr("cities.csv", city_rows, city_cols[:-1] + ["segment", "class"])
counts["states.csv"] = wr("states.csv", states)
counts["retailers.csv"] = wr("retailers.csv", retailers)
counts["retailer_outlets.csv"] = wr("retailer_outlets.csv", outlets)
rep = [p for p in osm_kept if p["class"] in REP_CLS | {"electrician"}]
for p in rep:
    p["verification_status"] = "LISTED (OSM) - NOT VERIFIED"; p["technician_headcount"] = "UNKNOWN"
counts["repair_agencies.csv"] = wr("repair_agencies.csv", rep, ["osm_type", "osm_id", "name", "class", "lat", "lon", "addr_city", "addr_postcode", "addr_state",
                                                                 "brand", "operator", "city_id", "dist_km", "verification_status", "technician_headcount", "osm_url", "retrieved"])
counts["competitor_coverage.csv"] = wr("competitor_coverage.csv", claims)
counts["appliance_estimates.csv"] = wr("appliance_estimates.csv", est_rows)
score_cols = ["rank_entry", "rank_market", "city_id", "city", "state", "tier_pop", "entry_default", "entry_raw", "market_score", "opp_per_100k_hh", "confidence",
              "class", "retailer_access", "monetizable_demand", "fulfilment", "unmet_demand", "unit_economics", "entry_demand-heavy", "rank_demand-heavy",
              "entry_supply-heavy", "rank_supply-heavy", "entry_equal", "rank_equal", "advantages", "risks"]
counts["opportunity_scores.csv"] = wr("opportunity_scores.csv", [{**c, **{k: round(v, 3) for k, v in c["factors"].items()}} for c in ranked], score_cols)
src = []
for f, kind in [("geo/geo_sources.csv", "geo"), ("demand/demand_sources.csv", "demand")]:
    for r in rd(f): src.append({**r, "module": kind})
for r in retailers:
    for u in re.split(r"\s*;\s*|\s+\|\s+", r.get("source_urls", "")):
        if u.startswith("http"): src.append({"source": r["retailer"], "url": u, "retrieval_date": r.get("retrieved", ""), "module": "retail"})
for r in rd("competitors/competitors.csv"):
    for u in re.split(r"\s*;\s*", r.get("source_urls", "")):
        if u.startswith("http"): src.append({"source": r["company"], "url": u, "retrieval_date": r.get("retrieved", ""), "module": "competitors"})
src.append({"source": "OpenStreetMap contributors via Overpass API (ODbL)", "url": "https://www.openstreetmap.org/copyright", "retrieval_date": TODAY, "module": "osm"})
counts["research_sources.csv"] = wr("research_sources.csv", src, ["module", "source", "url", "publication_date", "retrieval_date", "coverage", "definition", "confidence"])
dq = []
for c in units:
    if not (c["core"] or c["small"]): continue
    gaps = []
    if c["lat"] is None: gaps.append("no coordinates")
    if not c["chain_outlets"]: gaps.append("no verified chain outlets")
    if c["osm_retail"] + c["osm_repair"] < 5: gaps.append("sparse OSM listings")
    if not c["comp_checked"]: gaps.append("competitors not checked")
    if c["own_src"] != "state NFHS-5": gaps.append("national ownership proxy")
    gaps.append("population is Census 2011 x state urban growth (DERIVED)")
    dq.append({"city_id": c["city_id"], "city": c["city"], "state": c["state"], "confidence": c["confidence"], "confidence_points": c["conf_pts"], "gaps": "; ".join(gaps)})
counts["data_quality_report.csv"] = wr("data_quality_report.csv", dq)

# ---------------------------------------------------------------- dashboard payload
def r1(x): return round(x, 1) if isinstance(x, float) else x


DATA = {
    "built": TODAY,
    "params": {f"{k[0]}|{k[1]}": {s: v[s] for s in SC} | {"label": v["label"]} for k, v in PAR.items()},
    "econ": ECON, "econ_out": ECON_OUT, "weights": WEIGHTS,
    "cities": [{"id": c["city_id"], "n": c["city"], "s": c["state"], "d": c["district"], "t": c["tier_pop"], "h": c["tier_hra"],
                "la": c["lat"], "lo": c["lon"], "p11": c["pop_2011"], "p26": c["pop_2026_est"], "hh": c["hh_2026_est"],
                "co": c["chain_outlets"], "ch": c["chains"], "or": c["osm_retail"], "ora": c["osm_retail_appliance"], "op": c["osm_repair"],
                "opa": c["osm_repair_appliance"], "asc": c["osm_asc"], "cc": c["comp_checked"], "cv": c["comp_verified"], "cl": c["comp_claimed"],
                "cn": c["comp_list"], "core": c["core"],
                "e": {s: {cat: {k: round(v) for k, v in c["est"][s][cat].items()} for cat in CATS + ("total",)} for s in SC},
                "conf": c["confidence"], "cls": c.get("class", "small town"), "es": c.get("entry_default"), "ms": c.get("market_score"),
                "re": c.get("rank_entry"), "rm": c.get("rank_market"), "f": {k: round(v, 3) for k, v in c.get("factors", {}).items()},
                "adv": c.get("advantages", ""), "risk": c.get("risks", ""), "rk": {w: c.get(f"rank_{w}") for w in WEIGHTS}}
               for c in units if (c["core"] or c["small"])],
    "states": states,
    "retailers": retailers,
    "outlets": [{k: o[k] for k in ("retailer", "store_name", "address", "city", "state", "pincode", "source_url", "matched_city_id")} for o in outlets],
    "osm": [[r1(fnum(p["lat"])), r1(fnum(p["lon"])) if False else fnum(p["lon"]), p["name"], p["class"], p["city_id"], p["osm_url"]] for p in osm_kept
            if p["class"] in RET_CLS | REP_CLS],
    "competitors": rd("competitors/competitors.csv"),
    "claims": claims,
    "counts": counts,
}
for p in DATA["osm"]:
    p[0], p[1] = round(p[0], 5), round(p[1], 5)
geo = json.load(open(RAW / "geo/india_states.geojson"))
for f in geo["features"]:
    def rnd(x):
        return [rnd(y) for y in x] if isinstance(x[0], list) else [round(x[0], 2), round(x[1], 2)]
    g = f["geometry"]; g["coordinates"] = rnd(g["coordinates"])
    f["properties"] = {"name": f["properties"]["name_std"]}
DATA["geo"] = geo

tpl = (ROOT / "dashboard_template.html").read_text(encoding="utf-8")
html = tpl.replace("/*__DATA__*/", "window.D=" + json.dumps(DATA, ensure_ascii=False, separators=(",", ":")) + ";")
(DASH / "index.html").write_text(html, encoding="utf-8")

# ---------------------------------------------------------------- console summary (used in REPORT.md)
json.dump({"counts": counts, "econ": ECON_OUT, "avg_bill": AVG_BILL,
           "national": {s: {k: round(tot(s, k)) for k in ("installed", "oow", "jobs", "value", "accessible_value")} for s in SC},
           "core_cities": len(core), "osm_points": len(osm), "osm_assigned": sum(1 for p in osm_kept if p["city_id"]),
           "retail_rows_matched": sum(1 for r in rcc if r["matched_city_id"] in by_id), "retail_rows": len(rcc),
           "class_counts": collections.Counter(c["class"] for c in core),
           "conf_counts": collections.Counter(c["confidence"] for c in core),
           "top_entry": [(c["city"], c["state"], c["entry_default"], c["confidence"], c["class"]) for c in ranked[:25]],
           "top_market": [(c["city"], c["state"], c["market_score"]) for c in sorted(core, key=lambda c: -c["market_score"])[:25]],
           "state_entry": [(s["state"], s["startup_entry_score"], s["data_completeness"]) for s in sorted(states, key=lambda s: -s["startup_entry_score"])[:12]],
           "state_market": [(s["state"], s["annual_value_inr_cr_base"]) for s in sorted(states, key=lambda s: -s["annual_value_inr_cr_base"])[:12]],
           "unmatched_retail_by_state": unmatched_retail, "state_level": state_level},
          open(OUT / "_summary.json", "w"), indent=1, default=str)
print(json.dumps(counts), "| dashboard", round((DASH / "index.html").stat().st_size / 1e6, 2), "MB")
