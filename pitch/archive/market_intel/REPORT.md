> **ARCHIVED 19 Nov 2026.** Kept for reference; the conclusions are summarised in `../../RESEARCH_INSIGHTS.md`.

# Retailer-led post-warranty repair in Tier 2/3 India: research report

**Research date:** 18 Nov 2026.

**Status:** first full build.

- **Dashboard:** [`dashboard/index.html`](dashboard/index.html). It is a self-contained HTML file with 9 pages, an India choropleth and city maps. It needs an internet connection for map tiles.
- **Data:** [`data/`](data/), 10 CSV files.
- **Method:** [`METHODOLOGY.md`](METHODOLOGY.md).
- **Raw research:** [`raw/`](raw/), with each agent's log, sources and scripts.
- **Rebuild:** `python3 build_market_intel.py`.

**Open-data gap at the time of writing.** The OpenStreetMap pull of shops and repair businesses was still running when this was written; the public Overpass servers were timing out. Every "listed repair points" figure is therefore 0 in this build. As a result:
- No city can qualify as "HIGH OPPORTUNITY". That class needs at least 3 listed repair points.
- Repair supply is **unverified everywhere**.

When `raw/osm/osm_points.csv` lands, re-run the build. The supply map, the gap classes and the agency shortlist then fill in automatically.

---

## The answer in one paragraph

The opportunity is **real in size but not proven to be profitable**.

- **Demand is real.** Tier 2/3 cities hold an estimated **4.9 Cr out-of-warranty appliances**. They generate about **2.5 Cr paid service and repair requests a year, worth about ₹2,200 Cr** (BASE). The LOW–HIGH range is ₹560 Cr to ₹9,900 Cr.
- **The retailer channel is small and already partly occupied.** Only **about 13% of AC service jobs are arranged through the dealer** today (LocalCircles, n = 13,487). The regional chains that do sell after-sales already sell **extended warranties** through Onsitego, OneAssist or Zopper, or through their own schemes (Aditya Suraksha, Pittappillil Wecare). **We found no chain anywhere that refers paid, out-of-warranty repair jobs to local agencies.** No one is doing it, but no retailer has shown they want it either.
- **The unit economics are thin.**
  - **BASE:** contribution is about **₹56 per completed job**. Breaking even needs about **14,000 jobs a month, or about 1,100 active retailers**.
  - **LOW:** every job loses money.
  - **HIGH:** it works with about 40 retailers, but only if every input lands well together.

**Do not raise money on this model yet.** Run the 90-day pilot test in §7 first. The single number that decides the case is **paid repair referrals per retailer per month**. Nobody has measured it.

---

## 1. National findings

| Measure (core Tier 2/3, 449 cities) | LOW | **BASE** | HIGH |
|---|---|---|---|
| Installed ACs, refrigerators, washing machines and water purifiers | 4.1 Cr | **5.7 Cr** | 7.9 Cr |
| Out of warranty, still in use | 3.2 Cr | **4.9 Cr** | 7.1 Cr |
| Paid service + repair requests a year | 1.0 Cr | **2.5 Cr** | 6.0 Cr |
| Customer spend a year | ₹559 Cr | **₹2,209 Cr** | ₹9,924 Cr |
| Reachable through the retailer channel (13% dealer-arranged share) | ₹56 Cr | **₹287 Cr** | ₹1,489 Cr |

The LOW and HIGH columns set every input low or high at the same time, so the true range is narrower.

**Average bill:** ₹898 (BASE). AC jobs (service, gas refill, repair) are most of the value; water-purifier filter visits are most of the count.

**What the inputs rest on:**
- **Cities:** Census 2011 final tables. There are 80 Tier 2 cities (500k–3M) and 369 Tier 3 cities (100k–500k), plus 473 small towns (50k–100k) kept as a separate segment. Metro satellites are excluded, and so is double counting inside UAs.
- **Households in 2026:** each city's 2011 population is scaled by its state's projected urban growth (NCP Technical Group, 1 March 2026).
- **Ownership:** NFHS-5 state urban rates, scaled to the 2024 CLASP–BEE national survey. AC-only ownership is *derived* from NFHS-5's combined AC-or-cooler figure.
- **Weakest input:** repair incidence per machine-year. There is no Indian survey, so US SquareTrade figures are used as a proxy.

