# Team evidence extract: post-warranty appliance repair (demand side)

Extracted 2026-11-18 from the team's own research. Every number carries a file and line citation.

**Labels**
- **team primary (small sample)**: the team's own survey (n=19, 12 qualified) and interviews (6 household respondents across 7 call transcripts, 1 crew head, 1 mentor). Convenience sample, skewed 45+ and female, mostly Hyderabad and Visakhapatnam. It shows mechanisms, not prevalence. Don't write "X% of Indian households" from it (survey README line 45).
- **team primary, mentor opinion**: a single mentor's estimates. He was not reporting data from an agency.
- **team secondary**: figures the team collected from published sources. The original source is named as the team cited it. None of these were re-verified here.
- **excluded: illustrative**: pitch financials that the team made up for the storyline. Do not use them as evidence.

**Path keys** (relative to `/Users/Shared/Files From e.localized/Ken case comp/`)
- `EV/` = `ken-case-competition-2026/evidence/`
- `TR/` = `ken-case-competition-2026/evidence/Interviews/Transcripts/`
- `KW/` = `ESFS/keepwell/`
- `DIG` = `ken-case-competition-2026/EVIDENCE_DIGEST.md`

**Who the interview aliases are** (from DIG §3 and `EV/consent/CONSENT_LOG.md` lines 10-16)
- *6128maggi*: woman, lives alone, Bengaluru and Vizag.
- *Amma*: woman, Visakhapatnam, purifier case.
- *Rk Sir*: man, joint family, AC case.
- *Sai Kakki*: woman, Hyderabad, washing-machine case.
- *Sarala Aunty*: woman, working, manages properties in two other towns. Two calls.
- *Technician*: head of a carpentry crew of about 10 who passes jobs to other trades. He is not an appliance agency.
- *Vidya Sagar*: mentor.

**What the primary research does NOT contain.** Read this first. The survey did not ask about spend, repair frequency, appliance age, satisfaction or wait time. Its only rating is a 1-5 effort score. No interview gives technician jobs per day, jobs per month or payout per job. Rupee figures and frequencies come only from interviews, each with n=1.

---

## 1. Repair and breakdown frequency

| Parameter | Value | n / who | file:line | Label | Note |
|---|---|---|---|---|---|
| Arranged a repair, service or install in the last 6 months | 12 of 19 (7 screened out) | survey n=19 | `EV/survey/Ken2026_Survey_Responses_RAW.csv` col Q2, lines 2-20; `EV/survey/README.md:13` | team primary (small sample) | This is the screening question, not a breakdown rate |
| Type of incident | routine maintenance 5, degraded performance 3, stopped completely 1, part replacement 1, new install 1, water-inlet issue 1 | survey n=12 | CSV col "What was the situation"; `EV/survey/README.md:54` | team primary (small sample) | 5 of 12 were maintenance, not breakdowns |
| Appliance involved | washing machine 3, water purifier 3, AC 2, other home service 2, geyser 1, other kitchen 1; fridge 0 | survey n=12 | `EV/survey/README.md:53`; CSV col 4 | team primary (small sample) | No fridge incident in the sample |
| Same washing-machine error code came back after about a year | "like a year ago" | Sai Kakki, n=1 | `TR/Call Sai Kakki_260908_223212 - Transcript.txt:56` | team primary (small sample) | Repeat failure of the inlet. Hard water was the cause (DIG:51) |
| Repaired AC fixed only 60-70% after a foam wash | 60%-70% | Rk Sir, n=1 | `TR/Call Rk Sir_260909_132051 - Transcript.txt:64` | team primary (small sample) | About 1 month later it still works, but he expects the fault to return |
| Repair fails again within 2-3 days (named as the most annoying thing) | "coming two three days" | Rk Sir, n=1 | `TR/Call Rk Sir…:126` | team primary (small sample) | Qualitative, no rate |
| Rework rule: if the machine works 70-90%, a complaint gets a free revisit | 70-90% | Rk Sir, n=1 | `TR/Call Rk Sir…:134` | team primary (small sample) | — |
| AC faults seen from purchase in 2021 through the second year | bought 2021 | Rk Sir, n=1 | `TR/Call Rk Sir…:74` | team primary (small sample) | The transcript says "till 2033", which is likely a mis-transcription of 2023 |

