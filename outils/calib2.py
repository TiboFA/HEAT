from playwright.sync_api import sync_playwright
import pathlib, statistics
url="file://"+str(pathlib.Path("jeu.html").resolve())
JS = """
(cfg)=>{
  const {camp,level,actif,seed}=cfg;
  rng=seed;
  const s=newGame(camp,level);
  let coups=0, rates=0, tours=0;
  while(!s.over){
    tours++;
    if(actif){
      for(let i=0;i<3;i++){
        const coup = camp==="actif"?choixActif(s):choixAtt(s);
        if(!coup){ rates++; break; }
        s.plan.push({k:"lev",id:coup.id,bk:coup.b}); coups++;
      }
      if(s.ev&&s.ev.attr&&!s.satur) s.plan.push({k:"attr"});
    }
    s.fx=[];
    s.plan.forEach(e=>{ if(e.k==="attr"){attribuer(s,camp);return;} jouer(s,e.id,e.bk,camp); s.actions--; });
    s.plan=[];
    verifierCombos(s,s.coups,camp);
    iaJoue(s);
    finTour(s);
  }
  return {T:s.T, proj:projeter(s), sc:score(s), emis:+totE(s).toFixed(1), morts:+s.morts.toFixed(0),
    actifs:s.actifs, evitees:s.evitees, coups, rates, tours, dgB:s.dmgBase, dgA:s.dmgAutres, cp:s.res[camp==="actif"?"actif":"att"].cp,
    contr:Math.round(s.blocs.reduce((a,b)=>a+b.contr,0)/8), verrous:s.blocs.filter(b=>b.verrou).length,
    res:s.res[camp==="actif"?"actif":"att"].cap};
}
"""
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(); pg.goto(url); pg.wait_for_timeout(300)
    def run(camp,level,actif,n=12):
        v=[pg.evaluate(JS,{"camp":camp,"level":level,"actif":actif,"seed":1000+97*i}) for i in range(n)]
        m=lambda k: round(statistics.mean(x[k] for x in v),1)
        return dict(proj=round(statistics.mean(x["proj"] for x in v),3), sc=m("sc"), emis=m("emis"),
                    morts=m("morts"), coups=m("coups"), rates=m("rates"), contr=m("contr"),
                    verrous=m("verrous"), capfin=m("res"), cpfin=m("cp"), actifs=m("actifs"), dgB=m("dgB"), dgA=m("dgA"))
    print("passif      ", run("actif",2,False))
    for lv in (1,2,3,4): print(f"actif   niv{lv}", run("actif",lv,True))
    for lv in (1,2,3,4): print(f"attent. niv{lv}", run("att",lv,True))
    b.close()
