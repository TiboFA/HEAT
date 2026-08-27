from playwright.sync_api import sync_playwright
import pathlib,json
url="file://"+str(pathlib.Path("jeu.html").resolve())
JS=r"""()=>{
  // déterminisme total : même suite de tirages pour le témoin et pour l'essai
  rnd=()=>0.5;
  const TOURS=5;            // on laisse cinq tours au levier pour produire ses effets différés
  const BK="cn";            // bloc d'application standard
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
  function avance(s){
    for(let i=0;i<TOURS && !s.over;i++){ s.defi=null; finTour(s); s.plan=[]; }
    return projeter(s);
  }
  const out=[];
  CARDS.forEach(c=>{
    const camp = c.c==="actif"?"actif":"att";
    const t0=base(camp), t1=base(camp);
    let ref,ess,err=null;
    try{ ref=avance(t0); }catch(e){ err="temoin:"+e; }
    try{
      const s=t1; s.cur=camp;
      const b = c.cible==="global" ? null : B(s,BK);
      c.f(s,b);
      if(b) b.mesures.forEach(()=>{});
      ess=avance(s);
    }catch(e){ err=(err||"")+" essai:"+String(e); }
    out.push({id:c.id,n:c.n,c:c.c,cible:c.cible,fam:c.fam,
              cp:c.cp||0,cap:c.cap||0,att:c.att||0,
              ref,ess,d: (ref!==undefined&&ess!==undefined)? +(ess-ref).toFixed(3):null, err});
  });
  return out;
}"""
with sync_playwright() as p:
    br=p.chromium.launch(); pg=br.new_page(); pg.goto(url); pg.wait_for_timeout(400)
    res=pg.evaluate(JS); br.close()
json.dump(res,open("/tmp/puissance.json","w"),ensure_ascii=False,indent=1)
errs=[r for r in res if r["err"]]
print("cartes:",len(res),"erreurs:",len(errs))
for e in errs[:10]: print("  ",e["id"],e["err"])
# le signe utile : pour l'actif on veut d<0 (moins de réchauffement), pour l'att d>0
def eff(r):
    if r["d"] is None: return None
    return -r["d"] if r["c"]=="actif" else r["d"]
rows=[(eff(r),r) for r in res if r["d"] is not None]
rows.sort(key=lambda x:-x[0])
print("\n--- classement par effet utile sur la trajectoire (°C) ---")
for e,r in rows:
    if abs(e)>=0.001: print(f"{e:+.3f}  {r['id']:4} {r['c']:5} {r['cible']:6} {r['n'][:52]}")
nz=[e for e,r in rows if abs(e)>=0.001]
print(f"\n{len(nz)} leviers à effet mesurable sur {len(rows)} ; {len(rows)-len(nz)} sans effet mesuré sur la trajectoire")
