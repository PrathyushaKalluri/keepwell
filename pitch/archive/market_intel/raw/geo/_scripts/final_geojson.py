import json,sys,csv
src,out,sb=sys.argv[1],sys.argv[2],sys.argv[3]
d=json.load(open(src))
M={'Andaman & Nicobar':'Andaman and Nicobar Islands','Jammu & Kashmir':'Jammu and Kashmir'}
names={r['name_std'] for r in csv.DictReader(open(sb))}
for f in d['features']:
    n=f['properties']['ST_NM']; f['properties']={'ST_NM':n,'name_std':M.get(n,n)}
got={f['properties']['name_std'] for f in d['features']}
print('unmatched geo',got-names,'unmatched baseline',names-got)
json.dump(d,open(out,'w'),separators=(',',':'))
