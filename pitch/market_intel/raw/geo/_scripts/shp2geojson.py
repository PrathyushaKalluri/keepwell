import struct, json, sys
shp, dbf, out, tol = sys.argv[1], sys.argv[2], sys.argv[3], float(sys.argv[4])
# DBF
d=open(dbf,'rb').read()
nrec,hlen,rlen=struct.unpack('<IHH',d[4:12])
fields=[]; o=32
while d[o]!=0x0D:
    name=d[o:o+11].split(b'\0')[0].decode(); typ=chr(d[o+11]); ln=d[o+16]; fields.append((name,typ,ln)); o+=32
recs=[]
for i in range(nrec):
    r=d[hlen+i*rlen:hlen+(i+1)*rlen]; p=1; rec={}
    for name,typ,ln in fields:
        rec[name]=r[p:p+ln].decode('utf-8','replace').strip(); p+=ln
    recs.append(rec)
def dp(pts,tol):
    if len(pts)<5 or tol<=0: return pts
    import math
    keep=[False]*len(pts); keep[0]=keep[-1]=True; stack=[(0,len(pts)-1)]
    while stack:
        a,b=stack.pop(); ax,ay=pts[a]; bx,by=pts[b]; dx,dy=bx-ax,by-ay; L=math.hypot(dx,dy)
        best=-1; bi=None
        for i in range(a+1,b):
            px,py=pts[i]
            dist=abs(dy*px-dx*py+bx*ay-by*ax)/L if L>0 else math.hypot(px-ax,py-ay)
            if dist>best: best=dist; bi=i
        if bi is not None and best>tol: keep[bi]=True; stack+= [(a,bi),(bi,b)]
    return [p for p,k in zip(pts,keep) if k]
def area(r): return sum(r[i][0]*r[i+1][1]-r[i+1][0]*r[i][1] for i in range(len(r)-1))/2
s=open(shp,'rb').read(); o=100; feats=[]; idx=0
while o<len(s):
    num,clen=struct.unpack('>ii',s[o:o+8]); o+=8; c=s[o:o+clen*2]; o+=clen*2
    st=struct.unpack('<i',c[:4])[0]
    if st==0: feats.append(None); idx+=1; continue
    nparts,npts=struct.unpack('<ii',c[36:44])
    parts=list(struct.unpack('<%di'%nparts,c[44:44+4*nparts]))+[npts]
    base=44+4*nparts
    pts=struct.unpack('<%dd'%(2*npts),c[base:base+16*npts])
    pts=[(pts[2*i],pts[2*i+1]) for i in range(npts)]
    polys=[]
    for a,b in zip(parts[:-1],parts[1:]):
        ring=dp(pts[a:b],tol)
        ring=[(round(x,3),round(y,3)) for x,y in ring]
        rr=[ring[0]]
        for q in ring[1:]:
            if q!=rr[-1]: rr.append(q)
        if rr[0]!=rr[-1]: rr.append(rr[0])
        if len(rr)<4: continue
        ar=area(rr)
        if ar<0: polys.append([rr])          # clockwise = outer (shapefile)
        elif polys: polys[-1].append(rr)     # hole
        else: polys.append([rr[::-1]])
    # GeoJSON RFC7946: outer ccw, holes cw
    gp=[[[list(p) for p in poly[0][::-1]]]+[[list(p) for p in h[::-1]] for h in poly[1:]] for poly in polys]
    geom={'type':'MultiPolygon','coordinates':gp} if len(gp)>1 else {'type':'Polygon','coordinates':gp[0]}
    feats.append({'type':'Feature','properties':dict(recs[idx]),'geometry':geom}); idx+=1
fc={'type':'FeatureCollection','features':[f for f in feats if f]}
json.dump(fc,open(out,'w'),separators=(',',':'))
import os; print(len(fc['features']),os.path.getsize(out))
