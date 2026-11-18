# Retail intel: audit log and gaps (run date 2026-11-18)

## Files
| File | Rows | Notes |
|---|---|---|
| retailers.csv | 22 chains | 16 with a numeric outlet count; 6 UNKNOWN (Vijay Sales, Croma, Reliance Digital have ranges from news) |
| retailer_outlets.csv | 846 stores | only where a locator gave store-level data |
| retailer_city_counts.csv | 585 rows | city aggregates of the outlet file, plus Darling (district level), Aditya Vision and Sathya (state level, filings) and Value Plus (state level, self-reported) |
| retail_market_context.md | - | market structure, dealer proxies, evidence for and against |
| scripts/ | - | stdlib Python used: bajaj.py, kohi.py, parse_all.py, retailers.py |

## Store-level extraction method (all public pages, polite 1.2–2 s delays)
| Retailer | Rows | Method |
|---|---|---|
| Bajaj Electronics | 210 | `/country/getcitiesbystateid` + `/getstoredetails?stateId=X&cityId=0` (the site's own AJAX endpoints) |
| Girias | 187 | `/stores?page=1..7` HTML |
| Vasanth & Co | 153 | `/branches` HTML; lat/lon from Google embed `!2d/!3d` on the page |
| Pittappillil | 82 | `/store-locator` embedded JSON (title, lat, lng, address); the site says "81 showrooms" |
| Great Eastern | 76 | POST `/find-store` with pincode (CSRF from page), about 100 pincodes in WB, Odisha, NE, Bihar, Jharkhand, Delhi, Haryana, UP, Rajasthan, AP; deduped by fcId. Returns about a 50 km radius, so this may be incomplete; Sept 2025 news says "90+" |
| Nandilath G-Mart | 59 | `/our-stores/` HTML (district headings; city left UNKNOWN) |
| Oxygen | 38 | locator cards + 38 detail pages ("located at … in X District") |
| Lotus | 28 | schema.org Store JSON-LD on 9 `/contact-us/{city}` pages |
| Kohinoor | 13 | same POST `/find-store` platform, 23 Maharashtra/Goa pincodes (all within MMR) |

- Phone numbers and emails were deliberately stripped from addresses; no personal data was kept.
- Girias `state` values are inferred from the pincode prefix and labelled "(from pincode)".
- `district` is only filled where the page states it.

## Discrepancies to note
| Retailer | Locator / source | Other figure |
|---|---|---|
| EMIL | 210 on locator | 223 (31 Mar 2026) and 227 (Q1 FY27), company-reported via secondary sources. The locator has no West Bengal stores, although news says the WB rollout is planned |
| Darling | locator 174 | homepage says "185+" and also "119+" |
| Girias | locator 187 | homepage "175+" |
| Vijay Sales | 140+ (Mar 2026) | 160+ (Apr 2026); ScrapeHero 108 (Feb 2025) |
| Aditya Vision | 207 (filing, 31 Mar 2026) | 214 (30 Sep 2026, secondary only) |
| Great Eastern | 76 on locator | 90+ (news) |

## Blocked or failed sources
- croma.com: HTTP 403 (store locator and ZipCare pages). Evidence is from search snippets.
- vijaysales.com locator JS: 406 (bot protection). The count is from news.
- sathya.store: 403. The full Sathya DRHP was not located on SEBI; only the abridged prospectus was used.
- viveks.com: HTTP 522. Evidence is from search snippets only.
- Reliance Digital resQ T&C page: returned "Page not found" to fetch.
- paiinternational.in: JS-only shell, no locator data. The only count is from 2017.
- ezoneonline.in: did not resolve.
- adishwar.com: empty page. **Adishwar Auto Ride: no data at all.**
- alphaspread.com and mysmartprice.com: 403.
- EMIL and Whirlpool FY26 annual reports were not retrieved (NSE archive paths not found).

## Gaps (UNKNOWN)
- Service or EW evidence for: Sathya, Girias, Darling, Vasanth & Co, Nandilath, Lotus, Great Eastern, Kohinoor, Sales India, Pai, Unilet.
- Revenue for all unlisted chains except Sathya (from the DRHP) and Value Plus (self-reported).
- Online share of large appliances specifically.
- A current count of independent appliance dealers; no CEAMA or Technopak figure was found.
- Brand dealer counts for Havells/Lloyd, Whirlpool, Godrej, Samsung and Voltas (only a secondary "30,000+").
- EW commission rates paid to Indian retailers.
- Any documented failed retailer and service partnership.
- Chains not yet covered: Punjab, Assam / North-East and standalone Odisha regionals (a search found none with verifiable counts); Poorvika (475+, mobile-led, excluded); SS Retail (mobile, excluded).

## Next steps suggested
1. Get the full Sathya DRHP from SEBI. The CRISIL industry chapter likely has channel shares, and the business chapter may cover EW.
2. Get the EMIL FY26 annual report and recent transcripts for current EW revenue.
3. Fetch the Croma and Vijay Sales locators with a real browser.
4. Run phone or in-person checks with service heads at Girias, Sathya, Vasanth & Co and Pittappillil about referral appetite. These are primary interviews, not web data.
