# Keepwell — How the Story Is Told

*The whole seed pitch in one document: what we say, in what order, with which numbers, and why. It is built from the 13 locked step documents in [`steps/`](steps/), the financial model [`keepwell_model.xlsx`](keepwell_model.xlsx), and the deck in [`deck/`](deck/).*

---

## 1. The pitch in 60 seconds
> Every year, India does **15 crore appliance repairs**. Most are done by **37,500 small independent agencies** that run on a phone and a notebook. Calls get missed, technicians go in blind, and nothing about the machine is ever written down. That wastes about **₹550 Cr of trips** a year, and **27 crore machines** have no memory.
>
> **Keepwell** is the care layer for everything a home owns: one living record per machine, with a product at every stage of its life. We start with **Circuit**, an AI desk inside the agency's own WhatsApp. It understands a Telugu voice note, ranks the likely root cause and the part to carry, quotes from the agency's own rate card, and learns every time a technician verifies the fix.
>
> In a **four-week paid pilot with five agencies**:
> - one-visit closure went from **71% to 84%**
> - **96%** of requests became jobs
> - our root-cause accuracy rose **every week**
>
> We charge **₹40, only when the fix works**: about 7% of the job, against the 28% a platform keeps. We are raising **₹4.75 Cr** to take Circuit from 5 agencies to 260 and reach Series A from strength. Over time, Keepwell becomes **the record everyone checks before touching a machine.**

## 2. The one idea that runs through everything
***Every repair starts from zero. Keepwell remembers.***

Every slide serves this idea:
- **The problem:** no memory.
- **The insight:** trust is in people because nothing can be checked.
- **The product:** a prepared visit plus a record.
- **The moat:** verified outcomes compound.
- **The business:** the record unlocks plans, claims and parts.

## 3. The deal at a glance
| | |
|---|---|
| **Raising** | ₹4.75 Cr seed · priced CCPS · 24-month runway |
| **Valuation** | ₹20 Cr pre-money / ₹24.75 Cr post · 19.2% to seed investors · ₹113.33 per share |
| **Syndicate** | Lead seed VC ₹2.75–3 Cr + second fund ~₹1 Cr + 2–3 strategic angels ₹0.75–1 Cr |
| **Use of funds** | **Discover PMF 38%** · team and company 28% · build the product 23% · marketing and sales 10% · working capital 1% (+10% contingency). Grouped by what the money achieves; by cost type the same money is 40 / 28 / 21 / 10 / 1 |
| **Milestones (Series A gates)** | 40,000 machine records by month ~13 · ~120 paying agencies by month ~15 · one-visit +10 points held 3 months · ≥ 97% monthly retention · agency nets ≥ ₹3,000 a month · CAC payback ≤ 6 months · 1 warranty-administrator LOI |
| **Investor's return (base case)** | ~37% IRR, 6.7x, at a ₹243.5 Cr exit in year 6 |
| **Also unlocks** | Google for Startups AI credits (~₹34L of planned AI and cloud spend), not counted in the ask |

## 4. The story, slide by slide
**Timing:** ~11 minutes for 16 slides.
**Who speaks:**
- **CEO (Prathyusha):** opens and closes
- **CTO (Sri Charan):** the product and trust
- **COO (Kavyanth):** market, model and team

Each beat gives: *what's on screen → what we say → the line that must land → the transition.*

### Act 1: Why this matters (slides 1–4, ~2:45)
**Slide 1 · Title (CEO, 0:15)**
- **On screen:** *Keepwell, the care layer for everything a home owns.* Seed round ₹4.75 Cr.
- **Say:** "We're Keepwell. We're raising ₹4.75 crore to give every machine in an Indian home a memory, starting with the agencies who fix them."

**Slide 2 · The ₹350 part (CEO, 1:00)**
- **On screen:** *"A ₹350 part. A ₹38,000 new AC. Between them sits a repair system with no memory."*
- **Say:**
  1. Ramagundam, 23 May 2026, 46 °C. A retired miner's AC stops cooling at noon.
  2. Ramesh, the agency owner who serviced it, is up a ladder on another job. His phone rings 14 times, and the voice note is never written down.
  3. The son, 700 km away in Bengaluru, opens a shopping app: ₹38,000, three days.
  4. The fault was a ₹350 capacitor.
