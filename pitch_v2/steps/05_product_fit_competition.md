# Step 5: Product, fit and competition

**Phase B: The opportunity and the proof. Status: DRAFT for approval (20 Nov 2026).**

> **Update after Steps 7b–8 (20 Nov 2026, final).** Cluster EBITDA at maturity is now **14–16%** (Step 7b), not 10–12%. Breakeven is **22 shops at maturity** and 35 on pilot economics.

> **Update after Step 7b (approved 20 Nov 2026).** **New job flow: Keepwell Protect.**
> 1. *Sale:* the shop adds the 2-year repair plan to the bill, and the WhatsApp agent creates the plan record against the appliance's serial.
> 2. *Coverage:* the plan starts when the brand warranty ends.
> 3. *Claim:* the customer messages Keepwell, the AI triages the claim against the plan terms, and a partner or Keepwell technician repairs it at no charge.
>
> Guardrails: the AI does not decide claim rejections; a human does. Protect is a repairs-only service contract with expected claims ring-fenced. In partner clusters, Keepwell still owns the shop, the customer, the payment and the record. The north star is unchanged. See `07b_model_redesign.md`.

> **Illustrative case** for the IIIT Hyderabad ESFS course pitch.
> - Competitor facts are real and sourced **[R]**.
> - Product build status is **[Story]**, consistent with Step 2.
> - Unit numbers come from `ue_v2.py` **[Model]**.

**Builds on:** Steps 0–4 (approved). **Feeds:** Step 6 (pilot metrics), Step 11 (Product row), Step 12 (solution, demo and competition slides).

> ### Read this first (flags for approval)
> *Checked by an independent reviewer against Steps 0–4, the model and the research. Fixes applied.*
> 1. **New: what the product is.** Keepwell sells **one service** (authorised install, guaranteed repair, AMC) to three payers: households, brands and service centres, and plan sellers. The shop, the technician and the household each see a WhatsApp-first view. There are no apps to download (§5.3).
> 2. **New [Story]: what is built today.**
>    - Live in the pilot: WhatsApp and voice intake (Telugu, Hindi, English), job cards, dispatch, the photo and serial checklist, the appliance record with a QR sticker, the shop's weekly summary, technician payouts.
>    - AMC scheduling and renewal reminders went live in the Jul–Oct 2026 off-season run.
   - Next 6–12 months: parts prediction and the verification export for brands and plan sellers. The lead engine comes later (§5.4).
> 3. **New: one north-star metric.** *Verified jobs closed on the first visit, per cluster per month.* Guardrails: installed within 24 h, callbacks under 8%, zero safety incidents, contribution per shop of ₹4k or more. The guardrail thresholds are assumptions; Step 6 sets the pilot targets (§5.5).
> 4. **New: AI guardrails, stated as product rules.** AI never sets a price (the rate card does), never overrides a gas or electrical safety stop, and never approves a refund or warranty claim. A human decides those (§5.3).
> 5. **Competition, said plainly:**
>    - Urban Company serves households in Vijayawada and Guntur.
>    - Onsitego, Zopper and OneAssist sell plans at chain counters.
>    - 247around and SERVIZ do brand-paid jobs.
>    - Jeeves and resQ serve their own retailer only.
>    - **No one is the service arm of the independent shop** [R].
>
>    The closest threat is **Onsitego**. We plan to make plan sellers customers, not rivals (§5.7).
> 6. **Porter's five forces:** the strongest forces are **substitutes** (the local mechanic, the brand's own service centre) and **supplier power** (brands control authorisation). Our answers are in §5.8.
> 7. **Hardest investor questions:**
>    - *What stops Onsitego doing this?* It sells plans at chain counters and has thin repair supply in small towns. Running repair itself is what it left in 2020. We would rather fulfil its claims than fight it. Our shop agreements are multi-year and designed to be exclusive in each shop's catchment [Story].
>    - *Is the AI real or a slide?* It is live in the pilot [Story] at under ₹5 a job [R]. Its value is a lean team (one manager plus one dispatcher for 30 shops) and the record, not magic diagnosis.
>    - *Why won't brands squeeze you?* Brands need installs done in towns they can't staff. Service-centre sub-contracts and direct talks with brands give us two routes. With no authorisation at all, a four-appliance cluster needs **about 50 shops** to break even, against 30 with authorisation. So authorisation is a go/no-go gate in the pilot [Model].

