# Step 0: Validation report, retailer-led lifecycle idea (Gate 1)

> **Illustrative case** for the IIIT Hyderabad ESFS course pitch. The research is real and sourced. Model inputs are tagged.
>
> **For approval.** This is the only document to review at this gate. Steps 1–13 begin only after you approve it.

**Supporting files.** You don't need to read these to decide.

| File | What it holds |
|---|---|
| `00_tough_questions.md` | 45 questions from four perspectives, each answered or turned into a pilot test |
| `00_unit_economics.md` | The full rebuilt model |
| `ue_v2.py` | The engine behind the numbers |
| `research/` | Three research reports with about 260 sources, plus the course texts |

---

## 1. The verdict in one paragraph

**The problem is real.** The retailer sells and then loses the customer. Installation and after-sales in small towns are slow and untrusted. The retailer can be held jointly liable when things go wrong, and nobody keeps the appliance's record.

**The founders' solution, as written, does not survive the evidence.** It assumes we can install any AC the retailer sells. But **installation by anyone the brand hasn't authorised voids the AC warranty** at Samsung, Daikin, Carrier, IFB, Godrej and Panasonic. Re-priced on the evidence, that design needs **188 retailers per cluster** to break even.

**A redesigned version can work**, but only under three conditions:
1. Keepwell becomes a **brand-authorised (or sub-contracted) installation partner**.
2. It works with **every independent shop in a cluster**, large and small. Viability is measured in **units sold per cluster each month (about 2,400)**, not in a count of shops (see §4c).
3. It serves **four appliances (AC, washing machine, refrigerator, water purifier), with AC as the anchor**. The market and the numbers are shown for all four; ACs carry most of the value (see §4b).

On fair inputs, a cluster breaks even at **29–44 retailers**, not the 21 in the founders' document. Contribution is **₹3.8–5.8k per retailer per month**, not ₹7.8k. This is **a 15–20% contribution operator**, so it must be pitched as a density business that is honest about its margins.

**Fundable?** Yes, as an early round that buys proof. The red-team angel would invest **₹30 L in a ₹75 L–1 Cr round** (iSAFE, about ₹6 Cr cap, released in two parts), **not ₹2 Cr at ₹10 Cr**. The round is set properly in Step 8 from costed needs.

---

## 2. What holds and what breaks in the founders' document

| Claim in the document | Verdict | Evidence | Corrected value |
|---|---|---|---|
| Retailer loses the customer after the sale and gets blamed | **Holds** | Consumer commissions have held the seller jointly liable (Chennai ₹35k, Chandigarh, Hyderabad ₹60k) | Use as the retailer's pain |
| We install within 24 hours, customer-paid, ₹650 blended | **Breaks** | A non-authorised AC install voids the warranty. Flipkart and Reliance accept returns only after an authorised install | We must be authorised. Then an AC install is worth about ₹2,000–2,400 net |
| Brand installation takes 3–5 days | **Partly** | LG: 24–72 h. Flipkart: 2–5 days. One documented no-show. Tier 2/3 data: none | Measure 30 installs in the pilot |
| 1.2 L outlets → 23,400 serviceable retailers | **Breaks** | LG has 30,726 dealers, Voltas 30k+, Blue Star 10k+; 40–65% of sales go through independent shops | **5k / 9k / 18k** serviceable (BASE 9k) |
| ₹4,000 Cr TAM | **Breaks** | Follows from the retailer count | About **₹1,550 Cr** (BASE) |
| A shop sells 100 units a month | **Optimistic** | No source exists. Our working range is 30 / 60 / 120 | Use units per cluster, not shop size (§4c) |
| A technician does 76 jobs a month and earns ₹30k | **Breaks** | Urban Company partners average about 43 orders a month (₹28k net); a Tier 2/3 mechanic earns ₹10–25k | About 49 jobs a month. ₹30k needs about ₹610 a job |
| AMC at ₹1,800 | **Breaks** | Urban Company sells a 2-service AC plan for ₹1,098–1,298 | ₹1,299 including GST |
| Prices are net | **Breaks** | We pay 18% GST as principal; a local mechanic under ₹20 L turnover pays none | Repair and AMC prices must include GST |
| 17–19% contribution, rising with the layers | **Holds at 15–20%**; the layers are unproven | Refurbishment about 15.7% gross (Cashify); EPR goes to recyclers; parts margin UNKNOWN | Pitch 15–20%; the layers are upside |
| Retailer earns about ₹3,500 a month | **Holds roughly** | A shop's net is 2–3% (₹36–54k a month), so this matters to it | ₹2–3.5k |
| Nobody serves the independent retailer end to end | **Holds, untested** | 247around and SERVIZ (brand-paid), Onsitego, Zopper and OneAssist (plans), Jeeves and resQ (captive). No one does the full job for independent Tier 2/3 shops | Onsitego is the closest threat |
| ₹2 Cr at ₹10 Cr pre-money | **Too rich for the evidence** | Benchmarks are ₹6–12 Cr pre-money, and ₹6–8 Cr without data. The red team suggests ₹75 L–1 Cr at a ₹6 Cr cap | Decided in Step 8 |

