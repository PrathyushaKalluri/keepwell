import csv, sys, json, os
from collections import Counter, defaultdict
OUTD=sys.argv[1]; SCR=sys.argv[2]; R="2026-11-18"
def cat(n):
    if n is None: return "UNKNOWN"
    return "A" if n==1 else "B" if n<=5 else "C" if n<=20 else "D" if n<=100 else "E"
rows=[]
def add(**k): rows.append(k)
add(retailer="Bajaj Electronics",parent_company="Electronics Mart India Ltd (EMIL); also trades as Electronics Mart in NCR",outlets=210,hq_state="Telangana",
 states_present="Telangana (108); Andhra Pradesh (70); Delhi (22); Haryana (7); Uttar Pradesh (3) [store locator]",
 outlets_source_url="https://www.bajajelectronics.com/stores (JSON/HTML endpoint /getstoredetails?stateId=..&cityId=0)",outlets_as_of="2026-11-18 (locator). Company-reported: 223 stores at 31-Mar-2026, 227 stores >100 cities in Q1 FY27 (secondary: quartr.com Q4 FY26 summary; sahi.com) - not reconciled with locator",
 appliance_categories_sold="AC; refrigerators; washing machines; water purifiers; TVs; mobiles; laptops; kitchen & small appliances (site navigation)",
 brands_sold="LG, Samsung, Whirlpool, Sony, Voltas, Bajaj, Kenstar, Philips, Panasonic, Morphy Richards, Apple and others (site navigation; not exhaustive)",
 website="https://www.bajajelectronics.com",store_locator_url="https://www.bajajelectronics.com/stores",
 own_service_department="UNKNOWN - no evidence of in-house repair; management says EW is serviced by third parties: 'We only facilitate the product on our floor' (Q1 FY24 call)",
 external_service_partners="OnsiteGo and OneAssist (extended warranty) - EMIL Q1 FY24 earnings call transcript: 'We started the insurance business with OnsiteGo and OneAssist'",
 post_warranty_services_evidence="Sells third-party extended warranty on mobiles, TVs, large appliances. Q1 FY24: ~Rs 12 cr EW revenue -> ~Rs 4 cr PBT ('we only book the percentage revenue')",
 listed_company="yes (NSE: EMIL / BSE: 543626)",revenue_latest="Rs 7,183.3 cr revenue from operations FY26 (secondary: scanx.trade; annual report not retrieved)",
 source_urls="https://www.bajajelectronics.com/stores | https://nsearchives.nseindia.com/corporate/EMIL_17082023183331_Transcript30062023.pdf | https://quartr.com/events/electronics-mart-india-limited-emil-q4-25-26_FR4dhJtA | https://scanx.trade/stock-market-news/companies/electronics-mart-india-fy26-results-revenue-up-6-7-7-183-crore/51875139",
 confidence="high (outlets, EW partners); medium (revenue)")
add(retailer="Aditya Vision",parent_company="Aditya Vision Ltd",outlets=207,hq_state="Bihar",
 states_present="Bihar (118); Uttar Pradesh (53); Jharkhand (33); Chhattisgarh (3) [Annual Report 2025-26]",
 outlets_source_url="https://nsearchives.nseindia.com/corporate/ADITYAVISION_10082026194121_AnnualReportFinalUPLOAD2026.pdf",outlets_as_of="2026-03-31 (filing). Secondary: 214 stores at 30-Sep-2026 (Bihar 120, UP 56, Jharkhand 33, Chhattisgarh 5) per multibagg/quartr summaries - not verified in filing",
 appliance_categories_sold="TVs; refrigerators; washing machines; AC; water purifiers; kitchen appliances; mobiles; laptops (website overview + AR)",
 brands_sold="'100+ domestic and international brands' (AR); names not listed",
 website="https://adityavision.in (corporate); https://adityavision.com (e-commerce)",store_locator_url="UNKNOWN (no locator found on corporate site; /store-locator returns 404)",
 own_service_department="partial: 'Aditya Seva' in-house after-sales helpline/helpdesk, open to non-customers; resolution via 'network of technological experts from all of our partner brands' (i.e. brand service, not own workshops)",
 external_service_partners="UNKNOWN (Aditya Suraksha underwriter/administrator not named)",
 post_warranty_services_evidence="Aditya Suraksha: own-branded extended warranty 'covering repair costs well beyond the manufacturer's warranty' with free doorstep pick-up and drop. FY26 'sale of services' Rs 51.73 cr vs Rs 27.88 cr FY25 (Note 43)",
 listed_company="yes (NSE: ADITYAVISION / BSE: 540205)",revenue_latest="Rs 2,671.62 cr revenue from operations FY2025-26 (Annual Report)",
 source_urls="https://nsearchives.nseindia.com/corporate/ADITYAVISION_10082026194121_AnnualReportFinalUPLOAD2026.pdf | https://adityavision.in/company/aditya-seva-aditya-suraksha.html | https://adityavision.in/company/overview.html",
 confidence="high")