---

## 5.1 How this step is built
- **What we sell, and to whom:** the per-job economics from 00 and the market from Step 4.
- **What is built:** the [Story] timeline from Step 2.
- **Competition:** the research in `competitors_funding/` and the archived competitor files [R].
- **Tough questions answered:** I7, I8, S3, T1–T7.

## 5.2 The three fits
| Fit | The test | Where we stand |
|---|---|---|
| **Problem–solution** | Does the solution remove the pain for each side? | **Shop:** keeps the customer, earns commission, sheds complaints and liability. **Household:** fast install, fixed price, a 90-day guarantee, a record. **Technician:** steady jobs, parts, quick pay. **Brand or service centre:** installs done in towns it can't staff. **Plan seller:** small-town claims fulfilled |
| **Product–market** | Will the payers pay, repeatedly? | Households already pay for AC service and AMCs (₹550 service; ₹1,099–1,299 AMC [R]). Brands already pay installers: in one SERVIZ example, the brand pays ₹1,000 and the service centre keeps ₹700 [R, single proxy]. What brands pay us is still unknown and is the first question in Step 6. Plan sellers need small-town fulfilment [R]. The Step 6 pilot measures repeat use and routing |
| **Founder–market** | Can this team win shops, authorisation and supply? | CEO: 600+ dealers. COO: 200+ service-centre owners. CTO: plan sellers and the AI layer [Story, Step 2] |

## 5.3 How it works: one job, end to end

**A. An installation (brand-authorised)**
1. **Sale.** The shop sells an AC. The shop assistant taps *Book install* on WhatsApp, or scans the shop's QR code.
2. **Intake (AI).** The bill photo and a voice note become a job card. The AI reads the model, serial number, address, language and preferred slot.
3. **Authorisation check.** If the brand is covered by our service-centre sub-contract, Keepwell does the job and registers the installation for warranty activation. If not, the job is routed to the brand's own service centre, the shop still gets a status update, and we still record the appliance.
4. **Dispatch (AI and a human).** The nearest certified partner technician is assigned. The household gets the technician's photo and a time slot.
5. **Visit.** The technician follows the install checklist, with photos of the mount, insulation, drain and earthing. The **serial number is captured** and any materials used are logged. The household closes the job with an OTP.
6. **Record.** The appliance gets a service book, and a QR sticker goes on the unit. The shop's weekly summary shows the job.
7. **Later.** A check-up reminder goes out through the shop before the warranty ends. After warranty, the household is offered an AMC. When something breaks, the household scans the QR code or calls the shop.

**B. An out-of-warranty repair**
1. The household sends a WhatsApp or voice message, or calls the shop.
2. **The AI predicts the likely fault and part** from the appliance's history and the description, so the technician carries the part. **The price comes from the rate card, never from the AI.**
3. On the visit: diagnose, quote, fix, photograph, close with an OTP.
4. The job carries a 90-day guarantee.
5. Payment goes by UPI to Keepwell, and the technician is paid within 48 hours [Assumption].

**C. An AMC.** The shop sells the plan at the counter or at the install. Visits are scheduled into the AC off-season (Oct–Feb) to fill technicians' days. Renewal reminders go out in month 11.

**What each side sees:** no app downloads. WhatsApp for the household and the shop, a light web dashboard for the shop owner, and a simple technician app or WhatsApp flow.

