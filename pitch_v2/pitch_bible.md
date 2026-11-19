# Keepwell v2: Pitch Bible (the plan for every step)

This is the master plan for building the Keepwell investor pitch for the retailer-led lifecycle idea. It lists every stage, every step document, what each one decides, what it feeds, and its status.

> **Illustrative case** for the IIIT Hyderabad ESFS course. The research is real and sourced. Founder histories, the timeline, the pilot results and the financials are assumptions, kept consistent across every document.

**Goal.** Pitch Keepwell to investors and get funded.
- **Stage:** Stage 2, *finding the business model* (course M1).
- **What sets the investor type, the ask and the instrument:** the unit economics and the costed needs (Steps 7–9). They are not set up front.

**Folder:** `ESFS/pitch_v2/`, pushed to the branch `pitch/keepwell-seed-deck` under `keepwell/pitch_v2/`.

**Old pitch:** the agency/Circuit version was **archived to `pitch/archive/v1_agency/` at Gate 3 (19 Nov 2026)**.

---

## How we work (ground rules)
1. **One document at a time.** I write one step, you approve it, then I write the next. Supporting data and code for that step can come with it.
2. **Every claim needs data or stated reasoning.** Every number carries a tag:
   - **[Real]**: our own evidence
   - **[R]**: research in `research/`
   - **[Model]**: `ue_v2.py`, later the xlsx
   - **[Story]**: assumed backstory or pilot facts
3. **The team's rough figures are references only.** Unit economics are rebuilt from evidence and re-run whenever the solution changes.
4. **Tough questions first.** Each step answers the investor, founder/operator, builder and sceptic questions in `steps/00_tough_questions.md` that belong to it.
5. **One source of truth.** Deck numbers come from the model (`ue_v2.py`, then `keepwell_model.xlsx`), and every claim comes from a step document. A claims ledger (`claims_ledger.csv`) tracks every promise.
6. **One name.** Keepwell is the only name; there are no product sub-brands. The technology is "Keepwell's AI service layer".
7. **Think about later rounds** in every funding decision (dilution, preference stack, cap table). **Never quote a placeholder number** as if it were decided.

---

## The pipeline

