# Geo and census audit log

Run date 2026-11-18. Python standard library only. The build scripts are in `_scripts/`.

## What was done
1. **City inventory.** Downloaded the final Census 2011 tables A-4 (I) Class I (100k+) and A-4 (II) Class II (50k-99,999) from the Census NADA catalog (ids 42876 and 42877), then parsed their 1901-2011 history blocks and kept the 2011 row for each unit.
   - The parse reproduces the table headers exactly: Class I has 468 units (298 UAs + 170 towns) with 264,745,519 people, and Class II has 474 units (100 UAs + 374 towns) with 32,179,677 people.
   - The result is **942 non-overlapping "count units"** (`count_unit=1`) and **559 constituent rows** (`count_unit=0`). Constituent rows are statutory or census towns of 50k+ that lie inside a UA. They carry `parent_ua` and `parent_ua_id` and must not be added to the totals.
   - Outgrowths (OG), "portion" rows and constituents under 50k are not listed. Their population is included in the UA total.
2. **The 50k-100k band is complete.** The Census A-4 Class II table covers all of India, so no small towns are missing from the source. The constituent rows only cover constituents of 50k+ inside UAs.
3. **State attribution.** The state comes from the A-4 district/state text. For current boundaries:
   - Telangana is assigned from its 10 districts of 2011.
   - Ladakh is Leh and Kargil.
   - Daman & Diu and Dadra & Nagar Haveli are merged into one UT.
   - `state_census2011` keeps the 2011 state.
4. **Tiers.**
   - `tier_pop` is the primary definition: Tier 1 = the 8 metro UAs or anything over 3M (this adds Surat UA and Jaipur), Tier 2 = 500k-3M, Tier 3 = 100k-500k, Small town = 50k-100k. Constituents of a metro UA are Tier 1. Other constituents are banded on their own population, and `tier_pop_market_unit` gives the tier of the parent UA.
   - `tier_hra` follows the DoE OM 2/5/2017-E.II(B) of 07.07.2017 annexure. Its X/Y lists are matched to the units; everything else is Z. Para 6 extends Y-class rates to Shillong, Goa, Port Blair, Panchkula and SAS Nagar; these are marked "Y (para 6 extension)". For Goa, all three Goa UAs were marked because the OM does not say which cities in Goa are covered. The annexure lists Faridabad, Gurgaon, Ghaziabad and Noida as Y "for dependency only", and para 6 continues Delhi X-rates there.
   - `eligible_t2t3_core` = count unit, Tier 2 or 3, not a metro satellite. Result: **80 Tier 2 + 369 Tier 3**. A further 473 small towns are flagged in `eligible_small_town`.
5. **Metro satellites** (`metro_satellite=1`, 118 rows):
   - Every non-core constituent of the 8 metro UAs, for example Thane, Navi Mumbai, Haora (Howrah), Secunderabad Cantonment, Pimpri-Chinchwad and Ambattur.
   - Functional satellites outside the UA boundary, with the basis given in `metro_satellite_basis`. For the NCR (Ghaziabad UA, Faridabad, Gurgaon UA, Noida) the basis is the HRA OM para 6. Greater Noida, Vasai-Virar, Bhiwandi UA, Panvel, Navi Mumbai (Panvel) CT and Kharghar were added on analyst judgement as part of the Mumbai Metropolitan Region.
   - Gandhinagar, Sonipat and Bahadurgarh were **not** flagged. Review them if a wider definition is wanted.
6. **Coordinates** were taken from the following sources, in this order. A candidate was accepted only if it fell inside its state polygon (0.05° tolerance). Results:
   - Wikipedia "List of cities in India by population" (rev 1385294039): 463 rows.
   - Wikipedia article coordinates through the MediaWiki API: 614 rows.
   - Wikidata P625 coordinates (bulk SPARQL query for population ≥20k): 338 rows.
   - OSM Nominatim (featureType=settlement, about 1 request per second, generic User-Agent): 50 rows.
   - Blank: 36 rows.
   - Constituents more than 35 km from their parent UA were reviewed by hand. Six Nominatim hits and the Wikipedia-list point for Mathura (27.28N 77.41E, which falls outside UP) were rejected and left blank.
   - The Lucknow, Meerut, Dehradun and Ramgarh cantonments carry the parent city's point and are flagged APPROXIMATE. Tarn Taran resolved to a tahsil-level point.
7. **State baseline.** Built from Census A-1 (urban population and households) and NCP Table 9 (1 March 2026, read directly with no interpolation). See `state_baseline_notes.md`.
8. **GeoJSON.**
   - Source: DataMeet `States/Admin2` shapefile (CC BY 4.0, last geometry commit 2021-10-25). It has 36 features, including Telangana, Ladakh, J&K and the merged DNH&DD.
   - The shapefile was converted with a stdlib reader, simplified with Douglas-Peucker at 0.001° per ring and rounded to 3 decimals, giving 1.75 MB.
   - The simplification does not preserve topology, so slivers or gaps may appear between states. It is fine for choropleths but not for area calculations.
   - `name_std` matches all 36 rows of `state_baseline.csv` with no misses.

## Conflicts between sources
- **Wikipedia vs Census A-4 populations:** of the 299 Wikipedia cities matched, 274 have exactly the same population and 25 differ. For example, Wikipedia gives Chennai 6,748,026 (the expanded corporation area), while A-4 gives 4,646,732 (the 2011 boundary). Other gaps are small revisions between provisional and final figures, or city vs UA (Veraval, Chittoor, Panvel). **All populations in the outputs come from Census A-4 final.**
- **Census provisional (2011 PPT) vs final A-4:** the final figures differ slightly, for example Ludhiana 1,613,878 provisional vs 1,618,879 final. The provisional tables were consulted only as a check.
- **NCP vs Census for Telangana:** the NCP 2011 base for Telangana (13,731k) is 122k higher than the Census district split (13,608,665). AP agrees exactly. The NCP state values for 2026 sum to 513.0M, while its India total for 2026 is 515.2M.
- **Wikipedia list coordinates:** Mathura is misplaced in the list. Its coordinate was rejected.
- **HRA list:** this is the 2017 list, carrying forward the 2015 classification. Later reclassifications (for example reports about Mathura-Vrindavan) were **not verified**, so `tier_hra` may be out of date for some cities.

## Gaps
- 36 rows have no coordinates (mostly Delhi census towns, a few Chennai-UA CTs, Haldwani, Anklesvar, Dohad, Sunam, Shahade and Raghogarh). They are blank, not guessed.
- Districts are as of 2011, and many have been split since. Only Telangana, Ladakh and DNH&DD are re-mapped to current states.
- Populations are from 2011 only. There are no city-level projections, so nothing here is a 2026 city population.
- The A-1 household count was not reconciled with the HH-series normal households.
- Kerala and the Northeast show very high NCP urban growth (Kerala factor 1.85, DNH&DD 3.78). This is the report's census-town-driven URGD projection and was not checked independently.
- The Wikidata query service rate-limited our requests (HTTP 429). Name-based Wikidata matching was therefore partial, and those rows were filled from Wikipedia API and Nominatim instead.
