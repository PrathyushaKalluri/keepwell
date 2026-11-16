# Step 6 — Traction and validation plan
**Phase B: Why it's big and why we win · Status: LOCKED 16 Nov 2026**
**Tags:** **[Real]** = case-competition research · **[repo]** = team repo `ESFS/keepwell/` · **[Story]** = assumed for the pitch, kept consistent with the repo and Steps 1–5 · **[Model]** = calculated in `keepwell_model.xlsx` (Pilot tab, Assumptions §13).
**Plan:** [`../pitch_bible.md`](../pitch_bible.md) · **Builds on:** Steps 1–5 (locked) · **Feeds:** Step 7 (pricing and unit-economics inputs), Step 8 (experiments and milestones the seed pays for), Step 11 (score)

## 6.1 How this step is built
**What Stage 2 investors look for.**
- **Course M1:** in "Finding a Business Model" the startup should *"pilot the MVP with target customers; refine pricing, unit economics, revenue model; collect customer feedback and validate segments; build early sales frameworks"*.
- **Course M3, Market–Quality:** paid demand, repeat behaviour, willingness to pay.
- **Our Class Activity 4 lesson:** *"a full score is earned by verifiable achievements, not by describing intentions"*, and evidence must be split into case facts, modelled numbers and hypotheses.

**What the repo prescribes.** This pilot is the repo's own validate-first list, run as written:
- **15–20 agency interviews.** We did 18.
- **A paid pilot with 3–5 agencies at ₹40 and ₹100 per fix.** We run 5 agencies.
- **Primary metric:** *"share of jobs closed with one visit, compared against each pilot agency's own prior record."*
- **Kill condition:** *"Agencies see no cost from repeat visits or prefer them."*

**Rule for this step.** The traction is **early, small and honest**: 4 weeks, 5 agencies. It includes one result that didn't go our way. Stage 2 investors trust a pilot that shows its weak spot more than a perfect one. Every number below is **[Story]** unless tagged otherwise. All of them stay inside the repo's ranges and the locked Steps 2–5.

## 6.2 What we learned before building the pilot: 18 agency-owner interviews (Oct 2026)
**Where:** Ramagundam–Peddapalli and Karimnagar. **How we reached them:** introduced by our trade network and the operator angels (Step 3).

| Finding | Result | Why it matters |
|---|---|---|
| How agencies take bookings | 16 of 18 use phone + WhatsApp only; **0 of 18 use any field-service software**; 11 of 18 keep a paper notebook | Confirms the repo persona: "WhatsApp and phone only; no dashboard on day one" |
| Requests lost today | Owners estimate **about 1 in 8 requests is lost**: calls missed while on a job, voice notes never followed up | Confirms the repo's top problem (P2 intake chaos, 24/30) |
| Size | Median **4 technicians** (range 2–9); median **125 jobs a month** (range 60–260) | **Validates the Step 4 assumptions**: 4 technicians per agency; ~147 jobs a month modelled |
| Repeat visits | **13 of 18 say a repeat visit for the same complaint is mostly unpaid**, so it is a cost. 5 of 18 charge for it | **Answers the repo's kill condition for most agencies.** The 5 who charge are not our first customers |
| Parts | 15 of 18 buy from 1–2 local wholesalers; **12 of 18 had a job delayed by a wrong or missing part in the last month** | Supports the "part to carry" step and the later R4 parts line |
| How they'd pay | **14 of 18 prefer paying per completed job**; 3 prefer a flat monthly fee; 1 won't pay for software | Matches the repo: "pay per job, not per seat" |
| What they'd pay | Median acceptable fee **₹30–50 per job**; only 4 of 18 accepted ₹100 | An early signal for Step 7. The pilot then tests it with real money |
| Data worries | 2 of 18 worried about sharing customer data | The consent-first design and DPA (Step 10) are needed |

