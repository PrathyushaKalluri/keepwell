import re,sys,json
lines=open(sys.argv[1]).read().split('\n')
start=int(sys.argv[2]); end=int(sys.argv[3])
OVR={'ARUNACHAL':['ARUNACHAL PRADESH','NAGALAND','MANIPUR'],
     'DADRA & NAGAR':['DAMAN & DIU','DADRA & NAGAR HAVELI','GOA'],
     'ANDAMAN &':['LAKSHADWEEP','PUDUCHERRY','ANDAMAN & NICOBAR ISLANDS']}
out={}; names=None; py=None
for i in range(start-1,end-1):
    l=lines[i]
    if re.fullmatch(r'\s*(20[1-3]\d)\s*',l): py=int(l.strip()); continue
    m=re.match(r'^\s*(20[1-3]\d)\s+(.*)$',l)
    if m or (py and re.match(r'^\s*[\d,]+\s',l)):
        yr=int(m.group(1)) if m else py; rest=m.group(2) if m else l
        py=None
        if not names: continue
        nums=[int(x.replace(',','')) for x in re.findall(r'[\d,]+',rest)]
        k=len(names)
        if len(nums)!=3*k: print('WARN',i+1,names); continue
        for j,n in enumerate(names): out.setdefault(n,{})[yr]=nums[3*j]
        continue
    if 'Territories' in l or 'TABLE' in l or 'Projected' in l: names=None; continue
    if names is None and re.search(r'[A-Z]{3,}',l) and not re.search(r'\d',l) and 'Year' not in l and 'Person' not in l:
        parts=[p.strip() for p in re.split(r'\s{3,}',l.strip()) if p.strip()]
        names=OVR.get(parts[0],parts) if len(parts)==1 else parts
        if len(parts)==1 and parts[0] not in OVR: names=parts
json.dump(out,open(sys.argv[4],'w'),indent=1)
tot=0
for k,v in out.items():
    print(k,len(v),v.get(2011),v.get(2021),v.get(2026),v.get(2031))
    if k!='INDIA': tot+=v[2026]
print('sum states 2026',tot)
