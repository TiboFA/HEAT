from playwright.sync_api import sync_playwright
import pathlib,collections
url="file://"+str(pathlib.Path("jeu.html").resolve())
JS=r"""(lvl)=>{
  const res={defis:{},cartes:{},err:[],tours:0,manqueDefi:0};
  for(let p=0;p<8;p++){
    rng=(p*7919+13)&0x7fffffff;
    S=newGame("att",lvl); S.hand=[];S.handAI=[];refill(S);refillAI(S);
    while(!S.over && S.turn<=NTURNS){
      if(!S.defi) res.manqueDefi++;
      else res.defis[S.defi.t]=(res.defis[S.defi.t]||0)+1;
      let n=0;
      while(n<3){
        const jouables=S.hand.map(card).filter(c=>{
          if(c.cible!=="bloc") return !jouable(S,c,null,"att");
          return S.blocs.some(b=>!jouable(S,c,b,"att"));});
        if(!jouables.length) break;
        const c=jouables[0];
        const b=c.cible==="bloc"?S.blocs.find(z=>!jouable(S,c,z,"att")):null;
        try{ jouer(S,c.id,b?b.k:null,"att"); }catch(e){ res.err.push(c.id+" : "+e.message); break; }
        res.cartes[c.id]=(res.cartes[c.id]||0)+1; n++;
      }
      try{ iaJoue(S); finTour(S); }catch(e){ res.err.push("finTour t"+S.turn+" : "+e.message); break; }
      res.tours++;
    }
  }
  res.score=score(S); res.proj=projeter(S);
  return res;
}"""
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(); pg.goto(url); pg.wait_for_timeout(300)
    r=pg.evaluate(JS,3)
    print("tours joués:",r["tours"],"· tours sans défi:",r["manqueDefi"])
    print("erreurs:",r["err"][:5] or "aucune")
    print("\ndéfis tirés (joueur attentiste):")
    for k,v in sorted(r["defis"].items(),key=lambda x:-x[1]): print(f"   {v:3d}  {k}")
    neuf=[c for c in r["cartes"] if c in ("T60","T61","T62","T63","T64","T65","T66","T67","T68","T69","T70","T71","T72","T73")]
    print("\nnouveaux leviers effectivement joués:",len(neuf),"/14 —",sorted(neuf))
    print("jamais joués:",sorted(set("T60 T61 T62 T63 T64 T65 T66 T67 T68 T69 T70 T71 T72 T73".split())-set(neuf)))
    b.close()
