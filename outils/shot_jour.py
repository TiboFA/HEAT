from playwright.sync_api import sync_playwright
import pathlib
url="file://"+str(pathlib.Path("HEAT_jeu_v0.10.html").resolve())
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={"width":1680,"height":1250},device_scale_factor=2)
    errs=[]
    pg.on("pageerror",lambda e:errs.append("pageerror: "+str(e)))
    pg.on("console",lambda m: errs.append("console: "+m.text) if m.type=="error" else None)
    pg.goto(url); pg.wait_for_timeout(400)
    pg.click('#optLvl .opt[data-v="3"]'); pg.evaluate("()=>{GUIDE_VU=true;}"); pg.click("#start"); pg.wait_for_timeout(400)
    for tour in range(3):
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
        pg.wait_for_timeout(700)
    print("entrees:", pg.evaluate("()=>S.log.length"))
    # vue essentiel (defaut)
    pg.locator("#jour").scroll_into_view_if_needed(); pg.wait_for_timeout(200)
    pg.locator(".sideR").screenshot(path="j_essentiel.png")
    pg.click("#jourTog"); pg.wait_for_timeout(300)
    print("visibles tout:", pg.evaluate("()=>document.querySelectorAll('#jour > *').length"))
    pg.evaluate("()=>{const j=document.querySelector('#jour'); j.style.maxHeight='2000px';}")
    pg.wait_for_timeout(200)
    pg.locator("#jour").screenshot(path="j_tout.png")
    print("errors:", errs or "none")
    b.close()
