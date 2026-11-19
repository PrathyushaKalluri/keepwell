# Keepwell v2 story deck: the script (single source). Drives the speaker notes in index.html (press N) and SCRIPT.md.
# SHOW = what is on screen (proof). SAY = what the speaker says. Every number traces to ../keepwell_model.xlsx or ../steps/.
ACTS = [("hook", "The hook"), ("problem", "The problem"), ("team", "Why us"), ("keepwell", "Keepwell"), ("proof", "The proof"),
        ("win", "Why we win"), ("big", "How big"), ("ask", "The ask"), ("close", "The close")]
SPEAKERS = {"P": "Prathyusha (CEO)", "K": "Kavyanth (COO)", "S": "Sri Charan (CTO)"}
SHORT_CUT = {"aidesk", "misses", "partners", "clean"}   # folded into neighbours in the 10-minute version
SLIDES = [
dict(id="thursday", act="hook", sp="P", t=1, title="He sells an AC on Monday. By Thursday, the customer is angry at him.",
 show="Four day-cards build left to right: Monday (the sale), Tuesday–Wednesday (installer '2–5 days'), Thursday in red (the family at his counter), two years later (out of warranty, a mechanic guesses). [click] The punchline: 'Ravi earns nothing after the sale — but he carries all the blame.'",
 say="""Meet Ravi. He runs a multi-brand appliance shop in Guntur. On Monday he sells a thirty-eight-thousand-rupee AC to a family he has known for ten years.
The brand's installer says two to five days. So the family calls Ravi. Then calls again. And on Thursday, in forty-degree heat, they are standing at his counter — not the brand's.
Two years later the AC fails. It's out of warranty. A local mechanic guesses, charges what he likes, and keeps no record.
[click] Ravi earns nothing after the sale. But he carries all the blame.""",
 why="Open on a person, not a statistic: the investor feels the shop's problem in 45 seconds. Ravi is drawn from the shop owners we met in discovery; every fact on his cards is sourced in Step 4."),
dict(id="evidence", act="hook", sp="P", t=1, title="Families are already building the appliance's memory",
 show="A proof wall of real artefacts from our household research: a brand's WhatsApp bot failing (video plays), an agency sticker with the next date in marker, a handwritten repair diary, a gas cylinder with its refill date. Click any to open full screen.",
 say="""We didn't read about this. We watched it in real homes.
This is a brand's WhatsApp bot, recorded in one of our interviews. It says 'API related issue'. Her last message: 'My request was not done.'
And look what families do instead. A local agency's sticker, with the next service date in marker. A handwritten diary of every repair. A refill date written on the cylinder.
People are already building the appliance's memory — on paper. The demand is there. Nobody is serving it.""",
 why="First-hand evidence is the trust moment for the problem. It also shows the record is something families already want."),
dict(id="problem", act="problem", sp="P", t=1, title="The shop's promise ends at the counter",
 show="Four red counters: 2–5 days for a brand install; 80–91% of the installed base out of warranty; 44% of AC service to local mechanics; 7 of 12 households keep no record. Under them: shops net 2–3% and have been held jointly liable by consumer commissions.",
 say="""Here's the system Ravi lives in. Brand installs take two to five days. Eighty to ninety-one percent of machines in homes are already out of warranty. Forty-four percent of AC service goes to local mechanics — no guarantee, no GST, no record. Seven of the twelve households we surveyed keep no record at all.
And the shop makes two to three percent net, earns nothing after the sale — and consumer commissions have held sellers jointly liable with brands.
The person the family trusts has no way to keep the promise he made at the counter.""",
 why="Four numbers, each sourced (Step 4 §4.6). The last line is the insight the whole company is built on."),
dict(id="team", act="team", sp="P", t=1, title="Between us, we already know this market by name",
 show="Three founder cards, each with one big number: Prathyusha — 600+ dealers; Kavyanth — 200+ service centres; Sri Charan — claims platforms. Advisors underneath.",
 say="""We're the three people who saw this from three sides.
I'm Prathyusha. For ten years I ran distribution to six hundred independent dealers in Andhra and Telangana. Every one of them has a Ravi story.
Kavyanth ran a brand's service network across two hundred service centres — he knows how authorisation is granted, and who has idle technicians in the monsoon.
Sri Charan built claims verification at a device-protection platform — exactly the engine behind a plan sold at a counter.
Between us, we already know the shops, the service centres and the plan sellers in this market. Keepwell connects people who already trust us.""",
 why="Course M3 weights the team at half the score. The networks are the X-factor and they change the model (shop cost ₹9.5k warm vs ₹22k cold). Employers are described by type only."),
dict(id="keepwell", act="keepwell", sp="K", t=1, title="The shop sells the promise. Keepwell keeps it.",
 show="Dark slide. Four offers the shop now sells: authorised install in 24 h; guaranteed repair & AMC; Keepwell Protect (2-year repair plan, ~₹2,000) highlighted; the appliance record. [click] The four phases: Serve (now) → Supply → Know → Circulate.",
 say="""I'm Kavyanth. Keepwell is the after-sale service arm of every small-town appliance shop.
The shop sells the promise; we keep it. An authorised install within twenty-four hours, so the warranty is safe. Guaranteed repairs and AMC at a fixed rate card, for the AC, fridge, washing machine and purifier. And Keepwell Protect — a two-year repair plan the shop sells on its own bill. Every visit goes on one consented record.
All of it under the shop's name, delivered by certified local technicians.
[click] We start by serving. Then we supply parts and run partner clusters, then the record lets brands verify installs and claims, and finally we give appliances a second life.""",
 why="The name arrives as the answer to Ravi. Protect is highlighted because it turns the shop's promise into a product with a price (Step 7b)."),
dict(id="job", act="keepwell", sp="S", t=1, title="From the shop's bill to a guaranteed fix",
 show="Six step cards: Sale → Record → Install → Ask (a Telugu voice note) → Triage (AI drafts fault + part, checks cover) → Fix & verify (photo + OTP close, record updates), the last in teal.",
 say="""I'm Sri Charan. Here's one appliance's life with us.
At the sale, the shop adds the install and Protect to the bill, and the family consents on WhatsApp. We read the model, serial and invoice from photos and issue the plan. An authorised technician installs within a day.
Months later, a voice note in Telugu: 'AC not cooling'. Our AI desk drafts the likely fault and the part to carry, and checks the plan cover. The technician confirms the real fault, closes with a photo and an OTP, and the record updates.
That last step matters: a verified fix is what makes the record worth trusting.""",
 why="One job end-to-end makes the product concrete. The verify step links service to the Know layer (verification revenue)."),
dict(id="aidesk", act="keepwell", sp="S", t=1, title="AI reads and drafts. Rules and people decide.",
 show="Two columns: what the AI does (voice notes, photos, likely fault, dispatch) and what is never the AI's call (prices, safety stops, claim rejections, data sharing).",
 say="""The AI is our cost engine, not our moat. It understands voice notes, reads photos, drafts the fault and dispatches — so one coordinator can run a sixty-shop cluster.
But prices always come from the rate card, gas and high-voltage stops are hard rules, a person decides any claim rejection or refund, and data is shared only with consent.""",
 why="Investors ask 'what does the AI actually do, and where can it hurt someone?' This answers both in 30 seconds. ✂ in the 10-minute version."),
dict(id="pilot", act="proof", sp="K", t=1, title="Eight months, 34 shops — and the shops kept routing to us",
 show="Five counters: 34 shops on 2-year exclusive agreements; ~2,400 jobs; ₹25 L revenue; ₹4.5k contribution per shop by month 4; 6% Protect attach (teal). What worked / what it proves underneath. ",
 say="""We ran the pilot in Vijayawada–Guntur from March to October 2026.
Thirty-four shops signed two-year exclusive agreements, and thirty-three are still with us. About twenty-four hundred jobs — seven hundred and seventy-five installs, thirteen hundred service and repair. Twenty-five lakh of revenue. By month four, each shop was contributing four and a half thousand rupees a month.
Shops sold seventy-four units a month and routed fifty-eight percent of installs to us. Eighty-seven percent were installed within a day.
And in the last eight weeks of the summer we let twelve shops sell Protect at the counter. Six percent of buyers took it. That's the moment we knew the shop could sell the promise.""",
 why="Traction before economics: the investor sees field proof first (Step 6), then the economics explains it."),
dict(id="misses", act="proof", sp="K", t=1, title="Four misses — and what we changed",
 show="Table: shop signing lagged; one sub-contract partner under-delivered; 2.6 jobs/technician-day; plan-seller jobs 70 vs 100 — with the fix for each. Breakeven on pilot economics: about 35 shops.",
 say="""We missed four targets. Shop signing lagged, so we added a second field executive. One of our two service-centre partners under-delivered, so we opened talks with a third. Technicians did two-point-six jobs a day, not two-point-eight, until we re-zoned dispatch. And the plan seller sent seventy jobs a month, not a hundred — we widened that contract.
On today's pilot economics a cluster breaks even at about thirty-five shops. That's why density is our first milestone.""",
 why="Showing the misses is what makes the hits believable. ✂ in the 10-minute version (one line moves to the pilot slide)."),
dict(id="unitecon", act="proof", sp="K", t=1, title="Every cluster pays for itself — on service",
 show="Three tables: a mature shop (₹3.5 L service + ₹0.9 L Protect; ₹1.16 L contribution; shop earns ₹3,170/month); a 60-shop cluster (₹2.72 Cr revenue, ₹44 L EBITDA, 16%, breakeven 22 shops); the company (positive year 5; year 7 ₹130.5 Cr at 6.6%; mature network 13.4%, 9.1% on service alone).",
 say="""Here are the economics at maturity, from our model.
A mature shop brings three and a half lakh of service a year, plus about ninety thousand of Protect plans — one point one six lakh of contribution. The shop itself earns about three thousand a month from us, up from seventeen hundred today, because we pay it for the sale it controls.
Sixty shops make a cluster: two point seven crore of revenue and forty-four lakh of EBITDA — sixteen percent — on service. It breaks even at twenty-two shops.
The company turns EBITDA-positive in year five. While we're opening fifteen clusters a year, data like verified installs is what tips the company into profit. At maturity the network runs at thirteen percent, nine of it from service alone.""",
 why="The honest version (Step 7b, red-team fixed): clusters profit on service; data carries the growing company; at maturity service stands alone."),
dict(id="protect", act="proof", sp="S", t=1, title="We can sell repair cheaply because we are the repairer",
 show="A bar waterfall for one plan: net ₹1,695 → shop 25% ₹424 → claims at our cost 35% ₹593 → admin ₹85 → Keepwell keeps ₹593. Two cards: 'A service contract, not insurance' and 'Claims ~27% on our own data; we carry 35%; planning case 45%'.",
 say="""Why can we sell a plan that chains sell through insurers? Because we're the repairer.
Of a two-thousand-rupee plan, about seventeen hundred is net of GST. The shop keeps a quarter. Repairs, at our own cost, run about twenty-seven percent on our own failure data — we carry thirty-five, and our planning case uses forty-five. We keep about six hundred rupees a plan.
It's a repairs-only service contract we deliver ourselves — not insurance — and the expected claims on every unexpired plan sit in a ring-fenced reserve.""",
 why="Protect is the biggest lever in the redesign; this answers the two questions investors ask first: margin and regulation."),
dict(id="nobody", act="win", sp="S", t=1, title="Nobody owns the independent shop",
 show="Comparison table: Urban Company, Onsitego/Zopper, 247around/SERVIZ, Jeeves/resQ, local mechanics — and why none serves the independent shop. Keepwell's row in teal: exclusive shop agreements, density, authorisation, the record.",
 say="""So why hasn't someone done this? Because everyone serves someone else.
Urban Company serves metro households and takes the customer. Onsitego and Zopper sell plans at chain counters but don't own delivery in small towns. 247around is paid by brands. Jeeves and resQ are captive to their own retailers. Local mechanics are everywhere — and they're our future technicians.
Nobody owns the independent shop's after-sale relationship. Onsitego is the closest — and could be a partner. Our moat is the exclusive shop agreements, the density, the authorisation — and the record that compounds with every visit.""",
 why="Answers the skeptic's 'why hasn't X done this' with sourced positions (Step 5)."),
dict(id="partners", act="win", sp="K", t=1, title="Service centres run our clusters from year 3",
 show="Two cards: the partner (existing service centre: coordinator, premises, technicians; 10% fee ~₹21 L a year; fills idle capacity) and Keepwell (shops, customer, payment, Protect, parts, AI; ₹1 L a month per cluster; ₹38 L EBITDA, 14%). Line: Kavyanth knows 200+ owners; 66 needed by year 8.",
 say="""How do we grow without hiring sixty cluster teams? From year three, existing service centres run our clusters. They already have the manager, the premises and technicians who sit idle in the monsoon. They earn ten percent of the cluster's service revenue — about twenty-one lakh a year — plus their technicians' pay.
We keep the shops, the customer, the payment, Protect and the record — at a lakh a month per cluster instead of a twenty-three-lakh team. I know the owners of over two hundred of these centres. We need sixty-six by year eight.""",
 why="Partners buy speed and capital efficiency, not margin — said plainly. ✂ in the 10-minute version (one line moves to the journey slide)."),
dict(id="market", act="big", sp="P", t=1, title="₹4,000 Cr a year that no one organises",
 show="Bars: TAM ≈ ₹4,000 Cr (after-sale spend via independent shops, Tier 2/3) → SAM ≈ ₹1,040 Cr (five southern states) → beachhead ≈ ₹360 Cr (AP + TS) → year 7 ₹130 Cr (3,300 shops, ~7% of India's 45k independent shops).",
 say="""How big can this get? About four thousand crore a year of after-sale spend flows through the customers of independent Tier 2 and 3 shops — built from units sold, and cross-checked against households.
The five southern states are about a thousand crore; Andhra and Telangana, three hundred and sixty.
By year seven we plan a hundred and thirty crore from thirty-three hundred shops — about seven percent of India's independent shops. In the towns we enter, that's about a quarter of the shops. Density, not national share, is our test.""",
 why="Market after economics: the TAM lands as 'how far this repeats' (Step 4)."),
dict(id="journey", act="big", sp="K", t=1, title="Serve → Supply → Know → Circulate. Each round raised on proof.",
 show="Revenue bars, years 1–8 (2.4 → 181.6 ₹ Cr) with EBITDA under each (−1.1 … +15.3). [click] Four round cards: Seed now ₹2.5 Cr (Serve, 4 clusters); Round 2 H2 2028 ₹5 Cr (Supply, partners, verification); Round 3 2030 ₹15 Cr (scale to 72 clusters, Know + Circulate); exit 2033–34, EV ₹255–376 Cr.",
 say="""Here's the journey. Revenue grows from two crore next year to a hundred and thirty crore in year seven, EBITDA-positive from year five.
[click] And here's how it's funded — one step at a time, each raised on proof. The seed proves Serve in four clusters. Round two, in the second half of 2028, funds central parts and the first partner clusters. Round three, in 2030, scales to seventy-two clusters and adds the data and circular layers. And in 2033 or 34, a strategic buyer or PE — an enterprise value of two hundred and fifty-five to three hundred and seventy-six crore.""",
 why="Shows the vision and the future rounds without asking for them now — our rule, and the course's: ask only for the next proof."),
dict(id="clean", act="ask", sp="S", t=1, title="Three questions we answer before you ask",
 show="Three cards: Is Protect insurance? (no — repairs-only service contract, reserve, legal opinion = milestone); Are technicians employees? (per-job partners, gig levy 1.4%, accident cover); Do installs void warranties? (authorised only, sub-contracts renewed for 2027). Hygiene line underneath.",
 say="""Before the ask, three questions you'd ask us.
Is Protect insurance? No — a repairs-only service contract we deliver ourselves, on counsel-reviewed terms, with claims ring-fenced; the formal opinion comes by month six. Are technicians employees? They're per-job partners; we pay the gig-worker levy and carry accident cover. Do our installs void warranties? No — we install only under authorised sub-contracts, renewed for 2027, and a brand has signed a letter of intent for direct authorisation.""",
 why="Course M3 pillar 3: the last thing heard before the number is that the company is clean. ✂ in the 10-minute version."),
dict(id="ask", act="ask", sp="P", t=1, title="₹2.5 Cr · two tranches · 18 months",
 show="Dark slide. Three cards: ₹2.5 Cr CCPS (₹1.75 Cr at close + ₹0.75 Cr at the month-9 gate); ₹8 Cr pre-money (23.8%); 18 months from close (one-year need ₹1.34 Cr + six months to raise Round 2). [click] The month-9 gate that releases tranche 2, and the month-18 case for Round 2.",
 say="""So here's our ask. Two and a half crore, as CCPS, at an eight crore pre-money valuation — the value the course's own scorecard gives us, and inside what comparable seed rounds pay.
We sized it the way the course teaches: our one-year need from the close is one point three four crore; add six months to raise the next round on proof, and a small contingency, and you get two and a half.
[click] It comes in two tranches: one seventy-five at close, and the last seventy-five lakh only at month nine, after the first AC season — if shops sell sixty-five units a month, the pilot cluster pays for its own team, Protect sells and the legal opinion is in hand. By month eighteen: four clusters, two hundred shops and a run-rate of four and a half crore or more — the case for Round 2. If we're on plan, you'll see it at month nine.""",
 why="Requirement first, then the number; the tranche gate turns our checkpoint into the investor's protection (Steps 8, 9). Valuation and cap table stay in backup."),
dict(id="close", act="close", sp="P", t=1, title="Keepwell keeps the promise the shop made",
 show="Dark slide. [click] Ravi's week again, with Keepwell: Monday install and Protect on the same bill; Tuesday an authorised install; two years later a Telugu voice note and a covered fix; Ravi earns on the plan and the family comes back.",
 say="""Let's go back to Ravi.
[click] Monday, he sells the AC — with the install and Protect on the same bill. Tuesday, an authorised technician installs it. Two years later, a voice note in Telugu, and a covered fix the same week. Ravi earns on the plan — and the family comes back to his shop.
Keepwell keeps the promise the shop made when it sold the appliance. Thank you.""",
 why="The close replays the hook with the problem solved — the line the room should remember."),
]
BACKUP = [
 dict(id="b_valuation", title="Valuation", show="Course scorecard ₹8.2 Cr pre; comparables ₹6–12 Cr pre; VC method ≤ ₹13.5 Cr post (stress, 40% IRR); our price ₹8 Cr pre / ₹10.5 Cr post.", say="The course scorecard value, inside comparables, well under the VC-method ceiling (Step 9).", why="", sp="P", act="ask"),
 dict(id="b_captable", title="Cap table and returns", show="Founders 60.5 → 41.5% after Round 3; seed 23.8 → 16.3%; returns 6.9× (yr 5, stress) to 24.6× (yr 7, BASE).", say="Founders keep control through Round 2 and about 41% after Round 3.", why="", sp="K", act="ask"),
 dict(id="b_scen", title="Scenarios", show="BASE / stress / LOW: year-7 revenue, EBITDA, first positive year, peak cash need, what we do.", say="We plan on stress; LOW fails the month-9 gate, so tranche 2 is never paid.", why="", sp="K", act="ask"),
 dict(id="b_terms", title="Key terms", show="CCPS in two tranches (₹1.75 Cr + ₹0.75 Cr at the month-9 gate), 1x non-participating, broad-based weighted-average anti-dilution, 3-person board, vesting from Aug 2025, ESOP 10%.", say="The course's CCPS template, adjusted for a seed.", why="", sp="P", act="ask"),
]