## 6.3 Pilot design
| Item | Design | Source |
|---|---|---|
| Agencies | **5**: 3 in Ramagundam–Peddapalli, 2 in Karimnagar. Sizes: 2 small (2–3 technicians), 2 mid (4–6), 1 larger (8). **22 technicians** in total | Step 2 |
| Dates | Baseline logs from 6 to 19 Oct (agency's own record). Live from **20 Oct 2026**. **4 weeks of data** at the raise | Step 2 timeline |
| Price arms | **Arm A, ₹40 per verified fix: 3 agencies. Arm B, ₹100: 2 agencies**, matched by size | Repo pilot design |
| Paid from day 1 | **Yes.** This is a paid pilot (repo). The 30 free days (Step 7) apply only to the post-seed rollout | Repo + Step 7 |
| What's live | R1 core loop (A1, A2, A3, A6, A4, A9) on WhatsApp, on Gemini (Mumbai), **plus root-cause ranking (A5) in beta as a technician-only hint and owner-approved quote drafts (A7)**. Interim safety: the hazard list was reviewed with a certified technician before go-live, with full expert sign-off funded by the seed | Step 5 |
| Measured against | Each agency's own two-week baseline, not a global benchmark | Repo primary metric |

**Limit, said plainly.** Five agencies and 4 weeks give a **signal, not proof**. Splitting 3 vs 2 agencies by price can't separate price from agency differences. That is why the seed's first experiment (E1, 6.6) scales this to 30+ agencies.

## 6.4 Pilot results after 4 weeks [Story]
| Metric | Result | Gate / reference | Read |
|---|---|---|---|
| **Jobs handled by Circuit** | **~410** (share of each agency's jobs routed through Circuit: 45% in week 1 → **85% in week 4**) | — | Owners moved their work onto it without being pushed |
| **Requests captured as jobs** | **96%** of inbound WhatsApp requests became a job record; median **6 minutes** from voice note to job card | Repo P2 | The lost-requests problem (1 in 8) is largely closed |
| **One-visit closure** (primary metric) | **71% → 84%**, +13 points vs the agencies' own baseline (weeks 3–4) | Global benchmark 77% **[Real]** | Early: ~400 jobs. Must hold at scale (E2) |
| **Root-cause top-3 hit rate** (A5 beta) | **62% in week 1 (n≈40 verified jobs, ±15 pts) → 74% in week 4 (n≈125, ±8 pts)** | Gate 75% **[repo]** | **Just below the gate, and rising.** Honest split: about half the gain came from adding manuals for the most common AC and fridge models, about half from reviewed verified outcomes. E2/E4 test it at scale |
| **Verified fixes** | **82%** of routed jobs verified by the technician | Model: 80% billable | Verification is the moat event, and technicians do it |
| **Telugu speech** | Word error rate **21%** raw on agency voice notes, **15%** after vernacular-lexicon corrections; abstain rate **18%** | Abstain band 10–25% **[repo]**; IndicWhisper Telugu ~28.8% **[repo]** | Good enough with read-back and abstain; the lexicon is improving it |
| **Owner override rate** | **12%** of drafts edited | Band 5–20% **[repo]** | Owners review, not rubber-stamp |
| **Safety** | 9 hard-stops triggered in the field (gas, refrigerant); **0 false-accepts** on the 200-case red-team set | Zero tolerance **[repo]** | The hard-stop layer works |
| **AI cost per job** | **~₹3.1** measured | Repo modelled ₹1.5–5.5 (2026 prices) | Inside the modelled range; Step 7 budgets at 2027 prices |
| **Machine records created** | **~180**, household consent rate **74%** | Model: 70% consent | Home Memory is filling itself from repairs |
| **Paid invoices** | **5 of 5 first fortnightly invoices paid on time by UPI; ~₹20,000 billed in 4 weeks** | — | Agencies pay real money, small but real |
| **Agencies still active at week 4** | **5 of 5** | — | — |
| **Owner sentiment** | 4 of 5 owners would be "very disappointed" if Circuit went away | Sean Ellis PMF test: ≥ 40% | n = 5, a signal only |

**The result that didn't go our way: the ₹100 arm.**
- In arm B (₹100), **one of the two agencies cut its routed jobs to about half** in week 3. The owner said the fee "takes too much of a small job".
- Arm A (₹40) kept rising in all three agencies.
- **We show this openly.** It's what the pilot was for, and it feeds the Step 7 pricing decision.

## 6.5 Does the agency get more than it pays? (Pilot tab in the model)
Per median pilot agency per month **[Model on Story inputs]**:

| Value lever | Calculation | ₹ a month |
|---|---|---|
| 1. Recovered jobs | 125 jobs × 8% recovered = 10 jobs × ₹240 agency margin | **₹2,400** |
| 2. Repeat trips avoided | 106 routed jobs × 13-point gain = ~14 trips × ₹159 per wasted trip (Step 4) | **₹2,200** |
| 3. Owner time saved | 0.75 hours/day × 26 days × ₹150/hour | **₹2,925** |
| **Total value to the agency** | | **~₹7,500** |
| Our fee at ₹40 per verified fix (~87 verified fixes) | | ₹3,485 → **value ≈ 2.2x the fee** |
| Our fee at ₹100 per verified fix | | ₹8,713 → **value ≈ 0.86x the fee (the agency loses money)** |
| Fee at which value is exactly 2x the fee | | **~₹43 per verified fix** |

**What this says (input to Step 7; pricing is not decided here):**
- **Per-fix pricing works near ₹40, not at ₹100**, for a median agency. **At full routing** (all 145 jobs of a modelled agency through Circuit), value is ~₹8,700 against a ₹4,856 fee: **~1.8x, a net gain of ~₹3,850 a month**. The pilot's 2.2x is at 85% routing.
- The biggest value levers are **recovered jobs and owner time**, not only fewer trips. So the sales pitch to agencies leads with *"never lose a request again"*, which is also the repo's top problem (P2).
- This answers the repo's risk #1 ("fewer revisits cut their own fee"): even with no saved trips, recovered jobs plus owner time (~₹5,300) exceed the ₹40-arm fee.

## 6.6 What the seed pays to prove: the validation plan (next 18 months)
| # | Experiment | Hypothesis | Measure | Success | Kill / pivot condition | Repo link |
|---|---|---|---|---|---|---|
| E1 | **Price and willingness to pay at scale** | Agencies pay per verified fix when value ≥ 2x the fee | 30+ agencies, 3 towns, randomised price arms (the pricing options set in Step 7) | ≥ 70% still paying after month 2; value/fee ≥ 2x | < 40% convert → move to the hybrid or desk-fee option | Risk #1 |
| E2 | **First-visit improvement holds at scale** | One-visit closure rises ≥ 10 points vs each agency's own baseline | ≥ 3,000 jobs | +10 points sustained over 3 months | < +3 points → reposition around intake and owner time | Primary metric |
| E3 | **Repeat-visit economics** | Most agencies see repeat visits as a cost | Share of agencies charging repeat visits | ≥ 70% see a cost | Most prefer revisits → lead only with recovered jobs | Kill condition |
| E4 | **Language and safety** | Accuracy holds across Telugu, Hindi and Tamil | Word error rate per language; red-team safety | ≤ 10-point gap between languages; 0 safety false-accepts | Any safety false-accept → pause rollout | Risk #2, #4; guardrails |
| E5 | **Acquisition channel** | Our network and parts wholesalers bring agencies cheaply | CAC by channel (network, wholesalers, technician referral) | CAC payback ≤ 6 months (Step 7) | A channel above the CAC cap → stop it | — |
| E6 | **Household consent and Home Memory** | Households consent and engage with their record | Consent rate; reminder open rate | Consent ≥ 65%; reminders opened ≥ 40% | Consent < 50% → redesign consent before R2 | R2 precondition |
| E7 | **R2/R3 buyer discovery** | Warranty administrators want our claim evidence and plan channel | 2 administrator/OEM interviews (repo) → 1 letter of intent | 1 LOI signed | No interest → R2 plans first, delay R3 | "Two interviews before building C" |
| E8 | **Cost per job at 2027 prices** | Unit cost stays far below the fee | AI + messaging cost per job after the 1 Jan 2027 price change | ≤ ₹10 per job | > ₹10 → route more to Flash-Lite | Risk #8 |

## 6.7 Series A gates (what "done with Stage 2" means)
| Gate | Target | Source |
|---|---|---|
| Paying agencies | **~120** | One-pager |
| Household machine records | **~40,000** | One-pager. In the plan, records accumulate from all agencies: 28,000 by month 12, **40,000 by month ~13** **[Model]** |
| One-visit closure | **≥ +10 points** vs own baseline, sustained 3 months | Repo primary metric |
| Agency retention | **≥ 97% monthly** after month 3 | Matches the model's 3%/month churn |
| Value to the agency | **≥ 1.5x the fee and a net gain ≥ ₹3,000 a month** | 6.5 (at full routing: ~1.8x, ~₹3,850) |
| CAC payback | **≤ 6 months** | Step 7 |
| R2/R3 buyer signal | **1 administrator LOI** | E7 |
| North Star | Verified first-time-right jobs per active agency per month, trending up | Repo §3 |

These gates become **the milestones the seed buys** in Step 8.

## 6.8 What we track
- **Leading, daily** (repo): abstain rate, validator fail rate, speech disagreement rate, quote edit rate, time to close-out, cost per job, WhatsApp delivery.
- **Lagging, monthly** (repo): revisit rate, North Star, agency retention and jobs per agency, dispute rate, gross margin per job, agency NPS.

## 6.9 Weak points, said before an investor says them
1. **Small and short:** 5 agencies, 4 weeks, ~410 jobs. *Answer:* it's a design-partner pilot. E1/E2 scale it to 30+ agencies and 3,000+ jobs.
2. **Price arms confounded with agency:** 3 vs 2 agencies. *Answer:* E1 randomises at scale.
3. **Root-cause hit rate is below the 75% gate (74%).** *Answer:* it's rising weekly from verified outcomes. That *is* the moat, visible.
4. **The ₹100 arm underperformed.** *Answer:* that's the pilot doing its job. Pricing is set from it in Step 7.
5. **Owner-time value is self-reported.** *Answer:* E1 measures time to close-out directly from system logs.

## 6.10 How it shows up in the pitch (final choices in Step 12)
Available material:
- a traction strip (410 jobs · 96% requests captured · 71% → 84% one-visit · 5 of 5 active · 5 of 5 first invoices paid)
- the learning-curve chart (root-cause hit rate 62% → 74% by week)
- the value-vs-fee bar (₹7,500 value vs ₹3,485 fee)
- the 18-interview findings
- the validation-plan table
- the Series A gates

Cells covered: Market–Quality (paid demand, willingness to pay), Product–Quality (one-visit closure, safety, accuracy), Startup–Potential (the learning loop proven early).

---

## Decisions log (LOCKED 16 Nov 2026)
- **Accepted:** the 18-interview findings, the pilot design and 4-week results (including the ₹100-arm result), the value-to-agency model (~₹7,500/month; 2.2x at ₹40, 0.86x at ₹100), experiments E1–E8, and the Series A gates.
