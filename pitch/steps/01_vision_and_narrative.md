# Step 1 — Vision and narrative spine
**Phase A: Who we are · Status: LOCKED 16 Nov 2026**
**Tags:** **[Real]** = case-competition build, research or survey · **[repo]** = team repo `ESFS/keepwell/` · **[Story]** = assumed backstory or pilot fact · **[Model]** = modelled number.
**Plan:** [`../pitch_bible.md`](../pitch_bible.md) · **Model:** [`../keepwell_model.xlsx`](../keepwell_model.xlsx)


### 1.1 Names
- **Keepwell** is the company.
- **Circuit** is product 1: the AI agent for repair agencies. It is the MVP we built.
- **Mistri Gyan** is the shared fault library the agent learns into. **[Real]** (the name exists in the build)
- **Machine Kundli** is the per-machine record. **[Real]** In the pitch it surfaces as product 2, **Home Memory**.

**Sources for direction:** `ESFS/keepwell/` (team repo, cloned 15 Nov 2026). It frames Keepwell as one AI care engine with one module per scenario:
- **A**, Prepared Visit: the Circuit agency desk
- **B**, Home Memory and plans
- **C**, claims triage for plan administrators and OEMs
- **D**, a consumer fair-price and claim helper, folded into B
- **E**, circular resale, recycling and EPR
- revenue streams R1–R9

### 1.2 The idea the company is built on: care across the whole life of a machine
Every machine a home owns lives one life: **bought → used → fails → repaired → maintained → resold → recycled.**

Today every stage starts from zero, because nobody holds the machine's history:
- the technician arrives blind
- the warranty can't be proven
- the plan is sold to the wrong home
- the resale buyer can't trust the unit
- the recycler gets it too early

**Keepwell holds one living record per machine and puts a product at every stage of its life.**

Release order follows the repo's build order (spec §9.1 and the revenue file's ladder). The reasoning: R1 creates the data and the agency network, R2 links the household, R3 earns from both at scale, and the circular lines stay as vision because they need heavy logistics and EPR pricing is still contested (Delhi HC stay on the ₹22/kg floor).

| Release | Life stage | Keepwell product | Who pays (repo revenue stream) |
|---|---|---|---|
| R1 (now) | Fails / repaired | **Circuit**: the AI desk for repair agencies (the MVP) | agencies: per verified fix (R1), optional desk fee (R2) |
| R2 (~12 months) | Owned / maintained | **Home Memory + Service Plans**: the free machine record, reminders, claim evidence pack, then plans and AMCs once the IRDAI licence question is answered | plan providers and insurers, on commission (R3); optional household premium (R7) |
| R3 (year 2) | Claims | **Claims triage**: the first Data Services product, for warranty administrators and OEMs | per claim or licence (R5); service-lead routing (R6) |
| R4 | Repair supply | **Parts Marketplace**: a parts catalogue confirmed by technicians, plus referrals | parts sellers (R4) |
| R5 (vision) | Resold / recycled | **Resale & Recycling**: grading, refurbish/harvest/scrap routing, EPR hand-off | buyers, producers, recyclers (R9) |
| Phase 3 | All stages | **Data Services, insights layer**: repeat-failure and parts-demand data, consent-first | brands, insurers (R8) |

**The analogy for investors:** what CIBIL is to a borrower and Carfax is to a used car, Keepwell is to a household machine. It is the trusted history that every transaction about that machine checks first.

### 1.3 Company vision — LOCKED
> **Every machine an Indian home owns is cared for across its whole life: repaired right, remembered always, and never wasted.**

- End-state line for the closing slide: *"Keepwell is the record everyone checks before touching a machine."*
- Tagline under the logo: **"The care layer for everything a home owns."** (repo: the Keepwell vision)

### 1.4 Company mission — LOCKED
> **Build India's trusted record for household machines, and the services that run on it. With every owner's consent, we connect households, repair agencies, parts sellers, brands, insurers and recyclers, so every repair, plan, resale and recycling decision starts from the truth instead of from zero.**

"With every owner's consent" was added so the mission matches the repo's consent-first design: purpose-bound consent, withdrawal, retention limits, DPDP.

### 1.5 Why we start with Circuit
- **Product vision (Circuit):** *Every repair visit arrives prepared.* This matches the repo's scenario name, "Prepared Visit".
- **Product mission (Circuit):** *Find the likely root cause and the part to carry before anyone travels, learn from every verified repair outcome, and write it into the machine's record.*
- **Product principle (repo spec):** *"AI reads and drafts; rules decide anything with money, safety or legal effect."*
- **North Star (repo spec §3):** **verified first-time-right jobs per active agency per month.**

