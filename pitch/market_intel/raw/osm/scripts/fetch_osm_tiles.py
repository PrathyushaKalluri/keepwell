#!/usr/bin/env python3
"""Tiled Overpass fetch of appliance retail / repair POIs over India (standard library only).

Why tiles: on 2026-11-18 area-based (state) queries timed out on every reachable public
Overpass server (overpass-api.de refused connections from this network; private.coffee and
kumi.systems timed out; maps.mail.ru has a ~50 s gateway limit). So India is covered with
4-degree bbox tiles that intersect India (Natural Earth admin-1 polygons), and any tile/query
group that times out slowly is split into 4 sub-tiles, down to 0.25 degrees.
Points are clipped to India and assigned to a state in process_osm.py (point-in-polygon).

Each successful (group, tile) response is cached in ../overpass_json/tiles/ so the run resumes.
"""
import json, os, sys, time, urllib.parse, urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.dirname(HERE)
TILES = os.path.join(BASE, "overpass_json", "tiles")
os.makedirs(TILES, exist_ok=True)
sys.path.insert(0, HERE)
from geo import load_india, in_india_any  # noqa: E402

SERVERS = ["https://maps.mail.ru/osm/tools/overpass/api/interpreter",
           "https://overpass.private.coffee/api/interpreter",
           "https://overpass.kumi.systems/api/interpreter",
           "https://overpass-api.de/api/interpreter"]
UA = "india-appliance-market-study/1.0 (research; python-urllib)"
PAUSE = 4          # seconds between successful calls
QUICK_RETRY = 5    # seconds before retrying a fast 5xx (busy backend)
MIN_SIZE = 0.25    # degrees

NAME_RE = ("service cent(re|er)|repair|refrigerat|cooling|aircon|a/c|ac service|ac repair|"
           "air condition|washing machine|fridge|ro service|water purifier|aquaguard|kent ro|"
           "electronics|home appliance|appliances")

GROUPS = {
    "tags": ('nwr["shop"~"^(appliance|electronics|hifi|electrical|air_conditioning|water_purifier|water|repair)$"]{b};'
             'nwr["craft"~"^(electronics_repair|hvac|electrician)$"]{b};'),
    "keys": ('nwr[~"^repair(:.*)?$"~"."]{b};'
             'nwr[~"^service:"~"."]{b};'),
    "names_shop": 'nwr["shop"]["name"~"' + NAME_RE + '",i]{b};',
    "names_craft_office": ('nwr["craft"]["name"~"' + NAME_RE + '",i]{b};'
                           'nwr["office"="company"]["name"~"' + NAME_RE + '",i]{b};'),
}


def query_text(group, s, w, n, e):
    b = f"({s},{w},{n},{e})"
    return "[out:json][timeout:180];\n(" + GROUPS[group].replace("{b}", b) + ");\nout center tags;"


def log(*a):
    print(time.strftime("%H:%M:%S"), *a, flush=True)


def post(url, q, timeout):
    data = urllib.parse.urlencode({"data": q}).encode()
    req = urllib.request.Request(url, data=data, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.loads(r.read())


def run(q, label):
    """Return json, or None if the query is too slow (caller should split)."""
    slow = 0
    for attempt in range(40):
        url = SERVERS[0]
        # after repeated slow failures on mail.ru, try one of the long-timeout mirrors once
        if slow >= 1 and attempt % 6 == 5:
            url = SERVERS[1 + (attempt // 6) % 3]
        t0 = time.time()
        try:
            js = post(url, q, 200)
            rem = js.get("remark", "")
            if "runtime error" in rem or "Timeout" in rem or "timed out" in rem:
                raise RuntimeError(rem[:150])
            log(f"OK   {label} {url.split('/')[2]} {time.time()-t0:.0f}s n={len(js['elements'])}")
            return js
        except Exception as ex:  # noqa
            dt = time.time() - t0
            msg = str(ex)[:90]
            if dt > 35:
                slow += 1
                log(f"SLOW {label} {url.split('/')[2]} {dt:.0f}s {msg}")
                if slow >= 2:
                    return None
            else:
                if attempt % 10 == 9:
                    log(f"busy {label} {url.split('/')[2]} x{attempt+1} {msg}")
            time.sleep(QUICK_RETRY if dt <= 35 else 15)
    return None


def cell_has_india(polys, s, w, n, e):
    k = 6
    for i in range(k + 1):
        for j in range(k + 1):
            if in_india_any(polys, s + (n - s) * i / k, w + (e - w) * j / k):
                return True
    for st in polys:
        for bb, ring in zip(st["ring_bbs"], st["outer_rings"]):
            if bb[2] < s or bb[0] > n or bb[3] < w or bb[1] > e:
                continue
            for lon, lat in ring[::3]:
                if s <= lat <= n and w <= lon <= e:
                    return True
    return False


def fname(group, s, w, n, e):
    return os.path.join(TILES, f"{group}_{s:.3f}_{w:.3f}_{n:.3f}_{e:.3f}.json")


def do_tile(polys, group, s, w, n, e, stats):
    if not cell_has_india(polys, s, w, n, e):
        return
    f = fname(group, s, w, n, e)
    if os.path.exists(f):
        return
    split_marker = f + ".split"
    js = None
    if not os.path.exists(split_marker):
        js = run(query_text(group, s, w, n, e), f"{group} ({s},{w},{n},{e})")
    if js is not None:
        json.dump({"group": group, "bbox": [s, w, n, e], "osm_base": js.get("osm3s", {}).get("timestamp_osm_base"),
                   "elements": js["elements"]}, open(f, "w"), ensure_ascii=False)
        stats["ok"] += 1
        time.sleep(PAUSE)
        return
    size = n - s
    if size / 2 < MIN_SIZE:
        log(f"GIVEUP {group} ({s},{w},{n},{e})")
        stats["failed"].append([group, s, w, n, e])
        return
    open(split_marker, "w").close()
    h = size / 2
    for (a, b) in ((s, w), (s, w + h), (s + h, w), (s + h, w + h)):
        do_tile(polys, group, a, b, a + h, b + h, stats)


def main():
    polys = load_india()
    stats = {"ok": 0, "failed": []}
    step = 4.0
    lat0, lat1, lon0, lon1 = 6.0, 38.0, 68.0, 98.0
    groups = sys.argv[1:] or list(GROUPS)
    for g in groups:
        lat = lat0
        while lat < lat1:
            lon = lon0
            while lon < lon1:
                do_tile(polys, g, lat, lon, lat + step, lon + step, stats)
                lon += step
            lat += step
        log(f"group {g} finished; ok so far {stats['ok']}, failed {len(stats['failed'])}")
    json.dump(stats, open(os.path.join(BASE, "overpass_json", "tile_run_stats.json"), "w"))
    log("done", stats["ok"], "failed:", stats["failed"])


if __name__ == "__main__":
    main()
