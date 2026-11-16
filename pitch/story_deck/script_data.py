# Keepwell story deck: the script, single source of truth.
# Each entry drives (1) the speaker-notes panel in index.html (press N) and (2) SCRIPT.md.
# SHOW = what is on screen (the proof / the visual). SAY = what the speaker says (the explanation).
# Every number traces to ../keepwell_model.xlsx or a step document in ../steps/.
# Illustrative case for the IIIT Hyderabad ESFS course pitch.

ACTS = [
    ("hook", "The hook"),
    ("team", "The team"),
    ("saw", "What we saw"),
    ("problem", "The problem"),
    ("keepwell", "Keepwell"),
    ("stage", "Where we are"),
    ("solution", "The solution"),
    ("proof", "The proof"),
    ("moat", "Why we win"),
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

dict(id="ramagundam", act="hook", sp="P", t=70, title="We took it lightly too — until one afternoon in Ramagundam",
 show="""Left: Sri Charan's dark quote card, "Our machines cost my family ₹10,000 a month. Never evenly." — with the line "We treated it as normal. Everyone does."
Right, the story builds click by click, one human beat at a time:
1. 46 °C in Ramagundam. A retired miner, 74, is home alone — and running a fever. At noon, his AC stops cooling.
2. The one person he trusts, Ramesh of the local agency, is up a ladder across town. His phone rings 14 times. The old man's Telugu voice note is never heard.
3. His son, 700 km away in Bengaluru, calls everyone he knows. Nobody can say what's wrong, who will come, or when.
4. The old man sits through two nights of that heat under a table fan before anyone opens the machine.
5. A small, quiet footnote card at the end: the fault was a ₹350 capacitor; by then the family had ordered a ₹38,000 new AC, three days away.
The line lands: "Nobody is the villain. The system has no memory." """,
 say="""We took this problem lightly too. In Sri Charan's family the machines cost about ten thousand rupees a month, never evenly, and we treated that as normal. Everyone does.
Then one afternoon changed that. [click] Ramagundam, forty-six degrees. A retired miner, seventy-four years old, home alone, running a fever. At noon, his AC stops cooling. [click] The one man he trusts, Ramesh of the local agency, is up a ladder across town. The phone rings fourteen times. The voice note, in Telugu, is never heard. [click] His son, seven hundred kilometres away in Bengaluru, calls everyone he knows. Nobody can tell him what's wrong, who will come, or when. He is helpless, and so is everyone around that old man. [click] He sat through two nights of that heat under a table fan before anyone even opened the machine. [click] And when someone finally did? A three-hundred-and-fifty-rupee part. The family had already ordered a new AC.
Nobody in this story is the villain. Ramesh is good at his job. The son did everything a son can do. The system just has no memory — and when a system has no memory, it isn't money that gets lost first. It's people left suffering, with nobody able to help.""",
 why="The hook is the human intensity of Ramagundam — a sick old man in 46° heat whom nobody could help in time — not the money. The ₹350 / ₹38,000 detail stays only as a quiet footnote. The people are a composite (disclosed in the data room); the heat, the town and the reflex to replace are real."),

# ---------------------------------------------------------------- TEAM
dict(id="team", act="team", sp="P", t=55, title="Three founders, one from each side of the problem",
 show="""A triangle with the machine record at the centre. Each corner is one side of the problem with its founder card:
- **Agency network: Prathyusha, CEO.** FixNear: 1,200 technicians, 14 towns, sold in 2022.
- **Household and AI: Sri Charan, CTO.** 7 years of Indian-language voice AI; built Circuit himself.
- **Brand and warranty: Kavyanth, COO.** Ran 300+ service partners and a warranty-claims desk.
A ribbon underneath: "Full-time since May 2025 · ₹15 lakh of our own money · incubated at CIE-IIITH · DPIIT-recognised". """,
 say="""That afternoon is why the three of us are standing here. This problem has three sides, and each of us spent years on one of them.
I'm Prathyusha. I co-founded FixNear, a technician network of twelve hundred people across fourteen towns in Andhra and Telangana, and sold it in 2022. I learned the hard way that taking the customer away from the local agency doesn't work.
Sri Charan spent seven years building voice AI in Indian languages, and he built our product himself. Kavyanth ran a brand's network of more than three hundred service partners, and its warranty-claims desk.
Agency, household, brand. All three of us have been full-time since May 2025, with our own money in.""",
 why="The course gives the team 45 of 90 points. Coming straight after the story, the team lands as 'the people who saw this first-hand', not a CV slide. Each founder gets one line of proof: an exit, a shipped product, a network."),

# ---------------------------------------------------------------- WHAT WE SAW
dict(id="watched", act="saw", sp="S", t=60, title="We didn't read about it. We watched it happen.",
 show="""A proof wall of real artefacts. The brand-bot card is the actual screen recording, playing on the slide:
1. **A brand's WhatsApp bot failing, on camera** (the full recording, playing on loop): "There is some API related issue please try again later" … she types "What is API" … her last message: "My request was not done."
2. **A water purifier** with a local agency's sticker taped on, and the next service date written over the brand's label in marker
3. **A household's repair diary**: handwritten pages of what was fixed, when, by whom, for how much — two pages shown
4. **A gas cylinder** with its refill date written on it in marker
5. **Our own whiteboard**: "machine fails → technician travels → discovers the problem → another visit" vs "symptoms + photo + model → prepared technician → one visit"
Personal details are blurred in the images. Tag: "Real · from our discovery interviews". Click any image for full screen. """,
 say="""I'm Sri Charan. We didn't just read about this problem. We went into homes and watched it happen. [point at the playing video]
This is a real brand's WhatsApp bot, recorded in one of our interviews. A woman asks for her water purifier to be serviced. The bot says there's an API issue. She asks — what is API? Then it demands a job ID she doesn't have. Watch her last message: "My request was not done."
And look at what people do instead. A local agency has taped its own sticker onto the machine, and the family wrote the next service date in marker over the brand's label. This family keeps a handwritten diary of every repair. This one writes the refill date on the gas cylinder itself.
People are already building the machine's memory — on stickers, in diaries, in marker pen. The demand is there. The tool isn't.""",
 why="This is the trust moment for the problem: real, first-hand evidence instead of statistics. The bot recording playing live is the strongest 'wow' in the deck, and the sticker and diary show people already doing a paper version of Keepwell."),

dict(id="listened", act="saw", sp="S", t=55, title="We listened before we built",
 show="""The research funnel builds on the left:
- household survey: 19 responses, 12 qualified
- 7 recorded household interviews
- 18 agency-owner interviews
Named quote cards on the right:
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

# ---------------------------------------------------------------- PROBLEM
dict(id="problemmap", act="problem", sp="S", t=55, title="The full problem map: 14 problems, scored, grouped into 5 scenarios",
 show="""Left: the problem map as ranked score bars (out of 30), each tagged with who suffers:
- P2 · Intake chaos: missed calls, voice notes, no job record — agencies — **24**
- P1 · Unprepared first visit: wrong diagnosis, wrong part, repeat trips — agencies + households — **23**
- P3 · No machine history: lost invoices, unknown warranty — households — **22**
- P7 · Claims triage for administrators and OEMs — industry — **22**
- P4 · Warranty refusal, unresolved claims — households — **20**
- P5 · No fair-price benchmark — households — **20**
- P8 · Low plan uptake and renewals — households + insurers — **20**
- P6 · Wrong or unavailable spare parts — agencies — **18**
- P9 · Old-appliance exit: buyback, refurb, scrap — everyone — **18**
Right: the five scenarios they group into, as cards:
- **A · Prepared Visit** (P1 + P2) — the entry wedge → becomes **Circuit · live**
- **B · The two-sided record** (P3, P5, P8) — year 1–2
- **C · Claims triage** (P7) — year 2
- **D · Consumer advocate** (P4) — folded into B
- **E · The circular loop** (P9, P11, P6) — the stated vision
[click] A teal band lands: "We enter where impact is highest and barriers are lowest: the prepared visit." """,
 say="""When we put everything we'd seen and heard together, it wasn't one problem. We mapped fourteen distinct problems across a machine's life, and we scored every one of them: impact, effort, how hard it is to build, how hard it is to sell.
Look at the top of the list. Intake chaos. The unprepared first visit. The missing machine history. Claims that nobody can verify. The same missing record sits underneath all of them.
And the fourteen group naturally into five solvable scenarios: the prepared visit, the two-sided record, claims triage, the consumer advocate, and the circular loop at end of life. [click]
So we're not chasing one complaint. We're working down a scored map, and we enter where the impact is highest and the barriers are lowest: the prepared visit.""",
 why="It shows the broad problem set and that the entry point was chosen by scoring, not instinct — Stage 2 discipline. It also plants the five scenarios that later become the roadmap. Source: the team repo's problem map and impact-effort matrix."),

dict(id="bothsides", act="problem", sp="S", t=60, title="What goes wrong, on both sides",
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
 say="""Here's the size of it, on both sides.
For the agency, the pain starts at the very first moment. About one request in eight is simply lost: a missed call, a voice note nobody follows up. The technician goes in blind, often with the wrong part, so a lot of jobs need a second trip, and that costs the agency money.
For the household, nothing can be checked: not the price, not the part, not whether the job is really done. Fifty-five percent of families have had a defective machine, and only twenty-one percent of those were made whole. Almost half the complaints are about chasing someone. And in most homes the person who decides, the person who pays and the person who opens the door aren't the same.
Two sides, one missing thing: a shared memory of the machine.""",
 why="It proves we understand the buyer (the agency) and the user (the household) separately, which is where most repair pitches blur. The broken thread keeps the one idea visible."),

dict(id="lifecycle", act="problem", sp="S", t=50, title="From one repair to a machine's whole life",
 show="""A ring of seven life stages: bought, used, fails, repaired, maintained, resold, recycled. Each carries a red tag:
- technician arrives blind
- warranty can't be proven
- plan sold to the wrong home
- resale buyer can't trust it
- recycled too early
[click] A teal ring draws through all seven stages: "One record, every stage". [click] The vision line appears: "Every machine an Indian home owns is cared for across its whole life: repaired right, remembered always, and never wasted." Analogy chips: CIBIL → borrowers · Carfax → used cars · nothing, yet → household machines. """,
 say="""And when we zoomed out, the small problem became a big one. Every machine lives one life: bought, used, fails, repaired, maintained, resold, recycled. At every single stage it starts from zero. The technician arrives blind, the warranty can't be proven, the plan is sold to the wrong home, the resale buyer can't trust it. [click]
The same missing piece sits under all of them: the machine's history. [click] So the vision we committed to is bigger than repair: every machine an Indian home owns, cared for across its whole life. India has CIBIL for borrowers. The world has Carfax for used cars. For household machines, there is nothing. Yet.""",
 why="Here the problem widens into a venture-scale category and the vision is stated — before the company is even named, so the name lands as the answer two slides later."),

dict(id="bigproblem", act="problem", sp="S", t=55, title="It isn't one family. It's 15 crore repairs a year.",
 show="""Four counters count up, each with a small picture:
- 15 Cr appliance repairs a year
- 27 Cr fridges, washing machines and ACs with no shared record
- ₹550 Cr of technician time lost to repeat trips each year
- 37,500 repair agencies running on a phone and a notebook
A red "broken thread" runs under all four. Source line: repo; Data for India; CLASP/BEE 2024; ICAP/CEEW. """,
 say="""Now put numbers on all of that. India does about fifteen crore appliance repairs a year. There are about twenty-seven crore fridges, washing machines and ACs in our homes, and not one has a shared history.
Technicians go in blind, and when the first visit doesn't fix it, someone goes back. If India fixed things at the global first-visit rate, that would still be about five hundred and fifty crore rupees of technician time wasted every year.
And the work is done by about thirty-seven thousand five hundred small agencies, on one phone and a notebook. The problem isn't skill. It's memory.""",
 why="The scale lands only after the full problem set has been told, as decided. Four numbers, each with one job: frequency (15 Cr), the asset with no record (27 Cr), money lost (₹550 Cr) and the customer we sell to (37,500). Say the ₹550 Cr caveat out loud — it's the honest way to quote it."),

# ---------------------------------------------------------------- KEEPWELL
dict(id="keepwell", act="keepwell", sp="S", t=40, title="Keepwell: the care layer for everything a home owns",
 show="""Dark slide. The broken thread from the last slide joins into the Keepwell mark. Below it, a machine "record card" fills in line by line:
- Voltas 1.5 T split AC · bought Mar 2021
- Warranty: compressor till Mar 2026
- Repairs: 3, each verified
- Parts fitted: capacitor, Aug 2026
- Next service: Apr 2027
Tagline: "One living record per machine, and a service at every stage of its life." """,
 say="""That's why we started Keepwell. Keepwell gives every machine in an Indian home a memory. One living record of what it is, what went wrong, what was fitted and what it needs next, built only with the owner's consent.
On top of that record, a service at every stage of the machine's life. Keepwell is the CIBIL of household machines: the history that everyone checks first.""",
 why="The company is named only after the room has felt the problem, its full map, its whole-life breadth and its scale — so the name arrives as the answer. The record card makes 'memory' concrete."),

# ---------------------------------------------------------------- STAGE
dict(id="companystage", act="stage", sp="P", t=70, title="Where we are: the stage, the journey, the money",
 show="""One picture in three layers, read top to bottom.
Top: the company stage as a simple three-step path — build the product → **find the business model (we are here)** → scale — with our badge on step two.
Middle: the journey timeline, milestone by milestone: discovery (Jan–Apr 2025) → incorporated · full-time · CIE-IIITH (May 2025) → prototype, 2 design partners (Jun–Sep) → **₹30 L from two operator angels** (Oct) → production, Mumbai (Jan 2026) → paid price test, 5 agencies (Feb–Apr) → government seed fund ₹20 L sanctioned (Mar) → 5 → 14 paying agencies (May–Oct) → accuracy gate passed (Aug) → **raising the seed (now)**.
Bottom: three money tiles that read left to right —
- **RAISED ₹55 L** — founders ₹15 L · operator angels ₹30 L (iSAFE) · Startup India Seed Fund ₹10 L of ₹20 L
- **SPENT ₹34 L** — stipends ₹19.5 L · contract engineer ₹6 L · cloud + AI ₹3 L · pilot field work ₹3 L · legal ₹2.5 L
- **IN THE BANK ₹21 L**
A strip underneath — what that money built: the team · the research · the prototype · production · 14 paying agencies. """,
 say="""So where is Keepwell today? We're at stage two. The product exists, customers pay for it, and we're proving the business model.
Here's the whole journey on one line. Four months of listening. Incorporated in May 2025, all three of us full-time, incubated at CIE-IIITH. The prototype by September. Then two operator angels — one built a home-services company, one ran service at a durables brand — put in thirty lakh, and they introduced three of our first five agencies. Production in January. A paid price test in the spring. The government's seed fund sanctioned in March. Fourteen paying agencies by October.
And here's the money, plainly. Raised: fifty-five lakh. Spent: thirty-four — modest stipends, one contract engineer, and the pilots. In the bank: twenty-one. That thirty-four lakh bought the team, the research, the prototype, production, and fourteen paying customers.""",
 why="One intuitive slide answers four diligence questions at once: what stage are you at, what have you done, who backed you, and what did you do with their money. Every rupee is itemised before anyone asks."),

# ---------------------------------------------------------------- SOLUTION
dict(id="roadmap", act="solution", sp="S", t=40, title="The roadmap: one record, a product at each stage",
 show="""A rising staircase of six steps, each with its product, its stage of life and who pays:
- **R1 · live:** Circuit, the AI desk for repair agencies (agency pays per verified fix)
- **R2 · ~12 months:** Home Memory + Service Plans (insurer commission)
- **R3 · year 2:** Claims triage (warranty administrators, OEMs)
- **R4:** Parts marketplace (parts sellers)
- **R5:** Resale & recycling (buyers, producers, recyclers)
- **Phase 3:** Data services, consent-first (brands, insurers)
The record runs under every step as one teal line. """,
 say="""From that scored problem map came the roadmap — the five scenarios, in order, as products. Each step is a product on the same record, with a different payer.
We start with Circuit for repair agencies, which is live today. Next, Home Memory and service plans, sold for insurers. Then claims triage for warranty administrators, then parts, then resale and recycling, and finally data services, always with consent.
Each step is paid for by someone who already spends money at that stage of the machine's life.""",
 why="It shows a clear expansion path, scored under Product–Potential, and that each step has its own payer. The order follows the team repo's build order and the scenario scores."),

dict(id="whycircuit", act="solution", sp="S", t=35, title="Why we start with repair",
 show="""Three overlapping circles:
- **The pain:** the moment a household needs help
- **The payer:** the agency earns on every job
- **The truth:** the only moment someone opens the machine and sees what's wrong
The overlap lights up: "The repair". Then the name appears in the middle: **Circuit**. """,
 say="""Why start with repair? Because it's the only moment where three things meet.
The pain is highest, because the machine is broken. The payer is there, because the agency earns on that job. And it's the only moment someone opens the machine and records what's really wrong.
Start there, and the record fills itself as a by-product of work that's already happening. [click] That's Circuit.""",
 why="It answers 'why this wedge?' in 35 seconds and hands over to the product."),

dict(id="circuit", act="solution", sp="S", t=55, title="Circuit, simply",
 show="""Left: the six steps as cards, lighting up in order:
1. 🎙 **Customer sends a voice note**, in Telugu, Hindi, Tamil, Kannada, Marathi or English
2. **Circuit understands** and reads it back
3. **Finds the likely fault and the part to carry**, using this machine's history and every past repair
4. **Quotes from the agency's own rate card**; the owner approves
5. **Sends the technician a job card** he can read in ten seconds
6. **The technician confirms the fix.** The record updates, Circuit gets smarter, and we earn ₹40.
Beside the six steps, a browser frame with the **live Circuit site (circuit-landing-page.netlify.app) scrolling end to end like a video** — the same product, as an agency owner first meets it. Underneath: "AI reads and drafts. People decide anything with money or safety." """,
 say="""Here's what Circuit does, in plain words. A customer sends the agency a voice note on WhatsApp, in their own language. Circuit understands it and reads it back. It looks at the machine's history and everything learned from past repairs, and tells the technician the likely fault and the part to carry. It builds the quote from the agency's own price list, and the owner approves it. The technician gets a job card he can read in ten seconds.
And when he confirms what was actually wrong, three things happen at once. The machine's record updates, Circuit gets smarter for the next job, and only then do we earn forty rupees.
What's playing on the right is our live website, scrolling — the same six steps, exactly as an agency owner first sees them.""",
 why="No architecture or technical terms. The last step carries the whole business: one event that is the fix, the learning and the revenue."),

dict(id="demo", act="solution", sp="S", t=60, title="See how easy it is",
 show="""Three tabs on the demo stage:
- **The agency's WhatsApp** (opens first): an animated chat. A Telugu voice note arrives, Circuit reads it back, a photo of the AC label, an owner-approved quote, then the technician's job card and the green tick: "Fixed in one visit · record updated".
- **The website, scrolling**: the live landing page (circuit-landing-page.netlify.app) auto-scrolling top to bottom like a video, beside three snippets cut straight from it — "the first visit is almost never the repair visit", the four-step "how it works", and "you keep the customer, you keep the margin". Each snippet opens full-screen on click.
- **A real run, 30× speed**: the recorded run of the prototype (real).
Ease chips along the bottom: no new app · set up in one visit · 6 languages · 30 free days · pay only when a fix is verified · the owner approves every quote. """,
 say="""And it's genuinely easy — let me show you rather than tell you. [chat plays] For the customer, nothing changes. Same agency, same WhatsApp number, their own language. For the owner, the job arrives ready, with a quote he only has to approve. For the technician, a ten-second card with the part to carry. [switch tab] This is our live website — watch it scroll: the repair-ready checklist, how it works, the pricing. Everything a shop owner needs to understand us in one page. [switch tab] And this is a real run of the system, sped up thirty times.
Setting up takes one visit: the owner's price list and his WhatsApp number. Thirty free days, and after that the agency pays only when a fix is verified.""",
 why="Investors judge ease of adoption by watching it. The scrolling landing page plays like a product video without needing one, and the real run proves the demo isn't a mock-up."),

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
 why="It turns growth from an assertion into a formula with evidence, and sets up the plan and the use of funds."),

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
 why="It answers 'why hasn't X done it' with a picture. Keepwell sitting alone in a corner is the image investors remember."),

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
 why="The funnel sits right before the growth plan, so every growth number that follows can be checked against the market. The funnel ends at '120', which leads straight into the plan and the ask."),

