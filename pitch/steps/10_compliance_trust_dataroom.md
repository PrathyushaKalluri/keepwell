# Step 10 — Compliance, trust and data room
**Phase D: The deal · Status: LOCKED 16 Nov 2026** (recommendations adopted; the team asked for Steps 10–13 to be completed end to end)
> **Illustrative case.** Founder histories, the company timeline, the pilot results and the financials are assumptions made for the IIIT Hyderabad ESFS course pitch. They are kept consistent with the team repo and with each other.
**Tags:** **[Real]** = course material or real record · **[repo]** = team repo `ESFS/keepwell/` · **[Story]** = assumed company state · **[KB]** = established regulation, not in the repo (verify with our CA/lawyer before filing)
**Plan:** [`../pitch_bible.md`](../pitch_bible.md) · **Builds on:** Step 2 (clean company), Step 3 (enablers), Step 5 (trust design), Step 8 (compliance budget) · **Feeds:** Step 11 (Startup–Quality), Step 12 (trust slide, data room)

## 10.1 How this step is built
**Course frame (M3, Pillar 3: Compliance, "hygiene").** Compliance covers four areas:
1. **Corporate and legal:** incorporation, board, statutory registers, licences, shareholder agreements, a clean cap table.
2. **HR, finance and tax:** contracts, ESOP policy, PF/ESI, POSH, audited statements, GST/TDS, financial controls.
3. **Customer and vendor:** contracts, SLAs, NDAs, service records, anti-bribery and anti-money-laundering.
4. **IP, data privacy and other:** IP filings, confidentiality, data privacy (IT Act), certifications, ESG and a litigation log.

*Why it matters:* "right to operate, builds confidence for investors, foundational for due diligence".

**Pillar 4, Data Room ("proof"):** "evidence behind every claim".

**Our rule.** Every obligation gets three things: a **status** (Done / In progress / Due by date), an **owner**, and a **cost line** that already sits in the Step 8 budget.

## 10.2 The obligations Keepwell actually has
### A. Corporate and legal
| Item | Status | Owner | Cost (Step 8) |
|---|---|---|---|
| Incorporation papers: MoA, AoA, CIN, PAN, TAN | Done (May 2025) **[Story]** | CEO | in place |
| DPIIT recognition (Startup India) | Done **[Story]** | CEO | — |
| Statutory registers, board minutes, ROC filings | Done / ongoing | CA/CS | retainer |
| Founders' agreement: vesting, **IP assignment of Circuit code and Mistri Gyan to the company** (closes the student-IP risk, checked with CIE) | Done **[Story]** | CEO | in place |
| iSAFE (CCPS) issue: registered-valuer report, PAS-4, special resolution, PAS-3 | Done **[Story]** | CA/CS | in place |
| Seed CCPS: valuation report, shareholders' agreement (SSHA), restated AoA, PAS-3, FC-GPR if a foreign investor | At close | Lawyer + CA/CS | ₹8L seed transaction costs |
| Shops and Establishments registration (Telangana) | Done **[Story]**; renew yearly | COO | retainer |

### B. HR, finance and tax
| Item | Status | Owner |
|---|---|---|
| Employment contracts with confidentiality and IP clauses | Done (12 people in Y1) | CEO |
| **ESOP plan** (10% pool): board and shareholder approval, grant letters, digital tracking (course M3: "must digitally track/report grants") | Adopt at seed close | CEO + CA |
| GST registration and returns; TDS | Done / monthly | CA |
| PF (≥ 20 employees) and ESI (≥ 10 employees) **[KB]** | ESI from ~10 employees (Y1); PF from ~20 (Y2–Y3) | Finance lead |
| POSH policy and internal committee (≥ 10 employees) **[KB]** | Before the 10th hire | CEO |
| Audited annual financials; monthly books; separate bank account | Done / yearly | CA |
| Field-sales and agency-success staff are **employees, not gig workers** (avoids the reclassification risk the repo flags for platforms) | Policy | COO |

