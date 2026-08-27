from playwright.sync_api import sync_playwright
import pathlib, statistics, json
url="file://"+str(pathlib.Path("HEAT_jeu_v0.3.html").resolve())
JS = """
(cfg)=>{
  const {camp,level,actif,seed}=cfg;
  rng=seed;
  const s=newGame(camp,level);
  while(!s.over){
    const plan=[];
    if(actif){
      for(let i=0;i<3;i++){
        const coup = camp==="actif"?choixActif(s):choixAtt(s);
        if(!coup) break;
        plan.push({k:"lev",id:coup.id,bk:coup.b});
      }
      if(s.ev&&s.ev.attr&&!s.satur) plan.push({k:"attr"});
    }
    s.fx=[];
    plan.forEach(e=>{ if(e.k==="attr"){attribuer(s,camp);return;} jouer(s,e.id,e.bk,camp); s.actions--; });
    verifierCombos(s,s.coups,camp);
    iaJoue(s);
    finTour(s);
  }
  return {T:s.T, proj:projeter(s), sc:score(s)};
}
"""
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page()
    pg.goto(url); pg.wait_for_timeout(300)
    def run(camp,level,actif):
        v=[pg.evaluate(JS,{"camp":camp,"level":level,"actif":actif,"seed":1000+97*i}) for i in range(16)]
        return statistics.mean(x["proj"] for x in v)
    print("passif (aucun coup)      :", round(run("actif",2,False),3))
    for lv in (1,2,3,4):
        print(f"actif      niveau {lv}      :", round(run("actif",lv,True),3))
    for lv in (1,2,3,4):
        print(f"attentiste niveau {lv}      :", round(run("att",lv,True),3))
    b.close()
