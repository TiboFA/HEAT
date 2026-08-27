from playwright.sync_api import sync_playwright
import pathlib
url="file://"+str(pathlib.Path("HEAT_jeu_v0.10.html").resolve())
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={"width":1680,"height":1250},device_scale_factor=3)
    pg.goto(url); pg.wait_for_timeout(300)
    pg.click('#optLvl .opt[data-v="3"]'); pg.evaluate("()=>{GUIDE_VU=true;}"); pg.click("#start"); pg.wait_for_timeout(300)
    pg.locator('.ev.defi').screenshot(path="c_defi_zoom.png")
    print(pg.evaluate("""()=>{const d=document.querySelector('.ev.defi');
      return [...d.children].map(c=>c.tagName+'.'+c.className+' | border:'+getComputedStyle(c).border);}"""))
    # avancer un peu pour voir une jauge remplie
    pg.evaluate("()=>{S.blocs[0].contr=18;S.blocs[1].contr=9;render();}"); pg.wait_for_timeout(300)
    pg.locator('.ev.defi').screenshot(path="c_defi_mid.png")
    pg.evaluate("()=>{S.blocs[1].contr=20;render();}"); pg.wait_for_timeout(300)
    pg.locator('.ev.defi').screenshot(path="c_defi_ok.png")
    # un défi « tenir »
    pg.evaluate("""()=>{S.defi=DEFIS.find(d=>d.t==="Tenir la rue");S.blocs[0].fr=30;render();}"""); pg.wait_for_timeout(250)
    pg.locator('.ev.defi').screenshot(path="c_defi_tenir.png")
    pg.evaluate("()=>{S.blocs[0].fr=52;render();}"); pg.wait_for_timeout(250)
    pg.locator('.ev.defi').screenshot(path="c_defi_rate.png")
    b.close()