add(retailer="Sathya",parent_company="Sathya Agencies Ltd (subsidiaries: Unilet Appliances Pvt Ltd; Sathya Mobiles)",outlets=427,hq_state="Tamil Nadu (Thoothukudi)",
 states_present="Tamil Nadu (301, incl. 35 mobile stores); Andhra Pradesh (65); Karnataka (54, Unilet); Kerala (4); Puducherry (3) [DRHP abridged prospectus]",
 outlets_source_url="https://www.sebi.gov.in/sebi_data/commondocs/apr-2026/Sathya%20Agencies%20Limited-Abridged%20Prospectus_p.pdf",outlets_as_of="2026-01-31 (DRHP dated 2026-03-30). 94.53% of stores in Tier II/II+ cities as at 2025-03-31",
 appliance_categories_sold="Large appliances (60.90% of FY25 net sale of goods); mobiles/IT (29.34%); small & kitchen appliances (9.76%); TVs, refrigerators, washing machines, AC named",
 brands_sold="UNKNOWN in filing extract; Hisense (2025 partnership news), Cellecor",
 website="https://sathya.in ; https://www.sathya.store",store_locator_url="UNKNOWN (sathya.store returned HTTP 403 to automated fetch)",
 own_service_department="UNKNOWN",external_service_partners="UNKNOWN",post_warranty_services_evidence="UNKNOWN (full DRHP not retrieved; abridged prospectus silent)",
 listed_company="no (DRHP filed; SEBI observation reported June 2026; not listed as of 2026-11-18 per ipoguru)",revenue_latest="Rs 3,496.87 cr revenue from operations FY2025 (Rs 34,968.73 mn); H1 FY26 Rs 1,996.67 cr",
 source_urls="https://www.sebi.gov.in/sebi_data/commondocs/apr-2026/Sathya%20Agencies%20Limited-Abridged%20Prospectus_p.pdf | https://www.franchiseindia.com/insights/en/news/sathya-agencies-acquires-unilet-appliances-adds-54-stores-in-karnataka.59972 | https://www.ipoguru.in/ipo/sathya-agencies-ipo",
 confidence="high (outlets, revenue); low (service)")
add(retailer="Unilet",parent_company="Unilet Appliances Pvt Ltd (acquired by Sathya Agencies, July 2025)",outlets=54,hq_state="Karnataka (Bengaluru)",
 states_present="Karnataka (46 MBOs + 8 EBOs) - INCLUDED in Sathya's 427",outlets_source_url="https://www.sebi.gov.in/sebi_data/commondocs/apr-2026/Sathya%20Agencies%20Limited-Abridged%20Prospectus_p.pdf",outlets_as_of="2026-01-31",
 appliance_categories_sold="consumer electronics and appliances (filing description); detail UNKNOWN",brands_sold="UNKNOWN",website="UNKNOWN (unilet.in did not resolve)",store_locator_url="UNKNOWN",
 own_service_department="UNKNOWN",external_service_partners="UNKNOWN",post_warranty_services_evidence="UNKNOWN",listed_company="no",revenue_latest="UNKNOWN",
 source_urls="https://www.sebi.gov.in/sebi_data/commondocs/apr-2026/Sathya%20Agencies%20Limited-Abridged%20Prospectus_p.pdf",confidence="high (count); do not double-count with Sathya")
