"""Consistency check across the model, the step docs, both stories and every output.
    python3 check_consistency.py
Fails on (a) model drift from the canonical numbers, (b) canonical numbers missing from the decks,
(c) stale numbers or wording anywhere in the current documents. Superseded Gate-1 records (00_*, 07_) and the
outside-review inputs (steps/reviews/) are not scanned for stale text.
"""
import pathlib, re, sys, csv
H = pathlib.Path(__file__).parent
sys.path.insert(0, str(H / "model"))
import plan_v3 as V, rounds as RD
rows, pk, u = V.run("base"); s_, a2, a3, x, out, vc = RD.returns()
canon = {
 "Y7 revenue": (rows[6]["revenue"] / 1e7, "130.5"), "Y7 EBITDA": (rows[6]["ebitda"] / 1e7, "8.6"),
 "cluster EBITDA %": (u["own"]["margin"] * 100, "16"), "breakeven": (u["be_shops"], "22"),
 "pre-money": (RD.R["seed_pre"] / 1e7, "8"), "seed stake": (s_["Seed"] * 100, "23.8"),
 "founders after seed": (s_["Founders"] * 100, "60.5"), "seed after R3": (a3["Seed"] * 100, "16.3"),
 "EV7 stress": (out[("STRESS", 7)]["ev"] / 1e7, "255"), "EV7 base": (out[("BASE", 7)]["ev"] / 1e7, "376"),
 "yr5 stress multiple": (out[("STRESS", 5)]["mult"], "6.9"),
}
bad = 0
for k, (v, sstr) in canon.items():
    tol = 0.06 if "." in sstr else 0.6
    if abs(v - float(sstr)) > tol: print("MODEL DRIFT", k, round(v, 3), "vs", sstr); bad += 1
must = {H / "deck/deck_content.py": ["130.5", "8.6", "16", "22", "₹8 Cr", "23.8", "60.5", "16.3", "255", "376"],
        H / "story_deck/slides.html": ["130.5", "8.6", "16%", "22 retailers", "₹8 Cr", "23.8", "60.5", "16.3", "255", "376"],
        H / "story_deck/slides_8min.html": ["130.5", "8.6", "16%", "22 retailers", "₹8 Cr", "23.8", "60.5", "16.3", "255", "376"]}
for p, keys in must.items():
    t = p.read_text()
    for kk in keys:
        if kk not in t: print(f"MISSING '{kk}' in {p.name}"); bad += 1
SCAN = [H / "deck/deck_content.py", H / "story_deck/slides.html", H / "story_deck/script_data.py", H / "story_deck/slides_8min.html", H / "story_deck/script_8min.py", H / "KEEPWELL_FULL_STORY.md"]
SCAN += list((H / "proof_pack").glob("*.md"))
SCAN += [p for p in (H / "steps").glob("*.md") if not p.name.startswith(("00", "07_"))]
STALE = [r"₹10 Cr pre", r"₹12\.5 Cr post", r"₹30 Cr pre", r"₹85 Cr pre", r"\b630 formulas", r"\b679 formulas", r"\b378 formulas",
         r"Nobody serves", r"nobody serves", r"\b21 issues", r"\[Story", r"\[Real", r"Illustrative case", r"illustrative case",
         r"month-12 checkpoint", r"₹14\.4 Cr", r"46\.6%", r"64\.0%", r"14\.9×", r"21\.9×", r"6\.2× \(44", r"HomeServe for India",
         r"five milestones", r"20 Nov 2026", r"minimum close ₹2\.0", r"[Tt]ranche", r"₹1\.75 Cr", r"month-9 gate", r"small-town appliance shop"]
OUTPUTS = SCAN[:6] + list((H / "proof_pack").glob("*.md")) + [H / "steps/Entire story.md"]
for p in OUTPUTS:
    for m in re.finditer(r"independent shop", p.read_text()):
        print(f"WORDING 'independent shop' in {p.relative_to(H)}"); bad += 1
for p in SCAN:
    t = p.read_text()
    for pat in STALE:
        for m in re.finditer(pat, t):
            print(f"STALE '{pat}' in {p.relative_to(H)}: …{t[max(0, m.start()-50):m.end()+30]!r}"); bad += 1
led = list(csv.DictReader(open(H / "claims_ledger.csv")))
print(f"claims ledger rows: {len(led)} | files scanned: {len(SCAN)} | problems: {bad}")
sys.exit(1 if bad else 0)
