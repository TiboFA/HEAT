# HEAT v0.19 — bilan de tour allégé

D'après la maquette `cadrage/HEAT_maquette_bilan_v1.html`.

## Avant

1 774 px de haut, dix blocs au même niveau : neuf indicateurs, pic/seuil/défi, cinq ressources, tableau des huit blocs (32 cases, surtout des « = »), coups adverses, leviers redevenus jouables, presse, tour suivant (deux encadrés et quatre pastilles), courbe, journal complet. Le chiffre qui décide la partie était le premier de neuf.

## Maintenant (environ 690 px sur ordinateur, sans défiler)

1. **Où finit la partie** en grand, avec son écart, et une phrase qui compare au **plan** : « Votre plan visait 2,58 °C. L'adversaire et la physique du tour en ont repris 0,05. » (ou « il a tenu », ou « la résolution a fait mieux »), plus « un de vos paris a échoué » le cas échéant. Une réglette situe le résultat entre 1,5 °C, le plan, le monde réel et « sans action » ; les étiquettes qui se touchent sont masquées par ordre d'importance.
2. **Quatre tuiles** : score, émissions, défi du tour (ou réchauffement s'il n'y en a pas), écart de crédibilité.
3. **Les coups côte à côte** : les vôtres (réussi / échoué avec la probabilité, leviers redevenus jouables) et ceux de l'adversaire (échoué, réplique à l'un de vos leviers), chacun avec son effet en une ligne.
4. **Ce qui a bougé** : seulement les blocs dont une jauge a varié d'au moins 2 (cinq au plus, trois jauges chacun, en vert ou en rouge selon votre camp) ; les autres sont dits « changements mineurs ».
5. **Le tour suivant** en une phrase : événement (à attribuer ou non) et défi.
6. **▸ déplier le détail**, replié par défaut et retenu d'un tour à l'autre : tous les indicateurs, vos ressources, la carte et le tableau des huit blocs, la presse, la courbe, le journal du tour. Rien n'a été supprimé.

« Continuer » passe dans l'en-tête ; la case « ouvrir ce bilan automatiquement » et « Rejouer ce tour » (Découverte) restent en pied.

## Ce qui a été ajouté au moteur

- La projection 2100 du plan est relevée au moment de la validation, avant l'effacement de l'état prévisionnel. Vérifié sur cinq tours : elle est égale à l'aperçu affiché avant validation.
- Chaque coup du joueur garde sa réussite et sa probabilité.

Ni l'un ni l'autre ne change le déroulement de la partie (étalonnage inchangé).

## Anglais

Nouveaux textes traduits ; un nom de levier oublié en v0.18 (« Investissement d'infrastructure » → *Infrastructure investment*) ajouté après un contrôle des 1 187 textes de données ; le lien « turn report » de la barre du haut raccourci en « report », il la faisait passer à la ligne.
