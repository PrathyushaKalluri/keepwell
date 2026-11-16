# Keepwell 10-minute deck: the script, single source of truth.
# 16 slides, ~1,250 spoken words: about 10 minutes at a calm pitch pace, including clicks.
# SHOW = what is on screen (the proof). SAY = what is read out, word for word (the explanation).
# Every number traces to ../keepwell_model.xlsx or a step document in ../steps/.
# Illustrative case for the IIIT Hyderabad ESFS course pitch.

ACTS = [
    ("hook", "The hook"),
    ("team", "The team"),
    ("problem", "The problem"),
    ("keepwell", "Keepwell"),
    ("stage", "Where we are"),
    ("solution", "Circuit"),
    ("proof", "The proof"),
    ("win", "Why we win"),
    ("ask", "The ask"),
    ("future", "The future"),
]

SPEAKERS = {"P": "Prathyusha (CEO)", "S": "Sri Charan (CTO)", "K": "Kavyanth (COO)"}

SLIDES = [
dict(id="hook", act="hook", sp="P", t=40, title="Every repair in your home starts from zero",
 show="""An illustrated home with eight machines. The presenter taps each machine as the audience calls it out; a red counter adds up "repairs in your home this year". [click] Question tags drop onto every machine: "Last service? Which part? What did you pay?" [click] The line: "Every repair in your home starts from zero." """,
 say="""Before we begin, think about your own home. This year, what broke? The AC? The fridge? The purifier, the geyser? [tap the machines as people answer]
Now pick one. When was it last serviced? Which part was changed? What did you pay? [click]
Most of us don't know. It's in a phone, a diary, or nowhere. [click]
Every repair in your home starts from zero.""",
 why="The room answers before we say a word about ourselves, so the problem is theirs from the first 30 seconds."),

dict(id="ramagundam", act="hook", sp="P", t=55, title="We took it lightly too — until Ramagundam",
 show="""Left: Sri Charan's quote card, "Our machines cost my family ₹10,000 a month. Never evenly." Right, one beat per click: 46 °C and a fever → 14 missed calls → the son 700 km away → 2 nights in the heat → "Nobody is the villain. The system has no memory." The ₹350 / ₹38,000 detail is a small footnote in the last card.""",
 say="""We took this lightly too. Sri Charan's family spends about ten thousand rupees a month on its machines, and we called that normal. Then, Ramagundam. [click]
Forty-six degrees. A seventy-four-year-old retired miner, home alone, with a fever. His AC stops. [click] Ramesh, the one technician he trusts, is up a ladder across town. Fourteen missed calls. [click] His son, seven hundred kilometres away, calls everyone. Nobody knows what's wrong, or who's coming. [click] The old man spends two nights in that heat. [click]
The fault was a three-hundred-and-fifty-rupee part. Nobody was the villain. The system has no memory, and when it has no memory, it's people who suffer first.""",
 why="The hook is the human cost, not the money. One concrete story everyone can picture."),

dict(id="team", act="team", sp="P", t=40, title="Three founders, one from each side",
 show="""A triangle around "the machine record": Prathyusha (agency network: FixNear, 1,200 technicians, sold 2022), Sri Charan (household + AI: 7 years of voice AI, built Circuit), Kavyanth (brand + warranty: 300+ service partners, closed 8 of our last 10 agencies). Ribbon: full-time since May 2025 · ₹15 L of our own money · CIE-IIITH · DPIIT.""",
 say="""That afternoon is why the three of us are here, and each of us has lived one side of it. I'm Prathyusha. I co-founded FixNear, a network of twelve hundred technicians in these same towns, and sold it in 2022. Sri Charan spent seven years on Indian-language voice AI and built our product himself. Kavyanth ran a brand's network of three hundred service partners and its warranty desk. All three of us have been full-time since May 2025, with our own money in.""",
 why="Team is 45 of 90 points on the course matrix. Placed right after the story, the founders land as witnesses, each with one line of proof."),

dict(id="evidence", act="problem", sp="S", t=55, title="What we saw, and what we heard",
 show="""The proof wall: the real brand WhatsApp-bot recording playing ("API issue" → "My request was not done"), the agency sticker on a purifier with the date in marker, the repair diary, the gas cylinder, our whiteboard. Research chips: 19 survey responses · 7 household interviews · 18 agency owners. Three named quotes underneath. [click] Teal band: "Nothing in a repair can be checked, so people trust the person. We make that agency the smartest in town." 44% local · 76% avoid brand service.""",
 say="""I'm Sri Charan. We didn't read about this. We watched it. This is a real brand's WhatsApp bot, recorded in an interview: an "API issue", a job ID she doesn't have, and then, "my request was not done." And look at what families do instead: an agency's sticker on the purifier, the next date in marker, a handwritten repair diary.
We listened for four months: a survey, seven households, eighteen agency owners. [click] It all said one thing. Nothing in a repair can be checked, so people trust the person. Forty-four percent stay with their local agency. So we don't replace that agency. We make it the smartest one in town.""",
 why="Real evidence plus the insight, merged into one slide. The video playing does the work while the voice explains what it means."),

dict(id="problem", act="problem", sp="S", t=50, title="The problem, mapped and sized",
 show="""A row of five counters: 15 Cr repairs a year · 27 Cr machines with no record · ₹550 Cr wasted on repeat trips · 37,500 agencies on a notebook · 1 in 8 requests lost (55% got a defective machine, 21% made whole). Below: the top six problems as scored bars (intake chaos 24, unprepared visit 23, no history 22, claims 22, warranty refusal 20, no fair price 20) beside the five scenarios A–E, with A "Prepared Visit → Circuit · live" highlighted. [click] Band: "We enter where impact is highest and barriers lowest: the prepared visit." """,
 say="""Then we mapped the whole problem. Fourteen distinct problems across a machine's life: lost calls, blind first visits, no history, warranties nobody can prove. We scored each one, and they group into five scenarios.
And the scale is real. Fifteen crore repairs a year. Twenty-seven crore machines with no record. Five hundred and fifty crore rupees lost to repeat trips. Thirty-seven thousand five hundred agencies running on a phone and a notebook. [click]
We start where impact is highest and barriers lowest: the prepared visit.""",
 why="Problem map, both sides and scale in one picture. The numbers sit on screen while the voice gives the logic of where to start."),

dict(id="keepwell", act="keepwell", sp="S", t=40, title="Keepwell, and the roadmap",
 show="""Dark slide. Left: the Keepwell mark, "The care layer for everything a home owns", one living record per machine, and the chips CIBIL → borrowers · Carfax → used cars · Keepwell → household machines. Right: the roadmap as six rows, each with a payer: R1 Circuit (live) · R2 Home Memory + Plans · R3 Claims triage · R4 Parts · R5 Resale & recycling · Phase 3 Data services.""",
 say="""So we built Keepwell: one living record for every machine in an Indian home, built with the owner's consent. The CIBIL of household machines.
Each scenario becomes a product on that record, and each has its own payer. Circuit for repair agencies, live today. Then home memory and service plans, sold for insurers. Then claims, parts, and resale and recycling.""",
 why="The name, the vision and the roadmap land together, as the answer to the problem slide before it."),

dict(id="companystage", act="stage", sp="P", t=45, title="Where we are",
 show="""A three-step stage path, with "2 · Find the business model — we are here" highlighted. The journey timeline from discovery (Jan 2025) to raising the seed (Nov 2026), including the ₹30 L angel round. Three tiles: Raised ₹55 L → Spent ₹34 L (itemised) → In the bank ₹21 L. Strip: what it built.""",
 say="""Where are we? Stage two. The product works, customers pay, and now we're proving the business model.
Incorporated May 2025 at CIE-IIITH. Prototype by September. Thirty lakh from two operator angels, who also brought us our first agencies. A government seed grant, and fourteen paying agencies by October.
In total we've raised fifty-five lakh and spent thirty-four, mostly on modest stipends and pilots, and we have twenty-one lakh in the bank.""",
 why="Stage, journey, angels and money on one slide: four diligence questions answered before anyone asks."),

dict(id="circuit", act="solution", sp="S", t=55, title="Circuit, and how easy it is",
 show="""Left: six step cards (voice note → understands → fault + part → quote from the rate card → job card → technician verifies, we earn ₹40). Right: a browser frame with the live Circuit site (circuit-landing-page.netlify.app) scrolling end to end like a video. Bottom chips: no new app · 6 languages · set up in one visit · 30 free days · ₹40 only per verified fix · owner approves every quote.""",
 say="""Here's Circuit. A customer sends the agency a voice note on WhatsApp, in their own language. Circuit understands it and reads it back. It finds the likely fault and the part to carry, quotes from the agency's own price list for the owner to approve, and sends the technician a job card he can read in ten seconds.
When he verifies the fix, the record updates, Circuit learns, and only then do we earn forty rupees.
That's our live site on the right. There's no new app. It's set up in one visit, and the first thirty days are free.""",
 why="What it does, how simple it is, and the live site scrolling as the visual. No technical jargon."),

dict(id="proof", act="proof", sp="K", t=60, title="The proof",
 show="""Left: the price test, ₹40 → 2.0× value vs ₹100 → 0.81×, the quote "It takes too much of a small job", and the stamp "₹40 for everyone since May". Below it: 11 of 14 owners "very disappointed" without Circuit. Middle: 14 paying agencies · ~8,200 jobs · 71% → 83% one-visit · ~₹59k MRR. Right: the learning curve 62% → 78%, passing the 75% gate, with "since June: verified repairs" shaded.""",
 say="""I'm Kavyanth. First, we tested price: five agencies, forty rupees against a hundred per fix. At a hundred, one owner halved his usage. In his words, "it takes too much of a small job." At forty, agencies get twice the value they pay. So everyone pays forty.
Nine months in, fourteen agencies pay us and only one has left. That's eight thousand two hundred jobs, and one-visit fixes have gone from seventy-one to eighty-three percent.
And this curve matters most. Accuracy went from sixty-two to seventy-eight percent, and since June the gains come from repairs our technicians verified. No competitor has that data.""",
 why="Pilot, traction and the learning curve merged. The failed ₹100 arm builds trust, and the curve is the moat in production data."),

dict(id="engine", act="proof", sp="K", t=55, title="The agency wins. So do we.",
 show="""Value bars per agency per month: recovered jobs ₹2,400 + trips avoided ₹2,150 (measured) + owner time ₹2,925 (self-reported) vs our fee ₹3,690 (₹100 fee ₹9,225 crossed out). Four tiles: ₹4,216/mo revenue per agency · 81% contribution · 6.3-month payback · 6.3× LTV:CAC. Growth equation: field reps × ~80 agencies a year.""",
 say="""Does the agency win? From system logs alone, recovered jobs and saved trips are worth four and a half thousand rupees a month. That's more than our fee of thirty-seven hundred. With the owner's time, it's twice the fee.
And we win too. Each agency pays us about forty-two hundred rupees a month, at an eighty-one percent margin. It pays back in six months and is worth six times what it costs to win, on conservative assumptions.
Growth comes from capacity: I closed eight agencies part-time in six months. One full-time rep brings about eighty a year.""",
 why="Value to the customer, unit economics and growth in one engine slide. The voice gives the logic; the screen shows the bars and tiles."),

dict(id="whywin", act="win", sp="K", t=40, title="Why we win",
 show="""The competitor map: Urban Company, Servify, Zoho, Fieldproxy and Bernard each in their slice, with Keepwell pulsing alone in the "serves the agency × holds the lifetime record" corner. Right: one line per rival, then "No one can copy: 8,200+ verified outcomes · a record that follows the machine · licence signed by all 14 agencies · switching costs". The five forces in one line.""",
 say="""Why hasn't anyone solved this? Everyone holds a slice. Urban Company takes the customer. Servify serves brands. Field-service software is in English and priced per seat. Nobody serves the agency and holds the machine's history. That corner is ours.
Our moat isn't the AI, which can be copied in a quarter. It's eight thousand verified repair outcomes, a data licence signed by every agency, and switching costs that grow every month.""",
 why="Competition, moat and five forces compressed. The empty corner is the image investors remember."),

dict(id="howbig", act="win", sp="K", t=45, title="How big, and the plan",
 show="""Left: the funnel 37,500 → 22,500 → 1,400 → 120 (Series A gate), with the Keepwell earnable pool ₹1,005–2,370 Cr a year beneath. Right: the plan chart: paying agencies 79 → 264 → 945 → 2,196 → 3,793 with revenue ₹0.2 → 19.2 Cr and EBITDA, under the stage bands seed (Telangana + AP) · Series A (the south) · national.""",
 say="""How big? We counted India's repair agencies three ways: thirty-seven thousand five hundred, with twenty-two thousand five hundred in our Tier 2 and 3 segment.
This seed takes us to about two hundred and sixty agencies, and a Series A takes us south and then national. By year five, that's thirty-eight hundred agencies, nineteen crore in revenue, and profitable. And the record opens a pool of over a thousand crore a year in plans, parts and claims.""",
 why="Market and plan side by side, so every growth number can be checked against the market."),

dict(id="askneed", act="ask", sp="P", t=45, title="What we need",
 show="""The bridge chart: costed needs ₹548 L + 10% contingency − revenue − cash − grant due = gap ₹467 L → ask ₹475 L. Use of funds by purpose: product–market fit 38% · team 28% · product 23% · sales 10% · working capital 1%. A compliance strip: DPDP consent-first · IRDAI via licensed partners · CERT-In runbook · owner approves every quote · 0 safety incidents · ₹26 L budgeted.""",
 say="""Now, what we need. We costed every requirement for the next twenty-four months, added a buffer, and subtracted our revenue, our cash and the grant still due. The gap is four hundred and sixty-seven lakh. The biggest share, thirty-eight percent, goes to proving product–market fit.
Compliance is built in and budgeted: consent-first data kept in India, insurance sold only through licensed partners, and zero safety incidents.""",
 why="The requirement comes before the number, so the ask lands as a calculation. Compliance sits right before the ask as a reason to trust."),

dict(id="ask", act="ask", sp="P", t=50, title="The ask",
 show="""A full dark page: ₹4.75 Cr, "to take Circuit from 14 agencies to ~260, and reach the Series A from strength." The bridge line, then four terms: 24 months · ₹4.0 Cr minimum close · priced Seed CCPS · 20% to one lead. Three columns: what we have today · what your money proves (the Series A gates) · what comes next.""",
 say="""So here's our ask. Four point seven five crore rupees, for twenty percent, from one lead investor, as priced seed preference shares. That's twenty-four months of runway, and our minimum close is four crore.
Your money proves the Series A gates: a hundred and twenty paying agencies, forty thousand machine records, retention above ninety-seven percent, and our first warranty partner. At month twenty, we raise from strength, not need.""",
 why="The most important slide gets a full page: the amount, the instrument, the equity, the runway and what it proves."),

dict(id="future", act="future", sp="P", t=40, title="Why now, and who buys",
 show="""Four why-now tiles: ₹4.5 a job AI cost · only 1 in 10 homes has an AC · repair regulation · DPDP in May 2027. Path to ₹100 Cr (~₹66 Cr by year 8). Four acquirer cards: warranty & protection platforms (Asurion bought Domestic & General, ~£2.1 bn) · Urban Company · Cashify / Attero · global field-service software.""",
 say="""Why now? Indian-language AI just became cheap enough for a small shop. The repair wave is still ahead of us. And data law arrives in 2027, so the consent-first record built now becomes the standard.
The buyers already exist: warranty platforms, home services and recommerce. Asurion paid two billion pounds for a company like that. We'd expect a strategic sale in years six to eight.""",
 why="Urgency and the exit together: why invest now, and how the money comes back."),

dict(id="close", act="future", sp="P", t=35, title="Back to Ramagundam",
 show="""Dark slide. One click, and five green beats cascade on their own (answered in minutes · Circuit knows it's the capacitor · the part arrives the same afternoon · one visit, verified · a 74-year-old man sleeps in a cool room), then the line "Keepwell becomes the record everyone checks before touching a machine." Names and "Raising ₹4.75 Cr · Thank you". """,
 say="""[click, then let it play] Back to Ramagundam. With Keepwell, that voice note is answered in minutes. Circuit knows it's the capacitor. The technician arrives the same afternoon, with the part, and fixes it in one visit. And a seventy-four-year-old man sleeps in a cool room.
Keepwell becomes the record everyone checks before touching a machine. Thank you.""",
 why="It mirrors the opening and resolves the human story. One click, then stop talking."),
]

BACKUP = [
dict(id="b_valuation", title="Backup · Valuation (Q&A only)", sp="P", t=0,
 show="Comparable ₹24.8 Cr post · scorecard ₹24.1 Cr · VC method ₹24.2 Cr. Pitched ₹19 Cr pre / ₹23.75 Cr post, never above the VC-method price. Base-case investor IRR ~35% (6.2×).",
 say="Only if asked: 'Three course methods; we priced at the investor's own required-return price, so the base case clears 35%.'", why="Q&A only."),
dict(id="b_captable", title="Backup · Cap table (Q&A only)", sp="P", t=0,
 show="After seed: founders 67.9% · angels 2.1% · ESOP 10% · lead 20%. Founders 54.3% after A, 46.2% after B.",
 say="Only if asked: 'Founders keep a majority through the Series A.'", why="Q&A only."),
dict(id="b_terms", title="Backup · Terms (Q&A only)", sp="P", t=0,
 show="1× non-participating · broad-based weighted average · board 2+1+1 · vesting credit since May 2025 · deal costs capped at ₹8 L · lead reserves for the Series A.",
 say="Only if asked: 'Standard seed terms, with two asks: vesting credit and a Series A reserve.'", why="Q&A only."),
]
