# The discrepancy story: what a diligence reviewer finds in `pitch_v2/steps`

Scope: all 19 files in `ESFS/pitch_v2/steps/` plus the model code beside them (`ue_v2.py`, `unit_economics.py`, `model/plan_v3.py`). Four reviewers each read a slice and recomputed the numbers; a fifth fact-checked the rewritten story. Nothing in the step files was edited. Refs are `file:line`; files are abbreviated by number (e.g. `07b`), and `00_` files by name (TQ = tough questions, VR = validation report).

**Short answer to "are all of them good?": No.** The reasoning is good and the arithmetic is mostly right. The package fails on three things: the proof is fictional, the files contradict each other, and the later steps drifted away from the honest conclusions of the early ones.

---

## Chapter 1. What is good (so you know what to keep)

- **The logic.** Problem, wedge, per-job economics, weak-points section in every step. Coherent end to end.
- **The arithmetic.** Reviewers recomputed per-job contribution, the Protect plan, cluster bridges, the 8-year plan (reproduced exactly by `plan_v3.py`), use of funds, dilution, cap table and all investor-return multiples. They match their inputs. Only three small rounding mismatches (below).
- **`00_validation_report` (Gate 1)** is a rigorous, honest teardown. **`00_tough_questions`** is candid about what is unknown.
- **Disclosure.** The pilot's five red misses and the "AI is not the moat" stance are stated, not hidden.

## Chapter 2. The three big discrepancies

### 2.1 The proof is fictional
Every file says so itself ("illustrative case", `01:7`, `02:7`, `06:18`, VR line 3). Founder histories, the company timeline, the 34-shop pilot (~2,400 jobs, ₹25 L), the two brand authorisations, interview counts, and the money raised and spent are all [Story]. Worse, pilot results are "generated from the same model the pitch uses" (`06:18`), so they cannot validate that model. The only real evidence: third-party research and a household survey of 19 people (12 qualified) in Hyderabad and Visakhapatnam, collected *after* the pilot and outside its belt.

### 2.2 The later steps drifted away from Gate 1
Gate 1 (VR) said one thing; the steps after it said another, with no new evidence in between.

| Topic | Gate 1 / early files said | Later files say |
|---|---|---|
| **Ask and valuation** | ₹2 Cr at ₹10 Cr pre is "too rich" (VR:51); an angel would put ₹30 L into a ₹75 L-₹1 Cr round at ~₹6 Cr cap (VR:31) | ₹2.5 Cr at ₹10 Cr pre (S12:34, 09). Scorecard value only ₹8.2 Cr (S12:104) |
| **TAM** | ₹4,000 Cr "breaks", corrected to ~₹1,550 Cr (VR:43, 127) | ₹4,000 Cr again (04, 10, 11, 12) with a redefinition (9k to 45k shops), a 2.6x jump |
| **Brand authorisation** | "No brand has authorised you", the go/no-go gate (VR:61, TQ) | "In place [Story]" (10:12, 10:30, 12:77) |
| **Competition** | Onsitego is "the closest threat"; "untested, not disproven" (TQ:25) | Slide 9: "Nobody serves the independent shop" (12:31) |
| **Pilot timing** | First proof is a cluster through one summer, Mar-Jun 2027 (VR:201) | Pilot already ran Mar-Oct 2026 and "worked" (12:11) |
| **Margin** | A 15-20% contribution, density business (VR) | 14-16% mature cluster EBITDA (07b), driven by a Protect product Gate 1 never approved |
| **Desk fee** | Dropped (VR:62) | Still in TQ sections 8 and 9 (stale) |

### 2.3 The files contradict each other on core numbers
Any reviewer finds these in minutes.

