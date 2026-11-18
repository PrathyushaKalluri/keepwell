import sys, zipfile, re, csv, xml.etree.ElementTree as ET
ns={'m':'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
def col2n(c):
    n=0
    for ch in c: n=n*26+ord(ch)-64
    return n-1
z=zipfile.ZipFile(sys.argv[1])
ss=[]
if 'xl/sharedStrings.xml' in z.namelist():
    r=ET.fromstring(z.read('xl/sharedStrings.xml'))
    for si in r.findall('m:si',ns):
        ss.append(''.join(t.text or '' for t in si.iter('{%s}t'%ns['m'])))
sh=ET.fromstring(z.read('xl/worksheets/sheet1.xml'))
w=csv.writer(open(sys.argv[2],'w',newline=''))
for row in sh.iter('{%s}row'%ns['m']):
    vals={}
    for c in row.findall('m:c',ns):
        ref=re.match(r'([A-Z]+)',c.get('r')).group(1)
        v=c.find('m:v',ns); t=c.get('t')
        if t=='inlineStr':
            val=''.join(x.text or '' for x in c.iter('{%s}t'%ns['m']))
        elif v is None: val=''
        elif t=='s': val=ss[int(v.text)]
        else: val=v.text
        vals[col2n(ref)]=val
    if vals:
        m=max(vals); w.writerow([vals.get(i,'') for i in range(m+1)])