dict(id="stages", act="scale", sp="K", t=55, title="The plan, stage by stage: seed → Series A → year five",
 show="""Left: one clean chart. Bars = paying agencies by year (**79 → 264 → 945 → 2,196 → 3,793**), revenue above each bar (₹0.2 → 0.85 → 3.6 → 9.6 → 19.2 Cr), EBITDA beneath. Stage bands across the years: **Seed (this raise): Telangana + AP** · **Series A (~month 20): the south, then wider** · **Year 5: national Tier 2/3**.
Right: the plan in three plain, numbered sentences:
1. **The seed** takes us from 14 to ~264 agencies across Telangana and AP, and proves the Series A gates.
2. **A Series A** around month 20 funds field sales into the four southern states, then national.
3. **Year 5:** 3,793 agencies · ₹19.2 Cr revenue · EBITDA **+₹2.6 Cr** · 34 lakh machine records.
Chips: revenue per agency +33% as plans, parts and claims attach · Y5 is 17% of our segment (our own ceiling: 20%). """,
 say="""Here's the plan, stage by stage. This seed round takes us across Telangana and Andhra: from fourteen agencies to about two hundred and sixty, and it proves the gates a Series A investor will ask for. The Series A, around month twenty, funds field sales into the four southern states, and then national Tier 2 and 3.
By year five, that's about thirty-eight hundred paying agencies, nineteen crore rupees of revenue, EBITDA positive, and thirty-four lakh machine records. Revenue per agency rises by a third as plans, parts and claims attach — that's the record becoming the business.
And even then we'd hold just seventeen percent of our segment. We set ourselves a ceiling of twenty.""",
 why="Redesigned to be read at a glance: one chart on the left, the plan as three numbered sentences on the right. Growth stages tied to funding rounds avoids the 'flimsy growth claims' red flag."),

