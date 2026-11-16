# KeepWell pitch deck V3: change log

**Date:** 15 Nov 2026
**Files:** `KeepWell_Pitch_Deck_V3.pptx` (editable), `KeepWell_Pitch_Deck_V3.pdf` (9 pages, 1.1 MB, under the 5 MB limit), built by `spec_parts/build_deck_v3.py` from the official template artwork in `spec_parts/v3_assets/`.
**Spec followed:** `KeepWell_V2_Audit_and_V3_Enhancement_Brief.md`.

## How V3 was built

- **Template.** The official template is only a PDF, so V3 is a new editable PPTX rebuilt on it. The template's cover banner, logo header strip and Thank-you page are rendered from the official PDF as images, so branding is exactly preserved. All KeepWell content (titles, text, diagrams, tables) is editable. Slide order matches the template: cover → Problem Statement → Proposed Solution → Solution Architecture → Google AI Tools → Google AI Models → free slide(s) → Thank you. The template's own "Submission Guidelines" instruction page is left out, as in V1/V2. As in V2, the single free slide is used twice (Business, Evaluation); see Unresolved Decisions #6.
- **Typography.** The template uses Google Sans Flex, which is not installed here; V3 uses Arial for portability. Minimum body text is about 7.5 pt (V2 went down to 7 pt in dense tables); key messages are 9–10.5 pt.
- **Export.** PDF exported from the PPTX with LibreOffice and every page rendered and inspected. No clipping found on the final pass.
- **Inputs not available.** `Keepwell_AI_Product_Blueprint.md` was not provided and is not on this machine. The repo's own spec and architecture docs (`spec_parts/`, `Keepwell product architecture and scenario IO.md`, `Keepwell Google stack mapping.md`) were used instead.

## Fresh source checks (15 Nov 2026)

| Claim area | What was checked | Result used in V3 |
|---|---|---|
| LocalCircles defective products | Primary page, 15 Mar 2024 (32,000+ responses, 311 districts) | 55% of households reported at least one high-value product bought in the last 5 years was defective within warranty; n=10,641. V2's "2022, 28,000+ responses" attribution was wrong (that is a different 2022 survey). |
| LocalCircles "21% got refund/replacement" | Same page | Denominator is unclear on the page (arithmetic implies 21% of all 10,740 respondents, not 21% of those who sought action). **Removed from the deck.** |
| LocalCircles AC servicing | Primary page, 16 Apr 2026 (27,000+ responses) | Question covered servicing done *or planned* this year (n=13,487): 24% brand, 57% local or organised third party. V2's "3 in 4 did not use brand service" replaced with these exact figures. |
| Tier 3 durables 10% vs Tier 1 7% | Only an IANS wire story (12 Mar 2025) citing NIQ/GfK; primary report not found | **Removed** (single secondary source, category is all tech & durables). |
| Gemini 3.8 Flash regions | Official Agent Platform model page | Standard PayGo: global, us, eu only. Provisioned throughput: adds Montreal, Tokyo. **Not Mumbai.** |
| Gemini 3.5 Flash / Flash-Lite regions | Official model pages | Standard PayGo global/us/eu; asia-south1 offered for provisioned throughput (Flash-Lite also lists asia-south1 data processing). |
| Gemini 3.5 Transcribe | Official AI Studio + Agent Platform pages | Hindi, Telugu, Kannada, Marathi listed; **Tamil not listed**; custom vocabulary up to 1,000 phrases; $0.003/min audio in (Gemini API); Agent Platform endpoints global/us/eu. |
| Gemini Embedding 2 | Official page; Vertex region from a search summary | Multimodal (text, image, audio, video, PDF), $0.20/1M text tokens; Vertex endpoints reported global/us/eu only. |
| Document AI | Official processor list | Enterprise OCR reads Telugu, Hindi, Tamil, Kannada, Marathi and runs in asia-south1; Invoice Parser has no Indian languages; Custom Extractor generative mode not in Mumbai. |
| Chirp 3 STT | Official page | hi-IN GA; te/ta/kn/mr-IN Preview; us/eu only. |
| Model Armor | Official overview + locations | Prompt-injection, jailbreak, sensitive-data screening; asia-south1 supported (some features limited). |
| Gemini 3.8 Live | Official Live API pages | GA; audio-only sessions about 15 min without compression. |
| ADK evaluation | adk.dev criteria page | `tool_trajectory_avg_score` (EXACT / IN_ORDER / ANY_ORDER), rubric-based checks, `hallucinations_v1`, `safety_v1`. |
| Google Agent Skills | github.com/google/skills | Official Apache-2.0 repo of developer skills for Google Cloud, Gemini API, Agent Platform, Cloud SQL etc.; installable in Antigravity CLI. |
| Maps India pricing | Official India price list | Routes Essentials 70k free then $1.50/1k; Route Optimization single vehicle $0.80, fleet $2.40 per shipment (free caps 35k / 7k). |
| Competition | startupbuildathon.com | Judging: founder profile, product potential, market viability, technical architecture, use of Google AI/Cloud. City Buildathons 20–21 Nov (two days). Slide count / extra-slide rules not published on the site. |

