import json,re,csv,sys,collections
D,OUT=sys.argv[1],sys.argv[2]
rows=json.load(open(D+'/cities_stage1b.json'))
geo={}
try:
    for g in json.load(open(D+'/cities_stage2.json')): geo[(g['unit_name_census'],g['pop_2011'],g['state'])]=g
except FileNotFoundError: pass
A4I='https://censusindia.gov.in/nada/index.php/catalog/42876'
A4II='https://censusindia.gov.in/nada/index.php/catalog/42877'
HRAURL='https://finance.py.gov.in/sites/default/files/hra23aug18.pdf'
def nk(s): return re.sub(r'[^a-z]','',s.lower())
METRO_UA={('greatermumbai','Maharashtra'),('delhi','Delhi'),('kolkata','West Bengal'),('chennai','Tamil Nadu'),('bruhatbangalore','Karnataka'),('hyderabad','Telangana'),('ahmadabad','Gujarat'),('pune','Maharashtra')}
METRO_CORE={'greatermumbai','delhimunicipalcorporationurban','kolkata','chennai','bbmp','hyderabadmcorpog','ahmadabad','pune'}
# functional satellites outside the metro UA boundary (top-level units)
FUNC_SAT={('ghaziabad','Uttar Pradesh'):'NCR: Ghaziabad (DoE HRA OM 07.07.2017 para 6 extends Delhi X-rate)',('faridabad','Haryana'):'NCR: Faridabad (HRA OM para 6, Delhi X-rate)',('gurgaon','Haryana'):'NCR: Gurgaon (HRA OM para 6, Delhi X-rate)',('noida','Uttar Pradesh'):'NCR: NOIDA (HRA OM para 6, Delhi X-rate)',('greaternoida','Uttar Pradesh'):'NCR: Greater Noida, Gautam Buddha Nagar district adjoining Noida (analyst judgement)',
 ('vasaivirarcity','Maharashtra'):'MMR: Vasai-Virar (analyst judgement, Mumbai Metropolitan Region)',('bhiwandi','Maharashtra'):'MMR: Bhiwandi (analyst judgement, MMR)',('navimumbaipanvelraigarh','Maharashtra'):'MMR: Navi Mumbai Panvel node (analyst judgement)',('panvel','Maharashtra'):'MMR: Panvel (analyst judgement)',('kharghar','Maharashtra'):'MMR: Kharghar, Navi Mumbai node (analyst judgement)'}
HRA_X={'Telangana':['hyderabad'],'Delhi':['delhi'],'Gujarat':['ahmadabad'],'Karnataka':['bruhatbangalore'],'Maharashtra':['greatermumbai','pune'],'Tamil Nadu':['chennai'],'West Bengal':['kolkata']}
HRA_Y={'Andhra Pradesh':['vijayawada','visakhapatnam','guntur','nellore'],'Telangana':['warangal'],'Assam':['guwahati'],'Bihar':['patna'],'Chandigarh':['chandigarh'],
 'Chhattisgarh':['durgbhilainagar','raipur'],'Gujarat':['rajkot','jamnagar','bhavnagar','vadodara','surat'],'Haryana':['faridabad','gurgaon'],'Jammu & Kashmir':['srinagar','jammu'],
 'Jharkhand':['jamshedpur','dhanbad','ranchi','bokarosteelcity'],'Karnataka':['belgaum','hublidharwad','mangalore','mysore','gulbarga'],
 'Kerala':['kozhikode','kochi','thiruvananthapuram','thrissur','malappuram','kannur','kollam'],'Madhya Pradesh':['gwalior','indore','bhopal','jabalpur','ujjain'],
 'Maharashtra':['amravati','nagpur','aurangabad','nashik','bhiwandi','solapur','kolhapur','vasaivirarcity','malegaon','nandedwaghala','sangli'],
 'Odisha':['cuttack','bhubaneswar','raurkela'],'Puducherry':['puducherry'],'Punjab':['amritsar','jalandhar','ludhiana'],'Rajasthan':['bikaner','jaipur','jodhpur','kota','ajmer'],
 'Tamil Nadu':['salem','tiruppur','coimbatore','tiruchirappalli','madurai','erode'],
 'Uttar Pradesh':['moradabad','meerut','ghaziabad','aligarh','agra','bareilly','lucknow','kanpur','allahabad','gorakhpur','varanasi','saharanpur','noida','firozabad','jhansi'],
 'Uttarakhand':['dehradun'],'West Bengal':['asansol','siliguri','durgapur']}