## 2. Servicing frequency (AC service, RO filter)

| Parameter | Value | n / who | file:line | Label | Note |
|---|---|---|---|---|---|
| RO service visit | every 6 months | 6128maggi, n=1 (Vizag, hard water) | `TR/Call 6128maggi_260909_123351 - Transcript.txt:52`, `:74` | team primary (small sample) | Tied to water taste and hard water |
| RO filter (softening) change | every 2 years | 6128maggi, n=1 | `TR/Call 6128maggi…:52` | team primary (small sample) | — |
| RO filter change | every year | Sai Kakki, n=1 (Hyderabad hard water) | `TR/Call Sai Kakki…:64` | team primary (small sample) | In practice she services only "whenever the water purifier stops working" (`:114`) |
| RO re-service interval | "six months or in a year", depending on what the technician advises | Sai Kakki, n=1 | `TR/Call Sai Kakki…:136` | team primary (small sample) | — |
| RO AMC visits | twice a year: filter change plus cleaning. Has held this AMC for 5 years | Rk Sir, n=1 (Eureka purifier) | `TR/Call Rk Sir…:82` | team primary (small sample) | — |
| AC servicing pattern | the brand sent schedules for the first 3-4 services. Now a regular mechanic cleans filters before summer, and again when cooling drops or water drips | Rk Sir, n=1 | `TR/Call Rk Sir…:78` | team primary (small sample) | Roughly yearly before summer, plus on-failure visits |
| Seasonal AC service peak | Jan-Mar | mentor | `EV/Vidya Sagar transcript.md:1095` | team primary, mentor opinion | — |
| Next RO filter date written by hand on the machine | "NEXT 15/M/26" | photo caption | `EV/explanations.md:25-27` | team primary (small sample) | The household tracks the interval itself |
| Keeps no service record ("I don't track it, I just call when needed") | 7 of 12 | survey n=12 | CSV col Q14; `EV/survey/README.md:66` | team primary (small sample) | Multi-select question |

## 3. Spend per repair, visit charges and part costs (₹)

| Parameter | Value | n / who | file:line | Label | Note |
|---|---|---|---|---|---|
| AC chemical wash (dismantle) quote, Urban Company mechanic | ₹3,000-4,000 | Rk Sir, n=1 | `TR/Call Rk Sir…:64` | team primary (small sample) | Declined |
| Same job, cross-check through a friend's mechanics | ₹2,500-3,000 | Rk Sir, n=1 | `TR/Call Rk Sir…:64` | team primary (small sample) | Local quote is about 17-25% lower |
| Final price rose above the quote (foam-jet job, capacitor added) | qualitative | Rk Sir, n=1 | `TR/Call Rk Sir…:94-98` | team primary (small sample) | — |
| Tip asked for after an app-paid job | unquantified | Rk Sir, n=1 | `TR/Call Rk Sir…:126` | team primary (small sample) | — |
| Typical repair estimate, given as a range | "₹3,000 to ₹5,000" | Sai Kakki, n=1 | `TR/Call Sai Kakki…:88` | team primary (small sample) | Says the price "hikes every year… every service" |
| Charge for a second day or visit (Vizag) | ₹100-200 | 6128maggi, n=1 | `TR/Call 6128maggi…:58` | team primary (small sample) | Customer-paid, which offsets the agency's cost of a revisit |
| Part markup example: gas pipe | ~₹300 market vs ₹350 charged, plus ₹200 for coming "two days" | 6128maggi, n=1 | `TR/Call 6128maggi…:82` | team primary (small sample) | Also says ~₹400 for a part bought online ("in some app") |
| Mixer: repair vs new | ₹1,700 repair vs ₹2,400 new, so she replaced it | Sarala Aunty, n=1 | `TR/Call Sarala Aunty_260909_135058 - Transcript.txt:88` | team primary (small sample) | Repair cost was ~71% of the new price, so replace |
| Interviewer's price-check prompt | ₹1,000 (hypothetical) | Amma | `TR/Call Amma_260908_230414 - Transcript.txt:152` | n/a | Not a data point. She would check with neighbours and WhatsApp groups (`:154`) |
| Warranty on a replacement part | 3 months, so a duplicate can't be told from an original | Amma, n=1 | `TR/Call Amma…:177` | team primary (small sample) | — |
| AC warranty cost schedule | year 1 free; year 2 "minimal amount"; from year 3 regular charges | Rk Sir, n=1 (Lloyd AC) | `TR/Call Rk Sir…:74` | team primary (small sample) | — |
| Mentor's travel cost per trip | ₹50 each way, ₹100 round trip | mentor | `EV/Vidya Sagar transcript.md:203-207` | team primary, mentor opinion | Assumption, not measured |