| # | Stage / step | Document | What it decides | Feeds | Status |
|---|---|---|---|---|---|
| **0** | **Validation (Gate 1)** | `steps/00_validation_report.md` | Whether the idea holds. The redesign: authorised installer; customers, brands and plan sellers pay; the shop is the source; one cluster through one summer | everything | **APPROVED 19 Nov** |
| 0a | Tough questions | `steps/00_tough_questions.md` | 45 questions from 4 perspectives, each answered or turned into a pilot test | Q&A, every step | APPROVED |
| 0b | Unit economics | `steps/00_unit_economics.md` + `ue_v2.py` | Evidence-based job, shop, cluster and company economics; the solution variants | Steps 4–9 | APPROVED |
| 0c | Margin and vision | `steps/00b_margin_and_vision.md` | 15–20% contribution is healthy for an operator. The 9 opportunities assessed. 8-year plan; exit in years 7–8 | Steps 1, 7–9 | APPROVED |
| 0d | Service value and pilot site | `steps/00c_service_value_and_pilot.md` | The five tests for a healthy service business. Pilot in Vijayawada–Guntur, then Warangal | Steps 2, 6 | APPROVED (location detail to be added from research) |
| **A** | **Who we are** | | | | |
| 1 | Vision and narrative spine | `steps/01_vision_and_narrative.md` | Vision, mission, tagline, the 4 phases (Serve, Supply, Know, Circulate), moat, narrative order, why now, candidate X-factor | Steps 2, 12 | **APPROVED 20 Nov** |
| 2 | Founders and company backstory (from scratch) | `steps/02_founders_and_backstory.md` | Three founders: retailer channel sales, field operations, AI. Advisors. Company timeline. Money raised so far. Clean-company checklist. The pre-seed instrument, with later rounds in mind | Steps 6, 8, 9, 10, 11 | **APPROVED 20 Nov** |
| 3 | Ecosystem map | `steps/03_ecosystem_map.md` | Partners and what each gives: AC brands and service centres, plan sellers (Onsitego/Zopper), exchange operators (Selsmart/Digi2L), parts distributors, recyclers, ESSC/Skill India, AP Startup Policy 4.0, T-Hub, Google | Steps 5, 8 | **APPROVED 20 Nov** |
| **B** | **The opportunity and the proof** | | | | |
| 4 | Market and problem scale | `steps/04_market_and_problem.md` | Bottom-up TAM/SAM/SOM across all four appliances: 30k / 45k / 70k independent shops; repair and service spend in Tier 2/3. The problem-scale numbers for the problem slide | Steps 7, 12 | **APPROVED 20 Nov** |
| 5 | Product, fit and competition | `steps/05_product_fit_competition.md` | How a job works end to end. The AI service layer. Problem–solution and product–market fit. Competition (Onsitego, 247around, SERVIZ, Jeeves, resQ, Urban Company, local mechanics). Porter's five forces. Defensibility | Steps 11, 12 | **APPROVED 20 Nov** |
| 6 | Traction and validation plan [Story] | `steps/06_traction_and_validation.md` | Backdated discovery (shops, technicians, households, brand talks). The 90-day Vijayawada–Guntur pilot and its results. Kill criteria. Series A gates | Steps 7, 8, 11 | **APPROVED 20 Nov (Gate 2 passed)** |
| **C** | **The money** | | | | |
| 7 | Business model and unit economics | `steps/07_business_model_unit_economics.md` + `steps/07b_model_redesign.md` + `keepwell_model.xlsx` (built by `build_model_v3.py`) | Revenue lines by phase. Contribution per job, shop and cluster. 8-year P&L and cash. Sensitivity. Low, base and high cases | Steps 8, 9, 13 | **APPROVED with 7b redesign; xlsx rebuilt on `plan_v3.py` (`build_model_v3.py`, 630 formulas, 0 errors, 0 mismatches)** |
| 8 | Funding needs to the ask | `steps/08_funding_needs_and_ask.md` | Costed needs minus revenue, cash and grants gives the amount. Round size, use of funds, milestones per round (first round, seed, Series A). The investor type follows the story stage | Steps 9, 12 | **FINAL: ₹2.5 Cr seed at ₹8 Cr pre, single close** |
| **D** | **The deal and the trust** | | | | |
| 9 | Investor, instrument, valuation, cap table, exit | `steps/09_deal_valuation_exit.md` | Investor type. Instrument (iSAFE / CCPS / note). Valuation by comparable, scorecard and VC methods. Cap table through Series A–B. Exit routes, buyers, comparables, returns (IRR vs the course benchmarks) | Steps 11, 12 | **FINAL: CCPS ₹8 Cr pre; cap table and returns in xlsx Funding sheet** |
| 10 | Compliance, trust and data room | `steps/10_compliance_trust_dataroom.md` | Labour codes and gig levies, consumer protection and the guarantee, DPDP consent, GST, safety (gas and electrical), insurance, brand authorisation contracts, e-waste rules, data-room index | Steps 11, 13 | **FINAL** |
| **E** | **Score, storyboard, build** | | | | |
| 11 | Fundability self-score | `steps/11_fundability_score.md` | M3 matrix (Market, Product and Startup × Potential, Uniqueness and Quality) plus the X-factor, with fixes for weak cells | Step 12 | **FINAL: 73/100** |
| 12 | Storyboard and investor red-team | `steps/12_storyboard_redteam.md` | Slide-by-slide storyboard (what we show / what we say). Two red-team passes and their fixes | Step 13 | **FINAL: storyboard + red team (21 fixes applied)** |
| 13 | Build the outputs | `steps/13_build_outputs.md` | The deliverables listed below | — | **DONE: see steps/13_build_outputs.md** |

**Gates:**

| Gate | When | What it decides |
|---|---|---|
| Gate 1 | After Step 0 | The idea and solution shape. **Passed** |
| Gate 2 | After Step 6 | The story and proof |
| Gate 3 | After Step 10 | Numbers and deal terms locked; the old pitch is archived |

---

## Final outputs (Step 13)

