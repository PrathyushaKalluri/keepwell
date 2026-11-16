# Google Cloud infrastructure, security, operations and startup programs for an India AI SaaS (state: 15 Nov 2026)

Method note: ~19 tool calls. Most cloud.google.com pricing pages (Cloud Run, Cloud SQL, Model Armor, Sensitive Data Protection, Vertex/"Agent Platform" pricing, startup/AI, startup FAQ) returned only a title to the fetch tool, so per-SKU prices could NOT be verified. Rows tagged 🔴 come from my training knowledge or inference and must be re-checked on the live page. Tags: 🟢 official page fetched, 🟡 secondary, 🔴 unverified. Existing notes (Gemini models, Mumbai model list, token costs) are not repeated. Note: Vertex AI pricing page is now titled "Agent Platform Pricing" (rename seen in page title) 🟢.

## 1. Catalogue: what each product does, status, Mumbai/Delhi availability, pricing and fit

### Takeaway
Everything needed for a lean stack (Cloud Run, Cloud SQL, GCS, KMS, Secret Manager, Pub/Sub, Tasks, Scheduler, Logging) is available in Mumbai; Delhi (asia-south2) is a thinner region and should only be a DR option. Security services Sensitive Data Protection (DLP), Cloud Armor, Access Transparency, Monitoring, Trace, Error Reporting, Cloud Build and Gemini Cloud Assist are "global" services, so they have no region pin but DLP can be called with a region location (🔴).

