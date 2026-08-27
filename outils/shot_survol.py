from playwright.sync_api import sync_playwright
import pathlib
url="file://"+str(pathlib.Path("jeu.html").resolve())
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={"width":1680,"height":1250},device_scale_factor=2)
    errs=[]
    pg.on("pageerror",lambda e:errs.append("pageerror: "+str(e)))
    pg.on("console",lambda m: errs.append("console: "+m.text) if m.type=="error" else None)
    pg.goto(url); pg.wait_for_timeout(300)
    # la difficulté vit désormais dans un <details> replié : on l'ouvre avant de cliquer
    pg.evaluate("()=>document.querySelectorAll('details.hdet').forEach(d=>d.open=true)");
    pg.click('#optLvl .opt[data-v="2"]'); pg.evaluate("()=>{GUIDE_VU=true;}"); pg.click("#start"); pg.wait_for_timeout(300)
    pg.evaluate("""()=>{S.turn=11;S.year=2065;S.hist=[];
      const v=[3.48,3.31,3.12,2.97,2.85,2.76,2.70,2.66,2.63,2.61,2.60];
      v.forEach((p,i)=>S.hist.push({p,g:GHOST[i]}));PV=null;render();}""")
    pg.wait_for_timeout(300)
    n=pg.locator('#traj .trg .tp').count()
    print("colonnes sensibles:", n)
    for i in (3,10):
        pg.locator('#traj .trg .tp rect').nth(i).hover(); pg.wait_for_timeout(350)
        print(i, "tooltip:", pg.evaluate("()=>document.querySelector('#tip').innerText.replace(/\\n/g,' | ')"))
        pg.screenshot(path=f"s_traj_{i}.png", clip={"x":360,"y":700,"width":1320,"height":420})
    print("errors:", errs or "none")
    b.close()