Why repair is the entry point:
1. **It is the moment of highest pain.** A broken machine is when a household needs help and an agency earns money.
2. **It creates the truth.** A repair is the only time someone opens the machine and records what is really wrong: model, serial, fault, part fitted. The spec's step A14 "Fix verified" writes this to the record.
3. **The payer is there.** In the repo's priority scores, agency problems P1/P2 rank highest, and agencies can pay per job. Households stay free, so the record fills without asking them for money.
4. **It gives distribution.** Each agency brings its households. The record grows as a by-product of work the agency already does, not through data entry.

### 1.6 The moat — LOCKED: root-cause analysis + a learning loop on verified repair outcomes
- **Root-cause analysis.** From the customer's voice note and photos, Circuit ranks the likely root causes and the part to carry. It uses the machine's history, manuals and Mistri Gyan, our shared fault library. The ranking is a private hint for the technician; the customer never sees it as a diagnosis (repo spec A5).
- **The learning loop on verified outcomes.** The technician confirms what was actually wrong and what was fitted. That verified outcome goes into Mistri Gyan and into the machine's record, after review and consent, never as auto-learning (repo). So the next root-cause ranking for that model, fault and town is better.
- **Why it compounds.** Diagnosis alone can be copied: Bernard (US) and Fieldproxy already rank faults and cite manuals (repo competitive analysis). What rivals can't copy is the outcome data, which only builds up through agency use. Add to it:
  - the record linked across invoice, repairs, plan and EPR (each rival holds one slice: OEM, administrator or recycler)
  - the parts-compatibility catalogue confirmed by technicians
  - corrections to vernacular speech recognition

  A rival needs both the repairs and the history. The model itself is not the moat (repo spec §8.2).

### 1.7 Positioning of Circuit
Repo one-line positioning: *"the machine record and pre-visit desk for India's independent appliance agencies, in their language, paid per fix that passes a test."*

- **For** independent multi-brand appliance and AC repair agencies in Tier 2/3 India (owner-run, 2–10 technicians, WhatsApp and phone, no software)
- **who** lose jobs and hours to missed calls and mixed-language voice complaints that never become records, unprepared first visits, and no history of the machine,
- **Circuit is** an AI desk inside WhatsApp that speaks the customer's language (Hindi, Telugu, Tamil, Kannada, Marathi, English).
- **It** turns a voice note and two photos into the likely root cause, a quote from the agency's own rate card, and a job card with the part to carry.
- **Unlike** Urban Company, which takes the customer onto its platform and keeps 28% of the professional's earnings, generic FSM tools like Zoho that are English-first and priced per seat, or Servify, which serves brands and administrators,
- **we** make the agency the household already trusts better at its job, charge only when a fix passes a test, and get smarter with every verified repair.

### 1.8 The narrative spine — LOCKED
| # | Beat | The line to land | Fundability cell |
|---|---|---|---|
| 1 | **Hook (personal)** | Sri Charan's real line: our machines cost his family ₹10,000 a month, never evenly. **[Real]** | Startup–Potential (founder–market fit) |
| 2 | **Hook (customer)** | 46 °C in Ramagundam. A ₹350 part, a technician who has said "coming in ten minutes" since yesterday, and a son 700 km away about to buy a ₹38,000 AC. **[Real story, composite people]** | Market–Potential |
| 3 | **The real buyer's pain** | Ramesh, the agency owner, has one phone. Calls he misses and voice notes in three languages never become jobs. His technicians go in blind, and nothing about the machine is written down. (Repo P2 intake chaos 24, P1 unprepared visit 23, P3 no history 22) | Market–Quality |
| 4 | **The insight** | *Nothing in a repair can be checked*: not the price, not the part, not "job done". So people trust the **person**, not the work, and they grant more authority one good job at a time. **[Real, interviews]** | Product–Uniqueness |
| 5 | **The vision** | Every stage of a machine's life starts from zero because nobody holds its history. Keepwell is the care layer: one record per machine, with a product at every stage. "The CIBIL of household machines." | Market–Potential, Startup–Potential |
| 6 | **Where we start: Circuit** | Repair is where the pain, the payer and the truth meet. Circuit answers as the agency, ranks the likely root cause, quotes from the agency's rate card, and sends a job card with the part. The agency stays the trusted person. | Product–Potential |
| 7 | **Why it compounds** | Root-cause analysis plus a learning loop on verified outcomes. Every confirmed fix teaches Mistri Gyan and writes the machine's record. Records unlock plans → claims → parts → resale → data. | Product–Uniqueness, X-factor |
| 8 | **Proof** | MVP built, pilot and validation numbers (Step 6), economics (Step 7). | Product–Quality, Market–Quality |
| 9 | **Why us, why now, the ask** | Founders (Step 2), why now (1.10), the ask (Steps 8–9). | Startup–all, X-factor |