# ---------------------------------------------------------------- ASK
dict(id="compliance", act="ask", sp="S", t=45, title="Before we ask: trust and compliance, built in and budgeted",
 show="""A grid of the laws that matter. Each card shows the law, why it matters to us, and our status:
- **DPDP Act 2023 + Rules** (duties from May 2027): household data needs consent → consent-first record, hosted in Mumbai
- **IRDAI:** service plans are insurance products → sold *for* licensed insurers via a registered route; we never underwrite
- **CERT-In and the IT Act:** 6-hour incident reporting, 180-day logs → runbook in year 1
- **Consumer Protection and CCPA:** no dark patterns in quotes → the owner approves every quote
- **Safety (BIS, CEA):** gas, refrigerant, high voltage → hard-stops outside the AI: 47 triggered, 0 incidents in 9 months
- **E-waste rules:** recycling (R5) → registered recycling partners
A trust strip: AI only / human approves / human only. Budget chip: "₹26 L of compliance and legal inside the ask". """,
 say="""Before we talk about money, one thing matters. We're asking you to back a company that holds household data and will sell insurance products later — so for us, compliance isn't a slide. It's part of the product.
The data protection law's main duties start in May 2027. We built consent-first from day one, and our data stays in India. Service plans are insurance, so we'll sell them for licensed insurers through a registered route, and we never underwrite. Every quote is approved by the owner, and safety calls are never left to the AI: forty-seven safety stops, zero incidents in nine months.
And about twenty-six lakh of what we're about to ask for is legal and compliance work, so we're ready before the law requires it.""",
 why="Placed deliberately just before the ask: the last thing an investor hears before the number is that the company is clean, safe and ready for regulation — a reason to invest, not a disclaimer."),

