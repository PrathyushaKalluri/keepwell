# Keepwell seed story (reconciled): review verdict first, then the story

Source: the 19 step files in `ESFS/pitch_v2/steps/` and the model code beside them (`ue_v2.py`, `unit_economics.py`, `model/plan_v3.py`). Four independent review agents each read a slice of the files, recomputed the arithmetic and listed contradictions. Their raw reports are in the session scratchpad. The skeleton (sections only) follows `KEEPWELL_FULL_STORY.md`; none of its content is used.

Tags used throughout: **[Real]** measured by the team. **[Research]** third-party source, cited in the step files, not re-checked here. **[Model]** output of the team's model. **[Story]** invented or illustrative for the ESFS course case (the step files say so themselves). **[DECIDE]** a founder decision.

---

# PART 0. REVIEW VERDICT (read this first)

## Would the investor pitch work from this story?

**As written, no. As a plan with honest labels and one reconciled number set, yes.**

| Question | Verdict |
|---|---|
| Is the logic coherent? | **Yes.** Insight (trust sits at the shop, skill with the technician, nobody keeps the record), a one-line wedge (the after-sale service arm of the independent shop), per-job economics, and a "weak points" section in every step. |
| Is the arithmetic right? | **Yes.** The agents recomputed the per-job, per-plan, per-cluster, cap-table, dilution and return numbers. They match the stated inputs (7 of 7 model checks, all deal checks except 3 small rounding items). |
| Is the evidence real? | **No.** Founder histories, the pilot (34 shops, ~2,400 jobs, ₹25 L), brand authorisations, interview counts and money raised are all [Story]. The pilot results were "generated from the same model the pitch uses", so they cannot validate that model. The only measured evidence is third-party research plus a household survey of 19 people (12 qualified) in Hyderabad and Visakhapatnam, collected after the pilot. |
| Do the files agree with each other? | **No.** See the contradiction list below. |
| Would a seed investor sign the deal? | **Probably not as structured.** ₹10 Cr pre-money is about 27x the annualised pilot revenue (~₹37 L, unaudited), the validation file itself called ₹10 Cr "too rich", cash lasts about 4.4 months, and the milestones do not line up with the calendar. |

## What gels

1. Problem to solution to wedge is one clean line: *the shop sells, Keepwell stands behind it, the technician is paid fast, the record stays with the appliance.*
2. Pain evidence for households is real third-party data (installation waits, warranty voiding, 80-91% out of warranty, 44% of AC service to local technicians).
3. The red misses in the pilot are disclosed, not hidden.
4. "AI is the cost engine, not the moat" is a credible, sober stance.

## What does not gel (the contradictions to fix)

| # | Contradiction | Where | Fix |
|---|---|---|---|
| 1 | **Breakeven shops per cluster** is stated as 19, 22, 27, 30, 35, 36 | 00, 00c, 01, 05, 06, 07, 07b | Use **~35 at full ramp** (06:31, 06:53, 06:139; the pilot had 34 shops at only ~60% ramp in October and was not yet profitable) and say **22** is the mature-cluster figure with Protect and the new commission mix. Show both. |
| 2 | **Units per shop per month**: 60 / 74 / 80 | 00, 04, 06, 07b, 00b | Use **74** (pilot-measured, hand-picked shops) for pilot claims and **60** (BASE) for planning. State why they differ. |
| 3 | **Mature cluster EBITDA**: 5.2% / 10-12% / 14-16% | 07, 00c, 07b | Use **16.3% own-run, 14.1% partner-run** (07b, final), and say the jump came from Protect, the commission shift and parts margin, not new evidence. |
| 4 | **TAM**: ₹1,550 Cr in validation, ₹4,000 Cr later, no re-derivation | 00_validation_report vs 04, 10, 11, 12 | Keep ₹4,000 Cr (₹3,500-4,800) only with the shop-count sensitivity (9k vs 45k shops). Lead the deck with the **beachhead (₹360 Cr)** and the **year-7 plan (₹130.5 Cr)**, not TAM. |
| 5 | **Year 1 revenue**: ₹40 L (00) vs ₹2.4 Cr (07b). **Year 7**: ₹115.5 / 81.5 / 130.5 Cr | 00, 00b, 07, 07b | Use **07b only**. Archive or banner the stale numbers. |
| 6 | **Ask and valuation**: ₹2.5 Cr at ₹10 Cr pre vs "too rich" and a suggested ₹75 L-₹1 Cr at ~₹6 Cr cap | 08, 09, 12 vs 00_validation_report | See Part 14. Tranche the round and re-base the valuation. |
| 7 | **Pilot status**: "future, Mar-Jun 2027" vs "already ran Mar-Oct 2026 and worked" | 00_validation_report vs 12 | Label every pilot number [Story]/[Model] on every slide, or run a real pilot. |
| 8 | **Installation payer**: brand pays ₹800 / customer pays brand rate and Keepwell nets ₹800 / brand pays ₹1,000 | 03, 05, 06 | Pick one (the signed sub-contract terms) and flag the others as unverified. |
| 9 | **Technician pay does not close**: "15 jobs ≈ ₹15k a month" but per-job pay is ₹330-500, so 15 jobs ≈ ₹5-7.5k | 06:49 vs 03:68-71 | See Part 9. Say technicians are *supplemented*, not replaced, and show real pay records. |
| 10 | **Protect attach**: 3.5% (08), 5% (07b stress), 8% (07b BASE), 6% (pilot counter test) | 07b, 08, 06 | Lead with the **5% stress** case. No Indian benchmark exists for 8%. |
| 11 | **Runway**: "funds 18 months" vs tables saying month 21; model starts Jan 2027, close is Feb-Mar 2027 | 08 | Re-base the calendar from the close date. |
| 12 | **Exit multiples**: 10x EBITDA (00b) vs 25x and 15x (07b) vs 2.5-3x revenue; seed priced at 27-33x revenue, later rounds at 5-7x, exit at 2.5x | 00b, 07b, 09 | Value the exit on EBITDA as well as revenue; recompute returns (Part 14). |
| 13 | **Competition**: slide says "nobody serves the independent shop", Tough Questions says Onsitego is "the closest threat" | 12 vs 00_tough_questions | Replace the absolute claim with "nobody *owns* it; Onsitego is the closest, and may be a partner". |
| 14 | **Housekeeping**: "21 issues, all fixed" (the table lists 20); 07b "approved 20 Nov 2026" is after today (19 Nov); stale 00/00b/07 tables still in the folder | 12, 07b | Remove the claim, fix the date, archive stale files. |

## The changes to make, in priority order

