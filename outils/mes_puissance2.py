from playwright.sync_api import sync_playwright
import pathlib,json
url="file://"+str(pathlib.Path("jeu.html").resolve())
JS=r"""()=>{
  rnd=()=>0.5;
  const BK="cn";
  const FLAGS=["verrou","compens","media","suivi","transp","censure","repress","refer","revoyure","bloque","achat","cap"];
  function base(camp){
    const s=newGame(camp,2);
    s.turn=3; s.year=AN0+2*YPT;
    s.doc.actif={d1:50,d2:50,d3:50,d4:50}; s.doc.att={d1:50,d2:50,d3:50,d4:50};
    s.blocs.forEach(b=>{b.contr=35;b.reel=45;b.percu=45;b.fr=25;
      b.mesures=[{src:"A01",v:10},{src:"A02",v:8}];});
    s.tech=25;
    s.res.actif={cp:40,cap:40,att:9,cred:70};
    s.res.att   ={cp:40,cap:40,att:9,cred:60};
    s.cur=camp;
    return s;
  }
  function snap(s){
    return {
      percu:s.blocs.reduce((a,b)=>a+b.percu,0),
      fr:s.blocs.reduce((a,b)=>a+b.fr,0),
      contr:s.blocs.reduce((a,b)=>a+b.contr,0),
      capm:s.blocs.reduce((a,b)=>a+b.cap,0),
      reel:s.blocs.reduce((a,b)=>a+b.reel,0),
      mes:s.blocs.reduce((a,b)=>a+b.mesures.length,0),
      pend:s.blocs.reduce((a,b)=>a+b.pend.reduce((x,p)=>x+p.v,0),0),
      tech:s.tech+s.techPend.reduce((a,p)=>a+p.v,0),
      fl:s.blocs.reduce((a,b)=>a+FLAGS.reduce((x,f)=>x+(f==="cap"?0:(b[f]?1:0)),0),0),
      glob:(s.cliquet?1:0)+(s.sommetOff?1:0)+(s.techOff?1:0)+(s.avis?1:0)+(s.pubOff?1:0)+(s.attOff?1:0),
      acp:s.res.actif.cp,acap:s.res.actif.cap,aatt:s.res.actif.att,acred:s.res.actif.cred,
      tcp:s.res.att.cp,tcap:s.res.att.cap,tatt:s.res.att.att,tcred:s.res.att.cred
    };
  }
  const out=[];
  CARDS.forEach(c=>{
    const camp = c.c==="actif"?"actif":"att";
    const s=base(camp); const av=snap(s);
    let err=null;
    try{ c.f(s, c.cible==="global"?null:B(s,BK)); }catch(e){ err=String(e); }
    const ap=snap(s), d={};
    Object.keys(av).forEach(k=>{ if(ap[k]!==av[k]) d[k]=+(ap[k]-av[k]).toFixed(2); });
    out.push({id:c.id,n:c.n,c:c.c,cible:c.cible,d,err});
  });
  return out;
}"""
with sync_playwright() as p:
    br=p.chromium.launch(); pg=br.new_page(); pg.goto(url); pg.wait_for_timeout(400)
    res=pg.evaluate(JS); br.close()
json.dump(res,open("/tmp/puissance2.json","w"),ensure_ascii=False,indent=1)
traj={r["id"]:(-r["d"] if r["c"]=="actif" else r["d"]) for r in json.load(open("/tmp/puissance.json")) if r["d"] is not None}
muets=[r for r in res if abs(traj.get(r["id"],0))<0.001]
print(len(muets),"leviers sans effet mesuré sur la trajectoire — voici ce qu'ils font :\n")
for r in sorted(muets,key=lambda r:r["id"]):
    print(f"{r['id']:4} {r['c']:5} {r['cible']:6} {r['n'][:44]:46} {r['d']}")
