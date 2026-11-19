# Step 7c: The financial model, simplified

**Phase C (the money). Status: FINAL (19 Nov 2026). This replaces the numbers in Steps 7 and 7b.**

- **Model:** `keepwell_model.xlsx` (141 formulas, 0 errors), built by `model/build_model_v4.py` from `model/simple_model.py`.
- **Check:** `model/verify_model_v4.py` finds **0 mismatches**.
- **One unit drives everything: the active retailer.**

## 7c.1 Four lines that link the whole story

| Level | The number | What it means |
|---|---|---|
| **One job** | ₹1,625 average bill, net of GST; 26% contribution ≈ **₹420** | After technician pay, parts cost, the retailer's commission and per-job costs |
| **One retailer** | 12 jobs a month = **₹19,500 revenue, ₹5,070 contribution a month** (pilot) | Grows to ₹30,000 revenue at 32% as Protect, AMC renewals and parts build (2031) |
| **One cluster** | team cost **₹1.0 L a month** (pilot) | **20 retailers pay for it.** A mature cluster of 60 retailers: ₹2.16 Cr revenue, ₹69 L contribution, ₹18 L team, **₹51 L EBITDA (24%)** |
| **The company** | clusters × retailers, minus head office | **EBITDA positive from year 1** |

## 7c.1b One retailer's month, opened up (deck slide 6; xlsx Unit sheet rows 14–40)

| The 12 jobs behind ₹19,500 (one retailer, a month) | Jobs | ₹ each, net of GST | ₹ a month | Why this price (market reference) |
|---|---|---|---|---|
| AC installation, authorised | 4 | 2,600 | 10,400 | The brand's own price. LG's charter: ₹1,199 fee (Keepwell keeps ₹800, the service centre the rest), bracket ₹750, copper ₹1,050 a metre. Same price, done in 24 hours instead of 2–5 days |
| Other installation: washing machine, fridge, purifier | 2 | 300 | 600 | The market rate. Low margin, but it starts the appliance record |
| Service visit, labour only (e.g. a washing-machine check) | 1 | 300 | 300 | Matches the local mechanic, below the ₹500–900 basic service of Urban Company and LG. Price is never the reason to leave |
| Repair with a part: capacitor, fan motor, gas top-up, PCB | 3 | 2,000 | 6,000 | About ₹2,360 with GST, averaged across part types on Urban Company's rate card (capacitor ₹599–749, fan motor ₹2,299, gas ₹3,000, PCB ₹1,500–4,500). Genuine part and a 90-day guarantee |
| AMC, 2 AC services a year | 2 | 1,100 | 2,200 | ₹1,299 with GST, the top of Urban Company's ₹1,098–1,298; adds the record and reminders |
| **Total** | **12** | **average 1,625** | **19,500** | **₹1,625 is the average of the mix, not a price.** A third of the jobs are AC installs with materials, which lifts the average above the ₹300 jobs |

**Protect is not in the pilot month.** It was sold only in the pilot's last 8 weeks (72 plans) and is booked over its 2-year term, so it enters from year 1. Protect sells at ₹2,000 with GST (₹1,700 net) for 2 years; Croma ZipCare charges ₹1,139–2,499 for 1 year.

**The pricing rule:** Keepwell charges the market rate on every job and wins on speed, the guarantee and the record, not on price.


| Pilot | ₹ | Year 5 | ₹ |
|---|---|---|---|
| Revenue (12 jobs × ₹1,625) | 19,500 | Pilot revenue | 19,500 |
| − Technicians (≈ ₹400 a job; Step 6: ₹330–500) | 4,900 | + Protect (2 plans × ₹1,700 net) | 3,400 |
| − Parts | 6,400 | + AMC renewals (1 × ₹1,100 net) | 1,100 |
| − Retailer commission (5/8/12/25% by job) | 1,320 | + Repairs on the installed base (3 × ₹2,000) | 6,000 |
| − Travel, payments, AI desk, guarantee reserve | 1,810 | = Revenue | 30,000 |
| **= Contribution (26%)** | **5,070** | **Contribution at 32%** | **9,600** |

Cluster month: pilot October 34 × ₹5,070 − ₹1.0 L = **+₹0.72 L**; mature 60 × ₹9,600 − ₹1.5 L = **+₹4.26 L** (₹51 L a year; breakeven 16).

## 7c.2 The pilot (one cluster, Vijayawada–Guntur, March–October 2026)

The pilot uses the same unit: ₹19,500 revenue per active retailer a month, 26% contribution, and a ₹1.0 L-a-month cluster team.

| Month | Active retailers | Revenue (₹ L) | Contribution (₹ L) | Team (₹ L) | Cluster EBITDA (₹ L) |
|---|---|---|---|---|---|
| Mar | 12 | 2.34 | 0.61 | 1.00 | −0.39 |
| Apr | 15 | 2.93 | 0.76 | 1.00 | −0.24 |
| May | 20 | 3.90 | 1.01 | 1.00 | **+0.01** |
| Jun | 24 | 4.68 | 1.22 | 1.00 | +0.22 |
| Jul | 28 | 5.46 | 1.42 | 1.00 | +0.42 |
| Aug | 30 | 5.85 | 1.52 | 1.00 | +0.52 |
| Sep | 32 | 6.24 | 1.62 | 1.00 | +0.62 |
| Oct | 34 | 6.63 | 1.72 | 1.00 | +0.72 |
| **Total** | 34 retailers | **38.0** | **9.9 (26%)** | **8.0** | **+1.9** |

