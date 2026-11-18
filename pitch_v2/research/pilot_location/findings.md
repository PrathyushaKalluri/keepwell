# Pilot location: findings (19 Nov 2026)

This was written by the location research agent. The lead saved it in condensed form. Per-belt data is in `belts.csv`.

## Scores

Each factor was scored 1–5 and weighted. The total is out of 100.

| Weight | Factor |
|---|---|
| 25% | AC demand |
| 20% | Retail |
| 15% | Competition gap |
| 10% | Technicians |
| 10% | Multi-appliance demand |
| 10% | Policy |
| 10% | Logistics |

| Rank | Belt | Score |
|---|---|---|
| 1 | Vijayawada–Guntur | 76.0 |
| 2 | Warangal (+Karimnagar) | 73.5 |
| 3 | Nizamabad | 65.0 |
| 4 | Rajahmundry–Kakinada | 62.5 |
| 5 (joint) | Kurnool | 62.0 |
| 5 (joint) | Khammam | 62.0 |
| 7 | Tirupati | 61.0 |
| 8 | Nellore | 59.5 |
| 9 | Visakhapatnam | 59.0 |

**Sensitivity:** Warangal moves into first place in either case:
- its retail score rises from 2.5 to 3.5;
- 10 points of weight move from retail to competition gap.

## Evidence

**Heat** (IMD 1991–2020 normals):

| Station | May mean max |
|---|---|
| Hanamkonda | 41.6 °C |
| Ramagundam | 42.2 °C |
| Nizamabad | 42.1 °C |
| Vijayawada | 40.2 °C (record 48.8 °C) |
| Nellore | 40.1 °C |
| Khammam | 40.1 °C |
| Kurnool | 39.8 °C |
| Kakinada | 37.7 °C |
| Vizag | 33.3 °C |

**May humidity at 17:30:**

| Station | Humidity |
|---|---|
| Vizag | 76% |
| Kakinada | 62% |
| Nellore | 54% |
| Hanamkonda | 50% |
| Vijayawada | 46% |
| Khammam | 37% |
| Nizamabad | 24% |

**AC ownership** (NFHS-5, urban AC+cooler): Telangana 62.7%, AP 36.2%.

**Installed ACs** (DERIVED):

| Belt | ACs | AC jobs a year |
|---|---|---|
| Vijayawada–Guntur | about 129k | about 186k |
| Warangal+Karimnagar | about 94k | about 135k |

**Water:**
- Telangana's fluoride hotspots include Hanamkonda, Warangal, Karimnagar, Khammam and Nalgonda. 14.8% of samples exceed 1.5 mg/L (TS GW Year Book 2025).
- AP has salinity in parts of Krishna, Guntur, Nellore, Kurnool, the Godavari districts and Vizag (CGWB).
- District TDS medians: UNKNOWN.

**Retail** (Bajaj Electronics outlets):

| Belt | Outlets |
|---|---|
| Vijayawada–Guntur–Tenali | 10 |
| Warangal+Karimnagar | 5 |
| Vizag | 8 |
| Rajahmundry–Kakinada | 7 |

Independent shops: UNKNOWN. OSM was unusable. To settle it, use GST registrations under HSN 8415/8418/8450, or a 2-day shop walk.

**Competition** (Urban Company live pages, 19 Nov 2026):

| Status | Cities |
|---|---|
| Full catalogue, including AC | Vijayawada (AC from ₹799), Guntur (AC from ₹699), Vizag, Rajahmundry |
| No AC page | Warangal, Kakinada |
| No pages at all | Karimnagar, Khammam, Nizamabad, Kurnool, Nellore, Tirupati |

Eureka Forbes has 6 centres in Vijayawada and none in Warangal.

**Technicians:**
- JCH-Hitachi and APSSDC run AC skill centres in Vijayawada and Kakinada.
- ITI RAC seats: UNKNOWN.
- Entry pay is about ₹10–25k a month.

**Policy:**
- AP Startup Policy 4.0 offers grants, seed equity and go-to-market support. AP has no state gig law.
- Telangana's Act 21 of 2026 sets a fee of 1–2% of payouts.
- The central Code on Social Security has applied in both states since 21 Nov 2025. Its rate is not yet notified, with a cap of 5% of payouts.
- Whether Keepwell counts as an "aggregator" needs a legal view.

**Logistics** (OSRM free-flow from Hyderabad):

| Belt | Distance | Time |
|---|---|---|
| Warangal | 143 km | 2.0 h |
| Nizamabad | | 2.4 h |
| Kurnool | | 2.7 h |
| Khammam | | 2.7 h |
| Vijayawada | 273 km | 3.6 h (about 5 h in practice) |
| Rajahmundry | | 4.9 h |
| Nellore | | 5.7 h |
| Vizag | | 7.3 h |

**Income** (AP per-capita GDDP, 2023–24):

| District | Per-capita GDDP |
|---|---|
| Vizag | ₹5.46 L |
| Krishna | ₹4.22 L |
| NTR | ₹3.60 L |
| Guntur | ₹3.04 L |
| Nellore | ₹2.62 L |
| Kurnool | ₹1.94 L |

In Telangana, Hanumakonda is ₹1.87 L.

## Corrections applied to Step 0c

- "Competition thin" now reads "present for households, absent for shops".
- "Most humid" was removed.
- "AP no gig levy" now reads "no *state* fee; the central Code applies in both states".
