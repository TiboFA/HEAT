from playwright.sync_api import sync_playwright
import pathlib
url="file://"+str(pathlib.Path("jeu.html").resolve())
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={"width":1720,"height":1250},device_scale_factor=2)
    errs=[]; pg.on("pageerror",lambda e:errs.append(str(e)))
    def calme():
        for _ in range(80):
            if not pg.evaluate("()=>RESO"): break
            pg.evaluate("()=>{resoStop=true;}"); pg.wait_for_timeout(120)
        pg.wait_for_timeout(150)
        for _ in range(4):
            if pg.locator("#ovl.open").count(): pg.evaluate("()=>fermer()"); pg.wait_for_timeout(120)
            else: break
    pg.goto(url); pg.wait_for_timeout(400)
    pg.click('#optCamp .opt[data-v="att"]'); pg.click('#optLvl .opt[data-v="3"]')
    pg.evaluate("()=>{GUIDE_VU=true;}"); pg.click("#start"); pg.wait_for_timeout(400)
    for i in range(5):
        calme()
        for _ in range(3):
            c=pg.locator('.hand .card:not(.no)')
            if c.count()==0: break
            c.first.click(); pg.wait_for_timeout(40)
            tg=pg.locator('.gp.tgt')
            if tg.count(): tg.first.click()
            elif pg.locator('.hint').count(): pg.keyboard.press("Escape")
            pg.wait_for_timeout(40)
        pg.click("#endturn"); pg.wait_for_timeout(250); calme()
    calme(); pg.wait_for_timeout(400)
    pg.screenshot(path="v_att.png")
    print("erreurs:", errs or "none")
    b.close()
