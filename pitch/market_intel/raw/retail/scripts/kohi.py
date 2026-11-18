import urllib.request, urllib.parse, http.cookiejar, re, json, time, sys
dom, out = sys.argv[1], sys.argv[2]; pins = sys.argv[3].split(',')
cj=http.cookiejar.CookieJar(); op=urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/124 Safari/537.36"
p=op.open(urllib.request.Request(f"https://{dom}/store-locator",headers={"User-Agent":UA}),timeout=40).read().decode('utf-8','ignore')
tok=re.search(r'csrfmiddlewaretoken" value="([^"]+)',p).group(1)
stores={}
for pin in pins:
    data=urllib.parse.urlencode({"csrfmiddlewaretoken":tok,"store_pincode":pin}).encode()
    r=urllib.request.Request(f"https://{dom}/find-store",data=data,headers={"User-Agent":UA,"X-CSRFToken":tok,"Referer":f"https://{dom}/store-locator","X-Requested-With":"XMLHttpRequest"})
    try: d=json.loads(op.open(r,timeout=40).read())
    except Exception as e: print(pin,'ERR',e,file=sys.stderr); time.sleep(2); continue
    new=0
    for x in d.get('data',[]):
        if x['fcId'] not in stores: stores[x['fcId']]=x; new+=1
    print(pin,len(d.get('data',[])),'new',new,'total',len(stores),file=sys.stderr)
    time.sleep(2)
json.dump(list(stores.values()),open(out,'w'),indent=0)
