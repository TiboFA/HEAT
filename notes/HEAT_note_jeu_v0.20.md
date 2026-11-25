# HEAT v0.20 — le fil de résolution

Demande : pendant le calcul qui suit le tour, faire défiler les résultats dans une fenêtre plutôt qu'un affichage un par un qu'on n'a pas le temps de lire.

## Avant

Chaque étape (votre levier, le pari, le coup adverse, l'élection, le défi, la presse…) s'affichait dans un bandeau au-dessus de la carte, remplacé par le suivant au bout d'une seconde environ.

## Maintenant

- Une fenêtre **« Résolution du tour »**, à droite de l'écran (en bas sur téléphone). Chaque étape y **ajoute une ligne qui reste** : vos leviers (▸, avec le tirage des paris : « pari 66 % · échec (88) »), les coups de l'adversaire (◂, « réplique à votre A02 »), les effets bloc par bloc regroupés en pastilles (« CN +20 contrainte »), élections, effets différés, retours de flamme, la dérive automatique (« le monde bouge tout seul »), le défi, la presse, et en dernier où finit la partie.
- Les titres de section (Vos leviers, Le camp attentiste joue, Élections, Physique du climat…) n'apparaissent que si la section contient quelque chose.
- Défilement automatique vers le bas, sauf si vous êtes remonté relire.
- À la fin, la fenêtre **reste ouverte** (« Résolution terminée ») ; le plateau est déjà à jour. **Continuer ▸** la ferme et ouvre le bilan. **passer ▸**, pendant la séquence, applique tout d'un coup et ouvre le bilan directement. Valider le tour suivant referme une fenêtre restée ouverte.
- Les animations sur la carte (jauges, chiffres flottants, blocs qui pulsent) sont conservées.

## Correction trouvée en route

Vos leviers sans pari n'étaient pas annoncés pendant la résolution : seuls les paris et les coups adverses l'étaient. Dans le fil, leurs effets se seraient accrochés au levier précédent. Chacun de vos leviers a maintenant sa ligne (testé sur trois tours : tous les leviers joués y sont nommés).

Aucune règle ni donnée modifiée ; étalonnage inchangé.