**Blockers (fix before any investor sees it):**
1. **Relabel the evidence.** Every pilot number is a plan or a modelled result until it comes from job logs and payment records. Replace [Story] with: 10-20 signed shop LOIs (with exclusivity terms), one real brand or service-centre authorisation letter with its payout, 3-5 real technician pay records, and a ledger-backed revenue figure.
2. **One number set.** Use the canon in Appendix B everywhere. Banner or delete stale numbers in 00, 00b, 07.
3. **Re-base the ask and valuation.** Tranche the ₹2.5 Cr, base the valuation on the evidence, fix the calendar, fix the milestones (Part 13-14).
4. **Settle Protect before the pitch.** Get the legal opinion (service contract, not insurance). Make it a condition precedent to the second tranche. Run a real counter test. Do not net Protect cash against the operating need.
5. **Fix the technician maths** and show real pay data.

**Strong recommendations:**
6. Name the category honestly: a **principal-model services operator with a software layer**, not an "operating system for agencies". An OS/SaaS investor and a services investor price this very differently.
7. Replace the HomeServe/Asurion analogy with comparables an investor accepts.
8. Say plainly that the core moat (exclusive multi-year shop agreements) has no signed example, that the brand sub-contracts are non-exclusive 12-month terms that lapse around now, and that partner operators running clusters for 10% is untested.
9. Fix the team slide: invented credentials for named real people, and "letters of intent in Step 6" that do not exist. Show what you can document.
10. Re-cut TAM bottom-up from pilot capture (shops x units x capture), with one headline number.

---

# PART I. THE STORY

# Keepwell: the whole story, told from the outside

## How to read this document

Everything here is built from the `pitch_v2` step files and reconciled to the numbers in Appendix B. The step files say they describe an **illustrative case** for the IIIT-H ESFS course, so most traction is [Story]. Read each tag literally. Where this document differs from a step file, the reason is in Part 0 and Part 16.

## Contents

- Prologue: A shop, a four-day wait, a legal notice
- The ending first: where Keepwell stands today
- Part 1. A problem nobody has measured end to end
- Part 2. Three people who had each seen one side of it
- Part 3. Listening before building
- Part 4. The idea that is bigger than the product
- Part 5. Building the product
- Part 6. The first money, and why it was structured that way
- Part 7. The test that went against us
- Part 8. Eight months in the field
- Part 9. Does the shop, the household and the technician actually win?
- Part 10. Why nobody can catch up (and why they might)
- Part 11. The engine: how one shop becomes a cluster becomes a business
- Part 12. How big this can get
- Part 13. What we need now, and why exactly that much
- Part 14. The deal
- Part 15. Trust, law and whose data it is
- Part 16. How we tried to break our own story
- Part 17. What could go wrong, and what we do then
- Part 18. What is real and what is illustrative
- Epilogue: What the money becomes
- Appendix A. Proof index
- Appendix B. Every number on one page

---

## Prologue: A shop, a four-day wait, a legal notice

A multi-brand appliance dealer in a Guntur-type town sells a split AC on Monday for about ₹38,000. The brand's installer is booked for Thursday. The customer's relative offers to fit it on Tuesday. The AC runs for three weeks, then the compressor fails. The brand says the installation was unauthorised and the warranty is void. The customer does not call the brand. The customer calls the shop. Then a consumer commission sends the shop a notice.

That last step is not invented: consumer commissions have held sellers jointly liable in appliance cases (Chennai ₹35,000, Chandigarh, Hyderabad ₹60,000) **[Research]**. The Guntur dealer shown a consumer-court notice is a **[Story]** composite.

The shop earns 2-3% net margin **[Research]**. It earned nothing after the sale, and it was blamed for what happened after. Nobody in the chain (brand, installer, customer, mechanic) kept a record of what was installed, by whom, or when.

## The ending first: where Keepwell stands today

- **Product:** the after-sale service arm of an independent appliance shop. The shop sells; Keepwell installs, repairs, sells service plans, pays the technician in 48 hours, and keeps the appliance record. **[Model/Story]**
- **Pilot (Mar-Oct 2026, Vijayawada-Guntur belt):** 34 shops, about 2,400 jobs, ~₹25 L revenue, about 20% contribution before the off-season floor and shop acquisition cost. The pilot lost about ₹12.7 L net after cluster team cost. **[Story, model-generated]**
- **Misses:** five of the scorecard rows were red (Part 7).
- **Cash:** ₹18 L plus a ₹5 L grant instalment against a burn of ~₹5-6 L a month, so about 4.4 months (to early April 2027). **[Story]**
- **Raising:** ₹2.5 Cr, in two tranches, to prove four things (Part 13).
- **The honest summary:** the logic is sound and the per-job arithmetic holds. The proof is modelled. The next 18 months replace the model with data.

---

## Part 1. A problem nobody has measured end to end

### 1.1 The size of the problem

| Fact | Number | Tag |
|---|---|---|
| Out-of-warranty share of installed units | 80-91% | Research |
| AC service done by local technicians (brand 24%, dealer 13%, platform 13%) | 44% (n=13,487) | Research (LocalCircles) |
| Brand installation wait | LG 24-72 h; Flipkart 2-5 days; documented no-shows | Research |
| Shop net margin | 2-3% | Research |
| Households keeping no record of their appliance | 7 of 12 qualified | Real (small sample) |
| After-sale spend through independent shops (Tier 2/3, India) | about ₹4,000 Cr a year (₹3,500-4,800 Cr) | Model (see Part 12) |

### 1.2 What goes wrong, on both sides

**The household:**
- Installation waits for days. A non-authorised install voids the warranty at Samsung, Daikin, Carrier, IFB, Godrej and Panasonic **[Research]**.
- After warranty, a local mechanic with no fixed price, no guarantee and no record.
- The same fault returns: "a repaired AC fixed only 60-70%", the same washing-machine error code a year later **[Real, n=1 each]**.
- The invoice and warranty card are lost; the RO filter date is on a handwritten sticker.

**The shop:**
- Trust sits at the counter, but the role ends at the counter. It carries blame and legal liability for work it does not control, and earns nothing after the sale.
- In discovery, 51 of 64 shops said install delays are blamed on them; 9 had a complaint or legal notice; none earn anything after the sale **[Story]**.

**The technician:**
- Uneven work, no parts on credit, take-home ₹12-22k a month, no certificate and no customer base of their own **[Story; wage range consistent with Research]**.

**The brand and the plan seller:**
- Brands miss small-town installation targets and do not want to staff 3,000 small towns. Warranty-plan sellers have thin small-town repair supply **[Story]**.

### 1.3 We have watched the problem happen

- Real household research (Hyderabad and Visakhapatnam, Sept 2026): 19 households (12 qualified) and 6 interviews, with photos of stickers, diaries and handwritten filter dates **[Real, small]**.
- **Caution for the deck:** this research was done *after* the pilot, and in cities outside the pilot belt. Present it as "what we heard", not as the discovery that led to the product.

### 1.4 Why this has not been solved

