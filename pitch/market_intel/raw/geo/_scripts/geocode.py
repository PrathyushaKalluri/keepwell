import json,re,sys,time,urllib.request,urllib.parse,os
D=sys.argv[1]; GJ=sys.argv[2]
rows=json.load(open(D+'/cities_stage1b.json'))
wiki=json.load(open(D+'/wiki_cities.json'))
gj=json.load(open(GJ))
def nk(s): return re.sub(r'[^a-z]','',s.lower())
STMAP={'Andaman & Nicobar':'Andaman & Nicobar Islands','Delhi':'Delhi','Dadra and Nagar Haveli and Daman and Diu':'Dadra and Nagar Haveli and Daman and Diu'}
polys={}
for f in gj['features']:
    n=f['properties']['ST_NM']; n=STMAP.get(n,n); g=f['geometry']
    polys[nk(n.replace(' and ',' & '))]=g['coordinates'] if g['type']=='MultiPolygon' else [g['coordinates']]
def pip(x,y,ring):
    c=False; n=len(ring); j=n-1
    for i in range(n):
        xi,yi=ring[i]; xj,yj=ring[j]
        if ((yi>y)!=(yj>y)) and (x<(xj-xi)*(y-yi)/(yj-yi+1e-12)+xi): c=not c
        j=i
    return c
def in_state(lat,lon,st):
    k=nk(st.replace(' and ',' & '))
    P=polys.get(k)
    if P is None: return None
    for poly in P:
        if pip(lon,lat,poly[0]) and not any(pip(lon,lat,h) for h in poly[1:]): return True
    # tolerance 0.05 deg to nearest vertex
    for poly in P:
        for (x,y) in poly[0]:
            if abs(x-lon)<0.05 and abs(y-lat)<0.05: return True
    return False
ALIAS={'bengaluru':['bbmp','bruhatbangalore','bangalore'],'prayagraj':['allahabad'],'chhatrapatisambhajinagar':['aurangabad'],'gurugram':['gurgaon'],'hublidharwad':['hublidharwad'],'delhi':['delhimunicipalcorporationurban','delhi'],'mumbai':['greatermumbai'],'hyderabad':['hyderabad','greaterhyderabad'],'dharashiv':['osmanabad'],'ahilyanagar':['ahmednagar'],'mysuru':['mysore'],'belagavi':['belgaum'],'kalaburagi':['gulbarga'],'vijayapura':['bijapur'],'ballari':['bellary'],'shivamogga':['shimoga'],'tumakuru':['tumkur'],'mangaluru':['mangalore'],'puducherry':['puducherry','pondicherry'],'thiruvananthapuram':['thiruvananthapuram'],'ayodhya':['faizabad'],'kolkata':['kolkata']}
W={}
for w in wiki:
    st=w['state'].replace('Jammu and Kashmir','Jammu & Kashmir').replace(' and ',' & ') if 'Daman' not in w['state'] else w['state']
    keys={nk(w['label']),nk(w['article'].split(',')[0])}
    for a in list(keys): keys|=set(ALIAS.get(a,[]))
    for k in keys: W.setdefault((k,nk(st)),w)
WD={}
for b in json.load(open(D+'/wd.json'))['results']['bindings']:
    m=re.match(r'Point\(([-\d.]+) ([-\d.]+)\)',b['coord']['value'])
    if not m: continue
    if re.search(r'district|division|tehsil|taluk|mandal|block|constituency',b['itemLabel']['value'],re.I): continue
    rec=(b['item']['value'].split('/')[-1],b['itemLabel']['value'],float(m.group(2)),float(m.group(1)),float(b['pop']['value']))
    for nm_ in {b['itemLabel']['value'], b.get('alt',{}).get('value','')}:
        if nm_: WD.setdefault(nk(nm_),set()).add(rec)
def wd_lookup(names,st,pop):
    best=None
    for n in names:
        for rec in WD.get(nk(n),()):
            if in_state(rec[2],rec[3],st):
                d=abs(rec[4]-pop)/max(pop,1)
                if best is None or d<best[0]: best=(d,rec)
    return best[1] if best else None
WDN={}
if os.path.exists(D+'/wd_names.json'):
    for b in json.load(open(D+'/wd_names.json')):
        m=re.match(r'Point\(([-\d.]+) ([-\d.]+)\)',b['coord'])
        if m: WDN.setdefault(nk(b['lab']),[]).append((b['item'],b['lab'],float(m.group(2)),float(m.group(1)),float(b['pop']) if b['pop'] else None,b['types'].lower()))
