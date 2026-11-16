# AI desk for small Indian appliance repair agencies: inputs, outputs, triggers (as of Nov 2026)

Research budget (~15 calls) went mostly to platform docs. Agency-workflow sections (channels, job-card fields, safety, triggers) are thinly sourced; items marked UNVERIFIED are domain knowledge, not found in a source.

## 1. Complaint channels and what a complaint contains

### Takeaway
No source found that measures channel mix for small Indian agencies. Design should assume voice notes/calls, WhatsApp text+photos, walk-ins, and OEM-forwarded jobs, with free-text fault descriptions.

### Cited Findings
- WhatsApp inbound webhooks deliver `messages[]` with a `type` per message and `contacts[].wa_id` / profile name, plus `metadata.phone_number_id` — [Meta webhooks components](https://developers.facebook.com/docs/whatsapp/cloud-api/webhooks/components)
- Consumer-forum matters show repeated technician visits recorded as job sheets (five in the Howrah/Whirlpool case), and job sheets that omit "nature of service" were faulted — [LiveLaw](https://www.livelaw.in/consumer-cases/howrah-district-commission-whirlpool-repair-replace-washing-machine-manufacturing-defects-warranty-period-261153) (secondary report; full judgment not read)

### Inferences
- Minimum intake record: caller phone (wa_id), name, address/pincode/landmark, appliance type, brand, free-text symptom, any error code seen, media (voice note/photo of display or nameplate), preferred slot, warranty claim (Y/N), source channel.

### Gaps
- Channel proportions, OEM call-centre job-forward format (SMS/app/portal) and what it contains: not found. UNVERIFIED.

## 2. Job card / call slip / OEM service request fields

### Takeaway
No official OEM form fetched. Field list below is UNVERIFIED practitioner convention, except the legal-evidence point.

### Cited Findings
- Job sheets are used as evidence in consumer disputes; advice is to keep job sheet, bill and technician contact — [LiveLaw Howrah](https://www.livelaw.in/consumer-cases/howrah-district-commission-whirlpool-repair-replace-washing-machine-manufacturing-defects-warranty-period-261153); [search summary of consumer-advice page](https://righttoinformation.wiki/_export/xhtml/washing-machine-fridge-repair-damage-india)
- NCDRC has examined frequent job cards in warranty as evidence of inherent defect (excavator case, analogous) — [LiveLaw PDF](https://livelaw.in/pdf_upload/warranty-547019.pdf) (not opened; from search snippet)

### Inferences (UNVERIFIED field list)
- Job ID, OEM complaint/ticket no., dates (logged, visit, closed), customer details, appliance, brand, model, serial no., purchase date, invoice ref, warranty status (in/out, extended/AMC), fault reported, fault found, action taken, parts used (code, qty, price), visit/service charge, payment mode, customer signature/OTP, technician ID, status.
- "Nature of service" and repeat-visit history should be mandatory because they matter legally.

### Gaps
- Real OEM forms (LG/Samsung/Whirlpool/Voltas) not retrieved.

## 3. Error codes, symptoms, pre-visit needs

### Takeaway
Codes are brand and model specific; third-party lists conflict, so the AI must ground on the model's own manual and never guess a code meaning.

### Cited Findings
- LG washer: OE drain, IE fill, UE unbalance, LE motor lock, PE water-level sensor — [WhiteGoodsHelp](https://www.whitegoodshelp.co.uk/lg-washing-machine-error-codes/); search summary notes LG's own help library is the authoritative reference per model (third-party sources, UK/EU-oriented)
- Samsung AC: E1 reported mostly as communication/sensor fault (Samsung LatAm lists E1/22 as heat-exchanger sensor); gas-leak codes cited as E497, E554, E5 with sources conflicting on E5; recharge without leak repair recurs — [Samsung support](https://www.samsung.com/ar/support/home-appliances/error-codes-on-your-samsung-indoor-air-conditioner/); [Digirake](https://knowledge.digirake.com/ac/samsung-ac-error-codes?amp=1); [BOXT](https://www.boxt.co.uk/air-conditioning/guides/samsung-air-conditioning-fault-codes)

### Inferences
- Pre-visit output: probable causes ranked, parts to carry (e.g. drain pump, inlet valve, pressure sensor, sensor probes), tools, gas kit for AC. Treat as a suggestion with citation to manual page.

### Gaps
- Fridge codes, Indian-market manual structure, tool/parts checklists: not researched.

## 4. Safety triggers

### Takeaway
No sourced standard found. Proposed hard-stop list is UNVERIFIED and should be reviewed by a domain expert.

### Inferences (UNVERIFIED)
- Stop troubleshooting and tell customer to isolate power/gas and wait for technician when: burning smell or smoke, sparks, electric shock or tingling on body, water near live parts or wet sockets, gas smell or gas geyser involved, swollen/hot compressor or refrigerant hiss/leak, melted plug.
- Never advise customer to open panels, handle refrigerant or bypass fuses.

### Gaps
- Indian regulatory/OEM safety text not retrieved.

## 5. Outputs agencies use

### Takeaway
Not sourced from agency software docs. Expected outputs: job card, parts list, quote, status messages.

### Cited Findings
- Outbound business-initiated messages outside a window must be pre-approved templates, each categorised authentication, marketing or utility — [Meta template overview](https://developers.facebook.com/documentation/business-messaging/whatsapp/templates/overview)
- Outbound statuses: sent, delivered, read (failed also exists) — [Meta webhooks](https://developers.facebook.com/docs/whatsapp/cloud-api/webhooks/components)

### Inferences
- Utility templates needed: complaint registered, technician assigned + slot, on the way, parts ordered, quote approval request, job completed + feedback, warranty/repeat-visit info. Quote needs line items (visit charge, parts, labour), customer approval event.

### Gaps
- Real customer message samples: none found.

## 6. Technical limits (Gemini and WhatsApp)

### Cited Findings
- Gemini audio: up to 9.5 h per prompt, 32 tokens/s, 20 MB total inline request (use Files API beyond), formats WAV, MP3, AIFF, AAC, OGG, FLAC, M4A, Opus, WebM etc. — [Gemini audio docs](https://ai.google.dev/gemini-api/docs/audio) (redirects to aistudio.google.com/docs/audio)
- WhatsApp voice notes are normally OGG/Opus (UNVERIFIED here), which is in the supported list.
- Gemini images: PNG, JPEG, WEBP, HEIC, HEIF; 20 MB inline total; up to 3,600 images/request; 258 tokens per 768x768 tile; `media_resolution` param on Gemini 3 — [Image docs](https://ai.google.dev/gemini-api/docs/image-understanding)
- Structured output: set `mime_type` application/json plus `schema`; subset of JSON Schema; `minLength/maxLength/uniqueItems` etc. silently ignored (validate in app); `minItems/maxItems` enforced; too-deep schemas can 400. Combining with tools (Search, URL Context, code exec, File Search, function calling) is preview on Gemini 3/4 series — [Structured output docs](https://ai.google.dev/gemini-api/docs/structured-output)
- Function calling modes AUTO / ANY / NONE, with `allowed_function_names` for ANY — [Google Cloud function-calling reference](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/models/function-calling) (Vertex doc; assumed same for Gemini API)
- File Search (RAG over own docs): 100 MB per document; store limits by tier (Free 1 GB); citations include file_name, page_number; metadata filters; combinable with function calling and structured output on Gemini 3+; not combinable with Google Search/URL Context; not supported in Live API — [File Search docs](https://ai.google.dev/gemini-api/docs/file-search)
- Live API: stateful WebSocket; input PCM 16-bit 16 kHz, output PCM 24 kHz; JPEG video frames at <=1 FPS; function calling and Google Search supported; 70 languages — [Live API docs](https://ai.google.dev/gemini-api/docs/live)
- WhatsApp webhook: `object: whatsapp_business_account`, `changes[].field: messages`; `messages[]` incoming (type-dependent), `statuses[]` outgoing, `errors[]`; unsupported message type reported as `type: "unsupported"` — [Meta webhooks](https://developers.facebook.com/docs/whatsapp/cloud-api/webhooks/components)
- Templates are the only message type allowed outside a customer service window — [Meta template overview](https://developers.facebook.com/documentation/business-messaging/whatsapp/templates/overview)
- Window: 24 h, resets on each customer message (third party); Click-to-WhatsApp ad entry gives 72 h free window; from 1 Oct 2026 free-form replies and in-window utility templates reportedly become billable (third-party; Sinch mentions a monthly free service allowance, others don't; Meta's own pricing page still showed old wording) — [Courier](https://www.courier.com/blog/whatsapp-pricing-changes-october-2026); [WATI](https://www.wati.io/en/blog/whatsapp-service-message-pricing/); [Sinch](https://support.app.sinch.com/hc/en-us/articles/17433223449103-How-WhatsApp-pricing-works); [Meta pricing](https://developers.facebook.com/docs/whatsapp/pricing). Verify before costing.

### Inferences
- File Search cannot be used inside Live API, so a voice agent must fetch manual snippets via a function call to a separate retrieval service.
- Since constraints like maxLength are ignored, validate phone, pincode, serial format in code.

### Gaps
- Live API session length limit, model names and pricing not on fetched page; official WhatsApp 24 h window page (moved) not read directly; opt-in rules for India not read.

## 7. Trigger events in an agency's day

### Takeaway
No source; list is proposed (UNVERIFIED) and mapped to platform signals.

### Inferences
- New complaint: webhook `messages` (new wa_id or no open job) or call transcript -> create job, ask missing fields.
- Missed call: telephony event -> send template (outside window) offering WhatsApp intake.
- No reply from customer: timer since last outbound; if window closed, only template allowed (per Meta); `statuses` read/failed informs retry.
- Part unavailable: technician/parts input -> status "awaiting part", utility template with ETA.
- Repeat complaint within N days (N is agency/OEM policy, not found): match on phone/serial/address against closed jobs -> flag, escalate, copy prior job history (legal relevance: repeat job sheets cited in consumer cases).
- Technician completes job: job card fields, parts, charges, signature/OTP -> closure message, feedback request.
- Safety keyword in any message/voice note: immediate hard-stop reply and priority dispatch.

### Gaps
- N-day repeat thresholds, SLA norms, escalation rules: not found.
