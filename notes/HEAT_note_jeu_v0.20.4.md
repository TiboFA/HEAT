# HEAT v0.20.4 — la fiche d'un bloc ne passe plus sous ses voisins

Signalé : au survol de la Chine, sa fiche (jauges, leviers adverses) passait sous les pastilles de Golfe & Russie et de l'Inde.

Cause : toutes les pastilles de bloc ont le même niveau d'empilement ; la fiche qui s'ouvre au survol hérite de celui de sa pastille, et les pastilles dessinées après passaient par-dessus.

Correction : le bloc survolé (ou qui a le focus) passe au premier plan. Vérifié pour les huit blocs : au survol de chacun, aucune pastille voisine ne reste visible par-dessus sa fiche.

Aucune règle ni donnée modifiée.
