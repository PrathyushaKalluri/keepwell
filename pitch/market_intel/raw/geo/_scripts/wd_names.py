import json,re,sys,time,urllib.request,urllib.parse
D=sys.argv[1]
rows=json.load(open(D+'/cities_stage2.json'))
names=set()
for r in rows:
    if r['lat']=='':
        c=re.sub(r'\s+Cantonment$','',r['city']); names.add(c); names.add(c.split('(')[0].strip())
        names.add(c.replace('-',' ')); names.add(c.replace(' ',''))
names=sorted(n for n in names if n and '"' not in n)
print(len(names))
out=[]
for i in range(0,len(names),300):
    chunk=names[i:i+300]
    vals=' '.join('"%s"@en'%n for n in chunk)
    q="""SELECT ?item ?lab ?coord ?pop (GROUP_CONCAT(DISTINCT ?tl;separator='|') AS ?types) WHERE {
 VALUES ?lab { %s } ?item rdfs:label|skos:altLabel ?lab. ?item wdt:P17 wd:Q668; wdt:P625 ?coord.
 OPTIONAL{?item wdt:P1082 ?pop} OPTIONAL{?item wdt:P31 ?t. ?t rdfs:label ?tl. FILTER(LANG(?tl)='en')} } GROUP BY ?item ?lab ?coord ?pop"""%vals
    url='https://query.wikidata.org/sparql?'+urllib.parse.urlencode({'query':q})
    req=urllib.request.Request(url,headers={'User-Agent':'market-research-script/1.0 (generic research client)','Accept':'application/sparql-results+json'})
    for attempt in range(3):
        try:
            b=json.load(urllib.request.urlopen(req,timeout=120))['results']['bindings']; break
        except Exception as e:
            print('err',e); time.sleep(65); b=[]
    for x in b:
        out.append({'item':x['item']['value'].split('/')[-1],'lab':x['lab']['value'],'coord':x['coord']['value'],'pop':x.get('pop',{}).get('value'),'types':x.get('types',{}).get('value','')})
    print(i,len(b),flush=True); time.sleep(65)
json.dump(out,open(D+'/wd_names.json','w'))
print(len(out))
