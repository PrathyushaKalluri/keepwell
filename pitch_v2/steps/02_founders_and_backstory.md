# Step 2: Founders and company backstory (rebuilt from scratch)

**Phase A: who we are. Status: DRAFT for approval (20 Nov 2026).**

> **Illustrative case.** Built for the IIIT Hyderabad ESFS course pitch. The founder names are the real team. Their histories, the company timeline, the pilot and the money raised are **[Story]**: assumptions kept consistent across every document. Employers are described generically (e.g. "a top-5 AC brand") so the pitch doesn't impersonate or misattribute any real company.

**Tags:**
- **[Story]** assumed backstory
- **[R]** research in `pitch_v2/research/`
- **[Model]** `ue_v2.py`

**Builds on:** Step 1 (approved). **Feeds:** Step 6 (pilot), Step 8 (ask), Step 9 (cap table), Step 10 (clean company), Step 11 (Startup row of the fundability matrix).

---

### 2.1 What the business needs from its founders (derived from Step 0)

Each "what decides it" item is a key driver of the Step 0 unit economics.

| The business lives or dies on… | What decides it [Model] | So we need a founder who has… |
|---|---|---|
| **Signing 50–70 independent shops per cluster** | shop density (sensitivity rank 1); routing at least 50% of installs | sold to these exact dealers and is trusted at their counters |
| **Brand authorisation for installs** | authorised coverage (rank 2); install fee (rank 3) | run a brand's service network and knows how authorisation is granted |
| **Technician supply, quality and the off-season** | jobs per day, payout, leakage | recruited, trained and managed field technicians at scale |
| **Running 50–70 shops with a small team** | the AI service layer, at under ₹5 a job | built Indian-language voice and WhatsApp systems in production |

That gives three muscles: **winning shops, running the field, building the system.**

---

### 2.2 The three founders [Story]

| | **Prathyusha Kalluri, CEO** | **Kavyanth Munagala, COO** | **Sri Charan Peri, CTO** |
|---|---|---|---|
| **Owns** | Retailers, brands, fundraising, the P&L | Technicians, service quality, authorisation, parts | The AI service layer, data, security and DPDP (acting Data Protection Officer) |
| **Before Keepwell** | **9 years of consumer-durables channel sales.** Area sales manager, then regional sales head for Andhra Pradesh at a top-5 AC brand. Managed about **350 independent dealers** across the Krishna–Guntur–Godavari belt | **8 years of brand after-sales.** Ran an appliance brand's authorised-service network across AP and Telangana: about **220 service centres and 3,000 technicians**, plus installation service-level targets, warranty claims and regional parts depots | **7 years of Indian-language voice AI.** Built WhatsApp and voice intake systems handling about **2 million calls a month** for a conversational-AI company. Previously worked on dispatch and routing software |
| **What they saw** | Dealers lost sales and goodwill over late installations they didn't control. A Guntur dealer showed her a consumer-court notice naming him alongside the brand | A third of the installation complaints in small towns were really technician shortages, and out-of-warranty customers were turned away | Most service calls in small towns arrive as Telugu voice notes that nobody structures |
| **Why they're credible here** | Grew up in **Vijayawada**, the pilot hub. Knows dealers by name and is trusted at the counter | Knows how a brand grants installation authorisation and what it pays service centres. Knows technician economics | Has shipped production AI at a cost per call that matters |
| **Links to the research** | I1, F7, F13 (`00_tough_questions.md`) | I3, F3–F5, F9, F11 | T1–T7 |

**How they met [Story].** Prathyusha and Kavyanth worked at the same AC brand, she in sales and he in service. They kept hearing the same complaint from opposite sides: dealers said service was failing them, and service said dealers sent customers with no records. Sri Charan, a college friend of Kavyanth's, had built the voice systems a brand call centre used.

**The gap we name ourselves:** none of the founders has run a startup to exit. We close it with advisors who have scaled service businesses (§2.3) and with a board from the next round.

**Founder–problem fit for the fundability matrix (M3, Startup row):**
- **Potential:** three complementary operators with domain depth.
- **Uniqueness:** a CEO with existing trust at the target dealers' counters, and a COO who knows the authorisation route.
- **Quality:** full-time, vested, a clean company (§2.5).

**X-factor candidate (Step 1):** *"the founder who sold to these very dealers."*

