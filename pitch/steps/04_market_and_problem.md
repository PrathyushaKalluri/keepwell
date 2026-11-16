# Step 4 — Market and problem scale
**Phase B: Why it's big and why we win · Status: LOCKED 16 Nov 2026**
> **Illustrative case.** Founder histories, the company timeline, the pilot results and the financials are assumptions made for the IIIT Hyderabad ESFS course pitch. They are kept consistent with the team repo and with each other.
**Tags:** **[Real]** = real research · **[repo]** = team repo `ESFS/keepwell/` · **[web]** = checked online on 16 Nov 2026 · **[Model]** = calculated in `keepwell_model.xlsx` (Market tab) · **[DRAFT]** = assumption to validate.
**Plan:** [`../pitch_bible.md`](../pitch_bible.md) · **Builds on:** Steps 1–3 (locked) · **Model:** Market tab, Assumptions §2 · **Feeds:** Step 7 (volumes), Step 8 (milestones), Step 9 (valuation narrative)

## 4.1 How this step is built
**Course frame.** The M3 matrix scores **Market** on three things:
- **Potential:** TAM/SAM, growth, barriers to entry
- **Uniqueness:** underserved niches, policy tailwinds, a local edge
- **Quality:** sunrise vs sunset, global vs local, demand shifts

Our own Class Activity 4 set the rules we follow here:
- size the market bottom-up, not from a headline report
- don't mix GMV with revenue
- show every assumption
- show sensitivity
- keep SOM a small, believable share

**The problem with sizing this market.** The repo says plainly: *"No reliable national count of repair shops."* So we don't invent an agency count. We **build it from technicians** (a government estimate exists), convert it to agencies, and **cross-check it against repair jobs and the ₹ market**. Three independent sources have to agree.

## 4.2 How many agencies? (supply side)
| Line | Value | Source |
|---|---|---|
| Appliance and AC repair technicians in India | **~2.5 lakh** (range 2.0–3.7 lakh) | **[web]** ICAP (govt): *"about 2,00,000 AC service technicians… most in the informal sector"*. **[repo]** CEEW: skilled AC technician requirement ~0.37M. The base adds washing-machine and other appliance technicians to ICAP's AC/refrigeration figure |
| × share working in agencies of 2–10 technicians | 60% | **[DRAFT]** The rest are solo, brand-employed or platform partners. Validated in the 18 agency interviews (Step 6) |
| ÷ technicians per agency | 4 | **[repo]** persona: owner-run, 2–10 technicians |
| **TAM: repair agencies in India** | **~37,500** (low 20,000 · high 64,750) | **[Model]** |
| **SAM: agencies in Tier 2/3 towns** | **~22,500** | × 60% non-metro **[web]**: Blue Star ~70% of sales from non-metros; Redseer: Tier 2+ = 68% of incremental durables sales |
| **Beachhead: Tier 2/3 agencies in Telangana + Andhra Pradesh** (years 1–2) | **~1,400** | × 6.2% population share (TS ~3.8 Cr + AP ~5.3 Cr) **[Model]** |
| **Next ring: the four southern states** (years 2–3) | **~3,600** | × 16% population share (TS, AP, KA, TN) **[Model]** |

## 4.3 Does it hold? (demand-side cross-check)
| Line | Value | Source |
|---|---|---|
| Appliance repair jobs per year | **~15 crore (150M)** | **[repo]** ~150M appliances a year come in for repair (2017, single source) |
| Same figure from ₹ | ₹9,000 Cr ÷ ₹600 average bill = 150M | **[Real]** ₹9,000 Cr repair market. The ₹600 bill is **[DRAFT]**: it sits inside the ₹200–500 visit charge plus parts. *This shows the two figures are consistent at a ₹600 bill; it does not prove the bill* |
| Jobs done by local (independent) agencies | 44% → **6.6 crore** | **[repo]** LocalCircles: 44% use a local provider (up from 38%); 76% of AC owners avoid brand service |
| **Implied jobs per agency per month** | **~147** | 6.6 crore ÷ 37,500 agencies ÷ 12. **Lands inside the repo's own range (100 small, 250 mid)** |

**Result.** Three independent sources agree within the repo's own operating range:
- the technician count (government)
- the jobs count (repo)
- the ₹ market (ICICI/BlueWeave/Servify)

That makes the agency count defensible in Q&A even though no official count exists. The model uses the **observed median of our paying agencies, 125 jobs a month** (Step 6). The market average (~147) is upside, not modelled.

