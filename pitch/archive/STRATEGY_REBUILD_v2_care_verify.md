> **ARCHIVED, 18 Nov 2026. Not the current strategy.** Kept for the record only.
> The team reviewed this version and rejected both new products:
> - **Keepwell Care (₹1,499 plan sold by agencies): rejected.** An agency can sell its own AMC with its own technicians and keep all ₹1,499. Giving Keepwell ~₹1,250 of its own customer's money makes no sense. Extended warranties (retailer, brand, OneAssist) already cover the first 2–5 years, and older machines already have local AMCs.
> - **Keepwell Verify (₹20 a job for brands): rejected.** In-warranty repairs go to brand-authorised service centres, not independent agencies (mentor transcript). Repeat-visit cost mostly sits with the service centre, not the brand. The "proof" would come from the agency's own technician, and brands already run technician apps with photo and OTP closure, so a third-party "verification" adds nothing.
> - **Jobs per agency per day are unsourced** (2–15 a day across our own figures).
> Current direction: an evidence-first market study of retailer-led post-warranty repair in Tier 2/3 India, in `../market_intel/`.

# Keepwell strategy rebuild: who pays, how much, and why the money now
> **Illustrative case.** Founder histories, the company timeline, the pilot results and the financials are assumptions made for the IIIT Hyderabad ESFS course pitch. The research, the interviews, the evidence and the prototype are real. **Status: proposal for the team's decision (17 Nov 2026), version 2 after an independent investor red-team. The decks and the financial model are not changed until the team approves a direction.**

### How this was built
1. **Three specialist research agents ran in parallel:**
   - payers and budgets across a machine's after-sales life
   - 12 business models, scored
   - funding and round strategy
2. **Every strategy was modelled month by month for 6 years** in [`strategy_model.py`](strategy_model.py). Run `python3 strategy_model.py` and every table below prints.
3. **An independent agent playing the investor who said "zero value" attacked version 1.** It was right on most points (§11). Version 2 re-tested every strategy on its harder assumptions, and **the recommendation changed** as a result.

### Tags
- **[web]**: a public source checked in Nov 2026 (§13)
- **[repo]**: `ESFS/keepwell/`
- **[Real]**: our own interviews and evidence
- **[Model]**: `strategy_model.py`
- **[assumption]**: our estimate; it must be validated with real buyers before the pitch

---

## The answer in one page
**The investors were right about the old model. Our own numbers agree with them.** Charging agencies for a tool can't carry a venture. No single B2B "wedge" can either, once tested on honest assumptions. What does work is one platform with three products on one agency network and one record:
1. **Households pay** for a **Keepwell Care plan**, sold by the local agency they already trust, at the repair. They pay upfront.
2. **Brands and protection administrators pay** for **Keepwell Verify**: a prepared, verified, proven job on *their own* service networks, per job or per claim.
3. **Agencies are paid, not charged.** They earn plan commissions and paid service visits, and they use Circuit free. Circuit is the engine that makes every job prepared and verified, and every job grows the machine record.

| | Today's pitch | Proposed (lean, evidence-gated) |
|---|---|---|
| **Who pays** | Agencies, ₹40 per fix | **Households** (care plans, through agencies) + **brands and administrators** (Verify per job or claim) |
| **Agencies** | The customer | **Distribution and delivery partners**: they earn ~₹0.5–0.6 L more a year each, and get Circuit free |
| **Revenue Y1 / Y2 / Y3** | ₹0.20 / 0.85 / 3.64 Cr | **₹0.11 / 1.38 / 4.91 Cr** [Model] |
| **Revenue Y6** | ~₹31 Cr (plan G, extrapolated) | **₹28 Cr**, from three lines, most of it recurring [Model] |
| **Cash** | Paid in arrears | **Care plans are paid upfront**, so the deferred revenue funds growth |
| **The ask** | ₹4.75 Cr seed now at ₹19 Cr pre | **A 90-day validation sprint first** (existing cash), then **₹2.5 Cr now**, then a **₹6.5 Cr seed at month ~12–15**. Each step is gated on evidence [Model] |
| **Valuation** | ₹19 Cr pre on ~₹7 L ARR | Step A cap **₹12–15 Cr**; seed **₹15–20 Cr pre** |
| **Investor return on the seed** | ~24% IRR | **22–35%** at ₹15 Cr pre (3–5x revenue exit). Borderline, and we say so [Model] |

