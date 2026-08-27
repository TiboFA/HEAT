from playwright.sync_api import sync_playwright
import pathlib
url="file://"+str(pathlib.Path("jeu.html").resolve())
with sync_playwright() as p:
    br=p.chromium.launch(); pg=br.new_page(viewport={"width":1680,"height":1250},device_scale_factor=2)
    errs=[]; pg.on("pageerror",lambda e:errs.append(str(e)))
    pg.goto(url); pg.wait_for_timeout(500)
    # la difficulté vit désormais dans un <details> replié : on l'ouvre avant de cliquer
    pg.evaluate("()=>document.querySelectorAll('details.hdet').forEach(d=>d.open=true)");
    pg.click('#optLvl .opt[data-v="2"]'); pg.evaluate("()=>{GUIDE_VU=true;}"); pg.click("#start"); pg.wait_for_timeout(600)
    pg.evaluate("""()=>{ S.hand=["A67","A02","A50","A33","A65","A01","A53","A12","A39","A31","A57","A61"]; render(); }""")
    pg.wait_for_timeout(400)
    pg.locator("#handCtl").screenshot(path="z_pds_main.png")
    print(pg.evaluate("""()=>({lourds:document.querySelectorAll('.tag.lourd').length,
        legers:[...document.querySelectorAll('.tag')].filter(x=>x.textContent==='1 action').length,
        btn:document.querySelector('#endturn').textContent})"""))
    pg.evaluate("()=>ficheLevier('A67')"); pg.wait_for_timeout(500)
    pg.screenshot(path="z_pds_fiche.png")
    print(pg.evaluate("""()=>[...document.querySelectorAll('.fl-kv')].slice(0,3).map(x=>x.textContent.trim())"""))
    pg.evaluate("""()=>{fermer(); planVider(); planAjouter({id:"A67",bk:null}); planAjouter({id:"A65",bk:null}); planAjouter({id:"A01",bk:"cn"}); render();}""")
    pg.wait_for_timeout(400)
    print(pg.evaluate("""()=>({plan:document.querySelector('.pt').textContent, btn:document.querySelector('#endturn').textContent,
        ko:S.plan.map(e=>e.id+" → "+(e.ko||"ok")), reste:V().actions})"""))
    pg.locator(".plan").screenshot(path="z_pds_plan.png")
    print("errors:",errs or "none")
    br.close()
