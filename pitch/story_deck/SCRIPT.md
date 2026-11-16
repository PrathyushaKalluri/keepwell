# Keepwell seed pitch: the story deck script
> **Illustrative case.** Founder histories, the company timeline, the pilot results and the financials are assumptions made for the IIIT Hyderabad ESFS course pitch. The research, the household quotes, the photo and video evidence and the Circuit prototype are real.

**Deck:** [`index.html`](index.html). Open it in Chrome and press **F** for full screen and **N** for these notes. **→ / space** moves to the next click, **←** goes back, **B** opens the backup slides (valuation, cap table, terms; Q&A only).
**Generated** from [`script_data.py`](script_data.py) by [`build_story_deck.py`](build_story_deck.py), so the deck's speaker notes and this script are always the same words.

## The rule for every slide: the screen proves, the voice explains
- **SHOW** is the proof: a picture, a number, a real artefact, something to interact with. It is never read aloud.
- **SAY** is the explanation: what it means and why it matters. It says what the screen can't.
- When the two say the same thing, it's on purpose: only for the one line we want remembered (the hook, the insight, the ask, the close).
- `[click]` in SAY means press → once to reveal the next part of the slide.

## Timing and speakers
- **Full story: 31 slides, about 26:30** at a calm 145 words a minute, including clicks and the demo.
- **Shorter version: about 23:46.** Drop or fold the slides marked ✂ into their neighbours (bothsides, growth, porter, whycircuit). For a hard 10–12 minute slot, also say only the first paragraph of each SAY block.
- **Prathyusha (CEO):** about 8:02
- **Sri Charan (CTO):** about 10:18
- **Kavyanth (COO):** about 8:10

**Hand-overs** are built into the words. Sri Charan starts with "I'm Sri Charan." Kavyanth starts with "I'm Kavyanth." Prathyusha takes the ask with "So here's our ask."

## Why the story runs in this order
1. **The audience feels it before we explain it.** The hook makes them count their own repairs; Ramagundam makes the cost human — a sick old man nobody could help — with the money (₹350 vs ₹38,000) only a footnote.
2. **The team lands as witnesses, not CVs:** the three people who each saw one side of that afternoon.
3. **Proof we saw it ourselves:** the brand-bot recording playing live, the stickers, the diary — then four months of listening and the insight.
4. **The full problem set before any product:** all 13 problems in plain words, grouped by who feels them, each tagged with the scenario that solves it, both sides of a repair, the whole life of a machine, and only then the 15-crore numbers.
5. **Keepwell is named only after all of that**, so the name arrives as the answer.
6. **The company stage next:** stage two, the journey, the angel round, raised → spent → in the bank, every rupee itemised.
7. **The solution:** the roadmap from the problem map, why repair is the wedge, Circuit in six plain steps, then the demo with the live site scrolling like a video.
8. **The proof chain:** price test (including the failure) → traction → the learning curve → value to the agency → unit economics → growth from capacity.
9. **Why we win:** the empty corner, the moat, the five forces — then the market funnel and the stage-by-stage plan.
10. **Trust and compliance sit immediately before the ask**, so the last thing heard before the number is that the company is clean and regulation-ready.
11. **The ask shows the requirement first** (costed needs → the gap → use by purpose), and only then, on one click, the number and terms. Valuation, cap table and terms stay in backup.
12. **Why now and who buys share the future slide**, and the close replays Ramagundam with Keepwell — one click, the beats cascade on their own.