### 2.3 Advisors and board [Story]

Each advisor is chosen to fill a named gap. Advisors join on ESOP grants, not as investors.

| Advisor | Gap filled | Role |
|---|---|---|
| A former national service head of an appliance brand | Brand authorisation and plan-seller introductions | Monthly; opens the doors to AC brands and Onsitego-type fulfilment |
| The president of a regional consumer-electronics dealers' association (AP) | Shop access beyond the CEO's network; trust | Introduces dealers; testimonial |
| A field-service operator who has scaled a home-services business to 20+ cities | Scaling experience | Quarterly; cluster playbook |
| A CA/CS firm and a startup lawyer (on retainer) | Compliance and contracts | Step 10 |

**Board:** the three founders today. One independent director or investor seat comes at the next priced round (Step 9).

### 2.4 Company timeline [Story]

Backdated so that the Vijayawada–Guntur summer pilot has happened. Its results are in Step 6.

| When | What happened |
|---|---|
| Mar 2025 | Prathyusha leaves her sales role. All three founders commit |
| **Apr–Jul 2025** | **Discovery in Vijayawada, Guntur and Warangal:** shops, technicians, households, and talks with brand service centres. The numbers are in Step 6 |
| **Aug 2025** | **Keepwell Services Pvt Ltd incorporated** (Hyderabad, with a Vijayawada branch office). DPIIT recognition. All founders full-time |
| Sep–Nov 2025 | **AI service layer, first version:** WhatsApp and voice intake in Telugu, Hindi and English, job cards, a photo and serial checklist, the appliance record and QR code. Technician certification curriculum written |
| **Nov 2025** | **Installation sub-contract with an authorised service centre** in Vijayawada covering two AC brands. This is the route to authorisation that Step 0 required |
| **Dec 2025** | **Pre-seed: ₹45 L on an iSAFE** from three operator angels (§2.6) |
| Feb 2026 | **AP Startup Policy 4.0 grant sanctioned: ₹15 L** (₹10 L received; ₹5 L on a milestone) [R: policy exists, our sanction is Story] |
| **Mar–Jun 2026** | **Summer pilot in the Vijayawada–Guntur cluster.** It started with 12 shops and grew. Results are in Step 6 |
| Jul–Oct 2026 | **Off-season run:** washing machines, fridges, water purifiers, AMC renewals. The cluster keeps growing. Warangal is scouted as cluster 2 |
| **Nov 2026** | **Raising the next round.** Amount and instrument are set in Steps 8–9 |

### 2.5 Money raised and spent so far [Story]

**Raised: ₹70 L**

| Source | Amount | Instrument | When |
|---|---|---|---|
| Founders' own money | ₹15 L | Equity, at incorporation | Aug 2025 |
| Three operator angels | ₹45 L | iSAFE (§2.6) | Dec 2025 |
| AP Startup Policy 4.0 grant | ₹10 L received (₹15 L sanctioned) | Grant, non-dilutive | Feb 2026 |

**Spent: about ₹52 L** (Aug 2025 to Oct 2026)

| Item | ₹ L |
|---|---|
| Founders' living stipend (3 × ₹50k × about 14 months) | 21 |
| Pilot cluster operations (manager, dispatcher, training, office, onboarding; part-year) | 13 |
| Technology (cloud, WhatsApp, AI usage, devices) | 4 |
| Cluster setup and working capital (tools, kits, parts stock) | 6 |
| Legal, compliance, insurance | 3 |
| Travel, discovery, miscellaneous | 5 |
| **Total** | **52** |

**Cash today: about ₹18 L**, plus the ₹5 L grant tranche still due. Contribution from pilot operations is netted inside the cluster line. Step 6 reconciles the pilot's contribution exactly.

### 2.6 The pre-seed instrument: why an iSAFE from operator angels (with later rounds in mind)

**Why operator angels.**
- **Who they are:** a retired appliance-brand service head, a multi-store dealer from Guntur, and an ex-home-services founder.
- **What they did besides the money:** they introduced the service centre that gave us the sub-contract, plus 6 pilot shops.
- **The signal:** at Stage 2, insiders who checked the business and put money in send a stronger signal than friends and family (course M1/M2).

