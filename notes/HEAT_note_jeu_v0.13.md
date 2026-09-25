# HEAT — version jouable v0.13

Fichier : `jeu/jeu.html`, autonome, aucune dépendance, s'ouvre par double-clic.
L'archive datée est à côté, sous `HEAT_jeu_v0.13.html`.

Cette version corrige les trois défauts d'équilibre relevés par la note v0.12, et reprend plusieurs chantiers laissés ouverts depuis la v0.5.

## 1. La crédibilité redevient un rapport des deux côtés

En v0.12, le budget du joueur suivait sa crédibilité, mais celui de l'adversaire restait fixé par le niveau. Discréditer l'adversaire enrichissait donc le joueur sans jamais appauvrir l'adversaire.

**Règle** : le budget de l'adversaire est désormais `n × budgetPuissance(sa crédibilité) / 4,5`. C'est le même facteur que le joueur, entre 2/3 et 4/3, et `n` est sa valeur à crédibilité neutre.

**Valeurs de n, mesurées** (20 parties par point, joueur automatique tirant au hasard) :

| Niveau | n | Actif — score | Attentiste — score | Ce qui a décidé |
|---|---|---|---|---|
| Découverte | 3 → **3,5** | 336 → 332 | 551 → 386 | à 3, le seuil des 20 Gt n'était presque jamais atteint côté attentiste, et le jalon rapportait tout |
| Standard | 5 → **4,5** | 280 → 310 | 274 → 307 | rétablit l'écart avec Découverte |
| Réaliste | 6,5 → **6** | 258 → 280 | 190 → 211 | l'écart avec Expert se resserrait côté actif |
| Expert | **8** | 210 | 145 | inchangé |

## 2. L'adversaire joue la crédibilité, et ses combinaisons en Expert

Ces deux points étaient ouverts depuis la v0.11 et la v0.6.

- **Crédibilité.** À 10 points de retard ou plus, l'adversaire essaie chacun de ses leviers sur une copie de l'état, et joue celui qui redresse le plus l'écart par point de puissance, pondéré par ses chances de passer. Sur 20 parties au niveau Réaliste, il est en retard dans 303 situations. Dans la grande majorité, il n'a aucun levier de crédibilité en main, et c'est cela qui limite, pas le seuil. Quand il en a un, le gain va de 4,5 à 21 points d'écart par point de puissance.
- **Expert.** L'adversaire cherche ses combinaisons, les joue en premier et les déclenche comme le joueur. Sur 10 parties en Expert, 28 combinaisons se déclenchent. Expert devient un palier de règles, et plus seulement un budget plus gros.
- **Ce qui n'a pas été fait : une anticipation générale sur la projection 2100.** La projection ne voit ni l'opinion ni les effets différés : un adversaire qui l'optimiserait deviendrait myope sur exactement ce que ses listes de priorités savent bien jouer.

## 3. Des événements qui dépendent du climat

- **Pondération.** Les catastrophes physiques (dôme de chaleur, inondations, incendies, sécheresse) ont un poids de 1 à 1,0 °C, 2 à 1,5 °C et 3 à 2,0 °C. Les autres événements gardent un poids de 1. Le même événement ne tombe plus deux tours de suite. Avant, les dix événements étaient équiprobables quelle que soit la température.
- **Trois événements de palier**, tirables seulement au-delà d'une température courante :

| Événement | Seuil | Effet |
|---|---|---|
| Récoltes perdues sur plusieurs continents | 1,6 °C | attribuable ; une fois attribué, perçu +20 sur place, +6 ailleurs (contre +14 / +4) |
| Exode climatique | 1,8 °C | friction +6 en Europe et en Amérique du Nord, soutien réel +4 dans les blocs du Sud |
| Point de bascule franchi | 2,0 °C | soutien réel +5 partout ; attribuable comme les récoltes |

Aucun n'ajoute de contrainte (principe n°2). Partie passive vérifiée : **3,48 °C**, inchangée.

## 4. Trois scénarios de départ

