# Keepwell: the angel investor pitch (retailer-led appliance lifecycle, business-model stage)

Working document for the pitch, the deck and the Q&A. Built bottom-up from fundamentals (retailers, sales per day, repairs per appliance, technician capacity), not from a top-down "India appliance market is $X billion" line.

## 0. How to read this file (read before you use any number)

| Tag | Meaning |
|---|---|
| **[A]** | Assumption, our guesstimate. No evidence yet. Say so out loud. |
| **[E]** | External fact from general knowledge. Approximate. Verify and source before the deck goes out. |
| **[M]** | Measured by us. **None in this file.** |
| **[FILL]** | Founder must supply a real fact. |

Three honest cautions:

1. **Stage:** we are in the "finding the business model" stage. The deck must say so. Investors at this stage back the team, the insight, and the quality of the learning plan, not the revenue.
2. **Pilot and traction:** you asked me to assume. So section 9 and 10 describe the pilot as a *design with targets*, not as results. Do not show targets as achieved results. Replace them with actuals as they arrive.
3. **Conflict with your other Keepwell files:** `Keepwell overall story.md` says 14 agencies pay today and calls this "measured (M)". `KeepWell_Unresolved_Decisions.md` (item 5) says the V2/V3 decks claim no pilot. I did not reuse the 14-agency numbers here because I can't tell which is true. If they are real, put them in section 10 as **[M]**: they are your strongest evidence. If not, never show them.

All money is in ₹. L = lakh (₹1,00,000), Cr = crore (₹1,00,00,000). The model code used to compute the numbers is described in section 12 so you can re-run it with real data.

---

## 1. The pitch in one page

**The one-liner:** *Keepwell is the after-sale service arm for India's small-town appliance retailers: we install what they sell, repair it when the warranty ends, and later refurbish and recycle it, all through a trained local technician network.*

**The problem:** In a Tier 2/3 town, the appliance retailer sells the product and then loses the customer. Installation depends on a brand technician who may take days. After warranty, the customer has no one to trust except a local mechanic. Nobody keeps a record of the appliance. The retailer earns nothing after the sale, and the customer blames the retailer when anything goes wrong.

**The solution:** A managed service layer sitting inside the retailer's shop. The retailer sells; Keepwell installs (within 24 hours), repairs (fixed price, 90-day guarantee), sells annual service contracts (AMC), supplies genuine parts, trains the technicians, and later takes the old unit back for refurbishment or recycling. The retailer earns a commission on every job and keeps the customer.

**Why it can work:** The retailer owns the trust and the address book. The technician owns the skill. Nobody connects them. We connect them and run the quality layer.

**The numbers (base case, all [A]):**

| Metric | Value |
|---|---|
| Serviceable retailers in India (Tier 2/3) | about 23,000 |
| Service spend linked to those retailers | about ₹4,000 Cr a year |
| One retailer, one month, steady state | 25 installs + 14 repairs + 5 AMCs = about 41 jobs, ₹41k revenue, ₹7.8k contribution |
| One cluster (a hub town plus nearby towns) | 25 retailers, about 40 jobs a day, 14 technicians, breakeven at about 21 retailers |
| Retailer commission earned | about ₹3,500 a month, plus extra sales |
| Technician income | about ₹30k a month vs about ₹20k today **[A]** |

**The ask:** ₹2 Cr (about $240k) at ₹10 Cr pre-money (16.7%), 24 months of runway, to open three clusters and prove four numbers: retailer retention, jobs per technician per day, contribution per retailer, and AMC attach.

**What an angel gets:** A team with direct Tier 2/3 field experience, a wedge (installation) that gets us into every retailer, and a recurring revenue line (repair plus AMC) that compounds. The honest risk: margins are thin, so the business works only with density. We design for density from day one.

---

## 2. The problem

### 2.1 The problem, told from each side

**The retailer** (owner of a multi-brand appliance shop in a town of 5-15 lakh people, selling about 100 appliances a month):
- Sells an AC for ₹35,000. Brand installation takes 3-5 days. The customer calls the shop angrily. The shop gets blamed for a delay it does not control.
- After the sale, the customer vanishes. A repair, a service, a resale: all go to someone else.
- Takes old units in exchange but has no good way to resell them. They sit in a godown or go to a scrap dealer at a loss.
- Has no digital record of who bought what, when. Can't remind anyone about service.

**The household:**
- Post-warranty, calls a local mechanic found through word of mouth. Price is a guess, quality varies, there is no guarantee, and the same fault returns.
- Doesn't know if a part is genuine.
- Loses the invoice and warranty card, so can't prove the age of the appliance.
- Doesn't know when to service an AC or a washing machine, so it fails in peak season.

**The technician:**
- Income is irregular (a few jobs one day, none the next). **[A]**
- Often can't get the right part on the first visit, so a second visit follows.
- Little formal training. Learns on the job. No certificate, so no way to move up.
- Has no customer base of his or her own.

**The brand (OEM):**
- Service network in Tier 2/3 towns is thin. Installation delays hurt customer ratings. Out-of-warranty jobs are not worth its time.
- Wants happier customers and repeat purchases, but doesn't want to build a field force in 3,000 small towns.

### 2.2 How big is the pain? (estimates to validate in interviews)

| Pain | Estimate | Tag |
|---|---|---|
| Brand installation delay for ACs in smaller towns | 2-5 days typical in peak season | A |
| Share of repair jobs needing a second visit (part missing, wrong fault) | 25-35% | A |
| Share of repair jobs that are out of warranty | about 75% | A |
| Share of out-of-warranty repairs done by unorganised mechanics | well above 80% | A |
| Share of customers who lose the invoice by year 3 | a third or more | A |

**What to do with this:** In the deck, use one real quote from a retailer and one from a technician (**[FILL]** from the 60+ discovery interviews). Keep statistics to one slide. The goal is for the investor to *feel* the shopkeeper's problem.

### 2.3 The insight

Every other player starts at one end of the chain. The brand sells the product. The marketplace (Urban Company) serves the end customer in big cities. The mechanic fixes it. **Nobody owns the full lifecycle of the appliance in a small town, and the one person who knows the customer, the retailer, earns nothing after the sale.** If we give that retailer a reliable service arm, three things happen: customers stay, technicians get steady work, and we get a record of every appliance. That record is the foundation for repair, parts, refurb and recycle.

---

## 3. Why now

