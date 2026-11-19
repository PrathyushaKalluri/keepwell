# Step 0: Unit economics, rebuilt from evidence

> **Superseded in part (19 Nov 2026).** Design E (desk fee, filler jobs) was replaced by Steps 7 and 7b. The AC install contribution is ₹469 (pilot mix); ₹730 applied only to the full designed fee. LTV, CAC and payback for the final model are in Step 7b.


**Engine:** `pitch_v2/ue_v2.py`. Run `python3 ue_v2.py --json --company` to reproduce every table here.

**Inputs:**
- Every input is a (LOW, BASE, HIGH) triple with a tag and a source key.
- **RA:** `research/retail_install/parameters.csv`
- **RB:** `research/supply_layers/parameters.csv`
- **RC:** `research/competitors_funding/`
- **AR:** `pitch/archive/market_intel/raw/demand/parameters.csv`

**How to read LOW and HIGH:** they are corner cases, with *every* input set pessimistic or optimistic together. The realistic range is narrower. The sensitivity in §5 shows which inputs actually matter.

## 1. First, the founders' reference model

`unit_economics.py` reproduces the founders' document to check its logic.
- **Per job:** install ₹112, repair ₹202, AMC ₹500. The document says ₹450 for AMC, but its own listed costs leave ₹500.
- **Per retailer:** revenue ₹41.3k and contribution ₹8.1k a month.
- **Cluster:** breakeven at 21 retailers.

**Its logic is sound. Its inputs are not.** Evidence breaks five of them:

| Reference input | Evidence | Effect |
|---|---|---|
| Installs: ₹650 blended, customer-paid, any installer | **A third-party AC installation voids the warranty.** This is in the terms of Samsung, Daikin, Carrier, IFB, Godrej and Panasonic. Flipkart and Reliance accept returns only after an authorised install. The customer pays the brand's technician ₹1,199–1,500 plus GST, with materials extra (RA) | An unauthorised provider can't take in-warranty AC installs at all. If we are brand-authorised, an AC install is worth about ₹2,400 net with materials, not ₹650 |
| Technician does 76 jobs a month (3.8 a day at 80% use) | Urban Company partners average about 43 orders a month, roughly 1.7 a day (RB). AC demand runs at a 1.8× index in Mar–Jun and 0.6× in Oct–Feb (RB) | BASE is about 49 jobs a month. The cluster must hire for the peak |
| Technician paid about ₹400 a job → ₹30k a month | A Tier 2/3 mechanic earns ₹10–25k today (BASE ₹20k). UC partners net about ₹28k (RB) | At about 49 jobs a month, ₹30k needs about ₹610 a job |
| AMC ₹1,800 | UC sells a 2-service AC plan for ₹1,098–1,298 (RB) | BASE ₹1,299 including GST |
| Prices net of tax | **GST is 18% on the whole bill for us as principal.** A local mechanic with under ₹20 L turnover charges none (RB) | Repair and AMC prices must include GST to compete. That takes about ₹150 out of a ₹1,000 job |
| 100 units a month per retailer; 23,400 serviceable retailers | The typical independent shop sells 30 / 60 / 120 units. Serviceable shops number 5k / 9k / 18k (RA, derived) | BASE is 60 units a month, and the TAM roughly halves |

## 2. One job (net of GST)

| Job (BASE) | Customer pays | Net to us | Contribution | Margin | LOW → HIGH contribution |
|---|---|---|---|---|---|
| Out-of-warranty repair or service | ₹1,000 incl. GST | ₹847 | **₹164** | 19% | ₹32 → ₹319 |
| AC installation, brand-authorised (fee plus materials) | ₹900 fee (+GST) + ₹1,500 materials | ₹2,400 | **₹730** | 30% | ₹149 → ₹1,599 |
| Other installation (geyser, washing machine, TV) | ₹300 | ₹300 | ₹77 | 26% | −₹9 → ₹164 |
| AMC, 2 AC services | ₹1,299 incl. GST | ₹1,101 | ₹203 | 18% | −₹187 → ₹567 |

**Out-of-warranty repair BASE (₹847 net):**
- Parts: 35% of the bill at a 20% margin.
- Technician: 60% of the labour.
- Retailer: 8%.
- Rework: 4%.
- Gig levy: 1%.
- Technology: ₹2.5 a job (WhatsApp utility message about ₹0.12, Gemini audio about ₹0.08 a minute).
- Insurance: ₹2.5 a job (RB).

**The single biggest unknown here is what a brand pays an installer.** The only proxy is SERVIZ: the brand pays ₹1,000, the service centre gets ₹700 (RC). This is the first interview question.

## 3. One retailer and one cluster: five designs (BASE)

