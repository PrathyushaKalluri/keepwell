# KeepWell: idea submission answers

## 1. Provide one sentence summary of your new product/project that you are planning to build.

KeepWell is an AI repair desk on WhatsApp for appliance repair agencies: it turns customers' voice notes and photos in Telugu or Hindi into prepared technician visits with clear quotes, then saves each verified repair to a lasting history of the appliance.

## 2. What is the main problem that you are solving with the new product idea?

Independent appliance repair agencies get incomplete complaints through calls and WhatsApp voice notes, with no model number and no repair history. Technicians then often arrive without the right part or a clear diagnosis, which leads to avoidable repeat visits and price disputes. Households are also left with no reliable record of their appliances' warranties and past repairs.

## 3. Who would be a typical user/customer?

The owner of an independent appliance repair agency in a Tier 2 or Tier 3 Indian city such as Warangal or Vijayawada. They run 2–10 technicians who fix fridges and ACs, and take most bookings through phone calls and WhatsApp in Telugu or Hindi. They pay because they want fewer wasted trips, faster quotes and fewer price disputes. The secondary user is the household that owns the appliance: it uses KeepWell free through WhatsApp to report problems, approve quotes and keep a record of its appliances.

## 4. What is your solution to this problem?

KeepWell is an AI repair desk that works inside WhatsApp. It reads the customer's voice note or photo in Telugu or Hindi, reads the model and serial number from a label photo, and pulls up the appliance's past repairs. Hazards such as a gas smell or sparking go straight to a person. It then suggests likely faults backed by the service manual, confirms the part against a catalogue (or asks the technician to inspect first if the model is unknown), and assigns a technician and time slot. The quote comes from the agency's own rate card and is approved by the agency and the customer before any payment. After the visit, the technician's voice note becomes the repair record and, once the customer confirms, is saved to the appliance's history. Money, safety and final decisions always come from rules or a person, never the AI alone.

## 5. What is the stage of your product or project?

Idea and design stage. The product spec, solution architecture, AI evaluation plan and pricing hypotheses are written. The working prototype will be built at the City Buildathon; there is no live product, pilot or customer data yet. Next, we will interview 15–20 repair agencies in one Tier 2 city and then run a paid pilot.

## 6. What is the potential business model of this product?

B2B subscription priced per technician, with the first 60 days free (all prices to be tested in the pilot). Starter, for owner-run agencies: ₹1,499 per technician per month, including 60 AI-handled jobs per technician, then ₹10 per extra job. Pro, for service centres and brand-authorised networks: ₹2,499 per technician per month, adding route optimisation, parts management, multi-branch support and analytics. Enterprise, for appliance brands and plan providers: annual contracts at ₹30–100 per claim checked and ₹100–250 per routed repair job. Households use KeepWell free; their records keep them with the agency. Later revenue with partners: service-plan commissions, genuine-parts referrals, resale and recycling. One Starter technician costs us about ₹90–600 a month to serve, and pays for itself if it saves an agency 3–4 wasted visits a month.

## 7. Who will be your primary competitor(s) and how is your solution different from them?

Urban Company sells consumer bookings for home services, using its own network of technicians. Servify runs warranty and after-sales programmes for brands. Field-service software such as Fieldproxy and Zuper manages tickets and dispatch, mostly in English. The real everyday competitor is the agency's own phone, notebook and WhatsApp. KeepWell is different in three ways. It works for the independent agency rather than taking its customers. It works in WhatsApp, in Telugu and Hindi voice notes, so no new app or typing is needed. And it prepares each visit with evidence (model, history, manual-backed fault ideas, verified parts), then keeps a verified repair history for every appliance that the household controls and the next technician can use.

## 8. What will be your primary and secondary target countries, if applicable?

Primary: India, starting with Tier 2 and Tier 3 cities in Telangana and Andhra Pradesh (Telugu and Hindi), then other Indian states and languages. Secondary, later and subject to research: other WhatsApp-first markets with large independent repair sectors, such as Bangladesh, Indonesia and the UAE.