| Reason | Detail | Tag |
|---|---|---|
| **Installed base is growing fast and ageing** | AC, washing machine and refrigerator penetration in Tier 2/3 households has grown rapidly for 5+ years, so a large wave of units is leaving warranty now. AC penetration is still under 10%, so growth continues. | E, verify |
| **Tier 2/3 is where the volume growth is** | Appliance makers report that smaller towns drive most incremental volume. Retailers there are independent and have no service arm. | E, verify |
| **Right to Repair** | India's Department of Consumer Affairs launched a Right to Repair framework and portal in 2022; appliances are among the sectors covered. It increases pressure on brands to make parts and manuals available, and legitimises independent repair. | E, verify |
| **E-waste rules** | The E-Waste (Management) Rules, 2022 (effective April 2023) made producer EPR (extended producer responsibility) a formal, tradable obligation. Collection and refurbishing become a paid service. | E, verify |
| **WhatsApp and UPI are universal** | Over 500 million WhatsApp users in India and near-universal UPI acceptance in small shops. Job intake, quotes, photos and payments can run on tools everyone already uses. | E, verify |
| **Voice AI in Indian languages is now cheap** | Models like Gemini transcribe and understand Hindi, Telugu and other languages at a fraction of the cost of two years ago. A voice note from a technician becomes a structured job card. | E, verify |
| **Urban Company proved the model, but only in cities** | It showed that customers pay for trained, background-checked service at a fixed price. It has not built for small-town retailers. | E, verify city coverage |
| **Skill India and ESSC funding** | Government skilling programmes fund technician training, which lowers our supply cost. | E, verify |

**The one sentence:** *Millions of appliances in small towns are leaving warranty right now, the technology to run a trusted service layer is cheap for the first time, and regulation is starting to reward repair and recycling.*

---

## 4. The solution

### 4.1 What we are

A **managed service layer for the retailer**, delivered by a **trained local technician network**, run on a **light technology platform** (WhatsApp + voice + a job record).

We are *not* an app for customers to download. The customer interacts via the retailer, a QR sticker on the appliance, a phone call or WhatsApp.

### 4.2 The lifecycle, in the order we build it

| Stage | What we do | When | Why in this order |
|---|---|---|---|
| **1. Installation and demo** | Install within 24 hours of sale; photo checklist; sticker with QR on the unit | Pilot (month 0) | Retailer's biggest pain, daily volume, gets us a record of every new appliance |
| **2. Out-of-warranty repair and service** | Fixed-price quote, 90-day guarantee, genuine-part tag | Pilot | Highest recurring revenue; the retailer sends past customers to us |
| **3. AMC (annual service contract)** | AC and washing machine packages sold at the counter | Month 3 | Turns a one-off job into recurring revenue and predictable work |
| **4. Technician training and certification** | 2-week course, in-field mentoring, certificate | Month 1 onward | Our supply engine; also the quality system |
| **5. Parts procurement** | Pooled buying; supply to our technicians first, then independent mechanics | Month 9 onward | Needs repair volume first; improves first-visit fix rate and margin |
| **6. Refurb and second-hand** | Take trade-ins from retailers, refurbish at a hub, resell through the same retailers with a 6-month warranty | Month 18+ | Needs hub, grading, and stock capital; supply comes from stages 1-3 |
| **7. Recycle and e-waste** | Collect end-of-life units, sell to authorised recyclers; claim EPR payment | Month 24+ | Small margin, regulated; comes free once collection exists |

### 4.3 How a job works (end to end)

1. **Sale:** Retailer sells an AC. The shop assistant taps "book install" on WhatsApp, or the retailer's billing sticker has a QR.
2. **Intake:** Our system creates a job card (model, address, customer language, preferred slot, installation checklist).
3. **Dispatch:** A coordinator assigns the nearest certified technician; the customer gets an SMS/WhatsApp with the technician's photo and time slot.
4. **Visit:** Technician installs using the checklist, takes photos (outdoor unit mount, pipe insulation, drain, earthing), pays no cash to anyone; customer pays the install fee via UPI to the retailer or to Keepwell (depends on arrangement).
5. **Record:** The appliance gets a digital service book (model, serial number, date, installer). A QR sticker goes on the unit. The retailer's dashboard shows the job as complete.
6. **Later:** At month 11, the system sends a "free warranty check-up" message through the retailer; at month 13 the customer can buy AMC. When it breaks, the customer scans the QR or calls the retailer. The same technician (or a nearby one) gets the job with the full history and the likely part ready.

### 4.4 The four things that make it hard to copy

1. **The retailer relationship** (we are the retailer's service arm, not the customer's app).
2. **The technician certification and quality score** (a certified, rated, trained workforce in each cluster).
3. **The appliance record** (installation date, service history, parts used for every unit sold through our retailers).
4. **Cluster density** (routes, parts stock and technicians shared across 25+ retailers in one area; a late entrant has to rebuild it town by town).

---

## 5. Value proposition for every stakeholder

| Stakeholder | What they get | In numbers (base case) | What they give us |
|---|---|---|---|
| **Retailer** | A service arm with no investment; commission on every job; fewer complaints; extra sales from "installed in 24 hours" and "service guarantee"; a path to monetise trade-ins | About ₹3,500 a month commission (installs ₹800, repairs ₹1,300, AMC ₹1,350). Extra sales from better service: 3-4% more units, about ₹10-14k a month margin **[A]**. Total about ₹14-17k a month for a shop with ₹3 lakh/month gross margin | Customer referrals, shelf space for our QR/AMC, trade-in stock |
| **Household** | Installation in 24 hours; fixed-price quote before the visit; 90-day repair guarantee; genuine parts; digital service book; reminders; a trusted number to call | Repair callbacks down by about a third; AMC at about ₹1,800 a year for two AC services instead of unplanned ₹3-8k failures **[A]** | Payment, reviews, consent to keep the record |
| **Technician** | Steady jobs routed to them; parts on the first visit; training and certificate; transparent payout in 48 hours; a growing customer record | About 76 jobs a month, about ₹30k a month vs about ₹20k typical **[A]**, about 50% more | Quality, punctuality, photo proof, use of our tool |
| **Local repair agency / small service centre** | Can join as a partner: gets retailer-sourced jobs and parts; keeps its brand | More jobs per technician-day; parts at pooled prices | Capacity and local presence |
| **Brand (OEM)** | Faster installation and fewer low-star reviews in small towns; a certified local network without building one; data on field failures; refurb and recycle (EPR) partner | Installation SLA from days to under 24 hours; potential per-job fee for in-warranty installs (about ₹300-600 **[A]**) | Parts, manuals, training content, in-warranty job volume |
| **Parts distributor** | A consolidated buyer with predictable demand and prompt payment | Orders pooled into weekly runs | Credit terms, genuine-part guarantee |
| **Extended-warranty / plan sellers (e.g. Onsitego-type)** | A fulfilment partner in towns where they have none | Per-job fee | Volume |
| **Recyclers / EPR buyers** | Reliable collection of end-of-life units with records | Per-kg collection fee | Payment |
| **Investor** | A path from a wedge (installation) to compounding service revenue, with a record that sets up refurb, parts and recycle | See section 13 | Capital and introductions |

