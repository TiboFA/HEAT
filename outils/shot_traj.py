from playwright.sync_api import sync_playwright
import pathlib
url="file://"+str(pathlib.Path("jeu.html").resolve())
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={"width":1680,"height":1250},device_scale_factor=2)
    pg.goto(url); pg.wait_for_timeout(300)
    # la difficulté vit désormais dans un <details> replié : on l'ouvre avant de cliquer
    pg.evaluate("()=>document.querySelectorAll('details.hdet').forEach(d=>d.open=true)");
    pg.click('#optLvl .opt[data-v="2"]'); pg.evaluate("()=>{GUIDE_VU=true;}"); pg.click("#start"); pg.wait_for_timeout(300)
    # remplir l'historique comme après une dizaine de tours
    pg.evaluate("""()=>{S.turn=11;S.year=2065;S.hist=[];
      const v=[3.48,3.31,3.12,2.97,2.85,2.76,2.70,2.66,2.63,2.61,2.60];
      v.forEach((p,i)=>S.hist.push({p,g:GHOST[i]}));
      B(S,'cn').contr=45;B(S,'eu').contr=60;PV=null;render();}""")
    pg.wait_for_timeout(300)
    pg.locator('.traj').screenshot(path="t_traj.png")
    b.close()