dict(id="askneed", act="ask", sp="P", t=45, title="Before the ask: what the next 24 months need",
 show="""A bridge chart builds bar by bar:
- costed requirements for the next 24 months: ₹548 L
- + 10% contingency: ₹55 L
- − revenue we'll earn: ₹105 L
- − cash in the bank: ₹21 L
- − government grant still due: ₹10 L
- = **the gap: ₹467 L**
Beside it, where every rupee goes, by purpose: **finding product–market fit 38%** · team and company 28% · product 23% · sales 10% · working capital 1% — with the note "at Stage 2, the heaviest need is proving product–market fit; every Series A gate is a PMF proof", and what we deliberately don't spend on: consumer ads, a consumer app, a big office. """,
 say="""Now, the money — and we didn't start from a round number. We started from the requirement. We listed everything the next twenty-four months need and costed every line: five hundred and forty-eight lakh. We added ten percent for surprises, then subtracted the revenue we'll earn, the cash we have, and the grant that's still due. The gap is four hundred and sixty-seven lakh.
And look at where it goes. The biggest share, thirty-eight percent, goes to proving product–market fit: our AI and speech engineers, the agency-success team, price tests in new towns. That is exactly what a company at our stage should spend on. We don't spend on consumer ads, a consumer app, or a big office.
So that's the requirement. Here is the ask.""",
 why="Exactly the order asked for: the investor first understands what a startup at this stage needs and why, so the number on the next page lands as a calculation, not a wish."),

