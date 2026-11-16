# Step 13 — Build the deck and outputs
**Phase E: Assemble and stress-test · Status: DONE 16 Nov 2026**
> **Illustrative case.** Founder histories, the company timeline, the pilot results and the financials are assumptions made for the IIIT Hyderabad ESFS course pitch. They are kept consistent with the team repo and with each other.
**Plan:** [`../pitch_bible.md`](../pitch_bible.md) · **Builds on:** Steps 1–12 (locked, with review fixes applied)

## 13.1 What was built
| Output | File | How it's made |
|---|---|---|
| **Pitch deck (PowerPoint)**: 16 main slides + divider + 16 appendix slides, with speaker notes on every main slide and native, editable charts | `../deck/Keepwell_Seed_Deck.pptx` | `../deck/build_deck.py` from `../deck/deck_content.py` |
| **Pitch deck (PDF)** | `../deck/Keepwell_Seed_Deck.pdf` | LibreOffice conversion of the .pptx |
| **Animated web deck**: one self-contained HTML file. Elements animate in; charts draw themselves; light/dark theme; speaker notes on **N**; arrows, space, swipe or the on-screen buttons to move; prints to PDF | `../deck/Keepwell_Seed_Deck.html` | Same builder, same content file |
| **Financial model**: 12 tabs, 530+ formulas, all checks OK | `../keepwell_model.xlsx` | `../build_model.py` |
| **Proof pack**: data-room index, investor Q&A bank, voice of the customer, demo walkthrough script | `../proof_pack/` | Step 12.5 |
| **Presenter's script** (what we say, slide by slide) | `../KEEPWELL_PITCH_STORY.md` | Combines Steps 1–13 into one telling |
| **The whole story for an outsider**, with every proof linked | `../KEEPWELL_FULL_STORY.md` | One narrative across all steps, the model and the proof pack |

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
| Model recalculation | 530+ formulas, **0 errors** |
| Model checks tab | Use of funds 100% ✓ · ask ≥ gap ✓ · cap table 100% (seed and post-B) ✓ · seed shares × price = investment ✓ · iSAFE converts at cap ✓ · SOM 16.9% ≤ 20% ✓ · Series A needed after runway (expected) |
| Visual check of every PDF page (contact sheets) | Fixed in this pass: negative EBITDA bars rendered upward in the PDF (replaced with a signed EBITDA row); low-contrast labels on the ask tiles; overlapping chart labels; three appendix headlines with pre-review numbers |
| Web deck in headless Chrome (slides 1, 7, 11, 13) | Renders and animates; charts draw; navigation and notes work |
| Number consistency across documents | One regeneration pass after the investor review (Step 12.7) |
| Disclosure | Appendix A16 states what is real and what is illustrative for the course case |

## 13.4 Final numbers (as pitched)
| | |
|---|---|
| Ask | **₹4.75 Cr seed** (minimum close ₹4.0 Cr), priced CCPS, **one lead seed VC**, 24-month runway |
| Valuation | **₹19 Cr pre-money / ₹23.75 Cr post-money**, 20.0% to the lead at ₹107.51 per share; never above the VC-method price; walk-away floor ₹16 Cr pre |
| Investor return (base case) | ~35% IRR, 6.2x (₹215.5 Cr exit in year 6 at 7x revenue) |
| Use of funds (by purpose) | PMF 38% · team and company 28% · product 23% · marketing and sales 10% · working capital 1% (+10% contingency) |
| Company so far | Incorporated May 2025; ₹55L raised (founders ₹15L, iSAFE ₹30L, SISFS ₹10L of ₹20L); ~₹34L spent; ~₹21L in the bank |
| Traction (Nov 2026) | 14 paying agencies (1 churned of 15) · ~8,200 jobs · one-visit closure 71% → 83% held 6 months · root-cause 62% → 78% (gate passed) · ~₹59k MRR |
| Unit economics (observed inputs) | ARPA ₹4,216/month · 81% contribution · CAC ~₹17,900 · payback 6.3 months · LTV:CAC 6.3x |
| Plan | 14 → 3,793 paying agencies; revenue ₹0.2 Cr → ₹19.2 Cr; EBITDA +₹2.6 Cr in Y5; 34 lakh machine records |
| Market | 37,500 agencies (TAM) → 22,500 Tier 2/3 (SAM) → 1,400 beachhead; earnable pool ₹1,005–2,370 Cr a year |
| Fundability self-score | 78 / 100 |