## Slide-by-slide changes

### Slide 1: Cover
| V2 text | Defect | V3 text | Why |
|---|---|---|---|
| Team Name: KeepWell | No product identity | KeepWell \| The AI repair desk and Home Memory for every appliance | Brief: memorable identity on the cover |
| Team Size: 2 | One-pager names three people | 2 (kept) | The user confirmed the team is two; names stay off the deck |
| "...first visits fail, quotes get disputed..." | Implies all first visits fail | "...can arrive underprepared. That raises the risk of avoidable repeat visits, makes quotes harder to explain, and leaves households without a trustworthy service record." | Removes overclaim; keeps the specific customer and channel |

### Slide 2: Problem Statement
| V2 text | Defect | V3 text | Why |
|---|---|---|---|
| "Root cause: no structured record ... exists anywhere" | Absolute claim | "Repair context is scattered across customer messages, paper invoices, technicians' memory and past visits..." | Brief wording; defensible |
| Three stakeholder cards (agencies, households, OEMs) | Not a causal story | Causal chain: Fragmented complaint → Weak preparation → Repeat visits, low trust | Brief section 2, slide 2 redesign |
| 55% / 21% / 3 in 4 stats, "2022, 28,000+ responses" | Wrong year/sample; 21% denominator unclear; AC stat paraphrased | Two stats with exact sources: 57% local/third-party vs 24% brand AC servicing (Apr 2026, n=13,487); 55% defective-in-warranty (Mar 2024, n=10,641) | Verified on primary pages; 21% dropped |
| "Why Tier 2/3: durables grew 10% vs 7%... agencies carry the load with WhatsApp and no software" | Secondary stat; overgeneralisation | Removed. New "What the evidence does and doesn't show" card naming the pilot's first measurements | Honest evidence gap (brief) |
| — | ICP unclear | "Who we serve first: owner-run independent agencies, 2–10 technicians, Tier 2/3; households second" | Brief |