| Scénario | Ce qui change |
|---|---|
| 2015, au hasard | la partie habituelle |
| 2015, l'histoire réelle | tour 1 : les méga-incendies australiens de 2019-2020 ; tour 2 : la flambée du gaz de 2022. En fin de tour, le journal compare vos émissions aux émissions réelles de 2020 (≈ 35,0 Gt) et 2025 (≈ 38,1 Gt, estimation), d'après le Global Carbon Project |
| 2030, quinze ans perdus | les trois premiers tours se jouent sans personne ; vous commencez au tour 4 avec les ressources de départ, 43 GtCO₂/an et 1,34 °C |

Le départ en 2030 n'est pas étalonné : l'indice de performance (ci-dessous) n'y est pas calculé.

## 5. Un score comparable, et un verdict qui dépend du camp

- **L'écran de fin n'affichait pas le score.** Il affiche maintenant le score, son palier, et un **indice** : 100 correspond au joueur automatique du même camp et du même niveau. Les formules de score des deux camps diffèrent, et seul l'indice permet de dire « j'ai mieux joué attentiste qu'actif ».
- **Le verdict était écrit du point de vue du seul camp actif.** Un joueur attentiste qui finissait à 2,1 °C lisait « Victoire nette ». Il lit maintenant « Défaite nette ».

## 6. Interface

- **Titres des boutons d'accueil lisibles.** Ils sortaient en noir sur fond sombre depuis la v0.11.2 (`button` sans `color:inherit`).
- **Barre du haut fixe** au défilement, avec la température projetée en 2100. Sur téléphone, seul le bouton de validation reste fixe, en bas de l'écran.
- **Infobulles au toucher** : un appui long de 0,45 s les affiche. Elles n'existaient qu'au survol de la souris, et restaient donc inaccessibles sur tablette et téléphone.
- **Plan réordonnable** (ouvert depuis la v0.5) : chaque levier peut être avancé ou reculé, et l'ordre affiché est l'ordre d'application.
- **Vue compacte des cartes** : titre, puissance, coût et une ligne d'effet. Elle est mémorisée, et active par défaut sur téléphone.
- **Restes de la v0.12** : « 3.1 actions restantes » dans le plan, « ne consomme pas d'action », « 1 pts ».
- **Règles** : un paragraphe sur les événements de palier, et un sur le coefficient climatique. 0,58 °C par millier de gigatonnes, c'est au-dessus de l'estimation centrale du GIEC pour le CO₂ seul (0,45 °C, fourchette probable 0,27 à 0,63). Le texte dit qu'on peut le lire comme incluant grossièrement les autres gaz.

## Étalonnage v0.13

30 parties par configuration, `outils/verifier.py`.

| | Découverte | Standard | Réaliste | Expert |
|---|---|---|---|---|
| Actif — score | 308 | 289 | 237 | 176 |
| Actif — °C 2100 | 2,58 | 2,60 | 2,69 | 2,83 |
| Attentiste — score | 412 | 293 | 205 | 140 |
| Attentiste — °C 2100 | 2,49 | 2,31 | 2,11 | 1,93 |

Passif : **3,48 °C**. Les scores décroissent avec le niveau pour les deux camps. Ces valeurs sont aussi celles de `SCORE_REF`, la référence de l'indice.

## Ce qui reste ouvert

- **Le choix du bloc incarné**, en attente à votre demande depuis la v0.7. Il ne relève pas d'un ajustement : il faut décider ce que change le fait d'incarner la Chine plutôt que l'Europe.
- **Un départ en 1992.** Cela demande des émissions, des blocs et un catalogue de leviers pour 1992 : c'est un jeu de données à construire, pas un réglage.
- **L'amortissement de la projection des premiers tours** (v0.5). Écarté volontairement : la projection est la trajectoire réelle de la partie à contraintes figées, pas une extrapolation, et l'amortir la rendrait fausse. La barre du haut l'affiche désormais en permanence, ce qui rend visible sa remontée quand l'adversaire répond.
- **La pioche de l'adversaire ignore sa crédibilité** : il ne peut jouer la crédibilité que s'il en a tiré les leviers.
- **Le joueur automatique reste glouton** : tous les chiffres d'étalonnage sont des planchers.