**The honest headline for the jury:** *we tested our own model, it failed, we found out why, and we rebuilt it around the people who actually have the budget.* The ask now buys **proof of two numbers that decide everything**:
- the **care-plan attach rate** through agencies (we assume 4%)
- **brands' willingness to pay per verified job** (we assume ₹20)

---

## 1. The feedback, and the honest diagnosis
| Problem | The number | Source |
|---|---|---|
| **Agencies were never shown to pay** | The evidence digest says "Agencies would pay: **not evidenced**. One mentor's opinion." The 14 paying agencies are illustrative | [Real] `EVIDENCE_DIGEST.md` §8 |
| **Agencies pay for jobs, not tools** | Urban Company takes **~28%** of partner earnings. Justdial earns **~₹19k a year** per paid listing. We asked **₹50.6k a year** for software | [web] |
| **The revenue is tiny next to the ask** | 24 months of revenue = **₹1.05 Cr** against a **₹4.75 Cr** ask | Plan G |
| **The market has a low ceiling** | Circuit-only tops out at **~₹23 Cr a year** | Step 7 |
| **The valuation is out of line** | ₹19 Cr pre on ~₹7 L ARR. Rough Indian SMB-SaaS norm: ₹7–10 Cr pre per ₹1 Cr ARR | [web, weak source] |
| **The investor's maths fails** | ~24% IRR, below the 35% hurdle | [Model] |
| **The roadmap is promises** | Plans, claims, parts and resale need partners or money not in the ask | Steps 7–9 |
| **The product was rail-locked** | The competition mandated **Pine Labs** (Reserve Pay caps at ₹10,000), **Delhivery** and **Gnani** (no confidence score). We scored them 5–6 out of 10 | [Real] Round 3 kit |

**The root cause.** We charged the party with the pain but not the budget. The parties with budgets were placed years away on the roadmap.

---

## 2. First principles: who has the pain and the budget?
| Rank | Payer | Budget a year (India) | Already pays third parties? | What it means for us |
|---|---|---|---|---|
| 1 | **Appliance brands** (warranty and installation) | Warranty **~₹1,900–3,700 Cr** (1.27% of ₹1.86 lakh Cr). AC installation **~₹1,500–1,900 Cr** | **Yes.** Blue Star ~2,100 partners; 247around routes for 150+ brands; Jeeves | They already *have* networks. Sell them **Verify on their own network**, not a replacement network |
| 2 | **Protection administrators and insurers** | **~₹3,100 Cr** appliance premium [repo]. OneAssist ₹623 Cr revenue at a 4.1% EBITDA margin | **Yes**, for repair partners and triage software | **Verify per claim**: evidence packs |
| 3 | **Households** (AMC, plans) | Eureka Forbes service alone **~₹875 Cr**; AMCs from ₹599 | **Yes.** Proven willingness to pay for machine subscriptions | **The largest recurring pool, and our insight fits it:** households trust *the person*, so the agency sells the plan |
| 4 | **Agencies** | Pay for **jobs** (UC ~28%, Justdial ~₹19k) | Yes, for demand | **Pay them; don't charge them** |
| 5 | Retailers | In-house crews (resQ, Jeeves, Croma) | Their own crews | Low priority |
| 6 | Financiers, EPR, parts, RWAs | Unproven for this use | No evidence | Vision only |

---

## 3. The options we considered, and what the model says about each
We scored 12 models (research, /50) and then **modelled the five serious ones over 6 years on the red-team's harder assumptions** [Model]:

| Strategy | Who pays | Revenue Y3 | Revenue Y6 | Verdict |
|---|---|---|---|---|
| **C. Agency tool (today)** | Agencies, ₹40 per fix | ₹3.64 Cr | — | Weak payer; ₹23 Cr ceiling. **Rejected** |
| **A. Verified service network** | Brands pay per resolved complaint; we pay agencies | ₹1.56 Cr | ₹5.3 Cr | **Rejected.** A middleman keeps ~₹101 a job (₹83 after costs) on mid-tier volumes; never profitable; ~0% IRR. Version 1 looked good only because the inputs were tuned (§11) |
| **B. Software-only API** | Enterprises, ₹25 L ACV | ₹3.42 Cr | — | Slow enterprise sales; weak moat without our own jobs |
| **D. Verify for brand networks** | Brands ₹20 per verified job; administrators ₹40 per claim | ₹3.28 Cr | ₹10.5 Cr | **Kept as a line.** 80% gross margin and no working capital, but ~₹0.6–0.8 Cr per customer: too small alone |
| **E. Keepwell Care plans** | Households, ₹1,499 a year, sold by agencies | ₹2.69 Cr | ₹18.9 Cr | **Kept as a line.** The biggest recurring pool and paid upfront, but slow to build alone |
| **E + D, lean (recommended)** | Households + brands/administrators, one shared team | **₹4.91 Cr** | **₹28.3 Cr** | **Recommended.** Two lines on one network and one record |