**One line per stakeholder, for the deck:**
- *Retailer:* "You sell it; we stand behind it, and you earn on every job."
- *Household:* "One trusted number for your appliance, from day one."
- *Technician:* "Steady work, the right part, and a certificate."
- *Brand:* "Your installation promise, kept in towns you can't reach."

---

## 6. Market size, built from fundamentals

**Method:** count the retailers, count what one retailer's customer base generates, multiply. Every line is **[A]** unless marked. Ranges are shown because the inputs are guesses.

### 6.1 How many retailers? (the funnel)

| Step | Number | Basis |
|---|---|---|
| Outlets in India selling major home appliances (non-chain, not mobile-only) | 1,20,000 (range 80,000-1,60,000) | A. Cross-check against dealer-association counts and brand dealer numbers. |
| In Tier 2/3 towns and beyond | 65% = 78,000 | A |
| "Serviceable": multi-brand, sells at least 60 major-appliance units a month, no service arm of its own | 30% of 78,000 = **23,400** | A |

**Serviceable retailer** is our customer. A shop selling 10 units a month does not generate enough jobs; a chain store has its own service.

### 6.2 What does one serviceable retailer's customer base generate?

Assumptions for a typical serviceable shop (a town of 5-15 lakh):

| Input | Value | Reasoning |
|---|---|---|
| Major appliance units sold per month | 100 | ACs, refrigerators, washing machines, TVs, geysers, RO. About 3-4 a day. |
| Share needing installation or demo | 55% | AC, washing machine, geyser, RO and wall-mounted TV need it; most refrigerators need only a demo. |
| Active installed base from this shop's past sales | 5,000 units | About 4-5 years of sales, less units that have been scrapped or moved. |
| Service or repair events per unit per year | 0.30 | Fridge about 0.15, washing machine 0.25, AC about 0.4 (service plus repair), TV 0.1 |
| Share out of warranty | 75% | Warranty is 1-2 years on most units; compressor and motor are longer but rarely claimed |
| Average out-of-warranty ticket | ₹1,150 | Labour about ₹450 + parts about ₹700 |
| Average installation fee (blended) | ₹650 | AC ₹1,200-1,800, washing machine ₹300-500, geyser ₹500-800, TV ₹400-800 |

**Annual service spend linked to one serviceable retailer (100% captured):**
- Installs: 100 × 55% × 12 = 660 installs × ₹650 = **₹4.3 L**
- Repair and service: 5,000 × 0.30 × 75% = 1,125 jobs × ₹1,150 = **₹12.9 L**
- **Total about ₹17 L a year per retailer**

### 6.3 TAM, SAM, SOM

| Layer | Calculation | Value |
|---|---|---|
| **TAM** (retailer-linked service spend, all serviceable retailers) | 23,400 × ₹17.2 L | **about ₹4,000 Cr a year** |
| **SAM** (towns we can reach with clusters in 5-6 years: about the 150 largest districts) | about 30% of TAM | **about ₹1,200 Cr a year** |
| **SOM, year 5** (30 clusters × 30 retailers = 900 retailers) | 900 retailers = 3.8% of serviceable | **about ₹75-85 Cr revenue**, about 2% of TAM |

The TAM excludes parts wholesale to independent technicians, refurb resale, AMC float, and e-waste, all of which add to our revenue per retailer but not to this pool.

**What to say:** "Our first 900 retailers are under 4% of the serviceable base. We don't need a big market share, we need density in the right towns."

### 6.4 The sanity checks an investor will run

- **Retailers per town:** a city of 12 lakh people, with about one appliance outlet per 4,000 people, has about 300 outlets; 30% serviceable = 90. A cluster of hub plus 4 satellite towns has 100-150 serviceable shops. We need 25 to break even, so **we need about 20-25% of serviceable shops in a cluster**. That is a high bar, and it is the first thing the pilot must prove.
- **Jobs per day:** 100 units a day per shop? No: 100 a *month*, about 3-4 a day. Installs per shop per day about 1.0 captured; repairs about 0.5 a day. For 25 shops, about 40 jobs a day.
- **Technicians:** a technician does 3.8 jobs a day, 25 days a month, 80% utilisation = 76 jobs. 40 jobs/day × 26 days = 1,040/month → **14 technicians**. A town of 12 lakh people probably has 100-150 independent appliance mechanics, so we need about 10% of them.

---

## 7. Business model

### 7.1 Revenue lines

| Line | Who pays | How we earn | Typical ticket | Margin (contribution) | Stage |
|---|---|---|---|---|---|
| **Installation** | Customer (AC and geyser mostly); brand for in-warranty installs | Fee per job (we are the service provider) | ₹650 average | about 17% (₹110) | Pilot |
| **Out-of-warranty repair** | Customer | Labour plus parts, fixed quote | ₹1,150 | about 17% (₹200) | Pilot |
| **AMC (annual service plan)** | Customer, sold by the retailer | Plan price, delivered visits cost us | ₹1,800 a year | about 25% (₹450) after the retailer's 15% | Month 3 |
| **Parts wholesale** | Independent technicians and agencies | Margin on pooled buying | ₹25k a month per technician | about 14% | Month 9 |
| **Refurb and resale** | Buyers via retailers | Spread over trade-in cost plus refurb cost | ₹7,500 resale | about ₹1,500 a unit | Month 18 |
| **Brand and EPR fees** | OEMs and producers | Per-job (in-warranty install) and per-kg collection | ₹300-600 per job | **[A]** | Month 18+ |
| **Technician training** | Technician (small fee), skilling funds, brands | Course fees or funded seats | ₹3,000-5,000 a seat | break-even; it is a supply cost | Month 1 |