| Player | Why it does not cover the independent shop |
|---|---|
| Brands | Their service network is thin in small towns and they do not want out-of-warranty work. |
| Urban Company | Sells to the household in cities and takes about 36% of the job **[Research]**. Live in Vijayawada and Guntur for AC from ₹699-799, so it is already in the pilot belt. |
| Warranty-plan sellers (Onsitego-Qdigi, Zopper) | They sell plans and need repair fulfilment. Closest in channel. Possible partner or competitor. |
| Brand-paid installers (247around, SERVIZ) | Paid by the brand, not the shop. |
| Local mechanics | 44% of AC service, cheap, no guarantee, no record. The biggest competitor by volume. |

---

## Part 2. Three people who had each seen one side of it

The step files state that the founder names are real and their histories are [Story]. Treat the table below as the claim to be documented, not as evidence.

| Founder | Claimed background | Maps to | What an investor should be able to check |
|---|---|---|---|
| **Prathyusha Kalluri, CEO (38%)** | 10 years in consumer-durables distribution; regional head AP/TS at a large multi-brand distributor; region supplied 600+ independent dealers | The shop channel | Employer name (unnamed by design), two dealer references, the pilot shops she introduced |
| **Kavyanth Munagala, COO (31%)** | 9 years in after-sales; ran a water-purifier service network, then a zonal service head AP/TS (~220 authorised service centres, 3,000 technicians) | Technicians, brand authorisation, partner clusters | Brand reference, signed authorisation letter |
| **Sri Charan Peri, CTO (31%)** | 8 years of engineering; Indian-language voice/WhatsApp at a conversational-AI company (~2 M calls a month); engineering lead at a device-protection and claims platform | Product, AI, plan-seller fulfilment | Working product, cost per job |

**How the founders map to revenue:** the CEO's dealer network lowers shop acquisition cost (₹22k cold to ~₹10k warm; pilot ₹9.5k **[Story]**). The COO's service-centre network lifts brand authorisation (35% BASE to 45-50% edge; pilot achieved 41%, with one of two sub-contractors under-delivering **[Story]**). The CTO's claims background supports plan-seller fulfilment (70 jobs a month achieved against a 100 target **[Story]**).

**Honest gaps:** nobody on the team has taken a startup to an exit. Two of the three founder "edges" under-delivered in the pilot. The "letters of intent" promised for the team are not in the files. Advisors are unnamed roles, and the board is founders only. **Fix before pitching:** name two advisors, attach one real reference per founder.

---

## Part 3. Listening before building

### 3.1 What we did

| Activity | Count | Tag |
|---|---|---|
| Shop discovery interviews (Apr-Jul 2025, Vijayawada, Guntur, Warangal) | 64 shops | Story |
| Technician interviews | 41 | Story |
| Authorised service-centre owners | 6 (2 open to sub-contract) | Story |
| Brand teams | 3 | Story |
| Plan sellers | 2 (1 willing to pilot) | Story |
| Household survey and interviews (Sept 2026) | 19 (12 qualified) + 6 | Real |

### 3.2 What households told us [Real, small sample]
- Seven of twelve keep no record of their appliance.
- A repaired AC "fixed only 60-70%".
- The same washing-machine error code returned a year later.
- Service history lives in a sticker or a diary.

### 3.3 The insight
Every player starts at one end of the chain. The brand sells the product. A marketplace serves the household. The mechanic fixes the fault. Nobody *owns* the full life of the appliance in a small town, and the one party that holds the customer's trust, the shop, earns nothing after the sale. Give the shop a reliable service arm and three things follow: the customer stays, the technician gets steady work, and a record of every appliance builds up that nobody else has.

### 3.4 What shop owners told us [Story]
- 51 of 64 said install delays are blamed on them.
- 9 had received a complaint or legal notice.
- 41 of 64 said they would route their installs to a service arm.
- None earn anything after the sale.
- Technicians: 29 of 41 would join for steady extra jobs paid in 48 hours.

**Weak point to state aloud:** these counts are [Story]. Replace them with signed LOIs.

---

## Part 4. The idea that is bigger than the product

### 4.1 Every machine lives one life
Install, use, break, repair, resell, recycle. Today a different party touches each step and none of them keep the record.

### 4.2 The roadmap, and who pays at each stage

| Phase | Years | What | Who pays | Gross margin |
|---|---|---|---|---|
| **Serve** | 1-2 | Install, repair, service plans (AMC), Protect | Household; brand for authorised installs | 18-20% contribution |
| **Supply** | 2-4 | Pooled parts; trade-in field arm | Other agencies; resellers | ~10% parts, 57% trade-in |
| **Know** | 3-6 | Verified records, failure data, leads and renewals | Brands, plan sellers, retailers | 70-90% (benchmark only) |
| **Circulate** | 5-8 | Refurbished units, e-waste | Resale buyers; producers (EPR) | 12% refurb, 50% e-waste |

**Caution:** the "Know" layer has no contracted buyer and no price paid. It is a hypothesis. Keepwell Protect (a 2-year repair plan sold at the shop counter) sits in the year-7 plan (about ₹10 Cr) but not in the four-phase story, so introduce it as part of Serve.

### 4.3 Why we start with install and repair, and why AC first
- Installation is frequent, visible to the shop, and creates the appliance record.
- Out-of-warranty repair is the recurring revenue.
- AC is about 85% of the value per shop **[Model]**, but it is seasonal, so a four-appliance mix (AC, washing machine, refrigerator, water purifier) lifts revenue 17% and contribution 23% and needs 7 fewer shops to break even **[Model]**.

---

## Part 5. Building the product

### 5.1 The timeline [Story]
- Discovery: Apr-Jul 2025. Incorporation: Aug 2025 (Hyderabad and Vijayawada, DPIIT-recognised).
- AI v1 built: Sep-Nov 2025. Two service-centre sub-contracts: Nov 2025.
- Pre-seed iSAFE: Dec 2025. Plan-seller pilot letter: Jan 2026. State grant sanctioned: Feb 2026.
- Summer pilot: Mar-Jun 2026. Off-season pilot: Jul-Oct 2026. Raising: Nov 2026.

### 5.2 What the product does, step by step

**A. Authorised installation**
1. The shop taps "Book install" on WhatsApp, or scans the QR.
2. AI reads the bill photo and a voice note into a job card (Telugu, Hindi, English).
3. Authorisation check: if the brand is not covered by a sub-contract, the job goes to the brand's own service centre and Keepwell only records it.
4. A dispatcher (AI-assisted, human-approved) assigns the nearest certified technician.
5. The visit uses a photo checklist, captures the serial number, and closes with an OTP.
6. The appliance record and QR sticker are created, and the shop gets a weekly summary.
7. A reminder fires before the warranty ends and an AMC offer follows.

**B. Out-of-warranty repair:** WhatsApp or voice, AI predicts the fault and part, price comes from the rate card, diagnose, quote, fix, photo, OTP, 90-day guarantee, UPI to Keepwell, technician paid in 48 hours.

**C. AMC (annual service plan):** sold at the counter or at installation, visits scheduled in the Oct-Feb trough, renewal reminder in month 11.

