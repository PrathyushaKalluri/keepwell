# Retail market context: appliance retail in India, and whether retailers will refer repair work

Retrieved 2026-11-18 unless stated otherwise. Every fact carries a source. Labels: **[filing]** = annual report, DRHP or exchange filing; **[official]** = the company's own site; **[secondary]** = news, broker note or aggregator; **[snippet]** = seen only in a search-result summary because the page itself could not be fetched (treat as low confidence).

---

## 1. Market structure

### Organised vs general trade
- **CRISIL, cited in the Sathya Agencies DRHP (Mar 2026):** the consumer durables and electronics retail market was about Rs 5,318 bn in FY25 (12.2% CAGR FY20–25), projected at Rs 8,400–8,800 bn by FY30. The organised segment was about **56.6%** of consumer durables in FY25 and is projected at about 59.6% by FY28. Large-format retailers were **33–38% by volume** in FY25. South India is 25–30% of the national market, and Tamil Nadu is 26–31% of the South. [filing] https://www.sebi.gov.in/sebi_data/commondocs/apr-2026/Sathya%20Agencies%20Limited-Abridged%20Prospectus_p.pdf
- **Redseer (30 Jul 2025):** "General trade still accounts for ~40% of the market" for appliances and electronics overall. Local shops "thrive on local trust and personal service" beyond the metros. Online "dominate[s] in electronics like mobiles and accessories", while online penetration of appliances is lower. No separate split for large appliances is given. [secondary] https://redseer.com/articles/indias-130-billion-appliances-market-opportunity/
- **CRISIL, cited in the EMIL IPO notes (2022):** the consumer durables industry was about Rs 3.2 tn in FY22. B&M chains hold the largest part of organised retail. [secondary] https://www.icicidirect.com/mailimages/IDirect_ElectronicsMart_IPOReview.pdf ; https://www.hdfcsec.com/hsl.docs/Electrnoics%20Mart%20India%20Limited%20IPO%20Note-202210031436456872608.pdf
- **Online:** electronics are about 13% of online retail. Online electronics growth swung to +22% in H1 FY26, helped by the GST cut on large appliances (28% to 18%, Sept 2025). [secondary/snippet] https://indiantelevision.com/mam/online-electronics-growth-hits-20-per-cent-as-festive-demand-shifts-early/
- **Gap:** no public source gives the online share of ACs, refrigerators, washing machines or water purifiers specifically. I found no Technopak or CEAMA channel split.

### Regional vs national chains (store counts, latest available)
| Chain | Outlets | Basis |
|---|---|---|
| Reliance Digital | 695+ stores, 200+ cities | locator page [snippet]; all Reliance Retail CE formats incl. MyJio: "Over 8,000 Stores" [official] |
| Croma (Tata) | 560+ stores, 200+ cities (Aug 2026) | [secondary] |
| Sathya Agencies | 427 (31 Jan 2026); 94.53% in Tier II/II+ cities | [filing] |
| Bajaj Electronics / EMIL | 210 on locator; 223 company-reported at 31 Mar 2026 | [official]/[secondary] |
| Aditya Vision | 207 (31 Mar 2026); claims >50% share in Bihar | [filing] |
| Girias | 187 on locator | [official] |
| Darling Retail | 174 on locator | [official] |
| Vijay Sales | 140+ to 160+ (conflicting, 2026) | [secondary] |
| Vasanth & Co | 153 on locator | [official] |
| Value Plus | 135 (self-reported) | [official] |

- Sathya calls itself "fifth largest in India among our peers" by FY25 revenue (CRISIL). [filing]
- EMIL was described in 2022 as "the largest regional organised player in the southern region". [secondary] HDFC note above.
- Regional chains are deeply Tier 2/3. Outside the metros: Sathya has 94.5% of its stores; Pittappillil, Nandilath, Oxygen and Lotus have 100%; Vasanth & Co has 123/153, Girias 126/187 and Bajaj Electronics 119/210 (computed from `retailer_outlets.csv`).

## 2. How many independent appliance retailers exist: brand dealer counts as a proxy
I found no current census or CEAMA estimate of independent consumer-durable retailers. Proxies:
- **LG Electronics India (RHP, Jun 2025):** 35,640 B2C touchpoints. These are 30,726 distributors and sub-dealers, 777 brand shops, 1,134 multi-brand outlets, 1,615 regional specialty stores and 1,385 modern trade outlets. It also has 1,006 authorised service centres. LG's distributor base is 1.2x that of the next-largest player. [secondary, quoting the RHP] https://www.icicidirect.com/mailcontent/idirect_lgelectronicsindia_iporeview-oct25.pdf
  - **Implication:** about 86% of LG's touchpoints are dealers and sub-dealers, which is general trade.
  - Regional specialty chains are a separate 1,615-outlet bucket.
