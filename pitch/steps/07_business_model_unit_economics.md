# Step 7 — Business model and unit economics
**Phase C: The engine · Status: LOCKED 16 Nov 2026**
**Tags:** **[Real]** = case-competition research · **[repo]** = team repo `ESFS/keepwell/` · **[Story]** = pilot (Step 6) · **[Model]** = calculated in `keepwell_model.xlsx` (Revenue Build, P&L and Cash, Unit Economics, Sensitivity, Pilot).
**Plan:** [`../pitch_bible.md`](../pitch_bible.md) · **Builds on:** Steps 1–6 (locked) · **Feeds:** Step 8 (budget and ask), Step 9 (valuation)

> **All figures are DRAFT outputs of the recommended base case.** They become final only when the team locks pricing here and costs in Step 8. They are shown so the team can decide. They are not yet pitch numbers.

## 7.1 How this step is built
**Course frame (M3, Pillar 2: "putting numbers to the narrative").** Investors want three things: the growth plan, the unit economics, and the path to profitability. They ask:
- How do we make money?
- What does it take to get a customer?
- What does it cost to serve a customer?
- What is the pricing strategy, and why?
- When will the cash come in?
- What are the sensitive parameters?

**Assumptions to defend:** number of customers, average revenue per customer, retention, growth triggers, LTV, delivery cost, CAC, team cost, financial expenses, D&A, gross margin, CAC and LTV, SG&A, EBITDA and EBIT, cash burn.

**Red flags to avoid** (M3): missing or negative unit economics; flimsy growth or margin claims; no proof of stickiness; being unable to explain the numbers simply.

**What changed in the model in this step:**
1. **Growth is now derived, not typed in.** New agencies = field-sales people × agencies each adds a year + referrals. This is what Step 4 required.
2. **No double counting.** Field-sales and support people sit in team cost. CAC on the P&L is cash only. The *fully loaded* CAC is calculated from both.
3. **AI cost is budgeted at 2027 prices.**
4. **Google for Startups credits are applied** against AI and cloud cost in Y1–Y2.
5. **The other revenue lines start in their roadmap years** (Step 1).
6. **A sensitivity tab** shows which drivers matter.

## 7.2 How we make money
| Release | Stream (repo ID) | Who pays | Why they pay | Model | Starts |
|---|---|---|---|---|---|
| R1 | **Per verified fix (R1)** | Agency | Recovered jobs, fewer trips, owner time saved (pilot value ~₹7,500/month) | ₹ per fix the technician verifies | Now |
| R1 | **Desk Pro add-on (R2)** | Agency, optional | Owner reports, reminders, quote templates | Monthly add-on | Now |
| R2 | **Service Plans commission (R3)** | Plan provider / insurer | Plans sold to the right home at the right time, triggered by the record | % of plan value | Y2 |
| R3 | **Claims-triage licence (R5)** | Warranty administrators, OEMs | Faster, evidence-backed claims | Annual licence | Y3 (LOI in Y2) |
| R4 | **Parts referral (R4)** | Parts sellers | Demand predicted from records | % of matched orders | Y3 |
| R5 | **Resale and recycling take (R9)** | Buyers, producers | Verified history raises resale value | % of deal | Y5 |
| Later | Lead routing (R6), household premium (R7), data insights (R8) | OEMs, households, brands | — | **Not modelled.** OEM agreements are uncertain; the repo says don't depend on R7; R8 needs consent coverage | After Y5 |

**Not a revenue line:** payments. Small-merchant UPI stays at zero MDR (repo), so customers keep paying the agency directly.

## 7.3 Pricing: options, evidence and recommendation (team decision)
| Option | What it is | Evidence | Verdict |
|---|---|---|---|
| **1. ₹40 per verified fix + optional Desk Pro ₹399/month + 30 free days** | Pay only when a fix passes the technician's test | **Pilot:** value = 2.2x the fee at ₹40 (value is 2x the fee at ~₹43). **Interviews:** 14 of 18 prefer per job; median acceptable ₹30–50. **Repo:** "pay per job, not per seat"; R1 ₹40; R2 optional ₹300–500 | **Recommended** |
| 2. ₹1,500/month + ₹40 per fix (the one-pager) | A fixed desk fee plus per fix | Pilot value/fee = ₹7,523 ÷ (₹1,500 + ₹3,485) = **1.5x**, below the 2x bar. Only 3 of 18 owners prefer a flat fee | Too heavy for Tier 2/3 at entry |
| 3. ₹100 per verified fix | The repo's high test point | **Pilot: value/fee = 0.86x.** One of two agencies halved its usage. Only 4 of 18 accepted ₹100 | Rejected by the pilot |
| 4. Flat ₹999/month only (no per-fix fee) | A simple subscription | At 145 jobs, AI and messaging cost ₹827 + tools ₹100, so **contribution is only ~₹72 per agency per month.** The fee is disconnected from usage, and heavy users lose us money | Doesn't cover cost to serve |

