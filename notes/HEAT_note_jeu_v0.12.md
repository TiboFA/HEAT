# HEAT — version jouable v0.12

Fichier : `jeu/jeu.html`, autonome, aucune dépendance, s'ouvre par double-clic.
L'archive datée est à côté, sous `HEAT_jeu_v0.12.html`.

## v0.12 — le budget de puissance intégral

C'est le chantier laissé ouvert en v0.10 et v0.11 : remplacer le compteur d'actions par une somme de puissances plafonnée par la crédibilité.

### Ce qui change

- **La puissance devient continue.** L'étiquette binaire léger/lourd (1 ou 2 actions) cède la place à une table `PUISSANCE` : chaque levier coûte entre 1 et 3,5 points, par pas de 0,5. Le calcul reste celui de la v0.10, le plus grand de quatre rapports à un seuil (0,06 °C de trajectoire, 30 points d'opinion, 20 points de plafond, 12 points d'indice technologique), mais arrondi au demi-point au lieu d'être coupé en deux. Trente-huit leviers sont au minimum, quarante et un sont lourds (2 points ou plus), six sont extrêmes (3 points ou plus) et portent une étiquette rouge.
- **Le budget du joueur suit sa crédibilité** : `4,5 + 1,5 × (crédibilité − 50) / 50`, soit 3 points à crédibilité nulle et 6 à crédibilité pleine. Il est recalculé au début de chaque tour.
- **Le budget de l'adversaire reste fixé par le niveau** : 3 / 5 / 6,5 / 8.
- **Format de sauvegarde** : `SAVE_V` passe à `0.12`. `s.actions` n'est plus un entier, une sauvegarde plus ancienne ne se recharge pas.
- **Mise en page** : quand la colonne de gauche passe au-dessus de la carte (moins de 1 400 px), les cartes s'y répartissent en grille au lieu de s'empiler une par ligne.

### Comment cette version est entrée dans le dépôt

La v0.12 a d'abord été écrite directement dans `jeu/jeu.html`, sans passer par `jeu/src/`. Les sources produisaient donc encore la v0.11.2, et un `build.py` relancé l'aurait effacée. Elle a été reportée dans les cinq morceaux de `src/`. La reconstruction redonne `jeu.html` à l'octet près (md5 `1bbbc794…`), et l'archive `HEAT_jeu_v0.12.html` a été ajoutée.

Pour que cela ne se reproduise pas, `outils/verifier.py` commence par reconstruire les sources et les compare à `jeu.html`.

`calib3.py` lisait la constante `ACTIONS`, supprimée en v0.12, et s'arrêtait en erreur. Il lit maintenant le budget du tour dans l'état de la partie (`S.actions`), ce qui marche pour toutes les versions.

### Étalonnage v0.12, et ce qu'il révèle

20 parties par configuration, joueur automatique tirant au hasard. Entre parenthèses, la v0.11.2 sur les mêmes graines.

| | Découverte | Standard | Réaliste | Expert |
|---|---|---|---|---|
| Actif — score | 345 (346) | 279 (318) | 269 (265) | 216 (235) |
| Attentiste — score | **566** (424) | 278 (318) | 214 (226) | 169 (181) |
| Attentiste — °C 2100 | **2,72** (2,51) | 2,28 (2,30) | 2,14 (2,10) | 2,00 (1,96) |

Passif : 3,48 °C, inchangé.

Trois défauts, corrigés en v0.13 :

1. **Découverte côté attentiste devient trop facile.** L'adversaire y a 3 points contre 4,8 pour le joueur, et le score bondit de 424 à 566.
2. **Côté actif, Standard et Réaliste se confondent** (279 contre 269). Sur 10 parties, Réaliste passe même sous Expert.
3. **Le principe de la crédibilité comme rapport n'est tenu qu'à moitié.** Le budget du joueur suit sa crédibilité, mais celui de l'adversaire ne suit pas la sienne. Discréditer l'adversaire enrichit donc le joueur sans jamais appauvrir l'adversaire.

Le texte de l'écran d'accueil annonçait aussi « 4,5 au départ ». C'est faux : la crédibilité de départ vaut 70 côté actif et 60 côté attentiste, ce qui donne des budgets de 5,1 et 4,8.
