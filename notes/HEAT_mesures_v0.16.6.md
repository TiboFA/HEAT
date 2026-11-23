# HEAT v0.16.6 — mesures : multi-bloc et écart entre niveaux

Joueur automatique de `outils/calib3.py`, 30 parties par configuration, mêmes graines.

## Levier sur plusieurs blocs (règle de la v0.15.7)

Nouvelle option : `calib3.py 30 multi` (après chaque levier de bloc, une chance sur deux de l'étendre à un autre bloc éligible, tant que le budget le permet) et `calib3.py 30 multi1` (étend toujours).

| Score moyen | Découverte | Standard | Réaliste | Expert |
|---|---|---|---|---|
| actif, un bloc par levier (référence) | 313 | 291 | 261 | 186 |
| actif, `multi` | 313 | 302 | 259 | 180 |
| actif, `multi1` | 364 | 341 | 275 | 177 |
| attentiste, référence | 367 | 293 | 221 | 152 |
| attentiste, `multi` | 378 | 286 | 210 | 140 |
| attentiste, `multi1` | 332 | 272 | 209 | 145 |

Lecture : concentrer ses leviers est une vraie stratégie pour le camp actif aux niveaux faciles (+50), presque neutre en Réaliste, nulle en Expert. Pour le camp attentiste, elle coûte. Pas de faille : le niveau le plus dur n'en est pas affecté. La référence de la vérification reste le joueur à un bloc.

## Écart entre niveaux

| | Découverte | Standard | Réaliste | Expert |
|---|---|---|---|---|
| actif : score (écart type) | 313 (±96) | 291 (±95) | 261 (±79) | 186 (±48) |
| actif : seuil des 20 Gt atteint | 18/30 | 14/30 | 11/30 | 1/30 |
| attentiste : score (écart type) | 367 (±76) | 293 (±61) | 221 (±33) | 152 (±26) |

Côté attentiste, chaque marche (≈ 70) dépasse l'écart d'une partie à l'autre : on sent le niveau. Côté actif, les marches Découverte → Standard → Réaliste (22, 30) sont trois fois plus petites que la dispersion d'une partie : le score ne les distingue pas, seul le taux de seuil atteint le fait. Une partie actif se joue surtout sur le jalon (atteint ou non), qui fait sauter le score.

À trancher : soit on l'accepte (la difficulté du camp actif se lit dans la probabilité d'atteindre le seuil, pas dans le score), soit on écarte les niveaux côté actif, par les suppléments de ressources de l'adversaire plutôt que par sa puissance (la v0.13 a montré qu'un adversaire à 6,5 points resserre Réaliste et Expert).

## Vérification rapide

`verifier.py --vite` (10 parties) échouait à chaque version sur l'inversion Standard / Réaliste du camp actif, un effet du hasard. Une inversion entre niveaux voisins y est désormais tolérée si elle tient dans deux erreurs types de la différence, et elle est signalée. Le mode complet (30 parties, la CI) reste strict.
