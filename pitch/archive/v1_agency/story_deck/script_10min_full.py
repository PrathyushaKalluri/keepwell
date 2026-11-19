"""10-minute read-out script for the FULL 31-slide deck (story_deck/index.html).

    python3 script_10min_full.py   ->  SCRIPT_10MIN.md

The deck itself is unchanged; its built-in speaker notes (press N) are the long version.
This is the tight version: ~950 spoken words over 31 slides, about 10 minutes including clicks.
[click] marks match each slide's builds in the deck.
"""
import re, pathlib

WPM = 145
SP = {"P": "Prathyusha (CEO)", "S": "Sri Charan (CTO)", "K": "Kavyanth (COO)"}

S = [
(1, "What broke in your home this year?", "P", 10,
 "Before we begin, think about your home. This year, what broke? The AC? The fridge? The purifier? [tap the machines as people answer] Now: when was it last serviced? Which part was changed? What did you pay? [click] Nobody knows. Every repair in your home starts from zero."),
(2, "Until one afternoon in Ramagundam", "P", 0,
 "We took this lightly too, until Ramagundam. [click] Forty-six degrees. A seventy-four-year-old man, home alone, with a fever. His AC stops. Ramesh, the one technician he trusts, is up a ladder. Fourteen missed calls. His son, seven hundred kilometres away, can't find anyone who knows anything. The old man spends two nights in that heat. The fault was a three-hundred-and-fifty-rupee part. Nobody was the villain. The system has no memory."),
(3, "Three founders, one from each side", "P", 0,
 "That's why we're here, and each of us has lived one side of it. I'm Prathyusha. I built and sold FixNear, a twelve-hundred-technician network in these towns. Sri Charan built Indian-language voice AI, and built our product. Kavyanth ran a brand's three-hundred-partner service network. We've all been full-time since May 2025."),
(4, "We watched it happen", "S", 0,
 "I'm Sri Charan. We watched this happen. This is a real brand's WhatsApp bot: an API issue, and then, \"my request was not done.\" So families fix it themselves, with agency stickers, repair diaries and dates in marker. The demand exists. The tool doesn't."),
(5, "We listened before we built", "S", 0,
 "We listened for four months: a survey, seven households and eighteen agency owners. Everyone said the same thing: you can't check the price or the part. [click] So people trust the person, not the work. We don't replace that agency. We make it the smartest in town."),
(6, "The problem map", "S", 0,
 "Here are all thirteen problems, in plain words: lost calls, blind first visits, wrong parts, no history, refused warranties, claims nobody can verify. Each letter is the solution that fixes it. [click] We start with A, the prepared visit, because it hurts most and is easiest to fix."),
(7, "Both sides", "S", 0,
 "For agencies, one request in eight is lost, and technicians go in blind. For households, nothing can be checked. Fifty-five percent got a defective machine, and only twenty-one percent were made whole."),
(8, "A machine's whole life", "S", 0,
 "And it happens at every stage: bought, repaired, resold, recycled. Each one starts from zero. [click] One missing record sits under all of it. Our vision: every machine cared for across its whole life."),
(9, "15 crore repairs a year", "S", 0,
 "At scale, that's fifteen crore repairs a year, twenty-seven crore machines with no record, five hundred and fifty crore rupees wasted on repeat trips, and thirty-seven thousand five hundred agencies running on a notebook."),
(10, "Keepwell", "S", 0,
 "So we built Keepwell: one living record per machine. The CIBIL of household machines."),
(11, "Where we are", "P", 0,
 "Where are we? Stage two: finding the business model. Incorporated May 2025, prototype by September, thirty lakh from two operator angels, a government seed grant, and fourteen paying agencies. We've raised fifty-five lakh, spent thirty-four, and have twenty-one in the bank."),
(12, "The roadmap", "S", 0,
 "Each scenario becomes a product on the same record: Circuit today, then home memory and plans, claims, parts and resale."),
(13, "Why repair", "S", 0,
 "We start at repair, where the pain, the payer and the truth meet. [click] That's Circuit."),
(14, "Circuit, simply", "S", 0,
 "A customer sends a voice note in their language. Circuit understands it, finds the likely fault and the part, quotes from the agency's price list, and sends the technician a job card. When he verifies the fix, the record updates, Circuit learns, and we earn forty rupees. That's our live site on the right."),
(15, "See how easy it is", "S", 8,
 "For the customer, nothing changes: same WhatsApp, same agency. [switch tab: the website] Here's the site, scrolling. Setting up takes one visit. The first thirty days are free, and after that the agency pays only per verified fix."),
(16, "The price test", "K", 0,
 "I'm Kavyanth. We tested price with five agencies: forty rupees against a hundred. [click] At a hundred, usage halved. At forty, agencies get twice the value they pay. So everyone pays forty."),
(17, "Nine months of paid use", "K", 0,
 "Nine months later: fourteen paying agencies, one churned. Eight thousand two hundred jobs. One-visit closures rose from seventy-one to eighty-three percent, and have held for six months."),
(18, "It learns", "K", 0,
 "And it learns. Accuracy rose from sixty-two to seventy-eight percent. [click] Since June, the gains come from verified repairs: data no competitor has."),
(19, "Does the agency win?", "K", 0,
 "Measured alone, agencies get forty-five hundred rupees of value for a thirty-seven-hundred-rupee fee. With the owner's time, it's twice the fee."),
(20, "Unit economics", "K", 0,
 "Per agency: about forty-two hundred rupees a month, at an eighty-one percent margin. It pays back in six months, and lifetime value is six times acquisition cost, on conservative assumptions."),
(21, "Growth from capacity", "K", 0,
 "Growth comes from capacity. I closed eight agencies part-time in six months, so one full-time rep brings about eighty a year."),
(22, "Competition", "K", 0,
 "Everyone holds a slice. Nobody serves the agency and holds the machine's history. That corner is ours."),
(23, "Why nobody can catch up", "K", 0,
 "The AI can be copied in a quarter. Eight thousand verified outcomes, a signed data licence and growing switching costs cannot."),
(24, "Five forces", "K", 0,
 "The strongest force is substitutes, and we run inside WhatsApp, so the substitute is our channel."),
(25, "The market", "K", 0,
 "Thirty-seven thousand five hundred agencies, twenty-two thousand five hundred in our segment, fourteen hundred in our home states. [click] And the record opens a pool of a thousand to two thousand four hundred crore."),
(26, "The plan", "K", 0,
 "The seed takes us to about two hundred and sixty agencies. A Series A takes us south, then national. By year five: thirty-eight hundred agencies, nineteen crore in revenue, and profitable."),
(27, "Trust and compliance", "S", 0,
 "Compliance is built in: consent-first data kept in India, insurance sold only through licensed partners, and zero safety incidents. Twenty-six lakh of it is budgeted."),
(28, "The requirement", "P", 0,
 "We costed every need for twenty-four months, then took out revenue, cash and grants. That leaves a gap of four hundred and sixty-seven lakh, and thirty-eight percent of it goes to proving product–market fit."),
(29, "The ask", "P", 0,
 "So we're raising four point seven five crore: twenty percent, for one lead investor, as priced seed preference shares, with twenty-four months of runway. It proves a hundred and twenty agencies, forty thousand records and our first warranty partner. Then we raise the Series A from strength."),
(30, "Why now, and who buys", "P", 0,
 "Why now? AI just got cheap, the repair wave is still ahead, and data law arrives in 2027. And the buyers already exist, most likely a warranty platform: Asurion paid two billion pounds for a company like this."),
(31, "Back to Ramagundam", "P", 0,
 "[click] With Keepwell, that voice note is answered in minutes, the right part arrives, and a seventy-four-year-old man sleeps in a cool room. Keepwell becomes the record everyone checks before touching a machine. Thank you."),
]

