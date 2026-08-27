from playwright.sync_api import sync_playwright
import pathlib
url="file://"+str(pathlib.Path("HEAT_jeu_v0.4.html").resolve())
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={"width":1720,"height":1080})
    errs=[]; pg.on("pageerror",lambda e:errs.append(str(e)))
    pg.on("console",lambda m: errs.append(m.text) if m.type=="error" else None)
    pg.goto(url); pg.wait_for_timeout(300)
    pg.click("#start"); pg.wait_for_timeout(300)
    # jouer une carte ciblée sur un bloc pour voir le feedback immédiat
    played=False
    for i in range(7):
        cards=pg.locator('.hand .card:not(.no)')
        if i>=cards.count(): break
        cards.nth(i).click(); pg.wait_for_timeout(100)
        tg=pg.locator('.gp.tgt')
        if tg.count():
            tg.first.click(); played=True; break
        pg.keyboard.press("Escape")
    pg.wait_for_timeout(120)
    print("flottants après un coup :", pg.evaluate("document.querySelectorAll('.flot').length"))
    print("pulses :", pg.evaluate("document.querySelectorAll('.gp.fx').length"))
    pg.click("#endturn")
    tot=0; steps=0; bars=set()
    for _ in range(60):
        pg.wait_for_timeout(250)
        tot=max(tot,pg.evaluate("document.querySelectorAll('.flot').length"))
        steps+= pg.evaluate("document.querySelector('.rsHead')?1:0")
        h=pg.evaluate("[...document.querySelectorAll('.gp .cb i')].map(e=>e.style.height).join(',')")
        bars.add(h)
        if not pg.evaluate("RESO"): break
    print("flottants max pendant résolution :", tot)
    print("ticks avec bandeau :", steps)
    print("états distincts des jauges pendant la résolution :", len(bars))
    print("errors:", errs or "none")
    b.close()
