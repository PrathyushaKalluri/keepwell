# Methodology

Rebuild everything with `python3 build_market_intel.py` (standard library only). Each research module's raw files, logs and source lists are in `raw/<module>/`.

## Tier definitions
- **Primary (population, Census 2011 final, Table A-4):**
  - Tier 1: the 8 metros, plus any city over 3M (excluded).
  - Tier 2: 500k–3M.
  - Tier 3: 100k–500k.
  - Small towns: 50k–100k, kept as a separate segment and not scored.
- **Counting units:** a city or UA is counted once (`count_unit=1`). Constituent towns point to their `parent_ua`. Metro satellites (Thane, Howrah, Ghaziabad and others; 118 flagged) are excluded from the core.
- **Alternative (sensitivity):** the 7th Pay Commission HRA classes (2017 list). Y and Z cities of at least 100k, excluding satellites. The state ranks under both definitions are in `states.csv`.
- **Population year:** all city populations are **2011**. A 2026 household figure is DERIVED as `pop_2011 × state urban growth factor 2011→2026 (NCP Technical Group, tabulated 1 Mar 2026) ÷ 2011 state average urban household size`. Two simplifications: every city is assumed to grow at its state's urban rate, and household size is held at its 2011 value.

## Installed base and demand (per city, per category, LOW/BASE/HIGH)
```
ownership(state,cat) = NFHS-5 state urban rate × national 2024 survey rate / NFHS-5 national rate
   (AC: NFHS-5 AC+cooler × national AC-only / national AC+cooler. DERIVED. States missing from NFHS-5 use the national rate)
machines   = households × ownership × tier-2/3 index (0.70/0.85/1.00) × machines per owning household
in_use     = machines × share still in use
oow        = in_use × share out of comprehensive warranty
requests   = Σ job types: in_use × routine service frequency + oow × repair/refill incidence
spend      = Σ requests × bill per job type
retailer-accessible = requests × dealer-arranged channel share (13% BASE, LocalCircles AC data, applied to all categories as a proxy)
daily      = annual ÷ 365 (calendar) and ÷ 300 (operating days)
```
Every parameter, with its LOW/BASE/HIGH values, label (FACT / SOURCE-BACKED PROXY / ASSUMPTION / DERIVED ESTIMATE) and source, is in `raw/demand/parameters.csv` and on dashboard page 4. LOW and HIGH are corner cases: every input is set low, or high, together.

## Supply
- **Retail:** chain outlets come from official store locators and filings (`raw/retail`). They are matched to census cities by name, using aliases and fuzzy matching within the state. Unmatched outlets (towns under 50k, neighbourhoods inside metros) and state-total-only figures are reported separately per state, never assigned to a city.
- **Repair (OSM):** OpenStreetMap points are assigned to the nearest city whose centroid lies within `2 + 2.5·√(pop/100k)` km. Every point is **LISTED, NOT VERIFIED**, and technician headcount is UNKNOWN. A listing count is never treated as capacity.
- **Competitors:** 28 companies × 30 cities, each with a status: VERIFIED ACTIVE, PUBLICLY CLAIMED, NOT VERIFIED or NO EVIDENCE FOUND. "No evidence" is never read as "absent."

## Scores (core Tier 2/3 cities only)
- **Market size (0–100):** 70% × percentile of BASE annual spend, plus 30% × percentile of known retail outlets. Population, installed base and requests are not added separately, because they are the same driver counted three ways.
- **Startup entry (0–100):** the default weights are below. Each factor is a percentile rank among core cities.

  | Weight | Factor | Rule |
  |---|---|---|
  | 25 | Retailer access | Chain outlets + ½ × OSM appliance shops. Scores 0 if none are known |
  | 25 | Monetizable demand | Retailer-accessible spend |
  | 20 | Fulfilment | Listed repair points. Scores 0 if none |
  | 15 | Unmet demand | Fewer competitors + lower repair density. Only where evidence exists; otherwise a fixed 0.15, so missing data is not rewarded |
  | 15 | Unit economics | Average ticket, which reflects the category mix |

- **Confidence adjustment:** the entry score is multiplied by 1.0 (HIGH), 0.85 (MEDIUM) or 0.70 (LOW).
- **Alternative weightings:** demand-heavy 15/40/20/10/15, supply-heavy 20/20/35/10/15 and equal 20s. The resulting ranks are in `opportunity_scores.csv`.
- **State scores:**
  - Market = √(state spend ÷ the maximum state spend) × 100.
  - Entry = the average of the state's top 5 city entry scores × (0.7 + 0.3 × data completeness).

## Confidence
Each city gets one point for each of the following:
1. Verified chain outlets matched.
2. 5 or more OSM listings.
3. Competitors checked.
4. A state-specific ownership rate.

**HIGH** = 3 or more points, including retail. **MEDIUM** = 2. **LOW** = fewer than 2. Per-city gaps are in `data_quality_report.csv`.

## Gap classes
- **INSUFFICIENT DATA:** LOW confidence and no chain outlets.
- **COMPETITIVE / SATURATED:** 3 or more competitors verified, or 8 or more verified plus claimed.
- **HIGH OPPORTUNITY:** top 15% on entry score, confidence not LOW, 2 or more outlets, and 3 or more listed repair points.
- **PROMISING BUT UNVERIFIED:** top 40% on entry score.
- **LOW COMMERCIAL ATTRACTIVENESS:** everything else.

## Economics
The simulator is on dashboard page 7, and `build_market_intel.py` (the `econ` function) mirrors it. GTV is what the customer pays, and it is not revenue.
- **Revenue** = labour × (1 − agency payout) + parts × (1 − parts cost share) + booking fee.
- **Contribution** = revenue − retailer commission − payment fees − refund/rework allowance − support − coordination.

**Labels:**
- The average bill is DERIVED from the demand model.
- Support cost is a SOURCE-BACKED PROXY (Urban Company disclosures).
- Everything else is an ASSUMPTION and can be edited.

## Limitations
1. **Repair incidence:** no Indian survey exists. US proxies are used.
2. **Repair capacity:** OSM coverage of Indian businesses is incomplete and urban-biased, and nothing was verified by phone or a visit.
3. **Chain coverage:** most regional chains' service arrangements are UNKNOWN, and Vijay Sales', Croma's and Reliance Digital's city-level outlets are not public in usable form.
4. **Competitor checks:** competitor presence was checked in 30 cities only. Those cities therefore score higher on confidence, which is a selection effect.
5. **Population:** 2011 figures scaled to 2026. City populations are not current counts.
6. **AC ownership:** AC-only ownership by state is derived from a combined AC-or-cooler figure.
7. **Retailer channel:** the retailer-accessible share is AC data applied to all four categories.
