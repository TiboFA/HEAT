from playwright.sync_api import sync_playwright
import pathlib, json
url="file://"+str(pathlib.Path("jeu.html").resolve())
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={"width":1680,"height":1250},device_scale_factor=2)
    errs=[]
    pg.on("pageerror",lambda e:errs.append("pageerror: "+str(e)))
    pg.on("console",lambda m: errs.append("console: "+m.text) if m.type=="error" else None)
    pg.goto(url); pg.wait_for_timeout(400)
    pg.click('#optLvl .opt[data-v="3"]'); pg.evaluate("()=>{GUIDE_VU=true;}"); pg.click("#start"); pg.wait_for_timeout(400)
    snap=lambda: pg.evaluate("()=>({contr:S.blocs.map(b=>b.contr),cp:S.res[S.camp==='actif'?'actif':'att'].cp,plan:S.plan.length,proj:projeter(S),vproj:projeter(V()),act:V().actions,turn:S.turn,log:S.log.length})")
    a=snap(); print("initial", a)
    # engager 3 leviers
    for i in range(3):
        cards=pg.locator('.hand .card:not(.no)')
        if not cards.count(): break
        cards.first.click(); pg.wait_for_timeout(80)
        if pg.locator('#jouerg').count(): pg.click('#jouerg')
        else:
            tg=pg.locator('.gp.tgt')
            if tg.count(): tg.first.click()
            else: pg.keyboard.press("Escape")
        pg.wait_for_timeout(120)
    if pg.locator("#battr").count() and pg.locator("#battr").is_enabled(): pg.click("#battr")
    pg.wait_for_timeout(200)
    b1=snap(); print("plan  ", b1)
    assert b1["contr"]==a["contr"], "l'etat reel a bouge alors que le tour n'est pas valide !"
    assert b1["cp"]==a["cp"], "les ressources reelles ont bouge !"
    pg.screenshot(path="p_plan.png")
    pg.locator("#plan .pchip").first.hover(); pg.wait_for_timeout(200)
    pg.locator("#plan").screenshot(path="p_bandeau.png")
    # retirer le premier levier
    pg.locator("#plan .px").first.click(); pg.wait_for_timeout(200)
    c=snap(); print("retire", c)
    assert c["plan"]==b1["plan"]-1
    # ctrl+z
    pg.keyboard.press("Control+z"); pg.wait_for_timeout(200)
    d=snap(); print("ctrlz ", d)
    assert d["plan"]==c["plan"]-1
    # tout retirer
    pg.click("#pclear"); pg.wait_for_timeout(200)
    e=snap(); print("vide  ", e)
    assert e["plan"]==0 and e["vproj"]==e["proj"]
    pg.locator("#plan").screenshot(path="p_vide.png")
    # rejouer puis valider
    for i in range(2):
        cards=pg.locator('.hand .card:not(.no)')
        if not cards.count(): break
        cards.first.click(); pg.wait_for_timeout(80)
        if pg.locator('#jouerg').count(): pg.click('#jouerg')
        else:
            tg=pg.locator('.gp.tgt')
            if tg.count(): tg.first.click()
            else: pg.keyboard.press("Escape")
        pg.wait_for_timeout(120)
    f=snap(); print("plan2 ", f)
    pg.screenshot(path="p_avant.png")
    pg.click("#endturn"); pg.wait_for_timeout(600)
    pg.screenshot(path="p_reso.png")
    sk=pg.locator("#rsSkip")
    if sk.count(): sk.click()
    pg.wait_for_timeout(900)
    g=snap(); print("apres ", g)
    assert g["plan"]==0
    assert g["turn"]==2 and g["log"]>a["log"]+20, "la validation n'a rien resolu"
    pg.screenshot(path="p_apres.png")
    print("errors:", errs or "none")
    b.close()