Sustainability runs as a secondary thread: *"A wrong diagnosis manufactures e-waste. The greenest AC is the one already on the wall."* It sets up R5.

### 1.9 Why this problem, why this solution, why us
- **Why this problem.** The after-sales economy for household machines is large and blind:
  - Repair is about ₹9,000 Cr a year. ICICI Direct, citing the Urban Company DRHP, gives ₹165–170bn for install, repair and service, about half of it repairs **[Real]**. BlueWeave gives ~$981M (2023), growing 8.18% a year to ~$1.49B by 2030, and Servify's own estimate is ~$1B for on-demand repair **[repo]**.
  - Over 80% of electronics repair is unorganised (unverified media claim) and under 1% is booked online **[case-comp research]**.
  - Extended warranty is USD 3.6–4.4B (upper bound; IMARC may include auto), with plan uptake in low single digits **[repo]**.
  - 55% of households had an inherently defective product, and only 21% of those who acted got a refund or replacement (LocalCircles, self-selected) **[repo]**.
  - Over half of technicians use non-original parts (Toxics Link, Mar 2026) **[repo]**.
  - The same gap sits underneath every market: nobody holds the machine's history.
- **Why this solution.** A shared record fixes every stage at once, and it can only be built where the truth is created: at the repair.
  - The local agency already holds the household's trust. 76% of AC owners avoid brand service (LocalCircles) **[repo]**. Local providers rose 38%→44% while platforms fell 15%→13% **[Real]**.
  - So we build the record through the trusted agency, not around it.
- **Why us.** See Step 2.

### 1.10 Why now (four tailwinds) — LOCKED
1. **Indian-language AI is now cheap enough for a 5-technician shop.**
   - Modelled AI cost is ₹1.5–5.5 per job on 2026 prices, against a ₹40 fee per fix **[repo]**.
   - Hindi speech-recognition error rate is ~14% on current frontier models **[repo]**.
   - A vernacular voice-AI ecosystem now exists (Sarvam, Gnani, Bolna, Ringg), but "no technician-focused appliance copilot" was found **[repo]**.
2. **More machines, fewer technicians.**
   - ACs per 100 Indian households tripled from 2010 to 2023, and 55% of installed ACs are under five years old **[Real, case comp]**.
   - Skilled AC technician demand rises from ~0.37M to ~2M by 2036-37, with cooling demand up ~8x (CEEW) **[repo]**.
   - Tier 3 durables sales grew 10% against 7% in Tier 1 (Q4 2024) **[repo]**.
3. **Repair is being opened up and regulated.**
   - The DoCA Right to Repair portal (launched 2022; voluntary, no binding law yet) **[repo]**.
   - A Repairability Index committee reported in May 2025 **[repo]**.
   - The Kigali HFC freeze from 2028 brings a refrigerant changeover **[repo]**.
4. **A clear rulebook for household data.** The DPDP Rules were notified on 14 Nov 2025, with the main duties applying from ~13 May 2027 **[repo]**. A consent-first record built now becomes an advantage once incumbents must retrofit consent.

### 1.11 X-factor (candidate, confirmed in Step 11)
> **We own the moment the truth about a machine is created, and we learn from it.** Circuit sits inside the agency the household already trusts. It ranks the root cause, the technician verifies the outcome, and every verified fix makes the next diagnosis better and the machine's record richer.

Who holds what today:
- Platforms (Urban Company) take the customer away.
- Administrators (Servify, OneAssist) hold only their own plans.
- OEMs hold only their own brand.
- Recyclers start only at collection.

Nobody builds the independent agency's brain or a record that follows the machine across every stage (repo: "not found in public sources", absence of evidence).

---

## Decisions log (LOCKED 16 Nov 2026)
- **Vision, mission, CIBIL/Carfax analogy, opening story, sustainability as a secondary thread:** approved by the team.
- **Moat:** RCA + learning loop on verified repair outcomes (team decision, consistent with repo §8.2 and the competitive analysis).
- **Roadmap order:** follows the repo build order (R1–R5 plus Phase 3 data insights). Claims triage is R3, the first Data Services product, because the repo calls B2B claims "the best-evidenced money".
- **Agency pain:** ordered by the repo's problem scores (P2 > P1 > P3). Price disputes moved to the household side (Home Memory fair-price view).
- **Pricing:** deferred (team decision).
- **MVP:** FastAPI + Claude Circuit prototype (team decision).
