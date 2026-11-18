# Step 0: The tough-questions bank, answered

**Status:** answered 19 Nov 2026 from the research (A, B and C), the unit-economics engine (M) and our reasoning (R).

**Sources:**
- **RA:** `research/retail_install/findings.md`
- **RB:** `research/supply_layers/findings.md`
- **RC:** `research/competitors_funding/findings.md`
- **UE:** `steps/00_unit_economics.md`

**Status codes:**
- **D:** answered with data
- **R:** answered with reasoning
- **OPEN:** a pilot test, with its kill threshold

## 1. Investor
| ID | Question | Answer | Status |
|---|---|---|---|
| I1 | Why would a retailer hand over its customers? | It doesn't hand them over. We operate under the retailer's name, and the customer stays the retailer's. **What it gains:** ₹2–3.5k a month in commissions (UE). Relief from complaints and from *joint liability*: consumer commissions have held sellers liable alongside brands (Chennai ₹35k, Chandigarh, Hyderabad ₹60k; RA). A service record of every buyer, for resale and exchange. **What it loses:** nothing it earns today; a retailer earns ₹0 after the sale. Its net margin is only 2–3% (RA), so a ₹3k commission is meaningful. | D + OPEN (routing ≥40%) |
| I2 | Who pays for AC installation today? | **The customer, paid directly to the brand's authorised technician:** ₹1,199–1,500 plus GST, with materials extra (copper ₹850–1,100 a metre, bracket ₹750). It is "free" only on promotions. Water purifier installation is free inside the brand plan. A geyser costs ₹250 (RA). | D |
| I3 | Does a third-party installation void the warranty? | **Yes, for ACs.** The terms of Samsung, Daikin, Carrier, IFB, Godrej and Panasonic say so. Flipkart and Reliance accept returns only after an authorised install, and warranty activation depends on the installer registering the unit (RA). **So we must be brand-authorised, or work under the retailer's authorised-dealer status.** | D |
| I4 / S7 | How many retailers, and how many are serviceable? | 30k / 45k / 70k independent large-appliance dealers. **5k / 9k / 18k sell more than 60 units a month** (derived from LG's 30,726 dealers, Voltas 30k+, Blue Star 10k+ and a 40–65% general-trade share; RA). The founders' 23,400 is above our HIGH, so the market is about half the stated size. | D (derived, Low confidence) |
| I5 | Venture-scale or services? | It is an **operator with 15–25% contribution** (UE §6). Operators sell at 2–3× revenue (HomeServe 2.9×, Domestic & General 2.0×, Frontdoor 2.9×; RC). A venture outcome needs scale (₹100 Cr+ revenue) plus the high-margin layers. Be honest that this is a density business. | D + R |
| I6 | Leakage? | No Indian rate is published. The home-cleaning analog is about 1.2%. For repairs, where the customer keeps the technician's number, we assume 5–30% (RB). **Our levers:** the 90-day guarantee applies only to jobs booked through us; payment through us; a QR code on the unit; parts access; the retailer's name. | OPEN (measure it by auditing the installed base) |
| I7 / S3 | Why hasn't 247around, Onsitego or Urban Company done this? | **They each cover a different slice:** 247around and SERVIZ do brand-paid jobs (247around makes about ₹14.5 Cr a year at a loss after 10 years). Onsitego, Zopper and OneAssist sell plans at the counter. Jeeves and resQ serve their own retailer only. Urban Company is in 51 cities, and its top 10 cities are over 90% of the value of its jobs. Onsitego left consumer repair because customer acquisition was too costly. **No one runs the full job for independent Tier 2/3 shops. That is untested, not disproven** (RC). Onsitego is the closest threat. | D |
| I8 | What is the moat? | Analogs (HomeServe, Asurion, Urban Company) built moats from (1) exclusive multi-year contracts with whoever owns the point of sale and (2) dense, trained supply (RC). Ours: multi-year service-arm agreements with retailers, cluster density, certified partner technicians, and the appliance record. **The AI is the cost engine, not the moat.** | D + R |
| I9 | Exits? | **Strategic buyers:** Onsitego (bought Qdigi for ₹80 Cr), Servify (bought 247around; valued at ₹5,660 Cr), Urban Company (12.9× net revenue at IPO), brands' service arms, Asurion-type acquirers. **Operator multiples:** 2–3× revenue (RC). | D |
| I10 | What is proven? | **Today:** the research (shops, installation rules, prices, competitors). **Story:** discovery and a 90-day pilot (Step 6). **Not proven:** routing rate, brand authorisation, repair capture, technician productivity. | R |
| I11 | Why this team? | The backstory is rebuilt in Step 2 so one founder comes from a brand's dealer and channel sales. | R (Step 2) |
| I12 | Why now? | AC penetration is about 10%, and 85% of Voltas buyers buy for the first time. Blue Star makes 65% of its sales in Tier III–V towns. GST on ACs was cut to 18% (Sep 2025). Indian-language AI costs under ₹5 a job. Right to Repair and E-waste rules are coming in (RA, RB). | D |
| I13 | Capital to Series A? | The Series A bar is about ₹16–20 Cr+ in run-rate (RC). That means 420–525 retailers, or 14–18 clusters (UE). The path: **about ₹2–2.5 Cr to prove 3 clusters, then a ₹8–15 Cr seed, then Series A.** | D + M |
| I14 | What do angels and seed investors pay? | ₹1.5–2.5 Cr at a ₹6–12 Cr pre-money, on iSAFE or CCPS. 100X.VC invests ₹1.25 Cr for 15%. The India seed median is $1M. The course's MediQuick example is ₹2.5 Cr at ₹7.5 Cr pre (RC). | D |
| I15 | Gross or net revenue? | **We are the principal** (we set the price, guarantee the job and carry the rework), so revenue is booked gross under Ind AS 115. Show the gross job value, our revenue, contribution and our take side by side. Benchmark against operators, not marketplaces (RC). | D |

## 2. Founder and operator
| ID | Question | Answer | Status |
|---|---|---|---|
| F1 | Real job volume per retailer? | BASE (60 units a month, 3,000 units installed): about 6 brand-authorised AC installs, 5 other installs, 11 out-of-warranty jobs and 4 AMCs sold, which is **about 23 field visits a month** (UE). | M + OPEN |
| F2 | Installation share by category? | Split AC 100%, water purifier 100% (free), geyser about 100%, washing machine 80–100%, TV 40–70%, fridge about 0% (RA). | D/A |
| F3 | Can we recruit and keep technicians? | A Tier 2/3 mechanic earns ₹10–25k today; Urban Company partners net about ₹28k (RB). In the hybrid design, partners average about ₹18k from us on top of their own jobs. **Attrition among employed technicians is 30–60% a year** (TeamLease). | D + OPEN |
| F4 | Jobs a day? | Urban Company averages 1.7 a day; partners claim 70–80 a month. BASE is 2.8 a day at 70% utilisation, which is **about 49 a month** (RB). | D/A |
| F5 | Seasonality? | AC index is 1.8× in Mar–Jun and 0.6× in Oct–Feb. Voltas books 35.8% of its sales in Q1 and 14.9% in Q2 (RB). We fill the trough with AMC visits and brand-paid filler jobs. | D |
| F6 | Working capital? | About ₹3 L per cluster for parts and kits (assumption). Distributor credit terms are UNKNOWN. | OPEN |
| F7 | Time and cost to sign 25 shops? | UNKNOWN. The CAC of ₹18k is an assumption (RA). | OPEN (2-week founder sales sprint) |
| F8 | Liability insurance? | About ₹2.5 a job: group personal accident cover about ₹1,250 per technician per year, public liability ₹8–20k a year (RB). No refrigerant licence is mandatory. | D |
| F9 | Employ, contract or partner? | All four labour codes are in force from 21 Nov 2025. The central aggregator levy (1–2%) is not yet notified. Karnataka charges 1% of payout, Telangana 1–2% (2026 Act), Andhra Pradesh nothing. Employing adds about 6–12% in statutory costs (RB). **Certified partners paid per job** avoid the cost of an income floor. | D |
| F10 | GST? | 18% on installation, repair and AMC (SAC 9987). An unregistered local mechanic under ₹20 L turnover charges none. The ₹50 L composition limit is outgrown by one cluster (RB). **Price including GST** for repair and AMC. | D |
| F11 | Parts? | Parts are 30–60% of the repair bill. Our margin is UNKNOWN; dealer margins of 15–40% are a proxy (RB). | OPEN (distributor interviews) |
| F12 | First cluster? | Warangal–Karimnagar or Vijayawada–Guntur. Bajaj Electronics has 1–7 stores per city (RA). Fewer chains in Warangal and Karimnagar suggests more independents. | D + R |
| F13 | Commission expectations? | No Indian rate is published for extended-warranty commission. EMIL turns about a third of extended-warranty revenue into PBT (RA). **5–8% looks low against that.** We test 3 commission levels. | OPEN |

## 3. Product and technology builder
| ID | Question | Answer | Status |
|---|---|---|---|
| T1 | What does the technology automate? | Intake (voice and WhatsApp in Telugu, Hindi and English), triage and likely-part prediction, dispatch and routing, a photo and serial-number checklist with AI quality checks, the appliance record and QR code, reminders and AMC renewals, the retailer dashboard and commissions, technician payouts. **Effect:** one cluster manager plus one dispatcher can run 30 retailers and about 700 visits a month. | R (Step 5) |
| T2 | Cost per job? | Under ₹5: WhatsApp utility message about ₹0.12, Gemini audio ₹0.05–0.17 a minute, Sarvam speech-to-text about ₹0.49 a minute, UPI MDR 0% (RB). | D |
| T3 | Data for diagnosis? | Brand manuals (Right to Repair portal coverage UNKNOWN by brand) plus our own job logs, which compound with every verified job. | R + OPEN |
| T4 | Where AI must not decide | Safety (gas, electrical), the price (always the rate card), refunds and warranty claims: a human decides these. | R |
| T5 | What the retailer touches | WhatsApp ("book install"), a QR standee, a weekly summary. No app. | R |
| T6 | Proving the work was done | A photo checklist, serial capture, customer OTP at close, and random callbacks. | R |
| T7 | Stopping leakage with technology | The QR code points to us, payments go through us, the guarantee applies only when booked, and payouts are fast. | R + OPEN |

## 4. Rational skeptic
| ID | Question | Answer | Status |
|---|---|---|---|
| S1 | If installation is the brand's, what's left? | Being authorised, or working under the dealer's authorised status. If not authorised: house-move reinstalls (₹500–600 to dismantle plus about ₹1,200 to install), materials, non-AC installs and out-of-warranty work. **Without authorisation the founders' design breaks even only at 188 retailers per cluster** (UE). | D + M |
| S2 | Retailer already has an on-call technician? | UNKNOWN. **Pitch:** a guaranteed, recorded, liability-safe service under the retailer's name. | OPEN (10 shop interviews) |
| S3 | Why not subcontract for 247around? | A subcontractor keeps about 70% of the job but owns neither the retailer nor the household (RC). We use brand-paid jobs only as filler. | D + R |
| S4 | Does installation lose money after overhead? | Authorised AC installs contribute about ₹730 each with materials (BASE), the strongest line. Non-AC installs contribute about ₹77. | M |
| S5 | Will a household pay for an AMC? | The market price is ₹1,098–1,298 (Urban Company). Attach rates are 2–10% of out-of-warranty units. Renewal is UNKNOWN (RB). AMC contributes about 18% at ₹1,299. | D + OPEN |
| S6 | Refurbishment and EPR? | Recommerce gross margin is about 15.7% (Cashify). An AC is worth about ₹3,500 as scrap. EPR certificates go to recyclers, and the ₹22/kg floor is contested in court (RB). **These are upside layers, not the base case.** | D |
| S8 | Retailer wants a share forever? | Design it as a multi-year service-arm agreement: a commission on jobs from the retailer's base for its term, a desk fee and exclusivity in its catchment. The HomeServe utility model is the precedent (RC). | R |
| S9 | Earlier research found about ₹56 a job. What's different? | That model was routing only, with no install wedge and no principal margin. This model **does the job** (installs about ₹730, repairs about ₹164) and adds a desk fee. Routing-only (design D) still fails here: 53 retailers to break even. | M |
| S10 | Kill criteria? | Kill if, by month 4 of the pilot, any of these holds: units under 40 a month, no brand authorisation, install routing under 40%, contribution per retailer under ₹4k (UE §5). | M + R |
