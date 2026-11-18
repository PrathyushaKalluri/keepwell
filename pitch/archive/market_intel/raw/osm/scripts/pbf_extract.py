#!/usr/bin/env python3
"""Fallback extractor: read a Geofabrik .osm.pbf with the Python standard library only
(zlib + a hand-written protobuf reader, multiprocessing for speed) and pull the same
elements the Overpass queries in fetch_osm_tiles.py ask for.

Used because on 2026-11-18 every reachable public Overpass server failed or timed out
(see overpass_json/fetch_log.txt and tile_fetch_log.txt).

Output: ../pbf_json/elements.json  (Overpass-like: type, id, lat/lon or center, tags)
Usage:  python3 -I pbf_extract.py /path/to/india-latest.osm.pbf
"""
import json, multiprocessing as mp, os, re, struct, sys, time, zlib

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(os.path.dirname(HERE), "pbf_json")

NAME_RE = re.compile("service cent(re|er)|repair|refrigerat|cooling|aircon|a/c|ac service|ac repair|"
                     "air condition|washing machine|fridge|ro service|water purifier|aquaguard|kent ro|"
                     "electronics|home appliance|appliances", re.I)
SHOPS = {"appliance", "electronics", "hifi", "electrical", "air_conditioning", "water_purifier", "water", "repair"}
CRAFTS = {"electronics_repair", "hvac", "electrician"}
KEY_RE = re.compile(r"^(repair(:.*)?|service:.*)$")
NPROC = max(1, (os.cpu_count() or 2) - 1)
PREFILTER = (b"shop", b"craft", b"repair", b"service:", b"office")


def matches(t):
    """Exact equivalent of the union of the Overpass filters (tags / keys / names groups)."""
    shop, craft = t.get("shop"), t.get("craft")
    if shop in SHOPS or craft in CRAFTS:
        return True
    for k in t:
        if KEY_RE.match(k):
            return True
    name = t.get("name")
    if name and (shop is not None or craft is not None or t.get("office") == "company") and NAME_RE.search(name):
        return True
    return False


# ---------------- protobuf primitives ----------------
def varint(b, p):
    r = 0; s = 0
    while True:
        x = b[p]; p += 1
        r |= (x & 0x7F) << s
        if x < 0x80:
            return r, p
        s += 7


def fields(b, p, end):
    while p < end:
        k, p = varint(b, p)
        wt = k & 7; fn = k >> 3
        if wt == 0:
            v, p = varint(b, p); yield fn, v
        elif wt == 2:
            l, p = varint(b, p); yield fn, (p, p + l); p += l
        elif wt == 1:
            p += 8
        elif wt == 5:
            p += 4
        else:
            raise ValueError("wire type %d" % wt)


def packed(b, se):
    p, end = se; out = []; ap = out.append
    while p < end:
        r = 0; s = 0
        while True:
            x = b[p]; p += 1
            r |= (x & 0x7F) << s
            if x < 0x80:
                break
            s += 7
        ap(r)
    return out


def zz(n):
    return (n >> 1) ^ -(n & 1)


def delta_zz(vals):
    out = []; acc = 0; ap = out.append
    for v in vals:
        acc += (v >> 1) ^ -(v & 1); ap(acc)
    return out


# ---------------- file index ----------------
def index_blobs(path):
    res = []
    with open(path, "rb") as f:
        pos = 0
        while True:
            h = f.read(4)
            if len(h) < 4:
                break
            hl = struct.unpack(">I", h)[0]
            hb = f.read(hl)
            typ, size = None, 0
            for fn, v in fields(hb, 0, len(hb)):
                if fn == 1: typ = hb[v[0]:v[1]].decode()
                elif fn == 3: size = v
            dpos = pos + 4 + hl
            if typ == "OSMData":
                res.append((dpos, size))
            f.seek(size, 1)
            pos = dpos + size
    return res


def read_block(path, off, size):
    with open(path, "rb") as f:
        f.seek(off); blob = f.read(size)
    raw = zdata = None
    for fn, v in fields(blob, 0, len(blob)):
        if fn == 1: raw = blob[v[0]:v[1]]
        elif fn == 3: zdata = blob[v[0]:v[1]]
    return raw if raw is not None else zlib.decompress(zdata)


def block_meta(b):
    strings, groups, gran, lato, lono = [], [], 100, 0, 0
    st = None
    for fn, v in fields(b, 0, len(b)):
        if fn == 1: st = v
        elif fn == 2: groups.append(v)
        elif fn == 17: gran = v
        elif fn == 19: lato = zz(v)
        elif fn == 20: lono = zz(v)
    if st:
        for fn, v in fields(b, st[0], st[1]):
            if fn == 1: strings.append(b[v[0]:v[1]])
    return strings, groups, gran, lato, lono


