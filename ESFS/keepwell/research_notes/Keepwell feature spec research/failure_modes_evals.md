# Failure modes, fallbacks and evals for LLM agents: Indic voice, GST/label OCR, manual RAG, quotes, claims triage, WhatsApp

Method note: 10 search/fetch calls. Search tool returned summaries, not full pages; one key PDF (Voice of India) was unreadable (compressed). Tags: 🟢 sourced (a URL seen in results supports it), 🟡 secondary/forum/blog, 🔴 inference by me. Anything numeric not tagged 🟢 must be re-verified before external use.

## 1. Documented failure modes with numbers (ASR, OCR/vision, RAG, structured output, injection, tool/API, WhatsApp, outages)

### Takeaway
Hard Indic ASR numbers exist for Hindi but are sparse and non-comparable across papers; no single source ranks Chirp 3, Gemini, IndicConformer on IndicVoices. Vision extraction fails mainly by fabricating plausible values (esp. invoice numbers); structured-output length constraints are unreliable; WhatsApp 131047 (24h window) and Gemini 429s are routine operational failures that need designed-in handling.

### Cited Findings
**ASR**
- 🟢 IndicVoices: 7,348 h, 22 languages, read/extempore/conversational, 16,237 speakers, 145 districts — [AI4Bharat IndicVoices / ACL Findings](https://aclanthology.org/2024.findings-acl.639.pdf)
- 🟢 Hindi (Vaani benchmark, clean speech) WER: Gemini-3.1-Pro ~11.7, Gemini-3.5-Flash ~14.2, Azure ~17.4, Whisper-large-v3 ~23.8; all systems worse on Vaani than Lahaja, IndicConformer shows the largest drop — [Vaani Benchmark V1.0](https://arxiv.org/pdf/2606.21408)
- 🟢 Voice of India (closed benchmark, 14 ASR systems, 11 proprietary): Gemini 3 Pro ~6.0 Hindi, ~8.5 Bengali; Gemini 3 Flash ~8.3 Hindi (via search summary, tables unreadable) — [Voice of India](https://arxiv.org/pdf/2604.19151)
- 🟢 Metric choice matters: orthography-aware WER reduced average WER by 6.3 points on IndicVoices (22 langs) and narrowed the Gemini vs Canary gap — [arXiv 2603.00941](https://arxiv.org/pdf/2603.00941)
- 🟢 Vistaar: IndicWhisper lowest WER on 39/59 benchmarks; Kathbath avg WER 22.3, Kathbath-Hard 25.3 (IndicWhisper row) — [AI4Bharat Vistaar](https://github.com/AI4Bharat/vistaar)
- 🟡 Whisper >125% WER on Odia (unverified, Deepgram blog) — [Deepgram](https://deepgram.com/learn/why-wer-fails-indian-languages-bridge-7-metric-framework)
- 🟢 Chirp 3: asia-south1 is Preview in every doc version seen (GA in us/eu); Tamil ta-IN listed Preview; Hindi confirmed for diarization list; batch limits ~1 min to 1 h (20 min with word timestamps) — [Chirp 3 docs](https://docs.cloud.google.com/speech-to-text/docs/models/chirp-3). Mirrors disagree on asia-northeast1/southeast1 status.
- Not found: Chirp 3 WER by language; WER by noise level / telephony for Indic; code-mixed (Hinglish) WER. 

**OCR / vision extraction**
- 🟢 ReceiptBench: Gemini-3-Pro 516 hallucination errors vs 248 for authors' trained Qwen3-VL; Gemini fabricates a plausible invoice_number to fill schema when not visible; invoice_number hardest field — [arXiv 2605.22413](https://arxiv.org/pdf/2605.22413)
- 🟢 SROIE/CORD/WildReceipt each <2k images, too small/easy for current MLLMs (same paper). Joint multi-field prompt helps some fields vs per-field prompts — [arXiv 2503.16868](https://arxiv.org/pdf/2503.16868)
- 🟡 Codesota claims (GPT-4o table TEDS 72.0; Claude Sonnet 4 0.09% hallucination) lack methodology — [Codesota](https://codesota.com/ocr/invoice-receipt-benchmark). Do not cite.
- Not found: GST-invoice-specific or appliance-label/serial-number accuracy numbers.

**RAG on manuals/tables**
- 🟢 Fixed-size/sliding-window chunking splits multi-page tables and procedures; vision-guided page-batch chunking proposed (internal dataset only) — [arXiv 2506.16035](https://arxiv.org/html/2506.16035v2)
- 🟡 LangChain benchmark (30 Qs, 6 docs, 25 table-based): page-boundary chunking OK except multi-page tables — [LangChain](https://www.langchain.com/blog/benchmarking-rag-on-tables)
- 🟡 Header kept but value dropped by fixed-size split, model then guesses (opinion) — [VentureBeat](https://venturebeat.com/orchestration/most-rag-systems-dont-understand-documents-they-shred-them) (URL as returned: most-rag-systems-dont-understand-documents-they-shred-them)
- Not found: verified REAL-MM-RAG numbers; fault-code-specific retrieval benchmarks.

**Structured output / Gemini**
- 🟡 Forum: maxLength 600 not respected on gemini-2.5-flash-lite; advice: enforce in system prompt — [Google AI forum](https://discuss.ai.google.dev/t/maxlength-not-respected-by-schema/114526)
- 🟢 Vertex docs: only listed schema fields are used, others ignored — [Vertex structured output](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/multimodal/control-generated-output). Whether min/maxLength are on the list was NOT confirmed.
- 🟡 Opposite symptom: HTTP 400 on a gemini-3.x Interactions endpoint with bounds in schema — [forum](https://discuss.ai.google.dev/t/gemini-3-8-flash-interactions-v1beta-http-400-invalid-request-with-stateless-structured-output/184654); 500 with large maxItems — [forum](https://discuss.ai.google.dev/t/500-internal-error-when-using-structured-output-with-large-maxitems/87466); one blog says minItems/maxItems stripped silently — [blog](https://joshualelon-com.pages.dev/posts/ai-sdk-google-silently-strips-minitems-maxitems)
- Thinking-token cost: search returned nothing. 🔴 Treat as unverified: check usage_metadata thinking vs output counts and Gemini pricing page before budgeting.
- 🟢 Schema validity is not truth: ReceiptBench fabrication above is the canonical example.

**Prompt injection**
- 🟢 AgentDojo: attacks succeeded against best agents in <25% of cases; secondary detector cut to ~8% — [AgentDojo](https://arxiv.org/pdf/2406.13352v2)
- 🟢 NIST CAISI: strongest baseline attack 11% vs 81% for new adaptive attacks on one model; baselines understate risk — [NIST](https://www.nist.gov/node/1872381)
- 🟢 Minimize-and-sanitize at tool interface reported near-zero ASR with modest utility loss (Bhagwatkar et al., in [arXiv 2510.05244](https://arxiv.org/html/2510.05244v1) results list).
- Not found: image/document (invoice, voice-note text) injection numbers.

**API limits / outages**
- 🟢 Gemini 429 RESOURCE_EXHAUSTED across RPM, TPM, RPD; RPD resets midnight Pacific; spend caps per 10 min (Tier1 $10, Tier2 $50, Tier3 $200) — [Gemini rate limits](https://ai.google.dev/gemini-api/docs/rate-limits)
- 🟡 Paid-tier 429s well below quota, attributed to free-tier metric (unconfirmed) — [forum](https://discuss.ai.google.dev/t/429-resource-exhausted-on-gemini-api-paid-tier-1-paid-tier-not-enforced-requests-stuck-on-free-tier-quota/173738)

**WhatsApp**
- 🟡 Error 131047 = >24h since customer's last message; free-form blocked, only approved templates; one source (Zernio) misclassifies it as rate-limit — [ChatDaddy](https://help.chatdaddy.tech/article/meta-whatsapp-error-code-131047-waba-re-engagement-outside-24h-window-customer-s)
- 🟡 Pricing moved to per-message template; utility templates free inside open window (from 1 Jul 2025, per provider) — [360dialog](https://360dialog.com/partner-updates/rate-adjustments-and-updates-whatsapp-business-platform). No Meta primary source seen; 131049 semantics conflict across sources.

### Inferences
- 🔴 Plan on Indic WER of roughly 10-25% on clean Hindi for best systems and materially worse for low-resource languages, noise, and code-mixing; treat as priors, then measure on own audio.
- 🔴 Every extracted field needs a "not_visible/null" option plus a verifier (checksum/regex/source-span), because schema-forced models invent values.
- 🔴 GSTIN has a checksum (15 chars, 15th is check character; from my knowledge, not sourced here) so serial/GSTIN/invoice-total arithmetic can be deterministically validated.
- 🔴 Voice-note transcripts and invoice text are untrusted input; never let extracted text choose tools or amounts unreviewed.

### Gaps
- Chirp 3 vs Gemini vs IndicConformer on same Indic set; WER vs noise/SNR; Gemini thinking-token billing; GST invoice and label benchmarks; Meta primary docs on window/pricing/rate tiers; fault-code RAG benchmarks.

## 2. Fallback patterns (ladders)

### Takeaway
Layer cheap deterministic checks before and after the model, abstain-and-ask via WhatsApp for low-confidence fields, then human queue; make all side effects idempotent. Specific thresholds below are design proposals, not sourced.

### Cited Findings
- 🟢 Google guidance for 429: wait and retry with exponential backoff — [Gemini rate limits](https://ai.google.dev/gemini-api/docs/rate-limits)
- 🟢 Rubric/adaptive-rubric judge metrics make multiple Gemini calls (one metric: 6 calls to Gemini 2.5 Flash), relevant to eval cost — [Vertex rubric metrics](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/models/rubric-metric-details)
- 🟡 Outside 24h window the only path is approved template; a delivered utility template opens a 24h window — [ChatDaddy](https://help.chatdaddy.tech/article/meta-whatsapp-error-code-131047-waba-re-engagement-outside-24h-window-customer-s)
- 🟢 Defense in depth for injection: detector (25%→8%) and tool-boundary sanitizer — see section 1 sources.

### Inferences (proposed ladders; all 🔴)
- Voice note: Chirp 3/Gemini transcript -> if language-ID confidence low or WER proxy (second-model disagreement, e.g. normalized edit distance >0.3 between two ASR outputs) high -> reroute to the other engine -> still low: reply on WhatsApp "please confirm: model X, serial Y?" -> human queue. Offline: client records, queues, uploads on connectivity; keep original audio.
- OCR: Flash tier -> deterministic validators (GSTIN checksum/regex, HSN length, subtotal+tax=total within Rs 1, date sanity, serial regex per brand) -> fail -> Pro tier with crop/zoom -> fail -> ask user for retake or typed value -> human queue. Null allowed always.
- RAG: hybrid BM25+embedding with exact fault-code match first (deterministic dictionary lookup by code string), cite page/figure; if top score below threshold or code not found: "I don't have this code in the manual", never free-generate repair steps; escalate to technician. Safety-relevant steps (gas, electrical): require retrieved span quotation.
- Quotes: LLM proposes line items only from rate card; price computed by code; any item outside rate card or total deviating >X% from historical median -> human approval. 
- Claims triage/fraud: rules + features produce flag; LLM only summarizes/explains; never auto-deny; flags go to human with evidence; adverse decisions need human.
- Reliability: retry 429/5xx with jittered exponential backoff (e.g. 1,2,4,8 s, max 4); circuit breaker after N consecutive failures to switch model/region; idempotency key per WhatsApp message id (Meta webhooks redeliver; dedupe on wamid); queue (Cloud Tasks/PubSub) with dead-letter; degraded modes: SMS/IVR callback, template message if window closed; log every fallback taken.
- Routing: cheap model default, escalate on validator fail or low confidence; calibrate threshold on golden set so that escalation rate is ~10-20% (target, not sourced).

### Gaps
- No sourced benchmark for confidence-threshold values or for LLM verbalized-confidence calibration in Indic tasks; I did not search calibration/ECE literature.

## 3. Eval design (golden sets, labelling, kappa, judge calibration, CI gates, monitoring, Google tooling)

### Takeaway
Small teams should build ~100-200 cases per feature, stratified by language/noise, report Wilson/bootstrap CIs, use LLM judges only after calibration against human labels, and gate CI on field-level exact-match plus safety false-accept. ADK evalset and Vertex Gen AI Eval cover trajectory and rubric metrics; verify current criteria names against docs.

### Cited Findings
- 🟢 LLM judges show position, verbosity, self-enhancement bias, and weak reasoning; GPT-4 judge agreement with humans >80%, similar to human-human — [MT-Bench paper](https://arxiv.org/html/2306.05685v4). Exact kappa not in results.
- 🟡 Mitigation: run the judge twice with answer order swapped — [Grepture](https://grepture.com/blog/llm-as-a-judge-bias). Blog recommends chance-corrected kappa over raw agreement — [memx](https://memx.app/blog/llm-as-a-judge-biases-and-fixes/).
- 🟢 Landis-Koch: 0.61-0.80 substantial, 0.81-1.00 almost perfect; authors called bands arbitrary; many fields treat <0.60 as inadequate (McHugh 2012); kappa depressed by skewed prevalence; example kappa 0.65 on n=30 had 95% CI 0.46-0.85 — [York Univ](https://www-users.york.ac.uk/~mb55/intro/kappa4.htm), [Datanovia](https://www.datanovia.com/en/blog/kappa-coefficient-interpretation/)
- 🟢 ADK eval: criteria in test_config.json, values 0-1; tool_trajectory_avg_score default EXACT match, also IN_ORDER and ANY_ORDER; response_match_score is ROUGE-1 (blogs cite 0.8 default/example); final_response_match_v2 is LLM-judged (configurable judge model, samples per invocation); extra tool calls fail EXACT; missing expected intermediate tool calls fail — [ADK criteria](https://google.github.io/adk-docs/evaluate/criteria), [codelab](https://codelabs.developers.google.com/adk-eval/instructions). Sources disagree on defaults; verify.
- 🟢 Vertex Gen AI Eval Service: model-based (judge) and computation-based metrics; pointwise and pairwise (pairwise needs Gemini judge); custom metrics via templates; managed adaptive rubrics (e.g. general_quality_v1) return pass rate plus per-rubric verdicts; docs now under "Gemini Enterprise Agent Platform" URLs — [Define metrics](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/models/eval-python-sdk/determine-eval), [Rubric details](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/models/rubric-metric-details)
- Antigravity / Agent Skills evals: not researched; verified nothing.
- Oracle blog: build a chunking eval set before tuning; test tables separately — [Oracle](https://blogs.oracle.com/developers/rag-chunking-and-parsing-for-tables-pdfs-transcripts-and-media)

### Inferences (🔴 unless noted; from standard statistics, not from search)
- Sample size: for proportion p with 95% CI half-width h, n ~ 1.96^2 p(1-p)/h^2. At p=0.9: n=100 gives ±~6 pts; n=200 ±~4; n=385 (p=0.5) ±5. To detect a regression of 5 pts you need several hundred paired items; use paired comparisons (McNemar) to cut n. Use Wilson interval for accuracy near 0/1; use "rule of three" (3/n) for zero-failure safety claims: 0 false-accepts in 100 only bounds the rate <3% at 95%.
- Practical golden sizes: ASR 30-50 clips per language x condition (clean/noisy/code-mixed) for the 4-6 priority languages (~150-300 min of audio total); extraction 100-150 invoices and 100 labels with field-level labels (each field counted separately, so effective n per field = docs); RAG 100-150 Qs incl. >=30 fault-code exact lookups, >=20 table, >=20 unanswerable; claims/fraud 200+ with positives oversampled (report PR-AUC, precision@k, not accuracy); red team 50-100 injection/jailbreak cases; WhatsApp flow end-to-end 30-50 scripted conversations.
- Labelling protocol: 2 annotators per item on 20-30% overlap, written guidelines, adjudication by a third; native speakers for each language; kappa target >=0.7 (accept 0.6-0.7 only with adjudication); for ASR use CER/WER plus semantic-field accuracy because orthographic variance inflates WER (supported by 2603.00941).
- Judge calibration: label 100+ items by humans, compute judge-vs-human kappa/accuracy, require >=0.7 before use, randomize order, swap order, use different model family from the system under test (self-preference), length-normalize or penalize verbosity in the rubric, binary rubric items over 1-10 scores; recalibrate when judge model changes; never use a judge for numeric fields (use exact match).
- CI gates: block merge if any critical field (amount, GSTIN, serial, fault code) exact-match drops >2 pts or the CI lower bound falls below the threshold; zero tolerance on safety-instruction false-accept in the red-team set; track cost and p95 latency; run full eval nightly, 30-item smoke set per PR.
- Online monitoring: log confidence, validator failures, abstention rate, human override/edit rate per field, language mix, ASR-disagreement rate; weekly sample 50 production items for human review; alert on shifts (PSI or 2-sigma) in abstention or override rate; feed corrected cases back into goldens.

### Gaps
- No sourced sample-size guidance specific to LLM evals (Wilson/bootstrap search returned nothing); no Hamel Husain/Eugene Yan pages fetched; ADK evalset schema fields (eval_cases, conversation, intermediate_data) not verified here; Antigravity not researched.

## 4. Target metrics and credible ranges

### Takeaway
Few sourced ranges exist; use sourced ASR Hindi figures as anchors and treat everything else as proposed targets to be calibrated on the golden set.

### Cited Findings
- 🟢 Hindi WER anchors: best Gemini ~6-12%, Azure ~17%, Whisper-large-v3 ~24% (Section 1 sources). Vistaar IndicWhisper Kathbath avg 22.3, Hard 25.3.
- 🟢 AgentDojo attack success <25% (best agents, baseline attacks), ~8% with detector; adaptive attacks up to 81% (NIST).
- 🟢 LLM judge-human agreement >80% (MT-Bench) as upper reference for judge acceptance.

### Inferences (🔴 proposed targets, not benchmarks)
- Field-level exact match: critical fields (total, GSTIN, invoice no.) >=97-99% after validators, with abstain; non-critical >=90%. Report hallucination rate (value present but not in image) separately; target <1% on critical fields.
- ASR: WER/CER by language; Indic target ~15-25% WER on noisy extempore speech is realistic; downstream field accuracy (model, symptom) matters more; >=90% on those after confirm step.
- Abstention/ask rate 10-25% initially; at the chosen threshold, accuracy on answered items should be >=95% (selective accuracy); report risk-coverage curve.
- Calibration ECE <0.05-0.10 if using confidence thresholds; verbalized LLM confidence is typically poorly calibrated (my knowledge; not searched), prefer validator/agreement-based signals.
- Safety: false-accept on unsafe repair instructions 0 in red-team set (CI upper bound reported); fraud flags: precision >=60-70% at the review capacity, recall dependent on base rate; human override rate tracked, healthy band 5-20% (target; very low may mean rubber-stamping).
- RAG: exact fault-code retrieval recall@3 >=95%; answer faithfulness (all claims in cited span) >=95%; correct "not in manual" refusal >=90%.

### Gaps
- No credible published ranges found for claims-triage, fraud flag precision/recall, override rates, ECE for Indic agent tasks.

## 5. Public datasets for bootstrapping goldens and licences

### Takeaway
IndicVoices (CC BY 4.0, gated) and Kathbath/Vistaar cover ASR; SROIE/CORD cover receipts but are small, English/Latin-script and not GST format; no public GST-invoice or appliance-label set was found.

### Cited Findings
- 🟢 IndicVoices: CC BY 4.0 on Hugging Face, access requires sharing contact info — [HF](https://huggingface.co/datasets/ai4bharat/IndicVoices)
- 🟢 Vistaar repo MIT licensed (covers the code/models; benchmark sets come from Kathbath, others) — [Vistaar](https://github.com/AI4Bharat/vistaar)
- 🟢 Kathbath: 1,684 h, 12 Indian languages, 1,218 contributors; licence not found (AI4Bharat listing has empty field) — verify on HF/IndicSUPERB repo — [IndicSUPERB arXiv 2208.11761 / ar5iv 2305.15386 result](https://ar5iv.labs.arxiv.org/html/2305.15386)
- 🟢 SROIE, CORD, WildReceipt each <2k images (ReceiptBench). Licences not verified in this research (my recollection: CORD CC BY 4.0, SROIE research-use; unverified 🔴).
- 🟡 Vaani (Hindi benchmark) and Lahaja exist as additional Hindi eval sets; licences not checked.

### Inferences
- 🔴 Use public sets only for ASR priors and pipeline smoke tests; domain goldens (appliance service voice notes, GST invoices, label photos, manuals) must be self-collected, with consent and PII redaction (GSTIN, phone, address) under DPDP considerations (not researched).

### Gaps
- Licences for Kathbath, SROIE, CORD, Vaani, Lahaja not verified; no GST invoice or Indian appliance-label dataset found.
