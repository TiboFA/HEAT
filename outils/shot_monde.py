from playwright.sync_api import sync_playwright
import pathlib
url="file://"+str(pathlib.Path("HEAT_jeu_v0.10.html").resolve())
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={"width":1680,"height":1250},device_scale_factor=2)
    errs=[]
    pg.on("pageerror",lambda e:errs.append("pageerror: "+str(e)))
    pg.on("console",lambda m: errs.append("console: "+m.text) if m.type=="error" else None)
    pg.goto(url); pg.wait_for_timeout(400)
    pg.click('#optLvl .opt[data-v="3"]'); pg.evaluate("()=>{GUIDE_VU=true;}"); pg.click("#start"); pg.wait_for_timeout(400)
    # forcer une main avec un levier mondial jouable (A65 accord multilatéral, cible global)
    pg.evaluate("""()=>{S.hand=["A65","A01","A05","A02","A17","A20","A40","A11","A04","A10","A19","A12"];render();}""")
    pg.wait_for_timeout(200)
    print("plan avant:", pg.evaluate("()=>S.plan.length"))
    pg.locator('.card[data-id="A65"]').first.click(); pg.wait_for_timeout(300)
    print("plan apres 1 clic:", pg.evaluate("()=>S.plan.map(e=>e.id||e.k)"))
    print("hint present:", pg.locator('.hint').count())
    print("sel:", pg.evaluate("()=>sel"))
    pg.locator("#plan").screenshot(path="m_plan.png")
    # une carte de bloc garde bien l'étape de ciblage
    pg.locator('.card[data-id="A01"]').first.click(); pg.wait_for_timeout(250)
    print("sel apres carte bloc:", pg.evaluate("()=>sel"), "hint:", pg.locator('.hint').count())
    pg.locator('.sideL').screenshot(path="m_hint.png")
    tg=pg.locator('.gp.tgt')
    if tg.count(): tg.first.click()
    pg.wait_for_timeout(250)
    print("plan final:", pg.evaluate("()=>S.plan.map(e=>e.id||e.k)"))
    # retirer le levier mondial
    pg.locator("#plan .px").first.click(); pg.wait_for_timeout(200)
    print("apres retrait:", pg.evaluate("()=>S.plan.map(e=>e.id||e.k)"), "en main:", pg.evaluate("()=>V().hand.includes('A65')"))
    print("errors:", errs or "none")
    b.close()
