# Keepwell 8-minute story deck (v4): the script. 12 slides, one point per slide.
# SHOW = what is on screen. SAY = word for word. WHY = the slide's job. BELIEVE = what the investor takes away. NEXT = the bridge.
# Every number traces to ../keepwell_model.xlsx (model/simple_model.py) or ../steps/. See ../claims_ledger.csv.
ACTS = [("open", "Keepwell"), ("problem", "The problem"), ("answer", "Our answer"), ("proof", "The proof"), ("money", "The money"),
        ("win", "Why we win"), ("ask", "The ask")]
SPEAKERS = {"P": "Prathyusha (CEO)", "K": "Kavyanth (COO)", "S": "Sri Charan (CTO)"}
SLIDES = [
dict(id="title", act="open", sp="P", title="Keepwell keeps the promise the retailer made",
 show="Logo, the line 'Keepwell keeps the promise the retailer made', the tagline, and three founder cards, each with a background line (600+ local retailers; 200+ service centres; claims platforms). Advisors along the bottom.",
 say="""Every local appliance retailer makes a promise at the counter: this will be installed properly, and it will be looked after. Then the sale ends, and nobody keeps that promise. Keepwell does. We are the after-sale service arm of the local retailer.
We're three founders, and each of us saw this from one side. I'm Prathyusha: I spent ten years in appliance distribution, supplying six hundred local retailers, and watched them blamed for installs they never did. Kavyanth ran a brand's service network. Sri Charan built claims platforms.""",
 why="It opens with the promise and the people, and each founder's reason is the problem seen from one side: the retailer, the service network, the plan.",
 believe="These founders have lived this problem and already know the people who can solve it.",
 next="Here's what that looks like at a retailer's counter."),
dict(id="problem", act="problem", sp="P", title="Retailers sell the appliance, then lose the customer",
 show="Three cards: Slow installs (2–5 days; 51 of 64 retailers take the blame); Guesswork repairs (80–91% out of warranty; 44% of AC service to local mechanics); Blame, no income (2–3% net; nothing after the sale; held jointly liable). [click] The result line: 7 of 12 households keep no record, and the person they trust can't keep the promise.",
 say="""Three things go wrong after the sale. Installs are slow: brands take two to five days, and fifty-one of the sixty-four retailers we met get the blame. Repairs are guesswork: most machines are out of warranty, and forty-four percent of AC service goes to local mechanics, with no fixed price and no record. And the retailer earns nothing after the sale, yet courts hold him liable.
[click] So the person the family trusts has no way to keep the promise he made.""",
 why="One problem, three causes, one result line, the same structure an investor scans in five seconds.",
 believe="The pain sits with the local retailer and the family, and nobody owns it.",
 next="So here is our answer. Kavyanth."),
dict(id="answer", act="answer", sp="K", title="The retailer sells the promise. Keepwell keeps it.",
 show="Dark slide. The vision in one sentence, then [click] three steps: Step 1 Live, Serve (installs, repair, AMC, Protect under the retailer's name); Step 2 Next, Supply (central parts, partner clusters, trade-ins); Step 3 Later, Know and circulate (verified records; refurbish and recycle).",
 say="""I'm Kavyanth. Our answer is simple: the retailer sells the promise, and Keepwell keeps it. We look after every appliance a local retailer sells, for its whole life.
[click] We build it in three steps. Today we serve: authorised installs in twenty-four hours, guaranteed repairs, maintenance plans, and Keepwell Protect, a two-year repair plan, all under the retailer's name. From year two we supply genuine parts and run partner clusters. From year three, the record verifies installs for brands, and old units get a second life.""",
 why="Vision first, then the live, next, later steps, so the investor sees where it starts and where it goes.",
 believe="A clear company with a big vision and a simple first step.",
 next="Here is what that means for one appliance. Sri Charan."),
dict(id="lifecycle", act="answer", sp="S", title="Not every appliance reaches every stage",
 show="Seven stage arrows across the top (Sold → Installed → Warranty years → Covered → Repaired → Traded in → Recycled), each with ● every unit or ○ only some. Band 1, who reaches it. Band 2, what happens: the first touch (who starts the stage), the order of touches as coloured initials with the first ringed, and what Keepwell does. [click] Band 3, value for each party, each with its value proposition: Family — peace of mind; Retailer — retention; Technician — steady income; Brand or partner — reach and proof. [click] Three decisions: it breaks after warranty? worth repairing? can it be resold?",
 say="""I'm Sri Charan. This is the most important slide: one appliance's whole life, from the shop counter to the recycler. Every unit is sold, installed and lives through its warranty. After that, only some are covered, repaired, traded in or recycled. At each stage a different party makes the first touch: the family walks into the shop, we confirm the install, we send the month-eleven reminder, the family sends a voice note when it breaks. And at every stage we do one job: open the record, install in a day, remind, repair with a genuine part, collect, recycle.
[click] Now read down any column, because this is why it works. The family gets peace of mind: one number, a fixed price and a guarantee. The retailer gets retention: a commission on every job, and the next sale when the old unit comes back. The technician gets steady income: paid within forty-eight hours, and busy even in the off-season. Brands and partners get reach and proof: installs in towns they can't staff, and a verified record.
[click] Three questions decide where each appliance goes next: does it break, is it worth repairing, can it be resold. Every answer keeps it with us.""",
 why="It shows the whole product as one journey, makes clear which stages every unit reaches, and puts every party's gain in the same column.",
 believe="Keepwell runs the appliance's whole life, and everyone around it gains.",
 next="Before the pilot, how we got here."),
dict(id="journey", act="proof", sp="P", title="₹70 L raised, ₹52 L spent",
 show="A timeline: discovery (Apr–Jul 2025) → incorporated → 2 authorised service-centre contracts → ₹45 L pre-seed (Dec 2025) → ₹10 L AP grant (of ₹15 L) and 28 retailer LOIs → pilot (Mar–Oct 2026) → raising the seed. Two bars: raised ₹70 L (angels ₹45 L iSAFE, founders ₹15 L, grant ₹10 L); spent ₹52 L (stipends ₹21 L, pilot set-up ₹13 L, parts ₹6 L, travel/tech/legal ₹12 L) with ₹18 L in the bank. [click] Why: iSAFE at a ₹6 Cr cap, priced on proof; the AP grant gives up no ownership; stipends are 40% of spend.",
 say="""Before the pilot, here's how we got here. Four months interviewing sixty-four retailers, then we incorporated and signed two authorised service centres. We raised seventy lakh: forty-five from three operator angels, fifteen of our own, ten from the state grant. We've spent fifty-two, forty percent of it our own stipends, and eighteen is in the bank.
[click] We used an iSAFE so our price is set on proof, not on an idea.""",
 why="It shows the money already raised and spent, so the seed reads as the next step on a track record.",
 believe="The team spends carefully and has already turned ₹52 L into a working cluster.",
 next="Here's what the pilot proved. Kavyanth."),
dict(id="traction", act="proof", sp="K", title="The pilot cluster paid for itself from 20 retailers",
 show="Left, one sum read top to bottom: 195 retailer-months × ₹19,500 = ₹38.0 L revenue (2,340 jobs) − ₹28.1 L job costs = ₹9.9 L contribution (26%) − ₹8.0 L cluster team = +₹1.9 L cluster profit. Right, the monthly chart with active retailers under each month: contribution crosses the ₹1.0 L team cost in May, at 20 retailers. [click] The result line.",
 say="""I'm Kavyanth. One cluster, March to October. Read the left side as one sum: a hundred and ninety-five retailer-months at nineteen and a half thousand rupees is thirty-eight lakh of revenue. After job costs, nine point nine lakh; after the eight-lakh team, one point nine lakh of profit.
[click] The chart shows when it turned: May, the month we passed twenty retailers. By October, seventy-two thousand a month.""",
 why="Every number is a step in one sum, and the chart shows the month the sum turned positive. One point: the cluster pays for itself.",
 believe="The cluster model is profitable in the field, and they know exactly why.",
 next="Why does each retailer leave ₹5,070? Next slide."),
dict(id="unit", act="proof", sp="K", title="Each retailer leaves ₹5,070 a month today and ₹9,600 at maturity",
 show="Top row: the 12 jobs behind ₹19,500, in whole jobs at market prices: 4 AC installs × ₹2,600 (brand price), 2 other installs × ₹300, 1 service visit × ₹300 (local mechanic), 3 repairs with a part × ₹2,000 (UC rate card), 2 AMCs × ₹1,100 = ₹19,500, average ₹1,625. Below, three panels. One retailer's month in the pilot: ₹19,500 − technicians ₹4,900 − parts ₹6,400 − retailer commission ₹1,320 − travel, payments, AI desk ₹1,810 = ₹5,070 (26%). The same retailer in year 5: + Protect ₹3,400 + AMC renewals ₹1,100 + repairs on our installs ₹6,000 = ₹30,000; at 32%, ₹9,600. One cluster's month: pilot October 34 × ₹5,070 − ₹1.0 L team = +₹0.72 L; mature 60 × ₹9,600 − ₹1.5 L team = +₹4.26 L a month, ₹51 L a year. [click] The result line.",
 say="""Why twenty? Each retailer gives us twelve jobs a month at market prices: installs at the brand's price, three-hundred-rupee visits, repairs at Urban Company's rates. That's nineteen and a half thousand. After technicians, parts, the retailer's commission and travel, five thousand and seventy is ours, and a one-lakh team divided by five thousand is twenty.
[click] Add Protect, renewals and repairs on our own installs, and the same retailer reaches thirty thousand. A sixty-retailer cluster makes fifty-one lakh a year.""",
 why="It opens up the ₹5,070 from slide 5, grows the same retailer, and ends on slide 5's October number before scaling it. A continuation, not a new set of facts.",
 believe="Every rupee of the unit is accounted for, and growth comes from the same retailers.",
 next="Here's who pays for each of those lines."),
dict(id="model", act="money", sp="K", title="Families pay market prices per job. Keepwell keeps ₹26 of every ₹100.",
 show="One bar: every ₹100 a family pays: technician ₹25, parts ₹33, retailer ₹7, travel and payments ₹9, Keepwell ₹26. Three cards: Now, families pay (install ₹2,600, visit ₹300, repair ₹2,000, AMC ₹1,299, Protect ₹2,000); Year 2, agencies and partners pay (parts, partner clusters at a 10% fee, trade-ins); Year 3, brands and buyers pay (verified installs and claims, refurbished units, e-waste).",
 say="""So the model is simple: families pay per job, at market prices. Of every hundred rupees, the technician gets twenty-five, parts thirty-three, the retailer seven, travel and payments nine, and we keep twenty-six. Later, agencies pay us for parts and brands pay to verify installs.""",
 why="One bar shows who gets what from each job; three cards show who pays now and later.",
 believe="The revenue is simple, per job, and every party in the chain is paid.",
 next="Here's the five-year plan."),
dict(id="plan", act="money", sp="K", title="Profitable from year one",
 show="A 5-year table and bars: retailers 200 → 3,000; clusters 4 → 50; revenue ₹3.5 Cr → ₹86 Cr; EBITDA +₹0.13 Cr → +₹16.9 Cr (4% → 20%). [click] 'EBITDA is positive every year. The seed funds cluster launches and working capital: the peak cash need is ₹2.0 Cr.'",
 say="""From two hundred retailers next year to three thousand in year five, revenue grows from three and a half crore to eighty-six crore. EBITDA is positive every year, rising to a twenty percent margin.
[click] We aren't raising to cover losses. We're raising to open clusters faster: the plan's peak cash need is two crore.""",
 why="One table, one point: profitable from year one. The click explains why we still raise money.",
 believe="This is a profitable, capital-efficient business.",
 next="And there's a lot of room. Prathyusha."),
dict(id="market", act="win", sp="P", title="₹4,000 Cr a year keeps small-town appliances running. We need 2% of it.",
 show="Left, what the market is: ≈ ₹4,000 Cr a year spent installing, servicing and repairing ACs, fridges, washing machines and purifiers bought from local retailers in Tier 2/3 India; 45,000 retailers × ≈ ₹9 L each = ≈ ₹4,000 Cr; a bar: repair and service 71% (₹2,840 Cr), installs 26% (₹1,040 Cr), AMC 3%; who takes it today. Right, nested squares drawn to scale: ₹4,000 Cr India → ₹1,040 Cr five southern states → ₹360 Cr AP + Telangana. [click] The small amber square: Keepwell year 5, ₹86 Cr, about 2%, and the result line. Why-now strip underneath.",
 say="""Every year, small-town families spend about four thousand crore installing, servicing and repairing these appliances: forty-five thousand retailers, about nine lakh each. Today it goes to brand centres and local mechanics, with no price, no guarantee, no record.
On the right, to scale: the south is a thousand crore; Andhra and Telangana, where we start, three hundred and sixty.
[click] This small square is us in year five: eighty-six crore, about two percent.""",
 why="One side says what the money is; the other shows, to scale, how little of it the plan needs.",
 believe="The market is real, unorganised and large, and the plan needs only a sliver of it.",
 next="Why hasn't anyone done this? Sri Charan."),
dict(id="competition", act="win", sp="S", title="Same price as the market. Far more for it.",
 show="Left, four pairs of bars, Keepwell vs the market, near-equal heights: AC install ₹1,199 vs brand ₹1,199; service visit ₹300 vs mechanic ₹300; gas repair ₹3,000 vs Urban Company ₹3,000; AMC ₹1,299 vs Urban Company ₹1,298. [click] Right, a ✓/✗ grid: 24-h authorised install, guarantee and fixed price, small towns, through the local retailer, one record. Only Keepwell's row is all ticks.",
 say="""We charge what the market charges. The bars are the same height: the brand's install price, the mechanic's three hundred, Urban Company's AMC.
[click] But look at what you get. Only one row is all ticks: a day-one authorised install, a guarantee, small towns, through the retailer, on one record.""",
 why="Bars of equal height make 'same price' visible; the tick grid makes 'more for it' visible.",
 believe="Keepwell does not win on price; it wins on what the customer gets.",
 next="And can someone copy it?"),
dict(id="moat", act="win", sp="S", title="Built one retailer at a time. Hard to copy.",
 show="Four big tiles: 33 of 34 retailers stayed on 2-year exclusive deals; Authorised (brand sub-contracts, others void the warranty); 20 retailers before a cluster pays; ₹9.5k vs ₹22k to sign a retailer. [click] A dark band: ₹80 Cr, what Onsitego paid for Qdigi; easier to buy than to build: that is our exit.",
 say="""To copy us, you'd need retailers on exclusive deals, authorised installs, and twenty retailers in every cluster before it pays, signed at twice our cost.
[click] It's easier to buy than to build. Onsitego paid eighty crore for Qdigi. That's our exit.""",
 why="Four numbers answer 'can't they copy you'; the Qdigi deal turns the threat into the exit.",
 believe="The moat is the network, and the likely competitors are the likely buyers.",
 next="So here's what we're asking for."),
dict(id="ask", act="ask", sp="P", title="Raising ₹2.5 Cr for the seed round",
 show="Dark slide. A table: 1 · Cluster launches 64% ₹1.6 Cr (8 new clusters, 500 retailers by March 2029; ₹20 L per cluster); 2 · Working capital 16% ₹0.4 Cr; 3 · Buffer and compliance 20% ₹0.5 Cr. Three cards: ₹2.5 Cr CCPS, single close; ₹10 Cr pre-money, 20%; 20× seed return at a year-5 exit (March 2032). [click] 'The only round we need to reach 1,000 retailers.'",
 say="""We're raising two and a half crore, as CCPS, at a ten crore pre-money valuation, in one close. Sixty-four percent opens eight new clusters, sixteen percent is working capital, and twenty percent is buffer and compliance above our two-crore peak need. Head office runs on our operating profit.
At a year-five exit, in March 2032, at fifteen times EBITDA, the seed's twenty percent returns about twenty times.
[click] This is the only round we need to reach a thousand retailers.""",
 why="The ask as a use-of-funds table, then the terms, then the close line.",
 believe="A fairly priced, capital-efficient round with a clear return.",
 next="And why now."),
dict(id="whynow", act="ask", sp="P", title="The appliance wave has reached small towns",
 show="Four picture tiles: 1 in 10 homes has an AC (ten squares, one filled); +75% AC market 2025 → 2029 (two bars); 80–91% of appliances out of warranty (a ring); GST on ACs 28% → 18% (two bars stepping down). [click] 'Whoever organises the after-sale first keeps the retailer.'",
 say="""Why now? One home in ten has an AC, and the market grows seventy-five percent in four years. Most machines are already out of warranty, and ACs just got cheaper.
[click] Whoever organises the after-sale first keeps the retailer.""",
 why="Four pictures, no small print: the wave is arriving, and the after-sale is up for grabs.",
 believe="The timing is now.",
 next="The close."),
dict(id="close", act="ask", sp="P", title="Keepwell keeps the promise the retailer made",
 show="Dark slide: the logo and one line, 'Keepwell keeps the promise the retailer made.' Underneath: installed right · repaired with genuine parts · covered · given a second life.",
 say="""Keepwell keeps the promise the retailer made. Thank you.""",
 why="The last image is the one-line value proposition.",
 believe="Keepwell is the after-sale arm every local retailer needs.",
 next="Questions."),
]
BACKUP = [
 dict(id="b_pilot", title="Pilot, month by month", show="Retailers 12 → 34; revenue ₹2.34 L → ₹6.63 L a month; contribution crosses the ₹1.0 L team in May; total +₹1.9 L.", say="The monthly table behind the traction slide.", why="", sp="K", act="ask"),
 dict(id="b_prices", title="Why we charge what we charge", show="Table: each job, our price net of GST, the market reference (LG charter, Urban Company rate card, local mechanic, Croma ZipCare) and why customers pick us.", say="Every price is at the market rate; the average of ₹1,625 comes from the mix.", why="", sp="K", act="money"),
 dict(id="b_valuation", title="Valuation", show="Course scorecard ₹10.0 Cr (89/100); comparables ₹6–12 Cr; VC method ceiling ₹47 Cr post; our price ₹10 Cr pre / ₹12.5 Cr post.", say="The course scorecard, inside comparables, far under the VC ceiling.", why="", sp="P", act="ask"),
 dict(id="b_captable", title="Cap table and return", show="Founders 64.0%, iSAFE 6.0%, ESOP 10.0%, seed 20.0%; exit ₹254 Cr; seed 20×, 83% IRR.", say="Founders keep 64% after the seed.", why="", sp="P", act="ask"),
 dict(id="b_cons", title="Conservative case", show="Revenue per retailer −10%, margin −2 points, rollout −25%, head office −15%: breakeven in year 1, positive from year 2; peak need ₹2.6 Cr, covered by the buffer and a one-quarter delay in two launches.", say="Even the conservative case breaks even in year one.", why="", sp="K", act="ask"),
]