**D. Keepwell Protect:** the shop adds a 2-year repairs-only plan to the bill. It starts when the brand warranty ends. Claims come in by WhatsApp, AI triages, a human decides every rejection. **Status: counter-tested only, legal opinion pending.**

### 5.3 What is built and what is next [Story]

| Status | Items |
|---|---|
| Live | Intake in 3 languages, dispatch with a human dispatcher, photo and serial check, record and QR, shop summary, technician payouts, AMC reminders |
| Next (6 months) | Part prediction (needs a few thousand verified jobs) |
| Next (12 months) | Verification export |
| Later (year 3+) | Lead engine |

**Guardrails:** AI never sets a price, never overrides a gas or electrical safety stop, never decides a refund or a claim. AI cost under ₹5 a job (WhatsApp utility ~₹0.12, Gemini audio ₹0.05-0.17 a minute) **[Research]**.

**Weak point:** the files mention no demo, repository or screenshots. An investor will ask to see the product running.

---

## Part 6. The first money, and why it was structured that way

### 6.1 What we raised [Story]

| Source | ₹ | When |
|---|---|---|
| Founders' equity | 15 L | Aug 2025 |
| Pre-seed iSAFE (₹6 Cr post-money cap, 20% discount) | 45 L | Dec 2025 |
| State startup-policy grant (₹15 L sanctioned) | 10 L received | Feb 2026 |
| **Total** | **70 L** | |

### 6.2 Why an iSAFE
It was fast, priced no valuation, and bought time to run a pilot. At ₹10 Cr pre-money it converts to 6.0% (7.5% x 80% of the pre-money share). The iSAFE preference is capped at ₹45 L (02). Open question: whether it ranks pari passu with the seed.

### 6.3 Where every rupee went [Story]

| Use | ₹ L |
|---|---|
| Founder stipends | 21 |
| Cluster operations | 13 |
| Technology | 4 |
| Setup and working capital | 6 |
| Legal | 3 |
| Travel | 5 |
| **Spent** | **52** |
| **Cash left** | **18 (+5 grant due)** |

Founder equity today: 38 / 31 / 31, with a 4-year vest and 1-year cliff. The 10% option pool is created at the next round (02:151).

---

## Part 7. The test that went against us

The pilot scorecard had five red rows **[Story, model-generated]**:

| Miss | Result | Target |
|---|---|---|
| Units per month under signed shops by day 90 | 1,258 (2,516 by October) | 2,000 |
| Technician jobs per day | 2.6 (2.8 by October) | 2.8 (06:122) |
| Plan-seller jobs a month | 70 | 100 |
| Second service-centre sub-contractor | Under-delivered | Deliver |
| Brand authorisation | 41% of AC units | 45-50% edge |

**What we changed because of it:**
- **Shop commission mix:** repairs cut from 8% to 3% and AMC from 12% to 8%, with 25% on Protect, so a shop's income is about ₹3,170 a month **[Model]**.
- **Protect added** as a margin line (₹593 contribution per plan **[Model]**).
- **Partner clusters:** from year 3, service-centre owners run clusters for 10% of core revenue plus a ₹8 L opening-year minimum **[Model]**.

**Be candid with the investor:** the lift in mature cluster margin from about 5% to 14-16% comes from Protect, the commission shift and pooled parts buying (07b:85). Partner clusters change who carries the cost, not the margin. None of these has new field evidence behind it.

---

## Part 8. Eight months in the field

### 8.1 The results [Story, model-generated]

| Measure | Result |
|---|---|
| Shops | 12 (Mar) to 20 (Jun) to 34 (Oct) |
| Technicians | 8 to 22 (9 core); 1 of 22 left |
| Jobs | ~2,400 (775 installs, 1,330 service and repair, 280 plan-seller Jul-Oct) |
| AMC sold | ~240 |
| Appliance records created | ~2,150 |
| Revenue | ~₹25 L |
| Contribution | ~₹5 L (~20%), before the ₹1.5 L off-season floor and ₹3.2 L shop acquisition |
| Net pilot loss after cluster team cost | ~₹12.7 L |
| Units per shop per month | 74 |
| Install routing to Keepwell | 58% |
| Authorisation (brand) | 41% |
| Installs within 24 hours | 87% |
| First-visit fix rate | 81% |
| Callbacks | 6.5% |
| Safety incidents | 0 |
| Leakage (audit of 200 records) | 9% |
| AMC attach | 3.4% |
| Shop acquisition cost | ₹9.5k |

### 8.2 The learning curve
Contribution per shop was ₹4.5k in June, fell to about ₹2.8k a month in July-October (off-season, ~60% of full ramp), and is modelled at about ₹4.8k at full ramp. **Seasonality is the lesson:** an AC-only shop is idle in winter, which is why the plan adds washing machines, refrigerators and water purifiers, and schedules AMC visits in the trough.

### 8.3 Why only 34 shops, and why that is deliberate
One cluster, one belt, one language. Density is the unit of the business. Breakeven is about 35 shops at full ramp **[Model]**; the pilot reached 34 shops but was at about 60% ramp in October and not yet profitable. The Protect counter test (12 shops, ~1,200 covered units, ~6% attach, 72 plans, ₹1.4 L including GST, 0 claims) shows willingness to buy, not claims cost. **[Story]**

---

## Part 9. Does the shop, the household and the technician actually win?

| Stakeholder | What they get | Numbers | Tag |
|---|---|---|---|
| **Shop** | Its name on a guarantee; less joint-liability risk; keeps the customer; commission on every job; a record of its buyers | Shop pays ₹0. Commission: 5% installs, 3% repairs, 8% AMC, 25% Protect. Income about ₹3,170 a month (modelled); the earlier core-only figure was ₹1.7k a month. 41 of 64 said they would route | Model/Story |
| **Household** | Install within 24 hours (87% in pilot), fixed price from a rate card, 90-day guarantee, a record, AMC | AC service ₹550; AMC ₹1,099-1,299; Urban Company from ₹699-799; Protect ₹1,499-2,999 | Research/Story |
| **Technician** | Extra jobs, parts on credit, insurance, payment in 48 hours, an off-season floor for the core group | Per job: install ₹500, repair ~₹330, AC AMC ₹400 a visit, purifier AMC ₹450 a visit | Model |
| **Brand or service centre** | Installs done in towns it cannot staff, jobs closed against targets | Keepwell nets ~₹800 per AC install; the service centre keeps ~₹400 | Story |
| **Plan seller** | Fulfilment in towns where it has no repair supply | 70 jobs a month (target 100) | Story |

**Technician arithmetic, corrected.** At ₹330-500 a job, 15 Keepwell jobs a month is about ₹5-7.5k, not ₹15k. A technician working only for Keepwell at 2.6 jobs a day (65 jobs a month at ~₹400) earns about ₹26k (an upper bound: it assumes 25 active days, while 06:49 counts only days with Keepwell jobs and core technicians did about 15 jobs a month). So the honest line is: "Keepwell supplements a mechanic's income, and a core technician on full routing earns about ₹26k." **[Model; my arithmetic. Replace with real pay records.]**

