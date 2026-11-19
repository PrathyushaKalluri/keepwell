# Step 2 — Founders and company backstory
**Phase A: Who we are · Status: LOCKED 16 Nov 2026 (timeline backdated after the team's review)**
> **Illustrative case.** Founder histories, the company timeline, the pilot results and the financials are assumptions made for the IIIT Hyderabad ESFS course pitch. They are kept consistent with the team repo and with each other. Real names are used with the founders' agreement.

**Tags:** **[Real]** = real research or build · **[repo]** = team repo `ESFS/keepwell/` · **[Story]** = assumed backstory or pilot fact · **[Model]** = modelled number.
**Plan:** [`../pitch_bible.md`](../pitch_bible.md) · **Model:** [`../keepwell_model.xlsx`](../keepwell_model.xlsx)

**How this step is built.** The course's fundability matrix (M3) gives the **Startup** category 45 of 90 points, the largest share. It scores:
- **Potential:** founders and team; business and entrepreneur experience; ability to sell the vision; capability to pivot.
- **Uniqueness:** why this team; unfair advantage; effective leverage.
- **Quality:** governance and compliance; a clean cap table; legal, HR and accounts in order; data room ready.

M1 adds that personal credibility matters more than company brand at this stage.

**The timeline rule (team decision):** we pitch the seed **now (Nov 2026)**, so the company is backdated to **May 2025**. That gives a believable path: discovery → company → prototype → angel round → paid pilot → expansion → seed. Each step takes a realistic length of time. Prior companies are fictional names, so no real company is misrepresented.

### 2.1 The three founders
| Founder | Role | Background **[Story]** | Founder–market fit (what investors hear) |
|---|---|---|---|
| **Prathyusha Kalluri** | **CEO**: strategy, fundraising, partnerships with administrators and insurers | 9 years in home services. Co-founded **FixNear** (2016), a technician-booking service in 14 Tier 2 towns across AP and Telangana: 1,200 partner technicians, ~₹11 Cr GMV at its peak. **Sold in 2022 (~₹4 Cr, mostly in stock) to a regional home-services aggregator, not a Keepwell competitor; her 2-year non-compete ended in 2024.** Then category head for appliance repair at the buyer until early 2025 | "I've built a technician network in exactly these towns, and sold it. I saw from the inside why a marketplace that takes the customer away doesn't work for the local agency. Keepwell is the opposite bet." **Business experience, selling the vision, a prior exit** |
| **Sri Charan Peri** | **CTO**: Circuit, the AI stack, eval and safety system; acting DPO | 7 years building conversational AI and speech systems for Indian languages. Lead engineer on a vernacular voice-assistant product handling ~2M calls a month. **Built the Circuit prototype himself**: FastAPI agent, 14-condition readiness gate, learning loop, Telugu voice | "Our machines cost my family ₹10,000 a month, never evenly." He lives the household side and has already shipped the agent. **Technical depth and a shipped product** |
| **Kavyanth Munagala** | **COO**: agency network, field ops, sales, parts and plans | 8 years in appliance after-sales at a large consumer-durables brand. Ran a 300+ authorised-service-partner network across South India and the warranty-claims desk for ACs and refrigerators. **At Keepwell he has personally closed 8 of the 10 agencies added since May 2026 (the other 2 came by referral), at ~25% of his time** | "I ran the brand side of this: the claims nobody can verify, the parts nobody can find. I know why the independent agency is where repair really happens." **Agency, sales, parts and warranty knowledge for R2–R4** |

**All three have been full-time on Keepwell since incorporation (May 2025).**

**What the team holds together:**
- three tiers and three languages
- a carpenter in the family running a ten-man crew that subcontracts plumbers, electricians and technicians
- *"We are the customer, and we know the people who do the work."*

**Why this combination works, in the matrix's language:**
- **Potential.** Business, tech and operations each have an owner, and there is a prior exit. The course case studies flag the opposite as a weakness (LearnEasy: "two MBAs with no coding"; PowerMF: "single founder, no startup experience").
- **Uniqueness.** One team covers the three sides Keepwell connects: household, agency network, brand and warranty.
- **Pivot capability.** FixNear began as a marketplace and moved to B2B agency supply before its sale. That is the insight Keepwell is built on.

### 2.2 Advisors and board **[Story]**, chosen to fill the gaps the repo names
| Advisor | Why (repo requirement it fills) |
|---|---|
| Former head of after-sales for an appliance brand (South India) | Claims triage (R3) buyer access; OEM manual licensing |
| Refrigeration and electrical safety expert (certified) | External sign-off on the ~400-term hazard lexicon and the safety hard-stops |
| Technology and data-protection lawyer | DPDP roles, the IRDAI plan route, the "evidence pack, not legal advice" line |
| Faculty mentor, IIIT Hyderabad (speech and language lab) | Telugu/Tamil speech accuracy (the repo's #2 risk), golden test sets |
| Incubation mentor, CIE-IIITH | Governance, compliance and data-room readiness |
| **Strategic advisors (from the seed round):** an ex-warranty-administrator executive, a parts-distribution owner, an ex-OEM service head | Doors to R2 (plans), R3 (claims) and R4 (parts). They join on **ESOP advisor grants from the 10% pool, not as investors**, which keeps the cap table clean (Step 9) |

**Board at seed (proposed):** 2 founder directors (CEO, COO), 1 investor director (the lead seed VC), 1 independent director (the after-sales expert). This mirrors the course term sheet structure.

### 2.3 Company timeline **[Story]**
| When | What |
|---|---|
| 2016–2024 | Prathyusha builds and sells FixNear (2022), then runs appliance repair at the buyer. Sri Charan builds Indian-language voice AI. Kavyanth runs a brand's service-partner network and warranty desk |
| **Jan–Apr 2025** | The three come together around one problem. Discovery: a household survey (19 responses, 12 qualified), 7 household interviews, and **18 agency-owner interviews** in Ramagundam–Peddapalli and Karimnagar (Step 6.2) |
| **May 2025** | **Keepwell Technologies Pvt Ltd incorporated** (Hyderabad). Founders put in ₹15L. Founders' agreement: 4-year vesting, 1-year cliff, IP assigned to the company. Incubated at **CIE-IIITH**; DPIIT recognised. **All three full-time** |
| Jun–Sep 2025 | **Circuit prototype built** by the CTO (FastAPI + Claude, Telugu voice, readiness gate, learning loop). 2 design-partner agencies use it free and shape it |
| **Oct 2025** | **Pre-seed: ₹30L iSAFE** from two operator angels (₹10 Cr post-money cap, 2.7). Founder stipends begin (₹50k/month each) |
| Nov 2025 | SISFS application via CIE-IIITH |
| Jan 2026 | Production moves to Gemini on Vertex AI (Mumbai) behind a model router; WhatsApp Business go-live. One contract engineer joins for 6 months |
| **Feb–Apr 2026** | **Paid pilot, 5 agencies, ₹40 vs ₹100 per verified fix.** One ₹100 agency halves its usage, so all move to ₹40 from May (Step 6) |
| Mar 2026 | **SISFS ₹20L sanctioned**; ₹10L received; ₹10L due on the 25-paying-agency milestone |
| May–Oct 2026 | **Founder-led expansion from 5 to 14 paying agencies** (Ramagundam–Peddapalli, Karimnagar, Warangal). Root-cause accuracy passes the 75% gate in August |
| Nov 2026 | Google Startup Buildathon idea submitted; team repo research completed |
| **Now (Nov 2026)** | **Raising the seed**, ~13 months after the angel round, to go from 14 to ~260 paying agencies (Step 8) |

**Why this timeline holds up:**
- **About 13 months between the angel round and the seed,** a normal gap.
- **9 months of paid usage**, including a 3-month price test and 6 months of retention data.
- The founders were full-time throughout.
- Each step follows the repo's own validation plan, done in order.

### 2.4 Money raised and how it was used
Uses the course's Product Development stage ecosystem (M1): angels, government grants, incubators, university labs, legal CS/CA.

| Source | When | Amount | Instrument |
|---|---|---|---|
| Founders' savings (incl. family support to the founders personally) | May 2025 | ₹15L: CEO ₹6L, CTO ₹4.5L, COO ₹4.5L | Equity: 15,00,000 shares at ₹1 face value, **40 / 30 / 30** |
| Pre-seed: 2 operator angels (an ex-founder from home services; an ex-head of service at a durables brand) | Oct 2025 | ₹30L | **iSAFE**, ₹10 Cr post-money cap, converts at the seed |
| Startup India Seed Fund Scheme (SISFS), via CIE-IIITH | Sanctioned Mar 2026 | ₹20L sanctioned: **₹10L received**, ₹10L on the 25-agency milestone (~Q1 2027) | **Grant** (non-dilutive) |
| **Total cash raised** | | **₹55L** (+₹10L SISFS to come) | |

**Where the money went (May 2025 – Nov 2026) [Story]:**

| Use | ₹ L |
|---|---|
| Founder stipends: ₹50k/month each from the pre-seed (Oct 2025 – Nov 2026). Before that, unpaid, living on savings; the CEO also on FixNear proceeds | 19.5 |
| One contract engineer for the production build (Jan–Jun 2026) | 6.0 |
| Cloud, AI and WhatsApp (small at pilot scale: the repo puts the pilot stack at ~₹12–35k a month) | 3.0 |
| Pilot field costs: travel, onboarding kits, agency visits | 3.0 |
| Legal: incorporation, iSAFE filings, registered valuer, trademarks | 2.5 |
| **Total spent** | **~34.0** |
| **Cash in bank now** | **~₹21L** (₹55L − ₹34L) |

**Why it's this lean:**
- The CTO built the product himself.
- AI and cloud cost little at 14 agencies.
- The founders took ₹50k stipends.

Eighteen months of progress on ₹34L is a capital-efficiency signal. The flip side, **key-person risk** (one person built everything), is answered by the contract engineer in 2026 and the six-person engineering team the seed funds.

**Why we need seed money now:**
- The angel round paid for discovery, the product and the pilot, not for scale.
- Growing from 14 to ~260 agencies needs field sales, agency success and engineers.
- Grants are capped and can't fund scale (course M2), so the scaling has to come from equity.
- The seed also unlocks Google for Startups AI-tier credits (Step 3).

### 2.5 Clean-company checklist, already in place **[Story]** (M3 "Startup–Quality", feeds Step 10)
- Incorporation papers (MoA, AoA, CIN, PAN, GST) and a statutory register
- Founders' agreement with vesting, plus IP assignment of the Circuit code and Mistri Gyan to the company
- A clean cap table: founders, plus one iSAFE that converts at the seed
- A CA/CS firm on retainer; separate bank account; monthly books; SISFS utilisation reports
- Consent records from discovery interviews, plus household consent captured in-product (74% consent rate)
- All 14 paying agencies on the standard agency agreement, which includes the de-identified-outcomes licence (Step 10.2E)

### 2.6 Pre-seed: why an iSAFE from operator angels (analysed with later rounds in mind)
**First, the terms.** "Friends and family" is a *source* of money. iSAFE is an *instrument*. So there were three options:

| | A. Friends and family, priced equity | B. Friends and family, iSAFE | C. Operator angels, iSAFE (chosen) |
|---|---|---|---|
| Typical cheque (course M2) | ₹1–10L each, so ₹30L means **3–10 people** | same | ₹10L–1Cr each, so ₹30L means **2 people** |
| What it signals to a seed VC | Founders' own network believes in them | same | **Industry insiders checked us and put money in.** Course M1: at Stage 2, strategic angels bring "industry access" and "introduce pilot customers" |
| Valuation needed then? | **Yes**, before any product existed | No | No |
| Cap table at seed | Many small voting holders, each signing every future agreement | Few, but unsophisticated holders | 2 holders who sign quickly |
| Relationship risk | High (course M2) | High | Low |
| Value beyond money | Goodwill | Goodwill | Mentoring; they introduced 3 of the 5 pilot agencies |

**What iSAFE is in India.** A US-style SAFE isn't recognised under Indian company law. The iSAFE (popularised by 100X.VC) is issued as **CCPS** that converts at the next priced round at the lower of a valuation cap or a discount.
- **One-time cost to issue:** a registered-valuer report, private-placement filings (PAS-4, special resolution, PAS-3) and shareholder approval.
- **No angel-tax issue:** Section 56(2)(viib) was abolished from FY 2024-25.

**Five ways an iSAFE complicates later rounds, and how ours is designed out.** Numbers are the final Step 9 figures: seed price **₹107.51** at ₹19 Cr pre-money; cap price **₹64.67**.

| # | Complication | Our numbers | Designed out by |
|---|---|---|---|
| 1 | **Conversion dilution lands on founders** (VCs require notes to convert inside the pre-money) | The angels convert at ₹64.67 vs ₹107.51: ~1.66x more shares per rupee; 3.0% before the seed, 2.1% after, for ₹30L | A **post-money cap**, so the angels' 3.0% was fixed and known from the start |
| 2 | **Preference overhang** | Uncapped: 46,392 × ₹107.51 = **₹49.9L of preference for ₹30L** | Preference **capped at the ₹30L invested** (a "shadow series") |
| 3 | **Stacking** | 1 note | One iSAFE round, one cap, closed |
| 4 | **Anchoring** | ₹10 Cr cap vs ₹23.75 Cr seed post-money | The cap priced pre-product risk (Oct 2025). The seed is priced on 9 months of paid traction. A **2.4x step-up over 13 months** reads as "the price rose because the risk fell" |
| 5 | **Rights creep** | — | No board seat, no vetoes; information rights only; pro-rata right for the seed only; most-favoured-nation clause ends at the seed; long-stop conversion at the cap after 24 months |

**Exposure after later rounds:**

| | After pre-seed (as converted) | After seed | After Series A | After Series B |
|---|---|---|---|---|
| CEO (Prathyusha) | 38.8% | 27.2% | 21.7% | 18.5% |
| CTO (Sri Charan) | 29.1% | 20.4% | 16.3% | 13.9% |
| COO (Kavyanth) | 29.1% | 20.4% | 16.3% | 13.9% |
| Angels (iSAFE) | 3.0% | 2.1% | 1.7% | 1.4% |
| Founders combined | 97.0% | 67.9% | 54.3% | 46.2% |

Founders keep a majority through Series A. M4's playbook: *"better off with a low percentage in a highly valued company"*.

### 2.7 Is the ₹10 Cr iSAFE cap reasonable? (benchmarked)
No reliable public dataset of Indian iSAFE caps exists, so we triangulate **[web]**:
- Indian pre-seed rounds typically raise **₹25L–2 Cr**; median pre-seed cheques were **$200–500k** in 2025.
- iSAFE guides use **₹10 Cr** and **₹30 Cr** caps as worked examples.
- A comparable recent pre-seed, **Unveilr AI (Oct 2026)**, was priced at **₹16.7 Cr post-money**.
- Our raise was ₹30L at a ₹10 Cr cap: **3% dilution**, in Oct 2025, with a team (including an ex-founder CEO) but **before a paid pilot**.

**Verdict:** ₹10 Cr sits at the low-to-middle of the range, which fits pre-product risk. It is not so low that it anchors the seed. The step-up to ₹23.75 Cr post is 2.4x after 13 months and a paid pilot.

---
## Decisions log (LOCKED 16 Nov 2026; timeline backdated after the team's review)
- **Roles and equity:** Prathyusha Kalluri, CEO, 40% · Sri Charan Peri, CTO and acting DPO, 30% · Kavyanth Munagala, COO, 30%. All full-time since May 2025.
- **Prior exit:** FixNear (2016, sold 2022 for ~₹4 Cr, mostly stock, to a non-competing regional aggregator; non-compete ended 2024).
- **Timeline:**
  - discovery Jan–Apr 2025
  - incorporated May 2025
  - prototype Jun–Sep 2025
  - iSAFE Oct 2025
  - paid pilot Feb–Apr 2026
  - 14 paying agencies by Oct 2026
  - seed raise Nov 2026
- **Pre-seed:** ₹30L iSAFE from two operator angels, ₹10 Cr post-money cap (benchmarked, 2.7), with the five protections.
- **SISFS:** ₹20L sanctioned Mar 2026; ₹10L received; ₹10L on the 25-agency milestone.
- **Cash at the raise:** ~₹21L after ~₹34L spent (itemised in 2.4).
- **Strategic advisors** join on ESOP grants, not as investors.
