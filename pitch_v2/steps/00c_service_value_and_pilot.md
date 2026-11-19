# Step 0c: Why the service business is valuable on its own, and where to pilot (Gate 1 follow-up)

> **Update after Step 7b (approved 20 Nov 2026).** The line "10–12% from service alone" is superseded. A mature cluster now earns 14–16% EBITDA (Step 7b). At the company level, the mature run-rate from service alone is 9.1%.

> **Illustrative case** for the IIIT Hyderabad ESFS course pitch. The research is real and sourced, and the model's assumptions are tagged.
>
> **For approval, together with `00_validation_report.md` and `00b_margin_and_vision.md`.**

The engine is `ue_v2.py` (`variant_G`). Every number below re-runs from it.

## 1. What "a healthy service business" means for Keepwell

Data layers are upside. On its own, the service business must meet five tests that an operator investor checks. Each has a benchmark:

| # | Test | Keepwell target | Benchmark | Status |
|---|---|---|---|---|
| 1 | **Every cluster pays for itself** | Cluster EBITDA-positive at about 30 shops, within 12–15 months of opening | — | Model: break-even at 30 shops (80 units each) |
| 2 | **Mature cluster earns a real margin** | **10–12% cluster EBITDA from service alone** | US HVAC independents earn 8–12% EBITDA and PE-run platforms 15–22%; HomeServe 17.2%; Urban Company India 5.3% of total job value | Model: 9–12% (see the build-up below) |
| 3 | **Revenue repeats** | 40%+ of a mature cluster's revenue from AMCs, repeat customers and appliances we installed | 82% of Urban Company's job value is from repeat users (FACT) | To prove in the pilot |
| 4 | **Capital comes back fast** | Opening a cluster costs about ₹20 L and pays back in under 24 months | — | Model: a mature cluster earns about ₹0.3–0.4 Cr a year |
| 5 | **Asset-light** | Partner technicians, no warehouses until parts volume justifies one | — | By design |

**How a mature cluster gets from 0% to about 12% on service alone** (60–70 shops, four appliances, 80 units a shop):

| Step | What changes | Cluster EBITDA |
|---|---|---|
| Year-1 cluster | 30 shops | 0% |
| Density | 50 shops (we serve every shop, not only the large ones) | 7% |
| Our own installed base | Appliances we install come back to us for service, so capture rises from 12% to 15% | 7% (revenue +12%) |
| AMC | Uptake rises from 3% to 5% a year | 8% |
| Route density | 3.2 jobs a technician a day instead of 2.8 | 8% |
| Mature team and size | Cluster team costs ₹1.9 L a month; 60 shops | 9% |
| Pooled parts buying | Parts margin rises from 20% to 30% | 10% |
| Guarantee premium | Guaranteed jobs are priced 8% higher | 11% |
| 70 shops | | **12%, about ₹0.4 Cr a year per cluster** |

**What the service business alone is worth at exit:**
- In year 7 (BASE), service and operations revenue is about **₹105 Cr**, and EBITDA from operations is about 6–8%.
- **At operator multiples of 2–3× revenue, that is about ₹210–315 Cr.**
- That is **without** any data layer. The data layers add about ₹70–100 Cr on top (00b §5).

**The message for investors:** *"Keepwell is a service business that is profitable by design. Each cluster breaks even at about 30 shops and earns 10–12% at maturity. That is the same range as good operators, and better than Urban Company's 5% today. Every job also builds the appliance record, which we sell to brands and retailers at 70–90% margin."*

**What we must not claim:** contribution well above 20% from service alone, or SaaS-like margins. Our gross margin is about 33–36%. We say we are moving "towards 40%", not that we are there.

## 2. Pilot location: the Vijayawada–Guntur belt (Andhra Pradesh)

**Decision:** pilot in **Vijayawada, with Guntur, Mangalagiri and Tenali in the same cluster**.
- **Second cluster and backup:** **Warangal–Hanamkonda–Kazipet** (Telangana).
- **Basis:** the model and `pitch/archive/market_intel/data/cities.csv`.
- **Location research (19 Nov):** `research/pilot_location/` scores 9 belts on 7 weighted factors. **Vijayawada–Guntur 76.0, Warangal 73.5, Nizamabad 65.0.** The research confirms the choice, but the lead is narrow. It also corrected three claims; the corrections are applied below.

