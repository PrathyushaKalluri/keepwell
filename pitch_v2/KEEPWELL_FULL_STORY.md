# Keepwell: The Founder's Story

19 Nov 2026 · Seed round

## Before you read

We are raising **₹2.5 Cr in seed money** as CCPS at an ₹8 Cr pre-money valuation, giving investors 23.8%. It comes in two tranches: ₹1.75 Cr at close and ₹0.75 Cr at a month-9 gate. It buys 18 months from the close, measured against a gate at month 9 and milestones at month 18.

**What Keepwell is, in one breath.** Keepwell is the after-sale service arm of the small-town appliance shop. The shop sells the AC, fridge, washing machine or water purifier. Keepwell installs it within 24 hours under brand authorisation, repairs it at a fixed price, sells a 2-year repair plan on the shop's bill, and keeps a record of the appliance's life. The shop sells the promise; Keepwell keeps it.

**Who we are.** Three founders: Prathyusha Kalluri (CEO, ten years in appliance distribution, 600+ dealers), Kavyanth Munagala (COO, ran a brand's zonal service network, knows 200+ service centres) and Sri Charan Peri (CTO, built voice AI and claims verification at a device-protection platform).

**How to read this.** This is the pitch told as a story, in the founders' voice. Each slide comes as a short chapter: what we show, why we believe it, and then the hardest questions an investor would ask, with our answers. Read it top to bottom and you should be able to pitch Keepwell yourself.


## How we got here

The idea we pitch today is not the one we started with. Our first design broke on contact with the evidence, and the version that survived is narrower, more honest about margins and much harder to copy.

### What we saw first

We started in real homes in Hyderabad and Visakhapatnam. We surveyed 19 households (12 qualified) and recorded interviews. What we heard was one sentence in many forms: nothing in a repair can be checked.

> "They are never going to say the price, they're going to just give you an estimation… three thousand to five thousand." — a young professional, Hyderabad

> "We won't know if the part is duplicate or original." — a homemaker, Andhra Pradesh

Seven of twelve households kept no service record at all. The rest kept it on paper: an agency sticker on a purifier with the next date in marker, a handwritten repair diary, a refill date written on a gas cylinder. One family recorded a brand's WhatsApp bot replying "API related issue" until they gave up. Families already want an appliance memory. Nobody keeps it for them.

### Who the family actually trusts

The family did not trust the brand's call centre or the local mechanic. They trusted the shop owner who sold them the machine, often someone they had known for years. When the install was late, they called him. When the repair failed, they blamed him. Consumer commissions have even held sellers jointly liable with brands (Chennai ₹35k, Hyderabad ₹60k).

Yet the shop nets 2–3% on the sale and earns nothing afterwards. That gap is the company: **the shop owns the trust, but has no way to keep the promise it made at the counter.**

### Our first design broke, and we let it

Our first plan was an agency-style installer: install any AC within 24 hours, charge the customer ₹650, add a desk fee from the shop. Before building the pitch, we ran it through a validation gate and a red-team investor who saw none of our reasoning.

It did not survive. Three facts killed it:

1. **Warranty.** At Samsung, Daikin, Carrier, IFB, Godrej and Panasonic, an install by anyone the brand has not authorised voids the warranty. Re-priced on that fact, our design needed **188 shops per cluster** to break even.
2. **Shops don't pay for service.** There is no precedent for small shops paying a monthly desk fee, so we dropped it.
3. **Our inputs were optimistic.** Technicians do about 49 jobs a month, not 76. AMC sells at ₹1,299, not ₹1,800. And we owe 18% GST, which a local mechanic under ₹20 L turnover does not.

### The redesign that survived

We tested six designs on one engine (`ue_v2.py`) with the same fair inputs. The one that held is the company we pitch:

- **Authorised, not freelance.** We install under sub-contracts from brand-authorised service centres, so the warranty stays safe. Authorisation became a go/no-go gate.
- **The shop is the source, not the payer.** Households, brands, plan sellers and later data buyers pay. The shop earns from us.
- **Four appliances, AC as the anchor.** AC alone needed 37 shops to break even; adding washing machine, fridge and purifier cut it to 30 and smoothed the seasonal peak from 1.8 to 1.6.
- **Keepwell Protect.** A 2-year repairs-only plan the shop sells on its own bill. Because we are the repairer, we can price it where chains need an insurer.
- **Partner clusters from year 3.** Existing service centres run new clusters for 10% of service revenue, using technicians who sit idle in the monsoon.

### Then we built the pitch, one gate at a time

Every step was written, challenged and approved before the next began: vision, founders, ecosystem, market, product and competition, traction, the model, the ask, the deal, compliance, a fundability score (73/100) and a storyboard with two red-team passes, then an outside review that re-based the deal. The financial model (`keepwell_model.xlsx`) has 680 formulas and zero errors, and a script checks that every number agrees across the deck, the model and the story.

| Gate | What it decided |
| --- | --- |
| Gate 1: validation | The idea holds only as an authorised, four-appliance, shop-sourced operator |
| Gate 2: story and proof | The founders, the pilot and the misses we disclose |
| Gate 3: numbers and terms | ₹2.5 Cr seed, CCPS at ₹8 Cr pre in two tranches; the old agency pitch archived |

## The pitch, slide by slide

The story deck has 18 slides and runs about 13 minutes (the investor PDF deck has 12), shared across the three founders. Each chapter below says what the slide shows, what we say, why we believe it, and then the questions we expect, answered.

### Slide 1. He sells an AC on Monday. By Thursday, the customer is angry at him.

Meet Ravi. He runs a multi-brand appliance shop in Guntur. On Monday he sells a ₹38,000 AC to a family he has known for ten years. The brand's installer says two to five days. So the family calls Ravi, then calls again. On Thursday, in 40-degree heat, they are standing at his counter, not the brand's.

Two years later the AC fails. It is out of warranty. A local mechanic guesses at the fault, charges what he likes and keeps no record. Ravi earns nothing after the sale, but he carries all the blame.

**Why we open here.** An investor should feel the problem in 45 seconds, through one person. Ravi stands for the shop owners we met in discovery; every fact on his cards is sourced in our market research.

**Tough questions**

- **"Is Ravi's week typical?"** Yes. 51 of the 64 shop owners we met told us some version of it, and the facts in it are on record: the 2–5 day install window comes from brand and marketplace terms, the out-of-warranty share from industry data, and the joint-liability rulings from consumer commission orders.
- **"Isn't a late install a minor annoyance?"** Not for the shop. It is the moment the family decides whether to come back. In our discovery, 51 of 64 owners said install delays get blamed on them, and 9 had faced a consumer complaint or legal notice.

### Slide 2. Families are already building the appliance's memory

We did not read about this. We watched it in homes. A brand's WhatsApp bot replying "API related issue" until the customer wrote "My request was not done." A local agency's sticker on a purifier, the next service date in marker. A handwritten repair diary. A refill date written on a gas cylinder.

People are already building the appliance's memory, on paper. The demand exists. Nobody owns it.

**Why this slide.** It is our first-hand household evidence, and it proves the appliance record is a habit families already have, not a feature we hope they adopt.

**Tough questions**

- **"Twelve households is not a sample."** Agreed. It is not meant to size anything. It is meant to show behaviour: what people do when nobody helps them. Sizing comes from the bottom-up market model on slide 14.
- **"Will families actually consent to a digital record?"** They already keep one on paper. Ours is created at the sale, with consent asked on WhatsApp, and it is what makes the warranty and the plan claimable. The record serves them first.
- **"These are Hyderabad and Visakhapatnam homes. Your pilot is Guntur."** True. The household research was the problem discovery. The pilot then tested whether the solution works in the target towns.

### Slide 3. The shop's promise ends at the counter

Here is the system Ravi lives in, in four numbers:

| What happens | Number |
| --- | --- |
| A brand install takes | 2–5 days |
| Appliances in homes already out of warranty | 80–91% |
| AC service going to local mechanics (no guarantee, no GST, no record) | 44% |
| Households in our survey with no service record | 7 of 12 |

The shop nets 2–3% on the sale, earns nothing afterwards, and consumer commissions have held sellers jointly liable with brands. **The person the family trusts has no way to keep the promise he made.** That sentence is the whole company.

**Tough questions**

- **"Why doesn't the brand fix this?"** The brand's service network is built for in-warranty work and is short of technicians at the summer peak. Once the machine is out of warranty, which is most of them, the brand has little reason to chase a ₹600 repair in a small town.
- **"If 44% go to local mechanics, families are happy with them."** They use them because nothing else shows up. Our interviews were full of doubt: unknown prices, unknown parts, repairs "fixed only 60–70%". Choosing the only option is not satisfaction.
- **"Joint liability: is that real or one odd case?"** Several commissions have ruled it, in Chennai (₹35k), Chandigarh and Hyderabad (₹60k). It is not routine, but every shop owner knows the risk.

### Slide 4. Between us, we already know this market by name

We are the three people who saw this from three sides.

| Founder | Role | What they bring |
| --- | --- | --- |
| Prathyusha Kalluri | CEO | Ten years in appliance distribution, latest as regional head (AP/TS) at the region's largest multi-brand distributor. Reaches **600+ independent dealers** |
| Kavyanth Munagala | COO | Zonal service head at a multi-category appliance brand, before that a water-purifier brand's service network. Knows the owners of **200+ service centres**, and how authorisation is granted |
| Sri Charan Peri | CTO | Built voice AI, claims verification and a partner field app at a device-protection platform: the engine behind a plan sold at a counter |

Keepwell connects people who already trust us. That is not a soft claim; it changes the numbers. Signing a shop through a warm network costs about ₹9.5k, against ₹22k cold.

**Tough questions**

- **"None of you has built a startup to exit."** True, and we say it first. We close the gap with an advisor who scaled home services to 20+ cities, and with the lead investor's director on our board.
- **"Networks are easy to claim. How do we check?"** By reference calls with dealers and service-centre owners, which we arrange on request. The strongest proof is already signed: our two authorised install sub-contracts (renewed for 2027) came through Kavyanth's relationships, and the 34 pilot shops, all on 2-year exclusive service-arm agreements, came through Prathyusha's.
- **"What stops a founder from walking away?"** Founder shares vest over 4 years with a 1-year cliff, running since incorporation in August 2025, plus a 3-year lock-in. Nobody keeps equity they have not earned.

### Slide 5. The shop sells the promise. Keepwell keeps it.

Keepwell is the after-sale service arm of every small-town appliance shop. The shop now has four things to sell, all under its own name, delivered by certified local technicians:

| Offer | What the family gets |
| --- | --- |
| Authorised install in 24 hours | The machine running the next day, warranty intact |
| Guaranteed repair and AMC | A fixed rate card for AC, fridge, washing machine and purifier, with a guarantee on the work |
| Keepwell Protect (about ₹2,000) | A 2-year repairs-only plan sold on the shop's own bill |
| The appliance record | Every visit, part and plan, consented on WhatsApp |

We grow in four phases: **Serve** (now), then **Supply** (central parts and partner clusters), then **Know** (the record lets brands verify installs and claims), then **Circulate** (second life for old appliances).

**Why the shop's name, not ours.** Trust in small towns goes to people, not systems. Families told us they trust a person who has done good work for them before, and doubt a stranger sent by a system. The shop owner is that person. So we do not compete with the shop for the customer; we make the shop more trustworthy.

**Tough questions**

- **"Why would a shop hand you its customers?"** It doesn't. The job carries the shop's name and the shop earns on it: about ₹1.7k a month in the pilot, about ₹3,170 at maturity once it sells Protect. Its after-sale blame goes away. Before we built anything, 41 of 64 owners said they would route installs to "a service partner who puts my name on the guarantee".
- **"What does the shop have to do?"** Almost nothing new. It adds the install and Protect to the bill and sends a WhatsApp message. No app, no staff, no fee.
- **"Four phases sounds like a lot for a seed company."** The seed funds only Serve. The other three are where the business goes once Serve works, and each is funded by its own round, raised on proof (slide 15).

### Slide 6. From the shop's bill to a guaranteed fix

Here is one appliance's life with us, all on WhatsApp:

1. **Sale.** The shop adds the install and Protect to the bill; the family consents on WhatsApp.
2. **Record.** We read the model, serial and invoice from photos and issue the plan certificate.
3. **Install.** An authorised technician installs within a day.
4. **Ask.** Months later, a voice note in Telugu: "AC not cooling."
5. **Triage.** Our AI desk drafts the likely fault and the part to carry, and checks the plan cover.
6. **Fix and verify.** The technician confirms the real fault, closes with a photo and a customer OTP, and the record updates.

The last step matters most. A verified fix is what makes the record worth trusting, and a trusted record is what brands and plan sellers will later pay to check (the Know layer).

**Tough questions**

- **"Why WhatsApp and not an app?"** Shop owners and families in these towns already live on WhatsApp. An app would need a download for every customer; a WhatsApp message needs nothing. It also costs about ₹0.12 per utility message.
- **"How do you know the technician actually did the work?"** A photo checklist, serial capture, the customer's OTP at close and random callbacks. Payment also flows through us, so the job, the proof and the payout sit in one record.
- **"What does all this technology cost per job?"** Under ₹5 on our research: WhatsApp messages, a few minutes of voice AI and about 6,000 tokens. Our model carries ₹2.5 a job, against a job worth hundreds of rupees.

### Slide 7. AI reads and drafts. Rules and people decide.

The AI is our cost engine, not our moat. It understands voice notes, reads photos, drafts the likely fault and dispatches, so one coordinator can run a 60-shop cluster.

But some decisions are never the AI's:

| The AI does | Never the AI's call |
| --- | --- |
| Understands voice notes in Telugu, Hindi and English | Prices: always the rate card |
| Reads model, serial and invoice from photos | Safety stops on gas and high voltage: hard rules |
| Drafts the likely fault and the part to carry | Rejecting a claim or issuing a refund: a person decides |
| Plans dispatch and routes | Sharing data: only with consent |

**Tough questions**

- **"If the AI isn't the moat, what is?"** Four things that take years: exclusive shop agreements, cluster density, brand authorisation and the record, which compounds with every verified visit. Anyone can rent a speech model; nobody can rent 60 signed shops in Guntur.
- **"What if the AI misdiagnoses?"** It only drafts. The technician confirms the real fault on site before any work or charge. A wrong draft costs at most a second trip, and every confirmed fix makes the next draft better.
- **"What about customer data and DPDP?"** Consent is asked at the sale, on WhatsApp, and recorded. Data goes to a brand or plan seller only with that consent, and only for the purpose stated.

### Slide 8. Eight months, 34 shops, and the shops kept routing to us

We ran the pilot in Vijayawada–Guntur from March to October 2026, through one full AC summer.

| Result | Number |
| --- | --- |
| Shops signed | 34 |
| Jobs | about 2,400 (775 installs, 1,330 service and repair, 280 plan-seller jobs) |
| Revenue | ₹25 L |
| Contribution | ₹5 L |
| Contribution per shop by month 4 | ₹4.5k a month |
| Units sold per shop | 74 a month |
| Installs routed to us | 58% |
| Installed within 24 hours | 87% |
| Fixed on the first visit | 81% |
| AC units we could install under authorisation | 41% |
| Protect attach (12 shops, last 8 weeks of summer) | 6% |

The number we care about most is 58%. Shops did not just sign; they kept sending us their installs, month after month. And when twelve shops were allowed to sell Protect at the counter, 6% of buyers took it. That is when we knew the shop could sell the promise.

**Tough questions**

- **"₹25 L of revenue is tiny."** It is a pilot, sized to learn, not to impress. What it proves is behaviour: routing, speed, first-time fixes and willingness to pay for a plan. Revenue scales with clusters, which is what the seed funds.
- **"Why were only 41% of AC installs authorised?"** Our two sub-contracts cover some brands, not all. That is why both sub-contracts were renewed for 2027, a brand's regional team has signed a letter of intent for direct authorisation, and authorising at least 35% of AC units is a condition of the month-9 gate. With zero authorisation, breakeven rises to about 50 shops; it still works, but worse.
- **"Were these numbers audited?"** Our books are CA-reviewed, and the seed budget pays a CA to certify the gate data, so investors see checked numbers, not our word.

### Slide 9. Four misses, and what we changed

We missed four targets. Showing them is what makes the hits believable.

| What we missed | What we changed |
| --- | --- |
| Shop signing lagged | Added a second field executive |
| One of two service-centre partners under-delivered | Opened talks with a third service centre |
| Technicians did 2.6 jobs a day, not 2.8 | Re-zoned dispatch; it reached 2.8 |
| The plan seller sent 70 jobs a month, not 100 | Widened that contract |

On today's pilot economics, a cluster breaks even at about 35 shops. That is why density is our first milestone.

**Tough questions**

- **"If you missed four targets in a pilot, why will you hit them at scale?"** Because each miss had a cause we could fix, and the fixes are in the plan and its cost. We set the gate and the milestones on the stress case, not the optimistic one.
- **"Breakeven at 35 shops, but you only have 34."** Correct, and we say so. The pilot cluster is at the edge of breakeven on pilot economics. Gate condition 2 is that it pays for its own team over the 12 months to December 2027. At maturity the model breaks even at 22 shops, because Protect and better density lift each shop's contribution.

### Slide 10. Every cluster pays for itself, on service

Here are the economics at maturity, from our model:

| Level | Revenue | Contribution or EBITDA |
| --- | --- | --- |
| One mature shop | ₹3.5 L service + ₹0.9 L Protect a year | ₹1.16 L contribution |
| One mature 60-shop cluster | ₹2.72 Cr | ₹44 L EBITDA (16%) on service; breaks even at 22 shops |
| The company | ₹130.5 Cr in year 7 | EBITDA-positive from year 5; ₹8.6 Cr (6.6%) in year 7 |

The shop itself earns about ₹3,170 a month from us at maturity, up from ₹1.7k in the pilot, because we pay it for the sale it controls.

The honest version: every cluster is profitable on service. While the company opens 15+ clusters a year, the cost of growth holds company-level service near breakeven, and data (verified installs, claims checks, leads) tips the company into profit. At the mature run-rate the network earns 13.4%, of which 9.1% is service alone.

**Tough questions**

- **"So you're only profitable because of data?"** No. Each cluster is profitable on service. Growth costs money, and while we grow fast, data covers that cost. Once growth slows, service alone earns 9.1%. That is exactly why a paid verification contract is a seed milestone: we want that proof early.
- **"16% EBITDA is low for venture."** It is healthy for an operator, and we pitch as one. Field-service operators like HomeServe and Frontdoor trade at 2–3× revenue. Our returns come from density and scale, not software margins.
- **"Which case do you plan on?"** The stress case: 5% Protect attach, 45% claims and 50 shops per cluster. Every milestone and the ask itself is sized on it.

### Slide 11. We can sell repair cheaply because we are the repairer

Chains sell protection plans through insurers, who price for risk and add their margin. We are the repairer, so our cost of a claim is our own cost of repair.

One ₹2,000 plan breaks down like this:

| Step | ₹ per plan |
| --- | --- |
| Price, net of GST | 1,695 |
| Shop's share (25%) | −424 |
| Claims at our own repair cost (we carry 35%) | −593 |
| Admin | −85 |
| **Keepwell keeps** | **593** |

On our own failure data, claims run about 27% of the net price. We carry 35%, and the planning case uses 45%.

**Tough questions**

- **"Is Protect insurance?"** No. It is a repairs-only service contract that Keepwell fulfils itself: no accidental damage, no theft. Expected claims on every unexpired plan sit in a ring-fenced reserve. The pilot plans were sold on counsel-reviewed terms; the formal opinion is a condition of tranche 2. If counsel disagrees, we sell through a licensed insurer as an agent, and the model has been run with no Protect at all: the stress cash need to month 48 rises from ₹7.7 Cr to ₹8.7 Cr.5 Cr to ₹8.5 Cr.
- **"6% attach from 72 plans proves nothing."** Agreed. It shows willingness to buy, nothing more. BASE assumes 8% at maturity; the stress case 5% (3.75% in a cluster's second year); the month-18 milestone is 3.5%.
- **"Claims could blow up."** At 55% claims, the stress cash need to month 48 rises only from ₹7.7 Cr to ₹8.1 Cr. The first pilot plans come into cover from mid-2027, and we track every claim from then.
- **"Why does the shop get 25%?"** Because the shop makes the sale. Paying it well is what makes it sell, and the shop's earnings are what keep it exclusive to us.

### Slide 12. Nobody owns the independent shop

So why hasn't someone done this? Because everyone serves someone else. Onsitego comes closest, and it could be a partner.

| Player | Who it serves | Why it doesn't do what we do |
| --- | --- | --- |
| Urban Company | Metro households | Takes the customer for itself; its top 10 cities are over 90% of its job value |
| Onsitego, Zopper | Chain counters | Sells plans but owns no delivery in small towns; Onsitego left consumer repair because acquisition cost too much |
| 247around, SERVIZ | Brands | Paid by brands for brand jobs; 247around makes about ₹14.5 Cr a year, at a loss, after 10 years |
| Jeeves, resQ | Their own retailer | Captive to Flipkart and Reliance |
| Local mechanics | Everyone, informally | No guarantee, no GST, no record. They are our future technicians |
| **Keepwell** | **The independent shop** | Exclusive shop agreements, density, authorisation, the record |

**Tough questions**

- **"Onsitego could do this tomorrow."** It is the closest threat, and we treat it as a customer first. Plan sellers need someone to fulfil claims in small towns; we already fulfil about 70 of their jobs a month. Competing with us means building the delivery network they chose not to build.
- **"What if a brand builds this itself?"** A brand serves only its own machines. The shop sells five brands and wants one partner for everything. A brand-owned arm cannot be that partner.
- **"If it is such a good gap, why is it empty?"** Because it is hard and unglamorous: small shops, small towns, field technicians, seasonality. That is precisely what makes it defensible once it is built. Nobody has proved it impossible; nobody has tried it with authorisation and a counter-sold plan.

### Slide 13. Service centres run our clusters from year 3

How do we grow without hiring sixty cluster teams? From year 3, existing brand service centres run our new clusters. They already have a manager, premises and technicians who sit idle in the monsoon.

|  | The partner service centre | Keepwell |
| --- | --- | --- |
| Brings | Coordinator, premises, technicians | Shops, customer, payment, Protect, parts, the AI desk and the record |
| Earns | 10% of cluster service revenue (about ₹21 L a year) plus technicians' per-job pay | About ₹38 L EBITDA (14%) per partner cluster |
| Costs | Its idle capacity, put to work | ₹1 L a month per cluster, instead of a ₹23 L-a-year team |

Kavyanth knows the owners of 200+ such centres. We need 66 by year 8.

**Tough questions**

- **"What stops a partner from cutting you out?"** Keepwell holds the shop agreements, the plans, the payment, the guarantee and the record. A partner who leaves takes its technicians, not the demand. Partner contracts include a non-solicit clause.
- **"Partners take margin. Why not run everything yourselves?"** Partners buy speed and capital efficiency, not margin. A partner cluster earns 14% for us versus 16% for an owned one, but costs a fraction of the capital to open. That trade lets us reach 72 clusters on ₹22.5 Cr of total equity.
- **"Why would technicians stay with you at all?"** Per-job pay at 60% of labour, more jobs a day at cluster density, an off-season pay floor for a core group, and accident cover. In the pilot, 1 of 22 technicians left.

### Slide 14. ₹4,000 Cr a year that no one organises

We built the market bottom-up, from units sold through independent shops, and cross-checked it against household spend.

| Level | Size | What it covers |
| --- | --- | --- |
| TAM | ≈ ₹4,000 Cr a year | After-sale spend flowing through the customers of independent Tier 2/3 shops |
| SAM | ≈ ₹1,040 Cr | Five southern states |
| Beachhead | ≈ ₹360 Cr | Andhra Pradesh and Telangana |
| Year-7 plan | ₹130 Cr | 3,300 shops, about 7% of India's 45k independent shops |

In the towns we enter, 3,300 shops is about a quarter of the shops. Density, not national share, is our test.

**Tough questions**

- **"Your validation report said ₹1,550 Cr. Now it's ₹4,000 Cr. Which is it?"** ₹1,550 Cr counted only the \~9k large shops that sell 60+ units a month. Validation then showed we should serve every shop in a cluster, so all \~45k independent shops count. Two independent methods agree: shops give ₹4,150 Cr, households ₹3,600 Cr (range ₹3,500–4,800 Cr). Protect is new spend and is not in the TAM. And we plan on the beachhead (₹360 Cr), not the TAM.
- **"Is 7% share realistic?"** Nationally it is modest. The real test is local: about a quarter of the shops in the towns we enter. Pilot routing of 58% in our first towns says that is reachable.

### Slide 15. Serve, Supply, Know, Circulate. Each round raised on proof.

Revenue grows from about ₹2.4 Cr in year 1 to ₹130.5 Cr in year 7, EBITDA-positive from year 5 (BASE).

**Revenue reaches ₹130.5 Cr by year 7; EBITDA turns positive in year 5** (BASE case, ₹ Cr a year; source: `keepwell_model.xlsx`, Step 7b plan)

| Year | Y1 | Y2 | Y3 | Y4 | Y5 | Y6 | Y7 | Y8 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Calendar | 2027 | 2028 | 2029 | 2030 | 2031 | 2032 | 2033 | 2034 |
| Revenue | 2.4 | 6.8 | 15.3 | 29.7 | 53.9 | 86.9 | 130.5 | 181.6 |
| EBITDA | −1.1 | −1.5 | −1.9 | −1.4 | +0.6 | +4.1 | +8.6 | +15.3 |

EBITDA stays slightly negative through year 4 because we open 15+ clusters a year, each at a quarter of its output in its first year. In the stress case, profit arrives a year later, in year 6.

We fund the journey one step at a time, each raised on proof:

| Round | When | Amount | What it funds |
| --- | --- | --- | --- |
| **Seed (now)** | March 2027, at ₹8 Cr pre | **₹2.5 Cr** | Serve in AP/TS: clusters 1–4 |
| Round 2 | H2 2028, at ₹25 Cr pre | ₹5 Cr | Supply: central parts, the first partner clusters; Know starts with install verification for brands |
| Round 3 | 2030, at ₹70 Cr pre | ₹15 Cr | Scale to 72 clusters; data and second-life layers |
| Exit | 2033–34 | — | Strategic sale or PE, enterprise value ₹255–376 Cr |

**Tough questions**

- **"You need three rounds. What if Round 2 doesn't come?"** Then the month-18 milestones were missed, and the month-9 gate would already have shown it, before tranche 2 was paid. Each later round is priced at about 2.4–3.7× trailing revenue, the same logic as the exit, so it does not depend on a hot market.
- **"Why not raise ₹7.5 Cr now and skip a round?"** It would sell close to half the company at its lowest-ever price. Raising each round at a higher price on new proof (₹8 Cr, ₹25 Cr, ₹70 Cr pre) leaves founders about 41% after Round 3, which keeps them motivated to the exit.
- **"What does the stress case look like?"** Profitable from year 6, not 5, with a peak cash need of ₹10.1 Cr at its monthly low point. That is why the ask, the gate and the milestones are set on stress.

### Slide 16. Three questions we answer before you ask

Before the number, the hygiene. These are the three questions that kill field-service companies in diligence.

| Question | Answer |
| --- | --- |
| Is Protect insurance? | No. A repairs-only service contract we deliver ourselves, on counsel-reviewed terms, claims ring-fenced; the formal opinion is a condition of tranche 2 |
| Are technicians employees? | Per-job partners. We pay the gig-worker levy (modelled at 1.4%) and carry accident cover |
| Do our installs void warranties? | No. We install only under authorised sub-contracts, renewed for 2027 |

**Tough questions**

- **"The labour codes changed in November 2025. Are you exposed?"** All four codes are in force; the central aggregator levy is not yet notified. Telangana charges 1–2%, Andhra Pradesh nothing so far. We model a 1.4% levy and still hit the numbers. Employing technicians would add 6–12% in statutory cost, which is why we use certified per-job partners.
- **"What about GST?"** We are the principal, so we charge 18% GST on install, repair and AMC, and our prices include it. That makes us dearer than an unregistered mechanic on paper, and the guarantee and record are why families pay the difference.
- **"Safety on gas and high-voltage work?"** Hard stops in the workflow, certified technicians, and public-liability and accident cover at about ₹2.5 a job.

### Slide 17. ₹2.5 Cr, two tranches, 18 months

Here is our ask: **₹2.5 Cr as CCPS at an ₹8 Cr pre-money valuation**, for 23.8% of the company. It comes in two tranches: ₹1.75 Cr at close and ₹0.75 Cr at a gate in month 9.

We sized it the way the course teaches. Our one-year need from the close is ₹1.34 Cr. Add six months to raise the next round on proof and a small contingency, and you get ₹2.5 Cr: 18 months of runway.

**The month-9 gate (December 2027) releases tranche 2:**
1. **Shops sell enough:** 65+ units per shop a month, with 50%+ of installs routed to us.
2. **The pilot cluster pays for its own team.**
3. **Protect sells:** 3.75%+ in the pilot shops (the stress path; the counter test showed 6%).
4. **Protect is legally clean:** the formal legal opinion is in hand.
5. **Authorisation holds:** 35%+ of AC units authorised.

**Month 18 (September 2028): the case for Round 2.**
- 4 clusters and 200+ shops
- a ₹4.5 Cr+ revenue run-rate
- 3 partner-cluster agreements
- one paid verification contract

Every threshold is at or below our own stress path. If we are on plan, you see it at month 9. Beyond money, we want introductions to brand after-sales heads and dealer associations.

**Tough questions**

- **"How did you get to ₹8 Cr pre?"** It is what the course scorecard gives (₹8.2 Cr), inside comparable Indian seed rounds (₹6–12 Cr pre), and well under the VC-method ceiling: ₹13.5 Cr post for a 40% IRR in the stress case, against our ₹10.5 Cr. It is a 1.3× step-up from our ₹6 Cr pre-seed cap, and about 3.3× next year's revenue.
- **"What do I get as the seed investor?"** 23.8% now, about 16.3% after two more rounds. At a year-5 exit in the stress case that is 6.9× (47% IRR); at year 7, 16.7× in stress and 24.6× in BASE. All clear the course's 35–40% IRR bar. The exit value is about 2.9× year-7 revenue and about 25× year-8 EBITDA.
- **"What if it fails?"** Then it fails the month-9 gate. Tranche 2 is never paid, so the most you have at risk is ₹1.75 Cr, protected by a 1x preference ahead of the founders. Protect customers are paid from the reserve.
- **"What are the terms?"** CCPS in two tranches at one price, 1x non-participating preference, broad-based weighted-average anti-dilution, a 3-person board (two founders, one lead-investor director, plus an AP observer), a 10% ESOP pool, pro-rata and information rights, and a monthly extract of jobs, attach and claims from the Keepwell record.

### Slide 18. Keepwell keeps the promise the shop made

Let's go back to Ravi.

Monday, he sells the AC, with the install and Protect on the same bill. Tuesday, an authorised technician installs it, and the warranty is safe. Two years later, a voice note in Telugu brings a covered fix the same week. Ravi earns on the plan, and the family comes back to his shop.

**Keepwell keeps the promise the shop made when it sold the appliance.**

**Why we close here.** The close replays the opening with the problem solved. It is the one line we want the room to remember.

## The money: why we need it, and exactly what it buys

We need ₹2.5 Cr because the pilot proved the model works in one cluster, and the only way to prove it repeats is to open three more through a full AC season. Our cash runs out in early April 2027; the target close is February–March 2027.

### Where we stand today (November 2026)

| Item | Amount |
| --- | --- |
| Raised so far | ₹70 L: ₹45 L pre-seed iSAFE, ₹15 L from founders, ₹10 L of a ₹15 L AP Startup Policy grant |
| Spent | about ₹52 L on discovery, incorporation and the March–October 2026 pilot |
| Cash in hand | ₹18 L, plus a ₹5 L grant instalment due; about ₹2 L at the March 2027 close |
| Monthly burn | about ₹6 L (pilot cluster team, 2 engineers, founder stipends); ₹5.25 L with stipends halved until the close |
| Runway | to early April 2027 |

This pitch is the round. There is no separate bridge.

### How we sized it

| Step (stress case, from the close) | ₹ Cr |
| --- | --- |
| Costed needs for the first 12 months (head office, three cluster teams, onboarding 150 shops, set-up, working capital, fees) | 1.73 |
| Less contribution we earn in those months | −0.37 |
| Less cash at the close | −0.02 |
| **One-year need** | **1.34** |
| Plus six more months to raise Round 2 on proof | 1.00 |
| Plus contingency for the January–March low | 0.16 |
| **The ask** | **2.50** |

Protect customers' plan money is never counted: it sits in a ring-fenced claims reserve.

### What the ₹2.5 Cr pays for

Over the 18 months the business spends ₹3.34 Cr. Contribution covers ₹0.98 Cr; the seed covers the rest.

| Use | Share of spend | ₹ Cr | What it is |
| --- | --- | --- | --- |
| Build the team | 37% | 1.22 | Founders on below-market pay, a finance and compliance lead from day 1, a claims and quality lead after the gate |
| Discover product–market fit | 27% | 0.91 | Running clusters 1–4: coordinators, dispatch, quality checks, Protect claims audits |
| Working capital | 19% | 0.63 | Cluster set-up, parts stock, receivables through the AC season |
| Build the product | 9% | 0.31 | The AI desk: WhatsApp intake, triage, dispatch, the appliance record, the Protect plan record; cloud and AI costs |
| Marketing and sales | 7% | 0.23 | Onboarding 200+ shops; Protect counter kits and training |
| Payment fees | 1% | 0.04 | Payment gateway |

**Protect customers' money is not in the ask and is never spent on growth.** Expected claims on every unexpired plan sit in a ring-fenced account.

### The real need, in one paragraph

The money is not for discovering whether families want this; the pilot answered that. It is for proving three things an investor cannot take on trust: that a second, third and fourth cluster fill with shops as the first did; that the pilot cluster pays for its own team; and that Protect sells and claims behave at scale. Those three proofs are what Round 2 will be priced on.

### Who we raise from

| Investor | Amount | What else they bring |
| --- | --- | --- |
| Lead: an early-stage seed fund or angel network (consumer services, Bharat or circular-economy focus) | ₹1.25 Cr | Prices the round, sits on the board, opens Round 2 introductions |
| 3–5 strategic angels: ex-service heads of appliance brands, a dealers' association leader, a scaled field-service founder | ₹0.75 Cr | Brand authorisation, partner recruitment, shops beyond AP/TS |
| AP Startup Policy 4.0 seed equity | ₹0.5 Cr | State channels and dealer-association credibility |

**How the tranches split:** the lead (₹1.25 Cr) and the angels (₹0.5 Cr) fund tranche 1, ₹1.75 Cr at close. The angels' last ₹0.25 Cr and AP's ₹0.5 Cr come at the month-9 gate as tranche 2.

### Why now

- **The installed base is entering repair age.** AC penetration is about 10% and growing about 15% a year; most buyers are first-time owners, and most machines in homes are already out of warranty.
- **Small towns are where the growth is.** One AC major makes 65% of its sales in Tier III–V towns.
- **The rules are formalising service.** The labour codes (in force since November 2025), Right to Repair and the e-waste rules all favour a registered, recorded operator over an informal mechanic.
- **The technology just became cheap enough.** Indian-language voice AI on WhatsApp now costs under ₹5 a job, so one coordinator can run a 60-shop cluster.

### Tough questions on the money

- **"Your early validation said a smaller round at about a ₹6 Cr cap. Why ₹2.5 Cr at ₹8 Cr now?"** That was before the pilot, and the pre-seed that funded the pilot was raised at exactly that ₹6 Cr cap. After 34 shops, about 2,400 jobs, ₹25 L of revenue and a 6% Protect test, ₹8 Cr pre-money is a 1.3× step-up. It is also what the course scorecard gives, and it sits well under the VC-method ceiling.
- **"₹2.5 Cr is above the course's seed band of ₹50 L–2 Cr."** The first tranche, ₹1.75 Cr, sits inside the band. The second ₹0.75 Cr comes only if the month-9 gate is met, and in a field service that money pays for cluster teams and working capital before revenue arrives.
- **"Is the revenue real enough to justify this?"** Over the seed's 18 months the business is planned to earn ₹5.1–6.4 Cr of revenue, so each rupee of seed sits under about two rupees of revenue.

## What we don't know yet, and how we will find out

We would rather an investor hear our weak points from us. Each one below has a test and a date, and most are written into the month-9 gate or the month-18 milestones.

| Unknown | Why it matters | How we find out | By when |
| --- | --- | --- | --- |
| Protect attach at scale | No Indian attach rate is published; our 6% comes from 72 plans | Gate: 3.75%+ in pilot shops; milestone: 3.5%+ across all clusters | Dec 2027 / Sep 2028 |
| Protect claims | Our 27% claims figure is from repair data, not plans in cover | Track every claim as the first pilot plans enter cover | From mid-2027 |
| Protect's legal status | If it were classed as insurance, we would need an insurer partner | Counsel-reviewed terms today; formal opinion is a gate condition; fallback is selling as an insurer's agent | By month 6 (Sep 2027) |
| Brand authorisation | Only 41% of AC installs were authorised in the pilot | Sub-contracts renewed for 2027, a brand's letter of intent, a third centre; gate of 35%+ of AC units | Dec 2027 |
| Whether clusters 2–4 fill like the first | The pilot had a founder's network behind it | Milestone: 4 clusters, 200+ shops | Sep 2028 |
| Data revenue | Company profit while growing depends on it | One paid install-verification contract (month-18 milestone) | Sep 2028 |
| Leakage | Technicians may take customers direct | Guarantee only on booked jobs, payment through us, QR on every unit; audit the installed base | Ongoing |
| Parts margin | Distributor terms are not yet known | Distributor interviews and 30 invoice checks | 2027 |

**The scenarios we plan around:**

| Case | What it assumes | What happens |
| --- | --- | --- |
| BASE | 8% Protect attach, 35% claims | EBITDA-positive in year 5; year-7 revenue ₹130.5 Cr |
| Stress (our planning case) | 5% attach, 45% claims, 25% parts margin, 50 shops per cluster, slower rollout | Profitable from year 6; peak cash need ₹10.1 Cr (monthly low point) |
| LOW | Every pilot input at its worst | Never profitable. It fails the month-9 gate, so tranche 2 is never paid and expansion stops; the investor's exposure is ₹1.75 Cr |

The LOW case is why the gate exists. We do not ask investors to fund it; we promise to stop before it costs them more.

**What the founding team lacks.** None of us has taken a startup to exit. We close that gap with an advisor who scaled home services to 20+ cities and the lead investor's director on the board.

## The whole story on one page

If you remember nothing else, remember these answers.

| Question | Answer |
| --- | --- |
| What did we do? | Interviewed households and 64 shop owners, sized the market bottom-up, broke our own first design on the evidence, redesigned it, ran an 8-month pilot with 34 shops on 2-year agreements, and built a model with 680 formulas and zero errors |
| What is the company doing? | Running the after-sale service for small-town appliance shops: authorised installs in 24 hours, guaranteed repair and AMC, a counter-sold 2-year repair plan, and a record of every appliance, all under the shop's name |
| What do the founders do? | Prathyusha brings the shops, Kavyanth brings the service centres and authorisation, Sri Charan builds the AI desk and the plan engine |
| Why do they need funding? | To prove the pilot repeats: three more clusters through a full AC season, before cash runs out in April 2027 |
| What is the real need? | Cluster teams, a finance and claims team, the AI desk and working capital for the summer peak, not marketing or salaries for their own sake |
| How much? | ₹2.5 Cr seed, CCPS at ₹8 Cr pre-money (23.8%), in two tranches: ₹1.75 Cr at close and ₹0.75 Cr at the month-9 gate |
| What does it buy? | 18 months from the close: a month-9 gate that releases tranche 2, and month-18 milestones (4 clusters, 200+ shops, a ₹4.5 Cr+ run-rate) that earn Round 2 |
| What does the investor get? | 6.9× (47% IRR) at year 5 and 16.7× at year 7 in the stress case, with a 1x preference ahead of founders |

The shop sells the promise. Keepwell keeps it.