- **Land:** *"Nobody here is the villain. The system just has no memory."* Then Sri Charan's real line: *"Our machines cost my family ₹10,000 a month, never evenly."*
- **Transition:** "And this isn't one family. It's the whole system."

**Slide 3 · The problem (CEO, 0:50)**
- **On screen:** *"15 crore repairs a year. ₹550 Cr of wasted trips. 27 crore machines with no memory. And the 37,500 agencies that do the work run on a phone and a notebook."*
- **Say** the two sides:
  - **Agency:** ~1 in 8 requests lost; technicians go in blind; nothing is recorded.
  - **Household:** 55% got a defective machine, and only 21% of those who acted were made whole.
- **Caveat, said once:** "₹550 Cr assumes India matches the global 77% first-visit fix rate. No India figure exists, and our pilot measures it."
- **Transition:** "So why hasn't anyone fixed this? Because of one thing we learned in our interviews."

**Slide 4 · The insight (CEO, 0:40)**
- **On screen:** *"Nothing in a repair can be checked, so people trust the person, not the work."*
- **Say:** "The price is a guess, the part may be fake, and 'job done' proves nothing. So households trust a person, and they grant that person more authority one good job at a time. That's why 44% go local, up from 38%, and 76% avoid brand service."
- **Land:** *"We don't replace the trusted agency. We make it the smartest one in town."*

### Act 2: What we're building (slides 5–8, ~3:30)
**Slide 5 · The vision (CEO, 0:45)**
- **On screen:** *"The CIBIL of household machines."* The life of a machine, with one record running under it, and six products in release order.
- **Say:** "Every stage of a machine's life starts from zero: the repair, the warranty claim, the plan, the resale, the recycling. Keepwell holds one record per machine and puts a product at each stage. We start where the pain, the payer and the truth meet: the repair."

**Slide 6 · Circuit (CTO, 1:00)**
- **On screen:** *"Every repair visit arrives prepared."* The 7-step flow. Play the 20-second clip (`proof_pack/demo_walkthrough.md`).
- **Say:**
  1. A Telugu voice note comes in on the agency's own number.
  2. Circuit reads it back and checks the model and warranty.
  3. A safety hard-stop runs *outside* the AI.
  4. It ranks the likely root cause and the part to carry.
  5. It quotes from the agency's own rate card, and the owner approves.
  6. A job card goes to the technician.
  7. **The technician verifies the fix.**
- **Land:** *"We only earn when the technician verifies the fix, and that same moment teaches the system."*

**Slide 7 · Traction (CTO, 1:00)**
- **On screen:** *"Four weeks, five agencies, paid from day one."* ~410 jobs · 96% of requests became jobs · 71% → 84% one-visit · 5 of 5 first invoices paid · 5 of 5 active. Learning curve 62% → 74%.
- **Say:** "Root-cause accuracy rose every week: 62% to 74% on about 125 jobs in week four. We're honest about why: about half came from adding manuals and half from verified outcomes. And we tested price. At ₹100 a fix, one agency halved its usage. So we price at ₹40."
- **Land:** *"The learning loop is visible in four weeks."*

**Slide 8 · Why it compounds (CTO, 0:45)**
- **On screen:** *"Anyone can copy the AI. No one can copy verified repairs."*
- **Say:** "A rival can copy WhatsApp intake or an LLM in a quarter. Bernard and Fieldproxy already rank faults. What they can't copy is verified outcomes by model, town and season, a record that follows the machine its whole life, a technician-confirmed parts catalogue, and our Telugu corrections. Under our agency agreement, de-identified outcomes stay with us even if an agency leaves."

### Act 3: Why now, how big, and why us (slides 9–11, ~1:55)
**Slide 9 · Why now (COO, 0:30)**
- **Four tailwinds:**
  1. AI at ₹4.5 a job against a ₹40 fee.
  2. Only 1 in 10 homes has an AC, and India needs ~5x more AC technicians by 2037.
  3. Repair is opening up (Right to Repair portal, Repairability Index, the Kigali HFC freeze in 2028).
  4. DPDP 2027 rewards a consent-first record.

