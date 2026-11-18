import re, html, json, csv, sys, time, urllib.request, os
D=sys.argv[1]; OUT=sys.argv[2]; R="2026-11-18"
UA={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/124 Safari/537.36"}
def rd(f): return open(os.path.join(D,f),errors='ignore').read()
def clean(x): return re.sub(r'\s+',' ',html.unescape(re.sub(r'<br\s*/?>',', ',x))).strip(' ,')
def pin(a):
    p=re.findall(r'\b([1-8]\d{2}\s?\d{3})\b',a); return p[-1].replace(' ','') if p else "UNKNOWN"
rows=[]
def add(**k):
    base=dict(retailer="",store_name="",address="",city="UNKNOWN",district="UNKNOWN",state="UNKNOWN",pincode="UNKNOWN",lat="",lon="",source_url="",retrieved=R); base.update(k); rows.append(base)
# Bajaj
for r in json.load(open(os.path.join(D,'..','bajaj_rows.json'))): rows.append(r)
# Vasanth & Co
s=rd('sl_vasanthandco_in_branches.html')
for ch in s.split('<div class="store-content ">')[1:]:
    ch=ch.split('<div class="store-wrap')[0]
    nm=re.search(r'<a href="(Store/[^"]+)"[^>]*>(.*?)</a>',ch,re.S); ad=re.search(r'<div class="store-address"[^>]*>(.*?)</div>',ch,re.S)
    if not nm or not ad: continue
    name=clean(nm.group(2)); addr=clean(ad.group(1))
    ll=re.search(r'!2d([\d.]+)!3d([\d.]+)',ch)
    st="UNKNOWN"
    for cand,norm in [("tamilnadu","Tamil Nadu"),("tamil nadu","Tamil Nadu"),("tamil nau","Tamil Nadu"),("karnataka","Karnataka"),("kerala","Kerala"),("puducherry","Puducherry"),("pondicherry","Puducherry")]:
        if cand in addr.lower(): st=norm; break
    if re.search(r'(?i)pondicherry|puducherry',addr) and re.search(r'\b605\d{3}\b',addr): st="Puducherry"
    c=re.search(r'([A-Za-z\. ]+?)\s*,?\s*-\s*\d{3}\s?\d{3}',addr)
    city=c.group(1).strip() if c else "UNKNOWN"
    city=city.split()[-1].title() if city!="UNKNOWN" and city.split() else "UNKNOWN"
    add(retailer="Vasanth & Co",store_name=name,address=addr,city=city,state=st,pincode=pin(addr),lat=ll.group(2) if ll else "",lon=ll.group(1) if ll else "",source_url="https://vasanthandco.in/branches")
# Nandilath G-Mart
s=rd('sl_nandilathgmart_com_our-stores_.html')
for ch in s.split('<h4 class="storeareaHeading">')[1:]:
    dist=clean(ch[:ch.index('</h4>')])
    body=ch.split('class="mapouter"')[0]
    q=re.search(r'maps\?q=([^&"]+)',ch)
    parts=[clean(x) for x in re.findall(r'<div class="storeareaDesc">(.*?)</div>',body,re.S)]
    parts=[p for p in parts if p and not p.lower().startswith('phone')]
    addr=", ".join(parts)
    loc=urllib.request.unquote(q.group(1)).lower().replace('nandilath','').replace('g mart','').replace('g-mart','').strip().title() if q else "UNKNOWN"
    add(retailer="Nandilath G-Mart",store_name="Nandilath G-Mart ("+(loc if loc!="UNKNOWN" else (parts[0] if parts else dist))+")",address=addr,city="UNKNOWN",district=dist,state="Kerala",pincode=pin(addr),source_url="https://nandilathgmart.com/our-stores/")
# Lotus
for c in ["indore","bhopal","ujjain","jabalpur","nagpur","raipur","bhilai","bilaspur","jaipur"]:
    s=rd(f'lotus/{c}.html')
    for m in re.finditer(r'<script type="application/ld\+json"[^>]*>(.*?)</script>',s,re.S):
        try: d=json.loads(m.group(1))
        except: continue
        for x in d.get('@graph',[d]):
            if isinstance(x,dict) and x.get('@type')=='Store':
                a=x.get('address',{})
                add(retailer="Lotus Electronics",store_name=x.get('name',''),address=a.get('streetAddress',''),city=a.get('addressLocality','UNKNOWN'),state=a.get('addressRegion','UNKNOWN'),pincode=a.get('postalCode') or pin(a.get('streetAddress','')),source_url=f"https://www.lotuselectronics.com/contact-us/{c}")
# Great Eastern + Kohinoor (find-store JSON)
for files,ret,url in [(['ge_all.json','ge_all2.json','ge_all3.json','ge_all4.json'],"Great Eastern Retail","https://www.greateasternretail.com/find-store (POST by pincode, via /store-locator)"),(['kohi_all.json'],"Kohinoor Electronics","https://www.kohinoorelectronics.com/find-store (POST by pincode, via /store-locator)")]:
    seen={}
    for f in files:
        for x in json.load(open(os.path.join(D,'..',f))): seen[x['fcId']]=x
    for x in seen.values():
        a=clean(x.get('streetName') or '')
        st=(x.get('country') or "UNKNOWN").strip().title()
        add(retailer=ret,store_name=clean(x.get('fcName','')),address=a,city=clean(x.get('city') or x.get('town') or 'UNKNOWN').strip(',').title(),state=st,pincode=x.get('postCode') or pin(a),lat=x.get('latitude',''),lon=x.get('longitude',''),source_url=url)
# Oxygen: fetch detail pages
s=rd('sl_www_oxygendigitalshop_com_pages_store-locator.html')
cards=re.findall(r'href="(https://www.oxygendigitalshop.com/pages/store-locator-[^"]+)"\s*class="oxygen-store-card"\s*data-district="([^"]+)"',s)
for u,dist in cards:
    nm=re.search(re.escape(u)+r'.*?<h3>(.*?)</h3>',s,re.S); nm=clean(nm.group(1)) if nm else u.split('locator-')[-1]
    try:
        p=urllib.request.urlopen(urllib.request.Request(u,headers=UA),timeout=40).read().decode('utf-8','ignore'); time.sleep(1.2)
        t=clean(re.sub(r'<[^>]+>',' ',re.sub(r'(?s)<(script|style).*?</\1>','',p)))
        m=re.search(r'is located at (.*?) in ([A-Za-z ]+?) District',t)
        addr=m.group(1) if m else "UNKNOWN"
    except Exception as e: addr="UNKNOWN"
    add(retailer="Oxygen The Digital Expert (Oxygen Digital Shop)",store_name=nm,address=addr,city=re.sub(r'(?i)\\s*(old\\s+)?oxygen digital (shop|expert).*$','',nm).strip(),district=dist.title(),state="Kerala",pincode=pin(addr),source_url=u)
# Pittappillil
s=rd('pitt_sl.html')
seen=set()
for m in re.finditer(r'\\u0022title\\u0022:\\u0022(.*?)\\u0022,\\u0022lat\\u0022:\\u0022([-\d.]*)\\u0022,\\u0022lng\\u0022:\\u0022([-\d.]*)\\u0022,\\u0022description\\u0022:\\u0022(.*?)\\u003Cbr',s):
    t,la,lo,d=m.groups()
    rest=s[m.end():m.end()+600]
    a=re.match(r'\\\\\\/\\u003E(.*?)\\u003Cbr',rest)
    addr=a.group(1) if a else "UNKNOWN"
    addr=addr.encode().decode('unicode_escape',errors='ignore').replace('\\/','/')
    if t in seen: continue
    seen.add(t)
    parts=[x.strip() for x in addr.split(',')]
    dist=next((x.title() for x in parts if x.upper() in ["ALAPPUZHA","ERNAKULAM","IDUKKI","KANNUR","KASARAGOD","KOLLAM","KOTTAYAM","KOZHIKODE","MALAPPURAM","PALAKKAD","PATHANAMTHITTA","THIRUVANANTHAPURAM","THRISSUR","WAYANAD"]),"UNKNOWN")
    city=t.replace('PITTAPPILLIL AGENCIES','').replace('DIGIPARK','').replace('DIGI PARK','').strip().title() or "UNKNOWN"
    add(retailer="Pittappillil Agencies",store_name=t.title(),address=addr,city=city,district=dist,state="Kerala",pincode=pin(addr),lat=la,lon=lo,source_url="https://www.pittappillilonline.com/store-locator")
# Girias
def st_from_pin(pc):
    if not re.match(r'^\d{6}$',pc): return "UNKNOWN"
    if pc[:3] in ('605','607','609') and pc in ('605001','605002','605003','605004','605005','605006','605007','605008','605009','605010','605011','605013','605014','609602','609603','609604','609605','609606','609607','609609'): return "Puducherry (from pincode)"
    if pc[:2] in ('56','57','58','59'): return "Karnataka (from pincode)"
    if pc[:2] in ('60','61','62','63','64'): return "Tamil Nadu (from pincode)"
    if pc[:2] in ('50',): return "Telangana (from pincode)"
    if pc[:2] in ('51','52','53'): return "Andhra Pradesh (from pincode)"
    return "UNKNOWN"
seen=set()
for pg in range(1,8):
    s=rd(f'girias/p{pg}.html')
    for m in re.finditer(r'<address[^>]*>(.*?)</address>',s,re.S):
        pre=s[max(0,m.start()-3000):m.start()]; h=re.findall(r'<h4[^>]*>(.*?)</h4>',pre,re.S)
        nm=clean(re.sub(r'<[^>]+>','',h[-1])) if h else "UNKNOWN"; addr=clean(re.sub(r'<[^>]+>','',m.group(1)))
        if (nm,addr) in seen: continue
        seen.add((nm,addr)); pc=pin(addr)
        add(retailer="Girias",store_name=nm.title(),address=addr,city=nm.title(),state=st_from_pin(pc),pincode=pc,source_url=f"https://www.giriasindia.com/stores?page={pg}")
for r in rows:
    if r['retailer'].startswith('Oxygen'):
        r['city']=re.sub(r'(?i)\s*oxygen digital (shop|expert)\s*$','',r['store_name']).replace('Old ','').strip()
for r in rows:
    for k in ('address','store_name'):
        v=re.sub(r'<[^>]+>',' ',r[k])
        v=re.sub(r'(\+91[- ]?)?\b[6-9]\d{9}\b','',v)
        v=re.sub(r'\b0\d{2,4}[- ]\d{6,8}\b','',v)
        v=re.sub(r'\s+,',',',re.sub(r'\s+',' ',v)).strip(' ,')
        r[k]=v
    if r['retailer']=='Nandilath G-Mart' and len(r['store_name'])>45:
        r['store_name']='Nandilath G-Mart ('+r['district']+')'
cols=["retailer","store_name","address","city","district","state","pincode","lat","lon","source_url","retrieved"]
with open(OUT,'w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=cols,extrasaction='ignore'); w.writeheader(); [w.writerow(r) for r in rows]
from collections import Counter; print(Counter(r['retailer'] for r in rows), len(rows))