add(retailer="Girias",parent_company="Girias Investment Pvt Ltd (per directory listing; not verified)",outlets=187,hq_state="Karnataka (Bengaluru)",
 states_present="Tamil Nadu (84), Karnataka (75), Puducherry (3), state not derivable (25) - states inferred from pincode prefix",
 outlets_source_url="https://www.giriasindia.com/stores?page=1..7",outlets_as_of="2026-11-18 (locator: 187 entries). Homepage claims '175+ Hyper Stores'",
 appliance_categories_sold="consumer durables / home appliances & electronics (homepage title); detail not captured",brands_sold="'Authorised seller of leading brands' (homepage); names not captured",
 website="https://www.giriasindia.com",store_locator_url="https://www.giriasindia.com/stores",
 own_service_department="UNKNOWN",external_service_partners="UNKNOWN",post_warranty_services_evidence="UNKNOWN",listed_company="no",revenue_latest="UNKNOWN",
 source_urls="https://www.giriasindia.com | https://www.giriasindia.com/stores",confidence="high (outlets); low (service)")
add(retailer="Darling Retail",parent_company="UNKNOWN (Darling group; also Darling Solar)",outlets=174,hq_state="Tamil Nadu",
 states_present="Tamil Nadu; Puducherry (8 in 'Puducherry' district bucket) [store locator DISTRICT_DATA, 40 districts]",
 outlets_source_url="https://darlingretail.com/pages/store-location (embedded DISTRICT_DATA JS array)",outlets_as_of="2026-11-18 (locator: 174 stores). Homepage text claims '185+ branches' and elsewhere '119+ retail outlets' (inconsistent)",
 appliance_categories_sold="AC; refrigerators; washing machines; laptops; furniture; gadgets; rooftop solar (site product chips)",brands_sold="Whirlpool, Haier and others (product listings; not exhaustive)",
 website="https://darlingretail.com",store_locator_url="https://darlingretail.com/pages/store-location",
 own_service_department="UNKNOWN (homepage mentions 'Darling Product Expert' guidance on installation only)",external_service_partners="UNKNOWN",post_warranty_services_evidence="UNKNOWN",listed_company="no",revenue_latest="UNKNOWN",
 source_urls="https://darlingretail.com/pages/store-location | https://darlingretail.com",confidence="high (outlets); low (service)")
add(retailer="Vasanth & Co",parent_company="UNKNOWN",outlets=153,hq_state="Tamil Nadu (Chennai)",
 states_present="Tamil Nadu (150); Puducherry (2); Karnataka (1) [branches page]",
 outlets_source_url="https://vasanthandco.in/branches",outlets_as_of="2026-11-18",
 appliance_categories_sold="AC; washing machines; refrigerators; water purifiers; water heaters; kitchen appliances; TVs; furniture (site navigation)",brands_sold="UNKNOWN",
 website="https://vasanthandco.in",store_locator_url="https://vasanthandco.in/branches",
 own_service_department="UNKNOWN",external_service_partners="UNKNOWN",post_warranty_services_evidence="UNKNOWN",listed_company="no",revenue_latest="UNKNOWN",
 source_urls="https://vasanthandco.in/branches",confidence="high (outlets); low (service)")