| Belt | Households 2026 (est.) | Repair and service spend a year (BASE) | Chain stores found | Competitors checked (verified / claimed) | Distance from Hyderabad | State rules |
|---|---|---|---|---|---|---|
| **Vijayawada + Guntur + Tenali** (hub to satellites 25–35 km) | **about 8.1 L** | **about ₹31 Cr** | 10 (Bajaj Electronics) | 1/3 (Vijayawada), 1/2 (Guntur) | 275 km, about 5 h | AP: no *state* gig fee (the central Code on Social Security applies in both states); AP Startup Policy 4.0 grants ₹15–20 L + seed equity up to ₹50 L |
| Warangal tri-city (+ Karimnagar 70 km) | about 2.4 L (3.4 L with Karimnagar) | about ₹14 Cr (₹19.5 Cr) | 3 (5) | 1/1 | 145 km, about 3 h | TS: state gig fee of 1–2% of each payout (Act 21 of 2026) on top of the central Code; T-Hub / T-Fund |
| Visakhapatnam | about 6.1 L | about ₹23 Cr | 8 | 1/4 | 620 km | AP; one city, no satellites |
| Nellore | about 2.0 L | about ₹7.5 Cr | 1 | 1/1 | 460 km | AP |
| Kurnool / Rajahmundry–Kakinada / Khammam / Nizamabad | 0.85–3.2 L | ₹4.9–12.3 Cr | 2–4 | not checked | 200–470 km | |

**Why Vijayawada–Guntur:**
1. **Density decides viability (Step 0, sensitivity rank 1).** A cluster needs about 2,400 appliances sold a month across 50–70 shops to reach 10–12%. This belt has about 8 lakh households within 35 km of the hub, more than 3× the Warangal tri-city. It is the only belt where 50–70 independent shops in one cluster is realistic.
2. **The demand fits the products.**
   - It has a real AC season: the IMD May mean maximum is **40.2 °C**, the record is **48.8 °C**, and **4 months average 35 °C or more**. The belt has the **largest AC base of any candidate**, about **129k ACs and 186k AC jobs a year** [Model]. Its humidity is moderate (46% on May afternoons); the claim that it is "most humid" is corrected.
   - Saline groundwater in parts of Krishna and Guntur (CGWB) supports water-purifier service. District TDS medians are still UNKNOWN.
   - Incomes are strong: per-capita GDDP is **₹4.2 L in Krishna** and **₹3.6 L in NTR**, against ₹1.87 L in Hanumakonda (Warangal).
   - It has a technician pipeline: a JCH-Hitachi / APSSDC AC-training centre in Vijayawada, and the ITI refrigeration and AC trade.
   - Its large households support washing machines and fridges.
   - The detailed heat and TDS figures come from the location research.
3. **The independent shops are there.** Chains have about 10 stores across three cities (Bajaj Electronics). Everything else is independent, which is our customer. Bajaj's extended-warranty counters (Onsitego / OneAssist) don't serve independent shops.
4. **Andhra Pradesh is cheaper and gives more support.** AP has no *state* gig fee; Telangana adds 1–2% of payouts on top of the central Code, which applies in both states. AP Startup Policy 4.0 offers grants up to ₹15–20 L, seed equity up to ₹50 L and go-to-market support up to ₹50 L. The grants are non-dilutive money for the first round; the seed equity and go-to-market support are taken as equity.
5. **Competition is present for households and absent for shops.** Urban Company is live with AC prices in Vijayawada (from ₹799) and Guntur (from ₹699), and Eureka Forbes has 6 centres in Vijayawada. That proves households pay for service. **None of them serves the independent shop**, which is our customer and channel. This is the strongest argument against the belt. The Amaravati capital region adds new households.

**The strongest arguments against it:** households here already have Urban Company and Eureka Forbes, and the belt is 273 km away (3.6 h at free flow, about 5 h in practice) from the Hyderabad team.
- **Mitigation:** the CEO and the first cluster manager live in Vijayawada for the pilot.
- Hyderabad keeps only technology and HQ.

**Why Warangal is the second cluster, not the first:**
- **For it:** it is the hottest belt (Hanamkonda's May maximum is 41.6 °C). Telangana's urban AC/cooler ownership is 62.7%, against 36.2% in AP. It has no Urban Company AC page, it is a fluoride hotspot, and it is 2–3 h from Hyderabad.
- **Against it:** about 2.4 L households, and no town of 50k or more within 40 km (Karimnagar is 70 km away). Incomes are lower, and Telangana adds the state gig fee.
- **What would flip the decision:** a shop count showing 30–50 or more independents the tri-city can sign (from GST HSN data or a 2-day shop walk). That is worth doing before the cluster-2 decision.
- It becomes cluster 2 in month 7 to test a smaller-town format, with Karimnagar as a satellite.

**What the pilot must confirm in this belt (90 days):**
- At least 2,000 units a month across the signed shops.
- One AC brand authorising us, or a service-centre sub-contract, covering at least 30% of units.
- At least 50% of installs routed to us.
- At least ₹4k contribution per shop by month 4.
