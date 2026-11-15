# Google AI models and agent/developer tools catalogue for Keepwell (as of 15 Nov 2026)

Tags: 🟢 official Google page fetched; 🟡 secondary (news/blog/search snippet); 🔴 unverified or my inference. Method: ~19 tool calls; many pages fetched via a summarising tool, so re-check exact figures. ai.google.dev URLs 301-redirect to aistudio.google.com/docs/... Extends (does not repeat) google_architecture_options.md and cost_token_economics.md. Prices USD per 1M tokens, Standard tier, public Gemini API unless stated.

## 1. Which Gemini/Gemma/speech models exist now, status, price, free tier, deprecation (catalogue)

### Takeaway
Current lineup is Gemini 4 (Carbon/Argon/Hydrogen, status unlabelled) plus stable Gemini 3.8/3.6 Flash and 3.5/3.1 Flash-Lite; Gemini 2.5 Flash/Pro auto-route on 1 Dec 2026. The "3.8 Flash" name is real on Google's own models and deprecation pages, so the earlier "unverified" flag can be dropped. Paid tier = no training on data; free tier = used to improve products.

### Cited Findings

**A. Text/multimodal Gemini (Gemini API; Vertex IDs mostly same)** — sources: [Models](https://aistudio.google.com/docs/models) 🟢, [Pricing](https://aistudio.google.com/docs/pricing) 🟢, [Deprecations](https://aistudio.google.com/docs/deprecations) 🟢

| Product (ID) | Status | Price in/out | Free tier | Deprecation | Keepwell fit |
|---|---|---|---|---|---|
| Gemini 4 Carbon (gemini-4-carbon), 1M ctx, 64K-1M out | Status not labelled on page | $2/$10 to 30 Nov 2026; $4/$20 from 1 Dec 2026; batch 50% | No | none announced | Too costly for chat; use for hard claims/fraud reasoning only |
| Gemini 4 Argon (gemini-4-argon) | not labelled | same as Carbon; invite-only Contributor tier $1/$5 (data used to improve products) | No | none | Mid reasoning tier; not needed at pilot |
| Gemini 4 Hydrogen (gemini-4-hydrogen); page recommends it for new projects | not labelled | $1.50/$7.50; cache $0.075; batch/Flex $0.75/$3.75 | Yes | none | Candidate default agent model; but same price as 3.8 Flash from 2027 and India-region support unconfirmed |
| Gemini 3.8 Flash (gemini-3.8-flash) | Stable | $0.75/$3.75 to 31 Dec 2026, then $1.50/$7.50 | Yes | none; receives 2.5 Pro auto-route 1 Dec 2026 | Strong default for diagnosis/quote reasoning |
| Gemini 3.6 Flash | Stable | same as 3.8 | Yes | none; 3-flash-preview and 3.5-flash route here | Fallback |
| Gemini 3.5 Flash | Gone from AI Studio, auto-routed to 3.6 Flash (deprecations page) | not on pricing page | n/a | n/a | But Google India says it is the model with in-country ML processing (see Q2); conflict |
| Gemini 3.5 Flash-Lite | Stable | $0.30/$2.50; batch 0.15/1.25 | Yes | none; receives 2.5 Flash route 1 Dec 2026 | Intake triage, classification, language ID |
| Gemini 3.1 Flash-Lite | Stable | $0.25 (audio $0.50)/$1.50 | via pricing page | 7 May 2027 -> 3.5 Flash-Lite | Cheapest; plan migration |
| Gemini 3 Flash Preview | Preview | $0.50/$3 | Yes | none stated; points to 3.6 Flash | Avoid |
| Gemini 3.1 Pro Preview | Preview-named, no deprecation | $2/$12 (<=200k), $4/$18 | No | none | Skip; Pro tier now = Gemini 4 Carbon |
| Gemini 2.5 Flash / 2.5 Pro | Deprecated | n/a | n/a | both 1 Dec 2026 auto-route (to 3.5 Flash-Lite / 3.8 Flash) | Silent behaviour change risk: do not pin |
| Gemini 2.5 Flash-Lite | Served "until further notice" | n/a | n/a | none | Legacy |
| Gemini Decision 1 (gemini-decision-1, Decisions API) | not labelled | not captured | Yes | none | Zero-output-token yes/no/score; cheap claim-approval gates (🔴 untested) |

Priority tier = 1.8x Standard; Flex = Batch price. Doubling on 1 Jan 2027 for 3.8/3.6 Flash and Flash TTS. 🟢 [Pricing](https://aistudio.google.com/docs/pricing)

**B. Voice / audio** — same three pages

| Product (ID) | Status | Price | Free | Deprecation | Fit |
|---|---|---|---|---|---|
| Gemini 3.8 Live (gemini-3.8-live) | New (Live API itself = preview per earlier notes) | audio in $3/1M or ~$0.005/min; out $12/1M or ~$0.018/min; text $0.75/$4.50 | Yes | none | Voice-call agent; no confirmed India region |
| 3.8 Live Extended Thinking | New | same family | Yes | none | Complex voice troubleshooting |
| 3.5 Live Translate preview | Preview | audio in $3.50 (~$0.0053/min), out $21 (~$0.0315/min); 70+ languages | Yes | none | Customer-technician cross-language bridge |
| 3.5 Transcribe / Transcribe Live | Stable | $3.50 in/$21 out (~$0.005/min blended) | Live variant yes | none | Voice-note STT with diarization, timestamps; Indic quality not stated (gap) |
| 3.8 Flash TTS (130 languages) | New | $0.50 text in, $9 audio out (~$0.00225/10s); doubles 1 Jan 2027 | Yes | none | Spoken quote read-back |
| 3.8 Flash-Lite TTS (101 languages) | New | $0.50 / $6 (~$0.0015/10s); doubles 1 Jan 2027 | Yes | none | High-volume IVR-style replies |
| 3.1 Flash TTS preview; 2.5 Flash/Pro preview TTS | Preview/legacy | 2.5 Pro TTS $1/$20, no free tier | mixed | 18 Dec 2026 -> 3.8 TTS | Migrate off |
| 3.1 Flash Live preview (legacy) | Preview | as 3.8 Live | Yes | none, points to 3.8 Live | Avoid |
| 2.5 Flash native audio preview | preview by ID | $0.50/$2 text, $3 in/$12 out audio | Yes | 31 Mar 2027 -> 3.8 Live | Avoid |

Live API limits from existing notes (15 min audio session, 128k ctx etc.) not repeated.

**C. Image / video / embeddings / agents**

| Product | Status | Price | Free | Deprecation | Fit |
|---|---|---|---|---|---|
| Nano Banana 2.1 (gemini-nano-banana-2.1) | New | in $1.50; ~$0.0336/1K img, ~$0.113/4K | No | none | Annotate fault location on photo; generating repair-step diagrams (low priority) |
| Nano Banana 2 (gemini-3.1-flash-image) | Stable | ~$0.067/1K img | No | none; points to 2.1 | Same |
| Nano Banana 2 Lite (gemini-3.1-flash-lite-image) | Stable | ~$0.0336/1K img | No | none | Cheapest; weak at multi-turn edits |
| Nano Banana Pro (gemini-3-pro-image) | Stable | ~$0.134/1K-2K, $0.24/4K | No | none | Overkill |
| Nano Banana (2.5 flash image) | Deprecated | ~$0.039/img | | 15 Mar 2027 | Avoid |
| Imagen 4 | Shut down (17 Aug 2026) | | | done | n/a |
| Gemini Omni Flash 1.2 (video gen/edit up to 15s with audio) | New | not captured | No | 1.1: 3 Dec 2026 | Not relevant; Veo 3.x shut down (Veo 3.1 preview 22 Oct 2026) |
| Lyria 3.5, Lyria RealTime; Robotics ER 2 | various | n/a | n/a | n/a | Irrelevant |
| Gemini Embedding 2 (gemini-embedding-2; text/image/video/audio/PDF) | not labelled | text $0.20, image $0.45, audio $6.50, video $12 | Yes | none | Multimodal RAG over photos of parts/labels |
| Gemini Embedding 001 | not labelled | $0.15 | Yes | 14 May 2028 | Text RAG |
| gemini-embedding-2-preview | | | | 6 Nov 2026 (already past) | n/a |
| Deep Research / Deep Research Max (deep-research-preview-04-2026) | Preview | not captured | n/a | pro-preview-12-2025 shut 23 Oct 2026 | Market/parts research, not runtime |
| Antigravity Agent (antigravity-preview-09-2026) | Preview | tokens + tools | n/a | 05-2026 shut 5 Oct 2026 | Dev accelerator only |
| Computer Use | GA 30 Oct 2026 per release notes (🟡 secondary quoting the notes: [FourWeekMBA](https://fourweekmba.com/ai-gemini-computer-use-reaches-ga-388-days-after-first-preview/)); built-in tool in 3.5 Flash since 24 Jun 2026 ([Google blog](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-computer-use-gemini-3-5-flash/) 🟢 title only fetched via search); old gemini-2.5-computer-use-preview shut 28 Jul 2026 🟢 | model token rates | n/a | n/a | Could drive OEM warranty/claim portals lacking APIs (🔴 reliability untested) |

Conflict: search summaries said "Gemini 3.8 Flash release unverified", but Google's models, pricing and deprecations pages list it as Stable. Also Computer Use docs examples use gemini-3.6-flash. Google's own pages disagree on 3.5 Flash: Models/Deprecations pages say it is auto-routed to 3.6 Flash, while Google India blog and the Vertex residency page (existing notes) name it for Mumbai. 🟢/🟢.

**D. Gemma (open weights)**
- Gemma 4: sizes E2B (2.3B effective), E4B (4.5B effective), 26B MoE, 31B dense; Apache 2.0 (first OSI licence for Gemma); trained on 140+ languages; multimodal; E2B/E4B built for phones/edge with native audio input; 128K-256K context. 🟡 [TNW](https://thenextweb.com/news/google-gemma-4-open-models-apache-2-launch), [Google blog](https://blog.google/innovation-and-ai/technology/developers-tools/gemma-4/) (search snippet only); 🟢 [Gemma docs](https://ai.google.dev/gemma/docs) confirm Gemma 4 (140+ languages, 128-256K), EmbeddingGemma 2 (text/image/audio/video), ShieldGemma 2, no sizes or Indic languages named on that page.
- No Google-published Hindi/Tamil/Telugu benchmark found for Gemma 4; a Google talk cites official Indian languages as candidates for further training on own data. 🟡 [ai.engineer](https://ai.engineer/talks/_gVFUEdhCyI-gemma-deepminds-family-open-models). National Health Authority used Gemma 4 for Aarogya Setu 2.0; AIIMS uses MedGemma. 🟢 [Google India blog](https://blog.google/intl/en-in/company-news/deepening-our-commitment-to-indias-ai-ambition/)
- Cost: free weights; hosting on Vertex Model Garden/Cloud Run GPU/self-host (pricing not fetched). Fit: on-device E2B/E4B for offline technician voice notes; self-hosted 26B/31B as India-resident fallback if Gemini regional coverage fails (🔴).

**E. Speech/translation services (Cloud, non-Gemini)**
- Chirp 3 HD TTS (Cloud Text-to-Speech): Hindi, Tamil, Telugu, Bengali, Marathi, Gujarati, Kannada, Malayalam, Urdu supported; Punjabi (India) Preview; regions listed global, us, eu, asia-southeast1, europe-west2, asia-northeast1 (all GA); asia-south1 NOT listed; custom pronunciation unavailable for bn, gu, pa, ur; SSML/voice control carry pre-GA warnings. 🟢 [Chirp 3 HD](https://docs.cloud.google.com/text-to-speech/docs/chirp3-hd). Price not captured (gap).
- Chirp 3 STT: hi-IN GA, te-IN/ta-IN Preview, us/eu only; $0.016/min list. Already in existing notes.
- Cloud Translation: Basic and Advanced; 189 languages; Adaptive Translation priced $25 per 1M chars in and out (lower tiers $22.50/$20); another Google page describes Translation LLM at $10/1M chars in and out. 🟡 conflicting snippets from [Google pricing](https://cloud.google.com/translation/pricing); I could not tell which applies. Regional page 404; asia-south1 availability not verified. Fit: glossary-controlled appliance terminology in Indic languages, but Gemini Flash prompts with a glossary are likely cheaper per token (🔴).

### Inferences
- Cheapest defensible stack for pilot: Flash-Lite 3.5 (triage) + 3.8 Flash (reasoning) + Gemini 3.5 Transcribe (voice) + Gemini Embedding/text-embedding-005; avoid anything marked preview.
- Dec 2026 and Jan 2027 are price/route cliffs: 1 Dec (Gemini 4 price doubling, 2.5 auto-route, 3.1 TTS shutdown 18 Dec), 1 Jan 2027 (Flash and TTS doubling).

### Gaps
- Gemini 4 stable/preview status and any India region; Deep Research, Omni, Computer Use prices (pricing page cut off after 100k chars, last 11.6k chars unread); Gemma 4 Indic benchmarks; Chirp 3 HD price; Translation LLM region/status.

## 2. India / asia-south1 availability and data-residency terms

### Takeaway
The only India in-country commitment Google states in primary text is for Gemini 3.5 Flash, plus Gemini on Google Distributed Cloud in Indian data centres. The Vertex locations page cannot be machine-read for Mumbai markers, and Delhi is absent.

### Cited Findings
- "Starting now, [Gemini 3.5 Flash] will be available with strict in-country machine learning processing commitments", for Indian enterprises and startups through Gemini Enterprise Agent Platform and the Gemini Enterprise app; Gemini on Google Distributed Cloud can run in Indian data centres, disconnected. — [Google India blog](https://blog.google/intl/en-in/company-news/deepening-our-commitment-to-indias-ai-ambition/) 🟢
- Vertex locations page has a Mumbai (asia-south1) column with rows for Gemini 4 Hydrogen, 3.8 Flash, 3.8 Live, embeddings, Veo, speech, but availability marks were lost in extraction; Delhi (asia-south2) absent; Provisioned Throughput discussed only for global endpoint; tuning not available on global endpoint. — [Vertex locations](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/locations) 🟢 (inconclusive). Existing notes' residency list (3.5 Flash, 3.5 Flash-Lite, 2.5 Flash 128k in Mumbai) remains the best reading; 2.5 Flash is being retired 1 Dec 2026 so Mumbai coverage may shrink.
- Chirp 3 HD TTS has no asia-south1 listing (above). Chirp 3 STT us/eu only (existing notes).
- Vertex AI was renamed Gemini Enterprise Agent Platform at Cloud Next '26 (April 2026); existing Vertex APIs keep working, new features ship under the new brand. — 🟡 [The Register](https://www.theregister.com/2026/04/22/google_enterprise/), [TNW](https://thenextweb.com/news/google-cloud-next-ai-agents-agentic-era), [PYMNTS](https://www.pymnts.com/artificial-intelligence-2/2026/google-brings-all-enterprise-ai-agent-tools-under-one-roof/); the Gemini API pricing page itself says "Enterprise Agent Platform prices may differ" 🟢 (existing notes). Sub-product renames conflict: Agent Engine -> "Agent Runtime" (one Japanese guide only 🔴; ADK docs per existing notes say Agent Runtime 🟢); Agent Designer -> "Agent Studio" (two sources disagree on whether it merges Vertex AI Studio). docs.cloud.google.com/gemini-enterprise-agent-platform/... returned 404 for me.
- Gemini Live (consumer) now converses in 25+ Indian languages and dialects incl. Sanskrit, Bhojpuri, Maithili; Project Vaani with IISc open-sourced datasets for 109 Indic languages. 🟢 [Google India blog](https://blog.google/intl/en-in/company-news/deepening-our-commitment-to-indias-ai-ambition/). A press report says Google published no accuracy benchmarks for newly added languages. 🟡 [FPJ](https://www.freepressjournal.in/tech/google-unveils-ai-initiatives-across-education-health-at-io-connect-india-2026-all-details). Note this is the consumer Gemini app, not the Live API.
- Managed MCP servers (Maps incl. Grounding Lite, BigQuery, Compute, GKE; 50+ GA/preview at Next '26) are Google-hosted endpoints, enabled per project with IAM. 🟡 [Google Cloud blog](https://cloud.google.com/blog/products/ai-machine-learning/google-managed-mcp-servers-are-available-for-everyone), [Techzine](https://www.techzine.eu/news/infrastructure/137200/google-cloud-offers-managed-mcp-servers-for-bigquery). Region residency not stated.

### Inferences
- Model-region mismatch risk: Mumbai in-country model (3.5 Flash) is the one Google's pages call retired on AI Studio; on Vertex it may persist but confirm lifecycle in writing.
- Voice path (Live API, Chirp 3 TTS/STT, Transcribe) has no confirmed India residency; if residency is contractual, use text-only after on-device/own-hosted STT or accept global processing disclosure.

### Gaps
- Mumbai support per model (markers unreadable), Delhi, Provisioned Throughput/batch/tuning in India, Agent Platform product-by-product regions, allowlisting requirements (none found stated; Contributor tier is invite-only; Gemini 4 Argon contributor tier invite-only).

## 3. Free vs paid tier, data use, rate/size limits

### Takeaway
Free tier content is used to improve Google products; paid tier is not (Contributor tier excepted); Vertex does not train on customer data without permission.

### Cited Findings
- Free tier: yes for Hydrogen, 3.8/3.6 Flash, 3.5 Flash-Lite, Live, TTS (except 2.5 Pro TTS), Transcribe Live, embeddings, Decision 1; no for Gemini 4 Carbon/Argon, 3.1 Pro, Omni, all image models. Paid: not used to improve products for most models; Contributor tier (invite-only, discounted $1/$5 Argon) does use data. — [Pricing](https://aistudio.google.com/docs/pricing) 🟢
- Vertex: no training on customer data without permission; caching and logging details in existing notes. 🟢
- Search/Maps grounding: 5,000 free requests/month then $14/1,000 (existing notes).

### Inferences
- Never send real customer photos/voice to free-tier keys; make the paid-tier billing account the only key in any environment that touches pilot users. 🔴 policy.

### Gaps
- Rate limits per tier; Free tier on-device terms.

## 4. Developer and agent tools: status and deprecations (late 2026)

### Takeaway
Google consolidated dev tooling under Antigravity in 2026: Gemini CLI/Code Assist IDE extensions shut 18 Jun 2026, Jules winds down 31 Dec 2026. ADK, A2A and managed MCP remain the durable layers.

### Cited Findings

| Product | Status (Nov 2026) | Price/limits | India/residency | Fit |
|---|---|---|---|---|
| Google AI Studio (Build/vibe coding) | Live; pricing page now hosted on aistudio.google.com 🟢 (redirects). Build export behaviour not verified | Free to use; API usage per tier | Dev tool, not tenant runtime | Prototype WhatsApp-flow demos fast |
| Gemini Enterprise Agent Platform (ex-Vertex AI): Model Garden, Agent Studio/Designer, Agent Runtime (ex-Agent Engine), RAG Engine, Vector Search, Search, Model Armor, Gen AI Evaluation, tuning, batch, caching, PT | Renamed Apr 2026 🟡; sub-product GA/preview labels and regional lists NOT verified | Enterprise pricing may differ from Gemini API | Mumbai only partial (Q2) | Production plane; see existing notes for RAG/residency |
| ADK (Python/TS/Go/Java/Kotlin), ADK 2.0 graph workflows, evals, A2A, MCP | Open source, current 🟢 existing notes | Free; runtime costs | Self-hosted on Cloud Run Mumbai (🔴 inference) | Orchestrator |
| A2A protocol | Supported in ADK 🟢 existing notes; spec not fetched | free | n/a | Optional OEM/partner agent interop |
| Managed MCP servers (Maps Grounding Lite, BigQuery, Compute, GKE; 50+) | GA or preview mixed at Next '26 🟡; launched 10 Dec 2025 | free server; underlying API charges | region not stated | Maps for technician routing/ETA, BigQuery for analytics |
| Antigravity 2.0 (desktop, `agy` CLI in Go, SDK), Agent Skills | Launched 19 May 2026 (I/O); SDK research preview per secondary | Google AI plan tiers | dev tool | Builder tooling; skills = SKILL.md |
| Antigravity Agent / Managed Agents | Preview (antigravity-preview-09-2026) | tokens + tool use | Sandbox, not residency-sure | Internal only |
| Gemini CLI + Gemini Code Assist IDE extensions | Retired: stopped serving 18 Jun 2026 for free/AI Pro/Ultra/individual users; Enterprise and paid Cloud API key users reportedly unaffected (sources differ); Code Assist for GitHub deprecated 18 Jun, shutdown 17 Jul 2026. 🟡 [developers.googleblog](https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/), [9to5Google](https://9to5google.com/2026/06/17/gemini-cli-code-assist-shutting-down/) | | | Use `agy` instead |
| Jules | Winding down: announced 29 Oct 2026; read-only after 11 Nov; closes 31 Dec 2026 (secondary only, dates vary) 🟡 [TechRadar](https://techradar.com/pro/google-kills-off-jules-its-ai-coding-agent-which-promised-to-do-all-the-jobs-you-didnt-want-to), [FourWeekMBA](https://fourweekmba.com/ai-google-shuts-jules-exit-guide-points-users-to-claude-code/) | | | Do not adopt |
| Genkit, Firebase Studio, Firebase AI Logic, Gemini Nano on-device (Prompt API), NotebookLM, Opal, Grounding with Google Maps (as API), Model Armor, prompt optimizer details | NOT verified this session (searches returned nothing on Firebase Studio/AI Logic/Nano/Genkit/Opal/NotebookLM) 🔴 | | | Need follow-up |

### Inferences
- Stable foundation = ADK + Agent Platform runtime + managed MCP; treat Antigravity and Managed Agents as developer productivity only. Avoid Jules and Gemini CLI.

### Gaps
- Unverified entries in the last row above; Agent Platform per-product status (Agent Runtime, Agent Studio, RAG Engine, Vector Search 2.0, Model Armor, eval service) and India regions; Gen AI Evaluation Service; prompt optimizer; supervised tuning in asia-south1; Provisioned Throughput pricing; allowlisting requirements.

## 5. Indic language-quality statements by Google

### Takeaway
Google makes breadth claims, not per-language accuracy claims, for models relevant to Keepwell.

### Cited Findings
- Gemma 4: "over 140 languages", no Indic breakdown. 🟢 [Gemma docs](https://ai.google.dev/gemma/docs)
- Gemini 3.8 Flash TTS 130 languages, Flash-Lite TTS 101, Live Translate 70+, Live API 99 languages (existing notes), Gemini Live app 25+ Indian languages/dialects; no WER or MOS published for Hindi/Tamil/Telugu in pages fetched. 🟢
- Chirp 3 HD TTS supports 8 major Indian languages plus Urdu and Punjabi (preview). 🟢 above
- Gemini Spark reportedly speaks Haryanvi (regional dialect preview at I/O 2026). 🟡 [Business Today](https://www.businesstoday.in/amp/technology/news/story/google-previews-regional-dialect-capabilities-as-gemini-spark-speaks-haryanvi-at-io-2026-532715-2026-05-21)

### Inferences
- Build own Indic eval set (code-mixed Hinglish voice notes about appliance faults) before choosing between Gemini Transcribe, Chirp 3 and self-hosted models.

### Gaps
- Any official per-language benchmark for Gemini 3.x/4 Indic text or speech; Gemini Nano Indic support.
