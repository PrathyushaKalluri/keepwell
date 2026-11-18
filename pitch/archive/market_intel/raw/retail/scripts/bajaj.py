import urllib.request, json, re, html, time, csv, sys
UA={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/124 Safari/537.36"}
B="https://www.bajajelectronics.com"
def get(u):
    return urllib.request.urlopen(urllib.request.Request(u,headers=UA),timeout=40).read().decode('utf-8','ignore')
states={77:"Andhra Pradesh",78:"Delhi",88:"Haryana",76:"Telangana",85:"Uttar Pradesh"}
rows=[]
for sid,sn in states.items():
    cities={c['id']:c['name'].title() for c in json.loads(get(f"{B}/country/getcitiesbystateid?stateId={sid}&addSelectStateItem=true")) if c['id']}
    time.sleep(1.5)
    h=get(f"{B}/getstoredetails?stateId={sid}&cityId=0"); time.sleep(1.5)
    for m in re.finditer(r'data-cityId="(\d+)" data-storeId="(\d+)">\s*<div class="add_box">\s*<h3>(.*?)</h3>\s*<p class="storelocator_address">(.*?)</p>.*?href="([^"]+)"',h,re.S):
        cid,stid,name,addr,link=m.groups()
        addr=html.unescape(re.sub(r'\s+',' ',addr)).strip(); name=html.unescape(name).strip()
        pin=re.findall(r'(\d{6})\s*$',addr) or re.findall(r'\b(\d{6})\b',addr)
        dist=re.findall(r'([A-Za-z\. ]+?)\s+Dist',addr)
        rows.append(dict(retailer="Bajaj Electronics (Electronics Mart India Ltd)",store_name=name,address=addr,city=cities.get(int(cid),"UNKNOWN"),district=(dist[-1].strip()+" (as written in address)") if dist else "UNKNOWN",state=sn,pincode=pin[-1] if pin else "UNKNOWN",lat="",lon="",source_url=f"{B}/getstoredetails?stateId={sid}&cityId=0 (via {B}/stores)",retrieved="2026-11-18"))
    print(sn,len(cities),sum(1 for r in rows if r['state']==sn),file=sys.stderr)
json.dump(rows,open(sys.argv[1],'w'),indent=0)
