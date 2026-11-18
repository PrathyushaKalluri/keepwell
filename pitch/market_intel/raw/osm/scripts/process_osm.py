#!/usr/bin/env python3
"""Turn raw Overpass JSON (../overpass_json/) into osm_points.csv, osm_place_cities.csv and stats.json.
Standard library only. Classification rules are applied in order; the first match wins."""
import csv, glob, json, math, os, re
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.dirname(HERE)
RAW = os.path.join(BASE, "overpass_json")
RETRIEVED = "2026-11-18"

I = re.IGNORECASE
MAJOR = re.compile(r"applian|refrigerat|fridge|freez|washing|air ?-?condition|\ba\.?/?c\.?\b|aircon|hvac|"
                   r"cooling|cooler|chiller|water purif|purifier|\bro\b|r\.o\.|aquaguard|kent ro|geyser|"
                   r"water heater|micro ?wave|chimney|white goods|home needs", I)
ELEC = re.compile(r"electronic|\btv\b|t\.v\.|television|radio|audio|sound|video|led tv|electric|"
                  r"digital|home theat", I)
REPAIRWORD = re.compile(r"repair|servic|service cent|maintenance|mechanic|technician|works?\b|solutions", I)
SERVICE_CENTRE = re.compile(r"servic|customer care|care cent|authori[sz]ed|\bASC\b|after ?sales", I)
MOBCOMP = re.compile(r"mobile|cell ?phone|\bphones?\b|smart ?phone|iphone|\bapple\b|computer|laptop|"
                     r"\bpc\b|infotech|\bit (solutions|services)\b|printer|cartridge|tablet|\bsim\b|"
                     r"recharge|\bmi (store|home)\b|xiaomi|\bvivo\b|\boppo\b|realme|oneplus|poorvika|"
                     r"sangeetha|\bbig c\b|lot mobiles|\bhp world\b|\bdell\b|lenovo|\basus\b|\bacer\b|"
                     r"mobiles?\b|gadget", I)
BROAD_KEEP = re.compile(r"electronic|electrical|electricals|\btv\b|applian|home|furnitur", I)

APPL_BRANDS = ["lg", "samsung", "voltas", "whirlpool", "godrej", "haier", "ifb", "bosch", "siemens",
               "panasonic", "daikin", "blue star", "bluestar", "hitachi", "carrier", "lloyd", "kent",
               "aquaguard", "eureka forbes", "livpure", "pureit", "onida", "videocon", "kelvinator",
               "o general", "o'general", "mitsubishi", "toshiba", "sharp", "havells", "crompton",
               "v-guard", "vguard", "usha", "ao smith", "a.o. smith", "racold", "electrolux", "tcl",
               "hisense", "midea", "bpl", "sony", "philips", "bajaj", "symphony", "kenstar",
               "preethi", "prestige", "butterfly", "faber", "elica", "glen", "hindware"]
BRAND_RE = re.compile(r"\b(" + "|".join(re.escape(b) for b in APPL_BRANDS) + r")\b", I)
# Brand-exclusive retail (not service): brands whose own stores sell major appliances
APPL_RETAIL_BRANDS = re.compile(r"\b(lg|samsung|voltas|whirlpool|godrej|haier|ifb|bosch|panasonic|daikin|"
                                r"blue ?star|hitachi|carrier|lloyd|kent|aquaguard|eureka forbes|livpure|"
                                r"onida|videocon|kelvinator|o ?general|mitsubishi|toshiba|electrolux)\b", I)

