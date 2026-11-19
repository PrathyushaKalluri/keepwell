"""Consistency check across the model, step docs and every output. Fails on stale numbers or missing canonical ones.
    python3 check_consistency.py
"""
import pathlib, re, sys, csv
sys.path.insert(0, str(pathlib.Path(__file__).parent / "model"))
import plan_v3 as V, rounds as RD
H = pathlib.Path(__file__).parent
rows, pk, u = V.run("base"); s_, a2, a3, x, out, vc = RD.returns()
canon = {  # value computed from the model -> string that must appear in outputs
 "Y7 revenue": (rows[6]["revenue"] / 1e7, "130.5"), "Y7 EBITDA": (rows[6]["ebitda"] / 1e7, "8.6"),
 "cluster EBITDA %": (u["own"]["margin"] * 100, "16"), "breakeven": (u["be_shops"], "22"),
 "founders after seed": (s_["Founders"] * 100, "64.0"), "seed after R3": (a3["Seed"] * 100, "14.6"),
 "EV7 stress": (out[("STRESS", 7)]["ev"] / 1e7, "255"), "EV7 base": (out[("BASE", 7)]["ev"] / 1e7, "376"),
}
bad = 0
for k, (v, sstr) in canon.items():
    if abs(v - float(sstr)) > (0.6 if "." not in sstr else 0.06): print("MODEL DRIFT", k, v, "vs", sstr); bad += 1
OUT = [H / "deck/deck_content.py", H / "story_deck/slides.html", H / "story_deck/script_data.py", H / "KEEPWELL_FULL_STORY.md"] + list((H / "proof_pack").glob("*.md"))
text = {p: p.read_text() for p in OUT if p.exists()}
for k, (v, sstr) in canon.items():
    for p in (H / "deck/deck_content.py", H / "story_deck/slides.html"):
        if sstr not in text.get(p, ""): print(f"MISSING {k} ({sstr}) in {p.name}"); bad += 1
STALE = [r"₹7\.5 Cr seed", r"₹4\.75", r"\bCircuit\b", r"\btranche", r"Series A gates", r"10–12% at maturity", r"₹115 Cr", r"1,950 shops", r"T2 gates"]
for p, t in text.items():
    for pat in STALE:
        for m in re.finditer(pat, t): print(f"STALE '{pat}' in {p.name}: …{t[max(0,m.start()-40):m.end()+30]!r}"); bad += 1
led = list(csv.DictReader(open(H / "claims_ledger.csv")))
print(f"claims ledger rows: {len(led)} | outputs checked: {len(text)} | problems: {bad}")
sys.exit(1 if bad else 0)
