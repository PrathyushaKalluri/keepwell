# Step 3 — Ecosystem map
**Phase A: Who we are · Status: LOCKED 16 Nov 2026**
**Tags:** **[Real]** = case-competition build, research or survey · **[repo]** = team repo `ESFS/keepwell/` · **[web]** = checked online on 16 Nov 2026 · **[Story]** = assumed backstory.
**Plan:** [`../pitch_bible.md`](../pitch_bible.md) · **Builds on:** Steps 1–2 (locked) · **Feeds:** Step 8 (what the seed must pay for), Step 12 (the "who's backing us" slide)

## 3.1 What this map is for
The course asks for **five ecosystem partners needed now, each with a one-sentence justification and an engagement plan** (M1 activity). Stage 2 partners should be:
- **early-stage VCs**
- **strategic angels** who "introduce pilot customers"
- **government pilot schemes**
- **research institutions**
- **industry associations** that make "introductions to early adopters"

In the pitch, the map does three jobs:
1. **Credibility.** Others have already checked us and put something behind us.
2. **Leverage.** We got help without giving up equity, so the VC's money goes further.
3. **Justifying the ask.** It shows what the ecosystem *cannot* give us. That is what the seed money pays for.

**Rule:** each category gets the partners that are already doing something specific for us, or that the seed round directly unlocks. Nothing is listed just because it exists.

## 3.2 The five partners
Five of the six sit in one place, **IIIT Hyderabad and our two Telangana pilot towns**, and the sixth (Google) is unlocked by the seed. That is the story: a team rooted in one institution and one region, with every partner reinforcing the others.

