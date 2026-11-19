# Keepwell: The Whole Story, Told From the Outside
> **Illustrative case.** Founder histories, the company timeline, the pilot results and the financials are assumptions made for the IIIT Hyderabad ESFS course pitch. They are kept consistent with the team repo and with each other. Section 18 lists exactly what is real and what is illustrative.

*This document is for someone who was not in the room: an investor, a mentor, a judge. It tells everything Keepwell did, from the first problem to the money we are asking for. Every claim names its proof. You can read it top to bottom as a story, or jump to a part and follow the links to the evidence.*

---

## How to read this document
**Every fact carries a tag that tells you where it comes from:**

| Tag | Meaning | How to check it |
|---|---|---|
| **[Real]** | Real research, a real build, a real public source | Linked source, our survey, our interview recordings, our prototype |
| **[repo]** | The team's research repo (market, competitors, costs, law, product spec) | Files in the root of this repo, linked inline |
| **[Story]** | The company's operating history: timeline, pilot, traction | Steps 2 and 6; the data room (section 17) |
| **[Model]** | Calculated in the financial model | [`keepwell_model.xlsx`](keepwell_model.xlsx): 530 formulas, 0 errors, all checks pass. The tab is named each time |

**The chain of proof.** Every number in this story comes from one of three places, and the places link to each other:
1. **The step documents** ([`steps/`](steps/)): the reasoning behind each decision, with its sources.
2. **The financial model** ([`keepwell_model.xlsx`](keepwell_model.xlsx), rebuilt by [`build_model.py`](build_model.py)): every money number.
3. **The proof pack** ([`proof_pack/`](proof_pack/)): customer quotes, the Q&A bank, the demo, the data-room index.

Nothing in the deck is typed by hand. The deck is generated from [`deck/deck_content.py`](deck/deck_content.py), whose numbers trace back to the model.

---

