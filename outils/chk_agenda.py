from playwright.sync_api import sync_playwright
import pathlib
url="file://"+str(pathlib.Path("jeu.html").resolve())
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={"width":1680,"height":1250})
    errs=[]; pg.on("pageerror",lambda e:errs.append(str(e)))
    pg.goto(url); pg.wait_for_timeout(300)
    pg.click('#optLvl .opt[data-v="2"]'); pg.evaluate("()=>{GUIDE_VU=true;}"); pg.click("#start"); pg.wait_for_timeout(300)
    # aller au tour 2 (élections) avec un bloc démocratique juste sous 50
    pg.evaluate("""()=>{S.turn=2;S.year=2020;B(S,'eu').percu=44;B(S,'cn').fr=50;
      S.hand=["A51","A01","A05","A02","A17","A20","A40","A11","A04","A10","A19","A12"];
      S.res.actif={cp:20,cap:20,att:5,cred:70}; PV=null; render();}""")
    pg.wait_for_timeout(250)
    ag=lambda: pg.evaluate("()=>[...document.querySelectorAll('#agenda .ag')].map(e=>e.textContent)")
    print("avant :", [x for x in ag() if "lection" in x or "flamme" in x])
    # A51 = mobilisation de masse, perçu +14 sur les trois blocs les plus favorables (mondial)
    pg.locator('.card[data-id="A51"]').first.click(); pg.wait_for_timeout(300)
    print("apres A51 :", [x for x in ag() if "lection" in x or "flamme" in x])
    # A01 sur la Chine : friction +22 -> franchit le seuil
    pg.locator('.card[data-id="A01"]').first.click(); pg.wait_for_timeout(150)
    pg.locator('.gp[data-k="cn"]').first.click(); pg.wait_for_timeout(300)
    print("apres A01 cn :", [x for x in ag() if "flamme" in x])
    # retirer A01 : la menace doit disparaitre
    pg.evaluate("()=>{planRetirer(S.plan.length-1);render();}"); pg.wait_for_timeout(250)
    print("apres retrait :", [x for x in ag() if "flamme" in x])
    print("errors:", errs or "none")
    b.close()
