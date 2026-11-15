# Keepwell Care Engine: inputs, outputs, input providers and triggers per scenario

*Product specification, 15 Nov 2026. Working name: Keepwell Care Engine. Vision: the care layer for everything a home owns.*

**Evidence labels.** **Sourced** = backed by the three research notes or the scenarios file. **UNVERIFIED** = domain inference with no source. All money figures live in the scenarios file and are assumptions. This spec adds no numbers of its own except where a source gives them.

**Alignment with the existing build** (`keepwell/shared/types.ts`, `keepwell/server/workflow.ts`; read only, not modified). Names below match the build. Places where the spec needs something the build lacks are tagged **BUILD GAP**.

---

## 1. One-screen summary

**One product:** the Keepwell Care Engine. It takes a messy home-care event (a complaint, an invoice, a claim, an old unit), reads or writes the machine record, and returns a checked, evidence-labelled next step that a human can approve.

| Module | Scenario | Job | Payer | Release |
|---|---|---|---|---|
| Prepared Visit | A | Complaint to safe, ready job card | Repair agency | R1 |
| Home Memory and Plans | B (D folded in) | Invoice to machine record, reminders, plan renewals, claim and price help | Agency first, plan commission | R2 |
| Claims Triage | C | Claim file to triage recommendation for an administrator | Warranty administrator, OEM | R3 |
| Circular Loop | E | Old-unit photos to grade and route | Refurbisher, recycler, producer | Vision |

**Shared machine record.** One record per appliance, owned by a household, written to by agencies, owners and (later) administrators. Every field carries a provenance and a verification state. Every module reads it. Every repair, claim or exit event writes back to it. That is the link between modules.

**Rules that hold across all modules**
- The model proposes. Code validates. A human approves anything that costs money, changes a warranty position, or discloses personal data.
- No part compatibility without a catalogue. No payment without a provider event. No warranty eligibility without evidence.
- Safety stops come before everything else.

---

## 2. Shared machine record

### 2.1 Entities and key fields

Existing names from `types.ts` and `workflow.ts` are kept. New entities are marked NEW.

| Entity | Key fields | In build? |
|---|---|---|
| Household | id, members, consent records | `household_id` exists on `SessionUser`. Entity detail not in the shared types. **BUILD GAP**: members and consent |
| Appliance | appliance_id, category, brand, model, serial, seller name, seller GSTIN, invoice no., invoice date, amount, warranty start date and start basis (purchase, install, registration; user can override) | `appliance_id`, `appliance_category`, `brand`, `model` are in `FieldKey`. **BUILD GAP**: serial, seller, invoice fields, start basis |
| Warranty term (NEW) | appliance_id, component, months, conditions (residential only, authorised service only), source | **BUILD GAP**. Store per component, never assume. Sourced: terms vary by brand, model and date |
| Plan (NEW) | plan_id, provider, type (EW or AMC; labour or comprehensive), start, end, visits included and used, parts excluded, price | **BUILD GAP** |
| Service request (job) | id, code, status, safety_flag, fields, channel, media, timestamps | Table `service_requests`, `RequestStatus`, `IntakeResult` exist. **BUILD GAP**: channel, media refs, slot, OEM ticket no., source channel |
| Job card (NEW) | fault reported, fault found, nature of service, action taken, parts used (code, qty, price), charges, payment mode, customer OTP or signature, technician id | **BUILD GAP**. Nature of service is mandatory (UNVERIFIED legal relevance, but Howrah case faulted its absence) |
| State transition | from_state, to_state, actor, actor_type, reason, approval_ref, evidence | Table `state_transitions`, `Actor` exist |
| Audit log | actor, role, action, entity, payload | `audit()` exists |
| Quote (NEW) | line items (visit, parts, labour), approval event | `QUOTED` and `CUSTOMER_APPROVED` states exist. Quote entity **BUILD GAP** |
| Part catalogue entry (NEW) | model, part code, confirmed-by (technician repair id), date | **BUILD GAP**. Needed before any compatibility claim |
| Claim (NEW) | plan_id, serial, invoice, plan start, damage type, photos, prior claims, decision, reason code | **BUILD GAP** (Scenario C) |
| Exit case (NEW) | unit id, grade, route, 180-day storage start, receiver registration no. | **BUILD GAP** (Scenario E) |
| Consent (NEW) | principal, purpose, recipient, granted, withdrawn | **BUILD GAP** |

### 2.2 Field provenance and verification

The build has `Provenance = customer | history | ai_inferred | operator | unknown` and a `Field {value, provenance, evidence, source_ref}`. Keep it. The notes (UNVERIFIED inference) also want a verification state.

| Add | Values | Why |
|---|---|---|
| Source (extends Provenance) | `invoice_scan`, `oem`, `agency_signed`, `technician` | **BUILD GAP**. Separates OCR, OEM and signed entries from self-report |
| Verification state | self_reported, OCR-confirmed, agency-signed (OTP or job-card ID), owner-approved | **BUILD GAP**. Needed for claim evidence |

