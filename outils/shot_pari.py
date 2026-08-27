from playwright.sync_api import sync_playwright
import pathlib
url="file://"+str(pathlib.Path("HEAT_jeu_v0.4.html").resolve())
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={"width":1680,"height":1250},device_scale_factor=2)
    errs=[]
    pg.on("pageerror",lambda e:errs.append("pageerror: "+str(e)))
    pg.on("console",lambda m: errs.append("console: "+m.text) if m.type=="error" else None)
    pg.goto(url); pg.wait_for_timeout(400)
    pg.click('#optLvl .opt[data-v="2"]'); pg.click("#start"); pg.wait_for_timeout(400)
    # forcer une main contenant deux paris et un combo connu
    pg.evaluate("""()=>{ S.hand=["A01","A31","A33","A05","A02","A17","A20","A40","A11","A04","A10","A19"]; render(); }""")
    pg.wait_for_timeout(200)
    # jouer A01 puis A31 (combo « Le chèque avec la taxe »)
    for cid in ["A01","A31"]:
        el=pg.locator(f'.card[data-id="{cid}"]')
        if not el.count(): print("absent",cid); continue
        el.first.click(); pg.wait_for_timeout(120)
        if pg.locator('#jouerg').count(): pg.click('#jouerg')
        else:
            tg=pg.locator('.gp.tgt')
            if tg.count(): tg.first.click()
            else: pg.keyboard.press("Escape")
        pg.wait_for_timeout(150)
    pg.locator("#plan").screenshot(path="p_pari.png")
    print(pg.evaluate("()=>S.plan.map(e=>e.id||e.k)"))
    # rendre un levier injouable : vider les ressources
    pg.evaluate("()=>{S.res.actif.cap=0;S.res.actif.cp=0;simuler();render();}")
    pg.wait_for_timeout(200)
    pg.locator("#plan").screenshot(path="p_ko.png")
    print("ko:",pg.evaluate("()=>S.plan.map(e=>e.ko)"))
    pg.click("#endturn"); pg.wait_for_timeout(500)
    print("bloque a la validation:", pg.evaluate("()=>S.turn"))
    print("errors:", errs or "none")
    b.close()
