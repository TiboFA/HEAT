from playwright.sync_api import sync_playwright
import pathlib,statistics,sys
url="file://"+str(pathlib.Path("HEAT_jeu_v0.10.html").resolve())
N=int(sys.argv[1]) if len(sys.argv)>1 else 24
JS=r"""([camp,lvl,n])=>{
  const out=[];
  for(let p=0;p<n;p++){
    rng=(p*2654435761+lvl*7919+(camp==="actif"?1:2))&0x7fffffff;
    S=newGame(camp,lvl); S.hand=[];S.handAI=[];refill(S);refillAI(S);
    const tr=[];
    while(!S.over && S.turn<=NTURNS){
      let k=0;
      while(k<ACTIONS){
        const j=S.hand.map(card).filter(c=>pds(c)<=ACTIONS-k)
                 .filter(c=>c.cible!=="bloc"?!jouable(S,c,null,camp):S.blocs.some(b=>!jouable(S,c,b,camp)));
        if(!j.length) break;
        const c=j[Math.floor(rnd()*j.length)];
        const b=c.cible==="bloc"?S.blocs.find(z=>!jouable(S,c,z,camp)):null;
        jouer(S,c.id,b?b.k:null,camp); k+=pds(c);
      }
      iaJoue(S); finTour(S);
      tr.push([S.turn,S.res.actif.cred,S.res.att.cred]);
    }
    out.push(tr);
  }
  return out;
}"""
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(); pg.goto(url); pg.wait_for_timeout(300)
    for camp,nom in (("actif","actif     "),("att","attentiste")):
        for lvl in (1,3):
            r=pg.evaluate(JS,[camp,lvl,N])
            print(f"--- joueur {nom} niveau {lvl}")
            for t in (2,6,10,14,18):
                a=[x[1] for tr in r for x in tr if x[0]==t]; d=[x[2] for tr in r for x in tr if x[0]==t]
                if not a: continue
                ec=[x-y for x,y in zip(a,d)]
                print(f"    tour {t-1:2} : actif {statistics.mean(a):5.1f}  att {statistics.mean(d):5.1f}  écart {statistics.mean(ec):+6.1f}  (min {min(ec):+.0f} max {max(ec):+.0f})")
            fin=[tr[-1] for tr in r]
            sat=sum(1 for x in fin if x[1]<=0 or x[2]<=0 or x[1]>=100 or x[2]>=100)
            print(f"    parties où une crédibilité touche 0 ou 100 : {sat}/{len(fin)}")
    b.close()