---

## 4. The recommendation: one platform, three products, one record
### What we sell, and to whom
| Product | Buyer | Price | Why they pay |
|---|---|---|---|
| **Keepwell Care** | The household, sold by its local agency at the repair visit | **₹1,499 a year per home**: 2 preventive services, labour-free repairs, priority visits, the machine record and reminders. Parts at the agency's rate, not covered (so it's a service plan, not insurance) | Households already buy AMCs. They trust their agency, and the agency sells at the moment of need |
| **Keepwell Verify** | Brands (on their own partner networks) and protection administrators | **₹20 per verified job; ₹40 per claim evidence pack**; ₹5 L setup | ~1 in 4 warranty visits is a repeat (₹400–700 each). A prepared visit plus a proof pack for every "part replaced" attacks repeat visits and inflated claims |
| **Circuit** | Agencies | **Free** | It's how jobs get prepared and verified, and how the record fills |

### Unit economics [Model; assumptions to validate]
**Care plan:**

| Line | New plan | Renewal |
|---|---|---|
| Price | ₹1,499 | ₹1,499 |
| Agency commission | (₹250) | (₹100) |
| Delivery (2 preventive visits + ~0.5 labour repair, paid to agencies, plus ops/AI) | (₹800) | (₹800) |
| **Contribution** | **₹449** | **₹599** |

- **Renewal rate:** 55% assumed.
- **Per agency:** at a 4% attach rate on 125 jobs a month, an agency sells ~60 plans a year. That earns it **~₹15k in commission plus ~₹36–45k in paid service visits**.

**Verify, per brand at full national rollout:**
- 4 lakh jobs × ₹20 = **₹0.8 Cr a year**, at about **80% gross margin**.
- Per administrator: 1.5 lakh claims × ₹40 = **₹0.6 Cr a year**.

### Why this beats the alternatives
1. **It answers every investor objection:**
   - Agencies are *paid*, so the value proposition is obvious.
   - The payers have real budgets.
   - Revenue per relationship is larger.
   - The roadmap lines are the business, not promises.
2. **It uses our real insight.** Households trust the person, not the work, so the trusted agency is the best distribution channel in Tier 2/3. Nobody else has it, because platforms take the customer away from the agency.
3. **It improves cash.** Care plans are paid upfront.
4. **It builds the moat faster.** Every plan visit, brand job and claim writes verified outcomes into one machine record.

### Is Circuit still the first product?
**As something agencies pay for, no. As the engine, yes.**
- Circuit is free to agencies.
- It's what makes a care-plan visit and a brand job *prepared* and *verified*.
- The first things we sell are **the care plan** (households) and **Verify** (brands).

### Freed from the case-competition rails
| Need | Forced rail (competition) | What we'd pick freely |
|---|---|---|
| Payments | Pine Labs Reserve Pay (₹10,000 cap) | **UPI autopay or a one-time UPI payment** for plans, through any payment aggregator; payouts to agencies by UPI |
| Parts | Delhivery | Not needed: agencies carry parts; local distributors are flagged by Circuit |
| Speech | Gnani (no confidence score) | **Gemini / Google Chirp, Sarvam as fallback**, all with confidence scores |
| Channel | — | **WhatsApp Cloud API** for households and agencies; a **REST API** for brands and administrators |

---

## 5. The plan, month by month (lean, evidence-gated) [Model]
| Month | Partner agencies | Active care plans | B2B payers signed | Run-rate revenue | Monthly EBITDA |
|---|---|---|---|---|---|
| 6 | 30 | 450 | 0 | ₹0.07 Cr | −₹13 L |
| 12 | 61 | 1,631 | 1 | ₹0.29 Cr | −₹14 L |
| 18 | 157 | 4,184 | 3 | ₹1.03 Cr | −₹33 L |
| 24 | 242 | 9,058 | 5 | ₹2.87 Cr | −₹25 L |
| 30 | 419 | 16,553 | 7 | ₹4.41 Cr | −₹41 L |
| 36 | 577 | 27,606 | 10 | ₹7.50 Cr | −₹29 L |

