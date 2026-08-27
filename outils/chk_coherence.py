from playwright.sync_api import sync_playwright
import pathlib,json,re
url="file://"+str(pathlib.Path("jeu.html").resolve())
JS=r"""()=>{
  alg=()=>1; mGeo=()=>1;
  const out=[];
  const snap=s=>({T:s.tech,cum:s.cum,
    blocs:s.blocs.map(b=>({k:b.k,contr:b.contr,cap:b.cap,reel:b.reel,percu:b.percu,fr:b.fr,
      verrou:b.verrou?1:0,bloque:b.bloque,compens:b.compens,suivi:b.suivi?1:0,media:b.media?1:0,
      revoyure:b.revoyure,transp:b.transp?1:0,guerre:b.guerre?1:0,cbam:b.cbam,subv:b.subv,coal:b.coal,mes:b.mesures.length})),
    res:JSON.parse(JSON.stringify(s.res)), pubOff:s.pubOff,attOff:s.attOff,avis:s.avis,cliquet:s.cliquet,
    reveles:s.reveles,evitees:s.evitees,satur:s.satur?1:0,boost:s.boost,
    tp:s.techPend.length, pend:s.blocs.reduce((a,b)=>a+b.pend.length,0)});
  CARDS.forEach(c=>{
    const s=newGame(c.c==="actif"?"actif":"att",3);
    s.doc.actif={d1:50,d2:0,d3:50,d4:50}; s.doc.att={d1:50,d2:50,d3:50,d4:50};
    s.blocs.forEach(b=>{b.contr=30;b.reel=40;b.percu=50;b.fr=20;});
    s.tech=20; s.cur=c.c;
    const av=snap(s), b=B(s,"cn");
    try{ c.f(s,b); }catch(e){ out.push({id:c.id,err:String(e)}); return; }
    const ap=snap(s);
    const d=[];
    ap.blocs.forEach((nb,i)=>{const ob=av.blocs[i];
      Object.keys(nb).forEach(k=>{ if(k==="k")return;
        if(nb[k]!==ob[k]) d.push(nb.k+"."+k+" "+(nb[k]-ob[k]>0?"+":"")+(typeof nb[k]==="number"?(nb[k]-ob[k]):nb[k]));});});
    ["tp","pend","pubOff","attOff","avis","cliquet","reveles","evitees","satur","boost"].forEach(k=>{
      if(ap[k]!==av[k]) d.push(k+" "+(ap[k]-av[k]>0?"+":"")+(ap[k]-av[k]));});
    if(ap.T!==av.T) d.push("tech "+(ap.T-av.T>0?"+":"")+(ap.T-av.T));
    ["actif","att"].forEach(cp=>["cp","cap","att","cred"].forEach(k=>{
      if(ap.res[cp][k]!==av.res[cp][k]) d.push(cp+"."+k+" "+(ap.res[cp][k]-av.res[cp][k]>0?"+":"")+(ap.res[cp][k]-av.res[cp][k]));}));
    out.push({id:c.id,n:c.n,c:c.c,e:c.e,d});
  });
  return out;
}"""
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page()
    pg.goto(url); pg.wait_for_timeout(300)
    res=pg.evaluate(JS); b.close()

def nums(t):
    return set(int(m) for m in re.findall(r"[+−-]\s?(\d+)", t.replace("−","−")))
susp=[]
for r in res:
    if "err" in r: susp.append((r["id"],"ERREUR",r["err"],"")); continue
    dec=nums(r["e"]); meas=set()
    for x in r["d"]:
        m=re.search(r"([+-]?\d+)$",x)
        if m: meas.add(abs(int(m.group(1))))
    manque=sorted(n for n in dec if n not in meas and n>1)
    if manque: susp.append((r["id"],r["n"],r["e"],"; ".join(r["d"]) or "AUCUN EFFET MESURÉ",manque))
print(len(res),"cartes ·",len(susp),"à vérifier\n")
for s in susp:
    print(s[0],"—",s[1]); print("   dit :",s[2]); print("   fait:",s[3]); print("   nombres annoncés introuvables:",s[4]); print()
