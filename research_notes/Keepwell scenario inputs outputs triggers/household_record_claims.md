# Household appliance record, warranty, service-plan renewal and claim help (India, as of Nov 2026)

Research stopped at the search budget (about 16 calls). Items marked UNVERIFIED have no authoritative source.

## 1. Invoice, GST invoice and warranty card contents; how warranty clocks work

### Takeaway
A GST tax invoice already carries seller GSTIN, invoice number, date, item description, HSN and tax. Model and serial numbers are often only on the product or the warranty card, so the record needs a second capture step. OEM warranty terms vary by brand and model (1 year comprehensive plus longer cover on selected parts, with invoice and authorised-service conditions), so terms should be stored per record, not assumed.

### Cited Findings
- Rule 46 CGST tax invoice must show: supplier legal name, address, GSTIN; a unique invoice number (max 16 characters) and date; recipient name, address, GSTIN/UIN (unregistered buyers: delivery address and state code at Rs 50,000 or more); HSN/SAC; description, quantity, value; taxable value, rate, CGST+SGST or IGST; place of supply for inter-state sales; signature. Secondary sources disagree on the count (16 vs 17 fields), so verify against CBIC text. — [Tally](https://tallysolutions.com/gst/gst-invoice-format-mandatory-fields-rules-and-examples-for-businesses/); [GST Council flyer](https://www.gstcouncil.gov.in/sites/default/files/e-version-gst-flyers/Tax_Invoice_and_other_new.pdf); [Invoicedataextraction](https://invoicedataextraction.com/blog/india-gst-invoice-requirements-rule-46)
- Samsung India AC terms list PCB/PBA, evaporator, condenser, fan motor and step motor as covered parts. They mention an extended 4 years on gas charging (on condenser and compressor failure) in addition to 1-year comprehensive cover. — [Samsung AC T&C](https://images.samsung.com/is/content/samsung/assets/in/tnc/ac_warranty_terms_and_conditions.pdf)
- A retailer page for Voltas says 5-year comprehensive and 10-year compressor on inverter ACs, residential use only. A Flipkart listing for a 2018 Voltas model says refrigerant gas has only 1 year. Terms vary by model and purchase date. — [Flipkart Voltas T&C](https://www.flipkart.com/pages/voltas-ac-wd-tnc); [Flipkart listing](https://www.flipkart.com/voltas-2018-model-1-5-ton-3-star-split-ac/p/itm31c5bdc17af48)
- LG: warranty limited to the first purchaser and non-transferable (a staging-site page, treat with caution). — [LG](https://wdev50.lg.com/lg5-common-gp/html/static/in/warranty.html)
- A finance blog says Samsung, LG, Voltas, Carrier, Panasonic, Blue Star, Lloyd and Godrej offer 10-year compressor warranty on select inverter splits, and that the invoice is mandatory for any claim. — [Bajaj Finserv, Apr 2026](https://www.bajajfinserv.in/best-10-year-warranty-ac-in-india)
- Exclusions seen: unauthorised-technician repairs can void extended compressor cover, and consumables (filters, remote batteries) are excluded. This is from third-party guides. — [DigiRake](https://knowledge.digirake.com/uncategorized/check-voltas-ac-warranty-online)
- Registration within 30 days is claimed by one third-party Voltas guide only (same DigiRake link). UNVERIFIED against OEM.

### Inferences
- Minimum record fields: brand, model, serial, seller name, seller GSTIN, invoice no., invoice date, amount, warranty start date, and a warranty-terms object per component (component, months, conditions such as residential-only or authorised-service-only).
- Warranty start is not always the invoice date (installation or registration date can differ for ACs). Store the start basis and let the user override it. UNVERIFIED per brand.
- The retailer-extended plan (Croma, Servify and similar) is a separate record with its own provider, plan ID, start and end.

### Gaps
- No primary OEM page confirmed the exact warranty-card layout (serial, dealer stamp, registration). Warranty-card physical contents were not verified.
- Not confirmed whether the clock starts at purchase or installation for each OEM.

## 2. Google Document AI

### Takeaway
Invoice Parser is the best fit but is built for business invoices, supports Latin-script European languages (English is included; Hindi is not listed), and has no model or serial field. Expect to add a custom extractor or an LLM pass for model, serial and warranty text. It is available in asia-south1 (Mumbai), but v2.0 is not.

### Cited Findings
- Invoice Parser fields: invoice_id, invoice_date, due_date, delivery_date, currency, net_amount, total_amount, total_tax_amount, supplier_name, supplier_address, supplier_phone, supplier_email, supplier_tax_id, supplier_registration, receiver_name/address/tax_id, line_item/description, product_code, quantity, unit_price, amount, and vat/tax_rate, vat/tax_amount. — [Processor list](https://docs.cloud.google.com/document-ai/docs/processors-list)
- Invoice Parser regions: asia-south1, asia-southeast1, australia-southeast1, eu, northamerica-northeast1, us. Version 2.0 is not available in asia-south1. Languages: German, English, Spanish, Estonian, French, Italian, Latvian, Lithuanian, Dutch, Portuguese, Romanian, Swedish. — [Processor list](https://docs.cloud.google.com/document-ai/docs/processors-list)
- Expense Parser (receipts): supplier, receipt_date, currency, total, tax and line items. Regions: asia-southeast1, australia-southeast1, eu, northamerica-northeast1, us (no asia-south1). Languages include English, not Hindi. Limit 10 pages. — [Processor list](https://docs.cloud.google.com/document-ai/docs/processors-list)
- Limits: online 40 MB and 15 pages (Invoice Parser; imageless mode 30). Batch 1 GB per file, 5,000 files per request, 200 pages for Invoice Parser. — [Limits](https://docs.cloud.google.com/document-ai/limits)
- Regional support: asia-south1 (Mumbai) is a single-region option with limited support. Custom extractor (generative, v1.5 only, no fine-tuning) and template-based custom extractors are available in asia-south1. OCR there is v2.1.1 Preview. Form Parser v1.0 to v2.1 is available. — [Regions](https://docs.cloud.google.com/document-ai/docs/regions)

### Inferences
- GSTIN would likely land in supplier_tax_id and recipient GSTIN in receiver_tax_id. The docs list the fields but do not say how Indian GSTIN is handled. UNVERIFIED; test with sample invoices.
- Model and serial need a custom extractor or Gemini-style extraction, or a user-confirmed step. Thermal-print and WhatsApp-photo invoices need a confidence threshold and a human confirm screen.

### Gaps
- No documented India-specific accuracy, no Hindi or regional-language support for the Invoice Parser, no pricing checked, no request-rate quotas retrieved.

## 3. Maintenance triggers and warranty-expiry reminders

### Takeaway
Time-based triggers are well supported for AC (before summer) and RO (6 to 12 months). Washing machine and fridge intervals have thin sourcing and should be user-configurable defaults.

### Cited Findings
- AC: at least 1 professional service a year, ideally before summer; some advise two sessions a year. Filter cleaning is suggested about every 2 weeks in peak summer. — [Hitachi tips](https://www.hitachiaircon.com/hk/en/news/air-conditioner-maintenance-general-tips); [TCL India](https://tcl.com/in/en/blog/Dont-know-what-happens-during-your-AC-maintenance-A-simple-7-point-Checklist)
- RO: pre-filters 6 to 12 months, post-carbon about yearly, membrane 2 to 4 years; vendor blogs, model-specific. — [RO Care India](https://www.rocareindia.com/blog/49/ro-water-purifier-service-schedule-maintenance-guide)
- Washing machine: only a monthly drum-clean cycle was found. No descaling interval found. — [Fatafat Service](https://fatafatservice.com/blog/appliance-care-tips-that-actually-work)

### Inferences
- Trigger types: calendar (season), usage or time since last service, warranty end minus N days, and AMC end minus N days. A suggested warranty-expiry cadence of 60/30/7 days is a design choice, not sourced.

### Gaps
- No source on fridge schedules or on warranty-expiry reminder norms among Indian providers. UNVERIFIED.

## 4. AMC / service-plan structure and price

### Takeaway
Plans split into labour-only (non-comprehensive) and comprehensive (parts included), with a fixed visit count. Reliable India price points were not found.

### Cited Findings
- Godrej AMC: for ACs older than 5 years, 1-year AMC, labour or comprehensive, 2 services a year; cooling coil and condenser covered only on the WIN-WIN (comprehensive) contract. — [Godrej](https://www.godrejenterprises.com/support/appliances/air-conditioners/amc)
- Croma ZipCare for split ACs: 2-year plans tiered by product price band (up to Rs 25,000, Rs 25-35k, Rs 70k-1 lakh); one plan includes 4 wet cleanings, 2 gas charges and labour-only breakdown support. Price is not shown in snippets. — [Croma ZipCare](https://www.croma.com/zipcare-all-in-one-for-split-air-conditioners-upto-rs-25000-2-years/p/281821)
- Single-visit AC service range Rs 500 to 1,500. — [Urban Company](https://www.urbancompany.com/articles/understanding-ac-service-charges-in-india)

### Inferences
- Plan fields: provider, type (EW/AMC; labour vs comprehensive), start/end, visits included and used, parts excluded, price, plan ID. Renewal triggers: end date, expired OEM warranty, appliance older than about 5 years (Godrej's threshold).

### Gaps
- Annual AMC prices for AC, RO, washing machine and fridge not found. UNVERIFIED.

## 5. Complaint and claim channels

### Takeaway
Escalation order is OEM toll-free or app, then NCH, then a consumer commission. The record's main output is an evidence bundle: invoice, warranty terms, a dated log of complaints and service events, and payments.

### Cited Findings
- NCH: web portal, mobile app, UMANG, WhatsApp +91 88000 01915, SMS, and toll-free 1915 (8 AM to 8 PM). INGRAM is the grievance system, integrated with WhatsApp. NCH forwards the grievance to the company and you can track status. The required fields are not listed on the page. — [consumerhelpline.gov.in](https://consumerhelpline.gov.in/)
- e-Daakhil: mandatory uploads per one guide are index, list of dates and events, memo of parties, and complaint with affidavit. Proof such as bills, receipts and payment records is expected. PDFs, up to 5 MB each (secondary sources). — [Better India](https://www.thebetterindia.com/269846/edaakhil-login-file-consumer-complaint-online-portal-rules-registration/); [Sansa Legal](https://www.sansalegal.com/post/how-to-file-a-consumer-complaint-online-through-the-e-daakhil-portal-in-india-process-documents-f)
- Fee: nil up to Rs 5 lakh under Rule 7 of the 2020 Rules (secondary source; verify). — [Citizennest](https://www.citizennest.com/guide/consumer-forum-complaint-edaakhil)
- Limitation: 2 years from cause of action (Section 69; delay condonable). District up to Rs 50 lakh, State to Rs 2 crore, National above that (2021 rules). — [Drishti](https://www.drishtiias.com/daily-updates/daily-news-analysis/consumer-protection-rules-2021); [Pioneer](https://www.dailypioneer.com/2021/india/govt-notifies-new-rules-for-consumer-commissions.html)
- One source says e-Daakhil now runs via e-Jagriti (single source). UNVERIFIED. — [righttoinformation.wiki](https://righttoinformation.wiki/edaakhil-online-consumer-commission-filing-india)

### Inferences
- The system should output a dated chronology (the list of dates and events), a party memo (buyer, seller, OEM, service centre with addresses), and an invoice PDF, with a size check.
- Legal notice: no source found on whether it is mandatory. Commonly sent before filing but not required for a consumer complaint (UNVERIFIED, my understanding only).

### Gaps
- OEM toll-free and app requirements not checked. The portal's exact form fields were not retrieved.

## 6. DPDP Act 2023 and Rules (status)

### Takeaway
Rules were notified on 14 Nov 2025 with phased commencement. The substantive duties (notice, consent, withdrawal, breach reporting) are due about 18 months later, around 12 to 14 May 2027, so at Nov 2026 they are not yet in force. Design to them now.

### Cited Findings
- Rules 1, 2 and 17 to 21 (definitions, Data Protection Board) took effect on publication. Rules 3, 5 to 16, 22 and 23 (substantive duties) are at about 18 months (about May 2027; sources vary on the exact day). Consent manager registration (Rule 4) is at 1 year per one source and later per another. Existing SPDI Rules 2011 continue meanwhile. — [SCC Online](https://www.scconline.com/blog/post/2025/12/26/digital-personal-data-protection-rules-2025-key-highlights/); [The Week](https://www.theweek.in/wire-updates/business/2025/11/14/del148-biz-dpdp-rules-ld-govt.html); [YourStory](https://yourstory.com/2025/11/digital-personal-data-protection-dpdp-rules-2025-rollout-over-18-months)

### Inferences
- I did not confirm whether any amendment or acceleration occurred between Nov 2025 and Nov 2026. UNVERIFIED; check MeitY.
- Design implications (from general DPDP principles, not retrieved here): an itemised consent notice with purpose (reminders, claim help), per-purpose withdrawal, and deletion. Household members: each person whose data appears (name, phone, address on invoices) is a data principal, so use per-member invitations and avoid showing another member's personal data. Sharing invoices with a service agency or OEM needs separate consent per disclosure.

### Gaps
- Consent notice contents, withdrawal mechanics and children's data rules were not retrieved from primary text.

## 7. Who inputs data and trust

### Cited Findings
- Warranty is typically non-transferable and limited to the first purchaser (LG page above), and Voltas extended cover is residential-use only (Flipkart T&C above). Hence tenant-versus-owner and resale cases matter.

### Inferences (no sources)
- Roles: owner (invoice and warranty), family member (add events, view), tenant (limited view, appliance may be the landlord's), service agency (adds repair events). Tag every record with source (invoice scan, OEM, agency, self-reported) and a verification state (OCR-confirmed, agency-signed, self-reported). Agency entries should be proposals the owner approves. Agency OTP or job-card ID adds trust. Keep an audit trail for claim evidence.

### Gaps
- No research on household-sharing norms or verification practice in Indian home-service platforms.