| Output | Location | Reuses |
|---|---|---|
| Seed deck (pptx / pdf / html) | `pitch_v2/deck/` | `pitch/deck/build_deck.py`, `deck_content.py` |
| Animated story deck, full version, plus script | `pitch_v2/story_deck/` | `pitch/story_deck/` engine (`deck_template.html`, `build_story_deck.py`, `script_data.py`) |
| Animated story deck, 10-minute version, plus script | `pitch_v2/story_deck_10min/` | same engine; `script_10min_full.py` pattern |
| Financial model (formulas, 0 errors) | `pitch_v2/keepwell_model.xlsx` | `pitch/build_model.py` patterns |
| Full story for outsiders | `pitch_v2/KEEPWELL_FULL_STORY.md` | — |
| Proof pack: investor Q&A, voice of the customer, demo walkthrough | `pitch_v2/proof_pack/` | `00_tough_questions.md` |
| Data room index | `pitch_v2/proof_pack/data_room_index.md` | Step 10 |
| Claims ledger | `pitch_v2/claims_ledger.csv` | every step |

**Media** (real household evidence, the landing page and video) stays git-ignored, because the repo is public.

## Verification before the pitch
- **Model:** the xlsx recalculates with 0 errors, and every deck number traces to a model cell or a claims-ledger row.
- **Course coverage:** a table maps each M1–M4 requirement and fundability cell to the step and slide that covers it.
- **Decks:** still-mode screenshots and contact sheets. Click counts match the script, and the short deck runs to about 10 minutes.
- **Consistency:** one script checks that founder facts, dates, money raised and every number agree across the steps, the model, the decks and the full story.
- **Red team:** every objection from the two passes is either answered or listed as a risk.

## Key facts so far (from Gate 1)
- **Problem:** the shop owns the trust but earns nothing after the sale and can be held jointly liable. Families get unguaranteed repairs. No appliance has a record.
- **Solution:** the authorised, guaranteed service arm for independent shops, covering AC (the anchor), washing machine, fridge and water purifier, run by certified partner technicians and the AI service layer.
- **Who pays:**
  - households (repair and AMC)
  - brands (installs)
  - plan sellers (fulfilment)
  - later, brands and retailers for data
- **Healthy service business:**

  | Measure | Value |
  |---|---|
  | Cluster breakeven | about 30 shops |
  | Mature cluster EBITDA | 10–12% |
  | Repeat and AMC share of revenue | 40%+ |
  | Payback on a ₹20 L cluster | under 24 months |

- **Scale (BASE):**

  | | Year 5 | Year 7 | Year 8 |
  |---|---|---|---|
  | Clusters | 28 | 65 | 90 |
  | Revenue | ₹40 Cr | ₹115 Cr | ₹164 Cr |
  | EBITDA | | 7% | 8% |

- **Peak cash need:** about ₹10.6 Cr.
- **Exit:** a strategic sale in years 7–8, valued at about ₹330–480 Cr.
- **Pilot:** Vijayawada–Guntur (with Mangalagiri and Tenali). Second cluster: Warangal.


## v2 status (19 Nov 2026): complete
- **The ask:** ₹2.5 Cr seed, CCPS at ₹8 Cr pre-money (23.8%), single close, 18 months from close, month-9 board checkpoint (Step 8 §8.4).
- **The roadmap:** Round 2 ₹5 Cr at ₹25 Cr pre (H2 2028); Round 3 ₹15 Cr at ₹70 Cr pre (2030); exit 2033–34.
- **Reconciled 19 Nov 2026** after an outside review (`steps/reviews/`): one canonical number set, the deal re-based, no real/illustrative tags.
- **Outputs:** all in `steps/13_build_outputs.md`.
- **Checks:** run `python3 check_consistency.py` before any edit to an output.


## v4 (19 Nov 2026, final): simple model and the 12-slide flow
- **One unit, the active retailer:**
  - A job is ₹1,580; a retailer is ₹19,500 a month (₹5,070 contribution); 20 retailers pay for a cluster.
  - The pilot made +₹1.9 L on ₹38 L of revenue.
  - The company is profitable from year 1 (Step 7c).
- **The ask:** ₹2.5 Cr CCPS at ₹10 Cr pre (20%), single close. Peak cash need ₹2.0 Cr; the only round needed to reach 1,000 retailers.
- **Fundability:** 89/100 (Step 11).
- **Outputs:** see Step 13. Earlier decks are in `archive_v3/`.
