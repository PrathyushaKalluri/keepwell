# Keepwell: problems, scenarios and revenue streams
**Go-to-market: Indian Tier 2/3 cities first, then Tier 1.**
Builds on the earlier files in this folder (problem map, scenario IO, competitive analysis, architecture). Evidence tags: 🟢 sourced, 🟡 single/secondary source, 🔴 my assumption, to be validated.

---

## 1. Why Tier 2/3 first (and what it changes)

**Supporting evidence**
- 🟡 Q4 2024 durables data: Tier 3 cities grew 10%, versus 7% for Tier 1 and 6% for Tier 2.
- 🟡 Trade and market reports say first-time buyers of refrigerators and washing machines are a significant share of Tier 2 sales, while metros are replacement-driven. No percentage was found.
- 🟡 Organised repair is thin in small towns. ServiceOnDoors says it is expanding to 200 cities to address technician shortage. This is a company claim, not an independent measurement.
- 🟢 LocalCircles: 76% of AC owners avoid brand service. Local technicians are the default.
- 🟡 Urban Company and the OEM networks are metro-weighted. Tier 2/3 is served by owner-run agencies and shops.
- 🔴 No source gave the number of repair agencies in India, or the Tier 2/3 share of appliance sales. Both are needed for sizing.

**What this changes in the product**

| Tier 2/3 reality | Design consequence |
|---|---|
| Owner-operated agencies with 2–10 technicians, WhatsApp and phone, no software | The product must run inside WhatsApp and a phone. No dashboard is needed on day one. |
| Hindi, Telugu, Tamil, Kannada and Marathi, often mixed with English | Voice-first with transcribe-then-extract. Test accuracy per language before launch. |
| Low willingness to pay for software, high willingness to pay for a job done | Charge per fix or on commission, not a monthly seat fee. |
| Cash and UPI, thin margins | Don't model payments as revenue. Small-merchant UPI stays at zero MDR. |
| Parts are hard to find, and informal parts are common | Parts sourcing and "awaiting part" status are core features. |
| Warranty is poorly documented. Invoices are paper or photographed. | Photo-of-invoice capture is the main way records get created. |
| Trust deficit with brand service and with local technicians | A verified job record and a visible warranty status build trust on both sides. |
| Low-bandwidth, shared and older Android phones | Light web/WhatsApp flows, offline-tolerant capture, small uploads. |

---

## 2. Problems

Priority scores come from the earlier problem map (2×Impact + Google leverage + (6−Effort) + (6−Build barrier) + (6−Penetration barrier)). Tier fit is new.

| # | Problem | Who feels it | Evidence | Tier 2/3 fit | Who pays |
|---|---|---|---|---|---|
| P1 | Agencies lose visits to poor diagnosis. They go without the part, the model or the history, and the revisit costs a trip. | Agency owner, technician | 🔴 mechanism plausible, no measured revisit rate | **High** | Agency |
| P2 | Job notes are in voice and Hindi/regional language. Records, quotes and warranty claims are unstructured or never written. | Agency, customer | 🟡 | **High** | Agency |
| P3 | Customers can't prove warranty. Invoice, serial and model are lost or unreadable. | Household | 🟢 55% had a defective in-warranty high-value product; only 21% of those who acted got refund/replacement | **High** (first-time buyers, paper invoices) | No clear payer today |
| P4 | Quote disputes and fear of overcharging. No benchmark for a fair price. | Household | 🟡 | **High** | Household, indirectly agency |
| P5 | Parts: wrong part, long wait, grey market, no visibility. | Agency | 🟡 | **High** | Agency, parts sellers |
| P6 | Warranty/protection claims are slow and fraud-prone. Administrators and OEM networks pay for manual triage. | Administrators, OEMs | 🟡 B2B is the best-evidenced money | **Medium** (needs partners, mostly metro-led) | Administrators, OEMs |
| P7 | Plan and AMC upsell is untargeted. Agencies don't know which homes are about to need service. | Agency, plan seller | 🔴 | **Medium** | Agency, plan provider |
| P8 | End of life: no good resale, pickup or recycling route. Only 22.3% of global e-waste is documented as recycled. | Household, producers | 🟢 global figure | **Low now**, vision | Producers (EPR), recyclers |
| P9 | OEMs and administrators have no view of repair quality in the unorganised channel. | OEMs | 🔴 | **Low now** | OEMs |
| P10 | Safety: unsafe repair or reuse of gas, heating and high-voltage appliances. | Household | 🔴 hard-stop list is unverified inference | **Cross-cutting**, needs expert review | None, but a liability |

