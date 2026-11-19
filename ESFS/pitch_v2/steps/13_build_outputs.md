# Step 13: The outputs

**Phase E. Status: DONE (20 Nov 2026).** Every output is generated from one source, and `check_consistency.py` checks it against the model (0 problems).

| Output | File(s) | Built by | Notes |
|---|---|---|---|
| **Seed deck: 12 slides + 3 appendix** (the structure of the founders' idea document §16, ordered for investors) | `deck/Keepwell_Seed_Deck.pptx` · `.pdf` · `.html` | `deck/build_deck.py` from `deck/deck_content.py` | Speaker notes in the pptx. HTML: arrow keys or click |
| **Story deck, full** (animated) | `story_deck/index.html` · `story_deck/SCRIPT.md` | `story_deck/build_story_deck.py` from `slides.html` + `script_data.py` (the v1 visual engine) | 18 slides + 4 backup, about 12½ minutes. **F** full screen, **N** notes, **B** backup |
| **Story deck, 10-minute** | `story_deck/index_10min.html` · `story_deck/SCRIPT_10MIN.md` | same | 14 slides, about 10½ minutes (4 slides folded) |
| **Full story** | `KEEPWELL_FULL_STORY.md` | hand-written from Steps 1–12 | The narrative, start to close |
| **Proof pack** | `proof_pack/investor_qa.md` · `voice_of_customer.md` · `data_room_index.md` · `demo_walkthrough.md` | hand-written | 15 Q&As; real household quotes; data-room map; 2-minute demo script |
| **Financial model** | `keepwell_model.xlsx` | `model/build_model_v3.py` (+ `rounds.py`) | 679 formulas, 0 errors; 4 scenarios; Funding sheet (rounds, cap table, returns, VC method); `verify_model_v3.py` gives 0 mismatches |
| **Claims ledger** | `claims_ledger.csv` | hand-written | 40 claims, each with value, source, tag and where it is used |
| **Pitch bible v2** | `pitch_bible.md` | — | All steps final; Gate 3 done |

**Media:** `story_deck/media/` holds redacted real household evidence. It is git-ignored, so copy the folder to the presenting laptop.

**Archive (Gate 3):** the v1 agency/Circuit pitch is now in `pitch/archive/v1_agency/` (README inside).

## How the story hangs together (one line per link)

1. **Problem → solution:** the shop's promise ends at the counter → Keepwell is the shop's after-sale arm.
2. **Solution → proof:** the pilot [Story] shows that shops route jobs (58%) and that families buy Protect (6%).
3. **Proof → economics:** pilot inputs drive the model. Clusters earn 16% on service; Protect, the commission shift, central parts buying and partners fix Step 7's thin margins (Step 7b).
4. **Economics → ask:** the course method (one-year need plus runway) gives ₹2.44 Cr, so we ask for ₹2.5 Cr.
5. **Ask → milestones → next round:** five month-18 milestones, set on the stress path, earn Round 2 (₹5 Cr).
6. **Rounds → vision:** Serve → Supply → Know → Circulate, a year-7–8 exit, and the close line: *"Keepwell keeps the promise the shop made when it sold the appliance."*
