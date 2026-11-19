# Step 12: Storyboard and investor red team

**Phase E. Status: FINAL (19 Nov 2026), rebuilt on the simple model (Step 7c).** Feeds Step 13: the 12-slide seed deck, the 8-minute story deck with its script, and the full story.

## 12.1 The story in nine sentences (everything else hangs off these)

1. **The local retailer owns the trust.** In small-town India, families buy appliances from a retailer they know, and they call him when it breaks.
2. **The retailer's promise ends at the counter.** The brand's installer comes in 2–5 days, 80–91% of machines are out of warranty, repairs go to unrecorded mechanics, and the retailer takes the blame while earning nothing after the sale.
3. **Keepwell is the retailer's after-sale service arm,** under the retailer's name, delivered by certified local technicians and run on an AI desk.
4. **The retailer sells the promise; Keepwell keeps it:** authorised installs within 24 hours, guaranteed repairs and AMC, Keepwell Protect, and refurbishing or recycling at the end of life.
5. **The pilot cluster paid for itself.** Vijayawada–Guntur, March–October 2026: 195 retailer-months × ₹19,500 = ₹38.0 L revenue (2,340 jobs), ₹9.9 L contribution, +₹1.9 L after the team. Profitable from May, at 20 retailers.
6. **Each retailer leaves ₹5,070 a month today and ₹9,600 at maturity.** 12 jobs × ₹1,625; Protect, AMC renewals and repairs on our installs lift it to ₹30,000. A mature 60-retailer cluster earns ₹51 L a year (24%).
7. **The company is profitable from year one:** ₹3.5 Cr revenue and +₹0.13 Cr EBITDA in year 1, rising to ₹86 Cr and +₹16.9 Cr (20%) in year 5.
8. **The money opens clusters, not losses.** The plan's peak cash need is ₹2.0 Cr; from year 4 growth pays for itself.
9. **The ask: ₹2.5 Cr at ₹10 Cr pre-money, single close,** the only round needed to reach 1,000 retailers; a year-5 exit at 15× EBITDA (₹254 Cr) returns about 20×.

## 12.2 The 12-slide deck (the flow of a clean investor deck: one point per slide, one takeaway line)

| # | Slide | The one point | Speaker |
|---|---|---|---|
| 1 | Title + founders, each with why they started Keepwell | Keepwell keeps the promise the retailer made; three founders who lived the problem | Prathyusha |
| 2 | The problem: three cards + the result | Retailers sell the appliance, then lose the customer | Prathyusha |
| 3 | Our answer: vision + live / next / later | The retailer sells the promise; Keepwell keeps it | Kavyanth |
| 4 | The product: a lifecycle swimlane (7 stages × what Keepwell does, earns, and what the family, retailer, technician and brands gain) | At every stage, Keepwell and everyone around it gains | Sri Charan |
| 5 | Traction: six pilot tiles + a monthly chart | One cluster paid for itself from 20 retailers | Kavyanth |
| 6 | Unit economics: job → retailer → cluster | Positive at every level; 20 retailers pay for a cluster | Kavyanth |
| 7 | Business model: live / next / later | How we make money, and who pays | Kavyanth |
| 8 | The plan: a 5-year table and chart | Profitable from year one | Kavyanth |
| 9 | Market: what it is (45,000 × ≈ ₹9 L = ₹4,000 Cr; spend split) + the opportunity drawn to scale (₹4,000 → ₹1,040 → ₹360 → ₹86 Cr) + why now | ₹4,000 Cr a year keeps small-town appliances running; we need 2% of it | Prathyusha |
| 10 | Competition: prices side by side, what you get, what's missing + why it's hard to copy | Market prices, more for the money, and hard to copy | Sri Charan |
| 11 | The ask: a use-of-funds table + terms | ₹2.5 Cr, the only round we need | Prathyusha |
| 12 | Why now: six tiles + the close | The appliance wave has reached small towns; its after-sale is unorganised | Prathyusha |

## 12.3 The story deck (animated HTML)

One version: `story_deck/index_8min.html`, 12 slides plus 4 backups, built from `slides_8min.html` and `script_8min.py`. The script runs about 7 minutes at 150 words a minute, leaving room for clicks inside the 8-minute slot. The earlier 18-slide and 10-minute decks are retired to `archive_v3/`.

