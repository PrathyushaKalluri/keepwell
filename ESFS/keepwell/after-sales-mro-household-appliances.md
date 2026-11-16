# After-Sales Service Technology for Household Machines
### Maintenance, Repair & Overhaul (MRO), with marketplaces for parts, resale and recycling

> Domain deep-dive. Written 15 Nov 2026.
> **Confidence legend:** 🟢 verified in web research this session (source linked) · 🟡 general industry knowledge, not re-verified now · 🔴 contested / conflicting sources. Treat 🟡 items as "check before you quote it".

---

## 0. The 60-second version

A household machine (fridge, washing machine, AC, microwave, TV, water purifier, laptop, phone…) is **sold once but serviced for 8–15 years**. Everything that happens *after the sale* is the "after-sales" domain:

```
SELL → INSTALL → USE → MAINTAIN → BREAKS → DIAGNOSE → REPAIR (needs PARTS + TECHNICIAN)
                                              ↓ not worth fixing
                              RESELL / REFURBISH  →  RECYCLE / DISPOSE
```

Each arrow is a business. The domain is being reshaped by **four forces**: (1) right-to-repair law, (2) sustainability / circular economy and EPR rules, (3) AI + IoT making service predictive, and (4) platforms (marketplaces) aggregating a historically fragmented, offline, trust-poor market.