---

## 3. The red team, in brief

A fresh agent played a sceptical angel investor and saw none of our reasoning. Its 12 objections are summarised below, along with our answers.

| # | Objection | Our answer |
|---|---|---|
| 1 | No brand has authorised you; existing service centres hold the slots | Agreed, this is the main risk. The redesign makes **authorisation, or a sub-contract under an existing service centre**, the first milestone before any cluster spend |
| 2 | Retailers don't pay for service | Agreed. **The desk fee is dropped.** The retailer is the demand source and the trust surface, not the payer |
| 3 | Partner technicians keeping their own customers means leakage by design | 10% leakage is now built into the model. Mitigations: the guarantee only applies when booked through us, payment through us, a QR code on the unit, parts on credit. Measured in the pilot |
| 4 | Technician productivity has no cost in variant E | Fixed. Variant F pays a minimum floor in the off-season to a core half of technicians and checks capacity at the peak |
| 5 | The filler jobs aren't counter-cyclical | Fixed. Replaced by a **contracted fulfilment deal with a plan seller** (Onsitego or Zopper type, 100 jobs a month), shown with and without the contract |
| 6 | The materials margin is unmeasured, and the figure was counted including GST | Fixed. Now net of GST at a 20% margin. Measured from 30 invoices |
| 7 | Repair is thin (19%) | Agreed. Repair is volume and record-building, not profit |
| 8 | The capital path needs three rounds | Agreed. Step 8 plans each round around a milestone, with dilution |
| 9 | Onsitego already holds the counter | Redesign: make Onsitego and Zopper **customers** for fulfilment, not competitors |
| 10 | Everyone who ran operations stopped | We take the risk deliberately: one cluster, one summer, with kill criteria |
| 11 | CAC, churn and fixed costs are unsourced | Fixed. Fair inputs are now CAC ₹22k, churn 25%, AMC visit ₹400. A two-week founder sales sprint will measure them |
| 12 | The team has no retail-sales experience; the "14 agencies" claims conflict | **The backstory is rebuilt from scratch in Step 2**, dropping the agency history. One founder gets dealer-channel experience |

**The red team's middle case:** contribution of about ₹4.2k per retailer and breakeven at about 40 retailers. Our variant F on fair inputs gives a similar ₹3.8k and 44.

---

## 4. The solution options we tested (same engine, BASE)

