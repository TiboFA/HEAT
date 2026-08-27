from playwright.sync_api import sync_playwright
import pathlib
url="file://"+str(pathlib.Path("jeu.html").resolve())
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={"width":1680,"height":1250},device_scale_factor=2)
    errs=[]
    pg.on("pageerror",lambda e:errs.append("pageerror: "+str(e)))
    pg.on("console",lambda m: errs.append("console: "+m.text) if m.type=="error" else None)
    pg.goto(url); pg.wait_for_timeout(300)
    pg.click('#optLvl .opt[data-v="3"]'); pg.evaluate("()=>{GUIDE_VU=true;}"); pg.click("#start"); pg.wait_for_timeout(400)
    print("lien:", pg.locator("#avenir").text_content())
    pg.click("#avenir"); pg.wait_for_timeout(400)
    pg.locator("#modal").screenshot(path="p_avenir.png")
    print("lignes:", pg.locator("#modal .avl").count())
    # ouvrir la fiche d'un levier fermé
    pg.locator("#modal .avl").first.click(); pg.wait_for_timeout(400)
    print("sous-titre fiche:", pg.locator("#modal .mh .sub").inner_text()[:150])
    pg.locator("#modal").screenshot(path="p_fiche_fermee.png")
    pg.keyboard.press("Escape"); pg.wait_for_timeout(200)
    print("errors:", errs or "none")
    b.close()
