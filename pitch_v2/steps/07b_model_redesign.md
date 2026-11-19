# Step 7b: Making the business model work (redesign)

**Phase C (the money). Status: APPROVED (20 Nov 2026); model rebuilt (`keepwell_model.xlsx`: 630 formulas, 0 errors, 0 mismatches in all four scenarios). Replaces the A/B/C decision in Step 7 §7.6.**

> **Illustrative case** for the IIIT Hyderabad ESFS course pitch.
> - **Engine:** `model/plan_v3.py`, which runs on the Step 7 engine (`plan_core.py`). Run `python3 model/plan_v3.py` to print every table below.
> - **Check:** lever 0 of the waterfall reproduces the corrected Step 7 BASE exactly (₹81.5 Cr; ₹1.0 Cr; peak ₹21.6 Cr).
> - **Review:** an independent reviewer pass found 10 issues, and all are fixed in this version (§7b.8).
> - The xlsx will be rebuilt after you approve.

> ### Read this first (flags for approval)
> 1. **Why Step 7 failed, in one line.** Three things together sank it:
>    - We earned money only after something broke.
>    - We paid the shop on every job.
>    - Every cluster carried its own ₹23 L-a-year team.
>
>    A 20%-contribution service job cannot pay for that plus head office and expansion.
> 2. **The fix is five changes to the business model, not better pilot numbers.** Units per shop, capture, authorisation and technician pay are **unchanged**.
>    - **Keepwell Protect:** the shop sells our 2-year repair plan with the appliance.
>    - **Commission moves to Protect.**
>    - **Central parts buying.**
>    - **Partner clusters** run by existing service-centre owners from year 3.
>    - **60 shops per cluster** and a leaner head office.
> 3. **New BASE** (after the reviewer's fixes):
>    - year-7 revenue **₹130.5 Cr**, EBITDA **₹8.6 Cr (6.6%)**
>    - year 8: ₹181.6 Cr, 8.4%
>    - EBITDA-positive in **year 5**
>    - **peak funding need ₹5.8 Cr**
>    - a mature cluster earns **14–16% EBITDA**; breakeven is **22 shops**
>
>    Step 7 had 1% in year 7 and a ₹21.6 Cr peak.
> 4. **Why year 7–8 margins look modest:** the company is still opening 15–17 clusters a year, each at 25% output in its first year. **If the year-8 network were fully mature**, it would run at **₹249 Cr revenue and 13.4% EBITDA, with 9.1% from service alone** (no data revenue). This is the real health number for the service business.
> 5. **Customer plan money is ring-fenced.** Expected claims on unexpired plans sit in a reserve and are **not** used to fund the company. Without any plan cash at all, the peak need would be ₹11.7 Cr. With the reserve it is ₹5.8 Cr.
> 6. **Stress case** (5% attach, 45% claims, 25% parts margin, 50 shops per cluster, slower rollout): profitable from **year 6**, **peak need ₹8.9 Cr**. **LOW** (every pilot input at its worst) is never profitable and needs ₹58 Cr. So the money must come in **tranches with kill gates** (Step 8).
> 7. **NEW revenue line, Keepwell Protect: ₹10.2 Cr in year 7 (8% of revenue).**
>    - **Assumed:** 8% attach on covered appliances, and claims at 35% of the net price.
>    - **Evidence:** Indian buyers do buy plans at the counter (chains earn crores from them), and our own failure data supports the claims figure.
>    - **Gap:** there is **no published Indian attach rate**. This is the riskiest new number (§7b.3).
> 8. **⚠ Regulatory flag.** Protect is a **repairs-only service contract** that Keepwell fulfils itself. Vijay Sales VS+, Aditya Suraksha, Viveks and WeCare already sell their own plans this way. It is **not insurance** and has no accidental-damage cover. IRDAI's 2026 proposals target plans sold *as insurance*. **Verify with a lawyer before Step 10.**
> 9. **Approved steps that would change** (§7b.7):
>    - **Step 6:** add a Protect counter test [Story].
>    - **Step 4:** year-7 shops 1,950 → 3,300.
>    - **Step 3:** service centres become partners.
>    - **Step 2:** Kavyanth's network of 200+ service-centre owners becomes the partner pipeline.
> 10. **Toughest investor questions,** answered in §7b.6:
>     - "Why would a shop sell your plan at 25% when insurers pay 40–50%?"
>     - "What's the plan if Protect fails?"
>     - "What stops partners from cutting you out?"
>     - "Who pays claims if a cluster closes?"

---

## 7b.1 Diagnosis: where the Step 7 money went

One mature Step 7 cluster (50 shops):

| Revenue | Contribution | Cluster team | Cluster EBITDA |
|---|---|---|---|
| ₹1.85 Cr | ₹32.4 L (17.5%) | ₹22.8 L | **₹9.6 L (5.2%)** |

Head office (₹10.5 Cr in year 7), shop acquisition and set-up of new clusters used up more than all of it. The three structural reasons:

| # | Problem | Evidence |
|---|---|---|
| 1 | **We only earn after something breaks.** Revenue per shop is capped by the failure rate and our 11% capture | Shop revenue ₹3.5 L a year; repair lines run at 16–24% margin (Step 7 §7.2) |
| 2 | **We pay the shop on every job** (8% on repairs, 12% on AMC), though the shop does nothing after the hand-off | Commission is about ₹25k per shop a year, about a third of shop contribution |
| 3 | **Every cluster carries a full Keepwell team** (₹1.9 L a month) and an off-season pay floor (₹4.5 L a year), so expansion is slow and capital-heavy | Cluster fixed costs are 12% of cluster revenue; peak need ₹21.6 Cr |

## 7b.2 The five changes, and what each one buys

The levers are added one at a time to the corrected Step 7 BASE; pilot inputs are unchanged. "Peak (no plan cash)" assumes none of the customers' plan money is used at all.

| Lever added | Y7 revenue | Y7 EBITDA | Y8 EBITDA % | Peak need | Peak (no plan cash) | First positive year | Mature cluster EBITDA |
|---|---|---|---|---|---|---|---|
| 0. Corrected Step 7 BASE (check) | ₹81.5 Cr | ₹1.0 Cr (1.3%) | 3.5% | ₹21.6 Cr | ₹21.6 Cr | Y7 | 5% |
| 1. 60 shops per cluster | ₹91.5 Cr | ₹2.7 Cr (3.0%) | 5.0% | ₹17.5 Cr | ₹17.5 Cr | Y6 | 8% |
| 2. **Keepwell Protect** | ₹98.6 Cr | ₹3.8 Cr (3.9%) | 6.1% | **₹9.2 Cr** | ₹16.7 Cr | Y6 | 13% |
| 3. Commission moved to Protect | ₹98.6 Cr | ₹5.6 Cr (5.6%) | 7.8% | ₹7.3 Cr | ₹13.6 Cr | Y6 | 15% |
| 4. Central parts buying (20% → 30%) | ₹98.6 Cr | ₹6.4 Cr (6.4%) | 8.6% | ₹6.5 Cr | ₹12.3 Cr | Y5 | 16% |
| 5. Partner clusters from year 3 | ₹98.6 Cr | ₹5.1 Cr (5.2%) | 7.2% | ₹6.4 Cr | ₹12.4 Cr | Y6 | 16% own / 14% partner |
| 6. Faster rollout through partners (72 clusters by Y8) | ₹130.5 Cr | ₹6.7 Cr (5.1%) | 7.2% | ₹7.6 Cr | ₹15.0 Cr | Y6 | same |
| 7. Head office 0.85× (AI intake and dispatch) | **₹130.5 Cr** | **₹8.6 Cr (6.6%)** | **8.4%** | **₹5.8 Cr** | ₹11.7 Cr | **Y5** | same |

**How to read it:**
- **Protect, the commission change and parts buying** fix the margin. Together they take mature cluster EBITDA from 8% to 16%.
- **Partners do not raise margin.** Keepwell earns about ₹6 L less per partner cluster than per own cluster. What partners buy is **speed and less capital**: 66 partner clusters can open in 6 years without hiring 66 cluster teams. **That is what lifts year-7 revenue from ₹99 Cr to ₹130 Cr.**
- **Head office stays at 0.85×**, but it now **grows with the cluster count** (half fixed, half per cluster), so 72 clusters cost more than 52 would.

### Lever 1: Keepwell Protect, the plan the shop sells

**What it is.** A **repairs-only** plan for 2 years after the brand warranty ends. Parts and labour are covered, with the Keepwell guarantee. There is no free preventive check: checks stay a paid AMC service. The shop sells it at the counter on the same bill, and Keepwell fulfils every claim through its own network.

| Per plan (BASE) | ₹ |
|---|---|
| Price incl. GST, average across the four categories | 2,000 |
| Net of GST | 1,695 |
| Shop commission, 25% (paid and expensed at sale) | 424 |
| Repair claims at Keepwell's own delivery cost, 35% | 593 |
| Admin, processing and disputes, 5% | 85 |
| **Keepwell contribution** | **593 (35%)** |

**Volume.** The four covered categories are 75% of units sold. 74 units × 12 months × 75% × 8% attach gives **53 plans per shop a year**. Per mature shop that adds about ₹0.9 L of revenue and **₹32k of contribution**, against ₹85k from all core service.

**Accounting.**
- Nothing is delivered in the sale year (the brand warranty still applies). Revenue is therefore recognised **half in each of the 2 covered years**.
- Expected claims on unexpired plans (35% of unearned revenue) sit in a **ring-fenced reserve** and never fund operations.
- Covered repairs are no longer billed, so the lost repair revenue and margin are deducted from core.

### Lever 2: Commission moves from repairs to Protect

| Commission | Before | After |
|---|---|---|
| Repairs | 8% | **3%** |
| AMC | 12% | **8%** |
| Installs | 5% | 5% |
| Protect | — | **25%** |

**The shop earns more:** about ₹3,170 a month, against about ₹2,130 before (₹1,880 of it from Protect).

**Why it's right:** the shop is paid for the moment it controls (the sale), not for jobs it only passes on. Shops already earn well from plans: Electronics Mart booked about ₹12 Cr of plan revenue and about ₹4 Cr of profit in one quarter.

### Lever 3: Central parts buying (Supply phase)

**Change:** parts margin rises from 20% to 30% from a cluster's second year. Keepwell buys for all clusters from distributors and stocks fast-moving parts centrally.

### Lever 4: Partner clusters (asset-light growth from year 3)

**Who runs them.** The first 6 clusters (AP/TS) are Keepwell-run and prove the playbook. From year 3, new clusters are run by **existing brand service-centre owners**.

**Who does what:**

| Party | Role |
|---|---|
| **Partner** | Provides a local coordinator, premises, technicians and the off-season pay floor |
| **Keepwell** | Owns the shop agreements and the shop sales lead, the customer record, Protect, payment, the guarantee, parts supply, AI intake and dispatch, and quality audits |
| Revenue | Booked gross by Keepwell as principal, as now |

**Mature partner cluster, per year:**

| | Keepwell-run | Partner-run |
|---|---|---|
| Revenue | ₹2.72 Cr | ₹2.72 Cr |
| Keepwell's fixed cost | ₹22.8 L | **₹12.0 L** (₹1 L a month: shop sales lead, QC, local marketing) |
| Partner fee | — | **₹21.2 L** (10% of core revenue) |
| Off-season floor | Keepwell pays ₹4.5 L | Partner pays |
| **Keepwell EBITDA** | **₹44.3 L (16.3%)** | **₹38.4 L (14.1%)** |

**Why a service-centre owner says yes:**
- Its manager, premises and technicians already exist for brand work and sit idle off-season.
- From the ₹21.2 L fee, it pays a coordinator (about ₹4–6 L), the floor (₹4.5 L) and a share of premises (about ₹1.5 L), and keeps **about ₹9–11 L a year**. Its technicians also earn the per-job pay.
- In the opening year, Keepwell **guarantees a minimum fee of ₹8 L**, so the partner never loses money while the cluster ramps.

**Founder edge [Story].** Kavyanth's relationships with owners of 200+ service centres (Step 2) are the pipeline. 66 partners are needed by year 8.

**Brand-contract risk.** Some brand contracts limit multi-brand work. Partners take Keepwell jobs only for brands their contract allows. Other brands go to a second partner or to Keepwell's own technicians in that cluster. **Check this in the first 3 partner contracts** (tranche gate).

### Lever 5: 60 shops per cluster and a leaner head office

**60 shops per cluster.** This is between the 50 in Step 7 and the 65 in Option B. Every shop is counted (Step 4).

**Head office.** 0.85× the Step 7 headcount path, **scaled with the number of clusters** (₹13.2 Cr in year 8). AI intake, triage and dispatch (Step 5) slow the growth of care and dispatch headcount.

**Shop acquisition cost.** ₹14k blended in own clusters. **₹20k in partner clusters**, which are mostly outside the warm AP/TS network.

**Rollout and reach:**
- Clusters by year: 3 → 6 → 11 → 18 → 28 → 40 → 55 → 72 by year 8.
- Shops: **3,300 in year 7, 4,320 in year 8**.
- That is about **7% (year 7) to 10% (year 8)** of India's ~45k independent shops (Step 4). About 2,000 are in the south; the rest are partner clusters in the west.

## 7b.3 Evidence behind every new input

| Input | BASE (stress) | Basis | Tag |
|---|---|---|---|
| Protect price, average | ₹2,000 | **Derived from market prices:**<br>• AC 2-year plan ₹3,299 on a ₹30–40k AC ([Onsitego, 2017 prices](https://onsitego.com/blog/protect-your-air-conditioner-with-an-extended-warranty))<br>• Whirlpool 1-year plan ₹3,399<br>• resQ 1-year AC plan listed at ₹3,699 ([Reliance Digital](https://www.reliancedigital.in/product/1-year-resq-care-plan-rcp-extended-warranty-air-conditioner-upto-rs-10000-9500830))<br>By category: AC ₹3,000, fridge ₹1,500, washing machine ₹1,400, purifier ₹900, which weights by mix to **₹2,040**. We price at ₹2,000, below 2017 metro prices | R / derived |
| Attach rate | 8% of covered units (5%) | **Evidence:**<br>• US attach is about 30% (39% for ovens) ([Warranty Week](https://www.warrantyweek.com/archive/ww20170309.html))<br>• Indian chains sell plans at scale: Electronics Mart about ₹12 Cr of plan revenue in a quarter; Aditya Suraksha "sale of services" ₹51.7 Cr in FY26, up from ₹27.9 Cr<br>**Our assumption:** **no Indian attach rate is published**, so we use about a quarter of the US rate. It ramps 40% → 75% → 100% over a cluster's first 3 years, on top of cluster maturity (a deliberately conservative double ramp) | **Assumption**, with research context |
| Claims cost | 35% (45%) of net price | **Derived from our own failure data:**<br>• Step 7 repair rates and tickets, weighted by mix, give about ₹534 of retail repairs per covered appliance-year<br>• × 2 years × 0.6 (younger appliances fail less; **this factor is an assumption**) = ₹640 retail<br>• At Keepwell's delivery cost (parts at cost, labour at 60% payout, plus rework, levy and per-job costs, about 0.83 of net), that is about ₹450, or **27% of net**<br>We carry **35%** for disputes, misuse and adverse selection. Without the 0.6 factor, claims would be about 45%, which is the stress case | Derived + assumption |
| Shop commission on Protect | 25% | US stores keep 50–70% ([Checkbook](https://www.checkbook.org/redirect/categoryID/1080)). We pay less because the shop also gets our service and liability relief. **This is a risk to attach**, so it is covered by the stress case | R |
| Protect as a service contract | — | Indian retailers already sell their own plans: Vijay Sales VS+ (up to 4 years), Viveks, WeCare, Aditya Suraksha. IRDAI's 2026 proposals concern plans sold as insurance | R |
| Claims reserve | 100% of expected claims on unearned plans | Prudence. Consumer protection may require it. Lawyer check in Step 10 | Assumption |
| Parts margin, centralised | 30% (25%) | Dealer and distributor parts margins of 15–40% (`research/supply_layers`) | R |
| Partner fee | 10% of core revenue + an ₹8 L opening-year floor | **Franchise-style service is the norm in Indian appliances:** IFB about 1,512 franchisees, Blue Star 2,100+ partners, LG 1,006 centres, Qdigi 200+ franchise centres. Mr. Appliance's royalty is 5–7% plus 2%, paid by the operator; here we pay the operator because we own the demand | R / assumption |
| Keepwell cost per partner cluster | ₹1 L a month | Shop sales lead, QC audits, local marketing | Assumption |
| Shop acquisition cost in partner clusters | ₹20k | Cold rate about ₹22k (Step 7 research) | R |
| Head office | 0.85× Step 7 path, scaled with clusters | AI intake and dispatch (Step 5) | Assumption |

## 7b.4 New BASE plan (year 1 = 2027)

| Year | Clusters (partner) | Shops | Revenue | of which Protect | Data lines | EBITDA | EBITDA % | Service-only EBITDA | Cash, cumulative | Claims reserve |
|---|---|---|---|---|---|---|---|---|---|---|
| Y1 | 3 (0) | 180 | ₹2.4 Cr | 0.0 | 0.0 | −₹1.1 Cr | −45% | −₹1.1 Cr | −₹1.0 Cr | 0.1 |
| Y2 | 6 (0) | 360 | ₹6.8 Cr | 0.2 | 0.0 | −₹1.5 Cr | −23% | −₹1.5 Cr | −₹2.7 Cr | 0.5 |
| Y3 | 11 (5) | 660 | ₹15.3 Cr | 0.7 | 0.2 | −₹1.9 Cr | −13% | −₹2.1 Cr | −₹4.5 Cr | 1.1 |
| Y4 | 18 (12) | 1,080 | ₹29.7 Cr | 1.8 | 0.9 | −₹1.4 Cr | −5% | −₹2.2 Cr | **−₹5.8 Cr (peak)** | 2.1 |
| Y5 | 28 (22) | 1,680 | ₹53.9 Cr | 3.6 | 3.9 | ₹0.6 Cr | 1% | −₹2.3 Cr | −₹5.0 Cr | 3.6 |
| Y6 | 40 (34) | 2,400 | ₹86.9 Cr | 6.3 | 7.1 | ₹4.1 Cr | 5% | −₹1.3 Cr | −₹0.4 Cr | 5.8 |
| Y7 | 55 (49) | 3,300 | **₹130.5 Cr** | 10.2 | 11.0 | **₹8.6 Cr** | **6.6%** | ₹0.3 Cr | +₹7.4 Cr | 8.6 |
| Y8 | 72 (66) | 4,320 | **₹181.6 Cr** | 15.4 | 16.2 | **₹15.3 Cr** | **8.4%** | ₹3.1 Cr | +₹20.3 Cr | 12.2 |

**The health check investors should use: the mature run-rate.** The table above is depressed by growth. In year 8, 17 new clusters are running at 25% output, and 15 more are at 60%. If the year-8 network of 6 own and 66 partner clusters were all mature:

| | Revenue | EBITDA | EBITDA % |
|---|---|---|---|
| **Whole network** | **₹249 Cr** | **₹33 Cr** | **13.4%** |
| Service only (no verification, leads or brand data contracts) | — | ₹21 Cr | **9.1%** |

**Service is a healthy business on its own; data is upside.**

**Exit check (year 7–8, Step 9 will set the multiple):**

| Year | Revenue at operator multiples (2.5–3×) | EBITDA cross-check | Mature run-rate cross-check |
|---|---|---|---|
| Y7 | ₹130.5 Cr → **₹325–390 Cr** | — | — |
| Y8 | ₹181.6 Cr → **₹455–545 Cr** | ₹15.3 Cr × 25 = ₹380 Cr | ₹33 Cr × 15 = ₹500 Cr |

## 7b.5 Scenarios

| | BASE | Stress (planning case) | LOW |
|---|---|---|---|
| **What changes** | Pilot inputs plus the five levers | Attach 5%, claims 45%, parts margin 25%, 50 shops per cluster, Step 7 rollout (52 clusters by Y8) | Every pilot input at LOW: 60 units, 8% capture, 30% authorisation, 15% leakage, 65% payout, head office 1.2×, data at 0.6×. Plus the stress Protect inputs. Rollout and density as in BASE |
| Y7 revenue | ₹130.5 Cr | ₹85.2 Cr | ₹79.8 Cr |
| Y7 EBITDA | ₹8.6 Cr (6.6%) | ₹4.0 Cr (4.7%) | −₹9.0 Cr |
| Y8 EBITDA | 8.4% | 6.8% | −8.0% |
| First positive year | Y5 | Y6 | never (to Y8) |
| Peak need | **₹5.8 Cr** | **₹8.9 Cr** | ₹57.7 Cr |
| Mature cluster EBITDA | 16% own / 14% partner | 11% / 10% | −5% / +1% |

**Reading:**
- **Stress** reaches profit with about ₹9 Cr.
- **LOW** means the pilot inputs were wrong. Nobody should fund that, so the round is released in **tranches**. Step 8 sizes these gates:
  - units per shop ≥ 65
  - Protect attach ≥ 5%
  - claims ≤ 45%
  - one partner cluster at breakeven
  - 3 partner contracts cleared for multi-brand work

## 7b.6 What this does to the story, and the hard questions

**Positioning is unchanged:** "the after-sale service arm of every small-town appliance shop". The story gains one line: ***the shop sells the promise; Keepwell keeps it.*** Protect turns the Step 1 closing line into a product with a price.

**Phases:** Serve → Supply → Know → Circulate. Protect sits in Serve, and partners scale Serve.

| Hard question | Answer |
|---|---|
| "Why would a shop sell your plan at 25% when insurers pay 40–50%?" | Independent small-town shops mostly have **no plan partner** (every plan partnership in our archived retail research sits with chains: Onsitego, OneAssist, Zopper). We also take the after-sale complaints off the shop. Its total Keepwell income rises from about ₹2,130 to about ₹3,170 a month. If attach stays low, the stress case (5%) still works |
| "What if Protect fails completely?" | The model without Protect is lever 1: profitable from year 6, but needing about ₹17.5 Cr. **That is why Protect attach is a tranche gate, not an assumption we bank** |
| "What stops partners from cutting you out?" | Keepwell holds the shop agreements, the Protect contracts, the customer payment, the guarantee and the appliance record. A partner who leaves takes its technicians but none of the demand. Partner contracts include non-solicit of Keepwell shops (Step 10) |
| "Who pays claims if a cluster closes?" | The ring-fenced reserve (₹8.6 Cr by year 7), plus another partner or Keepwell technicians nearby |
| "Your margins are thin for a startup." | They are services margins at the mature level: 14–16% per cluster and 13% for the whole network at maturity. They compare well with Urban Company's 17.7–21.7% contribution on net transaction value (00b). We are honest that this is an operator, valued at about 2.5–3× revenue |

## 7b.7 Changes needed in approved steps (only if you approve 7b)

| Step | Change |
|---|---|
| 2 Founders | Kavyanth's network of 200+ service-centre owners is named as the partner-cluster pipeline. Prathyusha's dealer network sells Protect into shops |
| 3 Ecosystem | Service centres move from "sub-contract" to **partner-cluster operator** (10% fee, ₹8 L opening floor). Add a plan-terms or legal advisor row (service contract, reserve) |
| 4 Market | SOM year 7 becomes about **3,300 shops and ₹130 Cr** (was 1,950 shops and ₹115 Cr). Add Protect to the market: covered units × attach × ₹2,000 |
| 5 Product | Add Protect to the job flows: sale → plan record → claim. North star unchanged |
| 6 Traction [Story] | Add a **Protect counter test in the last 8 weeks of the pilot** at 12 shops: about 6% attach on about 1,200 covered units, so 72 plans and ₹1.4 L sold; 0 claims so far (coverage starts after the brand warranty). **Applied.** |
| 7 | Rebuild `keepwell_model.xlsx` on `plan_v3`; 7b replaces §7.6 |
| 00b / 00c | Replace the old 8-year stack and the "10–12% from service alone" line with this plan and the mature run-rate |

## 7b.8 What the independent review changed

| Finding | Fix | Effect on Y7 EBITDA / peak |
|---|---|---|
| A free preventive check was promised but not costed | Removed from Protect; checks stay paid AMC | Avoided a −₹6 Cr hit |
| Protect revenue was booked in the sale year | Now recognised over the 2 covered years | Lower; first positive year Y4 → Y5 |
| Peak need relied on spending customer plan cash | Ring-fenced claims reserve; peak shown with and without plan cash | Peak ₹2.6 Cr → ₹5.8 Cr |
| Attach was applied to all units, not just the 4 covered categories | Applied to covered units only (75%) | Lower |
| Head office was not grown with 72 clusters; partner-cluster shop cost was too low | Head office scales with clusters; shop cost ₹20k in partner clusters | Lower |
| The partner cluster team was under-costed, and the partner lost money in its first year | Keepwell's cost per partner cluster ₹1 L a month; ₹8 L opening floor | Lower |
| LOW ignored the head-office and data multipliers | Applied | LOW peak ₹17 Cr → ₹58 Cr |
| Claims derivation assumed parts at a margin | Re-derived at cost plus per-job costs (27%); 35% kept | — |
| Lost repair revenue was left in core revenue | Deducted | Small |

**Net effect of the review:**

| | Before review | After review |
|---|---|---|
| Y7 EBITDA | ₹14.5 Cr (10.6%) | **₹8.6 Cr (6.6%)** |
| Peak need | ₹2.6 Cr | **₹5.8 Cr** |

I am showing the corrected numbers, not the flattering ones.

## Decisions to approve (Step 7b)

1. **The five levers**, especially **Keepwell Protect as a repairs-only service contract, with claims reserved**.
2. **The new BASE** (₹130.5 Cr and 6.6% in year 7; 13.4% at mature run-rate; peak ₹5.8 Cr), with the **stress case (peak ₹8.9 Cr) as the planning case for Step 8**.
3. **The changes to Steps 2–6** in §7b.7, including the Protect test in the pilot story.
