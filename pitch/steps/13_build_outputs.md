# Step 13 — Build the deck and outputs
**Phase E: Assemble and stress-test · Status: DONE 16 Nov 2026**
**Plan:** [`../pitch_bible.md`](../pitch_bible.md) · **Builds on:** Steps 1–12 (locked, with review fixes applied)

## 13.1 What was built
| Output | File | How it's made |
|---|---|---|
| **Pitch deck (PowerPoint)**: 16 main slides + divider + 16 appendix slides, with speaker notes on every main slide and native, editable charts | `../deck/Keepwell_Seed_Deck.pptx` | `../deck/build_deck.py` from `../deck/deck_content.py` |
| **Pitch deck (PDF)** | `../deck/Keepwell_Seed_Deck.pdf` | LibreOffice conversion of the .pptx |
| **Animated web deck**: one self-contained HTML file. Elements animate in; charts draw themselves; light/dark theme; speaker notes on **N**; arrows, space, swipe or the on-screen buttons to move; prints to PDF | `../deck/Keepwell_Seed_Deck.html` | Same builder, same content file |
| **Financial model**: 12 tabs, 528 formulas, all checks OK | `../keepwell_model.xlsx` | `../build_model.py` |
| **Proof pack**: data-room index, investor Q&A bank, voice of the customer, demo walkthrough script | `../proof_pack/` | Step 12.5 |
| **The full story, end to end** | `../KEEPWELL_PITCH_STORY.md` | Combines Steps 1–13 into one telling |

**One source of truth.** All three deck formats are generated from **one content file** (`deck_content.py`), so they can't disagree. Every number in that file traces to the model or a locked step document.

## 13.2 How to rebuild
```bash
# model (writes keepwell_model.xlsx; recalc with LibreOffice to cache values)
python build_model.py keepwell_model.xlsx
# deck (writes .pptx and .html), then PDF
cd deck && python build_deck.py . && soffice --headless --convert-to pdf Keepwell_Seed_Deck.pptx
```
Requires `openpyxl`, `python-pptx` and LibreOffice.

## 13.3 Checks run before shipping
| Check | Result |
|---|---|
| Model recalculation | 528 formulas, **0 errors** |
| Model checks tab | Use of funds 100% ✓ · ask ≥ gap ✓ · cap table 100% (seed and post-B) ✓ · seed shares × price = investment ✓ · iSAFE converts at cap ✓ · SOM 16.8% ≤ 20% ✓ · Series A needed after runway (expected) |
| Visual check of every PDF page (contact sheets) | Fixed in this pass: negative EBITDA bars rendered upward in the PDF (replaced with a signed EBITDA row); low-contrast labels on the ask tiles; overlapping chart labels; three appendix headlines with pre-review numbers |
| Web deck in headless Chrome (slides 1, 7, 11, 13) | Renders and animates; charts draw; navigation and notes work |
| Number consistency across documents | One regeneration pass after the investor review (Step 12.7) |
| Disclosure | Appendix A16 states what is real and what is illustrative for the course case |

## 13.4 Final numbers (as pitched)
| | |
|---|---|
| Ask | **₹4.75 Cr seed**, priced CCPS, 24-month runway |
| Valuation | **₹20 Cr pre-money / ₹24.75 Cr post-money**, 19.2% to seed investors at ₹113.33 per share; walk-away floor ₹16 Cr pre |
| Investor return (base case) | ~37% IRR, 6.7x (₹243.5 Cr exit in year 6 at 7x revenue) |
| Use of funds (by purpose) | PMF 38% · team and company 28% · product 23% · marketing and sales 10% · working capital 1% (+10% contingency) |
| Pilot | 5 agencies, 4 weeks, ~410 jobs, one-visit closure 71% → 84%, 96% of requests captured, 5 of 5 first invoices paid (~₹20,000 billed) |
| Unit economics | ARPA ₹4,856/month · 81% contribution · CAC ~₹17,900 · payback 5.6 months · LTV:CAC 7.3x |
| Plan | 72 → 3,789 paying agencies; revenue ₹0.18 Cr → ₹21.7 Cr; EBITDA +₹4.7 Cr in Y5; 39 lakh machine records |
| Market | 37,500 agencies (TAM) → 22,500 Tier 2/3 (SAM) → 1,400 beachhead; earnable pool ₹1,005–2,370 Cr a year |
| Fundability self-score | 76 / 100 |
