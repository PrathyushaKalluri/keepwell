# Step 3: Ecosystem map

**Phase A: who we are. Status: DRAFT for approval (20 Nov 2026).**

> **Illustrative case** for the IIIT Hyderabad ESFS course pitch.
> - **Real and sourced [R]:** schemes, players and prices.
> - **Assumed [Story]:** the status of each partnership, kept consistent with Step 2.

**Builds on:** Steps 1–2 (approved). **Feeds:** Step 5 (product and competition), Step 7 (model inputs), Step 8 (cost lines and grants).

---

## 3.1 What this map is for
Keepwell does not own the shops, the brands, the technicians or the recyclers. It **connects people who already trust the founders** (Step 2). This map lists each partner, then answers four questions:
1. What the partner gives us.
2. What the partner gets.
3. Where the relationship stands today [Story].
4. Which model number it moves.

The last column of each table matters most for investors. Every partnership is tied to a driver in `ue_v2.py`, not shown as a logo.

## 3.2 Demand and channel partners (who brings the customer)
| Partner | They give us | They get | Status [Story] | Model number it moves |
|---|---|---|---|---|
| **Independent multi-brand appliance shops** (the core channel) | Their buyers. Our service runs under the shop's name. Installs are routed to us; past customers are referred | A commission on every job (5–12%). Relief from complaints and joint liability [R]. A record of every buyer. Upgrade and renewal leads (Phase 3) | 40+ shops signed in the Vijayawada–Guntur pilot cluster (Step 6) | Shop density (sensitivity rank 1); install routing (rank 5) |
| **The largest multi-brand distributor in AP/TS** (the CEO's former employer type) | Warm introductions to 600+ dealers, and dealer sales data to target shops | Happier dealers who sell more; a service story for its dealer meets | Informal; the regional team introduces dealers | Shop CAC ₹22k → about ₹10k |
| **Regional consumer-electronics dealers' association (AP)** | Endorsement; access to dealer meet-ups | A member benefit to offer | President is an advisor (Step 2) | Shop CAC; trust |
| **Plan sellers** (device-protection and extended-warranty platforms, Onsitego / Zopper / OneAssist type [R]) | Paid fulfilment jobs for their small-town claims. Later, they buy verified records | A repair partner in towns where they have none [R: Onsitego left consumer repair because acquiring customers cost too much] | Pilot letter Jan 2026 (Step 2) | About 100 jobs a month per cluster as off-season filler; first customer for the verification data layer |

## 3.3 Authorisation and supply partners (who lets us do the work)
| Partner | They give us | They get | Status [Story] | Model number it moves |
|---|---|---|---|---|
| **Brand-authorised service centres** (ASCs) | Sub-contracted installs and in-warranty jobs for their brands (AC, washing machine, refrigerator). A third-party AC install without authorisation **voids the warranty** [R] | Capacity in the peak; certified technicians; jobs closed against their service targets | 2 sub-contracts in Vijayawada covering 2 brands (Nov 2025), through the COO | Authorised coverage 35% → 45% (rank 2); install fee received (rank 3) |
| **Appliance brands' regional service teams** | Direct authorisation in year 2 (installs, in-warranty jobs). Parts and manuals | Faster installs and better ratings in towns they can't staff. Field-failure data later | Talks with 2 brands through the COO and the ex-national-service-head advisor | Authorised coverage; failure-intelligence layer (Phase 3) |
| **Parts distributors** | Genuine and compatible parts on credit; weekly runs | One consolidated buyer with predictable demand | 2 distributors in Vijayawada (CEO's credit network) | Parts margin 20% → 30% (pooled buying); working capital |
| **Exchange and e-waste operators** (Selsmart / Attero, Digi2L, Recykal, Karo Sambhav [R]) | A fee per trade-in pickup; e-waste handling fee. They hold the EPR certificates, not us [R] | A field arm in towns where they have no pickup network | Advisor in place; partnership from year 2 | Trade-in about ₹230 contribution a unit [R]; e-waste feeder |

## 3.4 Technician supply partners
| Partner | They give us | They get | Status [Story] | Model number it moves |
|---|---|---|---|---|
| **Certified partner technicians** (the supply) | Paid per job, plus an off-season floor for the core group | Steady jobs, parts on credit, insurance, a certificate, payout in 48 hours | 22 certified in the pilot (Step 6) | Jobs per day, leakage, quality |
| **Government ITI Vijayawada (RAC trade); JCH-Hitachi / APSSDC AC skill centre** [R] | Trained entrants; a place to run certification | Placements for their trainees | Placement tie-up | Technician supply; training cost |
| **ESSC / PMKVY (Skill India)** [R] | Training subsidy of about ₹2,800–6,760 per trainee; RPL reward ₹500 per candidate [R] | Certified outcomes | Applied | Lowers training cost per technician |

## 3.5 Money, programmes and technology partners
| Partner | They give us | Status [Story] | Model or budget line |
|---|---|---|---|
| **AP Startup Policy 4.0** [R] | Grant up to ₹15–20 L; seed equity up to ₹50 L; go-to-market support up to ₹50 L (equity) | ₹15 L sanctioned, ₹10 L received (Step 2). Seed-equity application to be considered in Step 8 | Non-dilutive offset in Step 8 |
| **DPIIT recognition** [R] | Startup status; tax and compliance benefits; access to schemes | Recognised (Step 2) | Step 10 |
| **T-Hub and the Google for Startups hub at T-Hub, Hyderabad** [R: hub opened Dec 2025] | Mentoring, investor access, Google Cloud credits | HQ team is part of the programme | Cloud and AI cost offset (§3.6) |
| **Telangana T-Fund** [R] (₹25 L–1 Cr cheques) | A possible co-investor for the Warangal cluster | Not approached; reserved for cluster 2 | Step 8 option |
| **Meta WhatsApp Business API via a BSP; Gemini; Sarvam (speech); UPI / Razorpay** [R] | The AI service layer's building blocks, at under ₹5 a job [R] | Live | Technology cost per job |
| **Insurers** (group personal accident; public liability) [R] | Cover at about ₹2.5 a job [R] | Live | Insurance line |

## 3.6 What the Google credits do and don't cover
**Covered:**
- Google Cloud usage: hosting, database, storage, speech.
- Gemini / Vertex AI.

The high-volume calls of the AI service layer run on Gemini: voice-note transcription, job-card extraction, photo and serial checks, reminders.

**Not covered:**
- Third-party services, e.g. the WhatsApp BSP fees and Sarvam speech-to-text.
- Salaries and field teams.

**Honest size:** our technology cost is under ₹5 a job [R], so the credits offset a **small** line. Step 8 counts only the cloud and AI spend we would actually use, never the headline credit amount.

## 3.7 Not partners now, and why
| Who | Why not now | When |
|---|---|---|
| **Urban Company** | It competes for households in Vijayawada and Guntur [R: live AC pages], and it does not serve shops | Possible buyer at exit (Step 9) |
| **Regional chains** (Bajaj Electronics, Sathya) | They already have extended-warranty partners (Onsitego, OneAssist) [R]. Our customer is the independent shop | Year 3+: offer verification and fulfilment |
| **Consumer-durable lenders** (Bajaj Finance type) | Ownership data for underwriting is low-feasibility and needs consent and scale [R] | Year 5+, if at all |
| **AI manufacturing inspection buyers** | Out of scope (00b) | Never; we sell field-failure data instead |

## 3.8 What the ecosystem cannot give us, which is why we raise
| Need | Can partners or grants cover it? |
|---|---|
| Cluster teams and shop onboarding for 3 clusters (about ₹20 L per cluster to open, plus fixed costs until breakeven) | **No.** Grants are capped at ₹15–20 L. Course M2: grants don't scale |
| Off-season floor for core technicians, and working capital (parts stock, exchange float) | **No.** Partners give credit terms, not cash |
| Engineering to harden the AI service layer: consent, audit trail, verification-grade records for brands | **Partly.** Credits cover cloud and AI; salaries need equity |
| 18–24 months of runway to the next round's milestones | **No.** Only equity capital does this |

**This table is the bridge to Step 8:** it lists what the next round must pay for.

---

## Decisions to approve (Step 3)
1. The **partner map**, as organised in §3.2–3.5:
   - **Channel:** shops, the distributor, the dealers' association, plan sellers.
   - **Authorisation and supply:** service centres, brands, parts distributors, exchange and e-waste operators.
   - **Technicians:** partners, ITI / APSSDC, ESSC.
   - **Money, programmes and technology:** AP Policy 4.0, DPIIT, T-Hub / Google, T-Fund, the technology stack, insurers.
2. **Each partner is tied to a model number** (this table goes into the deck appendix).
3. **Status of the partnerships [Story]:**
   - 2 service-centre sub-contracts
   - 1 plan-seller pilot letter
   - 2 parts distributors
   - an ITI placement tie-up
   - AP grant ₹15 L sanctioned
4. **Not now:** Urban Company, regional chains, lenders, inspection buyers.
5. **Google credits** are counted only at real usage.

On approval, the next step is Step 4: market and problem scale.
