# Competitor landscape: post-warranty appliance repair via regional retailers (India, Tier 2/3)

Retrieved 2026-11-18. Every claim below is in `competitors.csv` or `competitor_city_claims.csv` with its source URL. Three labels are used:

- **[V]** Verified: a filing, a fetched page with a local address, or a city-specific price page.
- **[C]** Company or marketing claim.
- **[I]** My inference.

"Not found" means only that I searched and found nothing. It does not mean the thing does not exist.

## 1. The models, explained simply

| Model | How it works | Who pays | Examples |
|---|---|---|---|
| **Captive retailer service arm** | A big retailer runs its own repair and warranty arm for things it sold. | The shopper pays a plan fee at checkout, and the retailer covers installs. | Reliance resQ, Jeeves (Flipkart), Croma ZipCare |
| **Extended-warranty / protection plan seller (B2B2C)** | Plans are sold at the retailer's counter or checkout. Claims are later sent to a service-centre network. The retailer earns a commission. | The shopper, upfront and at the time of purchase. | Onsitego, Zopper, OneAssist, Servify (white-label) |
| **Outsourced brand after-sales operator** | A brand hands its warranty and installation jobs to an operator, who sends them to local agencies. | The brand, per job. | 247around (Servify), Qdigi (Onsitego), Bigfix/Warrantify, SERVIZ managed ops |
| **After-sales software** | Software that links brand, service centres, retailer counter and customer. | The brand, as a licence. | SERVIZ OS (has a retailer panel), Servsy CRM, Bigfix API |
| **On-demand consumer marketplace** | The consumer books a standard-price job in an app, and a trained freelancer does it. | The consumer, per job. The platform keeps about 28% commission [C, secondary from RHP]. | Urban Company, Servsy, NoBroker, ServiceOnDoors, HomeTriangle |
| **Brand's own service / AMC** | The brand's authorised service centres (often local partner businesses) sell AMCs and charge for out-of-warranty work. | The consumer. | Eureka Forbes, Kent, LG, Samsung, Voltas, Godrej, Daikin |
| **Lead-gen directory** | Local repair shops pay to be listed and to receive leads. | The local shop. | Justdial |

## 2. Who pays whom

- **Consumers pay at purchase, before anything breaks.** This applies to resQ, ZipCare, Onsitego, Zopper and OneAssist. These businesses earn on plans, not on repair jobs.
- **Consumers pay per job, after a breakdown.** This applies to Urban Company, Servsy, brand out-of-warranty work, and local agencies found through Justdial.
- **Brands pay per job.** This applies to 247around, Qdigi, Bigfix and SERVIZ.
- **Local shops pay for leads.** This is Justdial. Its average campaign value is about Rs 1,100 in Tier 2/3 against about Rs 2,300 in Tier 1 [C, earnings-call analysis].

## 3. Does anyone already do "retailer customer → post-warranty repair routed to local agencies"?

**Yes, in captive form, for national chains:**

- **Reliance resQ.** Its plans can only be bought on Reliance Retail purchases and start after the brand warranty ends [V]. It claims 1,200+ centres and 6,500+ engineers [C].
- **Jeeves for Flipkart buyers.** It claims 300+ walk-in centres, 1,000+ service partners and 400 cities [C]. It has already served non-Flipkart products through ApnaComplex (December 2023) [V].
- **Croma.** It runs ZipCare "Maintain" one-time service and AMC SKUs, with repairs at brand-authorised centres [V].

**Yes, in plan form, at regional chains:**

- **Onsitego** sells extended warranty at these regional chains:
  - Vijay Sales, as "VS+" [V].
  - Value Plus, with 135 stores across UP, Uttarakhand, Rajasthan, West Bengal and Sikkim [V].
  - Great Eastern and Sanket [C].
- **Onsitego's network.** It claims 3,300+ service centres and has owned Qdigi since February 2024 [V]. Qdigi has 100+ owned and 200+ franchise centres [C].
- **Zopper's** consumer-durables page shows logos for regional South-India chains: Sathya, Vasanth & Co, Darling, Celekt, B New, Cellbay and Ace Best Buy [C]. These are logos only, and the page does not say what each chain uses Zopper for.