| Design | What changes | Contribution per retailer per month (all-in) | Breakeven retailers per cluster | Verdict |
|---|---|---|---|---|
| Founders' design, re-priced on evidence | Not authorised, so no in-warranty AC installs | about ₹0.9k | 188 | Not viable |
| A. Authorised partner, salaried technicians | Paying a ₹22k income floor through the off-season | about ₹4.6k | 36 | Too costly in the trough |
| C. A + retailer desk fee | Assumes retailers pay ₹2,500 a month | about ₹6.0k | 28 | No precedent for retailers paying, so dropped |
| D. Asset-light routing | We only route jobs and take a 20% fee | about ₹1.8k | 53 | Too thin; repeats the earlier ₹56-a-job result |
| E. Hybrid with desk fee and filler jobs | | ₹9.1k | 19 | **Tuned, according to the red team. Rejected** |
| **F. Recommended: AC-first, paid by businesses, retailer as the source** | See §5 | **₹3.8k at 60 units; ₹5.8k at 100 units** | **44 at 60 units; 29 at 100 units** | **Viable only with larger shops plus authorisation** |

**How retailer size moves variant F** (fair inputs; the engine runs `variant_F` with `units_month` changed):

| Units per month | Revenue per retailer | Contribution per retailer | Breakeven retailers | Cluster EBITDA at 30 retailers |
|---|---|---|---|---|
| 60 | ₹20.7k | ₹3.8k | 44 | −₹0.50 L |
| 80 | ₹26.2k | ₹4.9k | 34 | −₹0.19 L |
| **100** | **₹31.8k** | **₹5.8k** | **29** | **+₹0.10 L** |
| 120 | ₹37.4k | ₹7.0k | 24 | +₹0.44 L |

**Stress tests at 60 units:**
- With no brand authorisation, breakeven rises to 80 retailers. **Authorisation is a go/no-go gate.**
- Without the plan-seller contract, breakeven rises to 50.

---

## 4b. AC only, or four appliances? (decision added after your review)

**Your concern was that the idea broke because it covered many products. It didn't.** It broke on five other inputs: installation authorisation, the number of retailers, technician productivity, the AMC price and GST.

**We should not pitch AC only.** I re-ran the same fair inputs with each category's own repair frequency, bill, parts share and seasonality, using `variant_G` in `ue_v2.py` with 80 units a month and 30 retailers:

| Portfolio | Revenue per retailer per month | Contribution per retailer per month (all-in) | Breakeven retailers | Cluster EBITDA at 30 | Seasonal peak index |
|---|---|---|---|---|---|
| AC only | ₹26.6k | ₹4.5k | 37 | −₹0.30 L | 1.80 |
| AC + washing machine + refrigerator | ₹29.1k | ₹5.2k | 32 | −₹0.09 L | 1.63 |
| AC + water purifier | ₹28.5k | ₹4.9k | 34 | −₹0.19 L | 1.72 |
| **AC + WM + fridge + water purifier (recommended)** | **₹31.0k** | **₹5.5k** | **30** | **+₹0.01 L** | **1.59** |
| All five (+ geyser) | ₹31.5k | ₹5.7k | 29 | +₹0.07 L | 1.55 |

| Portfolio at 100 units a month | Contribution per retailer per month (all-in) | Breakeven retailers | Cluster EBITDA at 30 |
|---|---|---|---|
| AC only | ₹5.5k | 30 | ₹0.00 L |
| Four appliances | ₹6.9k | 25 | +₹0.41 L |

**What the comparison shows:**
- **The four-appliance portfolio is better on every measure.** It brings about 17% more revenue and 23% more contribution per retailer, and needs 7 fewer retailers to break even. The difference comes from better use of technicians across the year.
- **The year is smoother.** The seasonal peak index falls from 1.8 to 1.6, because washing machines, fridges and purifiers keep technicians busy from October to February.
- **The retailer gets one partner for everything it sells.** A retailer won't hand us its ACs and keep calling someone else for washing machines.
- **The market is larger.** It is sized on everything the retailer sells (about ₹1,550 Cr retailer-linked, BASE), not AC alone.

**Why AC is still the anchor:**
- AC is about 85% of the value per retailer, because it brings brand-authorised installs, frequent paid service, gas refills and the only AMC customers readily buy.
- So AC leads the go-to-market and the first-season test.
- A pilot that starts before summer will be AC-heavy in volume anyway. **That is a test plan, not the business definition.**

