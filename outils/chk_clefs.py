from playwright.sync_api import sync_playwright
import pathlib
url="file://"+str(pathlib.Path("HEAT_jeu_v0.10.html").resolve())
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={"width":1680,"height":1250},device_scale_factor=2)
    errs=[]; pg.on("pageerror",lambda e:errs.append(str(e)))
    pg.on("console",lambda m: errs.append("console: "+m.text) if m.type=="error" else None)
    pg.goto(url); pg.wait_for_timeout(300)
    pg.click('#optLvl .opt[data-v="3"]'); pg.evaluate("()=>{GUIDE_VU=true;}"); pg.click("#start"); pg.wait_for_timeout(300)
    # sur 200 tirages, un levier clef doit toujours etre en main
    print(pg.evaluate("""()=>{
      const res={};
      DEFIS.filter(d=>d.clefs).forEach(D=>{
        let ko=0;
        for(let i=0;i<200;i++){
          rng=7000+i;
          const s=newGame(D.att?"att":"actif",3);
          s.defi=D; s.hand=[]; refill(s);
          if(!s.hand.some(id=>D.clefs.includes(id))) ko++;
        }
        res[D.t]=ko+" échec(s) sur 200";
      });
      return JSON.stringify(res,null,1);}"""))
    # cas ou tous les leviers clefs sont épuisés : pas de plantage
    print(pg.evaluate("""()=>{rng=1;const s=newGame("actif",3);
      s.defi=DEFIS.find(d=>d.t==="Un verrou");
      s.joues=["A12","A12","A12","A62","A62","A62"];
      s.hand=[];refill(s);
      return "épuisés -> main de "+s.hand.length+", clef en main : "+s.hand.some(id=>["A12","A62"].includes(id));}"""))
    # marqueur visuel
    pg.evaluate("""()=>{S.defi=DEFIS.find(d=>d.t==="Un verrou");S.hand=[];refill(S);PV=null;render();}""")
    pg.wait_for_timeout(300)
    print("cartes marquées ★ :", pg.evaluate("()=>[...document.querySelectorAll('.card .tag.defi')].map(e=>e.closest('.card').dataset.id)"))
    print("mention carte défi :", pg.evaluate("()=>document.querySelector('.ev.defi .dfw small').textContent"))
    pg.locator('#events').screenshot(path="k_defi.png")
    print("errors:", errs or "none")
    b.close()
