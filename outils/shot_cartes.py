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
    pg.evaluate("""()=>{S.hand=["A01","A65","A33","A05","A51","A12","A20","A40","A11","A63","A19","A02"];
      S.res.actif={cp:20,cap:20,att:5,cred:70};PV=null;render();}""")
    pg.wait_for_timeout(300)
    pg.locator('#handL').screenshot(path="c_gauche.png")
    pg.locator('#events').screenshot(path="c_defi.png")
    print("scopes:", pg.evaluate("()=>[...document.querySelectorAll('.card .scope')].map(e=>e.textContent).slice(0,8)"))
    print("paris:", pg.evaluate("()=>[...document.querySelectorAll('.card .tag.pari')].map(e=>e.textContent)"))
    print("errors:", errs or "none")
    b.close()
