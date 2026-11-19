"""Build the Keepwell story deck (index.html) and its script (SCRIPT.md) from one source.

    python3 build_story_deck.py

Inputs:  script_data.py (what we show / say / why, per slide) + deck_template.html (the visual layer)
Outputs: index.html (open in Chrome; press N for notes) and SCRIPT.md (show vs say, slide by slide)
"""
import importlib.util, json, re, pathlib

HERE = pathlib.Path(__file__).parent
spec = importlib.util.spec_from_file_location("d", HERE / "script_data.py")
d = importlib.util.module_from_spec(spec); spec.loader.exec_module(d)

WPM = 145  # calm pitch pace

def secs(sl):
    words = len(re.sub(r"\[.*?\]", "", sl["say"]).split())
    clicks = sl["say"].count("[click")
    extra = 25 if sl["id"] == "demo" else 0          # time to let the demo play
    extra += 10 if sl["id"] == "hook" else 0          # audience answers
    return round(words / WPM * 60 + 3 + clicks * 1.5 + extra)

def mmss(s): return f"{s // 60}:{s % 60:02d}"

# deck checks: every slide in the script exists in the template, and [click] counts match data-steps
tpl = (HERE / "deck_template.html").read_text()
steps = dict(re.findall(r'data-id="([a-z_]+)"[^>]*data-steps="(\d+)"', tpl))
problems = []
for sl in d.SLIDES:
    if sl["id"] not in steps:
        problems.append(f"missing slide in template: {sl['id']}")
    elif sl["say"].count("[click") != int(steps[sl["id"]]) and sl["id"] not in ("hook", "demo"):
        problems.append(f"{sl['id']}: {sl['say'].count('[click')} clicks in script vs data-steps={steps[sl['id']]}")
for p in problems: print("CHECK:", p)

notes = []
for sl in d.SLIDES + d.BACKUP:
    notes.append(dict(id=sl["id"], act=sl.get("act", ""), title=sl["title"], speaker=d.SPEAKERS[sl["sp"]],
                      time=mmss(secs(sl)) if sl.get("t") else "", say=sl["say"].strip(), why=sl["why"].strip()))
html = tpl.replace("/*__NOTES__*/[]", json.dumps(notes, ensure_ascii=False)).replace("/*__ACTS__*/[]", json.dumps(d.ACTS, ensure_ascii=False))
(HERE / "index.html").write_text(html)

# ---------------- SCRIPT.md
SHORT_CUT = {"porter", "whycircuit", "bothsides", "growth"}  # dropped or folded in the shorter version
acts = dict(d.ACTS)
total = sum(secs(s) for s in d.SLIDES)
short = sum(secs(s) for s in d.SLIDES if s["id"] not in SHORT_CUT)
by_sp = {}
for s in d.SLIDES: by_sp[s["sp"]] = by_sp.get(s["sp"], 0) + secs(s)

L = []
L.append("# Keepwell seed pitch: the story deck script")
L.append("> **Illustrative case.** Founder histories, the company timeline, the pilot results and the financials are assumptions made for the IIIT Hyderabad ESFS course pitch. The research, the household quotes, the photo and video evidence and the Circuit prototype are real.\n")
L.append("**Deck:** [`index.html`](index.html). Open it in Chrome and press **F** for full screen and **N** for these notes. **→ / space** moves to the next click, **←** goes back, **B** opens the backup slides (valuation, cap table, terms; Q&A only).")
L.append("**Generated** from [`script_data.py`](script_data.py) by [`build_story_deck.py`](build_story_deck.py), so the deck's speaker notes and this script are always the same words.\n")
L.append("## The rule for every slide: the screen proves, the voice explains")
L.append("- **SHOW** is the proof: a picture, a number, a real artefact, something to interact with. It is never read aloud.")
L.append("- **SAY** is the explanation: what it means and why it matters. It says what the screen can't.")
L.append("- When the two say the same thing, it's on purpose: only for the one line we want remembered (the hook, the insight, the ask, the close).")
L.append("- `[click]` in SAY means press → once to reveal the next part of the slide.\n")
L.append("## Timing and speakers")
L.append(f"- **Full story: {len(d.SLIDES)} slides, about {mmss(total)}** at a calm {WPM} words a minute, including clicks and the demo.")
L.append(f"- **Shorter version: about {mmss(short)}.** Drop or fold the slides marked ✂ into their neighbours ({', '.join(sorted(SHORT_CUT))}). For a hard 10–12 minute slot, also say only the first paragraph of each SAY block.")
for k, v in by_sp.items(): L.append(f"- **{d.SPEAKERS[k]}:** about {mmss(v)}")
L.append("\n**Hand-overs** are built into the words. Sri Charan starts with \"I'm Sri Charan.\" Kavyanth starts with \"I'm Kavyanth.\" Prathyusha takes the ask with \"So here's our ask.\"\n")
L.append("## Why the story runs in this order")
L.append("1. **The audience feels it before we explain it.** The hook makes them count their own repairs; Ramagundam makes the cost human — a sick old man nobody could help — with the money (₹350 vs ₹38,000) only a footnote.")
L.append("2. **The team lands as witnesses, not CVs:** the three people who each saw one side of that afternoon.")
L.append("3. **Proof we saw it ourselves:** the brand-bot recording playing live, the stickers, the diary — then four months of listening and the insight.")
L.append("4. **The full problem set before any product:** all 13 problems in plain words, grouped by who feels them, each tagged with the scenario that solves it, both sides of a repair, the whole life of a machine, and only then the 15-crore numbers.")
L.append("5. **Keepwell is named only after all of that**, so the name arrives as the answer.")
L.append("6. **The company stage next:** stage two, the journey, the angel round, raised → spent → in the bank, every rupee itemised.")
L.append("7. **The solution:** the roadmap from the problem map, why repair is the wedge, Circuit in six plain steps, then the demo with the live site scrolling like a video.")
L.append("8. **The proof chain:** price test (including the failure) → traction → the learning curve → value to the agency → unit economics → growth from capacity.")
L.append("9. **Why we win:** the empty corner, the moat, the five forces — then the market funnel and the stage-by-stage plan.")
L.append("10. **Trust and compliance sit immediately before the ask**, so the last thing heard before the number is that the company is clean and regulation-ready.")
L.append("11. **The ask shows the requirement first** (costed needs → the gap → use by purpose), and only then, on one click, the number and terms. Valuation, cap table and terms stay in backup.")
L.append("12. **Why now and who buys share the future slide**, and the close replays Ramagundam with Keepwell — one click, the beats cascade on their own.\n")

