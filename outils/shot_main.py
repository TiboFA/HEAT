from playwright.sync_api import sync_playwright
import pathlib
url="file://"+str(pathlib.Path("jeu.html").resolve())
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={"width":1720,"height":1250},device_scale_factor=2)
    errs=[]; pg.on("pageerror",lambda e:errs.append(str(e)))
    pg.on("console",lambda m: errs.append(m.text) if m.type=="error" else None)
    pg.goto(url); pg.wait_for_timeout(400)
    pg.evaluate("()=>{GUIDE_VU=true;}"); pg.click("#start"); pg.wait_for_timeout(500)
    print("cartes en main :", pg.locator('.hand .card').count())
    pg.screenshot(path="m_main.png")
    # tester la repioche
    ids_av=pg.evaluate("S.hand.join(',')")
    pg.click("#redraw"); pg.wait_for_timeout(400)
    ids_ap=pg.evaluate("S.hand.join(',')")
    print("repioche : ", len(set(ids_av.split(','))&set(ids_ap.split(','))), "cartes communes sur", pg.locator('.hand .card').count())
    print("attention restante :", pg.evaluate("S.res[S.camp==='actif'?'actif':'att'].att"))
    pg.screenshot(path="m_redraw.png")
    print("errors:", errs or "none")
    b.close()
