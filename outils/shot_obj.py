from playwright.sync_api import sync_playwright
import pathlib
url="file://"+str(pathlib.Path("jeu.html").resolve())
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={"width":1680,"height":1250},device_scale_factor=2)
    errs=[]
    pg.on("pageerror",lambda e:errs.append("pageerror: "+str(e)))
    pg.on("console",lambda m: errs.append("console: "+m.text) if m.type=="error" else None)
    pg.goto(url); pg.wait_for_timeout(400)
    pg.locator("#home").screenshot(path="o_home.png")
    pg.click('#optLvl .opt[data-v="2"]'); pg.evaluate("()=>{GUIDE_VU=true;}"); pg.click("#start"); pg.wait_for_timeout(400)
    pg.locator('#events').screenshot(path="o_t1.png")
    # milieu de partie : pic passé, seuil pas encore
    pg.evaluate("""()=>{S.turn=9;S.year=2055;S.picE=39.8;S.picAn=2040;
      S.blocs.forEach(b=>b.e*=0.75);S.cum=1400;PV=null;render();}""")
    pg.wait_for_timeout(250); pg.locator('#events').screenshot(path="o_mid.png")
    # seuil franchi
    pg.evaluate("""()=>{S.blocs.forEach(b=>b.e*=0.62);S.seuilAn=2080;S.turn=14;S.year=2080;PV=null;render();}""")
    pg.wait_for_timeout(250); pg.locator('#events').screenshot(path="o_ok.png")
    print("errors:", errs or "none")
    b.close()
