# Claims triage and buyback/refurb/recycling triage: inputs, outputs, triggers (India first; as of Nov 2026)

Method note: about 13 tool calls. Public sources are thin on actual claim data schemas and SLAs. Most administrator pages are marketing. Anything marked [UNVERIFIED] is an inference or a vendor claim without a primary source.

## 1. What a protection/warranty claim file contains, decision outputs, SLAs, fraud signals

### Takeaway
Public Indian sources confirm only a thin core claim file: claim form, invoice, ID proof, device details and damage photos. Detailed schemas, SLAs and fraud rules are not publicly documented by Servify, OneAssist, Onsitego or Zopper, so the product team must treat the rest as design assumptions.

### Cited Findings
- OneAssist plan T&Cs (Axis Bank-linked) list claim documents as: signed claim form, invoice copy, govt ID proof, and any other evidence the insurer requires. The same T&Cs say OneAssist cancels the plan if device details or images are not supplied within 15 days of plan purchase. So the proof-of-purchase and device-image intake happens at plan activation, not only at claim time. — [Axis/OneAssist T&C PDF](https://campaign.axisbank.com/Generic/EA-Reserve-Protection-Plan-Tnc-Axis-Bank.Pdf)
- OneAssist FAQ: customer submits the claim documents plus damaged-device photos to begin the "cashless repair" process; service requests can be raised on the OneAssist app via registered mobile number. — [OneAssist FAQ (Scribd copy, unofficial)](https://www.scribd.com/document/520411264/FAQ-1); [PhonePe help page on claim documents](https://cms.phonepe.com/en/myhelp/insurance/mobile-insurance/claims/what-documents-do-i-have-submit-claim)
- Servify (marketing pages): platform covers claim adjudication and settlement, device diagnostics, logistics, repairs, buyback/financing, payment collection; TPA arm does end-to-end claim management; API integration with partner CRM, sales systems, claims portals and customer app; ecosystem of call centres, repair centres, payment gateways and logistics providers; dashboards with KPIs on sales, GMV, claims, CSAT. The page states no SLAs, no claim inputs and no fraud features. — [Servify OEM page](https://servify.com/tr/oem)
- Servify global platform page claims 65K+ onboarded locations (retailer and service partners), 50+ OEM partnerships, and "OEM integrations" that supply activation dates and service history (vendor claim, unverified). — [Servify tech platform](https://global.servify.com/tech-platform)
- Servify lists APIs and an Integration Suite, SDKs, and SOC2 Type II / GDPR compliance. There is no public API documentation. — [Servify tech platform](https://global.servify.com/tech-platform); [Servify insurers page](https://servify.com/tr/insurers/)
- Assurant has used Shift Technology AI fraud detection since 2018, including for multi-claim schemes (vendor case study). — [Shift case study](https://www.shift-technology.com/resources/case-studies/assurants-focus-on-innovation-increases-stopped-fraud)
- UK Financial Ombudsman decisions involving Assurant show real fraud-signal patterns: serial/IMEI matched claimant, but the manufacturer warranty activation date was after the reported loss date (a timeline conflict, not by itself a fraud finding); an insurer cannot decline for "false information" unless fraud is actually identified. — [DRN-5680955](https://www.financial-ombudsman.org.uk/decision/DRN-5680955.pdf) and related [DRN-5601788](https://www.financial-ombudsman.org.uk/decision/DRN-5601788.pdf) (decision-to-case mapping per search summary; not read in full)
- Industry commentary: Assurant claim forms ask for identity verification; weak ID checks let duplicate or fraudulent claims through. This is commentary, not Assurant policy. — [btw.media](https://btw.media/en/assurants-device-protection-claim-is-a-logistics-cost-disguised-as-insurance)
- One consumer post says Asurion (US/Verizon) verified only name, billing address and phone number to file a claim. It is a single anecdote, not an Asurion process. — [Verizon community post](https://community.verizon.com/t5/Verizon-Wireless-Services/Asurion-security-concerns-fraud/m-p/960266)

### Inferences
- Minimum claim-file schema to specify: policy/plan ID, customer ID and contact, product category/brand/model, serial number (IMEI for phones), invoice (date, seller, amount), plan start date, fault description (free text plus coded symptom), damage type (accidental/liquid/electrical/wear), photos/video, prior-claim history, ID proof, service address, pickup/visit preference.
- Decision outputs implied by the sources (cashless repair, plan cancellation, adjudication and settlement): approve, deny (reason code), route to repair (network partner and visit slot), replace, cash settle, request more info.
- Likely fraud/ineligibility signals for a rules engine (design assumptions, [UNVERIFIED] for Indian administrators): repeat claims on the same serial or same customer; serial or invoice mismatch; warranty or plan start date after the loss date; photo shows pre-existing damage; claim within a waiting period; document tampering.

### Gaps
- No public Indian SLA figures (visit TAT, repair TAT, settlement TAT) found for OneAssist, Onsitego or Zopper. Onsitego/Zopper claim pages did not surface in two searches. IRDAI or Consumer Protection rules on TAT for these (non-insurance) service contracts were not checked.
- No documented webhook or API payload spec from any administrator.

## 2. Administrator-to-service-network integration and repair-vs-replace inputs

### Takeaway
Integration is described only as "API integration with CRM, claims portal, customer app" plus partner portals and apps. Repair-vs-replace logic is not publicly disclosed, only discussed as a cost and logistics trade-off.

### Cited Findings
- Servify describes an integrated ecosystem of call centres, repair centres, logistics and payment gateways with real-time monitoring. — [Servify OEM page](https://servify.com/tr/oem)
- Commentary: repair becomes unprofitable if the part is expensive, the repair causes repeat visits, the location cannot handle demand, or the customer needs extra support. — [btw.media](https://btw.media/en/assurants-device-protection-claim-is-a-logistics-cost-disguised-as-insurance)

### Inferences
- Repair-vs-replace inputs to specify: product age (from invoice) and remaining warranty/plan term; diagnosed fault code and severity; estimated repair cost (parts plus labour plus visit) against current market value or plan cover limit; parts availability and ETA at the local service centre; prior repair count on the unit; technician diagnostic outcome (post-visit); policy replacement terms. A typical rule is replace or settle when repair cost exceeds a set % of value or after N failed repairs [UNVERIFIED; the threshold is a design choice].
- Suppliers and consumers: customer and retailer supply the invoice, serial and photos; OEM supplies activation date and service history; the service partner supplies diagnosis, parts and cost; the administrator adjudicates; the insurer or OEM funds it; the customer gets the outcome.

### Gaps
- No public repair/replace thresholds from any Indian provider. No Asurion or Assurant India claim-flow pages were retrieved.

## 3. Buyback/refurb grading: inputs, outputs, routes

### Takeaway
Indian buyback is quote-first with brand, model and condition questions, and refurbishers grade A/B/C after a multi-point check. Public pages do not describe photo, age or accessory inputs for large appliances, nor an explicit harvest-or-scrap route.

### Cited Findings
- Cashify AC sell flow: choose brand, model, answer condition questions, see an instant value, schedule free doorstep pickup (1,500+ cities), get payment and billing documentation. Pricing factors named are working condition (cooling, airflow, remote), cleanliness of indoor and outdoor units, small repairs, and season (summer demand). Age, photos and accessories are not mentioned on the page. — [Cashify AC sell page](https://app.cashify.in/how-to-sell-your-old-air-conditioner-online-for-instant-cash-in-india)
- Cashify also has a page on how compressor condition impacts AC buyback price. I did not read it. — [Cashify compressor page](https://app.cashify.in/how-compressor-condition-impacts-ac-buyback-price)
- Refwash (Bangalore refurbisher): grades Premium (A), Smart Choice (B), Value (C) by cosmetic wear and model age. It runs a 22-point check (the page also says "14/22", so the count is ambiguous) covering performance, electrical safety, physical condition, leaks, internal components (compressor, motor, relay, capacitor, thermostat), and cleaning. All grades get a 6-month warranty and a 50% buyback within 1 year. — [Refwash grades](https://refwash.in/refurbished-appliance-grades-a-b-c-bangalore); [Refwash buyback policy](https://refwash.in/warranty-buyback-policy)
- Costify (Delhi NCR, founded 2022, per a startup profile) sells refurbished refrigerators, ACs and washing machines at 50-70% below new (company claim). I found no Costify buyback or grading page. — [Startuppedia](https://startuppedia.in/startup-stories/sibling-duo-from-delhi-that-started-a-refurbishment-startup-for-home-appliances-raise-funding-now-clocking-rs-4-cr-annual-revenue-10894704)
- Back Market grades phones on cosmetics only (Premium, Excellent, Good, Fair), with all devices fully functional. Battery minimums are at least 90% for Premium and at least 80% for the others. Sellers must follow a quality charter, and a 25-point inspection is cited. — [Back Market Pro grading](https://pro.backmarket.com/pages/grading); [Back Market phone grades](https://backmarket.com/en-us/c/smartphones/what-are-back-market-phone-grades)

### Inferences
- Inputs to specify for a large-appliance triage: category, brand, model, year or age (invoice or label), working status (powers on, core function), symptom checklist (for an AC: cooling, compressor noise, gas leak), cosmetic photos (all sides, label plate for serial), accessories (remote, stand, hoses), location and pickup accessibility, invoice presence.
- Outputs: grade (A/B/C/scrap), price band or offer, route. Routes are refurb and resale, harvest (parts), or scrap and recycle. A route is justified only if the offer minus refurb cost is positive. The harvest and scrap routes are my inference [UNVERIFIED] and come from the EPR chain in section 4.
- Final grade is set at physical inspection after pickup, so the app quote is provisional; the re-quote is the main friction point [UNVERIFIED].

### Gaps
- Underdog: no public grading page found. No Back Market, OEM certified-refurb or Underdog large-appliance grading criteria were found (those pages are phone-centric). The Costify grading method is not public.

## 4. EPR/e-waste documents and data flowing with a unit; pickup triggers

### Takeaway
E-Waste (Management) Rules 2022 (effective 1 April 2023) require producers, refurbishers, recyclers and manufacturers to register on the CPCB portal, keep sale/transfer/storage records, and trade only with registered entities. Refurbishing certificates let producers defer EPR targets. Unit-level traceability fields are not specified in the sources I reached.

### Cited Findings
- Rule 4 requires registration of manufacturers, producers, refurbishers and recyclers on the portal. Entities must not deal with unregistered entities. Refurbisher duties (Rule 7): register, hand e-waste generated during refurbishing to a registered recycler, and upload information to the portal. — [CPCB-derived summary via ICSI article](https://www.icsi.edu/media/webmodules/CSJ/September_2025/Articles_CS_Rajiv_Malik_20.pdf); [TNPCB refurbisher SOP page](https://www.tnpcb.gov.in/eWaste.php)
- Storage is limited to 180 days, with a record of sale, transfer and storage kept available for inspection; records of e-waste collected, dismantled, recycled and sent to registered recyclers are maintained on the portal. The excerpt did not name the entity type, so verify the gazette text. — [Taxguru Rules 2022 summary](https://taxguru.in/corporate-law/e-waste-management-rules-2022-1st-april-2023.html)
- Refurbisher registration: application with company and facility details plus declarations and affidavits; CPCB can raise shortcomings within 30 working days; then physical or virtual inspection. A consultancy lists fees (Rs 15,000 new, unverified, check the portal). — [Corpseed refurbisher page](https://www.corpseed.com/service/epr-e-waste-registration-for-refurbishers)
- Refurbishing certificates are issued to registered refurbishers; producers buy them to defer part of their EPR obligation, and the deferred quantity is added to a later year's target. Recycling certificates are valid two years from the end of the generating financial year. — [Lexplosion on 2023 amendment (summary)](https://lexplosion.in/?p=137061) and [Taxguru](https://taxguru.in/?p=927356) (search-summary level; verify)
- Amendment Rules 2024 (effective 8 March 2024): the Centre may extend the filing period for returns and reports by an additional 9 months; platforms for exchanging EPR certificates, with the price band at 30% to 100% of the environmental compensation. — [Lexplosion 2024 amendment](https://lexplosion.in/e-waste-management-amendment-rules-2024-notified-includes-provisions-for-relaxing-the-period-for-filing-annual-and-quarterly-returns/)
- The 2023 second amendment covered refrigerant management by producers and the EPR certificate conversion factor. — [Corpseed summary](https://corpseed.com/knowledge-centre/e-waste-management-second-amendment-rules-2023)

### Inferences
- Data to carry with each unit to a recycler or refurbisher (derived from the record-keeping duties; the exact schema is [UNVERIFIED]): unit ID and serial, category, brand/model, weight, collection date, collector, storage start (for the 180-day clock), receiving entity registration number, outcome (refurbished, dismantled, recycled), and certificate reference.
- Pickup triggers (design view, not found in sources): replacement purchase with exchange offer; buyback acceptance; claim outcome of replace or settle (old unit returns); the unit being unrepairable; end of plan term. Whether bulk consumers or "exchange" counts for producer collection targets was not verified.

### Gaps
- Official gazette and CPCB portal field lists were not read (the TNPCB refurbisher SOP PDF returned 404). Which large-appliance categories fall under Schedule I, the 2022 EPR targets per category, and refrigerant handling for ACs and fridges were not checked.
- No source on Indian producers' (Voltas, LG, Samsung) exchange-pickup data flows.

## 5. Who supplies each input, who consumes each output, triggers (synthesis)

### Takeaway
Cross-cutting roles come from the sources above plus design inference. Suppliers are mostly the customer and retailer or OEM at intake, and service partners at diagnosis.

### Cited Findings
- OEM integrations supply activation date and service history to Servify. — [Servify tech platform](https://global.servify.com/tech-platform)
- Registered refurbishers and recyclers report on the CPCB portal and produce certificates that producers consume. — [Lexplosion](https://lexplosion.in/?p=137061)

### Inferences
- Claims: supplier is the customer (fault, photos), retailer or OEM (invoice, serial, activation), service partner (diagnosis, quote). Consumers are the administrator's adjudicator, insurer or OEM (funding) and the customer (outcome). Triggers: fault raised, tech diagnosis complete, repair failure, parts delay.
- Buyback/EPR: supplier is the customer (condition, photos, invoice), the platform (quote) and the inspector (final grade). Consumers are the refurbisher (stock), the recycler (scrap) and the producer (certificates for CPCB returns). Triggers: replacement purchase, exchange offer, claim write-off, end of life.

### Gaps
- No single public source ties the claim outcome to e-waste routing. That linkage would be the product's novel integration point.