| # | Category (M1) | Partner | What they have done for us **[Story unless marked]** | What they do in the next 18 months | What it means for the ask |
|---|---|---|---|---|---|
| 1 | **Investors** | **2 operator angels** (an ex-founder from home services; an ex-head of service at a durables brand) | Put in ₹30L via iSAFE before the pilot. Introduced 3 of the 5 pilot agencies | Introductions to the seed lead and to warranty administrators (the R2/R3 buyers) | Proof that industry insiders backed us first. **The seed VC is the next partner in this row**: the cheque the ecosystem can't write |
| 2 | **Government** | **Startup India Seed Fund (SISFS)**, via our incubator | ₹20L grant **applied for** via CIE-IIITH (Nov 2026), for proof of concept and product trials **[web: up to ₹20L, milestone-based, via incubators]** | Evaluation and, if sanctioned, milestone-based release | **Not counted in the ask.** If sanctioned, ~₹20L of non-dilutive runway |
| 3 | **Incubator** | **CIE-IIITH** (IIIT Hyderabad's incubation centre) **[Real institution]** | Incubated since Oct 2026. Routes our SISFS application. Set up governance, books and a data room from day one | Investor introductions, diligence readiness, mentoring through the seed close | The "CIE-mentored, clean diligence" signal the course rewards (M3, Startup–Quality) |
| 3b | **Accelerator / corporate programme** (not incubation) | **Google for Startups Cloud Program, AI tier** | Relationship began with our **Google Startup Buildathon** submission **[Real]** | **Unlocked by the seed round.** The AI tier is for Seed-to-Series-A-funded startups: up to **$350k** of credits, $250k in year 1 and up to $100k in year 2, valid 24 months **[web]**. Covers Google Cloud usage: hosting, database, storage and Gemini/Vertex models | **Cloud and AI cost is paid by credits for two years** while agencies are on free days and low fees, so the seed money goes to people and field work. This is also a reason to raise from a VC rather than only angels: VC backing unlocks the credits |
| 4 | **Research institution** | **IIIT-H speech and language lab** (our faculty mentor) | Benchmarked Circuit's Telugu speech recognition on real agency voice notes | Builds the golden test audio and vernacular lexicon the repo requires before scaling; a joint student project | Closes the repo's #2 risk (Telugu/Tamil accuracy) at research cost, not hiring cost |
| 5 | **Networks and associations** | **Our trade network + parts wholesalers in the pilot towns**: a ten-man family carpenter crew **[Real]**, FixNear's 1,200 former partner technicians, the COO's ex-brand service partners | Brought the 18 interviewed agencies and the 5 pilot agencies | The route to the first ~120 paying agencies. Every agency visits a parts counter, which is why the case-competition GTM plan had ~30% of agencies coming via wholesalers **[Real]** | Low-cost acquisition, so the CAC in Step 7 is credible |

**Professional enablers** (the CA/CS firm and the lawyer) are hygiene, not story. They appear in Step 10 (compliance) and as cost lines in Step 8. Our two advisors (the safety expert and the lawyer) are already in Step 2.

## 3.3 What the ecosystem cannot give us, which is why we raise
| Need for Stage 2 (from the repo) | Can the ecosystem cover it? |
|---|---|
| Field team to take 5 agencies to ~120 across more towns | No. Grants are capped at ₹20L and can't fund scale (course M2: grants "don't scale") |
| Engineers to harden Circuit: safety hard-stops, consent, eval harness (repo "Foundations, must precede any customer data") | No. The lab supports research, not product engineering |
| AI cost on every job before a fee is earned, during free days | **Largely, once the seed unlocks Google for Startups credits.** The size of the offset is computed in Step 8 from the real cost lines. The $350k is a ceiling, not what we will consume |
| Lawyer and safety sign-off before launch | No. Paid work (Step 8) |
| Runway of 18–24 months to reach Series A milestones | No. Only equity capital does this |

This table is the bridge to Step 8: **it lists what the seed money pays for.**

## 3.3a What the Google credits do and don't cover (checked 16 Nov 2026)
- **Covered:** Google Cloud usage, which means hosting (Cloud Run), database (Cloud SQL), storage, speech, and **Gemini / Vertex AI models** **[web]**.
- **Not covered:** "third-party services or offerings, including those on Google Cloud Marketplace" **[web]**. Partner LLMs in Model Garden get only a **separate allowance of up to $10k** **[web; repo]**. Whether Claude qualifies is **unconfirmed**.
- **What this means for Circuit.** If every model call stays on Claude, the credits mostly pay for hosting and storage. The repo puts that at about ₹1,000–3,000 a month at pilot, which is small. For the credits to cut our real cost per job, the **high-volume, low-judgment calls** run on **Gemini on Vertex**:
  - language detection and routing
  - voice and photo extraction (model, serial, invoice)
  - the safety second-reader
  - reminders and message drafting

  **Claude stays the root-cause reasoning engine** (the moat, and our MVP). This follows the repo's own design: a model router, "one SDK wrapper, no vendor calls from feature code", and swappable vendors. It also matches the repo's routing, where these tasks were already assigned to Flash and Flash-Lite. **Decided: all-Gemini (see the decisions log).**
- **The honest size of the benefit.** The credits offset cloud and AI cost, not salaries or field teams. Step 8 will show what share of the seed budget they cover. We will not claim the full $350k as savings.

## 3.4 Not partners now, and where they live instead
| Item | Why it isn't on the map | Where it goes |
|---|---|---|
| Other incubators and accelerators (T-Hub, WE Hub) | One incubator is enough. More programmes cost founder time and look like collecting logos. (Google for Startups stays: it is a credits programme tied to the ask, not incubation) | Not used |
| Bhashini | A technology option, not a partner | Step 5 (only if needed for Telugu/Tamil hosting) |
| DoCA / National Consumer Helpline, Toxics Link, CEEW, LocalCircles | Data sources, not partners | Step 4 (market and problem slide) |
| NSDC / DGT technician courses | A possible acquisition channel | Step 7 (only if the CAC model needs it) |
| Warranty administrators (Servify, OneAssist, Onsitego, Zopper), insurers | R2/R3 partners and acquirers, after the seed | Steps 7 and 9 |
| Banks, venture debt, the SISFS debt tranche | No revenue to service debt; adds instruments before the seed | Not used |
| Urban Company | Competitor (takes the agency's customer, keeps 28.3%) **[repo]** | Step 5 |

## 3.5 How it shows up in the pitch
**One slide, "Who's already backing us":**
- the partner logos, with Google shown as "unlocked by this round"
- one line each on what they did
- the closing line: *"They took us from idea to a paid pilot. The seed takes us from 5 agencies to 120."*

It feeds the course's Startup–Quality score ("CIE-mentored, clean diligence"), Startup–Uniqueness ("network access") and the X-factor ("local alumni mentor effect", M3).

---

## Decisions log (LOCKED 16 Nov 2026)
- **Six partners:** operator angels, SISFS, CIE-IIITH, Google for Startups Cloud Program AI tier (unlocked by the seed), the IIIT-H speech lab, and our trade network plus parts wholesalers.
- **Model stack:** all Gemini on Vertex AI (Mumbai), as designed in the repo. The Google credits then cover AI cost as well as hosting, and the Telugu/Tamil hosting gap is closed in India. Pitch wording: *"built model-agnostic, proven on Claude, production on Gemini"*. The moat is not the model, so the story is unchanged.
- **Framing:** "IIIT-H and two Telangana towns, plus Google unlocked by this round."
