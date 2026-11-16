# Step 5 — Product, fit and competition
**Phase B: Why it's big and why we win · Status: LOCKED 16 Nov 2026 (content); slide choices deferred to Step 12**
**Tags:** **[Real]** = case-competition build or research · **[repo]** = team repo `ESFS/keepwell/` · **[Story]** = assumed pilot or backstory · **[Model]** = calculated.
**Plan:** [`../pitch_bible.md`](../pitch_bible.md) · **Builds on:** Steps 1–4 (locked) · **Feeds:** Step 6 (what the pilot measures), Step 10 (trust and compliance), Step 12 (solution, moat, competition and trust slides)

## 5.1 How this step is built
**Course frame (M3).** The **Product / Service** category is worth 30 of the 90 points:
- **Potential:** scalable and repeatable, a clear business model, a long-term vision
- **Uniqueness:** "Is there a real IP here? How easy or difficult is it to copy? Sticky user experience, integrations, high switching costs, lock-in"
- **Quality:** retention, engagement, NPS, consistent uptime, willingness to pay a premium

This step also answers the fit questions you set:
- problem–market fit
- problem–solution fit
- founder–market fit
- how innovative we are versus competitors
- where we sit in a competitor matrix
- Porter's Five Forces
- how hard we are to copy
- how easy we are to adopt

**Source rule.** The product is described as the repo specifies it (scenario A "Prepared Visit", features A1–A11, the R1 build order). What exists today is described from the case-competition build **[Real]** plus the pilot hardening since October **[Story]**.

## 5.2 The three fits
| Fit | Question | Our answer | Evidence |
|---|---|---|---|
| **Problem–market** | Is the problem big, frequent and felt by someone who can pay? | 15 crore repairs a year; ~₹550 Cr of wasted trips; 37,500 agencies running on a phone. The agency feels it on every job and decides fast | Step 4. Repo problem scores: P2 intake chaos 24/30, P1 unprepared visit 23/30 |
| **Problem–solution** | Does the solution remove the pain where it starts? | The pain starts at intake: the call missed, the voice note never written down, the technician sent blind. Circuit sits **at intake, inside WhatsApp, in the customer's language**, and turns the complaint into a ready job before anyone travels | Repo spec A1–A9. Case-comp demo: a Telugu voice note became a repair-ready visit **[Real]** |
| **Founder–market** | Why is this team the one to solve it? | A CEO who built and sold a technician network in these towns; a COO who ran a brand's service-partner and claims desk; a CTO who shipped the agent; a family trade crew | Step 2 |

## 5.3 What Circuit does (the demo flow)
The flow follows the repo's six-step loop, *Understand → Check → Triage → Quote → Prepare → Close out*, plus the verification step that feeds the moat.

| # | Step | What happens | Repo feature | Who decides |
|---|---|---|---|---|
| 1 | **Understand** | The customer sends a voice note or photo on WhatsApp in Hindi, Telugu, Tamil, Kannada, Marathi or English. Circuit transcribes it, extracts the complaint, and reads its own understanding back to the customer | A1 intake and language ID, A2 voice extract | AI only (T1) |
| 2 | **Check** | Reads the model, serial and invoice from photos; checks warranty against the brand's rules; pulls the machine's past repairs from its record (with consent) | A3 label and invoice reading, A4 warranty rules (code, not the model) | Rules |
| 3 | **Triage** | **Safety hard-stops first** (gas, refrigerant, high voltage), from a deterministic rule list *outside* the AI. Then **root-cause ranking**: the likely faults and the part to carry, grounded in manuals, Mistri Gyan and this machine's history. A private hint to the technician, never shown to the customer as a diagnosis | A6 safety hard-stop, A5 diagnosis | Hard-stops: human only (T3). Ranking: AI drafts |
| 4 | **Quote** | A quote is built **from the agency's own rate card by code**, never invented by the model. The owner approves it before it goes out | A7 quote | Human approves (T2) |
| 5 | **Prepare** | A job card the technician can read in ten seconds: fault, steps, part; plus the schedule | A8 brief and dispatch (R1: the operator assigns) | Human approves |
| 6 | **Close out** | The technician's voice note becomes the job record, and the machine's record is saved with consent | A9 close-out, A10 messaging | AI drafts, human confirms |
| 7 | **Verify (the moat step)** | The technician confirms what was actually wrong and what was fitted. The verified outcome goes into Mistri Gyan and the machine record. **The per-fix fee is charged only on a verified fix** | A14 "Fix verified" → `VERIFIED` | Technician |

**Product principle (repo):** *"AI reads and drafts; rules decide anything with money, safety or legal effect."* Circuit **abstains and asks when unsure**, never invents a price, and never denies a claim.

