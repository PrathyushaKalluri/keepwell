# Keepwell Care Engine: competitive analysis and workarounds

*As of 15 Nov 2026. Built only from the problem map (`Keepwell problem map and scenarios.md`) and three research notes in `research_notes/Keepwell competitive landscape and architecture/` (`competitors_scenario_A.md`, `competitors_scenarios_B_D.md`, `competitors_scenarios_C_E.md`). No new research was run. Most vendor facts in the notes come from search snippets, not full-page reads.*

**Labels.** Sourced = linked in the notes. Secondary = aggregator, press relay or vendor marketing. UNVERIFIED = no source or conflicting sources. Inference = my reading, not a finding. **"Not found" always means absence of evidence in a small number of searches, not proof that nothing exists.**

Scenario order: A (agency AI desk, entry wedge), B (two-sided record plus plans; D is folded in here), C (claims triage for administrators and OEMs), D (consumer claim and price advocate), E (circular buyback, refurb, EPR; vision).

---

## 1. Summary

**Whitespace (inference, absence of evidence).**
- No India-first, vernacular, voice or WhatsApp-first tool was found that links intake, job card and parts-to-carry for small appliance agencies (about 11 searches).
- No consumer-first, brand-agnostic record app with traction in India was found. The one named (TOTOKO) had about 1,000 downloads by May 2022.
- No product was found that carries one unit from warranty to service history to exchange to EPR certificate.
- No Indian private service for consumer warranty complaints was found (LegalKart and others returned nothing).

**Crowded.**
- Warranty administration and plans: OneAssist, Servify, Onsitego, Zopper, plus OEM and retailer plans (Samsung Care+, Croma ZipCare, Reliance resQ).
- Generic field-service software: Zoho FSM, Jobber, Housecall Pro.
- EPR and recycler traceability: Attero, Recykal, Karo Sambhav.
- Phone and laptop recommerce: Cashify, Back Market, refurbed.

**Top three threats (inference).**
1. **Servify.** It already claims diagnostics and an AI claims agent, serves OEMs and insurers, and has about 60% of its business in India. It is the nearest rival for C and E (phones), and its consumer-wallet origin means it understands B.
2. **Bernard and Fieldproxy.** Bernard is the closest functional match to A (diagnosis plus ranked parts, US). Fieldproxy already has an appliance diagnostic agent with cited manuals and service history. Neither is verified for Indian languages or India.
3. **Horizontal Indian voice-agent firms (Hunar.AI, Ringg, Bolna, Smallest.ai) moving into home services.** They are funded and vernacular, but none is shown in appliance repair. A close fourth for B and E: OEMs with their own apps (Samsung, LG) and Attero, who is both LG's exchange operator and a recycler.

**One-line positioning.** Keepwell is the machine record and pre-visit desk for India's independent appliance agencies, in their language, paid per fix that passes a test, which later lets warranty networks and recyclers act on verified history.

**Honest caution.** The notes find no evidence either way that small agencies will pay for software, and no measured repeat-visit rate. The gap is plausible, not proven.

---

## 2. Scenario analysis

### Scenario A: Prepared Visit (agency AI desk)

**(a) Competitors**

