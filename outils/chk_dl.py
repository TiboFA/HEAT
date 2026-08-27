from playwright.sync_api import sync_playwright
import pathlib
url="file://"+str(pathlib.Path("HEAT_jeu_v0.10.html").resolve())
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={"width":1680,"height":1250})
    pg.goto(url); pg.wait_for_timeout(300)
    pg.click('#optLvl .opt[data-v="3"]'); pg.evaluate("()=>{GUIDE_VU=true;}"); pg.click("#start"); pg.wait_for_timeout(300)
    for _ in range(3):
        c=pg.locator('.hand .card:not(.no)')
        if not c.count(): break
        c.first.click(); pg.wait_for_timeout(50)
        if pg.locator('#jouerg').count(): pg.click('#jouerg')
        else:
            tg=pg.locator('.gp.tgt')
            if tg.count(): tg.first.click()
            else: pg.keyboard.press("Escape")
        pg.wait_for_timeout(50)
    pg.click("#endturn"); pg.wait_for_timeout(300)
    sk=pg.locator("#rsSkip")
    if sk.count(): sk.click()
    pg.wait_for_timeout(900)
    print(pg.evaluate("""()=>[...document.querySelectorAll('.btr')].slice(0,3).map(tr=>
      [...tr.querySelectorAll('.bg')].map(g=>{
        const d=g.querySelector('.dl');
        return g.className.replace('bg ','')+':'+(d?d.className.replace('dl ','')+' '+d.textContent+' '+getComputedStyle(d).color:'—');
      }))"""))
    b.close()