dict(id="ask", act="ask", sp="P", t=70, title="The ask, on its own page",
 show="""A full dark page for the ask alone.
- **₹4.75 Cr seed**, huge — "to take Circuit from 14 agencies to ~260, and reach the Series A from strength."
- The one-line bridge from the previous page: costed need ₹602.9 L − revenue − cash − grant = gap ₹467 L → rounded to ₹475 L.
- Four term tiles: **24 months** of runway · **₹4.0 Cr** minimum close (21 months) · **priced Seed CCPS**, one clean class · **20% to one lead seed investor**.
- Three columns:
  - **What we have today:** 14 paying agencies · 83% one-visit · 78% accuracy · ₹21 L in the bank
  - **What your money proves — the Series A gates:** 120 paying agencies by month ~15 · 40,000 machine records by month ~13 · +10 points one-visit at scale · ≥ 97% retention · payback ≤ 7 months · 1 warranty-administrator LOI
  - **What comes next:** ~260 agencies and 1.37 lakh records by month 24 → a Series A of ~₹8–10 Cr around month 20, raised from strength → Tier 1, plans and claims. """,
 say="""The ask is four point seven five crore rupees — the four-sixty-seven-lakh gap you just saw, rounded up to the nearest twenty-five.
The shape of the round, plainly. Twenty-four months of runway, so we never negotiate the next round out of desperation; our minimum close is four crore, which is twenty-one months. Priced seed preference shares — one clean class of stock, the instrument every later investor expects. And twenty percent to a single lead investor, because a clean cap table today is what keeps the Series A simple tomorrow.
What does your money buy? Three things. Today you're buying what exists: fourteen paying agencies and a product that gets smarter every week. Over the next fifteen months it proves the Series A gates — a hundred and twenty paying agencies, forty thousand machine records, retention above ninety-seven percent, payback under seven months, and our first warranty partner. And then it buys position: at month twenty we raise a Series A of eight to ten crore from strength, not from need.
One number, one instrument, one lead, and a defined set of proofs. That's the ask.""",
 why="The ask gets its own full page, as the most important slide: the number, the one-line bridge back to the requirement, every term stated and justified in words, and the have / prove / next structure answering 'what do I get'. Valuation, cap table and terms stay in backup."),