# ---------------- pass 1: find matching elements ----------------
def pass1(args):
    path, off, size = args
    b = read_block(path, off, size)
    strings, groups, gran, lato, lono = block_meta(b)
    relevant = any(any(s.startswith(pf) for pf in PREFILTER) for s in strings)
    sd = None
    out = {"nodes": [], "ways": [], "rels": [], "kind": None, "idrange": None}
    for g0, g1 in groups:
        for fn, v in fields(b, g0, g1):
            if fn == 2:  # dense
                out["kind"] = "n"
                ids = latr = lonr = kv = None
                for f2, v2 in fields(b, v[0], v[1]):
                    if f2 == 1: ids = v2
                    elif f2 == 8: latr = v2
                    elif f2 == 9: lonr = v2
                    elif f2 == 10: kv = v2
                idl = delta_zz(packed(b, ids))
                out["idrange"] = (idl[0], idl[-1]) if idl else None
                if not relevant or kv is None:
                    continue
                kvl = packed(b, kv)
                if sd is None:
                    sd = [s.decode("utf-8", "replace") for s in strings]
                hits = []; i = 0; ni = 0; n = len(kvl)
                while i < n:
                    if kvl[i] == 0:
                        i += 1; ni += 1; continue
                    t = {}
                    while kvl[i] != 0:
                        t[sd[kvl[i]]] = sd[kvl[i + 1]]; i += 2
                    i += 1
                    if matches(t):
                        hits.append((ni, t))
                    ni += 1
                if hits:
                    la = delta_zz(packed(b, latr)); lo = delta_zz(packed(b, lonr))
                    for ni, t in hits:
                        out["nodes"].append({"type": "node", "id": idl[ni],
                                             "lat": round(1e-9 * (lato + gran * la[ni]), 7),
                                             "lon": round(1e-9 * (lono + gran * lo[ni]), 7), "tags": t})
            elif fn == 1:  # plain node
                out["kind"] = "n"
                nid = lat = lon = 0; keys = vals = None
                for f2, v2 in fields(b, v[0], v[1]):
                    if f2 == 1: nid = zz(v2)
                    elif f2 == 2: keys = v2
                    elif f2 == 3: vals = v2
                    elif f2 == 8: lat = zz(v2)
                    elif f2 == 9: lon = zz(v2)
                if keys and relevant:
                    if sd is None:
                        sd = [s.decode("utf-8", "replace") for s in strings]
                    t = {sd[k]: sd[x] for k, x in zip(packed(b, keys), packed(b, vals))}
                    if matches(t):
                        out["nodes"].append({"type": "node", "id": nid, "lat": round(1e-9 * (lato + gran * lat), 7),
                                             "lon": round(1e-9 * (lono + gran * lon), 7), "tags": t})
            elif fn in (3, 4):  # way / relation
                out["kind"] = "w" if fn == 3 else "r"
                if not relevant:
                    # still need id range for ways (used when relations need member ways)
                    if fn == 3:
                        for f2, v2 in fields(b, v[0], v[1]):
                            if f2 == 1:
                                r = out["idrange"]
                                out["idrange"] = (v2, v2) if r is None else (min(r[0], v2), max(r[1], v2))
                                break
                    continue
                eid = 0; keys = vals = refs = mids = types = None
                for f2, v2 in fields(b, v[0], v[1]):
                    if f2 == 1: eid = v2
                    elif f2 == 2: keys = v2
                    elif f2 == 3: vals = v2
                    elif f2 == 8 and fn == 3: refs = v2
                    elif f2 == 9 and fn == 4: mids = v2
                    elif f2 == 10 and fn == 4: types = v2
                if fn == 3:
                    r = out["idrange"]
                    out["idrange"] = (eid, eid) if r is None else (min(r[0], eid), max(r[1], eid))
                if not keys:
                    continue
                if sd is None:
                    sd = [s.decode("utf-8", "replace") for s in strings]
                t = {sd[k]: sd[x] for k, x in zip(packed(b, keys), packed(b, vals))}
                if not matches(t):
                    continue
                if fn == 3:
                    out["ways"].append({"type": "way", "id": eid, "tags": t, "refs": delta_zz(packed(b, refs)) if refs else []})
                else:
                    mem = list(zip(packed(b, types) if types else [], delta_zz(packed(b, mids)) if mids else []))
                    out["rels"].append({"type": "relation", "id": eid, "tags": t, "members": mem})
    return out


# ---------------- pass 2: way refs for relation members ----------------
WANTED = set()


def _init(w):
    global WANTED
    WANTED = w


def pass_ways(args):
    path, off, size = args
    wanted = WANTED
    b = read_block(path, off, size)
    _, groups, *_ = block_meta(b)
    res = {}
    for g0, g1 in groups:
        for fn, v in fields(b, g0, g1):
            if fn != 3:
                continue
            eid = 0; refs = None
            for f2, v2 in fields(b, v[0], v[1]):
                if f2 == 1: eid = v2
                elif f2 == 8: refs = v2
            if eid in wanted and refs:
                res[eid] = delta_zz(packed(b, refs))
    return res


