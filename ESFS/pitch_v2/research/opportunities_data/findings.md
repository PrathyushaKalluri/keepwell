# Is a 15–20% contribution margin investable, and which data layers lift it?

**Prepared:** 19 Nov 2026 by the research agent (margins and data layers). The lead saved and condensed it. The detail is in `margin_benchmarks.csv` and `layers.csv`.

**Tags:**
- **FACT:** filing or company number
- **PROXY:** a nearby comparable
- **ASSUMPTION:** our input
- **DERIVED:** our arithmetic

**Search gaps.** The web-search budget ran out. These were not retrieved: price per lead in India, the claims-fraud rate, Bajaj Finance's consumer-durables book, and the Khatabook, Bizom, Marg and Carfax figures.

## Part 1. Is 15–20% contribution thin?
**Use the right base.** Keepwell is the principal, so it books the gross job value. The comparable at Urban Company is therefore **NTV** (total job value), not UC's revenue. UC's revenue is only its take, about 34% of NTV.

**Urban Company, India consumer services** (FACT unless marked):

| | FY23 | FY24 | FY25 | FY26 | H1 FY27 |
|---|---|---|---|---|---|
| NTV (₹ Cr) | 1,805 | 2,216 | 2,667 | 3,167 | 2,019 |
| Contribution, % of NTV | 17.7% | 19.6% | 20.2% | 21.2% | 21.7% (DERIVED) |
| Adjusted EBITDA, % of NTV | −9.7% | −0.5% | 3.3% | 4.1% | 5.3% (DERIVED) |

- **Trajectory.** In FY22, contribution was 11.8% of NTV (PROXY). It took UC 4 years to add about 9 points.
- **UC's targets.** Steady-state adjusted EBITDA of 9–10% of NTV, consolidated breakeven by Q3 FY28, and ₹1,000 Cr adjusted EBITDA by FY31.
- **Don't compare against UC's revenue-based margins.** Its 81–84% "gross margin" and 61% contribution on revenue are marketplace accounting.

**Indian peers:**
- **OneAssist:** FY25 EBITDA 4.1% on ₹623 Cr.
- **Servify:** FY24 EBITDA −8.8% on ₹755 Cr.
- **Onsitego:** about −17.6%.
- **247around:** about −22%.
- **Snabbit:** FY26 loss ₹167.75 Cr on ₹12.25 Cr revenue.
- **Housejoy:** loss-making.
- **Lloyd (Havells) division:** FY26 contribution 8.4% on ₹3,948 Cr.

**Global operators:**
- **Frontdoor:** gross margin 55%, adjusted EBITDA 26.5%. It is a home-warranty business, so it carries the risk.
- **HomeServe:** about 17.2% adjusted operating margin (FY22).
- **ServiceTitan:** total gross margin 70%; non-GAAP operating margin 9.8%.
- **Asurion:** EBITDA 24–25% (PROXY).
- **Mr. Appliance:** franchisor royalty of 5–7%.
- **US HVAC:** independent operators earn 8–12% EBITDA; private-equity platforms 15–22%.

**Reading:** operators that own the labour earn 8–20% EBITDA. Those above 20% either carry underwriting risk (plans) or own software or data.

**What investors expect:**
- **Gross margin:** about 40%+ for services and 70%+ for SaaS (one Indian blog; PROXY).
- **Bain–IVCA 2026:** a decisive shift to profitability and unit economics.
- **IPV:** looks for NRR above 100% and LTV/CAC above 2.
- **Tidemark and a16z:** a thin gross margin earns a services multiple.
- **Not found:** specific thresholds from Blume, Accel, Elevation or 3one4.

**Verdict:**
1. Contribution of 15–20% is **not thin for an operator**. It matches UC India on the same base and is above Lloyd's 8.4%.
2. Gross margin is about 33% on the BASE repair job, which is below the ~40% heuristic. The pitch should show the path to 40%.
3. EBITDA at maturity would be about 5–10% of gross revenue, which earns operator multiples of 2–3×. **The data layers are what make this a venture story.**

## Part 2. Data layers
**The budget brands already have** (FACT: annual reports and LG's RHP):

| Company | Warranty accrual | Note |
|---|---|---|
| LG India FY25 | ₹125.6 Cr (0.52% of revenue) | 788,911 claims, **about ₹1,590 per claim**. Installation revenue ₹344 Cr. |
| Whirlpool FY26 | ₹90.9 Cr (1.22%) | |
| Voltas FY26 | ₹113.7 Cr | |
| Blue Star FY26 | ₹65.8 Cr | |
| Havells FY26 | ₹401.6 Cr | |

- **Category sizes:** AC about ₹36,000 Cr, refrigerators about ₹32,500 Cr, washing machines about ₹26,500 Cr. The AMC market is ₹6,000 Cr (Redseer, via LG's RHP).
- **Warranty spend in these three categories:** about **₹475–1,140 Cr a year** (DERIVED).

| # | Layer | Price | Gross margin | Market | Feasibility | First ₹1 Cr |
|---|---|---|---|---|---|---|
| 1 | Failure intelligence for brands (SaaS) | ₹10 L–1 Cr ACV (ASSUMPTION) | 70–80% | Software wallet ₹10–25 Cr; its value is leverage in authorisation talks | Low–med: brands already hold in-warranty data, so our slice is out-of-warranty and Tier 2/3 | Year 4–6 |
| 2 | **Installation and claims verification** | ₹20 / 40 / 100 per verified record, plus an API | 80–90% | ₹85–220 Cr | **High:** a by-product of every job, and it strengthens the authorisation case | Year 3–4 |
| 3 | Retailer sales and inventory SaaS | myBillBook ₹3.5–4k/yr; Busy ₹4–22k/yr (FACT) | | ₹6–54 Cr | Low on its own (Vyapar's EBITDA −103%); medium as a dashboard inside a desk fee | Year 3, as part of the desk fee |
| 4 | **Ownership intelligence:** replacement leads and AMC renewals sold to retailers | ₹100–200 per qualified lead, or ₹500 per converted sale | 60–80% | Ceiling ₹70–280 Cr (price per lead UNKNOWN) | Medium. Needs DPDP consent; underwriting use is low feasibility | Year 4–5 |

**Comparables:** PTC (Servigistics) is being acquired by Schneider for $22.6B. Tractable was valued at $1B. Servify is valued at ₹5,660 Cr.

**Multiples:**
- Operators: about 2.0–2.9×.
- Marketplaces: median 2.3× (UC 12.9×).
- Vertical SaaS: 7.4–7.8×.
- Servify: about 7.5×.

**Years 5–7 (DERIVED, assuming 30 clusters in year 5 and 60 in year 7):**
- **Layer 2:** ₹2.5–5 Cr in year 5, rising to ₹7–11 Cr in year 7.
- **Layer 4:** ₹0.5–1.5 Cr in year 5, rising to ₹2–4 Cr in year 7.
- **Blended contribution:** about 20–29% in year 5, rising to 22–31% in year 7.
- **Blended gross margin:** about 37–41% by year 7.

**Pilot tests:**
- Two brands or protection providers pay at least ₹20 per verified record.
- Retailers pay at least ₹150 per qualified lead.
- Retailers consent to the use of their customers' data.
