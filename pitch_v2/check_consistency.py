"""Consistency check for the final (v4) pitch: the model vs every current output and the current step docs.
    python3 check_consistency.py
"""
import pathlib, re, sys, csv
H = pathlib.Path(__file__).parent
sys.path.insert(0, str(H / "model"))
import simple_model as S
pr, pt = S.pilot(); u = S.unit(); pl, need = S.plan(); d = S.deal()
canon = [("₹38 L", pt["revenue"] / 1e5, 38.0), ("₹9.9 L", pt["contribution"] / 1e5, 9.9), ("+₹1.9 L", pt["ebitda"] / 1e5, 1.9),
         ("₹5,070", pt["contrib_per_retailer_month"], 5070), ("20 retailers", pt["breakeven_retailers"], 20), ("₹51 L", u["cluster_ebitda"] / 1e5, 51),
         ("₹3.5 Cr", pl[0]["revenue"] / 1e7, 3.5), ("+₹0.13", pl[0]["ebitda"] / 1e7, 0.13), ("86.4", pl[4]["revenue"] / 1e7, 86.4),
         ("₹2.0 Cr", need / 1e7, 2.0), ("₹10 Cr", S.D["pre"] / 1e7, 10), ("₹254 Cr", d["ev"] / 1e7, 254), ("20×", d["multiple"], 20)]
bad = 0
for lab, v, ref in canon:
    if abs(v - ref) > max(0.06, abs(ref) * 0.02): print("MODEL DRIFT", lab, round(v, 3), "vs", ref); bad += 1
OUT = [H / "deck/deck_content.py", H / "story_deck/slides_8min.html", H / "story_deck/script_8min.py", H / "KEEPWELL_FULL_STORY.md", H / "steps/Entire story.md", H / "KEEPWELL_EXPLAINED.md"]
OUT += list((H / "proof_pack").glob("*.md")) + [H / f"steps/{f}" for f in ("07c_simple_model.md", "08_funding_needs_and_ask.md", "09_deal_valuation_exit.md", "11_fundability_score.md", "13_build_outputs.md", "12_storyboard_redteam.md")]
must = ["₹38.0 L", "₹9.9 L", "+₹1.9 L", "₹2.5 Cr", "₹10 Cr", "20 retailers"]
for p in OUT[:2]:
    t = p.read_text()
    for m in must:
        if m not in t: print(f"MISSING '{m}' in {p.name}"); bad += 1
STALE = [r"₹25 L", r"₹5 L contribution", r"₹4\.5k", r"130\.5", r"₹8 Cr pre", r"23\.8%", r"6\.6%", r"16\.3%", r"₹25 Cr pre", r"₹70 Cr pre", r"[Tt]ranche",
         r"\[Story", r"\[Real", r"[Ii]llustrative case", r"small-town appliance shop", r"Round 2 \(", r"month-18 milestones", r"₹1\.34 Cr", r"₹3,170", r"181\.6", r"1,580", r"2,400 jobs", r"₹410", r"₹1,430", r"from ₹550", r"\+₹4,000", r"\+₹3,900", r"₹3,300", r"× ₹2,300", r"1,480"]
for p in OUT:
    t = p.read_text()
    for pat in STALE:
        for m in re.finditer(pat, t):
            print(f"STALE '{pat}' in {p.relative_to(H)}: …{t[max(0, m.start()-50):m.end()+30]!r}"); bad += 1
led = list(csv.DictReader(open(H / "claims_ledger.csv")))
print(f"claims ledger rows: {len(led)} | files scanned: {len(OUT)} | problems: {bad}")
sys.exit(1 if bad else 0)
