# Keepwell cost and token economics (India, as of 15 Nov 2026)

Labels: 🟢 sourced from an official page I fetched; 🟡 secondary (blog, aggregator, search snippet); 🔴 my assumption or calculation. FX used: 1 USD = Rs 94 🟡 (mid-market 93.7 to 94.9 in the first half of Nov 2026, [HDFC Sky](https://hdfcsky.com/news/rupee-falls-10-paise-to-close-at-94-86-against-us-dollar), [CurrencyBeacon](https://currencybeacon.com/rates/USD/INR)). All Gemini prices are USD per 1M tokens, public Gemini API (AI Studio) page. Existing notes are not repeated (residency, Mumbai model list, Document AI).

## 1. Gemini API and Vertex AI prices

### Takeaway
Flash-class prices double on 1 Jan 2027 (3.8 and 3.6 Flash: $0.75/$3.75 to $1.50/$7.50) but Flash-Lite 3.5 and 3.1 do not change. Flash-Lite is 2.5x (now) to 5x (2027) cheaper per input token and 1.5x to 3x cheaper per output token. Vertex AI prices could not be fetched (page returned only a title), so Vertex = assumed equal to the Gemini API with a check needed.

### Cited Findings
Standard tier, USD per 1M tokens (output includes thinking tokens). Source for all rows: [Gemini API pricing](https://aistudio.google.com/docs/pricing) 🟢 (ai.google.dev/gemini-api/docs/pricing 301-redirects here).

| Model | Input (text/image/video) | Input audio | Output incl. thinking | Cache read | Cache storage per 1M tok-hr | Batch/Flex (50%) in / out |
|---|---|---|---|---|---|---|
| gemini-3.8-flash and gemini-3.6-flash (through 31 Dec 2026) | 0.75 | 0.75 (same row) | 3.75 | 0.075 | 0.50 | 0.375 / 1.875 |
| same, from 1 Jan 2027 | 1.50 | 1.50 | 7.50 | 0.15 | 1.00 | 0.75 / 3.75 |
| gemini-3.5-flash-lite (no 2027 change listed) | 0.30 | 0.30 | 2.50 | 0.03 | 1.00 | 0.15 / 1.25 |
| gemini-3.1-flash-lite (no 2027 change) | 0.25 | 0.50 | 1.50 | 0.025 (audio 0.05) | 1.00 (Batch 0.50) | 0.125 / 0.75 |
| gemini-3-flash-preview (legacy) | 0.50 | 1.00 | 3.00 | 0.05 | 1.00 | 0.25 / 1.50 |
| gemini-3.1-pro-preview (<=200k / >200k) | 2.00 / 4.00 | same | 12 / 18 | 0.20 / 0.40 | 4.50 | 1.00 / 6.00 (<=200k) |
| gemini-4-hydrogen | 1.50 | | 7.50 | 0.075 | not listed | 0.75 / 3.75 |
| gemini-4-carbon, gemini-4-argon | 2.00 to 4.00 on 1 Dec 2026 | | 10 to 20 on 1 Dec 2026 | 0.10 to 0.20 | not listed | half |

- Priority tier costs 1.8x Standard (3.8 Flash: $1.35 / $6.75 now). Flex tier = Batch price. 🟢
- Thinking tokens are billed as output at the output rate (stated in the column header on the page). 🟢
- Grounding with Google Search / Maps: 5,000 free requests per month, then $14 per 1,000. PDFs (documents) are billed at the image token rate. 🟢
- Embeddings on the Gemini API: gemini-embedding-001 $0.15/1M text; gemini-embedding-2 $0.20 text / $0.45 image, batch half. 🟢 Same page.
- Gemini 3.5 Transcribe (gemini-3.5-transcribe): $2.00/1M audio in and $12.00/1M out, page estimates $0.003/min in plus $0.002/min out, about $0.005/min blended. 🟢 estimate shown on page. No batch/cache.
- text-embedding-005 on Vertex: aggregators show $0.000025 per 1,000 characters online, $0.00002 batch; other aggregators show $0.03 to $0.10 per 1M tokens. Units conflict. 🟡 [cloudprice](https://cloudprice.net/models/text-embedding-005), [Costbench](https://www.costbench.com/software/embedding-apis/vertex-ai-embeddings/). Practical impact: negligible (a 500-token query = well under Rs 0.01 either way).
- Vertex AI pricing page ([cloud.google.com/vertex-ai/generative-ai/pricing](https://cloud.google.com/vertex-ai/generative-ai/pricing), now titled "Agent Platform Pricing"): not retrievable. Gemini API page itself says "Enterprise Agent Platform prices may differ". 🟢 for the caveat, number gap.

Model-name conflict: the AI Studio models page lists gemini-3.8-flash, 3.6-flash, 3.5-flash-lite, 3.1-flash-lite; the Vertex data residency page (per existing notes) lists gemini-3.5-flash and 3.5-flash-lite for Mumbai. The pricing page has no "gemini-3.5-flash" row at all, so the Mumbai in-region Flash model has no confirmed price. 🟢 conflict, price for Vertex 3.5 Flash: unknown. Use 3.6/3.8 Flash price as proxy 🔴.

### Inferences
- Budget on the 2027 price. The Flash-Lite rows give the 2027 hedge. 🔴
- Cache storage is not free: 4,000 cached tokens held 1 hour on 3.8 Flash cost $0.002 (Rs 0.19) now, Rs 0.38 in 2027. Read saving per hit on those 4,000 tokens is 0.9 x $0.75 x 4k/1M = $0.0027 (Rs 0.25) now. Explicit caching therefore pays only with roughly more than 1 hit per hour per cached prefix (more than 2 in 2027). Pilot volume may not clear it. 🔴
- Existing notes say tenant-prompt caching defaults off for privacy; only the static system prompt, skills and RAG manual should be cached. 🔴

### Gaps
- Official Vertex AI per-token prices, Vertex batch availability in asia-south1, and implicit-caching discount terms: not verified.
- Whether there is any India-region price uplift on Vertex: not found.

## 2. Speech-to-text and token counts

### Takeaway
Gemini audio input at 32 tokens/second is about 10x cheaper than Chirp 3 ($0.016/min) for the same clip, and transcribe-then-extract can be a single Flash call. Chirp is also us/eu only per existing notes.

### Cited Findings
- Gemini audio: 32 tokens per second (1,920 per minute), audio downsampled to 16 Kbps, multi-channel merged, up to 9.5 hours per prompt. 🟢 [Audio docs](https://aistudio.google.com/docs/audio)
- Cost of a 60 s voice note on gemini 3.8 Flash: 1,920 x $0.75/1M = $0.00144 = Rs 0.135 (2027: Rs 0.27); Flash-Lite 3.5: Rs 0.054. 🔴 calc.
- Chirp 3 / V2 standard: $0.016 per minute for the first 500,000 minutes per month, then $0.010 and $0.008; Dynamic Batch $0.003 per minute (one blog says $0.004). Search summary of Google's page. 🟡 [Speech-to-Text pricing](https://cloud.google.com/speech-to-text/pricing/) (page fetch returned only a title; figure from search snippet quoting it); OpenRouter lists Chirp 3 at $0.016/min, released 5 May 2026. 🟡 [OpenRouter](https://openrouter.ai/google/chirp-3)
- 60 s on Chirp 3 = $0.016 = Rs 1.50 (Dynamic Batch Rs 0.28). 🔴 calc. 60 s on Gemini 3.5 Transcribe = about $0.005 = Rs 0.47. 🟢/🔴
- Image tokens, Gemini 3 models, by media_resolution: unspecified (default) 1,120; low 280; medium 560; high 1,120; ultra_high 2,240 (per-item). PDF: 560 default, 280/560/1,120 plus native text. 🟢 [Media resolution](https://aistudio.google.com/docs/media-resolution)
- Older tiling rule (images <=384 px per side = 258 tokens; larger images tiled 768x768 at 258 tokens each; 960x540 = about 1,548) is on the image-understanding page and likely applies to 2.x models. 🟢 [Image understanding](https://aistudio.google.com/docs/image-understanding) (page does not say which models; conflicts with 1,120 default for Gemini 3).
- Typical Keepwell sizes 🔴 (mapping my assumption onto the sourced rates): label/nameplate photo = 1,120 (default) or 560 (medium); invoice photo = 1,120 default, 2,240 ultra_high only if text is tiny; a 2-page PDF invoice = about 1,120 at default.

### Gaps
- Token counts for real invoice/label photos not measured; need countTokens on 10 sample images. Chirp 3 billing increment not confirmed.

## 3. WhatsApp Business Platform India (INR)

### Takeaway
Utility, authentication and service messages cost about Rs 0.115 each, marketing Rs 0.8631, all ex-GST, but sources conflict on whether utility-in-window and service charges apply to India from 1 Oct 2026. Message fees are small next to AI cost per job.

### Cited Findings
- Meta page: marketing rate for India increased 1 Jan 2026; India INR billing from 1 Jan 2026, all accounts must migrate to INR by 31 Dec 2026; non-INR accounts of eligible customers stop delivering from 1 Jan 2027; authentication-international increased 1 Apr 2026. 🟢 [Meta pricing](https://developers.facebook.com/docs/whatsapp/pricing)
- Meta page: utility sent in an open customer service window was free since 1 Jul 2025, charged from 1 Oct 2026; service messages: 1,000 free delivered per business phone number per month, charged from the 1,001st; free entry-point window (Click-to-WhatsApp ad) up to 7 days (another source says 72 hours). 🟢 [Meta pricing md](https://developers.facebook.com/documentation/business-messaging/whatsapp/pricing.md). Page quotes no INR figures (they are in a linked CSV/PDF I could not open) and does not say whether the Oct 2026 change applies to India (India not in that month's rate change table).
- INR list rates: marketing Rs 0.8631 (up from Rs 0.7846, +10%), utility Rs 0.1150, authentication Rs 0.1150, authentication-international Rs 2.4971 (above eligibility threshold), service Rs 0.1150 after 1,000 free. Excl. 18% GST, which applies to the BSP invoice. 🟡 [InstantDM](https://instantdm.com/blog/whatsapp-business-api-pricing-2026-india-october-update); marketing/utility/auth match [Free Press Journal](https://www.freepressjournal.in/tech/how-much-does-india-have-to-pay-for-whatsapp-messages-from-october-1) 🟡 and [MSG91](https://msg91.com/guide/whatsapp-business-pricing-update) 🟡.
- BSP markups: AiSensy marketing Rs 1.09 / utility Rs 0.145; Interakt Rs 0.871 / 0.150; Wati Rs 1.0357 / 0.1495; Gupshup Meta + about $0.001. 🟡 InstantDM.
- Utility/auth volume tiers up to 24%; marketing not tiered. 🟡 [ChatMaxima](https://chatmaxima.com/whatsapp-api-pricing/india/)

Conflicts: (a) one search summary says service messages are free and utility is free in window "until" 1 Oct 2026 and chargeable after; InstantDM says Rs 0.115 for both from 1 Oct; Meta's page says charged but silent on India rate. Treat as chargeable (conservative). (b) Whether USD-billed WABAs can convert to INR: sources conflict, verify with BSP. (c) Free window 7 days vs 72 hours.

### Inferences
- Model: first 1,000 service messages/number/month free, so customer-initiated replies are near zero at pilot volume; templates sent outside the window (reminders, approvals) are utility at Rs 0.115 (Rs 0.12 to 0.18 with BSP markup/GST). Never use marketing for repair updates (7.5x). 🔴
- Cost in budget below: Rs 0.115 per utility template, 3 to 8 per job.

### Gaps
- Official INR rate card not opened. Whether conversational replies inside the window cost Rs 0.115 for India: unresolved.

## 4. Other per-job costs

### Takeaway
Infra is about Rs 0.2 per job at pilot scale. Maps Routes is the only non-trivial one (Rs 0.14 to 0.28 per call, 35k to 70k free per month). SMS fallback Rs 0.10 to 0.30.

### Cited Findings
- Maps Routes Compute Routes (India SKUs, USD per 1,000): Essentials $1.50 (free cap 70,000/month), Pro $3.00 (35,000 free), Enterprise $4.50 (7,000 free); above 5M events $0.38 / $0.75 / $1.14. 🟢 [Maps India pricing](https://developers.google.com/maps/billing-and-pricing/pricing-india) = Rs 0.14 / 0.28 / 0.42 per call; free at pilot volume.
- Cloud Run: Mumbai asia-south1 is Tier 2; snippet shows about $0.0000216 per vCPU-s (instance-billed), $0.0000024 per GiB-s, $0.0000336 per vCPU-s request-billed, $0.40 per 1M requests (probably tier 1); free 180k vCPU-s, 360k GiB-s, 2M requests per month. 🟡 [Cloud Run pricing search results](https://cloud.google.com/run/pricing). A job = about 20 requests of 0.5 s at 1 vCPU, 512 MiB = about $0.0004 = Rs 0.04; mostly within free tier. 🔴
- SMS fallback India: about Rs 0.10 to 0.30 per transactional SMS plus a few paise DLT scrubbing and 18% GST. 🟡 [Message Central](https://www.messagecentral.com/blog/a2p-sms-pricing-india), [RichAutomate](https://richautomate.in/blog/sms-api-pricing-india-2026)
- Cloud SQL Postgres: not researched (no source). Planning figure: smallest shared-core instance about Rs 1,000 to 2,000 per month fixed, 🔴 assumption; at 2,000 jobs/month = Rs 0.5 to 1 per job, at 20,000 = Rs 0.05 to 0.10. I used Rs 0.10.
- Cloud Storage: not researched. 5 MB of photos per job at about $0.02/GB-month is under Rs 0.01. 🔴 Used Rs 0.03 with ops/egress buffer.

### Gaps
- Cloud SQL and Cloud Storage prices for asia-south1 not fetched; Cloud Run asia-south1 exact rates unconfirmed.

## 5. Worked per-job cost model (INR)

Assumptions 🔴 (all token counts are mine; calibrate in the pilot). Text-in includes system prompt, skills, RAG chunks, history. "Cacheable" = static prefix (system prompt + skills + manual chunk set) assumed to hit at read price with storage amortized (hot prefix, many jobs per hour). Output includes thinking. Audio = 32 tok/s, image = 1,120 tokens each (default).

| Profile | Calls | Text in (cacheable) | Audio in | Image in | Output | WhatsApp utility msgs | Maps calls |
|---|---|---|---|---|---|---|---|
| 1 Simple fix | 5 | 9,000 (4,000) | 1,440 (45 s) | 1,120 (1 photo) | 2,500 | 4 | 0 |
| 2 Parts-needed fix | 7 | 16,000 (7,000) | 1,920 (60 s) | 2,240 (2) | 4,500 | 6 | 1 (Pro, Rs 0.28) |
| 3 Warranty claim | 9 | 24,000 (10,000) | 1,920 | 5,600 (invoice + label + 3 fault) | 6,000 | 8 | 0 |
| 4 Admin claim triage | 4 | 30,000 (12,000) | 0 | 3,360 | 5,000 | 3 | 0 |

Non-AI cost per job = WhatsApp (msgs x Rs 0.115) + Maps + Cloud Run Rs 0.05 + Postgres Rs 0.10 + storage Rs 0.03: P1 Rs 0.64, P2 Rs 1.15, P3 Rs 1.10, P4 Rs 0.53. No SMS fallback included (add Rs 0.2 per SMS).

AI cost per job (Rs, Gemini only, Flash = 3.8/3.6 Flash, Lite = 3.5 Flash-Lite; Lite also processes audio and images at $0.30):

| Profile | Flash 2026 no cache | Flash 2026 cached | Flash 2027 no cache | Flash 2027 cached | Lite no cache | Lite cached | Flash 2026 cached + Batch (async only) |
|---|---|---|---|---|---|---|---|
| 1 Simple fix | 1.70 | 1.44 | 3.39 | 2.88 | 0.91 | 0.81 | 0.72 |
| 2 Parts-needed | 3.01 | 2.56 | 6.02 | 5.13 | 1.63 | 1.45 | 1.28 |
| 3 Warranty claim | 4.34 | 3.70 | 8.67 | 7.41 | 2.30 | 2.05 | 1.85 |
| 4 Admin triage | 4.11 | 3.35 | 8.23 | 6.71 | 2.12 | 1.81 | 1.68 |

Total cost per job (AI + non-AI), Rs:

| Profile | Flash 2026 | Flash 2027 | Flash 2027 cached | Lite cached |
|---|---|---|---|---|
| 1 | 2.34 | 4.03 | 3.52 | 1.45 |
| 2 | 4.16 | 7.17 | 6.28 | 2.60 |
| 3 | 5.44 | 9.77 | 8.51 | 3.15 |
| 4 | 4.64 | 8.76 | 7.24 | 2.34 |

Gross margin and break-even. Break-even multiple = fee-minus-non-AI divided by AI cost, i.e. how many times the assumed token volume a job can burn before margin hits zero; "calls" = multiple x assumed calls per job (assumes average call size stays the same).

| Profile (scenario) | GM at Rs 40 | BE multiple / calls at Rs 40 | GM at Rs 100 | BE multiple / calls at Rs 100 |
|---|---|---|---|---|
| 1 Flash 2026 no cache | 94.2% | 23x / 116 | 97.7% | 59x / 293 |
| 1 Flash 2027 no cache | 89.9% | 12x / 58 | 96.0% | 29x / 146 |
| 1 Flash 2027 cached | 91.2% | 14x / 68 | 96.5% | 34x / 172 |
| 1 Lite cached | 96.4% | 49x / 242 | 98.5% | 122x / 612 |
| 2 Flash 2026 no cache | 89.6% | 13x / 90 | 95.8% | 33x / 230 |
| 2 Flash 2027 no cache | 82.1% | 6.5x / 45 | 92.8% | 16x / 115 |
| 2 Flash 2027 cached | 84.3% | 7.6x / 53 | 93.7% | 19x / 135 |
| 2 Lite cached | 93.5% | 27x / 188 | 97.4% | 68x / 478 |
| 3 Flash 2026 no cache | 86.4% | 9.0x / 81 | 94.6% | 23x / 205 |
| 3 Flash 2027 no cache | 75.6% | 4.5x / 40 | 90.2% | 11x / 103 |
| 3 Flash 2027 cached | 78.7% | 5.3x / 47 | 91.5% | 13x / 120 |
| 3 Lite cached | 92.1% | 19x / 171 | 96.9% | 48x / 435 |
| 4 Flash 2026 no cache | 88.4% | 9.6x / 38 | 95.4% | 24x / 97 |
| 4 Flash 2027 no cache | 78.1% | 4.8x / 19 | 91.2% | 12x / 48 |
| 4 Flash 2027 cached | 81.9% | 5.9x / 24 | 92.8% | 15x / 59 |
| 4 Lite cached | 94.1% | 22x / 87 | 97.7% | 55x / 220 |

Reading: the tightest case (Flash 2027, no cache, claim triage at Rs 40) still gives about 76% to 78% gross margin on variable cost, and tolerates about 4.5x the assumed token volume. The AI cost is not the binding constraint; the risks are (a) a fee that does not apply per call, (b) retries and long-running agent loops (a 20-turn conversation could be 5x+ the token volume), (c) payment gateway fees, support, and human technician time, which are not modeled. Margins here are variable-cost margins, not fully loaded. Unmodeled: GST on BSP/SMS (18%), payment fees, Document AI (if used), Pro-tier calls (a single Pro call of 20k in / 2k out = Rs 6.0 at $2/$12, so one escalation roughly equals an entire Flash job).

Why caching helps less than expected: only about 15% (Flash) saving because output tokens dominate (thinking is at output rate: P1 output 2,500 x $3.75 = Rs 0.88 of Rs 1.70). Output/thinking control is the bigger lever (see 6).

Calculation basis: AI Rs = [(uncached text + audio + image) x in-price + cached x cache-read + output x out-price] / 1M x 94. 🔴 Re-run once Vertex prices are confirmed.

## 6. Cost-control tactics

### Takeaway
Routing to Flash-Lite and capping thinking/output deliver most of the saving; batch halves async work; caching is marginal at pilot scale.

### Cited Findings and quantified (from the prices above)
- Route classification, extraction and templated messages to Flash-Lite 3.5, reserve Flash for diagnosis/triage: model-cost ratio 2.5x input, 1.5x output now (3.1-3.6x in 2027 on blended basis). In the model above, all-Lite cuts per-job AI cost 46% to 52% vs Flash 2026 and 73% vs Flash 2027. 🔴 calc on 🟢 prices. Quality loss is untested; evaluate on pilot data.
- Batch/Flex 50% discount on all Gemini models ([pricing](https://aistudio.google.com/docs/pricing) 🟢): use for nightly claim triage, reminder generation, re-indexing; not for live chat. Flex is Batch price with synchronous-style API but latency semantics unverified. Vertex batch in asia-south1 unconfirmed.
- Context caching: read is 10% of input (Flash) with storage $0.50/1M tok-hr (2027: $1.00). Break-even above roughly 1 to 2 hits per hour per prefix (section 1). Measured effect in model: 8% to 18% saving on Flash.
- Truncation and media resolution: image default 1,120 tokens, `low` 280, `medium` 560 ([Media resolution](https://aistudio.google.com/docs/media-resolution) 🟢). Using medium for label photos saves 560 tokens = 0.0004 USD per image on Flash; trivial in money, more useful for latency. Cap RAG context to the top 3 chunks, summarise history after N turns. Savings depend on chunk size: each 1,000 text tokens avoided = Rs 0.07 (2026) / Rs 0.14 (2027) on Flash. 🔴
- Output and thinking caps: output costs 5x input per token; the max-output-token and thinking-level settings are the largest single lever (halving output saves about 26% of P1 cost). 🔴
- Prefer Gemini audio over Chirp: Rs 0.135 vs Rs 1.50 per minute (11x). 🔴 on 🟢/🟡.
- Message design: use utility templates only when outside the window; keep service replies in-window (1,000 free per number per month); avoid marketing category (Rs 0.8631 vs Rs 0.115). 🟡
- Budget guards: per-job token budget and cost cap as config (matches existing architecture note), kill switch at e.g. 5x assumed volume (break-even is 4.5x to 12x in the worst 2027 case at Rs 40), alert on cost_ledger per job, fall back to rules when exceeded. 🔴
- Gemini Developer API paid tier does not train on data; caching retention and ZDR constraints are in existing notes. No external published savings numbers for any of these tactics were found beyond the vendor price ratios above; "agentic video understanding up to 88% fewer tokens" is on the pricing page but not relevant to photos. 🟢

### Gaps
- No published benchmarks of Flash-Lite vs Flash extraction accuracy for Indian invoices/Hindi audio found; real call counts and token sizes need pilot measurement.

## Key conflicts and open items (for the report writer)
1. Mumbai in-region model is "gemini-3.5-flash" (Vertex residency page) but the pricing page has 3.8/3.6 Flash and 3.5 Flash-Lite only.
2. Vertex pricing page unreadable; all token prices from the Gemini API page.
3. 1 Jan 2027: Flash 3.6/3.8 doubles (price, cache, storage). Gemini 4 Carbon/Argon double on 1 Dec 2026 (earlier). Flash-Lite and Pro unchanged.
4. WhatsApp India: INR rates only from secondary sources; charging of service and in-window utility from 1 Oct 2026 for India not confirmed by Meta's page.
5. Chirp 3 price from a search snippet of Google's page, not a clean fetch.
6. Image token counts: 258/tile (older doc) vs 1,120 default (Gemini 3 media-resolution doc).
