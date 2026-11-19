# Step 8 — Funding needs → the ask
**Phase C: The engine · Status: LOCKED 16 Nov 2026 (updated for the backdated timeline and observed inputs)**
> **Illustrative case.** Founder histories, the company timeline, the pilot results and the financials are assumptions made for the IIIT Hyderabad ESFS course pitch. They are kept consistent with the team repo and with each other.

**Tags:** **[repo]** = team repo `ESFS/keepwell/` · **[web]** = checked online · **[Story]** = backstory or pilot · **[Model]** = `keepwell_model.xlsx` (Funding Need, P&L and Cash, Assumptions §8–10).
**Plan:** [`../pitch_bible.md`](../pitch_bible.md) · **Builds on:** Steps 2, 3, 6 and 7 · **Feeds:** Step 9 (valuation, stake)

## 8.1 How this step is built
**Course frame (M1).** Five funding needs: build the product, build the team, discover PMF, marketing and sales, working capital. At **Stage 2, "Finding a Business Model"**, M1's stage matrix marks **PMF as the heaviest need (✓✓)**.

**Method (our Class Activity 1):** gross cash need − revenue in the period − cash in hand − sanctioned grants = the external gap. Round up slightly.

**Rule.** The ask is an **output** of costed requirements. Every line traces to Steps 3, 5, 6 and 10 or to the locked P&L (Step 7).

## 8.2 Runway: why 24 months
| Month (from seed close, ~Dec 2026) | What happens **[Model]** |
|---|---|
| 0 | Seed closes. Google for Startups AI-tier application (14–28-day review) |
| 1–6 | First field-sales hire; E1 in 3 new towns; E4 Hindi/Tamil gates; SISFS second ₹10L at 25 paying agencies (~month 3) |
| ~13 | **40,000 machine records** (Series A gate; 29,000 by month 12) |
| ~15 | **~120 paying agencies** (Series A gate; from 14 today) |
| 15–18 | Gates held for 3 months |
| **18–24** | **Series A raised from strength** (a 4–6-month process) |
| 24 | ~**264 paying agencies**, ~**1.37 lakh records**, revenue run-rate **~₹1.4 Cr a year** |

**Why not 18 months?** With 18 months, the gates are only *just* met when the money runs out, which forces a "distress decision" (M1). The trade-off, each row re-priced by the model:

| Runway | Ask | Pre-money | Investor stake | Founders after seed | Agencies at the end |
|---|---|---|---|---|---|
| 18 months | ₹3.5 Cr | ₹20 Cr | 14.9% | 72.9% | 172 |
| 21 months (**minimum close**) | ₹4.0 Cr | ₹20 Cr | 16.7% | 71.1% | 218 |
| **24 months (target)** | **₹4.75 Cr** | **₹19 Cr** | **20.0%** | **67.9%** | **264** |

## 8.3 What the money pays for: the costed requirement list, grouped by purpose
**How the lanes are grouped.** Each line sits in the lane of **what it achieves**, not of who is paid. Three of the six engineers run the PMF experiments (model input `eng_pmf` = 50%), so they sit in the PMF lane:
- the **AI lead** (root-cause accuracy, E2)
- the **eval/data engineer** (gates and measurement)
- the **speech/ML engineer** (Hindi/Tamil, E4)

8.5 also shows the same money by cost type.

### Lane 1: Discover product–market fit (₹2.08 Cr, 38%)
| Requirement | Why (Step 6 experiment) | Y1 | Y2 |
|---|---|---|---|
| **AI lead, eval/data engineer, speech/ML engineer** | Root-cause accuracy beyond 78%, release gates, Hindi/Tamil accuracy (E2, E4, E8) | ₹36L | ₹58L |
| **Agency success team** (3 → 5 people) | Onboarding, rate cards, weekly reviews with owners; E1, E2 | ₹15L | ₹27L |
| E1 price and retention test in 3 new towns: onboarding kits, field travel | Will agencies pay ₹40 outside our network? | ₹6L | ₹8L |
| Golden datasets: audio per language, photos, retrieval cases **[repo]** | E4, with the IIIT-H speech lab | ₹5L | ₹6L |
| Vernacular and hazard lexicons, signed off by the safety expert **[repo]** | E4; zero safety false-accepts | ₹4L | ₹3L |
| Manuals (~150) and warranty terms (top 12 brands) **[repo]** | Accuracy for new appliance categories | ₹1.5L | — |
| Red-teaming (injection + hazard cases) **[repo]** | Release gate | ₹1.5L | — |
| Household research (E6); administrator discovery and LOI (E7) | R2/R3 preconditions | ₹3L | ₹5L |
| Agency census in TS/AP + analytics | Validates Step 4; E2/E5 measurement | ₹4L | ₹3L |
| AI, messaging and support tooling per job (cost of revenue) | Runs on every job, before credits | ₹4.5L | ₹16.7L |