- **Voltas:** "over 30,000 touch points". [secondary/snippet] https://www.share.market/buzz/trending/voltas-ac-million/
- **Blue Star:** ">900 towns, >10,000 retail outlets, >2,100 service partners". [snippet; mysmartprice.com returned 403]
- **Eureka Forbes (water purifiers, AR FY26):**
  - 19,500+ pin codes, 9,000+ service technicians, 1,650+ service partners, a database of 14 mn+ customers. [official] https://www.eurekaforbes.com/media/investor-relations/interactive-fy26-annual-report/extensive-pan-india.html
  - Distributes through direct sales, modern and general trade, and e-commerce. [filing] MD&A PDF.
- **Historic only:** Francis Kanoi's 2004 dealer census said more than 100,000 CE&A outlets had been added since 2000. [secondary] https://www.exchange4media.com/marketing-news/vcd/dvd-players-boost-ce-a-expansion-in-india-12377.html
- Statista counts 8,552 consumer-electronics chain stores (2021, chains only). [secondary]
- Havells, Whirlpool and Godrej dealer counts: UNKNOWN (annual reports not retrieved).

## 3. Evidence on whether retailers will refer repair work or sell service

### 3a. Extended-warranty commission economics (FOR)
- **EMIL / Bajaj Electronics, Q1 FY24 call, primary transcript:**
  - "We started the insurance business with OnsiteGo and OneAssist… We did around Rs. 12 odd crores in the first quarter as the revenue from that business which contributed to around Rs. 4 crores at the PBT level."
  - "We only facilitate the product on our floor. We only book the percentage revenue."
  - This implies roughly a third of EW revenue reaches PBT. It also shows the chain sells service but does not deliver it.
  - [filing] https://nsearchives.nseindia.com/corporate/EMIL_17082023183331_Transcript30062023.pdf
- **Aditya Vision:** "sale of services" was Rs 51.73 cr in FY26, up from Rs 27.88 cr in FY25 (+86%). That is about 1.9% of Rs 2,671.62 cr revenue (Note 43, AR 2025-26). The note does not say what this line consists of; Aditya Suraksha EW is the likely driver, but that is an inference. [filing] https://nsearchives.nseindia.com/corporate/ADITYAVISION_10082026194121_AnnualReportFinalUPLOAD2026.pdf
- **Generic benchmark (not India-specific):** EW costs 20–30% of product price; some retailers pay associates up to 15% commission. [secondary] https://en.wikipedia.org/wiki/Extended_warranty
- **Gap:** I found no published commission rate for Indian EW providers (Onsitego, OneAssist, Zopper, Servify) for retailers.

### 3b. Retailers with their own service arms or own-branded EW
- **Reliance Digital – resQ:**
  - "India's first multi-product, multi-brand, and multi-location service network"; it "expanded service availability through newer plans, additional categories and strengthened service centres". [filing] https://www.ril.com/ar2025-26/retail.html
  - 1,621 service-centre locations at Q1 FY26 (+31% YoY). [secondary] https://www.retail-insight-network.com/news/reliance-industries-limited-q1-fy26/
- **Aditya Vision:**
  - "Aditya Seva" is an in-house after-sales helpline, "available to anyone… [even if not] purchased… through our stores". It resolves issues via "technological experts from all of our partner brands".
  - "Aditya Suraksha" is its own EW, with free doorstep pick-up and drop. [official] https://adityavision.in/company/aditya-seva-aditya-suraksha.html
- **Pittappillil:** its own EW "Wecare", for a nominal premium after the manufacturer's warranty ends. Its FAQ says "visit your nearest showroom for service or support". [official] https://www.pittappillilonline.com
- **Viveks:** an own EW of up to 4 more years; the "contract between the buyer and Viveks"; a "Viveks Service Centre" phone line. [snippet; site unreachable] https://media.viveks.com/extended-warranty
- **Value Plus:** claims a "135-store after-sales service network". [official, self-description]