**Year by year:**

| | Y1 | Y2 | Y3 | Y4 | Y5 | Y6 |
|---|---|---|---|---|---|---|
| Revenue (₹ Cr) | 0.11 | 1.38 | 4.91 | 11.0 | 19.2 | 28.3 |
| EBITDA (₹ Cr) | −1.6 | −3.7 | −4.7 | −4.6 | −3.6 | −1.8 |

EBITDA turns positive around month 72.

**Honest caveat.** This is a 6-year path to profit, not a 3-year one. The model grows the team ahead of revenue (₹11 L a month rising to ₹60 L). If the two key numbers come in better (attach above 4%, renewal above 55%), the path shortens. If they come in worse, see §10.

### What happens in the first 24 months (the user's questions answered)
| When | What we do | Proof it creates | Funded by |
|---|---|---|---|
| **Days 0–90: validation sprint** | **Pre-sell Keepwell Care at 10 agencies** (refundable, at ₹1,499); measure attach and refunds. **Interview 5 brand service heads and 3 administrators**: current per-visit rate, repeat rate, what they'd pay per verified job. Apply to the Voltas–DPIIT PoC and HDFC ERGO TechPreneur | **The attach rate and a brand price, on paper** | Existing ₹21 L + SISFS ₹10 L (no new equity) |
| **Months 3–15: Step A** | Network 14 → ~60 agencies (TS+AP); first 1,600 active plans; first Verify pilot (one brand region) | A plan cohort and its first renewal signals; one paid Verify PO | **₹2.5 Cr Step A** + pilot revenue + GENESIS if eligible |
| **Month ~12–15: seed** | Raise once the attach rate and one brand contract are real | — | — |
| **Months 15–24** | ~240 agencies; ~9,000 plans; 5 B2B payers; claims evidence packs live with one administrator | Renewal rate on the first cohort; Verify across a brand's national network | **₹6.5 Cr seed** |
| **Months 25–34** | ~420+ agencies; four southern states; 7–10 B2B payers | ₹4–7 Cr run-rate, two revenue lines | Seed; Series A at ~month 30–34 |

### Parallel products: when, and what triggers each
| Product | Trigger | Built from | Funded by |
|---|---|---|---|
| Keepwell Care | Validation sprint shows ≥3% attach | Circuit + record (exist) | Step A |
| Verify for brands | One brand states a price ≥ ₹15 per job | Circuit + proof pack: **no new build** | Step A |
| Claims evidence packs | First administrator LOI | Verify | Seed |
| Door-step inspection | 2 exchange or administrator buyers | Same technicians and app | Seed / Series A |
| Parts demand signal | 1 lakh+ verified jobs | Record | Series A |
| Resale history and data services | Millions of consented records | Record | Series A+ |

---

## 6. Product and platform strategy
**Not "an AI service agency": one technology layer, built once, sold three ways.**
- **Circuit (the work layer):** intake in 6 languages, fault and part ranking, job card, technician verification. **Exists** (the prototype) [Real].
- **Verify (the trust layer):** a proof pack per job (photo, serial, part, the actual fault, outcome), warranty rules, an API. Partly exists; finish in months 1–6.
- **Record (the asset layer):** one consent-first record per machine, filled by every plan visit, brand job and claim.

Every roadmap product is a new buyer of the same layers. That is why the roadmap needs **less** new money than it looks: each new line adds customer success and sales, not a new product build.

---