| Number | Versions in the files | Which to use |
|---|---|---|
| **Breakeven shops per cluster** | 19, 22, 27, 30, 35, 36, 44 (00, 00c, 01, 05, 06, 07, 07b, VR) | ~35 at full ramp (06:31/53/139); 22 only for a mature cluster with Protect |
| **No-authorisation breakeven** | 50, 80, 188 (03, 05, VR) | Say which case each is: ~50 (S12), ~80 AC-only/F, 188 founders' design |
| **Units per shop per month** | 50, 60, 74, 80 (04, 00, 07b, 06, 00b) | 74 for pilot claims, 60 for planning |
| **Mature cluster EBITDA** | 5.2% (07), 10-12% (00c), 14-16% (07b) | 16.3% own / 14.1% partner (07b, final) |
| **Year 1 revenue** | ₹40 L (00) vs ₹2.4 Cr (07b) | 07b |
| **Year 7 revenue** | ₹115.5 Cr (00b), ₹81.5 Cr (07), ₹130.5 Cr (07b) | 07b |
| **Peak cash need** | ₹1.94 / 10.6 / 21.6 / 5.8 Cr across 00 / 00b / 07 / 07b | 07b, but see 5.3 |
| **AC install contribution** | ₹730 (00:39) vs ₹469 (07:81) | ₹469 (pilot mix) |
| **Shop acquisition cost** | ₹9.5k / ₹18k / ₹22k | One value, with its basis |
| **Routing kill threshold** | 40% (TQ) vs 50% (VR) | One value |
| **Protect attach** | 3.5% (08), 5% (07b stress), 6% (pilot test), 8% (07b BASE) | Lead with 5% |
| **Formula count** | 378 (07), 630 (07b), 679 (13) | One count |

---

## Chapter 3. File by file

Verdict key: **Good** = usable as is. **Stale** = superseded, risk of leaking old numbers. **Fix** = needs corrections before use. **Not usable as is** = core claims unsupported.

