from playwright.sync_api import sync_playwright
import pathlib
url="file://"+str(pathlib.Path("jeu.html").resolve())
errs=[]
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={"width":1720,"height":1250},device_scale_factor=2)
    pg.on("pageerror",lambda e:errs.append(str(e)))
    pg.goto(url); pg.wait_for_timeout(400)
    pg.click("#start"); pg.wait_for_timeout(1200)
    for i,name in enumerate(["g1","g2","g3","g4","g5","g6","g7","g8"]):
        pg.wait_for_timeout(400)
        pg.screenshot(path=f"g_{name}.png")
        if i<7: pg.click("#gnext"); pg.wait_for_timeout(500)
    print("errs",errs)
    b.close()
