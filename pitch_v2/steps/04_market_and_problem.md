# Step 4: Market and problem scale

**Phase B: the opportunity and the proof. Status: DRAFT for approval (19 Nov 2026). Revised after independent review.**

> **Final numbers (19 Nov 2026):** the pilot, unit economics, plan and deal are restated in **Step 7c** (`07c_simple_model.md`) and Steps 8–9. Where this document's numbers differ, Step 7c is the reference.



**Tags:**
- **[R]**: research in `pitch_v2/research/` and `pitch/archive/market_intel/`
- ****: `ue_v2.py` (the shop-level calculation in §4.2)
- ****: the team's own evidence (`pitch/archive/market_intel/raw/demand/team_evidence_extract.md`)
- ****: assumed founder facts (Step 2)

**Builds on:** Steps 0–3 (approved). **Feeds:** Step 7 (model), Step 9 (exit), Step 12 (market and problem slides).

> ### Read this first (flags for approval)
> 1. **TAM ≈ ₹4,000 Cr a year** (range ₹3,500–4,800 Cr). This is after-sale spend (installs, out-of-warranty service and repair, AMC) on the four appliances, linked to independent shops in Tier 2/3 India. It sits between two independent methods: shops ₹4,150 Cr, households ₹3,600 Cr.
> 2. **This replaces the ₹1,550 Cr in the validation report.** That figure counted only the ~9k large shops. Gate 1 then decided to serve **every** shop (00c §4c), so all ~45k shops count. The bridge is in §4.2. It is the same headline number the founders started with, reached a different way.
> 3. **SAM (5 southern states) ≈ ₹1,040 Cr. Beachhead (AP + Telangana) ≈ ₹360 Cr.** Both use the states' share of repair *value* (26% and 8.9%), not household counts.
> 4. **SOM in year 7: ₹130 Cr revenue from 3,300 shops (55 clusters).** Updated after Step 7b; was ₹115 Cr from 1,950 shops.
>    - **Nationally:** about 7% of India's ~45k independent shops. About 2,000 are in the south (20–25% of southern Tier 2/3 shops) and about 1,300 in partner clusters in the west.
>    - **Within the south:** about **20–25% of the southern Tier 2/3 shops**, because every year-7 shop is in the south.
>
>    The plan depends on winning density in the south, not a small national share.
> 5. **Honest point:** on the shop method, **AC is about 86% of the spend**. The household method puts it at about 56%, because it uses lower AC repair frequency. Either way AC anchors the business. The other three appliances are for utilisation and stickiness, not big money. The pilot's actual job mix will settle the share.
> 6. **Assumed, and it matters:**
>    - The average independent shop sells **50 major units a month** across all shops. This is lower than the 60 used in the model's BASE, which was for target shops.
>    - Total independent-shop sales are capped at **1.8–2.5 M units a month** nationally.
>    - **64%** of the value sits outside the metros [R: archive].
>
>    The Step 6 shop walk tests these.
> 7. **Hardest investor questions:**
>    - *"Your validation said ₹1,550 Cr. Why ₹4,000 Cr now?"* We now serve all 45k shops, not only the 9k large ones. National AC sales cap the total, and the household-side check lands at ₹3,600 Cr.
>    - *"Isn't that a quarter of the south?"* Yes: about 2,000 shops, 20–25% of southern Tier 2/3 shops by year 7, plus partner clusters in the west. Density, not national share, is the test.
>    - *"If AC is 86% of the spend, aren't you an AC company?"* AC drives the money. Without the other three appliances, a cluster needs 7 more shops to break even (00 §4b).

---

## 4.1 How this step is built
1. **Supply side (§4.2):** total units sold by independent shops × the after-sale spend each unit generates.
2. **Demand side (§4.3):** households × ownership × repair frequency × bills, from the earlier city study [R]. A cross-check.
3. **Revenue pools (§4.4):** what Keepwell can earn, not the total value of jobs.
4. **SAM and SOM (§4.5).**
5. **Problem scale (§4.6):** the numbers for the problem slide.

## 4.2 Supply side: units sold by independent shops × after-sale spend

**In the pitch we call these *local retailers*:** every independent appliance retailer in Tier 2/3 towns, of every size (00c §4c). National chains are excluded because their service is captive.

**Bridge from the validation report**
- **₹1,550 Cr:** 9k shops that sell more than 60 units a month, × the founders' per-shop spend. This counted large shops only.
- **00c §4c** changed the target to every independent shop, small ones included, because a small shop earns the same per unit.
- **So the base is all ~45k shops.** Shop count and shop size aren't independent: research derived units per shop by dividing national sales by the dealer count. We therefore size on **total units sold**, not shops × units.

