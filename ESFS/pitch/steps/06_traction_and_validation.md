# Step 6 — Traction and validation plan
**Phase B: Why it's big and why we win · Status: LOCKED 16 Nov 2026 (rewritten for the backdated timeline)**
> **Illustrative case.** Founder histories, the company timeline, the pilot results and the financials are assumptions made for the IIIT Hyderabad ESFS course pitch. They are kept consistent with the team repo and with each other.

**Tags:** **[Real]** = real research · **[repo]** = team repo `ESFS/keepwell/` · **[Story]** = assumed pilot fact · **[Model]** = `keepwell_model.xlsx` (Pilot tab, Assumptions §13). **Measured** = from system logs · **Self-reported** = from owners.
**Plan:** [`../pitch_bible.md`](../pitch_bible.md) · **Builds on:** Steps 1–5, Step 2 timeline · **Feeds:** Step 7 (inputs), Step 8 (milestones), Step 11 (score)

## 6.1 How this step is built
**What Stage 2 investors look for.**
- **Course M1:** "pilot MVP with target customers; refine pricing, unit economics, revenue model; collect customer feedback and validate segments; build early sales frameworks".
- **M3, Market–Quality:** paid demand, repeat behaviour, willingness to pay.
- **Our Class Activity 4 lesson:** *"a full score is earned by verifiable achievements, not by describing intentions."*

**What the repo prescribes.** This follows the repo's validate-first plan, run in order:
- 15–20 agency interviews (we did 18)
- a paid pilot with 3–5 agencies at ₹40 vs ₹100 per fix (we ran 5)
- the primary metric: *"share of jobs closed with one visit, against each agency's own prior record"*
- the kill condition: *"agencies see no cost from repeat visits or prefer them"*

**Rule for this step.**
- Lead with **measured** numbers, and label self-reported ones.
- Show the result that went against us.
- Keep every number inside the repo's ranges and the Step 2 timeline.

## 6.2 Discovery before building (Jan–Apr 2025)
**Households [Real data; dated to 2025 in the story]**

The research:
- a household survey: 19 responses, 12 qualified
- 7 consented household interviews

What it found:
- In **7 of 12** repairs, the person deciding, approving, paying and opening the door were not the same.
- **7 of 12** households keep no service record.
- **47%** of 110 coded public complaints are no-shows and chasing.
- **The insight:** *nothing in a repair can be checked, so people trust the person* (Step 1).

**18 agency owners, Ramagundam–Peddapalli and Karimnagar [Story]:**

| Finding | Result | Why it matters |
|---|---|---|
| How agencies take bookings | 16 of 18 phone + WhatsApp only; **0 of 18 use field-service software**; 11 of 18 keep a notebook | Confirms the repo persona |
| Requests lost today | Owners estimate **~1 in 8** (missed calls, unanswered voice notes) | Confirms the repo's top problem (P2, 24/30) |
| Size | Median **4 technicians**, **125 jobs a month** (range 60–260) | Validates Step 4; becomes the model's jobs input |
| Repeat visits | **13 of 18: mostly unpaid**, so a cost; 5 of 18 charge for them | Answers the repo's kill condition for most agencies |
| Parts | 12 of 18 had a job delayed by a wrong or missing part last month | Supports "part to carry" and later R4 |
| How they'd pay | **14 of 18 per completed job**; median acceptable ₹30–50; 4 of 18 accept ₹100 | Matches the repo: "pay per job, not per seat" |
| Data worries | 2 of 18 | Consent-first design (Step 10) |

## 6.3 What we ran, and when
| Phase | When | What |
|---|---|---|
| Design partners | Jun–Sep 2025 | 2 agencies use the prototype free and shape it |
| **Paid price-test pilot** | **Feb–Apr 2026** | **5 agencies** (3 Ramagundam–Peddapalli, 2 Karimnagar; 22 technicians), **arm A ₹40 per verified fix (3 agencies) vs arm B ₹100 (2)**, paid from day 1 (repo design). Measured against each agency's own 2-week baseline |
| **Founder-led expansion** | **May–Oct 2026** | All on ₹40. **5 → 14 paying agencies** (+Warangal). 15 onboarded in total, 1 churned. The COO closed 8 of the 10 new agencies part-time; 2 came by agency referral |
| What's live | since Jan 2026 | R1 core loop on WhatsApp and Gemini (Mumbai). **Root-cause ranking (A5) live from Mar 2026 as a technician-only hint**; verified outcomes reviewed weekly before entering Mistri Gyan. Quote drafts (A7) that owners approve. Hazard list reviewed with a certified technician before go-live |

