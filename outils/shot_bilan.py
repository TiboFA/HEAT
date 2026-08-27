from playwright.sync_api import sync_playwright
import pathlib
url="file://"+str(pathlib.Path("jeu.html").resolve())
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={"width":1680,"height":1250},device_scale_factor=2)
    errs=[]
    pg.on("pageerror",lambda e:errs.append("pageerror: "+str(e)))
    pg.on("console",lambda m: errs.append("console: "+m.text) if m.type=="error" else None)
    pg.goto(url); pg.wait_for_timeout(400)
    # la difficulté vit désormais dans un <details> replié : on l'ouvre avant de cliquer
    pg.evaluate("()=>document.querySelectorAll('details.hdet').forEach(d=>d.open=true)");
    pg.click('#optLvl .opt[data-v="3"]'); pg.evaluate("()=>{GUIDE_VU=true;}"); pg.click("#start"); pg.wait_for_timeout(400)
    def tour():
        if pg.locator("#ovl.open").count(): pg.click("#bok"); pg.wait_for_timeout(200)
        for _ in range(3):
            c=pg.locator('.hand .card:not(.no)')
            if not c.count(): break
            c.first.click(); pg.wait_for_timeout(60)
            if pg.locator('#jouerg').count(): pg.click('#jouerg')
            else:
                tg=pg.locator('.gp.tgt')
                if tg.count(): tg.first.click()
                else: pg.keyboard.press("Escape")
            pg.wait_for_timeout(60)
        if pg.locator("#battr").count() and pg.locator("#battr").is_enabled(): pg.click("#battr")
        pg.click("#endturn"); pg.wait_for_timeout(400)
        sk=pg.locator("#rsSkip")
        if sk.count(): sk.click()
        pg.wait_for_timeout(900)
    tour(); tour()
    print("ouvert:", pg.locator("#ovl.open").count()==1)
    pg.locator("#modal").screenshot(path="b_bilan.png")
    pg.click("#bjTog"); pg.wait_for_timeout(250)
    print("essentiel:", pg.evaluate("()=>document.querySelectorAll('#bjour > *').length"))
    pg.click("#bjTog"); pg.wait_for_timeout(250)
    print("tout:", pg.evaluate("()=>document.querySelectorAll('#bjour > *').length"))
    # decocher l'auto puis verifier qu'il ne s'ouvre plus
    pg.uncheck("#bauto"); pg.click("#bok"); pg.wait_for_timeout(250)
    print("ferme:", pg.locator("#ovl.open").count()==0)
    print("lien present:", pg.locator("#revoirBilan").count()==1)
    tour()
    print("auto off -> ferme:", pg.locator("#ovl.open").count()==0)
    pg.click("#revoirBilan"); pg.wait_for_timeout(300)
    print("reouvert:", pg.locator("#ovl.open").count()==1)
    pg.locator("#modal").screenshot(path="b_bilan2.png")
    pg.keyboard.press("Escape"); pg.wait_for_timeout(200)
    print("errors:", errs or "none")
    b.close()
