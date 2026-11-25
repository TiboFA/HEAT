# HEAT v0.20.4 — la fiche d'un bloc ne passe plus sous ses voisins

Signalé : au survol de la Chine, sa fiche (jauges, leviers adverses) passait sous les pastilles de Golfe & Russie et de l'Inde.

Cause : toutes les pastilles de bloc ont le même niveau d'empilement ; la fiche qui s'ouvre au survol hérite de celui de sa pastille, et les pastilles dessinées après passaient par-dessus.

Correction : le bloc survolé (ou qui a le focus) passe au premier plan. Vérifié pour les huit blocs : au survol de chacun, aucune pastille voisine ne reste visible par-dessus sa fiche.

Aucune règle ni donnée modifiée.

## Fil de résolution centré

La fenêtre « Résolution du tour » est centrée en largeur (520 px, ou la largeur de l'écran moins 32 px s'il est plus étroit), au lieu d'être collée à droite. Sur téléphone, elle reste en bas, sur toute la largeur. Contrepartie : en haut de l'écran, elle recouvre le haut de la carte (Europe, Golfe & Russie, une partie de la Chine) pendant la séquence ; les chiffres animés de ces blocs passent dessous.