add(retailer="Value Plus",parent_company="Value Plus Retail Pvt Ltd (subsidiary of Vishal Video & Appliances Pvt Ltd)",outlets=135,hq_state="Uttar Pradesh (Noida)",
 states_present="Uttar Pradesh (60+ stores, 56 cities); West Bengal (25+, 14 cities); Uttarakhand (20+, 15 cities); Rajasthan (15+, 9 cities); Sikkim [company profile page]",
 outlets_source_url="https://www.valueplusretail.com/pages/store-locator ; https://www.valueplusretail.com/pages/llms-full-txt",outlets_as_of="2026-11-18 (site states '135 Stores'; '135+ stores across 113 cities')",
 appliance_categories_sold="consumer electronics, home appliances, mobiles, laptops, rooftop solar (company profile)",brands_sold="Havells, LG, Haier, Bajaj (dealer awards listed); full list UNKNOWN",
 website="https://www.valueplusretail.com",store_locator_url="https://www.valueplusretail.com/pages/store-locator",
 own_service_department="claimed: '135-store after-sales service network across North India' (self-description; nature of service UNKNOWN)",
 external_service_partners="OneAssist - 'FREE 1-Year Extended Warranty by OneAssist' on every phone (site banner)",
 post_warranty_services_evidence="Free 1-yr Valueplus/OneAssist EW on phones; 'Extended Warranty' policy page in footer; appliance EW UNKNOWN",
 listed_company="no",revenue_latest="'over Rs 750 crore (FY2025)' - self-reported on company site, not a filing",
 source_urls="https://www.valueplusretail.com/pages/llms-full-txt | https://www.valueplusretail.com/pages/store-locator",confidence="medium (self-reported)")
add(retailer="Vijay Sales",parent_company="Vijay Sales (India) Pvt Ltd (legal name not verified)",outlets=None,hq_state="Maharashtra (Mumbai)",
 states_present="UNKNOWN in detail (locator is JS-only; JS bundle blocked HTTP 406)",outlets_source_url="https://techlomedia.in/2026/03/vijay-sales-announces-holi-2026-sale-with-up-to-65-discount-across-categories-121388 ; https://digitalterminal.in/smart-phone/vijay-sales-launches-apple-days-2026-with-massive-discounts-and-exchange-offers-across-india",
 outlets_as_of="news: '140+ stores' (Mar 2026) / '160+ retail outlets' (Apr 2026) - conflicting; exact count UNKNOWN; category E either way",
 appliance_categories_sold="AC; home & kitchen appliances; TVs; mobiles; laptops (site navigation)",brands_sold="Apple, Samsung, OnePlus, LG, Sony, Dyson and others (site)",
 website="https://www.vijaysales.com",store_locator_url="https://www.vijaysales.com/store-locator",
 own_service_department="UNKNOWN (an app 'com.vijaysales.vscare' is linked from the site; its function not verified)",
 external_service_partners="Onsitego - VS+ Extended Warranty: 'repaired by Onsitego authorised personnel' (vijaysales.com/vswarranty)",
 post_warranty_services_evidence="VS+ Extended Warranty up to 4 additional years after manufacturer warranty; AC plans include 1 preventive maintenance visit per year",
 listed_company="no",revenue_latest="UNKNOWN",source_urls="https://www.vijaysales.com/vswarranty | https://www.vijaysales.com/store-locator",category_override="E (news: 140+/160+)",
 confidence="high (EW partner); low (outlet count)")
add(retailer="Pittappillil Agencies",parent_company="Pittappillil group",outlets=82,hq_state="Kerala (Perumbavoor)",
 states_present="Kerala (13 districts in locator)",outlets_source_url="https://www.pittappillilonline.com/store-locator",outlets_as_of="2026-11-18 (locator: 82 entries; site FAQ: 'We have 81 showrooms located throughout Kerala')",
 appliance_categories_sold="home appliances incl. water purifiers, water heaters, refrigerators, washing machines, AC, kitchen appliances (site categories)",brands_sold="UNKNOWN",
 website="https://www.pittappillilonline.com",store_locator_url="https://www.pittappillilonline.com/store-locator",
 own_service_department="partial: FAQ says 'You can visit your nearest showroom for service or support'; in-house repair workforce not verified",
 external_service_partners="UNKNOWN",post_warranty_services_evidence="Own extended warranty 'Wecare/WE CARE' for a nominal premium, starting after manufacturer warranty, 'same terms and condition of manufacturers warranty'",
 listed_company="no",revenue_latest="UNKNOWN",source_urls="https://www.pittappillilonline.com | https://www.pittappillilonline.com/store-locator",confidence="high")