We are the **principal** for service work (we employ or contract the technician and carry the customer promise), so revenue is shown **gross**. This inflates revenue relative to a marketplace that shows only commission, so investors will compare gross margin and contribution, not just revenue.

### 7.2 How the retailer is paid

- **Installation:** 5% of the fee as commission. **[A]**
- **Repair:** 8% of the ticket for referring the customer. **[A]**
- **AMC:** 15% of the plan price. **[A]**
- **Refurb:** share of the resale spread (to be set in pilot).
- No joining fee. We want zero friction. A joining fee can come once the service is proven.

### 7.3 Why the model is built this way

- **Installation is the wedge, not the profit.** It is frequent, predictable and visible to the retailer. It creates the appliance record.
- **Repair and AMC are the engine.** They are recurring and higher margin.
- **Parts, refurb and recycle are the layers.** They need volume first, but once there, they raise revenue per retailer and make the business hard to copy.

---

## 8. Unit economics

All **[A]**. These are the numbers the pilot must replace. Base case unless stated.

### 8.1 One job

| | Installation | Repair (out of warranty) | AMC (one plan) |
|---|---|---|---|
| Revenue | ₹650 | ₹1,150 | ₹1,800 |
| Technician payout | ₹470 (72%) | labour ₹300 | 2 visits × ₹300 = ₹600 |
| Parts cost | n/a (consumables ₹30) | ₹490 (parts sold at ₹700) | ₹0 (parts extra) |
| Retailer commission | ₹32 (5%) | ₹92 (8%) | ₹270 (15%) |
| Rework / warranty cost | in payout | ₹35 (3%) | ₹100 |
| Payment fee, AI, messaging | ₹8 | ₹32 | ₹30 |
| Other direct (travel, tools) | ₹0 (in payout) | ₹0 | ₹300 |
| **Contribution** | **₹110 (17%)** | **₹200 (17%)** | **₹450 (25%)** |

### 8.2 One retailer, one month (steady state, base case)

| Item | Volume | Revenue | Contribution |
|---|---|---|---|
| Installs | 24.8 (100 units × 55% × 45% capture) | ₹16,100 | ₹2,740 |
| Repairs | 14.1 (5,000 × 0.30 ÷ 12 × 75% × 15% capture) | ₹16,200 | ₹2,820 |
| AMC sold | 5 | ₹9,000 | ₹2,250 |
| **Total** | about 41 jobs | **₹41,300** | **₹7,800 (19%)** |

The capture rates are the biggest swing factors: we win 45% of this retailer's installs (brands keep some) and 15% of the repairs on its installed base (the rest still go to mechanics).

### 8.3 Cost to acquire a retailer (CAC)

| Item | ₹ |
|---|---|
| Field sales time (2 visits, 1 demo) | 6,000 |
| Onboarding and staff training | 4,000 |
| Signage, QR standee, first stickers | 3,000 |
| Launch offer (free first installs) | 5,000 |
| **CAC** | **₹18,000** |

- **Payback on contribution:** 18,000 ÷ 7,800 = about 2.3 months at steady state. Allowing for the ramp (the retailer gives us only about 35% of steady-state volume at the start and reaches 100% after about 12 months), real payback is **about 5-6 months from go-live**.
- **Lifetime contribution:** at 20% yearly retailer churn **[A]**, expected life is 5 years; over three years the retailer produces about ₹2.8 L of contribution, so **LTV:CAC is about 15x** before cluster overheads.

### 8.4 The honest version: after cluster overheads

LTV:CAC looks excellent, but the cluster has fixed costs that the retailer contribution must cover:

| Cluster fixed cost per month | ₹ |
|---|---|
| Cluster manager | 45,000 |
| Dispatch and customer-care executive | 25,000 |
| Training lead (part time) | 30,000 |
| Office, vehicle, phone | 25,000 |
| Retailer onboarding and field marketing | 40,000 |
| **Total** | **₹1,65,000** |

| Retailers in cluster | Contribution (₹7,800 each) | Cluster EBITDA a month |
|---|---|---|
| 15 | ₹1.17 L | **-₹0.48 L** |
| 21 | ₹1.65 L | **about 0 (breakeven)** |
| 25 | ₹1.95 L | **+₹0.30 L** |
| 35 | ₹2.73 L | **+₹1.08 L** |
| 40 | ₹3.12 L | **+₹1.47 L** |

**This is the key finding for the pitch:** the business is a *density* business. Below about 21 retailers, a cluster loses money. Above it, each extra retailer adds about ₹7,800 a month with almost no new overhead. This is why the money goes to *three deep clusters*, not twenty shallow towns.

Layers that raise this: parts wholesale (+₹1.4 L a month per cluster at maturity), refurb (+₹1.3 L at half penetration), better AMC attach.

### 8.5 One technician

| | Value |
|---|---|
| Jobs a day | 3.8 (installs 3-4; repairs 3-4 with travel) |
| Working days | 25 |
| Utilisation | 80% |
| Jobs a month | 76 |
| Average payout per job | about ₹400 (installs ₹470, repairs ₹300) |
| **Monthly income** | **about ₹30,000** |
| Typical independent mechanic today | about ₹18,000-22,000 **[A]** |

If the technician is paid ₹30k and does the job in 3.8 jobs a day, then the technician supply is attractive. The risk is the opposite: utilisation lower than 80% in the off-season (AC jobs are seasonal), which is why we pair AC with washing machine, refrigerator, geyser and RO.

### 8.6 What matters most (sensitivity, per retailer contribution a month)

| Scenario | Installs capture | Repair capture | Ticket | Contribution per retailer | Cluster breakeven retailers |
|---|---|---|---|---|---|
| **Low** | 30% | 10% | ₹950 | about ₹3,300 | about 50 |
| **Base** | 45% | 15% | ₹1,150 | **about ₹7,800** | **about 21** |
| **High** | 55% | 20% | ₹1,300 | about ₹15,000 | about 11 |

Under the **low case** the model needs about 50 retailers per cluster to break even, which is probably not reachable. That is what a failed pilot looks like, and why we set the kill thresholds in section 10.

---

## 9. The team: the best three people to build this

### 9.1 The three roles

This business needs three different muscles: win retailers, run the field, build the system. One person cannot do all three.