CHAINS = [  # (canonical name, regex on name/brand/operator)
    ("Croma", r"\bcroma\b"), ("Reliance Digital", r"reliance (digital|resq)|\bmy jio store\b|reliance digital"),
    ("Vijay Sales", r"vijay sales"), ("Bajaj Electronics", r"bajaj electronics"),
    ("Lotus Electronics", r"lotus electronics"), ("Pai International", r"\bpai (international|electronics)\b"),
    ("Girias", r"girias"), ("Viveks", r"vivek'?s\b"), ("Vasanth & Co", r"vasanth ?(&|and) ?co"),
    ("Kohinoor", r"kohinoor (electronics|televideo)"), ("Great Eastern", r"great eastern"),
    ("Ezone", r"\bezone\b"), ("Sargam", r"sargam electronics"), ("Pittappillil", r"pittappillil"),
    ("Nandilath G-Mart", r"nandilath"), ("Oxygen", r"\boxygen (digital|the digital)"),
    ("Harini", r"harini"), ("Sathya", r"\bsathya (agencies|digital|showroom)"),
    ("Aditya Vision", r"aditya vision"), ("Jumbo Electronics", r"jumbo electronics"),
    ("Sony Center", r"sony (cent|world|exclusive)"), ("Samsung SmartPlaza", r"samsung (smart ?plaza|smart ?cafe|experience|plaza)"),
    ("LG Brand Shop", r"\blg (best ?shop|brand ?shop|showroom|exclusive)"),
    ("Videotex", r"videotex"), ("Ponnusamy", r"ponnusamy"), ("Next Retail", r"\bnext (retail|store)\b"),
    ("Tata Croma", r"infiniti retail"), ("Mahajan Electronics", r"mahajan electronics"),
    ("Value Plus", r"value plus"), ("Sales India", r"sales india"), ("Gem Electronics", r"\bgem electronics"),
]
CHAINS = [(n, re.compile(r, I)) for n, r in CHAINS]
MOBILE_CHAINS = re.compile(r"poorvika|sangeetha|\bbig c\b|lot mobiles|\bcelekt\b|happi mobiles|"
                           r"\bmi (store|home)\b|xiaomi|\bvivo\b|\boppo\b|realme|oneplus|apple|imagine|"
                           r"\bunicorn\b|aptronix|\bhp world\b|\bdell\b|lenovo|\basus\b|\bacer\b", I)

KEEP_TAG = re.compile(r"^(addr:.*|phone|contact:phone|contact:mobile|mobile|website|contact:website|"
                      r"opening_hours|repair(:.*)?|service:.*|office|amenity|name:en)$")


def chain_of(text):
    for n, rx in CHAINS:
        if rx.search(text):
            return n
    return ""


def has_repair_tags(t):
    for k, v in t.items():
        if (k == "repair" or k.startswith("repair:")) and v not in ("no",):
            return True
    return False


def repair_tag_text(t):
    return " ".join(f"{k}={v}" for k, v in t.items() if k.startswith("repair") or k.startswith("service:"))


