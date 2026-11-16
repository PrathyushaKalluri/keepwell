# Repo reconciliation — what the team repo changes
**Reference document used by every step.**
**Tags:** **[Real]** = case-competition build, research or survey · **[repo]** = team repo `ESFS/keepwell/` · **[Story]** = assumed backstory or pilot fact · **[Model]** = modelled number.
**Plan:** [`../pitch_bible.md`](../pitch_bible.md) · **Model:** [`../keepwell_model.xlsx`](../keepwell_model.xlsx)

Read on 16 Nov 2026 (`ESFS/keepwell/`).
**Source:** the full read of the team repo. Every file was read; `Keepwell feature specification.md` is the three `spec_parts` files joined together.
**Status:** Step 1 items APPLIED 16 Nov. Model cost items applied 16 Nov. Market and pricing items will be applied in Steps 4 and 7. Items marked ❓ need a decision from the team.

### A. Changes to the step structure
| Step | Change |
|---|---|
| 5 Product, fit, competition | **Adds three things:** (i) a technology and AI stack decision, (ii) trust and safety design (the human approval tiers and the hard stops on gas and high-voltage work), (iii) the North Star metric and its guardrails |
| 6 Pilot traction | **Becomes "Traction and validation plan".** The repo has no pilot data, and Stage 2 is about proving the model. The step shows (i) the pilot results we assume and (ii) the experiments the seed pays for, with kill conditions |
| 10 Compliance and data room | **Becomes "Compliance, trust and data room".** It adds data protection (DPDP) roles and dates, where data is stored, rules on selling plans (IRDAI), e-waste rules for refurbishers, the line between helping with claims and giving legal advice, and the responsible-AI controls |
| 12 Storyboard and red-team | **Adds a risk register drawn from the repo:** price rises in AI models, speech-recognition accuracy, invented fields, prompt injection, and the risk that agencies won't pay per fix |
| Roadmap, across all steps | **Order changes to match the repo:** Circuit → Home Memory with Plans → Claims triage → Parts → Resale & Recycling → Data Services. Claims triage is missing from the draft, and the repo puts it before Parts |

### B. Step 1 changes
1. **The mission wording "diagnose".** The spec forbids a final diagnosis: *"rank likely faults and say what to check"*. The likely faults are a private hint for the technician and are never shown to the customer as fact. Change to "**prepare every visit: rank the likely faults and the part to carry before anyone travels**".
2. **The moat ❓.** The repo rates diagnosis on its own as copyable. Bernard (US) already gives "a diagnosis, ranked parts and follow-up questions". Fieldproxy already "searches the business's manuals and service history and returns cited answers". What the repo rates as defensible:
   - verified repair outcomes that build up only through agency use
   - one machine's record linked across invoice, repairs, plan and EPR (competitors hold only one slice each)
   - a parts-compatibility catalogue confirmed by technicians
   - corrections to vernacular speech recognition
   - the agency network

   The learning loop is allowed only with review and consent. **Proposed restatement:** the moat is a *learning loop on verified repair outcomes*. Every fix the technician confirms teaches the engine and writes the machine's record. The model itself is not the moat.
3. **"remembered always".** This clashes with the repo's consent and retention rules. Change to "**remembered for as long as the owner wants**". Alternatively, keep the vision line and add "with consent" to the mission.
4. **Order of the agency owner's pain.** The repo scores the problems as:
   - P2, intake chaos (missed calls, mixed-language voice complaints, no job record): **24**
   - P1, an unprepared first visit: **23**
   - P3, no machine history: **22**

   No file shows agencies suffering from price disputes; the fair price is a household problem and belongs to Home Memory. So lead with **lost calls and intake chaos → blind first visits → no record**.
5. **Why now, revised:**
   - Soften the Right to Repair portal: voluntary, launched 2022 (one source says 2024), no binding law.
   - Add the DPDP Rules, notified 14 Nov 2025 with the main duties from ~May 2027. This favours a consent-first record.
   - Add that Gemini audio costs about ₹0.135 a minute against ₹1.50 on Chirp 3, and Flash-Lite prices hold through 2027.
   - Add demand for skilled AC technicians rising from ~0.37M to ~2M by 2036-37 (CEEW) and cooling demand up ~8x.
   - Add the Kigali HFC freeze from 2028, which brings a refrigerant changeover.
   - Keep the AC-ownership figures, which come from our case-competition research rather than the repo.
