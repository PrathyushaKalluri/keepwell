"""Build the Keepwell 10-minute deck (index.html) and its script (SCRIPT.md) from one source.

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
SHORT_CUT = set()  # this deck is already the 10-minute version
acts = dict(d.ACTS)
total = sum(secs(s) for s in d.SLIDES)
short = sum(secs(s) for s in d.SLIDES if s["id"] not in SHORT_CUT)
by_sp = {}
for s in d.SLIDES: by_sp[s["sp"]] = by_sp.get(s["sp"], 0) + secs(s)

L = []
L.append("# Keepwell seed pitch: the 10-minute deck script")
L.append("> **Illustrative case.** Founder histories, the company timeline, the pilot results and the financials are assumptions made for the IIIT Hyderabad ESFS course pitch. The research, the household quotes, the photo and video evidence and the Circuit prototype are real.\n")
L.append("**Deck:** [`index.html`](index.html). Open it in Chrome and press **F** for full screen and **N** for these notes. **→ / space** moves to the next click, **←** goes back, **B** opens the backup slides (valuation, cap table, terms; Q&A only).")
L.append("**Generated** from [`script_data.py`](script_data.py) by [`build_story_deck.py`](build_story_deck.py), so the deck's speaker notes and this script are always the same words.\n")
L.append("## The rule for every slide: the screen proves, the voice explains")
L.append("- **SHOW** is the proof: a picture, a number, a real artefact, something to interact with. It is never read aloud.")
L.append("- **SAY** is the explanation: what it means and why it matters. It says what the screen can't.")
L.append("- When the two say the same thing, it's on purpose: only for the one line we want remembered (the hook, the insight, the ask, the close).")
L.append("- `[click]` in SAY means press → once to reveal the next part of the slide.\n")
L.append("## Timing and speakers")
L.append(f"- **{len(d.SLIDES)} slides, about {mmss(total)}** at a calm {WPM} words a minute, including clicks. Built to fit a 10-minute slot.")
L.append("- **If you're running long:** say only the first paragraph of each SAY block on slides 6, 11 and 12; never cut slides 2, 9 and 14.")
for k, v in by_sp.items(): L.append(f"- **{d.SPEAKERS[k]}:** about {mmss(v)}")
L.append("\n**Hand-overs** are built into the words. Sri Charan starts with \"I'm Sri Charan.\" Kavyanth starts with \"I'm Kavyanth.\" Prathyusha takes the ask with \"So here's our ask.\"\n")
L.append("## How the 31-slide story became 16 slides without losing the crux")
L.append("| 10-minute slide | Carries these slides from the full deck |")
L.append("|---|---|")
for row in [("1 Hook","Hook"),("2 Ramagundam","Ramagundam"),("3 Team","Team"),("4 What we saw and heard","Evidence wall + listening + the insight"),("5 The problem, mapped and sized","Problem map + both sides + the 15-crore numbers (+ the whole-life idea in the speech)"),("6 Keepwell + roadmap","Keepwell + vision + roadmap"),("7 Where we are","Company stage, journey, angel round, money"),("8 Circuit","Why repair + Circuit's six steps + the live site + ease of use"),("9 The proof","Price test + traction + the learning curve"),("10 The engine","Value to the agency + unit economics + growth from capacity"),("11 Why we win","Competition map + moat + the five forces in one line"),("12 How big","Market funnel + the stage-by-stage plan"),("13 What we need","The requirement bridge + use of funds + compliance"),("14 The ask","The ask, on its own page"),("15 Why now + exit","Why now + path to Rs 100 Cr + who buys"),("16 Close","Back to Ramagundam")]:
    L.append(f"| {row[0]} | {row[1]} |")
L.append("")
L.append("**The rule on every slide:** the screen carries the numbers and the proof; the voice carries the logic. We never read the screen aloud, so two or three old slides fit into one.\n")

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
L.append("- **Media files** live in `media/`. They hold redacted real evidence, so they are kept out of the public GitHub repo. Copy the whole `story_deck_10min/` folder to the presenting laptop.")
L.append("- **Fonts** load from Google Fonts. Open the deck once while online, or it falls back to Georgia and the system sans-serif.")
L.append("- **The demo tab** 'The Circuit website' loads `media/circuit_landing.html`. 'A real run' plays `media/circuit_live_run_30x.mp4`.")
L.append("- **Rehearse word for word:** the hook (1), Ramagundam (2), the proof (9) and the ask (14). Time yourselves twice; the target is 9:30–10:00.")
L.append("- **Never say** 'DPDP-compliant', 'AI diagnosis', or any number that isn't in the model.")
(HERE / "SCRIPT.md").write_text("\n".join(L) + "\n")
print(f"built index.html + SCRIPT.md · {len(d.SLIDES)} slides · full {mmss(total)} · short {mmss(short)}")
