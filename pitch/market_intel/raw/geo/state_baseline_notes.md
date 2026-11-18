# state_baseline.csv: notes

Built 2026-11-18. There is one row for each of the 36 current states and UTs. `name_std` matches `india_states.geojson` (property `name_std`) and the `state` column of `cities_raw.csv`.

## Sources
- **Census 2011 urban population and urban households**: Census of India 2011, Table A-1 "Number of villages, towns, households, population and area" (final). Source: https://censusindia.gov.in/nada/index.php/catalog/42526 (source year 2011). Household counts are the A-1 "number of households". They were not reconciled with the HH-series normal-household counts, which may differ slightly.
- **Projected urban population for 2026**: Report of the Technical Group on Population Projections 2011-2036, National Commission on Population, MoHFW. The cover is dated November 2019 and the report was released in July 2020. The figures come from Table 9, "Projected urban population by sex as on 1st March, 2011-2036" ('000). Source: https://nhm.gov.in/New_Updates_2018/Report_Population_Projection_2019.pdf

## Interpolation
**None.** Table 9 tabulates every year from 2011 to 2036, so the 2026 value (as on 1 March 2026) is read directly from it. It is labelled PROJECTED, not Census. The report also has 1 July (Table 12) and 1 October (Table 15) versions. Those were not used. The 1 March date matches the Census reference date. The 2021 and 2031 values are kept for reference only.

## Derived fields (flagged DERIVED in the CSV)
- `census2011_avg_urban_hh_size` = urban population / urban households (A-1).
- `urban_growth_factor_2011_2026` = NCP 2026 / NCP 2011. Both values come from the same projection series, so boundary differences cancel out.
- `proj2026_over_census2011` = NCP 2026 (persons) / Census 2011 urban population (A-1). This is an alternative factor. For Telangana it differs from the growth factor (see below).
- `proj_urban_pop_2026` = NCP value in thousands × 1000. It is only precise to the nearest thousand.

## Boundary handling
- **Andhra Pradesh and Telangana**: Census 2011 had a single undivided AP (state code 28). The Census figures were split using A-1 district rows. Telangana is the 10 districts with codes 532-541 (Adilabad, Nizamabad, Karimnagar, Medak, Hyderabad, Rangareddy, Mahbubnagar, Nalgonda, Warangal, Khammam). Residual AP is the other 13 districts. These figures are DERIVED.
  - **Conflict:** The NCP 2011 base for AP is 14,610k, which matches the district split exactly. Its Telangana base is 13,731k, against 13,608,665 from the district split. The NCP AP and Telangana bases together come to 28,341k, against an undivided AP urban population of 28,219,075 in Census A-1. The roughly 122k gap was not resolved. One possibility is the 2014 transfer of Polavaram mandals, but that would move population from Telangana to AP, not add any. Use the in-series growth factor for Telangana.
- **J&K and Ladakh**: Ladakh = Leh (Ladakh) + Kargil districts. J&K = the rest of the 2011 state. These figures are DERIVED, and they match the NCP bases (3,371k and 62k).
- **Dadra and Nagar Haveli and Daman and Diu** (merged UT, 2020): the Census and NCP figures are both sums of the two former UTs (DERIVED). NCP projects very fast urban growth for them (factor 3.78 to 2026). This comes from the report and has not been verified.

## Checks
- The state Census urban figures sum to 377,106,125, which equals the India urban total in A-1.
- The NCP state values for 2026 sum to 513,014k, while the NCP India total for 2026 is 515,197k (a 0.4% gap). The report projects the India total separately, so its state values do not add up to it. Use the state rows for state work.
- Do not treat the 2011 figures as 2026. Only `proj_urban_pop_2026` and the growth factors refer to 2026, and both are projections.