6. **Name ❓.** "Circuit" does not appear anywhere in the repo, which calls it "AI desk" or "Prepared Visit". Keep Circuit as the product's brand name.
7. **Positioning line from the repo** (competitive analysis): *"the machine record and pre-visit desk for India's independent appliance agencies, in their language, paid per fix that passes a test."*

### C. What the repo adds by step
- **Step 3 Ecosystem.**
  - **Government:** DoCA/CCPA, the National Consumer Helpline (20.49 lakh complaints in FY26, ~30% via WhatsApp), the CPCB EPR portal (8,940 producers, 374 recyclers, 107 refurbishers), a BEE scheme to swap ACs over 10 years old (in drafting), the NSDC skill qualification ELE/Q7201, and the DGT NSQF-4 appliance mechanic course.
  - **Industry:** Samsung's Dost programme (14,500+ engineers trained through 22 ITIs).
  - **Research:** Toxics Link (Mar 2026 repair report: over half of technicians use non-original parts), CEEW, IIT Kanpur (audio fault work), LocalCircles.
  - **Startup programmes:** Google for Startups Scale AI, up to $350k in credits, which needs institutional or VC funding. A seed round unlocks it. Our earlier list adds incubators such as CIE-IIITH and T-Hub (the repo has none).
- **Step 4 Market.**
  - **Repair market:** BlueWeave puts it at ~$981M in 2023, growing 8.18% a year to ~$1.49B by 2030. Servify's own estimate is ~$1B for on-demand repair and ~$1.1B for device protection, out of a $5.3B after-sales pie. Both corroborate ₹9,000 Cr.
  - **Extended warranty:** the ₹37,000 Cr figure becomes "USD 3.6–4.4B (upper bound; IMARC may include auto)".
  - **Unorganised share:** "~90% unorganised" becomes "80%+ (unverified)".
  - **Grey market:** ">90% grey market" is really the informal share of e-waste, not of used goods. Rewrite it.
  - **No agency count exists.** The only anchors: ~200,000 certified technicians against demand above 500,000 (unsourced); Urban Company's ~54,000 monthly active professionals across all its categories; ~150M appliances repaired a year (2017).
  - **So the SAM must be built from technicians:** technicians ÷ technicians per agency.
- **Step 5 Competition.**
  - **Threat ranking from the repo:** (1) Servify, (2) Bernard and Fieldproxy, (3) Indian voice-AI firms moving into the vertical (Hunar.AI, Ringg, Bolna, Gnani, Sarvam), (4) Samsung's in-house AI, (5) Attero and Recykal, (6) Zoho FSM as the price anchor (₹1,000–1,800 per user per month).
  - **Other Indian players:** Wiffy (AI workforce management for brands, $3M Series A, Jul 2026), ServiceOnDoors (Tier 2/3, 200+ cities), Eazzy, 247around, EasyFix.
  - **White space:** "vernacular, offline-first technician copilots" is open or thin. Dispatch SaaS and voice booking are crowded.
  - **North Star:** "Verified first-time-right jobs per active agency per month".
  - **Guardrails:** zero safety false-accepts, zero unapproved prices, a cost-per-job cap, a language gap of ≤10 points, and an override rate of 5–20%.
  - **Release order:**
    - R1: Prepared Visit core loop
    - R2: Home Memory, reminders, claim evidence pack (plans only after the licence question is answered)
    - R3: Claims triage
    - R4: Parts catalogue
    - R5: Circular (resale and recycling)
- **Step 6 Validation.**
  - **The repo's plan:** 15–20 agency interviews; a paid pilot with 3–5 agencies at ₹40 against ₹100 per fix; voice tests in Hindi, Telugu and Tamil; two administrator or OEM interviews.
  - **Primary metric:** share of jobs closed in one visit, against each agency's own past record.
  - **Kill condition:** "agencies see no cost from repeat visits or prefer them".
  - **Metrics to show:** leading (abstain rate, quote edit rate, cost per job, time to close-out) and lagging (revisit rate, retention, jobs per agency, NPS).
- **Step 7 Economics.**
  - **Cost per job by profile** (simple / parts-needed / warranty claim), total AI and non-AI:
    - Flash at 2027 prices: ₹4.03 / 7.17 / 9.77
    - Lite with caching: ₹1.45 / 2.60 / 3.15
  - **Gross margin:** worst case 75.6% at ₹40 per fix; above 90% in every case at ₹100. These are variable-cost margins only.
  - **The repo's verdict:** "the binding risk is whether agencies pay, not token cost."
  - **Comparison point:** Urban Company takes 28.3% of what its professionals earn. ₹40 on a ₹500–1,000 job is 4–8%, a strong pricing story.
  - **Revenue streams to add:** R5 claims triage at ₹25–100 per claim, or a ₹40–60L a year licence; R6 lead routing at ₹100–250 per job; R7 an optional household premium at ₹199–499 a year.