add(retailer="Great Eastern Retail",parent_company="Great Eastern Retail Pvt Ltd (legal form not verified)",outlets=76,hq_state="West Bengal (Kolkata)",
 states_present="West Bengal (33); Rajasthan (14); Delhi (13); Uttar Pradesh (9); Odisha (6); Andhra Pradesh (1) [locator, pincode sweep]",
 outlets_source_url="https://www.greateasternretail.com/store-locator (POST /find-store by pincode; 100+ pincodes swept)",outlets_as_of="2026-11-18 (locator sweep: 76; may be incomplete). News Sept 2025: '90+ stores across seven states' (Hisense partnership)",
 appliance_categories_sold="water purifiers, TVs, cameras, home appliances (site navigation)",brands_sold="Hisense (2025 partnership); others UNKNOWN",
 website="https://www.greateasternretail.com",store_locator_url="https://www.greateasternretail.com/store-locator",
 own_service_department="UNKNOWN",external_service_partners="UNKNOWN",post_warranty_services_evidence="UNKNOWN (third-party page says it 'extends warranties' - not verified)",listed_company="no",revenue_latest="UNKNOWN",
 source_urls="https://www.greateasternretail.com/store-locator | https://www.indianretailer.com/news/hisense-partners-great-eastern-retail-add-90-stores-across-seven-states",confidence="medium")
add(retailer="Nandilath G-Mart",parent_company="Nandilath Group",outlets=59,hq_state="Kerala",
 states_present="Kerala (14 districts in locator)",outlets_source_url="https://nandilathgmart.com/our-stores/",outlets_as_of="2026-11-18",
 appliance_categories_sold="AC; refrigerators; washing machines; water heaters; kitchen appliances; TVs; mobiles (site navigation)",brands_sold="Hisense (partnership news), Impex and others",
 website="https://nandilathgmart.com",store_locator_url="https://nandilathgmart.com/our-stores/",
 own_service_department="UNKNOWN (site claims 'exceptional after-sales support', unspecified)",external_service_partners="UNKNOWN",post_warranty_services_evidence="UNKNOWN (site search for 'extended warranty' returned no plan products)",listed_company="no",revenue_latest="UNKNOWN",
 source_urls="https://nandilathgmart.com/our-stores/ | https://bwretailworld.com/companies/hisense-india-deepens-kerala-presence-with-nandilath-group-partnership",confidence="high (outlets)")
add(retailer="Oxygen The Digital Expert",parent_company="UNKNOWN",outlets=38,hq_state="Kerala (Kottayam)",
 states_present="Kerala (10 districts in locator)",outlets_source_url="https://www.oxygendigitalshop.com/pages/store-locator",outlets_as_of="2026-11-18 (38 store cards on oxygendigitalshop.com; separate 'Oxygen Digital Expert' larger-format count, if any, UNKNOWN)",
 appliance_categories_sold="mobiles; laptops; TVs; washing machines; refrigerators; AC stabilisers; kitchen appliances; inverters (site)",brands_sold="UNKNOWN",
 website="https://www.oxygendigitalshop.com",store_locator_url="https://www.oxygendigitalshop.com/pages/store-locator",
 own_service_department="no (for warranty): Warranty Policy - 'does not independently provide any warranty'; 'All warranty claims... must be raised directly at the manufacturer's authorized service centre'",
 external_service_partners="UNKNOWN (sells an 'Extended Warranty' product category; provider not named)",post_warranty_services_evidence="'Extended Warranty' listed among items dealt (homepage); terms UNKNOWN",listed_company="no",revenue_latest="UNKNOWN",
 source_urls="https://www.oxygendigitalshop.com/pages/warranty-policy | https://www.oxygendigitalshop.com/pages/store-locator",confidence="high")
add(retailer="Lotus Electronics",parent_company="UNKNOWN",outlets=28,hq_state="Madhya Pradesh (Indore)",
 states_present="Madhya Pradesh (15); Chhattisgarh (5); Maharashtra (4, Nagpur); Rajasthan (4, Jaipur)",
 outlets_source_url="https://www.lotuselectronics.com/contact-us/{city} (schema.org Store JSON-LD, 9 city pages)",outlets_as_of="2026-11-18",
 appliance_categories_sold="refrigerators; washing machines; AC; water purifiers; kitchen & floor-care appliances; TVs; mobiles (site)",brands_sold="LG, Haier, Apple, Samsung, Godrej, Eureka Forbes, boAt and others (site brand stores)",
 website="https://www.lotuselectronics.com",store_locator_url="https://www.lotuselectronics.com/stores",
 own_service_department="UNKNOWN",external_service_partners="UNKNOWN",post_warranty_services_evidence="UNKNOWN (site search for 'extended warranty' returned no plan)",listed_company="no",revenue_latest="UNKNOWN",
 source_urls="https://www.lotuselectronics.com/stores | https://www.lotuselectronics.com/contact-us/indore",confidence="high (outlets)")
