# HEAT — version jouable v0.15

Fichier : `jeu/jeu.html`, autonome, aucune dépendance, s'ouvre par double-clic.
L'archive datée est à côté, sous `HEAT_jeu_v0.15.html`.

## v0.15 — un accueil en bandes de réchauffement, un plateau filaire

Directions retenues dans `cadrage/HEAT_maquettes_design_v1.html` : la C (bandes de réchauffement) pour l'accueil, la A (salle de veille) pour le plateau. Aucune règle ne change.

### Accueil

Un bandeau en tête d'écran, une bande par année de 1850 à 2100. Les couleurs reprennent la palette des « warming stripes » d'Ed Hawkins, selon l'écart à la moyenne 1850-1900.

- **De 1850 à 2014 : l'observé.** C'est la série NOAA GlobalTemp (GCAG), via `datasets/global-temp`, rebasée sur 1850-1900 : de −0,07 °C en 1850 à 1,03 °C en 2014. Ce sont les vraies valeurs annuelles, et non plus la courbe stylisée des maquettes.
- **De 2015 à 2100 : la partie si personne ne joue.** `PASSIF_T` donne la température atteinte à chaque tour par le moteur sans aucun coup joué (de 1,00 à 3,475 °C), interpolée année par année.
- Un trait marque 2015, le début de la partie. En grand : 3,48 °C, avec le monde réel (2,70 °C) en dessous. Les deux valeurs sont lues dans `T_BASELINE` et `REEL_2100`, pas recopiées.

Le reste de l'accueil ne change pas.

### Plateau

La carte passe au style filaire :
- **graticule** tous les 15° ;
- **mer** presque noire ;
- **contours des blocs** en trait fin vert d'eau. Le remplissage reste la teinte calculée par `teinteBloc` (chaleur, dommages, contrainte), à demi-transparent ;
- **trame** discrète et vignettage par-dessus, sans effet sur les clics.

Deux états nouveaux sur la carte elle-même :
- le **plus gros émetteur** du moment est tracé en orange, avec un léger halo ;
- quand un levier de bloc est sélectionné, les **blocs où il peut être joué** s'éclairent en bleu. Avant, seule leur pastille le signalait.

Dans la barre du haut, les chiffres passent en chasse fixe : ils ne font plus bouger la ligne quand ils changent.

### Vérification

`outils/verifier.py` : tout passe. Partie passive à 3,48 °C, étalonnage identique à la v0.14 : seul l'affichage a changé.
