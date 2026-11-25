# HEAT v0.20.3 — bouton de fin de tour raccourci, halo d'émissions visible

## Bouton de fin de tour

- « Passer le tour (5,5 pts restants) » → **« Passer · 5,5 pts »** (*Pass · 5.5 pts*).
- Sur le même modèle, « Valider le tour (2 leviers, 3 pts) » → **« Valider · 2 leviers · 3 pts »** (*Confirm · 2 levers · 3 pts*) : sans cela, la barre repassait sur deux lignes dès qu'un levier était engagé.
- Au-delà de 1 400 px, le texte de la barre ne se coupe plus (il tenait déjà en largeur, le navigateur le coupait quand même).

Résultat à 1440 px : une seule ligne en Découverte et en Standard, avec ou sans plan, en français et en anglais.

## Halo d'émissions

Le guide annonce un « halo rouge autour d'un bloc qui vaut ses émissions » ; il ne se voyait pas. Il mesurait de 26 à 69 px pour le plus gros émetteur, moins que la pastille du bloc (environ 65 px), et son opacité allait de 5 à 25 %. Il mesure maintenant de 50 à 135 px selon les émissions, avec une opacité de 12 à 40 %, et il rétrécit toujours quand le bloc décarbone.

Sur téléphone, où la grille des blocs remplace les pastilles, il n'y a pas de halo.

Aucune règle ni donnée modifiée.