### Cited Findings
Region rules (official):
- All new regions offer at launch: Compute Engine, GKE, Cloud Storage, Persistent Disk, Cloud SQL, VPC, VPN, KMS, Cloud Identity, Secret Manager; further products (Cloud Run, Bigtable, Memorystore, Apigee, Spanner, BigQuery, Dataflow, Dataproc, Pub/Sub) within ~6 months of launch — [Cloud locations](https://cloud.google.com/about/locations) 🟢. This is a policy statement, not a per-region confirmation.
- Globally available (no location dependence): Cloud Armor, Cloud Load Balancing, Cloud CDN, Cloud DNS, Cloud Monitoring (see regional scenarios), Cloud Trace, Error Reporting, Profiler, Cloud Build, Cloud Endpoints, IAM, Access Transparency, Cloud Data Loss Prevention, Security Command Center, Gemini Cloud Assist, Gemini Code Assist, Looker Studio — [Cloud locations](https://cloud.google.com/about/locations) 🟢.
- Cloud Run: asia-south1 Mumbai is Tier 1 pricing; L4 GPU there is "available by invitation only"; asia-south2 Delhi is Tier 2 pricing and lists NVIDIA RTX PRO 6000 Blackwell (no L4) — [Cloud Run locations](https://docs.cloud.google.com/run/docs/locations) 🟢 (fetch-tool summary; re-check).
- Cloud SQL PostgreSQL extensions: pgvector 0.8.5 (PG13+), pg_cron 1.6.4 (flag cloudsql.enable_pg_cron), pgAudit (up to PG18), google_ml_integration 1.4.3 (PG12+) — [Cloud SQL extensions](https://docs.cloud.google.com/sql/docs/postgres/extensions) 🟢.
- Free-tier (monthly) numbers are in section 2.

Catalogue table (Availability column: M = Mumbai, D = Delhi; "G" = global service; pricing detail for 🔴 rows is from memory).

| Product | What it does | Status | M / D | Pricing model and free tier | Fit for Keepwell-type SaaS |
|---|---|---|---|---|---|
| Cloud Run services | Serverless containers, scale to zero, request or instance billing | GA | M yes (Tier 1) 🟢 / D yes (Tier 2) 🟢 | vCPU-s, GiB-s, requests; free 2M req, 180k vCPU-s, 360k GiB-s per month 🟢 | Primary compute: webhook receiver, API, workers |
| Cloud Run jobs | Run-to-completion batch tasks | GA | M/D 🔴 same as services | Same CPU/memory billing; shares free tier 🔴 | Nightly evals, reports, backfills |
| Cloud Run GPU | L4 / RTX PRO 6000 on Run | GA elsewhere; M invite-only L4 🟢 | M L4 by invite; D RTX PRO 6000 🟢 | Per GPU-second 🔴; no free tier (GPUs excluded) | Not needed; use Gemini API |
| Cloud Run functions (ex Cloud Functions) | Function-as-a-service on Run | GA | M/D 🔴 | Free 2M invocations, 400k GB-s, 200k GHz-s 🟢 | Optional; prefer plain Run services |
| App Engine | Legacy PaaS | GA, maintenance mode 🔴 | M 🔴 (Mumbai has had App Engine) | Free 28 F1 hrs/day 🟢 | Skip |
| GKE Autopilot | Managed Kubernetes | GA | M/D 🔴 (GKE is a launch product 🟢) | Per pod resource; free credit covers one cluster fee only 🟢 | Overkill |
| Pub/Sub | Messaging, push to Cloud Run, DLQ | GA | M 🔴 | Per GiB; free 10 GiB/month 🟢 | WhatsApp event fan-out, retries |
| Cloud Tasks | Per-task HTTP queue with rate limits/delay | GA | M 🔴 | Per million ops; free tier 🔴 (first 1M/month from memory) | Per-tenant throttled sends, delayed follow-ups |
| Cloud Scheduler | Cron triggers | GA | M 🔴 | 3 free jobs per billing account 🔴 | Daily digests, sweeps |
| Workflows | Orchestrate steps/HTTP calls | GA | M 🔴 | Free 5,000 internal steps, 2,000 external HTTP calls 🟢 | Multi-step job pipelines (optional) |
| Eventarc | Route events (GCS, Pub/Sub, audit logs) to Run | GA | M 🔴 | Pay per event beyond Google sources 🔴 | GCS upload -> process voice/photo |
| Cloud SQL for PostgreSQL (pgvector) | Managed Postgres, HA, PITR, CMEK | GA | M yes (launch product 🟢) / D 🔴 | vCPU, RAM, storage, backups; no always-free 🔴; pgvector 🟢 | Core multi-tenant DB; RLS + pgvector |
| AlloyDB | Postgres-compatible, columnar engine, ScaNN index, AI functions | GA | M 🔴 / D 🔴 | Higher min cost (HA cluster) 🔴; trial offers exist 🔴 | Later; overkill at <1k jobs/day |
| Spanner | Global relational | GA | M 🔴 (6-month rule 🟢) | Min ~100 PU / 1 node scale 🔴 | Overkill |
| Firestore | Document DB, realtime | GA | M 🔴 | Free 1 GiB, 50K reads, 20K writes, 20K deletes/day 🟢 | Optional for session state; Postgres is simpler |
| Memorystore (Redis/Valkey) | Managed cache | GA | M 🔴 | Per GB-hour; no free 🔴 | Skip at pilot scale (use Postgres) |
| Cloud Storage | Object storage, lifecycle, signed URLs, CMEK, retention locks | GA | M yes (launch product 🟢) | GB-month + ops; free tier only in us-east1/us-west1/us-central1 so NOT free for Mumbai 🟢 | Voice notes, photos, with lifecycle delete |
| BigQuery (BQML, AI functions, vector search) | Warehouse; ML and AI SQL functions; vector index | GA | M 🔴 | Free 1 TiB query, 10 GiB storage 🟢 | Analytics/eval logging, cheap |
| Looker Studio | Free BI dashboards | GA | G 🟢 | Free (Pro paid) 🔴 | Agency dashboards, internal |
| Looker (original/platform) | Enterprise BI | GA | separate location list 🟢 | Quote based 🔴 | Skip |
| Dataflow | Beam streaming/batch | GA | M 🔴 | Per vCPU/GB-hour 🔴 | Skip |
| Identity Platform / Firebase Auth | End-user auth, phone OTP, multi-tenancy | GA | G 🔴 | Free tier of MAU on Identity Platform 🔴 (phone SMS billed per SMS) | Agency staff login, tenant-aware |
| Secret Manager | Secrets with versions | GA | M yes (launch product 🟢) | Free 6 versions, 10k accesses 🟢 | WhatsApp tokens, API keys |
| Cloud KMS | Keys, CMEK | GA | M yes 🟢 | Free only for Autokey keys (100 versions, 10k ops) 🟢; otherwise per key-version | CMEK for Cloud SQL/GCS if required |
| Sensitive Data Protection (DLP) | Inspect/de-identify text, images, structured data; India infoTypes | GA | G 🟢; location param available 🔴 | Per GB; free tier exists 🟡 (fetch summary: "a free tier is available") | PII redaction before LLM/logging |
| Model Armor | Screens prompts/responses: injection, jailbreak, SDP data loss, malicious URLs | GA 🔴 | locations not verified | Per-token pricing with free tier 🔴 (not verified) | Guard WhatsApp text into LLM |
| Cloud Armor | WAF, DDoS, rate limits at LB | GA | G 🟢 | Per policy/rule/request 🔴; needs external LB | Optional; Run + webhook secret verification is cheaper |
| reCAPTCHA Enterprise | Bot/abuse scoring | GA | G 🔴 | Free 10,000 assessments/month 🟢 | Signup form only |
| API Gateway / Apigee | API management | API Gateway GA; Apigee GA | Apigee in 6-month list 🟢 | API Gateway per million calls 🔴; Apigee expensive | Skip both; Cloud Run + IAM |
| Cloud Logging / Monitoring | Logs, metrics, alerts | GA | G (Monitoring regional scenarios 🟢) | Free 50 GiB logs per project/month 🟢 | Core |
| Cloud Trace / Error Reporting / Profiler | Tracing, error grouping | GA | G 🟢 | Trace free tier 🔴; Error Reporting free 🔴 | Core, near-zero cost |
| Gen AI Evaluation Service | Managed LLM-as-judge metrics, rubrics | GA 🔴 | Vertex region support unverified | Billed per judge-model tokens 🔴 | Eval harness; or DIY with Flash-Lite |
| Vertex Experiments / Model Monitoring | Track runs; drift monitoring for deployed models | GA | 🔴 | Experiments nearly free 🔴 | Low value unless self-hosting models |
| Assured Workloads / Data residency / Access Transparency | Compliance controls; residency terms; admin-access logs | Access Transparency listed global 🟢 | Assured Workloads India packages unverified | Assured Workloads has premium fees 🔴 | Skip Assured Workloads; use org policy `gcp.resourceLocations` (🔴) |
| Billing budgets / quotas | Budget alerts, programmatic caps; quota requests | GA | G | Free 🔴 | Mandatory on day 1; note trial accounts cannot request quota increases 🟢 |
| Terraform / Infrastructure Manager | IaC; managed Terraform runs | GA 🔴 | G | Infra Manager billed via Cloud Build 🔴 | Use plain Terraform |
| Cloud Build / Artifact Registry | CI builds, container images | GA | Build G 🟢; AR regional 🔴 | Free 2,500 build-min e2-standard-2; AR 0.5 GB 🟢 | CI/CD core |
| Gemini Cloud Assist / Code Assist | AI help for ops; coding assistant | GA, global 🟢 | G 🟢 | Pricing/tier unverified | Nice-to-have |
| Cloud Translation | NMT/LLM translation, Indian languages | GA | not in global list; regional 🔴 | Per character; free monthly tier 🔴 (Natural Language API free 5,000 units 🟢 is different product) | Probably unnecessary: Gemini handles Indic text |

### Inferences
- Because Cloud Storage always-free benefits apply only to US regions, a Mumbai bucket is billed from byte one; cost is small but not zero.
- Cloud Run request-based free tier is large relative to <1,000 jobs/day and region-agnostic (only egress is North America-based), so Mumbai compute is effectively free at pilot scale.
- Skip Apigee, Spanner, AlloyDB, GKE, Memorystore, Dataflow, Assured Workloads for now.

### Gaps
- Mumbai/Delhi per-product availability for Pub/Sub, Tasks, Scheduler, Workflows, Eventarc, BigQuery, Memorystore, AlloyDB, Spanner, Artifact Registry not verified: the locations page renders in an iframe and was not readable. Check `gcloud <product> locations list` or each product's locations doc.
- No current price figures for Cloud SQL, Model Armor, SDP, Gen AI Evaluation, Translation, Cloud Armor (fetch returned title only).

## 2. Free tiers for a 20-agency pilot, and cheapest sane production stack in Mumbai (<1,000 jobs/day)

### Takeaway
Free tiers cover Cloud Run, Pub/Sub, Secret Manager, Logging (50 GiB), Workflows, Build and BigQuery for a pilot; the real recurring costs are Cloud SQL, Cloud Storage in Mumbai (not free), and Gemini tokens. The $300 trial credit cannot be used for Vertex AI/Gemini if you sign up on or after 16 Nov 2026 (tomorrow), so Gemini spend must come from startup credits or cash.

### Cited Findings
- Free tier list (Cloud Run 2M req/360k GB-s/180k vCPU-s; Run functions 2M invocations; Pub/Sub 10 GiB; Secret Manager 6 versions + 10k ops; Logging 50 GiB/project; Workflows 5k internal + 2k external steps; BigQuery 1 TiB query + 10 GiB storage; Firestore 1 GiB + 50K reads/20K writes/day; Cloud Build 2,500 min; Artifact Registry 0.5 GB; reCAPTCHA Enterprise 10,000 assessments; Cloud KMS 100 Autokey versions) — [Free cloud features](https://docs.cloud.google.com/free/docs/free-cloud-features) 🟢.
- Cloud Storage free tier (5 GB, 5k Class A, 50k Class B) is limited to us-east1, us-west1, us-central1 — same source 🟢.
- $300 trial: 90 days, cannot pay for Gemini platform (Vertex AI) if signing up/upgrading on or after 16 Nov 2026, nor Gemini API in AI Studio or managed partner models; on trial billing accounts you cannot add GPUs, use Marketplace or request quota increases; resources are deleted after 30-day grace — same source 🟢.
- Compute Engine free e2-micro only in US regions — same source 🟢.

Cheapest sane production stack (Mumbai, asia-south1) 🔴 design inference:

| Layer | Choice | Cost note |
|---|---|---|
| Ingress/API | Cloud Run service (min instances 0, or 1 for webhook latency) + Meta HMAC signature check | Free tier covers; min-instance 1 small cost 🔴 |
| Queue/async | Pub/Sub push + Cloud Tasks for per-tenant rate limit; DLQ | Free tier |
| Orchestration | Cloud Run jobs + Scheduler; Workflows only if needed | Free/near-free |
| DB | Cloud SQL Postgres (smallest Enterprise shared-core or 1 vCPU dedicated, HA off for pilot), pgvector, RLS by tenant_id | Largest fixed cost; price not verified |
| Files | GCS regional Mumbai bucket, uniform access, signed URLs, lifecycle delete (e.g. 30/90 days), optional CMEK | Billed from first byte |
| Secrets/keys | Secret Manager; KMS only if CMEK needed | Free tier |
| PII | SDP inspect/redact before logging or non-essential LLM calls | Per GB; small text volumes |
| Guard | Model Armor on inbound text (optional) | Unverified |
| Ops | Logging/Monitoring/Trace/Error Reporting, budget alerts at 50/80/100% | Free tier |
| Auth | Identity Platform (tenant-aware) or app-level auth | MAU free tier unverified |
| CI | Cloud Build + Artifact Registry (Mumbai) | Free tier, AR 0.5 GB |

### Inferences
- Skip Cloud Armor/Apigee/Memorystore/AlloyDB/GKE at this scale; add Cloud Armor only after abuse is seen.
- Sign up for the paid account today if the plan relies on the $300 trial toward Vertex (cutoff is 16 Nov 2026), or accept that Gemini must be funded by startup credits.

### Gaps
- Cloud SQL, Cloud Run min-instance, GCS Mumbai, Pub/Sub overage rates not retrieved; no rupee conversions (none official found).

## 3. Security controls mapped to DPDP; Vertex data governance; India residency and compliance

### Takeaway
Google publishes no DPDP-specific commitment I could find; use the standard Cloud Data Processing Addendum (customer = data fiduciary, Google = processor), keep data in asia-south1, and implement fiduciary duties (consent, erasure, breach notice) in your own app. Vertex governance terms (no training on customer data; Mumbai in-region ML processing for a few Gemini models) are covered in the existing architecture notes.

### Cited Findings
- No Google Cloud document mapping DPDP Act obligations (consent, breach notification, data principal rights, processor/fiduciary split) was found; Google India's overview says customer data belongs to the customer and is processed per the agreement, via the Cloud Data Processing Addendum — [Google India regulatory overview](https://services.google.com/fh/files/misc/insights_into_india_telecom_regulations.pdf) 🟡 (search summary), [search result commentary on DPDP rules permitting transfers abroad subject to government restrictions; sector rules (SEBI, RBI) stricter](https://practiceguides.chambers.com/practice-guides/cloud-computing-2025/india) 🟡.
- Google has RBI digital-lending whitepaper for Cloud — [Google Cloud RBI whitepaper](https://services.google.com/fh/files/misc/google_cloud_rbi_digital_lending_guidelines_whitepaper_2023.pdf) 🟡 (title only seen; sector-specific, not DPDP).
- DPDP Rules 2025 are in force per press coverage on Google's consumer privacy tools — [Bureaucrats India](https://bureaucratsindia.in/news/tech-governance/google-ramps-up-privacy-tech-and-scam-protection-tools-as-dpdp-rules-come-into-force) 🟡.
- Access Transparency and Cloud DLP are listed as global services — [Cloud locations](https://cloud.google.com/about/locations) 🟢. Services with configurable data location are listed on [Data residency terms](https://cloud.google.com/terms/data-residency) 🟢 (page not fetched).
- Sensitive Data Protection supports India-specific infoTypes; the fetch summary and my memory suggest IN_AADHAAR and IN_PAN, but the names were not confirmed in docs — [SDP pricing page summary](https://cloud.google.com/sensitive-data-protection/pricing) 🟡/🔴.

DPDP control mapping 🔴 (my mapping, not an official Google document):

| DPDP duty | Google control |
|---|---|
| Reasonable security safeguards (s.8(5)) | CMEK via KMS, TLS, IAM least privilege, VPC-SC (🔴), Secret Manager, Cloud Audit Logs |
| Data minimisation, purpose limit | SDP redaction before LLM/logs; GCS lifecycle rules |
| Erasure and retention | GCS lifecycle + retention policies; Postgres tenant-level delete jobs; BigQuery table expiry |
| Breach detection/notice | Cloud Logging alerts, Security Command Center Standard (free tier listed 🟢), Access Transparency |
| Processor oversight | Cloud DPA; Access Transparency logs |
| Localisation preference | asia-south1 for Run/SQL/GCS; org policy resource locations; Gemini Mumbai in-region models per prior notes |
| Children's data / consent | App-level; no Google control |

### Inferences
- Be careful claiming "DPDP compliant Google stack"; claim "hosted in Mumbai with security safeguards" and keep your consent records in your own DB.
- Voice and photo storage plus WhatsApp text via Gemini: only models listed for asia-south1 stay in-region; others leave India.

### Gaps
- No Google statement on DPDP processor terms, data-breach notification SLAs for DPDP, or Assured Workloads India package (not found).
- Model Armor locations and regions for SDP/DLP processing not verified.

## 4. Startup programs, credits and eligibility (2026)

### Takeaway
Official Google program pages could not be fetched (title only), but search shows the official AI page citing up to $350,000 over 2 years for AI-tier startups, and the FAQ citing up to $200,000 (Scale) — the Scale/AI tiers need institutional (VC/partner) funding; self-serve Start tier is up to ~$2,000. The India Accelerator is separate: equity-free, AI-first, Seed to Series A, applications for 2026 closed 19 Apr and cohort already announced.

### Cited Findings
- Official AI program page (via search snippet): up to $350,000; Year 1 covers 100% of eligible usage up to $250,000 (Scale credits plus extra $150k for AI tier), Year 2 covers 20% up to another $100k; also $12,000 Enhanced Support credit and possibly $10,000 partner LLM credit via Model Garden (Year 1); "for VC-funded startups ready to Grow and Scale", at Google Cloud's discretion — [Startup AI program](https://cloud.google.com/startup/ai) 🟢 (snippet only; page body not fetchable) and [search result summary](https://cloud.google.com/startup) 🟡.
- Official FAQ (snippet): up to $200,000, or up to $350,000 for Scale-tier AI startups; non-qualifying funding types will not qualify for Scale but may be evaluated for other tiers — [Startup FAQ](https://cloud.google.com/startup/faq) 🟡 (snippet).
- Tier table: Start up to $2,000 (1 year), Scale up to $200,000 (2 years), Scale AI up to $350,000 (2 years); up to $10,000 credits for Anthropic Claude and Fireworks AI; AI Futures Fund co-invests up to $2M — [DEV Community Google AI guide](https://dev.to/googleai/the-2026-ultimate-guide-to-google-for-startups-funding-accelerators-and-350k-in-credits-10ha) 🟡 (hosted by Google AI community; article does not say whether non-AI SaaS qualifies for Scale).
- Third-party: Start for early startups with MVP and no VC, ~$2,000; Scale requires partner investor/accelerator/incubator and equity funding; review time 14-28 days; no India-specific rules — [Gupta Deepak guide](https://guptadeepak.com/startup-offers/guides/google-for-startups-cloud) 🟡 (dates inconsistent: "Jul 2026" vs "Oct 2026"); prior-credit cap ($5K) and company-age limits conflict across sources 🟡.
- Accelerator India 2026: Seed to Series A Indian AI-first startups in Agentic, Multimodal, Physical and Sovereign AI; 3 months, equity-free; Bengaluru bootcamp late June, Demo Day October; benefits include Cloud TPUs, AI tools, Cloud credits "subject to eligibility" (no amount); applied by 19 Apr — [Google India blog](https://blog.google/intl/en-in/inviting-ai-first-startups-to-apply-for-google-for-startups-accelerator-india/) 🟢. 20 startups chosen from ~2,500 applications, cohort announced ~8 Jul 2026 — [Google India blog](https://blog.google/intl/en-in/announcing-the-2026-cohort-of-google-for-startups-accelerator-india/) 🟢 (title) with counts from [Deccan Herald](https://www.deccanherald.com/technology/artificial-intelligence/startups-accelerator-google-picks-20-indian-ai-firms-for-2026-batch-4066655) 🟡.
- $300 free trial cannot pay for Vertex/Gemini for sign-ups from 16 Nov 2026 — [Free cloud features](https://docs.cloud.google.com/free/docs/free-cloud-features) 🟢.

Programs table:

| Program | Status | Amount/benefit | Condition | Tag |
|---|---|---|---|---|
| GFS Cloud Program: Start | Open 🟡 | up to $2,000, 1 yr | Not yet VC funded; MVP | 🟡 |
| Scale | Open | up to $200k, 2 yrs | Institutional/VC funding; partner link | 🟢/🟡 |
| Scale AI | Open | up to $350k (250k Y1, 100k Y2 at 20%) | AI-first, VC funded | 🟢 (snippet) |
| Accelerator India AI First | 2026 cohort closed | credits/TPUs undisclosed | Seed-Series A, India AI-first | 🟢 |
| Gemini API startup credits | Not found separately | — | — | gap |
| Cloud Marketplace listing, Startup School India, Hack2skill/Buildathon credits, nasscom, GDG | Not researched (no results returned in budget) | — | — | gap |

### Inferences
- A pre-seed Indian bootstrapped team most likely qualifies only for Start (~$2,000) unless backed by a VC, accelerator or partner; this does not cover meaningful Gemini volume. Confirm whether Start credits can be used for Vertex AI/Gemini (the trial credit cannot from 16 Nov 2026).
- Accelerator India is the only India-specific path but is closed until the next cohort (likely a 2027 call, 🔴).

### Gaps
- Official tier amounts could not be read directly from cloud.google.com/startup, and whether credits are usable on Gemini API in AI Studio is unverified.
- Gemini API startup credits, Cloud Marketplace, Startup School India, Hack2skill/Buildathon credits, nasscom, GDG not covered.
- No INR conversions from official sources.
