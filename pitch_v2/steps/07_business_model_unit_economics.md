# Step 7: Business model and unit economics

**Phase C (the money). Status: DRAFT for approval. ⚠ It contains a decision point (19 Nov 2026).**

> **Final numbers (19 Nov 2026):** the pilot, unit economics, plan and deal are restated in **Step 7c** (`07c_simple_model.md`) and Steps 8–9. Where this document's numbers differ, Step 7c is the reference.


> **Superseded in part (19 Nov 2026).** §7.4–7.7 record the corrected Step 7 BASE (year 7 ₹81.5 Cr, peak ₹21.6 Cr), which was **replaced by Step 7b**. Use 7b for every number.

> **Update after Step 7b (approved 19 Nov 2026).** **§7.6 is decided: the redesign in `07b_model_redesign.md` replaces options A/B/C.** `keepwell_model.xlsx` is rebuilt on `model/plan_v3.py`:
> - Builder: `build_model_v3.py`, with 680 formulas, 0 errors.
> - `verify_model_v3.py`: 0 mismatches in all four scenarios (LOW, BASE, HIGH, STRESS).
> - Scenario switch at `Inputs!C2`.
>
> §7.1–7.5 remain as the record of the corrected Step 7 BASE (lever 0 in 7b).


**Model:** `pitch_v2/keepwell_model.xlsx`
- Built by `model/build_model_v2.py`.
- LibreOffice recalculation: **680 formulas, 0 errors** (current model; the first Step 7 build had fewer).
- `model/verify_model.py` reports **0 mismatches** against the Python mirror `model/plan_core.py`.
- The scenario switch is at `Inputs!C2`.

**Builds on:** Steps 0–6 (approved). **Feeds:** Steps 8, 9 and 12.

> ### Read this first (flags for approval). This step changes earlier conclusions.
> 1. **An independent review of my first draft found real gaps, now fixed:**
>    - **Missing costs added:** tax (with loss carry-forward), payment fees, the cost of replacing shops that leave (10% a year), and a realistic head-office team built by headcount (₹1.0 Cr in year 1, rising to ₹13 Cr in year 8).
>    - **Double count removed:** the parts layer had counted our own jobs, which are already in core.
>    - **Plan-seller revenue added.**
>    - **Shop acquisition cost moved into EBITDA** (it is opex), and it is now a blended ₹14k, not the ₹9.5k warm-introduction cost. Our network only covers the first shops.
>    - **Slower cluster ramp:** 25% / 60% / 90% / 100% of mature output by year of operation.
>    - **Growth working capital added.**
>    - **Opening cash added:** ₹18 L.
> 2. **The result is much weaker than the Gate 1 plan:**
>
>    | | Gate 1 plan (00b) | Corrected BASE (50 shops per cluster) |
>    |---|---|---|
>    | Year-7 revenue | ₹115 Cr | **₹81.5 Cr** |
>    | Year-7 EBITDA | 7% | **1% (₹1.0 Cr)** |
>    | EBITDA-positive | Year 5 | **Year 7** |
>    | Peak funding need | ₹10.6 Cr | **₹21.6 Cr** (not cash-positive by year 8) |
>    | Mature cluster EBITDA | 10–12% | **5.2% at 50 shops** |
>    | Exit check | ₹330–480 Cr | **₹246 Cr (year 7) – ₹341 Cr (year 8)** |
>
> 3. **Why:** a cluster is profitable on its own (breakeven at 36 shops; +₹9.6 L a year at 50), but **head office, shop replacement and expansion use up all of it.** On core service alone, company EBITDA is negative every year (−₹10.7 Cr in year 7). The layers carry the company.
> 4. **The stress case** (60 units per shop, 8% capture, 30% authorisation, data layers at 60%) **never turns profitable**. It needs ₹44.6 Cr.
> 5. **⚠ Decision for you (§7.6).** Options:
>    - **A.** Pitch the corrected BASE as it is: thin margins, about ₹22 Cr over three rounds.
>    - **B (my recommendation).** A **density-first plan**: 65 shops per cluster, fewer and deeper clusters, a leaner head office (0.85×). Peak need **₹11.7 Cr**, EBITDA-positive in **year 6**, year-8 EBITDA 6%.
>    - **C.** Pause and look for a structurally higher-margin model before Steps 8–13.
> 6. **Hardest investor questions:**
>    - *"Core service loses money at company level; is this a parts and trade-in business?"* Each cluster earns on its own; head office is the cost of scale. Under plan B, density lifts cluster EBITDA to 8% and the company turns profitable in year 6.
>    - *"Why ₹12–22 Cr for a services company?"* Because each cluster takes about 3 years to mature. The money is released in tranches against density and authorisation gates (Step 8).
>    - *"Your stress case never works. What stops you burning the money?"* The tranche gates. If month-12 density or authorisation misses, expansion stops and we run the clusters we have for cash.