### 2.3 Who may write each part of the record

| Data | Customer (owner) | Household member | Agency operator | Technician | Agency admin | Administrator or OEM | System (AI) |
|---|---|---|---|---|---|---|---|
| Appliance identity and invoice | write, confirm | add events, view | propose | propose (photo of nameplate) | propose | supply activation date, service history (API) | propose from OCR; never confirm |
| Warranty terms | confirm | view | propose | no | propose | supply | propose; never set eligibility |
| Service request and job card | create, approve quote | view | write, approve AI draft | write repair fields | all agency jobs | read-only on shared jobs | draft intake, never close |
| Repair history entry | approve before it is shown as verified | view | propose | propose | propose | no | no |
| Claim decision | no | no | no | no | no | decide | recommend only |
| Consent | grant, withdraw | own data only | no | no | no | no | no |

Roles in the build are `agency_admin, agency_operator, technician, customer, eval_admin`. **BUILD GAP**: add `household_member`, `administrator` (warranty or OEM), and a read-only `refurbisher_or_recycler` for E. `eval_admin` stays internal.

### 2.4 Consent and visibility (consent-first)

DPDP Rules were notified 14 Nov 2025. Core duties (notice, consent, withdrawal, breach reporting) apply about May 2027, sources differ on the exact day (Sourced). Existing SPDI Rules continue meanwhile. No check was made for later amendments (UNVERIFIED). The rules below are design choices from general principles (UNVERIFIED), applied from day one.

| Rule | Detail |
|---|---|
| Purpose-bound consent | Separate consent for reminders, claim help, sharing with an agency, and sharing with an administrator or OEM |
| Per-disclosure consent | Each share of an invoice or history with a third party is its own grant |
| Withdrawal and deletion | Per purpose. Withdrawal stops new use. Audit entries stay but drop personal data where allowed |
| Each person is a principal | Names, phones and addresses of other household members are hidden unless that person consents |
| Agency view | Agency sees the appliances and history the owner shared with it, nothing else |
| Tenant limit | Tenant sees limited view. Appliance may belong to the landlord (Sourced: warranty is often first-purchaser only) |
| Owner approval | Agency repair entries are proposals until the owner approves |
| Audit | Every read of shared history by another party is logged |
| Children's data | Rules not retrieved. Do not collect (UNVERIFIED) |

---

## 3. Scenario A: Prepared Visit (agency AI desk)

### 3a. Trigger points

| # | Event | Fired by | Condition or threshold | System action | Evidence |
|---|---|---|---|---|---|
| A1 | New complaint | WhatsApp webhook `messages[]` | New `wa_id`, or no open job for that `wa_id` | Create request `NEW`, run intake, write `IntakeResult` | Webhook shape Sourced. Flow UNVERIFIED |
| A2 | Voice note received | Webhook `type: audio` | Any audio message | Send audio to Gemini, extract fields, keep transcript | Limits Sourced. Voice-note format OGG/Opus UNVERIFIED |
| A3 | Call transcript arrives | Telephony or Live API session end | Transcript attached to a phone number | Same intake path | UNVERIFIED |
| A4 | Missed call | Telephony event | No open call | Send utility template offering WhatsApp intake | UNVERIFIED. Template rule Sourced |
| A5 | Safety keyword | Rules engine plus model on any message or voice note | Any hard-stop hazard (section 3d) | Status `SAFETY_ESCALATED`, hard-stop reply, priority alert to operator | List UNVERIFIED, needs expert review |
| A6 | Missing fields | Intake result | `missing_info` not empty | Status `NEEDS_INFO`, send follow-up questions | Build has `NEEDS_INFO`. Trigger UNVERIFIED |
| A7 | Customer silent | Timer since last outbound | Threshold set per agency. Inside 24 h window free-form allowed, outside only a template | Retry or close; log `failed` status | Window rule Sourced (third party). Threshold UNVERIFIED |
| A8 | Repeat complaint | Matcher on phone, serial, address | Prior closed job within N days. N is agency or OEM policy, not found | Flag `repeat`, copy prior history, notify operator | UNVERIFIED. Repeat job sheets matter in consumer cases (Sourced, secondary) |
| A9 | Duplicate complaint | Matcher | Open job, same appliance | Link, do not create a second job | In `IntakeResult.duplicate`. Rule UNVERIFIED |
| A10 | Triage ready | Intake plus history plus manual retrieval | Appliance, symptom present | `TRIAGED`, job card draft to operator | UNVERIFIED |
| A11 | Quote sent and answered | Operator sends, customer replies | Customer approval event | `QUOTED` to `CUSTOMER_APPROVED` | States exist |
| A12 | Part unavailable | Technician or parts input | Part not in stock | Status "awaiting part", utility template with ETA | UNVERIFIED. **BUILD GAP**: no such state (see 3e table) |
| A13 | Technician finishes | Technician form | Fault found, action taken, parts, signature or OTP present | `REPAIR_RECORDED` to `VERIFICATION_PENDING`, closure message, feedback request | States exist. Fields UNVERIFIED |
| A14 | Fix verified | Test result or customer confirmation | Passed test or customer confirms | `VERIFIED`, write repair to record, raise per-verified-fix fee event | Fee basis is in the one pager |
| A15 | Customer reopens | Customer message | After `VERIFIED` | `REOPENED`, reason required | Build requires reason |
| A16 | Dispute | Customer or operator | Disagreement at verification | `DISPUTED`, human only | State exists |

