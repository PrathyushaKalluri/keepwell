# Keepwell seed pitch: the 10-minute deck script
> **Illustrative case.** Founder histories, the company timeline, the pilot results and the financials are assumptions made for the IIIT Hyderabad ESFS course pitch. The research, the household quotes, the photo and video evidence and the Circuit prototype are real.

**Deck:** [`index.html`](index.html). Open it in Chrome and press **F** for full screen and **N** for these notes. **→ / space** moves to the next click, **←** goes back, **B** opens the backup slides (valuation, cap table, terms; Q&A only).
**Generated** from [`script_data.py`](script_data.py) by [`build_story_deck.py`](build_story_deck.py), so the deck's speaker notes and this script are always the same words.

## The rule for every slide: the screen proves, the voice explains
- **SHOW** is the proof: a picture, a number, a real artefact, something to interact with. It is never read aloud.
- **SAY** is the explanation: what it means and why it matters. It says what the screen can't.
- When the two say the same thing, it's on purpose: only for the one line we want remembered (the hook, the insight, the ask, the close).
- `[click]` in SAY means press → once to reveal the next part of the slide.

## Timing and speakers
- **16 slides, about 9:55** at a calm 145 words a minute, including clicks. Built to fit a 10-minute slot.
- **If you're running long:** say only the first paragraph of each SAY block on slides 6, 11 and 12; never cut slides 2, 9 and 14.
- **Prathyusha (CEO):** about 4:36
- **Sri Charan (CTO):** about 2:43
- **Kavyanth (COO):** about 2:36

**Hand-overs** are built into the words. Sri Charan starts with "I'm Sri Charan." Kavyanth starts with "I'm Kavyanth." Prathyusha takes the ask with "So here's our ask."

## How the 31-slide story became 16 slides without losing the crux
| 10-minute slide | Carries these slides from the full deck |
|---|---|
| 1 Hook | Hook |
| 2 Ramagundam | Ramagundam |
| 3 Team | Team |
| 4 What we saw and heard | Evidence wall + listening + the insight |
| 5 The problem, mapped and sized | Problem map + both sides + the 15-crore numbers (+ the whole-life idea in the speech) |
| 6 Keepwell + roadmap | Keepwell + vision + roadmap |
| 7 Where we are | Company stage, journey, angel round, money |
| 8 Circuit | Why repair + Circuit's six steps + the live site + ease of use |
| 9 The proof | Price test + traction + the learning curve |
| 10 The engine | Value to the agency + unit economics + growth from capacity |
| 11 Why we win | Competition map + moat + the five forces in one line |
| 12 How big | Market funnel + the stage-by-stage plan |
| 13 What we need | The requirement bridge + use of funds + compliance |
| 14 The ask | The ask, on its own page |
| 15 Why now + exit | Why now + path to Rs 100 Cr + who buys |
| 16 Close | Back to Ramagundam |

**The rule on every slide:** the screen carries the numbers and the proof; the voice carries the logic. We never read the screen aloud, so two or three old slides fit into one.