## 4. Channel used

| Parameter | Value | n / who | file:line | Label | Note |
|---|---|---|---|---|---|
| First contact route | brand service centre 4; known technician 3; app (Urban Company or Housejoy) 2; society office or resident group 2; local shop 1; DIY 0 (not offered as an option) | survey n=12 | CSV col Q5; `EV/survey/README.md:55` | team primary (small sample) | Informal routes (known tech, shop, society) total 6 of 12 |
| By appliance | AC 2 of 2 via app; RO 3 of 3 via brand centre; washing machine 2 via known tech, 1 via brand | survey n=12 | CSV lines 2,5 (AC); 4,17,18 (RO); 3,13,20 (WM) | team primary (small sample) | Computed here |
| Society has a shared maintenance office | arrange it themselves 6; a bit of both 3; shared office or approved list 2; not sure 1 | survey n=12 | `EV/survey/README.md:56` | team primary (small sample) | — |
| Left the brand for Urban Company after franchise overcharging | — | Rk Sir, n=1 | `TR/Call Rk Sir…:74-76` | team primary (small sample) | "after a few calls like this I switched" |
| Rule of thumb: big or costly items (TV, AC, fridge) go to the company; others go to local people | — | Sarala Aunty, n=1 | `TR/Call Sarala Aunty_260909_135058…:100` | team primary (small sample) | — |
| Urban Company used only once the warranty has ended | — | mentor | `EV/Vidya Sagar transcript.md:635-639` | team primary, mentor opinion | — |
| Urban Company arrives within "a few hours or… within a day" | — | 6128maggi, n=1 | `TR/Call 6128maggi…:74` | team primary (small sample) | Bengaluru. Afterwards she took the UC technician's own number (DIG:123) |
| Instagram reels used to find and book a technician | — | Amma, n=1 | `TR/Call Amma…:140`, `:228` | team primary (small sample) | — |
| DIY first (tap leaks, drain cleaning, gas knob) | — | Amma, n=1 | `TR/Call Amma…:100` | team primary (small sample) | — |
| DIY or never called a professional (survey free text) | about 3 of 12 describe a self-fix or a community fix | survey n=12 | CSV col Q16, lines 2, 4, 13 | team primary (small sample) | Free text, coded loosely |

## 5. Satisfaction, ratings and effort

| Parameter | Value | n / who | file:line | Label | Note |
|---|---|---|---|---|---|
| Effort or hassle (1-5) | mean 2.17; 1→4, 2→4, 3→3, 5→1 | survey n=12 | CSV col Q15; `EV/survey/README.md:60` | team primary (small sample) | This is effort, not satisfaction. DIG:168 warns that it understates pain |
| Mean effort by channel | known tech 1.33 (n=3); brand centre 2.0 (n=4); app 2.0 (n=2); society 2.5 (n=2); local shop 5 (n=1) | survey n=12 | CSV cols Q5×Q15 | team primary (small sample) | Computed here. The cells are tiny |
| Most annoying parts | rude mechanics; home left dirty; tip demands; repeat failure within 2-3 days | Rk Sir, n=1 | `TR/Call Rk Sir…:124-126` | team primary (small sample) | — |
| Technicians taking money and not returning | "5 years before… now nothing like that" | Amma, n=1 | `TR/Call Amma…:172` | team primary (small sample) | — |

## 6. Wait times and follow-ups