**One line per stakeholder (for the deck):**
- Shop: "You sell it, we stand behind it, you earn on every job."
- Household: "One trusted number for your appliance."
- Technician: "Steady work, the right part, paid in 48 hours."
- Brand: "Your installation promise, kept in towns you cannot staff."

---

## Part 10. Why nobody can catch up (and why they might)

### 10.1 What can be copied, and what cannot

| Layer | Copyable? | Evidence status |
|---|---|---|
| WhatsApp and voice intake, AI job cards | Yes, quickly | The files say "AI is the cost engine, not the moat" |
| A technician certification | Partly | Needs local density |
| **Exclusive multi-year shop service-arm agreements** | Hard, if signed | **No signed example. No retention data yet.** |
| **Cluster density (50-70 shops sharing routes, parts, technicians)** | Hard, but needs time and capital | One pilot cluster |
| **Consent-based appliance record** | Hard to rebuild once shops sign | ~2,150 records [Story] |
| **Brand authorisation** | By partnership, not by moat | 41% via two non-exclusive 12-month sub-contracts that lapse about now |

### 10.2 The competitive map

| Player | Position | Threat |
|---|---|---|
| Onsitego-Qdigi | Plans through chain counters, ~400-450 service centres | **High, closest.** Possible partner |
| Urban Company | Household app, from ₹699-799, takes ~36% | Medium; in the pilot belt |
| Zopper and OneAssist | Plan sellers | Medium; partners or competitors |
| 247around and SERVIZ | Brand-paid installs | Low-medium |
| Jeeves and resQ | Captive | Low |
| Brand service centres | Thin in small towns | Medium |
| Local mechanics | 44% of AC service | **Biggest by volume** |

### 10.3 Porter's five forces, in short
Substitutes (local mechanics) and supplier power (brands and parts) are strong. New entrants are possible. The verdict in the files is "attractive only with density plus authorisation plus shop exclusivity", and all three are still unproven in the field.

**Statements to drop:** "nobody serves the independent shop" (replace with "nobody *owns* it"), and the HomeServe/Asurion analogy, which does not hold because HomeServe's exclusivity sits with utilities and insurers that own the billing relationship, not shops.

---

## Part 11. The engine: how one shop becomes a cluster becomes a business

### 11.1 One job (net of 18% GST) **[Model]**

| Job | Contribution | Note |
|---|---|---|
| Out-of-warranty repair (₹1,000 bill) | ₹164 (19%) | |
| AC service | ₹112 | |
| AC gas refill | ₹346 | |
| AC repair | ₹224 | |
| **AC installation, authorised** | **₹469** (pilot mix) | ₹730 only if the brand pays the full designed fee |
| AC AMC | ₹103 per plan | |
| Washing-machine installation | ₹77 | |
| Water-purifier AMC | ₹438 per plan | |
| **Protect plan (₹2,000 incl. GST)** | **₹593 (35%)** | Shop 25% (₹424), claims 35% (₹593), admin 5% (₹85) |

### 11.2 One shop, one year **[Model]**
About 350 jobs, ₹4.39 L revenue, ₹116k contribution (₹85k core plus ₹32k from about 53 Protect plans: 74 units x 12 months x 75% covered x 8% attach).

### 11.3 One cluster, steady state **[Model]**

| | Own-run | Partner-run |
|---|---|---|
| Shops (mature) | 60 | 60 |
| Revenue | ₹2.72 Cr | ₹2.72 Cr |
| EBITDA | ₹44.3 L (**16.3%**) | ₹38.4 L (**14.1%**) |
| Breakeven | **22 shops** (mature, with Protect) | |
| Breakeven from pilot data | **~35 shops** at full ramp (the pilot had 34 at ~60% ramp, not yet profitable) | |

### 11.4 Growth comes from capacity, not hope
Clusters: 3, 6, 11, 18, 28, 40, 55, 72 across years 1-8. Each cluster ramps 25 / 60 / 90 / 100% by year. Shop acquisition cost ₹14k own-run, ₹20k partner. 10% of shops are replaced each year.

### 11.5 Eight-year plan, BASE (₹ Cr) **[Model; the numbers an investor should see]**

| Year | Clusters | Shops | Revenue | EBITDA | EBITDA % | Cumulative cash |
|---|---|---|---|---|---|---|
| 1 | 3 | 180 | 2.4 | -1.1 | -45% | -1.0 |
| 2 | 6 | 360 | 6.8 | -1.5 | -23% | -2.7 |
| 3 | 11 | 660 | 15.3 | -1.9 | -13% | -4.5 |
| 4 | 18 | 1,080 | 29.7 | -1.4 | -5% | **-5.8 (peak)** |
| 5 | 28 | 1,680 | 53.9 | +0.6 | 1% | -5.0 |
| 6 | 40 | 2,400 | 86.9 | +4.1 | 5% | -0.4 |
| 7 | 55 | 3,300 | 130.5 | +8.6 | 6.6% | +7.4 |
| 8 | 72 | 4,320 | 181.6 | +15.3 | 8.4% | +20.3 |

**Read this table with three warnings:**
1. The ₹5.8 Cr peak includes **Protect cash held as a float**. Without plan cash the peak is ₹11.7 Cr; without Protect at all, ₹17.5 Cr.
2. In the stress case the peak is **₹8.9 Cr** and year-7 EBITDA is 4.7% (₹4.0 Cr). In the LOW case the business never turns profitable and needs ₹57.7 Cr. **Lead with the stress case.**
3. Service-only EBITDA is only +0.3 Cr in year 7 (0.2%). The "service is healthy on its own" claim rests on a hypothetical mature run-rate (9.1%), not on the plan years.

### 11.6 What moves the numbers

| Assumption | BASE | Stress | Why it matters |
|---|---|---|---|
| Protect attach | 8% | 5% | No Indian benchmark for 8%. It is the riskiest input |
| Protect claims cost | 35% | 45% | The 35% rests on an assumed 0.6 factor |
| Units per shop per month | 74 (pilot), 60 (plan) | | Pilot shops were hand-picked |
| Brand authorisation | 35% of AC units | not varied in stress | Separate sensitivity (05:158): at 0%, breakeven is ~50 shops (~80 if AC-only). Based on non-exclusive sub-contracts |
| Partner operators | 10% fee | | No evidence any service-centre owner will run a cluster for this |
| Shop acquisition cost | ₹14k own / ₹20k partner | not varied in stress | Older files used ₹9.5k, ₹18k and ₹22k (the red-team set) |

**Gap to close:** lifetime value, LTV to acquisition cost and payback were never restated for the final model. The only figures are from the earlier designs (LTV:CAC of about 9x with red-team inputs). Recompute them per shop under the Protect and partner structure.

---

## Part 12. How big this can get