### Lane 2: Build the product (₹1.25 Cr, 23%)
| Requirement | Why | Y1 | Y2 |
|---|---|---|---|
| **Backend/platform, WhatsApp/full-stack and SRE/security engineers** | Repo Foundations (consent store, cost ledger, eval harness, admin console) before customer data at scale; the rest of R1 (A7, A8, A10, A11); DPDP security duties | ₹36L | ₹58L |
| Cloud, tools, model hosting | Repo stack, scaled | ₹6L | ₹12L |
| Devices and field kits | Low-end Android test phones, laptops | ₹5L | ₹8L |

### Lane 3: Build the team and the company (₹1.54 Cr, 28%)
| Requirement | Why | Y1 | Y2 |
|---|---|---|---|
| 3 founders | Stipends rise from ₹6L to ₹12L a year each, still below market | ₹36L | ₹39L |
| Finance, HR and admin (1 → 2) | Books, payroll, ESOP administration, investor reporting | ₹10L | ₹22L |
| **Seed transaction costs** | Legal due diligence, SSHA, stamp duty, valuer (the course term sheet has the company bear up to ₹12.5L) | **₹8L** | — |
| Lawyer engagement | DPA, consent notices, terms, the IRDAI route, the "evidence pack" line **[repo]** | ₹4L | ₹3L |
| CA/CS retainer, valuer, trademarks, security review | Clean company (Step 2.5) | ₹4L | ₹4L |
| DPDP readiness and ISO 27001 preparation | DPDP duties from ~13 May 2027 **[repo]** | — | ₹3L |
| Office and travel | CIE-IIITH space; field travel across TS/AP | ₹8L | ₹14L |

