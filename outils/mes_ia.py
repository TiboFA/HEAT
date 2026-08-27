from playwright.sync_api import sync_playwright
import pathlib,sys,statistics
f=sys.argv[1]
url="file://"+str(pathlib.Path(f).resolve())
JS=r"""(lvl)=>{
  const out=[];
  for(let g=0; g<12; g++){
    for(const camp of ["actif","att"]){
      rng=1234+g*77;
      const s=newGame(camp,lvl);
      // le joueur ne joue rien : on ne mesure que l'adversaire
      while(!s.over && s.turn<=NTURNS){
        const av=s.joues.length;
        iaJoue(s);
        out.push({adv:camp==="actif"?"att":"actif", n:s.joues.length-av, lvl});
        finTour(s);
      }
    }
  }
  return out;
}"""
with sync_playwright() as p:
    br=p.chromium.launch(); pg=br.new_page(); pg.goto(url); pg.wait_for_timeout(400)
    print(f)
    for lvl in (1,2,3,4):
        res=pg.evaluate(JS,lvl)
        for adv in ("att","actif"):
            v=[r["n"] for r in res if r["adv"]==adv]
            print(f"  niveau {lvl}  adversaire {adv:5} : {statistics.mean(v):.2f} leviers/tour  (n={len(v)})")
    br.close()