**Why an iSAFE.**
- **It is CCPS under Indian law.** It converts at the next priced round, at the lower of the cap and the discounted round price (M2).
- **It postponed the valuation.** We had no data in Dec 2025, so we didn't have to set a price yet.
- **No angel tax.** Angel tax was abolished from AY 2025-26 [R].

**Terms [Story]:**
- **Cap:** ₹6 Cr **post-money**, at the low end of the ₹6–8 Cr range for a team without data [R].
- **Discount:** 20%.
- **Preference:** capped at the ₹45 L invested.
- **Rights:** information rights only.
- **Pro-rata:** a pro-rata right for the next round only.
- **Long stop:** converts at the cap after 24 months if no round happens.

**How it behaves in later rounds.** This is an illustrative sensitivity, not a decided round: the next-round price is set in Step 9. A post-money cap fixes the angels' stake at **7.5%** (₹45 L ÷ ₹6 Cr), however high the next round is priced. That makes their dilution predictable. The trade-off is that the cost falls on the founders if the next round is priced low.

| If the next round's pre-money is… | Angels convert at | Angels' stake right after conversion | Founders' combined stake before the new money |
|---|---|---|---|
| ₹8 Cr | the cap | 7.5% | 92.5% |
| ₹12 Cr | the cap (discount gives more) | 7.5% | 92.5% |
| ₹20 Cr | the cap | 7.5% | 92.5% |

**Designed out (same five protections as the course playbook):**
- one note, one cap, closed
- preference capped at the amount invested
- no board seat or vetoes
- the most-favoured-nation clause ends at the next round
- a long-stop conversion

**The ESOP pool (10%)** is created at the next round. Its effect is set out in Step 9.

**Equity today (fully diluted, iSAFE unconverted):**

| Founder | Equity |
|---|---|
| Prathyusha | 38% |
| Kavyanth | 31% |
| Sri Charan | 31% |

All founder shares vest over 4 years with a 1-year cliff (reverse vesting), counted from Aug 2025.

### 2.7 Clean-company checklist, already in place [Story] (M3 Startup–Quality; feeds Step 10)
- **Company papers:** MoA, AoA, CIN, PAN, GST registration (Andhra Pradesh and Telangana), Shops & Establishments registration, statutory registers.
- **DPIIT:** startup recognition.
- **Founders:** a founders' agreement with vesting, plus **IP assignment** of all code, the AI service layer, the certification curriculum and the brand name to the company. The trademark "Keepwell" is filed.
- **Signed contracts:**
  - a service-centre installation sub-contract
  - a **standard shop service-arm agreement**: multi-year, revenue share, the shop's name on the guarantee, and customer consent for the record
  - a **partner-technician agreement**: per-job pay, the off-season floor for core technicians, the code of conduct and non-solicit
- **Insurance:** group personal accident for technicians, public liability.
- **Finance:** a CA/CS firm on retainer, monthly books, a separate bank account, and grant-utilisation reports.
- **Data protection (DPDP):** household consent captured in-product, with a stated purpose, withdrawal and retention limits.

---

## Decisions to approve (Step 2)

1. **Founders and roles:**
   - **Prathyusha Kalluri, CEO:** channel sales; AP dealers; from Vijayawada.
   - **Kavyanth Munagala, COO:** brand service network; authorisation; technicians.
   - **Sri Charan Peri, CTO:** Indian-language voice AI; acting Data Protection Officer.
2. **Advisors:** an ex-brand national service head, an AP dealers' association president, a scaled field-service operator, and a CA/legal firm on retainer. All on ESOP.
3. **Timeline:**
   - discovery Apr–Jul 2025
   - incorporated Aug 2025
   - service-centre sub-contract Nov 2025
   - pre-seed Dec 2025
   - AP grant Feb 2026
   - **summer pilot Mar–Jun 2026**
   - off-season run Jul–Oct 2026
   - raising Nov 2026
4. **Money so far:**
   - raised ₹70 L: founders ₹15 L, iSAFE ₹45 L, AP grant ₹10 L
   - spent about ₹52 L
   - cash about ₹18 L
5. **Pre-seed terms:** iSAFE, ₹6 Cr post-money cap, 20% discount, preference capped, information rights only.
6. **Equity:** 38 / 31 / 31, with 4-year vesting and a 1-year cliff.

On approval, the next step is Step 3, the ecosystem map.