### C. Customers and vendors
| Item | Status | Owner |
|---|---|---|
| **Agency agreement**: per-verified-fix fee, the 30-day trial, an SLA, and the **data-processing clause** (agency = data fiduciary, Keepwell = processor) **[repo]** | Template done; lawyer review in Y1 | COO + lawyer |
| Household consent notices in 6 languages; a purpose-bound consent ledger checked on every read **[repo]** | Built (pilot); lawyer review | CTO |
| Vendor agreements: Google Cloud (Cloud DPA), Meta WhatsApp Business (BSP), payment of Google credits | In place | CTO |
| Service records: every job and verification event is logged (append-only `machine_event`) **[repo]** | Built | CTO |
| Anti-bribery / AML policy (no cash incentives to agencies; wholesaler referrals paid by invoice) | Policy | CEO |

### D. Data, AI, IP and sector rules (the material ones for us)
| Rule | What it means for Keepwell | Status / control | Source |
|---|---|---|---|
| **DPDP Act 2023 + DPDP Rules (notified 14 Nov 2025)** | Main duties apply from **~13 May 2027**: notice and consent, breach reporting (to the Board without delay, then a detailed report within **72 hours**), security safeguards (encryption, access control, monitoring), **logs kept for 1 year**, erasure with 48 hours' notice, verifiable parental consent for under-18s | Consent-first design is built. Keepwell is a **processor** for agencies, and becomes a **fiduciary** if it uses data for its own purposes (model improvement, benchmarking), which needs separate consent. Lawyer to confirm the roles | **[repo]** |
| Data residency | Production runs in **Mumbai (asia-south1)**. The model router carries a residency flag. Anything processed out of region (e.g. Chirp 3 speech in the US/EU) is redacted and disclosed in consent | Built | **[repo]** |
| Claim wording | Say *"hosted in Mumbai with security safeguards"*, **not** "DPDP-compliant Google stack" (Google publishes no DPDP-specific commitment) | Pitch rule | **[repo]** |
| **CERT-In directions (2022)** | Report cyber incidents within **6 hours**; keep ICT logs for **180 days** in India **[KB]** | Logging pipeline; incident runbook (Y1) | **[KB]** (gap in the repo) |
| **IT Act 2000** — reasonable security practices; intermediary obligations | Security policy; grievance officer named | Y1 | **[KB]** |
| **IRDAI**: extended warranties are insurer-filed products (UINs at Zurich Kotak, Digit, Bajaj Allianz, ICICI Lombard…) | **Service Plans (R2) are sold *for* licensed insurers or administrators.** Keepwell does not underwrite. Earning commission needs an **IRDAI-registered route**: a corporate-agent registration, or distributing through a registered intermediary partner (e.g. a warranty administrator) on a referral/service fee. `plan_selling_enabled = false` until the route is in place | Lawyer opinion in Y1 (Step 8) | **[repo]** |
| **Consumer Protection Act 2019** and **CCPA dark-pattern guidelines** | No drip pricing, bait-and-switch or false urgency in quotes. Seller and manufacturer are jointly liable for defects. The fair-price view (R2) is "indicative" | Quote rules in code; owner approves every quote | **[repo]** |
| Legal-advice boundary | The claim help (R2) is an **"evidence pack, not legal advice"**. The FTC's DoNotPay order cost **$193,000** | Product copy and terms | **[repo]** |
| **E-Waste (Management) Rules 2022**: refurbishers must register on the CPCB EPR portal | Needed only at R5 (resale and recycling). Partner with registered recyclers (Attero, Recykal) | Later (R5) | **[repo]** |
| Safety | A deterministic hard-stop layer for gas, refrigerant and high-voltage work. Map to **BIS IS 302** and **CEA 2023** safety norms. The hazard lexicon is signed off by an external safety expert | Built; sign-off budgeted | **[repo]** |
| WhatsApp Business policy | Approved templates outside the 24-hour window; **INR billing from 1 Jan 2026; non-INR accounts stop delivering from 1 Jan 2027** | Migrated to INR **[Story]** | **[repo]** |
| IP | Trademarks for Keepwell, Circuit and Mistri Gyan (classes 9, 42). Code and fault library assigned to the company. Model outputs never declare a part "compatible" without a technician's confirmation | Filing in Y1 | **[KB]** |
| Certifications | **ISO 27001 readiness** in Y2. SOC 2 later; Servify advertises SOC 2 Type II, and claims buyers will ask (R3) | Y2 / pre-R3 | **[repo]** gap |

