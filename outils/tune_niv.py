from playwright.sync_api import sync_playwright
import pathlib,statistics,itertools
url="file://"+str(pathlib.Path("jeu.html").resolve())
JS=r"""(cfg)=>{
  NIVEAUX.forEach((x,i)=>{ if(x) x.n=cfg[i]; });
  const out=[];
  for(let g=0; g<12; g++){
    for(const camp of ["actif","att"]){
      rng=1234+g*77;
      const s=newGame(camp,cfg.lvl);
      while(!s.over && s.turn<=NTURNS){
        const av=s.joues.length; iaJoue(s);
        out.push({adv:camp==="actif"?"att":"actif", n:s.joues.length-av});
        finTour(s);
      }
    }
  }
  return out;
}"""
CIBLE={1:(1.89,1.87),2:(2.88,2.63),3:(3.74,3.51),4:(4.46,4.44)}
with sync_playwright() as p:
    br=p.chromium.launch(); pg=br.new_page(); pg.goto(url); pg.wait_for_timeout(400)
    for lvl,cands in {1:(2,3),2:(3,4,5),3:(5,6),4:(6,7,8)}.items():
        for n in cands:
            cfg=[None,0,0,0,0]; cfg[lvl]=n
            cfg={"0":None,"1":2,"2":3,"3":4,"4":5,"lvl":lvl}
            arr=[None,2,3,4,5]; arr[lvl]=n
            res=pg.evaluate(JS,{**{str(i):v for i,v in enumerate(arr)},"lvl":lvl,"length":5,
                                "0":None,"1":arr[1],"2":arr[2],"3":arr[3],"4":arr[4]})
            a=[r["n"] for r in res if r["adv"]=="att"]; b=[r["n"] for r in res if r["adv"]=="actif"]
            ca,cb=CIBLE[lvl]
            print(f"niveau {lvl} n={n} : att {statistics.mean(a):.2f} (cible {ca})  actif {statistics.mean(b):.2f} (cible {cb})")
    br.close()
