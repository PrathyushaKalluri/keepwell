# Step 7 — Business model and unit economics
**Phase C: The engine · Status: LOCKED 16 Nov 2026 (updated to observed inputs and the backdated timeline)**
> **Illustrative case.** Founder histories, the company timeline, the pilot results and the financials are assumptions made for the IIIT Hyderabad ESFS course pitch. They are kept consistent with the team repo and with each other.

**Tags:** **[repo]** = team repo `ESFS/keepwell/` · **[Story]** = observed in our paid usage (Step 6) · **[Model]** = calculated in `keepwell_model.xlsx` (Revenue Build, P&L and Cash, Unit Economics, Sensitivity, Pilot).
**Plan:** [`../pitch_bible.md`](../pitch_bible.md) · **Builds on:** Steps 1–6 · **Feeds:** Step 8 (budget and ask), Step 9 (valuation)

## 7.1 How this step is built
**Course frame (M3, Pillar 2: "putting numbers to the narrative").** Investors want three things: the growth plan, the unit economics, and the path to profitability. They ask:
- How do we make money?
- What does it take to get a customer?
- What does it cost to serve one?
- What's the pricing strategy, and why?
- When will the cash come in?
- What are the sensitive parameters?

**Red flags to avoid** (M3): missing or negative unit economics; flimsy growth or margin claims; no proof of stickiness; being unable to explain the numbers simply.

**Rule: model what we observe.** Every input we have measured comes from our 9 months of paid usage (Step 6):
- jobs per agency: **125** (the market average of ~147 is upside, not modelled)
- verified share: **82%**
- Desk Pro uptake: **29%**
- AI cost per job

The model's other mechanics:
- Growth comes from field-sales capacity.
- Field-sales and support *people* sit in team cost, so CAC isn't double-counted.
- AI is budgeted at 2027 prices.
- Google credits are applied against AI and cloud in Y1–Y2.