## 9. How are you planning to use AI for this solution?

AI handles the messy, language-heavy parts of a repair job, and rules and people handle the decisions. AI transcribes Telugu and Hindi voice notes and pulls out the complaint, then asks one or two useful follow-up questions. It reads model and serial numbers from label and invoice photos. It suggests likely faults, citing the service manual and the appliance's past repairs, and says "inspect first" when evidence is weak. It drafts the technician brief and the customer message. After the visit, it turns the technician's voice note into a structured repair record and flags repeat failures. Prices, part compatibility, payments, consent, safety stops and scheduling use rules, catalogues and Google Maps optimisation, not the AI. Every AI step is tested against a 100-case gold set with hard checks, expert-scored rubrics and tool-sequence checks before release.

## 10. Please select Google's AI model(s) that you will be leveraging for your AI usecase.

Select: **Gemini API**, **Gemini Live**, **Gemma** and **Other** (Other: Gemini 3.5 Transcribe, Gemini Embedding 2, Document AI Enterprise OCR).

## 11. Please describe how are you planning to leverage the above selected Google's AI models to tackle the problem you mentioned?

Through the Gemini API on Google Cloud, Gemini 3.5 Transcribe converts noisy Telugu and Hindi voice notes to text, using a custom vocabulary of repair terms. Gemini 3.5 Flash-Lite extracts intent, appliance details and missing information, and asks short follow-ups. Gemini 3.8 Flash reasons over the appliance's history and cited service-manual excerpts to rank likely faults, or abstains. Gemini vision and Document AI OCR read model plates and invoices, and Gemini Embedding 2 finds relevant manual sections and similar past repairs. These run inside ADK agents on Cloud Run, built with AI Studio and Antigravity. Later, Gemini Live will give technicians real-time voice help on site, and Gemma can run on-device for offline use. Each model is benchmarked on our gold cases, and the simplest one that passes is chosen.

## 12. How do you intend to deploy and scale your product on Google Cloud?

KeepWell runs serverless in the Mumbai (asia-south1) region. Cloud Run hosts the WhatsApp webhook, the ADK agents and the agency web app; it scales to zero when idle and scales out automatically under load. Pub/Sub and Cloud Tasks queue every message and job event, so traffic spikes never drop requests. Cloud SQL for PostgreSQL (with pgvector) stores jobs, appliance records and manual search, with row-level security separating agencies. Cloud Storage keeps voice notes, photos and invoices under retention rules. Gemini models are called through Vertex AI, with Flash-Lite as the default and Flash only when needed, to control cost. Secret Manager, Model Armor, Cloud Logging and Monitoring cover security and operations, and budgets cap AI spend per job. To scale, we add Cloud Run instances and Cloud SQL capacity, move to provisioned throughput for steady AI load, and deploy in more regions as we grow.

## 13. What is the intended industry for your product?

Home services and after-sales repair: maintenance and repair of household appliances such as refrigerators, ACs and washing machines. KeepWell is B2B SaaS (field-service software) for independent repair agencies and service centres, later extending to warranty, service plans, parts and recycling for appliance brands.

## 14. Team bio: background, experience and complementary skills

We are a two-person team from IIIT Hyderabad's M.Tech in Product Design and Management (2025–27), and both were McKinsey Forward Program fellows in 2026, trained in structured problem solving, business strategy and AI strategy. Prathyusha Kalluri is a software engineering and product management specialist: a VIT computer science graduate (data analytics), she built healthcare software for nearly two years at athenahealth and now works in product management at Contexta Health, covering AI product management, requirements and LLM-based systems. Sri Charan Peri is design-led: a mechanical engineer who has worked as a product manager and in UX, product design and prototyping (Designland, IIT Hyderabad, T-Works, SOLIZE), bringing user research, product strategy and hands-on hardware sense. Together we combine engineering and AI depth with design, research and strategy to take KeepWell from problem to product. We also built CONTINUUM, an AI-agent product that reached the top 10 at the LPL WealthX Hackathon.