| Design | What it is | Retailer revenue a month | Contribution per retailer (after top-up) | Cluster at 30 retailers: EBITDA a month | Breakeven retailers | LTV:CAC (3 yr) |
|---|---|---|---|---|---|---|
| **Founders' design, priced on evidence** | Unauthorised. Only non-AC installs, repair and AMC | ₹15.1k | about ₹0.9k | **−₹1.39 L** | 188 (not viable) | 1.1 |
| **A. Authorised partner** | Brand-authorised AC installs + repair + AMC. Salaried technicians with a ₹22k floor | ₹30.2k | about ₹4.6k | −₹0.26 L | 36 | 6.0 |
| **C. A + after-sales desk fee** | Retailer pays ₹2,500 a month for the desk (60% take it up) | ₹31.7k | about ₹6.0k | +₹0.15 L | 28 | 7.7 |
| **D. Asset-light routing** | Route retailers' jobs to existing service centres and agencies for a 20% fee | ₹6.8k | ₹1.8k | −₹0.41 L | 53 | 2.3 |
| **E. Hybrid (recommended to test)** | C + certified partner technicians paid per job (no salary floor, +5 points of payout) + brand- or e-commerce-paid "filler" jobs in the off-season | ₹31.7k | **₹9.1k** | **+₹1.08 L** | **19** | **11.7** |

**What drives these results:**
- **Technician economics decide the business.** In A and C, a cluster needs 18 technicians to cover the Mar–Jun peak. The rest of the year they earn about ₹17k from jobs, so a ₹22k floor costs about ₹88k a month. That is most of the gap between A and E.
- **E removes the gap** by paying certified partners per job. They keep their own customers, so they aren't idle on our clock. We fill the off-season with brand-paid jobs.
- **The cost of E** is that technicians average only about ₹18k a month from us. That raises the risk of them taking customers off-platform. We counter it with the 90-day guarantee, payment through us, the QR code on the unit and parts access.

## 4. Company: 24 months, three clusters (E_HYBRID)

Clusters open in months 1, 7 and 13. HQ costs ₹4–7 L a month.

| | LOW | **BASE** | HIGH |
|---|---|---|---|
| Year 1 revenue | ₹6 L | **₹40 L** | ₹2.6 Cr |
| Year 2 revenue | ₹30 L | **₹1.98 Cr** | ₹13.2 Cr |
| Year 1 EBITDA | −₹1.03 Cr | **−₹0.82 Cr** | +₹0.14 Cr |
| Year 2 EBITDA | −₹1.67 Cr | **−₹0.94 Cr** | +₹3.8 Cr |
| **Peak funding need** | ₹2.87 Cr | **₹1.94 Cr** | ₹0.28 Cr |
| Run-rate at month 24 | ₹0.43 Cr | **₹2.8 Cr** | ₹18.9 Cr |

**The founders' reference (Y2 revenue ₹4.3 Cr) was about 2× too optimistic**, because it assumed 100 units a retailer and 76 jobs a technician.

**What it means for funding** (the funding benchmarks are in RC):
- India's Series A bar is now about ₹16–20 Cr+ run-rate.
- At about ₹3.8 L gross revenue a year per retailer, that bar needs about 420–525 retailers, or 14–18 clusters.
- **So the first raise funds proof, not scale:** about ₹2–2.5 Cr to prove 3 clusters. Then a ₹8–15 Cr seed round to reach about 15 clusters, then Series A.
- That is a 3-round path, and the ask must be framed that way.

## 5. What decides viability (BASE E; each input swung to its LOW or HIGH value alone)

| Rank | Input | Contribution per retailer at LOW → HIGH (BASE ₹9.1k) | What settles it |
|---|---|---|---|
| 1 | Units a retailer sells a month (30 / 60 / 120) | ₹6.7k → ₹14.0k | Shop interviews; distributor ledgers |
| 2 | Share of AC brands that authorise us (30 / 50 / 65%) | ₹7.3k → ₹10.5k | Talks with 3–4 brand regional service heads |
| 3 | AC installation fee we receive (₹700 / 900 / 1,199) | ₹8.0k → ₹10.8k | Brand payout sheets; SERVIZ and 247around |
| 4 | Materials sold per install (₹800 / 1,500 / 2,500) | ₹8.0k → ₹10.7k | Install logs |
| 5 | Retailer routes installs to us (50 / 70 / 85%) | ₹7.8k → ₹10.1k | Pilot |
| 6 | Installed base per retailer; repair capture | ±₹1.0–1.2k | Retailer sales history; pilot |

**These become the pilot's kill criteria, which are set in Step 6:**
- under 40 units a month at pilot retailers
- no brand authorisation by month 3
- install routing under 40%
- contribution per retailer under ₹4k by month 4

## 6. The layers (parts, refurbishment, EPR): do they lift margin above 25%?

**Not on current evidence (RB):**
- **AMC** runs at about 10–18%.
- **Parts margin** is UNKNOWN; the proxy is 15–40%.
- **Refurbishment** benchmarks at about 15.7% gross (Cashify FY25) and needs stock capital.
- **EPR certificates** go to recyclers, not collectors. The ₹22/kg floor is being contested in the Delhi High Court.

**A margin above 25% needs three things at once:** a parts margin of at least 20%, AMC at ₹1,500 or more with visits at ₹300 or less, and 3+ jobs a technician a day. **Pitch it as a 15–25% contribution operator** (operator multiples are 2–3× revenue, RC). The layers are upside, not the base case.
