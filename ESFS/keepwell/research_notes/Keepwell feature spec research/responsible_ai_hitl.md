# Responsible AI and Human-in-the-Loop (HITL) for Keepwell (India appliance repair/warranty AI)

Tag legend: 🟢 sourced from an official or primary page (as surfaced by search); 🟡 secondary (law-firm/trade commentary, vendor, blog); 🔴 inference or my own background knowledge, not verified in this research. Research was search-snippet based (about 16 calls); primary PDFs (Gazette, MeitY guidelines, CCPA annexure) were NOT opened, so every legal item needs lawyer verification against the official text.

## 1. India legal and governance (DPDP Act/Rules, AI Governance Guidelines, Consumer Protection, voice consent)

### Takeaway
DPDP Rules were notified 14 Nov 2025 with a staggered rollout (core fiduciary duties about 18 months later, around 13 May 2027), so Keepwell should design to them now. The agency is most likely the data fiduciary and Keepwell a processor, but this must be decided and papered by a lawyer. India's AI guidelines are voluntary principles, not law; the binding duties for AI quotes and claims come from DPDP, Consumer Protection Act 2019 and the dark-pattern guidelines.

### Cited Findings
- 🟡 DPDP Rules 2025 notified 14 Nov 2025 (a PIB release dated 17 Nov confirms notification on 14 Nov; some firms say 13 Nov, likely gazette vs announcement) — [PIB doc](https://static.pib.gov.in/WriteReadData/specificdocs/documents/2025/nov/doc20251117695301.pdf); [Storyboard18](https://www.storyboard18.com/amp/digital/breaking-govt-notifies-final-dpdp-rules-sets-staggered-rollout-with-key-obligations-for-data-fiduciaries-84201.htm)
- 🟡 Phasing: governance provisions (Board) immediate; Consent Manager obligations after 12 months; main fiduciary obligations (notice, consent, breach, retention, children) after 18 months, cited as 13 May 2027 — [India Briefing](https://www.india-briefing.com/news/dpdp-rules-2025-india-data-protection-law-compliance-40769.html); [Ogma](https://ogma.in/blog/dpdpa-technical-implementation-playbook-13-month-roadmap-to-may-2027)
- 🟡 Notice must state purposes, categories of data, retention, and how to withdraw consent — [Biometric Update](https://www.biometricupdate.com/202511/india-notifies-its-sweeping-digital-personal-data-protection-rules)
- 🟡 Breach: intimate the Board and affected persons without delay, then a detailed report to the Board within 72 hours (sources vary on exact wording) — [Mondaq](https://www.mondaq.com/india/data-protection/1708164/digital-personal-data-protection-rules-2025-notified); [KSK Rule 6](https://ksandk.com/data-protection-and-data-privacy/dpdp-rule-6-and-indias-new-cybersecurity-compliance-standard/)
- 🟡 Rule 6 security baseline: encryption/obfuscation, access control, monitoring, backups, processor contracts with equivalent safeguards; logs and related data retained one year unless other law requires longer — [KSK](https://ksandk.com/data-protection-and-data-privacy/dpdp-rule-6-and-indias-new-cybersecurity-compliance-standard/); [SFLC](https://sflc.in/?p=13285)
- 🟡 Erasure: after specified period/inactivity (Third Schedule applies to certain large classes), with 48 hours advance notice to the data principal; Keepwell is probably not in those classes, but the general rule is purpose-limited retention — [Seclore guide](https://www.seclore.com/fundamentals/dpdp-rules-2025-compliance-guide/); [SFLC](https://sflc.in/?p=13285)
- 🟡 Cross-border (Rule 15): transfers allowed subject to conditions the Central Government may specify, possibly by country/entity — [DSCI brief](https://www.dsci.in/files/content/knowledge-centre/2025/Insight-Brief-on-DPDP-Rules.pdf)
- 🟡 Act s.8: processor only under a valid contract; fiduciary remains responsible for compliance even when a processor processes (s.8(1)) — [dpdpa.com s.8](https://dpdpa.com/dpdpa2023/chapter-2/section8.html); [EY](https://www.ey.com/en_in/insights/technology/how-data-fiduciaries-should-engage-processors-for-effective-compliance)
- 🟡 Children: anyone under 18 (s.2(f)); verifiable parental consent (s.9(1)); no tracking, behavioural monitoring or targeted ads at children (s.9(3)); Rules give class exemptions (healthcare, education, crèches) not obviously covering a repair agency — [consent.in](https://www.consent.in/blog/child-consent); [AM Legals](https://amlegals.com/processing-of-childrens-data/)
- 🟡 Legitimate uses are in s.7 (not s.4, which is grounds); s.7 could cover voluntarily provided data for the specified purpose — [dpdpa.com ch.2](https://dpdpa.com/dpdpa2023/chapter-2/chapter2.html)
- 🟡 India AI Governance Guidelines released by MeitY 5 Nov 2025; seven "sutras" (Trust; People First; Innovation over Restraint; Fairness and Equity; Accountability; Understandable by Design; Safety, Resilience and Sustainability); four parts (principles, six pillars, action plan, implementation guidance); voluntary, no umbrella AI law planned now; labels vary by outlet, so quote from the official PDF — [Tribune](https://www.tribuneindia.com/news/business/meity-unveils-india-ai-governance-guidelines-to-ensure-safe-inclusive-and-responsible-ai-adoption); [IPRMentLaw copy of PDF](https://iprmentlaw.com/wp-content/uploads/2025/11/India_AI_Governance_Guidelines__1762344347.pdf); [SCC Online](https://www.scconline.com/blog/?p=365854)
- 🟡 Dark Patterns Guidelines 2023 issued 30 Nov 2023 under s.18 CPA 2019 by CCPA; 13 listed patterns incl. drip pricing, bait and switch, false urgency, basket sneaking, forced disclosure, nagging, subscription trap, disguised ads; indicative list; apply to platforms, advertisers, sellers — [Mondaq](https://www.mondaq.com/india/consumer-trading-unfair-trading/1398262/ccpa-issues-guidelines-for-prevention-and-regulation-of-dark-patterns-2023-effective-30-november-2023); [JSA](https://jsalaw.com/?p=49613)

### Inferences
- 🔴 Role split: agency decides why/what (customers' data for its service, warranty claims) = fiduciary; Keepwell processes on instructions = processor, bound by a DPA. If Keepwell also uses data for its own purposes (model improvement, benchmarking, selling insights) it becomes a fiduciary for that purpose. Households interacting directly with a Keepwell app may make Keepwell fiduciary. Lawyer to confirm.
- 🔴 Practical design: consent/notice text surfaced by the agency (or Keepwell on its behalf) in the customer's language; a withdrawal path; per-job retention schedule; breach runbook with 72-hour clock; no use of customer data to train models by default; do not process minors' data knowingly (flag if the claimant/user is under 18, e.g. household with a child account).
- 🔴 AI quotes: dark-pattern risk areas are drip pricing (quote excludes parts/GST then adds), bait and switch (low AI estimate, higher final bill), false urgency ("book now, price expires"), basket sneaking (auto-added add-ons). Show an itemised all-in range, label as estimate, and have a human confirm before sending binding quotes. CPA "unfair trade practice" and "deficiency in service" exposure on misleading quotes or wrongful claim repudiation: needs a lawyer; not researched here.
- 🔴 Voice notes: DPDP treats recording a voice as personal data, so notice plus consent applies (voice may be biometric-adjacent; DPDP has no separate sensitive category). Telegraph/Indian Wiretap law concerns relate to interception of third-party calls, not a user's own voice note; but if notes capture a technician and customer conversation, both should be told. 🔴 Needs lawyer.
- 🔴 E-commerce Rules and Legal Metrology: only relevant if Keepwell sells parts or is a marketplace; not researched and likely out of scope for a first release.

### Gaps
- Official DPDP Rules text/Gazette not opened; exact rule numbers (6, 7, 8, 15) conflict across sources; breach-timing wording varies.
- Section 8 fiduciary/processor liability text only via secondary sources; no authority on how India will treat AI vendors as processors.
- Full numbered list of 13 dark patterns and CPA 2019 sections (unfair trade practice, product/service liability, e-filing of complaints) not retrieved.
- No source found on Indian law specifically governing voice-recording consent in a service app; pure inference above.
- Cross-border conditions (negative-list vs conditions) not yet specified in what I found.

## 2. HITL design patterns for claims and quoting AI

### Takeaway
Regulatory direction (EU AI Act, NAIC, IRDAI working group) is: AI may recommend and triage, but adverse or binding decisions and anything safety-critical need a trained human who has real power to override, plus logging and override metrics. Evidence says nominal human review degrades into rubber-stamping, so measure it.

### Cited Findings
- 🟡 EU AI Act Annex III lists AI for risk assessment and pricing in life and health insurance as high-risk (point 5(c), numbering varies across commentary); P&C pricing/underwriting is not listed; Art. 6(3) exception narrow; timing of obligations in flux (one source cites a postponement to Dec 2027; verify) — [Knowlee](https://www.knowlee.ai/blog/ai-act-financial-services-compliance); [actuary.info](https://actuary.info/insights/eu-ai-act-august-2026-carrier-high-risk-compliance-gaps)
- 🟡 EU AI Act Art. 14 requires oversight enabling humans to understand limits, interpret output and stay aware of automation bias — [arXiv 2502.10036](https://arxiv.org/pdf/2502.10036)
- 🟡 NAIC Model Bulletin on AI Systems used by Insurers adopted 4 Dec 2023: board-approved written AI program, governance, risk controls, internal audit, third-party vendor oversight; non-binding but adopted by 25 states plus DC per a March 2026 source — [NAIC PDF](https://content.naic.org/sites/default/files/2023-12-4%252520Model%252520Bulletin_Adopted_0.pdf); [Lumenova](https://www.lumenova.ai/blog/naic-ai-model-bulletin-insurers-guide/); [Quarles](https://www.quarles.com/newsroom/publications/states-adopt-naic-model-bulletin-on-insurers-use-of-ai)
- 🟡 IRDAI: no AI-specific rulebook found; formed an AI working group (chair Prof. Sandeep K. Shukla) to propose a framework for explainable AI in claims and fraud; IRDAI 2025 fraud monitoring framework commentary stresses human vigilance at claim — [Insurance Business](https://www.insurancebusinessmag.com/asia/news/technology/indias-insurance-regulator-steps-in-to-govern-ai-adoption-579846.aspx); [indialaw.in](https://www.indialaw.in/blog/sarfaesi/irdai-2025-guidelines-zero-tolerance-insurance-fraud/)
- 🟡 Rubber-stamp evidence (unverified against primary papers): physicians reportedly signed denials at about 1.2 seconds each (Cigna PxDx, over 300,000 denials in two months); a 2023 Radiology study where AI errors cut inexperienced radiologists' accuracy from about 80% to under 20%; HBS 2024 study of reviewers aligning 19 points more with AI; NAIC-linked suggestion to track human override statistics — [tianpan.co](https://tianpan.co/blog/2026/04/15/human-in-the-loop-rubber-stamp); [Insurance Thought Leadership](https://www.insurancethoughtleadership.com/ai-machine-learning/why-human-audits-ai-decisions-fail); [Economy for Everyone](https://economyforeveryone.pages.dev/case-studies/claims-eligibility/)
- 🟡 Vendor survey (Wisedocs/PC360 2025, biased sponsor): trust rises about 4x with expert human oversight — [Wisedocs](https://www.wisedocs.ai/reports/2025-ai-in-claims-survey)
- 🟡 Some US states (CA, CT, IL, RI) considering bans on claims adjudication without human oversight — [InsuranceNewsNet](https://insurancenewsnet.com/oarticle/where-the-human-ai-workflow-in-health-care-breaks-down)

### Inferences
- 🔴 Appliance warranty/repair is not insurance regulated by IRDAI unless the warranty is an insurance product (extended warranty sold as insurance is). Lawyer to check whether any Keepwell flow touches IRDAI-regulated products. Use the EU/NAIC/IRDAI items as analogues, not obligations. EU Annex III is not triggered by repair quoting.
- 🔴 Recommended decision tiers: (A) AI-only allowed, no human gate: transcription, summarisation, extracting fields from invoices/photos, drafting evidence-pack structure. (B) Human must approve before it leaves the system or binds anyone: any price quote sent to a household, any claim "eligible/ineligible/likely rejected" label shown to a customer or manufacturer, any fraud or document-tampering flag, any statement about warranty validity. (C) Human only, AI silent or refuse-and-escalate: safety hard-stops (section 5), legal opinions, denial communications, anything involving a minor or dispute.
- 🔴 Confidence thresholds: no published benchmark for this domain; treat numbers as to-be-calibrated. Suggest: low-confidence extraction (OCR field, ASR segment, model-assessed uncertainty, missing evidence) routes to a human; a "never auto-approve adverse outcome" rule rather than a threshold; calibrate thresholds on a labelled set of at least a few hundred jobs per language and recheck monthly.
- 🔴 Automation-bias mitigations: show evidence before the AI recommendation; require the reviewer to enter their own estimate or reason for approvals; randomly seeded known-wrong cases to test reviewer attention; track approval time, override rate, and agreement rate per reviewer; alert when override rate approaches 0 or review time under a few seconds; do not default the accept button.
- 🔴 Audit trail and appeal: store input hashes, model version, prompt version, output, confidence, reviewer id, decision, time, reason code; customer-facing "ask a person to review" for any flagged claim or quote; override reasons feed an error taxonomy.

### Gaps
- No peer-reviewed field-service AI (appliance repair) HITL study found; no concrete deployments in Indian appliance warranty found.
- Primary sources for the rubber-stamp statistics not checked; Cigna/Health Affairs attributions unverified.
- NAIC text on human override tracking not confirmed in bulletin; IRDAI working-group output not yet published in what I found.
- EU AI Act application dates for Annex III are conflicting across sources.

## 3. Fairness and language (Indic ASR)

### Takeaway
Indic ASR error rates vary a lot by language and speech style, with Hindi best and Dravidian languages worse in the best open Vistaar results; spontaneous, accented, noisy and code-mixed speech is harder than read speech. Keepwell should treat ASR text as a draft the user or agent confirms, and test per language and accent.

### Cited Findings
- 🟢 Vistaar (Bhogale et al., Interspeech 2023): 59 benchmarks across languages/domains; fine-tuned IndicWhisper had lowest WER on 39 of 59 and 4.1 WER average gain over others — [arXiv 2305.15386](https://ar5iv.labs.arxiv.org/html/2305.15386); [AI4Bharat Vistaar GitHub](https://github.com/AI4Bharat/vistaar)
- 🟡 Per-language IndicWhisper averages read from the README (row alignment uncertain, verify): Hindi about 13.6, Kannada about 18.3, Marathi about 18.2, Tamil about 25.3, Telugu about 28.8 WER — [Vistaar GitHub](https://github.com/AI4Bharat/vistaar)
- 🟢 Adding Shrutilipi data cut Hindi average WER from 18.8 to 13.5 on Vistaar Hindi benchmarks (shows data-dependence) — [Vistaar GitHub](https://github.com/AI4Bharat/vistaar)
- 🟢 IndicVoices (ACL Findings 2024): 7,348 hours, 16,237 speakers, 145 districts, 22 languages; mix 9% read, 74% extempore, 17% conversational; includes noisy recordings and varied devices; used to build IndicASR for 22 languages — [ACL Anthology](https://aclanthology.org/2024.findings-acl.639.pdf); [arXiv 2403.01926](https://arxiv.org/html/2403.01926v1)
- 🟡 Related accent benchmarks: Svarah (Indian-accented English, 117 speakers, 65 locations) and LAHAJA (Hindi accents, 12.5 hours) — [CatalyzeX](https://www.catalyzex.com/author/Tahir%20Javed)
- 🟡 Single-reference WER penalises non-standard spellings and code-mixed English words — [IndicVoices page via search](https://ai4bharat.iitm.ac.in/indicvoices_r)

### Inferences
- 🔴 I did NOT find Google/Gemini per-language WER on Indic spontaneous speech; Keepwell must measure Gemini or Google Speech on its own sample of repair-shop audio (noise, speakerphone, technician jargon like "compressor", "gas fill", "PCB" in English words inside Hindi/Telugu).
- 🔴 Fairness risks: worse transcription of Telugu/Tamil/rural accents makes claim notes look inconsistent (leading to false "mismatch" flags) or quotes mis-scoped; women or elderly household speakers may be under-represented in training data. Fraud/inconsistency flags driven by transcript should be disabled or require human review for languages below an accuracy bar.
- 🔴 Mitigations: show transcript back to speaker for confirmation; keep original audio; allow typed correction; per-language/accent error dashboards; calibrate price quotes on job features (appliance, fault, part), not on speaker attributes, language, name, pincode or locality; test quote variance by region and language and document; keep a prohibited-feature list.
- 🔴 Suggested acceptance gate: per-language WER or entity-level accuracy (model number, price, date, fault term) on a local test set, with release blocked for languages that miss the bar; entity accuracy matters more than WER.

### Gaps
- No Gemini/Google per-language Indic WER found; IndicVoices benchmark WER numbers not retrieved; Vistaar per-language mapping uncertain.
- No evidence on quote/flag disparity in Indian service markets.
- Code-mixing (Hinglish, Tenglish) benchmark numbers not found.

## 4. Safety: hazard hard-stop list

### Takeaway
The AI should never give step-by-step instructions for hazardous work (gas, refrigerant handling, mains-voltage internals, capacitor discharge, geyser pressure/thermostat, microwave HV), and should escalate to a qualified technician or the manufacturer. The list must be reviewed by a licensed electrician/appliance engineer and a gas safety expert; standards exist but I found only partial coverage.

### Cited Findings
- 🟡 CEA (Measures relating to Safety and Electric Supply) Regulations 2023 notified 8 June 2023, superseding 2010; cover installation, operation and maintenance of electric lines/apparatus and use of electricity; consumer-installation duties relevant to qualified persons — [TeamLease RegTech](https://www.teamleaseregtech.com/updates/article/24769/central-electricity-authority-measures-relating-to-safety-and-electric/); [CEA](https://cea.nic.in/regulations-category/measures-relating-to-safety-and-electric-supply/?lang=en)
- 🟡 BIS IS 302 series (safety of household and similar electrical appliances) is under revision to align with CEA 2023 — [BIS draft](https://services.bis.gov.in/tmp/PETD25425694_19052024_1.pdf)
- 🟡 CEA invited comments on a draft list of standards referenced under the 2023 regulations — [CEA](https://cea.nic.in/regulations-category/measures-relating-to-safety-and-electric-supply/?lang=en)

### Inferences
- 🔴 Candidate hard-stop categories (from general domain knowledge, unverified here): LPG/gas smell or leak, gas hob/oven burner repair; refrigerant (R32/R290 flammable, R22 toxic/ODS) recharge or brazing; opening a microwave magnetron/HV transformer/capacitor (stored charge); AC/inverter board capacitors and PFC; geyser tank, safety valve, thermostat bypass, scaling with exposed live parts, earth-leak shocks; any burning smell, sparks, swollen parts, water near live parts; work at height (AC outdoor units). Behaviour: refuse instructions, give a generic "switch off at the mains, ventilate, call a qualified technician/emergency number" message, log, notify the agency human. For gas leak: standard advice is no switches/flames, open windows, shut regulator, contact distributor emergency number; verify wording with an expert.
- 🔴 Standards to ask the domain expert to map: BIS IS 302 series, IS 4246 (domestic gas stoves; not confirmed by search), IS 8978/ related LPG standards, IS 1293 plugs/sockets, IS 3043 earthing, manufacturer service manuals and safety labels, Gas Cylinder/Static & Mobile Pressure Vessels rules via PESO, Ozone Depleting Substances Rules for refrigerants, NBC. None of these were verified in this research.
- 🔴 Hard-stop list must be a deterministic rule layer (keyword/classifier plus model) outside the LLM prompt, with a test suite in all supported languages and recall favoured over precision; expert sign-off, versioning and review at least yearly or after incident.

### Gaps
- IS 4246, LPG standards, PESO rules and refrigerant standards not found or verified.
- No Indian regulation found on who may repair household appliances; licensed-electrician requirements apply to electrical installations but not appliance repair per se (unconfirmed).
- Hard-stop list content needs an electrician, refrigeration engineer and gas safety professional.

## 5. Security: prompt injection, PII, Gemini/Vertex data governance

### Takeaway
Treat all customer text, voice, images and PDFs as untrusted data; models can follow instructions hidden in them, and prevention is not fully solved, so limit what the model can do and put humans before consequential actions. Use paid Gemini API (billing-enabled) or Vertex AI, never free tier, for customer data.

### Cited Findings
- 🟢 OWASP LLM01:2025: indirect and multimodal injection (instructions hidden in images or documents, even imperceptible to humans) are in scope; no fool-proof prevention; recommends segregating/labelling untrusted content, least privilege, human approval for high-risk actions — [OWASP LLM01](https://genai.owasp.org/llmrisk/llm01-prompt-injection/)
- 🟡 CSA 2026 note on image-based prompt injection for multimodal agents (claim that OWASP extended LLM01 to multimodal is unconfirmed) — [CSA](https://labs.cloudsecurityalliance.org/research/csa-research-note-image-prompt-injection-multimodal-llm-2026/)
- 🟢 Gemini API Additional Terms: Unpaid Services content may be used to improve products and human reviewers may read it; "Do not submit sensitive, confidential, or personal information"; Paid Services (Cloud project with active billing) not used to improve products, prompts/responses logged for a limited period for abuse detection; EEA/CH/UK get paid terms on all services; versions change (a version effective 23 Mar 2026 seen) — [Gemini API terms](https://ai.google.dev/gemini-api/terms)
- 🟢 Vertex AI data residency: Mumbai (asia-south1) listed for some Gemini models; data at rest stays in the chosen location; generative ML processing occurs in the region/multi-region of the request (model coverage varies) — [Google Cloud docs](https://cloud.google.com/vertex-ai/generative-ai/docs/learn/data-residency)
- 🟡 Vertex defaults per a third-party summary: flagged prompts may be cached/kept up to 90 days for abuse monitoring, zero data retention only by approval, no training on customer data without permission (verify with Google docs/account team) — [DevelopersDigest](https://www.developersdigest.tech/models/data-retention/vertex)
- 🟢 Gemini API safety settings: adjustable categories harassment, hate speech, sexually explicit, dangerous; default threshold Off for Gemini 2.5 and 3 models if unset; thresholds based on probability not severity; built-in non-adjustable protections (e.g. child safety) — [Gemini safety settings](https://ai.google.dev/gemini-api/docs/safety-settings)

### Inferences
- 🔴 Safety filters are about content harms, not repair hazards or prompt injection; they will not catch "unsafe appliance advice". Build hazard rules separately (section 4). Vertex safety-filter and model-card docs were not retrieved; read Google's Vertex "Responsible AI" and Gemini model card pages directly.
- 🔴 Injection controls: structured-output only (JSON schema) so the model cannot call tools or send messages; no tool access from document-reading prompts; strip/flag text like "ignore previous instructions", "approve this claim", or invoice text that addresses the AI; run a second pass that compares extracted fields with the image; deterministic validation of amounts (GST math, date in range); human approval for any claim decision or price; log inputs; red-team with poisoned invoice images and PDF hidden text.
- 🔴 PII: redact Aadhaar, PAN, phone, address, bank, UPI before sending where not needed (extract only fields needed); mask face/identifiers in appliance photos; encrypted storage in India region; per-agency tenant isolation; retention schedule; DPA with agencies; check if Gemini API calls via India region endpoints keep data in India (API-key route may not offer residency; Vertex does for listed models). For cross-border: DPDP Rule 15 conditions pending, so choose asia-south1 to be safe.

### Gaps
- Vertex zero-retention and abuse-monitoring retention not verified on Google Cloud's own pages; model-by-model Mumbai availability for current Gemini versions not checked.
- Vertex AI safety filters, model cards and Google Responsible AI resources not retrieved.
- No source quantified injection success rates on Gemini invoices.

## 6. Legal-advice boundary ("evidence pack, not legal advice")

### Takeaway
The FTC's DoNotPay order is a US consumer-protection warning against marketing an AI as equivalent to a lawyer without evidence; no Indian equivalent was found, so the safe design is to present Keepwell output as an organised evidence file with factual summaries and sourced warranty terms, never as a prediction of legal rights or a drafted legal opinion.

### Cited Findings
- 🟡 FTC finalised order against DoNotPay (approved 16 Jan 2025, announced Feb 2025, 5-0): must pay $193,000, notify subscribers from 2021 to 2023, and may not claim its service performs like a real lawyer unless it has competent evidence — [FTC](https://www.ftc.gov/node/87474); [GRC Report](https://www.grcreport.com/post/ftc-takes-a-stand-against-donotpays-ai-lawyer-claims)

### Inferences
- 🔴 India: the Advocates Act 1961 restricts "practising law" to enrolled advocates, and the Bar Council of India has been hostile to unauthorised legal-service providers; I did not verify any Indian case on AI legal advice. Needs a lawyer.
- 🔴 Framing requirements: do not say "we will win your claim", "legally valid", "you are entitled to"; say "documents found, warranty clause X says Y (quoted), gaps: invoice date missing"; include disclaimers in plain local language but do not rely on them alone (the FTC order targeted marketing claims); avoid drafting consumer-forum notices as legal advice unless reviewed by a lawyer; point to consumer helpline (National Consumer Helpline 1915) and e-Daakhil as options, with factual information only (confirm).
- 🔴 Marketing claims should be substantiated (accuracy statements, "AI expert" wording); CCPA's misleading advertisement guidelines apply (not researched).

### Gaps
- Indian law on AI and unauthorised practice of law not researched.
- No evidence found whether warranty "eligibility" prediction counts as legal advice in India.

## Summary of items needing professional review
- Lawyer: fiduciary/processor allocation and DPA; consent/notice text and voice-recording consent; children's data; CPA unfair-trade exposure on quotes and claim repudiation; whether any product is insurance (IRDAI); unauthorised practice of law; cross-border Rule 15.
- Domain experts: hazard hard-stop list, safe-escalation wording, mapping to BIS/CEA/PESO/manufacturer manuals; refrigerant and gas specialists.
- Technical/security: prompt-injection red team; Google account team for Vertex retention/ZDR and region support.
