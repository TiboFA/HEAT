from playwright.sync_api import sync_playwright
import pathlib
url="file://"+str(pathlib.Path("HEAT_jeu_v0.10.html").resolve())
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={"width":1720,"height":1080},device_scale_factor=2)
    errs=[]; pg.on("pageerror",lambda e:errs.append(str(e)))
    pg.on("console",lambda m: errs.append(m.text) if m.type=="error" else None)
    pg.goto(url); pg.wait_for_timeout(400)
    pg.click('#optLvl .opt[data-v="2"]'); pg.evaluate("()=>{GUIDE_VU=true;}"); pg.click("#start"); pg.wait_for_timeout(400)
    # jouer trois cartes
    for _ in range(3):
        cards=pg.locator('.hand .card:not(.no)')
        if not cards.count(): break
        cards.first.click(); pg.wait_for_timeout(120)
        if pg.locator('.hint').count():
            if pg.locator('#jouerg').count(): pg.click('#jouerg')
            else:
                tg=pg.locator('.gp.tgt')
                if tg.count(): tg.first.click()
                else: pg.keyboard.press("Escape")
        pg.wait_for_timeout(200)
    pg.screenshot(path="r_apres_coups.png", full_page=True)
    pg.click("#endturn")
    for i,t in enumerate([700,1500,2600,4200,6000]):
        pg.wait_for_timeout(t if i==0 else t-[700,1500,2600,4200,6000][i-1])
        pg.screenshot(path=f"r_reso{i}.png")
    pg.wait_for_timeout(9000)
    pg.screenshot(path="r_fin_tour.png")
    print("errors:", errs or "none")
    b.close()
