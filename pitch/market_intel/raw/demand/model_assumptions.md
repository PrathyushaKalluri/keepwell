# Demand model: assumptions, worked example and sanity checks

Prepared 18 Nov 2026. Parameter values, labels and URLs are in `parameters.csv`; ownership rates are in `ownership_by_state.csv`; team numbers are in `team_evidence_extract.md`; sources are in `demand_sources.csv`.
Labels: FACT / SOURCE-BACKED PROXY / ASSUMPTION / DERIVED ESTIMATE. LOW/HIGH results below are **corner cases** (every input set to LOW or to HIGH together), so the true range is narrower than LOW–HIGH.

## 1. Formula chain (per city, per category)

```
owning_HH          = urban_HH(city) x ownership_rate(state, urban, category) x tier_index
machines           = owning_HH x machines_per_owning_HH
oow_in_use         = machines x share_out_of_comprehensive_warranty x share_still_in_use
repair_events      = oow_in_use x repair_incidence            (+ AC: x refrigerant_refill_incidence)
service_events     = oow_in_use x routine_service_frequency   (AC wash, RO filter/service)
jobs_by_channel    = (repair_events + service_events) x channel_share[channel]
value (Rs)         = sum(events x average_bill[event type])
addressable_jobs   = jobs_by_channel[independent_local + dealer_arranged (+ part of brand ASC)]
```

Notes on the chain:
- **Routine service is not covered by warranty.** AC washes and RO filter changes are paid even on in-warranty units. Applying `share_out_of_warranty` to service events (as the chain above does) understates service demand by 10–20%. For a service-led model, apply service frequency to *all* in-use machines.
- **Compressor/motor cover (5–10 years, parts only)** means a unit can be "out of comprehensive warranty" but still get a free part. The labour and gas are still billed (Samsung and Daikin terms), so these jobs are still paid jobs for a technician.
- **Ownership surveys measure possession.** `share_still_in_use` (0.95–1.0) is a small correction only.
- **Room-AC stock is not all residential.** See conflict C1 below. Do not size household AC demand from sales or stock numbers.

## 2. Parameter strength

**Strongest** (FACT, large-sample or audited):
1. Ownership rates by state: NFHS-5 state reports, with urban and rural shown separately. The data is from 2019–21, so it understates 2026 levels. The CLASP–BEE 2024 survey is the update.
2. The AC service channel split: LocalCircles, Apr 2026, n = 13,487 across 289 districts, 56% of them Tier 2–4. Brand 24%, dealer-arranged 13%, local technician 44%, platform 13%.
3. Platform unit economics: the Urban Company Q2 FY27 shareholder letter, which is audited-grade disclosure. UC fee 28.6% of partner gross; partner net in hand ₹30,708 a month (49% of gross) for 97 hours; travel ₹2,863 a month; support and refunds 3.2% of NTV; marketing 2.7% of NTV.
4. Warranty structure: 1 year comprehensive; 5–10 year parts-only compressor or motor cover, with labour and gas charged.
5. AC price points: Urban Company price list, and iFOREST's ₹2,300 refill cost.

**Weakest** (ASSUMPTION or thin proxy):
1. **Repair incidence per machine-year** for fridges, washing machines, purifiers and non-gas AC faults. No Indian failure-rate survey was found, so these values are anchored on US SquareTrade figures with an uplift. This has the largest effect on the output.
2. **Agency volume.** Covers jobs per technician per day, technicians per agency, and jobs per agency per month. The inputs are the CEEW technician survey (200–800 AC units a year, active 4–6 months), UC orders per partner (about 43 a month across all categories) and two team opinions (n = 2). The pitch's "3 jobs a day" is illustrative only and was not used.
3. **Retailer extended-warranty commission and attach rate.** No India-specific figure was found. The 25/40/60% range comes from US retail (stores keep 50–70%; providers suggest about 50% dealer margin) plus one Indian anecdote of a 25% price gap.

Also weak: refrigerator annual unit sales (no CEAMA or ICRA figure); the Tier 2/3 share of urban households, which depends on how tiers are defined; urban household size (the urban HCES figure was not fetched); and the technician payout share at agencies or ASCs.

## 3. Worked example: urban India, Tier 2/3 only

Inputs (from `parameters.csv`, LOW / BASE / HIGH):
- Urban HH: 125 / 135 / 143 mn. This is 535 mn urban population divided by 3.8–4.17 persons per household.
- Tier 2/3 share: 40% / 47% / 60%. That gives **50.0 / 63.4 / 85.8 mn Tier 2/3 households**.
- Tier index on the national urban rate: 0.70 / 0.85 / 1.0.

### Air conditioners
| Step | LOW | BASE | HIGH |
|---|---|---|---|
| National urban AC ownership (AC only) | 15% | 17% (CLASP–BEE 2024) | 20% |
| AC-owning Tier 2/3 HH | 5.25 mn | 9.17 mn | 17.2 mn |
| ACs per owning HH | 1.13 | 1.2 | 1.4 |
| Share out of warranty x in use | 0.80 x 0.95 | 0.85 x 0.98 | 0.90 x 1.0 |
| **OOW ACs in use** | **4.5 mn** | **9.2 mn** | **21.6 mn** |
| Gas refills (0.30 / 0.40 / 0.50 per AC-year) | 1.35 mn | 3.67 mn | 10.8 mn |
| Other repairs (0.10 / 0.15 / 0.25) | 0.45 mn | 1.37 mn | 5.4 mn |
| Routine services (0.6 / 1.0 / 1.5) | 2.7 mn | 9.2 mn | 32.4 mn |
| **Total paid jobs per year** | **4.5 mn** | **14.2 mn** | **48.7 mn** |
| Value (refill ₹1.5k/2.3k/3k; repair ₹600/1.5k/4.5k; service ₹449/550/900) | ₹351 Cr | **₹1,553 Cr** | ₹8,595 Cr |