L.append("## Overview: show vs say")
L.append("| # | Act | Slide | Speaker | Time | What we SHOW (the proof) | What we SAY (the point) |")
L.append("|---|---|---|---|---|---|---|")
for i, s in enumerate(d.SLIDES, 1):
    show1 = re.sub(r"\s+", " ", s["show"]).split(". ")[0].replace("|", "/")[:150]
    say1 = re.sub(r"\[.*?\]", "", s["say"]).strip().split("\n")[0].split(". ")[0].replace("|", "/")[:120]
    cut = " ✂" if s["id"] in SHORT_CUT else ""
    L.append(f"| {i} | {acts[s['act']]} | **{s['title']}**{cut} | {d.SPEAKERS[s['sp']].split(' ')[0]} | {mmss(secs(s))} | {show1}… | “{say1}…” |")
L.append("")

L.append("## Slide by slide")
cur_act = None
for i, s in enumerate(d.SLIDES, 1):
    if s["act"] != cur_act:
        cur_act = s["act"]; L.append(f"\n---\n### Act: {acts[cur_act]}")
    cut = " ✂ *(short version: drop or fold in)*" if s["id"] in SHORT_CUT else ""
    L.append(f"\n#### {i}. {s['title']}{cut}")
    L.append(f"**Speaker:** {d.SPEAKERS[s['sp']]} · **Time:** ~{mmss(secs(s))}\n")
    L.append("| 🖥 SHOW (on screen, the proof) | 🎙 SAY (word for word, the explanation) |")
    L.append("|---|---|")
    show = s["show"].strip().replace("\n", "<br>").replace("|", "/")
    say = s["say"].strip().replace("\n", "<br><br>").replace("|", "/")
    L.append(f"| {show} | {say} |")
    L.append(f"\n**Why this works:** {s['why']}")

L.append("\n---\n## Backup slides (press B; Q&A only)")
for s in d.BACKUP:
    L.append(f"\n#### {s['title']}\n- **Show:** {s['show']}\n- **Say:** {s['say']}")

L.append("\n---\n## Before you present")
L.append("- **Media files** live in `media/`. They hold redacted real evidence, so they are kept out of the public GitHub repo. Copy the whole `story_deck/` folder to the presenting laptop.")
L.append("- **Fonts** load from Google Fonts. Open the deck once while online, or it falls back to Georgia and the system sans-serif.")
L.append("- **The demo tab** 'The Circuit website' loads `media/circuit_landing.html`. 'A real run' plays `media/circuit_live_run_30x.mp4`.")
L.append("- **Rehearse the five turning points word for word:** the hook (1), Ramagundam (2), the insight (5), the learning curve (18) and the ask (28).")
L.append("- **Never say** 'DPDP-compliant', 'AI diagnosis', or any number that isn't in the model.")
(HERE / "SCRIPT.md").write_text("\n".join(L) + "\n")
print(f"built index.html + SCRIPT.md · {len(d.SLIDES)} slides · full {mmss(total)} · short {mmss(short)}")