### 12.1 How many shops exist? Two methods, and their disagreement

| Method | Result | Note |
|---|---|---|
| **Supply side:** ~14 M ACs a year, 46-65% through general trade, 25-35% of a dealer's major units, so 1.8-2.5 M major units a month, divided across ~45,000 independent shops | ~₹4,150 Cr | ~50 units per shop per month (low confidence) |
| **Demand side:** households in 449 cities (NFHS-5), times frequency and bills, plus small towns, grossed up for installs | ~₹3,600 Cr | Covers all households, not just shop customers |

**TAM: about ₹4,000 Cr a year (₹3,500-4,800 Cr)**, in after-sale spend through independent shops, outside the metros (64% of the all-India ₹6,500 Cr).

**Cautions:** (a) the two methods disagree on AC share (86% vs 56%) and the files admit that landing close "is partly coincidence"; (b) the earlier validation figure was ₹1,550 Cr (9,000 large shops), so the target was redefined, a 2.6x jump; (c) "outside metros" includes rural and Tier 4+, not only Tier 2/3.

### 12.2 From the whole market to our first towns

| Layer | Value | Tag |
|---|---|---|
| TAM | ~₹4,000 Cr | Model |
| SAM (five southern states, 26% of Tier 2/3 repair value) | ~₹1,040 Cr | Research x Model |
| **Beachhead (AP and Telangana)** | **~₹360 Cr (8.9%)** | Model |

### 12.3 What Keepwell can earn (revenue, not market value)
Year-7 SOM is ₹130.5 Cr, built from: core service ₹79 Cr, plan seller ₹3 Cr, Protect ₹10 Cr, parts, trade-in and refurb ₹27 Cr, data ₹11 Cr **[Model/plan]**. That is 3,300 shops, which is about 7% of the ~45,000 independent shops, about 11% of the ~29,000 non-metro shops, and about 20-25% of the southern Tier 2/3 shops.

### 12.4 The path, and the honest framing
At year 7 this is a **~₹130 Cr services business at 6.6% EBITDA**, exiting to a strategic buyer. It is not a software multiple. The ₹11 Cr data line has no buyer yet. Lead with the beachhead and the pilot-based capture rate, and present TAM as context.

**To replace before pitching:** a bottom-up SOM from real capture data (shops signed x units x capture rate), not a plan.

---

## Part 13. What we need now, and why exactly that much

### 13.1 The method: the ask is an output, not a wish

| Component | ₹ Cr |
|---|---|
| One-year costed need (after the Protect float and grant) | 1.08 |
| Six months to raise the next round | 0.84 |
| Jan-Mar seasonal buffer | 0.52 |
| **Total** | **2.44, rounded to ₹2.5 Cr** (minimum close ₹2.0 Cr) |

**Corrections:**
- The cash used in the netting (₹18 L) is a **November** figure. By a Feb-Mar close it is about ₹2 L, so the true need is about ₹2.6 Cr **[derived by me, not in the step files]**.
- The model clock starts January 2027 but the close is Feb-Mar 2027, so "month 18" is about 15 months after the money arrives.
- Do **not** net Protect cash against the operating need: it is customer money held for claims.

### 13.2 Why this much, and what it does not fund
The ₹2.5 Cr takes the business to roughly month 18-21. The model's peak need is ₹5.8 Cr (BASE with float), ₹8.9 Cr (stress), so the seed is the first of two rounds: **Round 2 of about ₹5 Cr in H2 2028**, plus a stress-case tail. By my arithmetic that is 8.9 - (2.5 + 5) = about ₹1.4 Cr, whereas 08:137 says about ₹2.5 Cr, so reconcile the two. The earlier "Round 3 of ₹15 Cr" is a growth round, not a funding need; resize it.

### 13.3 What the money pays for, by purpose

| Purpose | ₹ L | Share |
|---|---|---|
| Discover product-market fit (pilot belt and second cluster) | 75 | 30% |
| Build the team | 75 | 30% |
| Build the product | 38 | 15% |
| Marketing and sales (shop acquisition) | 25 | 10% |
| Working capital | 37 | 15% |
| **Total** | **250** | **100%** |

**Gap:** the use of funds does not map to the cost lines, and the ₹0.52 Cr buffer has no row. Add it.

### 13.4 What the ₹2.5 Cr buys: the gates

**Month-12 gate. [DECIDE: this is my proposal, not in the step files.** They set these thresholds at month 18 and keep only a month-12 stop rule (units under 60 or attach under 2%); `12_storyboard_redteam.md` says tranche gates were removed. Routing and contribution targets come from the pilot scorecard (06). Making it a contractual release, not a founder promise, is the change.**]**
- Units per shop at least 65; install routing at least 50%.
- Authorisation for at least 35% of AC units, evidenced by a signed letter.
- Contribution per shop at least ₹4.5k.
- Protect attach at least 3.5% (at least 5% in mature shops) with **real claims data**.
- Protect legal opinion obtained (service contract, not insurance).
- If units per shop fall below 60 or attach below 2%, stop expanding.

**Month-18 milestones (re-based to the close date):**
- 4 clusters; at least 150 shops (lenient: this equals the stress count at month 12, so raise it); at least 65 units per shop.
- Pilot cluster at or above 45 shops with contribution at least equal to team cost.
- At least ₹5 Cr run-rate revenue.
- 3 signed partner-cluster agreements; one paid install-verification contract.
- Reserve account live for Protect.

### 13.5 Sanity checks
- Seed band in India: ₹50 L-2 Cr; the ask is above it.
- About 1x year-1 revenue (₹2.4 Cr BASE).
- Runway: about 4.4 months of cash today, so a bridge or a faster close is needed.

---

## Part 14. The deal

### 14.1 Who we raise from
One lead seed fund or angel network (₹1.25 Cr), strategic angels (₹0.75 Cr), and the state startup-policy equity (₹0.5 Cr, policy "up to ₹50 L"). All three amounts are **[Story/target]**. **Soft-circle the lead before pitching.**

### 14.2 The instrument
Priced seed CCPS (compulsorily convertible preference shares). The pre-seed iSAFE converts into the round. The term sheet follows the course template, which was designed for a Series A, so adapt it for a seed.

### 14.3 The valuation: methods, and the gap

| Method | Result |
|---|---|
| Indian seed comparables (not shown in the files) | ₹6-12 Cr pre |
| Course scorecard: 9 x 73/80 | ₹8.2 Cr pre |
| Weighted-factor (founder-scored, labelled "cross-check only") | ₹10.0 Cr pre |
| VC method ceiling (stress case, 40% target return, 5 years) | ₹14.4 Cr post |
| Same at a 50% hurdle / 60% hurdle | ~₹10.2 Cr / ~₹7.4 Cr post |

**The problem:** ₹10 Cr pre-money is about **27x** the annualised pilot revenue (~₹37 L, unaudited), and about 4-5x forward year-1 revenue. The founders scored themselves high on team and channels. The validation file called ₹10 Cr "too rich" and suggested ₹75 L-₹1 Cr at a ~₹6 Cr cap.

