#!/usr/bin/env python3
"""Fetch appliance retail / repair POIs and city/town places for India from OSM Overpass.

Standard library only. Queries are split by state/UT area (admin_level=4 relations inside
India, relation 304716). Each state's raw JSON response is saved to ../overpass_json/.
Usage: python3 fetch_osm.py [states|pois|places|all]
"""
import json, os, sys, time, urllib.parse, urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(os.path.dirname(HERE), "overpass_json")
os.makedirs(RAW, exist_ok=True)

SERVERS = [
    "https://overpass.private.coffee/api/interpreter",
    "https://overpass-api.de/api/interpreter",
    "https://maps.mail.ru/osm/tools/overpass/api/interpreter",
    "https://overpass.kumi.systems/api/interpreter",
]
UA = "india-appliance-market-study/1.0 (research; python-urllib)"
WAIT = 8  # seconds between calls
INDIA_REL = 304716

NAME_RE = ("service cent(re|er)|repair|refrigerat|cooling|aircon|a/c|ac service|ac repair|"
           "air condition|washing machine|fridge|ro service|water purifier|aquaguard|kent ro|"
           "electronics|home appliance|appliances")


def log(*a):
    print(time.strftime("%H:%M:%S"), *a, flush=True)


def overpass(query, label):
    last = None
    for attempt in range(8):
        url = SERVERS[attempt % len(SERVERS)]
        data = urllib.parse.urlencode({"data": query}).encode()
        req = urllib.request.Request(url, data=data, headers={"User-Agent": UA})
        t0 = time.time()
        try:
            with urllib.request.urlopen(req, timeout=240) as r:
                body = r.read()
            js = json.loads(body)
            remark = js.get("remark", "")
            if "runtime error" in remark or "timed out" in remark:
                raise RuntimeError("remark: " + remark[:200])
            log(f"OK {label} via {url.split('/')[2]} in {time.time()-t0:.0f}s, "
                f"{len(js.get('elements', []))} elements")
            return js, url
        except Exception as e:  # noqa
            last = e
            log(f"FAIL {label} via {url.split('/')[2]} after {time.time()-t0:.0f}s: {str(e)[:160]}")
            time.sleep(WAIT * (1 + attempt))
    raise RuntimeError(f"all servers failed for {label}: {last}")


def states():
    q = (f"[out:json][timeout:180];rel({INDIA_REL});map_to_area->.in;"
         'rel["boundary"="administrative"]["admin_level"="4"](area.in);out tags;')
    js, url = overpass(q, "state list")
    json.dump(js, open(os.path.join(RAW, "states.json"), "w"), ensure_ascii=False)


def poi_query(area_id, part):
    a = f"(area:{area_id})"
    if part == "tags":
        body = (
            f'nwr["shop"~"^(appliance|electronics|hifi|electrical|air_conditioning|water_purifier|water|repair)$"]{a};'
            f'nwr["craft"~"^(electronics_repair|hvac|electrician)$"]{a};'
        )
    elif part == "keys":
        body = (
            f'nwr[~"^repair(:.*)?$"~"."]{a};'
            f'nwr[~"^service:"~"."]{a};'
        )
    elif part == "names":
        body = (
            f'nwr["shop"]["name"~"{NAME_RE}",i]{a};'
            f'nwr["craft"]["name"~"{NAME_RE}",i]{a};'
            f'nwr["office"="company"]["name"~"{NAME_RE}",i]{a};'
        )
    else:
        raise ValueError(part)
    return f"[out:json][timeout:180];\n({body});\nout center tags;"


def pois():
    st = json.load(open(os.path.join(RAW, "states.json")))["elements"]
    for e in st:
        iso = e["tags"].get("ISO3166-2", f"rel{e['id']}")
        area_id = 3600000000 + e["id"]
        out = os.path.join(RAW, f"pois_{iso}.json")
        if os.path.exists(out):
            continue
        merged, servers = {}, []
        for part in ("tags", "keys", "names"):
            js, url = overpass(poi_query(area_id, part), f"{iso} {part}")
            servers.append(url)
            for el in js["elements"]:
                merged[(el["type"], el["id"])] = el
            osm_base = js.get("osm3s", {}).get("timestamp_osm_base")
            time.sleep(WAIT)
        json.dump({"iso": iso, "rel": e["id"], "name": e["tags"].get("name:en", e["tags"].get("name")),
                   "servers": servers, "timestamp_osm_base": osm_base,
                   "elements": list(merged.values())}, open(out, "w"), ensure_ascii=False)


def places():
    q = (f"[out:json][timeout:180];area({3600000000 + INDIA_REL})->.in;"
         'node["place"~"^(city|town)$"](area.in);out qt;')
    js, url = overpass(q, "places")
    js["server"] = url
    json.dump(js, open(os.path.join(RAW, "places.json"), "w"), ensure_ascii=False)


if __name__ == "__main__":
    what = sys.argv[1] if len(sys.argv) > 1 else "all"
    if what in ("states", "all") and not os.path.exists(os.path.join(RAW, "states.json")):
        states(); time.sleep(WAIT)
    if what in ("places", "all") and not os.path.exists(os.path.join(RAW, "places.json")):
        places(); time.sleep(WAIT)
    if what in ("pois", "all"):
        pois()
    log("done")