### E. Data rights: who consents, to whom, for what (added after the Step 12 review)
"The record is the business" only holds if Keepwell has the right to use it. The rights are split by purpose:

| Data | Whose data | Keepwell's role | Basis | What happens if an agency leaves |
|---|---|---|---|---|
| Job intake, quotes, technician notes for *that agency's* service | Household (personal data) | **Processor** for the agency (the fiduciary) | Agency agreement with a data-processing clause; the household's notice from the agency | Returned to or deleted for the agency; Keepwell keeps no personal data |
| **De-identified repair outcomes**: model, fault, part fitted, did it hold, town, season (no name, phone or address) | Not personal data once de-identified | **Owner of the aggregate** that Mistri Gyan learns from | **Agency agreement grants Keepwell a perpetual licence to de-identified outcomes**; de-identification is tested (no re-identifiable fields) | **Stays in Mistri Gyan.** This is the compounding asset, and it survives churn |
| **Home Memory** (the household's own machine record) | Household | **Fiduciary** in Keepwell's own right, from R2 | **Separate, purpose-bound consent** from the household, directly to Keepwell, in 6 languages (pilot consent rate 74%) | **The household keeps its record** and can share it with any agency. We never lock households in |
| Plans, claims, data services (R2, R3, R8) | Household | Fiduciary | A separate consent per purpose, checked on every read; audit row per third-party read **[repo]** | Consent withdrawal stops that purpose |

**Controls in place today** (before the repo's full Foundations, which the seed funds). **All 14 paying agencies have signed the agency agreement, including the de-identified-outcomes licence.**
- consent log
- append-only job log
- paid-tier API keys only
- hazard list reviewed with a certified technician
- owner approval on every quote
- the team reviews outcomes weekly before anything enters Mistri Gyan

## 10.3 Trust by design (the product's responsible-AI controls, from the repo)
| Control | What it does |
|---|---|
| **Principle** | *"AI reads and drafts; rules decide anything with money, safety or legal effect."* |
| **Three decision tiers** | **T1 AI-only:** extraction, language ID. **T2 human approves:** quotes, warranty labels, fraud flags. **T3 human-only:** safety releases, legal matters, claim denials, minors. *The system never auto-denies a claim.* |
| **Safety hard-stops** | A rule layer *outside* the LLM; ~400 hazard terms × 6 languages; zero tolerance for false-accepts |
| **Grounded prices** | Quotes are computed by code from the agency's rate card; the model never invents a price |
| **Abstain and ask** | The target abstain band is 10–25%. Read-back on every voice note |
| **Against automation bias** | Evidence shown before the AI suggestion; the "accept" button is never pre-selected; seeded known-wrong cases; a healthy override band of 5–20% |
| **Prompt-injection defences** | Uploads are treated as data; extraction agents have no write tools; a `suspicious_upload` flag |
| **Validators on every field** | A null option and a schema validator (stops invented invoice numbers) |
| **Tenant isolation and secrets** | Row-level security, Secret Manager, optional CMEK, budget alerts at 50/80/100%, an audit row on every third-party read |
| **Eval release gates** | 100–200 golden cases per feature; LLM judge kappa ≥ 0.7 against humans; per-language gap ≤ 10 points |
| **Paid-tier only** | Free-tier keys may let a provider use content, so real data never goes on free keys |

**Pilot evidence (Step 6):** 0 false-accepts on the 200-case red-team set; 9 field hard-stops triggered; override 12%; abstain 18%. These are pilot-scale numbers, presented as such.

## 10.4 What compliance costs (already inside the Step 8 ask)
| Item | Y1 | Y2 |
|---|---|---|
| Seed transaction costs (legal due diligence, SSHA, stamp duty, valuer) | ₹8.0L | — |
| Lawyer: DPA, consent notices, terms, IRDAI opinion, legal-advice line | ₹4.0L | ₹3.0L |
| CA/CS retainer, registered valuer, trademarks, security review | ₹4.0L | ₹4.0L |
| DPDP readiness and ISO 27001 preparation | — | ₹3.0L |
| **Total (the model's "Compliance, legal, audit, IP" line)** | **₹16L** | **₹10L** |
| Safety-expert sign-off (in the PMF lane) | ₹4L | ₹3L |

## 10.5 Data room index (course M3, Pillar 4: "evidence behind every claim")
`/dataroom` at seed. Each folder maps to a pitch claim.

| # | Folder | Contents | Backs which claim |
|---|---|---|---|
| 1 | **Corporate** | MoA/AoA, CIN, PAN, DPIIT certificate, board resolutions, ROC filings, statutory registers, founders' agreement, IP assignment, iSAFE documents | Startup–Quality ("clean diligence") |
| 2 | **Cap table** | Fully diluted cap table, iSAFE conversion calculation, ESOP plan and grants (from `keepwell_model.xlsx`, Cap Table tab) | "No surprises" |
| 3 | **Financials** | Monthly books, bank statements, SISFS application (₹20L, under evaluation), 5-year model (`keepwell_model.xlsx`), budget vs actuals | Business model |
| 4 | **Market** | Bottom-up sizing workings (Step 4), sources: ICAP/CEEW, LocalCircles, BlueWeave, Servify estimate, CLASP/BEE survey | Market slide |
| 5 | **Customer evidence** | 18 interview notes, the household survey (19 responses) **[Real]**, consent log **[Real]**, pilot agreements, pilot dashboard export, invoices and UPI receipts | Traction slide |
| 6 | **Product** | Demo video, architecture (repo), feature spec (repo), eval reports and release gates, red-team results, hazard-lexicon sign-off | Solution, moat, trust |
| 7 | **Unit economics** | Pilot value calculation, cost-per-job measurements, cohort table, CAC by channel | Business-model slide |
| 8 | **Compliance** | DPA template, consent notices, privacy policy, security policy, incident runbook (DPDP 72h / CERT-In 6h), IRDAI opinion (when ready), GST/TDS returns | Trust slide |
| 9 | **Team** | Bios, references, employment contracts, ESOP grant letters, advisor agreements | Team slide |
| 10 | **Ask** | Use of funds (Step 8), milestone plan, term-sheet positions (Step 9) | Ask slide |

## 10.6 Weak points, said before an investor says them
| Weak point | Answer |
|---|---|
| "Are you DPDP-compliant?" | We are **consent-first by design, ahead of the May 2027 duties**. Roles (processor vs fiduciary) are being confirmed by counsel. We never claim certification we don't have |
| "Can you even sell plans?" | Not as an insurer. We distribute insurer-filed plans on commission, gated by a legal opinion |
| "What happens when the AI gets a gas leak wrong?" | It can't release a hazardous job: the hard-stop is outside the model, and safety calls are human-only (T3) |
| "Telugu voice data leaves India?" | Only the US/EU speech path does, redacted and with explicit consent. The production default stays in Mumbai |
| "If an agency churns, who owns its outcomes?" | De-identified outcomes stay in Mistri Gyan under the agency agreement's licence. Personal data goes back to the agency. Households keep their own record (10.2E) |

## 10.7 How it shows up in the pitch (Step 12)
- **Trust slide** (shared with Step 5): the principle line, the three tiers, the hard-stops, "hosted in Mumbai, consent-first ahead of DPDP 2027".
- **One line on the team slide:** "CIE-mentored, DPIIT-recognised, clean cap table, data room ready".
- **Appendix:** obligations table (10.2) and the data-room index (10.5).

Covers: M3 Pillar 3 (Compliance) and Pillar 4 (Data Room), and Startup–Quality ("governance, compliance, reporting readiness").
