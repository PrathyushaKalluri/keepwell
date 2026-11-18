#!/usr/bin/env python3
"""Write osm_summary.md from osm_points.csv, osm_place_cities.csv and overpass_json/stats.json."""
import csv, json, math, os, sys
from collections import Counter, defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import fetch_osm_tiles as ft  # noqa: E402  (query text)
import fetch_osm as fo  # noqa: E402
import pbf_extract as px  # noqa: E402

rows = list(csv.DictReader(open(os.path.join(BASE, "osm_points.csv"), encoding="utf-8")))
places = list(csv.DictReader(open(os.path.join(BASE, "osm_place_cities.csv"), encoding="utf-8")))
stats = json.load(open(os.path.join(BASE, "overpass_json", "stats.json")))
src = json.load(open(os.path.join(BASE, "pbf_json", "elements.json")))
CLASSES = ["retail_appliance", "retail_electronics_general", "repair_appliance", "repair_electronics_general",
           "authorised_service_centre", "electrician", "other", "excluded_mobile_computer"]


def km(a, b, c, d):
    p = math.pi / 180
    x = (d - b) * p * math.cos((a + c) / 2 * p); y = (c - a) * p
    return 6371 * math.hypot(x, y)


L = []
w = L.append
by_class = Counter(r["class"] for r in rows)
w("# OSM appliance retail & repair points, India: summary\n")
w(f"Retrieved {rows[0]['retrieved'] if rows else ''}. Data © OpenStreetMap contributors, ODbL 1.0 "
  "(https://www.openstreetmap.org/copyright). Attribute OSM in anything built from these files.\n")
w("## Files\n")
w("| File | Rows | What |\n|---|---|---|")
w(f"| `osm_points.csv` | {len(rows):,} | one row per OSM element (deduped on type+id), classified |")
w(f"| `osm_place_cities.csv` | {len(places):,} | every `place=city` ({sum(p['place']=='city' for p in places)}) and `place=town` ({sum(p['place']=='town' for p in places)}) node in India |")
w("| `overpass_json/` | | raw Overpass responses (state list, places), fetch logs, failed tile attempts |")
w("| `pbf_json/elements.json` | | raw matched elements extracted from the Geofabrik PBF |")
w("| `boundaries/ne_india_admin1.geojson` | | Natural Earth 10m admin-1 polygons used to clip to India and assign `state_pip` |")
w("| `scripts/` | | `fetch_osm.py`, `fetch_osm_tiles.py`, `pbf_extract.py`, `geo.py`, `process_osm.py`, `make_summary.py` (stdlib only) |\n")

w("## How the data was pulled (read this first)\n")
w("""* **Overpass worked for the reference layers only.** On 2026-11-18 `overpass-api.de` refused TCP connections
  from this network (all of `overpass-api.de`, `lz4.`, `z.`, port 80 and 443), `overpass.kumi.systems` and
  `overpass.private.coffee` timed out on almost every request (even a single-tag query on one 1° tile), and
  `maps.mail.ru` answered small queries but returns nginx 504 after ~50 s and alternates with a broken backend.
  State-area POI queries failed on every server; a bbox-tile fallback (4° tiles split adaptively to 0.25°) also
  stalled (one 1° Kerala tile took 17 minutes before timing out). Logs: `overpass_json/fetch_log.txt`,
  `overpass_json/tile_fetch_log.txt`.
* What did come from Overpass: the list of 36 state/UT relations (`overpass_json/states.json`, via maps.mail.ru) and
  all `place=city|town` nodes in India (`overpass_json/places.json`, via overpass.private.coffee).
* **The POIs come from the same OSM data via the Geofabrik India extract** (`india-latest.osm.pbf`, the
  2026-11-18 daily build, ODbL), parsed with a stdlib-only PBF reader (`scripts/pbf_extract.py`, zlib plus
  hand-written protobuf decoding). The filter applied to every node, way and relation is exactly the union of the
  Overpass filters below, so the result is the same set those queries would have returned. Ways and relations get
  the bounding-box centre of their member nodes, which is what Overpass `out center` gives.
* Geofabrik's India extract is cut with Geofabrik's own India polygon. Points are then clipped with Natural Earth
  10m admin-1 polygons (de facto boundaries) and assigned to `state_pip` by point-in-polygon. Points up to 2 km
  outside a polygon (generalised coastline) are snapped to the nearest state.
* `addr_state` is the raw `addr:state` tag. Few points have it, so use `state_pip` for state analysis.
""")
w("### Query text\n")
w("Overpass POI query, run per state area (`area:36xxxxxxxx` = 3600000000 + relation id), then per bbox tile when that failed:\n")
w("```overpass")
w(fo.poi_query(3600096905, "tags"))
w(fo.poi_query(3600096905, "keys"))
w(fo.poi_query(3600096905, "names"))
w("```\n")
w("Tile form (example tile, group `names_shop`):\n")
w("```overpass\n" + ft.query_text("names_shop", 12.0, 80.0, 13.0, 81.0) + "\n```\n")
w("State list and places (these ran):\n")
w("```overpass\n[out:json][timeout:180];rel(304716);map_to_area->.in;rel[\"boundary\"=\"administrative\"][\"admin_level\"=\"4\"](area.in);out tags;\n"
  "[out:json][timeout:180];area(3600304716)->.in;node[\"place\"~\"^(city|town)$\"](area.in);out qt;\n```\n")
