# Google non-LLM products and APIs for an Indian appliance-repair product (doc/vision, maps, search, data, channels, payments) — as of Nov 2026

Method: ~25 tool calls. Fetch tool summarises pages, so figures need a re-check on live pages. Tags: 🟢 official page fetched this session; 🟡 secondary/trade press; 🔴 unverified (training knowledge or not found). DEAD = shut down; WARN = deprecated or closing. Overlap with google_architecture_options.md (Document AI processor/region facts, Chirp) is only summarised.

## 1. Document, vision and on-device ML: what is usable in India?

### Takeaway
Document AI OCR (Indian languages) and Custom Extractor run in asia-south1; Invoice Parser is English-only; Layout Parser is not in Mumbai. For serial/model labels, ML Kit text recognition (Latin, Devanagari only) and barcode scanning on-device are the cheapest path. Vertex AI Vision is DEAD (EOL 30 Sep 2026).

### Cited Findings
| Product | What it does | Status | India | Pricing | Limits | Fit |
|---|---|---|---|---|---|---|
| Document AI Enterprise OCR | Text/layout from scans | GA | asia-south1; Bangla, Gujarati, Hindi, Kannada, Malayalam, Marathi, Nepali, Punjabi, Tamil, Telugu 🟢 [list](https://docs.cloud.google.com/document-ai/docs/processors-list) | $1.50/1k pages (1-5M), $0.60/1k after 🟡 [activepieces quoting official](https://www.activepieces.com/blog/google-document-ai-pricing-cost-per-page-2026-guide) | Not fetched | Bills, warranty cards, handwritten job sheets |
| Invoice Parser | Structured invoice fields | GA, v1.3 only in asia-south1 | asia-south1, no Indian-language support 🟢 [list](https://docs.cloud.google.com/document-ai/docs/processors-list) | $0.10 per 10 pages of a doc 🟡 (per-10-page block rounding claimed by third party) | - | Spare-part/dealer invoices (English only) |
| Custom Extractor | Train fields on own docs | GA, asia-south1; Hindi/Marathi/Nepali/Sanskrit; generative extraction English-only, not in asia-south1 🟢 | as left | Not retrieved (pricing page truncated) | - | Warranty card / job card fields |
| Layout Parser | Chunking for RAG | Not in asia-south1 🟢 | No in-region | $10/1k pages 🟡 | - | Manuals ingestion only if residency not needed |
| Expense Parser | Receipts | Not in asia-south1 🟢 | No | not retrieved | - | Skip |
| Cloud Vision API (OCR, labels, objects) | Per-image detection | GA 🔴 | Global API 🔴 | Pricing page fetch truncated; commonly ~1,000 free units/month then per-1k 🔴 | - | Cheap generic OCR; Gemini vision usually better for appliance photos |
| Video Intelligence API | Video labels/shots | Status not confirmed 🔴 | 🔴 | 🔴 | - | Low fit; use Gemini video input |
| Vertex AI Vision | Video analytics | DEAD: deprecated 15 Jun 2026, EOL 30 Sep 2026 🟡 (single mirror of official deprecations page; verify) [deprecations](https://docs.cloud.google.com/vertex-ai/docs/deprecations) | - | - | - | Do not use |
| Gemini image understanding | Model-plate/fault photo reading | GA (see sibling note) | asia-south1 limited | Token-based | - | Primary vision path (covered in google_architecture_options.md) |
| ML Kit text recognition v2 | On-device OCR | Not stated; scripts: Latin, Devanagari, Chinese, Japanese, Korean 🟢 [doc](https://developers.google.com/ml-kit/vision/text-recognition/v2) | Works offline; no Tamil/Telugu/etc. script | Free 🔴 | Android API 23+ 🟢 [guides](https://developers.google.com/ml-kit/guides) | Model/serial plates (mostly Latin) |
| ML Kit barcode scanning | On-device 1D/2D decode | Listed in ML Kit; stage not stated 🟢 | Offline | Free 🔴 | Formats list not fetched | Serial/QR/IMEI-style labels |
| ML Kit Document Scanner | Scan UI, crop, deskew via Play services | Stage not stated; Android only; whole flow on-device; modes BASE/BASE_WITH_FILTER/FULL; page cap setting 🟢 [doc](https://developers.google.com/ml-kit/vision/doc-scanner) | Offline | Free 🔴 | - | Invoice/warranty capture |
| ML Kit GenAI APIs (image description, proofreading, rewriting, summarisation) | On-device Gemini Nano | Beta; Prompt API Alpha 🟢 [guides](https://developers.google.com/ml-kit/guides) | Device-dependent 🔴 | Free 🔴 | Supported-device list not fetched | Optional offline helper; not core |
| Firebase AI Logic | Client SDK for Gemini with App Check, per-user rate limits, hybrid on-device fallback | Stage not stated 🟢 [doc](https://firebase.google.com/docs/ai-logic) | Region/India not stated | Free tier for Gemini Developer API; paid via Blaze 🟢 (details not shown) | - | Direct-from-app AI without own backend |
| Google Lens / Circle to Search | Consumer visual search | Consumer features, no API 🔴 | - | - | - | Relevance: user discovery only; not integrable |

### Inferences
- Pipeline: ML Kit barcode + text on-device for label capture; Document Scanner for paper; Document AI OCR (Mumbai) or Gemini for server-side. Use Custom Extractor only if Hindi/Marathi docs matter.
- ML Kit has no Tamil/Telugu/Kannada script OCR; those need Document AI OCR or Gemini.

### Gaps
- Cloud Vision, Video Intelligence, Document AI Custom Extractor pricing; ML Kit barcode formats and bundled vs unbundled size; Translate API status (not searched, 🔴: Cloud Translation basic/advanced GA, Indian languages supported, ~500k chars/month free).

## 2. Maps Platform: Routes, Route Optimization, Places, address quality

### Takeaway
India has its own, cheaper price list with higher free caps (70k/month for Essentials SKUs). Route Optimization is per-shipment billed, with a 1-vehicle SKU (Pro) and 2+ vehicle SKU (Enterprise), so 2-10 technicians fits Fleet Routing cheaply. Address Validation lists IN but quality caveat applies.

### Cited Findings
| Product | Status | India price (USD/1k, 0-5M) and free cap | Global free cap and price | Notes |
|---|---|---|---|---|
| Routes: Compute Routes Essentials | GA 🔴 (status not stated) | $1.50; 70k free 🟢 [India](https://developers.google.com/maps/billing-and-pricing/pricing-india) | $5.00; 10k free 🟢 [global](https://developers.google.com/maps/billing-and-pricing/pricing) | Traffic-aware = Pro $3.00/35k free India |
| Compute Route Matrix | - | Not listed in India fetch; global Essentials $5.00/10k free 🟢 | | Distance Matrix charged per element 🟢 |
| Route Optimization Single Vehicle (Pro) | Not stated (page lists no GA label) 🟢 | $0.80 per shipment; 35k free 🟢 | $10.00; 5k free 🟢 | Request with 1 vehicle |
| Route Optimization Fleet Routing (Enterprise) | as above | $2.40 per shipment; 7k free 🟢 | $30.00; 1k free 🟢 | 2+ vehicles; per shipment count x unit price 🟢 [billing](https://developers.google.com/maps/documentation/route-optimization/usage-and-billing) |
| Places API (New) Autocomplete | - | $0.85; 70k free; session usage unlimited 🟢 | $2.83; 10k free | |
| Place Details Essentials | - | $1.50; 70k free; IDs-only free 🟢 | $5.00 | Pro $17 global (India Pro not fetched) |
| Text/Nearby Search Pro/Enterprise | - | India not fetched | $32 / $35; 5k / 1k free 🟢 | Agency discovery use |
| Geocoding | - | $1.50; 70k free 🟢 | $5.00; 10k free | |
| Address Validation | India (IN) listed as supported incl. residential/commercial metadata 🟢 [coverage](https://developers.google.com/maps/documentation/address-validation/coverage); GA-vs-preview for IN unclear | Pro $5.10, 35k free; Enterprise $7.50, 7k free 🟢 | Pro $17 / Ent $25 | "Data quality can vary by country" 🟢 |
| Navigation SDK | - | not fetched | $25 per request (Enterprise), 1k free 🟢 | Overkill for tiny agencies |
| Fleet Engine | - | not found | Pricing absent from the pricing page 🟢 | Likely heavy; skip for 2-10 techs 🔴 |
| Maps Grounding (Gemini) | stored 30 days, no opt-out 🟢 [governance](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/data-governance) | pricing 🔴 | | Not for residency-sensitive data |

- Route Optimization limits: Optimize Tours 60 QPM, Batch 60 QPM, up to 100 requests/100 MB per batch; no daily cap; max shipments/vehicles per request not stated 🟢 [billing](https://developers.google.com/maps/documentation/route-optimization/usage-and-billing). Needs OAuth and billing on project.
- Fetch tool said India pricing page shows USD only; INR pricing not found 🟢.
- Indian address quality: no official benchmark found; informal knowledge that unstructured Indian addresses geocode coarsely 🔴.

### Inferences
- A 5-technician agency with ~30 jobs/day = ~900 shipments/month, inside India Fleet Routing free cap (7k). Route Optimization is affordable; the real constraint is OAuth/service-account integration and request shaping, not cost.
- Use Autocomplete (session) + Place Details IDs-only + customer pin drop to fix weak address quality.

### Gaps
- Max shipments per request; GA status of Route Optimization; Fleet Engine pricing; India Text Search/Place Details Pro price; address-validation accuracy in India.

## 3. Business discovery, reviews, search, trends, YouTube

### Takeaway
Business Profile APIs need an access request and are not open to all. Programmable Search JSON API is closed to new customers and ends 1 Jan 2027, so do not build on it. YouTube search.list defaults to only 100 calls/day.

### Cited Findings
| Product | Status | India | Pricing/limits | Fit |
|---|---|---|---|---|
| Business Profile APIs (locations, reviews via APIs) | Access by request: Google account, Cloud project, valid website, business reason; "not available to all users" 🟢 [overview](https://developers.google.com/my-business/content/overview) | Not country-restricted in text | Rate limits on separate page (not fetched) | Agency owner-side review reply/reputation if agency consents |
| Local Services Ads / Google Business Profile "Local Services" in India | Not found 🔴 | - | - | Do not assume availability |
| Programmable Search / Custom Search JSON API | WARN: closed to new customers; discontinued 1 Jan 2027 🟡 [Brave](https://brave.com/learn/google-api-shutdown/), [Firecrawl](https://www.firecrawl.dev/blog/google-search-json-api-alternative); successor Vertex AI Search covers up to 50 domains, not full web 🟡 | - | - | Avoid |
| Gemini Google Search grounding | GA; pricing in sibling note (5k free/month, then $14 per 1k) | stores derived queries 3 days 🟢 [governance](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/data-governance) | | Fair-price / market checks |
| YouTube Data API v3 | GA | Global | 10,000 units/day default; search.list 1 unit per call with 100 calls/day bucket per the fetched page; videos.list 1 unit 🟢 [quota](https://developers.google.com/youtube/v3/determine_quota_cost). Licensing: API Services Terms not covered by fetched page, caution: do not store/re-host video content 🔴 | Link to repair videos, do not copy |
| Google Trends | Official API was alpha/limited 🔴 | - | - | Use trends.google.com manually or BigQuery public dataset |
| BigQuery public datasets / Looker Studio | GA 🔴 (not fetched) | BigQuery has Mumbai/Delhi regions 🔴 | Free 1 TB queries/month, 10 GB storage 🔴 | Analytics, agency dashboards |
| Google Earth Engine | Not relevant | - | - | Skip |
| Google Cloud Marketplace | GA 🔴 | - | - | Later distribution channel only |

### Inferences
- Reputation data for agencies is mostly via Business Profile API (needs approval) or Places Details reviews (Enterprise SKU, display-only caches restrictions 🔴).

### Gaps
- Business Profile usage limits; Local Services in India; Trends API current state; Marketplace India listing rules.

## 4. Messaging channels: RCS, Business Messages, WhatsApp equivalent

### Takeaway
Google Business Messages is DEAD (31 Jul 2024). RCS Business Messaging is reviving in India through carriers (Airtel+Google announced 1 Mar 2026; Jio, Vi), billed per message via aggregators, not a free WhatsApp replacement. WhatsApp has no direct Google equivalent.

### Cited Findings
| Product | Status | Detail |
|---|---|---|
| Google Business Messages (Maps/Search chat) | DEAD | Customers could not start chats after 15 Jul 2024; service discontinued 31 Jul 2024; call history removed too 🟢 [Google notice](https://developers.google.com/business-communications/business-messages/resources/release-notes/update-on-gbm), 🟡 [9to5Google](https://9to5google.com/2024/05/28/google-business-messages-shutting-down/) |
| Business Profile chat/call history | DEAD | Same dates 🟡 |
| RCS Business Messaging (RBM) India | Paused by Google in May-Jun 2022 over spam 🟡 [Android Authority](https://androidauthority.com/google-rcs-ads-india-3170852); now returning: Airtel-Google carrier-backed RCS with AI spam filtering announced 1 Mar 2026 🟡 [TelecomTalk](https://telecomtalk.info/airtel-google-carrier-backed-rcs-messaging-india/1004767/); Airtel to use Tanla for enterprise RCS (Jun 2026) 🟡; Jio commercial RCS for iPhone Sept 2026 with rates ~Rs 0.27-0.30 marketing, Rs 0.25 transactional, Rs 0.11-0.16 OTP from 1 Sep 2026 🟡 [MEF](https://mobileecosystemforum.com/2026/09/14/jio-bring-rcs-business-messaging-to-iphones-in-india/); Vi has RBM with Google RCS/Dotgo 🟡 |
| Access path | Via Google-approved RBM partners/aggregators, TRAI DLT registration claimed by vendor blog 🟡 (no primary source) |

### Inferences
- Do not plan a Google-based WhatsApp substitute. Use WhatsApp Cloud API as primary; RCS only as a later low-priority channel; FCM push in own app as free in-app channel.

### Gaps
- Direct RBM agent onboarding for a startup in India; carrier coverage/reach; current device penetration (vendor figures 500-800M, unverified).

## 5. Payments and wallet: Google Pay UPI, Google Wallet

### Takeaway
Google Pay API for India (UPI intents) needs Google Pay & Wallet Console registration, approved business profile and a verified UPI ID (VPA) from a bank/PSP; omnichannel and payment-status APIs need allowlisting and bank APIs. For a software company collecting for agencies, Google's payment aggregator onboarding policy (KYC) applies, so a PA/PG partner (Razorpay etc., 🔴) is more realistic.

### Cited Findings
- Console path: register on Google Pay & Wallet Console, set India, get business profile approved, then enter and verify UPI ID on Integrations page; VPA comes from bank/PSP 🟢 [setup](https://developers.google.com/pay/india/api/merchant-sdk/guides/setup), search result summary.
- Omnichannel API requires Google Pay for Business registration, email allowlisting via Google rep, UPI-verified merchant, bank APIs for payment status 🟢 [prereqs](https://developers.google.com/pay/india/api/otherapis/omnichannel/prerequisites).
- Web integration begins after Google Pay business-development confirmation 🟢 [web](https://developers.google.com/pay/india/api/web/getting-started).
- Google India Digital Services acts as Payment Aggregator; policy covers KYC, security assessment, periodic refresh, and right to reject 🟢 [policy](https://pay.google.com/intl/en_in/about/business/policy/merchant-on-boarding/).
- Google Pay for Business requires India-based merchant, MCC, business name/address/phone 🟢 [support](https://support.google.com/googlepay/businessconsole/answer/10945206).
- Google Wallet API: generic passes need issuer account (demo mode first, then publishing access) 🟢 [onboarding](https://developers.google.com/wallet/generic/getting-started/issuer-onboarding). India page found covers only bank card tokenisation for GPay India (NDA, TSP) 🟢 [India issuers](https://developers.google.com/pay-wallet/solutions/issuers/overview/region_specific/india). Availability of generic passes to Indian users: not found.
- Transaction fees: UPI MDR zero by regulation for P2M 🔴 (not verified).

### Inferences
- Wallet warranty pass is a nice-to-have; verify India availability before promising it. QR/PDF/WhatsApp warranty card is safer.

### Gaps
- Exact timeline/approval for software company merchant; whether SaaS can onboard sub-merchants without PA licence; Google Wallet India generic pass support.

## 6. Workspace, Firebase, web/Android platform

### Takeaway
Firebase phone OTP works in India but SMS costs about $0.07 each (Blaze required; first 10/day free) and caps at 3,000/day, so local DLT SMS or WhatsApp OTP may be cheaper. Workspace APIs are viable as back office for tiny agencies.

### Cited Findings
| Product | Status | India-specific facts | Pricing/limits |
|---|---|---|---|
| Firebase Auth phone OTP | GA | Pricing India $0.07/SMS 🟡 [Logto](https://blog.logto.io/firebase-authentication-pricing) (snapshot varies; one snapshot $0.06) | SMS needs Blaze; 3,000 SMS/day, 900/min, 50/min and 500/h per IP, 150 verification requests per IP/h; Identity Platform raises limits 🟢 [limits](https://firebase.google.com/docs/auth/limits); first 10 SMS/day free 🟡 |
| Firebase Phone Number Verification | SMS-free via carrier; few carriers supported 🟡 | India support unknown 🔴 | billed separately |
| Firestore, Cloud Functions, FCM, Remote Config, Crashlytics, App Check | GA 🔴 not fetched | Firestore regions include Mumbai/Delhi 🔴 | FCM free 🔴; others pay-as-you-go 🔴 |
| Firebase AI Logic | see table 1 | | |
| Android Credential Manager | GA 🔴 | | free |
| PWA (Chrome) | Open standard 🔴 | Works for low-end Android, no Play install | free |
| Google Translate (Cloud Translation) | GA 🔴 | Indian languages supported 🔴 | free monthly chars then per-char 🔴 |
| Calendar/Sheets/Drive/Gmail APIs | GA 🔴 | Global | Free quotas, per-minute limits 🔴; restricted scopes (Gmail/Drive) need OAuth verification, possible security assessment 🔴 |
| Google Forms API | GA 🔴 | | free |

### Inferences
- Phone OTP cost at $0.07 dominates early; negotiate via Identity Platform or use WhatsApp/ local SMS gateway with DLT. Use Calendar + Sheets as optional sync for tiny agencies; avoid restricted scopes where possible.

### Gaps
- Official current prices for Firebase services; Android on-device Gemini Nano device coverage in India; Credential Manager and App Check specifics.

## Which have a valid India offering (summary)
- Yes, in-region: Document AI OCR/Custom Extractor/Invoice Parser (asia-south1); Maps Platform with India price list; ML Kit (on-device); Firebase Auth phone; Google Pay India APIs (with onboarding).
- Weak/unclear: Address Validation quality; Wallet generic pass; Route Optimization GA label; Business Profile APIs (access-gated).
- Dead/closing: Google Business Messages (31 Jul 2024), Vertex AI Vision (EOL 30 Sep 2026, single source), Custom Search JSON API (ends 1 Jan 2027), Document AI Layout/Expense not in Mumbai.