# ---------------------------------------------------------------- FUTURE
dict(id="future", act="future", sp="P", t=60, title="Why now — and who buys Keepwell in the end",
 show="""Top band — why this is the moment, four tiles:
- **₹4.5 a job:** Indian-language AI finally cheap enough for a 5-technician shop (against a ₹40 fee)
- **The repair wave is ahead:** only 1 in 10 homes has an AC; India needs ~5× more technicians by 2037
- **Regulation favours repair:** Right to Repair portal, Repairability Index, Kigali 2028
- **DPDP, May 2027:** consent duties arrive; the consent-first record built now becomes the standard others must retrofit
Below, left: the path to ₹100 Cr revenue as a stacked bar (Circuit Tier 2/3 ₹23 · Tier 1 ₹13.5 · plans ₹9 · claims ₹11 · parts/resale/data ~₹10 = ~₹66 Cr by year 8; ₹100 Cr+ with price reviews and new categories).
Right: who buys, four acquirer cards with precedents — **warranty and protection platforms** (Servify, OneAssist, Onsitego, Asurion; Asurion bought Domestic & General, ~£2.1 bn) · home-services platforms (Urban Company; IPO 103.6× subscribed) · recommerce and recycling (Cashify, Attero; Quikr bought Zefo, ~₹200 Cr) · global field-service software (ServiceTitan, $961M revenue).
Land: "A strategic sale in years 6–8, once the record and claims lines are proven." """,
 say="""Why is this the moment to invest? Four reasons. Indian-language AI just became cheap enough for a five-technician shop — that wasn't true two years ago. The repair wave is still ahead of us: only one in ten homes has an AC today. Regulation is opening repair up. And the data protection law lands in May twenty twenty-seven — whoever has built the consent-first record by then becomes the standard everyone else has to retrofit. The window is open, and it won't stay open.
And where does it end? The plan reaches about sixty-six crore of revenue by year eight; past a hundred crore needs new categories on the same record, and we say that plainly. The buyers already exist. Warranty and protection platforms are the most likely — our record prices their plans and proves their claims, and Asurion paid about two billion pounds for exactly such a company. Home-services platforms, recommerce players and global field-service software are the others. We'd expect a strategic sale in years six to eight.""",
 why="'Why now' gives the urgency the deck was missing, and the exit answers 'how do I get my money back' with named buyer types and real precedents — both on one slide, right after the ask, as the forward look before the closing story."),