**Why the recommendation works:**
- **Fee tied to value.** We charge only on a verified fix, which is also the North Star event and the moat event. The agency never pays for a failure.
- **A small share of the job.** ₹40 on a ~₹600 bill is **~7%** of the job, against Urban Company keeping **28.3%** of the professional's earnings **[repo]**. And we don't take the customer.
- **A shorter trial.** 30 free days instead of the one-pager's 60. Per-fix pricing already removes the agency's risk, and the pilot reached 85% routing in 4 weeks. Halving the free period lowers burn.
- **Room to raise the price later.** As Mistri Gyan improves, value per job rises. The price is reviewed at Series A (experiment E1, Step 6).

## 7.4 Unit economics: one agency, steady state (₹ a month) **[Model]**
| Line | Value | How |
|---|---|---|
| Jobs per month | 145 | Step 4 triangulation (pilot median 125) |
| Per-fix revenue | ₹4,756 | 145 × 82% verified (pilot) × ₹40 |
| Desk Pro (average across agencies) | ₹100 | ₹399 × 25% uptake |
| **Revenue per agency (ARPA)** | **₹4,856** (~₹58,000 a year) | |
| AI + messaging | ₹827 | 145 × (₹4.5 AI at 2027 prices + ₹1.2 WhatsApp) |
| Support tooling | ₹100 | People are in team cost |
| **Contribution per agency** | **₹3,929 (81% margin)** | |
| **Fully loaded CAC** | **~₹17,900** | (field-sales salaries + acquisition cash + brand) ÷ new agencies, Y3 |
| **CAC payback** | **5.6 months** (including 1 free month) | Gate ≤ 6 (Step 6) ✓ |
| Agency lifetime (at 3%/month churn) | 33 months | Conservative new-agency rate |
| **LTV, Circuit only** | **~₹1.31 lakh** | Contribution × lifetime. Excludes plans, parts and claims |
| **LTV : CAC** | **7.3x** | Healthy is > 3x |
| Revenue / cost to serve per job | ₹33.5 / ₹6.4 | |
| Jobs per month to cover cost to serve | 3.6 | Any active agency is contribution-positive |

**AI cost basis.** The repo's job profiles are mixed 50% simple, 35% parts-needed and 15% warranty. That gives ₹5.10 a job on Flash at 2027 prices and ₹1.22 on Lite with caching. Routing about half the calls to Lite gives ~₹3.2, plus Pro escalations of ~₹0.3, plus a 25% safety margin, for **₹4.5**. The pilot measured ₹3.1 at 2026 prices.

## 7.5 Growth plan: derived from capacity, not assumed
**New paying agencies** = field-sales people × 80 a year each, plus 10% referrals.
- **80 a year per person** = 10 trials a month × 12 × ~67% converting.
- **Churn** is 3% a month in Y1–Y2, falling to 2% in Y3 and 1.5% in Y4–Y5 as switching costs build.
- **Funded plan.** The seed funds Y1–Y2. The **Series A (~month 20) funds faster field sales from Y3**. This is the plan the cap table's Series A and B dilution assumes (see 7.7).

| | Y1 | Y2 | Y3 | Y4 | Y5 |
|---|---|---|---|---|---|
| Field-sales people | 1 (+ founders) | 3 | 10 | 18 | 24 |
| New paying agencies | 81 | 247 | 826 | 1,534 | 2,139 |
| **Paying agencies at year end** | **72** | **259** | **940** | **2,191** | **3,789** |
| Where (repo phasing) | TS+AP beachhead | TS+AP (Series A gate ~120 crossed) | Four southern states | South + beyond | National Tier 2/3 |
| Share of SAM (22,500) | 0.3% | 1.2% | 4.2% | 9.7% | **16.8%** (ceiling 20% ✓) |
| Jobs handled | 0.67 lakh | 2.9 lakh | 10.4 lakh | 27.2 lakh | 52.0 lakh |
| Machine records (cumulative) | 28,000 | 1.49 lakh | 5.87 lakh | 17.3 lakh | **39.2 lakh** |

