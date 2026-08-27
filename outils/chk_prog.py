from playwright.sync_api import sync_playwright
import pathlib
url="file://"+str(pathlib.Path("jeu.html").resolve())
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page()
    errs=[]; pg.on("pageerror",lambda e:errs.append(str(e)))
    pg.goto(url); pg.wait_for_timeout(300); pg.evaluate("()=>{GUIDE_VU=true;}"); pg.click("#start"); pg.wait_for_timeout(300)
    print(pg.evaluate("""()=>{const out=[];
      for(const lv of [1,2,3]){
        const s=newGame("actif",lv);
        for(const t of [1,3,5,9,13]){ s.turn=t;
          out.push(`niv${lv} tour${t} (${2015+(t-1)*5}) : actif ${pool(s,"actif").length} ouverts / ${aVenir(s,"actif").length} à venir`);}
      }
      for(const lv of [1,2,3]){
        const s=newGame("att",lv);
        for(const t of [1,3,5,9,13]){ s.turn=t;
          out.push(`niv${lv} tour${t} (${2015+(t-1)*5}) : attentiste ${pool(s,"att").length} ouverts / ${aVenir(s,"att").length} à venir`);}
      }
      return out.join("\\n");}"""))
    print("errors:", errs or "none")
    b.close()