## 5.4 What is built and what comes next
| | What exists | Tag |
|---|---|---|
| **Built for the case competition (Sep–Oct 2026)** | A working agent: FastAPI, an event store, 20 allowlisted tools, a 12-state job machine, a 14-condition readiness gate, a learning step that won't run until the technician's finding is recorded, Telugu voice intake, 25 tests. Demo run CASE-A44351: 47 decisions in 10.9 minutes, reaching a repair-ready visit | **[Real]** |
| **Hardened for the pilot (Oct–Nov 2026)** | Core loop ported to Gemini on Vertex AI (Mumbai) behind a model router. WhatsApp Business channel live for 5 agencies. Agency rate cards loaded. A consent log. **Also live in beta:** root-cause ranking (A5) as a *technician-only* hint, with verified outcomes reviewed weekly by our team before they enter Mistri Gyan; quote drafts (A7) that the owner must approve | **[Story]**, consistent with the repo's R1 core loop: *A1, A2, A3, A6, A4, A9 first* |
| **Seed-funded next 18 months (R1 complete)** | The rest of R1: quote (A7), root-cause ranking at scale (A5), messaging (A10), dispatch (A8), parts status (A11). The repo's "Foundations, must precede any customer data": consent store, cost ledger, eval harness, admin console | **[repo]** build order §9.1 |
| **Then** | R2 Home Memory and plans → R3 Claims triage → R4 Parts catalogue → R5 Resale & Recycling | Step 1 roadmap |

**Honest note for Q&A.** In the case-competition demo the payment and logistics partners were simulated from their documentation. R1 keeps payments out of the product (the repo: *"Payment is stubbed in R1"*; customers pay the agency by UPI as today). This is a simplification, not a gap.

## 5.5 North Star and guardrails (from the repo, §3)
- **North Star:** **verified first-time-right jobs per active agency per month.** It counts only jobs the technician verified, so it measures real value to the agency and is the same event that triggers our fee.
- **Guardrails.** Any breach pauses rollout.

| Guardrail | Target |
|---|---|
| Safety false-accepts (a hazard the system failed to stop) | **0** |
| Unapproved price or warranty statement sent | **0** |
| AI cost per job | ≤ 3x the assumed volume (cap) |
| Accuracy gap between languages | ≤ 10 points |
| Owner override rate | 5–20% (below 5% suggests rubber-stamping) |
| Abstain rate | 10–25% (above 35% means the model is failing) |
| Quote variance by language or pincode | none unexplained |

These are proposals in the repo. **We present them as our operating rules, not as achieved results** (the repo: keep thresholds out of external claims until measured).

## 5.6 Why it is hard to copy: the moat, made concrete
**Locked in Step 1:** root-cause analysis plus a learning loop on verified repair outcomes.

**What a rival can copy in a quarter** (the repo is explicit here):
- the WhatsApp intake
- prompting an LLM
- RAG over manuals
- ranking faults and parts

Bernard (US) already gives *"a diagnosis, ranked parts and follow-up questions"*; Fieldproxy already *"searches the business's manuals and service history and returns cited answers"* **[repo]**. Servify or a recycler could "copy features within quarters" **[repo]**.

**What a rival cannot copy, because it only builds up through agencies using us:**

| Asset | Why it compounds | Repo basis |
|---|---|---|
| **Verified repair outcomes**: fault → part → did it hold, by model, town and season | Each verified fix sharpens the next ranking for the same model and fault. A newcomer starts with zero outcomes | §8.2 "fault-to-part outcomes"; A14 verify |
| **The machine record**, one append-only history per appliance, with a verification ladder: self-reported → OCR-confirmed → agency-signed → owner-approved | Rivals each hold one slice (OEM: one brand; administrator: its own plans; recycler: from collection on). We hold the whole life of the machine | `machine_event` log; ARCH §4.2 |
| **A parts-compatibility catalogue confirmed by technicians** | Slow to build, and the model is never allowed to declare a part compatible | Competitive analysis: "Yes, slow" |
| **Vernacular speech corrections** from real agency voice notes | Telugu/Tamil accuracy is the #2 risk. Every correction is training data a rival doesn't have | §8.2 |
| **Price distributions** from approved quotes | The basis for the fair-price view (R2) and plan pricing | §8.2 |
| **The agency network** | The record needs both sides: households bring the history, agencies bring the repairs. A rival needs both | One-pager |

**Switching costs that grow with use.** After a few months, an agency's rate card, its customers' machine histories and its technicians' habits all live in Circuit. Leaving means losing them. Households keep their record, because it belongs to the owner (consent-first), so we never lock households in. That is a trust point, not a weakness.

**The flywheel:** more agencies → more verified outcomes → better root-cause ranking → more first-time fixes → agencies pay and stay → more machine records → plans, claims and parts revenue → more value per agency.