---

## 7.1 How we make money
| Line | Who pays | Contribution | Starts |
|---|---|---|---|
| Out-of-warranty service and repair (4 appliances) | Households | About 20% (the core) | Year 0 |
| Authorised installs (AC; washing machine) | Customer pays the brand rate through the service-centre sub-contract | ₹469 per AC install; ₹77 per washing machine | Year 0 |
| AMC (AC, water purifier) | Households, through the shop | ₹103 / ₹438 a plan | Year 0 |
| Plan-seller fulfilment | Plan sellers | About ₹150 on ₹700 revenue a job | Year 0 |
| Parts to *other* agencies (own-job parts are already in core) | Agencies | 10% | Year 2 |
| Trade-in field arm | Exchange operators and brands | 57% | Year 2 |
| E-waste feeder | Recyclers | 50% | Year 3 |
| Verified records | Brands and plan sellers | 80% | Year 3 |
| Leads and AMC renewals | Shops | 70% | Year 4 |
| Refurbished appliances (about half of clusters) | Budget buyers | 12% | Year 5 |
| Brand data contracts | Brands | 75% | Year 5 |

**Revenue recognition:** Keepwell is the principal, so revenue is booked gross under Ind AS 115 [R]. AMC is booked at sale in this model. The audited accounts will spread it over the plan's term.

## 7.2 One mature shop, per year (pilot inputs)

**Total: about 350 jobs, ₹3.53 L revenue, ₹0.70 L contribution (20%).**

| Job | Jobs a year | Contribution per job |
|---|---|---|
| AC service | 108 | ₹112 |
| Gas refill | 37 | ₹346 |
| AC repair | 14 | ₹224 |
| Authorised AC install | 63 | ₹469 |
| AC AMC | 28 | ₹103 |
| Washing-machine install | 42 | ₹77 |
| Water-purifier service | 29 | ₹92–107 |
| Water-purifier AMC | 4.5 | ₹438 |
| Washing-machine and fridge repairs | 17 | ₹41–211 |

**Reconciling with Step 6:**
- **Step 6 (34-shop pilot):** ₹4.8k contribution per shop a month at full ramp, after the off-season floor top-up of about ₹42k a month for that cluster.
- **Here (mature 50-shop cluster):** about ₹5.4k per shop a month after the top-up and plan-seller jobs.

## 7.3 One mature cluster (50 shops), per year
| | ₹ |
|---|---|
| Revenue, incl. plan-seller jobs | 1.85 Cr |
| Cluster contribution, after the technician floor and plan-seller jobs | 32.4 L |
| Cluster fixed costs (₹1.9 L a month) | (22.8 L) |
| **Cluster EBITDA** | **9.6 L (5.2%)** |
| Breakeven | **36 shops** |
| At 65 shops | about ₹20 L (8%) |

**Correction to 00c:** 00c's 10–12% from service alone needs 60–70 shops plus pooled parts and a guarantee premium. **At 50 shops it is about 5%.**

## 7.4 Corrected BASE plan (50 shops per cluster; year 1 = 2027)
| | Y1 | Y2 | Y3 | Y4 | Y5 | Y6 | **Y7** | Y8 |
|---|---|---|---|---|---|---|---|---|
| Clusters (end of year) | 3 | 5 | 9 | 14 | 21 | 30 | **40** | 52 |
| Shops | 150 | 250 | 450 | 700 | 1,050 | 1,500 | **2,000** | 2,600 |
| **Revenue (₹ Cr)** | 2.0 | 5.2 | 10.8 | 19.8 | 35.0 | 55.3 | **81.5** | 111.4 |
| Core service | 1.9 | 4.6 | 8.8 | 14.9 | 23.6 | 35.2 | 49.8 | 67.3 |
| Data layers | 0 | 0 | 0.2 | 0.8 | 3.3 | 6.1 | 9.4 | 14.0 |
| Contribution margin | 18% | 19% | 21% | 22% | 25% | 26% | 26% | 26% |
| Head office (₹ Cr) | 1.0 | 1.6 | 2.6 | 4.0 | 6.0 | 8.0 | 10.5 | 13.0 |
| Shop acquisition (₹ Cr) | 0.15 | 0.16 | 0.32 | 0.41 | 0.59 | 0.78 | 0.91 | 1.12 |
| **EBITDA (₹ Cr)** | −1.3 | −1.7 | −2.4 | −2.8 | −2.0 | −0.8 | **+1.0** | +3.9 |
| Core-only EBITDA (₹ Cr) | −1.3 | −1.9 | −3.0 | −4.4 | −6.5 | −8.4 | −10.7 | −12.8 |
| Cumulative cash (₹ Cr) | −1.3 | −3.6 | −7.0 | −11.2 | −15.4 | −19.0 | −21.5 | **−21.6** |