## 6.4 Results as of Nov 2026 [Story]
| Metric | Result | Type | Read |
|---|---|---|---|
| **Paying agencies** | **14** (15 onboarded, 1 churned) | Measured | **~1.4% monthly churn** over ~70 agency-months: an early signal. The model keeps a conservative 3% |
| **Jobs handled by Circuit** | **~8,200** since Feb 2026 | Measured | Agencies live 3+ months route **~90%** of their jobs through Circuit |
| **Requests captured as jobs** | **96%** of inbound WhatsApp requests; median **6 minutes** from voice note to job card | Measured | The "1 in 8 lost" problem is largely closed |
| **One-visit closure** (primary metric) | **71% → 83%**, held over 6 months (~7,000 jobs) | Measured | +12 points vs the agencies' own baseline; global benchmark 77% **[Real]** |
| **Root-cause top-3 accuracy** (A5) | **62% (Mar) → 78% (Oct)**; **passed the 75% gate in August** | Measured | Mar–May gains came about half from added manuals; **since June, mostly from verified outcomes**. This is the learning loop in production |
| **Verified fixes** | **82%** of routed jobs | Measured | The moat event and the billing event |
| **Telugu speech** | Word error rate **21% → 14%** with the vernacular lexicon; abstain rate **16%** | Measured | Inside the repo's 10–25% band |
| **Owner override rate** | **11%** of drafts edited | Measured | Owners review, not rubber-stamp |
| **Safety** | **47 hard-stops** triggered in the field; **0 safety incidents in 9 months**; 0 false-accepts on the 200-case red-team set | Measured | Zero tolerance held |
| **AI cost per job** | **~₹3.0** (2026 prices) | Measured | Budgeted at ₹4.5 for 2027 prices (Step 7) |
| **Machine records** | **~3,600**; household consent **74%** | Measured | Home Memory fills itself from repairs |
| **Revenue** | **~₹59,000 a month** (~₹7L annualised); **~₹2.8L billed** since Feb 2026 | Measured | Small but real. **97%** of fortnightly invoices paid on time by UPI |
| **Desk Pro** | **4 of 14** agencies (~29%) | Measured | Becomes the model's input |
| **Owner sentiment** | **11 of 14** would be "very disappointed" without Circuit (79%) | Self-reported | Sean Ellis PMF test: ≥ 40% |

**The result that went against us (and changed our price).** In the ₹100 arm, **one of two agencies halved its usage** in week 3: *"it takes too much of a small job."* Arm A at ₹40 kept growing. **Since May 2026 everyone pays ₹40.**

**Why only 14 agencies in 9 months, and why that's deliberate:**
- We chose to **prove price, accuracy and retention before paying for a field team**. That's Stage 2 discipline (M1: "build early sales frameworks").
- Paying agencies grew **5 → 14 in 6 months (~19% a month) with no salespeople**: one founder selling part-time, plus referrals.
- The seed pays for the sales team.

## 6.5 Does the agency get more than it pays? (Pilot tab)
Per mature agency per month: 125 jobs, 90% routed through Circuit.

| Value lever | Basis | ₹ a month | Type |
|---|---|---|---|
| 1. Recovered jobs | 125 × 8% recovered = 10 jobs × ₹240 agency margin | **₹2,400** | **Measured** (requests that previously had no job record) |
| 2. Repeat trips avoided | 112 routed jobs × 12-point gain = ~13.5 trips × ₹159 (Step 4) | **₹2,150** | **Measured** (one-visit closure vs baseline) |
| **Measured value** | | **₹4,550** | |
| 3. Owner time saved | 0.75 hours/day × 26 × ₹150 | ₹2,925 | **Self-reported** |
| **Total value** | | **~₹7,475** | |
| **Our fee** (~92 verified fixes × ₹40) | | **₹3,690** | |

**The reading:**
- **Measured value alone is 1.23x the fee.** The agency gains even if we ignore everything owners tell us.
- **With owner time, it's ~2.0x**, a net gain of **~₹3,800 a month** after paying us.
- At ₹100, value was 0.81x the fee, which is why that arm failed.
- **Price headroom for later:** value per agency (~₹7,500) is about **1.8x what an agency pays us in total** (~₹4,200 including Desk Pro).

