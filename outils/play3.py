from playwright.sync_api import sync_playwright
import pathlib
NT=17
url="file://"+str(pathlib.Path("HEAT_jeu_v0.11.html").resolve())
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={"width":1680,"height":1250},device_scale_factor=2)
    errs=[]
    pg.on("pageerror",lambda e:errs.append("pageerror: "+str(e)))
    pg.on("console",lambda m: errs.append("console: "+m.text) if m.type=="error" else None)
    def calme():
        for _ in range(60):
            if not pg.evaluate("()=>RESO"): break
            pg.wait_for_timeout(150)
        pg.wait_for_timeout(200)
        for _ in range(4):
            if pg.locator("#ovl.open").count():
                pg.evaluate("()=>fermer()"); pg.wait_for_timeout(150)
            else: break
    ferme=calme
    pg.goto(url); pg.wait_for_timeout(500)
    pg.screenshot(path="i_home.png", full_page=True)
    pg.click('#optLvl .opt[data-v="3"]'); pg.evaluate("()=>{GUIDE_VU=true;}"); pg.click("#start"); pg.wait_for_timeout(500)
    pg.screenshot(path="i_turn1.png")
    pg.click('.hand .card:not(.no)'); pg.wait_for_timeout(250)
    pg.screenshot(path="i_sel.png")
    pg.locator('.gp').first.click(); pg.wait_for_timeout(300)
    # si le levier sélectionné était mondial, le clic sur un bloc a ouvert sa fiche :
    # elle recouvre le bandeau d'événement et bloquerait le clic suivant
    ferme()
    if pg.locator("#battr").count() and pg.locator("#battr").is_enabled() and pg.locator("#battr").is_visible():
        pg.click("#battr", timeout=5000)
    pg.wait_for_timeout(200)
    pg.locator('.gp').nth(3).click(); pg.wait_for_timeout(350)
    pg.screenshot(path="i_fiche.png"); ferme()
    pg.locator('.hand .card .info').first.click(); pg.wait_for_timeout(350)
    pg.screenshot(path="i_levier.png"); ferme()
    pg.click('#docTog'); pg.wait_for_timeout(200)
    pg.locator('#docPanel .dsl').first.evaluate("e=>{e.value=90;e.dispatchEvent(new Event('change',{bubbles:true}))}")
    pg.wait_for_timeout(300); pg.screenshot(path="i_doc.png")
    for i in range(NT+2):
        ferme()
        if pg.locator("#fin").is_visible(): break
        for _ in range(3):
            cards=pg.locator('.hand .card:not(.no)')
            if cards.count()==0: break
            cards.first.click(); pg.wait_for_timeout(50)
            tg=pg.locator('.gp.tgt')
            if tg.count(): tg.first.click()
            elif pg.locator('.hint').count(): pg.keyboard.press("Escape")
            pg.wait_for_timeout(50)
        if pg.locator("#battr").count() and pg.locator("#battr").is_enabled(): pg.click("#battr")
        pg.click("#endturn"); pg.wait_for_timeout(350)
        sk=pg.locator("#rsSkip")
        if sk.count(): sk.click()
        calme()
    ferme(); pg.wait_for_timeout(800)
    print("tour final:", pg.evaluate("()=>S.turn"), "over:", pg.evaluate("()=>S.over"))
    pg.screenshot(path="i_fin.png", full_page=True)
    print("errors:", errs or "none")
    b.close()