## 7. The new ask and round shape [Model + funding research]
| | **0. Validation sprint** | **Step A: pilot round** | **Step B: seed** | **Step C: Series A** |
|---|---|---|---|---|
| **When** | Now → day 90 | Months 3–15 | Month ~12–15 | Month ~30–34 |
| **Amount** | ₹0 new equity (₹21 L cash + ₹10 L SISFS) | **₹2.5 Cr** equity + non-dilutive | **₹6.5 Cr** | ₹20–30 Cr [assumption] |
| **Why this much** | Pre-sales kits, interviews, travel | Peak need to month 15 + 15% contingency, less cash and grant [Model] | Peak need to month 34 + 15% contingency [Model] | Southern scale, claims, data |
| **Instrument** | — | **Second close of the existing iSAFE** at a **₹12–15 Cr post-money cap**, preference capped. *Two closes of one note* | Priced Seed CCPS, one class; both iSAFE closes convert | Series A CCPS |
| **From** | — | Existing angels (pro-rata), 2–3 strategic angels (ex-AMC/service head, ex-claims head), one micro-VC (Titan, 8i, AJVC, IPV) | A lead such as Blume, Elevation, Accel Atoms, BEENEXT | Seed lead's network plus a strategic |
| **Valuation** | — | ₹12–15 Cr cap (~17–20%) | **₹15–20 Cr pre** | Priced on run-rate |
| **Gate to the next step** | **Attach ≥3% on pre-sold plans; one brand price ≥ ₹15 per job** | ≥1,500 active plans; one paid Verify PO; ≥60 agencies | ₹4–7 Cr run-rate; renewal ≥50%; 7+ B2B payers | — |

**Investor return on the seed** (₹6.5 Cr, exit on revenue, later rounds dilute to 68%) [Model]:

| Entry | Exit year 6 at 3x / 4x / 5x revenue | Exit year 7 at 3x / 4x / 5x |
|---|---|---|
| ₹15 Cr pre | **22% / 29% / 35%** | 22% / 28% / 33% |
| ₹20 Cr pre | 17% / 24% / 29% | 18% / 24% / 29% |

**Read it honestly:**
- At ₹15 Cr pre, the investor clears 35% only at a 5x revenue exit.
- 3–5x is the range for recurring service plus software. HomeServe sold at ~2.5x and Domestic & General at ~2.3x, both service-heavy; Servify was valued at ~7.2x.
- **Do not present it as a 35%-IRR certainty.** Present the range, and the two numbers that move it.

**Non-dilutive money in the first 12 months:**
- SISFS ₹10 L (renegotiate the milestone)
- MeitY GENESIS up to ₹40 L (needs a pilot PO; **check Hyderabad eligibility**)
- paid Verify pilots ₹5–15 L each
- Google for Startups credits
- Voltas–DPIIT PoC and HDFC ERGO TechPreneur

**For a course pitch that needs one ask today:** present **₹2.5 Cr now** as the round, and show the seed as the next step with its gate. That is a more credible story than one big ask on unproven numbers.

---

## 8. Series A and exit
**Series A gates** (month ~30–34):
- ₹4–7 Cr run-rate, at least 40% of it renewing plans
- renewal ≥55%
- 7–10 B2B payers across brands and administrators
- verified records growing from both sides

**Base-rate warnings:**
- **Wify** (a brand-paid service network, 100+ brands) raised only a $3M Series A.
- **Onsitego bought Qdigi for ₹80 Cr.**

Mid-size exits are the realistic base case.

**Exit:** a strategic sale in years 6–8.

| Buyer | Why they'd buy |
|---|---|
| **Protection and plan players** (OneAssist, Onsitego, Zopper, Servify; Asurion globally) | A Tier 2/3 plan base sold through trusted agencies, plus verified repair data that lowers their claims cost |
| **Brands** | A verified service layer |
| **Urban Company** | Supply and plans |

**Value range** at 3–5x of ₹28 Cr year-6 revenue: **~₹85–140 Cr**. Precedents: Qdigi ₹80 Cr; Servify's tuck-ins such as 247around.

---

## 9. What changes in the pitch (only after the team approves)
**What stays:**
- the hook and Ramagundam
- the team
- the evidence wall and the listening
- the insight (*people trust the person*, which is now the distribution strategy)
- the problem map
- the vision and the record
- the moat (verified outcomes)
- compliance

**What changes:**
1. **Business model:** Care + Verify replace ₹40 per fix. Agencies become paid partners.
2. **Traction:** state only what's real (the prototype, research, agency relationships) plus the validation-sprint results once we have them. **No enterprise contracts we don't have.**
3. **Plan:** the lean combined model replaces plan G. Plan G and Strategy A are kept as "paths we tested and rejected": that honesty is a strength.
4. **The ask:** ₹2.5 Cr Step A at a ₹12–15 Cr cap, with the seed as the gated next step.
5. **Compliance:** add a legal opinion that a labour-and-maintenance plan without parts cover is a service contract, not insurance.
6. **Financial model:** a new tab built from `strategy_model.py`.
7. **Step documents:** reopen Steps 3, 4, 6, 7, 8 and 9.