def classify(t):
    """Return (class, rule) or (None, reason) for elements dropped from the file."""
    name = t.get("name", "") or t.get("name:en", "")
    brand = " ".join(t.get(k, "") for k in ("brand", "operator"))
    nb = f"{name} {brand}"
    shop, craft, office = t.get("shop", ""), t.get("craft", ""), t.get("office", "")
    rtxt = repair_tag_text(t)
    allt = f"{nb} {rtxt}"
    is_repair = (craft in ("electronics_repair", "hvac") or shop == "repair" or has_repair_tags(t)
                 or bool(re.search(r"repair|servic", nb, I)))

    # 1. obvious mobile / computer only
    if shop in ("mobile_phone", "computer", "mobile_phone_accessories"):
        if not MAJOR.search(allt):
            return "excluded_mobile_computer", f"shop={shop}"
    if MOBILE_CHAINS.search(nb) and not MAJOR.search(nb):
        return "excluded_mobile_computer", "mobile/computer chain or brand in name/brand"
    if MOBCOMP.search(name) and not MAJOR.search(allt) and not BROAD_KEEP.search(name):
        return "excluded_mobile_computer", "name is mobile/computer-only"
    if rtxt and re.search(r"mobile|phone|computer|laptop", rtxt, I) and not MAJOR.search(allt) \
            and not re.search(r"electronics|tv|appliance", rtxt + " " + name, I):
        return "excluded_mobile_computer", "repair/service tags mobile/computer only"

    # 2. brand authorised service centre
    if BRAND_RE.search(nb) and SERVICE_CENTRE.search(name):
        return "authorised_service_centre", "appliance brand + service/care wording in name"
    if t.get("brand") and BRAND_RE.search(t.get("brand", "")) and is_repair:
        return "authorised_service_centre", "appliance brand tag on repair/service element"

    # 3. electricians (flagged)
    if craft == "electrician":
        if MAJOR.search(allt) and REPAIRWORD.search(allt):
            return "repair_appliance", "craft=electrician but name/tags say appliance repair"
        return "electrician", "craft=electrician"

    # 4. repair
    if craft == "hvac":
        return "repair_appliance", "craft=hvac"
    if is_repair:
        if re.search(r"service:vehicle|car|bike|motor|auto|tyre|tire|garage|cycle|two wheeler", allt, I) \
                and not MAJOR.search(name):
            return "other", "vehicle repair/service"
        if MAJOR.search(allt) or re.search(r"appliance|air_conditioning|refrigerator|washing", rtxt, I):
            return "repair_appliance", "repair element + major-appliance keyword in name/tags"
        if shop in ("appliance", "air_conditioning", "water_purifier"):
            return "repair_appliance", f"shop={shop} with repair tags"
        if craft == "electronics_repair" or ELEC.search(allt):
            return "repair_electronics_general", "electronics repair without major-appliance keyword"
        if shop in ("electronics", "hifi"):
            return "repair_electronics_general", f"shop={shop} with repair tags/name"
        if shop or craft or office:
            if not (shop == "repair"):
                pass
            else:
                return "other", "shop=repair, non-electronic"
        # fall through for shops with service:* tags (e.g. service:bicycle) etc.

    # 5. retail
    ch = chain_of(nb)
    if ch:
        if ch in ("Sony Center",):
            return "retail_electronics_general", f"chain:{ch}"
        return "retail_appliance", f"chain:{ch}"
    if shop in ("appliance", "air_conditioning", "water_purifier"):
        return "retail_appliance", f"shop={shop}"
    if shop == "water":
        if re.search(r"purif|\bro\b|r\.o\.|aqua|kent|filter", nb, I):
            return "retail_appliance", "shop=water + purifier/RO name"
        return "other", "shop=water (drinking water seller)"
    if shop in ("electronics", "hifi", "electrical") and APPL_RETAIL_BRANDS.search(nb):
        return "retail_appliance", f"shop={shop} + appliance brand (brand store/dealer)"
    if shop in ("electronics", "hifi", "electrical") and MAJOR.search(allt):
        return "retail_appliance", f"shop={shop} + major-appliance keyword"
    if shop == "electrical":
        if re.search(r"electronic|\btv\b|applian|home", nb, I):
            return "retail_electronics_general", "shop=electrical + electronics/appliance wording"
        return None, "shop=electrical without appliance hint (dropped)"
    if shop in ("electronics", "hifi"):
        return "retail_electronics_general", f"shop={shop}"

    # 6. name-match catch
    if shop and MAJOR.search(nb):
        return "retail_appliance", f"shop={shop} + major-appliance keyword in name"
    if (shop or office) and re.search(r"electronic", nb, I):
        return "retail_electronics_general", "name contains electronics"
    return "other", "matched query but no class rule"