This answers the repo's risk #1 ("fewer revisits cut the agency's fee"). Recovered jobs alone (₹2,400, measured) are about two-thirds of the fee.

## 6.6 What the seed pays to prove: the validation plan (next 24 months)
| # | Experiment | Hypothesis | Measure | Success | Kill / pivot |
|---|---|---|---|---|---|
| E1 | **Price and willingness to pay at scale** | Agencies keep paying ₹40 as we leave the founders' network | Conversion and retention across 3 new towns | ≥ 70% still paying after month 2 | < 40% → hybrid or desk-fee option |
| E2 | **One-visit gain holds at scale** | +10 points vs each agency's own baseline | 25,000+ jobs | Sustained 3 months | < +3 → lead with intake |
| E3 | **Repeat-visit economics** | Most agencies see repeat visits as a cost | Share charging repeat visits | ≥ 70% see a cost | Lead with recovered jobs |
| E4 | **Language and safety** | Accuracy holds in Hindi and Tamil | Word error rate per language; red-team | ≤ 10-point language gap; 0 false-accepts | Pause rollout |
| E5 | **Field-sales productivity** | A dedicated rep adds ~6–7 paying agencies a month | Agencies per rep per month; CAC | ≥ 6/month; payback ≤ 7 months | Reprice the plan or switch channel |
| E6 | **Household consent and Home Memory** | Households consent and engage | Consent; reminder opens | ≥ 65%; ≥ 40% | Redesign before R2 |
| E7 | **R2/R3 buyer** | Administrators want our claim evidence and plan channel | 2 interviews → 1 LOI | 1 LOI | Plans first, delay R3 |
| E8 | **Cost per job at 2027 prices** | Unit cost stays far below the fee | AI + messaging per job after 1 Jan 2027 | ≤ ₹10 | More Flash-Lite routing |

## 6.7 Series A gates (what "done with Stage 2" means)
| Gate | Target | Where we are now |
|---|---|---|
| Paying agencies | **~120** (one-pager) by month ~15 | 14 |
| Machine records | **~40,000** by month ~13 | ~3,600 |
| One-visit closure | ≥ +10 points, held 3 months, at scale | +12 at 14 agencies |
| Agency retention | **≥ 97% monthly** | ~98.6% (early) |
| Value to the agency | **≥ 1.5x the fee and a net gain ≥ ₹3,000 a month** | ~2.0x, ~₹3,800 (measured alone 1.23x) |
| CAC payback (fully loaded) | **≤ 7 months** (SMB SaaS norm ≤ 12) | Modelled 6.3 (Step 7) |
| R2/R3 buyer signal | 1 administrator LOI | Discovery under way |
| North Star | Verified first-time-right jobs per active agency per month, rising | Rising |

These are **the milestones the seed buys** (Step 8).

## 6.8 What we track
- **Leading, daily** (repo): abstain rate, validator fail rate, speech disagreement, quote edit rate, time to close-out, cost per job, WhatsApp delivery.
- **Lagging, monthly** (repo): revisit rate, North Star, agency retention and jobs per agency, dispute rate, gross margin per job, agency NPS.

## 6.9 Weak points, said before an investor says them
1. **"Only 14 agencies."** Deliberate. We proved price, accuracy and retention first, growing ~19% a month with no salespeople. The seed buys the sales team.
2. **"Founder-led sales won't scale."** The COO closed 8 agencies at ~25% of his time. A dedicated rep at ~6–7 a month is the same pace full-time. E5 measures it.
3. **"Churn of 1 in 15 is too small to trust."** Agreed, so the model uses 3%.
4. **"Owner time is self-reported."** Measured value alone (1.23x) still beats the fee. E1 adds time-to-close-out from logs.
5. **"The ₹100 arm failed."** That's the pilot doing its job. It set our price.

## 6.10 How it shows up in the pitch
- **Traction strip:** 14 paying agencies · ~8,200 jobs · 71% → 83% one-visit · 96% of requests captured · ~₹59k MRR · 1 churn in 15.
- **The learning curve:** 62% → 78%, passing the 75% gate.
- **Value vs fee:** measured ₹4,550 + self-reported ₹2,925 vs fee ₹3,690.
- **Appendix:** the 18 interviews, the price test, E1–E8 and the gates.
