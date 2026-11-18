import csv, re, sys, json
def parse(path, cls):
    rows=list(csv.reader(open(path)))
    units=[]; cur=None; top=None
    for r in rows:
        r=r+['']*(11-len(r))
        sl,name,dist,yr,st,area,pop=[x.strip() for x in r[:7]]
        m_=re.search(r'(19|20)\d\d',yr); isyear=m_ is not None; yr=m_.group(0) if m_ else yr
        if sl.startswith('('): name=sl+' '+name; sl=''
        istop=bool(re.fullmatch(r'\d+',sl))
        if name and isyear and not name.upper().startswith(('ALL TOWNS','URBAN AGGLOM')):
            if not istop and not re.match(r'^\(?\s*[A-Za-z]{1,7}\s*\)',name) and cur:
                cur['raw']+=' '+name
            else:
                cur={'sl':sl if istop else '','raw':name,'distlines':[],'cls':cls,'pop2011':None,'status2011':'','area':'','parent':None,'rowtext':[]}
                if istop: top=cur
                else: cur['parent']=top['raw'] if top else 'UNKNOWN'
                units.append(cur)
        if cur and isyear:
            if dist: cur['distlines'].append(dist)
            if yr=='2011':
                cur['pop2011']=pop; cur['status2011']=st; cur['area']=area
    t=None
    for u in units:
        if u['sl']: t=u
        else: u['parent']=t['raw'] if t else 'UNKNOWN'
    return units
out=[]
for p,c in [(sys.argv[1],'I'),(sys.argv[2],'II')]:
    out+=parse(p,c)
json.dump(out,open(sys.argv[3],'w'),indent=0)
print(len(out))
