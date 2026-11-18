import csv,json,re,sys
D,OUT=sys.argv[1],sys.argv[2]
A1URL='https://censusindia.gov.in/nada/index.php/catalog/42526'
NCPURL='https://nhm.gov.in/New_Updates_2018/Report_Population_Projection_2019.pdf'
ncp=json.load(open(D+'/ncp/ncp_urban_march.json'))
st={}; dist=[]
for r in csv.reader(open(D+'/xls/a1.csv')):
    if len(r)<12: continue
    if r[3]=='STATE' and r[5]=='Urban': st[r[0]]={'name':re.sub(r'[@&$\s]+$','',r[4]).strip(),'hh':int(r[9]),'pop':int(r[10])}
    if r[3]=='DISTRICT' and r[5]=='Urban': dist.append((r[0],r[1],r[4],int(r[9]),int(r[10])))
TEL=set(str(c) for c in range(532,542)); LAD={'003','004'}
NAME={'01':'Jammu and Kashmir','02':'Himachal Pradesh','03':'Punjab','04':'Chandigarh','05':'Uttarakhand','06':'Haryana','07':'Delhi','08':'Rajasthan','09':'Uttar Pradesh','10':'Bihar','11':'Sikkim','12':'Arunachal Pradesh','13':'Nagaland','14':'Manipur','15':'Mizoram','16':'Tripura','17':'Meghalaya','18':'Assam','19':'West Bengal','20':'Jharkhand','21':'Odisha','22':'Chhattisgarh','23':'Madhya Pradesh','24':'Gujarat','27':'Maharashtra','28':'Andhra Pradesh','29':'Karnataka','30':'Goa','31':'Lakshadweep','32':'Kerala','33':'Tamil Nadu','34':'Puducherry','35':'Andaman and Nicobar Islands'}
NCPK={'Jammu and Kashmir':['JAMMU & KASHMIR (UT)'],'Delhi':['NCT OF DELHI'],'Andaman and Nicobar Islands':['ANDAMAN & NICOBAR ISLANDS'],'Dadra and Nagar Haveli and Daman and Diu':['DADRA & NAGAR HAVELI','DAMAN & DIU'],'Ladakh':['LADAKH'],'Telangana':['TELANGANA']}
out=[]
def add(name,code,pop,hh,note):
    keys=NCPK.get(name,[name.upper()])
    v={y:sum(ncp[k][str(y)] if str(y) in ncp[k] else ncp[k][y] for k in keys) for y in (2011,2021,2026,2031)} if all(k in ncp for k in keys) else None
    row={'name_std':name,'census2011_state_code':code,'census2011_urban_pop':pop,'census2011_urban_households':hh,
         'census2011_avg_urban_hh_size':round(pop/hh,2),'census2011_avg_urban_hh_size_flag':'DERIVED (urban pop / urban households)',
         'census_source':'Census of India 2011, Table A-1 (Number of villages, towns, households, population and area), final','census_source_url':A1URL,'census_source_year':2011,
         'ncp_urban_2011_thousand':v[2011] if v else 'UNKNOWN','ncp_urban_2021_thousand':v[2021] if v else 'UNKNOWN',
         'proj_urban_pop_2026':v[2026]*1000 if v else 'UNKNOWN','proj_urban_pop_2026_flag':'PROJECTED (NCP Technical Group, Table 9, as on 1 March 2026; tabulated, not interpolated)' if v else 'UNKNOWN',
         'ncp_urban_2031_thousand':v[2031] if v else 'UNKNOWN',
         'urban_growth_factor_2011_2026':round(v[2026]/v[2011],4) if v else 'UNKNOWN','growth_factor_flag':'DERIVED = NCP 2026 / NCP 2011 base (same series)',
         'proj2026_over_census2011':round(v[2026]*1000/pop,4) if v else 'UNKNOWN',
         'ncp_source':'Report of the Technical Group on Population Projections 2011-2036, National Commission on Population, MoHFW (report dated Nov 2019, released Jul 2020)','ncp_source_url':NCPURL,'ncp_source_year':2020,
         'notes':note}
    out.append(row)
for code,s in st.items():
    name=NAME.get(code)
    if code=='28':
        t=[d for d in dist if d[0]=='28' and d[1] in TEL]; a=[d for d in dist if d[0]=='28' and d[1] not in TEL]
        add('Andhra Pradesh','28',sum(d[4] for d in a),sum(d[3] for d in a),'Census 2011 figures = sum of the 13 residuary AP districts (A-1 district rows). DERIVED split of undivided AP.')
        add('Telangana','28 (part)',sum(d[4] for d in t),sum(d[3] for d in t),'Census 2011 figures = sum of the 10 Telangana districts (codes 532-541) of undivided AP (A-1 district rows). DERIVED split; ignores 2014 transfer of Polavaram mandals from Khammam to AP.')
    elif code=='01':
        l=[d for d in dist if d[0]=='01' and d[1] in LAD]; j=[d for d in dist if d[0]=='01' and d[1] not in LAD]
        add('Jammu and Kashmir','01',sum(d[4] for d in j),sum(d[3] for d in j),'Census 2011 figures = J&K state minus Leh and Kargil districts (A-1 district rows). DERIVED split per J&K Reorganisation Act 2019.')
        add('Ladakh','01 (part)',sum(d[4] for d in l),sum(d[3] for d in l),'Census 2011 figures = Leh (Ladakh) + Kargil districts (A-1 district rows). DERIVED split.')
    elif code in ('25','26'): continue
    else: add(name,code,s['pop'],s['hh'],'')
dd,dn=st['25'],st['26']
add('Dadra and Nagar Haveli and Daman and Diu','25+26',dd['pop']+dn['pop'],dd['hh']+dn['hh'],'Merged UT (2020). Census 2011 and NCP figures are DERIVED sums of Daman & Diu (25) and Dadra & Nagar Haveli (26).')
out.sort(key=lambda r:r['name_std'])
tot_pop=sum(r['census2011_urban_pop'] for r in out); print('sum census urban',tot_pop,len(out))
print('sum ncp2026', sum(r['proj_urban_pop_2026'] for r in out if r['proj_urban_pop_2026']!='UNKNOWN'), 'India NCP 2026', ncp['INDIA']['2026']*1000)
with open(OUT+'/state_baseline.csv','w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(out[0].keys())); w.writeheader(); w.writerows(out)
for r in out: print(r['name_std'],r['census2011_urban_pop'],r['ncp_urban_2011_thousand'],r['census2011_avg_urban_hh_size'],r['proj_urban_pop_2026'],r['urban_growth_factor_2011_2026'])
