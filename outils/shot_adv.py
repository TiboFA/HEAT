from playwright.sync_api import sync_playwright
import pathlib,sys
NT=int(sys.argv[1]) if len(sys.argv)>1 else 4
url="file://"+str(pathlib.Path("jeu.html").resolve())
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={"width":1720,"height":1250},device_scale_factor=2)
    errs=[]
    pg.on("pageerror",lambda e:errs.append("pageerror: "+str(e)))
    pg.on("console",lambda m: errs.append("console: "+m.text) if m.type=="error" else None)
    def calme():
        for _ in range(80):
            if not pg.evaluate("()=>RESO"): break
            pg.evaluate("()=>{resoStop=true;}")
            pg.wait_for_timeout(120)
        pg.wait_for_timeout(180)
        for _ in range(4):
            if pg.locator("#ovl.open").count():
                pg.evaluate("()=>fermer()"); pg.wait_for_timeout(120)
            else: break
    pg.goto(url); pg.wait_for_timeout(400)
    pg.click('#optLvl .opt[data-v="3"]'); pg.evaluate("()=>{GUIDE_VU=true;}"); pg.click("#start"); pg.wait_for_timeout(400)
    for i in range(NT):
        calme()
        if pg.locator("#fin").is_visible(): break
        for _ in range(3):
            cards=pg.locator('.hand .card:not(.no)')
            if cards.count()==0: break
            cards.first.click(); pg.wait_for_timeout(40)
            tg=pg.locator('.gp.tgt')
            if tg.count(): tg.first.click()
            elif pg.locator('.hint').count(): pg.keyboard.press("Escape")
            pg.wait_for_timeout(40)
        if pg.locator("#battr").count() and pg.locator("#battr").is_enabled(): pg.click("#battr")
        pg.click("#endturn"); pg.wait_for_timeout(300)
        calme()
    calme(); pg.wait_for_timeout(500)
    print("tour:", pg.evaluate("()=>S.turn"), "adv:", pg.evaluate("()=>S.adv.length"))
    pg.screenshot(path="v_adv.png")
    pg.screenshot(path="v_adv_full.png", full_page=True)
    print("errors:", errs or "none")
    b.close()