| File | Verdict | What is off |
|---|---|---|
| **00_tough_questions** | **Fix** (mostly good) | Desk fee still in sections 8-9 though VR dropped it. Retailer counts 5k/9k/18k vs VR's 30k/45k/70k. Calls the ₹8-15 Cr round "seed" while 12 calls ₹2.5 Cr "seed". CAC ₹18k vs ₹22k in VR. Routing kill 40% vs 50%. 12 questions in heading, 13 in table. |
| **00_unit_economics** | **Stale** (arithmetic right) | Recommended design E (desk fee, filler jobs) is replaced by 07/07b, which has no desk fee. Its 11.7x LTV:CAC falls to ~9x with red-team CAC/churn or without the desk fee. AC install ₹730 vs ₹469. No supersession banner. |
| **00_validation_report** | **Good**, but ignored | Its own open items (authorisation, TAM, valuation) stay open and later files do not follow it. Treats the pilot as future while others treat it as done. Says "Decided in Step 8" without showing the decision. |
| **00b_margin_and_vision** | **Stale** | 8-year plan (₹115.5 Cr Y7) superseded by 07b. Exit at 10x EBITDA vs 07b's 15x/25x. Says the exit is small without data layers; 00c says no data layer is needed. Uses 80 units/shop. Compares Keepwell EBITDA to Urban Company contribution. |
| **00c_service_value_and_pilot** | **Stale** (location decision still valid) | "10-12% from service alone", "breakeven at 30", "Y7 revenue ₹105 Cr" all superseded. Arithmetic error: 2,400 units a month over "50-70 shops" is really 30 shops at 80 units. Compares cluster EBITDA to Urban Company's company EBITDA. |
| **01_vision_and_narrative** | **Fix** | Body still says breakeven 30 shops and 10-12% EBITDA while the banner says 22 and 14-16%. Says "90-day pilot" vs 8 months. Protect missing from the four phases. HomeServe/Asurion analogy stretched. Calls it an "operating system" while the files describe a principal-model services operator. |
| **02_founders_and_backstory** | **Not usable as is** (for evidence) | Invented 8-10 year histories for named real people. Promises "letters of intent in Step 6"; Step 6 has none. iSAFE table wording wrong at ₹12 Cr pre (cap is better than the discount). ESOP created only at the next round (02:151). T-Hub/Google hub membership not on the timeline. Runway under 5 months. Founder "edges" under-delivered (authorisation 41% vs 45-50%, plan seller 70 vs 100). |
| **03_ecosystem_map** | **Fix** | Install payer stated three ways (03:68, 05:56, 06:128). Gig levy 1% (03:110) vs 1.4% of revenue vs up to 5% of payouts (03:24). Brand sub-contracts are non-exclusive 12-month terms from Nov 2025, so they lapse about now. |
| **04_market_and_problem** | **Fix** | TAM redefined 2.6x (₹1,550 Cr to ~₹4,000 Cr). Two methods disagree on AC share (86% vs 56%), "partly coincidence". BASE units 60 here, 80 in 06. "Outside metros" labelled Tier 2/3 includes rural. Counts installs as household spend. SOM is a plan, not bottom-up. |
| **05_product_fit_competition** | **Fix** | Says what brands pay is "still unknown" (05:56) while 06 marks it "answered". Breakeven 27 vs others. Protect appears as a banner, not integrated. Moat (exclusive multi-year shop agreements) has no signed example. Urban Company already in the pilot belt. |
| **06_traction_and_validation** | **Not usable as is** (as traction) | Pilot is model-generated, so it is circular. Says "5 red of 16"; the table has 17 rows. Technician maths does not close (below). Breakeven 35, units 80. Real survey post-dates the pilot. Authorisation 41% with one of two sub-contractors under-delivering. |
| **07_business_model_unit_economics** | **Stale** | Sections 7.4-7.7 superseded by 07b (Y7 ₹81.5 Cr, peak ₹21.6 Cr, 5.2%). Breakeven 36 shops. EBITDA sums to -₹6.1 Cr but cumulative cash is -₹21.6 Cr with no bridge. Says 378 formulas and 630 in the same file. |
| **07b_model_redesign** | **Good arithmetic, shaky inputs** | See Chapter 5. Approved date is 20 Nov 2026, later than today. Says the model "will be rebuilt after you approve" and "rebuilt" in different places. |
| **08_funding_needs_and_ask** | **Fix** | Arithmetic right. But: runway "18 months" in headline vs "month 21" in tables; model clock starts Jan 2027 while close is Feb-Mar; cash netted is a November figure (~₹2 L by March); milestones lenient; no tranching. See Chapter 6. |
| **09_deal_valuation_exit** | **Fix** | Arithmetic right. But valuation ~27x annualised revenue; exit multiples inconsistent with round pricing; terms investor-unfriendly in places. See Chapter 6. |
| **10_compliance_trust_dataroom** | **Fix** | Authorisation "in place [Story]" while Gate 1 lists it open. GST "model is built net" vs VR "prices must include GST". Protect legal opinion still outstanding yet 72 plans sold. Claims ledger "every number" vs 40 claims. |
| **11_fundability_score** | **Fix** | Self-scores inflated vs Gate 1's provisional matrix (Market 4/4/3 and Startup 13/13/9 vs "Medium"). Scores 13/15 for team on "600+ dealers, 200+ service centres" with no evidence. Says "cash-positive in BASE year 5" but 07b shows year-5 EBITDA +₹0.6 Cr and cumulative cash still -₹5.0 Cr. "2,150 records" vs 72 plans at 6%. |
| **12_storyboard_redteam** | **Fix** | "21 issues, all fixed" but the table lists 20 (6/8/6) and the fixes are self-asserted. 12 vs 13 questions. Pilot "worked [Story]". Slide 9 contradicts TQ on competition. Ask contradicts VR. |
| **13_build_outputs** | **Fix** | Claims `check_consistency.py` finds "0 problems", which this review disproves. Formula count (679) disagrees with 07b (630). Slide counts disagree with 12. |

---

## Chapter 4. Evidence the files treat as fact but should not

