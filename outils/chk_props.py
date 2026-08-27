from playwright.sync_api import sync_playwright
import pathlib
url="file://"+str(pathlib.Path("jeu.html").resolve())
JS=r"""()=>{
  const s=newGame("actif",3), b=B(s,"cn");
  const okS=new Set(Object.keys(s)), okB=new Set(Object.keys(b));
  const bad=[];
  CARDS.forEach(c=>{
    const src=c.f.toString();
    // premier paramètre = état, second = bloc
    const m=src.match(/^\(?\s*([A-Za-z_$]\w*)?\s*,?\s*([A-Za-z_$]\w*)?\s*\)?\s*=>/);
    const ns=m&&m[1], nb=m&&m[2];
    const re=/([A-Za-z_$]\w*)\.([A-Za-z_$]\w*)/g; let x;
    while((x=re.exec(src))){
      const o=x[1], p=x[2];
      if(ns&&o===ns&&!okS.has(p)&&!["blocs","res","forEach","map","filter","sort","slice","push"].includes(p)) bad.push(c.id+" : s."+p);
      if(nb&&o===nb&&!okB.has(p)) bad.push(c.id+" : bloc."+p);
      if(["b","x","z","bl"].includes(o)&&o!==ns&&!okB.has(p)&&!["forEach","map","filter","sort","slice","push","length","toFixed"].includes(p)) bad.push(c.id+" : "+o+"."+p);
    }
  });
  return [...new Set(bad)];
}"""
with sync_playwright() as p:
    br=p.chromium.launch(); pg=br.new_page(); pg.goto(url); pg.wait_for_timeout(300)
    for r in pg.evaluate(JS): print(r)
    br.close()