### Lane 4: Marketing and sales (₹0.56 Cr, 10%)
| Requirement | Why | Y1 | Y2 |
|---|---|---|---|
| Field sales (1 → 3 people; ~80 paying agencies each a year, backed by the COO's pace) | The growth engine (Step 7); E5 | ₹9L | ₹29L |
| Acquisition cash (₹1,000 per new agency) | Wholesaler referral + onboarding | ₹0.8L | ₹2.5L |
| Brand: Telugu dailies, association memberships, events | Agency awareness | ₹5L | ₹10L |

### Lane 5: Working capital (₹0.04 Cr, 1%)
Fortnightly per-fix invoices paid by UPI (97% on time). Working capital is ~5% of revenue. Parts float comes only after R4 (Y3).

## 8.4 From budget to the ask **[Model]**
| | ₹ lakh |
|---|---|
| Gross spend over 24 months (the five lanes) | 548.1 |
| + Contingency (10%, as in Class Activity 1) | 54.8 |
| **= Total cash needed** | **602.9** |
| − Revenue earned in 24 months (Step 7) | (104.8) |
| = Net cash burn | 498.1 |
| − Cash in the bank (Step 2) | (21.0) |
| − SISFS second tranche (sanctioned; due at 25 paying agencies) | (10.0) |
| **= External funding gap** | **467.1** |
| **The ask (rounded up to the nearest ₹25L)** | **₹475 lakh = ₹4.75 Cr** |
| **Minimum close** | **₹4.0 Cr** (21 months of runway) |

**Not netted off the ask: Google for Startups credits** (~₹33L of AI and cloud cost in Y1–Y2). They're approved only after the seed closes, and our rule is not to plan survival on unapproved money. If approved, they add ~1.7 months of runway.

## 8.5 Use of funds
**By purpose (what we pitch):**

| Lane (M1) | ₹ Cr | Share | Why this weight at Stage 2 |
|---|---|---|---|
| **Discover product–market fit** | **2.08** | **38%** | The heaviest need at Stage 2 (M1 ✓✓). Every Series A gate (8.6) is a PMF proof |
| Build the team and the company | 1.54 | **28%** | M1: "typically 25% toward team building", plus one-off seed costs |
| Build the product | 1.25 | **23%** | The repo's Foundations and the rest of R1. The MVP already runs in production |
| Marketing and sales | 0.56 | **10%** | Stage 2 = "build early sales frameworks", not scale marketing |
| Working capital | 0.04 | **1%** | Asset-light until parts (R4) |

**By cost type (the same money):** engineering + cloud + devices 40% · founders, finance, office, compliance 28% · agency success, pilots, research, per-job AI 21% · field sales, acquisition, brand 10% · working capital 1%.

The contingency (₹0.55 Cr) sits on top.

**What we deliberately don't spend on:** paid consumer advertising, a consumer app, OEM integrations, a big office, a second accelerator (Step 3), or parts inventory before R4.

## 8.6 What the ₹4.75 Cr buys: the milestones (Series A gates)
| Gate | Target | Today |
|---|---|---|
| Paying agencies | ~120 by month ~15; ~264 by month 24 | 14 |
| Machine records | 40,000 by month ~13; ~1.37 lakh by month 24 | ~3,600 |
| One-visit closure | ≥ +10 points vs own baseline, held 3 months, at scale | +12 (14 agencies) |
| Retention | ≥ 97% a month | ~98.6% (early) |
| Value to the agency | ≥ 1.5x the fee and a net gain ≥ ₹3,000 a month | ~2.0x, ~₹3,800 |
| CAC payback (fully loaded) | ≤ 7 months | Modelled 6.3 |
| Language and safety | ≤ 10-point gap between languages; 0 false-accepts | Telugu only so far |
| AI cost per job (2027 prices) | ≤ ₹10 | ₹3.0 measured (2026) |
| R2/R3 buyer signal | 1 administrator LOI | Discovery under way |

## 8.7 Sanity checks
- **Market norm.** ₹4.75 Cr ≈ **$0.51M**, at the lean end of Indian seed rounds ($0.3–2M; median ticket ~$1M) **[web]**.
- **Course cheque ranges.** Within early VC ₹1–100 Cr (M2). Above M4's illustrative seed-VC band (₹0.5–2 Cr). The defence: the number comes from costed requirements, not from a stage label.
- **One investor can write it.** We target lead funds whose typical seed cheque is ₹4–8 Cr: Blume, Accel (Atoms), Elevation, BEENEXT (Step 9).
- **Not over-raising.** Headroom over the gap is ₹8L. Month 24 ends with ~₹62L before credits (~2.5 months of Y3 burn), or ~₹95L with them.
- **Dilution.** 20.0% sits inside the Indian norm of 15–25% **[web]**.

## 8.8 After the seed: what Series A will need
In the funded plan (Step 7.7, G), cash bottoms at about **−₹4.1 Cr in Y4** before break-even in Y5. The lean plan would need *more* (~₹4.9 Cr).

**Series A of ~₹8–10 Cr around month 20:**
- ~₹5 Cr funds the modelled plan to break-even, with a buffer.
- The rest funds **Tier 1 entry** (repo Phase 2), which is upside and not in the numbers.

**Target step-up 2–3x** (Series A pre-money ~₹50–70 Cr against the seed's ₹23.75 Cr post), earned by the gates. The model conservatively assumes 20% dilution at A.

## 8.9 Weak points, said before an investor says them
| Weak point | Answer |
|---|---|
| "Isn't moving engineers into PMF just relabelling?" | Same money, shown both ways (8.5). Three engineers run E2/E4/E8; three build the platform |
| "Why is product still 23% if you're live?" | The repo's Foundations (consent, eval, audit) come before customer data at scale, plus the rest of R1 |
| "Why not raise less, at 18 months?" | It would force a Series A raise under pressure. Six more months cost founders ~5 points. The minimum close (₹4.0 Cr, 21 months) is our floor |
| "What if credits are rejected?" | They aren't in the ask |
| "What if E1 fails outside your network?" | The kill/pivot path is defined (hybrid or desk-fee pricing). The contingency covers a 2–3-month re-test |

## 8.10 How it shows up in the pitch
- **The ask slide:** *"₹4.75 Cr seed for 24 months, to take Circuit from 14 to ~260 paying agencies and reach Series A from strength."*
- A use-of-funds bar by purpose (PMF 38 / team 28 / product 23 / sales 10 / WC 1), the milestones (8.6), and the minimum close.
- Appendix: the requirement list (8.3) and the budget-to-ask bridge (8.4).

Covers: M3's "Ask: amount, milestones, rationale", and the deck mistake it avoids: "unclear or unjustified fundraising ask".

---
## Decisions log (LOCKED 16 Nov 2026; updated for the backdated timeline)
- **Runway:** 24 months (target), 21 months (minimum close).
- **The ask: ₹4.75 Cr target, ₹4.0 Cr minimum close.** Gap ₹4.67 Cr after ₹21L cash and the sanctioned SISFS tranche (₹10L). Credits are kept outside.
- **Use of funds by purpose:** PMF 38% · team and company 28% · product 23% · marketing and sales 10% · working capital 1%, plus 10% contingency.
- **After the seed:** a Series A of ~₹8–10 Cr around month 20, targeting a 2–3x step-up.