| Role | Profile of the ideal person | Why this role | Must have |
|---|---|---|---|
| **1. CEO: retailer channel and business** | 8-12 years in consumer-durables distribution, retail sales or brand channel (e.g. a regional sales head at an appliance brand or a distributor). Has sold to hundreds of small retailers. Credible in a dealer's office. | The retailer decides whether we exist. Our first 25 retailers per cluster come from relationships and trust. | Dealer network, negotiation, P&L ownership, fundraising |
| **2. COO: field operations and technician network** | Ran a service-partner network, after-sales or claims for an appliance brand, or a field-service marketplace in Tier 2/3 towns. Has recruited, trained and managed 100+ technicians. | Technician quality, utilisation and parts are the business. A bad job damages the retailer's name. | Technician hiring and training, dispatch, parts, quality system |
| **3. CTO: product and AI** | Built WhatsApp/voice systems for Indian languages and a dispatch or marketplace product. Can ship a working system in weeks and keep cost per job low. | The platform is what lets 3 people run 25 retailers and 14 technicians per cluster, then copy it across clusters. | WhatsApp Business API, voice/AI in Hindi and Telugu, job and inventory systems, data |

### 9.2 What your team looks like today

From your other Keepwell files (confirmed real by the team there), the three founders map to these roles:

| Role | Who | Evidence in your files | Fit to this plan |
|---|---|---|---|
| CEO | Prathyusha Kalluri | Built FixNear, 1,200 technicians in 14 Tier 2 towns; sold 2022; ran repair at the buyer | Strong on technician supply and Tier 2 operations. **Gap: retailer-channel selling** |
| CTO | Sri Charan Peri | 7 years of Indian-language voice AI, about 2M calls a month | Strong match |
| COO | Kavyanth Munagala | 8 years of brand after-sales; ran a 300+ service-partner network and claims desk | Strong on partners and parts; and the one who closed the agencies |

**The gap an investor will see:** no founder has sold to hundreds of small *retailers*. Close it with (a) the first **cluster manager** hired from consumer-durables retail or distribution, (b) a named **advisor** who is a past regional sales head or dealer-association leader, and (c) the pilot's own retailer references.

### 9.3 First hires and advisors (what the ₹2 Cr buys)

| Role | When | Why |
|---|---|---|
| Cluster manager (per cluster) | Month 1, 7, 13 | Owns retailers and technicians in the cluster |
| Dispatch and care executive (per cluster) | With the cluster manager | Daily scheduling and customer calls |
| Training lead | Month 2 | Runs certification; reports to the COO |
| Full-stack engineer | Month 3 | Dashboards, dispatch, payouts |
| Advisor: ex-regional head at an appliance brand | Now | OEM introductions |
| Advisor: dealer association leader | Now | Retailer access |
| Advisor: e-waste/EPR expert | Month 12 | Prepares the recycle layer |

---

## 10. What we did up to product development, and what we do in the pilot

> **Reminder:** this section is a *plan with targets*. Replace each target with the real result as it comes. Do not present targets as results. Items I marked **[FILL]** need your real count.

### 10.1 Before building (discovery) **[FILL with actuals]**

| Step | What we did (or will do before the pitch) | Target |
|---|---|---|
| Retailer interviews | Spoke with owners of multi-brand appliance shops in 3 towns | 40+ |
| Technician interviews | Independent mechanics and agency owners | 30+ |
| Household interviews | Customers who had a repair or installation in the last 12 months | 60+ |
| Ride-alongs | Days spent on installations and repairs with technicians | 15 days |
| Brand conversations | After-sales and regional sales heads at appliance brands | 5 |
| Pricing tests | Showed 3 commission and fee options to 20 retailers | 20 |
| Written commitments (LOIs) | Retailers who agreed in writing to pilot | 10+ |

**What the investor must hear:** "We did not start by building an app. We spent N weeks in shops and on rooftops. Here is what we learned, in the retailer's words."

### 10.2 Product built (MVP) **[FILL with what is real]**

Kept deliberately small. Everything runs on WhatsApp and a simple dashboard.

| Component | What it does | Status |
|---|---|---|
| Job intake on WhatsApp | Retailer or customer sends a message, voice note or photo; creates a job card in Hindi/Telugu | [FILL] |
| Retailer dashboard | Shows jobs, commissions, customers; one-tap "book install" | [FILL] |
| Technician app (light) | Job list, checklist, photo upload, voice close-out, payout view | [FILL] |
| Rate card and quote | Price comes from a fixed rate card by code, never from the AI | [FILL] |
| Appliance record and QR | Service book per unit; QR sticker | [FILL] |
| Parts catalogue | Most common parts for AC, washing machine, refrigerator; price list | [FILL] |
| Training module | 2-week curriculum and quiz | [FILL] |

### 10.3 The pilot: design and targets

**Scope:** One Tier 2 hub plus nearby towns **[FILL: city]**; 90 days; AC, washing machine, refrigerator (geyser and RO added if demand appears); installation, out-of-warranty repair, AMC.