- **"600+ dealers, 200+ service centres"** as the unfair advantage (11:23, 12:32). VR:72 says the original backstory was rebuilt because the team had no retail-sales experience. No evidence is shown.
- **"41 of 64 owners said yes before we built anything"** (12:76): untagged, but sits in the story pilot.
- **"Authorisation: In place"** (10:12, 10:30, 12:77): two non-exclusive 12-month sub-contracts, one under-delivering, lapsing about now. TQ itself says "not proven".
- **"Protect is not insurance"** (10:10, 12:78): legal opinion not obtained.
- **"Our own repair data puts claims at ~27%"** (12:80): that "own data" is the story pilot.
- **Data layer at 7x revenue** (12:75): no comparable and no contracted buyer.
- **Exclusive multi-year shop agreements** as the moat: no signed example, no retention data.
- **Mature cluster 14-16% EBITDA**: no cluster has matured; it is extrapolated from a story pilot.
- **Model and QA claims** (679 formulas, 0 mismatches): cannot be checked from the files.
- **The brief calls it an "operating system for repair agencies"**: the files model a principal-model services operator (contribution 18-26%, service-only EBITDA ~0.2% in year 7) where agencies are paid partner operators. There is no SaaS fee anywhere (00b:40, 00b:55). An OS investor and a services investor price this very differently.

---

## Chapter 5. The model: right arithmetic, assumed inputs (07b)

The final plan (Y7 ₹130.5 Cr, EBITDA ₹8.6 Cr, peak ₹5.8 Cr) is carried by three assumptions added in 07b with no new evidence:

1. **Protect attach 8%.** No Indian benchmark (07b:38 says so). At the 5% stress case, a shop's Protect income falls to ~₹1,175 a month, below the old total income.
2. **Claims 35%.** Derived with an assumed 0.6 factor; 45% without it.
3. **Shop commission 25% on Protect**, with repairs cut to 3% and AMC to 8%. The shop earns more only because of Protect.

Further issues:
- **The ₹5.8 Cr peak uses Protect cash as a float.** Without plan cash it is ₹11.7 Cr; without Protect ₹17.5 Cr; stress ₹8.9 Cr; LOW case ₹57.7 Cr.
- **Mature revenue ₹249 Cr has no bridge:** 72 clusters x ₹2.72 Cr = ₹196 Cr. And "9.1% service-only" does not equal 21/249 = 8.4%.
- **Service-only EBITDA** is +₹0.3 Cr (0.2%) in year 7 and +₹3.1 Cr (1.9%) in year 8; the "healthy on its own" claim rests on a hypothetical maturity.
- **LTV, CAC, payback and churn were never restated** for the final model. Only the old 00 designs have them.
- **Exit multiples:** 10x EBITDA (00b), 15x and 25x (07b); the company is valued at 2.5-3x revenue, implying ~44-64x EBITDA.
- **Urban Company comparison** (07b:248) sets Keepwell EBITDA against Urban Company contribution.
- **Technician pay does not close (06:49 vs 03:68-71).** Per-job pay is ₹330-500, so "15 jobs a month ≈ ₹15k" is really ₹5-7.5k. Even full routing at 2.6 jobs a day (~65 jobs, ~₹26k) is an upper bound. The ₹1.5 L off-season floor top-ups imply core technicians earned near the floor.

---

## Chapter 6. The deal (08, 09)

**Arithmetic is right:** 1.08 + 0.84 + 0.52 = 2.44, rounded to ₹2.5 Cr; use of funds sums to ₹250 L; 2.5/12.5 = 20% dilution; the cap table sums to 100%; returns of 6.2x to 30.7x reproduce. Three small mismatches: "about 40%" dilution for ₹7.5 Cr at ₹10 Cr pre is really 43%; the year-7 stress value (₹255 Cr) needs ~11% data revenue, not 8-9%; the "25x EBITDA" cross-check gives ₹215 Cr, not ₹376 Cr.

