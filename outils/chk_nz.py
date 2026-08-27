from playwright.sync_api import sync_playwright
import pathlib
url="file://"+str(pathlib.Path("jeu.html").resolve())
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page()
    errs=[]; pg.on("pageerror",lambda e:errs.append(str(e)))
    pg.goto(url); pg.wait_for_timeout(300)
    pg.evaluate("()=>{GUIDE_VU=true;}"); pg.click("#start"); pg.wait_for_timeout(300)
    print(pg.evaluate("""()=>{const out=[];
      for(let a=2015;a<=2095;a+=5){ S.year=a; majDates(S); const c=card("A09");
        out.push(a+" -> "+c.n+" | +"+NZ.g+" | "+c.lim.slice(0,60)+"…"); }
      S.year=2015; majDates(S); return out.join("\\n");}"""))
    print("errors:", errs or "none")
    b.close()
