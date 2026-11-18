"""Point-in-polygon helpers over Natural Earth 10m admin-1 polygons for India (stdlib only)."""
import json, math, os

HERE = os.path.dirname(os.path.abspath(__file__))
NE = os.path.join(os.path.dirname(HERE), "boundaries", "ne_india_admin1.geojson")

# Natural Earth ISO codes -> current ISO 3166-2 / OSM codes
ISO_FIX = {"IN-CT": "IN-CG", "IN-OR": "IN-OD", "IN-TG": "IN-TS", "IN-UT": "IN-UK"}


def _polys(geom):
    if geom["type"] == "Polygon":
        return [geom["coordinates"]]
    return geom["coordinates"]


def load_india():
    out = []
    for f in json.load(open(NE))["features"]:
        p = f["properties"]
        polys = []
        for rings in _polys(f["geometry"]):
            outer = rings[0]
            xs = [c[0] for c in outer]; ys = [c[1] for c in outer]
            polys.append({"rings": rings, "bb": (min(ys), min(xs), max(ys), max(xs))})
        out.append({"name": p["name"], "iso": ISO_FIX.get(p["iso_3166_2"], p["iso_3166_2"]), "polys": polys,
                    "outer_rings": [pp["rings"][0] for pp in polys],
                    "ring_bbs": [pp["bb"] for pp in polys]})
    return out


def _in_ring(ring, lat, lon):
    inside = False
    j = len(ring) - 1
    for i in range(len(ring)):
        xi, yi = ring[i][0], ring[i][1]
        xj, yj = ring[j][0], ring[j][1]
        if (yi > lat) != (yj > lat) and lon < (xj - xi) * (lat - yi) / (yj - yi) + xi:
            inside = not inside
        j = i
    return inside


def state_of(states, lat, lon):
    for st in states:
        for p in st["polys"]:
            s, w, n, e = p["bb"]
            if s <= lat <= n and w <= lon <= e and _in_ring(p["rings"][0], lat, lon) \
                    and not any(_in_ring(h, lat, lon) for h in p["rings"][1:]):
                return st
    return None


def in_india_any(states, lat, lon):
    return state_of(states, lat, lon) is not None


def _seg_dist_km(lat, lon, a, b):
    # equirectangular projection around the point
    k = math.cos(math.radians(lat)) * 111.32
    ax, ay = (a[0] - lon) * k, (a[1] - lat) * 110.57
    bx, by = (b[0] - lon) * k, (b[1] - lat) * 110.57
    dx, dy = bx - ax, by - ay
    L = dx * dx + dy * dy
    t = 0 if L == 0 else max(0, min(1, -(ax * dx + ay * dy) / L))
    px, py = ax + t * dx, ay + t * dy
    return math.hypot(px, py)


def nearest_state(states, lat, lon, max_km):
    """For points just outside the generalised NE coastline: nearest state within max_km."""
    best, bd = None, max_km
    pad = max_km / 100.0
    for st in states:
        for p in st["polys"]:
            s, w, n, e = p["bb"]
            if not (s - pad <= lat <= n + pad and w - pad <= lon <= e + pad):
                continue
            r = p["rings"][0]
            for i in range(len(r) - 1):
                if abs(r[i][1] - lat) > pad and abs(r[i + 1][1] - lat) > pad:
                    continue
                d = _seg_dist_km(lat, lon, r[i], r[i + 1])
                if d < bd:
                    bd, best = d, st
    return best, bd
