# Concatène les cinq morceaux en un fichier unique, et l'écrit deux fois.
#
#   jeu.html                 le nom stable — c'est celui qu'on ouvre, toujours
#                            la dernière version. Les raccourcis, les liens et
#                            les harnais de test pointent là et n'ont jamais
#                            à être mis à jour.
#   HEAT_jeu_vX.Y.html       l'archive de la version, numéro lu dans le <title>
#                            de a_head.html. Les anciennes versions ne sont plus
#                            reconstructibles : on les garde.
#
# Depuis la v0.18, la version anglaise est produite en même temps, à partir du
# dictionnaire jeu/i18n/en.json (voir outils/i18n.py) :
#   en.html                  le nom stable anglais
#   HEAT_jeu_vX.Y_en.html    son archive
# Un morceau de texte sans traduction reste en français et est signalé.
import pathlib, re, sys
MORCEAUX = ['a_head.html', 'b_css.txt', 'c_body.html', 'd_js.txt', 'e_tail.html']
parts = [open(f, encoding='utf-8').read() for f in MORCEAUX]
h = '\n'.join(parts)

m = re.search(r'<title>[^<]*?(v\d+(?:\.\d+)+)[^<]*</title>', parts[0])
if not m:
    sys.exit("Numéro de version introuvable dans le <title> de a_head.html")
ver = m.group(1)

for nom in ('jeu.html', 'HEAT_jeu_%s.html' % ver):
    open(nom, 'w', encoding='utf-8').write(h)
print("%s — %d caractères → jeu.html + HEAT_jeu_%s.html" % (ver, len(h), ver))

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "outils"))
import i18n
en, manque = i18n.construire_en(parts)
for nom in ('en.html', 'HEAT_jeu_%s_en.html' % ver):
    open(nom, 'w', encoding='utf-8').write(en)
print("anglais — %d caractères → en.html + HEAT_jeu_%s_en.html%s"
      % (len(en), ver, "" if not manque else " — %d morceau(x) sans traduction :" % len(manque)))
for s in manque[:20]: print("   ·", s[:100])
