"""Build the 8-minute Keepwell story deck: index_8min.html + SCRIPT_8MIN.md.
    python3 build_8min.py
Visual engine (CSS, transitions, click-steps, notes panel, lightbox) is the v1 deck_template.html, as in build_story_deck.py.
Slides: slides_8min.html (12 slides + backup). Words: script_8min.py.
"""
import importlib.util, json, re, pathlib
HERE = pathlib.Path(__file__).parent
V1 = HERE.parent.parent / "pitch" / "archive" / "v1_agency" / "story_deck" / "deck_template.html"
spec = importlib.util.spec_from_file_location("d", HERE / "script_8min.py"); d = importlib.util.module_from_spec(spec); spec.loader.exec_module(d)
L = V1.read_text().split("\n")
head = "\n".join(L[:199]).replace("Keepwell · Seed Story", "Keepwell · Seed Story (8 minutes)")
hud = "\n".join(L[819:858])
js = "\n".join(L[858:]).split("// ---------- demo tabs + chat")[0] + "\n// start\nconst h0=parseInt(location.hash.slice(1));go(isNaN(h0)?0:h0-1);\n})();\n</script>\n</body>\n</html>"
tpl = head + "\n" + (HERE / "slides_8min.html").read_text() + "\n" + hud + "\n" + js
WPM = 150
def secs(s): return round(len(re.sub(r"\[.*?\]", "", s["say"]).split()) / WPM * 60 + 2 + s["say"].count("[click") * 1.5)
def mmss(x): return f"{x // 60}:{x % 60:02d}"
steps = dict(re.findall(r'data-id="([a-z_0-9]+)"[^>]*data-steps="(\d+)"', tpl))
main_ids = [m for m in re.findall(r'<section class="slide[^"]*" data-id="([a-z_0-9]+)"', tpl) if not m.startswith("b_")]
assert main_ids == [s["id"] for s in d.SLIDES], (main_ids, [s["id"] for s in d.SLIDES])
for s in d.SLIDES:
    if s["say"].count("[click") != int(steps[s["id"]]): print("CHECK clicks", s["id"], s["say"].count("[click"), steps[s["id"]])
notes = [dict(id=s["id"], act=s["act"], title=s["title"], speaker=d.SPEAKERS[s["sp"]], time=mmss(secs(s)) if "next" in s else "", say=s["say"].strip(),
              why=(s.get("why", "") + (" → Next: " + s["next"] if s.get("next") else "")).strip()) for s in d.SLIDES + d.BACKUP]
html = tpl.replace("/*__NOTES__*/[]", json.dumps(notes, ensure_ascii=False)).replace("/*__ACTS__*/[]", json.dumps(d.ACTS, ensure_ascii=False))
(HERE / "index_8min.html").write_text(html)
total = sum(secs(s) for s in d.SLIDES); acts = dict(d.ACTS); by = {}
for s in d.SLIDES: by[s["sp"]] = by.get(s["sp"], 0) + secs(s)
M = ["# Keepwell seed pitch: the 8-minute story deck, explained slide by slide", "",
     f"**Deck:** [`index_8min.html`](index_8min.html). Open it in Chrome. **F** goes full screen, **N** shows these notes, **→ / space** reveals the next click and **B** opens the backup slides for Q&A.",
     f"**Length:** {len(d.SLIDES)} slides, about **{mmss(total)}** at {WPM} words a minute.",
     "**Speaking time:** " + " · ".join(f"{d.SPEAKERS[k]} {mmss(v)}" for k, v in by.items()) + ".", "",
     "## How to use this script", "",
     "Each slide has five parts:", "",
     "| Part | What it is |", "|---|---|",
     "| **SHOW** | What is on screen. It is the proof, so never read it aloud. |",
     "| **SAY** | Word for word. `[click]` means press → once. |",
     "| **WHY** | The job this slide does in the story. |",
     "| **THEY SHOULD BELIEVE** | What the investor takes away when the slide ends. |",
     "| **BRIDGE** | The last line, which carries the room into the next slide. |", "",
     "**The screen and the voice do different jobs:** the screen proves and the voice explains. They repeat each other only once, on purpose, for the line we want remembered.", "",
     "## The story in one line per slide", "",
     "| # | Act | Slide | Speaker | Time | What the investor should believe |", "|---|---|---|---|---|---|"]
M += [f"| {i} | {acts[s['act']]} | {s['title']} | {d.SPEAKERS[s['sp']].split(' ')[0]} | {mmss(secs(s))} | {s['believe']} |" for i, s in enumerate(d.SLIDES, 1)]
M += ["", "## Why the story runs in this order", "",
      "1. **Feel it first (slides 1–2).** One shop owner's week, then the evidence and four numbers. The investor feels the problem before we name a product.",
      "2. **Trust the people (slide 3).** The team comes straight after the problem, as the people who lived it, with one network each.",
      "3. **The answer (slides 4–5).** Keepwell is named only now, as the answer to Ravi. One appliance's journey makes the product concrete.",
      "4. **Proof, then economics (slides 6–7).** The pilot comes first so the numbers explain something real. One slide carries both cluster profit and the plan's margin.",
      "5. **Why us, how big (slides 8–10).** The open lane, the market and the funded journey to exit.",
      "6. **The ask, then the close (slides 11–12).** The requirement comes before the number, the gate protects the investor, and we return to Ravi with the problem solved.", "",
      "## Slide by slide"]
for i, s in enumerate(d.SLIDES, 1):
    M += ["", f"### {i}. {s['title']}", f"**{d.SPEAKERS[s['sp']]}** · about {mmss(secs(s))} · act: {acts[s['act']]}", "",
          f"**SHOW (on screen):** {s['show']}", "",
          "**SAY (word for word):**", "", "> " + s["say"].strip().replace("\n", "\n>\n> "), "",
          f"**WHY this slide:** {s['why']}", "",
          f"**THEY SHOULD BELIEVE:** {s['believe']}", "",
          f"**BRIDGE:** *\"{s['next']}\"*" if not s["next"].startswith("(") else f"**BRIDGE:** {s['next']}"]
M += ["", "## Backup slides (press B; for Q&A only)", ""] + [f"- **{b['title']}:** {b['show']}" for b in d.BACKUP]
M += ["", "## Before you present", "",
      "- **Media:** the household photos and video live in `media/`. Copy the whole `story_deck/` folder to the presenting laptop.",
      "- **Fonts:** they load from Google Fonts, so open the deck once while online.",
      "- **Rehearse word for word:** slide 1 (the hook), slide 2's click line, slide 7's click line, slide 11 (the ask) and slide 12 (the close).",
      "- **Watch the clock:** if the timer passes 6:30 at slide 10, drop the last sentence of slide 10 and go straight to the ask."]
(HERE / "SCRIPT_8MIN.md").write_text("\n".join(M) + "\n")
print(f"built index_8min.html + SCRIPT_8MIN.md · {len(d.SLIDES)} slides · {mmss(total)} · " + ", ".join(f"{k} {mmss(v)}" for k, v in by.items()))
for s in d.SLIDES: print(f"  {s['id']:10s} {mmss(secs(s))} {len(re.sub(r'\\[.*?\\]','',s['say']).split())} words")
