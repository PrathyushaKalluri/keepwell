# Keepwell story deck: the script, single source of truth.
# Each entry drives (1) the speaker-notes panel in index.html (press N) and (2) SCRIPT.md.
# SHOW = what is on screen (the proof / the visual). SAY = what the speaker says (the explanation).
# Every number traces to ../keepwell_model.xlsx or a step document in ../steps/.
# Illustrative case for the IIIT Hyderabad ESFS course pitch.

ACTS = [
    ("hook", "The hook"),
    ("problem", "The problem"),
    ("keepwell", "Keepwell"),
    ("research", "What we found"),
    ("vision", "The vision"),
    ("stage", "Where we are"),
    ("product", "Circuit"),
    ("proof", "The proof"),
    ("moat", "Why us, why now"),
    ("scale", "How big"),
    ("ask", "The ask"),
    ("future", "The future"),
]

SPEAKERS = {"P": "Prathyusha (CEO)", "S": "Sri Charan (CTO)", "K": "Kavyanth (COO)"}

SLIDES = [
# ---------------------------------------------------------------- HOOK
dict(id="hook", act="hook", sp="P", t=50, title="Every repair in your home starts from zero",
 show="""An illustrated home with eight machines (AC, fridge, washing machine, water purifier, geyser, TV, fan, mixer). The presenter clicks each machine as the audience calls it out, and a counter adds up "repairs in your home this year". [click] A question tag drops onto every machine: "Last serviced? Which part? What did you pay? Who fixed it?" [click] The line lands: "Every repair in your home starts from zero." """,
 say="""Before we begin, think about your own home. In the last year, what broke? The AC? The fridge? The water purifier, the geyser, the washing machine? [click the machines as people answer] Keep counting.
Now a harder question. Pick any one of them. When was it last serviced? Which part was changed? What did you pay, and who fixed it? [click]
Most of us don't know. It's in someone's phone, in a diary, or nowhere. [click]
So every repair in your home starts from zero.""",
 why="The audience answers before we say anything about us. Once they've counted their own repairs, the problem is theirs too. The interaction also wakes the room up in the first 30 seconds."),

dict(id="lightly", act="hook", sp="P", t=60, title="We took it lightly too",
 show="""Left: Sri Charan's line on a dark card, "Our machines cost my family ₹10,000 a month. Never evenly." Right, building click by click:
1. a thermometer at 46 °C, "Ramagundam"
2. a phone ringing, and a counter that climbs to 14 missed calls
3. a Telugu voice note marked "unheard"
4. a shopping cart, "New AC ₹38,000"
5. a tiny capacitor, "The fault: ₹350"
The line lands: "Nobody is the villain. The system has no memory." """,
 say="""We were the same. In Sri Charan's family, the machines cost about ten thousand rupees a month, never evenly. We treated that as normal. [click]
Then one afternoon in Ramagundam, at forty-six degrees, a retired miner's AC stops cooling. [click] The agency owner he trusts, Ramesh, is up a ladder on another job. His phone rings fourteen times. [click] The son, 700 kilometres away, sends a voice note in Telugu. Nobody writes it down. [click] By evening the son orders a new AC: thirty-eight thousand rupees. [click] The fault was a three-hundred-and-fifty-rupee capacitor.
Nobody here is the villain. The system just has no memory.""",
 why="It moves from 'this happens to us' to 'this is a system failure', using one concrete story with two prices people remember: ₹350 and ₹38,000. The people are a composite (disclosed in the data room); the town, the heat and the reflex to replace are real."),

# ---------------------------------------------------------------- PROBLEM
dict(id="bigproblem", act="problem", sp="P", t=55, title="It isn't one family. It's 15 crore repairs a year.",
 show="""Four counters count up, each with a small picture:
- 15 Cr appliance repairs a year
- 27 Cr fridges, washing machines and ACs with no shared record
- ₹550 Cr of technician time lost to repeat trips each year
- 37,500 repair agencies running on a phone and a notebook
A red "broken thread" runs under all four. Source line: repo; Data for India; CLASP/BEE 2024; ICAP/CEEW. """,
 say="""This isn't one family. India does about fifteen crore appliance repairs a year. There are about twenty-seven crore fridges, washing machines and ACs in our homes, and not one has a shared history.
So technicians go in blind, and when the first visit doesn't fix it, someone goes back. If India fixed things at the global first-visit rate, that would still be about five hundred and fifty crore rupees of technician time wasted every year.
And the work is done by about thirty-seven thousand five hundred small agencies, on one phone and a notebook. The problem isn't skill. It's memory.""",
 why="Four numbers, each with one job: frequency (15 Cr), the asset with no record (27 Cr), money lost (₹550 Cr) and the customer we sell to (37,500). Say the ₹550 Cr caveat out loud, because it is the honest way to quote it."),

# ---------------------------------------------------------------- KEEPWELL
dict(id="keepwell", act="keepwell", sp="P", t=40, title="Keepwell: the care layer for everything a home owns",
 show="""Dark slide. The broken thread from the last slide joins into the Keepwell mark. Below it, a machine "record card" fills in line by line:
- Voltas 1.5 T split AC · bought Mar 2021
- Warranty: compressor till Mar 2026
- Repairs: 3, each verified
- Parts fitted: capacitor, Aug 2026
- Next service: Apr 2027
Tagline: "One living record per machine, and a service at every stage of its life." """,
 say="""That's why we started Keepwell. Keepwell gives every machine in an Indian home a memory. One living record of what it is, what went wrong, what was fitted and what it needs next, built only with the owner's consent.
On top of that record, a service at every stage of the machine's life. Think of it as the CIBIL of household machines: the history that everyone checks first.""",
 why="We name the company only after the room has felt the problem, so the name arrives as the answer. The record card makes 'memory' concrete before we explain the vision in detail."),

dict(id="team", act="keepwell", sp="P", t=55, title="Three founders, one from each side of the problem",
 show="""A triangle with the machine record at the centre. Each corner is one side of the problem with its founder card:
- **Agency network: Prathyusha, CEO.** FixNear: 1,200 technicians, 14 towns, sold in 2022.
- **Household and AI: Sri Charan, CTO.** 7 years of Indian-language voice AI; built Circuit himself.
- **Brand and warranty: Kavyanth, COO.** Ran 300+ service partners and a warranty-claims desk.
A ribbon underneath: "Full-time since May 2025 · ₹15 lakh of our own money · incubated at CIE-IIITH · DPIIT-recognised". """,
 say="""Why us? This problem has three sides, and each of us spent years on one of them.
I'm Prathyusha. I co-founded FixNear, a technician network of twelve hundred people across fourteen towns in Andhra and Telangana, and sold it in 2022. I learned the hard way that taking the customer away from the local agency doesn't work.
Sri Charan spent seven years building voice AI in Indian languages, and he built our product himself. Kavyanth ran a brand's network of more than three hundred service partners, and its warranty-claims desk.
Agency, household, brand. All three of us have been full-time since May 2025, with our own money in.""",
 why="The course gives the team 45 of 90 points. Each founder gets one line of proof (an exit, a shipped product, a network) instead of a CV. The triangle shows they are complementary, not just three people."),

# ---------------------------------------------------------------- RESEARCH
dict(id="bothsides", act="research", sp="S", t=60, title="What goes wrong, on both sides",
 show="""A split screen joined by a broken thread labelled "no shared memory".
**The agency (the person who pays us):**
- ~1 in 8 requests lost: missed calls, unanswered voice notes
- Technicians sent in blind: no model, no history
- 12 of 18 owners had a job delayed by the wrong part last month
- ~3.45 crore repeat trips a year at ~₹159 each
**The household (the person who trusts):**
- Price, part and "job done" can't be checked
- 55% got a defective machine; only 21% were made whole
- 47% of complaints are no-shows and chasing
- In 7 of 12 repairs, the person deciding, paying and opening the door were different people
- Consumer helpline complaints: 13.16 → 20.49 lakh in a year""",
 say="""I'm Sri Charan. Here's what goes wrong, from both sides.
For the agency, the pain starts at the very first moment. About one request in eight is simply lost: a missed call, a voice note nobody follows up. The technician goes in blind, often with the wrong part, so a lot of jobs need a second trip, and that costs the agency money.
For the household, nothing can be checked: not the price, not the part, not whether the job is really done. Fifty-five percent of families have had a defective machine, and only twenty-one percent of those were made whole. Almost half the complaints are about chasing someone. And in most homes the person who decides, the person who pays and the person who opens the door aren't the same.
Two sides, one missing thing: a shared memory of the machine.""",
 why="It proves we understand the buyer (the agency) and the user (the household) separately, which is where most repair pitches blur. The broken thread keeps the one idea visible."),

dict(id="watched", act="research", sp="S", t=60, title="We didn't read about it. We watched it happen.",
 show="""A proof wall of five real artefacts. Each opens full-screen on click:
1. **A brand's WhatsApp bot failing** (screen recording): "There is some API related issue please try again later" … "My request was not done"
2. **A water purifier** with a local agency's sticker taped on, and the next service date written over the brand's label in marker
3. **A gas cylinder** with its date written in marker
4. **A household's repair diary**: handwritten pages of what was fixed, when, by whom, for how much
5. **Our own whiteboard**: "machine fails → technician travels → discovers the problem → another visit" vs "symptoms + photo + model → probable issue + likely part → prepared technician → one visit"
Personal details are blurred. Tag: "Real · from our discovery interviews". """,
 say="""We didn't just read about this. We watched it happen. [open the bot]
This is a real brand's WhatsApp bot. A woman asks for her water purifier to be serviced. The bot says there's an API issue. She asks what an API is. Then it asks her for a job ID she doesn't have. Her last message: "My request was not done." [open the purifier]
And this is what people do instead. A local agency has taped its own sticker onto the machine, and the family has written the next service date over the brand's label in marker. [open the diary] This family keeps a handwritten diary of every repair, because nobody else will.
People are already building the machine's memory, on paper. The demand is there. The tool isn't.""",
 why="This is the trust slide for the problem. It is real evidence, not statistics, and the strongest moment for the 'wow'. The sticker and diary show people already doing a paper version of Keepwell, which de-risks the idea."),

dict(id="listened", act="research", sp="S", t=55, title="We listened before we built",
 show="""The research funnel builds on the left:
- household survey: 19 responses, 12 qualified
- 7 recorded household interviews
- 18 agency-owner interviews
Named quote cards rotate on the right:
- Sai Kakki: "They're never going to say the price… three thousand to five thousand."
- Amma: "We won't know if the part is duplicate or original."
- Rk Sir: "If we visit a local man, definitely doubts will arise."
- Sarala Aunty: "Since then, I have been able to trust him and approve his small works."
[click] The insight lands in a teal band: "Nothing in a repair can be checked, so people trust the person, not the work." Two proof chips: 44% use a local agency (up from 38%), and 76% of AC owners avoid brand service. """,
 say="""Before we wrote any production code, we spent four months listening. A household survey, seven recorded household interviews, and eighteen conversations with agency owners.
Listen to what households said. Sai Kakki: they never tell you the price. Amma: you can't tell if the part is original. Rk Sir: with a local man, doubts arise. And Sarala Aunty: he came, did a small job honestly, and since then she trusts him with more. [click]
That's our insight. Nothing in a repair can be checked, so people trust the person, not the work, one good job at a time. That's why forty-four percent of families stay with the local agency, and that number is rising.
So our strategy is simple. We don't replace the trusted agency. We make it the smartest one in town.""",
 why="The quotes are real and named with consent. The insight explains why an agency-first strategy wins against better-funded platforms, which is the strategic choice investors will question."),

dict(id="agencies", act="research", sp="S", t=50, title="What 18 agency owners told us, and what we decided",
 show="""A two-column "they said → so we built" table. Each row slides in:
- 0 of 18 use any software; 16 of 18 run on phone + WhatsApp → **Lives inside their WhatsApp. No new app.**
- ~1 in 8 requests lost → **The first job is intake, not diagnosis**
- Median 4 technicians, 125 jobs a month → **Our model uses 125, not the market's 147**
- 13 of 18 say repeat visits are unpaid → **Fewer trips is money in their pocket**
- 14 of 18 want to pay per completed job (₹30–50) → **₹40 per verified fix; we tested ₹100 too**""",
 say="""Then we sat with eighteen agency owners in Ramagundam, Peddapalli and Karimnagar. Every product decision we made came from this table.
None of them used any software, so we live inside their WhatsApp. They lose one request in eight, so we start with intake. Most say a repeat visit is unpaid, so fewer trips puts money in their pocket. And most wanted to pay per job, not per seat, so we charge only when a fix is verified.""",
 why="It turns research into decisions, the Stage 2 behaviour the course rewards. It also pre-empts the biggest risk in the repo: 'won't agencies want repeat visits?' The answer is that 13 of 18 say those visits are unpaid."),

# ---------------------------------------------------------------- VISION
dict(id="lifecycle", act="vision", sp="S", t=50, title="From one repair to a machine's whole life",
 show="""A ring of seven life stages: bought, used, fails, repaired, maintained, resold, recycled. Each carries a red tag:
- technician arrives blind
- warranty can't be proven
- plan sold to the wrong home
- resale buyer can't trust it
- recycled too early
[click] A teal ring draws through all seven stages: "One record, every stage". [click] The vision line appears: "Every machine an Indian home owns is cared for across its whole life: repaired right, remembered always, and never wasted." Analogy chips: CIBIL for borrowers · Carfax for used cars · **Keepwell for household machines**. """,
 say="""When we zoomed out, the small problem turned into a big one. Every machine lives one life: bought, used, fails, repaired, maintained, resold, recycled. And at every stage it starts from zero. The technician arrives blind, the warranty can't be proven, the plan is sold to the wrong home, the resale buyer can't trust it. [click]
The same missing piece sits under all of them: the machine's history. [click] So our vision is that every machine an Indian home owns is cared for across its whole life. What CIBIL is to a borrower, Keepwell is to a household machine.""",
 why="Here the problem widens from repair into a venture-scale category. We hold off on the product until the vision is clear, so Circuit lands later as the smart entry point rather than the whole company."),

dict(id="roadmap", act="vision", sp="S", t=40, title="The roadmap: one record, a product at each stage",
 show="""A rising staircase of six steps, each with its product, its stage of life and who pays:
- **R1 · live:** Circuit, the AI desk for repair agencies (agency pays per verified fix)
- **R2 · ~12 months:** Home Memory + Service Plans (insurer commission)
- **R3 · year 2:** Claims triage (warranty administrators, OEMs)
- **R4:** Parts marketplace (parts sellers)
- **R5:** Resale & recycling (buyers, producers, recyclers)
- **Phase 3:** Data services, consent-first (brands, insurers)
The record runs under every step as one teal line. """,
 say="""From those insights came the roadmap. Each step is a product on the same record, with a different payer.
We start with Circuit for repair agencies, which is live today. Next, Home Memory and service plans, sold for insurers. Then claims triage for warranty administrators, then parts, then resale and recycling, and finally data services, always with consent.
Each step is paid for by someone who already spends money at that stage of the machine's life.""",
 why="It shows a clear expansion path, scored under Product–Potential, and that each step has its own payer. The order follows the team repo's build order."),

dict(id="whycircuit", act="vision", sp="S", t=35, title="Why we start with repair",
 show="""Three overlapping circles:
- **The pain:** the moment a household needs help
- **The payer:** the agency earns on every job
- **The truth:** the only moment someone opens the machine and sees what's wrong
The overlap lights up: "The repair". Then the name appears in the middle: **Circuit**. """,
 say="""Why start with repair? Because it's the only moment where three things meet.
The pain is highest, because the machine is broken. The payer is there, because the agency earns on that job. And it's the only moment someone opens the machine and records what's really wrong.
Start there, and the record fills itself as a by-product of work that's already happening. [click] That's Circuit.""",
 why="It answers 'why this wedge?' in 35 seconds and hands over to the stage and the product."),

# ---------------------------------------------------------------- STAGE
dict(id="firstmoney", act="stage", sp="P", t=55, title="Where we are, and how the first money was used",
 show="""A money-flow diagram.
**In (₹55 lakh):**
- Founders' savings ₹15 L
- Two operator angels ₹30 L (iSAFE)
- Startup India Seed Fund ₹10 L received (₹20 L sanctioned)
- Plus CIE-IIITH incubation
**Out (₹34 lakh):**
- Founder stipends ₹19.5 L
- Contract engineer ₹6 L
- Cloud and AI ₹3 L
- Pilot field costs ₹3 L
- Legal ₹2.5 L
**In the bank: ₹21 lakh.**
A "what it built" strip: the team · the research · the prototype · production · 14 paying agencies. A stage badge reads: "Stage 2: finding the business model". """,
 say="""So where are we? We're at stage two: we have a product and paying customers, and we're proving the business model.
Here's how we got here. We put in fifteen lakh of our own savings. Two operator angels, one who built a home-services company and one who ran service at a durables brand, put in thirty lakh. They also introduced three of our first five agencies. The government's Startup India Seed Fund sanctioned twenty lakh through our incubator, CIE-IIITH, and we've received ten.
We've spent thirty-four lakh in eighteen months: mostly modest founder stipends, one contract engineer, and the pilots. That money built the team, the research, the prototype and fourteen paying customers. Twenty-one lakh is still in the bank.""",
 why="It establishes stage, credibility and capital discipline in one picture. Every rupee is itemised, which answers 'what did you do with the last money?' before anyone asks. Valuation and the iSAFE cap are kept for Q&A."),

# ---------------------------------------------------------------- PRODUCT
dict(id="circuit", act="product", sp="S", t=55, title="Circuit, simply",
 show="""A six-step infographic. A dot travels along the path as each step lights up:
1. 🎙 **Customer sends a voice note**, in Telugu, Hindi, Tamil, Kannada, Marathi or English
2. **Circuit understands** and reads it back
3. **Finds the likely fault and the part to carry**, using this machine's history and every past repair
4. **Quotes from the agency's own rate card**; the owner approves
5. **Sends the technician a job card** he can read in ten seconds
6. **The technician confirms the fix.** The record updates, Circuit gets smarter, and we earn ₹40.
Underneath: "AI reads and drafts. People decide anything with money or safety." """,
 say="""Here's what Circuit does, in plain words. A customer sends the agency a voice note on WhatsApp, in their own language. Circuit understands it and reads it back. It looks at the machine's history and everything learned from past repairs, and tells the technician the likely fault and the part to carry. It builds the quote from the agency's own price list, and the owner approves it. The technician gets a job card he can read in ten seconds.
And when he confirms what was actually wrong, three things happen at once. The machine's record updates, Circuit gets smarter for the next job, and only then do we earn forty rupees.""",
 why="No architecture or technical terms, as you asked. The last step carries the whole business: one event that is the fix, the learning and the revenue."),

dict(id="demo", act="product", sp="S", t=60, title="See how easy it is",
 show="""Three tabs on a device frame:
- **The agency's WhatsApp** (opens first): an animated chat. A voice note arrives (0:24, Telugu), Circuit reads it back, the customer sends a photo of the AC label, a quote arrives and is accepted. Then the technician's job card slides in ("likely: run capacitor; carry: 35 µF capacitor"), and finally a green tick: "Fixed in one visit · record updated".
- **The Circuit website**: the live landing page, scrollable.
- **A real run, 30× speed**: the recorded run of the prototype (real).
Ease chips along the bottom: no new app · set up in one visit · 6 languages · 30 free days · pay only when a fix is verified · the owner approves every quote. """,
 say="""Let me show you how easy this is. [chat plays] For the customer, nothing changes. Same agency, same WhatsApp number, their own language. For the owner, the job arrives ready, with a quote he only has to approve. For the technician, a ten-second card that tells him which part to carry. [switch tab] This is our website, [switch tab] and this is a real run of the system, sped up thirty times.
Setting up takes one visit: the owner's price list and his WhatsApp number. The first jobs flow the same day. There are thirty free days, and after that the agency pays only when a fix is verified.""",
 why="Investors judge ease of adoption by watching it. Three tabs let the presenter choose depth on the day. The ease chips are the adoption argument for Product–Quality and Product–Potential."),

# ---------------------------------------------------------------- PROOF
dict(id="pricetest", act="proof", sp="K", t=50, title="The pilot: we tested the price, and one test failed",
 show="""The pilot design card: 5 agencies, 22 technicians, Feb–Apr 2026, paid from day one, each measured against its own baseline.
Two arms side by side: **₹40 per verified fix** (3 agencies) vs **₹100** (2 agencies).
A value-to-fee gauge for each: ₹40 → **2.0×** the fee, ₹100 → **0.81×**.
[click] The red quote from the ₹100 owner who halved his usage in week 3: "It takes too much of a small job." The result stamp: "₹40 for everyone since May 2026". Pricing ladder: ₹40 per verified fix · optional Desk Pro ₹399/month · 30 free days. """,
 say="""I'm Kavyanth. Before we scaled anything, we ran a paid pilot with five agencies and twenty-two technicians, each measured against its own record before Circuit.
We tested two prices at the same time: forty rupees per verified fix, and a hundred. [click] At a hundred, one owner halved his usage in the third week. In his words, "It takes too much of a small job." At forty, the agency gets about two rupees of value for every rupee it pays us. At a hundred, it's less than one. So since May, everyone pays forty.
We're showing you the test that failed because it's what set our price.""",
 why="Showing a failed experiment builds more trust than a clean success. It also proves willingness to pay with a real test rather than a survey."),

dict(id="traction", act="proof", sp="K", t=50, title="Nine months of paid use",
 show="""Five counters count up:
- **14** paying agencies (1 of 15 churned)
- **~8,200** jobs through Circuit
- **96%** of requests became jobs
- **~₹59k** monthly recurring revenue, 97% of invoices paid on time by UPI
- **11 of 14** owners "very disappointed" without it
A large before/after dial: one-visit closure **71% → 83%**, held for 6 months over ~7,000 jobs (global benchmark 77%). """,
 say="""Then we expanded, and here's nine months of paid use. Fourteen agencies pay us every fortnight, and only one of fifteen has left. About eight thousand two hundred jobs have gone through Circuit. Ninety-six percent of requests now become a job, where before one in eight was lost.
The number that matters most to an agency is jobs closed in one visit. It went from seventy-one to eighty-three percent, and it has held there for six months, above the global benchmark. Eleven of fourteen owners say they'd be very disappointed if we disappeared.""",
 why="Real paid demand, retention and an outcome metric, covering Market–Quality and Product–Quality. The 'very disappointed' test is a known product–market-fit signal."),

dict(id="learning", act="proof", sp="K", t=45, title="The chart that matters most: it learns",
 show="""A line chart draws itself: root-cause accuracy (right fault in the top 3), Mar → Oct 2026: **62 → 68 → 73 → 76 → 78%**. A dashed line marks the 75% gate, with "passed in August". The chart is shaded in two zones:
- **Mar–May:** "about half from adding manuals" (grey: anyone can do this)
- **Jun–Oct:** "mostly from verified repairs" (teal: only we can do this)""",
 say="""This is the most important chart in our story. It's how often Circuit names the right fault in its top three. It started at sixty-two percent in March and it's at seventy-eight percent now. It passed our seventy-five percent gate in August.
Look at where the gain comes from. Up to May, about half of it came from adding repair manuals, and anyone can do that. Since June, it comes mostly from repairs that technicians verified. [click] No competitor can do that without our agencies. The product gets better every time it's used.""",
 why="This is the moat shown in production data rather than claimed on a slide. It answers Product–Uniqueness (our weakest cell, 7/10) with evidence."),

dict(id="value", act="proof", sp="K", t=45, title="Does the agency actually win?",
 show="""Horizontal stacked bars, per agency per month:
- **Value:** recovered jobs ₹2,400 + trips avoided ₹2,150 (**measured**, solid teal) + owner time ₹2,925 (**self-reported**, hatched) = ₹7,475
- **Our fee at ₹40:** ₹3,690
- **The fee at ₹100:** ₹9,225 (grey, crossed out)
Callouts: "Measured value alone = 1.23× the fee" and "Agency keeps ~₹3,800 a month after paying us". """,
 say="""A product only survives if the customer gets more than it pays. So we split what we measured from what owners told us.
From system logs alone, the jobs we recover and the trips we save are worth about four thousand five hundred rupees a month to an agency. That's more than our fee of three thousand seven hundred, even if you ignore everything owners say. Counting the owner's time, the value is about two times the fee, and the agency keeps about three thousand eight hundred rupees a month after paying us.
At a hundred rupees, the maths breaks, which is exactly what the pilot showed.""",
 why="It separates measured from self-reported value: the honest version, prompted by our red-team. It also answers the biggest business-model risk, 'why would an agency pay?'"),

dict(id="unitecon", act="proof", sp="K", t=55, title="Unit economics: one agency, one month",
 show="""A waterfall chart: revenue **₹4,216** → AI and messaging −₹713 → tools −₹100 → contribution **₹3,403 (81%)**.
Right panel, three gauges filling:
- Cost to win an agency: **₹17,900**
- Payback: **6.3 months** (gate ≤ 7; small-business software norm ≤ 12)
- LTV : CAC **6.3×** (healthy > 3×)
Footnote: "Observed inputs: 125 jobs, 82% verified, AI budgeted at 2027 prices, churn assumed 3% (observed ~1.4%). Stays ≥ 4.8× in every ±20% case." """,
 say="""Here's one agency, one month. It pays us about four thousand two hundred rupees. AI and messaging cost about seven hundred, and that's budgeted at next year's higher AI prices. We keep three thousand four hundred: an eighty-one percent margin.
Winning an agency costs about eighteen thousand rupees, fully loaded with salaries. So it pays back in a little over six months, and over its life an agency is worth six times what it cost to win.
Every input here is what we observed, not what we hoped. We assume three percent monthly churn when we see one and a half. And if any single input moves twenty percent against us, it stays at four point eight times or better.""",
 why="The course's 'missing unit economics' red flag is answered with observed inputs and a stress test. Stating the conservative assumptions out loud builds credibility."),

dict(id="growth", act="proof", sp="K", t=40, title="Growth comes from capacity, not hope",
 show="""An equation builds: **new agencies = field reps × ~80 a year + 10% referrals**.
Evidence cards beneath:
- "COO closed 8 agencies in 6 months at ~25% of his time = one full-time rep's pace"
- "2 of the last 10 came by referral"
- "5 → 14 paying agencies in 6 months: ~19% a month, with no salespeople"
A small chart: paying agencies by month, 5 → 14.""",
 say="""Can it grow? We don't plan growth from a hockey stick. We plan it from capacity.
I closed eight agencies in six months using about a quarter of my time. That's the pace of one full-time sales rep: around eighty agencies a year. Two of our last ten came by referral. And we grew from five to fourteen agencies in six months, about nineteen percent a month, with no salespeople at all.
So the growth plan is simple: hire reps, and each brings about eighty agencies a year.""",
 why="It turns growth from an assertion into a formula with evidence, and sets up the capacity plan and the use of funds."),

dict(id="timeline", act="proof", sp="K", t=35, title="How we got here: 18 months, ₹34 lakh",
 show="""A horizontal timeline draws left to right, milestones popping in turn:
- Jan–Apr 2025 · discovery
- May 2025 · incorporated, full-time, CIE-IIITH
- Jun–Sep · prototype
- Oct · ₹30 L from angels
- Jan 2026 · in production (Mumbai)
- Feb–Apr · paid price test
- Mar · government seed fund sanctioned
- May–Oct · 5 → 14 agencies
- Aug · accuracy gate passed
- **Nov 2026 · raising the seed**
Each phase is tagged with its spend. """,
 say="""So that's the journey. Four months of listening, then the company, the prototype, our angels, production, a paid price test, and steady expansion. We passed our accuracy gate in August.
Eighteen months and thirty-four lakh rupees to get here. Now we're raising to scale it.""",
 why="It compresses the whole build into one visual and reinforces capital efficiency right before the competition section."),

# ---------------------------------------------------------------- MOAT
dict(id="whynotsolved", act="moat", sp="K", t=50, title="Why this isn't solved yet, and where we sit",
 show="""A two-axis map. Horizontal: serves the brand/platform → serves the independent agency. Vertical: holds one job → holds the lifetime record + learning.
Competitor dots fly in to their places: Urban Company, ServiceOnDoors, Servify, Zoho FSM, Fieldproxy, Bernard (US), voice-AI firms. **Keepwell** pulses alone in the top-right corner.
Right column, one line each:
- Urban Company takes the customer and keeps 28%
- Servify serves brands
- Zoho/Fieldproxy: English, per seat
- Bernard: no Indian languages, no record""",
 say="""Why hasn't anyone solved this? Because everyone holds a slice. Urban Company takes the customer away from the agency and keeps twenty-eight percent of what the professional earns. Servify works for brands. Field-service software is in English, priced per seat, and needs a dashboard. The closest AI, Bernard in the US, has no Indian languages and no record.
Nobody serves the independent agency and holds the machine's whole history. That corner is empty, and that's where we are.""",
 why="It answers 'why now, why hasn't X done it' with a picture. Keepwell sitting alone in a corner is the image investors remember."),

dict(id="catchup", act="moat", sp="K", t=50, title="Why nobody can catch up",
 show="""Two columns:
- **"A rival can copy in a quarter"** (grey, crossed out): WhatsApp intake · prompting an AI model · searching manuals · ranking faults
- **"A rival cannot copy"** (teal, counters): 8,200+ verified repair outcomes and growing · a record that follows the machine · a technician-confirmed parts catalogue · Telugu speech corrections · an outcome licence signed by all 14 agencies
A flywheel spins in the centre: more agencies → more verified outcomes → better diagnosis → more first-time fixes → agencies stay and pay → more records → plans, claims, parts.
Switching-cost chips: rate card · customer histories · technician habits. """,
 say="""Let's be honest about what can be copied. A competitor can copy our WhatsApp intake and our AI in a quarter.
What they can't copy is what only builds up through use: eight thousand verified repair outcomes and counting, a record that follows each machine, a parts catalogue confirmed by technicians, and our Telugu speech corrections. All fourteen agencies have signed a licence that keeps the de-identified outcomes with us, even if they leave.
And the longer an agency uses Circuit, the harder it is to leave, because its price list, its customers' histories and its technicians' habits all live there. That's the flywheel.""",
 why="It concedes what is copyable, which is credible, then shows the data moat, the licence that protects it, and switching costs. This covers Product–Uniqueness and the X-factor."),

dict(id="porter", act="moat", sp="K", t=30, title="The industry forces, and our answer to each",
 show="""A pentagon of Porter's five forces around "AI for repair agencies in India". Each node has a rating pill and our one-line answer:
- **Rivalry: low, rising.** Move first in Tier 2/3.
- **New entrants: medium–high.** The moat is outcomes, not the model.
- **Buyer power: medium.** Charge only on a verified fix.
- **Supplier power (Meta, Google): medium–high.** Model router; budget at 2027 prices.
- **Substitutes (phone + notebook): high.** We run inside WhatsApp, so the substitute is our channel. """,
 say="""Quickly, the industry forces. The strongest one is the substitute: a phone and a notebook are free. Our answer is that we run inside WhatsApp, so the substitute becomes our channel.
Big suppliers like Meta and Google have power over us, so we can switch AI vendors and we budget at next year's prices. New entrants can build an AI wrapper cheaply, which is exactly why our moat is outcomes, not the model.""",
 why="Course vocabulary, kept to 30 seconds. Only the two forces that matter are spoken; the rest sit on screen for anyone who wants to read them."),

# ---------------------------------------------------------------- SCALE
dict(id="market", act="scale", sp="K", t=45, title="How big: the market, narrowed honestly",
 show="""An animated funnel narrowing level by level:
- **37,500** repair agencies in India
- **22,500** in Tier 2/3 towns, our segment
- **1,400** in Telangana + AP, our beachhead
- **120**, the Series A gate
Beside it, two revenue pools grow: Circuit fees ₹158–396 Cr a year → Keepwell earnable pool ₹1,005–2,370 Cr a year (fees + appliance plans + parts).
Footnote: "No official count exists. Built from ~2.5 lakh technicians (ICAP/CEEW), cross-checked with 15 Cr jobs and the ₹9,000 Cr market. Lands at ~147 jobs per agency; our agencies do 125." """,
 say="""How big can this get? No one has ever counted India's repair agencies, so we built the number three ways. From the government's technician estimate, from the number of repair jobs, and from the size of the market. All three agree on about thirty-seven thousand five hundred agencies.
Twenty-two thousand five hundred are in Tier 2 and 3 towns, which is our segment. Fourteen hundred are in our home states, and a hundred and twenty is our Series A gate.
Circuit alone is a solid niche. [click] But each record it creates opens plans, parts and claims, and that pool is a thousand to two thousand four hundred crore rupees a year. Circuit is the wedge. The record is the business.""",
 why="We place the funnel here, just before the growth plan, so every growth number that follows can be checked against the market (Y5 = 17% of the segment). The funnel ends at '120', which leads straight into the ask."),

dict(id="stages", act="scale", sp="K", t=55, title="The growth stages: from 14 agencies to 3,800",
 show="""Bars grow for paying agencies, **79 → 264 → 945 → 2,196 → 3,793** (Y1–Y5), with revenue labels **₹0.2 → 0.85 → 3.6 → 9.6 → 19.2 Cr**. Stage bands above them:
- Seed (Y1–Y2): Telangana + AP
- Series A (Y3–Y4): four southern states
- Y5: national Tier 2/3
Hiring rows below: field reps 1 → 3 → 10 → 18 → 24; team 12 → 84.
Chips: "EBITDA positive in Y5: +₹2.6 Cr" · "34 lakh machine records" · "Revenue per agency +33% as plans, parts and claims attach" · "Y5 = 17% of our segment (ceiling 20%)". """,
 say="""Here's how it scales, in stages. The seed takes us across Telangana and Andhra, to about two hundred and sixty agencies. A Series A funds field sales into the four southern states, then national Tier 2 and 3.
By year five, that's about thirty-eight hundred paying agencies, nineteen crore rupees of revenue, EBITDA-positive, and thirty-four lakh machine records. Revenue per agency rises by a third as plans, parts and claims attach. That's the record becoming the business.
And even then, we'd have just seventeen percent of our segment. We set ourselves a ceiling of twenty.""",
 why="Growth stages tied to funding rounds and hires, plus a self-imposed ceiling, avoids the 'flimsy growth claims' red flag and shows we know a Series A comes next."),

# ---------------------------------------------------------------- ASK
dict(id="ask", act="ask", sp="P", t=55, title="The ask",
 show="""Dark slide. Big number: **₹4.75 Cr seed**. Four term tiles:
- 24 months of runway
- minimum close ₹4.0 Cr
- priced Seed CCPS (compulsorily convertible preference shares)
- **20% equity** to one lead investor
Three columns:
- **What we have:** 14 paying agencies · 83% one-visit · 78% accuracy · ₹21 L in the bank
- **What the money proves (Series A gates):** 120 paying agencies by month 15 · 40,000 machine records by month 13 · +10 points one-visit at scale · ≥ 97% monthly retention · payback ≤ 7 months · 1 warranty-administrator letter of intent
- **What comes next:** Series A of ~₹8–10 Cr around month 20, and ~260 agencies by month 24""",
 say="""So here's our ask. We're raising four point seven five crore rupees, from one lead investor, as priced seed preference shares, for twenty percent of the company. That gives us twenty-four months of runway. Our minimum close is four crore.
Here's what we have today: fourteen paying agencies, a product that's getting smarter, and our own money and the angels' money spent carefully.
Here's what your money proves: a hundred and twenty paying agencies by month fifteen, forty thousand machine records, the one-visit gain holding at scale, and our first warranty partner. Those are our Series A gates. At month twenty, we raise a Series A from strength, not from need.""",
 why="Amount, instrument, equity, runway and milestones, as you asked; valuation, cap table and terms stay in backup. Milestones phrased as 'what your money proves' answer 'what do I get for this?'"),

dict(id="useoffunds", act="ask", sp="P", t=55, title="Why ₹4.75 Cr, and where every rupee goes",
 show="""Left: a bridge chart that builds bar by bar:
- costed requirements over 24 months: ₹548 L
- + 10% contingency: ₹55 L
- − revenue we'll earn: ₹105 L
- − cash in the bank: ₹21 L
- − government grant still due: ₹10 L
- = gap ₹467 L → **ask ₹475 L**
Right: use of funds by purpose, bars filling:
- **Finding product–market fit 38%**
- team and company 28%
- product 23%
- sales 10%
- working capital 1%
A teal note: "At Stage 2, the heaviest need is proving product–market fit. Every Series A gate is a PMF proof." A grey note: "Not spending on: consumer ads, a consumer app, a big office." """,
 say="""Why exactly four point seven five crore? We didn't pick a round number. We listed every requirement for the next two years and costed it: five hundred and forty-eight lakh. We added ten percent for surprises, then took out the revenue we'll earn, the cash we have, and the government grant still due. That leaves a gap of four hundred and sixty-seven lakh, and we rounded up to four seventy-five.
Where does it go? The biggest share, thirty-eight percent, goes to proving product–market fit: our AI and speech engineers, an agency-success team, and price tests in new towns. That's what a company at our stage should spend on. Then the team, the product, and only ten percent on sales, because we're building the sales engine, not buying growth.""",
 why="It shows the founders understand their stage's needs: the ask is an output of costed requirements (course Class Activity 1 method), not a wish. The 'not spending on' list signals discipline."),

dict(id="compliance", act="ask", sp="S", t=45, title="Trust and compliance, built in and budgeted",
 show="""A grid of the laws that matter. Each card shows the law, why it matters to us, and our status:
- **DPDP Act 2023 + Rules** (duties from May 2027): household data needs consent → consent-first record, hosted in Mumbai
- **IRDAI:** service plans are insurance products → sold *for* licensed insurers via a registered route; we never underwrite
- **CERT-In and the IT Act:** 6-hour incident reporting, 180-day logs → runbook in year 1
- **Consumer Protection and CCPA:** no dark patterns in quotes → the owner approves every quote
- **E-waste rules:** recycling (R5) → registered recycling partners
A trust strip: AI only / human approves / human only · 47 safety hard-stops, 0 incidents in 9 months.
Budget chip: "₹26 L of compliance and legal inside the ask". """,
 say="""Because we hold household data and will sell insurance products later, compliance isn't optional for us. It's part of the business.
The data protection law's main duties start in May 2027. We built consent-first from day one, and our data stays in India. Service plans are insurance, so we'll sell them for licensed insurers through a registered route, and we never underwrite. Every quote is approved by the owner, and safety calls are never left to the AI: forty-seven safety stops, zero incidents.
About twenty-six lakh of the ask is for legal and compliance work, so we're ready before the law requires it.""",
 why="It reassures on regulatory risk, the course's Compliance pillar, and ties it back to the ask, so it reads as a spending reason rather than a disclaimer."),

# ---------------------------------------------------------------- FUTURE
dict(id="exit", act="future", sp="P", t=45, title="The future, and who buys Keepwell",
 show="""Left: a stacked bar, "path to ₹100 Cr revenue":
- Circuit Tier 2/3: ₹23 Cr
- Tier 1: ₹13.5 Cr
- Service plans: ₹9 Cr
- Claims: ₹11 Cr
- Parts, resale, data: ~₹10 Cr
- = ~₹66 Cr by year 8; ₹100 Cr+ with price reviews and new categories
Right: four acquirer cards with precedents:
- **Warranty and protection platforms** (Servify, OneAssist, Onsitego, Asurion): Asurion bought Domestic & General (~£2.1 bn)
- **Home-services platforms** (Urban Company): IPO 103.6× subscribed
- **Recommerce and recycling** (Cashify, Attero): Quikr bought Zefo (~₹200 Cr)
- **Global field-service software**: ServiceTitan, $961M revenue""",
 say="""Where does this go? The plan gets us to about sixty-six crore rupees of revenue by year eight, from Circuit in every tier plus service plans and claims. Beyond a hundred crore, we'd need price reviews and new categories, like vehicles and homes, on the same record. We're not overclaiming that.
And who buys a company like this? Most likely, warranty and protection platforms, because our record prices their plans and proves their claims. Asurion paid about two billion pounds for a company like that. Home-services platforms, recommerce players and global field-service software are also natural buyers. We'd expect a strategic sale in years six to eight.""",
 why="It gives investors a believable exit with named buyer types and real precedents, plus an honest ceiling. This is Startup–Potential and the investor's 'how do I get my money back'."),

dict(id="close", act="future", sp="P", t=40, title="Back to Ramagundam",
 show="""Dark slide. The Ramagundam story replays, this time with Keepwell; each beat ticks green:
1. the voice note is answered in minutes, in Telugu, in the agency's name
2. Circuit knows this model, this town, this heat: it's almost always the capacitor
3. the technician arrives with a ₹350 part
4. fixed in one visit, verified, and the record grows by one
5. nobody buys a ₹38,000 AC
Final line: **"Keepwell becomes the record everyone checks before touching a machine."** Then: Prathyusha · Sri Charan · Kavyanth · raising ₹4.75 Cr. """,
 say="""Let's go back to Ramagundam. [click] With Keepwell, the son's voice note is answered in minutes, in Telugu, in Ramesh's name. [click] Circuit knows this model, this town, this heat: it's almost always the capacitor. [click] The technician arrives with a three-hundred-and-fifty-rupee part, [click] and it's fixed in one visit. The fix is verified, every agency on the network gets a little smarter, and nobody buys a new AC.
Today, that happens for fourteen agencies. With your help, it happens across India. [click] Keepwell becomes the record everyone checks before touching a machine.
Thank you.""",
 why="It mirrors the opening, closing the loop the audience has carried all along. End on the vision line, then stop talking."),
]