dict(id="close", act="future", sp="P", t=40, title="Back to Ramagundam",
 show="""Dark slide. One click, and the whole ending plays out on its own — the Ramagundam story replays with Keepwell, each beat ticking green in sequence:
1. the voice note is answered in minutes, in Telugu, in the agency's name
2. Circuit knows this model, this town, this heat: it's almost always the capacitor
3. the technician arrives the same afternoon, with a ₹350 part in his pocket
4. fixed in one visit · verified · the record grows by one, and every agency gets smarter
5. a 74-year-old man sleeps that night in a cool room
…then the final line fades in beneath: **"Keepwell becomes the record everyone checks before touching a machine."** Prathyusha · Sri Charan · Kavyanth · raising ₹4.75 Cr. """,
 say="""Let's go back to Ramagundam one last time. [click — then let the screen play on its own]
With Keepwell, the son's voice note is answered in minutes, in Telugu, in Ramesh's name. Circuit knows this model, this town, this heat — it's almost always the capacitor. The technician arrives the same afternoon with a three-hundred-and-fifty-rupee part, fixes it in one visit, and the fix is verified — so every agency on the network gets a little smarter. And a seventy-four-year-old man sleeps that night in a cool room.
Today that happens for fourteen agencies. With your help, it happens across India. Keepwell becomes the record everyone checks before touching a machine.
Thank you.""",
 why="It mirrors the opening and resolves the human story, not the money story. One click: the beats cascade on their own, so the speaker never touches the clicker again. End on the vision line, then stop talking."),
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
