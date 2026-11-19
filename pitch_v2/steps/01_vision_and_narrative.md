# Step 1: Vision and narrative spine

**Phase A: Who we are. Status: DRAFT for approval (20 Nov 2026).**

> **Update after Steps 7b–8 (20 Nov 2026, final).** Current numbers (Step 7b): a mature 60-shop cluster earns **14–16% EBITDA on service** and breaks even at **22 shops** (35 shops on today's pilot economics). The pilot ran **8 months (Mar–Oct 2026)**, not 90 days. At company level, service alone reaches about breakeven by year 7 while the company grows, and **9.1% at the mature run-rate**; the data layer is what makes the growing company profitable.

> **Illustrative case.** This pitch is for the IIIT Hyderabad ESFS course. The founder histories, company timeline, pilot results and financials are assumptions, kept consistent with each other and with the research. The research itself is real and sourced.

**Tags:**
- **[Real]**: real research or evidence
- **[R]**: research in `pitch_v2/research/`
- **[Model]**: `ue_v2.py`
- **[Story]**: assumed backstory or pilot fact, built in Steps 2 and 6

**Builds on Gate 1 (approved 19 Nov):**
- `00_validation_report.md`
- `00b_margin_and_vision.md`
- `00c_service_value_and_pilot.md`

---

### 1.1 Names
- **Keepwell** is the company and the only name used in the pitch. There are no product sub-brands.
- **Products** are described by what they do: installation, repair, AMC, parts, exchange, verified records, refurbished appliances.
- **The technology** is described as *Keepwell's AI service layer* (§1.7), not as a named product. The CTO tells that part of the story.

### 1.2 The insight the company is built on
In a small Indian town, **the appliance shop owns the trust.** Families buy where they know the owner, and they call him when the AC stops. **But the shop's role ends at the counter.**
- The brand's installer comes when it comes. Brands quote 24–72 hours (LG) or 2–5 days (Flipkart) [R]. Documented no-shows exist [R].
- After warranty, the family is on its own with a local mechanic, with no fixed price, no guarantee and no record.
- The retailer earns **nothing after the sale**. His net margin is only **2–3%** [R]. Yet consumer commissions have held **sellers jointly liable** with brands for faulty products and service: Chennai ₹35k, Chandigarh, Hyderabad ₹60k [R/Real].
- Nobody keeps the appliance's history, so every repair, claim, exchange and resale starts from zero.

**The insight:** *the person customers trust (the retailer) and the people who can fix things (local technicians) are never connected, and no one keeps the record.* Connect them, under the retailer's name, and three things follow:
- customers stay
- technicians get steady work
- every appliance gets a life record

### 1.3 Company vision
> **Every appliance in small-town India is installed right, kept working, and given a second life, by people the family already trusts.**

- **Closing line:** *"Keepwell keeps the promise the shop made when it sold the appliance."*
- **Tagline under the logo:** **"The after-sale service arm of every small-town appliance shop."**

### 1.4 Company mission
> **Be the authorised, guaranteed service arm for independent appliance retailers, delivered by certified local technicians and run on an AI service layer. With every owner's consent, build the record that brands, retailers and recyclers can trust.**

### 1.5 What Keepwell does: the four phases, one record

| Phase | Years | Keepwell is… | What it sells | Who pays | Margin role |
|---|---|---|---|---|---|
| **1. Serve** | 1–2 | the shop's service arm | Installation (brand-authorised), out-of-warranty service and repair, AMC. Covers AC, washing machine, refrigerator and water purifier, with AC as the anchor | households, brands, plan sellers | profitable-by-design core: 18–20% contribution; mature cluster EBITDA 10–12% [Model] |
| **2. Supply** | 2–4 | the cluster's parts and exchange hub | parts to local agencies; trade-in pickup for brand exchange programmes; e-waste feeder | agencies, brands and exchange operators, recyclers | volume on visits we already make |
| **3. Know** | 3–6 | the record brands and retailers check | verified installations and claims; replacement leads and AMC renewals; failure intelligence | brands, plan sellers, retailers | 70–90% gross margin [R] |
| **4. Circulate** | 5–8 | the appliance's second life | refurbished appliances sold back through the same shops, with a warranty | budget buyers | selective; stock-heavy |

**For investors:** *HomeServe for India's independent appliance shops.* HomeServe built its business on exclusive service agreements with whoever owns the customer, plus dense, trained supply [R]. Keepwell does the same with the shop. Its data layer is something HomeServe never had.

### 1.6 Why we start with Serve, and why AC is the anchor
- **The pain, the payer and the data meet at the service visit.** Every visit is paid, builds the record and earns the retailer's trust. Every later layer depends on visits.
- **The AC brings about 85% of the value per shop** [Model]. It drives brand-authorised installs, frequent paid service, gas refills, and the AMC customers actually buy.
- **Four appliances from day one, not AC only.**
  - Four appliances bring about 17% more revenue and 23% more contribution per shop.
  - They need 7 fewer shops to break even.
  - They smooth the AC off-season: the seasonal peak index drops from 1.8 to 1.6 [Model].
  - The shop gets one partner for everything it sells.

### 1.7 The technology thread (the CTO's story)
Keepwell's **AI service layer** runs every phase, and it is the reason a small team can run 50–70 shops per cluster.

| Phase | What the AI does | What it replaces |
|---|---|---|
| Serve | Turns a Telugu, Hindi or English voice note or WhatsApp message into a job card. Predicts the fault and the likely part. Dispatches the job. Checks the work from photos and the serial number. Sends AMC reminders | a call centre, a second visit, paper job cards |
| Supply | Predicts parts demand by model and season. Pre-grades an old unit from its history before quoting an exchange | guesswork stock, re-quotes |
| Know | Turns each verified job into a record brands can audit. Flags failure patterns by model, age and region | manual claim checks |
| Circulate | Grades refurbishment candidates from service history | blind buying |

- **Cost:** under ₹5 per job (WhatsApp utility messages about ₹0.12; Gemini audio ₹0.05–0.17 a minute) [R].
- **Guardrails:** the AI never sets prices (always the rate card), never overrides safety (gas or electrical), and never decides refunds or warranty claims [R/design].
- **Positioning:** the AI is the cost engine and the record-builder, **not the moat** (§1.8).

### 1.8 The moat
The moat is the same one that worked for HomeServe, Asurion and Urban Company [R], plus the record:
1. **Multi-year, exclusive service-arm agreements with shops**, with a revenue share. The shop's customers become Keepwell's serviced base.
2. **Cluster density.** Fifty to seventy shops per cluster shorten travel, fill technicians' days and lower cost per job. A late entrant has to rebuild this town by town.
3. **Certified partner technicians.** We give them what they can't get alone: parts on credit, insurance, the guarantee, a certificate and steady work.
4. **The appliance record.** It is consent-based and grows with every visit. It becomes valuable to brands (verification, failure intelligence) and to retailers (renewals, upgrades).

### 1.9 The narrative spine (the order investors hear it)
1. **Hook, a shop owner's week [Story].** He sells an AC on Monday. By Thursday the customer is angry at *him*, not the brand. A consumer case can make him pay [Real precedent].
2. **The family's side [Real].** The household evidence we already hold: survey, diaries, agency stickers, a brand bot that failed.
3. **The insight.** The shop owns trust, technicians own skill, and no one connects them or keeps the record.
4. **Keepwell.** The shop's authorised service arm, covering four appliances, guaranteed, under the shop's name.
5. **How a job works, and the AI service layer.**
6. **Proof [Story].** The 90-day Vijayawada–Guntur pilot (Step 6).
7. **A healthy service business.** It breaks even at about 30 shops, reaches 10–12% at maturity, and earns back its opening cost in under two years [Model].
8. **The four phases.** Serve, Supply, Know, Circulate, and how margin and value grow.
9. **Market** (Step 4), **competition** (Step 5), **team** (Step 2).
10. **The ask and the path to exit.** A strategic sale in years 7–8 (Steps 8–9).

### 1.10 Why this problem, why this solution, why us
- **Why this problem:** retailers lose customers and carry the blame after the sale, families get unguaranteed repairs, and appliances have no record. It happens in the towns where appliance sales are growing fastest.
- **Why this solution:**
  - Work through the shop: trust already lives there.
  - Be authorised: required for in-warranty installs [R].
  - Build dense clusters: density is the biggest lever [Model].
  - Use per-job partner technicians, so technicians aren't paid to sit idle in the off-season [Model].
  - Build the record: it is where the high margins come from [R].
- **Why us:** three founders who cover retailer channel sales, field service operations and Indian-language AI (Step 2, rebuilt from scratch).

### 1.11 Why now
| Tailwind | Evidence [R] |
|---|---|
| The appliance wave is in small towns | AC penetration is only about 10%. 85% of Voltas buyers are first-time buyers. Blue Star makes 65% of its sales in Tier III–V towns. The AC market is growing at a 15% CAGR, from ₹53,600 Cr (CY25) to ₹93,610 Cr (CY29) |
| Units are leaving warranty in huge numbers | 80–91% of installed units are out of comprehensive warranty |
| Cheaper appliances, more buyers | GST on ACs was cut from 28% to 18% (Sep 2025) |
| AI in Indian languages is now cheap | Under ₹5 per job for voice and WhatsApp |
| Rules reward records and repair | Right to Repair portal; E-Waste Rules 2022 with EPR prices; DPDP Act consent rules (the record is consent-based by design) |
| Investors want profitable services | The Bain–IVCA 2026 report describes a decisive shift to unit economics and profitability |

### 1.12 X-factor (candidate, confirmed in Step 11)
- **The candidate:** *a founder who has sold to these very dealers, plus a brand authorisation at the pilot.* Step 2 builds the founder half. Step 6 tests the authorisation half.
- **The backup candidate:** the guarantee under the shop's name. No one else offers this to independent shops.

### 1.13 How this shows up in the pitch
- **Title slide:** Keepwell, *The after-sale service arm of every small-town appliance shop.*
- **Slide 2:** the shop owner's week (hook).
- **Vision slide:** the four phases on one appliance's life line.
- **Closing slide:** *"Keepwell keeps the promise the shop made when it sold the appliance."*

---

## Decisions to approve (Step 1)
1. **Vision:** *"Every appliance in small-town India is installed right, kept working, and given a second life, by people the family already trusts."*
2. **Mission** (§1.4) and **tagline:** *"The after-sale service arm of every small-town appliance shop."*
3. **Positioning:** *HomeServe for India's independent appliance shops.* The AI is the cost engine, not the moat.
4. **Four phases** (Serve, Supply, Know, Circulate) as the vision structure.
5. **Narrative spine** (§1.9): opens with the shop owner's week, then the family's evidence.
6. **Closing line:** *"Keepwell keeps the promise the shop made when it sold the appliance."*

On approval, Step 2 (founders and backstory, from scratch) comes next.
