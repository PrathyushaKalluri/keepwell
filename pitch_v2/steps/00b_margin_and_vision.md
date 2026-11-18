# Step 0b: Is the margin good enough, and where does Keepwell go? (Gate 1 follow-up)

> **Illustrative case** for the IIIT Hyderabad ESFS course pitch. The research is real and sourced. The plan's numbers are a model with tagged assumptions.
>
> **For approval, together with `00_validation_report.md`.**

**Engine:** `ue_v2.py`. To reproduce: `python3 ue_v2.py --G --stack`.

**Research files:**
- `research/opportunities_data/` (margin benchmarks; data and software layers)
- `research/opportunities_physical/` (trade-in, parts, refurbishment, e-waste, inspection)

---

## 1. Is a 15–20% margin thin? The verdict

**No. It is a normal, healthy margin for an operator, and it is not, on its own, a venture story.** The data layers below make it one.

**Compare on the same base.** Keepwell collects the full price of every job, so its margin must be compared with other companies' margin on full job value, not on their commission.

| Company (on full job value) | Contribution margin | EBITDA margin | Note |
|---|---|---|---|
| **Keepwell core (4 appliances, BASE)** | **18–20%** | 5–8% at scale (model) | |
| Urban Company, India (FY23 → H1 FY27) | 17.7% → 21.7% | −9.7% → 5.3% | Targets 9–10% EBITDA. Took 11 years to reach 4% (FACT) |
| Lloyd (Havells' AC business) | 8.4% | — | FACT, FY26 |
| OneAssist | — | 4.1% | FACT, FY25 |
| Servify / Onsitego / 247around / Snabbit | — | all loss-making | FACT |
| HomeServe (UK/US operator) | — | 17.2% | Bought for 2.9× revenue |
| Frontdoor, Asurion | — | 25–27% | Carry warranty risk (they sell plans) |
| ServiceTitan (software) | gross margin 70% | 9.8% op. margin | 7–9× revenue |

**What this means for the pitch:**
1. **Contribution of 15–20% is good.** It equals Urban Company's India business on the same base, and is more than double Lloyd's. Say it with confidence.
2. **Gross margin is the visible gap.** It is about 33% today against the ~40% that investors look for in services. The layers below lift it to about 35–36%, so say "towards 40%", not "above 40%".
3. **EBITDA reaches about 7–8% by years 7–8.** That is better than Urban Company's 4.1% today, but it is an operator outcome, valued at 2–3× revenue.
4. **The data layers earn 70–90% gross margin and are valued at about 7× revenue.** They are the reason the exit value grows faster than revenue. They must be sequenced and costed, not just promised.

**Bottom line:** pitch Keepwell as **a profitable-by-design operator that builds the appliance record, and then sells that record to brands, retailers and recyclers.** It is not a SaaS company.

---

## 2. The nine opportunities from your table, assessed

| Opportunity | Who pays | Revenue model | Gross margin | Capital | Fit with our network | When | Verdict |
|---|---|---|---|---|---|---|---|
| **Installation and claims verification** | Brands, plan sellers | ₹20–100 per verified record + API | 80–90% | Low | **Very high.** Every job already captures serial number, photos and install date | Year 3 | **Build.** Best data layer. Brands spend ₹475–1,140 Cr a year on warranty; LG pays about ₹1,590 per claim (FACT) |
| **Product quality and failure intelligence** | Brands | Enterprise SaaS, ₹10 L–1 Cr a year | 70–80% | Low | High, from year 5 | Year 5+ | **Build later,** as the next step from verification. On its own the software wallet is small (₹10–25 Cr). Brands already hold in-warranty data, so our edge is out-of-warranty and Tier 2/3 data |
| **Appliance ownership intelligence** | Retailers (replacement leads, AMC renewals) | ₹100–200 per lead, or ₹500 per sale | 60–80% | Low | High. The retailer owns the customer; needs DPDP consent | Year 4 | **Build.** Not for lending or underwriting |
| **Spare-parts sourcing** | Our own jobs, then cluster agencies | Parts margin + catalogue | 15–25% (contribution 8–12%) | ₹10 L stock per cluster | **Very high.** The appliance record predicts the part before the visit | Year 1 for own jobs, year 2 for agencies | **Build.** Biggest revenue layer; thin but steady. Out-of-warranty parts pool is ₹2,400–4,900 Cr |
| **Regional trade-in network** | Brands and retailers (exchange programmes) | Fee per unit (₹250–600) | High on net revenue, small in rupees | Float ₹3–8 L per cluster | **Very high.** The old unit leaves on the install visit | Year 2 | **Build as the field arm of Selsmart, Digi2L or brand programmes.** We can't outbid recyclers, who earn the EPR certificate |
| **Refurbished appliance marketplace** | Budget buyers, landlords, hostels | Resale margin | 15–35% (base about 25%) | ₹12 L per cluster (stock + workshop) | High: trade-ins supply the units, and technicians refurbish in the off-season | Year 5, half the clusters | **Build selectively.** Watch warranty and R-22 risk. Back Market and Refurbed show the model works |
| **E-waste collection and tracking** | Recyclers, producer-responsibility organisations | Handling fee of ₹80–240 a unit | — | Low | Medium | Year 3 | **Feeder only.** EPR certificates go to recyclers, and the ₹22/kg floor is in court. Worth goodwill, not profit |
| **Retailer sales and inventory intelligence** | Retailers | SaaS ₹3.5–22k a year | — | Low | Medium | — | **Don't build it as a product.** The market is crowded (Vyapar lost ₹63 Cr on ₹69 Cr), and we don't see stock or sell-in. Give retailers a free dashboard showing their installed base and renewals |
| **Manufacturing quality inspection** | OEM and ODM plants | Enterprise contracts | 60–75% | Moderate | Low: different buyer, skills and sales cycle | — | **Avoid.** Funded specialists already exist (SwitchOn, Instrumental). Sell field-failure data to brands instead |

---

## 3. The vision: from service arm to the appliance's life record

**Keepwell keeps every appliance in small-town India working, from the day it is installed to the day it is recycled. Every visit adds to one trusted record.**

| Phase | Years | What Keepwell is | What it adds | Who pays |
|---|---|---|---|---|
| **1. Serve** | 1–2 | The authorised service arm for the town's appliance shops | Installs, repairs and AMC for AC, washing machine, fridge and purifier. Parts for our own jobs | Households, brands (installs), plan sellers |
| **2. Supply** | 2–4 | The cluster's parts and exchange hub | Parts to local agencies; trade-in pickup for brand exchange programmes; e-waste feeder | Agencies, brands and exchange operators, recyclers |
| **3. Know** | 3–6 | The record brands and retailers check | Verified installs and claims; replacement leads and AMC renewals for retailers; failure intelligence for brands | Brands, plan sellers, retailers |
| **4. Circulate** | 5–8 | The second life of the appliance | Refurbished appliances sold back through the same shops, with a warranty | Budget buyers, through retailers |

**The technology thread (the CTO's story; Keepwell is the only name):**

| Phase | What the AI layer does |
|---|---|
| Serve | Turns a Telugu or Hindi voice note into a job card and dispatches it |
| Supply | Predicts the part before the visit |
| Know | Verifies the job from photos and the serial number |
| Circulate | Grades an old unit from its history |

The same record and AI layer is reused at every phase, so the cost of each new layer falls.

---

## 4. Eight-year plan (BASE), the scaling and margin story

**Assumptions:**
- **Clusters at year end:** 1, 3, 8, 16, 28, 45, 65, 90.
- **Cluster size:** each cluster has about 30 shops selling about 80 units a month.
- **Ramp:** a new cluster runs at about 40% in its first year.

| | Y1 | Y2 | Y3 | Y4 | Y5 | Y6 | **Y7** | Y8 |
|---|---|---|---|---|---|---|---|---|
| Clusters (year end) | 1 | 3 | 8 | 16 | 28 | 45 | **65** | 90 |
| Shops served | 30 | 90 | 240 | 480 | 840 | 1,350 | **1,950** | 2,700 |
| **Revenue (₹ Cr)** | 0.4 | 2.3 | 7.3 | 18.4 | 39.6 | 71.4 | **115.5** | 164.3 |
| of which: core service | 0.4 | 2.0 | 5.6 | 12.5 | 23.2 | 38.9 | **59.2** | 83.8 |
| of which: data layers | 0 | 0 | 0.1 | 0.6 | 3.2 | 6.3 | **10.0** | 15.1 |
| Gross margin | 33% | 32% | 33% | 34% | 35% | 35% | **35%** | 35% |
| Contribution margin | 18% | 18% | 20% | 21% | 23% | 23% | **23%** | 23% |
| **EBITDA (₹ Cr)** | −0.6 | −0.8 | −1.1 | −0.9 | +1.0 | +3.6 | **+7.7** | +12.9 |
| EBITDA margin | — | — | — | −5% | 3% | 5% | **7%** | 8% |

**Year-7 revenue by line (₹ Cr):**

| Line | Year 7 |
|---|---|
| Core service | 59.2 |
| Refurbished | 21.2 |
| Parts | 18.6 |
| Trade-in | 5.7 |
| Brand intelligence / API | 5.0 |
| Verification | 2.9 |
| Leads and renewals | 2.1 |
| E-waste | 0.8 |

**Low and high cases:**
- **LOW** (data layers at 60% adoption): ₹93 Cr revenue in year 7, EBITDA only +2%. Cash turns positive only in year 8.
- **HIGH:** ₹119 Cr revenue and 8% EBITDA in year 7.

**What actually moves margin up:**
1. Data layers growing from 0% to about 9% of revenue.
2. Cluster fixed costs and HQ spread over more clusters.
3. Parts and trade-in riding on visits we already make.

**What does not:** wishing the core service above about 20% contribution.

---

## 5. Capital, rounds and exit

**Cash need, including cluster opening costs:** each new cluster costs about ₹20 L (shop onboarding, set-up, working capital, parts stock). Refurbishment adds ₹12 L per cluster from year 5.

| | LOW | BASE | HIGH |
|---|---|---|---|
| Peak cumulative cash need | ₹24 Cr (never turns positive in 8 years) | **₹10.6 Cr (year 6), cash-positive from year 7** | ₹8.8 Cr |

**Round path implied by BASE.** The exact ask is set in Step 8.

| Round | When | Amount | What it buys | Gate to the next round |
|---|---|---|---|---|
| First round (angels / pre-seed) | Now | about ₹1–2 Cr | 1 cluster through one summer, then 3 clusters | Contribution of ₹4k+ per shop, brand authorisation, routing of 50%+ |
| Seed | Year 2–3 | about ₹6–8 Cr | 3 → 16 clusters; parts and trade-in live | Revenue of about ₹18 Cr at the year-4 run-rate; first verification contract |
| Series A | Year 4–5 | about ₹15–25 Cr | 16 → 65 clusters; data layers | EBITDA-positive (year 5) |

**Exit: a strategic sale in years 7–8.**
- **Revenue:** about **₹115 Cr** (year 7) or **₹165 Cr** (year 8).
- **Value:** about **₹330 Cr** (year 7) to **₹480 Cr** (year 8). That is operations revenue at 2.5× plus data revenue at 7×.
- **Cross-check:** EBITDA × 10 gives only ₹77–129 Cr. The gap is the data layers; without them the exit is small.
- **Likely buyers:**
  - Onsitego / Servify (protection plus service)
  - Urban Company (Tier 2/3 entry)
  - An appliance brand's service arm
  - Asurion-type acquirers
  - Selsmart / Attero or Cashify (for the circular layer)

Precedents: Onsitego bought Qdigi for ₹80 Cr, Servify bought 247around, Asurion is buying Domestic & General at about 2×, and Brookfield bought HomeServe at 2.9×.

**Honest limits:**
- The exit value rests on the data layers reaching about 9% of revenue. The pilot must show that brands pay at least ₹20 per verified record.
- Refurbishment is the second-biggest line in year 7 and carries stock and warranty risk.
- In the LOW case the business is a modest operator. That is why the first round is small and tied to milestones.

---

## 6. Decisions for you (Gate 1, together with the validation report)

1. **Margin:** do you accept the framing "a healthy operator (contribution 18–23%) that becomes more valuable through data layers"? Recommended: yes.
2. **Opportunities:**
   - **Build:** verification, parts, trade-in, leads and renewals, and failure intelligence.
   - **Selective:** refurbishment.
   - **Feeder only:** e-waste.
   - **Drop:** retailer SaaS and manufacturing inspection.

   Do you agree?
3. **Exit framing:** a strategic sale in years 7–8 at about ₹115–165 Cr of revenue (BASE). Do you agree?
4. **Still open from before:** the pilot cluster (Warangal–Karimnagar or Vijayawada–Guntur).
