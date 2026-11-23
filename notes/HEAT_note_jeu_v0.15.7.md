# HEAT — version jouable v0.15.7

## v0.15.7 — rejouer le tour, un levier sur plusieurs blocs, des budgets au demi-point

### Rejouer le tour, en Découverte

Au niveau Découverte, le dernier tour résolu peut être rejoué. Le bouton est accessible à trois endroits : le lien « rejouer le tour N » dans la barre du haut, le bouton « Rejouer ce tour » du bilan, et « Rejouer le dernier tour » sur l'écran de fin.

- Juste avant la résolution, la partie entière est mise de côté, plan compris : c'est exactement ce qu'écrirait une sauvegarde. Rejouer la restaure. On revient à la planification du tour, avec le même plan, modifiable.
- **Le hasard est restauré aussi** : changer de plan change le résultat, mais rejouer le même plan redonne le même résultat (vérifié : 1,107 °C dans les deux cas). On ne relance donc pas les dés jusqu'à obtenir un succès.
- Seul le dernier tour résolu peut être rejoué. La copie n'est pas conservée à la fermeture de l'onglet.
- Les autres niveaux ne sont pas concernés.

### Un levier de bloc sur plusieurs blocs dans le même tour

Jusqu'ici, un levier de bloc quittait la main dès qu'il entrait dans le plan : on ne pouvait le jouer que sur un bloc par tour, et sur trois au maximum dans la partie. Il reste désormais en main pendant la planification, marqué « ×n dans le plan », et peut être ajouté sur d'autres blocs.

- **Chaque bloc coûte à nouveau** la puissance du levier et ses ressources. Exemple vérifié : A19 sur la Chine et l'Amérique du Nord coûte 2 × 2 points et 2 × 5 de capital.
- **Les limites ne changent pas** : pas deux fois sur le même bloc, trois blocs au maximum sur la partie.
- À la validation, le levier quitte la main comme avant. L'adversaire n'est pas concerné.

### Budgets au demi-point

La puissance des leviers est un multiple de 0,5 ; les budgets le sont maintenant aussi. Le budget du joueur et celui de l'adversaire sont arrondis au demi-point le plus proche. Avant, un budget de 5,1 laissait 0,1 point qu'aucun levier ne pouvait consommer.

Au départ, les budgets passent de 5,1 à 5 (actif) et de 4,8 à 5 (attentiste).

### Étalonnage v0.15.7

30 parties par configuration, `outils/verifier.py`.

| | Découverte | Standard | Réaliste | Expert |
|---|---|---|---|---|
| Actif — score | 313 | 291 | 261 | 186 |
| Attentiste — score | 367 | 293 | 221 | 152 |

Passif : 3,48 °C. Les scores décroissent avec le niveau pour les deux camps. `SCORE_REF`, la référence de l'indice de performance, reprend ces valeurs.

**À surveiller** : côté actif, l'écart entre Standard et Réaliste s'est resserré. Sur 10 parties seulement (`verifier.py --vite`), il s'inverse (280 contre 290) ; sur 30 parties, l'ordre est net (291 contre 261). Le joueur automatique ne place jamais un levier sur plusieurs blocs dans le même tour : ces chiffres ne mesurent pas cette nouvelle possibilité.
