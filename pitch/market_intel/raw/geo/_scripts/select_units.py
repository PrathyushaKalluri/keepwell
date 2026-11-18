import json,re,sys
u=json.load(open(sys.argv[1]))
STATES=["Jammu & Kashmir","Himachal Pradesh","Punjab","Chandigarh","Uttarakhand","Haryana","Delhi","Rajasthan","Uttar Pradesh","Bihar","Sikkim","Arunachal Pradesh","Nagaland","Manipur","Mizoram","Tripura","Meghalaya","Assam","West Bengal","Jharkhand","Odisha","Chhattisgarh","Madhya Pradesh","Gujarat","Daman & Diu","Dadra & Nagar Haveli","Maharashtra","Andhra Pradesh","Karnataka","Goa","Lakshadweep","Kerala","Tamil Nadu","Puducherry","Andaman & Nicobar Islands"]
def norm(s): return re.sub(r'[^a-z]','',s.lower().replace('and','&').replace('orissa','odisha').replace('pondicherry','puducherry').replace('uttaranchal','uttarakhand'))
SN={norm(s):s for s in STATES}
SN[norm('NCT of Delhi')]='Delhi'; SN[norm('Andaman & Nicobar')]='Andaman & Nicobar Islands'; SN[norm('Jammu and Kashmir')]='Jammu & Kashmir'; SN[norm('Daman and Diu')]='Daman & Diu'; SN[norm('Dadra and Nagar Haveli')]='Dadra & Nagar Haveli'; SN[norm('Chhatisgarh')]='Chhattisgarh'
def get_state(lines):
    txt=' '.join(lines)
    for g in re.findall(r'\(([^()]*)\)?',txt)[::-1]+[txt]:
        k=norm(g)
        if k in SN: return SN[k]
    k=norm(txt)
    best=None
    for kk,v in SN.items():
        if kk in k: best=v if best is None or len(kk)>len(norm(best)) else best
    return best
def clean(raw,top):
    s=raw.replace('\n',' ')
    s=re.sub(r'^\(?\s*[A-Za-z]{1,7}\s*\)\s*','',s)  # leading (a)
    if top: s=re.split(r'\s\(?\s*a\s*\)',s)[0]
    s=re.sub(r'\[\d+\]','',s); s=re.sub(r'Sl\.No\..*$','',s)
    s=re.sub(r'[\*\$@#!£\+~\'’%&]+(?=\s|$)',' ',s); s=re.sub(r'^[\*\$@#!£\+~\s]+','',s)
    s=re.sub(r'\s\d{1,3}\s*$','',s)
    s=re.sub(r'\s+',' ',s).strip(' *$@#!+,.')
    return s
def strip_status(s):
    s=re.sub(r'\s*\((M\.? ?Corp\.?|M\.? ?Corpn\.?|M Corp\.?\+OG|M\.?Corp\.?\s*\+\s*OG|CT|C\.T\.|CB|C\.B\.|M|NP|NPP|M Cl|MCl|OG|INA|CMC|TMC|NAC|ITS|Part|M\.Cl\.)\)\s*','',s,flags=re.I)
    s=re.sub(r'\s*U\.?\s?A\.?$','',s).strip()
    return s
def p(x):
    try: return int(float(x['pop2011']))
    except: return 0
BAD={'','..','-','OG','--','N.A.'}
rows=[]; tops={}
for i,x in enumerate(u):
    x['idx']=i
    if x['sl']:
        nm=clean(x['raw'],True); x['name']=nm; tops[x['raw']]=x
for i,x in enumerate(u):
    st=x['status2011'].strip()
    if x['sl']:
        x['state']=get_state(x['distlines']); x['district']=re.sub(r'\(.*?\)','',x['distlines'][0] if x['distlines'] else '').strip(' ,')
        isua=bool(re.search(r'U\.?\s?A\.?\b|\bUA\b',x['name']+' '+x['raw']))
        x['is_ua']=isua; x['keep']=True; continue
    x['name']=clean(x['raw'],False)
    x['state']=get_state(x['distlines']) or tops[x['parent']]['state'] if x['parent'] in tops else get_state(x['distlines'])
    x['district']=re.sub(r'\(.*?\)','',x['distlines'][0] if x['distlines'] else '').strip(' ,')
    keep = p(x)>=50000 and st not in BAD and 'portion' not in x['raw'].lower() and '(OG)' not in x['raw']
    # composite (M Corp + OG) rows whose children are 'portion' rows
    if p(x)>=50000 and st=='' and '+OG' in x['raw'].replace(' ','') :
        nxt=u[i+1] if i+1<len(u) else None
        if nxt and 'portion' in nxt['raw'].lower(): keep=True
    x['keep']=keep
json.dump(u,open(sys.argv[2],'w'))
sel=[x for x in u if x['keep']]
print(len(sel), sum(1 for x in sel if x['sl']), sum(1 for x in sel if not x['sl']))
print('no state:',[(x['raw'],x['distlines'][:3]) for x in sel if not x['state']][:20])