# ---------------- pass 3: node coordinates ----------------
def pass_nodes(args):
    path, off, size = args
    wanted = WANTED
    b = read_block(path, off, size)
    _, groups, gran, lato, lono = block_meta(b)
    res = {}
    for g0, g1 in groups:
        for fn, v in fields(b, g0, g1):
            if fn == 2:
                ids = latr = lonr = None
                for f2, v2 in fields(b, v[0], v[1]):
                    if f2 == 1: ids = v2
                    elif f2 == 8: latr = v2
                    elif f2 == 9: lonr = v2
                idl = delta_zz(packed(b, ids))
                hit = [i for i, x in enumerate(idl) if x in wanted]
                if hit:
                    la = delta_zz(packed(b, latr)); lo = delta_zz(packed(b, lonr))
                    for i in hit:
                        res[idl[i]] = (1e-9 * (lato + gran * la[i]), 1e-9 * (lono + gran * lo[i]))
            elif fn == 1:
                nid = lat = lon = 0
                for f2, v2 in fields(b, v[0], v[1]):
                    if f2 == 1: nid = zz(v2)
                    elif f2 == 8: lat = zz(v2)
                    elif f2 == 9: lon = zz(v2)
                if nid in wanted:
                    res[nid] = (1e-9 * (lato + gran * lat), 1e-9 * (lono + gran * lon))
    return res


def overlaps(rng, ids_sorted):
    import bisect
    if rng is None:
        return False
    i = bisect.bisect_left(ids_sorted, rng[0])
    return i < len(ids_sorted) and ids_sorted[i] <= rng[1]


def main(path):
    os.makedirs(OUT, exist_ok=True)
    t0 = time.time()
    idx = index_blobs(path)
    print(f"{len(idx)} data blobs indexed in {time.time()-t0:.0f}s", flush=True)
    nodes, ways, rels, kinds = [], [], [], []
    with mp.Pool(NPROC) as pool:
        for i, r in enumerate(pool.imap(pass1, [(path, o, s) for o, s in idx], chunksize=8)):
            nodes += r["nodes"]; ways += r["ways"]; rels += r["rels"]; kinds.append((r["kind"], r["idrange"]))
            if i % 2000 == 0:
                print(f"pass1 {i}/{len(idx)} {time.time()-t0:.0f}s nodes={len(nodes)} ways={len(ways)} rels={len(rels)}", flush=True)
        print(f"pass1 done {time.time()-t0:.0f}s nodes={len(nodes)} ways={len(ways)} rels={len(rels)}", flush=True)

        # relation member ways
        want_w = sorted({m for r in rels for typ, m in r["members"] if typ == 1})
        wrefs = {w["id"]: w["refs"] for w in ways}
        need = [w for w in want_w if w not in wrefs]
        if need:
            jobs = [(path, o, s) for (o, s), (k, rng) in zip(idx, kinds) if k == "w" and overlaps(rng, need)]
            with mp.Pool(NPROC, _init, (set(need),)) as p2:
                for r in p2.imap_unordered(pass_ways, jobs):
                    wrefs.update(r)
        # node coordinates
        want_n = set()
        for w in ways:
            want_n.update(w["refs"])
        for r in rels:
            for typ, m in r["members"]:
                if typ == 0: want_n.add(m)
                elif typ == 1: want_n.update(wrefs.get(m, []))
        ns = sorted(want_n)
        jobs = [(path, o, s) for (o, s), (k, rng) in zip(idx, kinds) if k == "n" and overlaps(rng, ns)]
        print(f"need {len(want_n)} node coords from {len(jobs)} node blocks", flush=True)
        coords = {}
        with mp.Pool(NPROC, _init, (want_n,)) as p3:
            for r in p3.imap_unordered(pass_nodes, jobs, chunksize=4):
                coords.update(r)
    print(f"coords done {time.time()-t0:.0f}s", flush=True)

    def center(refs):
        pts = [coords[n] for n in refs if n in coords]
        if not pts:
            return None
        la = [p[0] for p in pts]; lo = [p[1] for p in pts]
        return {"lat": round((min(la) + max(la)) / 2, 7), "lon": round((min(lo) + max(lo)) / 2, 7)}

    els = list(nodes)
    for w in ways:
        e = {"type": "way", "id": w["id"], "tags": w["tags"]}
        c = center(w["refs"])
        if c: e["center"] = c
        els.append(e)
    for r in rels:
        refs = []
        for typ, m in r["members"]:
            if typ == 0: refs.append(m)
            elif typ == 1: refs += wrefs.get(m, [])
        e = {"type": "relation", "id": r["id"], "tags": r["tags"]}
        c = center(refs)
        if c: e["center"] = c
        els.append(e)
    meta = {"source": os.path.basename(path), "source_url": "https://download.geofabrik.de/asia/india-latest.osm.pbf",
            "extracted": time.strftime("%Y-%m-%d %H:%M"), "elements": els}
    json.dump(meta, open(os.path.join(OUT, "elements.json"), "w"), ensure_ascii=False)
    print(f"wrote {len(els)} elements in {time.time()-t0:.0f}s", flush=True)


if __name__ == "__main__":
    main(sys.argv[1])