**Where the other categories earn less:**
- Refrigerator and washing machine repairs are rare (0.08–0.17 a year per unit).
- Water-purifier filter visits are frequent but small.
- So these categories add utilisation and stickiness more than profit.
- Geyser adds little and stays optional.

**Decision:** pitch and model **four appliances (AC, washing machine, refrigerator, water purifier)**, with AC as the anchor. Run the pilot on all four, timed to catch the AC season.

**Correction to the earlier F variant:** it was labelled "AC-first" but already counted the repair events of every category. These per-category numbers replace it.

## 4c. Every shop, or only large shops? (added after your review)

**The earlier "80+ units" cut was a modelling shortcut, not a finding.** Units per shop was the input that moved results most, so I filtered for big shops. Re-running by shop size shows that a small shop earns us **the same per unit sold**:

| Shop sells (units a month) | 15 | 30 | 45 | 60 | 80 | 100 | 120 |
|---|---|---|---|---|---|---|---|
| Contribution per shop per month (4 appliances) | ₹1.2k | ₹2.3k | ₹3.5k | ₹4.7k | ₹6.3k | ₹7.8k | ₹9.4k |
| Contribution per unit sold | ₹78 | ₹78 | ₹78 | ₹78 | ₹78 | ₹78 | ₹78 |
| Months to pay back ₹22k field-sales onboarding | 31 | 16 | 12 | 9 | 8 | 7 | 6 |
| Months to pay back ₹6k self-serve onboarding | 10 | 6 | 5 | 4 | 3 | 3 | 2 |

**What the table shows:**
- **Small shops are not less profitable per unit.** The only difference is the cost of signing them up. A field salesperson costs the same whether a shop sells 15 units or 120.
- **What a cluster needs is units, not big shops.** It must cover ₹1.65 L of fixed costs plus the off-season floor for technicians. That takes about **2,100–2,400 units sold a month across all its shops**, for example:
  - 30 shops at 80 units, or
  - 15 large shops plus 40 small shops.
- **So we work with every shop and give each a different sales motion:**
  - **Large shops (60+ units):** field sales, a demo, signage and a cluster-manager relationship, at about ₹22k CAC.
  - **Small shops (under 60 units):** self-serve onboarding over WhatsApp, with a QR standee, a referral from a nearby large shop and no field visit, at about ₹6k CAC (an assumption, to be tested).
- **The market grows.** The serviceable base becomes every independent large-appliance dealer: **30k / 45k / 70k**, not 5–18k. This also helps the story: we serve the long tail that chains and platforms ignore.
- **Small shops add density.** More shops in the same town shortens travel between jobs and raises technician jobs per day.

**Decision:** work with **every shop in the cluster**. Set cluster targets in **units sold per month**. Sales effort goes where the units are.

## 5. The recommended solution shape (to build Steps 1–13 on, if you approve)

**Keepwell is the authorised after-sale service arm for small-town appliance retailers. It covers ACs, washing machines, refrigerators and water purifiers, with AC as the anchor.**

1. **Who it serves.** **Every independent multi-brand appliance shop in a cluster** (30k / 45k / 70k nationally). Large shops get field sales, and small shops onboard themselves through WhatsApp (§4c). Keepwell works under the retailer's name, so the customer stays the retailer's.
2. **Who pays.**
   - **Customers** pay for out-of-warranty AC service, repair and AMC. Prices include GST and sit at the market rate.
   - **Brands, or their authorised service centres,** pay for in-warranty installs (we are authorised or sub-contracted). Customers pay the brand rate card and buy materials.
   - **Plan sellers** (Onsitego or Zopper type) pay per job to have their small-town claims fulfilled.
   - **The retailer earns** a commission and keeps its customer. It pays nothing.
3. **Moat.**
   - Multi-year, exclusive service-arm agreements with retailers that include a revenue share (the HomeServe pattern).
   - Cluster density.
   - Certified partner technicians.
   - The appliance record.