WPT=json.load(open(D+'/wp_titles.json')) if os.path.exists(D+'/wp_titles.json') else {}
URB=('city','town','municipal','cantonment','urban','nagar','metropolis','municipality','notified area')
def wdn_lookup(names,st,pop):
    best=None
    for n in names:
        for rec in WDN.get(nk(n),()):
            if not in_state(rec[2],rec[3],st): continue
            urb=any(t in rec[5] for t in URB)
            d=abs(rec[4]-pop)/max(pop,1) if rec[4] else 5
            if not urb and (rec[4] is None or d>0.5): continue
            score=(0 if urb else 1, d)
            if best is None or score<best[0]: best=(score,rec)
    return best[1] if best else None
cache_f=D+'/nominatim_cache_settlement.json'
cache=json.load(open(cache_f)) if os.path.exists(cache_f) else {}
def nom(q):
    if q in cache: return cache[q]
    url='https://nominatim.openstreetmap.org/search?'+urllib.parse.urlencode({'q':q,'format':'jsonv2','limit':3,'countrycodes':'in','featureType':'settlement'})
    req=urllib.request.Request(url,headers={'User-Agent':'market-research-script/1.0'})
    try:
        r=json.load(urllib.request.urlopen(req,timeout=30))
    except Exception as e:
        r={'error':str(e)}
    cache[q]=r; time.sleep(1.0)
    if len(cache)%10==0: json.dump(cache,open(cache_f,'w'))
    return r
done={}
for i,r in enumerate(rows):
    st=r['state']; base=re.sub(r'\s+Cantonment$','',r['city'])
    nm=base.split('(')[0].strip()
    key=(nk(nm),nk(st.replace(' and ',' & ')))
    lat=lon=None; src=''
    if (nk(r['city']),key[1]) in W and 'Cantonment' not in r['city']:
        w=W[(nk(r['city']),key[1])]; lat,lon=w['lat'],w['lon']; src='Wikipedia: List of cities in India by population ('+w['article']+')'
    elif key in W and 'Cantonment' not in r['city']:
        w=W[key]; lat,lon=w['lat'],w['lon']; src='Wikipedia: List of cities in India by population ('+w['article']+')'
    if lat is None:
        cand=[r['city'],nm,re.sub(r'-',' ',nm)]
        if r['is_ua'] or r['unit_type']!='UA': pass
        rec=wd_lookup(cand,st,r['pop_2011'] or 0) if 'Cantonment' not in r['city'] else None
        if rec: lat,lon=round(rec[2],5),round(rec[3],5); src='Wikidata '+rec[0]+' ('+rec[1]+'), P625 coordinate'
    if lat is None and 'Cantonment' not in r['city']:
        c0=re.sub(r'\s+Cantonment$','',r['city']).split('(')[0].strip(); d0=re.split(r'[,&(]',r['district'])[0].strip()
        for n in [c0, c0.replace('-',' ')]:
            for t in [n+', '+st.replace(' & ',' and '), n+', '+st, n+', '+d0, n]:
                w=WPT.get(t)
                if w and in_state(w['lat'],w['lon'],st):
                    lat,lon=round(w['lat'],5),round(w['lon'],5); src='Wikipedia article "'+w['page']+'" (coordinates via MediaWiki API)'; break
            if lat is not None: break
    if lat is None and 'Cantonment' not in r['city']:
        rec=wdn_lookup([r['city'],nm,nm.replace('-',' '),nm.replace(' ','')],st,r['pop_2011'] or 0)
        if rec: lat,lon=round(rec[2],5),round(rec[3],5); src='Wikidata '+rec[0]+' ('+rec[1]+'; '+rec[5][:40]+'), P625 coordinate'
    if lat is None and not os.environ.get("NONOM"):
        dist=re.split(r'[,&(]',r['district'])[0].strip()
        qs=[f"{r['city']}, {dist}, {st}, India", f"{nm}, {st}, India"]
        if r['city']==nm: qs=[f"{nm}, {dist}, {st}, India", f"{nm}, {st}, India"]
        for q in qs:
            res=nom(q)
            if isinstance(res,list):
                for c in res:
                    la,lo=float(c['lat']),float(c['lon'])
                    ok=in_state(la,lo,st)
                    if ok:
                        lat,lon=round(la,5),round(lo,5); src='OSM Nominatim q="'+q+'" ('+c.get('display_name','')[:80].replace('"','')+')'; break
            if lat is not None: break
    if lat is not None and src.startswith('Wikipedia') and in_state(lat,lon,st) is False:
        src+=' [WARN outside state polygon]'
    r['lat']=lat if lat is not None else ''; r['lon']=lon if lon is not None else ''; r['coord_source']=src
    if i%25==0: print(i, r['city'], src[:60], flush=True)
json.dump(cache,open(cache_f,'w'))
json.dump(rows,open(D+'/cities_stage2.json','w'),indent=0)
print('missing',sum(1 for r in rows if r['lat']==''), 'wiki',sum(1 for r in rows if r['coord_source'].startswith('Wiki')))