HRA_Y_EXT={('shillong','Meghalaya'),('portblair','Andaman & Nicobar Islands'),('panchkula','Haryana'),('sasnagar','Punjab'),('panchkulaurbanestate','Haryana')}
HRA_DEP={'faridabad','gurgaon','ghaziabad','noida'}
def key(r): return nk(re.sub(r'\s+Cantonment$','',r['city']))
stk=lambda s: s.replace('Andhra Pradesh','Andhra Pradesh')
tops={}
for r in rows:
    if r['count_unit']: tops[r['unit_name_census']]=r
# map parent -> top row
byparentname={}
for r in rows:
    if r['count_unit']:
        pn=re.sub(r'\s+',' ',r['unit_name_census']); byparentname.setdefault(r['state_census2011'],[]).append(r)
def find_parent(r):
    if r['count_unit']: return None
    pk=nk(re.sub(r'U\.?\s?A.*$','',r['parent_ua']))
    cands=[t for t in rows if t['count_unit'] and t['is_ua'] and nk(re.sub(r'U\.?\s?A.*$','',t['unit_name_census'].split('(a')[0]))==pk and t['state_census2011']==r['state_census2011']]
    if not cands: cands=[t for t in rows if t['count_unit'] and t['is_ua'] and nk(t['city'])==pk]
    return cands[0] if cands else None
def band(p):
    if p is None: return 'UNKNOWN'
    if p>3000000: return 'Tier 1'
    if p>=500000: return 'Tier 2'
    if p>=100000: return 'Tier 3'
    if p>=50000: return 'Small town'
    return 'Below 50k'
hra_found=set()
def hra_for(t):
    k=key(t); st=t['state']
    stc=t['state_census2011']
    for S_,L in HRA_X.items():
        if (st==S_ or stc==S_) and k in L: hra_found.add((S_,k)); return 'X',''
    for S_,L in HRA_Y.items():
        if (st==S_ or stc==S_) and k in L:
            hra_found.add((S_,k))
            return 'Y',('Annexure lists only for HRA on dependency basis; para 6 continues Delhi X-rate' if k in HRA_DEP else '')
    if (k,st) in HRA_Y_EXT: return 'Y (para 6 extension)','HRA OM para 6 continues Y-class rate (not in annexure list)'
    if st=='Goa': return 'Y (para 6 extension)','HRA OM para 6 continues Y-class rate for "Goa" (city scope not specified)'
    return 'Z',''
out=[]
for r in rows:
    par=find_parent(r)
    unit=r if r['count_unit'] else par
    g=geo.get((r['unit_name_census'],r['pop_2011'],r['state']),{})
    mu = unit is not None and (nk(unit['city']),unit['state']) in METRO_UA and unit['is_ua']
    own=band(r['pop_2011'])
    if r['count_unit']:
        tier = 'Tier 1' if (mu or own=='Tier 1') else own
    else:
        tier = 'Tier 1' if (mu or own=='Tier 1') else own
    mkt = None
    if unit:
        mkt = 'Tier 1' if ((nk(unit['city']),unit['state']) in METRO_UA and unit['is_ua']) or band(unit['pop_2011'])=='Tier 1' else band(unit['pop_2011'])
    sat=0; basis=''
    if not r['count_unit'] and mu and nk(r['city']) not in METRO_CORE:
        sat=1; basis='Constituent of metro UA: '+unit['city']+' UA (Census 2011 A-4)'
    fk=(key(unit) if unit else key(r), unit['state'] if unit else r['state'])
    if fk in FUNC_SAT: sat=1; basis=FUNC_SAT[fk]
    hra,hnote=hra_for(unit if unit else r)
    rec={'city_id':r['city_id'],'city':r['city'],'state':r['state'].replace(' & ',' and '),'state_census2011':r['state_census2011'],'district':r['district'],
      'unit_type':r['unit_type'],'census_status_code':r['census_status_code'],'unit_name_census':r['unit_name_census'],
      'parent_ua':(par['city']+' UA' if par else ('UNKNOWN' if not r['count_unit'] else '')),
      'parent_ua_id':(par['city_id'] if par else ''),
      'count_unit':r['count_unit'],
      'pop_2011':r['pop_2011'],'pop_basis':'Census 2011 final, Table A-4 '+r['size_class']+' (UA total if unit_type=UA)',
      'pop_source_url':A4I if r['size_class']=='Class I' else A4II,'pop_source_year':2011,
      'lat':g.get('lat',''),'lon':g.get('lon',''),'coord_source':g.get('coord_source','') or ('' if g else 'NOT RUN'),
      'tier_pop':tier,'tier_pop_market_unit':mkt or 'UNKNOWN','tier_hra':hra,'tier_hra_note':hnote,'tier_hra_source_url':HRAURL,
      'metro_satellite':sat,'metro_satellite_basis':basis}
    out.append(rec)