**Total units sold through independent shops** [R: `retail_install/findings.md`]
- About 14 M ACs a year, of which 46–65% go through general trade.
- ACs are 25–35% of a dealer's major-appliance units.
- That gives about **1.8–2.5 M major units a month** across all independent shops.
- Spread over about 45k shops, that is an **average of about 50 units a month per shop** (range 35–65).
- **Units per shop:** the plan uses **74 a month** (measured in the pilot shops). **60** is the LOW case. About 50 is the all-India average from the supply method. Clusters are built in towns with bigger shops.
- **TAM bridge:** Gate 1's ₹1,550 Cr counted only about 9,000 large shops. The founders decided to serve **every** shop, so the base is about 45,000 shops. That takes the TAM to about ₹4,000 Cr. The deck leads with the beachhead (₹360 Cr) and the year-7 plan (₹130 Cr).

**After-sale spend per unit sold each month, per year** [Model, at 100% of the shop's base, net of GST]

At an average shop (50 units a month), after-sale spend is **₹15.1 L a year**, or about **₹30,200 a year for each unit it sells per month**.

| Appliance | ₹ L per shop a year |
|---|---|
| AC | 13.0 |
| Water purifier | 0.9 |
| Washing machine | 0.7 |
| Fridge | 0.6 |

| Type of spend | ₹ L per shop a year | Share |
|---|---|---|
| Out-of-warranty service and repair | 10.7 | 71% |
| Installs | 4.0 | 26% |
| AMC | 0.4 | 3% |

**Inputs:**
- **Mix:** AC 30%, fridge 25%, washing machine 15%, purifier 5%. TVs and other items are not serviced.
- **Active base:** 4.5 years of sales, 90% still in use. This is probably conservative, since ACs last 10+ years.
- **Out of warranty:** 80–91%.
- **Repair and service events per unit-year:** AC 1.55, fridge 0.11, washing machine 0.17, purifier 1.65.
- **Bills, including GST:** AC service ₹550, gas ₹2,300, repairs ₹1,200–1,500, purifier ₹600.
- **Installs:** AC ₹800 plus materials; washing machine ₹300.
- **AMC:** 5% of the out-of-warranty base.

Sources [R]: `parameters.csv` files and `ue_v2.CAT`.

**TAM by the supply method**

| | Units a month | All India | Tier 2/3 (64% of value outside metros [R: archive `states.csv`]) |
|---|---|---|---|
| LOW | 1.8 M | ₹5,400 Cr | ₹3,500 Cr |
| **BASE** | **2.15 M** | **₹6,500 Cr** | **₹4,150 Cr** |
| HIGH | 2.5 M | ₹7,550 Cr | ₹4,800 Cr |

## 4.3 Demand side: households (cross-check)

The earlier city-by-city study [R: `pitch/archive/market_intel/`] measured paid repair and service spend in **449 Tier 2/3 cities** for the same four appliances: **₹2,210 Cr a year** (BASE). It used NFHS-5 ownership × repair frequency × bills.

| Step | ₹ Cr |
|---|---|
| Repair and service spend, 449 Tier 2/3 cities | 2,210 |
| + 473 small towns (+19.8%) | 2,646 |
| + installs, grossing up so repair and service are 74% of the total (÷ 0.74) | **≈ 3,600** |

**Reconciliation**

| Method | Tier 2/3 after-sale spend |
|---|---|
| Supply (shops) | ₹4,150 Cr (₹3,500–4,800 Cr) |
| Demand (households) | ₹3,600 Cr |
| **TAM** | **≈ ₹4,000 Cr (₹3,500–4,800 Cr)** |

- The two methods use **different AC repair-frequency assumptions**: AC is 86% of the value in the supply method and 56% in the demand method. That they land close is partly coincidence.
- **We quote ₹4,000 Cr with the range, and say this openly.**
- The pilot's job mix will settle the AC share.

## 4.4 Revenue pools Keepwell can earn from (detail in 00b)

| Pool | Size | Keepwell earns | Phase |
|---|---|---|---|
| **Tier 2/3 after-sale spend (TAM)** | ≈ ₹4,000 Cr | full job value as principal, at 18–20% contribution | Serve (the base) |
| Spare parts | ₹2,400–4,900 Cr (all India) | 15–25% margin | Supply |
| Verification of installs and claims | ₹85–220 Cr | | Know |
| Leads and renewals | ceiling ₹70–280 Cr | | Know |
| Refurbished appliances | ₹600–2,600 Cr | | Circulate |

**Overlap warning:** most of the parts pool is **already inside** the repair bills counted in the TAM. Parts to *other* agencies is the only truly additional part. **These pools are not added to the TAM.**

## 4.5 SAM and SOM

| Layer | Definition | Size | Basis |
|---|---|---|---|
| **TAM** | After-sale spend linked to independent shops, Tier 2/3 India | **≈ ₹4,000 Cr** (₹3,500–4,800 Cr) | §4.2–4.3 |
| **SAM** | Same, in AP, Telangana, Karnataka, Tamil Nadu and Kerala, reachable by year 8 | **≈ ₹1,040 Cr** (₹910–1,250 Cr) | 26% of Tier 2/3 repair value [R: archive `states.csv`] |
| **Beachhead** | AP + Telangana | **≈ ₹360 Cr** (₹310–430 Cr) | 8.9% of Tier 2/3 repair value [R] |
| **SOM, year 7** | Plan reach (Step 7b BASE) | **₹130.5 Cr revenue** (₹79 Cr core service and installs, ₹3 Cr plan-seller jobs, ₹10 Cr Keepwell Protect, ₹27 Cr parts, trade-in and refurbished, ₹11 Cr data), **55 clusters (49 partner-run), 3,300 shops** | See below |

**How big a share the SOM needs:**
- **Of India's ~45k independent shops:** about **7%** (11% of the ~29k outside metros).
- **Of the south's Tier 2/3 independent shops:** about 2,000 of the 3,300 are in the south, again about **20–25%** of its estimated 7.5–10.4k (45k × 64% outside metros × 26–36% southern share). The other ~1,300 are partner clusters in Maharashtra, Gujarat and MP.
- **Keepwell Protect is new spend, not in the TAM:** covered units × attach × ₹2,000. It is about ₹10 Cr of the year-7 SOM.
- **What to say:** *"By year 7 we serve about a quarter of the independent shops in the southern towns we enter. That's why density, not national share, is our test."*

**Geography:**
- **Years 1–3:** AP + Telangana.
- **Years 3–6:** partner clusters across Karnataka, Tamil Nadu and Kerala.
- **Years 5–8:** partner clusters in Maharashtra, Gujarat and MP. The SAM's year-8 reach widens beyond the 5 southern states.

## 4.6 Problem scale (numbers for the problem slide)

| Problem | Number | Source |
|---|---|---|
| The shop earns nothing after the sale but carries the blame | Independent shops net **2–3%**. Consumer commissions held sellers jointly liable: Chennai ₹35k, Chandigarh, Hyderabad ₹60k | [R: retail_install] |
| Installation waits | **24–72 h** (LG), **2–5 days** (Flipkart). Documented no-shows | [R] |
| A non-authorised installation voids the warranty | Samsung, Daikin, Carrier, IFB, Godrej, Panasonic terms | [R] |
| Most machines are out of warranty | **80–91%** of the installed base | [R] |
| Repairs go to informal mechanics | **44%** of AC service goes to local technicians; brand 24%, dealer 13%, platform 13% (LocalCircles, n=13,487) | [R] |
| No record is kept | **7 of 12** surveyed households keep none. A handwritten "NEXT 15/M/26" filter date on a purifier. Agency stickers and diaries | |
| Repeat failures | "Repaired AC fixed only 60–70%". The same washing-machine error code came back after a year | |
| Size of the pool | **≈ ₹4,000 Cr** a year of after-sale spend flows through the customers of independent Tier 2/3 shops | §4.2–4.3 |

**One line for the slide:** *"The shop sells it, the brand is slow, the mechanic guesses, and nobody keeps the record: ₹4,000 Cr a year of after-sale spend that no one organises."*

## 4.7 Market quality and uniqueness (fundability matrix, Market row: used in Step 11)

| Measure | Rating | Why |
|---|---|---|
| **Potential** | Medium–high | A ≈ ₹4,000 Cr pool growing with AC penetration (about 10%; AC market growing 15% a year [R]) |
| **Uniqueness** | Medium | Independent Tier 2/3 shops have no service arm; incumbents each hold a slice [R] |
| **Quality** | Medium | Recurring spend, operator margins, seasonal AC demand. Founder edges cut the cost of acquiring fragmented shops |

## 4.8 Weak points, said before an investor does
- **The shop count and total units are derived (Low confidence).** Fix: a shop walk plus GST HSN counts in the pilot belt (Step 6).
- **The two methods disagree on how much of the spend is AC (86% vs 56%).** We say so; the pilot's job mix settles it.
- **The SOM needs 20–25% of southern shops plus partner clusters in the west.** We state it; partners are how the rollout is staffed (Step 7b).
- **Our household survey is small.** It is used for patterns and quotes only, never as a market statistic.

---

## Decisions to approve (Step 4)
1. **TAM ≈ ₹4,000 Cr** (₹3,500–4,800 Cr), sized on total units sold and cross-checked against households. It replaces the ₹1,550 Cr large-shop figure.
2. **SAM ≈ ₹1,040 Cr** (5 southern states, by value share). **Beachhead ≈ ₹360 Cr** (AP + Telangana).
3. **SOM in year 7:** ₹130 Cr from 3,300 shops, about 7% of India's independent shops; **20–25% of southern Tier 2/3 shops** plus partner clusters in the west. Stated openly (updated after Step 7b).
4. **AC is the majority of the spend** (56–86%). The other three appliances are pitched for utilisation and stickiness.
5. **Problem-slide numbers** (§4.6) and the one-line problem statement.

On approval, the next step is Step 5: product, fit and competition.
