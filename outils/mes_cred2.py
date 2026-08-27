from playwright.sync_api import sync_playwright
import pathlib,sys,collections
url="file://"+str(pathlib.Path("jeu.html").resolve())
N=int(sys.argv[1]) if len(sys.argv)>1 else 24
JS=r"""([camp,lvl,n,prio])=>{
  // on instrumente CRED pour savoir d'où vient chaque point
  const CO=CRED; const cpt={};
  CRED=function(s,c,v,r){ const k=(r||"levier")+" → "+(c==="actif"?"actif":"att");
    cpt[k]=(cpt[k]||0)+v; CO(s,c,v,r); };
  for(let p=0;p<n;p++){
    rng=(p*2654435761+lvl*7919+(camp==="actif"?1:2))&0x7fffffff;
    S=newGame(camp,lvl); S.hand=[];S.handAI=[];refill(S);refillAI(S);
    while(!S.over && S.turn<=NTURNS){
      let k=0;
      while(k<ACTIONS){
        let j=S.hand.map(card).filter(c=>pds(c)<=ACTIONS-k)
                 .filter(c=>c.cible!=="bloc"?!jouable(S,c,null,camp):S.blocs.some(b=>!jouable(S,c,b,camp)));
        if(!j.length) break;
        let c=null;
        if(prio){ c=j.find(x=>prio.includes(x.id)); }
        if(!c) c=j[Math.floor(rnd()*j.length)];
        const b=c.cible==="bloc"?S.blocs.find(z=>!jouable(S,c,z,camp)):null;
        jouer(S,c.id,b?b.k:null,camp); k+=pds(c);
      }
      iaJoue(S); finTour(S);
    }
  }
  CRED=CO;
  return [cpt,S.res.actif.cred,S.res.att.cred];
}"""
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(); pg.goto(url); pg.wait_for_timeout(300)
    for camp,lvl,prio,lab in (("actif",3,None,"joueur actif niv3"),
                              ("att",3,None,"joueur attentiste niv3, politique aléatoire"),
                              ("att",3,["T48","T27","T53","T30","T26"],"joueur attentiste niv3, qui vise la crédibilité")):
        cpt,ca,cn=pg.evaluate(JS,[camp,lvl,N,prio])
        print(f"--- {lab}  ({N} parties)")
        tot=collections.Counter()
        for k,v in cpt.items(): tot[k]+=v
        for k,v in sorted(tot.items(),key=lambda x:-abs(x[1])):
            print(f"    {v/N:+7.1f} / partie   {k}")
    b.close()