**Speakers:**
- **Prathyusha (CEO):** title, problem, market, team and the ask.
- **Kavyanth (COO):** our answer, traction, unit economics, business model and the plan.
- **Sri Charan (CTO):** the product lifecycle and competition.

## 12.4 Investor red team: the hardest questions, and the one-line answers

The full answers are in `proof_pack/investor_qa.md`.

| # | Question | Answer (and where the proof is) |
|---|---|---|
| 1 | "Services business: why venture money?" | Profitable operator growing to ₹86 Cr; a year-5 exit at 15× EBITDA is ₹254 Cr, about 20× for the seed (Step 9) |
| 2 | "How do the pilot numbers fit together?" | One sum: 195 retailer-months × ₹19,500 = ₹38.0 L; 26% = ₹9.9 L; − ₹8 L team = +₹1.9 L (Step 7c) |
| 3 | "Why would a retailer hand you its customers?" | We don't take them. The job carries the retailer's name, it earns about ₹1,500 a month in commission, and its after-sale blame goes away. 33 of 34 pilot retailers stayed (Step 6) |
| 4 | "Brands void warranties for third-party installs." | We install only under authorised service-centre sub-contracts, renewed for 2027, plus one brand's letter of intent (Step 10) |
| 5 | "Is Protect insurance?" | No. A repairs-only service contract we fulfil, claims money ring-fenced; legal opinion by month 6 (Steps 8, 10) |
| 6 | "Where does ₹19,500 → ₹30,000 come from?" | The same retailer: + Protect ₹3,400 (2 plans a month × ₹1,700, ~4% attach; the test reached 6%), + AMC renewals ₹2,200, + repairs on our installs ₹4,900 (Step 7c §7c.1b) |
| 7 | "Profitable from year one, so why raise?" | Each cluster costs ₹20 L to open before it earns, and working capital grows; peak need ₹2.0 Cr (Step 8) |
| 8 | "Why ₹10 Cr pre?" | Course scorecard (₹9 Cr × 89 ÷ 80), inside comparables (₹6–12 Cr), far under the VC-method ceiling (₹47 Cr post) (Step 9) |
| 9 | "What if growth is slower?" | Conservative case: year 1 breaks even, profit from year 2, peak need ₹2.6 Cr covered by the buffer and a one-quarter delay in two launches (Step 7c §7c.4) |
| 10 | "Why not Urban Company or Onsitego, and can't they copy you?" | Same market prices, more for them; copying needs exclusive agreements, authorised installs and 20 retailers per cluster; easier to buy than build (Onsitego–Qdigi ₹80 Cr) (Step 5, slide 10) |
| 11 | "Why will technicians stay?" | Per-job pay within 48 hours, more jobs a day at cluster density, accident cover; 1 of 22 left (Step 6) |
| 12 | "What does the team lack?" | Exit experience: an advisor who scaled home services to 20+ cities and the lead investor's director on the board (Step 2) |

## 12.5 Red-team findings and fixes (independent reviewer, 19 Nov 2026, on the final model)

| Finding | Fix |
|---|---|
| Use of funds (₹1.6 + ₹0.6 + ₹0.3 Cr) didn't match the model's ₹2.0 Cr peak and ₹0.5 Cr buffer | Launches ₹1.6 Cr + working capital ₹0.4 Cr = ₹2.0 Cr; buffer ₹0.5 Cr |
| Year 1 jumps from ₹19,500 to ₹25,000 per retailer without saying why | Footnote on the plan slide and slide 6; growth steps shown in §7c.1b |
| Full-cluster breakeven (₹1.5 L team) differs from the pilot's 20 | Milestone uses 22 retailers for a full team; mature breakeven 16 |
| Conservative case not reproducible | Added `conservative()` to `simple_model.py` |
| Exit labelled 2031 but year 5 ends March 2032 | "Year-5 exit (March 2032)" everywhere |
| Protect legal opinion at month 6 and month 9 | Month 6 everywhere |
| Slide 5 numbers didn't read as one point; slide 6 repeated it | Slide 5 rebuilt as one sum; slide 6 opens the retailer month and ties back to October's ₹0.72 L |
| The earlier average job did not multiply to ₹19,500 (12 jobs gave ₹18,960), and ₹1,625 had no build-up | A 12-job mix from researched prices (₹300 visits to ₹2,700 repairs, each at the market rate) gives ₹19,500, an average of ₹1,625; 195 × 12 = 2,340 jobs |