## Overview: show vs say
| # | Act | Slide | Speaker | Time | What we SHOW (the proof) | What we SAY (the point) |
|---|---|---|---|---|---|---|
| 1 | The hook | **Every repair in your home starts from zero** | Prathyusha | 0:38 | An illustrated home with eight machines… | “Before we begin, think about your own home…” |
| 2 | The hook | **We took it lightly too — until Ramagundam** | Prathyusha | 0:48 | Left: Sri Charan's quote card, "Our machines cost my family ₹10,000 a month… | “We took this lightly too…” |
| 3 | The team | **Three founders, one from each side** | Prathyusha | 0:37 | A triangle around "the machine record": Prathyusha (agency network: FixNear, 1,200 technicians, sold 2022), Sri Charan (household + AI: 7 years of voi… | “That afternoon is why the three of us are here, and each of us has lived one side of it…” |
| 4 | The problem | **What we saw, and what we heard** | Sri | 0:50 | The proof wall: the real brand WhatsApp-bot recording playing ("API issue" → "My request was not done"), the agency sticker on a purifier with the dat… | “I'm Sri Charan…” |
| 5 | The problem | **The problem, mapped and sized** | Sri | 0:41 | Five counters across the top: 15 Cr repairs a year / 27 Cr machines with no record / Rs 550 Cr wasted on repeat trips / 37,500 agencies on a notebook … | “Then we mapped the whole problem, and it isn't one problem: it's thirteen…” |
| 6 | Keepwell | **Keepwell, and the roadmap** | Sri | 0:28 | Dark slide… | “So we built Keepwell: one living record for every machine in an Indian home, built with the owner's consent…” |
| 7 | Where we are | **Where we are** | Prathyusha | 0:32 | A three-step stage path, with "2 · Find the business model — we are here" highlighted… | “Where are we? Stage two…” |
| 8 | Circuit | **Circuit, and how easy it is** | Sri | 0:44 | Left: six step cards (voice note → understands → fault + part → quote from the rate card → job card → technician verifies, we earn ₹40)… | “Here's Circuit…” |
| 9 | The proof | **The proof** | Kavyanth | 0:46 | Left: the price test, ₹40 → 2.0× value vs ₹100 → 0.81×, the quote "It takes too much of a small job", and the stamp "₹40 for everyone since May"… | “I'm Kavyanth…” |
| 10 | The proof | **The agency wins. So do we.** | Kavyanth | 0:43 | Value bars per agency per month: recovered jobs ₹2,400 + trips avoided ₹2,150 (measured) + owner time ₹2,925 (self-reported) vs our fee ₹3,690 (₹100 f… | “Does the agency win? From system logs alone, recovered jobs and saved trips are worth four and a half thousand rupees a …” |
| 11 | Why we win | **Why we win** | Kavyanth | 0:32 | The competitor map: Urban Company, Servify, Zoho, Fieldproxy and Bernard each in their slice, with Keepwell pulsing alone in the "serves the agency × … | “Why hasn't anyone solved this? Everyone holds a slice…” |
| 12 | Why we win | **How big, and the plan** | Kavyanth | 0:35 | Left: the funnel 37,500 → 22,500 → 1,400 → 120 (Series A gate), with the Keepwell earnable pool ₹1,005–2,370 Cr a year beneath… | “How big? We counted India's repair agencies three ways: thirty-seven thousand five hundred, with twenty-two thousand fiv…” |
| 13 | The ask | **What we need** | Prathyusha | 0:30 | The bridge chart: costed needs ₹548 L + 10% contingency − revenue − cash − grant due = gap ₹467 L → ask ₹475 L… | “Now, what we need…” |
| 14 | The ask | **The ask** | Prathyusha | 0:32 | A full dark page: ₹4.75 Cr, "to take Circuit from 14 agencies to ~260, and reach the Series A from strength." The bridge line, then four terms: 24 mon… | “So here's our ask…” |
| 15 | The future | **Why now, and who buys** | Prathyusha | 0:33 | Left, Why now: Rs 4.5 (AI is finally cheap) / 1 in 10 (the repair wave is ahead) / 2027 (data law arrives) / R2R (repair is opening up)… | “Why now? Indian-language AI just got cheap: a job costs us four and a half rupees, and we charge forty…” |
| 16 | The future | **Back to Ramagundam** | Prathyusha | 0:26 | Dark slide… | “Back to Ramagundam…” |

## Slide by slide

---
### Act: The hook

#### 1. Every repair in your home starts from zero
**Speaker:** Prathyusha (CEO) · **Time:** ~0:38

| 🖥 SHOW (on screen, the proof) | 🎙 SAY (word for word, the explanation) |
|---|---|
| An illustrated home with eight machines. The presenter taps each machine as the audience calls it out; a red counter adds up "repairs in your home this year". [click] Question tags drop onto every machine: "Last service? Which part? What did you pay?" [click] The line: "Every repair in your home starts from zero." | Before we begin, think about your own home. This year, what broke? The AC? The fridge? The purifier, the geyser? [tap the machines as people answer]<br><br>Now pick one. When was it last serviced? Which part was changed? What did you pay? [click]<br><br>Most of us don't know. It's in a phone, a diary, or nowhere.<br><br>Every repair in your home starts from zero. |

**Why this works:** The room answers before we say a word about ourselves, so the problem is theirs from the first 30 seconds.

#### 2. We took it lightly too — until Ramagundam
**Speaker:** Prathyusha (CEO) · **Time:** ~0:48

| 🖥 SHOW (on screen, the proof) | 🎙 SAY (word for word, the explanation) |
|---|---|
| Left: Sri Charan's quote card, "Our machines cost my family ₹10,000 a month. Never evenly." Right, one beat per click: 46 °C and a fever → 14 missed calls → the son 700 km away → 2 nights in the heat → "Nobody is the villain. The system has no memory." The ₹350 / ₹38,000 detail is a small footnote in the last card. | We took this lightly too. Sri Charan's family spends about ten thousand rupees a month on its machines, and we called that normal. Then, Ramagundam. [click]<br><br>Forty-six degrees. A seventy-four-year-old retired miner, home alone, with a fever. His AC stops. Ramesh, the one technician he trusts, is up a ladder across town. Fourteen missed calls. His son, seven hundred kilometres away, calls everyone. Nobody knows what's wrong, or who's coming. The old man spends two nights in that heat.<br><br>The fault was a three-hundred-and-fifty-rupee part. Nobody was the villain. The system has no memory, and when it has no memory, it's people who suffer first. |

**Why this works:** The hook is the human cost, not the money. One concrete story everyone can picture.

---
### Act: The team

#### 3. Three founders, one from each side
**Speaker:** Prathyusha (CEO) · **Time:** ~0:37

| 🖥 SHOW (on screen, the proof) | 🎙 SAY (word for word, the explanation) |
|---|---|
| A triangle around "the machine record": Prathyusha (agency network: FixNear, 1,200 technicians, sold 2022), Sri Charan (household + AI: 7 years of voice AI, built Circuit), Kavyanth (brand + warranty: 300+ service partners, closed 8 of our last 10 agencies). Ribbon: full-time since May 2025 · ₹15 L of our own money · CIE-IIITH · DPIIT. | That afternoon is why the three of us are here, and each of us has lived one side of it. I'm Prathyusha. I co-founded FixNear, a network of twelve hundred technicians in these same towns, and sold it in 2022. Sri Charan spent seven years on Indian-language voice AI and built our product himself. Kavyanth ran a brand's network of three hundred service partners and its warranty desk. All three of us have been full-time since May 2025, with our own money in. |

**Why this works:** Team is 45 of 90 points on the course matrix. Placed right after the story, the founders land as witnesses, each with one line of proof.

---
### Act: The problem

#### 4. What we saw, and what we heard
**Speaker:** Sri Charan (CTO) · **Time:** ~0:50

| 🖥 SHOW (on screen, the proof) | 🎙 SAY (word for word, the explanation) |
|---|---|
| The proof wall: the real brand WhatsApp-bot recording playing ("API issue" → "My request was not done"), the agency sticker on a purifier with the date in marker, the repair diary, the gas cylinder, our whiteboard. Research chips: 19 survey responses · 7 household interviews · 18 agency owners. Three named quotes underneath. [click] Teal band: "Nothing in a repair can be checked, so people trust the person. We make that agency the smartest in town." 44% local · 76% avoid brand service. | I'm Sri Charan. We didn't read about this. We watched it. This is a real brand's WhatsApp bot, recorded in an interview: an "API issue", a job ID she doesn't have, and then, "my request was not done." And look at what families do instead: an agency's sticker on the purifier, the next date in marker, a handwritten repair diary.<br><br>We listened for four months: a survey, seven households, eighteen agency owners. [click] It all said one thing. Nothing in a repair can be checked, so people trust the person. Forty-four percent stay with their local agency. So we don't replace that agency. We make it the smartest one in town. |

**Why this works:** Real evidence plus the insight, merged into one slide. The video playing does the work while the voice explains what it means.

#### 5. The problem, mapped and sized
**Speaker:** Sri Charan (CTO) · **Time:** ~0:41

| 🖥 SHOW (on screen, the proof) | 🎙 SAY (word for word, the explanation) |
|---|---|
| Five counters across the top: 15 Cr repairs a year / 27 Cr machines with no record / Rs 550 Cr wasted on repeat trips / 37,500 agencies on a notebook / 1 in 8 requests lost. Below: all 13 problems in plain words, in three columns (the repair shop, the family, brands-insurers-recyclers), each tagged with the letter of the scenario that solves it; A (the prepared visit) glows. [click] Band: We start with A, the prepared visit. | Then we mapped the whole problem, and it isn't one problem: it's thirteen. For the repair shop, calls get lost and the first visit goes in blind. For the family, nobody keeps the machine's history or knows a fair price. For insurers, claims can't be verified.<br><br>And the scale is real: fifteen crore repairs a year, twenty-seven crore machines with no record, five hundred and fifty crore rupees lost to repeat trips. [click]<br><br>We start with A, the prepared visit, because it hurts most and is easiest to fix. |

**Why this works:** All 13 problems in plain words, tagged with the solution letter, under the scale numbers: the whole problem set in one picture, readable in seconds.

---
### Act: Keepwell

#### 6. Keepwell, and the roadmap
**Speaker:** Sri Charan (CTO) · **Time:** ~0:28

| 🖥 SHOW (on screen, the proof) | 🎙 SAY (word for word, the explanation) |
|---|---|
| Dark slide. Left: the Keepwell mark, "The care layer for everything a home owns", one living record per machine, and the chips CIBIL → borrowers · Carfax → used cars · Keepwell → household machines. Right: the roadmap as six rows, each with a payer: R1 Circuit (live) · R2 Home Memory + Plans · R3 Claims triage · R4 Parts · R5 Resale & recycling · Phase 3 Data services. | So we built Keepwell: one living record for every machine in an Indian home, built with the owner's consent. The CIBIL of household machines.<br><br>Each scenario becomes a product on that record, and each has its own payer. Circuit for repair agencies, live today. Then home memory and service plans, sold for insurers. Then claims, parts, and resale and recycling. |

**Why this works:** The name, the vision and the roadmap land together, as the answer to the problem slide before it.

---
### Act: Where we are

#### 7. Where we are
**Speaker:** Prathyusha (CEO) · **Time:** ~0:32

| 🖥 SHOW (on screen, the proof) | 🎙 SAY (word for word, the explanation) |
|---|---|
| A three-step stage path, with "2 · Find the business model — we are here" highlighted. The journey timeline from discovery (Jan 2025) to raising the seed (Nov 2026), including the ₹30 L angel round. Three tiles: Raised ₹55 L → Spent ₹34 L (itemised) → In the bank ₹21 L. Strip: what it built. | Where are we? Stage two. The product works, customers pay, and now we're proving the business model.<br><br>Incorporated May 2025 at CIE-IIITH. Prototype by September. Thirty lakh from two operator angels, who also brought us our first agencies. A government seed grant, and fourteen paying agencies by October.<br><br>In total we've raised fifty-five lakh and spent thirty-four, mostly on modest stipends and pilots, and we have twenty-one lakh in the bank. |

**Why this works:** Stage, journey, angels and money on one slide: four diligence questions answered before anyone asks.

---
### Act: Circuit

#### 8. Circuit, and how easy it is
**Speaker:** Sri Charan (CTO) · **Time:** ~0:44

| 🖥 SHOW (on screen, the proof) | 🎙 SAY (word for word, the explanation) |
|---|---|
| Left: six step cards (voice note → understands → fault + part → quote from the rate card → job card → technician verifies, we earn ₹40). Right: a browser frame with the live Circuit site (circuit-landing-page.netlify.app) scrolling end to end like a video. Bottom chips: no new app · 6 languages · set up in one visit · 30 free days · ₹40 only per verified fix · owner approves every quote. | Here's Circuit. A customer sends the agency a voice note on WhatsApp, in their own language. Circuit understands it and reads it back. It finds the likely fault and the part to carry, quotes from the agency's own price list for the owner to approve, and sends the technician a job card he can read in ten seconds.<br><br>When he verifies the fix, the record updates, Circuit learns, and only then do we earn forty rupees.<br><br>That's our live site on the right. There's no new app. It's set up in one visit, and the first thirty days are free. |

**Why this works:** What it does, how simple it is, and the live site scrolling as the visual. No technical jargon.

---
### Act: The proof

#### 9. The proof
**Speaker:** Kavyanth (COO) · **Time:** ~0:46

| 🖥 SHOW (on screen, the proof) | 🎙 SAY (word for word, the explanation) |
|---|---|
| Left: the price test, ₹40 → 2.0× value vs ₹100 → 0.81×, the quote "It takes too much of a small job", and the stamp "₹40 for everyone since May". Below it: 11 of 14 owners "very disappointed" without Circuit. Middle: 14 paying agencies · ~8,200 jobs · 71% → 83% one-visit · ~₹59k MRR. Right: the learning curve 62% → 78%, passing the 75% gate, with "since June: verified repairs" shaded. | I'm Kavyanth. First, we tested price: five agencies, forty rupees against a hundred per fix. At a hundred, one owner halved his usage. In his words, "it takes too much of a small job." At forty, agencies get twice the value they pay. So everyone pays forty.<br><br>Nine months in, fourteen agencies pay us and only one has left. That's eight thousand two hundred jobs, and one-visit fixes have gone from seventy-one to eighty-three percent.<br><br>And this curve matters most. Accuracy went from sixty-two to seventy-eight percent, and since June the gains come from repairs our technicians verified. No competitor has that data. |

**Why this works:** Pilot, traction and the learning curve merged. The failed ₹100 arm builds trust, and the curve is the moat in production data.

#### 10. The agency wins. So do we.
**Speaker:** Kavyanth (COO) · **Time:** ~0:43

| 🖥 SHOW (on screen, the proof) | 🎙 SAY (word for word, the explanation) |
|---|---|
| Value bars per agency per month: recovered jobs ₹2,400 + trips avoided ₹2,150 (measured) + owner time ₹2,925 (self-reported) vs our fee ₹3,690 (₹100 fee ₹9,225 crossed out). Four tiles: ₹4,216/mo revenue per agency · 81% contribution · 6.3-month payback · 6.3× LTV:CAC. Growth equation: field reps × ~80 agencies a year. | Does the agency win? From system logs alone, recovered jobs and saved trips are worth four and a half thousand rupees a month. That's more than our fee of thirty-seven hundred. With the owner's time, it's twice the fee.<br><br>And we win too. Each agency pays us about forty-two hundred rupees a month, at an eighty-one percent margin. It pays back in six months and is worth six times what it costs to win, on conservative assumptions.<br><br>Growth comes from capacity: I closed eight agencies part-time in six months. One full-time rep brings about eighty a year. |

**Why this works:** Value to the customer, unit economics and growth in one engine slide. The voice gives the logic; the screen shows the bars and tiles.

---
### Act: Why we win

#### 11. Why we win
**Speaker:** Kavyanth (COO) · **Time:** ~0:32

| 🖥 SHOW (on screen, the proof) | 🎙 SAY (word for word, the explanation) |
|---|---|
| The competitor map: Urban Company, Servify, Zoho, Fieldproxy and Bernard each in their slice, with Keepwell pulsing alone in the "serves the agency × holds the lifetime record" corner. Right: one line per rival, then "No one can copy: 8,200+ verified outcomes · a record that follows the machine · licence signed by all 14 agencies · switching costs". The five forces in one line. | Why hasn't anyone solved this? Everyone holds a slice. Urban Company takes the customer. Servify serves brands. Field-service software is in English and priced per seat. Nobody serves the agency and holds the machine's history. That corner is ours.<br><br>Our moat isn't the AI, which can be copied in a quarter. It's eight thousand verified repair outcomes, a data licence signed by every agency, and switching costs that grow every month. |

**Why this works:** Competition, moat and five forces compressed. The empty corner is the image investors remember.

#### 12. How big, and the plan
**Speaker:** Kavyanth (COO) · **Time:** ~0:35

| 🖥 SHOW (on screen, the proof) | 🎙 SAY (word for word, the explanation) |
|---|---|
| Left: the funnel 37,500 → 22,500 → 1,400 → 120 (Series A gate), with the Keepwell earnable pool ₹1,005–2,370 Cr a year beneath. Right: the plan chart: paying agencies 79 → 264 → 945 → 2,196 → 3,793 with revenue ₹0.2 → 19.2 Cr and EBITDA, under the stage bands seed (Telangana + AP) · Series A (the south) · national. | How big? We counted India's repair agencies three ways: thirty-seven thousand five hundred, with twenty-two thousand five hundred in our Tier 2 and 3 segment.<br><br>This seed takes us to about two hundred and sixty agencies, and a Series A takes us south and then national. By year five, that's thirty-eight hundred agencies, nineteen crore in revenue, and profitable. And the record opens a pool of over a thousand crore a year in plans, parts and claims. |

**Why this works:** Market and plan side by side, so every growth number can be checked against the market.

---
### Act: The ask

#### 13. What we need
**Speaker:** Prathyusha (CEO) · **Time:** ~0:30

| 🖥 SHOW (on screen, the proof) | 🎙 SAY (word for word, the explanation) |
|---|---|
| The bridge chart: costed needs ₹548 L + 10% contingency − revenue − cash − grant due = gap ₹467 L → ask ₹475 L. Use of funds by purpose: product–market fit 38% · team 28% · product 23% · sales 10% · working capital 1%. A compliance strip: DPDP consent-first · IRDAI via licensed partners · CERT-In runbook · owner approves every quote · 0 safety incidents · ₹26 L budgeted. | Now, what we need. We costed every requirement for the next twenty-four months, added a buffer, and subtracted our revenue, our cash and the grant still due. The gap is four hundred and sixty-seven lakh. The biggest share, thirty-eight percent, goes to proving product–market fit.<br><br>Compliance is built in and budgeted: consent-first data kept in India, insurance sold only through licensed partners, and zero safety incidents. |

**Why this works:** The requirement comes before the number, so the ask lands as a calculation. Compliance sits right before the ask as a reason to trust.

#### 14. The ask
**Speaker:** Prathyusha (CEO) · **Time:** ~0:32

| 🖥 SHOW (on screen, the proof) | 🎙 SAY (word for word, the explanation) |
|---|---|
| A full dark page: ₹4.75 Cr, "to take Circuit from 14 agencies to ~260, and reach the Series A from strength." The bridge line, then four terms: 24 months · ₹4.0 Cr minimum close · priced Seed CCPS · 20% to one lead. Three columns: what we have today · what your money proves (the Series A gates) · what comes next. | So here's our ask. Four point seven five crore rupees, for twenty percent, from one lead investor, as priced seed preference shares. That's twenty-four months of runway, and our minimum close is four crore.<br><br>Your money proves the Series A gates: a hundred and twenty paying agencies, forty thousand machine records, retention above ninety-seven percent, and our first warranty partner. At month twenty, we raise from strength, not need. |

**Why this works:** The most important slide gets a full page: the amount, the instrument, the equity, the runway and what it proves.

---
### Act: The future

#### 15. Why now, and who buys
**Speaker:** Prathyusha (CEO) · **Time:** ~0:33

| 🖥 SHOW (on screen, the proof) | 🎙 SAY (word for word, the explanation) |
|---|---|
| Left, Why now: Rs 4.5 (AI is finally cheap) / 1 in 10 (the repair wave is ahead) / 2027 (data law arrives) / R2R (repair is opening up). Right, Who buys Keepwell: Keepwell at the centre, four buyers around it with one precedent each, warranty platforms marked most likely (Asurion bought Domestic & General, about GBP 2.1 bn). Under both: about Rs 66 Cr revenue by year 8, and a strategic sale in years 6-8. | Why now? Indian-language AI just got cheap: a job costs us four and a half rupees, and we charge forty. The repair wave is still ahead of us. And data law arrives in 2027, so the consent-first record built now becomes the standard.<br><br>And the buyers exist. Warranty platforms are the most likely: Asurion paid two billion pounds for a company like this. We'd expect a strategic sale in years six to eight. |

**Why this works:** Urgency and the exit together: why invest now, and how the money comes back. Shown as one number per reason and a simple hub of buyers.

#### 16. Back to Ramagundam
**Speaker:** Prathyusha (CEO) · **Time:** ~0:26

| 🖥 SHOW (on screen, the proof) | 🎙 SAY (word for word, the explanation) |
|---|---|
| Dark slide. One click, and five green beats cascade on their own (answered in minutes · Circuit knows it's the capacitor · the part arrives the same afternoon · one visit, verified · a 74-year-old man sleeps in a cool room), then the line "Keepwell becomes the record everyone checks before touching a machine." Names and "Raising ₹4.75 Cr · Thank you". | [click, then let it play] Back to Ramagundam. With Keepwell, that voice note is answered in minutes. Circuit knows it's the capacitor. The technician arrives the same afternoon, with the part, and fixes it in one visit. And a seventy-four-year-old man sleeps in a cool room.<br><br>Keepwell becomes the record everyone checks before touching a machine. Thank you. |

**Why this works:** It mirrors the opening and resolves the human story. One click, then stop talking.

---
## Backup slides (press B; Q&A only)

#### Backup · Valuation (Q&A only)
- **Show:** Comparable ₹24.8 Cr post · scorecard ₹24.1 Cr · VC method ₹24.2 Cr. Pitched ₹19 Cr pre / ₹23.75 Cr post, never above the VC-method price. Base-case investor IRR ~35% (6.2×).
- **Say:** Only if asked: 'Three course methods; we priced at the investor's own required-return price, so the base case clears 35%.'

#### Backup · Cap table (Q&A only)
- **Show:** After seed: founders 67.9% · angels 2.1% · ESOP 10% · lead 20%. Founders 54.3% after A, 46.2% after B.
- **Say:** Only if asked: 'Founders keep a majority through the Series A.'

#### Backup · Terms (Q&A only)
- **Show:** 1× non-participating · broad-based weighted average · board 2+1+1 · vesting credit since May 2025 · deal costs capped at ₹8 L · lead reserves for the Series A.
- **Say:** Only if asked: 'Standard seed terms, with two asks: vesting credit and a Series A reserve.'

---
## Before you present
- **Media files** live in `media/`. They hold redacted real evidence, so they are kept out of the public GitHub repo. Copy the whole `story_deck_10min/` folder to the presenting laptop.
- **Fonts** load from Google Fonts. Open the deck once while online, or it falls back to Georgia and the system sans-serif.
- **The demo tab** 'The Circuit website' loads `media/circuit_landing.html`. 'A real run' plays `media/circuit_live_run_30x.mp4`.
- **Rehearse word for word:** the hook (1), Ramagundam (2), the proof (9) and the ask (14). Time yourselves twice; the target is 9:30–10:00.
- **Never say** 'DPDP-compliant', 'AI diagnosis', or any number that isn't in the model.
