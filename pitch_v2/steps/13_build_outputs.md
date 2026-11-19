# Step 13: The outputs

**Phase E. Status: DONE (19 Nov 2026), rebuilt on the simple model and the 12-slide flow.**

| Output | File(s) | Built by |
|---|---|---|
| **Seed deck, 12 slides** | `deck/Keepwell_Seed_Deck.pptx` · `.pdf` | `deck/build_deck.py` from `deck/deck_content.py` |
| **Story deck, 8 minutes, 12 slides** (animated) + the explained script | `story_deck/index_8min.html` · `story_deck/SCRIPT_8MIN.md` | `story_deck/build_8min.py` from `slides_8min.html` + `script_8min.py` |
| **Financial model** | `keepwell_model.xlsx` (141 formulas, 0 errors) | `model/build_model_v4.py` from `model/simple_model.py`; `verify_model_v4.py` finds 0 mismatches |
| **The story** | `steps/Entire story.md` (also `KEEPWELL_FULL_STORY.md`) | Written from Steps 1–12 |
| **Proof pack** | `proof_pack/*.md` | Q&A, voice of the customer, data room, demo |
| **Claims ledger** | `claims_ledger.csv` | Every number on every slide, with its source |

**Retired:** the earlier 18-slide and 10-minute story decks and the earlier deck builder are in `archive_v3/`.

**The story in six links:**
1. Retailers lose the customer after the sale.
2. Keepwell is their after-sale arm for the appliance's whole life.
3. The pilot cluster paid for itself from 20 retailers.
4. Each retailer adds ₹5,000 a month.
5. The company is profitable from year 1.
6. ₹2.5 Cr opens 8 clusters and is the only round needed.