| Parameter | Value | n / who | file:line | Label | Note |
|---|---|---|---|---|---|
| Promised time kept | kept 9; promised but broken 2; no clear time 1 | survey n=12 | CSV col Q11; `EV/survey/README.md:57` | team primary (small sample) | The 2 broken promises were a local shop (line 16) and a brand centre (line 17) |
| Follow-ups needed | none 6; 1-2 more 4; 3+ 2 | survey n=12 | CSV col Q12; `EV/survey/README.md:58` | team primary (small sample) | Follow-ups by route: app 0/2; brand 2/4; known tech 2/3; society 1/2; shop 1/1 |
| Brand purifier request still pending | 3 days, at more than 1 hour a day of her time | Amma, n=1 | `TR/Call Amma…:185`, `:197` | team primary (small sample) | Brand WhatsApp bot failure (DIG §5) |
| Known technician: reply, then visit | replied within half an hour; came the next day; one visit | Sai Kakki, n=1 | `TR/Call Sai Kakki…:38` | team primary (small sample) | Washing machine; brought the part |
| Brand helpline route | "a couple of days… waiting itself… a day or two" | Sai Kakki, n=1 | `TR/Call Sai Kakki…:104` | team primary (small sample) | — |
| AMC purifier technician | "will come within a day" | Rk Sir, n=1 | `TR/Call Rk Sir…:82` | team primary (small sample) | — |
| Urgent repair end to end | "half of the day or one day" | 6128maggi, n=1 | `TR/Call 6128maggi…:98` | team primary (small sample) | — |
| Mixer repair turnaround | "One hour maximum" | Sarala Aunty, n=1 | `TR/Call Sarala Aunty_260909_135058…:92` | team primary (small sample) | Translation is unclear |
| Revisit gap if the technician leaves to fetch parts | 2-3 days lost | mentor | `EV/Vidya Sagar transcript.md:25` | team primary, mentor opinion | — |
| Customers wait for even the simplest fault | at least 2-3 days | mentor | `EV/Vidya Sagar transcript.md:1233` | team primary, mentor opinion | — |
| Fridge down is tolerated in Oct-Dec | 2 days | mentor | `EV/Vidya Sagar transcript.md:1103` | team primary, mentor opinion | — |
| Some customers say waiting 2 days is fine | 2 days | Technician (crew head), n=1 | `TR/Technician - Transcript.txt:25` | team primary (small sample) | Triage by urgency |

## 7. Appliance age, ownership and warranty/AMC usage

| Parameter | Value | n / who | file:line | Label | Note |
|---|---|---|---|---|---|
| Keeps an annual contract (AMC) | 3 of 12 | survey n=12 | CSV col Q14 (lines 4, 11, 13); `EV/survey/README.md:68` | team primary (small sample) | — |
| Washing machine age | "more than five years", out of warranty | Sai Kakki, n=1 | `TR/Call Sai Kakki…:60` | team primary (small sample) | — |
| AC age and warranty | bought 2021; 2-year warranty; then took a 1-year brand AMC and did not renew it | Rk Sir, n=1 | `TR/Call Rk Sir…:74`, `:78` | team primary (small sample) | Moved to Urban Company or a regular mechanic |
| Purifier AMC tenure | 5 years, renewed each year | Rk Sir, n=1 | `TR/Call Rk Sir…:82` | team primary (small sample) | — |
| AMC held on purifier and ACs | yes (count not given) | 6128maggi, n=1 | `TR/Call 6128maggi…:74` | team primary (small sample) | — |
| Purifier still in warranty | yes | Amma, n=1 | `TR/Call Amma…:78` | team primary (small sample) | Uses the brand channel |
| Warranty "about 5 years" | ambiguous | Sarala Aunty, n=1 | `TR/Call Sarala Aunty_260909_135058…:104` | team primary (small sample) | The call was cut off, so unclear whether this is warranty length or appliance age |
| Renting instead of owning (Bengaluru) | fridge, washing machine, cot rented. Maintenance "10 rupees", item ~₹200 a month, mattress ~₹100 a month | 6128maggi, n=1 | `TR/Call 6128maggi…:32`, `:36` | team primary (small sample) | Rental repairs are free (DIG:112) |
| Typical warranty or guarantee length | 6 months to 3 years | mentor | `EV/Vidya Sagar transcript.md:763` | team primary, mentor opinion | — |
| Ownership count per household | not collected | — | — | gap | — |

## 8. Technician and agency volumes, payout, commission, travel