---

## 10. Risks and kill criteria
| Risk | Test | Kill or pivot |
|---|---|---|
| **Households won't buy plans from agencies** | Pre-sales at 10 agencies in 90 days | Attach below 2% → drop Care; Verify becomes the core, with a smaller ask |
| **Brands won't pay for Verify** | 5 interviews + one paid PO by month 9 | No PO by month 9 → administrators first (claims evidence) |
| **Renewals are weak** | First cohort at month 12–15 | Below 40% → reprice or bundle into brand warranty extensions |
| **Plan delivery costs more than ₹800** | Actual visits per plan from the first cohort | Above ₹1,000 → cut labour-repair cover; price to ₹1,799 |
| **IRDAI treats the plan as insurance** | Legal opinion before launch | Keep parts out of cover; or sell through a registered administrator partner for a commission |
| **Agency quality** | First-time fix and complaints per agency | Drop weak agencies; keep a bench |
| **Servify or Urban Company copy it** | Speed in Tier 2/3; agencies as partners (UC takes their customers; we don't) | Partner or sell to a protection player earlier |
| **Hiring runs ahead of evidence** | Hiring is gated on each step's proof | Freeze hiring if a gate is missed |

**Combined downside** (attach 2.5%, half the agency growth, brand fee ₹12 on half the jobs) [Model]:
- Revenue Y3 **₹2.04 Cr**, Y6 **₹10.2 Cr**.
- It needs **₹2.75 Cr + ₹9.0 Cr**.

**In that case we would not raise the seed as planned.** We would narrow to whichever line is working.

---

## 11. Independent investor red-team (version 1 → version 2)
*An independent agent, playing the seed VC who gave the original feedback, reviewed version 1 (a "verified service network": brands pay ₹475 per job, we pay agencies ₹325). **Verdict: pass, second meeting only with real evidence.***

| # | Objection | What we changed |
|---|---|---|
| 1 | **Nobody who would pay has been asked.** Prices and volumes are assumptions | Added the **90-day validation sprint before any new equity**: pre-sold plans and brand interviews. Every number is still tagged [assumption] |
| 2 | **Why pay a middleman to reach agencies brands already use?** Our take was 31.6%, *not* less than Urban Company's 28% (our claim was false) | **Dropped the middleman model (A).** Re-modelled honestly it fails (~₹83 contribution a job, never profitable). Brands now buy **Verify on their own networks**. The false Urban Company claim is removed |
| 3 | **Volumes were tuned** (1,200 jobs a month, 100% conversion, no churn) | Mid-tier volumes; **70% conversion; 8–10% churn**; expected-value modelling |
| 4 | **The ₹12 L platform fee carried the software story** | Replaced by usage pricing per verified job, with stress tests at ₹12 and on half the jobs |
| 5 | **A low-margin ops business valued as software**; re-visit reserve too thin | Verify is ~80% gross margin. Care plans are valued at 3–5x revenue (service comparables), not 6–7x |
| 6 | **Rounds priced too high; Step A too short** | Step A cap **₹12–15 Cr**, runway **to month 15**; seed at **₹15–20 Cr pre** |
| 7 | **IRR cleared in the base case only** | Now shown as a **range (17–35%)**; we say it's borderline |
| 8 | **Working-capital debt; downside tested one shock at a time** | Care plans are paid upfront (no receivables problem); Verify's receivables are small. **A combined downside** is shown (§10) |
| 9 | **Servify / 247around / Wify already do this** | We no longer compete as a network. We **sell Verify to brands' existing networks** and **sell plans through agencies**, a channel platforms can't use without taking the customer |
| 10 | **Can this team sell to enterprises?** An administrator was signed at month 6 | The first administrator is now at month 10+. B2B starts *after* the household line proves the network. Step A includes a commercial lead |
| 11 | **Inconsistent numbers** (records gate, ARR gate, Series A size) | All gates in §5 and §8 are taken from the model output; the Series A is resized to ₹20–30 Cr |

**What this round of red-teaming taught us.** The first version looked good because it was tuned to clear the bar. The honest version is smaller and slower, but it is **believable**, and it is the version that answers "zero value": every party in it is either paid or saves money.

---

## 12. The next 3 actions (real-world, not modelling)
1. **Run the 90-day validation sprint:**
   - **Pre-sell Keepwell Care at 10 partner agencies** (refundable). Target ≥3% attach.
   - **Interview 5 brand service heads and 3 administrators.** Ask for their per-visit rate, repeat rate, and a price per verified job.
2. **Get a legal opinion** that a labour-and-maintenance plan without parts cover is not insurance.
3. **Reopen Steps 3, 4, 6–9**, then rebuild the deck and model from this document. Only after the sprint data is in, decide the final ask.

---

## 13. Sources
- **Payers:**
  - [IBEF consumer durables](https://www.ibef.org/industry/consumer-durables-presentation)
  - [Warranty Week, Jun 2026](https://www.warrantyweek.com/archive/ww20260625.html)
  - [ICRA room-AC volumes](https://ianslive.in/room-ac-sales-surge-to-record-high-of-125-million-units-in-india-report--20241015112513)
  - [Samsung installation charges](https://www.samsung.com/in/support/home-appliances/ac-installation-and-repair-service-charges/)
  - [Servify acquires 247around](https://www.businesswireindia.com/servify-acquires-247around-an-at-home-service-platform-specialising-in-connecting-consumers-with-oems-service-network-77389.html)
  - [Servify FY25](https://www.pulse.bot/small-cap-stocks/news/us-emerges-as-servifys-largest-market-in-fy25-with-rs-400-cr-revenue-0f091502-40db-475e-b46e-0421dec4de8e)
  - [OneAssist FY25](https://entrackr.com/fintrackr/oneassist-posts-over-rs-620-cr-revenue-in-fy25-with-rs-26-cr-ebitda-10067658)
  - [Zopper](https://businessindia.co/amp/story/magazine/insurance/reshaping-access-zopper-takes-insurance-to-the-next-level)
  - [Jeeves](https://smestreet.in/infocus/flipkarts-jeeves-offers-end-to-end-post-purchase-solutions-to-businesses-and-customers)
  - [Eureka Forbes Q4 FY25](https://www.kotaksecurities.com/investing-guide/articles/eureka-forbes-q4fy25-results)
  - [Urban Company partner earnings](https://investorrelations.urbancompany.com/announcements-and-highlights/service-partners-earnings-index-9m-fy26)
  - [Urban Company take rate](https://inc42.com/features/inside-urban-companys-marketplace-model-what-it-keeps-from-every-booking/)
  - [Justdial FY26](https://www.investywise.com/just-dial-q4-fy26-financial-results/)
  - [Blue Star network](https://themachinemaker.com/news/blue-star-launches-new-range-of-room-air-conditioners-and-unitary-cooling-solutions-for-summer-2026/)
- **Models and comparables:**
  - [Frontdoor FY2025](https://www.businesswire.com/news/home/20260226042868/en/Frontdoor-Announces-Record-Full-Year-2025-Financial-Results)
  - [Brookfield–HomeServe](https://www.lse.co.uk/news/canadas-brookfield-to-buy-homeserve-in-16341bn-deal-tmmogu8oqkton23.html)
  - [Asurion–Domestic & General](https://asurion.com/press-releases/asurion-acquires-domestic-and-general/)
  - [Avoca $1B](https://pulse2.com/avoca-125-million-raised-at-1-billion-valuation-to-power-services-economy-with-ai/)
  - [IRDAI low-ticket commissions](https://www.businesstoday.in/personal-finance/story/rs800-premium-rs40-commission-why-low-ticket-insurance-could-become-the-biggest-casualty-of-new-rules-557628-2026-09-24)
- **Funding:**
  - Inc42 funding reports 2025–26
  - InnoVen Early-Stage Insights (May 2025)
  - Entrackr (Wify, 2024)
  - myScheme/ClearTax (SISFS)
  - MeitY GENESIS and SAMRIDH guidelines
  - cloud.google.com (Google for Startups AI tier)
  - The Week (Voltas–DPIIT MoU, Mar 2026)
  - ThePrint (HDFC ERGO TechPreneur)
  - YourStory (Onsitego–Qdigi ₹80 Cr)
  - **Some benchmarks come from consultancy blogs: verify them before quoting.**
- **Internal:**
  - `ESFS/keepwell/*`
  - `ken-case-competition-2026/EVIDENCE_DIGEST.md`
  - `ken-case-competition-2026/ROUND3_KIT/` (the mandated rails)
  - `ESFS/pitch/steps/*`, `keepwell_model.xlsx`