## 7.6 Five-year P&L (₹ lakh) **[Model]**
| | Y1 | Y2 | Y3 | Y4 | Y5 |
|---|---|---|---|---|---|
| Circuit (per fix + Desk Pro) | 18.5 | 84.5 | 309.9 | 838.8 | 1,640.0 |
| Service Plans | — | 8.9 | 35.2 | 103.9 | 235.0 |
| Claims-triage licences | — | — | 40.0 | 80.0 | 160.0 |
| Parts | — | — | 21.6 | 56.4 | 107.6 |
| Resale & Recycling | — | — | — | — | 31.3 |
| **Total revenue** | **18.5** | **93.4** | **406.7** | **1,079.1** | **2,173.9** |
| Gross margin (before credits) | 77% | 80% | 85% | 85% | 86% |
| Team cost | 142.0 | 233.3 | 461.9 | 768.4 | 1,096.6 |
| Headcount | 12 | 19 | 38 | 62 | 84 |
| Other opex (incl. ₹8L seed transaction costs in Y1) | 60.8 | 73.5 | 120.3 | 187.4 | 271.3 |
| Google credits applied | (9.0) | (24.9) | — | — | — |
| **EBITDA** | **(179.6)** | **(206.8)** | **(242.2)** | **(50.7)** | **473.5** |
| EBITDA margin | — | — | −60% | −5% | **+22%** |
| D&A (3-year straight line) | 1.7 | 4.3 | 8.3 | 12.7 | 18.3 |
| Free cash flow | (185.5) | (218.5) | (269.8) | (102.4) | 280.0 |
| Average monthly burn | 15.5 | 18.2 | 22.5 | 8.5 | — |
| Cash before Series A (closing) | 326.5 | 108.0 | (161.8) | (264.2) | 15.8 |
| Revenue per employee | 1.5 | 4.9 | 10.7 | 17.4 | 25.9 |

- **Break-even: Y5** (EBITDA +₹4.7 Cr, a 22% margin).
- On the Y5 cost base, break-even needs **~2,100 paying agencies** (Y5 opex ÷ ₹47,000 Circuit contribution + ₹17,900 platform revenue per agency per year).
- **Cash comes in fortnightly:** per-fix invoices are paid by UPI. Working capital is ~5% of revenue.
- **Outside money needed after the seed:** cash bottoms at about −₹2.6 Cr in Y4. The Series A covers that with a buffer (Step 8.8).

## 7.7 How we got here: the scenarios behind the plan
The first honest build (flat 3% churn, a tech team growing to 22) **never broke even in 5 years**. We tested the levers a founder would pull, one at a time:

| Scenario | Agencies Y5 | Revenue Y5 | EBITDA Y5 | Break-even |
|---|---|---|---|---|
| A. As first built | 2,221 | ₹13.4 Cr | −₹2.2 Cr | after Y5 |
| B. Churn falls as switching costs build | 2,697 | ₹15.7 Cr | −₹0.3 Cr | after Y5 |
| C. Lean tech team (4 → 15) | 2,221 | ₹13.4 Cr | −₹0.5 Cr | after Y5 |
| D. B + C: the **lean, seed-only plan** | 2,697 | ₹15.7 Cr | +₹1.4 Cr | Y5 |
| **G. D + Series A spent on field sales from Y3 (funded plan, adopted after the investor review)** | **3,789** | **₹21.7 Cr** | **+₹4.7 Cr** | **Y5** |

**Why G is the plan we pitch (changed after the Step 12 review):**
- The cap table already dilutes the seed investor for a Series A and B.
- The lean plan D never used that money, so judging the investor's return on D double-counted the dilution.
- G spends the Series A on what the pilot shows works (field sales at ~₹18,000 fully loaded CAC and 5.6-month payback) and stays under the 20% SAM ceiling (16.8%).