| Parameter | Value | n / who | file:line | Label | Note |
|---|---|---|---|---|---|
| Crew size | about 10 people | Technician (crew head), n=1 | `TR/Technician - Transcript.txt:25` | team primary (small sample) | Carpentry crew, not appliances |
| Commission on jobs passed to others | 10% | Technician, n=1 | `TR/Technician…:115` | team primary (small sample) | The only primary commission figure |
| Apprenticeship before working solo | 1-2 years | Technician, n=1 | `TR/Technician…:37` | team primary (small sample) | — |
| Size of a trade WhatsApp group | "10-20 people" | Technician, n=1 | `TR/Technician…:139` | team primary (small sample) | — |
| Household pays a carpenter-coordinator a commission | yes, amount not stated | Sarala Aunty, n=1 | `TR/Call Sarala Aunty_260909_135058…:64` | team primary (small sample) | — |
| Technicians per agency | "at least 5 agents" (typical) | mentor | `EV/Vidya Sagar transcript.md:219` | team primary, mentor opinion | — |
| Technicians are salaried, not paid by commission; kept busy 12 h a day (8 am-8 pm) | 12 h | mentor | `EV/Vidya Sagar transcript.md:1053-1067` | team primary, mentor opinion | — |
| Travel distance, town to village | 20-40 km; worst case 50 km | mentor | `EV/Vidya Sagar transcript.md:27`, `:31` | team primary, mentor opinion | — |
| Trips per job | best case 2; 3 with a wrong part | mentor | `EV/Vidya Sagar transcript.md:63-71` | team primary, mentor opinion | — |
| Target jobs per trip | 3-5 problems per trip | mentor | `EV/Vidya Sagar transcript.md:197` | team primary, mentor opinion | A goal, not current volume |
| Travel saving | ₹200 per technician per day; ₹1,000 a day for 5 technicians; ₹30,000 a month per agency | mentor | `EV/Vidya Sagar transcript.md:203-225` | team primary, mentor opinion | Arithmetic on assumed ₹100 round trips |
| Willingness to pay | ₹100 per successful one-visit resolution; "Percentages, these agencies will not play" | mentor | `EV/Vidya Sagar transcript.md:281`, `:319` | team primary, mentor opinion | — |
| AI cost per job | ₹40-50 | mentor | `EV/Vidya Sagar transcript.md:231` | team primary, mentor opinion | — |
| Festival load peak | from about 2 weeks before a festival | mentor | `EV/Vidya Sagar transcript.md:1075` | team primary, mentor opinion | — |
| Jobs per technician per day or month; payout per job | **not collected** | — | DIG:240-241 | gap | The digest lists agency economics as "Not evidenced" |

---

## 9. Survey tallies (computed with `python3 -I`, stdlib csv)

Source: `EV/survey/Ken2026_Survey_Responses_RAW.csv`. There are 20 lines (header plus 19 rows) and no multi-line cells, so CSV line N holds one respondent. `Ken2026_Survey_Response_Table.md` numbers these as R1 = CSV line 2 (Response_Table line 11), R2 = line 3 (Response_Table line 37), and so on.

- **n = 19**; **qualified = 12** (Q2 "Yes"); screened out 7 (CSV lines 6, 7, 9, 10, 12, 15, 19).
- **Cities, all 19 respondents:** Hyderabad 9; Visakhapatnam or Vizag 6; Bengaluru 2; Munich 1; Gandhinagar 1. Among the 12 qualified: Hyderabad 6, Vizag 4, Bengaluru 2. **Not one respondent is in a Tier 3 city.**
- **Age, qualified:** 45-54: 8; 35-44: 2; 25-34: 1; 65+: 1.
- **Gender, qualified:** woman 9, man 3.
- **Home, qualified:** rented 7, own 3, living with family 2.
- **Appliance:** washing machine 3, water purifier 3, AC 2, other home service 2, geyser 1, other kitchen 1.
- **Situation:** routine maintenance 5, degraded performance 3, stopped completely 1, part replacement 1, new install 1, water inlet 1.
- **Channel:** brand service centre 4, known technician 3, app (Urban Company or Housejoy) 2, society or resident group 2, local shop 1.
- **Channel by appliance:**

| Appliance | Brand | Known tech | App | Society | Shop |
|---|---|---|---|---|---|
| AC | 0 | 0 | 2 | 0 | 0 |
| Water purifier | 3 | 0 | 0 | 0 | 0 |
| Washing machine | 1 | 2 | 0 | 0 | 0 |
| Geyser | 0 | 1 | 0 | 0 | 0 |
| Other home service | 0 | 0 | 0 | 2 | 0 |
| Other kitchen | 0 | 0 | 0 | 0 | 1 |

