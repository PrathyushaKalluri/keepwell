import json,re,sys,time,urllib.request,urllib.parse
D=sys.argv[1]
rows=json.load(open(D+'/cities_stage2.json'))
titles=set()
for r in rows:
    if r['lat']=='':
        c=re.sub(r'\s+Cantonment$','',r['city']).split('(')[0].strip()
        st=r['state']; st2=st.replace(' & ',' and ')
        for n in {c, c.replace('-',' ')}:
            titles.add(n); titles.add(n+', '+st2); titles.add(n+', '+st)
            d=re.split(r'[,&(]',r['district'])[0].strip()
            if d: titles.add(n+', '+d)
titles=sorted(t for t in titles if t)
print(len(titles))
res={}
for i in range(0,len(titles),50):
    ch=titles[i:i+50]
    url='https://en.wikipedia.org/w/api.php?'+urllib.parse.urlencode({'action':'query','prop':'coordinates|pageprops','ppprop':'disambiguation','redirects':1,'titles':'|'.join(ch),'format':'json','colimit':'max'})
    req=urllib.request.Request(url,headers={'User-Agent':'market-research-script/1.0'})
    d=None
    for a in range(5):
        try: d=json.load(urllib.request.urlopen(req,timeout=60)); break
        except Exception as e: print('err',e); time.sleep(15*(a+1))
    if d is None: print('FAILED chunk',i); continue
    q=d.get('query',{})
    norm={x['from']:x['to'] for x in q.get('normalized',[])}
    red={x['from']:x['to'] for x in q.get('redirects',[])}
    pages={p['title']:p for p in q.get('pages',{}).values()}
    for t in ch:
        t2=norm.get(t,t); t3=red.get(t2,t2); p=pages.get(t3)
        if p and 'coordinates' in p and 'disambiguation' not in p.get('pageprops',{}):
            c=p['coordinates'][0]; res[t]={'page':t3,'lat':c['lat'],'lon':c['lon']}
    time.sleep(2)
json.dump(res,open(D+'/wp_titles.json','w'))
print('found',len(res))
