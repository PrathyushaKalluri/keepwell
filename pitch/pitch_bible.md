# Keepwell — Pitch Bible (the plan)

This document is **the plan for building the seed pitch deck**: the phases, the steps, what each step produces, and where it lives.
> **Illustrative case.** Founder histories, the company timeline, the pilot results and the financials are assumptions made for the IIIT Hyderabad ESFS course pitch. They are kept consistent with the team repo and with each other.
The work itself sits in one document per step in [`steps/`](steps/). The numbers sit in [`keepwell_model.xlsx`](keepwell_model.xlsx).

**Goal.** Pitch **Keepwell** to a lead seed VC and get funded.
- Circuit, the AI desk for repair agencies, is product 1 and the MVP.
- We are at **Stage 2, Finding a Business Model** (course M1).
- The pitch tells one personal, compelling story. Every claim is backed by data from our research or the repo, or by assumptions that are tagged and internally consistent.

---

## Status
| # | Step | Phase | Document | Model tabs it fills | Status |
|---|---|---|---|---|---|
| 0 | Repo reconciliation (reference) | — | [`steps/00_repo_reconciliation.md`](steps/00_repo_reconciliation.md) | — | Done 16 Nov |
| 1 | Vision and narrative spine | A | [`steps/01_vision_and_narrative.md`](steps/01_vision_and_narrative.md) | — | **LOCKED 16 Nov** |
| 2 | Founders and company backstory | A | [`steps/02_founders_and_backstory.md`](steps/02_founders_and_backstory.md) | Assumptions §10, §12 · Cap Table | **LOCKED 16 Nov** |
| 3 | Ecosystem map | A | [`steps/03_ecosystem_map.md`](steps/03_ecosystem_map.md) | feeds Step 8 cost lines | **LOCKED 16 Nov** |
| 4 | Market and problem scale | B | [`steps/04_market_and_problem.md`](steps/04_market_and_problem.md) | Market · Assumptions §2 | **LOCKED 16 Nov** |
| 5 | Product, fit and competition | B | [`steps/05_product_fit_competition.md`](steps/05_product_fit_competition.md) | — | **LOCKED 16 Nov** (slides in Step 12) |
| 6 | Traction and validation plan | B | [`steps/06_traction_and_validation.md`](steps/06_traction_and_validation.md) | Pilot · Assumptions §13 | **LOCKED 16 Nov** |
| 7 | Business model and unit economics | C | [`steps/07_business_model_unit_economics.md`](steps/07_business_model_unit_economics.md) | Revenue Build · Unit Economics · P&L and Cash · Sensitivity | **LOCKED 16 Nov** |
| 8 | Funding needs → the ask | C | [`steps/08_funding_needs_and_ask.md`](steps/08_funding_needs_and_ask.md) | Funding Need · Assumptions §8, §10 | **LOCKED 16 Nov** |
| 9 | Investor, instrument, valuation, cap table, exit | D | [`steps/09_deal_valuation_exit.md`](steps/09_deal_valuation_exit.md) | Valuation · Cap Table · Assumptions §11–12 | **LOCKED 16 Nov** |
| 10 | Compliance, trust and data room | D | [`steps/10_compliance_trust_dataroom.md`](steps/10_compliance_trust_dataroom.md) | Assumptions §8 (compliance spend) | **LOCKED 16 Nov** |
| 11 | Fundability self-score | E | [`steps/11_fundability_score.md`](steps/11_fundability_score.md) | Valuation (scorecard) | **LOCKED 16 Nov** (76/100) |
| 12 | Deck storyboard and investor red-team | E | [`steps/12_storyboard_redteam.md`](steps/12_storyboard_redteam.md) | — | **LOCKED 16 Nov** (review fixes applied) |
| 13 | Build the deck and outputs | E | [`steps/13_build_outputs.md`](steps/13_build_outputs.md) | Checks | **DONE 16 Nov** |

**How each step runs:** decide together → draft the step document → you edit → lock. The model inputs for that step are updated at the same time. Later steps build on locked earlier ones.

---

## Ground rules (apply to every step)
1. **Use the whole team repo, with no conflicting decisions.** Every decision cites `ESFS/keepwell/` where it speaks, and is researched and reasoned where it doesn't. See `steps/00_repo_reconciliation.md`.
2. **One source of truth.** Every deck number comes from `keepwell_model.xlsx`. Every claim comes from a step document.
3. **Tag every fact.**
   - **[Real]**: real research or build
   - **[repo]**: team repo
   - **[Story]**: assumed backstory or pilot fact
   - **[Model]**: modelled number

   The deck tells the story confidently. The tags are our private defence in Q&A.
4. **Course vocabulary.** Every slide maps to a fundability cell from M3 (Market / Product / Startup × Potential / Uniqueness / Quality, plus X-factor) and to one of the four pillars: Pitch, Business Model, Compliance, Data Room.
5. **Moat (locked).** Root-cause analysis plus a learning loop on verified repair outcomes. The machine record is the asset that compounds. Orchestration and the model itself are not the moat.
6. **Settled points.**
   - The MVP prototype was built on FastAPI + Claude. Production runs on Gemini on Vertex AI, Mumbai (Step 3).
   - Circuit is the product name.
   - Pricing: ₹40 per verified fix + optional ₹399 Desk Pro + 30 free days (Step 7).

---

## The plan, phase by phase