All six traction numbers are 8-month totals for one cluster:
- 34 retailers on 2-year exclusive agreements
- 2,340 jobs (195 retailer-months × 12)
- ₹38 L revenue
- ₹9.9 L contribution
- +₹1.9 L cluster profit
- 6% Protect attach in a 12-retailer counter test

**Together they say one thing:** the cluster paid for itself from 20 retailers (May), and made ₹0.72 L a month by October.

## 7c.3 The 5-year plan (year 1 = April 2027–March 2028, from the close)

| | 2027 | 2028 | 2029 | 2030 | 2031 |
|---|---|---|---|---|---|
| Retailers (end of year) | 200 | 500 | 1,000 | 1,800 | 3,000 |
| Clusters (end of year) | 4 | 9 | 18 | 30 | 50 |
| Revenue per retailer per year | ₹3.0 L | ₹3.2 L | ₹3.4 L | ₹3.5 L | ₹3.6 L |
| Contribution margin | 28% | 29% | 30% | 31% | 32% |
| **Revenue** | **₹3.5 Cr** | **₹11.2 Cr** | **₹25.5 Cr** | **₹49.0 Cr** | **₹86.4 Cr** |
| Contribution | ₹0.98 Cr | ₹3.25 Cr | ₹7.65 Cr | ₹15.2 Cr | ₹27.6 Cr |
| Cluster teams (₹18 L per cluster-year) | ₹0.45 Cr | ₹1.17 Cr | ₹2.43 Cr | ₹4.32 Cr | ₹7.20 Cr |
| Head office | ₹0.40 Cr | ₹0.80 Cr | ₹1.50 Cr | ₹2.50 Cr | ₹3.50 Cr |
| **EBITDA** | **+₹0.13 Cr (4%)** | **+₹1.28 Cr (11%)** | **+₹3.72 Cr (15%)** | **+₹8.37 Cr (17%)** | **+₹16.95 Cr (20%)** |
| Cluster launches (₹20 L each) | ₹0.60 Cr | ₹1.00 Cr | ₹1.80 Cr | ₹2.40 Cr | ₹4.00 Cr |
| Working capital (10% of revenue growth) | ₹0.27 Cr | ₹0.77 Cr | ₹1.43 Cr | ₹2.35 Cr | ₹3.74 Cr |
| Tax (25% of EBITDA) | ₹0.03 Cr | ₹0.32 Cr | ₹0.93 Cr | ₹2.09 Cr | ₹4.24 Cr |
| Cash flow | −₹0.77 Cr | −₹0.81 Cr | −₹0.44 Cr | +₹1.53 Cr | +₹4.97 Cr |
| Cumulative cash | −₹0.75 Cr | −₹1.56 Cr | **−₹2.00 Cr (peak)** | −₹0.47 Cr | +₹4.50 Cr |

**Why EBITDA is positive from year 1:**
- **Revenue per retailer is ₹25,000 a month in year 1, up from the pilot's ₹19,500.** Protect is sold from day one in every new retailer (the pilot added it only in its last 8 weeks), and the pilot's customers start AMC renewals. A full cluster team costs ₹1.5 L a month, so at ₹7,000 contribution per retailer, breakeven is about 22 retailers.
- **The pilot cluster is already profitable.**
- **Each new cluster is opened through warm networks**, which cuts the cost of signing a retailer from ₹22k to ₹9.5k. The field executive who signs retailers is inside the cluster team cost.
- **Head office is lean in year 1:** the founders, 2 engineers and a finance lead; the AI desk keeps dispatch staff low.

**Why we still raise money:** opening a cluster costs ₹20 L before it earns. That covers set-up, parts stock, onboarding and training. Working capital also grows with revenue. These are balance-sheet uses, not losses. The plan's peak cash need is **₹2.0 Cr** (March 2030), and from then on growth pays for itself.

## 7c.4 Conservative case

The conservative case assumes:
- revenue per retailer 10% lower
- contribution margin 2 points lower
- clusters opened 25% more slowly
- head office 15% smaller

| | 2027 | 2028 | 2029 | 2030 | 2031 |
|---|---|---|---|---|---|
| Revenue | ₹2.5 Cr | ₹7.2 Cr | ₹16.1 Cr | ₹30.9 Cr | ₹54.4 Cr |
| EBITDA | breakeven (−₹0.05 Cr) | +₹0.45 Cr | +₹1.6 Cr | +₹3.9 Cr | +₹8.3 Cr |

The peak cash need rises to ₹2.6 Cr: the ₹0.5 Cr buffer plus delaying two cluster launches by a quarter keep it within the ₹2.5 Cr seed. The case is in `simple_model.py` (`conservative()`).

## 7c.5 What changed from Steps 7 and 7b, and why

- **One unit instead of many lines.** Earlier models added 20 job lines, 6 layers and 4 scenarios. Investors could not tie the pilot to the plan, so this model drives everything from the active retailer.
- **The pilot is restated on the same unit,** so every traction number ties to the next one: retailers × ₹19,500 = revenue; × 26% = contribution; − team = cluster profit.
- **The plan is 5 years from the close, not 8,** and EBITDA is positive every year.

The layers in Step 7b (partner clusters, parts, verification, refurbishing) appear in the plan only through the rise in revenue per retailer, from ₹19,500 to ₹30,000 a month. Everything else is upside.