### 3b. Inputs

| Input | Who gives it | Channel and format | Required? | Validation or limit | If missing |
|---|---|---|---|---|---|
| Phone, name | Customer (`wa_id`, profile name) | WhatsApp webhook metadata | Required | Validate phone format in code | Ask customer |
| Address, pincode, landmark | Customer | WhatsApp text, form | Required for dispatch | Validate pincode in code (schema constraints ignored by Gemini) | Ask; do not schedule |
| Appliance type, brand | Customer, or history | Text, voice, photo | Required | Enumerated list; check against history | `IDENTIFY_APPLIANCE` |
| Model | Customer photo of nameplate, or history | Photo, text | Optional, strongly wanted | Photo: PNG, JPEG, WEBP, HEIC, HEIF; 20 MB inline total | `ASK_MODEL`; part claims off |
| Serial | Photo or history | Photo | Optional | Format check in code | Part claims off; repeat match weaker |
| Symptom, duration | Customer | Text, voice | Required | Keep verbatim snippet as evidence | `ASK_PROBLEM_DETAILS` |
| Error code | Customer photo of display, or text | Photo, text | Optional | Never decode from model memory. Ground on the model's manual (Sourced: codes vary by brand and model, third-party lists conflict) | Ask customer to photograph display |
| Voice note | Customer | WhatsApp audio, OGG/Opus likely | Optional | Gemini audio: 9.5 h per prompt, 20 MB inline, use Files API beyond. Formats incl. OGG, Opus, MP3, WAV, M4A | Fall back to text request |
| Photos | Customer, technician | WhatsApp image | Optional | Up to 3,600 images per request, 20 MB inline | Proceed without |
| Preferred slot | Customer | Text | Optional | Parse and confirm | Operator sets |
| Warranty claim Y/N, OEM ticket no. | Customer, OEM forward | Text, OEM forward (format not found) | Optional | UNVERIFIED format | Treat as out of warranty until shown |
| Prior history | System | Record read (see section 2) | Auto | Read only what the owner shared with this agency | Say "no history found" |
| Service manuals | OEM or agency admin | PDF upload to retrieval store | Optional | File Search: 100 MB per document, citations with file name and page | Mark "not verified, inspect first" |
| Part catalogue | Technician-confirmed repairs, OEM | Catalogue table | Optional in R1 | Must be structured | Compatibility stays "not verified" |
| Technician fields | Technician | Form or voice note | Required at close | Fault found, action taken, parts, signature or OTP | Block `REPAIR_RECORDED` |
| Agency policy (repeat window N, retry timers) | Agency admin | Settings | Required config | Defaults needed (UNVERIFIED) | Use default, flag |

### 3c. Outputs

| Output | Receiver | Channel and format | Human review before effect? | Never allowed to claim |
|---|---|---|---|---|
| `IntakeResult` (intake.v1) | Operator | Dashboard JSON | Operator reviews before dispatch | A field as customer-given if it was inferred. Build tags `provenance` |
| Safety hard-stop message | Customer, operator | WhatsApp text in the customer's language | No delay for the stop message. Operator must approve any move out of `SAFETY_ESCALATED` (build needs reason) | That the situation is safe, or that a repair is possible remotely |
| Follow-up questions | Customer | WhatsApp text or voice | No | Anything about cost or cover |
| Technician job card | Technician | App card or WhatsApp | Operator approves | Part compatibility without a catalogue entry. Fault cause as certain. Error-code meaning without manual citation |
| Likely faults with evidence | Technician | Card, cites manual page | Operator approves | Certainty. Must show evidence per fault |
| Parts to carry | Technician | Card list | Operator approves | "Compatible" unless catalogue confirms. Otherwise "not verified, inspect first" |
| Quote | Customer | WhatsApp utility template | Operator approves | Final price before inspection |
| Status messages (registered, assigned, on the way, awaiting part, done) | Customer | WhatsApp utility templates | Pre-approved templates | Anything outside the template |
| Repeat flag with prior history | Operator | Dashboard | Operator decides | That the first repair failed or who is at fault |
| Closure message and feedback request | Customer | WhatsApp | No | Payment received without provider event or agency confirmation |
| Repair entry to record | Owner (approval), record | Record write | Owner approves verified status | Verified without test or confirmation |

### 3d. Abstain and escalate cases

