from playwright.sync_api import sync_playwright
import pathlib, statistics
url="file://"+str(pathlib.Path("HEAT_jeu_v0.10.html").resolve())
JS = """
(cfg)=>{const {camp,level,actif,seed}=cfg; rng=seed;
  const s=newGame(camp,level);
  while(!s.over){
    if(actif){ for(let i=0;i<3;i++){const c=camp==="actif"?choixActif(s):choixAtt(s); if(!c)break;
        s.plan.push({k:"lev",id:c.id,bk:c.b});}
      if(s.ev&&s.ev.attr&&!s.satur) s.plan.push({k:"attr"}); }
    s.fx=[];
    s.plan.forEach(e=>{ if(e.k==="attr"){attribuer(s,camp);return;} jouer(s,e.id,e.bk,camp); s.actions--; });
    s.plan=[]; verifierCombos(s,s.coups,camp); iaJoue(s); finTour(s);
  }
  return {pic:s.picAn, seuil:s.seuilAn, sc:score(s), pal:palier(score(s))[1], proj:projeter(s), fin:+totE(s).toFixed(1)};}
"""
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(); pg.goto(url); pg.wait_for_timeout(300)
    def run(camp,level,actif,n=16):
        v=[pg.evaluate(JS,{"camp":camp,"level":level,"actif":actif,"seed":1000+97*i}) for i in range(n)]
        med=lambda k:[x[k] for x in v if x[k]]
        return dict(pic=(f"{int(statistics.median(med('pic')))} ({len(med('pic'))}/{n})" if med('pic') else "jamais"),
                    seuil=(f"{int(statistics.median(med('seuil')))} ({len(med('seuil'))}/{n})" if med('seuil') else "jamais"),
                    sc=round(statistics.mean(x["sc"] for x in v)),
                    proj=round(statistics.mean(x["proj"] for x in v),2),
                    paliers=", ".join(sorted({x["pal"] for x in v})))
    print("passif      ", run("actif",2,False))
    for lv in (1,2,3,4): print(f"actif   niv{lv}", run("actif",lv,True))
    for lv in (1,2,3,4): print(f"attent. niv{lv}", run("att",lv,True))
    b.close()
