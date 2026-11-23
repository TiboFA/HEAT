# HEAT v0.16.6 — infobulles au toucher

Préalable aux tests sur tablette et téléphone. Testé sur un Pixel 7 émulé, avec de vrais évènements tactiles.

Avant : l'appui long fonctionnait, mais chaque tap court ouvrait aussi une infobulle (le navigateur simule un survol de souris après un toucher), qui restait affichée. Sur une carte, le tap jouait le levier et ouvrait l'infobulle par-dessus.

Maintenant :
- **appui long** (0,45 s) sur n'importe quel élément : son explication, sans déclencher l'action ;
- **tap court** sur un élément qui ne fait rien d'autre (tuile du tableau de bord, jauge, intitulé) : son explication ;
- **tap court** sur un élément cliquable (carte, lien, bouton) : l'action seule, sans infobulle ;
- un toucher ailleurs referme l'infobulle ;
- à la souris, le survol fonctionne comme avant ;
- sur iOS, l'appui long n'ouvre plus le menu de sélection de texte sur les éléments expliqués ;
- l'accueil indique l'appui long, uniquement sur les écrans sans survol.

Aucune règle ni donnée modifiée.