## 2. State rankings (the two rankings differ, as intended)

| Rank | A. Largest market (BASE spend a year) | B. Best for a startup pilot (entry score) |
|---|---|---|
| 1 | Uttar Pradesh, ₹339 Cr | Andhra Pradesh, 49.7 |
| 2 | Maharashtra, ₹204 Cr | Telangana, 47.0 |
| 3 | Kerala, ₹185 Cr | Kerala, 45.7 |
| 4 | Madhya Pradesh, ₹181 Cr | Tamil Nadu, 43.6 |
| 5 | Punjab, ₹153 Cr | Karnataka, 39.9 |
| 6 | Rajasthan, ₹142 Cr | Madhya Pradesh, 37.1 |

**Most eligible cities:**

| Definition | Ranking |
|---|---|
| Population (primary) | UP 61, then MP 33, Maharashtra 31, Tamil Nadu 31, Andhra Pradesh 31 |
| HRA Y/Z classification (alternative) | Same leaders, in a slightly different order |

See `states.csv`, columns `rank_count_pop_def` and `rank_count_hra_def`.

**Why the two rankings differ:**
- **UP and Maharashtra are big but thinly documented.** Data completeness is 0.04 for UP and 0.06 for Maharashtra.
- **The southern states have verified chain store networks and checked competitors.** Bajaj Electronics, Sathya, Girias, Vasanth, Pittappillil and Darling publish store locators.
- **Part of B reflects where evidence exists, not just where opportunity exists.** Read it as "where a pilot can be planned on evidence today."

## 3. City rankings (startup entry, default weights 25/25/20/15/15)

1. Indore (MP)
2. Raipur (CG)
3. Warangal (TS)
4. Bhopal (MP)
5. Visakhapatnam (AP)
6. Vijayawada (AP)
7. Thrissur (KL)
8. Kochi (KL)
9. Guntur (AP)
10. Karimnagar (TS)
11. Lucknow
12. Kanpur
13. Nellore
14. Nagpur
15. Madurai
16. Tiruchirappalli
17. Hubli–Dharwad
18. Coimbatore
19. Mysore
20. Mangalore

**The top 4 barely move under the other weightings.** Under demand-heavy, supply-heavy and equal weights, Indore, Raipur, Warangal and Bhopal stay in the top 4.

**Caveat:** the 30 cities whose competitors were checked by hand score higher on confidence. That is a selection effect.

**All top cities are "PROMISING BUT UNVERIFIED"** because repair supply is not yet verified (see the gap above). 318 of the 449 cities are "INSUFFICIENT DATA".

## 4. Retailer landscape

- **The chains:** 22 chains are profiled. 846 store-level rows come from 9 public store locators, and 585 city-level counts are matched to census cities.
- **Largest Tier 2/3 networks:**

  | Chain | Outlets | Note |
  |---|---|---|
  | Sathya | 427 | 94.5% in Tier II and below |
  | Bajaj Electronics / Electronics Mart | 210 | |
  | Aditya Vision | 207 | Bihar, UP, Jharkhand |
  | Girias | 187 | |
  | Darling | 174 | |
  | Vasanth & Co | 153 | |
  | Value Plus | 135 | |
  | Pittappillil | 82 | |

- **After-sales arrangements:** 8 of 22 chains have an extended-warranty partner or their own service arm. 13 are UNKNOWN. One, Oxygen, sends customers to the brand.
- **Retailers make money from extended warranties.** Electronics Mart made about ₹12 Cr of warranty revenue and about ₹4 Cr profit in one quarter (Q1 FY24 call). Retail commission on warranties is typically 25–60%.
- **Independent single-store retailers:** no count exists. The best proxy is LG's 30,726 distributors and sub-dealers.

## 5. Repair-agency landscape

- **Supply is not verified.** No business was contacted, so verified operating agencies and technician headcount are **UNKNOWN** everywhere, and the dashboard shows that.
- **Where the agency pool is:** 44% of AC service jobs go to independent local technicians, 24% to the brand, 13% to platforms and 13% are dealer-arranged (LocalCircles 2026).
- **Brands keep post-warranty service for themselves.** Eureka Forbes earns about 31% of its revenue from service, and LG runs 1,006 service centres.
- **Eureka Forbes has verified local partner centres in 27 of the 30 checked cities.**

