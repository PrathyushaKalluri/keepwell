import json,re,csv,sys
D=sys.argv[1]
u=json.load(open(D+'/xls/units2.json'))
# district -> state(s) from A-1
dist2st={}
for r in csv.reader(open(D+'/xls/a1.csv')):
    if len(r)>5 and r[3]=='DISTRICT' and r[5]=='Total':
        k=re.sub(r'[^a-z]','',re.sub(r'\(.*?\)','',r[4]).lower())
        dist2st.setdefault(k,set()).add((r[0],r[1]))
STCODE={}
for r in csv.reader(open(D+'/xls/a1.csv')):
    if len(r)>5 and r[3]=='STATE' and r[5]=='Total': STCODE[r[0]]=re.sub(r'\s*[@&$]+\s*$','',r[4]).strip()
TITLE={'JAMMU & KASHMIR':'Jammu & Kashmir','NCT OF DELHI':'Delhi','ANDAMAN & NICOBAR ISLANDS':'Andaman & Nicobar Islands','DAMAN & DIU':'Daman & Diu','DADRA & NAGAR HAVELI':'Dadra & Nagar Haveli'}
def tt(s): return TITLE.get(s, s.title())
MANUAL_STATE={'Kolkata U.A.':'West Bengal','Port Blair':'Andaman & Nicobar Islands','Greater Noida*':'Uttar Pradesh','Kharghar':'Maharashtra','Benipur':'Bihar','Bihat':'Bihar','Wadgaon Kolhati':'Maharashtra','Bid (Rural)':'Maharashtra','Dabhel':'Daman & Diu','Arwal':'Bihar','Naya Gaon':'Punjab'}
TEL={'adilabad','nizamabad','karimnagar','medak','hyderabad','rangareddy','mahbubnagar','nalgonda','warangal','khammam'}
LAD={'leh','lehladakh','kargil'}
def current_state(st,district):
    dk=re.sub(r'[^a-z]','',re.sub(r'\(.*?\)','',district).lower())
    if st=='Andhra Pradesh':
        first=re.sub(r'[^a-z]','',re.split(r'[,&]| and ',district.lower())[0])
        if first in TEL: return 'Telangana'
    if st=='Jammu & Kashmir' and (dk in LAD or dk.startswith('leh')): return 'Ladakh'
    if st in ('Daman & Diu','Dadra & Nagar Haveli'): return 'Dadra and Nagar Haveli and Daman and Diu'
    return st
def p(x):
    try: return int(float(x['pop2011']))
    except: return None
def utype(st,is_ua,top):
    s=st.replace(' ','').replace('.','').upper()
    if top and is_ua: return 'UA'
    m={'MCORP':'municipal corporation','MCORPN':'municipal corporation','CMC':'city municipal council','MCL':'municipal council','MC':'municipal council','M':'municipality','MB':'municipal board','TMC':'town municipal council','NPP':'nagar palika parishad','NP':'nagar panchayat','TP':'town panchayat','CB':'cantonment board','CT':'census town','INA':'industrial notified area','NAC':'notified area council','NT':'notified town','ITS':'industrial township','MCI':'municipal council','NA':'notified area','OG':'outgrowth'}
    return m.get(s, st if st else ('UA' if is_ua else 'UNKNOWN'))
def slug(s): return re.sub(r'-+','-',re.sub(r'[^a-z0-9]+','-',s.lower())).strip('-')
rows=[]; seen={}
tops={x['raw']:x for x in u if x['sl']}
haskids=set(x['parent'] for x in u if not x['sl'])
for x in u:
    if not x.get('keep'): continue
    top=bool(x['sl'])
    st=x['state'] or MANUAL_STATE.get(x['raw'].strip())
    if not st and not top: st=tops[x['parent']]['state'] or MANUAL_STATE.get(x['parent'].strip())
    name=x['name']
    name=re.sub(r'\s+(X|Xy|xy|x)$','',name); name=name.replace('Imphal (MCI) OG','Imphal')
    name=re.sub(r'\[\s*\d+\s*\]','',name); name=re.sub(r"[@#\$!'¥£]+.*$",'',name) if re.search(r"[@#\$!'¥£]",name) else name
    name=re.sub(r'\s*\d+[A-Z]?(\s*,\s*\d+[A-Z]?)*\s*$','',name); name=re.sub(r'(?<=[a-z\.])\d+$','',name).strip()
    name=re.sub(r'-\s+','-',name); name=re.sub(r'[\^†]','',name); name=re.sub(r'\s*\(\s*$','',name.strip()); name=re.sub(r'\(\s*(?=Cantonment)','',name); name=re.sub(r'\s+(NPP|NP|N\.P\.|CT|C\.T\.|M\.Cl\.|M Cl|TP)$','',name).strip()
    disp=re.sub(r'\s*U\.?\s?A\.?$','',name).strip()
    stt=x['status2011'].replace(' ','').replace('.','').upper()
    if stt=='CB' and 'cant' not in disp.lower() and '(CB)' not in disp and 'CB' not in disp: disp=disp+' Cantonment'
    disp=re.sub(r'\s*\((CB|C\.B\.)\)',' Cantonment',disp)
    disp=re.sub(r'\s*\((M\.? ?Corp\.?|CT|M|NP|NPP|M Cl|INA|CMC|TMC)\)\s*$','',disp,flags=re.I).strip()
    is_ua=(x.get('is_ua',False) or x['raw'] in haskids) if top else False
    district=x['district']
    cs=current_state(st,district) if st else None
    parent=None
    if not top:
        pt=tops[x['parent']]; parent=re.sub(r'\s+',' ',pt['name']).strip()
        if not re.search(r'U\.?\s?A',parent): parent+=' (UA)'
    rid=slug(disp+'-'+(cs or 'x')) + ('-ua' if is_ua else '')
    if rid in seen: seen[rid]+=1; rid=rid+'-'+str(seen[rid])
    else: seen[rid]=1
    rows.append({'city_id':rid,'city':disp,'unit_name_census':re.sub(r'\s+',' ',x['raw'].replace('\n',' ')).strip(),'state_census2011':st,'state':cs,'district':district,
        'unit_type':('municipal corporation + outgrowths' if '+OG' in x['raw'].replace(' ','') and not x['status2011'] else utype(x['status2011'],is_ua,top)),'census_status_code':x['status2011'] or ('UA' if is_ua else ''),
        'parent_ua':parent or '','pop_2011':p(x),'size_class':'Class I' if x['cls']=='I' else 'Class II','count_unit':1 if top else 0,'is_ua':is_ua})
json.dump(rows,open(D+'/'+(sys.argv[2] if len(sys.argv)>2 else 'cities_stage1.json'),'w'),indent=0)
print(len(rows), sum(r['count_unit'] for r in rows))
print('no state',[r['city'] for r in rows if not r['state']])
import collections; print(collections.Counter(r['unit_type'] for r in rows).most_common())