### 3c. Retailer and service-provider partnerships
| Retailer | Partner | Source |
|---|---|---|
| Bajaj Electronics / EMIL | OnsiteGo, OneAssist | [filing] transcript above |
| Vijay Sales | Onsitego (VS+ EW: "repaired by Onsitego authorised personnel"; AC plans include one preventive maintenance visit per year) | [official] https://www.vijaysales.com/vswarranty |
| Value Plus | OneAssist ("FREE 1-Year Extended Warranty by OneAssist" on phones) | [official] https://www.valueplusretail.com/pages/store-locator |
| Croma | ZipCare ("ZipCare Protect – Advanced", Croma in-house products only) | [snippet; croma.com 403] |
| Croma, Vijay Sales, Ezone | Onsitego (named as partners in 2019) | [secondary] https://www.pressreader.com/india/my-mobile/20190815/281573767322543 |

- **Note:** every partnership found is for **extended warranty or insurance** (a risk product). None is for referring **paid, out-of-warranty, pay-per-job repair** to local agencies. That is the exact model under study, and I found no precedent.

### 3d. Failed partnerships
- I found no documented failure of a retailer and repair or EW partnership in India.
- Adjacent evidence:
  - **Mis-selling:** a Chembur dealer sold a TV buyer a Bajaj Allianz insurance policy presented as an "extended warranty" (Rs 4,523). The buyer planned a consumer-forum complaint against the dealer, the manufacturer and the insurer. [secondary] https://www.moneylife.in/article/when-a-tv-buyer-was-sold-insurance-policy-as-extended-warranty/56620.html
  - **Claim rejections:** consumer reviews allege OneAssist claim rejections. [secondary] https://ca.trustpilot.com/review/www.oneassist.in

## 4. Facts and quotes that argue AGAINST the idea
1. **Retailers disclaim after-sales responsibility.**
   - Oxygen: "does not independently provide any warranty… All warranty claims, repairs, or replacements must be raised directly at the manufacturer's authorized service centre. We will not entertain any claims… on behalf of the manufacturer." [official] https://www.oxygendigitalshop.com/pages/warranty-policy
2. **The large chains already monetise the post-warranty slot.**
   - Through their own arms: Reliance (resQ), Aditya Vision (Suraksha), Pittappillil (Wecare), Viveks.
   - Through incumbent EW partners: EMIL (Onsitego, OneAssist), Vijay Sales (Onsitego), Value Plus (OneAssist), Croma (ZipCare).
   - A referral startup would compete with an existing revenue line, or have to sit underneath it.
3. **Brands keep post-warranty service in-house, especially water purifiers.**
   - Eureka Forbes: "strengthen its recurring revenue streams through its services, AMC and filters business. AMC bookings grew at a double-digit rate in every quarter of FY26". [filing] MD&A https://www.eurekaforbes.com/media/investor-relations/interactive-fy26-annual-report/assets/pdfs/Eureka-Forbes-AR-2025-26-MDA.pdf
   - Service is reported as 31.4% of revenue. [secondary] https://www.multibagg.ai/market-pulse/articles/eureka-fy26-94303
   - LG has 1,006 authorised service centres; Blue Star has >2,100 service partners [snippet].
4. **The retailer acts only as a channel.** EMIL: "This is done through a third-party vendor… We don't take care of the insurance from our end." Retailers want a commission without operational liability; they have not shown appetite to own repair quality.
5. **The service line is small relative to retail.** Aditya Vision's service revenue is about 1.9% of revenue. EMIL's EW was about Rs 12 cr in a roughly Rs 1,500+ cr quarter (quarterly revenue inferred from FY26 Rs 7,183 cr / 4; not verified for Q1 FY24). Repair referral is unlikely to be a priority for chain management.
6. **Reputation risk sits with the retailer.** The mis-selling case named the dealer as a respondent, which makes retailers wary of attaching their brand to third-party service failures.
7. **Thin retail margins create both pressure and incentive.** Vijay Sales director: "making 2-3% profit". [secondary] https://www.outlookbusiness.com/regional-brand/taking-on-the-giants-1034

## 5. Facts that argue FOR (summary)
- EW and service is profitable for regional chains. EMIL gets about Rs 4 cr PBT from Rs 12 cr revenue in one quarter, and Aditya Vision's service revenue grew 86% YoY.
- At least 8 of 22 chains already sell post-warranty service, so the shop floor already handles it.
- Aditya Seva serves non-customers too, which shows a regional chain values owning the after-sales relationship.
- Regional chains sit where brand service is thinnest (Tier 2/3). Sathya has 94.5% of its stores in Tier II/II+.
- Most of the chains with service partnerships are mid-sized regionals, not the nationals. Partners are third-party EW firms, which shows chains will plug in an outside provider.
