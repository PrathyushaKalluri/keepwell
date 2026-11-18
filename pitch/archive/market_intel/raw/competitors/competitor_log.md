# Competitor research log

Run date: 2026-11-18. Analyst: Claude (agent). Tools used: WebSearch, WebFetch, curl, and the Python 3 standard library. Generator scripts were kept in the session scratchpad. The outputs are in this folder.

## Files

- `competitors.csv`: 32 rows (one per company or failure case) × 25 columns.
- `competitor_city_claims.csv`: 840 rows (28 companies × 30 cities). Status breakdown:

  | Status | Rows |
  |---|---|
  | VERIFIED ACTIVE | 28 |
  | PUBLICLY CLAIMED | 79 |
  | NOT VERIFIED | 553 |
  | NO EVIDENCE FOUND | 180 |

- `competitor_landscape.md`: the analysis and verdict.
- `evidence/`:
  - Eureka Forbes authorised-centre URL list (729 entries, taken from its sitemap).
  - Urban Company city-appliance slugs (taken from its category sitemaps, 84,327 URLs).
  - Raw research notes.

## How each city status was assigned

- **VERIFIED ACTIVE**: a city-specific page with a named local business and street address (Eureka Forbes), or local listings with addresses and ratings (Justdial, Warangal only). For Eureka Forbes, I fetched 4 centre pages and confirmed the address (Indore, Karimnagar, Thrissur, Guntur). The other 23 were inferred from the same URL and page template.
- **PUBLICLY CLAIMED**: the city appears on a coverage list, sitemap or templated page.
  - For Urban Company, a city got this status if its city page showed a city-specific price catalogue. That is stronger than a coverage list, but the reviews shown are national aggregates, and UC does not publish its 47-city list.
- **NOT VERIFIED**: the company makes a broad claim (PIN count, city count, "all major cities") that could include the city, but nothing city-specific was found.
- **NO EVIDENCE FOUND**: no claim and no page found for the city, or the company has exited or does not exist. **This is never to be read as "no competitor here".**

## Steps

1. **Sitemaps and robots.txt** for 24 domains.
   - Usable sitemaps: onsitego, bigfix, 247around, servsy, urbancompany (category sitemaps), oneassist, zopper, serviceondoors, hometriangle, eurekaforbes, daikinindia, kent and voltas (index only).
   - No sitemap, or blocked: jeeves (503, and the apex domain serves an F1 Infosolution app), servify (404), qdigi (404), housejoy (no HTTP response), hellotechie (domain for sale, or no DNS), justdial (blocks bots), nobroker (returns HTML).
   - serviz.com turned out to be a US company. The Indian SERVIZ is at serviz.in.
2. **Urban Company**:
   - Parsed 84,327 sitemap URLs to build city × category slugs.
   - Fetched 19 target-city pages and extracted prices. Foam-jet AC service starts at Rs 599–899 depending on city, and washing-machine and fridge check-ups at Rs 199.
   - Downloaded the abridged prospectus (8 pages) and the Q3 FY26 shareholder letter from NSE, and took city, partner and NTV-concentration figures from them.
3. **Company pages fetched**: servsy (service areas, pricing, about), bigfix about, 247around about, servify.com/in, onsitego home, oneassist home, zopper home and consumer-durables page, serviz.in, serviceondoors, mrright.in, qdigi.in.
   - qdigi.in could not be tied to Qdigi Services Ltd, so I did not use it.
   - OneAssist's 10 city repair pages all redirect to a category page.
4. **Brand service arms**: Kent AMC price card (effective 02-03-2026), Godrej AC AMC, Daikin annual service care, Voltas AMC terms, LG AC charge guide, the Samsung out-of-warranty page, and the Eureka Forbes sitemap of authorised centres.
   - Samsung's out-of-warranty table is rendered by JavaScript, so it came back empty.
5. **Financials from press and filings coverage**:

   | Company | Figures | Source |
   |---|---|---|
   | OneAssist | FY25 revenue Rs 623 Cr | Entrackr, provisional |
   | Servify | FY25 revenue Rs 781 Cr | Secondary sources citing Entrackr |
   | Zopper | FY25 revenue target only | — |
   | Onsitego | FY25 revenue projection only | — |
   | Flipkart group | FY25 figures | — |
   | Justdial | FY25 profit; revenue figures conflict | — |
   | Eureka Forbes | Q4 FY25 figures | — |

6. **Retailer partnership checks**: Vijay Sales and Value Plus pages (Onsitego), Croma ZipCare listings, and the Zopper logo strip. Web searches on Bajaj Electronics, Poorvika, Sangeetha, Pai International and Girias found no named partner.

## Gaps and caveats

- **Urban Company RHP not obtained.** I could not reach the full RHP (Morgan Stanley returned 503, and I found no SEBI direct link). The appliance-repair share of NTV and the full city list are **not found**. The 28% commission is a secondary figure (Finology, citing the RHP). The FY25 revenue of Rs 1,144 Cr and net profit of about Rs 240 Cr are also secondary.
- **Missing financials.** No audited revenue was found for Jeeves, resQ, Onsitego (an FY25 MCA filing exists but sits behind paywalls on Tofler and similar sites), Qdigi, 247around, Bigfix, SERVIZ, Servsy or Zopper (actuals). Tracxn and Tofler were not accessible.
- **City-level checks not done** for Jeeves, resQ, Onsitego, Servify, LG, Samsung, Voltas, Kent, Daikin and Croma. Their service-centre locators are API or JavaScript driven, or need a login. A follow-up could use a browser session, or call each locator by PIN code.
- **Justdial**: only Warangal was checked, through search snippets. A per-city check needs a browser.
- **Regional chains' in-store repair practices** are largely invisible online. The best way to fill this gap is field calls to store managers, for example Bajaj Electronics, Sathya, Pai, Viveks, Kohinoor and Value Plus.
- **Ownership details recalled, not re-checked this run**: Reliance's majority stake in Justdial and Eureka Forbes's controlling shareholder (Advent). Both are marked in the CSV.
- **Unresolved identities**:
  - The Indian SERVIZ's legal entity is not confirmed. CB Insights lists a 2022 "SERVIZ" under Infervize Home Services, but I could not link it to serviz.in.
  - ServiceOnDoors' legal entity was not found.
- **Unchecked metro or national players** that may matter: Snabbit/Pronto (house help, not repair), Sulekha (lead-gen), GoWarranty, Warrantyme, CPP Group (the extended-warranty administrator behind the Bajaj Finserv plans, which claims 400+ network centres), and Bajaj Finserv's own extended-warranty plans.
- **Possible bias**: web evidence favours companies with SEO-heavy sites (UC, ServiceOnDoors). Template pages were not treated as operational proof.