- **Step 8 Funding.**
  - **What the money buys** (named in the spec): golden test sets (150–300 min of audio, 450 photos, 420 retrieval cases, an 800-message hazard set), a ~600-row vernacular lexicon, a ~400-term hazard lexicon with sign-off from a safety expert, ~150 manuals (top 10 brands × 7 appliances), warranty terms for the top 12 brands, red-teaming, legal review, and the foundations (consent, cost ledger, eval harness, admin console).
  - **Roles named:** AI lead, safety lead (external), lawyer, eval owner, site reliability, security, platform, ops, claims lead, data protection officer, product.
- **Step 9 Exit and valuation.**
  - **Acquirers:** Servify; OneAssist, Onsitego and Zopper; Asurion (bought Domestic & General for a reported £2.1bn); Urban Company; Cashify; Attero and Recykal.
  - **OEMs as acquirers are weaker:** they tend to pull service into their own networks.
  - **Comparables:** Servify (~$700M valuation, FY25 revenue ₹781 Cr); Urban Company (IPO 103.6x subscribed); Onsitego bought Qdigi; Quikr bought Zefo for ~₹200 Cr.
  - **Investors already active in the space (target list):** BEENEXT, Blume, Accel, Elevation, Titan Capital, 8i, Axilor, Iron Pillar, Prosus, 360 ONE.
- **Step 10 Compliance.**
  - **DPDP roles:** the agency is the data fiduciary and Keepwell the processor. Keepwell becomes a fiduciary if it uses the data for its own purposes. Duties apply from ~13 May 2027; breach reports within 72 hours; logs kept for one year.
  - **Where data is stored:** Mumbai (asia-south1). The Telugu/Tamil speech service (Chirp 3) runs only in the US and EU, so it needs consent. Claim wording: "hosted in Mumbai with security safeguards", not "DPDP compliant".
  - **Extended warranties are insurer-filed products** (IRDAI). Service Plans must be sold for licensed insurers or administrators, on commission.
  - **Other rules:** refurbishers must register with CPCB; CCPA rules on dark patterns; joint liability under the Consumer Protection Act; claim help is an "evidence pack, not legal advice" (the FTC fined DoNotPay $193k).
  - **Not covered:** ISO 27001 / SOC 2 (Servify advertises SOC 2 Type II).

### D. Model input changes (keepwell_model.xlsx)
| Input | Draft | Repo says | Proposed |
|---|---|---|---|
| Pricing | ₹999/month + ₹40 per fix | Pay per job, not per seat. Subscription quoted as ₹300–500 (R2) or ₹1,500 (problem map) | ❓ Per fix only (₹40, test ₹100) plus an optional ₹300–500 desk fee |
| Fixes per agency per month | 75 jobs × 80% = 60 | Problem map: 100 (small) / 250 (mid) | ❓ Two agency sizes, blended |
| AI cost per job | ₹5.5 | 2027 Flash: ₹3.4–8.7 (AI only) | Blended ₹5.5, with the worst case (₹9.77 total) as a sensitivity |
| Messaging per job | ₹2.0 | ₹0.35–0.92 before GST and provider markup | ₹1.2 |
| Cloud and tools, Y1 | ₹12L | ₹1.4–4.2L a year all-in for the pilot | ₹6L, offset by Google credits |
| Resale deal value | ₹9,000 | Scrap and exchange ₹800–5,000; refurbished units sell 50–70% below new | ₹5,000 |
| Agency market | 150,000 agencies | No count exists | Build from technicians: ~200k certified technicians ÷ ~4 per agency ≈ 50k agencies; then the Tier 2/3 share and launch-state share |
| Revenue lines | 6 | 9 (R1–R9) | Add claims triage (per claim plus licence) inside Data Services, and lead routing |

### E. Open questions this raises
1. **Which codebase is the MVP?** The repo's architecture file reads an existing TypeScript/Express build (`keepwell/shared/types.ts`, `keepwell/server/workflow.ts`) that isn't in this clone. The case-competition Circuit prototype is FastAPI with Claude. ❓
2. **Stack in the pitch:** Gemini on Vertex Mumbai, as in the repo, or Claude, as in the prototype? Nothing technical forces either. Gemini has India in-country processing commitments, and the Google credits would point to it. ❓