## Contents
- [Prologue: A ₹350 part and a ₹38,000 mistake](#prologue-a-350-part-and-a-38000-mistake)
- [The ending first: where Keepwell stands today](#the-ending-first-where-keepwell-stands-today)
- [Part 1. A problem nobody had measured](#part-1-a-problem-nobody-had-measured)
- [Part 2. Three people who had each seen one side of it](#part-2-three-people-who-had-each-seen-one-side-of-it)
- [Part 3. Listening before building](#part-3-listening-before-building)
- [Part 4. The idea that is bigger than the product](#part-4-the-idea-that-is-bigger-than-the-product)
- [Part 5. Building Circuit](#part-5-building-circuit)
- [Part 6. The first money, and why it was structured that way](#part-6-the-first-money-and-why-it-was-structured-that-way)
- [Part 7. The test that went against us](#part-7-the-test-that-went-against-us)
- [Part 8. Nine months in the field](#part-8-nine-months-in-the-field)
- [Part 9. Does the agency actually win?](#part-9-does-the-agency-actually-win)
- [Part 10. Why nobody can catch up](#part-10-why-nobody-can-catch-up)
- [Part 11. The engine: how one agency becomes a business](#part-11-the-engine-how-one-agency-becomes-a-business)
- [Part 12. How big this can get](#part-12-how-big-this-can-get)
- [Part 13. What we need now, and why exactly that much](#part-13-what-we-need-now-and-why-exactly-that-much)
- [Part 14. The deal](#part-14-the-deal)
- [Part 15. Trust, law and whose data it is](#part-15-trust-law-and-whose-data-it-is)
- [Part 16. How we tried to break our own story](#part-16-how-we-tried-to-break-our-own-story)
- [Part 17. What could go wrong, and what we do then](#part-17-what-could-go-wrong-and-what-we-do-then)
- [Part 18. What is real and what is illustrative](#part-18-what-is-real-and-what-is-illustrative)
- [Epilogue: What the money becomes](#epilogue-what-the-money-becomes)
- [Appendix A. Proof index: every claim and where to check it](#appendix-a-proof-index-every-claim-and-where-to-check-it)
- [Appendix B. Every number on one page](#appendix-b-every-number-on-one-page)

---

## Prologue: A ₹350 part and a ₹38,000 mistake
It is a 46 °C afternoon in Ramagundam, an industrial town in Telangana. A retired coal miner's air conditioner stops cooling at noon.

He calls the local repair agency he has trusted for years. The owner, Ramesh, is up a ladder on another job. His one phone rings fourteen times. The old man's son, 700 km away in Bengaluru, sends a Telugu voice note to the agency's WhatsApp. Nobody writes it down. By evening, the son gives up and opens a shopping app: a new AC, ₹38,000, delivered in three days.

The fault was a **₹350 capacitor**.

Nobody in this story is the villain. Ramesh is good at his job. The son did what any worried son would do. **The system simply has no memory.** Nobody knew this machine's model, its history, or the fact that this exact fault on this exact model is almost always a capacitor.

*The people are a composite; the town, the heat, the scale of the gap and the reflex to replace instead of repair are real.* **[Real story, composite people]** ([Step 1.8](steps/01_vision_and_narrative.md))

One of our founders, Sri Charan, says it in one line from his own family: *"Our machines cost my family ₹10,000 a month, never evenly."* **[Real]**

This document is the story of how three people set out to give every machine in an Indian home a memory, and what they can prove so far.

---

## The ending first: where Keepwell stands today
Before the story, here is where it lands, so you know what each part is building towards.

**Keepwell** is building *the care layer for everything a home owns*: one living record per household machine, with a product at every stage of its life. Its first product, **Circuit**, is an AI desk that works inside a repair agency's own WhatsApp.

**As of November 2026** [Story] ([Step 6.4](steps/06_traction_and_validation.md)):
- **14 agencies pay us** every fortnight. 15 have joined; one has left.
- About **8,200 repair jobs** have gone through Circuit.
- Jobs closed in **one visit rose from 71% to 83%** and have held there for six months.
- **96% of customer requests** now become a job; before, about 1 in 8 was lost.
- Circuit's **root-cause accuracy climbed from 62% to 78%**. Since June, most of that gain has come from repairs that technicians verified. That is the system learning in production.
- **11 of 14 owners** say they would be "very disappointed" without it.
- We spent **₹34 lakh in 18 months** to get here, and have **₹21 lakh** in the bank.

**What we are asking for:** **₹4.75 Cr** from one lead seed investor, at **₹19 Cr pre-money**, for 24 months. That takes Circuit from 14 to about 260 paying agencies and gets us to a Series A from strength.

The rest of this document shows how we got here, and the proof behind every one of those lines.

---

## Part 1. A problem nobody had measured
### 1.1 The size of the problem
India does about **15 crore appliance repairs a year** (fridges, washing machines, ACs). **[repo]** This figure has a single 2017 source, so we checked it two other ways (Part 12). The repair market is worth about **₹9,000 Cr a year**. **[Real]** ICICI Direct, citing the Urban Company DRHP, puts install, repair and service at ₹16,500–17,000 Cr, about half of it repair. BlueWeave puts the market at ~$981M, growing 8.18% a year. ([Step 1.9](steps/01_vision_and_narrative.md), [Step 4.3](steps/04_market_and_problem.md))

Most of this work is done by **small independent agencies**: an owner, 2 to 10 technicians, one phone, one WhatsApp number, a notebook. Households prefer them:
- **44%** of households use a local provider, up from 38%; organised platforms *fell* from 15% to 13%. **[Real]** (LocalCircles)
- **76%** of AC owners avoid brand service. **[repo]** (LocalCircles)

### 1.2 What goes wrong, on both sides
**For the agency** (the person who can pay us):

| Pain | Proof |
|---|---|
| **Requests get lost.** Calls are missed while the owner is on a job; voice notes in Telugu, Hindi or English never become jobs | Owners estimate **~1 in 8** requests lost [Story, 18 interviews]. It is the repo's top-scored problem, **P2 intake chaos, 24/30** [repo] |
| **Technicians go in blind.** No model number, no history, often the wrong part | Repo problem **P1, 23/30** [repo]. **12 of 18** owners had a job delayed by a wrong or missing part last month [Story] |
| **Nothing is written down.** The machine's history lives in nobody's head | Repo problem **P3, 22/30** [repo]. **7 of 12** households in our survey keep no service record [Real] |
| **Repeat trips cost money.** If India matches the global 77% first-visit fix rate, about **3.45 crore repeat visits a year** happen, at **~₹159 each** in technician time and travel: **~₹550 Cr a year wasted** | Global rate and technician pay [Real]; the time per trip is an assumption; the total is [Model] (Market tab). No India first-visit rate exists, so our pilot measures it directly |

**For the household:**

| Pain | Proof |
|---|---|
| Nothing can be checked: price, part, or "job done" | Our own interviews (section 3.2) [Real] |
| **55%** got an inherently defective machine; **only 21%** of those who acted were made whole | LocalCircles, a self-selected sample [repo] |
| Chasing: **47%** of 110 public complaints we coded are about no-shows and follow-ups | Our case-competition research [Real] |
| In **7 of 12** repairs, the person deciding, approving, paying and opening the door were different people | Our household survey [Real] |
| National Consumer Helpline complaints went **12.36 → 13.16 → 20.49 lakh** (FY24–FY26), about **30% via WhatsApp** | [repo] |

**And the machines:** about **27 crore** fridges, washing machines and ACs sit in Indian homes, and not one of them has a shared record. ([Step 4.6](steps/04_market_and_problem.md)) The calculation: ~33.5 crore households × (fridge ~50% + washing machine ~20% + AC ~10–13%), from Data for India 2024 and the CLASP/BEE 2024 survey. **[Real]**

### 1.3 We have watched the problem happen
We did not only read about this. Our discovery produced first-hand artefacts. They are kept in the data room and not published, because they show private households. **[Real]**
- **A brand's WhatsApp bot failing on camera.** A 52-second screen recording shows a woman asking a brand to service her water purifier. The bot replies *"There is some API related issue please try again later."* She types *"What is API."* The bot loops, asking for a Job ID she does not have. Messages arrive in English and Hindi to a Telugu speaker. This is the decision-tree chatbot Circuit replaces.
- **An agency already doing the "machine record" on paper.** A purifier carries a taped card from a local Visakhapatnam agency, "Contact for Service", with four phone numbers. The household wrote the next service date over the brand's own sticker in marker. Our record is not an invention; people already make the paper version.
- **A household diary of repairs.** A homemaker keeps handwritten pages of what was serviced, when and for how much, because nobody else keeps that history.
- **A household already paying a human to be "Circuit".** One woman manages repairs at two properties in other cities through one carpenter she trusts. He brings in plumbers and electricians, she briefs them by video call, and she pays him a commission. *The job already exists and is already paid for; it just doesn't scale past one person's phone.*

### 1.4 Why this has not been solved
Each existing player holds one slice of a machine's life, and none of them serves the independent agency ([Step 5.7](steps/05_product_fit_competition.md), from the [repo competitive analysis](../Keepwell%20competitive%20analysis%20and%20workarounds.md)):
- **Urban Company** takes the customer onto its platform and keeps **28.3%** of the professional's earnings.
- **Servify** serves brands and warranty administrators.
- **Zoho FSM** and **Fieldproxy** are English-first, priced per seat, and need a dashboard.
- **Bernard (US)** ranks faults and parts but has no Indian languages and no machine record.

**Nobody builds the independent agency's brain, and nobody holds a record that follows the machine through its whole life.** The repo searched for one and found none. It records this honestly as "absence of evidence, not proof". ([Step 1.11](steps/01_vision_and_narrative.md))

---

## Part 2. Three people who had each seen one side of it
The problem has three sides: the household, the agency network, and the brand and warranty side. Each founder spent years on one of them. ([Step 2.1](steps/02_founders_and_backstory.md)) [Story]

| Founder | Role | What they had seen | Why it matters |
|---|---|---|---|
| **Prathyusha Kalluri** | CEO (40%) | Co-founded **FixNear** in 2016: a technician-booking service across 14 Tier 2 towns in Andhra Pradesh and Telangana, 1,200 partner technicians, ~₹11 Cr GMV at peak. **Sold it in 2022** (~₹4 Cr, mostly stock) to a regional aggregator that does not compete with Keepwell. Her non-compete ended in 2024 | She built a technician network in exactly these towns, and sold it. She saw from the inside why a marketplace that takes the customer away from the local agency doesn't work. **Keepwell is the opposite bet** |
| **Sri Charan Peri** | CTO (30%) | 7 years building speech and conversational AI in Indian languages; lead engineer on a voice product handling ~2M calls a month. **Built the Circuit prototype himself** | He has already shipped the product, and he lives the household side: *"Our machines cost my family ₹10,000 a month, never evenly."* |
| **Kavyanth Munagala** | COO (30%) | 8 years running a consumer-durables brand's network of **300+ authorised service partners** across South India, plus its warranty-claims desk | He knows the claims nobody can verify and the parts nobody can find. At Keepwell he **personally closed 8 of the last 10 agencies**, part-time |

**Why this combination matters to an investor.** The course's fundability matrix gives the founding team **45 of 90 points**, the largest share. The course case studies flag the opposite as weaknesses: "two MBAs with no coding" (LearnEasy), "single founder, no startup experience" (PowerMF). Keepwell has business, technology and operations each owned, plus a prior exit. FixNear also shows **the ability to pivot**: it began as a marketplace and moved to supplying agencies before its sale. That move is the insight Keepwell is built on.

**Commitment:** all three have worked **full-time on Keepwell since incorporation in May 2025**. They put in ₹15 lakh of their own money and took no salary for five months, then ₹50,000 a month each. Their equity vests over 4 years with a 1-year cliff, and all IP is assigned to the company. ([Step 2.3–2.5](steps/02_founders_and_backstory.md))

**Around them** ([Step 2.2](steps/02_founders_and_backstory.md)), each advisor fills a gap the repo names:
- a former head of after-sales for an appliance brand (doors to claims buyers)
- a certified refrigeration and electrical safety expert (signs off the safety rules)
- a technology and data-protection lawyer (DPDP, insurance distribution)
- a faculty mentor from IIIT Hyderabad's speech and language lab (Telugu and Tamil accuracy)
- an incubation mentor at CIE-IIITH (governance)

---

## Part 3. Listening before building
**January to April 2025.** Before writing a line of production code, the three founders spent four months listening. ([Step 6.2](steps/06_traction_and_validation.md))

### 3.1 What we did
- **A household survey:** 19 responses, 12 qualified. **[Real]**
- **7 household interviews**, recorded with consent. **[Real]**
- **18 interviews with agency owners** in Ramagundam–Peddapalli and Karimnagar. [Story]

### 3.2 What households told us, in their own words [Real]
The full quotes and their sources are in [`proof_pack/voice_of_customer.md`](proof_pack/voice_of_customer.md). Names are used with each person's verbal consent.

> "They are never going to say the price, they're going to just give you an estimation… three thousand to five thousand." — **Sai Kakki**, young professional, Hyderabad

> "Even a duplicate part will have 3 months of warranty and will work for 3 months at least. We won't know if the part is duplicate or original." — **Amma**, homemaker, Andhra Pradesh

> "If we visit a service station run by the company… whatever they say I will listen. If we visit a local man definitely doubts will arise." — **Rk Sir**, retired professional

> "I had a small door repair. When I asked him to come, he came and did it immediately. He took the amount genuinely. Since then, I have been able to trust him and approve his small works." — **Sarala Aunty**, who manages two properties in other cities through one tradesman

### 3.3 The insight
Put those quotes together and one pattern appears:

> **Nothing in a repair can be checked: not the price, not the part, not "job done". So people trust the *person*, not the work, and they grant more authority one good job at a time.**

This is why households stay with the local agency even though platforms are better funded. It decided our strategy: **we don't replace the trusted agency; we make it the smartest one in town.** ([Step 1.8, beat 4](steps/01_vision_and_narrative.md))

### 3.4 What agency owners told us [Story]

| Finding | Result | What it decided |
|---|---|---|
| Software | **0 of 18** use any field-service software; 16 of 18 run on phone and WhatsApp only | Circuit must live **inside WhatsApp**, with no new app and no dashboard on day one |
| Lost requests | About **1 in 8** | The first job is intake, not diagnosis |
| Size | Median **4 technicians**, **125 jobs a month** (range 60–260) | Became the model's input for jobs per agency |
| Repeat visits | **13 of 18:** mostly unpaid, so a cost | Agencies *want* fewer trips. This answers the repo's biggest risk ("fewer revisits cut the agency's fee") |
| Parts | 12 of 18 had a job delayed by a wrong part last month | "The part to carry" goes on the job card |
| How they'd pay | **14 of 18** prefer per completed job; ₹30–50 acceptable; 4 of 18 would accept ₹100 | We price per verified fix, and the pilot tests ₹40 against ₹100 |

A mentor we consulted independently gave the same rule **[Real]**: *"Percentages, these agencies will not play. They don't want to reveal that amount."* He suggested a flat fee per successful one-visit fix.

---

## Part 4. The idea that is bigger than the product
### 4.1 Every machine lives one life
Every machine a home owns goes through the same stages: **bought → used → fails → repaired → maintained → resold → recycled.** Today, every stage starts from zero, because nobody holds the machine's history ([Step 1.2](steps/01_vision_and_narrative.md)):
- the technician arrives blind
- the warranty can't be proven
- the service plan is sold to the wrong home
- the resale buyer can't trust the unit
- the recycler gets it too early

**Keepwell holds one living record per machine and puts a product at every stage.** What CIBIL is to a borrower and Carfax is to a used car, Keepwell is to a household machine: **the history every transaction checks first.**

**Vision:** *Every machine an Indian home owns is cared for across its whole life: repaired right, remembered always, and never wasted.*

### 4.2 The roadmap, and who pays at each stage
The order follows the team repo's build order ([repo revenue streams](../Keepwell%20problems,%20scenarios%20and%20revenue%20streams.md)):

| Release | Product | Who pays |
|---|---|---|
| **R1 (live)** | **Circuit**, the AI desk for repair agencies | Agencies, per verified fix |
| R2 (~12 months) | **Home Memory + Service Plans**: the free machine record, then plans sold for insurers | Insurers and plan providers, on commission |
| R3 (year 2) | **Claims triage** for warranty administrators and OEMs | Licence or per claim |
| R4 | **Parts marketplace**: a parts catalogue confirmed by technicians | Parts sellers, on referral |
| R5 | **Resale and recycling** with verified history | Buyers, producers, recyclers |
| Phase 3 | **Data services**: repeat-failure and parts-demand insight, consent-first | Brands, insurers |

### 4.3 Why we start with repair
Repair is where **the pain, the payer and the truth** meet ([Step 1.5](steps/01_vision_and_narrative.md)):
1. **The pain is highest.** A broken machine is when a household needs help and an agency earns money.
2. **The truth is created.** A repair is the only moment someone opens the machine and records what is really wrong: model, serial, fault, part fitted.
3. **The payer is there.** Agencies pay per job; households stay free, so the record fills without asking them for money.
4. **It brings distribution.** Every agency brings its households. The record grows as a by-product of work the agency already does.

That is why our pitch line is: **"Circuit is the wedge. The record is the business."**

---

## Part 5. Building Circuit
### 5.1 The prototype (June–September 2025)
The CTO built a working agent. Its architecture is documented in this repo ([feature specification](../Keepwell%20feature%20specification.md), [product architecture](../Keepwell%20product%20architecture%20and%20scenario%20IO.md)). **[Real]** ([Step 5.4](steps/05_product_fit_competition.md)) It has:
- FastAPI and an event store
- **20 allowlisted tools** (the AI can only do what is on the list)
- a **12-state job machine**
- a **14-condition readiness gate**: a job is not "ready" until every condition is met
- a learning step that **will not run until the technician's real finding is recorded**
- Telugu voice intake
- 25 automated tests

**A recorded demo run [Real]:** case **CASE-A44351** took a Telugu voice note to a repair-ready visit in **47 decisions over 10.9 minutes**. The 20-second walkthrough for the deck is in [`proof_pack/demo_walkthrough.md`](proof_pack/demo_walkthrough.md).

Two design-partner agencies used it free and shaped it. [Story]

### 5.2 What Circuit does, step by step
([Step 5.3](steps/05_product_fit_competition.md))

| # | Step | What happens | Who decides |
|---|---|---|---|
| 1 | **Understand** | The customer sends a voice note or photo on WhatsApp in Telugu, Hindi, Tamil, Kannada, Marathi or English. Circuit transcribes it and reads its understanding back | AI |
| 2 | **Check** | Reads model, serial and invoice from photos; checks warranty by the brand's rules; pulls the machine's past repairs (with consent) | Rules |
| 3 | **Safety** | Gas, refrigerant and high-voltage **hard-stops**, from a fixed rule list that sits *outside* the AI | Human only |
| 4 | **Root cause** | Ranks the likely faults and **the part to carry**: a private hint for the technician, never shown to the customer as a diagnosis | AI drafts |
| 5 | **Quote** | Built **from the agency's own rate card, by code**. The AI never invents a price. The owner approves | Owner |
| 6 | **Prepare** | A job card the technician reads in ten seconds | Owner |
| 7 | **Verify** | The technician confirms what was really wrong and what was fitted. That outcome teaches the system, updates the machine's record, **and is the only moment we charge** | Technician |

**The one principle behind all of it** (from the repo spec): ***"AI reads and drafts; rules decide anything with money, safety or legal effect."***

### 5.3 Into production (January 2026)
In January 2026 Circuit moved to **Gemini on Google's Vertex AI, hosted in Mumbai**, behind a model router that can switch vendors. WhatsApp Business went live, and one contract engineer joined for six months. [Story] Why Gemini: Google for Startups credits only cover Google's own models ([Step 3.3a](steps/03_ecosystem_map.md)), and the repo had already mapped every task to a Google service ([Google stack mapping](../Keepwell%20Google%20stack%20mapping.md)). The prototype was built on Claude; production runs on Gemini.

**Root-cause ranking went live in March 2026.** It is a technician-only hint. Verified outcomes are reviewed by the team every week before they enter **Mistri Gyan**, our shared fault library. [Story]

---

## Part 6. The first money, and why it was structured that way
### 6.1 What we raised
([Step 2.4](steps/02_founders_and_backstory.md)) [Story]

| Source | When | Amount | Instrument |
|---|---|---|---|
| Founders' own savings | May 2025 | ₹15 lakh (CEO ₹6L, CTO ₹4.5L, COO ₹4.5L) | Equity, split 40 / 30 / 30 |
| Two operator angels: an ex-founder from home services and an ex-head of service at a durables brand | Oct 2025 | ₹30 lakh | **iSAFE** at a ₹10 Cr post-money cap |
| Startup India Seed Fund Scheme, via CIE-IIITH | Sanctioned Mar 2026 | ₹20 lakh sanctioned: **₹10 lakh received**, ₹10 lakh due at 25 paying agencies | Grant (no equity given up) |
| **Total received** | | **₹55 lakh** | |

### 6.2 Why operator angels and an iSAFE
We had three options ([Step 2.6](steps/02_founders_and_backstory.md)):
- **Friends and family, priced equity.** ₹30 lakh would have meant 3–10 small cheques and putting a price on a company with no product.
- **Friends and family, iSAFE.** No price needed, but still many unsophisticated holders.
- **Operator angels, iSAFE (chosen).** ₹30 lakh from 2 people who know the industry. It sends a signal: *industry insiders checked us and put money in.* They also **introduced 3 of our 5 pilot agencies**.

**We thought about the next rounds before signing.** An iSAFE can cause five problems later. Each was designed out:

| Problem | How it was designed out |
|---|---|
| Conversion dilution lands on founders | A **post-money cap**, so the angels' 3.0% was fixed and known from day one |
| Preference overhang (₹49.9L of preference for ₹30L invested, if uncapped) | Preference **capped at the ₹30L invested** |
| Stacking several notes | One iSAFE round, one cap, closed |
| A low cap anchoring the seed price | The cap priced pre-product risk; the seed is priced on 9 months of paid traction. The 2.4x step-up over 13 months reads as "the price rose because the risk fell" |
| Rights creep | No board seat, no vetoes; information rights only |

**Was ₹10 Cr a reasonable cap?** No public dataset of Indian iSAFE caps exists, so we triangulated ([Step 2.7](steps/02_founders_and_backstory.md)) **[web]**:
- Indian pre-seed rounds raise ₹25 lakh to ₹2 Cr.
- iSAFE guides use ₹10 Cr and ₹30 Cr caps as worked examples.
- A recent comparable pre-seed, Unveilr AI, was priced at ₹16.7 Cr post-money.

₹10 Cr sits low-to-middle, which fits a company before its paid pilot.

### 6.3 Where every rupee went (May 2025 – Nov 2026) [Story]

| Use | ₹ lakh |
|---|---|
| Founder stipends: ₹50k/month each, Oct 2025 – Nov 2026 (unpaid before that) | 19.5 |
| One contract engineer, Jan–Jun 2026 | 6.0 |
| Cloud, AI and WhatsApp (the repo puts the pilot stack at ₹12–35k a month) | 3.0 |
| Pilot field costs: travel, onboarding kits, agency visits | 3.0 |
| Legal: incorporation, iSAFE filings, registered valuer, trademarks | 2.5 |
| **Total spent** | **34.0** |
| **Cash in the bank** | **21.0** |

**Eighteen months, a product in production, and 14 paying customers on ₹34 lakh** is a capital-efficiency signal. It was possible because the CTO built the product, AI costs little at this scale, and the founders took modest stipends. The flip side is key-person risk: one person built everything. The contract engineer in 2026 and the six-engineer team the seed funds answer it.

---

## Part 7. The test that went against us
**February to April 2026.** The repo's validation plan prescribed a paid pilot with 3–5 agencies at two prices. We ran it exactly. ([Step 6.3](steps/06_traction_and_validation.md)) [Story]

- **5 agencies, 22 technicians:** 3 in Ramagundam–Peddapalli, 2 in Karimnagar.
- **Arm A:** ₹40 per verified fix (3 agencies). **Arm B:** ₹100 per verified fix (2 agencies).
- **Paid from day one**, measured against each agency's own two-week baseline.

**The result that went against us.** In week 3, one of the two ₹100 agencies **halved its usage**. The owner said: *"It takes too much of a small job."* The ₹40 arm kept growing. **Since May 2026, everyone pays ₹40.**

**Why this matters to an investor:**
- **Our price is tested, not guessed.** At ₹100 the agency's value from Circuit was 0.81x the fee; at ₹40 it is ~2.0x (Part 9).
- **We show the failure.** The course lists "hiding weak metrics" as a pitch mistake. A pilot that can fail, and did, is evidence the pilot was real.

**The pricing that resulted** ([Step 7.3](steps/07_business_model_unit_economics.md)): **₹40 per verified fix**, an optional **Desk Pro** add-on at ₹399 a month, and **30 free days**. The alternatives were tested on paper and rejected:

| Option | Why rejected |
|---|---|
| ₹1,500/month + ₹40 (the original one-pager idea) | Value only 1.44x the fee; just 3 of 18 owners want a flat fee |
| ₹100 per verified fix | Failed the live test (0.81x) |
| Flat ₹999/month only | Contribution only ~₹186 a month at 125 jobs; the fee is disconnected from use |

₹40 is **about 7% of a ~₹600 job**. Urban Company keeps 28%, and it takes the customer.

---

## Part 8. Nine months in the field
**May to October 2026.** All agencies moved to ₹40, and the founders expanded from 5 to 14 paying agencies, adding Warangal. The COO closed 8 of the 10 new agencies **at about a quarter of his time**; 2 came because another owner referred them. ([Step 6.3–6.4](steps/06_traction_and_validation.md)) [Story]

### 8.1 The results

| Metric | Result | Type | What it means |
|---|---|---|---|
| **Paying agencies** | **14** (15 joined, 1 left) | Measured | ~1.4% monthly churn over ~70 agency-months. The model uses a conservative 3% |
| **Jobs through Circuit** | **~8,200** | Measured | Agencies live 3+ months route **~90%** of their jobs through it |
| **Requests captured as jobs** | **96%**; median **6 minutes** from voice note to job card | Measured | The "1 in 8 lost" problem is largely closed |
| **One-visit closure** (our primary metric) | **71% → 83%**, held 6 months over ~7,000 jobs | Measured | +12 points against the agencies' own baseline. Global benchmark: 77% |
| **Root-cause accuracy** (right fault in the top 3) | **62% (Mar) → 78% (Oct)**; passed our **75% gate in August** | Measured | See 8.2 |
| **Verified fixes** | **82%** of routed jobs | Measured | The learning event and the billing event |
| **Telugu speech errors** | Word error rate **21% → 14%**; abstains and asks **16%** of the time | Measured | Inside the repo's healthy 10–25% band |
| **Owner override** | **11%** of drafts edited | Measured | Owners review rather than rubber-stamp |
| **Safety** | **47** hard-stops triggered; **0 safety incidents in 9 months**; 0 failures on a 200-case red-team set | Measured | Zero tolerance held |
| **AI cost per job** | **~₹3.0** today | Measured | Budgeted at ₹4.5 for 2027 prices |
| **Machine records** | **~3,600**; **74%** of households consent | Measured | Home Memory fills itself from repairs |
| **Revenue** | **~₹59,000 a month**; ~₹2.8 lakh billed since Feb 2026; **97%** of invoices paid on time by UPI | Measured | Small, but real money from real customers |
| **Desk Pro** | **4 of 14** agencies (29%) | Measured | Used directly as a model input |
| **Owner sentiment** | **11 of 14** "very disappointed" without Circuit (79%) | Self-reported | The Sean Ellis product–market-fit test asks for ≥ 40% |

### 8.2 The learning curve: the most important chart in this story
Root-cause accuracy went **62% → 68% → 73% → 76% → 78%** between March and October 2026 (deck slide 7). Here is why that matters more than any other number:
- **March to May:** about half the gain came from adding manuals. Any competitor could do that.
- **Since June:** the gain comes **mostly from verified outcomes**, real repairs that technicians confirmed. **No competitor can do that without our agencies.**

This is the moat working in production, not on a slide.

### 8.3 Why only 14 agencies, and why that is deliberate
We chose to **prove price, accuracy and retention before paying for a sales team**. That is the course's Stage 2 discipline ("build early sales frameworks"). Even so, paying agencies grew **5 → 14 in six months, about 19% a month, with no salespeople**. The seed buys the sales team.

---

## Part 9. Does the agency actually win?
A product survives only if the customer gains more than they pay. We separated what we **measured from system logs** from what owners **told us**. ([Step 6.5](steps/06_traction_and_validation.md); model **Pilot** tab) [Story / Model]

**Per mature agency, per month** (125 jobs, 90% routed through Circuit):

| Value | How it is calculated | ₹ a month | Type |
|---|---|---|---|
| Recovered jobs | 125 × 8% recovered = 10 jobs × ₹240 agency margin | **2,400** | Measured |
| Repeat trips avoided | ~112 routed jobs × 12-point gain = ~13.5 trips × ₹159 | **2,150** | Measured |
| **Measured value** | | **4,550** | |
| Owner time saved | 0.75 hours a day × 26 days × ₹150 | 2,925 | Self-reported |
| **Total value** | | **~7,475** | |
| **Our fee** | ~92 verified fixes × ₹40 | **3,690** | |

**What this proves:**
- **Measured value alone is 1.23x our fee.** The agency gains even if we ignore everything owners say.
- **Counting owner time, it is about 2.0x**, a net gain of **~₹3,800 a month** after paying us.
- **At ₹100 it was 0.81x**, which is exactly why that arm failed.
- **Price headroom later:** total value (~₹7,500) is about 1.8x what an agency pays us in total (~₹4,200 with Desk Pro).

*A note on the two fee figures.* This value test uses today's 90% routing, so the fee is ₹3,690. The steady-state model in Part 11 assumes a mature agency routes all its jobs, so per-fix revenue is ₹4,100. Value rises with routing too: at full routing, measured value is ~₹4,785, still ~1.17x the fee.

**It also answers the biggest risk the repo named.** The risk was that agencies won't pay to make fewer trips, because a second trip earns a second fee. The answer has two parts:
- **13 of 18 owners** say repeat visits are mostly unpaid, so they are a cost.
- **Recovered jobs alone** (₹2,400, measured) cover about two-thirds of our fee.

---

## Part 10. Why nobody can catch up
### 10.1 What can be copied, and what cannot
We are honest about this ([Step 5.6](steps/05_product_fit_competition.md)). **A rival can copy in a quarter:**
- the WhatsApp intake
- prompting a language model
- search over manuals
- ranking faults and parts (Bernard and Fieldproxy already do)

**A rival cannot copy, because these only build up through agencies using us:**

| Asset | Why it compounds |
|---|---|
| **Verified repair outcomes** (fault → part → did it hold, by model, town and season): **~8,200 so far, and growing** | Each verified fix sharpens the next ranking. A newcomer starts at zero |
| **The machine record**, one history per appliance, with a verification ladder (self-reported → photo-confirmed → agency-signed → owner-approved) | Rivals each hold one slice: an OEM one brand, an administrator its own plans, a recycler only the end. We hold the whole life |
| **A parts catalogue confirmed by technicians** | Slow to build. The AI is never allowed to declare a part compatible on its own |
| **Telugu speech corrections** from real agency voice notes | Every correction is training data a rival lacks |
| **The legal right to the outcomes**: **all 14 agencies have signed** a licence that keeps de-identified outcomes with Keepwell | The asset survives even when an agency leaves (Part 15) |

**The flywheel:** more agencies → more verified outcomes → sharper root-cause ranking → more first-time fixes → agencies stay and pay → more machine records → plans, claims and parts revenue → more value per agency.

**Switching costs grow with use.** After a few months, an agency's rate card, its customers' histories and its technicians' habits all live in Circuit. Households, however, own their record and can take it anywhere. We never lock households in. That is a trust point, not a weakness.

### 10.2 The competitive map
On two axes (who it serves × what it holds), **Keepwell sits alone** in the corner of *serves the independent agency* × *holds the machine's lifetime record*. ([Step 5.7](steps/05_product_fit_competition.md); deck slide 11)

| Player | Size (repo) | Why it is not us |
|---|---|---|
| Urban Company | FY26 revenue ~₹1,555 Cr | Takes the customer; keeps 28.3%; metro-weighted |
| Servify | ~₹781 Cr revenue; $133–142M raised | Serves brands and administrators, not the agency |
| OneAssist, Onsitego, Zopper | OneAssist FY25 ~₹623 Cr | Hold only their own plans: **our future buyers and partners** |
| Zoho FSM, Fieldproxy | Zoho ₹1,000–1,800 per user a month | English-first, per seat, dashboard-based |
| Bernard (US), Aquant | Aquant $70M Series C | No Indian languages, no WhatsApp, no record |
| Indian voice-AI firms | Bolna $6.3M seed; Ringg $10M | Horizontal; no repair data |

**Proof the category can be big:** in the US, Avoca (AI call handling for home-service businesses) is valued at ~$1B, and ServiceTitan (software for trade businesses) makes $961M a year. **[repo]** India has no equivalent for its informal agencies.

### 10.3 Porter's Five Forces, in short
([Step 5.8](steps/05_product_fit_competition.md))
- **Rivalry:** low today, rising. We respond by moving first in Tier 2/3 and building outcome data early.
- **New entrants:** medium to high, because an AI wrapper is cheap. The moat is outcomes and records, not the model.
- **Buyer power:** medium. We charge only on a verified fix, so the value shows on every job.
- **Supplier power:** medium to high. Meta owns WhatsApp and Google prices the models. We keep a model router with a fallback vendor and budget at 2027 prices.
- **Substitutes:** high, because a phone and a notebook are free. We run *inside* WhatsApp, so the substitute is our channel.

---

## Part 11. The engine: how one agency becomes a business
### 11.1 One agency, steady state
([Step 7.4](steps/07_business_model_unit_economics.md); model **Unit Economics** tab) [Model on observed inputs]

| Line | Value | How |
|---|---|---|
| Jobs per month | 125 | Observed median of our agencies |
| Per-fix revenue | ₹4,100 | 125 × 82% verified × ₹40 |
| Desk Pro (average) | ₹116 | ₹399 × 29% uptake |
| **Revenue per agency (ARPA)** | **₹4,216 a month** | ~₹50,600 a year |
| AI + messaging | ₹713 | 125 × (₹4.5 AI at 2027 prices + ₹1.2 WhatsApp) |
| Support tooling | ₹100 | People are counted in team cost |
| **Contribution** | **₹3,403 (81%)** | |
| **Fully loaded cost to win an agency (CAC)** | **~₹17,900** | Field-sales salaries + acquisition cash + brand, ÷ new agencies |
| **Payback** | **6.3 months** (5.3 excluding the free month) | Gate ≤ 7; SMB software norm ≤ 12 |
| Lifetime | 33 months | At a conservative 3% monthly churn (observed ~1.4%) |
| **Lifetime value (Circuit only)** | **~₹1.13 lakh** | Excludes plans, parts and claims |
| **LTV : CAC** | **6.3x** | Healthy is above 3x |

**Why AI is ₹4.5 per job and not ₹3.0:** the repo's job mix costs ₹5.10 on Gemini Flash at 2027 prices and ₹1.22 on Flash-Lite with caching. Routing about half to each gives ~₹3.2. Escalations add ~₹0.3, and a 25% margin brings it to ₹4.5. We measure ~₹3.0 today. **We budget for tomorrow's prices, not today's.**

**Only 3.6 jobs a month** cover the cost to serve an agency. Any active agency is contribution-positive.

### 11.2 Growth comes from capacity, not hope
([Step 7.5](steps/07_business_model_unit_economics.md); model **Revenue Build** tab)

**New paying agencies = field-sales people × 80 a year + 10% referrals.**
- **The evidence for 80 a year:** the COO closed 8 agencies in 6 months at a quarter of his time. That is about the pace of a full-time rep at 6–7 a month.
- **Churn:** 3% a month in Y1–Y2, falling to 2% (Y3) and 1.5% (Y4–Y5) as switching costs build. Observed today: ~1.4%.

| | Y1 | Y2 | Y3 | Y4 | Y5 |
|---|---|---|---|---|---|
| Field-sales people | 1 (+ COO) | 3 | 10 | 18 | 24 |
| **Paying agencies at year end** (14 today) | **79** | **264** | **945** | **2,196** | **3,793** |
| Where | Telangana + AP | Telangana + AP | Four southern states | South + beyond | National Tier 2/3 |
| Share of all Tier 2/3 agencies | 0.4% | 1.2% | 4.2% | 9.8% | **16.9%** |
| Machine records (cumulative) | 29,000 | 1.37 lakh | 5.18 lakh | 15.1 lakh | **33.9 lakh** |

**A ceiling we set ourselves:** we never plan for more than 1 in 5 Tier 2/3 agencies paying us in five years. Even Urban Company, after ten years and an IPO, averages ~54,000 active professionals across all its categories. Year 5 sits at 16.9%, under the ceiling. ([Step 4.5](steps/04_market_and_problem.md))

### 11.3 Five-year P&L (₹ lakh)
([Step 7.6](steps/07_business_model_unit_economics.md); model **P&L and Cash** tab) [Model]

| | Y1 | Y2 | Y3 | Y4 | Y5 |
|---|---|---|---|---|---|
| Circuit | 20.1 | 76.5 | 271.6 | 730.6 | 1,425.9 |
| Service plans | — | 8.2 | 31.1 | 90.5 | 203.6 |
| Claims-triage licences | — | — | 40.0 | 80.0 | 160.0 |
| Parts | — | — | 21.8 | 56.5 | 107.8 |
| Resale & recycling | — | — | — | — | 27.2 |
| **Total revenue** | **20.1** | **84.7** | **364.4** | **957.6** | **1,924.5** |
| Gross margin | 77% | 80% | 84% | 84% | 85% |
| Headcount | 12 | 19 | 38 | 62 | 84 |
| **EBITDA** | **(178.2)** | **(215.2)** | **(276.7)** | **(151.3)** | **+264.6** |

- **Break-even in year 5**, at +₹2.6 Cr EBITDA (14% margin).
- **Revenue per agency rises 33%** by Y5, from ~₹50,600 to ~₹67,000 a year, as plans, parts and claims attach. That is *"the record is the business"* in numbers.
- **Cash comes in every fortnight** by UPI, 97% on time, so working capital stays at ~5% of revenue.

### 11.4 Why this plan and not a leaner one
([Step 7.7](steps/07_business_model_unit_economics.md))

| Plan | Agencies Y5 | Revenue Y5 | EBITDA Y5 | Outside cash needed after the seed |
|---|---|---|---|---|
| D. Lean: seed only, slow field sales | 2,701 | ₹13.9 Cr | ~₹0 | **~₹4.9 Cr** |
| **G. Funded growth (pitched):** a Series A spent on field sales from Y3 | **3,793** | **₹19.2 Cr** | **+₹2.6 Cr** | **~₹4.1 Cr** |

**Both plans need a Series A.** An earlier draft wrongly claimed the lean plan could break even without one; our red-team caught it (Part 16). Spending the Series A on field sales needs *less* outside cash than staying lean, because each new agency pays back in about six months.

### 11.5 What moves the numbers
([Step 7.8](steps/07_business_model_unit_economics.md); model **Sensitivity** tab)

| Driver moved ±20% | LTV:CAC becomes |
|---|---|
| Fee per verified fix | 4.8x / 7.8x |
| Verified share | 4.8x / 7.8x |
| Monthly churn | 7.9x / 5.3x |
| Cost to win an agency | 7.9x / 5.3x |
| Jobs per agency | 5.1x / 7.6x |
| AI cost per job | 6.5x / 6.1x |

**LTV:CAC stays at 4.8x or better in every ±20% case.** The real risks are commercial (price, verification, churn, CAC), not AI cost. That matches the repo's own conclusion: *"the binding risk is whether agencies pay, not token cost."*

---

## Part 12. How big this can get
### 12.1 How many agencies exist? Three sources that agree
No official count of repair agencies exists in India; the repo says so plainly. So we built the count three independent ways. ([Step 4.2–4.3](steps/04_market_and_problem.md); model **Market** tab)

**1. From technicians (supply):**
- ~2.5 lakh appliance and AC technicians (ICAP, a government source: ~2 lakh AC technicians; CEEW: 0.37M) **[Real]**
- × 60% working in agencies of 2–10
- ÷ 4 technicians per agency
- = **~37,500 agencies** (range 20,000–64,750)

**2. From repair jobs (demand):**
- 15 crore jobs × 44% done by local agencies = 6.6 crore
- ÷ 37,500 agencies ÷ 12 = **~147 jobs per agency a month**

**3. From money:** ₹9,000 Cr ÷ ₹600 average bill = 15 crore jobs, consistent with source 2.

**All three agree**, and the implied 147 jobs a month sits inside the repo's operating range (100–250). Our own agencies show 125, and **the model uses 125**. The market average is upside, not modelled.

### 12.2 From the whole market to our first towns

| Level | Agencies |
|---|---|
| **TAM:** all repair agencies in India | ~37,500 |
| **SAM:** in Tier 2/3 towns (60% non-metro; Blue Star ~70% of sales from non-metros, Redseer 68%) | ~22,500 |
| **Beachhead:** Telangana + Andhra Pradesh (6.2% population share) | ~1,400 |
| **Series A gate** | ~120 |

### 12.3 What Keepwell can earn (revenue, not GMV)
([Step 4.4](steps/04_market_and_problem.md))

| Pool | ₹ Cr a year |
|---|---|
| Circuit fees in our segment (SAM) | 158–396 |
| Service plans commission (appliances only; ~30% of device protection) | 310–620 |
| Parts referral | 95–252 |
| **Keepwell earnable pool** | **~1,005–2,370** (≈ $107–252M, India only) |

**The honest reading.** Circuit alone is a healthy niche: at our 20% ceiling it tops out near ₹23 Cr a year. **The record is what makes Keepwell venture-scale**, because every record Circuit creates opens the plans, parts, claims and resale pools. Claims triage, resale and data services are not even counted.

### 12.4 The path to ₹100 Cr revenue
([Step 9.4](steps/09_deal_valuation_exit.md)) [Model, illustrative beyond Y5]

| Line | How | ~Year 8 |
|---|---|---|
| Circuit, Tier 2/3 | 4,500 agencies × ~₹50,600 | ₹23 Cr |
| Circuit, Tier 1 (funded by the Series A) | ~15,000 metro agencies × 15% × ~₹60,000 | ₹13.5 Cr |
| Service plans at record scale | ~1 crore records × 3% × ₹2,000 × 15% | ₹9 Cr |
| Claims triage | 10 administrator licences + ₹25 a claim on ~20 lakh claims | ₹11 Cr |
| Parts, resale, data | Referral + take + data contracts | ~₹10 Cr |
| **Total** | | **~₹66 Cr** |

**₹100 Cr and beyond (years 9–10)** needs plan attach rising with records, price reviews as accuracy improves, and the next categories (vehicles, homes) on the same record. **We say so plainly rather than overclaim.**

---

## Part 13. What we need now, and why exactly that much
### 13.1 The method: the ask is an output, not a wish
We listed every requirement for the next 24 months, costed each line, and subtracted what we already have. The course's Class Activity 1 method ([Step 8.1](steps/08_funding_needs_and_ask.md); model **Funding Need** tab) [Model]:

| | ₹ lakh |
|---|---|
| Gross spend over 24 months (five lanes, 8.3 below) | 548.1 |
| + 10% contingency | 54.8 |
| **= Total cash needed** | **602.9** |
| − Revenue we will earn in those 24 months | (104.8) |
| − Cash in the bank | (21.0) |
| − SISFS second tranche (sanctioned; due at 25 agencies) | (10.0) |
| **= External funding gap** | **467.1** |
| **The ask (rounded up to the nearest ₹25 lakh)** | **₹475 lakh = ₹4.75 Cr** |
| **Minimum close** | **₹4.0 Cr** (21 months) |

**Not counted:** Google for Startups credits (~₹33 lakh of AI and cloud cost). They are approved only after the seed closes, and we don't plan survival on money that isn't approved. If they come through, they add ~1.7 months of runway.

### 13.2 Why 24 months
([Step 8.2](steps/08_funding_needs_and_ask.md))
- **Month ~3:** 25 paying agencies, which releases the second SISFS ₹10 lakh.
- **Month ~13:** 40,000 machine records.
- **Month ~15:** ~120 paying agencies.
- **Months 15–18:** the gates are held for three months.
- **Months 18–24:** the Series A is raised from strength (a 4–6-month process).

With 18 months, the gates would only *just* be met as the money ran out, forcing a raise under pressure. The extra six months cost the founders about 5 points of ownership.

| Runway | Ask | Pre-money | Investor stake | Founders after seed |
|---|---|---|---|---|
| 18 months | ₹3.5 Cr | ₹20 Cr | 14.9% | 72.9% |
| 21 months (minimum close) | ₹4.0 Cr | ₹20 Cr | 16.7% | 71.1% |
| **24 months (target)** | **₹4.75 Cr** | **₹19 Cr** | **20.0%** | **67.9%** |

### 13.3 What the money pays for, by purpose
([Step 8.3, 8.5](steps/08_funding_needs_and_ask.md))

| Lane (course M1) | ₹ Cr | Share | What it buys |
|---|---|---|---|
| **Discover product–market fit** | 2.08 | **38%** | AI lead, eval engineer, speech engineer; an agency-success team of 3–5; the price test in 3 new towns; Telugu, Hindi and Tamil test data with the IIIT-H lab; safety sign-off; household and administrator research |
| Build the team and company | 1.54 | 28% | Founder stipends (still below market), finance and HR, seed legal costs, lawyer, CA/CS, DPDP readiness |
| Build the product | 1.25 | 23% | Platform, WhatsApp and security engineers; the repo's "foundations" (consent store, cost ledger, eval harness, admin console) before customer data at scale |
| Marketing and sales | 0.56 | 10% | Field sales (1 → 3 people), ₹1,000 acquisition cash per agency, Telugu dailies and associations |
| Working capital | 0.04 | 1% | Asset-light until the parts business |

**Why PMF is the biggest lane:** the course's stage matrix marks product–market fit as the heaviest need at Stage 2, "Finding a Business Model". Every Series A gate is a PMF proof.

**What we deliberately don't spend on:** paid consumer ads, a consumer app, OEM integrations, a big office, or parts inventory.

### 13.4 What the ₹4.75 Cr buys: the Series A gates
([Step 6.7, 8.6](steps/08_funding_needs_and_ask.md))

| Gate | Target | Today |
|---|---|---|
| Paying agencies | ~120 by month 15 | 14 |
| Machine records | 40,000 by month 13 | ~3,600 |
| One-visit closure | +10 points at scale, held 3 months | +12 at 14 agencies |
| Monthly retention | ≥ 97% | ~98.6% |
| Value to the agency | ≥ 1.5x the fee; net gain ≥ ₹3,000 a month | ~2.0x; ~₹3,800 |
| CAC payback | ≤ 7 months | Modelled 6.3 |
| Languages and safety | ≤ 10-point gap; 0 false-accepts | Telugu only so far |
| Buyer signal for plans and claims | 1 warranty-administrator LOI | Discovery under way |

Each gate comes with a defined experiment, a success level and a kill-or-pivot rule. These are experiments **E1–E8** in [Step 6.6](steps/06_traction_and_validation.md), summarised in Part 17.

### 13.5 Sanity checks
- **Market norm:** ₹4.75 Cr (~$0.51M) sits at the lean end of Indian seed rounds ($0.3–2M). **[web]**
- **Not over-raising:** the headroom over the gap is ₹8 lakh.
- **After the seed:** a Series A of ~₹8–10 Cr around month 20. About ₹5 Cr funds the plan to break-even with a buffer; the rest opens Tier 1. We target a 2–3x step-up in price. ([Step 8.8](steps/08_funding_needs_and_ask.md))

---

## Part 14. The deal
### 14.1 Who we raise from: one lead seed VC
([Step 9.2](steps/09_deal_valuation_exit.md))
1. **A lead wants meaningful ownership.** A lead seed VC usually targets 15–20%. One lead takes the full 20.0%. Splitting it leaves the lead at ~11–12%, and good funds may decline to lead.
2. **A clean cap table for later rounds.** One new holder instead of four or five, so every future agreement is signed faster.
3. **The cheque is ordinary.** ~$0.5M is a normal solo seed cheque.
4. **Strategic value still comes in, through the ESOP pool.** An ex-warranty-administrator, a parts distributor and an ex-OEM service head join as advisors on ESOP grants, not as shareholders.
5. **The risk of a single investor**, answered: we ask the lead to reserve money for its Series A pro-rata (against signalling risk), and we run a process with several funds competing to lead.

**Target funds** (typical seed cheque ₹4–8 Cr, already active in this space per the repo): **Blume** (backed Zopper), **Elevation** (backed Zopper; led a vertical-AI seed in 2026), **Accel via Atoms** (backed Onsitego), **BEENEXT** (backed Servify).

### 14.2 The instrument: priced Seed CCPS
CCPS is the course's "most preferred by VC/PE" instrument and the Indian standard. A priced round also **converts the angels' iSAFE**, so the cap table is clean before the Series A. A second iSAFE (stacking notes), plain equity, convertible debt or a loan were each rejected, with reasons in [Step 9.3](steps/09_deal_valuation_exit.md).

**How the iSAFE converts:** the cap price is ₹64.67 against a seed price of ₹107.51. The angels get 46,392 shares (2.1% after the seed). Their preference stays capped at their ₹30 lakh.

### 14.3 The valuation: three course methods, one rule
([Step 9.4](steps/09_deal_valuation_exit.md); model **Valuation** tab) [Model]

At ~₹7 lakh annualised revenue, a revenue multiple gives a meaningless number. Following the course (M4: "pre-fundraising: Scorecard + Comparable"), we used:

| Method | Calculation | Post-money |
|---|---|---|
| **Comparable** | Average of Hisabkitab (AI accounting for small firms, seed, ₹20 Cr), Unveilr AI (₹16.7 Cr) and the Indian seed midpoint (~₹37.6 Cr, Kae Capital) **[web]** | **₹24.8 Cr** |
| **Scorecard** | Comparable × our fundability score ÷ benchmark = 24.8 × 78 ÷ 80 | **₹24.1 Cr** |
| **VC method** | Investor needs 35% a year for 6 years, so ₹4.75 Cr → ₹28.8 Cr. Year-6 revenue ₹30.8 Cr × 7x (Servify trades at ~7.2x) = **₹215.5 Cr exit**. After Series A and B dilution, the investor needs 19.6% today | **₹24.2 Cr** |

**What we pitch: ₹19 Cr pre-money, ₹23.75 Cr post, 20.0% to the lead at ₹107.51 a share.**
- **The rule:** never price above the VC-method price, so the investor's base case always clears their own 35% hurdle.
- **The investor's base case:** 20.0% becomes 13.6% after Series A and B. At a ₹215.5 Cr exit that is ₹29.3 Cr: **6.2x, ~35% a year.**

### 14.4 The investor's outcomes, honestly

| | Conservative | Base | Aggressive |
|---|---|---|---|
| Year-6 revenue | ₹22 Cr | ₹30.8 Cr | ₹40 Cr |
| Multiple | 5x | 7x | 9x |
| Exit value | ₹110 Cr | ₹215.5 Cr | ₹360 Cr |
| Investor return | 3.2x, ~21% a year | **6.2x, ~35% a year** | 10.3x, ~47% a year |

**Negotiation plan:** we anchor at ₹19 Cr (the investor's own maths). We expect an opening of ~₹15–16 Cr and walk away below ₹16 Cr pre. Instead of cutting the price, we can trade a 12% ESOP pool, or a small tranche released at the 120-agency gate.

### 14.5 The cap table
([Step 9.5](steps/09_deal_valuation_exit.md); model **Cap Table** tab)

| Holder | After seed | After Series A | After Series B |
|---|---|---|---|
| Prathyusha (CEO) | 27.2% | 21.7% | 18.5% |
| Sri Charan (CTO) | 20.4% | 16.3% | 13.9% |
| Kavyanth (COO) | 20.4% | 16.3% | 13.9% |
| Pre-seed angels | 2.1% | 1.7% | 1.4% |
| ESOP pool | 10.0% | 8.0% | 6.8% |
| **Lead seed VC** | **20.0%** | 16.0% | 13.6% |
| Series A / B | — | 20.0% | 17.0% / 15.0% |
| **Founders combined** | **67.9%** | **54.3%** | **46.2%** |

Founders keep a majority through the Series A. Fully diluted: 22,09,131 shares, with 4,41,826 seed CCPS issued.

### 14.6 The terms
([Step 9.6](steps/09_deal_valuation_exit.md); baseline: the course's MediQuick term sheet)
- **Accepted:**
  - 1x non-participating liquidation preference
  - broad-based weighted-average anti-dilution (never full ratchet)
  - a board of 2 founders + 1 lead director + 1 independent
  - 4-year founder vesting
  - standard information, pre-emption and tag-along rights
  - deal expenses capped at ₹8 lakh
- **We push for:**
  - vesting credit for time since May 2025
  - higher veto thresholds (₹25 lakh, not ₹10 lakh)
  - drag-along only after 6 years and above a price floor
  - no IPO valuation trigger
  - the lead reserving for its Series A pro-rata

### 14.7 Who buys Keepwell in the end
([Step 9.7](steps/09_deal_valuation_exit.md))
- **Warranty and protection platforms** (most likely): Servify, OneAssist, Onsitego, Zopper, Asurion. Precedents: Asurion bought Domestic & General (~£2.1bn, reported); Onsitego bought Qdigi. **[repo]**
- **Home-services platforms:** Urban Company (its IPO was 103.6x subscribed).
- **Recommerce and recycling:** Cashify, Attero, Recykal. Quikr bought Zefo (~₹200 Cr).
- **Global field-service software** entering India.

The timing is a **strategic sale in years 6–8**, once the record and claims lines are proven. Mid-size deals (Qdigi, Zefo) show buyers exist at our scale.

---

## Part 15. Trust, law and whose data it is
### 15.1 Trust is built into the product
([Step 10.3](steps/10_compliance_trust_dataroom.md))
- **Three decision tiers.** AI only (extraction, language); human approves (quotes, warranty labels); human only (safety releases, claim denials, anything involving minors). **The system never auto-denies a claim.**
- **Safety hard-stops** sit outside the AI: ~400 hazard terms in 6 languages, zero tolerance for misses. **47 triggered, 0 incidents in 9 months.**
- **Prices only from the agency's rate card.** The model never invents a price.
- **It abstains and asks when unsure** (16% of the time) and reads every voice note back.
- **Against automation bias,** the evidence is shown before the AI's suggestion, and "accept" is never pre-selected.

### 15.2 Whose data is it?
"The record is the business" only holds if we have the right to use the record. Rights are split by purpose ([Step 10.2E](steps/10_compliance_trust_dataroom.md)):

| Data | Our role | What happens if an agency leaves |
|---|---|---|
| Job details for that agency's customers | **Processor** for the agency | Returned or deleted; we keep no personal data |
| **De-identified repair outcomes** (model, fault, part, did it hold; no name, phone or address) | **Owner of the aggregate**, under a licence **signed by all 14 agencies** | **Stays in Mistri Gyan.** The compounding asset survives churn |
| Home Memory (the household's own record) | Fiduciary, with separate consent in 6 languages (74% consent so far) | **The household keeps it** and can share it with any agency |

### 15.3 The laws that matter, and where we stand
([Step 10.2](steps/10_compliance_trust_dataroom.md))
- **DPDP Act and Rules** (notified 14 Nov 2025; main duties from ~13 May 2027). Consent-first design is built, and production is hosted in Mumbai. We say *"hosted in Mumbai with security safeguards"*, never "DPDP-compliant".
- **IRDAI.** Extended warranties are insurer products. **We don't underwrite.** Plans are sold *for* licensed insurers through an IRDAI-registered route (corporate agency or a registered partner). Plan-selling stays switched off until that route exists.
- **CERT-In and the IT Act.** 6-hour incident reporting and 180-day logs, in Y1.
- **Consumer protection.** No dark patterns in quotes, and the owner approves every quote. Claim help is an *"evidence pack, not legal advice"*.
- **Company hygiene.** DPIIT recognition, IP assignment, an ESOP plan, a CA/CS on retainer, monthly books. Compliance costs ₹16 lakh in Y1 and ₹10 lakh in Y2, already inside the ask.

---

## Part 16. How we tried to break our own story
A story is only trustworthy if someone tried hard to break it. We did that twice. ([Step 12.6–12.7](steps/12_storyboard_redteam.md))

### 16.1 Red-team pass 1: an independent reviewer playing a seed VC who is also a founder
**Verdict: "second meeting, conditionally."** Its ten findings, and what we changed:
1. **The investor's return was below their hurdle.** We now never price above the VC-method price, and we added the path to ₹100 Cr.
2. **The moat's proof came from a feature that wasn't live.** Root-cause ranking has been live since March 2026, and the gate was passed in August.
3. **The timeline crammed angel money, pilot and seed into weeks.** The company history was set out realistically: incorporation May 2025, angels Oct 2025, paid pilot Feb 2026, seed now.
4. **Numbers disagreed between documents.** Everything is regenerated from one model.
5. **The "value ≥ 2x" gate failed.** Value is now split into measured and self-reported; the gate is ≥ 1.5x with a net gain ≥ ₹3,000.
6. **Weak metrics were softened.** Revenue and credits are shown as real figures.
7. **The plans market was inflated.** It is now appliances only, with the IRDAI route named.
8. **Data rights were missing.** Added; the licence is signed by all 14 agencies.
9. **Founder commitment was unclear.** All three are full-time since May 2025, and FixNear's buyer is not a competitor.
10. **The opening story's villain was our own customer.** Rewritten: "nobody is the villain".

### 16.2 Red-team pass 2: the full pitch
Its eleven findings, including:
- **The model used 145 jobs per agency while our agencies showed 125.** We now use the observed 125 everywhere. Revenue fell 14% and the price fell to ₹19 Cr. **We took the lower number because it is the true one.**
- **The claim that the lean plan breaks even without a Series A was false.** Corrected: both plans need one.
- **Payback of 6.3 months failed our own 6-month gate.** The gate was re-based to ≤ 7 months, openly. The SMB software norm is ≤ 12.
- **Desk Pro uptake was assumed at 25%.** Replaced with the observed 4 of 14 (29%).
- **₹30 lakh over 18 months was unexplained.** Every rupee is now itemised (Part 6.3).

### 16.3 We scored ourselves on the course's fundability matrix
([Step 11](steps/11_fundability_score.md)) **78 / 100**: Market 12/15, Product 23/30, Startup 35/45, X-factor 8/10.

That is just under the course's benchmark of 80. The two weakest cells are product uniqueness and product quality, which is why this story leans on the learning curve and the data moat rather than a feature list.

### 16.4 The model checks itself
The model has 530 formulas and 0 errors, and a **Checks** tab that tests itself:
- use of funds sums to 100%
- the ask ≥ the gap
- the cap table sums to 100% after each round
- seed shares × price = the investment
- the iSAFE converts at its cap
- year-5 agencies stay under 20% of SAM

All checks read OK. The one flag, "Series A needed after the runway", is expected and is the plan.

---

## Part 17. What could go wrong, and what we do then
An investor should see our risks before they find them. Each has a measure and a pre-agreed response ([Step 6.6](steps/06_traction_and_validation.md), plus the weak-points sections of every step).

| Risk | How we'll know | What we do |
|---|---|---|
| Agencies outside our network won't pay ₹40 (E1) | < 40% still paying after month 2 in 3 new towns | Switch to a hybrid or desk-fee price; the contingency funds a 2–3-month re-test |
| The one-visit gain fades at scale (E2) | Gain < +3 points over 25,000 jobs | Lead with intake (recovered jobs), which alone covers two-thirds of the fee |
| Hindi or Tamil accuracy lags (E4) | Gap > 10 points, or any safety false-accept | Pause rollout in that language |
| A field rep can't hit ~6–7 agencies a month (E5) | Below 6 a month; payback > 7 months | Reprice the plan or switch to the wholesaler channel |
| Households don't consent to Home Memory (E6) | < 65% consent | Redesign before R2 |
| No warranty administrator wants our claims evidence (E7) | No LOI after 2 discovery rounds | Plans first; delay claims triage |
| AI prices jump on 1 Jan 2027 (E8) | Cost per job > ₹10 | More Flash-Lite routing; it moves LTV:CAC by only ±0.4x |
| A big player copies the features | — | They can copy features, not 8,200+ verified outcomes and the records |
| Key-person risk (one person built the product) | — | The seed funds six engineers |

---

## Part 18. What is real and what is illustrative
This is a course pitch built on an assumed, internally consistent scenario. We are open about which parts are which (deck appendix A16).

| Real | Illustrative (ESFS course case) |
|---|---|
| The Circuit prototype and its recorded demo run (CASE-A44351) | Founder career histories (FixNear and prior roles) |
| The household survey (19 responses), 7 consented interviews, the named quotes, the photo and video evidence | The company timeline: incorporation, pre-seed, SISFS, cash |
| The team repo research: market, competitors, costs, law, product spec | The 18 agency interviews, the price test and the 14-agency results |
| Every public source cited (ICAP, CEEW, LocalCircles, Servify, BlueWeave, CLASP/BEE…) | The financial projections, the valuation and the terms |

**Consistency rules we held to:** every illustrative number sits inside the ranges the real research gives. Examples: jobs per agency inside the repo's 100–250 range, the abstain rate inside its 10–25% band, AI cost inside its ₹1.5–5.5 range. Every number traces to one model.

---

## Epilogue: What the money becomes
Go back to Ramagundam.

With Circuit, the son's Telugu voice note is answered in the agency's name within minutes. Circuit reads the AC's model from a photo and knows its history. It knows that on this model, in this town, in this heat, the fault is almost always a capacitor. The technician arrives with a ₹350 part in his pocket and fixes it in one visit. He confirms the fix, and that confirmation makes the next diagnosis better for every agency on the network. The machine's record now holds one more true fact. Nobody buys a ₹38,000 AC.

**Today that happens for 14 agencies.** The ₹4.75 Cr takes it to about 260 in two years and proves that it works far beyond our home towns. The Series A after that turns the record into plans, claims and parts, and makes Keepwell what we set out to build:

> ***Keepwell becomes the record everyone checks before touching a machine.***

---

## Appendix A. Proof index: every claim and where to check it

| Claim | Proof | Where |
|---|---|---|
| 15 crore repairs, ₹9,000 Cr market | Repo sources; ICICI Direct / UC DRHP; BlueWeave | [Step 4.3](steps/04_market_and_problem.md); [repo MRO report](../reports/Household%20appliance%20aftersales%20MRO%20ecosystem.md) |
| 37,500 agencies | Technicians (ICAP/CEEW) × 60% ÷ 4; cross-checked two ways | [Step 4.2–4.3](steps/04_market_and_problem.md); model **Market** tab |
| ₹550 Cr of wasted trips | 15 Cr × 23% × ₹159 | [Step 4.6](steps/04_market_and_problem.md); model **Market** tab |
| 27 crore machines | Households × ownership rates (Data for India, CLASP/BEE) | [Step 4.6](steps/04_market_and_problem.md) |
| 44% local, 76% avoid brand | LocalCircles | [Step 1.9](steps/01_vision_and_narrative.md) |
| "Nothing can be checked" insight | 7 consented household interviews; named quotes | [`voice_of_customer.md`](proof_pack/voice_of_customer.md); recordings in the data room |
| Brand bot failure, agency sticker, repair diary | Video and photos from discovery | Data room, folder 5 (not published: private households) |
| 18 agency interviews | Interview notes | [Step 6.2](steps/06_traction_and_validation.md); data room folder 5 |
| Prototype: 20 tools, 12 states, 14-condition gate, CASE-A44351 | The build and its demo run | [Step 5.4](steps/05_product_fit_competition.md); [`demo_walkthrough.md`](proof_pack/demo_walkthrough.md); [repo feature spec](../Keepwell%20feature%20specification.md) |
| Price test: ₹100 arm failed | Pilot results | [Step 6.3–6.4](steps/06_traction_and_validation.md); deck appendix A4 |
| 14 agencies, 8,200 jobs, 71% → 83%, 62% → 78% | Usage logs | [Step 6.4](steps/06_traction_and_validation.md); data room folder 5 |
| Value 1.23x measured, ~2.0x total | Value calculation | [Step 6.5](steps/06_traction_and_validation.md); model **Pilot** tab |
| ARPA ₹4,216, 81%, 6.3 months, 6.3x | Unit economics | [Step 7.4](steps/07_business_model_unit_economics.md); model **Unit Economics** tab |
| 3,793 agencies, ₹19.2 Cr, +₹2.6 Cr in Y5 | Capacity-driven plan | [Step 7.5–7.6](steps/07_business_model_unit_economics.md); model **Revenue Build**, **P&L and Cash** tabs |
| LTV:CAC ≥ 4.8x in every ±20% case | Sensitivity | [Step 7.8](steps/07_business_model_unit_economics.md); model **Sensitivity** tab |
| ₹4.75 Cr ask | Costed requirements − revenue − cash − grant | [Step 8.3–8.4](steps/08_funding_needs_and_ask.md); model **Funding Need** tab |
| ₹19 Cr pre-money | Three methods; never above the VC-method price | [Step 9.4](steps/09_deal_valuation_exit.md); model **Valuation** tab |
| Cap table and dilution | Share counts and conversion | [Step 9.5](steps/09_deal_valuation_exit.md); model **Cap Table** tab |
| iSAFE design and cap benchmark | Five protections; triangulated cap | [Step 2.6–2.7](steps/02_founders_and_backstory.md) |
| Competitors and their size | Repo competitive analysis | [Step 5.7](steps/05_product_fit_competition.md); [repo competitive analysis](../Keepwell%20competitive%20analysis%20and%20workarounds.md) |
| Google credits cover only Google models | Programme terms, checked 16 Nov 2026 | [Step 3.3a](steps/03_ecosystem_map.md) |
| Compliance obligations and costs | Law-by-law table | [Step 10.2, 10.4](steps/10_compliance_trust_dataroom.md) |
| Data rights survive churn | Signed agency licence | [Step 10.2E](steps/10_compliance_trust_dataroom.md) |
| Two red-team passes, 21 fixes | Findings logs | [Step 12.7](steps/12_storyboard_redteam.md) |
| 78/100 fundability | Course matrix | [Step 11](steps/11_fundability_score.md) |
| Investor answers in two sentences | Q&A bank (16 questions) | [`investor_qa.md`](proof_pack/investor_qa.md) |
| Everything a diligence team will ask for | Ten-folder data room | [`data_room_index.md`](proof_pack/data_room_index.md) |

## Appendix B. Every number on one page

| Topic | Number |
|---|---|
| Problem | 15 crore repairs a year · ₹550 Cr of wasted trips · 27 crore machines with no record |
| Market | 37,500 agencies → 22,500 Tier 2/3 → 1,400 beachhead · earnable pool ₹1,005–2,370 Cr a year |
| Company | Incorporated May 2025 · ₹55 lakh raised · ₹34 lakh spent · ₹21 lakh in the bank |
| Traction | 14 paying agencies · ~8,200 jobs · 71% → 83% one-visit · 96% captured · 62% → 78% accuracy · ~₹59k MRR · ~1.4% churn · 11 of 14 "very disappointed" |
| Value to an agency | Measured ₹4,550 + owner time ₹2,925 vs fee ₹3,690 |
| Unit economics | ARPA ₹4,216 · 81% contribution · CAC ₹17,900 · payback 6.3 months · LTV:CAC 6.3x |
| Plan, year 5 | 3,793 agencies · ₹19.2 Cr revenue · +₹2.6 Cr EBITDA · 33.9 lakh records |
| The ask | ₹4.75 Cr (minimum ₹4.0 Cr) · 24 months · one lead VC · priced CCPS |
| Use of funds | PMF 38% · team 28% · product 23% · sales 10% · working capital 1% (+10% contingency) |
| Valuation | ₹19 Cr pre · ₹23.75 Cr post · 20.0% · ₹107.51 a share · floor ₹16 Cr |
| Investor return | Base ~35% a year (6.2x); conservative ~21%; aggressive ~47% |
| Founders | 67.9% after seed · 54.3% after A · 46.2% after B |
| Next round | Series A ~₹8–10 Cr around month 20 |
| Self-score | 78 / 100 |