**Reading.** P1, P2 and P5 are the Tier 2/3 wedge: they hurt agencies, agencies decide quickly, and they can pay per use. P3 and P4 are the strongest consumer pain but have no payer, so they ride on the agency product. P6 and P7 are where larger money is, but they need distribution that Tier 2/3 agencies provide.

---

## 3. Scenarios

### A. Prepared Visit: the agency AI desk (Phase 1, Tier 2/3)
- **Trigger:** a customer calls, messages or sends a photo/voice note on WhatsApp.
- **Input:** voice, photo of appliance label and invoice, customer address, prior jobs.
- **Output:** a structured job card (model, serial, symptom, likely parts, warranty status, safety flag), quote draft, technician brief, follow-up message.
- **Human step:** agency approves price, warranty claims and any data sharing.
- **Value:** fewer revisits, quotes in minutes, a record exists for every job.
- **Priority score:** 23 (highest).

### B. Home Memory and plans (Phase 1.5, same households)
- **Trigger:** a completed job card, with the customer's consent.
- **Input:** the job record, the invoice photo, the appliance identity.
- **Output:** a household record (appliances, warranty dates, service history), reminders, a plan or AMC offer when a window is expiring.
- **Value:** trust (P3, P4), repeat business for the agency, a second data asset.
- **Priority score:** 22. Scenario D (consumer claim/fair-price helper) is folded in here as an evidence pack, not legal advice.

### C. Claims triage for administrators and OEM networks (Phase 2, from Tier 2/3 base into Tier 1)
- **Trigger:** a claim is raised against a plan or warranty.
- **Input:** job card, evidence photos, invoice, warranty terms.
- **Output:** a recommended decision with evidence, a fraud-risk flag, a repair-versus-replace view.
- **Human step:** the administrator's adjuster decides.
- **Value:** cost per claim down, evidence quality up. This is the best-evidenced B2B money.
- **Priority score:** 22.

### E. Circular pickup and EPR (vision, Phase 3)
- **Trigger:** end-of-life or unrepairable appliance.
- **Input:** grade, location, ownership record.
- **Output:** pickup, resale or recycling route, producer EPR evidence.
- **Why later:** EPR pricing is contested (₹22/kg floor stayed in the Delhi High Court, no final judgment found), and it is logistics-heavy.
- **Priority score:** 19.

### Sequence
**A → B → C**, with D inside B and E as the long-term vision. A creates the data and the agency network. B links the household. C monetises both at scale.

---

## 4. Phasing: Tier 2/3 first, then Tier 1

| Phase | Where | Product | Goal |
|---|---|---|---|
| 0 (now–buildathon) | 1–2 Tier 2 cities (suggest your pilot cities) | A prototype with 15–20 interviewed agencies | Validate willingness to pay per fix. Measure revisits, quote time and voice accuracy. |
| 1 | 5–10 Tier 2/3 cities | A, then B | Agency count, jobs per agency, household records created |
| 2 | Add Tier 1 | C with administrators and OEMs, B plans | Partner contracts. Tier 1 households already hold records created via Tier 2/3. |
| 3 | National | E circular | Producer EPR and resale partnerships |

**Why this order works.** Tier 2/3 agencies have the least software and the least competition from Urban Company and OEM networks, so adoption is easier. Tier 1 is where plan sellers, administrators and OEM decision-makers sit, so it is where C scales. One caution: Tier 1 customers on Urban Company are accustomed to polished apps, so the Tier 1 version needs a consumer-grade front end (a Phase 2 task).

---

## 5. Revenue streams

All numbers are 🔴 assumptions to test, not forecasts.

| # | Stream | Payer | Model | Illustrative price | Phase | Evidence / risk |
|---|---|---|---|---|---|---|
| R1 | Per-fix AI desk fee | Agency | Pay per completed job card | ₹40 per fix (test ₹100) | 1 | Cost per job at Gemini prices must stay well below the fee. Flash prices double on 1 Jan 2027, so test at 2027 prices. |
| R2 | Agency subscription (lite) | Agency | Monthly, optional, for quotes, reminders and reports | ₹300–500/month | 1 | Low WTP in small towns, so keep it optional. |
| R3 | Plan/AMC commission | Plan provider, agency | % of plan sold via Home Memory | 10–20% of plan value | 1.5–2 | Check the rules for selling plans and any licensing need. |
| R4 | Parts referral | Parts sellers, distributors | Referral on matched orders | 3–8% | 1.5 | Grey-market risk. Needs verified suppliers. |
| R5 | Claims triage fee | Administrators, OEMs | Per claim processed, or per month | ₹30–100 per claim | 2 | Best-evidenced demand, long sales cycle. |
| R6 | Service lead routing | OEM or plan provider | Fee per assigned, completed job | ₹100–250 per job | 2 | Needs OEM agreements. |
| R7 | Household premium (optional) | Household | Annual record plus claim pack | ₹199–499/year | 2 | Consumer warranty-wallet apps are tiny. Don't depend on it. |
| R8 | Data and insights | OEMs, administrators | Anonymised failure and repair-quality reports | Contract-based | 3 | Consent and DPDP duties apply (main duties ~May 2027). Needs consent-first design. |
| R9 | Resale / recycling margin and EPR service fees | Buyers, producers | Take rate, per kg or per unit | Contested EPR price (₹10–50/kg range) | 3 | Logistics-heavy, so treat as a vision. |

