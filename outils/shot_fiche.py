from playwright.sync_api import sync_playwright
import pathlib
url="file://"+str(pathlib.Path("HEAT_jeu_v0.10.html").resolve())
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={"width":1720,"height":1150},device_scale_factor=2)
    errs=[]; pg.on("pageerror",lambda e:errs.append(str(e)))
    pg.on("console",lambda m: errs.append(m.text) if m.type=="error" else None)
    pg.goto(url); pg.wait_for_timeout(400)
    pg.evaluate("()=>{GUIDE_VU=true;}"); pg.click("#start"); pg.wait_for_timeout(400)
    # fiche d'un levier de bloc
    n=pg.locator('.hand .card .info').count()
    for i in range(min(n,3)):
        pg.locator('.hand .card .info').nth(i).click(); pg.wait_for_timeout(400)
        pg.locator("#modal").screenshot(path=f"f_fiche{i}.png")
        pg.keyboard.press("Escape"); pg.wait_for_timeout(200)
    print("fiches capturées:", min(n,3))
    print("errors:", errs or "none")
    b.close()