| Case | Behaviour |
|---|---|
| Hard-stop hazards (UNVERIFIED list): burning smell or smoke, sparks, shock or tingling, water near live parts or wet sockets, gas smell or gas geyser, hot or swollen compressor, refrigerant hiss or leak, melted plug | Stop troubleshooting. Tell customer to isolate power or gas and wait. Priority alert. Never advise opening panels, handling refrigerant or bypassing fuses |
| Safety text ambiguous | Treat as hazard. Operator reviews |
| Appliance not identified | `IDENTIFY_APPLIANCE`. No fault list |
| No manual for the model | Give questions and generic checks only, label "not verified" |
| Language not understood or low transcript confidence | Ask in text. Mark `LangCode` `unknown` |
| Conflicting history (two serials, repeat across agencies) | Show both, flag, operator decides |
| Model output fails validation | Fall back to rules (`demo-rules` engine path exists), set `fallback_reason` |
| Out-of-scope request (legal advice, price dispute) | Route to human |

### 3e. Google components

| Component | Where used | Status and limits that affect design |
|---|---|---|
| AI Studio | Prompt and schema prototyping, evals before code | Export to Antigravity (reported, I/O 2026) |
| Antigravity 2.0 | Build agent workspaces | Reported launched May 2026. Managed Agents are preview |
| Agent Skills | Safety escalation, job-card generation, catalogue-only compatibility check | Antigravity reads `SKILL.md` (reported) |
| Gemini Flash tier | Intake, voice and photo reading | Model names conflict across sources (3.5 vs 3.8 Flash). Confirm in AI Studio |
| Gemini Pro-tier model | Harder diagnosis | Cost per job unmeasured |
| Structured output | `IntakeResult` | `minLength`, `maxLength`, `uniqueItems` silently ignored. `minItems`, `maxItems` enforced. Deep schemas can 400. Validate in code. Combining with tools is preview on Gemini 3 and 4 |
| Function calling | Record read, catalogue check | Modes AUTO, ANY, NONE with `allowed_function_names` (Vertex doc, assumed same for Gemini API) |
| File Search | Manuals retrieval | 100 MB per document. Not combinable with Google Search or URL Context. **Not supported in Live API** |
| Live API | Voice intake | WebSocket. Input PCM 16-bit 16 kHz, output 24 kHz. Preview items. Session limit and Indian-language accuracy not verified. A voice agent must fetch manual text by function call to a separate retrieval service |
| Maps Routes | Technician matching | Not needed in R1 (see build order) |
| Not Google | WhatsApp Business API | Free-form replies and in-window utility templates reportedly billable from 1 Oct 2026. Verify before costing |

### 3f. Pilot success metric

- **Primary:** share of jobs closed with one visit, compared against each pilot agency's own prior record. Baseline comes from the agency, not from this spec. No national rate was found.
- **Cost check:** Gemini cost per job against the per-verified-fix fee.
- **Safety check:** every safety-flagged complaint received a hard-stop reply before any troubleshooting. Target is all of them.

---

## 4. Scenario B: Home Memory, Plans, and consumer help (D folded in)

### 4a. Trigger points

| # | Event | Fired by | Condition | System action | Evidence |
|---|---|---|---|---|---|
| B1 | Invoice uploaded | Owner | PDF or photo received | Extract fields, show confirm screen | Document AI limits Sourced |
| B2 | Agency job verified | Module A (A14) | Owner has shared consent with agency | Propose repair entry to owner | Owner approval UNVERIFIED |
| B3 | Nameplate photo added | Owner or technician | Model or serial found | Propose model and serial, owner confirms | UNVERIFIED |
| B4 | Warranty ending | Date rule | End date minus 60, 30, 7 days | Reminder, with consent | Cadence is a design choice, not sourced |
| B5 | Seasonal AC service | Calendar | Before summer; at least once a year | Reminder, offer agency booking | Sourced (Hitachi, TCL) |
| B6 | RO filter due | Time since last service | Pre-filter 6 to 12 months, carbon about a year, membrane 2 to 4 years | Reminder | Sourced (vendor blogs, model-specific) |
| B7 | Washing machine or fridge due | Time since last service | Only monthly drum clean found for washers; no fridge source | User-configurable default | UNVERIFIED |
| B8 | Plan ending | Date rule | End date minus N days | Renewal offer | N is design choice |
| B9 | Old appliance | Age rule | Older than about 5 years | Offer plan | Godrej threshold, Sourced |
| B10 | Complaint from owner | Owner message | Any | Open request via A, history attached | Cross-module |
| B11 | Repeat visit from A | A8 | Same appliance | Read history for A | Cross-module |
| B12 | Quote to check | Owner uploads a quote | Quote present | Fair-price view | Source for price data not found. UNVERIFIED |
| B13 | Claim help requested | Owner | Defective in warranty | Build evidence bundle | Sourced channels (NCH, e-Daakhil) |
| B14 | Consent withdrawn | Owner | Any | Stop that purpose | Design rule |

### 4b. Inputs

