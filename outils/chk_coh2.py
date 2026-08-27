from playwright.sync_api import sync_playwright
import pathlib,re,json
url="file://"+str(pathlib.Path("jeu.html").resolve())
JS=open("/tmp/coh.js").read() if False else None
JS=r"""()=>{
  alg=()=>1; mGeo=()=>1;
  const out=[];
  CARDS.forEach(c=>{
    const s=newGame(c.c==="actif"?"actif":"att",3);
    s.doc.actif={d1:50,d2:0,d3:50,d4:50}; s.doc.att={d1:50,d2:50,d3:50,d4:50};
    s.blocs.forEach(b=>{b.contr=40;b.reel=45;b.percu=55;b.fr=30;b.mesures=[{src:"A01",v:12}];});
    s.tech=25; s.cur=c.c;
    const snap=()=>s.blocs.map(b=>[b.contr,b.reel,b.percu,b.fr,b.cap]).concat([[s.tech]]);
    const av=JSON.stringify(snap());
    const k={};
    try{ c.f(s,B(s,"cn")); }catch(e){ out.push({id:c.id,err:String(e)}); return; }
    const ap=snap(), a=JSON.parse(av);
    const champs=["contrainte","réel","perçu","friction","plafond"];
    const vus=new Set();
    ap.slice(0,8).forEach((r,i)=>r.forEach((v,j)=>{ if(v!==a[i][j]) vus.add(champs[j]); }));
    if(ap[8][0]!==a[8][0]) vus.add("technologique");
    out.push({id:c.id,n:c.n,e:c.e,vus:[...vus]});
  });
  return out;
}"""
MOT={"contrainte":["contrainte"],"réel":["réel"],"perçu":["perçu","opinion"],
     "friction":["friction"],"plafond":["plafond","verrou"],"technologique":["technolog"]}
with sync_playwright() as p:
    br=p.chromium.launch(); pg=br.new_page(); pg.goto(url); pg.wait_for_timeout(300)
    res=pg.evaluate(JS); br.close()
n=0
for r in res:
    if "err" in r: print(r); continue
    e=r["e"].lower()
    manque=[v for v in r["vus"] if not any(m in e for m in MOT[v])]
    if manque:
        n+=1; print(r["id"],"—",r["n"]); print("   dit :",r["e"]); print("   fait aussi bouger :",", ".join(manque)); print()
print(n,"cartes dont un effet mesuré n'est pas annoncé")
