# Data room index (course M3, Pillar 4: proof for every claim)

> [Story] items are illustrative for the course. Every slide number maps to a row in `../claims_ledger.csv`.

| Folder | Contents | Proves | Where in this repo |
|---|---|---|---|
| 1. Corporate | Incorporation, MoA/AoA, DPIIT, board minutes, founders' agreement (38/31/31, vesting from Aug 2025), iSAFE, cap table | A clean company; a cap table with no surprises | `steps/02`, `steps/09`, `keepwell_model.xlsx` Funding sheet |
| 2. Team | Founder bios and references, advisor letters, hiring plan | Why this team | `steps/02`, `steps/08 §8.3` |
| 3. Market | TAM/SAM/SOM workbook, research sources, household survey and interviews [Real] | ≈ ₹4,000 Cr TAM | `steps/04`, `research/`, `proof_pack/voice_of_customer.md` |
| 4. Product | AI-desk walkthrough, job-flow specs, guardrail rules, appliance-record schema | Product fit | `steps/05`, `proof_pack/demo_walkthrough.md` |
| 5. Traction | Pilot ledgers by month [Story], shop agreements, Protect counter-test log, scorecard with misses | 34 shops, ₹25 L, 6% attach | `steps/06` |
| 6. Financials | `keepwell_model.xlsx` (4 scenarios plus the Funding sheet; 0 formula errors, 0 mismatches with Python), monthly cash profile, FY26 accounts [Story] | Unit economics, the ask, returns | `keepwell_model.xlsx`, `model/` |
| 7. Contracts | Shop agreement, service-centre sub-contracts (renewed for 2027), partner-cluster template, Protect terms, insurance | Authorisation, partners, Protect | `steps/03`, `steps/07b`, `steps/10` |
| 8. Compliance | Protect legal opinion (a seed milestone), DPDP policy and consent flow, gig-levy workings, safety SOPs, complaints log | Hygiene | `steps/10` |
| 9. Consistency | Claims ledger and the automated check | Every number traces to a source | `claims_ledger.csv`, `check_consistency.py` |
