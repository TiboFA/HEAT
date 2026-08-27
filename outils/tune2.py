from playwright.sync_api import sync_playwright
import pathlib,statistics,sys,json
url="file://"+str(pathlib.Path("jeu.html").resolve())
N=int(sys.argv[1]) if len(sys.argv)>1 else 24
JS=r"""([camp,lvl,n,ACT,NS])=>{
  NIVEAUX.forEach((x,i)=>{ if(x) x.n=NS[i]; });
  const out=[];
  for(let p=0;p<n;p++){
    rng=(p*2654435761+lvl*7919+(camp==="actif"?1:2))&0x7fffffff;
    S=newGame(camp,lvl); S.hand=[];S.handAI=[];refill(S);refillAI(S);
    let nl=0,nt=0;
    while(!S.over && S.turn<=NTURNS){
      let k=0;
      while(k<ACT){
        const j=S.hand.map(card).filter(c=>pds(c)<=ACT-k)
                 .filter(c=>c.cible!=="bloc"?!jouable(S,c,null,camp):S.blocs.some(b=>!jouable(S,c,b,camp)));
        if(!j.length) break;
        const c=j[Math.floor(rnd()*j.length)];
        const b=c.cible==="bloc"?S.blocs.find(z=>!jouable(S,c,z,camp)):null;
        jouer(S,c.id,b?b.k:null,camp); k+=pds(c); nl++;
      }
      nt++;
      iaJoue(S); finTour(S); S.actions=ACT;
    }
    out.push([projeter(S),score(S),S.seuilAn||0,nl/nt]);
  }
  return out;
}"""
CFG=json.loads(sys.argv[2]) if len(sys.argv)>2 else {"ACT":4,"NS":[None,3,4,5,7]}
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(); pg.goto(url); pg.wait_for_timeout(300)
    print("actions joueur =",CFG["ACT"],"  budget adversaire =",CFG["NS"][1:])
    for camp,nom in (("actif","actif     "),("att","attentiste")):
        for lvl in (1,2,3,4):
            r=pg.evaluate(JS,[camp,lvl,N,CFG["ACT"],CFG["NS"]])
            T=[x[0] for x in r]; sc=[x[1] for x in r]; se=[x for x in r if x[2]]; lv=[x[3] for x in r]
            print(f"{nom} niveau {lvl} : T={statistics.mean(T):.2f}  score={statistics.mean(sc):.0f}"
                  f"  seuil {len(se)}/{N}  leviers joueur/tour {statistics.mean(lv):.2f}")
    b.close()