4. **Technicians.**
   - Certified partners paid per job, with an off-season floor for a core group.
   - Keepwell gives them what they can't get alone: parts on credit, insurance, the guarantee, a certificate and steady jobs.
   - Their own customers can join the platform, which turns leakage into volume.
5. **Technology (the CTO's thread; Keepwell is the only name).** An AI orchestration layer that:
   - takes voice and WhatsApp requests in Telugu, Hindi and English
   - predicts the fault and the likely part
   - dispatches the job
   - checks quality from photos and the serial number
   - keeps the appliance record and its QR code
   - sends AMC reminders
   - shows the retailer a summary

   It costs under ₹5 a job, and one cluster manager plus one dispatcher can run about 30 retailers. **The AI is the cost engine, not the moat.**
6. **Order of build.**
   1. **From day one:** all four appliances, covering installs (authorised), out-of-warranty service and repair, and AMC (AC and water purifier).
   2. **Then:** parts.
   3. **Last:** refurbishment and EPR, only once the data supports them. Geyser is optional.
7. **First proof.** **One cluster through one summer (Mar–Jun 2027)**, not three clusters in 13 months.

**What must be true in the first 90 days (the kill criteria):**
- Written authorisation, or a service-centre sub-contract, covering at least 30% of the pilot shops' AC units, with the payout known.
- Ledgers from the pilot shops showing at least 2,000 units a month across the cluster, with the size mix measured.
- 15 retailers live and routing at least 50% of AC installs to us.
- 8 technicians with jobs per day measured, and no more than 1 leaving.
- A fulfilment talk open with Onsitego or Zopper.
- Contribution per retailer of at least ₹4k by month 4.

---

## 6. Course check: where the idea stands now (provisional; scored properly in Step 11)

**M1 stage.** Stage 2, finding the business model. The course benchmark for Seed VC at this stage is ₹50 L–2 Cr at a 35–40% IRR over 3–5 years. The red team's ₹75 L–1 Cr fits inside it.

**M3 fundability matrix:**

| | Potential | Uniqueness | Quality |
|---|---|---|---|
| **Market** | Medium: about ₹1,550 Cr retailer-linked; ACs growing 15% a year | Medium: an untested niche (independent Tier 2/3 shops) | Low–Medium: thin margins, depends on density |
| **Product** | Medium: a lifecycle path from installation to recycling | Medium: authorised plus a full lifecycle plus the record | To prove: first-visit fix rate, rating |
| **Startup** | Depends on the Step 2 backstory | Retailer agreements and density, if signed | Governance, compliance and data room (Step 10) |

**X-factor:** to be found in Steps 1–2. Candidates are a founder who has sold to these dealers, and an early brand authorisation.

**M2 instruments.**
- An iSAFE or CCPS fits.
- A convertible note needs at least ₹25 L per investor.
- Angel tax is abolished.
- SISFS reportedly closed to new applications on 31 May 2026 (verify). Use AP Startup Policy 4.0 grants and seed equity, or Telangana T-Fund.

**M4.** Valuation by the comparable, scorecard and VC methods. Operator comparables trade at 2–3× revenue (HomeServe, Domestic & General, Frontdoor). Urban Company, at 12.9× net revenue, is a marketplace outlier. Worked out in Step 9.

---

## 7. Decisions for you (Gate 1)

1. **Approve the recommended shape (§5)?** That means four appliances with AC as the anchor, authorised or sub-contracted installation, businesses and customers paying, the retailer as the source with no fee, and one cluster through one summer. You can say yes, tweak it, or say no.
2. **Pilot cluster:** **Warangal–Karimnagar or Vijayawada–Guntur.**
   - Warangal–Karimnagar has fewer chain stores, so likely more independents.
   - Vijayawada–Guntur has denser retail, but Bajaj Electronics' extended-warranty counters are there.
3. **Accept that the story is a 15–20% margin density business**, with the parts, refurbishment and EPR layers as upside. The alternative is to look for a higher-margin angle before we go on.

Once you approve, the next document is **Step 1: Vision and narrative**. I'll write it alone and wait for your approval before Step 2.
