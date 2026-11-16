# KeepWell V3: unresolved decisions and missing evidence

Only items that need a founder decision or evidence we don't have. Everything else in V3 is sourced or labelled as a plan.

## Urgent

1. **Application deadline.** startupbuildathon.com says "Applications close on 15 November" on the homepage, but its FAQ says "13th Nov 2026". Today is 15 Nov. Confirm on the Hack2Skill dashboard that the idea submission is still open (or already submitted).

## Founder decisions

2. **Pricing.** V3 now proposes per-technician B2B pricing: Starter ₹1,499 per technician per month (60 AI-handled jobs each, then ₹10 a job), Pro ₹2,499 for service centres, Enterprise annual contracts for brands and plan providers, 60 days free. This replaces the one-pager's ₹1,500/month + ₹40 per verified fix. Confirm the price points, the 60-job cap and the free period. Benchmarks are directional (many vendors are quote-based); the ₹350–500 cost of a wasted visit is one practitioner's estimate, so measure it in the pilot.
3. **Verified fix.** It is no longer a billing trigger, but it still defines the north-star metric (closed, customer-confirmed, not reopened within 14 days). Confirm the definition and who settles disputed outcomes.
4. **MVP scope.** V3 states "refrigerators and ACs, Telugu + Hindi, one Tier 2 city". Confirm the categories, languages and the pilot city (Tamil is not supported by Gemini 3.5 Transcribe today, which is one reason it is not in the MVP).
5. **Pilot status.** The one-pager says "Product built and in first agency pilots"; V2 and V3 say no pilot data yet. V3 claims no pilot. If any agency work has actually happened (interviews, a running prototype), tell us what, and we will add it as real evidence.
6. **Slide count.** The template has one free slide; V3 (like V2) uses two (Business, Evaluation), giving 9 pages without the template's instruction page. The public site does not state a slide-count rule. If the organisers require exactly one extra slide, the Evaluation slide is the one to merge into Business.
7. **Merchant of record for UPI.** V3 assumes the agency is the merchant and money settles to the agency through a payment gateway, so KeepWell never holds customer funds. Confirm, choose a gateway, and get a legal view on whether KeepWell needs any RBI payment-aggregator licence.
8. **Data residency.** No Gemini model runs on standard pay-as-you-go in Mumbai. V3 says the pilot uses Gemini's global endpoint with customer consent. Decide if that is acceptable, or budget for 3.5 Flash / Flash-Lite provisioned throughput in asia-south1.

## Missing evidence (pilot questions, not deck claims)

9. Baseline first-visit resolution and repeat-visit rates at real agencies.
10. Agencies' willingness to pay under pricing A vs B.
11. Source of service manuals and part-compatibility data for the MVP categories, and their licence terms.
12. Who adjudicates technical ground truth for the gold set (named technician reviewers).
13. Real token counts and cost per job (V3's ₹1.50 / ₹5.50 / ₹10 are scenarios).
14. Whether agencies resist fewer repeat visits because a second visit earns a second fee.
15. The AI Product Blueprint (`Keepwell_AI_Product_Blueprint.md`) was referenced but not provided; if it contains decisions that differ from V3, share it.
