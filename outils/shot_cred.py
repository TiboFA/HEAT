from playwright.sync_api import sync_playwright
import pathlib
url="file://"+str(pathlib.Path("jeu.html").resolve())
with sync_playwright() as p:
    br=p.chromium.launch(); pg=br.new_page(viewport={"width":1680,"height":1250},device_scale_factor=2)
    errs=[]; pg.on("pageerror",lambda e:errs.append(str(e)))
    pg.goto(url); pg.wait_for_timeout(500)
    pg.click('#optLvl .opt[data-v="2"]'); pg.evaluate("()=>{GUIDE_VU=true;}"); pg.click("#start"); pg.wait_for_timeout(600)
    for lab,ca,cn in (("avance",78,42),("égalité",55,55),("retard",34,71)):
        pg.evaluate(f"()=>{{S.res.actif.cred={ca};S.res.att.cred={cn};render();}}"); pg.wait_for_timeout(250)
        print(lab, pg.evaluate("()=>document.querySelector('#res').textContent.replace(/\\s+/g,' ').slice(-70)"),
              "| vitesse opinion", pg.evaluate("()=>Math.round(vitesseOpinion(S)*100)+' %'"),
              "| pari A01", pg.evaluate("()=>proba(S,card('A01'),B(S,'cn'),'actif')"))
        pg.locator("#res").screenshot(path=f"z_cred_{lab}.png")
    # bilan : la ligne d'écart
    pg.evaluate("""()=>{planAjouter({id:"A01",bk:"cn"});finDeTour();}"""); pg.wait_for_timeout(3500)
    pg.evaluate("()=>{RESO&&(RESO=false);}")
    for _ in range(40):
        if not pg.evaluate("()=>RESO"): break
        pg.wait_for_timeout(200)
    pg.evaluate("()=>bilanTour()"); pg.wait_for_timeout(600)
    txt=pg.evaluate("""()=>[...document.querySelectorAll('.brow')].map(x=>x.textContent.replace(/\\s+/g,' ').trim()).filter(t=>/rédib|cart/.test(t))""")
    print("bilan:",txt)
    print("errors:",errs or "none")
    br.close()
