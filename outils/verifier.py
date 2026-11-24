# Les vérifications à passer avant toute livraison, en une commande.
#
#   python3 outils/verifier.py          depuis la racine du dépôt
#   python3 outils/verifier.py --vite   étalonnage sur 10 parties au lieu de 30
#
# Cinq contrôles, dans cet ordre :
#   1. sources   jeu/jeu.html et jeu/en.html sont bien ce que jeu/src/ produit,
#                et tout le texte a sa traduction anglaise. La v0.12 a été
#                écrite directement dans jeu.html pendant un temps : un
#                build.py relancé l'aurait effacée sans rien dire.
#   2. play3     une partie complète dans l'interface, sans erreur console
#   3. chk_coh2  aucun levier ne produit un effet qu'il n'annonce pas
#   4. chk_save  sauvegarde puis reprise bit à bit identiques
#   5. calib3    passif à 3,48 °C exactement, score décroissant avec le niveau
#                pour les deux camps
#
# Code de sortie 0 si tout passe, 1 sinon.
import hashlib, pathlib, re, subprocess, sys

RACINE = pathlib.Path(__file__).resolve().parent.parent
JEU = RACINE / "jeu"
SRC = JEU / "src"
N = "10" if "--vite" in sys.argv else "30"
MORCEAUX = ['a_head.html', 'b_css.txt', 'c_body.html', 'd_js.txt', 'e_tail.html']

echecs = []
def ok(nom, bon, detail=""):
    print(("  ok   " if bon else "  ÉCHEC ") + nom + ("  — " + detail if detail else ""))
    if not bon: echecs.append(nom)

def harnais(script, *args):
    r = subprocess.run([sys.executable, str(RACINE / "outils" / script), *args],
                       cwd=JEU, capture_output=True, text=True)
    return r.stdout + r.stderr

print("1. sources")
construit = '\n'.join((SRC / m).read_text(encoding='utf-8') for m in MORCEAUX)
livre = (JEU / "jeu.html").read_text(encoding='utf-8')
ok("jeu.html = build(src)", construit == livre,
   "" if construit == livre else "relancer build.py, ou reporter dans src/ ce qui a été modifié à la main")
ver = re.search(r'<title>[^<]*?(v\d+(?:\.\d+)+)', construit).group(1)
arch = JEU / ("HEAT_jeu_%s.html" % ver)
ok("archive %s présente et identique" % arch.name,
   arch.exists() and hashlib.md5(arch.read_bytes()).digest() == hashlib.md5(livre.encode('utf-8')).digest())

# la version anglaise : produite au build depuis jeu/i18n/en.json
sys.path.insert(0, str(RACINE / "outils"))
import i18n
en, manque = i18n.construire_en([(SRC / m).read_text(encoding='utf-8') for m in MORCEAUX])
livre_en = (JEU / "en.html").read_text(encoding='utf-8') if (JEU / "en.html").exists() else ""
ok("en.html = build(src)", en == livre_en, "" if en == livre_en else "relancer build.py")
arch_en = JEU / ("HEAT_jeu_%s_en.html" % ver)
ok("archive %s présente et identique" % arch_en.name, arch_en.exists() and arch_en.read_text(encoding='utf-8') == en)
ok("aucun texte sans traduction anglaise", not manque,
   "" if not manque else "%d morceau(x), dont « %s » — compléter jeu/i18n/en.json (python3 outils/i18n.py extraire)" % (len(manque), manque[0][:60]))

print("2. play3")
out = harnais("play3.py")
ok("partie complète sans erreur", "errors: none" in out and "over: True" in out, out.strip().splitlines()[-1] if out.strip() else "")

r = subprocess.run([sys.executable, str(RACINE / "outils" / "play3.py")], cwd=JEU, capture_output=True, text=True,
                   env=dict(__import__("os").environ, HEAT_PAGE="en.html"))
out = r.stdout + r.stderr
ok("partie complète sans erreur, en anglais", "errors: none" in out and "over: True" in out, out.strip().splitlines()[-1] if out.strip() else "")

print("3. chk_coh2")
out = harnais("chk_coh2.py")
ok("aucun effet non annoncé", re.search(r"^0 cartes", out, re.M) is not None, out.strip().splitlines()[-1] if out.strip() else "")

print("4. chk_save")
out = harnais("chk_save.py")
ok("sauvegarde identique", "IDENTIQUE: True" in out and "erreurs: none" in out)

print("5. calib3 (%s parties par configuration)" % N)
out = harnais("calib3.py", N)
print("     " + out.strip().replace("\n", "\n     "))
m = re.search(r"passif \(aucun coup\)\s*:\s*([\d.]+)", out)
ok("passif à 3,48 °C", bool(m) and m.group(1) == "3.48", m.group(1) if m else "illisible")
# En --vite (10 parties), deux niveaux voisins peuvent s'inverser par le seul
# hasard des tirages : l'inversion est tolérée si elle tient dans deux erreurs
# types de la différence, et signalée. En mode complet (30 parties, la CI),
# l'ordre doit être strict.
VITE = N == "10"
for camp in ("actif", "attentiste"):
    lus = re.findall(r"^%s\s+niveau \d : .*?score=(\d+) \(±(\d+)\)" % camp, out, re.M)
    sc = [int(x) for x, _ in lus]; et = [int(e) for _, e in lus]
    bruit = []
    bon = len(sc) == 4
    for i in range(3 if bon else 0):
        if sc[i] > sc[i + 1]: continue
        marge = 2 * ((et[i] ** 2 + et[i + 1] ** 2) / int(N)) ** 0.5
        if VITE and sc[i + 1] - sc[i] <= marge: bruit.append("niv. %d/%d : +%d, marge %.0f" % (i + 1, i + 2, sc[i + 1] - sc[i], marge))
        else: bon = False
    ok("%s : score décroissant avec le niveau" % camp, bon,
       str(sc) + (" — inversion dans le bruit de 10 parties (" + "; ".join(bruit) + "), à confirmer sans --vite" if bruit and bon else ""))

print()
print("TOUT PASSE" if not echecs else "%d ÉCHEC(S) : %s" % (len(echecs), ", ".join(echecs)))
sys.exit(1 if echecs else 0)
