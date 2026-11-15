# Keepwell: problem map, scenarios and revenue streams

*Prepared 15 Nov 2026. Starting direction: `Keepwell_One_Pager.pdf`. Evidence base: the two reports in `reports/` (domain overview; opportunities and problems) plus four new checks run for this file (Google tools, vernacular voice, UPI fees, agency counts).*

**How to read the labels.** **Sourced** = linked source. **Assumption** = my number, chosen to show the arithmetic, not a finding. **Judgment** = my scoring. Anything marked *unverified* needs a primary source or a customer interview before it goes in a pitch.

---

## 1. Bottom line

1. **Lead with the agency-side AI desk (Scenario A).** It is the only problem that scores high on impact, medium on effort, and low on build barrier at the same time, and Gemini does most of the heavy lifting. Its weak point is not technology. It is whether small agencies will pay, and whether fewer repeat visits actually appeals to them.
2. **No single problem scores "very high impact with very low barrier".** I looked for one and found none. The ones that are easy to build (intake, history, technician copilot) have modest revenue on their own. The ones with large revenue (claims, plans, buyback with EPR, parts) have a payer, a catalogue or an operations barrier. Impact only reaches "very high" when the scenarios are stacked on one machine record, which is exactly Keepwell's thesis.
3. **The revenue ceiling is set by take rate, not market size.** Under my stated assumptions the stacked scenarios reach roughly ₹100–120 Cr a year at maturity against a repair-plus-warranty pool of about ₹46,000–47,000 Cr (the one pager's figures, vendor-grade). That is about 0.2% of the pool, so there is headroom. The levers that move it are the per-fix price, parts flowing through the platform, and enterprise data fees.
4. **Three claims in the one pager need softening before a pitch.** See section 2.

---

## 2. What the one pager gets right, and what to check

**Consistent with my research**
- Repair market of ₹9,000–10,000 Cr. A vendor estimate puts India appliance repair at about USD 981M in 2023 ([BlueWeave](https://blueweaveconsulting.com/report/india-home-appliance-repair-service-market)), roughly ₹8,100 Cr at ₹83 per USD. Both are vendor-grade, so use as a range.
- Extended-warranty market of ₹37,000 Cr. Vendor estimates are USD 3.6–4.4B (IMARC, Credence), about ₹32,000–39,000 Cr. One other publisher shows USD 305B, which is almost certainly a scope or unit error.
- Positioning against Urban Company and Servify holds. Urban Company is loss-making in FY26 after its quick-service push. Servify serves brands and is protection-led (FY25 revenue about ₹781 Cr, net loss ₹85 Cr, from the earlier research).
- The one pager's own risk (a second visit earns the agency a second fee) matches what I found. No source measures repeat-visit rates, so it stays a test, not a fact.

**Check before pitching**
- **"Right to Repair portal (2022) opens repair information to independents."** The portal exists and is voluntary. Its launch date is disputed (2022 vs 2024), India has no binding right-to-repair law, and I could not confirm that manuals or parts prices are actually published there. Use it as a tailwind, not as the reason the product works.
- **"Over 90% of used goods sell through the grey market."** I did not verify this.
- **"Agencies lose no customers to us."** Untested. It is the central adoption promise, so interview agencies on it directly.
- **Payments are not a revenue line.** From 15 Oct 2026, UPI payments to merchants above ₹2,000 carry a 0.4% fee capped at ₹300, but small merchants receiving up to ₹1 lakh a month through QR stay at zero ([Business Today](https://www.businesstoday.in/personal-finance/story/upi-payments-to-remain-free-for-p2p-transactions-0-4-mdr-applicable-only-on-merchant-payments-above-rs2000-555715-2026-09-15), [Inc42](https://inc42.com/features/mdr-on-upi-is-here-but-who-foots-the-bill/)). The merchant pays it, so for larger agencies it is a cost, not a Keepwell earning. The one pager correctly does not count payments as revenue.
- **Agency count is unknown.** I found no reliable national count of repair shops or technicians. The nearest figure is about 200,000 certified consumer-electronics technicians against demand above 500,000, from an unsourced market-research page ([Ken Research](https://www.marketresearch.com/Ken-Research-v3771/India-Consumer-Electronics-Repair-Economy-42966709)). So the sizing below is built per agency and scaled by assumed counts.
- **A build already exists** in `keepwell/` (a Vite front end with an Express server and SQLite). I listed its structure but did not review the code, so effort scores below assume the core agency and household flows are partly done.

---

## 3. Problem map

Evidence strength is carried over from the two reports. "In Keepwell" shows where the one pager already covers it.

| # | Problem | Who suffers | Evidence | Already attempted by | In Keepwell? |
|---|---|---|---|---|---|
| P1 | Unprepared first visit: wrong diagnosis, wrong part on the truck, repeat visits | Agencies, households | Qualitative. No measured repeat-visit rate found | OEM remote diagnostics (Samsung, GE); US tools (Bernard, Revin, Bruviti) sell to OEMs and repair firms, not Indian agencies | Yes: AI Agent for Agencies |
| P2 | Complaint intake chaos: missed calls, mixed-language voice complaints, no job record | Small agencies | Anecdotal. Voice AI for Indian languages now exists (section 6) | None found for appliance agencies | Yes: part of the agent |
| P3 | No machine history: lost invoices, unknown warranty status, no repair record | Households | Anecdotal | Warranty apps from brands and administrators | Yes: Home Memory |
| P4 | Warranty refusal and unresolved claims | Households | Self-selected poll: 55% had a defective high-value product in warranty, only 21% of those who acted got a refund or replacement. Court awards small (₹5–25k) | Consumer courts, helpline; no startup found | Partly: Home Memory chases providers |
| P5 | No fair-price benchmark: overcharging, misdiagnosis | Households | Self-selected poll: 76% of AC owners avoid brand service, about two in three say it costs 50% or more above local vendors | None neutral found | Partly: agreed prices |
| P6 | Wrong or unavailable spare parts; no model-to-part mapping | Agencies, independents | Toxics Link: over half of technicians use non-original parts. No appliance counterfeit data | Parts e-commerce (SOS Accessoire in France); no funded Indian equivalent found | Yes: Parts Marketplace |
| P7 | Claims triage and repair-network quality for protection and OEM networks | Administrators, OEMs | Documented market (Servify, OneAssist, Onsitego), but no fraud or network-quality data found | Polygrade (US, claims automation) | Yes: Data Services |
| P8 | Low plan uptake and renewals; warranty-market uptake in low single digits | Households, plan sellers | One pager figure; renewal reluctance seen in solar maintenance (CEEW) | Servify, Onsitego, Zopper, OneAssist | Yes: Service Plans |
| P9 | Old-appliance exit: informal buyback, no triage into refurb, harvest or scrap | Households, refurbishers, recyclers | Informal share estimates conflict (75% to over 90%) | Attero exchanges (scrap-route valuation), Costify, Underdog (France) | Yes, Year 3 |
| P10 | Technician skills gap on inverter and PCB repair | Technicians | Qualitative only (Toxics Link, employer job ad) | Private PCB courses, OEM academies | No |
| P11 | EPR compliance and traceability for OEMs | OEMs, importers | Rules documented; price floor stayed in court (Jan 2026), no final judgment found | Recykal, Attero | Later |
| P12 | Safety (gas geyser CO), informal-worker transition, refrigerant leakage | Public | No national statistic for geyser deaths. India has no refrigerant-recovery mandate in practice | Pilots only | Safety escalation only |
| P14 | Technician lead generation and income volatility | Independent technicians | Beauty-sector protests documented, appliance-specific thin | Urban Company, Wiffy ($3M Series A, July 2026) | No |

---

## 4. Scoring and the impact-effort matrix

**Rubric (all judgment, 1–5).**
- **Impact (I):** revenue ceiling and evidence that someone pays. 5 means very high.
- **Effort (E):** work to reach a credible paid pilot. 1 is light, 5 is very heavy. Target is 2–3.
- **Feasibility barrier (BF):** how hard to build and ship (data, hardware, licences). 5 is hardest.
- **Penetration barrier (BP):** how hard to win the first 100 paying customers (payer, behaviour change, sales cycle, incumbents). 5 is hardest.
- **Google leverage (G):** how much Google models and tools carry the product. 5 means they do the heavy lifting.
- **Priority = 2×I + G + (6−E) + (6−BF) + (6−BP).** Maximum 30. Impact is double-weighted because you asked for very high impact.

| # | Problem | I | G | E | BF | BP | Priority |
|---|---|---|---|---|---|---|---|
| P2 | Vernacular intake and job record | 3 | 5 | 2 | 1 | 2 | **24** |
| P1 | Prepared first visit | 4 | 5 | 3 | 2 | 3 | **23** |
| P3 | Machine history and warranty record | 3 | 5 | 2 | 2 | 3 | 22 |
| P7 | Claims triage for administrators and OEMs | 4 | 5 | 3 | 2 | 4 | 22 |
| P10 | Technician copilot | 2 | 5 | 2 | 1 | 3 | 21 |
| P4 | Warranty claim resolution | 4 | 4 | 3 | 3 | 4 | 20 |
| P5 | Fair-price benchmark | 3 | 4 | 2 | 3 | 3 | 20 |
| P8 | Plan renewals | 4 | 3 | 3 | 3 | 3 | 20 |
| P6 | Parts fitment and marketplace | 4 | 3 | 4 | 4 | 3 | 18 |
| P9 | Triage-based buyback | 4 | 4 | 4 | 4 | 4 | 18 |
| P11 | EPR traceability for OEMs | 4 | 3 | 4 | 4 | 5 | 16 |
| P14 | Technician lead-gen marketplace | 3 | 2 | 3 | 2 | 5 | 16 |
| P12 | Safety, worker transition, refrigerant | 2 | 2 | 4 | 4 | 5 | 11 |

**Impact-effort grid** (problem IDs placed by Impact and Effort; the target zone is Impact 4 or more, Effort 3 or less).

| Impact \ Effort | 1 | 2 | 3 (target limit) | 4 | 5 |
|---|---|---|---|---|---|
| **5** | | | | | |
| **4** | | | **P1, P4, P7, P8** (target zone) | P6, P9, P11 | |
| **3** | | P2, P3, P5 | P14 | | |
| **2** | | P10 | | P12 | |

**Reading the grid.**
- Nothing sits at Impact 5. The market evidence supports 4 at most for any single problem.
- Four problems land in the target zone: **P1, P4, P7, P8**.
- Add the barrier test and the list narrows. **P1 and P8** have a penetration barrier of 3. **P4 and P7** score 4 because the payer is unproven (P4) or it is enterprise sales (P7).
- Strictly "very low barrier" (BF and BP both 2 or less) is only **P2**, which is a feature of P1 more than a business.
- So the practical choice is **P1 bundled with P2 and P10 as the entry**, then P3 and P8 around it.

---

## 5. Scenarios, revenue streams and sizing

All money figures below are **assumptions** unless a source is shown. They exist to show the arithmetic and which lever matters. Replace them with pilot data.

### Scenario A: Prepared Visit (agency AI desk). The entry wedge
**Problems solved:** P1, P2, P10. **Payer:** repair agencies.

**What it is.** The agent takes the complaint in text or voice (Hindi, Telugu, Tamil, English), reads the machine's record, names likely faults with evidence, and sends a technician-ready job card including candidate parts. Part compatibility is only claimed when a structured catalogue confirms it, otherwise the card says "not verified, inspect first". Safety complaints (burning smell, shock, gas) stop normal troubleshooting and escalate.

**Revenue streams**
| Stream | Basis | Status |
|---|---|---|
| Desk fee | ₹1,500 per agency per month | One pager |
| Per verified fix | ₹40 per passed test (pilots test ₹40–100) | One pager |
| Parts margin, later | About 8% of parts bought through the platform | One pager, Year 1–2 |

**Sizing (assumptions: small agency 100 verified fixes a month, mid agency 250).**
- Small agency at ₹40: ₹1,500 + ₹4,000 = ₹5,500 a month, about ₹0.66 lakh a year.
- Mid agency at ₹40: ₹1,500 + ₹10,000 = ₹11,500 a month, about ₹1.38 lakh a year.
- Blended about ₹1.0 lakh per agency per year at ₹40 a fix.

| Agencies | Annual revenue at ₹1.0 lakh each |
|---|---|
| 120 (Keepwell Stage 3 target) | about ₹1.2 Cr |
| 1,000 | about ₹10 Cr |
| 5,000 | about ₹50 Cr |

- **Biggest lever: price per fix.** At ₹100 a fix a mid agency pays ₹26,500 a month, about ₹3.2 lakh a year, 2.3 times the ₹40 case.
- **Second lever: parts.** If an agency routes ₹1 lakh a month of parts through the platform (assumption), 8% adds ₹8,000 a month, nearly doubling revenue per agency. It is also the stream with the highest build barrier (P6), so treat it as phase 2.
- **Unit-economics check.** The ₹40 fee must cover Gemini text, voice and image calls on every job. I have not verified current model pricing. Measure cost per job in the first pilot before committing to ₹40.

**Impact-effort:** I 4, E 3, BF 2, BP 3, G 5. **Priority 23.**
**Why the barrier is low:** free for 60 days, pay only on a passed test, no hardware, no licence. **What could break it:** the one pager's own risk, plus no evidence yet that small agencies pay for software. I found none either way.

### Scenario B: Prepared Visit plus Home Memory plus Plans. The two-sided record
**Problems solved:** A's, plus P3, P5, P8. **Payers:** agencies first; plan revenue shared.

**Added streams**
| Stream | Basis |
|---|---|
| Plan commission | 15% of yearly service-plan revenue (one pager) |
| Household referral to agency | Free for households; leads fund A's retention (not directly charged) |
| Retention and price power | Verified history lets A hold a higher per-fix price (inference) |

**Sizing for plans (assumptions: 3 appliances per household, 5% plan attach, ₹2,000 a year per plan).**
| Households | Appliances | Plans at 5% | Plan revenue | Keepwell 15% |
|---|---|---|---|---|
| 40,000 (Stage 3 target) | 120,000 | 6,000 | ₹1.2 Cr | about ₹18 lakh |
| 500,000 | 1.5M | 75,000 | ₹15 Cr | about ₹2.3 Cr |
| 2,000,000 | 6M | 300,000 | ₹60 Cr | about ₹9 Cr |

- **Honest reading.** Plans alone are small. Home Memory's value is the data moat and retention for A, which the one pager also says (it is free and "feeds every other product").
- **Cold-start risk.** Households do not install apps for fun. Seed the record from the agency's own jobs (every repair creates a record), not from consumer downloads.
- **Check:** whether agencies can sell their own annual service contracts directly, and whether insurer-backed plans need a partner licence. I did not research the rules.

**Impact-effort:** I 4, E 4 (two more surfaces, though partly built), BF 2, BP 3, G 5. **Priority 22.**

### Scenario C: Claims and first-visit triage for protection and OEM service networks
**Problems solved:** P7, with P1 reused. **Payer:** warranty administrators, protection firms, OEM service heads.

**Reuses Scenario A's engine** on claims instead of agency jobs: classify the claim, retrieve the machine record, flag likely repeat failures, and prepare the field visit.

**Revenue streams**
| Stream | Basis |
|---|---|
| Per-claim fee | Assumption: ₹25 per triaged claim |
| Platform licence | Assumption: ₹40–60 lakh a year for a mid-size administrator |
| Data services subscription | One pager Year 3: verified warranty claims, repeat-failure data, parts-demand forecasts |

**Sizing (assumption).** One customer handling 200,000 claims a year at ₹25 pays ₹50 lakh. Ten customers is about ₹5 Cr.
**Market context (sourced):** Servify FY25 revenue about ₹781 Cr, OneAssist about ₹623 Cr (conflicting figures across sources), so a small number of buyers carry large claim volumes. That is also why the sales cycle is long.

**Impact-effort:** I 4, E 3, BF 2, BP 4, G 5. **Priority 22.**
**Why not first:** the buyer is enterprise, procurement is slow, and you need agency-side proof from Scenario A to sell it. Best as a year-2 lane once A has produced verified outcomes.

### Scenario D: Consumer claim and fair-price advocate
**Problems solved:** P4, P5, with P3. **Payer:** unproven.

Households upload an invoice and a complaint. The product checks warranty status, drafts the demand or complaint, and benchmarks the quote.

**Revenue streams**
| Stream | Basis |
|---|---|
| Success fee | Assumption: 10% of recovered value, average recovery ₹15,000 (court awards run ₹5–25k, one AC refund was ₹1.14 lakh), so about ₹1,500 per claim |
| Referral to agencies | Indirect |

**Sizing (assumption).** 5,000 claims a year at ₹1,500 is about ₹75 lakh.
**Reading.** Strong evidence of pain, weak evidence of willingness to pay. Treat it as an acquisition channel for Scenario B, not a standalone business.

**Impact-effort:** I 3, E 3, BF 3, BP 4, G 4. **Priority 18.**

### Scenario E: Triage-at-pickup circular loop (buyback, refurb, EPR)
**Problems solved:** P9, P11, parts harvesting from P6. **Payers:** refurbishers, recyclers, producers.

A household uploads photos of an old unit. Gemini vision grades it as refurb-grade, harvest-for-parts or scrap, and routes it to the right partner at a fair price, capturing provenance.

**Revenue streams**
| Stream | Basis |
|---|---|
| Resale commission | About 4% of each sale (one pager) |
| Refurb lead fee | Assumption: ₹300–500 per refurb-grade unit |
| EPR-linked collection fee | Certificate prices run ₹10–50 per kg with a contested ₹22 per kg floor. For a 50 kg unit (weight assumption) that is ₹500–2,500, and a platform share of 10–20% is ₹50–500 per unit |

**Reading.** The largest ceiling in the map, because it stacks resale, EPR and parts harvest. It is also the heaviest to operate (pickups, partners, warranty on refurbished units) and exposed to the Delhi High Court outcome on the price floor. No appliance refurbisher publishes unit economics, so the numbers are unproven.

**Impact-effort:** I 5 (ceiling, not near-term), E 5, BF 4, BP 4, G 4. **Priority 19.**
**Where it fits:** the one pager already puts it in Year 3. Keep it as the vision and the reason the record matters.

### Scenario comparison

| Scenario | Combines | I | G | E | BF | BP | Priority | Earliest realistic revenue |
|---|---|---|---|---|---|---|---|---|
| **A. Prepared Visit** | P1, P2, P10 | 4 | 5 | 3 | 2 | 3 | **23** | Pilot now |
| **B. Two-sided record** | A + P3, P5, P8 | 4 | 5 | 4 | 2 | 3 | 22 | Year 1–2 |
| **C. Claims triage (B2B)** | P7 + A's engine | 4 | 5 | 3 | 2 | 4 | 22 | Year 2 |
| **E. Circular pickup** | P9, P11, P6 | 5 | 4 | 5 | 4 | 4 | 19 | Year 3 |
| **D. Consumer advocate** | P4, P5, P3 | 3 | 4 | 3 | 3 | 4 | 18 | Unclear |

**Stacked ceiling (assumptions, not a forecast).** Scenario A at 5,000 agencies about ₹50 Cr, A's parts stream at the same scale about ₹48 Cr, B's plans at 2 million households about ₹9 Cr, C at ten customers about ₹5 Cr. That totals roughly ₹110–115 Cr a year. It is a seed-to-Series-A scale story on these numbers, and it grows mainly if per-fix pricing becomes value-based, parts flow through, or brands and insurers pay for the data.

**Recommended sequence:** A now, B as the 12-month expansion, C as the year-2 enterprise lane, D folded into B as a feature, E as the stated vision.

---

## 6. How much Google can carry

**Buildathon submission requires** naming the Google AI tools (AI Studio, Antigravity, Agent Skills) and the Google models used (from the Idea Submission instructions).

**What the current evidence supports** (Google I/O 2026 coverage; third-party blogs vary, so check official docs before quoting).
- **Antigravity 2.0** launched at I/O in May 2026 as a desktop app, CLI and SDK, with Managed Agents in the Gemini API, and AI Studio projects can export into it ([Google blog](https://blog.google/innovation-and-ai/technology/developers-tools/google-io-2026-developer-highlights/), [TNW](https://thenextweb.com/news/google-antigravity-2-desktop-cli-sdk-io-2026)). Managed Agents and Live API items are preview.
- **Agent Skills.** Antigravity reads Markdown `SKILL.md` skills (same coverage).
- **Models.** Gemini 3.5 Flash is reported as the default. A Thai-language Google page says Gemini 3.8 Flash, so the version conflicts. Confirm the model names in AI Studio before the deck.
- **Voice.** Google's Live translate model lists Hindi, Tamil and Telugu ([Google Cloud docs](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/gemini/3-5-live-translate)), and Firebase's Live API page lists Tamil and Telugu locales ([Firebase](https://firebase.google.com/docs/ai-logic/live-api/limits-and-specs)). I could not retrieve the official per-language tables. Test accuracy on noisy phone-line repair complaints in a pilot, since vendor language lists do not prove that.

| Google piece | Used for | Scenarios |
|---|---|---|
| **AI Studio** | Prototype prompts and structured-output schemas, run evals before coding, export to Antigravity | All |
| **Antigravity** | Build the agency, household and technician workspaces with agents | All |
| **Agent Skills** | Package reusable skills: safety escalation, job-card generation, part-compatibility check (catalogue only), warranty eligibility, quote explanation | A, B, C |
| **Gemini (Flash tier for intake, a Pro-tier model for harder diagnosis)** | Multimodal complaint understanding from text, voice and photo, evidence-grounded fault hypotheses | A, B, C, D |
| **Gemini Live API / Chirp speech** | Vernacular voice intake and technician voice notes | A, B |
| **Document AI** | Read invoices into the machine record | B, D |
| **Retrieval over manuals** (Vertex AI Search or similar) | Ground answers in service manuals instead of model memory | A, C |
| **Maps Routes API** | Technician matching and pickup batching | A, E |
| **Gemini vision** | Grade old appliances from photos | E |
| **Cloud Run and Firebase** (suggestion) | Run the backend on Google Cloud. The build brief says Lovable Cloud and the existing build uses Express and SQLite, so moving server pieces to Google Cloud would strengthen the Google-fit story | All |

**Things Google does not give you.** WhatsApp intake needs the WhatsApp Business API, which is not a Google product. Importing invoices from Gmail requires restricted-scope verification, so start with upload and Document AI. Verified part compatibility needs a real catalogue, not a model.

---

## 7. Entry barriers, split as you asked

**Feasibility (can we build it?)**
- Low for A, B, C: all software on Gemini, no hardware, no licence.
- Medium for D (legal drafting, helpline and e-filing access).
- High for E (partner operations) and parts (catalogue).
- Rule from the brief that should stay: never let the model declare a part compatible. Verify against a catalogue built from technician-confirmed repairs.

**Market penetration (can we get paying customers?)**
- A: pay-per-passed-test and 60 free days lower the risk. The unknown is whether agencies value fewer trips. Test it first.
- B: cold-start on the consumer side. Seed households from agency jobs.
- C: slow enterprise sales; needs outcome proof from A.
- D: payer unproven.
- E: needs partners on both sides before the first sale.
- Data law: household data needs consent handling under India's DPDP Act. I did not check the current rules status.

---

## 8. What to validate first (before building more)

1. **Interview 15–20 agencies.** Ask what they pay for today, how many verified fixes a month they do, what a repeat visit costs them, and whether a lower trip count helps or hurts. This settles A's price and the one pager's central risk.
2. **Run a paid pilot with 3–5 agencies at ₹40 and ₹100 per fix.** Measure Gemini cost per job against the fee.
3. **Test voice accuracy** on real recorded complaints in Hindi, Telugu and Tamil.
4. **Ask two warranty administrators or OEM service heads** what a triaged claim is worth to them (Scenario C).
5. **Confirm the plan-selling rules** with someone who knows IRDAI and service-contract law before promising 15% plan revenue.

## 9. Gaps in this file

- No agency count; all sizing is per agency and assumption-driven.
- No appliance repair-visit, repeat-visit or first-time-fix rate for India.
- No willingness-to-pay data from agencies, households or administrators.
- Gemini pricing and the exact current model names were not verified.
- The existing `keepwell/` build was not reviewed.
- Everything from the two earlier reports keeps its original caveats (mostly search-summary evidence, conflicting market sizes, the unresolved Delhi High Court EPR ruling).
