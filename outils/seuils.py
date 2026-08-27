from playwright.sync_api import sync_playwright
import pathlib, statistics
url="file://"+str(pathlib.Path("HEAT_jeu_v0.10.html").resolve())
JS = """
(cfg)=>{
  const {camp,level,actif,seed}=cfg;
  rng=seed;
  const s=newGame(camp,level);
  const seuils=[30,25,20,15,10], hit={};
  let pic={e:totE(s),an:2015}, serie=[];
  while(!s.over){
    if(actif){
      for(let i=0;i<3;i++){const c=camp==="actif"?choixActif(s):choixAtt(s); if(!c)break;
        s.plan.push({k:"lev",id:c.id,bk:c.b});}
      if(s.ev&&s.ev.attr&&!s.satur) s.plan.push({k:"attr"});
    }
    s.fx=[];
    s.plan.forEach(e=>{ if(e.k==="attr"){attribuer(s,camp);return;} jouer(s,e.id,e.bk,camp); s.actions--; });
    s.plan=[]; verifierCombos(s,s.coups,camp); iaJoue(s); finTour(s);
    const e=totE(s);
    serie.push([s.year,+e.toFixed(1)]);
    if(e>pic.e){pic={e:+e.toFixed(1),an:s.year};}
    seuils.forEach(v=>{ if(hit[v]===undefined && e<v) hit[v]=s.year; });
  }
  return {hit, pic, fin:+totE(s).toFixed(1), T:s.T, proj:projeter(s)};
}
"""
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(); pg.goto(url); pg.wait_for_timeout(300)
    def run(camp,level,actif,n=16):
        v=[pg.evaluate(JS,{"camp":camp,"level":level,"actif":actif,"seed":1000+97*i}) for i in range(n)]
        out={}
        for s in (30,25,20,15,10):
            ans=[x["hit"].get(str(s)) or x["hit"].get(s) for x in v]
            ok=[a for a in ans if a]
            out[s]= f"{len(ok)}/{n}" + (f" med.{int(statistics.median(ok))}" if ok else "")
        out["pic"]=f'{round(statistics.mean(x["pic"]["e"] for x in v),1)} Gt en {int(statistics.median(x["pic"]["an"] for x in v))}'
        out["fin Gt"]=round(statistics.mean(x["fin"] for x in v),1)
        return out
    print("passif      ", run("actif",2,False))
    for lv in (1,2,3,4): print(f"actif   niv{lv}", run("actif",lv,True))
    for lv in (1,2,3,4): print(f"attent. niv{lv}", run("att",lv,True))
    b.close()