### Phase A: Who we are (story foundation)
- **Step 1, Vision and narrative spine.** Company vision and mission, the life-of-a-machine product map, why we start with Circuit, the moat, positioning, the 9-beat story spine, why now, X-factor.
- **Step 2, Founders and backstory.** Three founders (real names, ideal assumed bios), advisors and board, company timeline, money raised so far and instruments, cash and burn, clean-company checklist.
- **Step 3, Ecosystem map.** The course's (M1) five categories plus research institutes. For each: who, what they gave us (a USP or proof point), and what they still cost (a funding line). Covers investors, government (SISFS, DPIIT, NCH, CPCB EPR, BEE swap scheme, NSDC), incubators (CIE-IIITH, Google for Startups), professional enablers, networks and media, and research bodies (IIIT-H, Toxics Link, CEEW).

### Phase B: Why it's big and why we win
- **Step 4, Market and problem scale.**
  - A bottom-up TAM/SAM/SOM built from technicians and agencies (no official agency count exists), with ₹ revenue pools.
  - Platform pools for later lines: extended warranty, parts, resale, EPR.
  - Problem scale, and a low/base/high sensitivity.
- **Step 5, Product, fit and competition.**
  - Problem–market, problem–solution and founder–market fit.
  - Demo flow: Understand → Check → Triage → Quote → Prepare → Close out.
  - What is built and what comes next.
  - The North Star and its guardrails; human-in-the-loop tiers and safety hard-stops.
  - Competitor matrix (Servify, Bernard, Fieldproxy, Wiffy, ServiceOnDoors, Urban Company, Zoho, voice-AI firms), Porter's Five Forces, and how hard Circuit is to copy.
- **Step 6, Traction and validation plan.**
  - Pilot results (assumed, consistent with the repo's pilot design).
  - Leading and lagging metrics.
  - The experiments the seed funds, with kill conditions.

### Phase C: The engine
- **Step 7, Business model and unit economics.**
  - Who pays, why, how much and when, across revenue streams R1–R9 by release.
  - Pricing tests (the decision is deferred).
  - Unit economics: ARPA, cost per job by profile, contribution, CAC, payback, LTV.
  - 5-year P&L: gross margin, SG&A, EBITDA, D&A, EBIT, burn, break-even.
  - Sensitive parameters, with a tornado chart.
- **Step 8, Funding needs → the ask.**
  - Stage-2 requirements: pilots, focus groups, analytics, team, golden test sets, lexicons, manuals, safety sign-off, legal, compliance, marketing, working capital.
  - An 18–24-month budget by the course's five funding lanes (M1).
  - Gap = budget − revenue − cash − grants, which gives the ask.
  - Use of funds, and the milestones to Series A.

### Phase D: The deal
- **Step 9, Investor, instrument, valuation, cap table, exit.**
  - Why one lead seed VC (strategic people join as ESOP advisors).
  - The instrument: priced CCPS vs another iSAFE.
  - Valuation by the course's three methods (Comparable, Scorecard, VC method), with exit scenarios.
  - Cap table and dilution path, and the key terms we would accept.
  - Exit routes: Servify, OneAssist, Onsitego, Zopper, Asurion, Urban Company, Cashify, Attero, Recykal.
  - A target investor list.
- **Step 10, Compliance, trust and data room.**
  - DPDP roles and dates, data stored in Mumbai, consent.
  - IRDAI rules on selling plans, e-waste and refurbisher rules, CCPA dark patterns, the Consumer Protection Act, the legal-advice boundary.
  - Responsible-AI controls, the spend needed, and the data-room index.

### Phase E: Assemble and stress-test
- **Step 11, Fundability self-score.** Score ourselves on the 90 + 10 matrix. Every weak cell gets a fix or a slide.
- **Step 12, Storyboard and red-team.**
  - A slide-by-slide outline: ~12–15 slides plus an appendix.
  - Investor Q&A from the risk register: will agencies pay per fix, speech accuracy, AI price changes, made-up fields, competitors.
  - Founder rehearsal.
- **Step 13, Build the outputs.**
  - Animated web slides, plus .pptx and PDF exports.
  - The final financial model.
  - A proof pack chosen in Step 12, e.g. a voice-of-customer page, a Circuit demo walkthrough, an interactive unit-economics calculator, a data-room index.

---

## Outputs
| Output | File | Status |
|---|---|---|
| Plan | `pitch_bible.md` | this file |
| **The full story, end to end** | [`KEEPWELL_PITCH_STORY.md`](KEEPWELL_PITCH_STORY.md) | **done** |
| Step documents | `steps/00`–`13` | **all locked** |
| Financial model | `keepwell_model.xlsx` (rebuild with `build_model.py`) | **final**: 528 formulas, all checks OK |
| Deck (PowerPoint, PDF, animated web) | `deck/Keepwell_Seed_Deck.pptx` · `.pdf` · `.html` (rebuild with `deck/build_deck.py`) | **done**: 16 main + 16 appendix slides |
| Proof pack | `proof_pack/` | **done** |

## Verification (before the deck ships)
- **Model checks pass:**
  - use of funds = 100%
  - ask ≥ gap
  - cap table = 100%
  - seed shares × price = investment
  - iSAFE converts at its cap
  - SOM ≤ 20% of SAM
- **Traceability:** every deck number traces to the model, and every claim to a step document with a tag.
- **Coverage:** all 9 matrix cells, the X-factor and all 4 pillars appear in the deck.
- **Red-team:** a fresh reviewer plays a seed VC who is also a successful founder. We fix what they find.