**Recommendation [DECIDE]:**
- **Option A (preferred):** ₹2.5 Cr in **two tranches** (₹1.25 Cr at close, ₹1.25 Cr on the month-12 gate), at **₹8 Cr pre-money**. Pre-money includes the 10% option pool and the iSAFE.
- **Option B:** keep ₹10 Cr pre, tranche as above, and re-vest part of the founder shares (about 40% are vested at close).

### 14.4 The investor's outcomes, honestly (Option A)
Seed stake: 2.5 / 10.5 = **23.8%**. After Round 2 (₹5 Cr at ₹30 Cr pre, 14.3% dilution) and Round 3 (₹15 Cr at ₹85 Cr pre, 15% dilution), about **17.3%**.

| Exit | Enterprise value | Seed proceeds | Multiple | Basis |
|---|---|---|---|---|
| Stress, year 7, 12x EBITDA | ₹48 Cr | ₹8.3 Cr | **3.3x** | Realistic private-equity exit |
| BASE, year 7, 12x EBITDA | ₹103 Cr | ₹17.9 Cr | **7.2x** | Realistic private-equity exit |
| Stress, year 7, revenue multiples | ₹255 Cr | ₹44.2 Cr | 17.7x | Optimistic; needs data revenue of ~11% |
| BASE, year 7, revenue multiples | ₹376 Cr | ₹65.2 Cr | 26.1x | Optimistic |

**Say aloud:** the revenue-multiple outcomes use 2.5x operating revenue plus 7x data revenue (09:79) on a business earning 5-7% EBITDA, which implies a 44-64x EBITDA multiple. The realistic outcomes are 3-7x. Also, later rounds priced at 5-7x revenue contradict an exit at 2.5x revenue; if Round 3 prices at the exit multiple, the seed is diluted more. Recompute before a data room opens.

### 14.5 The cap table

| Holder | Today | After seed, Option A | After seed, ₹10 Cr pre (course case) |
|---|---|---|---|
| Founders | 100% (38 / 31 / 31) less the iSAFE | **60.5%** | 64.0% |
| Seed investors | n/a | **23.8%** | 20.0% |
| Option pool | none yet (created at the next round, 02:151) | **10.0%** | 10.0% |
| iSAFE | 7.5% (cap) | **5.7%** | 6.0% |

After Rounds 2 and 3 in the course case the founders hold 46.6% and the seed 14.6%.

### 14.6 The terms (investor-facing)
- 1x non-participating preference; broad-based weighted-average anti-dilution; pro-rata; information rights; a 3-person board (2 founders, 1 lead director) plus a state observer; 3-year founder lock-in; affirmative votes on off-budget spend over ₹5 L, debt over ₹10 L and any change to the Protect structure or reserve.
- **Add:** tranche release tied to the month-12 gate; partial founder re-vesting; the Protect legal opinion as a condition precedent to tranche two; clarity on the iSAFE's rank; a redemption or put right (the current exit clause "within 7 years" has no teeth).

### 14.7 Who buys Keepwell in the end
Warranty and after-sales platforms (Onsitego-Qdigi, Asurion-type), durables majors and chains, insurers and underwriters, and private-equity roll-ups (Frontdoor at about 2.9x revenue and 10.8x EBITDA is the cited precedent). Several precedents cited are US or unverified here. No letter of intent exists.

---

## Part 15. Trust, law and whose data it is

### 15.1 Trust is built into the product
OTP close on every job, photo checklist, serial capture, 90-day guarantee, payment in 48 hours, and an AI that never sets a price, never overrides a safety stop, and never decides a refund or a claim.

### 15.2 Whose data is it?
The appliance record belongs to the household and is shared with the shop and the technician with the household's consent. Keepwell holds it as the custodian. Any brand or plan-seller use (verification, failure intelligence) needs consent, and no data customer exists yet.

### 15.3 The laws that matter, and where we stand

| Area | Status |
|---|---|
| **Protect as a service contract, not insurance** (IRDAI risk) | **Legal opinion not yet obtained**, yet 72 plans already sold [Story]. Condition precedent to tranche two |
| Consumer protection: seller joint liability | Real precedent; the product reduces it but does not remove it |
| Personal-data law (DPDP Act): consent, audit | Audit open |
| GST | Prices include 18% GST; one step file says the model is "built net" while the validation file says prices must include GST. Confirm |
| Gig-worker levy | Estimated 1.0-1.4% of revenue (up to 5% of payouts worst case); not resolved |
| Money handling | The shop or service provider is the merchant for UPI; confirm with counsel whether any payment-aggregator licence is needed |

---

## Part 16. How we tried to break our own story

### 16.1 The files' own checks
- **Gate 1 red-team** (validation report) flagged that the TAM "breaks" at ₹4,000 Cr, ₹10 Cr pre is "too rich", and brand authorisation is the go/no-go. **Still open** in that file.
- **Tough-questions** pass: authorisation, repair capture, routing rate and technician productivity "not proven".
- **Fundability score:** 9 x 73/80 = ₹8.2 Cr, weighted ₹10.0 Cr.
- **Storyboard red-team:** "21 issues, all fixed". The table lists 20, and the fixes are self-asserted.

### 16.2 This review (four independent agents, this session)
- **Arithmetic:** per-job, Protect, cluster, P&L, cap table, dilution and returns all recompute correctly. Three small mismatches: "about 40%" dilution for ₹7.5 Cr at ₹10 Cr pre is really 43%; the year-7 stress value needs ~11% data revenue, not 8-9%; the "25x EBITDA" cross-check gives ₹215 Cr, not ₹376 Cr.
- **Evidence:** pilot, interviews, authorisations, founder histories and money raised are [Story]. The pilot is model-generated, so it cannot validate the model.
- **Drift from Gate 1:** TAM, valuation, ask size, the competition claim and margin all moved after the validation report without new evidence. Protect was added later and never formally approved.
- **Open items described as closed:** brand authorisation shows "in place [Story]" while the validation file still lists it as open.

### 16.3 What the model checks itself against
Stress and LOW cases, sensitivities on Protect attach and claims, and a no-float cash view. The LOW case (never profitable, ₹57.7 Cr need) is the real downside and is excluded from the headline.

---

## Part 17. What could go wrong, and what we do then

