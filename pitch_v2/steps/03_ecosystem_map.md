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

## 3.4 Technicians: our delivery partners (not employees, not trainees)

**What the relationship is.** Keepwell doesn't hire technicians as employees, and it doesn't run a training academy. Keepwell is the **principal**: it sets the price, gives the guarantee and collects the money, so the household and the brand pay Keepwell. The work is done by **independent local technicians and small repair agencies who sign up as Keepwell partners**. They are contractors paid per job, the way Urban Company partners are [R].

**Why they matter to the business:**
- They are **our biggest cost**: about 60% of the labour on every job.
- They decide **quality**: first-visit fix rate, rework, the shop's reputation.
- Brand authorisation through service centres needs **named, checked technicians** for each install [R: authorised-installer rule].

So they are a partner group we must manage well, even though they are not a revenue source.

**The business model with technicians** (BASE, `ue_v2.py`):

| Job | Who pays Keepwell | Technician gets (per job) | Keepwell keeps (contribution) |
|---|---|---|---|
| AC install (brand-authorised) | Brand / service-centre fee about ₹900 + materials about ₹1,270 net | ₹500 | about ₹470 |
| Out-of-warranty repair or service | Household, about ₹1,000 incl. GST | about ₹330 (60% of labour) | about ₹164 |
| AMC visit | Household (₹1,299 plan, 2 visits) | ₹400 a visit | about ₹100–200 per plan |

**What technicians pay Keepwell:** nothing. There is no joining fee and no commission charged to them.

**What they get from Keepwell:**
- **steady extra jobs:** about ₹15k a month on top of their own customers
- **an off-season minimum** for a core group
- **parts on credit**
- **insurance**
- **payout within 48 hours**
- **the shop's and the brand's backing**

**What Keepwell gets in return:**
- capacity without salaries
- photo-verified work under our guarantee
- the appliance record from every visit

**The only "training" is a short onboarding**, about 2–3 days. It is not a course. It covers:
- our app and the photo and serial checklist
- the safety rules (gas, electrical)
- the brand's install standard
- the code of conduct

That is what the guarantee and the authorisation require.

**Later, technicians become a revenue source in one way only.** In Phase 2 (Supply), they can **buy parts from Keepwell** (parts margin, 00b). Nothing else is planned.

**Where we find them:** through the COO's network of 200+ service-centre owners and their technicians (Step 2), and through local agencies that join as partners.

**Recruitment channels for later, not partners now:** ITI trainees and skilling subsidies (ESSC/PMKVY, about ₹2,800–6,760 per trainee [R]). They matter only once we need hundreds of technicians across many clusters (year 3+). They are **not part of the pilot or the pitch's core**.

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
   - **Technicians:** certified partner technicians and agencies, paid per job (§3.4). They are delivery partners: no employment, no academy, no fee charged to them. ITI and ESSC are only later recruitment channels.
   - **Money, programmes and technology:** AP Policy 4.0, DPIIT, T-Hub / Google, T-Fund, the technology stack, insurers.
2. **Each partner is tied to a model number** (this table goes into the deck appendix).
3. **Status of the partnerships [Story]:**
   - 2 service-centre sub-contracts
   - 1 plan-seller pilot letter
   - 2 parts distributors
   - AP grant ₹15 L sanctioned
4. **Not now:** Urban Company, regional chains, lenders, inspection buyers.
5. **Google credits** are counted only at real usage.

On approval, the next step is Step 4: market and problem scale.