**What I did not find:** any player that takes a regional chain's existing customers, whose warranty or plan has already lapsed, and sells them a paid repair job routed to local agencies.

- Value Plus's own page sends post-warranty customers either to the OnsiteGo plan or to the brand helpline [V].
- Every plan seller earns at the point of sale, so a customer who never bought a plan falls outside its model [I].
- The software players are closest in tooling. SERVIZ has a retailer panel for installs, demos and complaints, but it sells to brands [C].

**Confidence that this exact niche has no visible incumbent: low to medium.** Two things limit it:

- Informal tie-ups between stores and local mechanics are probably common and would not show up online [I].
- I could not check the in-store practice of chains such as Bajaj Electronics, Poorvika, Pai International or Girias. Searches for those chains found no named partner.

## 4. Tier 2/3 presence (30 target cities)

| Player | Evidence across the 30 cities | Strength |
|---|---|---|
| Eureka Forbes (RO) | 27 VERIFIED ACTIVE: authorised-centre pages naming a local partner business and street address (4 sample pages fetched). None found for Warangal or Bhubaneswar, and the Madurai entry has a bad PIN. | The strongest verified local network found. It is RO only, and its centres are the kind of local agency a startup would route jobs to. |
| Urban Company | 17 PUBLICLY CLAIMED: city pages with city-specific prices, e.g. foam-jet AC service Rs 599 in Jaipur, Surat and Vadodara and Rs 799 in Vijayawada, Guntur and Visakhapatnam. 6 have only a Native RO purchase page. 7 have no page. | Real but thin. Its top 10 cities were more than 90% of net NTV in Q3 FY26 [V, shareholder letter]. |
| Servsy | 20 listed on its coverage page [C]. | Weak. Its own About page describes a Mumbai/Pune pilot. |
| ServiceOnDoors | AC pages for all 30, but these come from a set of about 770 templated district pages. | SEO template only, not proof of operations. |
| Justdial | Warangal verified, with many local AC shops, addresses, ratings and prices (e.g. Rs 699 AC service). Other cities not checked because the site blocks automated fetching. | The real incumbent channel to the unorganised local agencies [I]. |
| resQ | Jaipur, Lucknow and Ludhiana named in its app listing [C]. | Not verified. |
| Jeeves, Onsitego, Qdigi, Servify/247around, SERVIZ, OneAssist | Claims of national coverage ("400 cities", "19,000 PIN codes", "3,300 centres") with no city list. | NOT VERIFIED. This means unknown, not absent. |

The "19,000+ PIN codes" figure appears for 247around, Servsy and OneAssist, and Eureka Forbes uses a close variant (19,500). It is probably the India Post PIN universe used as a marketing number, not a measure of coverage [I].

## 5. What would stop Jeeves, Onsitego, Bigfix or Servify from copying a retailer-led repair model?

**Onsitego is the most credible copier, and little stops it [I].**

- It already sits at regional retail counters through its SalesPro retailer app.
- It has a repair network through Qdigi.
- It already issues retailer-branded plans, such as VS+.
- A "post-warranty repair referral" SKU would be a small product step.
- Possible frictions:
  - Plan premiums probably carry far better margins than one-off jobs [I].
  - Job-based repair needs dispatch and price-quote handling that plan claims do not.
  - Qdigi's network leans towards phones and OEM work (Samsung, Apple, OnePlus, Xiaomi).

**Jeeves has three structural limits.**

- It is captive to Flipkart, and offline regional chains compete with Flipkart, so they are unlikely to hand it their customers [I].
- It has already served non-Flipkart products through a society app [V].
- It was rated 2.1 stars in 2022 [V, Inc42], so service quality has been a weakness.

**Servify has the B2B tooling and the 247around dispatch network.**

