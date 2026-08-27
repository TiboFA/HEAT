from playwright.sync_api import sync_playwright
import pathlib
url="file://"+str(pathlib.Path("jeu.html").resolve())
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={"width":1680,"height":1250},device_scale_factor=2)
    errs=[]
    pg.on("pageerror",lambda e:errs.append("pageerror: "+str(e)))
    pg.on("console",lambda m: errs.append("console: "+m.text) if m.type=="error" else None)
    pg.goto(url); pg.wait_for_timeout(400)
    # la difficulté vit désormais dans un <details> replié : on l'ouvre avant de cliquer
    pg.evaluate("()=>document.querySelectorAll('details.hdet').forEach(d=>d.open=true)");
    pg.click('#optLvl .opt[data-v="3"]'); pg.evaluate("()=>{GUIDE_VU=true;}"); pg.click("#start"); pg.wait_for_timeout(400)
    print("tour1:", pg.evaluate("()=>[...document.querySelectorAll('#agenda .ag')].map(e=>e.textContent)"))
    pg.locator("#agenda").screenshot(path="a_t1.png")
    def tour():
        if pg.locator("#ovl.open").count(): pg.click("#bok"); pg.wait_for_timeout(200)
        for _ in range(3):
            c=pg.locator('.hand .card:not(.no)')
            if not c.count(): break
            c.first.click(); pg.wait_for_timeout(60)
            tg=pg.locator('.gp.tgt')
            if tg.count(): tg.first.click()
            elif pg.locator('.hint').count(): pg.keyboard.press("Escape")
            pg.wait_for_timeout(60)
        if pg.locator("#battr").count() and pg.locator("#battr").is_enabled(): pg.click("#battr")
        pg.click("#endturn"); pg.wait_for_timeout(400)
        sk=pg.locator("#rsSkip")
        if sk.count(): sk.click()
        pg.wait_for_timeout(900)
    tour()
    if pg.locator("#ovl.open").count(): pg.click("#bok"); pg.wait_for_timeout(250)
    print("tour2 (elections):", pg.evaluate("()=>[...document.querySelectorAll('#agenda .ag')].map(e=>e.textContent)"))
    pg.locator("#agenda").screenshot(path="a_t2.png")
    # forcer des mécanismes installés pour couvrir tous les cas
    pg.evaluate("""()=>{const b=B(S,'cn');b.suivi=1;b.revoyure=1;b.fr=62;b.pend=[{v:9,t:1,src:'A05'}];
      const e=B(S,'eu');e.media=1;e.bloque=1;
      S.cliquet=1;S.tech=42;S.pubOff=2;S.avis=1;S.techPend=[{v:6,t:1}];render();}""")
    pg.wait_for_timeout(300)
    print("complet:", pg.evaluate("()=>document.querySelectorAll('#agenda .ag').length"))
    pg.locator("#agenda").screenshot(path="a_full.png")
    pg.locator("#agenda .ag").nth(2).hover(); pg.wait_for_timeout(400)
    pg.screenshot(path="a_tip.png", clip={"x":0,"y":0,"width":1680,"height":520})
    print("errors:", errs or "none")
    b.close()