add(retailer="Sales India",parent_company="Sales India Pvt Ltd",outlets=None,hq_state="Gujarat (Ahmedabad)",
 states_present="Gujarat (detail UNKNOWN)",outlets_source_url="https://salesindia.com/stores",outlets_as_of="site text '35+ stores' (2026-11-18); locator is JS-only (not parsed)",
 appliance_categories_sold="home appliances & electronics (site title)",brands_sold="UNKNOWN",website="https://salesindia.com",store_locator_url="https://salesindia.com/stores",
 own_service_department="UNKNOWN",external_service_partners="UNKNOWN",post_warranty_services_evidence="UNKNOWN",listed_company="no",revenue_latest="UNKNOWN",
 source_urls="https://salesindia.com/stores",confidence="medium (self-reported '35+')",category_override="D (from '35+' claim)")
add(retailer="Viveks",parent_company="Vivek Ltd (legal name not verified)",outlets=23,hq_state="Tamil Nadu (Chennai)",
 states_present="Tamil Nadu (5 cities)",outlets_source_url="https://viveks.com/page/about-us",outlets_as_of="date UNKNOWN; '23 showrooms spread across 5 cities in Tamil Nadu' (about-us page via search; viveks.com returned HTTP 522 on 2026-11-18)",
 appliance_categories_sold="consumer electronics & home appliances",brands_sold="UNKNOWN",website="https://viveks.com",store_locator_url="UNKNOWN",
 own_service_department="partial/low confidence: EW page refers customers to a 'Viveks Service Centre' phone line",external_service_partners="UNKNOWN",
 post_warranty_services_evidence="Viveks Extended Warranty: up to 4 more years after manufacturer warranty; contract 'between the buyer and Viveks' (per media.viveks.com/extended-warranty, seen only via search snippet; page unreachable)",
 listed_company="no",revenue_latest="UNKNOWN",source_urls="https://viveks.com/page/about-us | https://media.viveks.com/extended-warranty",confidence="low (site unreachable; search-snippet evidence)")
add(retailer="Kohinoor Electronics",parent_company="UNKNOWN",outlets=13,hq_state="Maharashtra (Mumbai)",
 states_present="Maharashtra - Mumbai (7), Thane district (6) [locator]",outlets_source_url="https://www.kohinoorelectronics.com/store-locator (POST /find-store by pincode)",outlets_as_of="2026-11-18 (23 Maharashtra/Goa pincodes swept)",
 appliance_categories_sold="consumer electronics & appliances (site)",brands_sold="LG, Bose, JBL, Marshall, boAt and others (site)",website="https://www.kohinoorelectronics.com",store_locator_url="https://www.kohinoorelectronics.com/store-locator",
 own_service_department="UNKNOWN",external_service_partners="UNKNOWN",post_warranty_services_evidence="UNKNOWN",listed_company="no",revenue_latest="UNKNOWN",
 source_urls="https://www.kohinoorelectronics.com/store-locator",confidence="high (outlets)")
add(retailer="Pai International",parent_company="Pai International Electronics Ltd (per dealer listings)",outlets=None,hq_state="Karnataka (Bengaluru)",
 states_present="Karnataka, Telangana, Andhra Pradesh (2017 report)",outlets_source_url="https://www.deccanherald.com/business/pai-international-opens-showroom-bengaluru-2016835",outlets_as_of="2017: 'over 80 showrooms' - outdated; current count UNKNOWN (website JS-only, no locator data)",
 appliance_categories_sold="laptops, mobiles, AC and appliances (site title)",brands_sold="LG, Sony (dealer listings)",website="https://www.paiinternational.in",store_locator_url="UNKNOWN",
 own_service_department="UNKNOWN",external_service_partners="UNKNOWN",post_warranty_services_evidence="UNKNOWN",listed_company="no",revenue_latest="UNKNOWN",
 source_urls="https://www.deccanherald.com/business/pai-international-opens-showroom-bengaluru-2016835",confidence="low",category_override="UNKNOWN (D in 2017)")