| Input | Who gives it | Channel and format | Required? | Validation or limit | If missing |
|---|---|---|---|---|---|
| Invoice | Owner | Photo or PDF upload | Required for warranty | Document AI Invoice Parser: online 40 MB and 15 pages (30 in imageless mode). Hindi not listed. Region asia-south1 (v2.0 not available there) | Ask to upload. Record stays "unverified warranty" |
| Seller GSTIN, invoice no., date | OCR | Fields `supplier_tax_id`, `invoice_id`, `invoice_date` | Required | GSTIN mapping UNVERIFIED, test on samples. Invoice no. max 16 chars (Rule 46, secondary sources disagree on field count) | Owner types in |
| Model and serial | Owner, technician photo | Photo, text | Required for claim | **Parser has no model or serial field**. Use custom extractor or Gemini pass, then owner confirms | Owner photographs nameplate |
| Warranty start and basis | Owner | Form | Required | Start can differ from invoice date (UNVERIFIED per brand). Owner can override | Default to invoice date, flagged |
| Warranty terms per component | Owner photo of card or OEM page | Photo, text | Optional | Store per component. Warranty card layout not verified | Show "terms unknown" |
| Plan details | Owner, plan provider | Photo, upload | Optional | Plan is a separate record | Skip |
| Repair events | Agency | API or job card | Auto | Proposal until owner approves | None |
| Household members | Owner | Invitation | Optional | Per-member consent | Owner only |
| Reminder preferences | Owner | Form | Required before any reminder | Opt-in | No reminders |
| Complaint log and payments | Owner, agency | Auto, upload | Optional | Dated | Chronology shows gaps |
| Quote | Owner | Photo or PDF | Optional (fair-price) | Same Document AI limits | Skip |

### 4c. Outputs

| Output | Receiver | Channel and format | Human review? | Never allowed to claim |
|---|---|---|---|---|
| Appliance record | Owner | App, WhatsApp summary | Owner confirms OCR fields | Verified status without confirmation |
| Warranty status view | Owner | Card with evidence | Shown as "per your terms, unconfirmed" until evidence is verified | Warranty eligibility without evidence. Cover that was not entered |
| Reminders | Owner | WhatsApp utility template | Opt-in required | Overdue service as a defect |
| Plan renewal offer | Owner | WhatsApp, app | Plan seller approves terms | Plan terms or price the system does not hold. Insurance cover until the licence question is closed |
| Repair history for A | Agency | Record read | Owner consent | Anything the owner did not share |
| Fair-price view | Owner | Card | None, but labelled indicative | Overcharge, without benchmark data. Data source not yet found |
| Claim evidence bundle | Owner | Chronology, party memo, invoice PDF, size check | Owner reviews before sending | That the claim will succeed. Legal advice |
| Draft complaint to OEM or NCH | Owner | Text | Owner sends | Filing happened |

e-Daakhil facts (secondary sources, verify): uploads of index, list of dates and events, memo of parties, complaint with affidavit; PDFs up to 5 MB each; fee nil up to Rs 5 lakh; two-year limitation. One source says e-Daakhil now runs via e-Jagriti (single source).

### 4d. Abstain and escalate

| Case | Behaviour |
|---|---|
| Invoice unreadable or low confidence | Confirm screen, no auto-save |
| Serial mismatch between invoice and unit | Flag, owner decides |
| Warranty start after reported fault date | Flag as timeline conflict, not as fraud (sourced from ombudsman decisions, case read via summary) |
| Tenant or resale unit | Mark first-purchaser rule, no eligibility statement |
| Conflicting history between agencies | Show both with source |
| Legal questions | Refer to a human; say what the record holds |
| Safety text in any B conversation | Hand to A hard-stop path |

### 4e. Google components

| Component | Where | Status and limits |
|---|---|---|
| Document AI Invoice Parser | Invoice to fields | Built for business invoices. Latin-script European languages only, English included. No Hindi. No model or serial field. Regions include asia-south1. v2.0 not in asia-south1 |
| Document AI custom extractor | Model, serial, warranty text | Generative, v1.5 only, no fine-tuning, available in asia-south1 |
| Expense Parser | Receipts fallback | No asia-south1, 10 page limit |
| Gemini Flash | Confirm-screen extraction, photo reading | Structured output caveats as in A |
| Gemini Pro | Chronology and complaint drafting | Validate dates and amounts in code |
| Gmail import | Not used | Restricted-scope verification needed. Start with upload |

### 4f. Pilot success metric

- Share of agency jobs that end with an owner-approved record entry.
- Share of invoices that reach a confirmed model and serial after the confirm screen.
- Whether history makes repeat matching in A work (matches found that A alone would have missed).
- Plan attach rate is measured, not targeted.

---

## 5. Scenario C: Claims triage for administrators and OEM networks

### 5a. Trigger points