**Size:** 8 retailers, 8 technicians (from the cluster's pool, certified in week 1), 1 cluster manager.

**What we do each week:**

| Weeks | Activity |
|---|---|
| 1-2 | Certify 8 technicians; stickers and QR standees in 8 shops; load rate card; test the WhatsApp flow on 20 internal jobs |
| 3-6 | Live installs for all 8 retailers; measure time-to-install, photo checklist compliance, customer rating |
| 5-10 | Start repair referrals from retailers' past customers; log first-visit fix rate and ticket size |
| 8-12 | Offer AMC at the counter; log attach rate; test retailer commission levels |
| 12 | Close-out interviews with 8 retailers, 8 technicians, 30 customers; decide go/no-go for cluster 1 scale-up |

**Pilot scorecard: targets and kill thresholds** (these are the hypotheses; the investor should see them on a slide)

| # | Hypothesis | Target | Kill if |
|---|---|---|---|
| 1 | Retailers will route their installs to us | 40%+ of each pilot retailer's installs | below 20% after 6 weeks |
| 2 | We can install within 24 hours | 85%+ within 24h | below 60% |
| 3 | Past customers will call us for repairs | 10-15 repair jobs per retailer per month by month 3 | below 5 |
| 4 | First-visit fix rate is high enough | 80%+ | below 65% |
| 5 | Customers rate the service well | 4.5+/5; 90-day callbacks under 8% | callbacks above 15% |
| 6 | AMC sells at the counter | 4-5 per retailer per month | below 1 |
| 7 | Technicians are productive and stay | 3.5+ jobs/day; income about ₹30k; none leave in 90 days | under 2.5 jobs/day |
| 8 | Contribution per retailer works | ₹6,000+ a month by month 3, trending to ₹7,800 | under ₹3,000 |
| 9 | Retailers keep going | 7 of 8 still active at month 3; would pay or pay commission-free | 4 or fewer |

**Why these kill thresholds matter:** if #1, #3 and #8 are all missed, the low case in section 8.6 applies and the cluster needs about 50 retailers to break even, which means the model is wrong. We would change it (e.g. charge retailers a fee, or drop installation as a wedge) instead of scaling.

---

## 11. Traction

Be precise. At this stage, traction is **learning and commitment**, not revenue.

### 11.1 What to show today **[FILL with real numbers]**

| Evidence | Where we should be at pitch time | Tag |
|---|---|---|
| Interviews completed | 130+ across retailers, technicians, households | FILL |
| Retailer LOIs | 10+ written commitments to pilot | FILL |
| Pilot retailers live | 8 | FILL |
| Installations done | 150+ in 90 days (8 retailers × about 6.2 a week) | FILL |
| Repairs done | 60+ | FILL |
| AMC sold | 20+ | FILL |
| Technicians certified | 8-12 | FILL |
| Customer rating | 4.5+/5 | FILL |
| Retailer quotes | 3 verbatim, with names and shop photos (with permission) | FILL |

### 11.2 If you have *none* of this yet

Do not pad. Say: "We are at interview stage. We have N retailer conversations and M LOIs. The seed funds the pilot." Investors respect honesty; they punish inflated traction when they check references.

### 11.3 If the 14 agencies from the other file are real

They are valuable evidence of *willingness to pay* on the supply side (agencies paid ₹40 a verified fix; about 100 fixes a month each). Frame them as: "Our first product, a job desk for repair agencies, already has paying users. Those agencies are the technician and service-partner supply for the retailer-led model." Mark them **[M]** only with job logs and payment records behind them.

---

## 12. Financial plan and how the numbers were built

### 12.1 The model (so you can re-run it)

Monthly simulation, 24 months, three clusters opening in months 1, 7 and 13.

| Mechanic | Rule |
|---|---|
| Retailers per cluster | 2 at opening, linear to 25 by month 9 |
| Volume ramp | Each retailer starts at 35% of steady-state volume and reaches 100% by month 12 |
| Per-retailer revenue and contribution | From section 8.2 (low/base/high) |
| Cluster fixed costs | ₹90k in the opening month, ₹1.65 L a month after |
| Cluster setup | ₹3 L one-off (tools, signage, demo kits, vehicle deposit) |
| Working capital | ₹3 L per cluster (parts stock, tool kits), spread over 6 months |
| Parts wholesale layer | From cluster month 9: ₹6 L gross a month, 14% contribution (60% of the maturity level) |
| HQ cost | ₹3.5 L a month in months 1-6, ₹5 L in 7-12, ₹6.5 L in 13-24 |

### 12.2 24-month outcome

| | Low | **Base** | High |
|---|---|---|---|
| Year 1 revenue | ₹45 L | **₹86 L** | ₹151 L |
| Year 2 revenue | ₹2.6 Cr | **₹4.3 Cr** | ₹7.1 Cr |
| Year 1 EBITDA | -₹71 L | **-₹64 L** | -₹52 L |
| Year 2 EBITDA | -₹94 L | **-₹62 L** | -₹12 L |
| **Peak funding need (cash trough)** | **₹1.83 Cr** | **₹1.44 Cr** | ₹0.88 Cr |
| Retailers live at month 24 | 75 | 75 | 75 |
| Revenue run-rate at month 24 (annualised) | ₹3.6 Cr | **₹5.8 Cr** | ₹9.3 Cr |

**Reading it:** the ₹2 Cr covers even the low case. In the base case, there is about ₹56 L left at month 24. The business is not EBITDA-positive in the first 24 months; each *cluster* reaches breakeven around month 10-12 after opening.

### 12.3 Use of the ₹2 Cr (24 months, base case)

| Use | ₹ Cr | Share |
|---|---|---|
| HQ team: 3 founders (lean pay), engineer, training lead, finance/legal | 1.29 | |
| Cluster operations: 3 clusters' fixed costs | 0.85 | |
| Cluster setup and working capital (parts, kits) | 0.18 | |
| **Total spend** | **2.32** | |
| Funded by operating contribution (installs, repairs, AMC, parts) | (0.88) | |
| **Net cash needed** | **1.44** | |
| **Buffer** | **0.56** | 28% of the round |

### 12.4 Where this goes by year 5 (illustrative; Series A and B needed)

| | Low | **Base** | High |
|---|---|---|---|
| Clusters | 18 | **30** | 45 |
| Retailers | 450 | **900** | 1,500 |
| Share of serviceable retailers | 1.9% | **3.8%** | 6.4% |
| Revenue | ₹40 Cr | **₹85 Cr** | ₹130 Cr |
| Source of revenue at maturity | services 55%, parts 40%, refurb 5% | | |
| EBITDA margin | 0-3% | **3-8%** | 8-12% |

**Honest note on margin:** the contribution margin on services is only 17-19%. The long-run business depends on the **layers** (parts wholesale, refurb, AMC) and on **fixed-cost leverage** (HQ and cluster overhead spread over more retailers). If the pilot shows that layers don't materialise, the business stays a low-margin service company and is not venture scale. That is the risk the angel is underwriting.

### 12.5 What the angel could earn (illustration, not a forecast)

Assume ₹2 Cr at ₹10 Cr pre-money (16.7%), later dilution for Series A (20%), Series B (15%) and a staff option top-up (8%). The ending stake is about 10.4%.

| Year 5 outcome | Revenue | Exit multiple | Company value | Angel proceeds | Multiple |
|---|---|---|---|---|---|
| Low | ₹40 Cr | 1.2x | ₹48 Cr | ₹5-6 Cr | **about 3x** |
| **Base** | ₹85 Cr | 1.8x | ₹153 Cr | ₹16 Cr | **about 8x** |
| High | ₹130 Cr | 2.5x | ₹325 Cr | ₹34 Cr | **about 17x** |

Multiples are for tech-enabled service businesses and are **[A]**. A strategic buyer could be a brand's service arm, a large retailer, an extended-warranty company, or a refurb/recommerce player. The investor gets a 1x non-participating preference; if sold below about ₹20 Cr, the preference applies.

---

## 13. Competition and why we win

| Player | What they do | Why they don't cover our position |
|---|---|---|
| **Urban Company** | Consumer app for appliance repair and installation in cities | City-focused; sells to the end customer, not through the retailer; no refurb, parts or training offering. Check its current city list; it may expand. **[E, verify]** |
| **Extended-warranty and protection-plan firms** (Onsitego, Servify and similar) | Sell plans through retailers; route repairs to partners | Closest to us on channel. They are plan sellers and need fulfilment partners in small towns, which can make them partners, not enemies. **[E, verify]** |
| **Brand service networks** | In-warranty installs and repairs | Thin in small towns; slow; not interested in out-of-warranty work |
| **Large retail chains' service arms** (Croma, Reliance Digital and similar) | Own service for own customers | Not in independent shops; not in small towns |
| **Local mechanics** | Cheap, fast, trusted by word of mouth | No guarantee, inconsistent quality, no record. This is the biggest competitor by volume. We win on trust, guarantee and the retailer's backing. |
| **Refurb and recommerce players** (Cashify and similar) | Buy and sell used devices | Mostly phones and urban; appliances are heavy and need local logistics **[E, verify]** |
| **Parts distributors and online spares sellers** | Sell parts | Not integrated with service demand or training |

**Why we should win:** we are the only one that starts from the retailer, builds a local certified workforce, and keeps the appliance record from the first installation to recycling. The competitor to worry about is a plan seller or brand that decides to build the same retailer-linked service layer. Our defence is speed, density in the first clusters, and the technician network.

---

## 14. The ask

| | |
|---|---|
| **Amount** | **₹2 Cr** (about $240k) |
| **Instrument and valuation** | **₹10 Cr pre-money, about 16.7% (equity or compulsorily convertible note)**. A convertible with a ₹12 Cr cap is acceptable. **[DECIDE]** |
| **Runway** | 24 months in the base case; 18+ months even in the low case |
| **Close** | One close. Or ₹1.2 Cr now and ₹0.8 Cr when cluster 1 shows contribution of ₹6,000+ per retailer (investor-friendly) |

### 14.1 What the money buys (milestones by month 24)

| Milestone | Target | Why it matters |
|---|---|---|
| **1. Three clusters live** | 75 retailers, about 1,000 jobs a month, about 40 technicians certified | Shows the model repeats |
| **2. Contribution per retailer** | ₹7,000+ a month | Proves unit economics |
| **3. Cluster 1 breakeven** | By month 10-12 | Proves density works |
| **4. Retailer retention** | 85%+ at 6 months | Proves the retailer value proposition |
| **5. AMC attach** | 20%+ of AC installs | Proves recurring revenue |
| **6. First brand or plan-seller paid pilot** | 1 signed | Opens the second revenue pool |
| **7. Series A readiness** | ₹5 Cr+ annualised revenue, 3 cluster P&Ls, cohort data | Sets up the next round |

### 14.2 The help we want beyond money

1. Introductions to **retailer associations** and large multi-brand dealers.
2. Introductions to **after-sales heads at appliance brands** and extended-warranty companies.
3. A **parts distributor** willing to extend credit.
4. An **e-waste/EPR** recycler for the future recycle layer.
5. A mentor who has **run a field-service business at scale**.

---

## 15. Risks, and what we do about each

| Risk | How it shows up | What we do |
|---|---|---|
| **Thin margin** | 17-19% contribution | Add layers (parts, refurb, AMC); watch contribution per retailer weekly; raise fees if retailers retain |
| **Retailers don't send volume** | Capture below 20% | Pilot kill threshold; test the "free installs" offer; consider a retailer fee |
| **Technician quality and leakage** (they take the customer directly) | Callbacks, lost customers | Certification, ratings, QR record, 90-day guarantee, quick payout, parts access they can't get elsewhere |
| **Seasonality** (AC peaks Mar-Jun) | Idle technicians in winter | Mix categories (geyser, RO, washing machine, fridge); AMC bookings spread over the year |
| **Urban Company or a plan seller moves into small towns** | Price pressure | Lock retailers in early; focus on density; partner with plan sellers |
| **Brands don't cooperate** | No parts, manuals, in-warranty work | Start with out-of-warranty and installation; use Right to Repair as a lever; independent parts |
| **Working capital** (parts, refurb stock) | Cash drain | Pooled buying; low-inventory model first; refurb only after repair volume |
| **Quality and safety incident** (AC gas, electrical) | Brand damage, liability | Safety checklist, insurance, certified-only dispatch, no AI override of safety rules |
| **Founder gap in retailer sales** | Slow retailer onboarding | Cluster manager hire; sales advisor; use pilot retailers as references |
| **Capital need beyond the seed** | Series A needs proof | Milestones in 14.1; the base case reaches ₹5.8 Cr annualised revenue at month 24 |

---

## 16. The deck, slide by slide (12 slides + appendix)

Each slide moves the investor along: curiosity, understanding, conviction, commitment.

| # | Slide | One line to land | Source in this file |
|---|---|---|---|
| 1 | **Title** | "The service arm for India's small-town appliance retailer." | 1 |
| 2 | **Problem (a person)** | A real retailer: "I sell an AC on Monday and the customer calls me angry on Thursday." | 2 |
| 3 | **Why now** | Wave of units leaving warranty; WhatsApp and voice AI; Right to Repair; EPR. | 3 |
| 4 | **Solution** | One picture of the lifecycle: install, repair, AMC, parts, refurb, recycle. | 4 |
| 5 | **How a job works** | Sale to job card to dispatch to record to renewal. | 4.3 |
| 6 | **Value for everyone** | Retailer, household, technician, brand: one line each. | 5 |
| 7 | **Market from the bottom up** | 23,400 retailers × ₹17 L = about ₹4,000 Cr. Our year-5 plan is 3.8% of retailers. | 6 |
| 8 | **Business model and unit economics** | ₹41k revenue and ₹7.8k contribution per retailer per month; cluster breakeven at 21 retailers. | 7, 8 |
| 9 | **What we did and the pilot** | Discovery numbers, MVP, pilot scorecard with kill thresholds. | 10 |
| 10 | **Traction** | Actual numbers (or honest "interview stage"). | 11 |
| 11 | **Team** | Three founders and the three roles; named gap and how we close it. | 9 |
| 12 | **The ask** | ₹2 Cr, 24 months, seven milestones, plus the help we want. | 14 |
| A | Appendix | Competition, financial model, 5-year view, risks, assumption list | 12, 13, 15, 17 |

**Rules for the deck:**
- Lead with what the retailer gets, not "AI-powered".
- One picture per slide; numbers on the slide are only the ones you will defend.
- Show the low, base and high cases, not a single forecast.
- Put every **[A]** in the appendix with a note on how the pilot tests it.

### 16.1 The ten-minute spoken flow

| Min | Beat | Line |
|---|---|---|
| 0:00 | Problem (a person) | "He sells an AC on Monday; by Thursday the customer is calling him, not the brand." |
| 1:30 | Insight | "The retailer owns the trust and the address book. Nobody connects him to a good technician." |
| 2:30 | Solution and a job | "Sale, install within 24 hours, a QR on the unit, a record for life." |
| 4:00 | Value for each side | "The retailer earns on every job, the technician earns 50% more, the customer gets a guarantee." |
| 5:00 | Market and unit economics | "About 40 jobs a day and 14 technicians in a cluster; it breaks even at 21 retailers." |
| 6:30 | Pilot and traction | "Here is what we tested in 90 days and what would have made us stop." |
| 7:30 | Team | "We have run Tier 2 technician networks, brand service partners and voice AI. Here is the gap and how we close it." |
| 8:30 | Risks, return | "Margins are thin; density fixes it; here's how you could lose, and what 3x, 8x and 17x look like." |
| 9:30 | Ask | "₹2 Cr, three clusters, seven milestones, and these introductions." |

---

## 17. Questions an angel will ask, with answers

**"Why would a retailer give you their customers?"**
Because we don't take the customer; we make them better served and pay the retailer on every job. The customer still sees the retailer's name on the sticker. The retailer is also protected from the installation-delay blame.

**"Why wouldn't a technician just take the customer directly?"**
Some will. We make that hard: the QR and record sit with us, the guarantee and parts come through us, and the technician earns more with us (steady jobs, parts access, certificate, payout in 48 hours). We also track the leakage rate as a metric.

**"Installation is only ₹110 contribution. Why bother?"**
It isn't the profit. It is the frequency and the data. Every install puts a QR on an appliance and creates a future repair, AMC and trade-in lead.

**"Isn't this just Urban Company for small towns?"**
Urban Company is a consumer app; we are a retailer-led service layer with a local workforce, parts and a record. In small towns customers call the shop they bought from, not an app. We will check UC's city list and sharpen this answer.

**"What stops a brand or a warranty company from doing this?"**
Brands want installations and ratings but not 3,000 small-town field forces; plan sellers need fulfilment. We can partner with both. The risk is that one of them builds it. Our defence is density and speed.

**"Your margins are thin. Where does the money come from?"**
From volume per cluster and from layers: parts wholesale, refurb, AMC and brand fees. Cluster economics show EBITDA of about ₹1.5 L a month at 40 retailers on services alone, before layers. We will show cluster P&Ls from the first cluster.

**"How do you hire and keep technicians?"**
We take them from the existing pool of 100-150 mechanics in each hub. We pay about 50% more per month than typical, train them for free, give a certificate, and route steady jobs. Training is our supply engine.

**"What if AC demand collapses in winter?"**
We pair AC with washing machines, refrigerators, geysers and RO, and sell AMC that spreads visits through the year.

**"How much of this is validated?"**
Today: **[FILL: interviews, LOIs, pilot jobs]**. The rest is assumption, tagged in this document. The pilot tests the nine hypotheses in section 10.3 and shows kill thresholds.

**"Why you?"**
Combine the three roles: Tier 2 technician networks (the CEO's FixNear), brand service partner network and claims (the COO), and Indian-language voice AI at scale (the CTO). The gap is retailer sales, and we are closing it with the first cluster manager and an advisor.

---

## 18. The assumption register (what to test first)

Ordered by how much each one moves the answer.

| # | Assumption | Base value | Low / high | How to test | Moves |
|---|---|---|---|---|---|
| 1 | Share of a retailer's installs we win | 45% | 30-55% | Pilot: count installs routed vs total sales | Contribution per retailer |
| 2 | Share of repairs from the retailer's base we win | 15% | 10-20% | Pilot: repair jobs per retailer per month | Contribution, breakeven |
| 3 | Retailers per cluster we can sign | 25 | 15-40 | Retailer LOIs and conversion | Cluster breakeven |
| 4 | Average out-of-warranty ticket | ₹1,150 | ₹950-1,300 | Log every job's bill | Repair contribution |
| 5 | Technician jobs per day | 3.8 | 3.2-4.2 | Dispatch logs | Technician pay, cost |
| 6 | Retailer commission levels | 5% / 8% / 15% | | Test 3 options with 20 retailers | Retailer value, margin |
| 7 | AMC attach | 5 per retailer per month | 3-8 | Counter sales in pilot | Recurring revenue |
| 8 | Retailer churn | 20% a year | 10-35% | Cohort retention | LTV |
| 9 | Outlets, serviceable share | 1.2 L, 30% | 0.8-1.6 L, 20-40% | Dealer association counts | TAM only |
| 10 | Active installed base per retailer | 5,000 | 3,500-6,500 | Ask 20 retailers for 5-year sales | Repair volume |
| 11 | Failure/service events per unit | 0.30 a year | 0.28-0.32 | Brand data; repair interviews | Repair volume |
| 12 | Parts wholesale to independent technicians | ₹10 L a month at maturity | | Pilot: sell to 10 mechanics | Layer margin |
| 13 | Exit multiple | 1.8x revenue | 1.2-2.5x | Comparable deals | Investor return |

**The three to test first:** #1 (installs won), #2 (repairs won) and #3 (retailers signed). If these three come in at the base case or above, the rest follows. If any one is at the low case, the model needs a change before scaling.

---

## 19. Next steps before you send this to investors

1. **Run the discovery numbers:** complete at least 40 retailer and 30 technician interviews and replace every **[FILL]** in sections 10-11.
2. **Resolve the pilot-status conflict** between `Keepwell overall story.md` and `KeepWell_Unresolved_Decisions.md`.
3. **Verify every [E]** (market facts, competitor coverage, regulations) and add sources.
4. **Check retailer counts** with two dealer associations and one brand's dealer list.
5. **Decide the two [DECIDE] items:** the valuation or cap, and the single versus two-tranche close.
6. **Name the advisors** and the first cluster manager (even as "in discussion").
7. **Collect three real retailer quotes** with permission and a photo.
8. **Re-run the model** with pilot actuals. The assumptions are in section 12.1 and 18; the base-case formulas are in sections 6 and 8.