- **Time promised:** kept 9, broken 2, none given 1.
- **Follow-ups:** none 6, 1-2 more 4, 3 or more 2.
- **Part or appliance moved elsewhere:** no 10, not sure 2, yes 0.
- **Effort (1-5):** 1: 4, 2: 4, 3: 3, 5: 1. Mean 26/12 = **2.17**. No median spend can be computed: **the survey has no spend question.**
- **Effort by channel:** known tech 1.33, brand 2.0, app 2.0, society 2.5, shop 5.0.
- **Tracking method (multi-select):** don't track or just call 7; saved phone contact 6; annual contract 3; WhatsApp chat 2; note or notebook 1.
- **Roles split across people (decision, cost, payment, access):** 7 of 12 split, 5 of 12 held by one person (`EV/survey/README.md:78-83`; not recomputed here).
- **One mismatch:** README line 39 lists age 45-54 = 9 for all 19 respondents. That is consistent with the 8 counted here among qualified respondents plus 1 among those screened out.

---

## 10. Secondary numbers the team already collected (team secondary, not re-verified)

| Parameter | Value | Team file:line | Original source as cited | Label / quality |
|---|---|---|---|---|
| AC owners not using manufacturer service | 76% (65% of those cite cost); about 2 in 3 say brand service costs 50%+ more than local vendors | `KW/reports/Appliance aftersales opportunities and problems.md:13`; `KW/Keepwell problems, scenarios and revenue streams.md:13` | LocalCircles poll, June 2022, ~22,000 responses (via ThePrint) | team secondary. Self-selected online poll |
| Technicians using non-original parts | over half | `KW/reports/Appliance aftersales…:13` | Toxics Link five-city study, 498-consumer survey (via Counterview) | team secondary, covered second-hand |
| Unorganised share of electronics repair | "over 80%" | `KW/reports/Appliance aftersales…:13` | Outlook Business | team secondary. Marked UNVERIFIED |
| Repairs per year in India | ~150M | `KW/reports/Appliance aftersales…:68` | YourStory 2017, single old source | team secondary, weak |
| Consumer-durables NCH grievances disposed | 49,066 (2023); 77,873 (2024); 38,885 (2025) | `KW/reports/Appliance aftersales…:11` | Rajya Sabha reply via search summary | team secondary. UNVERIFIED annexure |
| Platform commission on labour | ~20-30% | `KW/after-sales-mro-household-appliances.md:131` | none given (🟡) | team secondary, unsourced |
| Urban Company commissions and fees as a share of partner gross earnings | 28.3% (9M FY26) | `KW/research_notes/Household appliance aftersales MRO ecosystem/india_service_players.md:18` | Inc42. Inc42 notes this is not the overall take rate | team secondary |
| Urban Company top commission slab cut to | 25% (after the Oct 2021 protest; beauty category) | `KW/reports/Appliance aftersales…:31` | Business Today | team secondary. Not appliance-specific |
| India consumer-services take rate | 30.6% (2023) → ~36% (2026) | `KW/research_notes/…/india_service_players.md:19` | S&P Global, Apr 2026 | team secondary, forecast |
| Customers who book Urban Company only once | 45% | `KW/research_notes/…/india_service_players.md:20` | former executive quoted by TGN | team secondary, anecdotal |
| Urban Company Native RO filter renewals through UC | ~75% (early cohort) | `KW/research_notes/…/india_service_players.md:16` | UC management or IR | team secondary, company claim |
| Appliance repair share of Urban Company SAM | ~2% | `KW/research_notes/…/india_service_players.md:23` | IndiaInfoline | team secondary |
| Croma ZipCare AC AMC | ₹1,999 a year (list ₹2,499) | `KW/Keepwell competitive analysis and workarounds.md:88` | Croma product page | team secondary. A list price |
| AMC prices for AC, RO, washing machine or fridge (Urban Company, brand, local) | not found | `KW/research_notes/Keepwell scenario inputs outputs triggers/household_record_claims.md:77`; `KW/research_notes/Keepwell competitive landscape and architecture/competitors_scenarios_B_D.md:44` | — | gap |
| Extended-warranty or AMC attach rate | not found. Market size USD 4.40B (2025) per IMARC; USD 3.58B (2023) per Credence | `KW/research_notes/…/india_service_players.md:95-108` | IMARC, Credence | team secondary, vendor-grade |
| Market sizes | repair ~₹9,000-10,000 Cr; extended warranty ~₹37,000 Cr | `KW/Keepwell competitive analysis and workarounds.md:298` | one pager, vendor-grade | team secondary |
| Gig workers earning under ₹15,000 a month | ~40% of 12M (FY25) | `KW/research_notes/Appliance aftersales opportunities and problems/supply_side_problems.md:18` | Economic Survey 2025-26 (via Business Today) | team secondary. All gig work |
| Appliance worker earnings | skilled ~₹35,000 vs less experienced ~₹8,000 (a month, implied) | `…/supply_side_problems.md:22` | Toxics Link (secondary coverage) | team secondary. The sector pairing is ambiguous |
| Samsung India service network | 3,000+ touchpoints; 12,500+ engineers | `KW/reports/Household appliance aftersales MRO ecosystem.md:29` | Samsung India newsroom | team secondary, company-sourced |
| Durables growth, Q4 2024 | Tier 3 +10%, Tier 1 +7%, Tier 2 +6% | `KW/Keepwell problems, scenarios and revenue streams.md:10` | not named in that line (🟡) | team secondary |
| Urban Company AC repair that didn't hold | ₹9,500 (₹6,500 coil + ₹3,000 gas) | `EV/secondary_research/reviews/urban_company_trustpilot.txt:14`, `:18` | Trustpilot review, ~Sept 2026 | team secondary, anecdotal |
| Urban Company purifier filter swap wait | ~6 months | `EV/secondary_research/reviews/urban_company_pissedconsumer.txt:14` | PissedConsumer review | team secondary, anecdotal |
| Urban Company no-show after a ₹144 payment | ₹144 | `EV/secondary_research/reviews/urban_company_pissedconsumer.txt:46` | PissedConsumer review | team secondary, anecdotal |
| Urban Company cancellation deduction when the provider no-shows | 40% | `EV/secondary_research/reviews/urban_company_trustpilot.txt:70` | Trustpilot review | team secondary, anecdotal |
| Urban Company PissedConsumer aggregate | 1,357 reviews, 1.4 stars, 91% unfavourable | `EV/secondary_research/reviews/urban_company_pissedconsumer.txt:2` | PissedConsumer (via system_map.md) | team secondary. Self-selected |
| Gaps the team flagged | no measured rate for no-shows, wait times or repeat failures; no appliance-technician earnings survey; no Urban Company appliance commission; no count of agencies | `KW/reports/Appliance aftersales…:147`, `:157`; `KW/Keepwell problems, scenarios and revenue streams.md:15`, `:166` | — | gap |

