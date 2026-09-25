# Les vérifications à passer avant toute livraison, en une commande.
#
#   python3 outils/verifier.py          depuis la racine du dépôt
#   python3 outils/verifier.py --vite   étalonnage sur 10 parties au lieu de 30
#
# Cinq contrôles, dans cet ordre :
#   1. sources   jeu/jeu.html est bien ce que jeu/src/ produit. La v0.12 a été
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

print("2. play3")
out = harnais("play3.py")
ok("partie complète sans erreur", "errors: none" in out and "over: True" in out, out.strip().splitlines()[-1] if out.strip() else "")

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
for camp in ("actif", "attentiste"):
    sc = [int(x) for x in re.findall(r"^%s\s+niveau \d : .*?score=(\d+)" % camp, out, re.M)]
    ok("%s : score décroissant avec le niveau" % camp,
       len(sc) == 4 and all(a > b for a, b in zip(sc, sc[1:])), str(sc))

print()
print("TOUT PASSE" if not echecs else "%d ÉCHEC(S) : %s" % (len(echecs), ", ".join(echecs)))
sys.exit(1 if echecs else 0)