| # | Event | Fired by | Condition | System action | Evidence |
|---|---|---|---|---|---|
| C1 | Claim raised | Customer via administrator app, or administrator API | Claim file received | Open claim, run triage | Intake channels Sourced (OneAssist app, forms). API spec not public |
| C2 | Claim file incomplete | Triage | Missing document or photo | Request more info | Required documents Sourced (form, invoice, ID, photos) |
| C3 | Plan activation | Administrator | Plan sold | Capture device details and images | OneAssist cancels if not given within 15 days (Sourced) |
| C4 | Eligibility signal | Rules | Plan start after loss date, serial or invoice mismatch, repeat claim on same serial, waiting period | Flag for adjudicator | Signals UNVERIFIED for India. Timeline conflict not equal to fraud (Sourced) |
| C5 | Safety complaint in claim | Same hard-stop list as A | Any hazard | Stop and escalate | UNVERIFIED |
| C6 | Triage complete | Engine | Evidence collected | Recommendation to adjudicator | UNVERIFIED |
| C7 | Visit prepared | Engine | Route to repair chosen | Job card via A | Reuses A |
| C8 | Technician diagnosis done | Agency | Diagnosis and cost in | Repair or replace inputs complete | UNVERIFIED |
| C9 | Repair failed or parts delayed | Agency | Repeat repair count above policy | Flag replace review | Threshold is a design choice |

### 5b. Inputs

| Input | Who gives it | Channel and format | Required? | Validation or limit | If missing |
|---|---|---|---|---|---|
| Policy or plan ID, customer contact | Administrator | API | Required | Match to record | Reject triage |
| Product, brand, model, serial | Customer, retailer, OEM | Form, API | Required | Serial format in code | Request |
| Invoice | Customer, retailer | PDF, photo | Required | Document AI limits as in B | Request |
| Plan start date | Administrator | API | Required | Compare to loss date | Flag |
| Fault description, damage type | Customer | Text, voice, photo | Required | Damage type from list: accidental, liquid, electrical, wear | Request |
| Photos, video | Customer | Upload | Required | Image limits as in A | Request |
| ID proof | Customer | Upload | Required by some administrators | Sourced for OneAssist | Request |
| Prior claims | System, administrator | Record read | Auto | None | State "none found" |
| OEM activation date and service history | OEM | API | Optional | Vendor claim only | Skip |
| Technician diagnosis, parts, estimate | Agency | Job card | Required for repair-vs-replace | From A | Hold decision |
| Product value or plan limit | Administrator | API | Required for repair-vs-replace | Replace threshold is a design choice | Hold |
| Parts availability and ETA | Agency, catalogue | API | Optional | None | Mark unknown |

### 5c. Outputs

| Output | Receiver | Channel and format | Human review? | Never allowed to claim |
|---|---|---|---|---|
| Triage recommendation (approve, deny with reason code, route to repair, replace, cash settle, request more info) | Adjudicator | Dashboard, API JSON | **Yes. Adjudicator decides every time** | Fraud. The system flags signals only |
| Evidence summary with citations | Adjudicator | Dashboard | Reviewed with decision | Warranty or plan cover without records |
| Flags and reasons | Adjudicator | Dashboard | Yes | Fraud, intent, or a tampered document as fact |
| Prepared visit | Agency | Job card (A) | Operator approves | Compatibility without catalogue |
| Request-more-info message | Customer | Channel of the administrator | Administrator template | Rejection |
| Repair-vs-replace view | Adjudicator | Dashboard | Yes | That a threshold is policy. Thresholds are configured by the administrator |

### 5d. Abstain and escalate

| Case | Behaviour |
|---|---|
| Hard-stop hazard | Same as A. Claim paused, safety path first |
| Evidence thin or contradictory | Output "insufficient evidence" and a list of what is missing |
| Serial or invoice mismatch | Flag, never decline |
| Plan start after loss | Flag as timeline conflict |
| Customer identity doubts | Route to administrator's own check |
| Repeat claims across providers | Flag only with records shared under consent |
| Anything affecting money | Adjudicator signs |

### 5e. Google components

| Component | Where | Status and limits |
|---|---|---|
| Gemini Pro | Claim classification, evidence summary | Structured output validated in code |
| Gemini Flash | Photo and text reading | As in A |
| Document AI | Invoice | As in B |
| File Search | Plan terms, manuals | Not in Live API |
| Agent Skills | Claim triage skill packaged from A's skills | Antigravity feature |
| Live API | Not used | Claims are not voice-first (UNVERIFIED) |

### 5f. Pilot success metric

- Agreement rate between the engine's recommendation and the adjudicator's decision, on the same claims.
- Time from claim received to adjudicator decision, against the administrator's own record. No Indian SLA benchmark was found.
- Share of flags the adjudicator found useful.

---

## 6. Scenario D (folded into B): consumer claim and fair-price advocate

D has no separate module. It is the claim-help and fair-price features in B.

| Item | Where in this spec |
|---|---|
| Triggers | B12, B13 |
| Inputs | Invoice, complaint log, quote (section 4b) |
| Outputs | Evidence bundle, draft complaint, fair-price view (section 4c) |
| Abstain | Legal questions go to a human. Fair price is labelled indicative until a data source is found |
| Metric | Share of claim bundles the owner sends without edits and the share complete under e-Daakhil upload rules. Willingness to pay is not proven (scenarios file) |