w("PBF filter used for POIs (equivalent, from `pbf_extract.py`):\n")
w("```python\nSHOPS  = " + repr(sorted(px.SHOPS)) +
  "\nCRAFTS = " + repr(sorted(px.CRAFTS)) +
  "\nkeep if shop in SHOPS or craft in CRAFTS\n   or any key matches ^(repair(:.*)?|service:.*)$\n"
  "   or (shop or craft present or office=company) and name ~* /" + ft.NAME_RE + "/\n```\n")

w("## Counts by class\n")
w("| class | points |\n|---|---|")
for c in CLASSES:
    w(f"| {c} | {by_class.get(c, 0):,} |")
w(f"| **total** | **{len(rows):,}** |\n")
d = stats.get("dropped", {})
if d:
    w("Dropped and not in the file: " + "; ".join(f"{k}: {v:,}" for k, v in d.items()) + ".")
o = stats.get("outside", {})
if o:
    w("Clipping: " + "; ".join(f"{k}: {v:,}" for k, v in o.items()) + ".\n")
w("Classification rules (first match wins; `class_rule` names the rule that fired):\n")
w("| class | rule | n |\n|---|---|---|")
for c, r, n in stats["rules"]:
    w(f"| {c} | {r} | {n:,} |")
w("")

w("## Counts by state (point-in-polygon `state_pip`)\n")
st = defaultdict(Counter)
for r in rows:
    st[r["state_pip"]][r["class"]] += 1
order = sorted(st, key=lambda s: -(st[s]["retail_appliance"] + st[s]["repair_appliance"]))
short = ["retail_appliance", "repair_appliance", "authorised_service_centre", "retail_electronics_general",
         "repair_electronics_general", "electrician", "other", "excluded_mobile_computer"]
w("| # | state | " + " | ".join(short) + " | total | appliance (retail+repair) |")
w("|---|---|" + "---|" * (len(short) + 2))
for i, s in enumerate(order, 1):
    w(f"| {i} | {s} | " + " | ".join(str(st[s][c]) for c in short) +
      f" | {sum(st[s].values())} | {st[s]['retail_appliance'] + st[s]['repair_appliance']} |")
w("")
w("Raw `addr:state` tag values (top 15, unnormalised):\n")
for k, v in stats["addr_state_top"][:15]:
    w(f"* {k}: {v:,}")
w("")

w("## Top chains / brands found\n")
w("`brand` tag if present, otherwise chain name matched on name/operator. Top 30 brand × class pairs:\n")
w("| brand / chain | class | n |\n|---|---|---|")
for b, c, n in stats["top_brands"][:30]:
    w(f"| {b} | {c} | {n} |")
bw = sum(1 for r in rows if r["brand_wikidata"])
bt = sum(1 for r in rows if r["brand"])
w(f"\nOnly {bt:,} of {len(rows):,} points ({bt/len(rows):.1%}) carry a `brand` tag and {bw:,} carry `brand:wikidata`, "
  "so chain counts here are floors, not store counts.\n")

w("## OSM completeness: an honest assessment\n")
w("<<CITY>>")
open(os.path.join(BASE, "osm_summary.md"), "w", encoding="utf-8").write("\n".join(L) + "\n")

# city check data for manual write-up
CITIES = {"Warangal": (17.9689, 79.5941, 12), "Vijayawada": (16.5062, 80.6480, 12), "Coimbatore": (11.0168, 76.9558, 15)}
out = {}
for c, (la, lo, rad) in CITIES.items():
    near = [r for r in rows if km(la, lo, float(r["lat"]), float(r["lon"])) <= rad]
    out[c] = {"radius_km": rad, "by_class": Counter(r["class"] for r in near),
              "chains": sorted({(r["name"], r["brand"], r["class"], r["osm_url"]) for r in near
                                if r["class_rule"].startswith("chain") or r["brand"]})}
json.dump(out, open(os.path.join(BASE, "overpass_json", "city_check.json"), "w"), indent=1, default=list, ensure_ascii=False)
print(json.dumps(out, indent=1, default=list, ensure_ascii=False))