**What D still proves:** even with no Series A, the company reaches break-even in Y5. That's the downside protection.

**Why the falling churn is defensible:**
- Rate cards, customer histories and technician habits live in Circuit (the switching costs in Step 5).
- **Unit economics deliberately use the conservative 3%.**
- Only the growth plan uses the falling rate.

## 7.8 Sensitive parameters (Sensitivity tab: LTV:CAC when each driver moves ±20%)
| Driver | LTV:CAC at −20% / +20% | Swing | Proven by (Step 6) |
|---|---|---|---|
| Fee per verified fix | 5.5x / 9.1x | 3.5 | E1 price |
| Verified share | 5.5x / 9.1x | 3.5 | Pilot (82%) |
| Monthly churn | 9.1x / 6.1x | 3.0 | Retention gate |
| Fully loaded CAC | 9.1x / 6.1x | 3.0 | E5 channel |
| Jobs per agency | 5.8x / 8.8x | 2.9 | Pilot, E2 |
| AI cost per job | 7.5x / 7.1x | 0.5 | E8 |
| Messaging cost per job | 7.4x / 7.2x | 0.1 | — |

**Read:**
- **Unit economics stay above 5x in every ±20% case.**
- **The binding risk is commercial** (price, verification, churn, CAC), **not token cost.** This matches the repo: *"the binding risk is whether agencies pay, not token cost."*

## 7.9 The investor reading, said plainly
1. **Unit economics are strong:**
   - 81% contribution margin
   - 5.6-month payback (fully loaded CAC ~₹17,900)
   - **7.3x LTV:CAC**
2. **Circuit alone is a modest business.** ARPA is ~₹58,000 a year. At the 20% ceiling (4,500 agencies), Circuit revenue tops out around **₹26 Cr a year** in Tier 2/3.
3. **The venture case is the record.** By Y5 there are **39.2 lakh machine records**, and the platform lines are **~25% of Y5 revenue** and growing faster. The path to ₹100 Cr revenue (Tier 1, plans and claims at record scale) is in Step 9.4.
4. **The downside is protected.** The lean plan (D) still breaks even in Y5 with no Series A.
5. **The investor's return** at the pitched price is tested in Step 9: ~37% IRR in the base case, above the 35% hurdle.

## 7.10 Weak points, said before an investor says them
| Weak point | Answer |
|---|---|
| Y5 revenue (₹21.7 Cr) is small for venture | The wedge is profitable; the record compounds. Step 9 shows the exit maths (37% base-case IRR) and the path to ₹100 Cr |
| 80 agencies per field-sales person a year is unproven | E1 and E5 measure it. The sensitivity shows CAC ±20% still gives ~6–9x |
| Churn falling to 1.5% is an assumption | Unit economics use the conservative 3%. Only the growth plan uses the falling rate |
| Plan, claims and parts revenue depend on partners | Each has a gate: IRDAI licence answer (R2), administrator LOI (E7), wholesaler partners (Step 3) |
| Credits end after Y2 | Credits cover only ~₹34L of real spend. Unit economics are shown *before* credits |

## 7.11 How it shows up in the pitch (final choices in Step 12)
Material available:
- "How we make money" (7.2, as a ladder)
- pricing and why (7.3: "₹40 only when the fix works; 7% of the job vs 28% elsewhere")
- unit economics strip (7.4)
- growth and records chart (7.5)
- P&L summary with break-even (7.6)
- the sensitivity tornado (7.8)

Cells covered: Product–Potential (clear business model), Startup–Potential (path to profitability), and the M3 "Business Model (Engine)" pillar.

---

## Decisions log (LOCKED 16 Nov 2026)
- **Pricing: Option 1.** ₹40 per verified fix + optional Desk Pro ₹399/month + 30 free days.
- **Inputs:** taken from the pilot wherever the pilot measured them (82% verified share, value levers, AI cost basis).
- **Base case: Scenario D** (churn falls 3% → 1.5%; lean tech team 4 → 15). **Updated after the Step 12 investor review:** the pitched plan is **G = D + the Series A spent on field sales from Y3**, because the cap table already dilutes for A and B. D remains the downside case.
- **Revenue lines in the 5-year numbers:** R1, R2, R3, R4, R5, R9. R6, R7 and R8 are left out of the numbers and kept as upside.
