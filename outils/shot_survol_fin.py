from playwright.sync_api import sync_playwright
import pathlib
url="file://"+str(pathlib.Path("HEAT_jeu_v0.10.html").resolve())
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={"width":1680,"height":1250},device_scale_factor=2)
    errs=[]
    pg.on("pageerror",lambda e:errs.append("pageerror: "+str(e)))
    pg.on("console",lambda m: errs.append("console: "+m.text) if m.type=="error" else None)
    pg.goto(url); pg.wait_for_timeout(300)
    pg.click('#optLvl .opt[data-v="2"]'); pg.evaluate("()=>{GUIDE_VU=true;}"); pg.click("#start"); pg.wait_for_timeout(300)
    pg.evaluate("""()=>{S.hist=[];
      for(let i=0;i<=NTURNS;i++) S.hist.push({p:+(3.48-1.0*i/NTURNS).toFixed(2),g:GHOST[i]});
      S.over=true;S.turn=NTURNS+1;renderFin();}""")
    pg.wait_for_timeout(400)
    print("colonnes:", pg.locator('#fin .trg .tp').count())
    pg.locator('#fin .trg .tp rect').nth(17).hover(); pg.wait_for_timeout(350)
    print("tooltip:", pg.evaluate("()=>document.querySelector('#tip').innerText.replace(/\\n/g,' | ')"))
    pg.locator('#fin .trg .tp rect').nth(6).hover(); pg.wait_for_timeout(350)
    print("tooltip:", pg.evaluate("()=>document.querySelector('#tip').innerText.replace(/\\n/g,' | ')"))
    pg.screenshot(path="s_fin.png", clip={"x":420,"y":100,"width":1200,"height":560})
    print("errors:", errs or "none")
    b.close()