## 5.7 Competition
**Who is out there.** Compiled from the repo's competitive analysis; figures are as reported there.

| Group | Players | What they do | Size / funding (repo) | Why they are not us |
|---|---|---|---|---|
| Service marketplaces | **Urban Company**; ServiceOnDoors (Tier 2/3, 200+ cities) | Book a technician on their platform | UC FY26 revenue ~₹1,555 Cr; keeps **28.3%** of professionals' earnings | They take the customer away from the agency. Metro-weighted |
| B2B after-sales for brands | **Servify** (repo's threat #1); Wiffy; 247around | Brand service networks, claims, trade-in | Servify: $133–142M raised, ~$650–800M valuation, ~₹781 Cr revenue | Serve OEMs and administrators, not the independent agency |
| Warranty administrators | OneAssist, Onsitego, Zopper | Plans and claims | OneAssist FY25 ~₹623 Cr | Hold only their own plans. Our R2/R3 **partners and buyers** |
| Field-service software | Zoho FSM; Fieldproxy; Jobber, Housecall Pro, ServiceTitan (US) | Scheduling, dispatch, quotes | Zoho ₹1,000–1,800 per user per month; ServiceTitan FY26 revenue $961M | English-first, priced per seat, need a dashboard |
| Appliance AI | **Bernard** (US), Aquant, Bruviti | AI diagnosis, ranked parts, call handling | Aquant $70M Series C | US/OEM-focused; no Indian vernacular, no WhatsApp, no independent-agency focus found |
| Indian voice AI (horizontal) | Gnani, Sarvam, Bolna, Ringg, Hunar.AI | General voice agents | Ringg $10M; Bolna $6.3M seed; Hunar ₹40 Cr | Not in appliance repair; no repair data. Could move in (threat #3) |
| Warranty wallets | TOTOKO, CheckMyWarranty, Warranti | Store bills | TOTOKO "1,000+ downloads" | Households won't do data entry. Our record fills itself from repairs |
| Recommerce, recycling | Cashify, Attero, Recykal | Resale, EPR | Cashify FY25 ~₹1,096 Cr | Start at end of life, with no repair history. Our R5 **partners** |

**Feature comparison** (✓ = yes, ◐ = partly, ✗ = no, ? = not found in the repo)

| | Vernacular voice on WhatsApp | Root-cause + part before the visit | Learns from verified outcomes | Machine record across life stages | Built for the independent agency | Keeps the agency's customer | Paid per verified fix |
|---|---|---|---|---|---|---|---|
| **Keepwell (Circuit)** | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Urban Company | ✗ | ? | ? | ✗ | ✗ | ✗ | ✗ (commission) |
| Servify | ? | ◐ (diagnostics) | ? | ◐ (its own slice) | ✗ | ◐ | ✗ |
| Zoho FSM / Fieldproxy | ✗ / ◐ | ✗ / ◐ | ✗ | ✗ | ◐ | ✓ | ✗ (per seat) |
| Bernard (US) | ✗ | ✓ | ? | ✗ | ◐ | ✓ | ? |
| Indian voice AI firms | ✓ | ✗ | ✗ | ✗ | ✗ | ✓ | ✗ |

**Two-axis map (for the slide):**
- **X axis:** who it serves, from *brand / platform* to *independent agency*.
- **Y axis:** what it holds, from *one transaction* to *the machine's whole history plus learning*.

Urban Company and ServiceOnDoors sit at platform × transaction. Servify sits at brand × partial history. Zoho, Fieldproxy and Bernard sit at agency × transaction. **Keepwell is alone in the agency × lifetime-history corner.** The repo confirms this as an "absence of evidence, not proof": no rival with a unit-level record from warranty to EPR was found.

**Proof the category can be big.** In the US, **Avoca** (AI call handling for home-service businesses) is valued at ~$1B, and **ServiceTitan** (trade-business software) makes $961M a year **[repo / Real]**. India has no equivalent for its informal agencies. This feeds the valuation story in Step 9.

## 5.8 Porter's Five Forces (software and AI for independent repair agencies in India)
| Force | Rating | Why | Our response |
|---|---|---|---|
| **Rivalry** | Low today, rising | No vernacular agency desk was found; Fieldproxy and the voice-AI firms could move in | Move first in Tier 2/3. Build outcome data before they arrive |
| **New entrants** | Medium–high | An LLM wrapper is cheap to build | The moat is verified outcomes and records, not the model (5.6) |
| **Buyer power** (agencies) | Medium | Fragmented, so each agency has little leverage. But willingness to pay is low and early churn is easy | Charge only on a verified fix (no seat fee), 30 free days, value visible on every job |
| **Supplier power** | Medium–high | **Meta** owns the only channel (WhatsApp pricing changes; INR billing from 1 Jan 2026). **Google** prices: Flash doubles on 1 Jan 2027 | Model router with vendor fallback ("one SDK wrapper"); budget at 2027 prices; route bulk calls to Flash-Lite (stable price); credits cover 2 years |
| **Substitutes** | High | A phone, a notebook and WhatsApp are free; Urban Company leads; brand call centres | **We run inside WhatsApp**, so it's the same phone and the same number with no new app. The substitute becomes our channel |

**Reading.** The attractive profit pool is in the *data and the record*, not in the AI call. That is why Circuit is priced to win adoption, and the money is made on the platform (Step 4: Circuit is the wedge, the record is the business).

## 5.9 How easy it is to adopt
- **No new app.** Customers message the agency's existing WhatsApp number. The repo: "WhatsApp and phone only; no dashboard on day one".
- **Works on a shared, low-end Android** used by technicians (repo persona). Light flows, small uploads, tolerant of poor connectivity.
- **Set-up in one visit:** the agency's rate card and its WhatsApp number. The first jobs flow the same day [Story; Step 6 measures time to first job].
- **No upfront cost:** 30 free days, then payment only on a verified fix.
- **Owner stays in control:** every quote and every warranty decision needs owner approval.

## 5.10 Product quality: how we prove it
**Release gates** (repo proposals, used as our gates):

| Feature | Gate |
|---|---|
| Language and intent (A1) | ≥ 95% |
| Critical fields from labels and invoices (A3) | ≥ 97%, hallucination < 1% |
| Root-cause top-3 hit (A5) | 75%, citation validity 100% |
| Safety hard-stop recall (A6) | ≥ 99.5% (100% on the highest hazards), false stops ≤ 8% |
| Quote line agreement (A7) | ≥ 85% |
| Close-out fields (A9) | ≥ 95%, in under 60 seconds |

How the gates are run:
- **Eval method:** 100–200 golden cases per feature; an LLM judge calibrated against humans (kappa ≥ 0.7); zero tolerance on safety false-accepts. The golden audio and lexicons come from the IIIT-H speech lab (Step 3).
- **Measured results** come from the pilot (Step 6). The deck shows them as before/after, as the repo suggests ("before/after eval results shown live in the demo").

## 5.11 Weak points, said before an investor says them
| Risk (repo §11.1) | Our answer |
|---|---|
| Agencies won't pay per fix, because fewer revisits cut their own second-visit fee | Lead with answered calls, agreed prices and owner control. The paid pilot tests ₹40 vs ₹100 (Step 6). The kill condition is in Step 6 |
| Telugu/Tamil speech accuracy | IIIT-H lab golden sets; per-language gate (≤ 10-point gap); abstain and ask when unsure |
| Invented fields (the model fabricates an invoice number) | A null option plus a validator on every field; the owner confirms |
| Unsafe guidance | A deterministic hard-stop layer outside the LLM; a lexicon signed off by an external safety expert |
| Price shock on 1 Jan 2027 | Budget at 2027 prices; Flash-Lite for bulk calls; credits |
| A competitor copies the features | They can copy features, but not the verified outcomes or records (5.6) |
| Cold start: no outcome data on day one | The founders' network and the pilot agencies seed it; manuals and warranty terms (top 10 brands × 7 appliances) give a day-one baseline |

## 5.12 How it shows up in the pitch
1. **Solution slide:** the 7-step flow as one visual (voice note → job card → verified fix), plus a 20-second demo clip from the real prototype.
2. **"Why it compounds" slide:** the flywheel (5.6) and the line *"Anyone can copy the AI. No one can copy 10,000 verified repairs."* (The number on the slide comes from the Step 6/7 plan at the Series A gate.)
3. **Competition slide:** the two-axis map with Keepwell alone in the corner, plus a 5-row feature table.
4. **Trust slide** (shared with Step 10): the principle line, the three decision tiers, the hard-stops and zero-tolerance guardrails.
5. **Appendix:** Porter's Five Forces, the release gates, the risk table.

These cover the M3 Product cells:
- **Potential:** an asset-light, repeatable loop; six products on one record.
- **Uniqueness:** the outcome data moat, switching costs, no rival in our corner.
- **Quality:** guardrails, release gates, and the pilot results from Step 6.

---

## Decisions log (LOCKED 16 Nov 2026)
- **Content locked:** fits, the 7-step flow, built vs next, North Star and guardrails, the moat assets, the competitor map, Porter's Five Forces, adoption, release gates, weak points.
- **Which slides to use** (flow visual, moat line, competition visual, how guardrails are shown) is **decided in Step 12**, based on the best story.