BLANK={'ramapuram','eklahare','veerapandi','kasipalayame','ozar','jhunjhunun','mathura'}
for o in out:
    if o['lat']!='' and nk(o['city'].replace('Cantonment','')) in BLANK and ('OSM' in o['coord_source'] or 'WARN' in o['coord_source']):
        o['coord_source']='BLANK: rejected candidate ('+o['coord_source'][:100]+') failed manual/distance check'; o['lat']=o['lon']=''
    elif o['lat']=='' and not o['coord_source']: o['coord_source']='NOT FOUND (Wikipedia list, Wikipedia API, Wikidata, Nominatim)'
    if 'Cantonment' in o['city'] or 'Cantt' in o['city']:
        if o['coord_source'].startswith('OSM') and 'Cantonment' not in o['coord_source'] and 'Cantt' not in o['coord_source'] and 'Secunderabad' not in o['coord_source'] and 'Khadki' not in o['coord_source']:
            o['coord_source']+=' [APPROXIMATE: parent-city point, cantonment not separately geocoded]'
    if 'Tahsil, ' in o['coord_source'][:90] and o['coord_source'].split('(')[1].startswith(o['city'].split()[0]+' Tahsil'):
        o['coord_source']+=' [APPROXIMATE: tahsil-level result]'
# eligible core flag
for o in out:
    o['eligible_t2t3_core']=1 if (o['count_unit']==1 and o['tier_pop'] in ('Tier 2','Tier 3') and o['metro_satellite']==0) else 0
    o['eligible_small_town']=1 if (o['count_unit']==1 and o['tier_pop']=='Small town' and o['metro_satellite']==0) else 0
allhra={(s,k) for d in (HRA_X,HRA_Y) for s,L in d.items() for k in L}
print('HRA unmatched:',sorted(allhra-hra_found))
print('parent UNKNOWN:',[o['city'] for o in out if o['parent_ua']=='UNKNOWN'])
cols=list(out[0].keys())
with open(OUT+'/cities_raw.csv','w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=cols); w.writeheader(); w.writerows(out)
print(len(out))
c=collections.Counter((o['tier_pop']) for o in out if o['count_unit']); print(c)
print(collections.Counter(o['tier_hra'] for o in out if o['count_unit']))
print('sat',sum(o['metro_satellite'] for o in out), [o['city'] for o in out if o['metro_satellite'] and o['count_unit']])
el=collections.Counter(); 
for o in out:
    if o['eligible_t2t3_core']: el[(o['state'],o['tier_pop'])]+=1
json.dump({'el':[[s,t,n] for (s,t),n in el.items()]},open(D+'/eligible_counts.json','w'))
st=collections.Counter()
for (s,t),n in el.items(): st[s]+=n
for s,n in st.most_common(12): print(s,n,el[(s,'Tier 2')],el[(s,'Tier 3')])
print('tot T2',sum(v for (s,t),v in el.items() if t=='Tier 2'),'T3',sum(v for (s,t),v in el.items() if t=='Tier 3'), 'small',sum(o['eligible_small_town'] for o in out))