---

## 11. Excluded: illustrative (do not use as evidence)

The pitch storyline invents these numbers. They are not measurements.

- "14 paying agencies · ~8,200 jobs · 71% → 83% one-visit · 96% captured · 62% → 78% accuracy · ~₹59k MRR · ~1.4% churn": `KW/pitch/KEEPWELL_PITCH_STORY.md:101`, `:150`; `KW/pitch/KEEPWELL_FULL_STORY.md:78`, `:358`, `:906`; `KW/pitch/steps/06_traction_and_validation.md:55`, `:61`, `:141`
- ₹30L iSAFE from 2 operator angels; "FixNear's 1,200 former partner technicians": `KW/pitch/steps/03_ecosystem_map.md:27`, `:32`; `KW/pitch/KEEPWELL_FULL_STORY.md:290`
- Pilot plan with 15-20 interviewed agencies; agencies assumed to do "3 jobs a day" (the team itself notes this is unsourced); ₹3.6 Cr a year for 1,000 agencies: `KW/Keepwell problems, scenarios and revenue streams.md:94`, `:123-124`
- Desk fee of ₹1,500 per agency a month; plan commission 15%; resale commission ~4%; stacked ceiling of ₹100-120 Cr: `KW/Keepwell problem map and scenarios.md:13`, `:114`, `:142`, `:201`
- ₹39 per verified fix (the team's own price point, compared with the mentor's ₹100): DIG:22