add(retailer="Croma",parent_company="Infiniti Retail Ltd (Tata group)",outlets=None,hq_state="Maharashtra (Mumbai)",
 states_present="pan-India, 200+ cities",outlets_source_url="https://www.analyticsinsight.net/amp/story/press-release/croma-unveils-edge-a-digital-first-neighbourhood-retail-format",outlets_as_of="Aug 2026 press release: '560+ stores across 200+ cities' (exact UNKNOWN)",
 appliance_categories_sold="full range incl. AC, refrigerators, washing machines, water purifiers",brands_sold="550+ brands incl. Croma private label (indiaretailing.com, older)",website="https://www.croma.com",store_locator_url="https://www.croma.com/store-locator (HTTP 403 to automated fetch)",
 own_service_department="UNKNOWN",external_service_partners="ZipCare ('ZipCare Protect - Advanced' plans for Croma in-house products, support customersupport@zipcare.in); Onsitego named as a Croma partner in 2019",
 post_warranty_services_evidence="ZipCare Protect plans start after manufacturer warranty; buy within ~11 months; onsite or ASC repair (product listings via search; croma.com blocked direct fetch)",
 listed_company="no (Tata subsidiary)",revenue_latest="UNKNOWN",source_urls="https://croma.com/zipcare-protect-advanced-2-years-for-croma-television-/p/280980 | https://www.pressreader.com/india/my-mobile/20190815/281573767322543",
 confidence="medium",category_override="E")
add(retailer="Reliance Digital",parent_company="Reliance Retail Ventures Ltd (Reliance Industries)",outlets=None,hq_state="Maharashtra (Mumbai)",
 states_present="pan-India",outlets_source_url="https://www.reliancedigital.in/locateus",outlets_as_of="locator page '695+ stores across 200+ cities' (seen via search snippet); Reliance Retail CE formats incl. MyJio: 'Over 8,000 Stores' (relianceretail.com)",
 appliance_categories_sold="full range incl. AC, refrigerators, washing machines, water purifiers",brands_sold="multi-brand + own brands",website="https://www.reliancedigital.in",store_locator_url="https://www.reliancedigital.in/locateus",
 own_service_department="yes: resQ - 'India's first multi-product, multi-brand, and multi-location service network' (RIL AR 2025-26); 1,621 service centre locations at Q1 FY26 (secondary)",
 external_service_partners="resQ is in-house; financing partners incl. Bajaj Finserv",post_warranty_services_evidence="resQ Care Plans (extended warranty) and 'newer plans, additional categories' (RIL AR 2025-26); resQ revenue +27% YoY in Q1 FY27 (secondary)",
 listed_company="no (RRVL unlisted; parent RIL listed)",revenue_latest="UNKNOWN for Reliance Digital alone",
 source_urls="https://www.ril.com/ar2025-26/retail.html | https://relianceretail.com/our-business.html | https://www.retail-insight-network.com/news/reliance-industries-limited-q1-fy26/",confidence="high (resQ existence); medium (counts)",category_override="E")
add(retailer="Ezone",parent_company="Future Group (historic)",outlets=None,hq_state="Maharashtra",states_present="UNKNOWN",outlets_source_url="UNKNOWN (www.ezoneonline.in did not resolve on 2026-11-18)",outlets_as_of="UNKNOWN",
 appliance_categories_sold="UNKNOWN",brands_sold="UNKNOWN",website="https://www.ezoneonline.in (unreachable)",store_locator_url="UNKNOWN",own_service_department="UNKNOWN",
 external_service_partners="Onsitego named Ezone as a retail partner (2019 interview)",post_warranty_services_evidence="UNKNOWN (current)",listed_company="no",revenue_latest="UNKNOWN",
 source_urls="https://www.pressreader.com/india/my-mobile/20190815/281573767322543",confidence="low; current operating status UNKNOWN")
