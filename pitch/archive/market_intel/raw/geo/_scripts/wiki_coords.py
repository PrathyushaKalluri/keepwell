import re,json,sys
t=open(sys.argv[1]).read()
sec=t[t.index('== List of cities above 100,000 =='):t.index('== See also ==')]
out=[]; miss=[]
for chunk in re.split(r'\n\|-',sec):
    c=' '.join(chunk.split('\n'))
    links=re.findall(r'\[\[([^\]|]+)(?:\|([^\]]+))?\]\]',c)
    if len(links)<2: continue
    nums=re.findall(r'\|\|\s*([\d,]{5,})\s*\|\|',c)
    co=re.search(r'\{\{[Cc]oord\|([-\d.]+)\|([-\d.]+)',c)
    rec={'article':links[0][0],'label':links[0][1] or links[0][0],'state':links[1][1] or links[1][0],
         'pop2011_wiki':int(nums[0].replace(',','')) if nums else None,
         'lat':float(co.group(1)) if co else None,'lon':float(co.group(2)) if co else None}
    out.append(rec)
print(len(out), sum(1 for r in out if r['lat'] is None))
json.dump(out,open(sys.argv[2],'w'),indent=0)