- Its focus is drifting away from India repair:
  - White-label plans are about 97% of operating income.
  - The US was about 51% of FY25 revenue [C, secondary citing Entrackr].
- Barriers are focus and priority, not capability [I].

**Bigfix is small** (5,000 transactions a month [C]), has only metro city pages, and already pitches Warrantify to retailers. Its barrier is scale.

**Urban Company, plus Reliance and Tata:**

- Urban Company could take referrals from retailers but has shown no sign of it. Its Tier 2/3 volume is thin.
- Reliance (resQ, and Justdial, where Reliance's majority stake is from my prior knowledge and was not re-checked) and Tata (Croma) would not serve rival regional chains. That leaves the regional chains as the open partner pool.

**Bottom line [I].** The channel idea alone is easy to copy for Onsitego and Zopper, which already hold the regional-counter relationships. A defensible position would need something they do not already have. Examples include proven agency quality and outcome data in specific cities, or exclusive multi-year chain agreements.

## 6. Failures, shutdowns, pivots and consolidation

**Housejoy:**
- Raised about $29.7M (Amazon, Matrix, Qualcomm Ventures).
- Laid off staff and cut from 12 cities to 5 metros around 2018 [V, Inc42].
- Moved to construction, renovation and interiors.
- housejoy.in did not respond on 2026-11-18. It has exited appliance repair.

**Other closures:**
- **Taskbob** shut in January 2017, after absorbing and closing Zepper.
- **Doormint** shut down.
- **LocalOye** laid off 60+ staff and was in acquisition talks with Quikr and Flipkart in 2016 (final outcome not found).
- **Zimmber** was absorbed into QuikrServices (all-stock, May 2017).
- A 2016 YourStory review said most on-demand home-service startups, except UrbanClap and Housejoy, had shut or consolidated, and about 90% of them were aggregators.

**Defunct or unknown:**
- **Mr Right** (Bengaluru, 2015) is likely defunct. Its domain now sells pest-control products.
- **HelloTechie** shows no evidence of operating. Its domain is for sale.
- **Pync** (house help, 2026) shut down, and its founders joined Snabbit. It is an adjacent case, not appliance repair.

**Pivots away from consumer repair operations:**
- **Bigfix** moved from consumer device repair with its own hubs (2015–19) to B2B "managed aftersales" (2023+).
- **SERVIZ** moved from running service operations to selling software.
- **Servify**'s revenue is now almost all white-label protection plans.
- **Qdigi** changed owners twice: Quess bought it for Rs 30 Cr in 2018 and sold it to Onsitego for Rs 80 Cr in 2024.

**Urban Company's own data:**
- Appliance growth "moderated" in FY26 because of weather.
- More than 90% of net NTV comes from its top 10 cities.
- Even the best-run marketplace has not yet built Tier 2/3 appliance repair at scale. That fits either "hard" or "open", and the evidence here cannot tell which [I].

**Pattern [I].** Consumer-acquired, operations-heavy home-service models have mostly failed or pivoted. The survivors earn on plans sold at purchase (Onsitego, OneAssist, Zopper, Servify) or on brand-paid work (247around, Qdigi). A retailer-sourced model avoids consumer acquisition cost, but it inherits the operations burden that sank the aggregators.

## 7. Verdict

**Partly served. Medium confidence.**

**What is served:**
- Post-warranty cover for customers of national and captive chains (resQ, Jeeves, Croma ZipCare).
- Plan-based post-warranty cover at many regional chains (Onsitego, Zopper, OneAssist).
- Pay-per-job repair in larger Tier 2 cities, through Urban Company price pages, brand service centres and Justdial-listed local shops.

**Not visibly served:**
- Regional chains' lapsed-warranty customers sold a job-based paid repair that is routed and quality-controlled across local agencies.
- That gap is evidence-limited. Offline and informal arrangements are invisible to web research.

**Main threats:**
- Onsitego and Zopper, which hold the counters.
- Eureka Forbes and Kent in RO, where brand AMCs capture the demand.
- The local agencies themselves, reached through Justdial and word of mouth.
