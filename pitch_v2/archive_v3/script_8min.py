# Keepwell 8-minute story deck: the script (single source). 12 slides, about 8 minutes at a calm pace.
# Drives the speaker notes in index_8min.html (press N) and SCRIPT_8MIN.md.
# SHOW = what is on screen (the proof). SAY = word for word (the explanation). WHY = what the slide must achieve.
# BELIEVE = what the investor should believe when the slide ends. NEXT = the bridge line into the next slide.
# Every number traces to ../keepwell_model.xlsx or ../steps/ (see ../claims_ledger.csv).
ACTS = [("hook", "The hook"), ("problem", "The problem"), ("team", "Why us"), ("keepwell", "Keepwell"), ("proof", "The proof"),
        ("win", "Why we win"), ("big", "How big"), ("ask", "The ask"), ("close", "The close")]
SPEAKERS = {"P": "Prathyusha (CEO)", "K": "Kavyanth (COO)", "S": "Sri Charan (CTO)"}
SLIDES = [
dict(id="thursday", act="hook", sp="P", title="He sells an AC on Monday. By Thursday, the customer is angry at him.",
 show="Four day-cards build left to right: Monday (Ravi sells a ₹38,000 AC to a family he has known for ten years), Tuesday–Wednesday (the brand's installer says 2–5 days; the family calls Ravi twice), Thursday in red (the family is at his counter, not the brand's), two years later (out of warranty; a mechanic guesses and keeps no record). [click] The punchline in large type: 'Ravi earns nothing after the sale — but he carries all the blame.'",
 say="""Meet Ravi. He runs a multi-brand appliance store in Guntur — a local retailer. On Monday he sells a thirty-eight-thousand-rupee AC to a family he has known for ten years. The brand's installer says two to five days, so the family calls Ravi — twice. On Thursday, in forty-degree heat, they are standing at his counter, not the brand's.
Two years later the AC fails. It's out of warranty. A mechanic guesses, charges what he likes and keeps no record.
[click] Ravi earns nothing after the sale. But he carries all the blame.""",
 why="Open on one person, not a statistic. In 40 seconds the investor feels the problem from the side that matters to us: the retailer.",
 believe="The retailer carries the after-sale problem without owning any of the solution.",
 next="And Ravi's story is not one retailer's bad week — it is how the whole system works."),
dict(id="problem", act="problem", sp="P", title="The retailer's promise ends at the counter",
 show="Left: a brand's WhatsApp bot failing (the video plays), an agency sticker with the next service date in marker, a family's handwritten repair diary. Right: four counters — 2–5 days for a brand install; 80–91% of machines out of warranty; 44% of AC service to local mechanics; 7 of 12 households keep no record. [click] 'The person the family trusts has no way to keep the promise he made.'",
 say="""We went into homes to see it. This is a brand's WhatsApp bot telling a customer there's an 'API related issue' — her last message: 'My request was not done.' Families keep their own records — a sticker, a diary, a date in marker.
The numbers say the same thing. Brand installs take two to five days. Eighty to ninety-one percent of machines in homes are out of warranty. Forty-four percent of AC service goes to local mechanics with no guarantee and no record.
[click] The person the family trusts has no way to keep the promise he made.""",
 why="Evidence the investor can see (the video, the diary) plus four sourced numbers. The click lands the one-line insight the company is built on.",
 believe="This is a large, everyday, unorganised problem — and families already want a record and a guarantee.",
 next="We know this market because each of us has lived one side of it."),
dict(id="team", act="team", sp="P", title="Between us, we already know this market by name",
 show="Three founder cards, each with one big number: Prathyusha — 600+ dealers; Kavyanth — 200+ service centres; Sri Charan — claims platforms. Advisors in one line underneath.",
 say="""I'm Prathyusha. For ten years I ran distribution to six hundred independent dealers in Andhra and Telangana — every one of them has a Ravi story. Kavyanth ran a brand's service network across two hundred service centres; he knows who has idle technicians in the monsoon. Sri Charan built claims verification at a device-protection company — the engine behind a plan sold at a counter.
Keepwell connects people who already trust us.""",
 why="The course gives the team the most weight. Each founder brings one network, and each network changes a number in the model (cheaper retailers, authorisation, plan fulfilment).",
 believe="This team can sign retailers, service centres and plan partners faster and cheaper than anyone else.",
 next="So here is what we built. Kavyanth."),
dict(id="keepwell", act="keepwell", sp="K", title="The retailer sells the promise. Keepwell keeps it.",
 show="Dark slide. Four offers the retailer now sells under its own name: authorised install in 24 hours; guaranteed repair and AMC; Keepwell Protect, a 2-year repair plan on the retailer's bill (highlighted); the appliance record. [click] Our vision in one sentence: 'Keepwell looks after every appliance a local retailer sells for its whole life: installed right, repaired with genuine parts, kept covered, and refurbished or recycled when its time is up.'",
 say="""I'm Kavyanth. Keepwell is the after-sale service arm of every local appliance retailer. The retailer sells the promise; we keep it.
An authorised install within a day, so the warranty is safe. Guaranteed repairs and AMC at a fixed rate card, for AC, fridge, washing machine and purifier. And Keepwell Protect — a two-year repair plan the retailer sells on its own bill.
[click] Our vision, in one sentence: Keepwell looks after every appliance a local retailer sells for its whole life — installed right, repaired with genuine parts, kept covered, and refurbished or recycled when its time is up.""",
 why="The name arrives as the answer to Ravi. The click lands the whole vision — from install to recycling — in one sentence, which the next slide then draws as a flowchart.",
 believe="The product is simple, sold through a channel that already exists, with a clear path to bigger layers.",
 next="Here's what that looks like across one appliance's whole life. Sri Charan."),
dict(id="lifecycle", act="keepwell", sp="S", title="From the retailer's bill to a second life — what Keepwell does at every step",
 show="A flowchart of one appliance's life. Row 1: 1 Sold (retailer adds install + Protect to the bill; consent; record starts) → 2 Installed (authorised technician in 24 h; warranty registered) → 3 In use (AMC, Protect cover, reminders) → 4 Breaks (Telugu voice note; AI triage) → 5 Diagnosed (rate card or Protect). [click] 'Worth repairing? Yes' → 6 Parts (Keepwell buys genuine parts centrally from distributors, stocks each cluster, sells to local agencies) → 7 Repaired (photo + OTP; 90-day guarantee; technician paid in 48 h) → back to In use. [click] 'No' → 8 Traded in (Keepwell's field arm values and collects; the retailer sells the replacement) → 9 Refurbished (resold through retailers with a warranty, back to Sold) or 10 Recycled (registered e-waste recyclers). The Know bar along the bottom: every step is written to one consented record → verified installs and claims for brands, leads for the retailer. Legend: Serve now · Supply from year 2 · Circulate from year 3.",
 say="""I'm Sri Charan. Here is one appliance's whole life with us. The retailer adds the install and Protect to the bill; the family consents on WhatsApp and the record starts. An authorised technician installs it within a day. Months later, a Telugu voice note — our AI desk drafts the likely fault and the part to carry.
[click] If it's worth repairing, we buy genuine parts centrally from distributors, fix it, close with a photo and an OTP, and it goes back into use.
[click] If it isn't, we collect it as a trade-in while the retailer sells the new one — and we refurbish it or send it to a registered recycler. Every step goes on one record.""",
 why="The flowchart shows the whole lifecycle and Keepwell's job at every step — sale, install, service, parts, repair, trade-in, refurbish, recycle — so the investor sees one company running the appliance's entire after-sale life, not a single repair app. The two clicks keep it readable: life, then repair, then end of life.",
 believe="Keepwell runs the appliance's entire after-sale life — and every step adds revenue and data on the same visit and record.",
 next="We ran this for eight months. Kavyanth."),
dict(id="pilot", act="proof", sp="K", title="Eight months, 34 retailers — and the retailers kept routing to us",
 show="Five counters: 34 retailers on 2-year exclusive agreements (33 active); ~2,400 jobs; ₹25 L revenue; ₹4.5k contribution per retailer a month by month 4; 6% Protect attach (teal). Underneath: what worked (74 units per retailer a month, 58% of installs routed, 87% installed in 24 h, 81% first-visit fix) and what it proves.",
 say="""We ran the pilot in Vijayawada–Guntur from March to October 2026. Thirty-four retailers signed two-year exclusive agreements, and thirty-three are still with us. About twenty-four hundred jobs, twenty-five lakh of revenue, and by month four each retailer contributed four and a half thousand rupees a month.
Retailers routed fifty-eight percent of installs to us; eighty-seven percent were done within a day. We missed some targets too — retailer signing lagged and one partner under-delivered — and we fixed both.
And when twelve retailers offered Protect at the counter, six percent of buyers took it.""",
 why="Traction before economics: the investor sees field proof first, with the misses stated, so the hits are believable.",
 believe="Retailers hand over the after-sale job when their name stays on it, and families buy a plan at the counter.",
 next="Here is why that turns into a business."),
dict(id="unitecon", act="proof", sp="K", title="Every cluster pays for itself — and the plan sells because we are the repairer",
 show="Left: one mature 60-retailer cluster — ₹2.72 Cr revenue, ₹44 L EBITDA (16%), breakeven 22 retailers (35 today), the retailer earns ₹3,170 a month. Right: one ₹2,000 Protect plan as bars — net ₹1,695; retailer keeps ₹424; repairs at our cost ₹593; Keepwell keeps ₹593. [click] Company line: EBITDA-positive in year 5; ₹130.5 Cr revenue and ₹8.6 Cr EBITDA in year 7; mature network 13.4%.",
 say="""Sixty retailers make a cluster. At maturity it earns two point seven crore of revenue and forty-four lakh of EBITDA — sixteen percent, on service. It breaks even at twenty-two retailers; on today's pilot numbers, thirty-five. The retailer earns about three thousand a month from us.
Protect is why the margin works: we're the repairer, so a two-thousand-rupee plan costs us about six hundred to honour, and we keep about six hundred.
[click] The company turns EBITDA-positive in year five and reaches a hundred and thirty crore of revenue in year seven.""",
 why="One slide carries the two numbers investors test first — cluster profit and the plan's margin — and the click links them to the company plan.",
 believe="The unit economics are positive on service, and Protect is a structural advantage, not a hope.",
 next="So why hasn't anyone else done this? Sri Charan."),
dict(id="nobody", act="win", sp="S", title="Everyone serves the chains or the brands. Nobody owns the local retailer.",
 show="Comparison table: Urban Company (metro households, takes the customer), Onsitego/Zopper (plans at chain counters; closest, no owned delivery in small towns, a possible partner), 247around/SERVIZ (brand-paid), Jeeves/resQ (captive), local mechanics (44%, no guarantee or record). Keepwell's row in teal: exclusive retailer agreements · density · authorisation · the record.",
 say="""Because everyone serves someone else. Urban Company serves metro households and takes the customer. Onsitego sells plans at chain counters — it's the closest, but it has no delivery of its own in small towns, so it could be our partner. 247around is paid by brands. Jeeves and resQ are captive. Local mechanics are everywhere — and they're our future technicians.
Nobody owns the local retailer's after-sale relationship. Our moat is exclusive retailer agreements, cluster density, authorisation — and a record that grows with every visit.""",
 why="Answers 'why hasn't X done this' with named players, and states the moat as operational facts, not technology.",
 believe="There is an open lane, and Keepwell's position in it gets harder to copy with every retailer signed.",
 next="And the lane is big. Prathyusha."),
dict(id="market", act="big", sp="P", title="₹4,000 Cr a year that no one organises",
 show="Bars: TAM ≈ ₹4,000 Cr (after-sale spend through local retailers, Tier 2/3) → SAM ≈ ₹1,040 Cr (five southern states) → beachhead ≈ ₹360 Cr (AP + TS) → year 7 ₹130 Cr (3,300 retailers, about 7% of India's local retailers).",
 say="""About four thousand crore a year of after-sale spend flows through the customers of independent Tier 2 and 3 retailers. The five southern states are about a thousand crore; Andhra and Telangana alone, three hundred and sixty.
By year seven we plan a hundred and thirty crore from thirty-three hundred retailers — about seven percent of India's local retailers, and about a quarter of the retailers in the towns we enter.""",
 why="Market after economics: the TAM reads as 'how far this repeats', and the year-7 share is small and believable.",
 believe="The plan needs a modest share of a large, unorganised market.",
 next="Here is how we get there, one round at a time. Kavyanth."),
dict(id="journey", act="big", sp="K", title="Serve → Supply → Know → Circulate. Each round raised on proof.",
 show="Revenue bars, years 1–8 (₹2.4 Cr → ₹181.6 Cr) with EBITDA under each (−1.1 … +15.3). [click] Four round cards: Seed now ₹2.5 Cr at ₹8 Cr pre (Serve, 4 clusters); Round 2 H2 2028 ₹5 Cr at ₹25 Cr pre (Supply — service centres run partner clusters); Round 3 2030 ₹15 Cr at ₹70 Cr pre (scale to 72 clusters); exit 2033–34, EV ₹255–376 Cr.",
 say="""Revenue grows from two crore next year to a hundred and thirty crore in year seven.
[click] And it's funded one step at a time, each raised on proof. The seed proves Serve in four clusters. Round two funds central parts buying, and from year three existing service centres run our new clusters as partners — that's how we grow without hiring a team in every town. Round three scales to seventy-two clusters. And in 2033 or 34, a strategic buyer or PE — an enterprise value of two hundred and fifty-five to three hundred and seventy-six crore.""",
 why="Shows the vision and the later rounds without asking for them now — we only ask for the next proof.",
 believe="There is a clear, capital-light path from today's pilot to an exit, and each round is priced on evidence.",
 next="Which brings us to today's ask. Prathyusha."),
dict(id="ask", act="ask", sp="P", title="₹2.5 Cr · one close · 18 months",
 show="Dark slide. Three cards: ₹2.5 Cr CCPS (a single close before the term sheet); ₹8 Cr pre-money (23.8%); 18 months from close (one-year need ₹1.34 Cr + six months to raise Round 2). [click] The month-9 board checkpoint (Dec 2027) and the month-18 case for Round 2 (Sep 2028). A clean-company line underneath.",
 say="""So here's our ask: two and a half crore, as CCPS, at an eight crore pre-money valuation — the value the course's own scorecard gives, inside what comparable seed rounds pay.
We sized it the course's way: one year of need from the close is one point three four crore; add six months to raise the next round, and a small buffer.
[click] It's a single close. At month nine, after the first AC season, the board checks five numbers — units per retailer, the pilot cluster paying for its own team, Protect sales, the legal opinion and authorisation — before we expand further. By month eighteen: four clusters, two hundred retailers — the case for Round 2.""",
 why="Requirement first, then the number. The month-9 board checkpoint is the investor's protection; the clean-company line answers compliance before Q&A.",
 believe="The ask is sized by method, priced fairly, and the board can stop expansion at month 9 if the numbers miss.",
 next="Let's go back to Ravi."),
dict(id="close", act="close", sp="P", title="Keepwell keeps the promise the retailer made",
 show="Dark slide. [click] Ravi's week again, with Keepwell: Monday, install and Protect on the same bill; Tuesday, an authorised install, warranty safe; two years later, a Telugu voice note and a covered fix the same week; Ravi earns on the plan and the family comes back to his retailer.",
 say="""Let's go back to Ravi.
[click] Monday, he sells the AC — with the install and Protect on the same bill. Tuesday, an authorised technician installs it. Two years later, a voice note in Telugu, and a covered fix the same week. Ravi earns on the plan, and the family comes back to his retailer.
Keepwell keeps the promise the retailer made when it sold the appliance. Thank you.""",
 why="The close replays the hook with the problem solved, so the room leaves with one picture and one line.",
 believe="This is a company worth backing: a real problem, a working answer, a team that can scale it.",
 next="(Q&A — press B for the backup slides.)"),
]
BACKUP = [
 dict(id="b_valuation", title="Valuation", show="Course scorecard ₹8.2 Cr pre; comparables ₹6–12 Cr pre; VC method ≤ ₹13.5 Cr post (stress, 40% IRR); our price ₹8 Cr pre / ₹10.5 Cr post.", say="The course scorecard value, inside comparables, well under the VC-method ceiling.", why="", sp="P", act="ask"),
 dict(id="b_captable", title="Cap table and returns", show="Founders 60.5% → 41.5% after Round 3; seed 23.8% → 16.3%; returns 6.9× (year 5, stress) to 24.6× (year 7, BASE).", say="Founders keep control through Round 2 and about 41% after Round 3.", why="", sp="K", act="ask"),
 dict(id="b_scen", title="Scenarios", show="BASE / stress / LOW: year-7 revenue, EBITDA, first positive year, peak cash need, what we do.", say="We plan on stress; the worst case fails the month-9 checkpoint and expansion stops with about ₹1 Cr in hand.", why="", sp="K", act="ask"),
 dict(id="b_terms", title="Key terms", show="CCPS, single close, 1x non-participating, broad-based weighted-average anti-dilution, 3-person board, vesting from Aug 2025, ESOP 10%.", say="The course CCPS template, adapted for a seed.", why="", sp="P", act="ask"),
]