**The AI service layer (the CTO's thread)**

| Component | What it does | Built? [Story] |
|---|---|---|
| Intake | Voice, WhatsApp text and photos (Telugu, Hindi, English) in; structured job card out | Live |
| Dispatch | Matches skill, brand authorisation, location and load | Live (with a human dispatcher) |
| Quality check | Checks that photos are complete and the serial is readable; flags anomalies | Live |
| Appliance record and QR | One record per unit: install date, jobs, parts, photos | Live |
| Shop summary and commissions | Weekly WhatsApp summary; dashboard | Live |
| Technician payouts | Per job, within 48 hours | Live |
| Part prediction | Likely part by model, age and symptom | Next (about 6 months; needs a few thousand verified jobs [Assumption]) |
| Verification export | Audit-grade install and claim records for brands and plan sellers | Next (12 months) |
| AMC renewal reminders | Month-11 renewal reminders through the shop | Live (Jul–Oct 2026) |
| Lead engine | Upgrade leads for the shop (with consent), part of Phase 3 | Later (year 3+) |

**Cost:** under ₹5 per job [R: WhatsApp utility message about ₹0.12, Gemini audio ₹0.05–0.17 a minute].

**Guardrails:**
- The AI never sets prices.
- The AI never overrides safety stops.
- The AI never decides refunds or warranty claims.
- Household data is used only with consent (DPDP Act, Step 10).

## 5.4 What is built and what comes next [Story, consistent with Step 2]
| When | Built |
|---|---|
| Sep–Nov 2025 | First version of the service layer: intake, job cards, the photo and serial checklist, the record and QR. Technician certification curriculum written (Step 2) |
| Mar–Jun 2026 | Used live in the summer pilot across AC, washing machine and fridge installs (covered by the Nov 2025 sub-contracts). Dispatch, the shop summary and technician payouts added |
| Jul–Oct 2026 | AMC scheduling and renewal reminders for the off-season. Water-purifier and out-of-warranty repair volume grows |
| **Next (funded by the round)** | Part prediction, the verification export, hardening (audit trail, consent, uptime). The lead engine comes later |

## 5.5 North star and guardrails
- **North star:** **verified jobs closed on the first visit, per cluster per month.** It captures volume (density), quality (first visit) and the record (verified).
- **Guardrails** (assumed thresholds; Step 6 sets the pilot targets):
  - installs completed within 24 h: 85% or more
  - callbacks within 90 days: under 8%
  - safety incidents: zero
  - contribution per shop: ₹4k or more by month 4
  - technician jobs per day: 2.8 or more
  - shop routing: 50% of installs or more

## 5.6 Why it is hard to copy (the moat, made concrete)
| Moat | What it is | How it shows in the numbers |
|---|---|---|
| **Exclusive service-arm agreements with shops** (the HomeServe pattern [R]) | Multi-year, with a revenue share and the shop's name on the guarantee. Designed to be exclusive in the shop's catchment [Story] | We expect lower shop churn than a marketplace [Assumption]. Competitors can't route that shop's installs |
| **Cluster density** | 50–70 shops per cluster, with technicians close by | Cluster EBITDA rises from 0% at 30 shops to 10–12% at maturity [Model] |
| **Authorisation access** | Service-centre sub-contracts, then direct authorisation by brands | 35% of AC installs authorised (BASE), 45% with the COO's contacts [Story edge]. At 45%, breakeven falls from 30 to about 27 shops [Model] |
| **The appliance record** | Consent-based. Grows with every visit | The planned data layers (Phase 3) earn 70–90% gross margin [R; Plan] |

**The AI is the cost engine, not the moat.** It can be copied. The four items above can't be copied quickly.

## 5.7 Competition
| Player | What they do | Who pays them | Tier 2/3 presence in our belt | Why they don't cover our position | Threat |
|---|---|---|---|---|---|
| **Urban Company** | App for household repair, install and service | Households (Urban Company keeps about 36% of total job value, Q1 FY27 [R]) | **Live in Vijayawada (AC from ₹799) and Guntur (from ₹699)** [R] | Serves households, not shops. Does no brand-authorised installs for shops. Its top 10 cities are over 90% of its total job value [R] | Medium (households); low (shops) |
| **Onsitego (+Qdigi)** | Extended warranties and plans sold at chain counters. Repairs routed to about 400–450 service centres (2021, company claim) plus Qdigi [R] | Consumers, through retailers | At chains: Vijay Sales, Viveks, Value Plus, Great Eastern, Croma, Amazon [R] | Sells plans, doesn't serve independent shops, and has thin small-town repair supply. Left consumer repair because acquiring customers cost too much [R] | **High: closest.** Plan: make it a fulfilment customer |
| **Zopper / OneAssist** | Plans at counters | Consumers, through retailers | Chain counters [R] | Same as Onsitego | Medium; possible customer |
| **247around (Servify) / SERVIZ** | Brand-paid installs and repairs through partner centres | Brands | National claims [R] | Paid by brands, not tied to shops. 247around made about ₹14.5 Cr in FY25 at a loss [R] | Medium; a possible source of filler jobs |
| **Jeeves (Flipkart) / resQ (Reliance)** | Captive after-sales for their own retailer | Their retailer and consumers | Their own buyers only [R] | Captive: won't serve independent shops | Low |
| **Brand service centres** | In-warranty installs and repairs for their brand | Brands | Present everywhere (LG has about 1,006 centres [R, unverified]) | Single-brand, in-warranty, slow in peaks. **They are partners through sub-contracts** | Partner and competitor |
| **Local mechanics** | Cheap, fast, word of mouth | Households | Everywhere; 44% of AC service [R] | No guarantee, no record, no authorisation, no GST. **We recruit the good ones as partners** | Biggest by volume |

**Positioning line:** *"Everyone else serves one slice: the household app, the plan seller, the brand, or the captive retailer. Keepwell is the only service arm for the independent shop, with authorisation, a guarantee and a record."*

## 5.8 Porter's five forces (after-sale service for independent appliance shops, Tier 2/3)
**Two forces are strong.**
- **Substitutes:** local mechanics, brand service centres, Urban Company. *Our answer:* recruit good mechanics as partners, make the brand centres our sub-contractors, and serve the shop (which Urban Company doesn't). Our prices include GST but add the guarantee, the record and the shop's name.
- **Supplier power:** brands control authorisation, and technicians can leave. *Our answer:* two routes to authorisation, and partner technicians who get jobs, parts and an off-season floor. We measure leakage.

**The other three are medium:**
- **Buyers:** shops are fragmented and pay nothing.
- **New entrants:** the technology barrier is low, but density, exclusivity and authorisation take time.
- **Rivalry:** we serve a different customer from the incumbents.

**Verdict:** the business is attractive only with **density + authorisation + shop exclusivity**. The Step 6 pilot tests all three.

## 5.9 Weak points, said before an investor does
- **Authorisation depends on others.** The sub-contracts are non-exclusive [Story]. With zero authorisation, breakeven rises to about 50 shops [Model].
- **Urban Company is already in our belt** for households. Our edge holds only if shops route to us.
- **Part prediction needs data** (a few thousand verified jobs [Assumption]) before it is useful. Until then, it is a checklist plus the technician's experience.
- **Leakage**: partners keep their own customers. Measured in the pilot.

---

## Decisions to approve (Step 5)
1. **The product:** one service, three payers, WhatsApp-first, no app downloads. The job flows A–C.
2. **The AI service layer:** what's live versus next [Story], under ₹5 a job, and the four guardrails. Renewal reminders are live; the lead engine comes later.
3. **North star:** verified jobs closed on the first visit per cluster per month, plus the guardrails.
4. **The moat:** exclusive shop agreements, density, authorisation access, the record. The AI is the cost engine.
5. **Competition and positioning line.** Onsitego is the closest threat, and our plan is to make it a customer.
6. **Porter's verdict:** attractive only with density + authorisation + shop exclusivity.

On approval, the next step is Step 6: traction and validation plan (the pilot story and results).

