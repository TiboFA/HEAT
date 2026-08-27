# Concatène les cinq morceaux en un fichier unique, et l'écrit deux fois.
#
#   jeu.html                 le nom stable — c'est celui qu'on ouvre, toujours
#                            la dernière version. Les raccourcis, les liens et
#                            les harnais de test pointent là et n'ont jamais
#                            à être mis à jour.
#   HEAT_jeu_vX.Y.html       l'archive de la version, numéro lu dans le <title>
#                            de a_head.html. Les anciennes versions ne sont plus
#                            reconstructibles : on les garde.
import re, sys
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