D's payer is unproven. It stays an acquisition channel for B.

---

## 7. Scenario E: Circular loop (vision, briefer)

| Block | Content |
|---|---|
| Triggers (all UNVERIFIED design views) | Replacement purchase with exchange offer; buyback acceptance; claim outcome of replace or settle (C); unit unrepairable (A); plan end |
| Inputs | Category, brand, model, age (invoice or label), working status, symptom checklist, photos (all sides plus label plate), accessories, pickup location, invoice presence. Providers: owner, then an inspector at pickup (final grade). Photos on the same limits as A |
| Outputs | Provisional grade (A, B, C, scrap), price band, route (refurb, harvest, scrap). Receivers: owner, refurbisher, recycler. Provisional quote is not final. Final grade is set at physical inspection (UNVERIFIED) |
| Data carried with each unit (schema UNVERIFIED) | Unit ID, serial, category, brand, model, weight, collection date, collector, storage start for the 180-day clock, receiver registration number, outcome, certificate reference |
| Human review | Inspector sets the final grade. Partner confirms receipt |
| Never claim | Final price from photos. EPR certificate value. Refurbished unit warranty the partner has not agreed to |
| Abstain | Safety hazards (gas, leaking refrigerant) need handler escalation. Photo unclear: ask again. Unit lacks serial: grade only as scrap or harvest candidate |
| Google | Gemini vision for grading; Maps Routes for pickup batching. No Document AI role beyond invoice |
| Metric | Agreement between photo grade and inspection grade. Offer survival rate after inspection (the re-quote friction) |
| Dependencies | Partner registration on the CPCB portal; Delhi High Court outcome on the price floor; unit-level traceability fields not found in sources |

---

## 8. Cross-scenario event map

| Event | First handler | Hands off to | What passes |
|---|---|---|---|
| New complaint | A | B (history read) | `appliance_id`, phone, serial |
| Repeat complaint | A | B (read), then agency | Prior jobs. B supplies the record, A raises the flag |
| Safety keyword | A, B, C or E | A hard-stop path | Hazard code, evidence |
| Agency job verified | A | B (write) | Repair entry as proposal to owner |
| Invoice uploaded | B | A (later jobs read it) | Confirmed model, serial, warranty terms |
| Warranty ending | B | Owner, then A (booking) | Reminder, booking intent |
| Plan ending | B | Plan seller | Renewal lead |
| Claim raised | C | A (visit), B (record) | Claim file in; triage out |
| Claim triage | C | A | Reuses A's triage and job-card skills for the field visit |
| Diagnosis done | A | C | Diagnosis, parts, estimate |
| Claim outcome replace or settle | C | E | Unit ID, reason |
| Unit unrepairable | A | E | Unit ID, history |
| Owner claim help | B | NCH or e-Daakhil (owner files) | Chronology, memo, invoice |
| Consent withdrawn | B (consent store) | All | Stop, delete, log |
| Fix verified | A | B, then C (history for later claims) | Repair, parts, test |

---

## 9. Build order

### Release 1: Scenario A end to end

| Must include | Notes |
|---|---|
| WhatsApp intake (text, voice, photo) | Webhook for `messages[]`; templates registered and approved |
| `IntakeResult` with Gemini and rules fallback | Build has both engines (`demo-rules`, `gemini`) |
| Safety hard stop and `SAFETY_ESCALATED` flow | Build exists. Expert review of hazard list |
| History read and repeat or duplicate flag | Build has `history`, `repeat`, `duplicate` |
| Job card and technician close form | **BUILD GAP** |
| Quote entity and approval | **BUILD GAP** |
| Awaiting-part state | **BUILD GAP**. Needs a state and a transition, for example from `ON_SITE` or `SCHEDULED` |
| Safety release path to dispatch | **BUILD GAP**. `SAFETY_ESCALATED` can only go to `TRIAGED` or `CANCELLED`. Priority dispatch needs to go via `TRIAGED` and `SCHEDULED` |
| Appliance and invoice fields (serial, seller, invoice no.) | **BUILD GAP** |
| Channel, media refs, OEM ticket no. on request | **BUILD GAP** |
| Consent store and agency-share consent | **BUILD GAP** |
| Role additions | **BUILD GAP**: `household_member`, `administrator` |
| Per-verified-fix fee event | Pricing basis in one pager |

| Stubbed in R1 | Why |
|---|---|
| Live API voice agent | Use transcript path first. Preview status, session limits not verified |
| Part catalogue | Every card says "not verified, inspect first" until entries exist |
| Manual retrieval | Start with a few manuals in File Search |
| Maps Routes | Operator assigns by hand |
| OEM job-forward | Format not found |
| Payment | No provider event, so no payment claims |
| Home Memory app | Records arise from agency jobs (cold-start answer in scenarios file) |

