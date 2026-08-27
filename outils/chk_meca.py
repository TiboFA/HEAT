from playwright.sync_api import sync_playwright
import pathlib,re
url="file://"+str(pathlib.Path("jeu.html").resolve())
JS=r"""(lvl)=>{
  const cnt={}, add=k=>cnt[k]=(cnt[k]||0)+1; const err=[];
  const advCards={};
  for(let p=0;p<10;p++){
    rng=(p*104729+7)&0x7fffffff;
    S=newGame("actif",lvl); S.hand=[];S.handAI=[];refill(S);refillAI(S);
    while(!S.over && S.turn<=NTURNS){
      let n=0;
      while(n<3){
        const j=S.hand.map(card).filter(c=>c.cible!=="bloc"?!jouable(S,c,null,"actif"):S.blocs.some(b=>!jouable(S,c,b,"actif")));
        if(!j.length) break;
        const c=j[0], b=c.cible==="bloc"?S.blocs.find(z=>!jouable(S,c,z,"actif")):null;
        try{ jouer(S,c.id,b?b.k:null,"actif"); }catch(e){ err.push(c.id+" "+e.message); break; }
        n++;
      }
      const nAv=S.log.length;
      try{ iaJoue(S); finTour(S); }catch(e){ err.push("finTour "+e.message); break; }
      S.log.slice(nAv).forEach(l=>{
        if(/Référendum/.test(l.txt)) add(/confirmée/.test(l.txt)?"référendum gagné":"référendum perdu");
        if(/campagne saturée/.test(l.txt)) add("scrutin saturé");
        if(/veto de procédure/i.test(l.txt)) add("sommet bloqué");
        if(/seuils de la courbe/i.test(l.txt)) add("seuils techno neutralisés");
      });
    }
    S.adv.forEach(a=>{advCards[a.id]=(advCards[a.id]||0)+1;});
  }
  return {cnt,err:err.slice(0,5),advCards};
}"""
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(); pg.goto(url); pg.wait_for_timeout(300)
    r=pg.evaluate(JS,3)
    print("mécaniques déclenchées sur 10 parties :", r["cnt"])
    print("erreurs:", r["err"] or "aucune")
    neuf={k:v for k,v in r["advCards"].items() if k in ("T60","T61","T62","T63","T64","T65","T66","T67","T68","T69","T70","T71","T72","T73")}
    print("nouveaux leviers joués par l'IA attentiste:", dict(sorted(neuf.items(),key=lambda x:-x[1])))
    b.close()
