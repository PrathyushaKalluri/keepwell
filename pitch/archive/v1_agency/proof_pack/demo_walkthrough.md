# Keepwell — Circuit demo walkthrough (20-second clip for slide 6)
> **Illustrative case.** Founder histories, the company timeline, the pilot results and the financials are assumptions made for the IIIT Hyderabad ESFS course pitch. They are kept consistent with the team repo and with each other.
**Built from the real prototype run CASE-A44351** **[Real]**: FastAPI agent, 20 allowlisted tools, a 12-state job machine, a 14-condition readiness gate, Telugu voice intake. The run took 10.9 minutes and made 47 decisions, reaching a repair-ready visit. Payment and logistics responses were simulated from partner documentation. The final **verify** step is shown as designed (the 2025 prototype run ended at "repair-ready"; verification is live in production since 2026). The clip says both in small text.

| Second | On screen | Caption |
|---|---|---|
| 0–3 | A Telugu voice note arrives on the agency's WhatsApp number: *"AC is blowing warm air since noon…"* | *1:05 PM, Ramagundam, 46 °C* |
| 3–6 | Circuit reads its understanding back in Telugu and asks two questions the owner can answer from the balcony: *"Did it stop suddenly? Is the outdoor fan turning?"* | **Understand** |
| 6–9 | The model number is read from a photo of the label; warranty checked; the machine's past repair appears | **Check** |
| 9–12 | Safety check passes (no gas smell, no sparking). **Likely root cause: run capacitor (₹350 part), 2 candidates with confidence** | **Triage: root cause + part** |
| 12–15 | A quote from the agency's own rate card: *₹998, ceiling ₹1,200*; the son in Bengaluru approves with one reply | **Quote: approved by a human** |
| 15–18 | Job card on the technician's phone: fault, steps, part to carry; slot 2:00–2:45 | **Prepare** |
| 18–20 | The technician taps **"Fixed — capacitor replaced"**. The machine's record is updated and Mistri Gyan learns | **Verify: the moat step** |

**End card:** *"A new AC: ₹38,000 and three days. The repair: ₹998 and eighty minutes."*