## 6. Competition

**Already serving retailer-sourced customers:**
- Reliance **resQ** (Reliance Digital)
- **Jeeves** (Flipkart)
- **Croma ZipCare**
- **Onsitego** (Vijay Sales "VS+", Value Plus; it owns Qdigi)
- **Zopper** (logos of Sathya and Vasanth & Co)
- **OneAssist** (Electronics Mart, Value Plus)

All of them earn at the point of sale. A customer who never bought a plan falls outside their model.

**On the ground in Tier 2/3:**
- **Urban Company** has city price pages in 17 of 30 checked cities, but over 90% of its value comes from its top 10 cities.
- **Justdial** is the real channel to local agencies today.
- **Jeeves, Onsitego, Servify and Servsy** claim national coverage with no city list, so they count as "NOT VERIFIED", which is not the same as absent.

**Exits and pivots:**
- Housejoy moved to construction.
- Bigfix and SERVIZ moved to B2B services for brands.
- Taskbob, Doormint and Pync shut down.

**Verdict:** the niche is **partly served** (medium confidence). Nobody routes a regional chain's lapsed-warranty customers to local agencies for paid repairs. But the people best placed to copy it already sit at those chains' counters.

**What would stop Jeeves, Onsitego, Bigfix or Servify from copying it?** Very little. They already hold the retailer relationships, the partner networks and the software. The only defences would be exclusive retailer contracts or a data edge (the machine's record). Neither exists yet.

## 7. Business economics and the pilot

**Per completed job (BASE).** These figures come from the simulator on dashboard page 7; every input except the average bill and support cost is an ASSUMPTION.

| Line | ₹ |
|---|---|
| Average customer bill (GTV, not revenue) | 898 |
| Platform revenue: labour margin after paying the agency + parts margin + ₹49 booking fee | 227 |
| Retailer commission (8%), payment fees, refunds and rework, support, coordination | (171) |
| **Contribution per job** | **56** |
| Fixed costs per month | 8,00,000 |
| **Break-even** | **about 14,300 jobs a month ≈ 1,120 retailers** at 30 referrals × 50% booking × 85% completion |

**LOW:** contribution is −₹124 a job, so the model never breaks even.
**HIGH:** contribution is ₹400 a job, break-even is about 1,500 jobs a month with about 39 retailers.

**The result swings most on:**
1. Referrals per retailer.
2. The share of the bill the agency keeps.
3. The booking fee.

**Pilot recommendation (prospecting candidates, not partners):**
- **Two states: Andhra Pradesh and Telangana.**
  - They score best on entry.
  - Bajaj Electronics publishes its full store list (108 stores in Telangana, 70 in Andhra Pradesh).
  - Sathya has 65 stores in Andhra Pradesh.
  - The team is based in Hyderabad.
- **Five cities: Warangal, Vijayawada, Visakhapatnam, Guntur and Karimnagar.**
  - Indore, Raipur and Bhopal rank as high but sit outside the pilot states. They are the backup pair: MP and Chhattisgarh through Lotus Electronics.
- **Retailers to approach first:**
  - Bajaj Electronics / Electronics Mart (Telangana and AP)
  - Sathya (AP)
  - Pai International (UNKNOWN current size)
  - The independents in each pilot city. **These must be found on the ground.** No public list exists.

  The full chain list is in `retailers.csv` and the store rows in `retailer_outlets.csv`.
- **Repair agencies to approach:** the shortlist of 30 needs the OSM layer (pending). Until then, use Justdial manually and the brand authorised-service locators for each city.

**The 90-day test that decides the case:**
1. **Sign up 10 retailers** across 2–3 of the cities.
2. **Measure four numbers:**
   - real referrals per retailer per month
   - booking rate
   - completion rate
   - the agency payout the agency will accept
3. **Ask each retailer two things:** what commission they expect, and whether they fear service liability. Electronics Mart has said *"We only facilitate the product on our floor."*

**Kill the idea if any of these happens:**
- fewer than 15 paid referrals per retailer per month
- agencies insist on keeping more than 85% of labour
- retailers ask for more than 12%
- an incumbent (Onsitego or Zopper) offers the same thing to the chain first

## 8. Answers to the 15 final questions

| # | Question | Answer (evidence and confidence) |
|---|---|---|
| 1 | Most eligible Tier 2/3 cities | **Uttar Pradesh: 61** (13 Tier 2, 48 Tier 3). High confidence: Census 2011 |
| 2 | Most verified regional retail outlets in eligible cities | **Tamil Nadu: 163** matched to eligible cities, then Andhra Pradesh 49 and Kerala 31. Sathya's 301 Tamil Nadu stores are a state total only and aren't included. Medium: only 13 chains have city data |
| 3 | Highest retailer density per urban household | **Tamil Nadu: 4.1 chain outlets per 100k households**, then Telangana 2.3 (Puducherry 5.2 is a single city). This partly reflects where locators exist. Low–medium |
| 4 | Largest out-of-warranty installed base | **Kerala: 70 L, then Uttar Pradesh 65 L** (BASE). Kerala's census UAs are very large and its ownership is high. Medium |
| 5 | Highest potential repair demand | **UP (₹339 Cr), then Maharashtra and Kerala** (BASE). Medium |
| 6 | Strongest local repair networks | **Not determinable yet.** It needs the OSM layer and verification calls. Eureka Forbes partner centres are confirmed in 27 of 30 checked cities |
| 7 | Significant service gaps | **Not shown.** Low online visibility does not prove a shortage. No city is classed as a gap without supply evidence |
| 8 | Realistic retailer partners | Bajaj Electronics, Sathya, Lotus, Aditya Vision (it has its own service arm, so it is a competitor-partner) and the independents. Chains tied to Onsitego, OneAssist or resQ are harder |
| 9 | Best mix of retailer demand and technician supply | Pending supply data. On demand and retail alone: **Indore, Raipur, Warangal, Bhopal, Visakhapatnam, Vijayawada** |
| 10 | Underserved, or already served? | **Partly served.** Extended warranties at the counter are well served. Paid post-warranty repair referral by regional retailers has no visible player, and no visible demand from retailers either |
| 11 | What stops Jeeves, Onsitego, Bigfix or Servify from copying? | Very little. Only exclusive retailer deals or a machine-history data edge would. Low defensibility |
| 12 | Contribution per completed repair | **About ₹56 (BASE); −₹124 to ₹400 across LOW–HIGH** |
| 13 | Retailers and jobs needed to be viable | **About 14,300 jobs a month ≈ 1,120 retailers (BASE)**; about 39 retailers in HIGH |
| 14 | Pilot: 2 states, 5 cities | **AP and Telangana. Warangal, Vijayawada, Visakhapatnam, Guntur, Karimnagar** |
| 15 | What would reject the idea | The kill criteria in §7 |

## 9. Investor-ready summary (Deliverable 7)

| Question | Answer |
|---|---|
| **Why this market?** | Tier 2/3 homes hold about 4.9 Cr out-of-warranty appliances spending about ₹2,200 Cr a year on service and repair (BASE). 44% of it goes to informal local technicians. |
| **Why these states?** | AP and Telangana: the best evidence base, public store networks, and the team's home market. |
| **Why these cities?** | They are the top entry scores within those states, with verified chain outlets and checked competitors. |
| **Who pays?** | The household pays for the repair. The platform's revenue is the margin on top of the agency payout, plus a booking fee. |
| **Why would they pay?** | A retailer they already trust vouches for the technician and the price. This is **not yet tested**. |
| **Economic value created** | Retailers earn referral income. Agencies get jobs without paying the platforms. Households get a trusted repair. |
| **Revenue model** | About ₹227 of revenue per ₹898 job (BASE). |
| **Contribution margin** | About ₹56 a job (25% of revenue) in BASE. Negative in LOW. |
| **Defensibility** | Low today. It could come from exclusive retailer contracts and a per-machine service history. |
| **Major risks** | Retailer apathy or liability fear, incumbents at the counter, thin margins, unverified supply, and repair incidence inputs taken from US data. |

**The honest investor line:** "We have sized the demand and found the gap, and we are running a 90-day test of the one number that decides whether this is a business." Do not show a revenue plan until that number is measured.