**Slide 10 · Market (COO, 0:45)**
- **On screen:** *"Circuit is the wedge. The record is the business."* The funnel: 37,500 → 22,500 → 1,400 → 120. The pools: ₹158–396 Cr; ₹1,005–2,370 Cr.
- **Say:** "No official agency count exists, so we built one from the government's technician estimate. It agrees with 15 crore jobs and the ₹9,000 crore repair market, and lands at ~147 jobs per agency a month, exactly what agencies told us. Circuit alone is a healthy niche. The platform is what makes it big."

**Slide 11 · Competition (COO, 0:40)**
- **On screen:** *"Everyone holds a slice. We hold the machine's whole life."*
- **Say:** "Urban Company takes the agency's customer and keeps 28%. Servify serves brands. Zoho and Fieldproxy are English-first and per seat. Bernard has no Indian languages and no record. We're alone in the corner that serves the independent agency *and* holds the machine's lifetime history."

### Act 4: The engine (slides 12–13, ~1:30)
**Slide 12 · Business model (COO, 0:50)**
- **On screen:** *"₹40, only when the fix works."* ARPA ₹4,856 · 81% contribution · 5.6-month payback · 7.3x LTV:CAC.
- **Say:** "Agencies pay ₹40 per verified fix, about 7% of a job. At full use, the agency gets roughly 1.8x what it pays and keeps about ₹3,850 a month. Then the record unlocks plans for insurers, claims triage, parts and resale."

**Slide 13 · The plan (COO, 0:40)**
- **On screen:** *"From 5 agencies to 3,800, and 39 lakh machine records."*
- **Say:** "Growth comes from field-sales capacity, not hope: 80 agencies per person a year. By year 5 that's 3,789 agencies, 17% of our segment, ₹21.7 crore revenue and +₹4.7 crore EBITDA. Even without a Series A, the lean plan breaks even in year 5. The path to ₹100 crore: Tier 1, plus plans and claims at record scale, gets to ~₹72 crore by year 8."

### Act 5: Who, trust, and the ask (slides 14–16, ~2:20)
**Slide 14 · Team and backers (COO, 0:50)**
- **On screen:** *"We've built this network before, and sold it."*
- **Say:**
  - **Prathyusha** built FixNear (1,200 technicians, 14 Tier 2 towns) and sold it.
  - **Sri Charan** built Circuit.
  - **Kavyanth** ran a 300+ partner service network and a warranty-claims desk.
  - All three are full-time.
  - Backed by operator angels, CIE-IIITH, the IIIT-H speech lab, and our own trade network. Google for Startups is unlocked by this round.

**Slide 15 · Trust (CTO, 0:30)**
- **On screen:** *"AI reads and drafts. Rules decide money, safety and law."*
- **Say:** "Three tiers: AI only, human approves, human only. Safety hard-stops sit outside the model. Prices only come from the rate card. Consent-first, hosted in Mumbai, ready ahead of DPDP 2027."

**Slide 16 · The ask (CEO, 1:00)**
- **On screen:** *"₹4.75 Cr to take Circuit from 5 agencies to 260, and reach Series A from strength."* ₹4.75 Cr · ₹20 Cr pre · CCPS · 24 months.
- **Say:** "The biggest share, 38%, goes to proving product–market fit: the price test at 30-plus agencies, accuracy in three languages, and the agency success team. Here's what it buys: 40,000 records by month 13, 120 paying agencies by month 15, one-visit closure up 10 points, 97% retention. Then a Series A from strength."
- **Close, and stop talking:** *"Keepwell becomes the record everyone checks before touching a machine."*

## 5. Why the story is ordered this way
| Order | Why |
|---|---|
| Human story → scale → insight (1–4) | The course's "Big Why" first. Emotion, then proof it's big, then the non-obvious reason it's unsolved |
| Vision → product (5–6) | Investors see the size of the ambition before the size of the wedge |
| **Traction before moat (7–8)** | The moat lands as *proven*, not promised |
| Why now → market → competition (9–11) | After traction, the market reads as earned |
| Model → plan (12–13) | The engine, then where it goes |
| Team → trust → ask (14–16) | "Who's in the cockpit", hygiene, then a clear ask that closes on the vision |

