from playwright.sync_api import sync_playwright
import pathlib,re,html
url="file://"+str(pathlib.Path("jeu.html").resolve())
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page()
    pg.goto(url); pg.wait_for_timeout(300)
    txt=pg.evaluate("""()=>{
      rng=4242; const s=newGame("actif",3);
      // un tour joué à la main pour couvrir un maximum de cas
      s.hand=["A01","A31","A12","A05","A65","A18","A02","A17","A20","A40","A11","A04"];
      s.plan=[{k:"lev",id:"A01",bk:"cn"},{k:"lev",id:"A31",bk:"cn"},{k:"lev",id:"A12",bk:"eu"},{k:"attr"}];
      s.fx=[];
      s.plan.forEach(e=>{if(e.k==="attr"){attribuer(s,"actif");return;} jouer(s,e.id,e.bk,"actif"); s.actions--;});
      s.plan=[]; verifierCombos(s,s.coups,"actif"); iaJoue(s); finTour(s);
      return s.log.map(l=>(l.cls==="sh"?"### ":l.cls==="th"?"## ":"["+l.cls+"] ")+l.txt).join("\\n");
    }""")
    print(re.sub(r'<[^>]+>','',html.unescape(txt)))
    b.close()
