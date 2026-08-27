# Campagne de calibrage v0.10 — politique neutre : à chaque action, un levier
# jouable tiré au hasard. « Premier de la main » n'était pas neutre : l'ordre de
# la main est l'ordre de tirage pondéré par la doctrine, il corrèle avec rien.
from playwright.sync_api import sync_playwright
import pathlib,statistics,sys
url="file://"+str(pathlib.Path("HEAT_jeu_v0.10.html").resolve())
N=int(sys.argv[1]) if len(sys.argv)>1 else 30
JS=r"""([camp,lvl,n,passif])=>{
  const out=[];
  for(let p=0;p<n;p++){
    rng=(p*2654435761+lvl*7919+(camp==="actif"?1:2))&0x7fffffff;
    S=newGame(camp,lvl); S.hand=[];S.handAI=[];refill(S);refillAI(S);
    while(!S.over && S.turn<=NTURNS){
      if(!passif){
        let k=0;
        while(k<ACTIONS){
          // le joueur automatique paie le poids des leviers, comme le joueur humain
          const j=S.hand.map(card).filter(c=>pds(c)<=ACTIONS-k)
                        .filter(c=>c.cible!=="bloc"?!jouable(S,c,null,camp):S.blocs.some(b=>!jouable(S,c,b,camp)));
          if(!j.length) break;
          const c=j[Math.floor(rnd()*j.length)];
          const b=c.cible==="bloc"?S.blocs.find(z=>!jouable(S,c,z,camp)):null;
          jouer(S,c.id,b?b.k:null,camp); k+=pds(c);
        }
      }
      if(!passif) iaJoue(S);
      finTour(S);
    }
    out.push([projeter(S),score(S),totE(S),S.picAn||0,S.seuilAn||0]);
  }
  return out;
}"""
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(); pg.goto(url); pg.wait_for_timeout(300)
    r=pg.evaluate(JS,["actif",2,1,True])
    print(f"passif (aucun coup)      : {r[0][0]:.2f} °C · {r[0][2]:.1f} GtCO₂/an")
    for camp,nom in (("actif","actif     "),("att","attentiste")):
        for lvl in (1,2,3,4):
            r=pg.evaluate(JS,[camp,lvl,N,False])
            T=[x[0] for x in r]; sc=[x[1] for x in r]
            pic=[x[3] for x in r if x[3]]; se=[x[4] for x in r if x[4]]
            print(f"{nom} niveau {lvl} : T={statistics.mean(T):.2f} (±{statistics.stdev(T):.2f})"
                  f"  score={statistics.mean(sc):.0f}"
                  f"  pic={statistics.mean(pic):.0f}" if pic else "",
                  f" seuil atteint {len(se)}/{N}")
    b.close()