def secs(say, extra):
    words = len(re.sub(r"\[.*?\]", "", say).split())
    return round(words / WPM * 60 + 2 + say.count("[click") * 1.2 + extra), words

def mmss(s): return f"{s // 60}:{s % 60:02d}"

rows, total, tw, start = [], 0, 0, 0
for n, title, sp, extra, say in S:
    t, w = secs(say, extra); rows.append((n, title, sp, t, w, start, say)); start += t; total += t; tw += w

L = ["# Keepwell · the full 31-slide deck in 10 minutes: read-out script",
     "> **Illustrative case** for the IIIT Hyderabad ESFS course pitch. Research, quotes, evidence and the prototype are real; the timeline, pilot and financials are assumptions.\n",
     "**Deck:** [`index.html`](index.html), unchanged. Its built-in speaker notes (press **N**) are the long version. **This file is the 10-minute version.** Read it exactly as written.\n",
     f"**Total:** {len(S)} slides · {tw} spoken words · about **{mmss(total)}** at {WPM} words a minute, including clicks and the demo tab switch.\n",
     "## How to deliver it in 10 minutes",
     "- **The screen shows; you explain.** Don't read numbers off the slide. Say the one line here and move on. The slide carries the detail.",
     "- **`[click]`** means press → once. Every click here matches a build in the deck. With no `[click]`, press → once at the end to go to the next slide.",
     "- **Pace:** about 20 seconds a slide. Slides 2, 14, 29 and 31 get more time, and slides 10, 13, 22 and 24 get less.",
     "- **Hand-overs:** Sri Charan starts at slide 4 (\"I'm Sri Charan\"), Kavyanth at slide 16 (\"I'm Kavyanth\"), and Prathyusha takes back at slide 28.",
     "- **If you're running late:** on slides 7, 12, 21 and 24, say nothing extra. Just click through.\n",
     "## Running order",
     "| # | Slide | Speaker | Starts | Length |", "|---|---|---|---|---|"]
for n, title, sp, t, w, st, say in rows:
    L.append(f"| {n} | {title} | {SP[sp].split(' ')[0]} | {mmss(st)} | {mmss(t)} |")
L.append("\n## The script, word for word\n")
for n, title, sp, t, w, st, say in rows:
    L.append(f"### {n}. {title}  ·  {SP[sp]}  ·  {mmss(st)} → {mmss(st + t)}")
    L.append(f"> {say}\n")
pathlib.Path(__file__).with_name("SCRIPT_10MIN.md").write_text("\n".join(L) + "\n")
print(f"SCRIPT_10MIN.md · {len(S)} slides · {tw} words · {mmss(total)}")