## 4.4 Revenue pools: what Keepwell can earn (not GMV)
The fee pool is shown at the repo's two R1 **test points, ₹40 and ₹100 per verified fix**. This sizes the market and is **not a pricing decision** (pricing is deferred to Step 7).

| Pool (₹ Cr a year) | Low | High | Basis |
|---|---|---|---|
| Circuit fee pool, **TAM** (every repair job × fee) | 600 | 1,500 | 150M jobs × ₹40 / ₹100 |
| Circuit fee pool, **SAM** (local-agency jobs in Tier 2/3) | 158 | 396 | 6.6 crore × 60% × ₹40 / ₹100 |
| Service Plans commission (R3), **appliances only** | 310 | 620 | Device protection ~₹10,340 Cr (Servify's estimate, ~$1.1B) × **~30% appliances** (the rest is mostly smartphones; validated in E7) × 10–20% **[repo]**. Selling on commission needs an **IRDAI-registered route** (a corporate-agent licence or a registered intermediary partner, Step 10) |
| Parts referral (R4) | 95 | 252 | ₹9,000 Cr × 35% parts share **[DRAFT]** × 3–8% **[repo]** |
| **Keepwell earnable pool (TAM)** | **~1,005** | **~2,370** | **≈ $107–252M a year, India only** (revised after the Step 12 review: appliances-only plans) |
| Not sized: claims triage (R5), lead routing (R6), resale and recycling (R9), data (R8) | — | — | No India claims count, refurb market or data pricing in the repo. Listed as upside, not counted |

**The investor reading.**
- **Circuit alone is a ₹158–396 Cr SAM.** That is a healthy niche, but on its own it is not venture-scale.
- **The platform is what makes Keepwell venture-scale.** Each machine record Circuit creates opens the plans, parts, claims and resale pools. This is exactly the story in Step 1: Circuit is the wedge, and the record is the business.
- The pool also excludes Tier 1 cities (repo Phase 2) and the one-pager's later categories (vehicles, homes).

## 4.5 SOM: how much we can realistically win, explained step by step
**What SOM means here.** SOM is the number of agencies we expect to actually pay us by year 5. It is not a market size; it is our plan. The test is simple:
> **SOM share of SAM = paying agencies in Y5 ÷ all Tier 2/3 agencies (SAM)**

**The 20% ceiling, and why.** This is our own sanity rule, not a course rule. We will not plan for more than **1 in 5** of all Tier 2/3 agencies paying us within 5 years:
1. **The agencies are informal and use almost no software.** The repo: WhatsApp and a phone only, "no dashboard on day one". Adoption is slow.
2. **Even the best-funded player hasn't got close.** Urban Company, after ~10 years and an IPO, averages ~54,347 monthly active professionals across *all* its categories in 51 cities **[repo]**. Appliance repair is ~2% of its serviceable market.
3. **The course flags "flimsy growth claims" as a red flag** (M3 business-model red flags). Our Class Activity 4 showed that a big TAM proves nothing about winnable customers.
4. **The old draft broke this badly.** 15,000 agencies ÷ the old SAM = 83%: almost every agency in the segment paying us. No investor would believe it.

At 20% of 22,500, the ceiling is **4,500 agencies**. The plan must sit below it.

> **Superseded by Step 7.** The capacity-derived plan is **79 / 264 / 945 / 2,196 / 3,793** paying agencies (Y5 = 16.9% of SAM, under the 20% ceiling). The table below is kept only to show why the ceiling rule was needed.

**The placeholder ramp, year by year.** These are *round placeholders I set*. They follow the repo's phasing (TS/AP → four southern states → national Tier 2/3) and stay under the ceiling. They are **not yet derived**; Steps 6–8 derive the real ramp.

| Year | Where we sell (repo phasing) | Paying agencies at year end | Agencies in that area | Share of that area | Share of national SAM (22,500) |
|---|---|---|---|---|---|
| Today | 2 pilot towns | 5 | — | — | 0.02% |
| Y1 | Telangana + AP Tier 2/3 (beachhead) | 80 | 1,395 | 5.7% | 0.4% |
| Y2 | Telangana + AP; **Series A gate (~120) crossed** | 250 | 1,395 | 17.9% | 1.1% |
| Y3 | Four southern states | 900 | 3,600 | **25%** ⚠ | 4.0% |
| Y4 | South + first states beyond | 2,000 | 22,500 (national) | 8.9% | 8.9% |
| Y5 | National Tier 2/3 | **3,500** | 22,500 | 15.6% | **15.6%** |

**How 15.6% is calculated.** 3,500 ÷ 22,500 = 0.156 = **15.6%**. That is under the 20% ceiling.

**What the table shows that we must fix later.** **Y3 is aggressive.** 900 agencies would be 1 in 4 of every Tier 2/3 agency in the south within three years. Steps 6–8 either lower Y3 or open new states earlier.

**How Steps 6–8 will derive the real ramp** (instead of round numbers):
> **New agencies per month** = field people × onboardings per person per month × the share that pays after the free days. Subtract churn. Then check: can the seed money pay for that many field people, and does the result still sit under 20% of SAM?

Each input comes from the pilot (Step 6) and the budget (Step 8), so the ramp becomes a result, not a guess.

## 4.6 Problem scale (numbers for the problem slide)
| Who | Number | Source |
|---|---|---|
| Whole system | **~15 crore repair jobs a year**; **~63% outside brand and platform networks** (only 24% use the brand and 13% an organised platform; 44% use a local provider) | **[repo]** jobs; **[Real]** LocalCircles AC servicing split |
| Agencies: wasted trips | **~3.45 crore repeat visits a year** if India matches the global 77% first-visit fix rate. **~₹159 per wasted trip** (pay ₹19,408/month ÷ 200 hours × ~1.1 hours + ₹50 travel), so **~₹550 Cr a year of wasted technician time** | **[Real]** global FTF and pay; **[DRAFT]** time lost and travel; **[Model]** total. *No India FTF rate exists*; the pilot measures it (Step 6) |
| Agencies: lost calls and intake chaos | Not measured anywhere; the repo's top-scored problem (P2, 24/30) | **[repo]**; the pilot measures it (Step 6) |
| Agencies: too few skilled hands | **~2 lakh RAC technicians, mostly informal**, against demand for skilled AC technicians rising from **~0.37M to ~2M by 2036-37** | **[web]** ICAP; **[repo]** CEEW |
| Agencies: parts | **Over half of technicians use non-original parts** | **[repo]** Toxics Link, Mar 2026 |
| Households: no recourse | **55%** had an inherently defective product; **only 21%** of those who acted got a refund or replacement | **[repo]** LocalCircles (self-selected) |
| Households: complaints | National Consumer Helpline: **12.36 → 13.16 → 20.49 lakh** complaints (FY24–FY26), **~30% via WhatsApp**. Consumer durables ranked **2nd** (77,873 complaints in 2024) | **[repo]** |
| Households: chasing | **47%** of 110 coded complaints are no-shows and chasing. In **7 of 12** repairs, the person deciding, approving, paying and opening the door were different people | **[Real]** case-comp research and survey |
| Machines with no history | **~27 crore** fridges, washing machines and ACs in Indian homes; no shared record exists for any of them | **[web]** ~33.5 crore households × fridge ~50%, washing machine ~20%, AC ~10–13% (Data for India 2024; CLASP/BEE 2024 survey; Ken Research). Corrected from the earlier 30 crore estimate |
| Runway ahead | **Only ~1 in 10 homes has an AC**; India will need **~5x more skilled AC technicians by 2036-37** (~0.37M → ~2M) | **[web]** CII-EY / Business Today; **[repo]** CEEW |
| Waste | E-waste **13.98 lakh tonnes** (FY25, +11.45%); 75–95% handled informally | **[repo]** CPCB; sources conflict on the informal share |

**Headline line for the slide (kept, corrected to 27 crore):**
> *"15 crore repairs a year. ₹550 Cr of wasted trips. 27 crore machines with no memory. And the 37,500 agencies that do the work run on a phone and a notebook."*

**Stronger options.** Each adds a human beat and a "why now" beat to the scale numbers. Every number is sourced or modelled above.

**Option A, "starts from zero"** (recommended: it echoes the Step 1 vision line, so the deck has one idea running through it)
> **"Every year, 15 crore Indian repairs start from zero."**
> *Sub-line:* ₹550 Cr lost to wasted trips · 27 crore machines with no memory · only 21% of families with a defective machine are ever made whole · and the 37,500 agencies doing the work run on one phone.

**Option B, "the ₹350 part"** (opens with our Ramagundam story; the most emotional)
> **"A ₹350 part. A ₹38,000 new AC. Between them sits a repair system with no memory."**
> *Sub-line:* 15 crore repairs a year · ₹550 Cr of wasted trips · 55% of families got a defective machine, only 21% got it put right.

**Option C, "the wave is coming"** (the growth and why-now pitch)
> **"Only 1 in 10 Indian homes has an AC. India will need 5x more AC technicians by 2037. Today's 2 lakh mostly work from a phone and a notebook."**
> *Sub-line:* 15 crore repairs a year already · ₹550 Cr of wasted trips · 27 crore machines with no memory.

**How to use them together.** Option B is the **opening story** (beat 2 of the spine). Option A is the **problem-slide headline**. Option C goes on the **"why now" / market slide**. Each number then appears once, where it does the most work, and the deck never repeats a stat.

**Two numbers to say carefully in Q&A:**
- **₹550 Cr:** "if India matches the global 77% first-visit fix rate". No India rate exists, and the pilot measures it.
- **37,500:** "our bottom-up count from the government technician estimate". No official agency count exists.

## 4.7 Market quality and uniqueness (the M3 cells)
| Cell | Our case | Source |
|---|---|---|
| **Potential** | ₹9,000 Cr repair market growing **8.18% a year** to ~$1.49B by 2030; a Keepwell earnable pool of ~₹1,005–2,370 Cr | **[repo]** BlueWeave; **[Model]** |
| **Uniqueness** | **Tier 2/3 is underserved.** Tier 3 durables sales grew **10%** vs 7% in Tier 1 (Q4 2024); first-time buyers; organised repair is thin. Urban Company and the OEM networks are metro-weighted. **Policy tailwinds:** Right to Repair portal, Repairability Index, DPDP Rules, Kigali HFC freeze (2028) | **[repo]**, **[web]** |
| **Quality** | **Sunrise.** Cooling demand rises ~8x by 2037-38 and 55% of installed ACs are under five years old, so the repair wave is still ahead. Local and sticky: households already choose the local agency (44%, up from 38%) | **[repo]**, **[Real]** |

## 4.8 Weak points, said before an investor says them
1. **The jobs figure (150M) is a single 2017 source.** It agrees with the ₹ market and the technician count, but it needs a fresh source. *Mitigation:* the pilot measures jobs per agency directly.
2. **"60% of technicians in agencies" and "4 per agency" are assumptions.** *Mitigation:* the 18 agency interviews (Step 6) report technician counts. The low case (20,000 agencies) still gives a 12,000-agency SAM.
3. **The ₹37,000 Cr extended-warranty figure is dropped.** We use Servify's ~$1.1B device-protection estimate, which is conservative and sourced.
4. **The parts share of the repair bill (35%) has no source.** *Mitigation:* ask parts wholesalers (Step 3 partner).

## 4.9 How it shows up in the pitch
- **Problem slide:** Option A headline plus its sub-line. The opening story uses Option B; the why-now / market slide uses Option C (see 4.6).
- **Market slide:** a funnel in agencies (37,500 → 22,500 → 1,400 beachhead → 120 at Series A) beside the ₹ pools (Circuit ₹158–396 Cr SAM → Keepwell ~₹1,005–2,370 Cr). Caption: *"Circuit is the wedge; the record is the business."*
- **Appendix:** the triangulation table (4.3) and the weak-points list (4.8).

---

## Decisions log (LOCKED 16 Nov 2026)
- **Market structure accepted:** TAM ~37,500 agencies (20,000–64,750) → SAM ~22,500 Tier 2/3 → beachhead ~1,400 (TS + AP) → next ring ~3,600 (four southern states). Earnable pool ~₹1,005–2,370 Cr a year (appliances-only plans, after the Step 12 review); Circuit SAM ₹158–396 Cr.
- **Y5 ceiling accepted:** paying agencies in Y5 ≤ 20% of SAM (≤ 4,500). The real ramp is derived in Steps 6–8 from capacity, funding and pilot conversion. Y3 in the placeholder ramp is flagged as too aggressive.
- **Headlines:**
  - **Opening story:** Option B, *"A ₹350 part. A ₹38,000 new AC. Between them sits a repair system with no memory."*
  - **Problem slide:** the original line, *"15 crore repairs a year. ₹550 Cr of wasted trips. 27 crore machines with no memory. And the 37,500 agencies that do the work run on a phone and a notebook."*
  - Options A and C are not used.