### Later releases

| Release | Adds |
|---|---|
| R2 (B, D folded in) | Document AI invoice path with confirm screen; owner approval of repair entries; reminders; plan records; claim evidence bundle; household members; full consent |
| R3 (C) | Administrator role and API; claim entity; eligibility flags; repair-vs-replace inputs; adjudicator dashboard. Needs outcome proof from A |
| R4 (parts) | Catalogue built from technician-confirmed repairs; compatibility claims switch on only for confirmed entries; Maps Routes |
| Vision (E) | Exit case entity, vision grading, partner routing, 180-day clock |

---

## 10. Open items and unverified assumptions

| # | Gap | Source note | Closed by |
|---|---|---|---|
| 1 | Channel mix for small agencies unknown | Agency | Interview 15 to 20 agencies |
| 2 | OEM job-forward format (SMS, app, portal) unknown | Agency | Ask agencies for real forwarded jobs |
| 3 | Real OEM job card forms (LG, Samsung, Whirlpool, Voltas) not retrieved. Field list UNVERIFIED | Agency | Collect sample cards from pilot agencies |
| 4 | Fridge error codes and Indian manual structure not researched | Agency | Pilot manuals plus technician review |
| 5 | Safety hard-stop list has no source | Agency | Review by a domain expert and a technician panel |
| 6 | Repeat-complaint N days, SLA norms, escalation rules not found | Agency | Agency interviews; set per-agency config |
| 7 | Real customer message samples none | Agency | Pilot capture with consent |
| 8 | WhatsApp 24 h window page not read directly; India opt-in rules not read; 1 Oct 2026 billing change from third parties only | Agency | Read Meta pricing and policy pages; test one template |
| 9 | Live API session limit, model names, pricing not verified. Model names conflict (3.5 vs 3.8 Flash) | Agency, scenarios | Check in AI Studio |
| 10 | Voice accuracy in Hindi, Telugu, Tamil on noisy lines not shown | Scenarios | Test on recorded real complaints |
| 11 | Cost per job vs per-fix fee unmeasured | Scenarios | Pilot at fee levels in the scenarios file |
| 12 | Agency willingness to pay and whether fewer visits appeals | Scenarios | Paid pilot, 3 to 5 agencies |
| 13 | Warranty card layout and clock start (purchase vs install) per OEM not confirmed | Household | Read OEM terms for pilot brands; test owner override |
| 14 | 30-day registration claim only from one third-party page | Household | Check OEM page |
| 15 | GSTIN mapping to `supplier_tax_id`; Document AI accuracy on Indian invoices, thermal prints, WhatsApp photos; no Hindi; no pricing or quotas retrieved | Household | Run 50 to 100 sample invoices through Invoice Parser and a custom extractor |
| 16 | Model and serial capture path | Household | Custom extractor test plus confirm screen |
| 17 | Fridge and washer service intervals; reminder cadence 60/30/7 is design choice | Household | User-configurable defaults; pilot opt-out data |
| 18 | AMC annual prices for AC, RO, washer, fridge not found | Household | Plan seller quotes |
| 19 | NCH required fields, OEM toll-free and app requirements not checked; e-Jagriti change single-sourced; legal notice not confirmed | Household | Read portal and official rules; legal reviewer |
| 20 | DPDP: no check for amendments after Nov 2025; consent notice text, withdrawal mechanics, children's rules not read from primary text | Household | Check MeitY; counsel review before R2 |
| 21 | Household sharing norms and verification practice unresearched | Household | Owner interviews |
| 22 | Rule 46 field count differs between sources | Household | Verify against CBIC text |
| 23 | Claims: no public Indian SLAs, claim API specs, fraud rules, or repair-vs-replace thresholds | Claims | Interview two administrators or OEM service heads |
| 24 | Servify claims (65K locations, OEM integrations) are vendor claims | Claims | Treat as unproven; ask administrators |
| 25 | IRDAI and consumer rules on service-contract TAT and plan selling | Claims, scenarios | Sector counsel before promising plan commission |
| 26 | Buyback grading inputs for large appliances not public; Refwash 22-point count ambiguous; Costify, Underdog method not public | Claims | Visit a refurbisher; get grading sheet |
| 27 | EPR: gazette and CPCB portal field lists not read; which categories apply; refrigerant handling; storage-entity type; certificate rules at summary level | Claims | Read gazette and portal; talk to a registered refurbisher and recycler |
| 28 | No source ties claim outcome to e-waste routing (novel link) | Claims | Pilot with one administrator and one recycler |
| 29 | Delhi High Court ruling on EPR price floor unresolved | Scenarios | Monitor |
| 30 | Plan-selling licence and whether agencies can sell service contracts | Scenarios | Counsel |
| 31 | Existing build not reviewed in the scenarios file. This spec reviewed only `types.ts` and `workflow.ts` | Scenarios | Review remaining server and web code before R1 plan |
| 32 | Fair-price data source not found | Scenarios | Agreed-price data from pilot jobs |