**Not modelled:** payment processing. UPI MDR of 0.4% above ₹2,000 (cap ₹300) takes effect 15 Oct 2026, but small-merchant QR up to ₹1 lakh/month stays at zero. There is no margin here.

### Illustrative unit economics for R1 (🔴)
- An agency doing 3 jobs/day × 25 days = 75 jobs/month × ₹40 = ₹3,000/month, about ₹36,000/year per agency.
- 1,000 agencies ≈ ₹3.6 Cr/year. 10,000 agencies ≈ ₹36 Cr/year. Add R3–R6 and the stacked ceiling in the earlier problem map was about ₹110–115 Cr under its stated assumptions.
- These figures assume that the agency count exists and that agencies do 3 jobs a day. Neither is sourced. The first pilot should measure real jobs per agency.

### Revenue ladder
1. **Month 0–6:** R1 only. Prove a fee that is clearly below the agency's value from one saved revisit.
2. **Month 6–12:** add R3 and R4 on top of the records.
3. **Year 2:** R5 and R6 with one or two administrator/OEM partners.
4. **Year 3+:** R8 and R9.

---

## 6. Competition in one view

- 🟡 **Servify** (FY25 revenue ≈₹781 Cr, loss ₹85 Cr; figures conflict across years) is the main threat from the administrator side. It is B2B and metro/OEM-oriented.
- 🟡 **Urban Company** (FY26 revenue ≈₹1,555 Cr) is strong in metros. It doesn't serve Tier 2/3 agencies as its own network.
- 🟡 **ServiceOnDoors** is expanding into Tier 2/3. It is a service marketplace, not an agency tool.
- **Field-service software** (Bernard, Fieldproxy) is English-first and generic.
- **Whitespace** (absence of evidence, not proof): a vernacular, WhatsApp-first agency desk; a consumer record with traction; Indian warranty-complaint help; AI grading of large appliances.
- **Moat:** agency-side data, record linkage, vernacular speech data and partner agreements. It is not the Gemini model.

---

## 7. Google stack (for the buildathon)

- **Models:** Gemini Flash-class for extraction and quoting. Mumbai in-region is verified for `gemini-3.5-flash`, `3.5-flash-lite` and `2.5-flash`. Pro-tier is out-of-region and should be opt-in with redaction.
- **Voice:** Release 1 is transcribe-then-extract. Chirp 3 hi-IN is GA. te-IN and ta-IN are preview, and only in US/EU regions, so use them with explicit consent.
- **Vision:** invoice and label photos go to Gemini. Document AI generative extraction is English-only and not in Mumbai, so don't rely on it for Indian invoices.
- **Agents:** ADK on Cloud Run, with Antigravity and Agent Skills for the build. Keep Managed Agents out of the tenant data path.
- **Retrieval:** Postgres + pgvector + `text-embedding-005`. File Search is prototype-only.
- **Confirm before locking:** model names (Vertex vs AI Studio conflict) and prices.

---

## 8. Risks and what to validate first

1. **Do agencies pay ₹40 or ₹100 per fix?** Run a paid pilot with 15–20 agencies and measure cost per job.
2. **Does vernacular voice work?** Test Hindi, Telugu, Tamil and Kannada on real field recordings.
3. **Revisit rate and quote time.** The core benefit claim in P1 has no measured figure.
4. **Administrator and OEM interest.** Two interviews before building C.
5. **Plan-selling rules.** Confirm what licensing or rules apply to R3.
6. **Safety.** The hard-stop list needs review by an electrician or appliance safety expert.
7. **Privacy.** Records, invoices, voice and photos are personal data. Consent is a design requirement, DPDP Rules were notified 14 Nov 2025, main duties around May 2027.
8. **Claims in the one-pager still unverified:** "Right to Repair portal opens info" and "over 90% grey market".
9. **No agency-count or Tier 2/3 share figures were found.** Get them from interviews, CEAMA, or distributor data.

## 9. Recommendation

Start with Scenario A in 1–2 Tier 2 cities, sold per fix to agencies, with the household record created as a by-product. Use the pilot to prove R1, then add B and C. Pitch the larger vision (circular, data) as direction, not as present revenue.
