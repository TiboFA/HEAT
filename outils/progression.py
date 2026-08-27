from playwright.sync_api import sync_playwright
import pathlib, statistics
url="file://"+str(pathlib.Path("HEAT_jeu_v0.10.html").resolve())
JS = """
(cfg)=>{const {camp,level,seed}=cfg; rng=seed;
  const s=newGame(camp,level); const tr=[];
  while(!s.over){
    for(let i=0;i<3;i++){const c=camp==="actif"?choixActif(s):choixAtt(s); if(!c)break;
      s.plan.push({k:"lev",id:c.id,bk:c.b});}
    if(s.ev&&s.ev.attr&&!s.satur) s.plan.push({k:"attr"});
    s.fx=[];
    s.plan.forEach(e=>{ if(e.k==="attr"){attribuer(s,camp);return;} jouer(s,e.id,e.bk,camp); s.actions--; });
    s.plan=[]; verifierCombos(s,s.coups,camp); iaJoue(s); finTour(s);
    const cm=s.blocs.reduce((a,b)=>a+b.contr*b.e,0)/Math.max(totE(s),.01);
    tr.push({t:s.turn-1, an:s.year-5,
      cm:+cm.toFixed(0), tech:s.tech,
      pcMax:Math.max(...s.blocs.map(b=>b.percu)),
      pcMoy:Math.round(s.blocs.reduce((a,b)=>a+b.percu,0)/8),
      mes:s.blocs.reduce((a,b)=>a+b.mesures.length,0),
      joues:s.joues.length, verrou:s.blocs.filter(b=>b.verrou).length,
      cbam:s.blocs.filter(b=>b.cbam).length, subv:s.blocs.filter(b=>b.subv).length,
      credA:s.res.actif.cred, credT:s.res.att.cred});
  }
  return tr;}
"""
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(); pg.goto(url); pg.wait_for_timeout(300)
    runs=[pg.evaluate(JS,{"camp":"actif","level":3,"seed":1000+97*i}) for i in range(8)]
    print("joueur actif, niveau 3 — médianes par tour")
    print(f"{'tour':>4} {'année':>6} {'contr.moy':>9} {'tech':>5} {'perçu max':>9} {'perçu moy':>9} {'mesures':>8} {'coups':>6} {'verrous':>7}")
    for i in range(17):
        col=lambda k: int(statistics.median(r[i][k] for r in runs if len(r)>i))
        print(f"{col('t'):>4} {col('an'):>6} {col('cm'):>9} {col('tech'):>5} {col('pcMax'):>9} {col('pcMoy'):>9} {col('mes'):>8} {col('joues'):>6} {col('verrou'):>7}")
    b.close()