## 7.2 How we make money
| Release | Stream (repo ID) | Who pays | Why they pay | Model | Starts |
|---|---|---|---|---|---|
| R1 | **Per verified fix (R1)** | Agency | Recovered jobs, fewer trips, owner time (value ~₹7,500/month; measured part ~₹4,550) | ₹40 per fix the technician verifies | Live |
| R1 | **Desk Pro add-on (R2)** | Agency, optional | Owner reports, reminders, quote templates | ₹399/month | Live (4 of 14) |
| R2 | **Service Plans commission (R3)** | Plan provider / insurer, via an IRDAI-registered route | Plans offered to the right home at the right time, triggered by the record | % of plan value | Y2 |
| R3 | **Claims-triage licence (R5)** | Warranty administrators, OEMs | Faster, evidence-backed claims | Annual licence | Y3 (LOI in Y2) |
| R4 | **Parts referral (R4)** | Parts sellers | Demand predicted from records | % of matched orders | Y3 |
| R5 | **Resale and recycling take (R9)** | Buyers, producers | Verified history raises resale value | % of deal | Y5 |
| Later | Lead routing (R6), household premium (R7), data insights (R8) | OEMs, households, brands | — | **Not modelled** (repo: OEM agreements uncertain; don't depend on R7; R8 needs consent coverage) | After Y5 |

**Not a revenue line:** payments. Small-merchant UPI stays at zero MDR, so customers pay the agency directly.

## 7.3 Pricing: tested, not guessed
| Option | Evidence | Verdict |
|---|---|---|
| **1. ₹40 per verified fix + optional Desk Pro ₹399/month + 30 free days** | **Price test (Feb–Apr 2026):** the ₹40 arm grew; value ~2.0x the fee, measured value alone 1.23x. **Interviews:** 14 of 18 prefer per job; ₹30–50 acceptable. **Repo:** "pay per job, not per seat" | **Chosen; live since May 2026** |
| 2. ₹1,500/month + ₹40 (the one-pager) | Value/fee = ₹7,475 ÷ (₹1,500 + ₹3,690) = **1.44x**. Only 3 of 18 owners prefer a flat fee | Too heavy for Tier 2/3 at entry |
| 3. ₹100 per verified fix | **Price test: value/fee 0.81x;** one of two agencies halved its usage | Rejected by the test |
| 4. Flat ₹999/month only | At 125 jobs, AI + messaging ₹713 + tools ₹100 → **contribution only ~₹186/month**; the fee is disconnected from usage | Doesn't cover cost to serve |

**Why it works:**
- **Fee tied to value.** We charge only on a verified fix, which is also the North Star and moat event.
- **A small share of the job.** ₹40 is **~7% of a ~₹600 job**, against Urban Company keeping **28.3%** **[repo]**, and we don't take the customer.
- **A short trial.** 30 free days (the one-pager said 60). Per-fix pricing already removes the agency's risk, and mature agencies reach ~90% routing within weeks.
- **Price headroom.** Value per agency (~₹7,500) is ~1.8x what agencies pay in total (~₹4,200). The price is reviewed at Series A, once accuracy keeps improving.

## 7.4 Unit economics: one agency, steady state (₹ a month) **[Model on observed inputs]**
| Line | Value | How |
|---|---|---|
| Jobs per month | **125** | Observed median of our 14 paying agencies |
| Per-fix revenue | ₹4,100 | 125 × 82% verified × ₹40 |
| Desk Pro (average) | ₹116 | ₹399 × 29% uptake (4 of 14) |
| **Revenue per agency (ARPA)** | **₹4,216** (~₹50,600 a year) | |
| AI + messaging | ₹713 | 125 × (₹4.5 AI at 2027 prices + ₹1.2 WhatsApp) |
| Support tooling | ₹100 | People are in team cost |
| **Contribution per agency** | **₹3,403 (81% margin)** | |
| **Fully loaded CAC** | **~₹17,900** | (field-sales salaries + acquisition cash + brand) ÷ new agencies, Y3 |
| **CAC payback** | **6.3 months** (5.3 excluding the free month) | Gate ≤ 7 (SMB SaaS norm ≤ 12) |
| Agency lifetime | 33 months | At a conservative 3%/month churn (observed ~1.4%) |
| **LTV, Circuit only** | **~₹1.13 lakh** | Excludes plans, parts and claims |
| **LTV : CAC** | **6.3x** | Healthy is > 3x |
| Revenue / cost to serve per job | ₹33.7 / ₹6.5 | |
| Jobs per month to cover cost to serve | 3.6 | Any active agency is contribution-positive |

**AI cost basis.** The repo's job mix (50% simple, 35% parts-needed, 15% warranty) costs ₹5.10 on Flash at 2027 prices and ₹1.22 on Lite with caching. Routing ~50/50 gives ~₹3.2, plus escalations ~₹0.3, plus a 25% margin, for **₹4.5**. We measure ~₹3.0 today at 2026 prices.

**Revenue per agency rises as the platform attaches.** In Y5, Circuit earns ~₹50,600 per agency a year and the platform lines (plans, parts, claims, resale) add **~₹16,700**, for **~₹67,000 per agency (+33%)**. That's the "record is the business" effect, in numbers.

## 7.5 Growth plan: derived from capacity, not assumed
**New paying agencies** = field-sales people × 80 a year + 10% referrals.
- **Evidence for 80 a year:** the COO closed 8 agencies in 6 months at ~25% of his time, roughly the same pace as a full-time rep at ~6–7 a month. 2 of the last 10 came by referral.
- **Churn:** 3%/month in Y1–Y2, falling to 2% (Y3) and 1.5% (Y4–Y5) as switching costs build. Observed today: ~1.4%.
- **Funding:** the seed funds Y1–Y2; the **Series A (~month 20) funds faster field sales from Y3**.

| | Y1 | Y2 | Y3 | Y4 | Y5 |
|---|---|---|---|---|---|
| Field-sales people | 1 (+ COO) | 3 | 10 | 18 | 24 |
| New paying agencies | 81 | 248 | 826 | 1,535 | 2,140 |
| **Paying agencies at year end** (from 14 today) | **79** | **264** | **945** | **2,196** | **3,793** |
| Where (repo phasing) | TS+AP | TS+AP (Series A gate ~120 at month ~15) | Four southern states | South + beyond | National Tier 2/3 |
| Share of SAM (22,500) | 0.4% | 1.2% | 4.2% | 9.8% | **16.9%** (ceiling 20% ✓) |
| Jobs handled | 0.69 lakh | 2.6 lakh | 9.1 lakh | 23.6 lakh | 44.9 lakh |
| Machine records (cumulative) | 29,000 | 1.37 lakh | 5.18 lakh | 15.1 lakh | **33.9 lakh** |

## 7.6 Five-year P&L (₹ lakh) **[Model]**
| | Y1 | Y2 | Y3 | Y4 | Y5 |
|---|---|---|---|---|---|
| Circuit (per fix + Desk Pro) | 20.1 | 76.5 | 271.6 | 730.6 | 1,425.9 |
| Service Plans | — | 8.2 | 31.1 | 90.5 | 203.6 |
| Claims-triage licences | — | — | 40.0 | 80.0 | 160.0 |
| Parts | — | — | 21.8 | 56.5 | 107.8 |
| Resale & Recycling | — | — | — | — | 27.2 |
| **Total revenue** | **20.1** | **84.7** | **364.4** | **957.6** | **1,924.5** |
| Gross margin (before credits) | 77% | 80% | 84% | 84% | 85% |
| Team cost | 142.0 | 233.3 | 461.9 | 768.4 | 1,096.6 |
| Headcount | 12 | 19 | 38 | 62 | 84 |
| Other opex (incl. ₹8L seed costs in Y1) | 60.8 | 73.5 | 120.3 | 187.3 | 271.4 |
| Google credits applied | (9.1) | (23.6) | — | — | — |
| **EBITDA** | **(178.2)** | **(215.2)** | **(276.7)** | **(151.3)** | **264.6** |
| EBITDA margin | — | — | −76% | −16% | **+14%** |
| D&A | 1.7 | 4.3 | 8.3 | 12.7 | 18.3 |
| Free cash flow | (184.2) | (226.4) | (302.7) | (199.0) | 129.7 |
| Average monthly burn | 15.3 | 18.9 | 25.2 | 16.6 | — |
| Cash before Series A (closing) | 321.8 | 95.4 | (207.2) | (406.2) | (276.5) |

- **Break-even: Y5** (EBITDA +₹2.6 Cr, 14%). On the Y5 cost base it needs ~2,380 paying agencies.
- **Cash comes in fortnightly** (per-fix invoices by UPI; 97% on time). Working capital is ~5% of revenue.
- **After the seed:** cash bottoms at about **−₹4.1 Cr in Y4**, so the Series A covers that with a buffer (Step 8.8).

## 7.7 How we chose the plan: the scenarios
Tested one lever at a time on observed inputs:

| Plan | Agencies Y5 | Revenue Y5 | EBITDA Y5 | Outside cash needed after the seed |
|---|---|---|---|---|
| D. **Lean**: falling churn + lean tech team, seed only, slow field sales | 2,701 | ₹13.9 Cr | ~₹0 (−₹0.02 Cr) | **~₹4.9 Cr** |
| **G. Funded growth (pitched):** D + the Series A spent on field sales from Y3 | **3,793** | **₹19.2 Cr** | **+₹2.6 Cr** | **~₹4.1 Cr** |

**Why G:**
- **The Series A is needed in either plan.** Spending it on field sales needs *less* outside cash than staying lean, because each new agency pays back in ~6 months.
- The cap table already assumes the Series A and B dilution, so the investor's return must be judged on the plan that money funds.
- G stays under the 20% SAM ceiling (16.9%).

**Why the falling churn is defensible:**
- The observed churn is ~1.4% a month.
- Switching costs build: rate cards, customer histories and technician habits all live in Circuit.
- **Unit economics deliberately use 3%.**

## 7.8 Sensitive parameters (LTV:CAC when each driver moves ±20%)
| Driver | LTV:CAC at −20% / +20% | Swing | Proven by |
|---|---|---|---|
| Fee per verified fix | 4.8x / 7.8x | 3.0 | Price test; E1 |
| Verified share | 4.8x / 7.8x | 3.0 | Observed 82% |
| Monthly churn | 7.9x / 5.3x | 2.6 | Observed ~1.4%; retention gate |
| Fully loaded CAC | 7.9x / 5.3x | 2.6 | E5 |
| Jobs per agency | 5.1x / 7.6x | 2.5 | Observed 125 |
| AI cost per job | 6.5x / 6.1x | 0.4 | E8 |
| Messaging cost per job | 6.4x / 6.3x | 0.1 | — |

**Read:**
- **Unit economics stay above ~5x in every ±20% case.**
- The risk is commercial (price, verification, churn, CAC), not token cost. That matches the repo: *"the binding risk is whether agencies pay, not token cost."*

## 7.9 The investor reading, said plainly
1. **Unit economics are strong and observed:** 81% contribution margin, ~6-month payback, 6.3x LTV:CAC on the conservative 3% churn.
2. **Circuit alone is modest:** ~₹50,600 per agency a year. At the 20% ceiling (4,500 agencies), it tops out around **₹23 Cr a year** in Tier 2/3.
3. **The record is the business:** revenue per agency rises ~33% by Y5 as the platform attaches, and there are **33.9 lakh machine records** by Y5. The path to ₹100 Cr is in Step 9.4.
4. **Capital-efficient growth:** spending the Series A on field sales needs less outside cash than staying lean.

## 7.10 Weak points, said before an investor says them
| Weak point | Answer |
|---|---|
| ₹19 Cr revenue in Y5 is small for venture | The record compounds: Tier 1, plans and claims at scale (Step 9.4) |
| 80 agencies per field-sales person a year | Backed by the COO's part-time pace; E5 measures it; CAC ±20% still gives ~5–8x |
| Churn falling to 1.5% | Observed ~1.4%; unit economics use 3% anyway |
| Plan, claims and parts revenue depend on partners | Gated: IRDAI route (R2), administrator LOI (E7), wholesaler partners (Step 3) |
| Payback 6.3 months misses a 6-month gate | Gate re-based to ≤ 7 on observed inputs, stated openly; SMB SaaS norm is ≤ 12 |

## 7.11 How it shows up in the pitch
- How we make money (7.2)
- Pricing tested (7.3)
- Unit economics strip (7.4)
- Growth and records chart (7.5)
- P&L summary (7.6)
- Sensitivity (7.8)

Cells covered: Product–Potential (clear business model), Startup–Potential (path to profitability), and the M3 "Business Model (Engine)" pillar.

---
## Decisions log (LOCKED 16 Nov 2026)
- **Pricing:** ₹40 per verified fix + optional Desk Pro ₹399/month + 30 free days. Tested Feb–Apr 2026; live since May 2026.
- **Inputs:** observed wherever measured. 125 jobs per agency, 82% verified, 29% Desk Pro (updated after the full-pitch red-team).
- **Plan pitched: G** (the Series A funds field sales from Y3). D is shown for comparison; both need a Series A.
- **Revenue lines in the 5-year numbers:** R1, R2, R3, R4, R5, R9. R6–R8 are upside.
- **CAC payback gate:** ≤ 7 months (was ≤ 6), re-based on observed jobs and stated openly.
