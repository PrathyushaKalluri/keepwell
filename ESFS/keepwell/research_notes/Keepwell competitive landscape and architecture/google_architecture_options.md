# Google AI and Google Cloud building blocks for a multi-tenant, India-hosted, multilingual agent product (as of Nov 2026)

Method note: ~16 tool calls. Many ai.google.dev URLs now 301-redirect to aistudio.google.com/docs/... (same content). Items marked [UNVERIFIED] come from training knowledge or were not covered by fetched pages; confirm before committing. Page content was summarised by a fetch tool, so exact figures should be re-checked on the live page.

## 1. Gemini API vs Vertex AI Gemini; data residency, data terms, pricing options

### Takeaway
For India-hosted, regulated-ish household/claims data use Vertex AI with the regional asia-south1 (Mumbai) endpoint; Delhi (asia-south2) is NOT listed for Gemini. In-region Gemini coverage in Mumbai is narrow (3.5 Flash, 3.5 Flash-Lite, 2.5 Flash 128k) and no Live API model lists India. Gemini API (AI Studio) paid tier is fine for prototyping, with no training use on paid tier, but offers no region pinning [UNVERIFIED for region pinning: not seen on fetched pages].

### Cited Findings
- Vertex data residency page: asia-south1 (Mumbai) has in-region ML processing for gemini-3.5-flash, gemini-3.5-flash-lite, and gemini-2.5-flash (128k variant; 1M not listed for India). asia-south2 Delhi is not mentioned. No Live API model lists India. Only text-embedding-005 lists India among embeddings (gemini-embedding-001/2 do not). Global endpoints give no residency guarantee. — [Vertex data residency](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/data-residency)
- Vertex locations page copy fetched had blank per-region cells; Delhi not listed; Provisioned Throughput and batch availability in India not covered. — [Vertex locations](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/locations)
- Vertex data governance: Google will not use customer data to train or fine-tune models without prior permission (includes pre-GA models). Gemini caches customer data by default (in-memory and durable caches deleted within 24h; durable cache can be disabled per project; CMEK not supported for it). Prompt logging for abuse monitoring may occur. Zero data retention needs: request-response logging off, Live API session resumption off, `store=false` on Interactions API (default true), caching off, no Sandbox Snapshot API. Grounding with Google Search stores derived queries up to 3 days with no opt-out (Web Grounding for Enterprise recommended for ZDR); Grounding with Google Maps stores prompts/outputs 30 days, no opt-out. Agent products have own retention (Deep Research 7 days, CodeMender 7 days). — [Vertex data governance](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/data-governance)
- Gemini API pricing page: free-tier content is used to improve Google products; paid tier is not (Contributor Tier, invite-only, is the exception). Batch = 50% discount; Flex tier priced like Batch (e.g. 3.8 Flash Flex $0.375 input vs $0.75 Standard through 31 Dec 2026). — [Gemini API pricing](https://aistudio.google.com/docs/pricing)
- Per 1M tokens, paid Standard (USD): 3.8 Flash and 3.6 Flash $0.75 in / $3.75 out through 31 Dec 2026, rising to $1.50 / $7.50 from 1 Jan 2027; 3.5 Flash-Lite $0.30 / $2.50; 3.1 Flash-Lite $0.25 text (audio $0.50) / $1.50; 3 Flash Preview $0.50 (audio $1.00) / $3.00; 3.1 Pro Preview $2.00 / $12.00 (<=200k), $4 / $18 (>200k). — [Gemini API pricing](https://aistudio.google.com/docs/pricing)
- Context caching 3.8 Flash: $0.075 cached read ($0.15 from 2027) plus $0.50/1M tokens/hour storage ($1.00 from 2027). — [pricing](https://aistudio.google.com/docs/pricing)
- Search grounding (Gemini 3+): 5,000 free requests/month, then $14 per 1,000, daily cap 1,500 requests as reported by the fetch summary (check). — [pricing](https://aistudio.google.com/docs/pricing)
- Rate limits: page content not retrieved. [UNVERIFIED]

### Inferences
- A startup can prototype on Gemini API paid tier, then move to Vertex regional endpoint (asia-south1) for production with residency claims; design a model-abstraction layer since India-region model list is narrow and changes.
- Voice via Live API and Chirp 3 (see section 3) cannot be claimed as India-resident today; WhatsApp voice notes would route to US/EU or global unless alternate path used.
- Tenant data in Cloud Storage/DB in Mumbai or Delhi is independent of model processing region; document this split in the data-processing story.
- 2.5 Flash/Pro auto-route on 1 Dec 2026 (see below), so avoid pinning to them.

### Gaps
- Gemini API (non-Vertex) regional pinning/residency terms, rate-limit tiers, Flex latency/availability semantics, Vertex batch in asia-south1, Provisioned Throughput in India: not found.
- Whether 3.8 Flash / 3.6 Flash / Gemini 4 are available in asia-south1: not listed on residency page.

## 2. Models, multimodality, tools, Live API

### Takeaway
Model lineup per the current models page: Gemini 4 family (Carbon, Argon, Hydrogen), Gemini 3.x Flash/Flash-Lite stable, 3.1 Pro still preview-named. Live API is preview; audio-only sessions 15 min by default.

### Cited Findings
- Gemini 4: gemini-4-carbon (strongest), gemini-4-argon (efficient), gemini-4-hydrogen (speed); 1M context; text/image/audio/video/PDF input. Status not labelled stable/preview on page. — [Models](https://aistudio.google.com/docs/models)
- Gemini 3.x: gemini-3.8-flash and gemini-3.6-flash (Stable), gemini-3.5-flash-lite and gemini-3.1-flash-lite (Stable), gemini-3-flash-preview (Preview), gemini-3.1-pro-preview (Pro; status not stated; a search snippet suggests gemini-3-pro-preview is shut down). gemini-3.5-flash appears on Vertex residency page but not on the AI Studio models page I fetched (naming mismatch, check). — [Models](https://aistudio.google.com/docs/models)
- Legacy: gemini-2.5-flash deprecated, routes to gemini-3.5-flash-lite on 1 Dec 2026; gemini-2.5-pro deprecated, routes to gemini-3.8-flash on 1 Dec 2026; 2.5 API access limited to existing users. — [Models](https://aistudio.google.com/docs/models)
- Other models: gemini-3.5-transcribe and gemini-3.5-transcribe-live (stable; speech-to-text option), gemini-3.8-flash-tts and flash-lite-tts, gemini-embedding-2 (multimodal), gemini-embedding-001, gemini-decision-1, Nano Banana image models. — [Models](https://aistudio.google.com/docs/models)
- Live API models: gemini-3.8-live (default for voice agents), gemini-3.8-live-extended-thinking, gemini-3.5-live-translate-preview (70+ languages), gemini-3.1-flash-live-preview (legacy), gemini-2.5-flash-native-audio-preview-12-2025. Live API is in preview. Audio-only sessions 15 min, audio+video 2 min unless session management used; context 128k for native-audio models (32k others); input 16-bit PCM 16 kHz, output 24 kHz; video max 1 fps; 99 languages. — [Live API capabilities](https://aistudio.google.com/docs/live-api/capabilities)
- Live API pricing (3.8 Live): audio in ~$0.005/min, audio out ~$0.018/min; Search grounding supported. — [pricing](https://aistudio.google.com/docs/pricing)
- File Search (managed RAG): max 100 MB/file; project storage Free 1 GB, Tier 1 10 GB, Tier 2 100 GB, Tier 3 1 TB; keep stores <20 GB; raw files deleted after 48 h, store data persists; indexing pays embedding price, storage and query embeddings free; structured output supported on Gemini 3+; combinable with custom function calling on Gemini 3 and 4; NOT combinable with Google Search or URL Context grounding; not supported in Live API; audio/video not supported; GA status not stated; data residency not mentioned. — [File Search](https://aistudio.google.com/docs/file-search)
- Structured output, function calling, context caching, and multimodal audio/image input are supported on these models (referenced in the pages above); detailed per-model limits not fetched. [UNVERIFIED detail]

### Inferences
- File Search having no stated residency makes it a poor fit for India-resident tenant documents; prefer own pgvector/AlloyDB RAG with Vertex embeddings (text-embedding-005 is the only India-listed embedding).
- Tool-combination restriction means a claims agent cannot mix File Search and Search grounding in one call; use function-calling over own retrieval.

### Gaps
- Per-model rate limits; Gemini 4 pricing and status; Pro-tier successor naming; Vertex-side Live API model IDs and region support.

## 3. Agent tooling

### Takeaway
Managed Agents and Antigravity agent are preview, run in Google-hosted sandboxes, and are poor fits for residency-sensitive tenant data; ADK on Cloud Run/Agent Runtime is the controllable path.

### Cited Findings
- Managed Agents: base agent `antigravity-preview-09-2026`, preview via Interactions API and AI Studio; sandbox Linux environments (`environment="remote"`), custom agents saved with `agents.create` (model locked at creation); skills mountable at `.agents/skills`, AGENTS.md at `.agents/AGENTS.md`; context compaction ~135k tokens; default tools code_execution, google_search, url_context; remote MCP servers over streamable HTTP with `allowed_tools`; default model Gemini 4 Hydrogen; only text and image inputs; cron triggers; `max_total_tokens` budget; pay-as-you-go tokens + tool use. — [Managed agents quickstart](https://aistudio.google.com/docs/managed-agents-quickstart), [Antigravity agent](https://aistudio.google.com/docs/antigravity-agent)
- Managed agent data handling/residency: not covered on fetched pages. Vertex governance notes avoid Sandbox Snapshot API for ZDR. — [data governance](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/data-governance)
- ADK (adk.dev): open source; Python, TypeScript, Go, Java, Kotlin; ADK 2.0 introduces graph workflows; TypeScript 2.0 GA announced; deploy to Agent Runtime, Cloud Run, GKE or self-hosted; A2A (expose/consume) and MCP (consume/expose) supported; evaluation (criteria, user simulation, custom metrics); logging/metrics/traces with Cloud Trace. — [ADK](https://adk.dev/)
- Antigravity 2.0 (launched 19 May 2026, I/O): desktop app, `agy` CLI (replaces Gemini CLI), SDK, Managed Agents tier; Agent Skills in SKILL.md format carried over from Gemini CLI; AGENTS.md for project instructions; SDK described as Python/research preview by one source; skill paths differ between sources. — secondary only: [TNW](https://thenextweb.com/news/google-antigravity-2-desktop-cli-sdk-io-2026), [Analytics Vidhya](https://www.analyticsvidhya.com/blog/2026/05/google-antigravity-2-0/) [UNVERIFIED vs Google primary]
- Skills loading: SKILL.md files placed in a skills dir (e.g. `.agents/skills/`) are mounted into the agent sandbox; progressive-disclosure loading (name/description first, body on demand) is the Agent Skills convention [UNVERIFIED on Google pages].
- AI Studio Build export: not researched (no source). [GAP]
- A2A: supported in ADK per above; protocol spec not fetched.

### Inferences
- Use ADK (Python) on Cloud Run for the product's orchestrator; treat Managed Agents as a dev/internal accelerator, not tenant-data runtime.

### Gaps
- Antigravity SDK primary docs; AI Studio Build export behavior; Agent2Agent protocol governance/versions; MCP auth in ADK.

## 4. Document AI, Speech, Maps

### Takeaway
Document AI OCR/Custom Extractor/Invoice Parser run in asia-south1; Chirp 3 does not (US/EU only), a residency problem for Hindi/Telugu/Tamil audio.

### Cited Findings
- Document AI: OCR GA, in asia-south1, Indian-language coverage Bangla, Gujarati, Hindi, Kannada, Malayalam, Marathi, Nepali, Punjabi, Tamil, Telugu. Custom Extractor GA in asia-south1 (Indian languages: Hindi, Marathi, Nepali, Sanskrit); generative extraction officially English only and not in asia-south1. Invoice Parser GA in asia-south1 for v1.3 (v2.0 not available there), no Indian-language support. Layout Parser and Expense Parser not in asia-south1. — [Processor list](https://docs.cloud.google.com/document-ai/docs/processors-list)
- Chirp 3: hi-IN GA (diarization yes in Recognize/BatchRecognize), te-IN Preview, ta-IN Preview (no diarization); regions listed: `us` and `eu` multi-regions only. — [Chirp 3](https://docs.cloud.google.com/speech-to-text/docs/models/chirp-3)
- Gemini transcription models gemini-3.5-transcribe / -live exist (stable) but India region support not shown on the residency page. — [Models](https://aistudio.google.com/docs/models), [residency](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/data-residency)

### Gaps
- Maps Platform Routes API / Route Optimization (Fleet Routing) status and pricing: not searched. [UNVERIFIED]; Telugu/Tamil Chirp WER; Chirp 2 in asia-south1.

## 5. Backend building blocks

### Cited Findings
- Cloud Run, Firestore, Cloud SQL/AlloyDB, Pub/Sub, Cloud Tasks/Workflows, Cloud Storage signed URLs, Identity Platform/Firebase Auth (tenants), Secret Manager, Cloud Armor, BigQuery, Vertex GenAI evaluation: NOT researched in this session; no sources fetched. Mumbai (asia-south1) and Delhi (asia-south2) are both Google Cloud regions generally [UNVERIFIED service-by-service availability].
- ADK tracing goes to Cloud Trace; evals in ADK. — [ADK](https://adk.dev/)

### Inferences (training-knowledge, mark unverified)
- Cloud SQL or AlloyDB Postgres with row-level security suits relational machine-history and multi-tenant; Firestore suits chat/session state; Identity Platform supports multi-tenancy.

### Gaps
- Entire section needs follow-up with official docs, especially Identity Platform multi-tenancy, AlloyDB in asia-south2, Gen AI evaluation service in India.

## 6. WhatsApp

### Cited Findings
- WhatsApp Business Platform Cloud API relies on webhooks for inbound messages, status updates, errors; templates require approval and are the only messages allowed outside the customer service window; messaging limits and template quality scores apply. BSP vs direct, signature verification, pricing, India localisation not covered by page. — [Meta Cloud API](https://developers.facebook.com/docs/whatsapp/cloud-api/)
- Google equivalent: no Google product found in my research; Google's RCS Business Messaging exists in Google's ecosystem [UNVERIFIED]; Google Business Messages was retired in 2024 [UNVERIFIED]. Confirmation not completed.

### Inferences
- Webhook ingress pattern: Cloud Run endpoint, verify `X-Hub-Signature-256` HMAC [UNVERIFIED], ack fast, enqueue to Pub/Sub, process async.

### Gaps
- Direct vs BSP, pricing per template category, 24-hour window semantics, India-specific rules.

## 7. Reference architectures

### Gaps
- Google Cloud blueprints for agentic customer-support/field-service apps were not searched; no sources collected.
