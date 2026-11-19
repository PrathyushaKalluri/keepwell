"""Build the Keepwell v2 story deck: index.html (full), index_10min.html (short) and SCRIPT.md / SCRIPT_10MIN.md.
    python3 build_story_deck.py
The visual engine (CSS, navigation, notes, lightbox) is reused from pitch v1's deck_template.html; slides come from slides.html,
words from script_data.py.
"""
import importlib.util, json, re, pathlib
HERE = pathlib.Path(__file__).parent
V1 = HERE.parent.parent / "pitch" / "archive" / "v1_agency" / "story_deck" / "deck_template.html"
if not V1.exists(): V1 = HERE.parent.parent / "pitch" / "story_deck" / "deck_template.html"
spec = importlib.util.spec_from_file_location("d", HERE / "script_data.py"); d = importlib.util.module_from_spec(spec); spec.loader.exec_module(d)
L = V1.read_text().split("\n")
head = "\n".join(L[:199]).replace("Keepwell · Seed Story", "Keepwell · Seed Story (v2)")
hud_etc = "\n".join(L[819:858])
js_all = "\n".join(L[858:])
js = js_all.split("// ---------- demo tabs + chat")[0] + "\n// start\nconst h0=parseInt(location.hash.slice(1));go(isNaN(h0)?0:h0-1);\n})();\n</script>\n</body>\n</html>"
slides = (HERE / "slides.html").read_text()
(HERE / "deck_template.html").write_text(head + "\n" + slides + "\n" + hud_etc + "\n" + js)
WPM = 145
def secs(sl): return round(len(re.sub(r"\[.*?\]", "", sl["say"]).split()) / WPM * 60 + 3 + sl["say"].count("[click") * 1.5)
def mmss(s): return f"{s // 60}:{s % 60:02d}"
tpl = (HERE / "deck_template.html").read_text()
steps = dict(re.findall(r'data-id="([a-z_0-9]+)"[^>]*data-steps="(\d+)"', tpl))
for sl in d.SLIDES:
    if sl["id"] not in steps: print("CHECK: missing", sl["id"])
    elif sl["say"].count("[click") != int(steps[sl["id"]]): print("CHECK:", sl["id"], "clicks", sl["say"].count("[click"), "vs data-steps", steps[sl["id"]])
def build(short):
    keep = [s for s in d.SLIDES if not (short and s["id"] in d.SHORT_CUT)]
    notes = [dict(id=s["id"], act=s["act"], title=s["title"], speaker=d.SPEAKERS[s["sp"]], time=mmss(secs(s)) if s in d.SLIDES else "", say=s["say"].strip(), why=s["why"].strip()) for s in keep + d.BACKUP]
    html = tpl
    if short:
        for sid in d.SHORT_CUT:
            html = re.sub(r'<section class="slide[^"]*" data-id="%s".*?</section>\n' % sid, "", html, flags=re.S)
    html = html.replace("/*__NOTES__*/[]", json.dumps(notes, ensure_ascii=False)).replace("/*__ACTS__*/[]", json.dumps(d.ACTS, ensure_ascii=False))
    (HERE / ("index_10min.html" if short else "index.html")).write_text(html)
    total = sum(secs(s) for s in keep); acts = dict(d.ACTS)
    M = [f"# Keepwell seed pitch — story deck script ({'10-minute' if short else 'full'} version)",
         "> **Illustrative case** for the IIIT Hyderabad ESFS course pitch. Founder histories, the pilot results and the financials are [Story], generated from the same model as the plan. The household evidence and the research are real.\n",
         f"**Deck:** [`{'index_10min.html' if short else 'index.html'}`]({'index_10min.html' if short else 'index.html'}) — open in Chrome; **F** full screen, **N** notes, **→/space** next click, **B** backup slides (Q&A only).",
         "**Generated** from `script_data.py` by `build_story_deck.py` — the deck notes and this script are the same words.\n",
         "## Rule: the screen proves, the voice explains",
         "- **SHOW** is the proof on screen; never read it aloud. **SAY** is word-for-word. `[click]` = press → once.\n",
         f"## Timing\n- **{len(keep)} slides, about {mmss(total)}** at {WPM} words a minute."]
    by = {}
    for s in keep: by[s["sp"]] = by.get(s["sp"], 0) + secs(s)
    M += [f"- **{d.SPEAKERS[k]}:** about {mmss(v)}" for k, v in by.items()]
    if short: M.append(f"- Folded slides (in the full version only): {', '.join(sorted(d.SHORT_CUT))}. Their one key line is carried by the neighbouring slide's SAY.")
    M += ["\n## Overview", "| # | Act | Slide | Speaker | Time |", "|---|---|---|---|---|"]
    M += [f"| {i} | {acts[s['act']]} | {s['title']}{' ✂' if (not short and s['id'] in d.SHORT_CUT) else ''} | {d.SPEAKERS[s['sp']].split(' ')[0]} | {mmss(secs(s))} |" for i, s in enumerate(keep, 1)]
    M.append("\n## Slide by slide")
    for i, s in enumerate(keep, 1):
        M += [f"\n### {i}. {s['title']}", f"**Speaker:** {d.SPEAKERS[s['sp']]} · **Time:** ~{mmss(secs(s))}\n", "| 🖥 SHOW | 🎙 SAY |", "|---|---|",
              f"| {s['show'].strip().replace(chr(10), '<br>').replace('|', '/')} | {s['say'].strip().replace(chr(10), '<br><br>').replace('|', '/')} |", f"\n**Why:** {s['why']}"]
    M.append("\n## Backup slides (press B)")
    M += [f"- **{b['title']}:** {b['show']}" for b in d.BACKUP]
    M += ["\n## Before you present", "- `media/` holds redacted real household evidence and is kept out of the public repo. Copy the whole `story_deck/` folder to the presenting laptop.",
          "- Fonts load from Google Fonts; open once while online.", "- Never say 'insurance', 'AI diagnosis' or any number that is not in the model or the claims ledger."]
    (HERE / ("SCRIPT_10MIN.md" if short else "SCRIPT.md")).write_text("\n".join(M) + "\n")
    print(f"built {'10-min' if short else 'full'}: {len(keep)} slides, {mmss(total)}")
build(False); build(True)