## Overview: show vs say
| # | Act | Slide | Speaker | Time | What we SHOW (the proof) | What we SAY (the point) |
|---|---|---|---|---|---|---|
| 1 | The hook | **Every repair in your home starts from zero** | Prathyusha | 0:46 | An illustrated home with eight machines (AC, fridge, washing machine, water purifier, geyser, TV, fan, mixer)… | “Before we begin, think about your own home…” |
| 2 | The hook | **We took it lightly too — until one afternoon in Ramagundam** | Prathyusha | 1:28 | Left: Sri Charan's dark quote card, "Our machines cost my family ₹10,000 a month… | “We took this problem lightly too…” |
| 3 | The team | **Three founders, one from each side of the problem** | Prathyusha | 0:51 | A triangle with the machine record at the centre… | “That afternoon is why the three of us are standing here…” |
| 4 | What we saw | **We didn't read about it. We watched it happen.** | Sri | 1:03 | A proof wall of real artefacts… | “I'm Sri Charan…” |
| 5 | What we saw | **We listened before we built** | Sri | 0:59 | The research funnel builds on the left: - household survey: 19 responses, 12 qualified - 7 recorded household interviews - 18 agency-owner interviews … | “Before we wrote any production code, we spent four months listening…” |
| 6 | The problem | **Thirteen problems, one missing record** | Sri | 0:49 | All 13 problems from the team repo's problem map, in plain words, in three columns by who feels them… | “When we put everything together, it wasn't one problem…” |
| 7 | The problem | **What goes wrong, on both sides** ✂ | Sri | 1:01 | A split screen joined by a broken thread labelled "no shared memory"… | “Here's the size of it, on both sides.…” |
| 8 | The problem | **From one repair to a machine's whole life** | Sri | 0:49 | A ring of seven life stages: bought, used, fails, repaired, maintained, resold, recycled… | “And when we zoomed out, the small problem became a big one…” |
| 9 | The problem | **It isn't one family. It's 15 crore repairs a year.** | Sri | 0:45 | Four counters count up, each with a small picture: - 15 Cr appliance repairs a year - 27 Cr fridges, washing machines and ACs with no shared record - … | “Now put numbers on all of that…” |
| 10 | Keepwell | **Keepwell: the care layer for everything a home owns** | Sri | 0:30 | Dark slide… | “That's why we started Keepwell…” |
| 11 | Where we are | **Where we are: the stage, the journey, the money** | Prathyusha | 1:01 | One picture in three layers, read top to bottom… | “So where is Keepwell today? We're at stage two…” |
| 12 | The solution | **The roadmap: one record, a product at each stage** | Sri | 0:39 | A rising staircase of six steps, each with its product, its stage of life and who pays: - **R1 · live:** Circuit, the AI desk for repair agencies (age… | “From that scored problem map came the roadmap — the five scenarios, in order, as products…” |
| 13 | The solution | **Why we start with repair** ✂ | Sri | 0:31 | Three overlapping circles: - **The pain:** the moment a household needs help - **The payer:** the agency earns on every job - **The truth:** the only … | “Why start with repair? Because it's the only moment where three things meet.…” |
| 14 | The solution | **Circuit, simply** | Sri | 0:58 | Left: the six steps as cards, lighting up in order: 1… | “Here's what Circuit does, in plain words…” |
| 15 | The solution | **See how easy it is** | Sri | 1:18 | Three tabs on the demo stage: - **The agency's WhatsApp** (opens first): an animated chat… | “And it's genuinely easy — let me show you rather than tell you…” |
| 16 | The proof | **The pilot: we tested the price, and one test failed** | Kavyanth | 0:48 | The pilot design card: 5 agencies, 22 technicians, Feb–Apr 2026, paid from day one, each measured against its own baseline… | “I'm Kavyanth…” |
| 17 | The proof | **Nine months of paid use** | Kavyanth | 0:41 | Five counters count up: - **14** paying agencies (1 of 15 churned) - **~8,200** jobs through Circuit - **96%** of requests became jobs - **~₹59k** mon… | “Then we expanded, and here's nine months of paid use…” |
| 18 | The proof | **The chart that matters most: it learns** | Kavyanth | 0:43 | A line chart draws itself: root-cause accuracy (right fault in the top 3), Mar → Oct 2026: **62 → 68 → 73 → 76 → 78%**… | “This is the most important chart in our story…” |
| 19 | The proof | **Does the agency actually win?** | Kavyanth | 0:47 | Horizontal stacked bars, per agency per month: - **Value:** recovered jobs ₹2,400 + trips avoided ₹2,150 (**measured**, solid teal) + owner time ₹2,92… | “A product only survives if the customer gets more than it pays…” |
| 20 | The proof | **Unit economics: one agency, one month** | Kavyanth | 0:53 | A waterfall chart: revenue **₹4,216** → AI and messaging −₹713 → tools −₹100 → contribution **₹3,403 (81%)**… | “Here's one agency, one month…” |
| 21 | The proof | **Growth comes from capacity, not hope** ✂ | Kavyanth | 0:39 | An equation builds: **new agencies = field reps × ~80 a year + 10% referrals**… | “Can it grow? We don't plan growth from a hockey stick…” |
| 22 | Why we win | **Why this isn't solved yet, and where we sit** | Kavyanth | 0:35 | A two-axis map… | “Why hasn't anyone solved this? Because everyone holds a slice…” |
| 23 | Why we win | **Why nobody can catch up** | Kavyanth | 0:46 | Two columns: - **"A rival can copy in a quarter"** (grey, crossed out): WhatsApp intake · prompting an AI model · searching manuals · ranking faults -… | “Let's be honest about what can be copied…” |
| 24 | Why we win | **The industry forces, and our answer to each** ✂ | Kavyanth | 0:33 | A pentagon of Porter's five forces around "AI for repair agencies in India"… | “Quickly, the industry forces…” |
| 25 | How big | **How big: the market, narrowed honestly** | Kavyanth | 0:54 | An animated funnel narrowing level by level: - **37,500** repair agencies in India - **22,500** in Tier 2/3 towns, our segment - **1,400** in Telangan… | “How big can this get? No one has ever counted India's repair agencies, so we built the number three ways…” |
| 26 | How big | **The plan, stage by stage: seed → Series A → year five** | Kavyanth | 0:51 | Left: one clean chart… | “Here's the plan, stage by stage…” |
| 27 | The ask | **Before we ask: trust and compliance, built in and budgeted** | Sri | 0:56 | A grid of the laws that matter… | “Before we talk about money, one thing matters…” |
| 28 | The ask | **Before the ask: what the next 24 months need** | Prathyusha | 0:55 | A bridge chart builds bar by bar: - costed requirements for the next 24 months: ₹548 L - + 10% contingency: ₹55 L - − revenue we'll earn: ₹105 L - − c… | “Now, the money — and we didn't start from a round number…” |
| 29 | The ask | **The ask, on its own page** | Prathyusha | 1:20 | A full dark page for the ask alone… | “The ask is four point seven five crore rupees — the four-sixty-seven-lakh gap you just saw, rounded up to the nearest tw…” |
| 30 | The future | **Why now, and who buys Keepwell** | Prathyusha | 0:53 | Two calm halves… | “Why invest now? Four reasons…” |
| 31 | The future | **Back to Ramagundam** | Prathyusha | 0:48 | Dark slide… | “Let's go back to Ramagundam one last time…” |

## Slide by slide

---
### Act: The hook

#### 1. Every repair in your home starts from zero
**Speaker:** Prathyusha (CEO) · **Time:** ~0:46

| 🖥 SHOW (on screen, the proof) | 🎙 SAY (word for word, the explanation) |
|---|---|
| An illustrated home with eight machines (AC, fridge, washing machine, water purifier, geyser, TV, fan, mixer). The presenter clicks each machine as the audience calls it out, and a counter adds up "repairs in your home this year". [click] A question tag drops onto every machine: "Last serviced? Which part? What did you pay? Who fixed it?" [click] The line lands: "Every repair in your home starts from zero." | Before we begin, think about your own home. In the last year, what broke? The AC? The fridge? The water purifier, the geyser, the washing machine? [click the machines as people answer] Keep counting.<br><br>Now a harder question. Pick any one of them. When was it last serviced? Which part was changed? What did you pay, and who fixed it?<br><br>Most of us don't know. It's in someone's phone, in a diary, or nowhere.<br><br>So every repair in your home starts from zero. |

**Why this works:** The audience answers before we say anything about us. Once they've counted their own repairs, the problem is theirs too. The interaction also wakes the room up in the first 30 seconds.

#### 2. We took it lightly too — until one afternoon in Ramagundam
**Speaker:** Prathyusha (CEO) · **Time:** ~1:28

| 🖥 SHOW (on screen, the proof) | 🎙 SAY (word for word, the explanation) |
|---|---|
| Left: Sri Charan's dark quote card, "Our machines cost my family ₹10,000 a month. Never evenly." — with the line "We treated it as normal. Everyone does."<br>Right, on one click the whole story builds itself in quick succession, one human beat after another:<br>1. 46 °C in Ramagundam. A retired miner, 74, is home alone — and running a fever. At noon, his AC stops cooling.<br>2. The one person he trusts, Ramesh of the local agency, is up a ladder across town. His phone rings 14 times. The old man's Telugu voice note is never heard.<br>3. His son, 700 km away in Bengaluru, calls everyone he knows. Nobody can say what's wrong, who will come, or when.<br>4. The old man sits through two nights of that heat under a table fan before anyone opens the machine.<br>5. A small, quiet footnote card at the end: the fault was a ₹350 capacitor; by then the family had ordered a ₹38,000 new AC, three days away.<br>The line lands: "Nobody is the villain. The system has no memory." | We took this problem lightly too. In Sri Charan's family the machines cost about ten thousand rupees a month, never evenly, and we treated that as normal. Everyone does.<br><br>Then one afternoon changed that. [click] Ramagundam, forty-six degrees. A retired miner, seventy-four years old, home alone, running a fever. At noon, his AC stops cooling. The one man he trusts, Ramesh of the local agency, is up a ladder across town. The phone rings fourteen times. The voice note, in Telugu, is never heard. His son, seven hundred kilometres away in Bengaluru, calls everyone he knows. Nobody can tell him what's wrong, who will come, or when. He is helpless, and so is everyone around that old man. He sat through two nights of that heat under a table fan before anyone even opened the machine. And when someone finally did? A three-hundred-and-fifty-rupee part. The family had already ordered a new AC.<br><br>Nobody in this story is the villain. Ramesh is good at his job. The son did everything a son can do. The system just has no memory — and when a system has no memory, it isn't money that gets lost first. It's people left suffering, with nobody able to help. |

**Why this works:** The hook is the human intensity of Ramagundam — a sick old man in 46° heat whom nobody could help in time — not the money. The ₹350 / ₹38,000 detail stays only as a quiet footnote. The people are a composite (disclosed in the data room); the heat, the town and the reflex to replace are real.

---
### Act: The team

#### 3. Three founders, one from each side of the problem
**Speaker:** Prathyusha (CEO) · **Time:** ~0:51

| 🖥 SHOW (on screen, the proof) | 🎙 SAY (word for word, the explanation) |
|---|---|
| A triangle with the machine record at the centre. Each corner is one side of the problem with its founder card:<br>- **Agency network: Prathyusha, CEO.** FixNear: 1,200 technicians, 14 towns, sold in 2022.<br>- **Household and AI: Sri Charan, CTO.** 7 years of Indian-language voice AI; built Circuit himself.<br>- **Brand and warranty: Kavyanth, COO.** Ran 300+ service partners and a warranty-claims desk.<br>A ribbon underneath: "Full-time since May 2025 · ₹15 lakh of our own money · incubated at CIE-IIITH · DPIIT-recognised". | That afternoon is why the three of us are standing here. This problem has three sides, and each of us spent years on one of them.<br><br>I'm Prathyusha. I co-founded FixNear, a technician network of twelve hundred people across fourteen towns in Andhra and Telangana, and sold it in 2022. I learned the hard way that taking the customer away from the local agency doesn't work.<br><br>Sri Charan spent seven years building voice AI in Indian languages, and he built our product himself. Kavyanth ran a brand's network of more than three hundred service partners, and its warranty-claims desk.<br><br>Agency, household, brand. All three of us have been full-time since May 2025, with our own money in. |

**Why this works:** The course gives the team 45 of 90 points. Coming straight after the story, the team lands as 'the people who saw this first-hand', not a CV slide. Each founder gets one line of proof: an exit, a shipped product, a network.

---
### Act: What we saw

#### 4. We didn't read about it. We watched it happen.
**Speaker:** Sri Charan (CTO) · **Time:** ~1:03

| 🖥 SHOW (on screen, the proof) | 🎙 SAY (word for word, the explanation) |
|---|---|
| A proof wall of real artefacts. The brand-bot card is the actual screen recording, playing on the slide:<br>1. **A brand's WhatsApp bot failing, on camera** (the full recording, playing on loop): "There is some API related issue please try again later" … she types "What is API" … her last message: "My request was not done."<br>2. **A water purifier** with a local agency's sticker taped on, and the next service date written over the brand's label in marker<br>3. **A household's repair diary**: handwritten pages of what was fixed, when, by whom, for how much — two pages shown<br>4. **A gas cylinder** with its refill date written on it in marker<br>5. **Our own whiteboard**: "machine fails → technician travels → discovers the problem → another visit" vs "symptoms + photo + model → prepared technician → one visit"<br>Personal details are blurred in the images. Tag: "Real · from our discovery interviews". Click any image for full screen. | I'm Sri Charan. We didn't just read about this problem. We went into homes and watched it happen. [point at the playing video]<br><br>This is a real brand's WhatsApp bot, recorded in one of our interviews. A woman asks for her water purifier to be serviced. The bot says there's an API issue. She asks — what is API? Then it demands a job ID she doesn't have. Watch her last message: "My request was not done."<br><br>And look at what people do instead. A local agency has taped its own sticker onto the machine, and the family wrote the next service date in marker over the brand's label. This family keeps a handwritten diary of every repair. This one writes the refill date on the gas cylinder itself.<br><br>People are already building the machine's memory — on stickers, in diaries, in marker pen. The demand is there. The tool isn't. |

**Why this works:** This is the trust moment for the problem: real, first-hand evidence instead of statistics. The bot recording playing live is the strongest 'wow' in the deck, and the sticker and diary show people already doing a paper version of Keepwell.

#### 5. We listened before we built
**Speaker:** Sri Charan (CTO) · **Time:** ~0:59

| 🖥 SHOW (on screen, the proof) | 🎙 SAY (word for word, the explanation) |
|---|---|
| The research funnel builds on the left:<br>- household survey: 19 responses, 12 qualified<br>- 7 recorded household interviews<br>- 18 agency-owner interviews<br>Named quote cards on the right:<br>- Sai Kakki: "They're never going to say the price… three thousand to five thousand."<br>- Amma: "We won't know if the part is duplicate or original."<br>- Rk Sir: "If we visit a local man, definitely doubts will arise."<br>- Sarala Aunty: "Since then, I have been able to trust him and approve his small works."<br>[click] The insight lands in a teal band: "Nothing in a repair can be checked, so people trust the person, not the work." Two proof chips: 44% use a local agency (up from 38%), and 76% of AC owners avoid brand service. | Before we wrote any production code, we spent four months listening. A household survey, seven recorded household interviews, and eighteen conversations with agency owners.<br><br>Listen to what households said. Sai Kakki: they never tell you the price. Amma: you can't tell if the part is original. Rk Sir: with a local man, doubts arise. And Sarala Aunty: he came, did a small job honestly, and since then she trusts him with more. [click]<br><br>That's our insight. Nothing in a repair can be checked, so people trust the person, not the work, one good job at a time. That's why forty-four percent of families stay with the local agency, and that number is rising.<br><br>So our strategy is simple. We don't replace the trusted agency. We make it the smartest one in town. |

**Why this works:** The quotes are real and named with consent. The insight explains why an agency-first strategy wins against better-funded platforms, which is the strategic choice investors will question.

---
### Act: The problem

#### 6. Thirteen problems, one missing record
**Speaker:** Sri Charan (CTO) · **Time:** ~0:49

| 🖥 SHOW (on screen, the proof) | 🎙 SAY (word for word, the explanation) |
|---|---|
| All 13 problems from the team repo's problem map, in plain words, in three columns by who feels them. Each carries a coloured letter for the scenario that solves it.<br>- For the repair shop: calls and voice notes get lost (A) / the first visit goes in blind, wrong part, second trip (A) / technicians struggle with new electronics (A) / spare parts are wrong or hard to find (E) / technicians' income swings month to month (not our focus)<br>- For the family: nobody keeps the machine's history (B) / no way to know a fair price (B) / service plans are rarely bought or renewed (B) / warranty claims get refused (D) / safety risks such as gas leaks and refrigerant (not our focus)<br>- For brands, insurers, recyclers: claims that nobody can verify (C) / old machines get scrapped, not refurbished (E) / brands can't trace their e-waste (E)<br>A legend: A prepared visit, now (Circuit) / B machine record and plans, year 1-2 / C claims checking, year 2 / D fair price and warranty help, inside B / E parts, resale, recycling, later.<br>[click] Band: We start with A, the prepared visit, where it hurts most and is easiest to fix. | When we put everything together, it wasn't one problem. It was thirteen, and you can see them here in plain words.<br><br>For the repair shop: calls get lost, the first visit goes in blind, and the parts are wrong. For the family: nobody keeps the machine's history, nobody knows a fair price, and warranty claims get refused. For brands and insurers: claims can't be verified, and old machines get scrapped instead of reused.<br><br>Each letter is the solution that fixes it, and together they're the five steps of our roadmap. [click]<br><br>We start with A, the prepared visit. It's where it hurts most, and it's the easiest to fix. |

**Why this works:** All 13 problems in layman's terms, grouped by who feels them rather than by score, with one letter per problem tying it to the scenario that solves it. Readable in seconds. Source: the team repo's problem map (P1-P12 and P14; the repo has no P13).

#### 7. What goes wrong, on both sides ✂ *(short version: drop or fold in)*
**Speaker:** Sri Charan (CTO) · **Time:** ~1:01

| 🖥 SHOW (on screen, the proof) | 🎙 SAY (word for word, the explanation) |
|---|---|
| A split screen joined by a broken thread labelled "no shared memory".<br>**The agency (the person who pays us):**<br>- ~1 in 8 requests lost: missed calls, unanswered voice notes<br>- Technicians sent in blind: no model, no history<br>- 12 of 18 owners had a job delayed by the wrong part last month<br>- ~3.45 crore repeat trips a year at ~₹159 each<br>**The household (the person who trusts):**<br>- Price, part and "job done" can't be checked<br>- 55% got a defective machine; only 21% were made whole<br>- 47% of complaints are no-shows and chasing<br>- In 7 of 12 repairs, the person deciding, paying and opening the door were different people<br>- Consumer helpline complaints: 13.16 → 20.49 lakh in a year | Here's the size of it, on both sides.<br><br>For the agency, the pain starts at the very first moment. About one request in eight is simply lost: a missed call, a voice note nobody follows up. The technician goes in blind, often with the wrong part, so a lot of jobs need a second trip, and that costs the agency money.<br><br>For the household, nothing can be checked: not the price, not the part, not whether the job is really done. Fifty-five percent of families have had a defective machine, and only twenty-one percent of those were made whole. Almost half the complaints are about chasing someone. And in most homes the person who decides, the person who pays and the person who opens the door aren't the same.<br><br>Two sides, one missing thing: a shared memory of the machine. |

**Why this works:** It proves we understand the buyer (the agency) and the user (the household) separately, which is where most repair pitches blur. The broken thread keeps the one idea visible.

#### 8. From one repair to a machine's whole life
**Speaker:** Sri Charan (CTO) · **Time:** ~0:49

| 🖥 SHOW (on screen, the proof) | 🎙 SAY (word for word, the explanation) |
|---|---|
| A ring of seven life stages: bought, used, fails, repaired, maintained, resold, recycled. Each carries a red tag:<br>- technician arrives blind<br>- warranty can't be proven<br>- plan sold to the wrong home<br>- resale buyer can't trust it<br>- recycled too early<br>[click] A teal ring draws through all seven stages: "One record, every stage". [click] The vision line appears: "Every machine an Indian home owns is cared for across its whole life: repaired right, remembered always, and never wasted." Analogy chips: CIBIL → borrowers · Carfax → used cars · nothing, yet → household machines. | And when we zoomed out, the small problem became a big one. Every machine lives one life: bought, used, fails, repaired, maintained, resold, recycled. At every single stage it starts from zero. The technician arrives blind, the warranty can't be proven, the plan is sold to the wrong home, the resale buyer can't trust it. [click]<br><br>The same missing piece sits under all of them: the machine's history. So the vision we committed to is bigger than repair: every machine an Indian home owns, cared for across its whole life. India has CIBIL for borrowers. The world has Carfax for used cars. For household machines, there is nothing. Yet. |

**Why this works:** Here the problem widens into a venture-scale category and the vision is stated — before the company is even named, so the name lands as the answer two slides later.

#### 9. It isn't one family. It's 15 crore repairs a year.
**Speaker:** Sri Charan (CTO) · **Time:** ~0:45

| 🖥 SHOW (on screen, the proof) | 🎙 SAY (word for word, the explanation) |
|---|---|
| Four counters count up, each with a small picture:<br>- 15 Cr appliance repairs a year<br>- 27 Cr fridges, washing machines and ACs with no shared record<br>- ₹550 Cr of technician time lost to repeat trips each year<br>- 37,500 repair agencies running on a phone and a notebook<br>A red "broken thread" runs under all four. Source line: repo; Data for India; CLASP/BEE 2024; ICAP/CEEW. | Now put numbers on all of that. India does about fifteen crore appliance repairs a year. There are about twenty-seven crore fridges, washing machines and ACs in our homes, and not one has a shared history.<br><br>Technicians go in blind, and when the first visit doesn't fix it, someone goes back. If India fixed things at the global first-visit rate, that would still be about five hundred and fifty crore rupees of technician time wasted every year.<br><br>And the work is done by about thirty-seven thousand five hundred small agencies, on one phone and a notebook. The problem isn't skill. It's memory. |

**Why this works:** The scale lands only after the full problem set has been told, as decided. Four numbers, each with one job: frequency (15 Cr), the asset with no record (27 Cr), money lost (₹550 Cr) and the customer we sell to (37,500). Say the ₹550 Cr caveat out loud — it's the honest way to quote it.

---
### Act: Keepwell

#### 10. Keepwell: the care layer for everything a home owns
**Speaker:** Sri Charan (CTO) · **Time:** ~0:30

| 🖥 SHOW (on screen, the proof) | 🎙 SAY (word for word, the explanation) |
|---|---|
| Dark slide. The broken thread from the last slide joins into the Keepwell mark. Below it, a machine "record card" fills in line by line:<br>- Voltas 1.5 T split AC · bought Mar 2021<br>- Warranty: compressor till Mar 2026<br>- Repairs: 3, each verified<br>- Parts fitted: capacitor, Aug 2026<br>- Next service: Apr 2027<br>Tagline: "One living record per machine, and a service at every stage of its life." | That's why we started Keepwell. Keepwell gives every machine in an Indian home a memory. One living record of what it is, what went wrong, what was fitted and what it needs next, built only with the owner's consent.<br><br>On top of that record, a service at every stage of the machine's life. Keepwell is the CIBIL of household machines: the history that everyone checks first. |

**Why this works:** The company is named only after the room has felt the problem, its full map, its whole-life breadth and its scale — so the name arrives as the answer. The record card makes 'memory' concrete.

---
### Act: Where we are

#### 11. Where we are: the stage, the journey, the money
**Speaker:** Prathyusha (CEO) · **Time:** ~1:01

| 🖥 SHOW (on screen, the proof) | 🎙 SAY (word for word, the explanation) |
|---|---|
| One picture in three layers, read top to bottom.<br>Top: the company stage as a simple three-step path — build the product → **find the business model (we are here)** → scale — with our badge on step two.<br>Middle: the journey timeline, milestone by milestone: discovery (Jan–Apr 2025) → incorporated · full-time · CIE-IIITH (May 2025) → prototype, 2 design partners (Jun–Sep) → **₹30 L from two operator angels** (Oct) → production, Mumbai (Jan 2026) → paid price test, 5 agencies (Feb–Apr) → government seed fund ₹20 L sanctioned (Mar) → 5 → 14 paying agencies (May–Oct) → accuracy gate passed (Aug) → **raising the seed (now)**.<br>Bottom: three money tiles that read left to right —<br>- **RAISED ₹55 L** — founders ₹15 L · operator angels ₹30 L (iSAFE) · Startup India Seed Fund ₹10 L of ₹20 L<br>- **SPENT ₹34 L** — stipends ₹19.5 L · contract engineer ₹6 L · cloud + AI ₹3 L · pilot field work ₹3 L · legal ₹2.5 L<br>- **IN THE BANK ₹21 L**<br>A strip underneath — what that money built: the team · the research · the prototype · production · 14 paying agencies. | So where is Keepwell today? We're at stage two. The product exists, customers pay for it, and we're proving the business model.<br><br>Here's the whole journey on one line. Four months of listening. Incorporated in May 2025, all three of us full-time, incubated at CIE-IIITH. The prototype by September. Then two operator angels — one built a home-services company, one ran service at a durables brand — put in thirty lakh, and they introduced three of our first five agencies. Production in January. A paid price test in the spring. The government's seed fund sanctioned in March. Fourteen paying agencies by October.<br><br>And here's the money, plainly. Raised: fifty-five lakh. Spent: thirty-four — modest stipends, one contract engineer, and the pilots. In the bank: twenty-one. That thirty-four lakh bought the team, the research, the prototype, production, and fourteen paying customers. |

**Why this works:** One intuitive slide answers four diligence questions at once: what stage are you at, what have you done, who backed you, and what did you do with their money. Every rupee is itemised before anyone asks.

---
### Act: The solution

#### 12. The roadmap: one record, a product at each stage
**Speaker:** Sri Charan (CTO) · **Time:** ~0:39

| 🖥 SHOW (on screen, the proof) | 🎙 SAY (word for word, the explanation) |
|---|---|
| A rising staircase of six steps, each with its product, its stage of life and who pays:<br>- **R1 · live:** Circuit, the AI desk for repair agencies (agency pays per verified fix)<br>- **R2 · ~12 months:** Home Memory + Service Plans (insurer commission)<br>- **R3 · year 2:** Claims triage (warranty administrators, OEMs)<br>- **R4:** Parts marketplace (parts sellers)<br>- **R5:** Resale & recycling (buyers, producers, recyclers)<br>- **Phase 3:** Data services, consent-first (brands, insurers)<br>The record runs under every step as one teal line. | From that scored problem map came the roadmap — the five scenarios, in order, as products. Each step is a product on the same record, with a different payer.<br><br>We start with Circuit for repair agencies, which is live today. Next, Home Memory and service plans, sold for insurers. Then claims triage for warranty administrators, then parts, then resale and recycling, and finally data services, always with consent.<br><br>Each step is paid for by someone who already spends money at that stage of the machine's life. |

**Why this works:** It shows a clear expansion path, scored under Product–Potential, and that each step has its own payer. The order follows the team repo's build order and the scenario scores.

#### 13. Why we start with repair ✂ *(short version: drop or fold in)*
**Speaker:** Sri Charan (CTO) · **Time:** ~0:31

| 🖥 SHOW (on screen, the proof) | 🎙 SAY (word for word, the explanation) |
|---|---|
| Three overlapping circles:<br>- **The pain:** the moment a household needs help<br>- **The payer:** the agency earns on every job<br>- **The truth:** the only moment someone opens the machine and sees what's wrong<br>The overlap lights up: "The repair". Then the name appears in the middle: **Circuit**. | Why start with repair? Because it's the only moment where three things meet.<br><br>The pain is highest, because the machine is broken. The payer is there, because the agency earns on that job. And it's the only moment someone opens the machine and records what's really wrong.<br><br>Start there, and the record fills itself as a by-product of work that's already happening. [click] That's Circuit. |

**Why this works:** It answers 'why this wedge?' in 35 seconds and hands over to the product.

#### 14. Circuit, simply
**Speaker:** Sri Charan (CTO) · **Time:** ~0:58

| 🖥 SHOW (on screen, the proof) | 🎙 SAY (word for word, the explanation) |
|---|---|
| Left: the six steps as cards, lighting up in order:<br>1. 🎙 **Customer sends a voice note**, in Telugu, Hindi, Tamil, Kannada, Marathi or English<br>2. **Circuit understands** and reads it back<br>3. **Finds the likely fault and the part to carry**, using this machine's history and every past repair<br>4. **Quotes from the agency's own rate card**; the owner approves<br>5. **Sends the technician a job card** he can read in ten seconds<br>6. **The technician confirms the fix.** The record updates, Circuit gets smarter, and we earn ₹40.<br>Beside the six steps, a browser frame with the **live Circuit site (circuit-landing-page.netlify.app) scrolling end to end like a video** — the same product, as an agency owner first meets it. Underneath: "AI reads and drafts. People decide anything with money or safety." | Here's what Circuit does, in plain words. A customer sends the agency a voice note on WhatsApp, in their own language. Circuit understands it and reads it back. It looks at the machine's history and everything learned from past repairs, and tells the technician the likely fault and the part to carry. It builds the quote from the agency's own price list, and the owner approves it. The technician gets a job card he can read in ten seconds.<br><br>And when he confirms what was actually wrong, three things happen at once. The machine's record updates, Circuit gets smarter for the next job, and only then do we earn forty rupees.<br><br>What's playing on the right is our live website, scrolling — the same six steps, exactly as an agency owner first sees them. |

**Why this works:** No architecture or technical terms. The last step carries the whole business: one event that is the fix, the learning and the revenue.

#### 15. See how easy it is
**Speaker:** Sri Charan (CTO) · **Time:** ~1:18

| 🖥 SHOW (on screen, the proof) | 🎙 SAY (word for word, the explanation) |
|---|---|
| Three tabs on the demo stage:<br>- **The agency's WhatsApp** (opens first): an animated chat. A Telugu voice note arrives, Circuit reads it back, a photo of the AC label, an owner-approved quote, then the technician's job card and the green tick: "Fixed in one visit · record updated".<br>- **The website, scrolling**: the live landing page (circuit-landing-page.netlify.app) auto-scrolling top to bottom like a video, beside three snippets cut straight from it — "the first visit is almost never the repair visit", the four-step "how it works", and "you keep the customer, you keep the margin". Each snippet opens full-screen on click.<br>- **A real run, 30× speed**: the recorded run of the prototype (real).<br>Ease chips along the bottom: no new app · set up in one visit · 6 languages · 30 free days · pay only when a fix is verified · the owner approves every quote. | And it's genuinely easy — let me show you rather than tell you. [chat plays] For the customer, nothing changes. Same agency, same WhatsApp number, their own language. For the owner, the job arrives ready, with a quote he only has to approve. For the technician, a ten-second card with the part to carry. [switch tab] This is our live website — watch it scroll: the repair-ready checklist, how it works, the pricing. Everything a shop owner needs to understand us in one page. [switch tab] And this is a real run of the system, sped up thirty times.<br><br>Setting up takes one visit: the owner's price list and his WhatsApp number. Thirty free days, and after that the agency pays only when a fix is verified. |

**Why this works:** Investors judge ease of adoption by watching it. The scrolling landing page plays like a product video without needing one, and the real run proves the demo isn't a mock-up.

---
### Act: The proof

#### 16. The pilot: we tested the price, and one test failed
**Speaker:** Kavyanth (COO) · **Time:** ~0:48

| 🖥 SHOW (on screen, the proof) | 🎙 SAY (word for word, the explanation) |
|---|---|
| The pilot design card: 5 agencies, 22 technicians, Feb–Apr 2026, paid from day one, each measured against its own baseline.<br>Two arms side by side: **₹40 per verified fix** (3 agencies) vs **₹100** (2 agencies).<br>A value-to-fee gauge for each: ₹40 → **2.0×** the fee, ₹100 → **0.81×**.<br>[click] The red quote from the ₹100 owner who halved his usage in week 3: "It takes too much of a small job." The result stamp: "₹40 for everyone since May 2026". Pricing ladder: ₹40 per verified fix · optional Desk Pro ₹399/month · 30 free days. | I'm Kavyanth. Before we scaled anything, we ran a paid pilot with five agencies and twenty-two technicians, each measured against its own record before Circuit.<br><br>We tested two prices at the same time: forty rupees per verified fix, and a hundred. [click] At a hundred, one owner halved his usage in the third week. In his words, "It takes too much of a small job." At forty, the agency gets about two rupees of value for every rupee it pays us. At a hundred, it's less than one. So since May, everyone pays forty.<br><br>We're showing you the test that failed because it's what set our price. |

**Why this works:** Showing a failed experiment builds more trust than a clean success. It also proves willingness to pay with a real test rather than a survey.

#### 17. Nine months of paid use
**Speaker:** Kavyanth (COO) · **Time:** ~0:41

| 🖥 SHOW (on screen, the proof) | 🎙 SAY (word for word, the explanation) |
|---|---|
| Five counters count up:<br>- **14** paying agencies (1 of 15 churned)<br>- **~8,200** jobs through Circuit<br>- **96%** of requests became jobs<br>- **~₹59k** monthly recurring revenue, 97% of invoices paid on time by UPI<br>- **11 of 14** owners "very disappointed" without it<br>A large before/after dial: one-visit closure **71% → 83%**, held for 6 months over ~7,000 jobs (global benchmark 77%). | Then we expanded, and here's nine months of paid use. Fourteen agencies pay us every fortnight, and only one of fifteen has left. About eight thousand two hundred jobs have gone through Circuit. Ninety-six percent of requests now become a job, where before one in eight was lost.<br><br>The number that matters most to an agency is jobs closed in one visit. It went from seventy-one to eighty-three percent, and it has held there for six months, above the global benchmark. Eleven of fourteen owners say they'd be very disappointed if we disappeared. |

**Why this works:** Real paid demand, retention and an outcome metric, covering Market–Quality and Product–Quality. The 'very disappointed' test is a known product–market-fit signal.

#### 18. The chart that matters most: it learns
**Speaker:** Kavyanth (COO) · **Time:** ~0:43

| 🖥 SHOW (on screen, the proof) | 🎙 SAY (word for word, the explanation) |
|---|---|
| A line chart draws itself: root-cause accuracy (right fault in the top 3), Mar → Oct 2026: **62 → 68 → 73 → 76 → 78%**. A dashed line marks the 75% gate, with "passed in August". The chart is shaded in two zones:<br>- **Mar–May:** "about half from adding manuals" (grey: anyone can do this)<br>- **Jun–Oct:** "mostly from verified repairs" (teal: only we can do this) | This is the most important chart in our story. It's how often Circuit names the right fault in its top three. It started at sixty-two percent in March and it's at seventy-eight percent now. It passed our seventy-five percent gate in August.<br><br>Look at where the gain comes from. Up to May, about half of it came from adding repair manuals, and anyone can do that. Since June, it comes mostly from repairs that technicians verified. [click] No competitor can do that without our agencies. The product gets better every time it's used. |

**Why this works:** This is the moat shown in production data rather than claimed on a slide. It answers Product–Uniqueness (our weakest cell, 7/10) with evidence.

#### 19. Does the agency actually win?
**Speaker:** Kavyanth (COO) · **Time:** ~0:47

| 🖥 SHOW (on screen, the proof) | 🎙 SAY (word for word, the explanation) |
|---|---|
| Horizontal stacked bars, per agency per month:<br>- **Value:** recovered jobs ₹2,400 + trips avoided ₹2,150 (**measured**, solid teal) + owner time ₹2,925 (**self-reported**, hatched) = ₹7,475<br>- **Our fee at ₹40:** ₹3,690<br>- **The fee at ₹100:** ₹9,225 (grey, crossed out)<br>Callouts: "Measured value alone = 1.23× the fee" and "Agency keeps ~₹3,800 a month after paying us". | A product only survives if the customer gets more than it pays. So we split what we measured from what owners told us.<br><br>From system logs alone, the jobs we recover and the trips we save are worth about four thousand five hundred rupees a month to an agency. That's more than our fee of three thousand seven hundred, even if you ignore everything owners say. Counting the owner's time, the value is about two times the fee, and the agency keeps about three thousand eight hundred rupees a month after paying us.<br><br>At a hundred rupees, the maths breaks, which is exactly what the pilot showed. |

**Why this works:** It separates measured from self-reported value: the honest version, prompted by our red-team. It also answers the biggest business-model risk, 'why would an agency pay?'

#### 20. Unit economics: one agency, one month
**Speaker:** Kavyanth (COO) · **Time:** ~0:53

| 🖥 SHOW (on screen, the proof) | 🎙 SAY (word for word, the explanation) |
|---|---|
| A waterfall chart: revenue **₹4,216** → AI and messaging −₹713 → tools −₹100 → contribution **₹3,403 (81%)**.<br>Right panel, three gauges filling:<br>- Cost to win an agency: **₹17,900**<br>- Payback: **6.3 months** (gate ≤ 7; small-business software norm ≤ 12)<br>- LTV : CAC **6.3×** (healthy > 3×)<br>Footnote: "Observed inputs: 125 jobs, 82% verified, AI budgeted at 2027 prices, churn assumed 3% (observed ~1.4%). Stays ≥ 4.8× in every ±20% case." | Here's one agency, one month. It pays us about four thousand two hundred rupees. AI and messaging cost about seven hundred, and that's budgeted at next year's higher AI prices. We keep three thousand four hundred: an eighty-one percent margin.<br><br>Winning an agency costs about eighteen thousand rupees, fully loaded with salaries. So it pays back in a little over six months, and over its life an agency is worth six times what it cost to win.<br><br>Every input here is what we observed, not what we hoped. We assume three percent monthly churn when we see one and a half. And if any single input moves twenty percent against us, it stays at four point eight times or better. |

**Why this works:** The course's 'missing unit economics' red flag is answered with observed inputs and a stress test. Stating the conservative assumptions out loud builds credibility.

#### 21. Growth comes from capacity, not hope ✂ *(short version: drop or fold in)*
**Speaker:** Kavyanth (COO) · **Time:** ~0:39

| 🖥 SHOW (on screen, the proof) | 🎙 SAY (word for word, the explanation) |
|---|---|
| An equation builds: **new agencies = field reps × ~80 a year + 10% referrals**.<br>Evidence cards beneath:<br>- "COO closed 8 agencies in 6 months at ~25% of his time = one full-time rep's pace"<br>- "2 of the last 10 came by referral"<br>- "5 → 14 paying agencies in 6 months: ~19% a month, with no salespeople"<br>A small chart: paying agencies by month, 5 → 14. | Can it grow? We don't plan growth from a hockey stick. We plan it from capacity.<br><br>I closed eight agencies in six months using about a quarter of my time. That's the pace of one full-time sales rep: around eighty agencies a year. Two of our last ten came by referral. And we grew from five to fourteen agencies in six months, about nineteen percent a month, with no salespeople at all.<br><br>So the growth plan is simple: hire reps, and each brings about eighty agencies a year. |

**Why this works:** It turns growth from an assertion into a formula with evidence, and sets up the plan and the use of funds.

---
### Act: Why we win

#### 22. Why this isn't solved yet, and where we sit
**Speaker:** Kavyanth (COO) · **Time:** ~0:35

| 🖥 SHOW (on screen, the proof) | 🎙 SAY (word for word, the explanation) |
|---|---|
| A two-axis map. Horizontal: serves the brand/platform → serves the independent agency. Vertical: holds one job → holds the lifetime record + learning.<br>Competitor dots fly in to their places: Urban Company, ServiceOnDoors, Servify, Zoho FSM, Fieldproxy, Bernard (US), voice-AI firms. **Keepwell** pulses alone in the top-right corner.<br>Right column, one line each:<br>- Urban Company takes the customer and keeps 28%<br>- Servify serves brands<br>- Zoho/Fieldproxy: English, per seat<br>- Bernard: no Indian languages, no record | Why hasn't anyone solved this? Because everyone holds a slice. Urban Company takes the customer away from the agency and keeps twenty-eight percent of what the professional earns. Servify works for brands. Field-service software is in English, priced per seat, and needs a dashboard. The closest AI, Bernard in the US, has no Indian languages and no record.<br><br>Nobody serves the independent agency and holds the machine's whole history. That corner is empty, and that's where we are. |

**Why this works:** It answers 'why hasn't X done it' with a picture. Keepwell sitting alone in a corner is the image investors remember.

#### 23. Why nobody can catch up
**Speaker:** Kavyanth (COO) · **Time:** ~0:46

| 🖥 SHOW (on screen, the proof) | 🎙 SAY (word for word, the explanation) |
|---|---|
| Two columns:<br>- **"A rival can copy in a quarter"** (grey, crossed out): WhatsApp intake · prompting an AI model · searching manuals · ranking faults<br>- **"A rival cannot copy"** (teal, counters): 8,200+ verified repair outcomes and growing · a record that follows the machine · a technician-confirmed parts catalogue · Telugu speech corrections · an outcome licence signed by all 14 agencies<br>A flywheel spins in the centre: more agencies → more verified outcomes → better diagnosis → more first-time fixes → agencies stay and pay → more records → plans, claims, parts.<br>Switching-cost chips: rate card · customer histories · technician habits. | Let's be honest about what can be copied. A competitor can copy our WhatsApp intake and our AI in a quarter.<br><br>What they can't copy is what only builds up through use: eight thousand verified repair outcomes and counting, a record that follows each machine, a parts catalogue confirmed by technicians, and our Telugu speech corrections. All fourteen agencies have signed a licence that keeps the de-identified outcomes with us, even if they leave.<br><br>And the longer an agency uses Circuit, the harder it is to leave, because its price list, its customers' histories and its technicians' habits all live there. That's the flywheel. |

**Why this works:** It concedes what is copyable, which is credible, then shows the data moat, the licence that protects it, and switching costs. This covers Product–Uniqueness and the X-factor.

#### 24. The industry forces, and our answer to each ✂ *(short version: drop or fold in)*
**Speaker:** Kavyanth (COO) · **Time:** ~0:33

| 🖥 SHOW (on screen, the proof) | 🎙 SAY (word for word, the explanation) |
|---|---|
| A pentagon of Porter's five forces around "AI for repair agencies in India". Each node has a rating pill and our one-line answer:<br>- **Rivalry: low, rising.** Move first in Tier 2/3.<br>- **New entrants: medium–high.** The moat is outcomes, not the model.<br>- **Buyer power: medium.** Charge only on a verified fix.<br>- **Supplier power (Meta, Google): medium–high.** Model router; budget at 2027 prices.<br>- **Substitutes (phone + notebook): high.** We run inside WhatsApp, so the substitute is our channel. | Quickly, the industry forces. The strongest one is the substitute: a phone and a notebook are free. Our answer is that we run inside WhatsApp, so the substitute becomes our channel.<br><br>Big suppliers like Meta and Google have power over us, so we can switch AI vendors and we budget at next year's prices. New entrants can build an AI wrapper cheaply, which is exactly why our moat is outcomes, not the model. |

**Why this works:** Course vocabulary, kept to 30 seconds. Only the two forces that matter are spoken; the rest sit on screen for anyone who wants to read them.

---
### Act: How big

#### 25. How big: the market, narrowed honestly
**Speaker:** Kavyanth (COO) · **Time:** ~0:54

| 🖥 SHOW (on screen, the proof) | 🎙 SAY (word for word, the explanation) |
|---|---|
| An animated funnel narrowing level by level:<br>- **37,500** repair agencies in India<br>- **22,500** in Tier 2/3 towns, our segment<br>- **1,400** in Telangana + AP, our beachhead<br>- **120**, the Series A gate<br>Beside it, two revenue pools grow: Circuit fees ₹158–396 Cr a year → Keepwell earnable pool ₹1,005–2,370 Cr a year (fees + appliance plans + parts).<br>Footnote: "No official count exists. Built from ~2.5 lakh technicians (ICAP/CEEW), cross-checked with 15 Cr jobs and the ₹9,000 Cr market. Lands at ~147 jobs per agency; our agencies do 125." | How big can this get? No one has ever counted India's repair agencies, so we built the number three ways. From the government's technician estimate, from the number of repair jobs, and from the size of the market. All three agree on about thirty-seven thousand five hundred agencies.<br><br>Twenty-two thousand five hundred are in Tier 2 and 3 towns, which is our segment. Fourteen hundred are in our home states, and a hundred and twenty is our Series A gate.<br><br>Circuit alone is a solid niche. [click] But each record it creates opens plans, parts and claims, and that pool is a thousand to two thousand four hundred crore rupees a year. Circuit is the wedge. The record is the business. |

**Why this works:** The funnel sits right before the growth plan, so every growth number that follows can be checked against the market. The funnel ends at '120', which leads straight into the plan and the ask.

#### 26. The plan, stage by stage: seed → Series A → year five
**Speaker:** Kavyanth (COO) · **Time:** ~0:51

| 🖥 SHOW (on screen, the proof) | 🎙 SAY (word for word, the explanation) |
|---|---|
| Left: one clean chart. Bars = paying agencies by year (**79 → 264 → 945 → 2,196 → 3,793**), revenue above each bar (₹0.2 → 0.85 → 3.6 → 9.6 → 19.2 Cr), EBITDA beneath. Stage bands across the years: **Seed (this raise): Telangana + AP** · **Series A (~month 20): the south, then wider** · **Year 5: national Tier 2/3**.<br>Right: the plan in three plain, numbered sentences:<br>1. **The seed** takes us from 14 to ~264 agencies across Telangana and AP, and proves the Series A gates.<br>2. **A Series A** around month 20 funds field sales into the four southern states, then national.<br>3. **Year 5:** 3,793 agencies · ₹19.2 Cr revenue · EBITDA **+₹2.6 Cr** · 34 lakh machine records.<br>Chips: revenue per agency +33% as plans, parts and claims attach · Y5 is 17% of our segment (our own ceiling: 20%). | Here's the plan, stage by stage. This seed round takes us across Telangana and Andhra: from fourteen agencies to about two hundred and sixty, and it proves the gates a Series A investor will ask for. The Series A, around month twenty, funds field sales into the four southern states, and then national Tier 2 and 3.<br><br>By year five, that's about thirty-eight hundred paying agencies, nineteen crore rupees of revenue, EBITDA positive, and thirty-four lakh machine records. Revenue per agency rises by a third as plans, parts and claims attach — that's the record becoming the business.<br><br>And even then we'd hold just seventeen percent of our segment. We set ourselves a ceiling of twenty. |

**Why this works:** Redesigned to be read at a glance: one chart on the left, the plan as three numbered sentences on the right. Growth stages tied to funding rounds avoids the 'flimsy growth claims' red flag.

---
### Act: The ask

#### 27. Before we ask: trust and compliance, built in and budgeted
**Speaker:** Sri Charan (CTO) · **Time:** ~0:56

| 🖥 SHOW (on screen, the proof) | 🎙 SAY (word for word, the explanation) |
|---|---|
| A grid of the laws that matter. Each card shows the law, why it matters to us, and our status:<br>- **DPDP Act 2023 + Rules** (duties from May 2027): household data needs consent → consent-first record, hosted in Mumbai<br>- **IRDAI:** service plans are insurance products → sold *for* licensed insurers via a registered route; we never underwrite<br>- **CERT-In and the IT Act:** 6-hour incident reporting, 180-day logs → runbook in year 1<br>- **Consumer Protection and CCPA:** no dark patterns in quotes → the owner approves every quote<br>- **Safety (BIS, CEA):** gas, refrigerant, high voltage → hard-stops outside the AI: 47 triggered, 0 incidents in 9 months<br>- **E-waste rules:** recycling (R5) → registered recycling partners<br>A trust strip: AI only / human approves / human only. Budget chip: "₹26 L of compliance and legal inside the ask". | Before we talk about money, one thing matters. We're asking you to back a company that holds household data and will sell insurance products later — so for us, compliance isn't a slide. It's part of the product.<br><br>The data protection law's main duties start in May 2027. We built consent-first from day one, and our data stays in India. Service plans are insurance, so we'll sell them for licensed insurers through a registered route, and we never underwrite. Every quote is approved by the owner, and safety calls are never left to the AI: forty-seven safety stops, zero incidents in nine months.<br><br>And about twenty-six lakh of what we're about to ask for is legal and compliance work, so we're ready before the law requires it. |

**Why this works:** Placed deliberately just before the ask: the last thing an investor hears before the number is that the company is clean, safe and ready for regulation — a reason to invest, not a disclaimer.

#### 28. Before the ask: what the next 24 months need
**Speaker:** Prathyusha (CEO) · **Time:** ~0:55

| 🖥 SHOW (on screen, the proof) | 🎙 SAY (word for word, the explanation) |
|---|---|
| A bridge chart builds bar by bar:<br>- costed requirements for the next 24 months: ₹548 L<br>- + 10% contingency: ₹55 L<br>- − revenue we'll earn: ₹105 L<br>- − cash in the bank: ₹21 L<br>- − government grant still due: ₹10 L<br>- = **the gap: ₹467 L**<br>Beside it, where every rupee goes, by purpose: **finding product–market fit 38%** · team and company 28% · product 23% · sales 10% · working capital 1% — with the note "at Stage 2, the heaviest need is proving product–market fit; every Series A gate is a PMF proof", and what we deliberately don't spend on: consumer ads, a consumer app, a big office. | Now, the money — and we didn't start from a round number. We started from the requirement. We listed everything the next twenty-four months need and costed every line: five hundred and forty-eight lakh. We added ten percent for surprises, then subtracted the revenue we'll earn, the cash we have, and the grant that's still due. The gap is four hundred and sixty-seven lakh.<br><br>And look at where it goes. The biggest share, thirty-eight percent, goes to proving product–market fit: our AI and speech engineers, the agency-success team, price tests in new towns. That is exactly what a company at our stage should spend on. We don't spend on consumer ads, a consumer app, or a big office.<br><br>So that's the requirement. Here is the ask. |

**Why this works:** Exactly the order asked for: the investor first understands what a startup at this stage needs and why, so the number on the next page lands as a calculation, not a wish.

#### 29. The ask, on its own page
**Speaker:** Prathyusha (CEO) · **Time:** ~1:20

| 🖥 SHOW (on screen, the proof) | 🎙 SAY (word for word, the explanation) |
|---|---|
| A full dark page for the ask alone.<br>- **₹4.75 Cr seed**, huge — "to take Circuit from 14 agencies to ~260, and reach the Series A from strength."<br>- The one-line bridge from the previous page: costed need ₹602.9 L − revenue − cash − grant = gap ₹467 L → rounded to ₹475 L.<br>- Four term tiles: **24 months** of runway · **₹4.0 Cr** minimum close (21 months) · **priced Seed CCPS**, one clean class · **20% to one lead seed investor**.<br>- Three columns:<br>  - **What we have today:** 14 paying agencies · 83% one-visit · 78% accuracy · ₹21 L in the bank<br>  - **What your money proves — the Series A gates:** 120 paying agencies by month ~15 · 40,000 machine records by month ~13 · +10 points one-visit at scale · ≥ 97% retention · payback ≤ 7 months · 1 warranty-administrator LOI<br>  - **What comes next:** ~260 agencies and 1.37 lakh records by month 24 → a Series A of ~₹8–10 Cr around month 20, raised from strength → Tier 1, plans and claims. | The ask is four point seven five crore rupees — the four-sixty-seven-lakh gap you just saw, rounded up to the nearest twenty-five.<br><br>The shape of the round, plainly. Twenty-four months of runway, so we never negotiate the next round out of desperation; our minimum close is four crore, which is twenty-one months. Priced seed preference shares — one clean class of stock, the instrument every later investor expects. And twenty percent to a single lead investor, because a clean cap table today is what keeps the Series A simple tomorrow.<br><br>What does your money buy? Three things. Today you're buying what exists: fourteen paying agencies and a product that gets smarter every week. Over the next fifteen months it proves the Series A gates — a hundred and twenty paying agencies, forty thousand machine records, retention above ninety-seven percent, payback under seven months, and our first warranty partner. And then it buys position: at month twenty we raise a Series A of eight to ten crore from strength, not from need.<br><br>One number, one instrument, one lead, and a defined set of proofs. That's the ask. |

**Why this works:** The ask gets its own full page, as the most important slide: the number, the one-line bridge back to the requirement, every term stated and justified in words, and the have / prove / next structure answering 'what do I get'. Valuation, cap table and terms stay in backup.

---
### Act: The future

#### 30. Why now, and who buys Keepwell
**Speaker:** Prathyusha (CEO) · **Time:** ~0:53

| 🖥 SHOW (on screen, the proof) | 🎙 SAY (word for word, the explanation) |
|---|---|
| Two calm halves.<br>Left, Why now: four rows, each a big number and one line. Rs 4.5: AI is finally cheap (a job costs Rs 4.5 to run; we charge Rs 40). 1 in 10: the repair wave is ahead (homes with an AC today). 2027: data law arrives (consent-first records become the standard). R2R: repair is opening up (Right to Repair portal, Repairability Index).<br>Right, Who buys Keepwell: Keepwell in the centre with four buyers around it, one precedent each. Warranty platforms, most likely (Asurion bought Domestic & General, about GBP 2.1 bn). Home services (Urban Company, IPO 103x subscribed). Resale and recycling (Quikr bought Zefo, about Rs 200 Cr). Global service software (ServiceTitan, USD 961M revenue).<br>One line under both: about Rs 66 Cr revenue by year 8, and a strategic sale in years 6-8. | Why invest now? Four reasons. Indian-language AI just became cheap: a job costs us four and a half rupees, and we charge forty. The repair wave is still ahead, because only one home in ten has an AC today. Data law arrives in 2027, so the consent-first record built now becomes the standard. And repair is opening up.<br><br>And who buys Keepwell in the end? Most likely a warranty platform, because our record prices their plans and proves their claims. Asurion paid about two billion pounds for exactly that kind of company. Home services, resale and global service software are the others.<br><br>The plan reaches about sixty-six crore of revenue by year eight, with a strategic sale in years six to eight. |

**Why this works:** Rebuilt for clarity: one number and one line per reason on the left, and a simple hub of four buyers on the right, one precedent each. Far less text, readable at a glance.

#### 31. Back to Ramagundam
**Speaker:** Prathyusha (CEO) · **Time:** ~0:48

| 🖥 SHOW (on screen, the proof) | 🎙 SAY (word for word, the explanation) |
|---|---|
| Dark slide. One click, and the whole ending plays out on its own — the Ramagundam story replays with Keepwell, each beat ticking green in sequence:<br>1. the voice note is answered in minutes, in Telugu, in the agency's name<br>2. Circuit knows this model, this town, this heat: it's almost always the capacitor<br>3. the technician arrives the same afternoon, with a ₹350 part in his pocket<br>4. fixed in one visit · verified · the record grows by one, and every agency gets smarter<br>5. a 74-year-old man sleeps that night in a cool room<br>…then the final line fades in beneath: **"Keepwell becomes the record everyone checks before touching a machine."** Prathyusha · Sri Charan · Kavyanth · raising ₹4.75 Cr. | Let's go back to Ramagundam one last time. [click — then let the screen play on its own]<br><br>With Keepwell, the son's voice note is answered in minutes, in Telugu, in Ramesh's name. Circuit knows this model, this town, this heat — it's almost always the capacitor. The technician arrives the same afternoon with a three-hundred-and-fifty-rupee part, fixes it in one visit, and the fix is verified — so every agency on the network gets a little smarter. And a seventy-four-year-old man sleeps that night in a cool room.<br><br>Today that happens for fourteen agencies. With your help, it happens across India. Keepwell becomes the record everyone checks before touching a machine.<br><br>Thank you. |

**Why this works:** It mirrors the opening and resolves the human story, not the money story. One click: the beats cascade on their own, so the speaker never touches the clicker again. End on the vision line, then stop talking.

---
## Backup slides (press B; Q&A only)

#### Backup · Valuation (Q&A only)
- **Show:** Three course methods: comparable ₹24.8 Cr post · scorecard ₹24.1 Cr · VC method ₹24.2 Cr. Pitched at ₹19 Cr pre / ₹23.75 Cr post, never above the VC-method price. Investor base case ~35% IRR (6.2×); conservative ~21%; aggressive ~47%. Walk-away floor ₹16 Cr pre.
- **Say:** Only if asked: 'We used three methods from the course and priced at the investor's own required-return price, so the base case clears a 35% IRR.'

#### Backup · Cap table (Q&A only)
- **Show:** After seed: founders 67.9% · angels (iSAFE) 2.1% · ESOP 10% · lead VC 20%. After Series A 54.3% founders; after Series B 46.2%.
- **Say:** Only if asked: 'Founders keep a majority through the Series A. One iSAFE converts at its cap, and its preference is capped at what the angels put in.'

#### Backup · Terms we'd accept (Q&A only)
- **Show:** 1× non-participating preference · broad-based weighted-average anti-dilution · board 2 founders + 1 investor + 1 independent · 4-year vesting with credit since May 2025 · deal costs capped at ₹8 L · the lead reserves for its Series A pro-rata.
- **Say:** Only if asked: 'Standard, founder-friendly seed terms, the MediQuick template with two asks: vesting credit, and a reserve for the Series A.'

---
## Before you present
- **Media files** live in `media/`. They hold redacted real evidence, so they are kept out of the public GitHub repo. Copy the whole `story_deck/` folder to the presenting laptop.
- **Fonts** load from Google Fonts. Open the deck once while online, or it falls back to Georgia and the system sans-serif.
- **The demo tab** 'The Circuit website' loads `media/circuit_landing.html`. 'A real run' plays `media/circuit_live_run_30x.mp4`.
- **Rehearse the five turning points word for word:** the hook (1), Ramagundam (2), the insight (5), the learning curve (18) and the ask (28).
- **Never say** 'DPDP-compliant', 'AI diagnosis', or any number that isn't in the model.
