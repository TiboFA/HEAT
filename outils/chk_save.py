from playwright.sync_api import sync_playwright
import pathlib,json
url="file://"+str(pathlib.Path("jeu.html").resolve())
with sync_playwright() as p:
    b=p.chromium.launch(); ctx=b.new_context(); pg=ctx.new_page()
    errs=[]
    pg.on("pageerror",lambda e:errs.append("pageerror: "+str(e)))
    pg.on("console",lambda m: errs.append("console: "+m.text) if m.type=="error" else None)
    def calme():
        for _ in range(80):
            if not pg.evaluate("()=>RESO"): break
            pg.evaluate("()=>{resoStop=true;}"); pg.wait_for_timeout(120)
        pg.wait_for_timeout(150)
        for _ in range(4):
            if pg.locator("#ovl.open").count(): pg.evaluate("()=>fermer()"); pg.wait_for_timeout(120)
            else: break
    pg.goto(url); pg.wait_for_timeout(400)
    print("bandeau vide visible:", pg.locator("#reprise .rpz.vide").count()==1)
    # la difficulté vit désormais dans un <details> replié : on l'ouvre avant de cliquer
    pg.evaluate("()=>document.querySelectorAll('details.hdet').forEach(d=>d.open=true)");
    pg.click('#optLvl .opt[data-v="3"]'); pg.evaluate("()=>{GUIDE_VU=true;}"); pg.click("#start"); pg.wait_for_timeout(400)
    for i in range(4):
        calme()
        for _ in range(3):
            c=pg.locator('.hand .card:not(.no)')
            if c.count()==0: break
            c.first.click(); pg.wait_for_timeout(40)
            tg=pg.locator('.gp.tgt')
            if tg.count(): tg.first.click()
            elif pg.locator('.hint').count(): pg.keyboard.press("Escape")
            pg.wait_for_timeout(40)
        pg.click("#endturn"); pg.wait_for_timeout(250); calme()
    calme()
    av=pg.evaluate("()=>({turn:S.turn,T:S.T,em:totE(S),sc:score(S),rng:rng,hand:S.hand.join(','),adv:S.adv.length,log:S.log.length,defi:S.defi&&S.defi.t,ev:S.ev.t,nz:NZ.cible})")
    dump=pg.evaluate("()=>serialiser()")
    print("taille sauvegarde:",len(dump),"octets")
    print("localStorage ok:", pg.evaluate("()=>!!lireAuto()"))
    # rechargement complet de la page, puis reprise
    pg.reload(); pg.wait_for_timeout(500)
    print("bandeau reprise visible:", pg.locator("#rpgo").count()==1)
    pg.click("#rpgo"); pg.wait_for_timeout(500)
    ap=pg.evaluate("()=>({turn:S.turn,T:S.T,em:totE(S),sc:score(S),rng:rng,hand:S.hand.join(','),adv:S.adv.length,log:S.log.length,defi:S.defi&&S.defi.t,ev:S.ev.t,nz:NZ.cible})")
    print("avant :",av)
    print("après :",ap)
    print("IDENTIQUE:", av==ap)
    # on continue de jouer un tour après reprise
    for _ in range(3):
        c=pg.locator('.hand .card:not(.no)')
        if c.count()==0: break
        c.first.click(); pg.wait_for_timeout(40)
        tg=pg.locator('.gp.tgt')
        if tg.count(): tg.first.click()
        elif pg.locator('.hint').count(): pg.keyboard.press("Escape")
        pg.wait_for_timeout(40)
    pg.click("#endturn"); pg.wait_for_timeout(250); calme()
    print("tour après reprise:", pg.evaluate("()=>S.turn"))
    print("erreurs:", errs or "none")
    b.close()