**Peak need ₹21.6 Cr. Exit check ₹246 Cr (year 7) to ₹341 Cr (year 8).**

## 7.5 Scenarios and drivers
| Case | Year-7 revenue | Year-7 EBITDA | Peak need | Breakeven shops |
|---|---|---|---|---|
| LOW (everything bad together) | ₹47 Cr | −₹13 Cr | ₹79 Cr | 157 |
| Stress (4 realistic misses) | ₹59 Cr | −₹5.4 Cr | ₹44.6 Cr | 59 |
| **Corrected BASE** | **₹81.5 Cr** | **₹1.0 Cr** | **₹21.6 Cr** | **36** |
| HIGH (everything good together) | ₹149 Cr | ₹29 Cr | ₹0.3 Cr | 10 |

**Biggest one-at-a-time swings on year-7 EBITDA and peak need:**

| Driver moved to LOW | Year-7 EBITDA | Peak need |
|---|---|---|
| Data adoption | −₹1.8 Cr | ₹31 Cr |
| Head-office cost | −₹1.1 Cr | ₹31 Cr |
| Units per shop | −₹0.8 Cr | ₹28 Cr |
| Shops per cluster | −₹0.7 Cr | ₹28 Cr |
| Repair capture | −₹0.2 Cr | ₹26 Cr |
| Authorisation | −₹0.1 Cr | ₹26 Cr |

The full table is on the model's Sensitivity sheet.

## 7.6 ⚠ Decision: which plan do we take into Steps 8–13?
| Option | What changes | Peak need | EBITDA-positive | Year-8 revenue / EBITDA | Exit check (year 8) | Investor story |
|---|---|---|---|---|---|---|
| **A. Corrected BASE** | Nothing | ₹21.6 Cr (not cash-positive by year 8) | Year 7 | ₹111 Cr / 3% | ₹341 Cr | Thin. Hard to defend 3 rounds and about ₹22 Cr for a 3% margin |
| **B. Density-first (recommended)** | **65 shops per cluster**; clusters go 3 → 5 → 8 → 12 → 17 → 24 → **31** → 40 (2,015 shops in year 7, the same reach as Step 4); **head office 0.85×** | **₹11.7 Cr** | **Year 6** | ₹104.5 Cr / **6%** | ₹318 Cr | Deeper towns before more towns. Each cluster earns 8% at maturity. Stress case still needs ₹31 Cr, so it is tranche-gated |
| **C. Pause and rethink** | Look for a higher-margin structure before going on | — | — | — | — | Delays Steps 8–13 |

**Why B is credible:**
- **Density is where the evidence points.** It is the biggest driver in Steps 0, 4 and 7.
- **The shops exist.** 00c §4c serves every shop, and the Step 6 shop walk found 78 independents selling 30 or more units a month in our pilot belt alone.
- **Head office at 0.85× is still about 12% of revenue in year 7.**
- **What B costs:** a cluster takes longer to fill, and density must be proven in Vijayawada–Guntur first. That becomes **gate 1 of the round** (Step 8).

**What B does not fix:** it is still a 6% EBITDA operator by year 8, and the stress case needs about ₹31 Cr. The exit depends on the layers and density. We say that plainly.

## 7.7 The investor reading, said plainly
- **Unit economics work at cluster level:** about 20% contribution per shop, breakeven at 36 shops, 8% cluster EBITDA at 65 shops.
- **Company economics are thin** until the network is dense and the layers ramp. This is a **patient, operator-style business**, valued at about 2.5–3× revenue, not a SaaS one.
- **The case for investing** is three things together:
  - a large, unorganised after-sale pool (Step 4)
  - a channel no one else owns (independent shops)
  - the record that powers the high-margin data layers

---

## Decisions to approve (Step 7)
1. **The corrected model** (all review fixes) is the single source of truth: `keepwell_model.xlsx`.
2. **⚠ Choose A, B or C** (§7.6). **Recommended: B, density-first** (65 shops per cluster, 31 clusters in year 7, head office 0.85×). If you pick B, I'll set it as the BASE in the model and the documents.
3. **Corrections to earlier steps** (on your approval):
   - **00b:** replace the 8-year plan with this one.
   - **00c:** "10–12% from service alone" becomes **"about 5% at 50 shops, 8% at 65"**.
   - **Step 4:** SOM becomes **year-7 revenue about ₹78–82 Cr and about 2,000 shops**.
4. **The stress case is the planning case** for Step 8's tranches.

On approval, Step 8 (funding needs and the ask) comes next, sized on the plan you choose.
