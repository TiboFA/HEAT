from playwright.sync_api import sync_playwright
import pathlib
url="file://"+str(pathlib.Path("jeu.html").resolve())
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={"width":1720,"height":1180},device_scale_factor=2)
    pg.goto(url); pg.wait_for_timeout(400)
    # la difficulté vit désormais dans un <details> replié : on l'ouvre avant de cliquer
    pg.evaluate("()=>document.querySelectorAll('details.hdet').forEach(d=>d.open=true)");
    pg.click('#optLvl .opt[data-v="3"]'); pg.evaluate("()=>{GUIDE_VU=true;}"); pg.click("#start"); pg.wait_for_timeout(400)
    pg.evaluate("""()=>{S.turn=2;S.year=2020;S.defi=DEFIS.find(d=>d.t==="Refermer l'écart");
      B(S,'cn').contr=22;B(S,'cn').fr=41;B(S,'eu').percu=47;S.tech=18;PV=null;render();}""")
    pg.wait_for_timeout(300)
    pg.screenshot(path="c_board.png")
    b.close()
