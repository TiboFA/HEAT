from playwright.sync_api import sync_playwright
import pathlib,os,tempfile
url="file://"+str(pathlib.Path("HEAT_jeu_v0.10.html").resolve())
with sync_playwright() as p:
    b=p.chromium.launch(); ctx=b.new_context(accept_downloads=True); pg=ctx.new_page()
    errs=[]; pg.on("pageerror",lambda e:errs.append(str(e)))
    pg.goto(url); pg.wait_for_timeout(300)
    pg.evaluate("()=>{GUIDE_VU=true;}"); pg.click("#start"); pg.wait_for_timeout(300)
    pg.evaluate("()=>{S.turn=6;S.year=2040;S.T=1.77;render();}")
    pg.click("#ouvrirPartie"); pg.wait_for_timeout(300)
    with pg.expect_download() as d:
        pg.click("#pexp")
    dl=d.value; path=os.path.join(tempfile.gettempdir(),"partie.json"); dl.save_as(path)
    print("fichier:",dl.suggested_filename, os.path.getsize(path),"octets")
    pg.evaluate("()=>fermer()")
    # on casse la partie puis on recharge le fichier
    pg.evaluate("()=>{S.turn=1;S.T=1.0;render();}")
    pg.click("#ouvrirPartie"); pg.wait_for_timeout(200)
    with pg.expect_file_chooser() as fc:
        pg.click("#pimp")
    fc.value.set_files(path); pg.wait_for_timeout(600)
    print("après import — tour:",pg.evaluate("()=>S.turn"),"T:",pg.evaluate("()=>S.T"))
    # fichier invalide
    bad=os.path.join(tempfile.gettempdir(),"bad.json"); open(bad,"w").write('{"v":"0.1","etat":{}}')
    pg.click("#ouvrirPartie"); pg.wait_for_timeout(200)
    with pg.expect_file_chooser() as fc:
        pg.click("#pimp")
    fc.value.set_files(bad); pg.wait_for_timeout(500)
    print("message d'erreur:", pg.locator("#modal .gx").first.inner_text()[:110])
    print("tour intact:", pg.evaluate("()=>S.turn"))
    print("erreurs:", errs or "none")
    b.close()