add(retailer="Adishwar Auto Ride",parent_company="Adishwar Auto Ride India Pvt Ltd (not verified)",outlets=None,hq_state="Karnataka (UNKNOWN - not verified)",states_present="UNKNOWN",outlets_source_url="UNKNOWN (adishwar.com returned a 114-byte page; adishwarindia.com redirected to an IIS default page)",outlets_as_of="UNKNOWN",
 appliance_categories_sold="UNKNOWN",brands_sold="UNKNOWN",website="UNKNOWN",store_locator_url="UNKNOWN",own_service_department="UNKNOWN",external_service_partners="UNKNOWN",post_warranty_services_evidence="UNKNOWN",listed_company="no",revenue_latest="UNKNOWN",
 source_urls="https://www.adishwar.com (no content)",confidence="none - gap")
cols=["retailer","parent_company","category_by_outlets","hq_state","states_present","outlets_national","outlets_source_url","outlets_as_of","appliance_categories_sold","brands_sold","website","store_locator_url","own_service_department","external_service_partners","post_warranty_services_evidence","listed_company","revenue_latest","source_urls","retrieved","confidence"]
with open(os.path.join(OUTD,'retailers.csv'),'w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=cols); w.writeheader()
    for r in rows:
        o=dict(r); n=o.pop('outlets'); co=o.pop('category_override',None)
        o['outlets_national']=str(n) if n is not None else "UNKNOWN"
        o['category_by_outlets']=co or cat(n); o['retrieved']=R
        w.writerow(o)
print(len(rows))
# city counts
cc=[]
outl=list(csv.DictReader(open(os.path.join(OUTD,'retailer_outlets.csv'))))
agg=defaultdict(int); src={}
for x in outl:
    k=(x['retailer'],x['city'],x['state']); agg[k]+=1; src[k]=x['source_url'].split(' (')[0]
for (ret,c,s),n in sorted(agg.items()): cc.append(dict(retailer=ret,city=c,state=s,outlet_count=n,source_url=src[(ret,c,s)],basis="store locator"))
for d,stores in json.load(open(os.path.join(SCR,'darling_districts.json'))):
    cc.append(dict(retailer="Darling Retail",city=d+" (district)",state="Puducherry" if d=="Puducherry" else "Tamil Nadu",outlet_count=len(stores),source_url="https://darlingretail.com/pages/store-location",basis="store locator"))
for s,n in [("Bihar",118),("Uttar Pradesh",53),("Jharkhand",33),("Chhattisgarh",3)]:
    cc.append(dict(retailer="Aditya Vision",city="ALL (state total, 2026-03-31)",state=s,outlet_count=n,source_url="https://nsearchives.nseindia.com/corporate/ADITYAVISION_10082026194121_AnnualReportFinalUPLOAD2026.pdf",basis="filing"))
for s,n in [("Tamil Nadu",301),("Andhra Pradesh",65),("Karnataka",54),("Kerala",4),("Puducherry",3)]:
    cc.append(dict(retailer="Sathya",city="ALL (state total, 2026-01-31)",state=s,outlet_count=n,source_url="https://www.sebi.gov.in/sebi_data/commondocs/apr-2026/Sathya%20Agencies%20Limited-Abridged%20Prospectus_p.pdf",basis="filing"))
for s,n in [("Uttar Pradesh","60+ (56 cities)"),("West Bengal","25+ (14 cities)"),("Uttarakhand","20+ (15 cities)"),("Rajasthan","15+ (9 cities)"),("Sikkim","UNKNOWN")]:
    cc.append(dict(retailer="Value Plus",city="ALL (state total)",state=s,outlet_count=n,source_url="https://www.valueplusretail.com/pages/llms-full-txt",basis="news (company website self-description)"))
with open(os.path.join(OUTD,'retailer_city_counts.csv'),'w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=["retailer","city","state","outlet_count","source_url","basis"]); w.writeheader(); [w.writerow(r) for r in cc]
print(len(cc))