**What a seed investor would object to:**
- **Valuation.** ₹10 Cr pre is ~27x annualised pilot revenue (~₹37 L, unaudited) and ~33x post. The ₹10.0 Cr comes from the founder-scored weighted-factor method that the file labels "cross-check only". The course scorecard gives ₹8.2 Cr. A 50% hurdle on the same VC method gives ~₹10.2 Cr post; 60% gives ~₹7.4 Cr.
- **Round pricing contradicts the exit.** The exit is valued at 2.5x revenue, but Round 2 prices at ~7x run-rate and Round 3 at ~5-6x. Round 3 investors would get ~1.06x in the stress year-5 exit.
- **Runway and calendar.** About 4.4 months of cash (to early April 2027). Headline says 18 months; tables say month 21. The model starts Jan 2027 but close is Feb-Mar, so "month 18" is ~15 months after the money arrives, leaving ~3 months to close Round 2. The Jan-Mar buffer sits at months 19-21 (Jul-Sep 2028).
- **Netting of cash.** ₹18 L is a November figure; by close it is ~₹2 L, so the true need is ~₹2.6 Cr, above the ask. Netting ₹0.10 Cr of Protect cash against the need contradicts ring-fencing it.
- **Milestones.** 150 shops at month 18 equals the stress count at month 12. "₹5 Cr earned since close" is below the plan's ₹5.1 Cr from January 2027. The pilot-cluster milestone is nearly met already (breakeven ~35, pilot has 34). Protect attach 3.5% (08) vs 5% (07b). The legal opinion is a month-18 milestone in 08 but due within 6 months in 11.
- **Round 3.** The stress peak need is ₹8.9 Cr, so the tail beyond seed and Round 2 is ~₹1.4 Cr, not ₹2.5 Cr (08:137 says ₹2.5 Cr; reconcile). BASE needs no Round 3.
- **Use of funds** does not map to the cost lines, and the ₹0.52 Cr buffer has no row.
- **Terms.** No tranching despite a month-12 kill rule (a founder promise with a 2-founders-to-1 board); about 40% of founder shares already vested; no redemption or put; "within 7 years" exit clause with drag only after year 7; a Series A template used for a seed (circular, since the course case is also the comparable); iSAFE ranking unclear.

---

## Chapter 7. Housekeeping

- 07b "approved 20 Nov 2026" is dated after today (19 Nov).
- 07b says the model will be rebuilt after approval, and elsewhere that it is rebuilt.
- 12 says "21 issues, all fixed"; the table lists 20.
- 12 says "12 hardest questions"; the table has 13.
- 12 says an appendix of 5 items; 13 says "12 slides + 3 appendix".
- 07 says 378 formulas and 630 formulas in the same file; 13 says 679.
- 06 says "5 red of 16"; the table has 17 rows.
- 02: the iSAFE table row says at ₹12 Cr pre the "cap (discount gives more)"; at ₹12 Cr the discount price (₹9.6 Cr) is above the ₹6 Cr cap, so the cap is better. Immaterial to the 7.5% result.
- 06, 02: T-Hub/Google hub membership (03:107) flagged "to be added to the Step 2 timeline" and never added.
- Stale files (00, 00b, 07) carry old numbers (₹115.5 Cr, ₹81.5 Cr, ₹21.6 Cr, 10-12%) that can leak into a deck.

---

## Chapter 8. What to do, in order

1. **Banner or archive the stale files** (00 sections 3-4, 00b sections 4-5, 00c headline numbers, 07 sections 7.4-7.7).
2. **Pick one value** for each row in 2.3 and apply it in every file.
3. **Relabel the evidence.** Pilot, authorisations, team networks and paperwork are [Story]; show the tag on the slide, or replace them with LOIs, a brand letter and ledger-backed numbers.
4. **Reconcile the ask to Gate 1:** tranche it, re-base the valuation, fix the calendar, sharpen the milestones.
5. **Resolve Protect first:** legal opinion, a real counter test, and no netting of plan cash.
6. **Fix the technician maths** and show real pay records.
7. **Re-derive TAM** bottom-up from pilot capture and drop the unreconciled ₹4,000 Cr as a headline.
8. **Restate LTV, CAC and payback** for the final model, and bridge ₹249 Cr.
9. **Soften the competition claim** and drop the HomeServe/Asurion analogy.
10. **Decide the category** (services operator vs software) and align the vision, moat and valuation to it.

The corrected, single-number-set version of the pitch is in `Keepwell seed story (reconciled).md`.