### Slide 3: Proposed Solution
| V2 text | Defect | V3 text | Why |
|---|---|---|---|
| Six abstract steps (Understand... Close out) | No real journey | Flagship scenario (labelled illustrative): Telugu customer, fridge not cooling again after a repair two months ago; six steps Listen → Identify → Ask + safety → Prepare → Approve → Remember | Brief flagship demo |
| — | Demo realism not shown | Each step tagged: "Real AI/API call in demo", "Real logic, fixture data", "Payment sandbox" | Brief: label live vs simulated |
| "right part on the first visit" | Guarantee | "Catalogue-verified part, or an explicit inspect-first visit" | Brief |
| "Technician's voice note becomes the job card" | Job card should exist before the visit | Close-out becomes a "verified service event" (technician findings + customer confirmation) | Brief |
| "Goal: verified first-time-right jobs per active agency per month" | Rises with volume alone | North-star: first-visit resolution rate, 14-day reopen window, eligible-jobs denominator, tracked with volume, diagnostic-only, 30-day repeats, agency baseline | Brief definition |
| Rules card, roadmap card | Moved | Rules moved to Architecture; roadmap to Business/Validation | Focus |
| — | Scope missing | "MVP scope: refrigerators and ACs, Telugu + Hindi, one Tier 2 city" | Narrow, achievable first product (founder to confirm, Unresolved #4) |
| — | Before/after missing | Five-row Today vs With KeepWell table | Brief |

### Slide 4: Solution Architecture (rebuilt)
| V2 | Defect | V3 | Why |
|---|---|---|---|
| Columns of technologies (Gemini, rules, retrieval, Maps, SQL...) | No decision path; agents and services conflated | Five lanes: Channels → Orchestration (state machine, event log, idempotent signed webhooks, cost cap; untrusted-input guard; human approval gates) → AI agents → Verified tools + rules → Record, Home Memory, Eval loop. Colour legend separates LLM, deterministic/API, human/safety, record | Brief section 3 |
| "Gemini Flash / Flash-Lite" as one box | Not agentic, no responsibilities | Five bounded AI components: Intake agent, Appliance identity (OCR/vision + exact SQL match), Diagnostic agent (cited or abstain), Preparation agent, Repair memory agent (repeat-failure check) | Brief component table |
| — | Missing controls | Safety rules, consent + permissions, warranty + price policy, parts catalogue (verified/unknown/incompatible), dispatch (Routes + Route Optimization), UPI gateway (signed webhook, sandbox) | Brief tool contracts |
| "Hosted in Mumbai (asia-south1)" | Implied Gemini runs in India | "App, database and files in Mumbai. No Gemini model is offered on standard pay-as-you-go in Mumbai today, so the pilot calls Gemini's global endpoint with customer consent; in-India inference would need 3.5 Flash / Flash-Lite provisioned throughput" | Verified on official model pages |
| "WhatsApp Cloud API is the only non-Google component" | False | "Outside Google: WhatsApp Cloud API, UPI payment gateway, parts suppliers" | Brief |
| — | Prompt injection, vector-as-truth | Model Armor + rules on untrusted input; "vector index is never the source of truth for exact facts; no part is called compatible unless the catalogue says so" | Brief |
| A2A mentioned in V1 notes | Not needed | Not shown | Brief |

### Slide 5: Google AI Tools (replaced)
| V2 | Defect | V3 | Why |
|---|---|---|---|
| Three bullet lists of planned uses | Feature list; confused Google's developer skills with KeepWell runtime skills | Three cards, each Task → Deliverable → Proof. AI Studio: design and evaluate. Antigravity: build and test. Agent Skills: Google's published developer skills (github.com/google/skills) plus separate KeepWell domain skills, stated as build-time guidance, not runtime agents | Brief section 4 |
| "48-hour"/"two-day" build, "spec and eval cases drafted" | — | "All three are planned for the build; none has produced results yet." | No implied results |
| "Also in the stack" strip | — | Runtime strip (ADK on Cloud Run, Gemini, Cloud SQL/Storage, Document AI, Maps, authenticated adapters) + "Measured with" | Brief |

### Slide 6: Google AI Models (replaced)
| V2 | Defect | V3 | Why |
|---|---|---|---|
| Seven-row SKU table | Name-dropping; no evaluation | Five capability bands (Listen, Understand, Read, Reason, Remember), each with candidate, job, what it's evaluated on, fallback | Brief section 5 |
| Generic "Gemini audio; Chirp 3" | Missed specialised model | Gemini 3.5 Transcribe (Telugu, Hindi supported; custom vocabulary); fallback Flash-Lite audio | Verified |
| No Document AI comparison | Brief | "Document AI Enterprise OCR vs Gemini vision" (OCR reads Telugu/Hindi, runs in Mumbai) | Verified |
| "strongest reasoning per rupee", "cuts AI cost about half", "10x cheaper than Chirp" | Unmeasured | Removed; "each is a candidate to benchmark, not a guaranteed winner"; selection rule card | Brief |
| Gemini 3.5 Flash (India) row, Gemini 4 Hydrogen footnote | Region overclaim; future-model name-drop | Removed; region handled precisely on Slide 4 | Brief |
| Gemini 3.8 Live "preview" | Outdated | "Gemini 3.8 Live (GA; audio sessions about 15 min)" in a "Later, only if pilot shows demand" line | Verified |
| — | Brief: where rules/ML beat LLMs | "No LLM for these decisions" card (price/GST, consent, payment confirmation, part compatibility, slots, state changes) + "Classical ML, not LLMs: parts-demand forecasts, technician ranking, repeat-failure anomaly detection" | Brief section 6 |
| Cost footnote (₹1.5–5.5, ₹10 in 2027) | Mixed scenarios | Moved to Business slide as explicit scenarios | Brief |

### Slide 7: Business Model and Market (repriced as B2B, 15 Nov, second review)
**Why it changed.** At ₹1,500 per agency per month (plus ₹40 per fix) a typical agency was worth only about ₹4,500 a month, too little to build a company on. Comparable tools price per user or per technician, and the larger B2B money sits with service-centre networks, brands and plan providers.

**Market benchmarks used (vendor and comparison sites, Nov 2026; directional, many are quote-based):**
- Indian WhatsApp AI / customer-messaging tools: about ₹1,000–17,000 a month (AiSensy AI agent add-on about ₹1,350; Interakt AI agents from about ₹2,499; Gallabox ₹2,999–16,999).
- US field-service software: Jobber $29–349 a month; Housecall Pro $59–329; ServiceTitan about $245–500 per technician per month (reported, not published); Zuper about $65–105 per user per month.
- US AI call answering for home services: Sameday from about $449 a month; Avoca about $1,000–5,000+ (estimates).
- Cost of one service visit to an Indian service business: about ₹350–500 (a practitioner's LinkedIn estimate; anecdotal). Technician salaries in job listings: about ₹14,000–35,000 a month.

| Before | Problem | Now | Why |
|---|---|---|---|
| ₹1,500 per agency per month + ₹40 per verified fix; small-agency option ₹100 per fix | Revenue per agency too small; didn't scale with agency size | **Starter ₹1,499 per technician per month** (60 AI-handled jobs per technician, then ₹10 a job); **Pro ₹2,499 per technician per month** for service centres; **Enterprise** annual contracts for brands and plan providers (₹30–100 per claim, ₹100–250 per routed job); first 60 days free | Per-technician pricing matches the market and grows with the customer; the job cap protects margin |
| "Who pays: agencies; households free" | Single customer type | Four payers: owner-run agencies (pilot), service centres and brand-authorised networks, brands and plan providers (Phase 3), households free | Shows where larger contracts come from |
| — | No price justification | "What the market pays" card with the benchmarks above | Anchors the price |
| "What one agency is worth" (₹4,500 a month) | — | "One technician on Starter": ₹1,499 in, ₹90–600 running cost (≤60 jobs × ₹1.50–₹10), ₹900–1,410 left; pays for itself if it avoids 3–4 wasted visits a month (₹1,499 ÷ ₹350–500) | Clear value and margin per seat |
| — | No growth story | "How it grows (targets, not forecasts)": 300 agencies × 5 technicians on Starter ≈ ₹2.7 Cr a year (300×5×1,499×12); 40 service centres × 20 technicians on Pro ≈ ₹2.4 Cr (40×20×2,499×12); one plan provider at 10,000 claims a month × ₹30–100 ≈ ₹36 lakh–1.2 Cr a year | Shows a path beyond small agencies |
| Pilot tests | — | Agencies keep paying ₹1,499 per technician after 60 days; usage fits 60 jobs per technician; first-visit resolution beats baseline; one service centre or brand agrees to pilot Pro or Enterprise | Ties price to evidence |
| Competition / moat / later revenue cards | — | Competition and key risk moved to a two-line footer with a benchmark-source note | Space for pricing |

Slide 8's validation line now reads "paid pilot at ₹1,499 per technician".

### Slide 8: Trust, Evaluation and Validation
| V2 | Defect | V3 | Why |
|---|---|---|---|
| Golden datasets, three layers, "block on any drop in accuracy" | No example; unusable gate | One gold case end to end (input, expected, bad output, failure, fix, result = "to be measured") | Brief 7.6 |
| — | No dataset plan | 100 adjudicated cases with category split, ≥20 code-switched, ≥20 adversarial, untouched holdout, synthetic first | Brief 7.2 |
| Generic layers | — | Assertions; anchored 0–4 human-reviewed rubrics (five dimensions); trajectory + outcome with ADK `tool_trajectory_avg_score` (IN_ORDER) | Brief 7.3; verified ADK metric |
| — | No gates | Provisional release gates table (≥99% schema, 100% hazard recall, 0 invented compatible parts, ≥95% critical-field precision, ≥98% grounded claims, ≥95% next state, ≥85% rubric ≥3/4), labelled "not yet tested" | Brief 7.4 |
| "Built for DPDP Act 2023 and Rules 2025" | Compliance claim | Removed from this slide; consent/permissions shown as architecture controls | Brief |
| "Complaint help is an evidence pack" | Off-focus | Removed | Brief |
| "Months 6–12: 5–10 cities" | Aspiration as plan | "decide on more cities from pilot data" | Brief |
| — | Learning loop missing | Learning loop line | Brief 7.7 |
| — | Evidence status | "Today: spec, eval design and synthetic cases. No pilot, accuracy or cost results yet." | No fabricated results |

### Slide 9: Thank you
Unchanged official template page.

## Brief items deliberately not on slides
- Full tool-contract table (brief section 3): reflected as architecture nodes; contracts belong in the build spec.
- Full anchored rubric table (7.5): summarised as five dimensions; full rubric belongs in the eval artifact.
- Market-size figures from the one-pager (₹9,000–10,000 Cr repair, ₹37,000 Cr extended warranty, "over 90% grey market"): not verified, so left out.