## 6. The numbers to know cold
| Topic | Number | Source |
|---|---|---|
| Repairs a year | 15 crore | repo; ₹9,000 Cr ÷ ₹600 |
| Wasted trips | ₹550 Cr / year | global 77% first-visit fix × ₹159 per trip |
| Machines with no record | 27 crore | ~33.5 Cr households × ownership (CLASP/BEE 2024) |
| Agencies | 37,500 → 22,500 Tier 2/3 → 1,400 TS+AP | ICAP/CEEW technicians, triangulated |
| Earnable pool | ₹1,005–2,370 Cr / year | fees + appliance plans + parts |
| Pilot | ~410 jobs · 96% · 71% → 84% · 62% → 74% · ~₹20k billed | Step 6 |
| Value to the agency | ~1.8x fee at full use; nets ~₹3,850 / month | Pilot tab |
| Unit economics | ₹4,856 ARPA · 81% · ₹17,900 CAC · 5.6 mo · 7.3x | Unit Economics tab |
| Plan Y5 | 3,789 agencies · ₹21.7 Cr revenue · +₹4.7 Cr EBITDA · 39 lakh records | P&L tab |
| Ask | ₹4.75 Cr · ₹20 Cr pre · 19.2% · 24 months | Funding Need, Valuation tabs |
| Investor return | ~37% IRR, 6.7x (base); ~23% / ~49% (conservative / aggressive) | Valuation tab |
| Founders after seed / A / B | 68.7% / 55.0% / 46.7% | Cap Table tab |

## 7. Q&A: the 15 questions we answer in two sentences
The full bank is in [`proof_pack/investor_qa.md`](proof_pack/investor_qa.md). The five most likely:
1. **"Why would an agency pay to make fewer trips?"** 13 of 18 owners say repeat visits are mostly unpaid. And recovered jobs plus owner time alone exceed our fee.
2. **"Five agencies isn't traction."** It's a paid design-partner pilot. The seed runs it at 30+ agencies and 3,000+ jobs with randomised prices.
3. **"What stops a big player copying you?"** Features, yes; verified outcomes and a lifetime record, no. And their models take the customer or serve the brand.
4. **"Which line takes you past ₹100 Cr?"** Tier 1 plus plans and claims at record scale gets to ~₹72 Cr by year 8. ₹100 Cr+ needs the next categories, and we don't overclaim.
5. **"Is ₹20 Cr justified?"** Your own VC-method maths gives ₹27.4 Cr post, and we ask ₹24.75 Cr. The base case returns ~37%.

**Never say:** "DPDP-compliant", "AI diagnosis", or any number that isn't in the model.

## 8. What's real and what's illustrative
This is an IIIT Hyderabad ESFS course pitch.

**Real:**
- the Circuit prototype and demo run, and The Ken Case Competition finalist status
- the household survey, the 7 consented interviews and their quotes
- the team repo's market, competitor, cost and compliance research
- all cited public sources

**Illustrative assumptions** (kept consistent with the repo and with each other):
- founder career histories
- incorporation, pre-seed and the SISFS application
- the 18 agency interviews and the 5-agency pilot results
- financial projections, valuation and terms

The deck states this in appendix A16.

## 9. Where everything lives
| What | Where |
|---|---|
| The plan (phases, steps, status) | [`pitch_bible.md`](pitch_bible.md) |
| Each step's reasoning and decisions | [`steps/00`–`13`](steps/) |
| Financial model (12 tabs) | [`keepwell_model.xlsx`](keepwell_model.xlsx) · rebuild with [`build_model.py`](build_model.py) |
| Deck: PowerPoint, PDF, animated web | [`deck/`](deck/) · rebuild with `deck/build_deck.py` |
| Proof pack | [`proof_pack/`](proof_pack/) |
| Investor review and fixes | [`steps/12_storyboard_redteam.md`](steps/12_storyboard_redteam.md) §12.7 |
