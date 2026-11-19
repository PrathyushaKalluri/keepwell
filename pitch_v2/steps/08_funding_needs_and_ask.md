# Step 8: Funding needs and the ask

**Phase C (the money). Status: DRAFT for approval (20 Nov 2026). Revised after an independent review.**

> **Illustrative case** for the IIIT Hyderabad ESFS course pitch.
> - **Annual numbers** come from `keepwell_model.xlsx` (`model/plan_v3.py`).
> - **Monthly cash** comes from `model/monthly_cash.py`, which lays an AC-led seasonality over the annual plan:
>   - contribution and plan sales peak Mar–Jun
>   - people and fixed costs are flat
>   - stock and working capital build Feb–Apr
>   - clusters open in January and July
> - **Planning case = STRESS** (`Inputs!C2 = 4`).
> - **Method:** course Module 1 ("calculate the funding need, build assumptions, keep a sufficient runway").
> - **Instrument, valuation and cap table** are Step 9.

> ### Read this first (flags for approval)
> 1. **The ask: ₹7.5 Cr seed, in three tranches.**
>
>    | Tranche | Amount | When |
>    |---|---|---|
>    | T1 | ₹3.5 Cr | At close (target Mar–Apr 2027) |
>    | T2 | ₹2.5 Cr | Month 15 (Mar 2028), on demand and economics gates |
>    | T3 | ₹1.5 Cr | Month 24 (Dec 2028), after the first full AC season of plan claims |
>
>    *My first draft said ₹6 Cr. The review showed that the stress case could not reach its own Series A bar on ₹6 Cr.*
> 2. **Why ₹7.5 Cr:**
>    - In stress, the Series A metric (₹16–20 Cr revenue run-rate) is reached around **month 40**, so a Series A closes around **month 45 (Sep 2030)**.
>    - Monthly cash to month 45 is **−₹6.9 Cr**, and with 3 more months of buffer **−₹7.5 Cr**.
>    - **Base case:** the plan's whole monthly trough is ₹6.8 Cr, so in BASE the seed **just about** takes Keepwell to cash-positive (about ₹0.7 Cr margin).
> 3. **Cash before the close.** Today's ₹18 L lasts to about mid-January.
>    - **Bridge:** the pre-seed angels have agreed in principle to put in ₹40 L more (same iSAFE, Jan 2027) [Story]. We are also pulling forward the ₹5 L AP grant instalment.
>    - **Effect:** runway to about **June 2027**, so a 2–3-month slip in the close is survivable.
>    - **Conservative modelling:** the model still opens 2027 with only ₹18 L, which understates cash by about ₹27 L.
> 4. **Gates follow the plan's own path for a young cluster, not mature-cluster numbers** (§8.4). The month-15 gates are what the stress case expects at that age:
>    - attach ≥ 3.5% overall
>    - the pilot cluster covering its own team cost
>
>    **Claims are gated at month 24**, after about 1,000 plans have had a full summer of coverage. Month 15 would be too early to measure them.
> 5. **If the gates fail:** hold for at most 6 months to fix the failing number, then wind down in an orderly way.
>    - At month 15, cash left is **₹1.8 Cr in stress and ₹0.7 Cr in LOW**.
>    - An orderly wind-down costs about ₹0.45 Cr.
>    - Protect claims are paid from the ring-fenced reserve, and plans are transferred to a partner service centre.
> 6. **The ask is not very sensitive to single inputs.** One adverse input moves the stress need to month 45 from ₹6.9 Cr to **₹7.0–7.8 Cr**. The biggest single risks are no Protect (₹7.8 Cr) and a 1.0× head office (₹8.1 Cr). Head office is hired only against gates, so we control it (§8.3).
> 7. **Who** (the course's "Finding a Business Model" players):
>
>    | Investor | Amount | Role |
>    |---|---|---|
>    | Sector-focused seed VC | **₹5 Cr** | Lead |
>    | Strategic angels | **₹2 Cr** | Industry access |
>    | AP Startup Policy 4.0 seed equity | **₹0.5 Cr** | Government support |
>
>    Every amount is [Story/target]. India's median seed is about ₹8.5 Cr, so ₹7.5 Cr is below the median.
> 8. **Where it goes** (gross spend over 36 months, stress, ₹9.7 Cr): **65% people** (head office plus cluster teams); about 45% is self-funded from contribution and usable plan cash. The course's "about 25% on team" is a product-startup norm, and we say so.
> 9. **Series A** in 2030: **₹15–20 Cr** at a ₹16–20 Cr run-rate, to buy rollout speed. The bar is set so the stress case can meet it: mature cluster EBITDA **≥ 10%** (stress 10.7%) with the trend toward 14%.
> 10. **Toughest investor questions,** answered in §8.8:
>     - "You run out before we wire."
>     - "Is T2 designed to fail?"
>     - "How do you gate claims?"
>     - "Why hold rather than wind down?"

---

## 8.1 Starting position (Nov 2026, Step 2 [Story])

| Item | Amount |
|---|---|
| Raised so far | ₹70 L: ₹45 L pre-seed iSAFE (₹6 Cr post-money cap, 20% discount), ₹15 L founders, ₹10 L of the ₹15 L AP grant |
| Spent | about ₹52 L |
| Cash today | **₹18 L.** Protect counter-test cash is held in the reserve and excluded |
| Monthly burn now | about ₹9 L [Story]: founders' stipends, 2 engineers, the pilot cluster coordinator |
| Runway without action | **to about mid-January 2027** |
| **Bridge (Jan 2027)** | **₹40 L** from the pre-seed angels on the same iSAFE terms [Story], plus the ₹5 L grant instalment pulled forward. Founders' stipends are cut 50% until the close |
| Runway with the bridge | **to about June 2027**. The seed is targeted for Mar–Apr 2027, so this allows a 2–3-month slip |

## 8.2 What we need to fund

**The milestone is the Series A**, at the research bar of a ₹16–20 Cr revenue run-rate.

| Case | Year-4 revenue | Run-rate reaches ₹16 Cr | Series A closes |
|---|---|---|---|
| Stress | ₹20.5 Cr (Y3 ₹11.1 Cr) | about **month 40** | about **month 45** (Sep 2030), after a 5–6-month process |
| BASE | — | about month 30 | about month 36 |

**Monthly cumulative cash, before any seed money** (₹ Cr; opening ₹18 L; from `monthly_cash.py`):

| Month | 3 | 6 | 12 | 15 | 18 | 24 | 27 | 30 | 36 | 39 | 42 | 45 | 48 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Stress | −0.23 | −0.46 | −1.08 | −1.71 | −1.92 | −2.81 | −3.71 | −3.92 | −5.15 | −6.22 | −6.16 | **−6.91** | −7.50 |
| BASE | −0.21 | −0.40 | −0.95 | −1.66 | −1.76 | −2.66 | −3.57 | −3.46 | −4.53 | −5.56 | −4.84 | −5.40 | −5.77 |

Each year's trough comes in Jan–Mar. That is when new clusters open and stock is built, ahead of the season.

**Cash build by year, stress** (₹ Cr, from the model):

| | Y1 2027 | Y2 2028 | Y3 2029 | 3 years |
|---|---|---|---|---|
| Clusters (partner) / shops, year end | 3 / 150 | 5 / 250 | 9 (4) / 450 | |
| Head office | 0.85 | 1.36 | 2.21 | 4.42 |
| Cluster teams and partner support | 0.46 | 0.91 | 1.38 | 2.75 |
| Shop acquisition | 0.15 | 0.16 | 0.43 | 0.74 |
| Set-up, cluster working capital, parts stock | 0.12 | 0.32 | 0.38 | 0.82 |
| Growth working capital | 0.14 | 0.23 | 0.41 | 0.78 |
| Payment fees | 0.02 | 0.04 | 0.09 | 0.15 |
| **Gross spend** | 1.74 | 3.02 | 4.90 | **9.66** |
| less: contribution | −0.37 | −1.03 | −2.13 | −3.53 |
| less: usable plan cash (after the reserve) | −0.10 | −0.26 | −0.43 | −0.79 |
| **Net need** | 1.26 | 1.74 | 2.34 | **5.34** |

**By the course's five need columns** (36-month gross, ₹9.66 Cr):

| Column | ₹ Cr | Share |
|---|---|---|
| Build team: head-office people ₹3.5 Cr + cluster teams ₹2.75 Cr | 6.3 | 65% |
| Build product: tools, cloud, AI | 0.7 | 7% |
| Discover PMF: claims audits, legal opinion, gate audits | 0.2 | 2% |
| Marketing and sales: shop acquisition, Protect counter kits | 0.7 | 8% |
| Working capital | 1.6 | 17% |
| Fees | 0.15 | 2% |

**Hiring plan (head office; each hire after a gate waits for that gate):**

| When | Hires | Head-office run-rate |
|---|---|---|
| At close (Apr 2027) | 3 founders on market-minus salaries; 2 engineers (WhatsApp agent, dispatch, record) already on board; **finance and compliance lead** | about ₹0.85 Cr a year |
| After T2 (Mar 2028) | **Claims and quality lead**; 3rd engineer (data); 2 coordinators for clusters 4–5 | about ₹1.4 Cr a year |
| After T3 (Dec 2028) | **Partner-cluster regional lead**; second finance hire; data engineer | about ₹2.2 Cr a year (2029) |

## 8.3 Sizing the ask, and how sensitive it is

| Building block | ₹ Cr |
|---|---|
| Stress cash need to the Series A close (month 45) | 6.91 |
| Buffer: 3 more months, to month 48 | 0.59 |
| **Ask** | **7.5** |
| *Cross-check: BASE's monthly trough for the whole plan (month 50)* | *6.8. The seed covers it with about ₹0.7 Cr to spare* |
| *Cross-check: stress monthly trough for the whole plan (month 62)* | *10.0. About ₹2.5 Cr beyond the seed, covered by the Series A* |

**Sensitivity: stress need to month 45, one input at a time** (`monthly_cash.py`):

| Change on top of stress | Need to month 45 |
|---|---|
| Stress as planned | ₹6.9 Cr |
| Partner fee 12% | ₹7.0 Cr |
| Partner-cluster shop acquisition ₹28k | ₹7.2 Cr |
| Protect attach 3% | ₹7.3 Cr |
| Claims 55% | ₹7.3 Cr |
| 45 shops per cluster | ₹7.4 Cr |
| No Protect at all | ₹7.8 Cr |
| Head office 1.0× (not 0.85×) | ₹8.1 Cr |

**Reading the sensitivity:**
- The ₹7.5 Cr ask absorbs any one adverse input except no Protect or a heavier head office.
- **Head-office hiring is tied to the tranche gates**, so it only grows with proof.
- If Protect fails entirely, T3 is not drawn and the Series A is sized for the no-Protect plan.

**Alternatives considered:**

| Option | Stress runway | Verdict |
|---|---|---|
| ₹2.5 Cr angel round | about 22 months, no buffer | Ends mid-way to the Series A, so we would need a weak-position bridge in 2028 |
| ₹6 Cr (first draft) | to about month 41 | Misses the stress Series A close |
| **₹7.5 Cr, three tranches** | **to month 48** | **Recommended** |
| ₹10 Cr (stress whole-plan trough) | to cash-positive in stress | About a third more dilution at the lowest valuation, for money BASE never needs |

## 8.4 Tranches and gates

**Mechanics:**
- An independent CA firm certifies each gate from the Keepwell record (the data-room extract).
- The board, including the lead investor's director, confirms it.
- A majority of seed investors may waive a gate.
- All tranches are priced at the T1 price (Step 9).

**Runway on each tranche** (stress):

| Tranche | Amount | When | Covers stress cash to | Why that timing |
|---|---|---|---|---|
| **T1** | **₹3.5 Cr** | At close (Mar–Apr 2027) | about month 27 | Signed documents; the iSAFE and bridge convert; Protect legal opinion commissioned |
| **T2** | **₹2.5 Cr** | Month 15 (Mar 2028) | about month 41 | After the 2027 season and monsoon, and before the 2028 season build |
| **T3** | **₹1.5 Cr** | Month 24 (Dec 2028) | month 48 | After the first full summer of Protect claims (2028) |

**T2 gates (month 15).** Each threshold is the **stress path at that age**:

| # | Gate | Threshold | Stress path at month 15 |
|---|---|---|---|
| 1 | Density | ≥ 3 clusters live, **≥ 150 signed shops**, **≥ 65 units per shop per month** | 3 clusters, 150 shops, 74 units. Below 60 is the LOW case |
| 2 | Pilot cluster economics | Vijayawada–Guntur, **≥ 45 signed shops**, and cluster contribution **≥ its own team cost** (trailing 12 months) | The cluster is in its second year (60% of mature output). Contribution is about ₹27 L against a ₹22.8 L team. Step 6 targets 50+ shops |
| 3 | Protect demand | Attach **≥ 3.5%** of covered units across all shops; **≥ 5%** in the 12 shops on Protect since 2026 | 2% in a cluster's first year, 3.75% in its second, 5% from its third. The pilot test showed 6% |
| 4 | Legal | Opinion that Protect is a service contract; **reserve account open and funded** | — |

**T3 gates (month 24):**

| # | Gate | Threshold | Why it can be measured now |
|---|---|---|---|
| 5 | Protect claims | Claims over the 2028 summer on plans in coverage, annualised: **≤ 45% of net price** | About 1,000 plans sold in 2027 enter coverage in 2028 and have been through one full AC season |
| 6 | Claims, leading indicator | Repair incidence and cost on **1–3-year-old appliances** in Keepwell's own repair records (about 2,150 records from the pilot plus 2027 jobs) consistent with ≤ 45% | Read monthly from early 2027; cross-checks gate 5 |
| 7 | Partners | **3 signed partner-cluster agreements**, multi-brand work cleared by contract review; first partner cluster live in Jan 2029 | Partner clusters start in year 3 |

## 8.5 If gates fail: hold, then wind down with cash left

**Rule:** hold at 3 clusters for **at most 6 months** to fix the failing number. Expansion and gated hires are frozen. If the gate still fails, **wind down in an orderly way**. We do not stay in a slow-burn holding state: a 3-cluster hold still burns about ₹1 Cr a year.

| At the month-15 decision (T1 only) | Stress | LOW |
|---|---|---|
| Cash left (T1 + ₹18 L opening − cumulative burn) | ₹1.8 Cr | ₹0.7 Cr |
| 6-month hold burn | about ₹0.4 Cr | about ₹0.9 Cr |
| Orderly wind-down: 2 months' severance, lease exits, data-room close | about ₹0.45 Cr | about ₹0.45 Cr |
| **Left for investors** | **about ₹0.9 Cr** if we wind down after a failed hold | **about ₹0.25 Cr** if we wind down at once (LOW does not hold) |

**Protect customers are protected either way:**
- Claims are paid from the ring-fenced reserve (stress: ₹0.30 Cr at the end of 2028).
- The plans are novated to a partner service centre under contract.

## 8.6 Who we raise from

Course M1, "Finding a Business Model" stage: **early-stage VCs** (small, sector-specific seed rounds), **strategic angels** (industry access, pilot customers) and **government pilots**.

| Investor | Target | Why | Brings |
|---|---|---|---|
| **Lead: sector seed VC** (Bharat consumer, services or circularity thesis) | **₹5 Cr** | Prices the round, sits on the board, certifies the gates; pro-rata capacity for the Series A | Series A access; discipline |
| **Strategic angels** (4–6): ex-national service heads of appliance brands, a dealers'-association leader, a scaled field-service founder | **₹2 Cr** (₹30–50 L each) | Our advisor network (Step 2) | Brand authorisation, partner recruitment, shops beyond AP/TS |
| **AP Startup Policy 4.0 seed equity** | **₹0.5 Cr** | Policy offers up to ₹50 L (research) | Government channels; credibility with dealers |
| *Pre-seed iSAFE plus bridge holders (₹85 L)* | — | Convert at this round | Step 9: conversion terms |

**If the AP seed equity doesn't come:** the lead or angels take it up, or T1 is ₹3.0 Cr and T2 is drawn about 2 months earlier.

**Not chosen:**
- **Venture debt:** M2 positions it post-VC.
- **Revenue-based finance:** seasonal and pre-profit.
- **₹15 Cr+ "seed" cheques:** the dilution doesn't fit a patient operator.
- **SISFS:** don't count on it (Step 3).

## 8.7 Milestones and later rounds (memory rule: think ahead)

| By | Milestone | Funded by |
|---|---|---|
| Month 6 (Jun 2027) | 3 clusters in AP/TS; Protect in every shop; legal opinion done | T1 |
| Month 12 (Dec 2027) | 150 shops; about 1,100 plans sold; 3 partner LOIs | T1 |
| **Month 15 (Mar 2028)** | **T2 gates** | — |
| **Month 24 (Dec 2028)** | 5 own clusters, 250 shops; **T3 gates** (first summer of claims) | T1 + T2 |
| Month 36 (Dec 2029) | 9 clusters including 4 partner clusters; 450 shops; revenue ₹11 Cr (stress) to ₹15 Cr (BASE) | T2 + T3 + contribution |
| **Month 36–45 (2030)** | **Series A, ₹15–20 Cr** | — |

**Series A bar** (set so the planning case can meet it):
- ₹16–20 Cr revenue run-rate
- mature cluster EBITDA **≥ 10%**, trending to 14%
- Protect attach **≥ 5%** in clusters aged 3+
- claims **≤ 45%**
- 5+ partner clusters live

| Round | When | Size | Note |
|---|---|---|---|
| Seed (this) | Mar–Apr 2027 | ₹7.5 Cr in three tranches | Step 9: founder ownership after the iSAFE and bridge convert |
| Series A | 2030 | ₹15–20 Cr | Buys rollout speed; covers the stress tail (about ₹2.5 Cr) |
| Series B (optional) | 2032+ | Only to go beyond 72 clusters | BASE is cash-positive from year 5. Keep 1x non-participating preferences at every round (MediQuick) |
| Exit | 2033–34 | EV ₹325–545 Cr (Step 7b) | Strategic buyer or PE (Step 9) |

## 8.8 Hard questions

| Question | Answer |
|---|---|
| "You run out of cash before we wire." | The ₹40 L bridge from existing angels plus the grant instalment runs to about June 2027. The model doesn't even count it, so it is conservative by about ₹27 L |
| "Is T2 designed to fail, giving you a cheap option?" | No. Every month-15 threshold is the **stress path at that cluster age**, not a mature number. A business on its own planning case passes |
| "How do you gate claims with 72 plans and 10 months of coverage?" | We don't, at month 15. Claims are a **month-24 gate** after about 1,000 plans have had a full summer, cross-checked against our own repair records on 1–3-year-old appliances |
| "Why not wind down at month 15 instead of holding?" | The hold lasts at most 6 months and only to fix a named number. In LOW we wind down at once |
| "Your monthly troughs are deeper than your annual table." | Yes. The ask is sized on the **monthly** profile (₹6.9 Cr to month 45), not on the annual one (₹5.2 Cr at the end of year 3) |
| "65% of spend is people." | It is a field service. Each cluster pays back its own team from its second year (gate 2) |

## 8.9 Weak points, said before an investor does

- **The bridge and every investor amount are [Story] targets**, not commitments.
- **Monthly seasonality is an overlay** on an annual model. It is not a bottom-up monthly model, so the AC-season weights are assumptions. Fix: the pilot ledgers' monthly pattern, in the data room.
- **The claims gate rests on one summer.** Year-2 failure rates can rise, so the Series A bar repeats the claims test.
- **BASE only just reaches cash-positive on the seed** (about ₹0.7 Cr margin at the monthly trough).

---

## Decisions to approve (Step 8)

1. **Ask: ₹7.5 Cr seed**, sized on the stress monthly cash need to the Series A close (month 45) plus 3 months.
2. **Tranches:** ₹3.5 Cr at close; ₹2.5 Cr at month 15 (density, pilot-cluster economics, attach, legal); ₹1.5 Cr at month 24 (claims, partners). Gates certified by an independent CA.
3. **Bridge:** ₹40 L from the pre-seed angels plus the grant instalment, to cover a slipping close [Story].
4. **Fail rule:** hold for at most 6 months, then an orderly wind-down; Protect claims are paid from the reserve.
5. **Investor mix:** sector seed VC lead ₹5 Cr, strategic angels ₹2 Cr, AP seed equity ₹0.5 Cr. Instrument and valuation go to Step 9.
6. **Series A** in 2030, ₹15–20 Cr, with a bar the stress case can meet.
