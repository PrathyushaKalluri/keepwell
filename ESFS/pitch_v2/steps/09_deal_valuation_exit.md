# Step 9: Deal, valuation, cap table and exit

**Phase D (the deal). Status: FINAL (20 Nov 2026).**

> **Sources:**
> - Course M2 (instruments), M4 (valuation methods, stage table) and the MediQuick term sheet (clauses).
> - `keepwell_model.xlsx`, Funding sheet (built from `model/rounds.py`; 0 mismatches).
> - Research: `competitors_funding/findings.md`.

> ### Read this first (flags)
> 1. **Instrument:** **CCPS** (compulsorily convertible preference shares), the same instrument as the course's MediQuick term sheet. The pre-seed iSAFE (₹45 L) converts at this round.
> 2. **Valuation: ₹10 Cr pre-money, ₹12.5 Cr post. The seed takes 20%.** Course M4 says a raise should rest on **comparables plus the VC method**; the scorecard is "not market validated", so it serves only as a cross-check.
>
>    | Method | Result |
>    |---|---|
>    | Comparables (anchor) | ₹6–12 Cr pre |
>    | VC method, maximum post-money for a 40% IRR on a 5-year exit (stress) | ₹14.4 Cr (anchor ceiling) |
>    | Course scorecard (our 73/100 against the course's sample benchmark of 80) | ₹8.2 Cr pre (low end) |
>    | Weighted-factor scorecard | ₹10.0 Cr pre |
>
>    Our ₹12.5 Cr post sits **below the VC-method ceiling even in stress**.
> 3. **Cap table after the seed:** founders 64.0%, seed 20.0%, ESOP pool 10.0%, iSAFE 6.0%. After Rounds 2 and 3, **founders still hold 46.6%** and seed investors 14.6%.
> 4. **Seed-investor return** (diluted through Round 3):
>
>    | Exit | Return |
>    |---|---|
>    | Year 7, stress | **14.9×, about 47% IRR** |
>    | Year 7, BASE | 21.9×, about 55% IRR |
>    | Year 5 (the course's 3–5-year horizon), stress | 6.2×, 44% IRR |
>
>    All of them clear the course's 35–40% IRR bar.
> 5. **Terms follow MediQuick:**
>    - **Preferences:** 1x non-participating; broad-based weighted-average anti-dilution.
>    - **Founders:** 3-year lock-in; vesting already running since Aug 2025.
>    - **Governance and rights:** a 3-person board (2 founders, 1 lead-investor director) plus 1 observer for AP; pro-rata rights; information rights.
>    - **Exit clause:** a softer exit clause (a strategic sale in 7 years), not an IPO at ₹500 Cr in 5.
> 6. **Watch:** the Round 2 and Round 3 prices (₹30 Cr and ₹85 Cr pre) are plans. If Round 2 prices at ₹20 Cr pre, founders hold about 44% at exit (§9.5).

---

## 9.1 Instrument (course M2)

| Option | Fit | Decision |
|---|---|---|
| **CCPS (priced)** | Standard for an Indian priced seed. Investors get preference and protection. The course's MediQuick sheet uses it | **Chosen** |
| iSAFE / CCPS-based SAFE | Good for small pre-seed cheques; defers price. Already used at pre-seed | Converts now |
| Convertible note | Needs ≥ ₹25 L per investor (Companies Act / DPIIT rule). Several strategic angels write ₹15–25 L | Not used |
| Equity (ordinary) | No preference, so lead investors won't take it | Not used |

## 9.2 Valuation: three methods (course M4)

**1. Comparables**
- Indian angel/seed rounds in 2025–26: ₹1.5–2.5 Cr at **₹6–12 Cr pre-money** (research).
- Course MediQuick: ₹7.5 Cr pre.
- Our own pre-seed cap: ₹6 Cr post-money (Dec 2025, before the pilot).
- **Reading:** ₹10 Cr pre is a **1.67× step-up** after a pilot with ₹25 L revenue and 34 shops.

**2a. Course scorecard** (M4: benchmark valuation × company score ÷ benchmark score)
- Our Step 11 score is 73/100, against the course's sample benchmark of 80.
- **Result:** ₹9 Cr × 73/80 ≈ **₹8.2 Cr pre**, which is the low end.

**2b. Weighted-factor scorecard (cross-check only)** (base = ₹9 Cr, the midpoint of the comparable range)

| Factor | Weight | Score | Why |
|---|---|---|---|
| Team | 30% | 125% | Three domain founders with networks: 600+ dealers, 200+ service centres, the AI layer (Step 2) |
| Size of opportunity | 25% | 110% | ≈ ₹4,000 Cr TAM; Protect adds new spend (Step 4) |
| Product / technology | 15% | 100% | Working AI desk and record; not deep IP |
| Competitive environment | 10% | 100% | Incumbents each hold a slice; the shop channel is empty (Step 5) |
| Marketing / channels | 10% | 120% | The shop is the channel; cost to sign a shop ₹14k |
| Need for further funding | 5% | 90% | Two more rounds planned |
| Other (pilot, grant, CIE) | 5% | 100% | — |
| **Weighted** | | **111.5%** | **₹9 Cr × 1.115 ≈ ₹10.0 Cr pre** |

**3. VC method** (course M4: target IRR 35–40%, horizon 3–5 years; Funding sheet)

| | BASE | Stress |
|---|---|---|
| Year-5 (2031) enterprise value, at operator revenue × 2.5 + data revenue × 7 | ₹152 Cr | ₹106 Cr |
| Seed stake kept after Rounds 2–3 | 73% of 20% | 73% of 20% |
| Maximum seed post-money for a 35% / 40% IRR | ₹24.7 Cr / ₹20.6 Cr | ₹17.2 Cr / **₹14.4 Cr** |
| **Our post-money** | **₹12.5 Cr** | **₹12.5 Cr** |

**Conclusion: ₹10 Cr pre, ₹12.5 Cr post.** It is anchored on comparables (₹6–12 Cr) and sits under the strictest VC-method ceiling (₹14.4 Cr post). The course scorecard (₹8.2 Cr) marks the floor of the negotiation.

## 9.3 Cap table (fully diluted; Funding sheet)

| Holder | After seed | After Round 2 (₹5 Cr at ₹30 Cr pre) | After Round 3 (₹15 Cr at ₹85 Cr pre) / exit |
|---|---|---|---|
| Founders | 64.0% | 54.9% | **46.6%** |
| … Prathyusha (CEO, 38%) | 24.3% | 20.9% | 17.7% |
| … Kavyanth (COO, 31%) | 19.8% | 17.0% | 14.5% |
| … Sri Charan (CTO, 31%) | 19.8% | 17.0% | 14.5% |
| Pre-seed iSAFE | 6.0% | 5.1% | 4.4% |
| ESOP pool | 10.0% | 8.6% | 7.3% |
| **Seed investors** | **20.0%** | 17.1% | **14.6%** |
| Round 2 investors | — | 14.3% | 12.1% |
| Round 3 investors | — | — | 15.0% |

**How the iSAFE converts:**
- Terms: ₹45 L, ₹6 Cr post-money cap, 20% discount. The cap gives the better price (a 20% discount on ₹10 Cr is ₹8 Cr, above the cap).
- Result: the iSAFE takes 7.5% of the pre-money capitalisation, which is **6.0% after the seed**. Its holders' ₹45 L is worth ₹75 L at the seed price.

**ESOP:** a 10% pool after the seed. The course's MediQuick sheet uses 12%; we use 10% because the first key hires are known (Step 8). The pool is topped up at Round 2 if needed.

**Cap-table hygiene:**
- no side letters
- founders' vesting already running (4 years, 1-year cliff from Aug 2025)
- the AP grant is non-dilutive
- AP seed equity enters on the same CCPS as everyone else

## 9.4 Key terms (MediQuick as the template, adjusted for a ₹2.5 Cr seed)

| Clause | MediQuick (course) | Keepwell seed | Why different |
|---|---|---|---|
| Instrument and amount | CCPS Series A, ₹2.5 Cr | CCPS (seed), ₹2.5 Cr (minimum ₹2.0 Cr) | Same instrument; seed stage |
| Valuation | ₹7.5 Cr pre / ₹10 Cr post | **₹10 Cr pre / ₹12.5 Cr post** | Pilot revenue and a pre-seed cap already at ₹6 Cr |
| Board | 4: 1 investor, 2 promoters, 1 independent | **3: 1 lead-investor director, 2 founders; 1 AP observer.** An independent director is added at Round 2 | Small round, so a lean board |
| Liquidation preference | 1x non-participating | **1x non-participating** | Same. Keeps later rounds clean (no preference overhang) |
| Anti-dilution | Broad-based weighted average | Same | — |
| Pre-emptive / pro-rata | Yes | Yes | Lets the lead follow into Round 2 |
| Founders' lock-in | 3 years | 3 years | — |
| Vesting | 25% immediate, 75% over 4 years | **Already in place:** 4 years, 1-year cliff from Aug 2025 (Step 2). No reset | Founders are already 15 months in |
| ESOP | 12% post | **10% post** | See §9.3 |
| Affirmative votes | 16 matters | Same list, with thresholds scaled to a ₹2.5 Cr company: off-budget spend > ₹5 L, debt > ₹10 L, **any change to Protect's legal structure or reserve** | Protects plan customers |
| Information | Quarterly / annual / monthly metrics | Same, plus a **monthly Keepwell record extract** (jobs, attach, claims) | The milestones are measured on it |
| Exit | IPO at ₹500 Cr in 5 years, or strategic sale in 6 | **Strategic sale or secondary within 7 years**; drag-along at 70%+ after year 7 | A services operator. The plan's exit window is year 7–8 |
| ROFR / ROFO / tag / drag | Yes | Yes | — |

## 9.5 Seed-investor return, and the downside (Funding sheet; diluted through Round 3)

| Exit | Enterprise value | Seed stake | Value | Multiple | IRR |
|---|---|---|---|---|---|
| Year 5 (2031), stress | ₹106 Cr | 14.6% | ₹15.5 Cr | 6.2× | 44% |
| Year 5 (2031), BASE | ₹152 Cr | 14.6% | ₹22.2 Cr | 8.9× | 55% |
| **Year 7 (2033), stress** | **₹255 Cr** | 14.6% | **₹37.2 Cr** | **14.9×** | **47%** |
| Year 7 (2033), BASE | ₹376 Cr | 14.6% | ₹54.7 Cr | 21.9× | 55% |
| Year 8 (2034), BASE | ₹527 Cr | 14.6% | ₹76.8 Cr | 30.7× | 53% |

**Downside cases:**
- **LOW, stopped at the month-12 checkpoint:** wind down with about ₹0.35 Cr left. That is about **14 paise per rupee** returned under the 1x preference, ranking ahead of founders.
- **Round 2 priced at ₹20 Cr pre** (not ₹30 Cr): Round 2 takes 20%, seed holds 13.6%, and founders hold 43.5% at exit. The stress year-7 return is 13.9×.
- **No Round 3** (the BASE case is cash-positive from year 5): seed holds 17.1%, so the return is *higher*.

**What makes the multiples believable:**
- operator multiples (2.5× revenue), not marketplace or software multiples
- Frontdoor trades at about 2.9× revenue and 10.8× EBITDA (research)
- data revenue at 7× is 8–9% of revenue
- year-7 EBITDA cross-check: BASE ₹8.6 Cr × 25 ≈ ₹215 Cr; the mature run-rate ₹33 Cr × 12 ≈ ₹400 Cr

## 9.6 Exit path

| Buyer type | Why they buy Keepwell | Precedent (research) |
|---|---|---|
| **Warranty and after-sales platforms** | They sell plans through chains but have no owned delivery in small towns. Keepwell brings 3,300+ shops, partner clusters and the appliance record | Onsitego bought Qdigi (₹80 Cr, 2024); Asurion bought uBreakiFix (2019) |
| **Consumer-durables majors and regional chains** | An after-sales arm for independent dealers, beyond their own service centres | Reliance Retail's resQ; Aditya Vision's own-brand plans |
| **Insurers and plan underwriters** | Delivery capacity and claims data for appliance protection | Asurion |
| **PE (home-services roll-ups)** | Cash-positive operator with 12–13% mature margins | KKR acquired Neighborly (Mr. Appliance) in 2021; Frontdoor |

**Timing:** year 7–8 (2033–34), when the network is 55–72 clusters and EBITDA-positive.

**IPO:** not planned. An SME IPO is possible (Namo eWaste precedent) but not needed.

## 9.7 Weak points

- **The scorecard is our own scoring.** An investor will rescore Team and Channels lower until they meet the advisors.
- **Exit multiples assume an operator trade.** If no strategic buyer appears, a PE exit at 10–12× EBITDA gives about ₹86–103 Cr on BASE year-7 EBITDA (₹8.6 Cr). The seed still makes about 5–6×.
- **The Round 2 valuation needs the month-18 milestones.** That is exactly why they were set on the stress path.

---

## Decisions (Step 9, final)

1. **CCPS, ₹2.5 Cr at ₹10 Cr pre / ₹12.5 Cr post** (20%); the iSAFE converts at the cap (6.0%); ESOP 10%.
2. **MediQuick-based terms** with the changes in §9.4 (lean board, existing vesting, strategic-sale exit clause, Protect affirmative vote).
3. **Exit:** strategic sale or PE in 2033–34; IPO optional.