BACKUP = [
dict(id="b_valuation", title="Backup · Valuation (Q&A only)", sp="P", t=0,
 show="Three course methods: comparable ₹24.8 Cr post · scorecard ₹24.1 Cr · VC method ₹24.2 Cr. Pitched at ₹19 Cr pre / ₹23.75 Cr post, never above the VC-method price. Investor base case ~35% IRR (6.2×); conservative ~21%; aggressive ~47%. Walk-away floor ₹16 Cr pre.",
 say="Only if asked: 'We used three methods from the course and priced at the investor's own required-return price, so the base case clears a 35% IRR.'", why="Kept out of the main pitch, as decided; ready for Q&A."),
dict(id="b_captable", title="Backup · Cap table (Q&A only)", sp="P", t=0,
 show="After seed: founders 67.9% · angels (iSAFE) 2.1% · ESOP 10% · lead VC 20%. After Series A 54.3% founders; after Series B 46.2%.",
 say="Only if asked: 'Founders keep a majority through the Series A. One iSAFE converts at its cap, and its preference is capped at what the angels put in.'", why="Background check only."),
dict(id="b_terms", title="Backup · Terms we'd accept (Q&A only)", sp="P", t=0,
 show="1× non-participating preference · broad-based weighted-average anti-dilution · board 2 founders + 1 investor + 1 independent · 4-year vesting with credit since May 2025 · deal costs capped at ₹8 L · the lead reserves for its Series A pro-rata.",
 say="Only if asked: 'Standard, founder-friendly seed terms, the MediQuick template with two asks: vesting credit, and a reserve for the Series A.'", why="Background check only."),
]