**The core structural problem:** supply is fragmented (millions of small technicians, informal parts dealers, informal scrap pickers), information is asymmetric (customer can't tell if the ₹3,000 quote is fair), and incentives are misaligned (manufacturers earn more from selling new than enabling repair). Almost every startup in this space is attacking one of those three.

---

## 1. What "MRO" means here

| Term | In industrial/aviation | In household appliances |
|---|---|---|
| **Maintenance** | Scheduled upkeep to prevent failure | AMC (annual maintenance contract), AC gas top-up/servicing, RO filter change, washing-machine descaling |
| **Repair** | Fixing a failure | Compressor replacement, PCB/board repair, motor, door seal, drain pump |
| **Overhaul** | Full strip-down and rebuild to like-new | **Refurbishment** — grading, replacing worn parts, re-certifying, reselling with warranty |

Household MRO borrows the vocabulary but differs: low ticket size (₹500–₹10,000 typical), huge volume, home visits (the "machine doesn't come to the shop"), consumer rather than enterprise buyer, and highly variable brand/model coverage.

---

## 2. Who is involved (the full cast)

### 2.1 Demand side
- **Consumers / households** – the person with the broken fridge. Needs: speed, trust, fair price, warranty on repair.
- **Landlords, property managers, PG/hostel & co-living operators, hotels, Airbnb hosts** – bulk, recurring B2B2C demand.
- **Small businesses** (cafés, salons, clinics) using the same class of machines (commercial ACs, fridges, water coolers).
- **Builders / housing societies** – AMCs for common-area equipment.

### 2.2 Supply side: those who make and sell machines
- **OEMs (Original Equipment Manufacturers)** – Samsung, LG, Whirlpool, Haier, Bosch/BSH, Panasonic, Godrej, Voltas, Daikin, IFB, Bajaj, Philips, Apple, Xiaomi, Dyson, etc. They define warranty, control spare-part supply, run **authorised service centres (ASCs)**, and (often) the call centre.
- **Retailers / e-commerce** – Amazon, Flipkart, Croma, Reliance Digital, Best Buy, Home Depot. They sell extended warranties and increasingly "installation + service" bundles.
- **Distributors & importers** – move machines and *parts* down the chain.

### 2.3 Service delivery
- **Authorised service centres / franchisees** – OEM-appointed, warranty-work focused, genuine parts, brand-controlled.
- **Independent repair shops & freelance technicians** – by far the largest group by headcount; mostly informal, skill learned on the job, cash/UPI payments. 🟡
- **Gig-style platform technicians** – Urban Company-type partners who take jobs via an app. 🟢 (Urban Company listed on Indian exchanges Sept 2025; appliance repair is one of its categories — [TechCrunch](https://techcrunch.com/2025/09/16/indias-urban-company-soars-58-above-ipo-price-in-years-most-subscribed-offering))
- **Third-party service administrators (TPAs) / service aggregators** – companies that run OEM or insurer service networks under contract (e.g. in the US/EU: Assurant, Asurion; in India: Servify, Onsitego-type players 🟡).
- **Specialist repair labs** – chip-level PCB repair, compressor rewinding, display repair — often the *back-end* the front-line technician sends boards to.

### 2.4 Parts & components
- **OEM genuine parts channels** – controlled supply, higher price, sometimes unavailable to independents (a core right-to-repair fight).
- **Aftermarket / compatible parts makers** – cheaper, variable quality.
- **Parts distributors & wholesalers** – e.g. Delhi's Lajpat Rai/Nehru Place-style markets for India 🟡; in Europe/US, online part stores.
- **Parts marketplaces / e-commerce** – 🟢 France's SOS Accessoire (raised ~€10M; claimed the EU spare-parts market is ~€4.1B — [TechCrunch](https://techcrunch.com/2021/04/28/frances-sos-accessoire-raises-12m-to-help-people-repair-their-home-appliances-themselves)) and competitor Spareka.
- **Harvested / used parts ("donor boards")** – parts pulled from dead units; a quiet but important circular-economy flow.

### 2.5 Warranty, protection and insurance
- **Extended warranty / device-protection providers** – 🟢 Asurion, Assurant, Allstate (via SquareTrade), AIG, Amtrust, Allianz Partners are repeatedly named leaders; North America is the largest regional market ([IMARC overview](https://www.imarcgroup.com/blog/top-extended-warranty-companies)). 🔴 Sources disagree on how concentrated the market is.
- **Home warranty plans** (US: American Home Shield, Frontdoor) 🟡 – subscription covering many home systems and appliances, not re-verified here.
- **Insurers & banks** – embed protection into credit cards, mobile plans and e-commerce checkouts.

### 2.6 Resale & refurbishment
- **Refurbished marketplaces** – 🟢 Back Market (France; reported ~$3.2B valuation in 2021 — dated, [TechCrunch](https://techcrunch.com/?p=1656131)), refurbed (Austria; 🟢 €50M raise reported, Oct 2025 — [Vestbee](https://vestbee.com/insights/articles/refurbed-secures-50-m)), Reebelo (APAC), Underdog (France, vertically integrated: source → repair → deliver).
- **India second-hand/recommerce** – 🟢 Zefo (furniture + appliances, Sequoia India-backed Series A, [e27](https://e27.co/zefo-raises-us6m-to-source-you-refurbished-furniture-and-home-appliances-20161115/)), Refabd (buys from people relocating); 🟡 Cashify (phones/laptops, strongest recommerce brand in India), OLX, Quikr.
- **Trade-in programmes** – OEM and retailer trade-ins (Apple, Samsung, Amazon) that feed refurbishers.
- **Liquidation / returns processors** – handle e-commerce returns and open-box stock; a major source of refurbished inventory. 🟡

### 2.7 Recycling & end-of-life
- **Formal e-waste recyclers** – licensed, shred and recover metals (copper, aluminium, gold, palladium) safely.
- **Informal sector** – the large "kabadiwala"/scrap network, especially in India and Africa; cheap but often unsafe and environmentally damaging.
- **Producer Responsibility Organisations (PROs)** – collective schemes that fulfil manufacturers' EPR obligations (Europe, increasingly India).
- **Refrigerant / hazardous waste handlers** – ACs and fridges contain regulated gases and oils.

### 2.8 Enablers (the "technology" in "after-sales service technology")
- **Field service management (FSM) software** – dispatch, scheduling, job tracking, invoicing (ServiceTitan, ServicePower, Salesforce FSL, Jobber, Housecall Pro; in India, many in-house or niche tools). 🟢 ([ServicePower 2026 trends](https://www.servicepower.com/resources/whitepapers-ebooks/2026-field-service-management-trends-report))
- **CRM / ticketing / call-centre / WhatsApp bots** – the customer interface.
- **Parts catalogues & exploded-view databases** – "which part number fits which model" is a genuinely hard data problem.
- **Repair knowledge bases & manuals** – OEM service manuals, iFixit-style guides, YouTube.
- **Payments, logistics & reverse logistics** – 3PLs that pick up broken units, move parts, return refurbished ones.
- **IoT / telemetry platforms** – connected appliances that report fault codes.
- **Regulators & standards bodies** – see §5.

### 2.9 Influencers on the rules of the game
- Governments (EU Commission, India's Dept of Consumer Affairs, MoEFCC/CPCB, US FTC & state legislatures)
- Consumer groups & advocacy (Repair.org, iFixit, Right to Repair Europe, The Restart Project)
- Standards/certification bodies (BIS in India, CE/ecodesign in EU, Energy Star)

---

## 3. Products & services (the "what is actually sold")

| Layer | Product/service | Who sells it | Typical pricing model |
|---|---|---|---|
| **Pre-purchase** | Product repairability info, spare-part availability promises | OEMs, regulators (EU repairability index in some countries) | Free / compliance |
| **Install** | Installation & demo (AC, washing machine, chimney, RO) | OEM, retailer, platforms | Fixed fee, often free with purchase |
| **Warranty** | Manufacturer warranty (typically 1–2 yrs; extra on compressors/motors) | OEM | Bundled in product price |
| **Extended warranty / protection** | Plans covering breakdown/damage beyond OEM warranty | Asurion, Assurant, SquareTrade, Onsitego-type, OEMs, retailers | One-time premium or subscription; margin-rich, insurance-like |
| **AMC / preventive maintenance** | Scheduled servicing (AC, RO, geyser) | OEM, platforms, local shops | Annual contract; recurring revenue |
| **On-demand repair** | Visit + diagnose + fix | ASCs, independents, platforms | Visit fee + labour + parts |
| **Mail-in / carry-in repair** | Device shipped or brought to centre | Phone/laptop brands, repair chains | Fixed quote |
| **DIY repair** | Parts + guides + videos | Parts marketplaces (SOS Accessoire, Spareka), iFixit | Parts margin |
| **Parts supply** | Genuine/aftermarket/used | OEM, distributors, marketplaces | Per-part; margin 20–60% 🟡 |
| **Refurbish & resale** | Graded refurbished appliances with warranty | Back Market, refurbed, Underdog, Cashify | Discount of ~30–60% vs new 🟡 |
| **Trade-in / buyback** | Cash or credit for old units | OEMs, retailers, recommerce firms | Spread between buyback and resale price |
| **Rental / subscription** | Appliance-as-a-service (Rentomojo, Furlenco in India 🟡; Bundles in EU) | Rental platforms | Monthly fee; **incentivises durability and repair** (owner bears repair cost) |
| **Recycling / EPR services** | Collection, dismantling, certificate generation | Recyclers, PROs | Fee from producers; certificate trading |

**Important insight:** *Rental/"appliance-as-a-service" flips the incentive.* If the provider owns the machine, repair and refurbishment become cost-savers rather than a cost centre — which is why this model is considered a structural future bet.

---

## 4. How money actually flows (current business reality)

### 4.1 Market size (and why not to trust any single number)
- 🟢 One estimate puts **home-appliance after-sales services at ≈ US$16.4B in 2025, rising to ≈ US$22.2B by 2030 (≈ 6.3% CAGR)** — [360iResearch via GII](https://www.giiresearch.com/report/ires1803452-home-appliance-after-sales-services-market-by.html).
- 🟢 A different publisher projects *home-appliance repair services* alone at **≈ US$15.6B by 2030, ≈ 9.55% CAGR** — [BlueWeave](https://blueweaveconsulting.com/press-release/global-home-appliance-repair-service-market-size-booming-at-significant-cagr-of-9-55-to-touch-usd-15-6-billion-by-2030).
- 🔴 These disagree mostly because of **scope definition** (repair only vs. all after-sales; whether warranty, parts and resale are included). Realistically the *true* informal-inclusive global market is larger than any report captures, because most repair is cash-based and unrecorded.
- 🟢 Adjacent field-service software market: ≈ US$5.6B (2025) → ≈ US$9.7B (2030), per a vendor blog (treat as directional) — [Brocoders](https://brocoders.com/blog/global-field-service-management-trends-2026/).

### 4.2 Where profit sits (rough, 🟡)
1. **Extended warranty / protection** – highest margin (insurance-style: premiums collected ≫ claims paid for many products).
2. **Genuine parts** – OEMs earn healthy margins; this is a reason repair access is contested.
3. **Refurbished resale** – decent gross margin if sourcing and grading are efficient; capital- and ops-intensive.
4. **Labour/service** – thin; the technician's time is the scarce resource, the platform takes ~20–30% commission 🟡.
5. **Recycling** – low margin, driven by regulation (EPR certificates) and commodity metal prices.

### 4.3 Business-model archetypes
| Model | Example | How it makes money | Main weakness |
|---|---|---|---|
| **OEM service network** | Samsung/LG ASCs | Warranty cost centre + paid out-of-warranty + parts | Slow, variable quality, limited to own brand |
| **Service marketplace** | Urban Company (🟢 listed Sept 2025; also launching own-brand hardware like water purifiers) | Commission per job, subscriptions | **Disintermediation** — customers re-book technicians directly (🟢 noted risk in analyst coverage) |
| **Parts e-commerce** | SOS Accessoire, Spareka | Parts margin + guides/diagnostic content | Need accurate model↔part catalogue; shipping cost on bulky parts |
| **Refurbished marketplace** | Back Market, refurbed | Take-rate on sales + warranty/insurance upsell | Quality control; reliance on third-party refurbishers |
| **Vertically-integrated refurb** | Underdog | Margin on full chain | Capital/ops heavy |
| **Warranty/TPA** | Asurion, Assurant | Premiums + service admin fees | Claims fraud, regulatory (insurance) overhead |
| **Rental/subscription** | Rentomojo-style 🟡 | Monthly rent over multiple lifecycles | Capex, logistics, damage risk |
| **Recycler/PRO** | Formal e-waste players | Processing fees, EPR certificates, metal recovery | Informal-sector competition; weak enforcement |

### 4.4 Region snapshot
- **EU** – regulation-led. Strong repair-and-refurb marketplace scene (France, Germany, Austria), parts e-commerce, repair cafés/bonus schemes (France *bonus réparation*, Austria repair voucher 🟡).
- **US** – extended-warranty and home-warranty heavy; independent appliance repair shops; state-by-state right-to-repair laws (NY, CA, MN, CO, OR… 🟡).
- **India** – huge, fast-growing installed base, informal-dominated, platform-led formalisation (Urban Company), strong second-hand culture, newly enforced EPR.
- **China/SEA** – large OEMs (Haier, Midea) run integrated service + smart-home ecosystems; super-app-based service booking. 🟡
- **Africa/LatAm** – repair is the default (low replacement rate), recycling mostly informal. 🟢 Africa documented formal e-waste recycling <1% ([Global E-waste Monitor 2024](https://unitar.org/about/news-stories/press/global-e-waste-monitor-2024-electronic-waste-rising-five-times-faster-documented-e-waste-recycling)).

---

## 5. Regulation & policy (the biggest external driver)

### 5.1 Right to Repair
- 🟢 **EU Directive (EU) 2024/1799** applies from **31 July 2026**, for specified goods bought after that date (includes certain household appliances, smartphones, tablets, displays). Manufacturers must repair outside warranty where technically possible and supply parts/tools at reasonable prices; sellers are nudged toward repair over replacement within warranty. It is *not* a blanket "free repair for everything" ([Irish Dept of Enterprise](https://enterprise.gov.ie/en/what-we-do/the-business-environment/right-to-repair-directive/)).
- 🔴 **EU online repair platform:** one government page says it was established 31 July 2026; another source says operational in 2028. Check the Commission directly.
- 🟡 **Ecodesign for Sustainable Products Regulation (ESPR)** and **EU energy label/repairability rules** for phones/tablets/washing machines/etc. already require spare parts availability (e.g. 7–10 years for key appliance parts) and repairability information.
- 🟡 **US:** state laws (New York, California, Minnesota, Colorado, Oregon…) require OEMs to provide parts, tools and manuals; the FTC has taken a pro-repair stance on warranty-voiding claims.
- 🟢/🔴 **India:** Department of Consumer Affairs runs a **Right to Repair portal** listing authorised repair centres and manuals; approach is described as non-confrontational and voluntary-leaning. Whether a binding statute exists in 2026 is unclear from my research — **verify with DoCA**.

### 5.2 Extended Producer Responsibility (EPR) & e-waste
- 🟢 **Global scale:** 62 Mt e-waste generated in 2022 (+82% vs 2010); only **22.3% documented as formally collected and recycled**; projected ≈ 82 Mt by 2030 with the formal recycling share *falling* to ~20% under business-as-usual. ≈ US$62B of recoverable resources lost ([UNITAR/ITU Global E-waste Monitor 2024](https://unitar.org/about/news-stories/press/global-e-waste-monitor-2024-electronic-waste-rising-five-times-faster-documented-e-waste-recycling)).
- 🟢 **India E-Waste (Management) Rules 2022:** producers register on the CPCB portal and meet rising recycling targets for 106 items from April 2023, **buying EPR certificates from registered recyclers**; *recycling* certificates offset the target while *refurbishing* certificates only defer it. 🔴 Sources disagree on the exact target schedule (e.g. 60% → 80% by 2027–28 vs 70% → 80%); weak enforcement means much volume still goes informal ([IMPRI](https://www.impriindia.com/insights/policy-update/e-waste-management-rules-2022-assessing-indias-extended-producer-responsibility-framework/)).
- 🟡 **EU WEEE Directive** – long-standing collection/recycling targets; **battery regulation** adds removable-battery and passport requirements.

### 5.3 What regulation changes commercially
- Makes **spare parts and manuals a sellable, contestable market** (not OEM-monopolised).
- Creates **demand for repair capacity** (more technicians, more parts logistics).
- Creates a **compliance-tech market** (EPR reporting, product passports, parts-availability tracking).
- Turns **refurbishing and reuse** into a priced, certified activity.

---

## 6. Pain points = where the opportunities are

| Stakeholder | Core pain | Opportunity type |
|---|---|---|
| **Consumer** | Don't know cause/cost; fear of being overcharged; long wait for technician or parts; repair vs replace unclear | Instant AI diagnosis, upfront pricing, repair-vs-replace advisor, warranty on repair |
| **Technician** | Inconsistent job flow, no parts-at-hand, no knowledge of newer boards/inverter tech, payment delays, no credit/insurance | Job marketplace, parts-on-demand, training/certification, financing, tool rental |
| **Platform** | Disintermediation, quality variance, high acquisition cost, parts logistics | Subscriptions/AMC lock-in, ratings + warranty, parts inventory network |
| **OEM** | Warranty cost, call-centre load, brand damage from bad service, new regulatory obligations | Remote diagnostics, predictive maintenance, parts forecasting, third-party service enablement |
| **Parts seller** | Wrong-part returns, catalogue chaos, counterfeit risk | Model↔part matching (visual search/AI), authenticity verification |
| **Refurbisher** | Inconsistent sourcing, grading subjectivity, warranty cost, consumer distrust | Standardised grading, diagnostics automation, certified warranty, supply from trade-in/returns |
| **Recycler/PRO** | Informal competition, poor collection volumes, traceability | Reverse-logistics apps, incentivised collection, certificate marketplaces, material passports |
| **Regulator** | Weak data & enforcement | Digital product passports, traceable EPR certificates |

---

## 7. Technology landscape

### 7.1 Today (mature or maturing)
- **FSM & dispatch:** route optimisation, skills-based assignment, mobile job apps, invoices. 🟢
- **AI-assisted scheduling and parts prediction:** forecast which parts a technician needs based on job history, seasonality, and appliance age. 🟢 (vendor-sourced — directional)
- **Ticketing/CRM + chat/WhatsApp bots** for intake, status and feedback.
- **Parts catalogue search** (model number → exploded view → part number), increasingly with photo-based matching. 🟡
- **Remote video support** and AR overlays for guided repair/self-repair. 🟢
- **Digital grading & testing for refurb** (automated diagnostics for phones/laptops; less mature for big appliances). 🟡
- **Marketplace engines:** reviews, escrow, pricing, warranty-as-a-service on resale.
- **EPR/recycling compliance platforms** (CPCB-linked portals, certificate trading). 🟢

### 7.2 Emerging (2025–2030)
- **Predictive maintenance via IoT** — connected appliances report faults/usage; service fires *before* failure. 🟢 (analyst-forecast; real adoption data is thin)
- **Generative-AI repair copilots** — technician or consumer describes symptoms / uploads photo or sound; AI suggests probable causes, steps, parts, with citations to manuals.
- **Computer vision & audio diagnostics** — identify part, damage, or abnormal compressor/motor noise from a phone.
- **Digital Product Passports (DPP)** — EU ESPR mandates product-level data on materials, repairability, parts → enables automated repair/recycling routing. 🟡
- **Agentic dispatch** — AI agents that book technicians, order parts, negotiate slots, and follow up autonomously. 🟢 (trend)
- **Parts 3D-printing / on-demand manufacturing** for discontinued plastics and brackets. 🟡
- **Blockchain/serialised traceability** for authenticity of parts and refurbished units (hype risk). 🟡
- **Embedded finance** — instant EMI for repairs, protection at checkout, technician micro-loans.

### 7.3 Honest caveat
🟢 Most "AI in field service" literature I found is **vendor marketing**. Independent evidence on measured impact in appliance repair specifically is thin — an opportunity, but also a reason to be sceptical of quoted percentages.

---

## 8. Current business happenings (2025–2026 snapshot)

- 🟢 **Right-to-repair goes live in the EU** (31 July 2026) — expect a wave of repair-friendly product launches, parts-pricing announcements and compliance tooling.
- 🟢 **Urban Company IPO** (Sept 2025; ₹1,900 cr issue, ~58% listing pop) validated the "gig-platform for home services" model at public-market scale, and the company is moving into own-brand hardware — i.e. platforms are climbing toward the product/parts layer.
- 🟢 **Refurbished marketplaces keep raising** — refurbed's €50M (Oct 2025), Reebelo's Series A, Back Market's earlier mega-rounds — showing continued investor appetite for recommerce.
- 🟢 **Parts-and-guides e-commerce** (SOS Accessoire/Spareka) is maturing in Europe and a template for India.
- 🟢 **E-waste keeps growing faster than recycling** (UN: 5× faster) → policy pressure → more EPR enforcement and certificate-trading activity.
- 🟡 **OEMs are repositioning**: self-repair programmes (Apple, Samsung, Google, Dyson, Miele-type parts programmes), longer parts-availability pledges, and launching their own certified-refurbished channels.
- 🟡 **Insurers/warranty players** are embedding protection into e-commerce checkouts and telecom/credit bundles and consolidating (SquareTrade–Allstate-type deals).
- 🟡 **Rental & subscription** continues to grow in India and parts of Europe.

---

## 9. Future direction (where this industry is heading)

1. **From reactive to predictive to autonomous.** Break-fix → condition-based maintenance → self-diagnosing/self-ordering appliances. Service gets triggered by the machine, not the customer.
2. **Repair becomes the default, not the exception.** Law (EU, US states, possibly India), cost-of-living and ESG push the "repair-vs-replace" default toward repair, creating technician and parts demand.
3. **Parts become an open market.** Compatible/3D-printed/used parts compete with OEM parts; the winners own catalogues and fitment data.
4. **Platforms vertically integrate.** Service marketplaces add parts, warranty, AMC subscriptions and refurbishment to fight disintermediation (Urban Company's hardware move is the early signal).
5. **Circular loops close.** A single operator (or tight partner network) handles *sell → service → buy-back → refurbish → resell → recycle*, with EPR certificates monetising the end of the loop.
6. **Ownership models shift.** Appliance-as-a-service and long-term rental align incentives toward durability and repairability.
7. **Digital Product Passports & traceability** make every unit's history (repairs, parts, owner, materials) queryable → higher resale value, easier recycling, fraud reduction.
8. **Technician upskilling at scale.** AI copilots + AR + certification lift average technician skill; this is a bigger lever than adding more technicians.
9. **Formalisation of the informal.** In India/Africa/SEA, apps + payments + credit pull informal repairers and scrap collectors onto platforms (and onto the tax and compliance net).
10. **Consolidation.** Expect roll-ups of local repair chains, parts distributors and refurbishers, plus OEM acquisitions of service tech.

**Risks to this thesis:** weak enforcement (EPR and right-to-repair on paper only), OEM design lock-in (glued parts, serialised components, software locks), tariff and parts-logistics shocks, and consumer apathy if new is cheap enough.

---

## 10. White-space ideas (for a hackathon / startup lens)

*(Inspired by the pain-point table; not from the research above — hypotheses to validate.)*

1. **Photo/sound/error-code → likely cause → part number → local technician quote** in one flow (AI + catalogue + marketplace).
2. **Repair-vs-replace advisor** using age, model, failure type, local part price, and EPR/resale value of old unit.
3. **Parts fitment graph for Indian-market models** (the equivalent of European parts catalogues for India's long-tail brands).
4. **Technician copilot in vernacular languages** with offline manuals and voice interface.
5. **Warranty-backed repair guarantee** on gig technicians to defeat disintermediation.
6. **Reverse-logistics + refurb-grade + EPR certificate** pipeline for housing societies and offices.
7. **B2B AMC platform for PGs/co-living/hotels** — recurring, predictable, high-density.
8. **Donor-board and used-parts exchange** with authenticity verification.
9. **EPR compliance/traceability SaaS** for small producers/importers.

---

## 11. Glossary

- **AMC** – Annual Maintenance Contract.
- **ASC** – Authorised Service Centre (OEM-approved).
- **EPR** – Extended Producer Responsibility: producers financially/operationally responsible for end-of-life of their products.
- **EEE / WEEE** – (Waste) Electrical & Electronic Equipment.
- **FSM** – Field Service Management software.
- **MRO** – Maintenance, Repair & Overhaul.
- **OEM** – Original Equipment Manufacturer.
- **PRO** – Producer Responsibility Organisation.
- **PCB** – Printed circuit board (the most expensive repairable part in modern appliances).
- **TPA** – Third-Party Administrator (runs warranty/service on behalf of OEM/insurer).
- **DPP** – Digital Product Passport.
- **Recommerce** – Re-commerce: resale of pre-owned goods.
- **Disintermediation** – customer and provider bypass the platform after first match.

---

## 12. What to verify before relying on this doc

| Item | Why |
|---|---|
| Cashify, Servify, Onsitego, Rentomojo, Furlenco details | Searches returned nothing on these; descriptions are from general knowledge |
| American Home Shield / Frontdoor | Not covered in search results |
| India binding right-to-repair law status | Conflicting/unclear sources |
| EU repair platform launch date | Sources conflict (2026 vs 2028) |
| India EPR target percentages | Sources show different schedules; use the Gazette |
| Market-size figures | Scope differs between publishers; use as ranges, not facts |
| Back Market valuation | 2021 figure; likely outdated |
| Anything marked 🟡 | Not re-verified in this session |

---

## Sources (from this session's research)

- Market size: [360iResearch / GII](https://www.giiresearch.com/report/ires1803452-home-appliance-after-sales-services-market-by.html) · [BlueWeave](https://blueweaveconsulting.com/press-release/global-home-appliance-repair-service-market-size-booming-at-significant-cagr-of-9-55-to-touch-usd-15-6-billion-by-2030)
- EU right to repair: [Irish Dept of Enterprise](https://enterprise.gov.ie/en/what-we-do/the-business-environment/right-to-repair-directive/) · [Engadget](https://engadget.com/2227720/eu-right-to-repair-directive-kicks-in-today) · [Balkan Green Energy News](https://balkangreenenergynews.com/eu-citizens-gain-the-right-to-have-goods-repaired/)
- India R2R: [Legacy IAS](https://www.legacyias.com/?p=143767)
- Marketplaces: [refurbed/Vestbee](https://vestbee.com/insights/articles/refurbed-secures-50-m) · [Back Market/TechCrunch](https://techcrunch.com/?p=1656131) · [SOS Accessoire/TechCrunch](https://techcrunch.com/2021/04/28/frances-sos-accessoire-raises-12m-to-help-people-repair-their-home-appliances-themselves) · [Zefo/e27](https://e27.co/zefo-raises-us6m-to-source-you-refurbished-furniture-and-home-appliances-20161115/)
- AI / FSM: [ServicePower 2026 report](https://www.servicepower.com/resources/whitepapers-ebooks/2026-field-service-management-trends-report) · [Brocoders](https://brocoders.com/blog/global-field-service-management-trends-2026/) · [BCG](https://www.bcg.com/assets/2026/executive-perspectives-future-of-field-service-with-applied-ai.pdf)
- E-waste: [UNITAR Global E-waste Monitor 2024](https://unitar.org/about/news-stories/press/global-e-waste-monitor-2024-electronic-waste-rising-five-times-faster-documented-e-waste-recycling) · [IMPRI on India EPR](https://www.impriindia.com/insights/policy-update/e-waste-management-rules-2022-assessing-indias-extended-producer-responsibility-framework/)
- Warranty: [IMARC](https://www.imarcgroup.com/blog/top-extended-warranty-companies) · [Reanin](https://www.reanin.com/reports/extended-warranty-market)
- Urban Company: [TechCrunch](https://techcrunch.com/2025/09/16/indias-urban-company-soars-58-above-ipo-price-in-years-most-subscribed-offering)