At BASE, about 1.2 events per out-of-warranty AC per year. Applying the LocalCircles split, the local-technician and dealer-arranged channels (57%) take about **8.1 mn jobs a year (about ₹885 Cr)**. Brand service takes about 3.4 mn and platforms about 1.8 mn.

### Washing machines
| Step | LOW | BASE | HIGH |
|---|---|---|---|
| National urban WM ownership | 29% (CLASP) | 36% (NFHS-5 urban 36.1%) | 40.4% (HCES 2023-24, unverified snippet) |
| WM-owning Tier 2/3 HH | 10.2 mn | 19.4 mn | 34.7 mn |
| Units per HH / OOW / in use | 1.0 / 0.75 / 0.95 | 1.0 / 0.82 / 0.98 | 1.02 / 0.86 / 1.0 |
| **OOW WMs in use** | **7.2 mn** | **15.6 mn** | **30.4 mn** |
| Repairs (0.08 / 0.12 / 0.18) | 0.58 mn | 1.87 mn | 5.5 mn |
| Services (0 / 0.05 / 0.2) | 0 | 0.78 mn | 6.1 mn |
| **Total paid jobs per year** | **0.58 mn** | **2.65 mn** | **11.6 mn** |
| Value (repair ₹500/1.2k/3k; service ₹199/199/299) | ₹29 Cr | **₹240 Cr** | ₹1,824 Cr |

The BASE takeaway is that the Tier 2/3 AC base produces about 5x the washing-machine job count and 6x the value, because ACs get gas refills and an annual wash. The washing-machine job count depends almost entirely on the repair-incidence assumption.

## 4. Sanity checks and conflicts

**C1. AC stock vs household ownership (major conflict).** The RAC installed stock is about 66 mn (CEEW, 2022-23) to about 82 mn (implied by iFOREST, 2024-25), and ICRA puts annual sales at 12.5–13 mn. Household ownership gives far fewer units: 17% of 135 mn urban HH plus 4% of about 200 mn rural HH is about 31 mn HH, or about 37 mn residential ACs at 1.2 per HH. The gap of roughly 30–45 mn units must be commercial (shops, offices, clinics), undercounting in CLASP (n = 4,321), or both. **Implication:** do not size household AC demand from sales or stock. Shops and small offices in Tier 2/3 towns are probably an additional AC servicing pool, which is an upside to test.

**C2. iFOREST refill spend vs the AC market-research size.** iFOREST estimates consumers spend about ₹7,000 Cr a year on refills (2024). Our check gives 82 mn ACs x 0.40 x ₹2,300 = ₹7,544 Cr, which is consistent. But Credence sizes the whole Indian AC servicing market at USD 654.6 mn (about ₹5,500 Cr) for 2025, *less than refills alone*. One of the two definitions is off. We trust iFOREST more, because it is primary survey-based, though its 7-city sample skews to metros.

**C3. BlueWeave appliance repair market.** BlueWeave puts it at USD 980.7 mn for 2023 (about ₹8,100 Cr), all categories, all India. Our Tier 2/3 urban BASE for ACs plus washing machines alone is about ₹1,800 Cr. Scaled to all urban India (÷0.47 and the tier index) that is about ₹4,500 Cr, before fridges, purifiers and rural demand. This is the same order of magnitude, so BlueWeave is plausible but at the low end once refills are counted in. The scope of BlueWeave's figure is not verified.

**C4. Redseer / Urban Company RHP.** Redseer puts total home services at ₹5.1–5.2 trn (FY25), with online penetration below 1% of NTV. IIFL cites appliance repair as about 2% of UC's serviceable market. 2% of ₹5.1 trn is about ₹10,000 Cr, which is consistent with C2 and C3 at around ₹8–10k Cr nationally for appliance repair. The Redseer appliances and repair category figure itself was not found in public excerpts; it should be pulled from the RHP's industry chapter.

**C5. Ownership data vintage.** For urban refrigerators, NFHS-5 (2019-21) gives 63.4% and CLASP 2024 gives 76%. For urban washing machines, NFHS-5 gives 36.1%, CLASP gives 29% and HCES 2023-24 (secondary) gives 40.4%. The CLASP washing-machine figure is *lower* than NFHS-5 even though it is three years newer, which points to sample effects in CLASP. The BASE uses NFHS-5 for washing machines and CLASP for ACs, because NFHS-5 combines AC and cooler (39.5% urban).

**C6. Stock vs sales for fridges and washing machines.** About 160 mn fridge-owning HH divided by about 14.5 mn sales a year gives an implied 11-year replacement cycle. That is consistent with a 10–15 year lifespan once first-time buyers are included. About 60 mn washing-machine HH divided by 9.6 mn sales gives about 6 years, which is shorter than the 10-year lifespan. Either first-purchase growth is strong (likely, since washing-machine penetration is rising fast) or the HCES-based stock is understated.

## 5. What to collect next (to close the weakest gaps)
1. Repair incidence: add a question to the team survey or a LocalCircles-style poll asking "how many paid repairs in the last 12 months, per appliance", with n of at least 200 in Tier 2/3.
2. Agency volumes: interview 5–10 Tier 2/3 agencies or ASCs for jobs per technician per day by month, technician pay model, and visit charge.
3. Retailer extended-warranty economics: interview 3–5 Croma, Reliance or local dealers on attach rate and the share of the plan price they keep.