| Player | Type | Target user | What it does | What it does not do | Traction / funding (status) | India |
|---|---|---|---|---|---|---|
| Bernard | Direct (US) | Appliance repair firms | Pre-ID combines symptoms, history, manuals, parts to give diagnosis, ranked parts, follow-ups; 24/7 call handling ([Extruct](https://www.extruct.ai/hub/bernardhq-com/), [F4](https://f4.fund/startups/bernardhq)) | Indian languages, India pricing not found; may be an operator/roll-up model (UNVERIFIED) | Funding and pricing not found | None found |
| Fieldproxy | Direct / adjacent | Appliance field-service teams | Voice agent: symptom, likely cause, DIY steps or booking; cites manuals and service history ([page](https://www.fieldproxy.ai/ai-agents/appliance-diagnostic-agent)) | Looks customer-facing, not a technician job card or parts-to-carry (inference); languages, pricing, geography not stated | Not found | India-reachable (inference); not verified |
| Aquant | Adjacent (OEM) | OEM service teams | Service intelligence; Service Hero crowdsourced appliance troubleshooting; Vision AI early access ([FSN](https://www.fieldservicenews.com/aquant-announces-70-million-series-c-funding-round-to-revolutionize-the-service-industry-using-artificial-intelligence/), [Aquant](https://www.aquant.ai/service-hero/)) | Small independents; Indian languages | $70M Series C (date unconfirmed, one release Oct 2021); totals differ by source (secondary) | None found |
| Bruviti | Adjacent (OEM) | OEMs, distributors | Agentic aftermarket service ([release](https://www.accessnewswire.com/newsroom/en/computers-technology-and-internet/bruviti-raises-6-million-to-accelerate-agentic-automation-in-afte-1057663)) | Small independents (inference) | $5M (2022, Marcone) and $6M (Aug 2025); total $11M vs $6.0M conflict | None found |
| Zoho FSM, Jobber, Housecall Pro | Incumbent (generic FSM) | Service SMBs | Scheduling, dispatch, quotes | Fault hypotheses, parts-to-carry, appliance features (none mentioned in comparison pages) | Zoho India partner quotes ₹1,000 and ₹1,800 per user per month; Zoho's own page lists USD appointment-based pricing; conflict ([Zoho](https://help.zoho.com/portal/en/kb/fsm/getting-started/articles/fsm-pricing), [partner](https://precisiontech.in/software/zoho/zoho-fsm/zoho-fsm-in-gudgaon/)). Jobber/Housecall prices from affiliate aggregators, UNVERIFIED | Zoho has Indian distribution |
| Samsung, LG OEM tools | Incumbent (OEM) | Own customers and network | Samsung: 3,000+ touchpoints, AI remote diagnostics, Members app ([Samsung](https://news.samsung.com/in/samsung-india-enhances-customer-service-with-ai-powered-remote-diagnostic-and-troubleshooting-tool)); LG: ThinQ, engineer calls | Other brands; independents lack manuals and parts | Company statements | Yes |
| Urban Company | Adjacent (marketplace) | Households and partner technicians | AC and appliance repair, rate card, verified technicians ([UC](https://partner.urbancompany.com/bhopal)) | Partner-app features and commission not found | Not covered in A notes; loss-making FY26 per problem map | Yes |
| Hunar.AI, Ringg, Bolna, Smallest.ai, Hulp | Adjacent (voice/WhatsApp) | Enterprises, hiring, household concierge | Vernacular voice and WhatsApp agents. Hunar ₹40 Cr Series A (Oct 2026), Ringg $10M Series A (Aug 2026), Bolna $6.3M seed, Hulp $2.6M seed ([YourStory](https://yourstory.com/2026/10/hunarai-raises-rs-40-crore-in-series-a-led-by-blume-ventures), [Ringg](https://yourstory.com/2026/08/voice-ai-startup-ringg-ai-raises-10m-series-a-peak-xv-partners), [Bolna](https://yourstory.com/ai-story/voice-ai-startup-bolna-raises-63m-led-by-general-catalyst), [Hulp](https://ascendants.in/business-stories/hulp-raises-2-6-million-seed-funding-ai-personal-assistance/attachment/hulp/)) | None shown in appliance repair; no technician dispatch for Hulp | As listed (secondary press) | Yes |

Not searched: Revin AI, ServiceTitan, ServicePower, Marcone/mSupply tools, Whirlpool apps, Indian FSM startups.

**(b) Workarounds**

| Workaround | Who uses it | Why it works | Why it fails | Evidence |
|---|---|---|---|---|
| Salvaged parts, local dealers | Independent technicians | Free, immediate | Non-original parts; OEMs restrict manuals and genuine parts | Sourced ([TheNewsMinute](https://www.thenewsminute.com/amp/story/telangana/why-hyderabads-it-household-repair-shops-have-become-bad-at-fixing-your-devices-study), [Toxics Link](https://toxicslink.org/wp-content/uploads/2026/03/Electronic%20Repair%20report.pdf)) |
| YouTube and tutorials | Technicians | Free, familiar | No model-specific diagnosis | Weak source (low-authority blog) |
| Formal skilling (NSDC pack, OEM academies) | Technicians | Structured | Adoption unknown | Sourced, [Electronics Media](https://www.electronicsmedia.info/?p=82098) |
| Paper slips, notebooks, phone calls, WhatsApp/Telegram parts groups, IVR, spreadsheets | Small agencies | Free, familiar | Unknown | **UNVERIFIED, no source** |

**(c) Gap and difference.** Gap: a vernacular, voice/WhatsApp-first desk at small-agency price that links intake, job card, parts and repeat-failure history. Keepwell differs by: Hindi/Telugu/Tamil/English intake, job card in the technician's language, parts claimed only when a catalogue confirms, safety escalation, and pay-per-passed-test pricing (60 free days). Price anchor: Zoho at ₹1,000-1,800 per user per month; Keepwell desk fee ₹1,500 per agency per month (problem map). WhatsApp Business API costs are layered and sources conflict (UNVERIFIED).

**(d) Copyability (inference)**

| Feature | Ease | By whom and why |
|---|---|---|
| LLM call summary, manual retrieval, quote templates, WhatsApp notices | Easy | Zoho, Fieldproxy; generic |
| Voice intake in Indian languages | Medium | Bolna, Ringg, Smallest; they have the speech stack but not appliance context. Accuracy on noisy calls unproven for Keepwell too |
| Fault hypotheses and ranked parts | Medium | Bernard, Fieldproxy; needs India model and parts data |
| Catalogue-verified parts-to-carry | Hard | Needs technician-confirmed repair data and dealer data |
| Agency repeat-failure history | Hard | Only accrues with agency usage |
| Trust with unorganised agencies, low-ticket pricing | Hard | Enterprise vendors are not priced or sold for it |

---

### Scenario B: Record plus plans (D folded in)

**(a) Competitors**

| Player | Type | Target user | What it does | What it does not do | Traction / funding (status) | India |
|---|---|---|---|---|---|---|
| OneAssist | Incumbent | Households via retailers, OEMs | Protection, extended warranty | Covers only plans it sold; retailer owns relationship; T&Cs limit contact to plan terms (renewal impact unclear) | FY25 revenue ₹623 Cr, net loss about ₹11 Cr ([Entrackr](https://entrackr.com/exclusive/exclusive-peak-xv-backed-oneassist-to-raise-rs-108-cr-from-stride-ventures-10064749)); company claim of 2 crore customers via aggregator. Funding $64M vs $77M conflict | Yes |
| Servify | Incumbent / adjacent | OEMs, carriers, insurers | Began 2016 as a consumer wallet (bills, warranties) ([Business Standard](https://www.business-standard.com/amp/article/companies/servify-now-a-digital-assistant-for-your-devices-116120500054_1.html)); now mostly B2B | Consumer-first brand-agnostic record | Revenue differs by source: FY24 about ₹755 Cr (secondary), FY25 about ₹781 Cr (problem map), FY23 ₹611 Cr (company-claimed, C notes) | Yes |
| Onsitego, Zopper | Incumbent | Retail buyers | Plans, extended warranty | Same as OneAssist; Zopper/Apple campaign drew complaints; Onsitego current revenue not found | Onsitego $32M vs $28.5M conflict; Series B extended to $30M with IFC ([Inc42](https://inc42.com/buzz/onsitego-raises-capital-from-ifc-extends-series-b-round-to-30-mn)) | Yes |
| Croma ZipCare, Reliance resQ, Samsung Care+ | Incumbent (retailer/OEM) | Own buyers | AC AMC ₹1,999 per year (list ₹2,499), narrow coverage; resQ extended warranty for Reliance purchases only ([Croma](https://croma.com/zipcare-maintain-amc-plan-for-air-conditioner-1-year/p/272182), [Reliance](https://www.reliancedigital.in/product/4-year-resq-care-plan-rcp-extended-warranty-air-conditioner-from-rs-80000-to-rs-1l-9500851)) | Cross-brand; renewal terms not found | Prices only | Yes |
| TOTOKO, CheckMyWarranty, Warranti, HoldMyBill, SnapHome | Direct (tiny) | Households | Bill and warranty wallets, reminders | Claim execution; depend on manual entry | TOTOKO 1,000+ downloads (May 2022, [YourStory](https://yourstory.com/2022/05/delhi-based-startup-helping-households-msmes-manage-bills-and-warranty-totoko)); others no data; TOTOKO status after 2022 unknown | Yes |
| Samsung Members, LG ThinQ | Incumbent (OEM) | Own buyers | Registration, service tracking | Single brand; wrong dates reported ([SamMobile](https://sammobile.com/news/samsung-faces-complaints-galaxy-phones-showing-shorter-warranty-periods-india)) | App features and installs not researched | Yes |
| Centriq, HomeBinder (US) | Adjacent | Homeowners, insurers, HVAC | Home-management apps | Pivoted B2B or faded; Centriq last raise $5M Jan 2019, HomeBinder $2.99M ([CB Insights](https://www.cbinsights.com/company/centriq-technology), [CB](https://www.cbinsights.com/company/homebinder)); status unverified | Aggregator | None |

**For D (consumer claim help):** NCH complaints 12.36 lakh (FY24), 13.16 lakh (FY25), 20.49 lakh (FY26) per a Lok Sabha reply as relayed; periods not strictly comparable ([FPJ](https://www.freepressjournal.in/business/541-lakh-complaints-received-by-national-consumer-helpline-23-complaints-from-southern-states-says-nidhi-khare-secretary-of-the-department-of-consumer-affairs)). WhatsApp is about 30% of NCH intake ([FPJ](https://www.freepressjournal.in/business/national-consumer-helpline-receives-one-lakh-complaints-per-month-hike-in-grievance-registration-through-whatsapp)). Government channels (NCH, e-Jagriti) are the incumbents; private Indian legal-tech not found. DoNotPay shows the legal-claim risk: FTC order, $193,000 relief ([FTC](https://www.ftc.gov/node/87474)).

**(b) Workarounds (B and D)**

| Workaround | Who uses it | Why it works | Why it fails | Evidence |
|---|---|---|---|---|
| Dealer duplicate bill | Households | Dealers can usually supply one | Warranty card alone not enough | Sourced, [Business Standard](https://www.business-standard.com/article/pf/warranty-doesn-t-guarantee-good-service-114061700524_1.html) |
| Not keeping receipts | Many buyers | No effort | Invoice is the deciding document | Sourced, [Tribune](https://m.tribuneindia.com/news/archive/features/news-detail-787883) |
| Photos, WhatsApp-to-self, email search | Households | Zero cost | Not searchable by machine; no claim pack | **UNVERIFIED, inferred from common practice** |
| Brand call centres and OEM apps | Households | Official | Single brand; wrong dates; warranty start-date ambiguity taken up by CCPA in 2024 ([ThePrint](https://theprint.in/india/ccpa-appliance-makers-discuss-issue-of-commencement-of-warranty-period/2143793)) | Sourced |
| Consumer helpline, e-Jagriti, courts | Aggrieved households | Free or cheap | Slow; evidence pack is the missing input (inference) | Volumes sourced; resolution times not found |
| Dealer-sold plans at purchase | Households | Seller holds invoice | Narrow cover, non-transferable | Sourced (Croma) |

**(c) Gap and difference.** Record apps fail on entry burden and low need frequency; survivors had a B2B payer (Centriq/HomeServe, Servify B2B). Keepwell seeds the record from agency jobs, not consumer downloads, ingests invoices (Document AI), and outputs a claim-ready evidence pack framed as assistance, not legal advice. The evidence on retention is anecdotal (food-tracking thread, vendor blogs). Willingness to pay for D is unproven; the problem map treats D as an acquisition channel.

**(d) Copyability (inference)**

| Feature | Ease | By whom and why |
|---|---|---|
| Invoice upload and warranty reminder | Easy | Any wallet app, OEM apps |
| Cross-brand record seeded by agency jobs | Hard | Needs agency distribution; administrators own plan customers only |
| Plan renewal outreach | Medium | Administrators and retailers already hold the customers |
| Claim evidence pack and complaint draft | Medium | Easy to draft; hard to get verified service history |
| Selling plans (15% commission) | Medium | Licence rules unchecked (problem map says not researched) |

---

### Scenario C: Claims and first-visit triage for administrators and OEMs

**(a) Competitors**

| Player | Type | Target user | What it does | What it does not do | Traction / funding (status) | India |
|---|---|---|---|---|---|---|
| Servify | Direct / incumbent | OEMs, carriers, insurers | Diagnostics tool; marketed natural-language AI claims agent with approval/denial intelligence; 100+ brands self-reported ([Servify](https://global.servify.tech/tech-platform), [App Store](https://apps.apple.com/in/app/servify-device-assistant/id1048863815)) | Agency-side machine record and first-visit parts prediction not found; whether the AI agent is live in India or only in the AT&T programme is UNVERIFIED | Total raised $133M to $142M (rounds 8 to 14); valuation $654M vs about $800M; revenue figures conflict (see section 7) ([Multiples](https://multiples.vc/private-comps/servify), [CB Insights](https://www.cbinsights.com/company/servify/financials)) | Yes, about 60% of business |
| OneAssist, Onsitego, Zopper | Incumbent (buyers) | Retailers, OEMs | Administer claims | Likely price-sensitive, thin margin (inference) | See B | Yes |
| Shift Technology | Adjacent | Insurers | Fraud and claims AI, agentic claims 2025 ([PYMNTS](https://www.pymnts.com/?p=1069375)) | Appliance warranty; priced for large insurers (inference) | About $320M total (profile) | Not found |
| Tractable | Adjacent | Auto and property insurers | Photo damage assessment | Appliances (inference) | $65M Series E 2023, $184.9M total ([Insight](https://www.insightpartners.com/ideas/tractable-ai-raises-65m-in-series-e-funding-led-by-softbank-vision-fund-2-investment-to-power-next-generation-ai-for-instant-visual-assessments-within-the-automotive-and-property-ecosystems/)) | Not found |
| Aquant, Bruviti | Adjacent | OEM service teams | Technician copilots | Administrators' claims | See A | Not found |

Not researched: Assurant India, Asurion India, Polygrade, OEM in-house claim systems, any vendor pricing.

**(b) Workarounds**

| Workaround | Who uses it | Why it works | Why it fails | Evidence |
|---|---|---|---|---|
| Manual claims review and phone triage | Administrators | Existing staff | Slower turnaround | Thin; the only source is Deloitte via CFOtech on **insurance**, not warranty ([CFOtech](https://cfotech.in/story/insurance-samadhan-tackles-india-s-claims-grievance-crunch)) |
| OEM in-house claim systems | OEMs | Control | Single brand | Not researched |
| Dispatch without prior triage | Networks | Simple | Missed visits and unresolved requests alleged | Anecdotal single reviews ([MouthShut](https://www.mouthshut.com/review/zopper-review-pmrnmntloop)) |

**(c) Gap and difference.** "AI claims triage" alone is not differentiated because Servify claims it (inference). The difference must be the agency-side record plus predicted first-visit diagnosis and parts, proven first by Scenario A outcomes. No source shows anyone combining those for Indian administrators (absence of evidence). Buyer needs (pilot structure, security, DPDP, data residency) were not researched.

**(d) Copyability (inference)**

| Feature | Ease | By whom and why |
|---|---|---|
| Claim classification and approve/deny assist | Easy to medium | Servify already claims it |
| Triage using verified repair history | Hard | Requires agency-side data Servify does not obviously hold |
| Repeat-failure and parts-demand data | Hard | Accrues only with agency volume |
| Enterprise integration and security | Medium | Servify has relationships; Keepwell does not |

---

### Scenario D: Consumer claim and fair-price advocate

Mostly covered under B. Differences for D alone:

**(a) Competitors.** Government channels (NCH, e-Jagriti: 1,62,474 cases filed and 1,50,197 disposed in 2025 per [Tribune](https://www.tribuneindia.com/news/india/1-50-lakh-consumer-grievances-out-of-1-62-lakh-cases-disposed-of-via-e-jagriti-portal-in-2025-mos/); another report gives a different window, conflict). Consumer courts. Brand helplines. Private Indian legal-tech: not found. DoNotPay (US): adjacent cautionary precedent, not a competitor. No neutral fair-price benchmark was found.

**(b) Workarounds.** As in B (dealer duplicates, helpline, courts). Need evidence: LocalCircles polls (self-selected) show about 46% stuck with defective high-value products and 53% in a later survey not refunded ([Moneylife](https://moneylife.in/article/nearly-50-percentage-consumers-stuck-with-inherently-defective-highvalue-products-due-to-broken-redressal-system-localcircles/66777.html), [BS](https://business-standard.com/industry/news/53-consumers-did-not-get-refund-for-inherently-defective-products-survey-124031500916_1.html)).

**(c) Gap.** Strong pain evidence, weak willingness-to-pay evidence. Keepwell assembles the evidence pack from its own record; success fee assumption 10% of recovered value (assumption, not a finding).

**(d) Copyability (inference).** Drafting: easy (any LLM). Verified evidence from service history: hard. Legal credibility and helpline or e-filing access: medium. Legal-advice claims carry regulatory risk (DoNotPay).

---

### Scenario E: Circular loop (buyback, refurb, EPR)

**(a) Competitors**

| Player | Type | Target user | What it does | What it does not do | Traction / funding (status) | India |
|---|---|---|---|---|---|---|
| Cashify | Incumbent (phones/laptops) | Consumers | Recommerce | Large appliances; grading method not found | FY25 revenue about ₹1,096 Cr, loss about ₹10.5 Cr, IPO targeted early 2027 ([Inc42](https://inc42.com/buzz/cashify-trims-loss-by-80-to-inr-11-cr-in-fy25/), [Angel One](https://oga-prod.angelone.in/news/ipos/cashify-appointed-icici-securities-jm-financial-and-nomura-as-lead-bankers-ahead-of-ipo)) | Yes |
| LG exchange via Attero and Digi2L | Incumbent (OEM) | LG and other-brand owners | Door-step human check, fixed value tables; EPR take-back via call centre ([LG](https://www.lg.com/in/exchangeoffers/tnc)) | Photo-based grading; link to service history | Not applicable | Yes |
| Attero | Incumbent / possible partner | OEMs, recyclers | Recycling, MetalMandi B2B scrap platform with AI live prices (2 lakh+ downloads, claim) | Starts at collection, not the home record (inference) | ₹150 Cr capex ([Energetica](https://www.energetica-india.net/news/attero-to-invest-inr-150-crore-to-expand-e-waste-copper-and-lithium-ion-battery-recycling)) | Yes |
| Recykal | Adjacent | Producers, recyclers | EPR marketplace, audits with weighbridge and geo-tagged photos | Consumer or warranty link | $18M Series D at $280M (reported June 2026) and a $23M bridge; figures disagree ([Pulse](https://www.pulse.bot/venture-capital/news/exclusive-morgan-stanley-backed-recykal-raises-18-mn-at-280-mn-valuation-0368d366-ea7d-4979-b009-b1073fb7fa88/), [IamRenew](https://www.iamrenew.com/sustainability/waste-tech-maker-recykal-secures-23-million-funds-to-support-expansion/)) | Yes |
| Karo Sambhav | Adjacent (PRO) | Producers | Traceability platform | Same | ₹56 Cr pre-Series A ([Outlook Business](https://www.outlookbusiness.com/corporate/karo-sambhav-gets-56-cr-from-rainmatter-for-critical-raw-material-recovery)) | Yes |
| Servify trade-in | Adjacent | Phone owners | AI hardware test and valuation | Appliances | See C | Yes |
| Samsung (exploring), Eureka Forbes (Big Exchange, Aug 2025) | Incumbent (OEM) | Own buyers | Appliance exchange ([The Week](https://www.theweek.in/wire-updates/business/2026/01/14/samsung-explores-smartphone-like-upgrade-platform-for-home-appliances-customers-in-india.html)) | Samsung scheme unconfirmed | n/a | Yes |
| Back Market, refurbed, Reebelo | Adjacent (global) | Consumers | Refurb marketplaces; phone/laptop-centric | Large appliances (inference) | Back Market 2024 revenue about $415M (Sacra); refurbed Series D $58M; GMV claims conflict | None found |

Not fetched: Refwash, Costify, Underdog, OLX/Quikr, appliance kabadiwala price evidence, EPR certificate price benchmarks, grading methods.

**(b) Workarounds**

| Workaround | Who uses it | Why it works | Why it fails | Evidence |
|---|---|---|---|---|
| Informal kabadiwala | Households | Cash, door-step | Hazardous methods; no provenance. Informal share estimates conflict (75% to over 90%; Attero CEO claims 99%, interested party) | Secondary |
| OEM exchange | Households | Discount on a new unit | Fixed tables, human check | Sourced (LG) |
| LG call-centre EPR take-back | Households | Official | Call, callback, visit | Sourced |

**(c) Gap and difference.** Appliance grading by AI from photos and a unit-level record from warranty to EPR certificate were not found in public sources (absence of evidence). Keepwell: Gemini vision grading into refurb, harvest or scrap, with provenance. Exposure: EPR price floor stayed in court (problem map); CPCB portal API access unknown; no refurbisher unit economics published.

**(d) Copyability (inference)**

| Feature | Ease | By whom and why |
|---|---|---|
| Photo grading | Medium | Cashify has grading ops for phones; appliances need new standards |
| Pickup and partner network | Hard | Operations-heavy; Attero already bundled with LG |
| Provenance link from service record | Hard | Needs A and B data |
| EPR certificate traceability | Medium | Recykal and Attero already hold it from collection |

---

## 3. Cross-scenario view

| Scenario | Nearest competitor | Why |
|---|---|---|
| A | Bernard (function), Fieldproxy (agentic, India-reachable), Zoho FSM (price and distribution) | Bernard has diagnosis plus ranked parts; Zoho owns the Indian price anchor |
| B | OneAssist and Servify (plans, record origin); OEM apps (records) | They hold the customer and the plan |
| C | Servify | Already claims diagnostics and AI claims agent |
| D | Government channels (NCH, e-Jagriti) | Free, high volume; no private rival found |
| E | Attero (LG exchange plus recycling) and Cashify (grading for phones) | Bundled with OEMs; Recykal on traceability |

**Threat ranking (inference).**

| Rank | Threat | Reason |
|---|---|---|
| 1 | Servify | Funded, B2B relationships, diagnostics, India base; hits C directly and could add agency tools |
| 2 | Bernard / Fieldproxy | Same product shape as A; English-first so far; Indian entry would be the trigger |
| 3 | Indian voice-agent firms verticalizing | Funded, vernacular speech stack |
| 4 | OEM in-house AI (Samsung) | Deepening, but single brand |
| 5 | Attero / Recykal | Own the end-of-life data; threat to E only |
| 6 | Zoho FSM | Can add LLM features cheaply with Indian distribution |

**Likely partners or acquirers, not rivals (inference).**
- Servify, OneAssist, Onsitego, Zopper: buyers for C and plan partners for B (administrators need licensed plan underwriting; Keepwell would earn commission).
- Attero, Recykal, Karo Sambhav: partners for E (collection, certificates), also possible acquirers.
- Marcone (parts distributor, Bruviti investor): a parts-data partner type.
- Hunar.AI, Ringg, Bolna: a build-or-buy voice layer.
- Samsung, LG: unlikely to partner with independents; more likely to see Keepwell as access to the independent network.

---

## 4. Moat assessment

| Asset | Defensible? | Why (inference) |
|---|---|---|
| Gemini models, prompts, RAG over manuals | No | Commodity; Fieldproxy already cites manuals and history. Gemini alone gives nothing defensible |
| Agency-side data: job outcomes, parts used, repeat failures | Yes, once accrued | Only exists with agency usage; not held by OEMs, administrators or Zoho |
| Record linkage (invoice, service history, plan, EPR) | Yes, with scale | Competitors hold single slices: OEM (one brand), administrator (own plans), recycler (collection onward) |
| Vernacular noisy-speech data | Partly | Needs real recordings; Google's language lists do not prove accuracy; voice firms could build the same |
| Technician-confirmed catalogue for parts compatibility | Yes, slow | Hard to buy; the model must never declare compatibility alone |
| Partner agreements (administrators, recyclers, dealers) | Yes if exclusive or deep | Switching cost and data sharing |
| Low-ticket trust with unorganised agencies | Partly | Hard for enterprise vendors; not a barrier to a local competitor |

Cold start is the risk: the moat only forms if agencies adopt first, and the notes find no evidence that small agencies pay for software.

---

## 5. Positioning statements

- **A.** For independent appliance agencies in India, who lose trips to wrong diagnoses and wrong parts, Keepwell is a vernacular voice and WhatsApp desk that sends a technician-ready job card, unlike US tools (Bernard) or generic FSM (Zoho), and charges only for fixes that pass a test.
- **B.** For households and agencies, Keepwell is a cross-brand machine record seeded by real repairs, unlike single-brand OEM apps and plan-only administrators, so history, warranty status and plan renewals are always right.
- **C.** For warranty administrators and OEM service heads, Keepwell triages claims and prepares the first visit from verified agency history, unlike claims-AI that scores approval without repair-outcome data.
- **D.** For households stuck with a refused claim, Keepwell assembles the evidence pack and a draft complaint from the machine's own record, unlike helplines that start from nothing (framed as assistance, not legal advice).
- **E.** For households, refurbishers and recyclers, Keepwell grades an old unit from photos and routes it with provenance, unlike door-step fixed-table checks that carry no history.

---

## 6. What to validate next

| Gap claim | Test | Kills the claim if... | Tied to note gap |
|---|---|---|---|
| A: agencies lose trips and would pay | 15-20 agency interviews; 8-10 for workarounds (WhatsApp, slips, notebooks, repeat-visit cost); does fewer trips hurt revenue? | Agencies see no cost from repeat visits or prefer them | A: workarounds UNVERIFIED; no repeat-visit rate |
| A: price works | Paid pilot, 3-5 agencies, ₹40 vs ₹100 per fix; measure Gemini cost per job | Cost per job exceeds fee, or agencies refuse | Gemini pricing unverified |
| A: no vernacular rival | Search and call Bernard, Fieldproxy, Smallest.ai, Zoho; test Indian-language support | One already serves Indian-language small agencies | Language data missing for all vendors but Smallest |
| A: voice accuracy | Test Hindi, Telugu, Tamil recordings of real complaints | Accuracy fails on noisy lines | Google language lists only |
| B: household record sticks | Seed from agency jobs; measure return use at breakdown and renewal | Households never open it | Retention evidence anecdotal |
| B: current household workarounds | Small survey on lost bills, photos, WhatsApp-to-self | Few lose bills | Direct evidence not found |
| B: plan commission | Check IRDAI and service-contract rules; AMC prices and renewals for Urban Company and local vendors | Licence barrier, or plans not sellable | Renewal data not found; rules unresearched |
| C: buyer value | Interview two administrators or OEM service heads; confirm whether Servify's AI agent is live in India; check DPDP and security asks | Servify already covers it for them | Servify India status unverified; buyer evaluation unresearched |
| D: willingness to pay | Ask 20 consumers with refused claims; search Indian legal-tech again | No payer | LegalKart not found |
| E: appliance grading gap | Check Attero, Cashify and Refwash grading; get kabadiwala price evidence | Existing grading covers appliances | Several E sources not fetched |
| All | Rerun searches on unsearched names: Revin, ServiceTitan, ServicePower, Assurant, Asurion, Polygrade | A rival appears | Listed gaps in each note |

---

## 7. Evidence status

| Claim class | Status | Notes and conflicts |
|---|---|---|
| Competitor product descriptions (Bernard, Fieldproxy, Aquant, Bruviti, Servify, OEM tools) | Secondary | Vendor pages and profiles; many from snippets, not full-page reads |
| Competitor absence (no India-first vernacular desk, no consumer record app with traction, no Indian consumer legal-tech, no appliance AI grading) | UNVERIFIED | Absence of evidence in a limited number of searches (about 11 for A; 8 for B and D; 14 for C and E) |
| Servify revenue | Conflict | FY23 ₹611 Cr (company-claimed); FY24 about ₹755 Cr or ₹94 Cr loss (secondary, unverified against filings); FY25 about ₹781 Cr, loss ₹85 Cr (problem map, earlier research). Use as a range, verify against filings |
| Servify funding | Conflict | $133M to $142M total; D3 ₹66.27 Cr; valuation $654M vs about $800M vs $680-700M |
| OneAssist revenue and funding | Conflict | FY25 ₹623 Cr per the B notes; problem map cites about ₹623 Cr with a "conflicting figures across sources" caveat; funding $64M vs $77M; 2 crore customers is a company claim |
| Onsitego funding, revenue | Conflict / stale | $32M vs $28.5M; $82M 2020 revenue is stale; current revenue not found |
| Aquant, Bruviti funding | Conflict | Aquant totals $112M to $130M+, Series C date unconfirmed; Bruviti $11M vs $6.0M |
| Recykal, refurbed funding and GMV | Conflict | Round sizes and valuations differ across sources |
| Cashify revenue | Sourced / secondary | FY25 about ₹1,096 Cr; IPO timing from a broker report |
| Zoho, Jobber, Housecall Pro pricing | Conflict | Zoho USD vs INR partner pricing; Jobber and Housecall from affiliate aggregators |
| WhatsApp Business API pricing | UNVERIFIED | Rates differ by source |
| NCH and e-Jagriti volumes | Secondary | Article-to-figure mapping unverified; periods not comparable; e-Jagriti windows conflict |
| LocalCircles consumer polls | Secondary | Self-selected |
| Market sizes (repair about ₹9,000-10,000 Cr; extended warranty about ₹37,000 Cr) | Secondary | Vendor-grade; use as ranges. Not otherwise used here |
| Right-to-repair portal | UNVERIFIED | Launch date disputed; contents unconfirmed |
| Grey-market share (over 90%) and informal e-waste share | UNVERIFIED | Estimates conflict (75% to over 90%; Attero 99% from an interested party) |
| EPR rules, CPCB counts, price floor | Secondary | Price floor stayed in court; no final judgment found |
| Workarounds: paper, WhatsApp, spreadsheets, IVR, photo-to-self | UNVERIFIED | No source; inference from common practice |
| Workarounds: salvaged parts, restricted OEM access, lost invoices, dealer duplicates | Sourced / secondary | Toxics Link, Business Standard, Tribune |
| Willingness to pay (agencies, households, administrators) | UNVERIFIED | No data in any note |
| Retention of record apps | UNVERIFIED | Anecdotal only |
| Copyability and moat ratings, threat ranking, partner/acquirer views | Inference | Mine, not findings |
| Scenario revenue sizing | Assumption | Problem map assumptions, not findings |