def main():
    import sys
    sys.path.insert(0, HERE)
    import geo
    states = geo.load_india()
    els, groups_of, bases = {}, {}, set()
    for f in sorted(glob.glob(os.path.join(RAW, "tiles", "*.json"))):
        js = json.load(open(f))
        bases.add(js.get("osm_base"))
        for e in js["elements"]:
            k = (e["type"], e["id"])
            els.setdefault(k, e)
            groups_of.setdefault(k, set()).add(js["group"])
    servers = {"maps.mail.ru (primary), others as fallback; see tile_fetch_log.txt"}
    qstate, outside = {}, Counter()
    for k, e in list(els.items()):
        lat = e.get("lat", e.get("center", {}).get("lat"))
        lon = e.get("lon", e.get("center", {}).get("lon"))
        if lat is None:
            outside["no coordinates"] += 1; del els[k]; continue
        st = geo.state_of(states, lat, lon)
        tag = ""
        if st is None:
            st, d = geo.nearest_state(states, lat, lon, 2.0)
            tag = " (within 2 km of NE coastline/border)" if st else ""
        if st is None:
            outside["outside India polygons"] += 1; del els[k]; continue
        qstate[k] = st["name"]
        if tag:
            outside["snapped to nearest state <=2 km"] += 1
    cols = ["osm_type", "osm_id", "lat", "lon", "name", "brand", "brand_wikidata", "operator", "shop",
            "craft", "other_tags_json", "addr_city", "addr_postcode", "addr_state", "state_pip", "query_groups",
            "class", "class_rule", "osm_url", "retrieved"]
    rows, dropped = [], Counter()
    for k, e in els.items():
        t = e.get("tags", {})
        cls, rule = classify(t)
        if cls is None:
            dropped[rule] += 1
            continue
        lat = e.get("lat", e.get("center", {}).get("lat"))
        lon = e.get("lon", e.get("center", {}).get("lon"))
        other = {kk: vv for kk, vv in t.items() if KEEP_TAG.match(kk)}
        if not (t.get("name") and (t.get("shop") or t.get("craft") or t.get("office"))):
            for p in ("phone", "contact:phone", "contact:mobile", "mobile"):
                other.pop(p, None)
        rows.append({
            "osm_type": e["type"], "osm_id": e["id"], "lat": lat, "lon": lon,
            "name": t.get("name", ""), "brand": t.get("brand", ""), "brand_wikidata": t.get("brand:wikidata", ""),
            "operator": t.get("operator", ""), "shop": t.get("shop", ""), "craft": t.get("craft", ""),
            "other_tags_json": json.dumps(other, ensure_ascii=False, sort_keys=True),
            "addr_city": t.get("addr:city", ""), "addr_postcode": t.get("addr:postcode", ""),
            "addr_state": t.get("addr:state", ""), "state_pip": qstate[k],
            "query_groups": "|".join(sorted(groups_of[k])),
            "class": cls, "class_rule": rule,
            "osm_url": f"https://www.openstreetmap.org/{e['type']}/{e['id']}", "retrieved": RETRIEVED})
    rows.sort(key=lambda r: (r["state_pip"], r["class"], r["osm_type"], int(r["osm_id"])))
    with open(os.path.join(BASE, "osm_points.csv"), "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=cols); w.writeheader(); w.writerows(rows)

    # places
    pj = json.load(open(os.path.join(RAW, "places.json")))
    pcols = ["osm_type", "osm_id", "place", "name", "name_en", "population", "population_date", "lat", "lon",
             "wikidata", "addr_state", "is_in_state", "osm_url", "retrieved"]
    prow = []
    for e in pj["elements"]:
        t = e.get("tags", {})
        prow.append({"osm_type": e["type"], "osm_id": e["id"], "place": t.get("place", ""),
                     "name": t.get("name", ""), "name_en": t.get("name:en", ""),
                     "population": t.get("population", ""), "population_date": t.get("population:date", ""),
                     "lat": e.get("lat"), "lon": e.get("lon"), "wikidata": t.get("wikidata", ""),
                     "addr_state": t.get("addr:state", ""), "is_in_state": t.get("is_in:state", ""),
                     "osm_url": f"https://www.openstreetmap.org/node/{e['id']}", "retrieved": RETRIEVED})
    prow.sort(key=lambda r: (r["place"], r["name_en"] or r["name"]))
    with open(os.path.join(BASE, "osm_place_cities.csv"), "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=pcols); w.writeheader(); w.writerows(prow)

    # stats
    by_class = Counter(r["class"] for r in rows)
    by_state = {}
    for r in rows:
        by_state.setdefault(r["state_pip"], Counter())[r["class"]] += 1
    brands = Counter()
    for r in rows:
        b = r["brand"] or chain_of(f"{r['name']} {r['operator']}")
        if b:
            brands[(b, r["class"])] += 1
    addr_state = Counter(r["addr_state"] or "(no addr:state)" for r in rows)
    stats = {"n_rows": len(rows), "n_places": len(prow), "places_by_type": Counter(p["place"] for p in prow),
             "by_class": by_class, "by_type": Counter(r["osm_type"] for r in rows),
             "dropped": dropped, "outside": outside, "by_state": by_state, "top_brands": brands.most_common(40),
             "addr_state_top": addr_state.most_common(25), "servers": sorted(servers),
             "osm_base": sorted(b for b in bases if b), "places_osm_base": pj.get("osm3s", {}).get("timestamp_osm_base"),
             "rules": Counter((r["class"], r["class_rule"]) for r in rows).most_common(60)}
    stats["rules"] = [[a, b, c] for (a, b), c in stats["rules"]]
    stats["top_brands"] = [[a, b, c] for (a, b), c in stats["top_brands"]]
    json.dump(stats, open(os.path.join(RAW, "stats.json"), "w"), indent=1, ensure_ascii=False, default=dict)
    print(json.dumps({k: stats[k] for k in ("n_rows", "n_places", "by_class", "dropped", "outside")}, default=dict, indent=1))


if __name__ == "__main__":
    main()
