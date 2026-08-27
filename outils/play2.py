from playwright.sync_api import sync_playwright
import pathlib, sys
url="file://"+str(pathlib.Path("HEAT_jeu_v0.2.html").resolve())
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={"width":1680,"height":1250},device_scale_factor=2)
    errs=[]
    pg.on("pageerror",lambda e:errs.append("pageerror: "+str(e)))
    pg.on("console",lambda m: errs.append("console: "+m.text) if m.type=="error" else None)
    pg.goto(url); pg.wait_for_timeout(500)
    pg.screenshot(path="h_home.png", full_page=True)
    # la difficulté vit désormais dans un <details> replié : on l'ouvre avant de cliquer
    pg.evaluate("()=>document.querySelectorAll('details.hdet').forEach(d=>d.open=true)");
    pg.click('#optLvl .opt[data-v="3"]')
    pg.click("#start"); pg.wait_for_timeout(500)
    pg.screenshot(path="h_turn1.png")
    # jouer une carte sur un bloc
    pg.click('.hand .card:not(.no)'); pg.wait_for_timeout(250)
    pg.screenshot(path="h_sel.png")
    pg.click('.gp:nth-of-type(1)'); pg.wait_for_timeout(300)
    # attribuer si possible
    if pg.locator("#battr").count() and pg.locator("#battr").is_enabled(): pg.click("#battr")
    pg.wait_for_timeout(200)
    # fiche de bloc
    pg.locator('.gp').nth(3).click(); pg.wait_for_timeout(350)
    pg.screenshot(path="h_fiche.png")
    pg.keyboard.press("Escape"); pg.wait_for_timeout(200)
    # fiche levier
    pg.locator('.hand .card .info').first.click(); pg.wait_for_timeout(350)
    pg.screenshot(path="h_levier.png")
    pg.keyboard.press("Escape"); pg.wait_for_timeout(200)
    # ajustement de doctrine
    pg.keyboard.press("Escape"); pg.wait_for_timeout(250)
    pg.click('#docTog'); pg.wait_for_timeout(200)
    sl=pg.locator('#docPanel .dsl').first
    sl.evaluate("e=>{e.value=90;e.dispatchEvent(new Event('change',{bubbles:true}))}")
    pg.wait_for_timeout(300)
    pg.screenshot(path="h_doc.png")
    # dérouler 8 tours
    for i in range(9):
        if pg.locator("#fin").is_visible(): break
        for _ in range(3):
            cards=pg.locator('.hand .card:not(.no)')
            if cards.count()==0: break
            cards.first.click(); pg.wait_for_timeout(60)
            if pg.locator('.hint').count():
                if pg.locator('#jouerg').count(): pg.click('#jouerg')
                else:
                    tg=pg.locator('.gp.tgt')
                    if tg.count(): tg.first.click()
                    else: pg.keyboard.press("Escape")
            pg.wait_for_timeout(60)
        if pg.locator("#battr").count() and pg.locator("#battr").is_enabled(): pg.click("#battr")
        pg.click("#endturn"); pg.wait_for_timeout(220)
    pg.wait_for_timeout(400)
    pg.screenshot(path="h_fin.png", full_page=True)
    print("errors:", errs or "none")
    b.close()
