# Step 8 — Funding needs → the ask
**Phase C: The engine · Status: LOCKED 16 Nov 2026**
**Tags:** **[Real]** = case-competition research · **[repo]** = team repo `ESFS/keepwell/` · **[web]** = checked online on 16 Nov 2026 · **[Story]** = backstory or pilot · **[Model]** = `keepwell_model.xlsx` (Funding Need, P&L and Cash, Assumptions §8–10).
**Plan:** [`../pitch_bible.md`](../pitch_bible.md) · **Builds on:** Steps 2 (cash and grants), 3 (what the ecosystem can't give), 6 (experiments and Series A gates), 7 (P&L, locked) · **Feeds:** Step 9 (valuation, stake)

## 8.1 How this step is built
**Course frame (M1).** A startup needs funding for five things:
1. **build the product** (typically ~40% of funding)
2. **build the team** (~25%)
3. **discover product–market fit** ("generally invisible, but critical")
4. **marketing and sales**
5. **working capital** ("maintain a sufficient runway at all times… avoid distress decisions")

For **Stage 2, Finding a Business Model**, M1 marks *PMF discovery* as the heaviest need (✓✓), with all the others needed too (✓).

**Method (our Class Activity 1):** gross cash need − revenue in the period − cash in hand = the external gap. Round up slightly, without over-raising.

**Rule (from earlier in this work).** The ask is an **output** of costed requirements. We never start from a number. Every line below traces to a requirement from Steps 3, 5, 6 or 10, or to the locked P&L (Step 7).

## 8.2 Runway: why 24 months
| Month (from seed close) | What happens **[Model]** |
|---|---|
| 0 | Seed closes. Google for Startups AI-tier application (14–28-day review **[repo]**) |
| 1–6 | E1 price test across 30+ agencies in 3 towns; E4 language and safety gates; first field-sales hire |
| ~13 | **40,000 machine records** (Series A gate; 28,000 by month 12) |
| ~15 | **~120 paying agencies** (Series A gate) |
| 15–18 | Gates held for 3 months: one-visit closure +10 points, ≥ 95% retention, value ≥ 2x the fee, payback ≤ 6 months, 1 administrator LOI |
| **18–24** | **Series A raised from strength** (a 4–6-month process) |
| 24 | ~**260 paying agencies**, ~**1.49 lakh machine records**, revenue run-rate **~₹1.6 Cr a year**, ~₹1.08 Cr cash left (~5 months of Y3 burn) |

**Why not 18 months?** With 18 months, the gates are only *just* met when the money runs out. That means raising a Series A under pressure, which is exactly the "distress decision" M1 warns about.

**The trade-off, in numbers** (each row re-priced by the model):

| Runway | Ask | Pre-money | Investor stake | Founders after seed | Agencies at the end |
|---|---|---|---|---|---|
| 18 months | ₹3.25 Cr | ₹22 Cr | 12.9% | 74.8% | 165 |
| 21 months | ₹4.0 Cr | ₹21 Cr | 16.0% | 71.8% | 212 |
| **24 months (recommended)** | **₹4.75 Cr** | **₹20 Cr** | **19.2%** | **68.7%** | **259** |

Six extra months of safety cost the founders ~6 points of ownership. That's worth it.

## 8.3 What the money pays for: the costed requirement list
### Lane 1: Build the product (₹2.20 Cr, 40%)
| Requirement | Why (source) | Y1 | Y2 | Basis |
|---|---|---|---|---|
| **AI lead** | Owns root-cause ranking and the learning loop: the moat (Step 5) | ✓ | ✓ | |
| **Backend / platform engineer** | Repo "Foundations": consent store, cost ledger, admin console must precede customer data | ✓ | ✓ | Tech team: **4 in Y1 → 6 in Y2**, avg ₹18L/yr (Hyderabad) → **₹72L + ₹1.17 Cr** |
| **WhatsApp / full-stack engineer** | The only channel (repo); the agency and technician flows | ✓ | ✓ | |
| **Eval and data engineer** | Release gates, golden sets, LLM judge (repo §10.5) | ✓ | ✓ | |
| **SRE / security engineer** | Tenant isolation, secrets, audit log; DPDP breach duties from May 2027 | | ✓ | |
| **Speech / ML engineer** | Telugu → Hindi → Tamil accuracy (repo risk #2) | | ✓ | |
| Cloud, tools, model hosting | Cloud Run, Cloud SQL, storage, eval runs (~₹2,300/night) **[repo]** | ₹6L | ₹12L | Repo pilot stack ₹12–35k/month, scaled |
| Devices and field kits | Test phones (low-end Android, repo persona), laptops | ₹5L | ₹8L | Depreciated over 3 years |

### Lane 2: Build the team and the company (₹1.54 Cr, 28%)
| Requirement | Why | Y1 | Y2 | Basis |
|---|---|---|---|---|
| 3 founders | CEO, CTO and acting DPO, COO (Step 2) | ₹36L | ₹39L | ₹12L each, below market: skin in the game |
| Finance, HR and admin | Monthly books, payroll, ESOP administration, investor reporting (term sheet: quarterly financials, monthly KPIs) | 1 | 2 | ₹10L each |
| **Seed transaction costs** | Legal due diligence, shareholders' agreement, stamp duty, valuer (the course term sheet has the company bear up to ₹12.5L) | **₹8L** | — | One-off |
| Lawyer engagement | Agency–Keepwell processing agreement, consent notices, terms, IRDAI plan opinion, "evidence pack, not legal advice" line **[repo]** | ₹4L | ₹3L | Repo: "lawyer review, 2 weeks" |
| CA/CS retainer, registered valuer, trademarks, security review | Clean company (Step 2.5); Keepwell, Circuit and Mistri Gyan marks | ₹4L | ₹4L | ₹20k/month retainer + one-offs |
| DPDP readiness and audit | Main duties from ~13 May 2027 **[repo]**: breach reporting within 72h, one-year logs | — | ₹3L | ISO 27001 readiness prep |
| Office and travel | CIE-IIITH incubation space; field travel across TS/AP | ₹8L | ₹14L | |

### Lane 3: Discover product–market fit (₹1.15 Cr, 21%)
| Requirement | Why (Step 6 experiment) | Y1 | Y2 |
|---|---|---|---|
| **Agency success team** (3 → 5 people, 1 per ~50–80 agencies) | Onboarding, rate cards, weekly reviews with owners; E1, E2 | ₹15L | ₹27L |
| E1 price test at scale (30+ agencies, 3 towns): onboarding kits, field travel | Risk #1, "will agencies pay per fix" | ₹6L | ₹8L |
| Golden datasets: 150–300 min of audio per language, 450 photos, 420 retrieval cases **[repo]** | E4 language gates, with the IIIT-H speech lab | ₹5L | ₹6L (Tamil, Kannada) |
| Vernacular lexicon (~600 rows) and hazard lexicon (~400 terms × 6 languages), signed off by the safety expert **[repo]** | E4 safety; zero false-accepts | ₹4L | ₹3L (re-certification) |
| Manuals (~150: top 10 brands × 7 appliances) and warranty terms (top 12 brands) **[repo]** | Day-one baseline against cold start (Step 5) | ₹1.5L | — |
| Red-teaming (50–100 injection + 100+ hazard cases) **[repo]** | Release gate | ₹1.5L | — |
| Household research and Home Memory consent (E6); administrator discovery and LOI (E7) | R2/R3 preconditions | ₹3L | ₹5L |
| Agency census in TS/AP + analytics tooling | Validates the Step 4 count (37,500); E2/E5 measurement | ₹4L | ₹3L |
| AI, messaging and support tooling per job (cost of revenue) | Runs on every job, **before** credits | ₹4.3L | ₹18.4L |

### Lane 4: Marketing and sales (₹0.56 Cr, 10%)
| Requirement | Why | Y1 | Y2 |
|---|---|---|---|
| Field sales (1 → 3 people; each adds ~80 paying agencies a year) | The growth engine (Step 7) | ₹9L | ₹29L |
| Acquisition cash (₹1,000 per new agency: wholesaler referral + onboarding) | E5 channel test (Step 3: trade network + parts wholesalers) | ₹0.8L | ₹2.5L |
| Brand: Telugu dailies in the pilot towns, association memberships, events | Agency awareness (Step 3) | ₹5L | ₹10L |

### Lane 5: Working capital (₹0.05 Cr, 1%)
Fortnightly per-fix invoices paid by UPI (5 of 5 first pilot invoices paid on time). Working capital is ~5% of revenue. Parts float comes only after R4 (Y3).

## 8.4 From budget to the ask **[Model]**
| | ₹ lakh |
|---|---|
| Gross spend over 24 months (the five lanes) | 549.9 |
| + Contingency (10%, as in Class Activity 1) | 55.0 |
| **= Total cash needed** | **604.9** |
| − Revenue earned in 24 months (Step 7) | (111.9) |
| = Net cash burn | 492.9 |
| − Cash in the bank (Step 2) | (37.0) |
| − Grants | **0**: the SISFS application (₹20L) is not yet sanctioned, so it isn't counted |
| **= External funding gap** | **455.9** |
| **The ask (rounded up to the nearest ₹25L)** | **₹475 lakh = ₹4.75 Cr** |

**Not netted off the ask: Google for Startups credits and the SISFS grant.**
- **Credits:** ~₹34L of real AI and cloud cost in Y1–Y2. They're approved only after the seed closes.
- **SISFS:** ₹20L if sanctioned.
- Both are kept out for the same reason our MediQuick activity gave: *don't base survival on an unapproved grant*.
- **Together they extend runway by ~3 months** (~₹54L ÷ ~₹18L monthly burn in Y2). We pitch them as a buffer, not a budget line.

## 8.5 Use of funds
| Lane (M1) | ₹ Cr | Share | Course benchmark (M1) |
|---|---|---|---|
| Build the product | 2.20 | **40%** | "Typically 40% of funding needs is towards building the product" ✓ |
| Build the team and the company | 1.54 | **28%** | "Typically 25% … goes toward team building" ✓ (+ one-off seed costs) |
| Discover product–market fit | 1.15 | **21%** | Heaviest *need* at Stage 2. Much of the product and team spend also serves PMF |
| Marketing and sales | 0.56 | **10%** | Stage 2 = "build early sales frameworks", not scale marketing |
| Working capital | 0.05 | **1%** | Asset-light until parts (R4) |

The contingency (₹0.55 Cr) sits on top, as in Class Activity 1.

**What we deliberately don't spend on:** paid consumer advertising, a consumer app, OEM integrations, a big office, a second accelerator (Step 3), or parts inventory before R4.

## 8.6 What the ₹4.75 Cr buys: the milestones (Series A gates, Step 6)
| Gate | Target | Experiment |
|---|---|---|
| Paying agencies | ~120 by month ~15; ~260 by month 24 | E1, E5 |
| Machine records | 40,000 by month ~13; ~1.49 lakh by month 24 | E6 |
| One-visit closure | ≥ +10 points vs each agency's own baseline, held for 3 months | E2, E3 |
| Retention | **≥ 97% a month** (the plan's churn assumption) | E1 |
| Value to the agency | **≥ 1.5x the fee and a net gain ≥ ₹3,000 a month** (modelled: 1.8x, ~₹3,850) | E1 |
| CAC payback | ≤ 6 months (modelled 5.6) | E5 |
| Language and safety | ≤ 10-point gap between languages; 0 safety false-accepts | E4 |
| AI cost per job (2027 prices) | ≤ ₹10 (budgeted ₹4.5) | E8 |
| R2/R3 buyer signal | 1 administrator LOI | E7 |

## 8.7 Sanity checks
- **Market norm.** ₹4.75 Cr ≈ **$0.51M**. Indian seed rounds are typically **$0.3–2M**, with a median ticket of about **$1M** **[web]**. We're at the lean end, which suits a capital-efficient story.
- **Course cheque ranges.** Early VC ₹1–100 Cr (M2) ✓. M4's illustrative seed-VC range is ₹0.5–2 Cr, so the round is a **syndicate**: a lead seed VC plus a second fund plus strategic angels (Step 9).
- **Not over-raising.** Headroom over the gap is ₹19L. With contingency, the plan ends month 24 with **~₹1.08 Cr in the bank (~5 months of Y3 burn)**, plus ~₹54L of unbudgeted credits and grant.
- **Dilution.** 19.2% sits inside the Indian norm of 15–25% **[web]** (Step 9).

## 8.8 After the seed: what Series A will need
In the funded plan (Step 7.7, G), cash bottoms at about **−₹2.6 Cr in Y4** before break-even in Y5.

**Series A of ~₹8–10 Cr around month 20**, from strength:
- **~₹3–4 Cr** funds the modelled plan to break-even, with a buffer: field sales 3 → 24, agency success 5 → 32.
- **The rest funds Tier 1 entry** (repo Phase 2), which is upside and not in the numbers.

**Target step-up: 2–3x.** That means a Series A pre-money of ~₹50–75 Cr against the seed's ₹24.75 Cr post, earned by the Series A gates and a ~₹4 Cr Y3 revenue path. The model conservatively assumes 20% dilution at A.

Venture debt becomes possible only after Series A, with revenue (course M2).

## 8.9 Weak points, said before an investor says them
| Weak point | Answer |
|---|---|
| "40% on product, but you already have an MVP" | The MVP proves the loop; the seed builds the repo's Foundations (consent, eval, audit) that must come before customer data at scale, plus speech accuracy in two more languages |
| "Team and company is 28%" | It includes a one-off ₹8L of seed transaction costs and founder salaries below market. Without the one-off it's ~26%, in line with M1's 25% |
| "Why not raise less, at 18 months?" | It would have to raise a Series A under pressure (8.2). Six points of dilution buy six months of safety |
| "What if credits or SISFS are rejected?" | Neither is in the ask (8.4) |
| "What if E1 fails (agencies won't pay ₹40)?" | The kill/pivot path is defined: hybrid or desk-fee pricing (Step 6). The contingency covers a 2–3-month re-test |

## 8.10 How it shows up in the pitch (final choices in Step 12)
- **The ask slide:** *"₹4.75 Cr seed for 24 months, to take Circuit from 5 to ~260 paying agencies and 1.5 lakh machine records, and reach Series A from strength."*
- A use-of-funds bar (40 / 28 / 21 / 10 / 1), the milestone list (8.6), and one line: *"The round also unlocks Google for Startups AI credits (~₹34L of our planned AI and cloud spend)."*
- Appendix: the requirement list (8.3) and the budget-to-ask bridge (8.4).

Covers: course M3 "Ask: amount, milestones, rationale", and the deck mistake it avoids: "unclear or unjustified fundraising ask".

---

## Decisions log (LOCKED 16 Nov 2026; updated after the Step 12 review)
- **Runway:** 24 months. The Series A gates are reached ~months 13–18, and a Series A takes 4–6 months.
- **The ask: ₹4.75 Cr** (gap ₹4.56 Cr). It was ₹4.5 Cr before the review; it rose because the SISFS grant is now counted only once sanctioned. Google credits and SISFS are kept outside the ask (~3 months of buffer).
- **Use of funds:** product 40% · team and company 28% · PMF 21% · marketing and sales 10% · working capital 1%, plus 10% contingency.
- **After the seed:** a Series A of ~₹8–10 Cr around month 20, targeting a 2–3x step-up.