| Risk | Trigger | What we do | Stop rule |
|---|---|---|---|
| **Brand authorisation does not come** | Under 35% of AC units by month 12 | Focus on out-of-warranty repair and non-AC categories; push for a direct brand letter | Breakeven moves to ~50-80 shops; stop expanding |
| **Shops will not route installs** | Routing under 40-50% | Test commission levels and free-install offers | Kill if under 40% after 6 weeks |
| **Technician leakage** (they take the customer) | Leakage above 9% | QR, record, guarantee, parts access, fast payout | Audit monthly |
| **Protect claims or regulation** | Claims above 45%; no legal opinion | Cap exposure, hold the reserve, re-price | Do not release tranche two without the opinion |
| **Seasonality** | Technicians idle Oct-Feb | Add washing machine, refrigerator, purifier; schedule AMC visits in the trough | |
| **Urban Company or a plan seller moves in** | Price pressure in the belt | Lock shops early; focus on density; partner with plan sellers | |
| **Partner operators will not run clusters for 10%** | Fewer than 3 signed by month 18 | Run clusters ourselves, which needs more capital | |
| **Cash** | About 4.4 months today | Close faster, or take a bridge | |
| **Founder gap and no exit experience** | | Name advisors; add an independent director later | |

---

## Part 18. What is real and what is illustrative

| Item | Status |
|---|---|
| Third-party facts (warranty terms, wait times, LocalCircles survey, Urban Company pricing, GST change, AC market data) | **Real/Research**, cited, not re-checked here |
| Household survey: 19 households (12 qualified) and 6 interviews, Hyderabad and Visakhapatnam, Sept 2026 | **Real**, small and outside the pilot belt |
| Founder names | **Real** |
| Founder histories and network counts (600+ dealers, 200+ service-centre owners, 220 centres, 3,000 technicians) | **Story** |
| Company timeline, incorporation, iSAFE, grant | **Story** |
| Discovery counts (64 shops, 41 technicians, 6 centres, 3 brand teams, 2 plan sellers) | **Story** |
| Pilot results (34 shops, ~2,400 jobs, ₹25 L, scorecard) | **Story, model-generated** |
| Protect counter test (72 plans) | **Story** |
| Money raised and spent (₹70 L, ₹52 L, ₹18 L) | **Story** |
| Per-job and per-cluster economics, the eight-year plan | **Model**, arithmetic verified, inputs assumed |
| TAM, SAM, SOM | **Model**, with the caveats in Part 12 |
| Round 2 and 3 sizes, exit values, investor commitments | **Story/target** |

**Rule for the deck:** show a [Story]/[Model] tag on every slide that carries one of these numbers, and put "what we will replace it with, and when" beside it.

---

## Epilogue: What the money becomes

The ₹2.5 Cr, released in two tranches, does four things: it runs the pilot belt to a real, ledger-backed record; it opens the second cluster; it gets the Protect legal opinion and a real claims history; and it signs the first brand authorisation letter and the first three partner clusters. If the month-12 gate is met, Round 2 of about ₹5 Cr scales the model. If it is not, the stop rule applies and the investor keeps their preference.

The story an angel can believe is not "we have proven it". It is: *the logic is sound, the arithmetic holds, the per-job economics are positive, and here is exactly which four numbers the next twelve months will prove or kill.*

---

## Appendix A. Proof index: every claim and where to check it

| Claim | Source file (in `ESFS/pitch_v2/steps/`) | Status |
|---|---|---|
| Problem evidence (waits, warranty voiding, 44%, 80-91%) | 01, 04 | Research |
| Shop and technician discovery counts | 06 (lines 73-78) | Story |
| Household survey n=19 (12 qualified) | 06 (line 73), 04 (line 158) | Real |
| Founder backgrounds | 02 | Story |
| Product flows and guardrails | 05 | Story/Model |
| Per-job economics | 00, 03, 07 | Model, recomputed |
| Protect per-plan economics | 07b (lines 93-100) | Model, recomputed |
| Eight-year plan, scenarios | 07b (lines 188-225), `model/plan_v3.py` | Model, reproduced |
| TAM, SAM, SOM | 04 | Model, caveated |
| Pilot results and scorecard | 06 | Story |
| Ask, use of funds, milestones | 08 | Derived, arithmetic verified |
| Valuation, cap table, returns | 09 | Derived, arithmetic verified |
| Compliance and data room | 10 | Mixed |
| Fundability score | 11 | Founder-scored |
| Red-team | 00_tough_questions, 00_validation_report, 12 | Self-review |

## Appendix B. Every number on one page (the canon: use only these)

| Number | Meaning | Tag |
|---|---|---|
| ~₹4,000 Cr (₹3,500-4,800) | TAM, after-sale spend via independent shops, outside metros | Model |
| ~₹1,040 Cr / ~₹360 Cr | SAM (five southern states) / beachhead (AP and Telangana) | Model |
| ₹130.5 Cr; 3,300 shops; 55 clusters | Year-7 SOM (plan) | Model |
| 45,000 shops; ~50 units/shop (supply); 74 (pilot); 60 (plan) | Shop count and units | Assumed / Story / plan |
| ₹164 / ₹469 / ₹593 | Contribution: repair / authorised AC install (pilot mix) / Protect plan | Model |
| 8% (5% stress) | Protect attach | Assumed, no benchmark |
| 35% (45% stress) | Protect claims cost | Assumed |
| 60 shops; ₹2.72 Cr; 16.3% / 14.1% | Mature cluster: size, revenue, EBITDA own-run / partner-run | Model |
| 22 shops mature / ~35 at full ramp from pilot data | Cluster breakeven | Model / Story |
| ₹2.4 Cr / ₹130.5 Cr / ₹181.6 Cr | Revenue year 1 / 7 / 8 (BASE) | Model |
| 6.6% / 8.4% | EBITDA year 7 / 8 (BASE) | Model |
| ₹5.8 Cr / ₹11.7 Cr / ₹8.9 Cr / ₹57.7 Cr | Peak need: BASE with float / BASE no float / stress / LOW | Model |
| 34 shops; ~2,400 jobs; ~₹25 L; ~₹37 L annualised | Pilot | Story |
| 58% / 41% / 87% / 81% / 6.5% / 9% / 3.4% | Routing / authorisation / 24 h install / first-visit fix / callbacks / leakage / AMC attach | Story |
| ₹9.5k / ₹14k / ₹20k / ₹22k | Shop acquisition cost: pilot / plan own / plan partner / red-team | Story / Model |
| ₹70 L / ₹52 L / ₹18 L (+5 L) | Raised / spent / cash (grant due) | Story |
| ~4.4 months | Runway to early April 2027 | Derived |
| ₹2.5 Cr (min ₹2.0 Cr), two tranches | The ask | [DECIDE] |
| ₹8 Cr pre / ₹10.5 Cr post / 23.8% | Option A | [DECIDE] |
| ₹10 Cr pre / ₹12.5 Cr post / 20% | Course-case valuation | Derived |
| 23.8% to ~17.3% | Seed stake after Rounds 2 and 3 (Option A) | Derived |
| 3.3x / 7.2x | Realistic exits (12x EBITDA, stress / BASE) | Derived |
| 17.7x / 26.1x | Optimistic exits (revenue multiples) | Derived |
| ₹5 Cr at ₹30 Cr pre; ₹15 Cr at ₹85 Cr pre | Round 2 (H2 2028); Round 3 (resize) | Story/target |
