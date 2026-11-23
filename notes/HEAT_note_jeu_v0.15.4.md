# HEAT — version jouable v0.15.4

## v0.15.4 — l'écran de fin passe au style filaire, avec les bandes de la partie

### La carte du monde en 2100

En tête de l'écran de fin, une copie de la carte du plateau dans l'état final de la partie : même style filaire, même graticule, coins de cadre. Elle montre :
- **chaque bloc** avec son code, sa contrainte finale et ses émissions de 2100 ;
- **le plus gros émetteur** de 2100 en orange, et les blocs sous loi-cadre en vert ;
- **la température atteinte**, en grand, en bas à droite.

Sur téléphone, les étiquettes des blocs sont masquées : elles seraient illisibles.

### Les bandes de la partie

Sous la carte, les bandes de réchauffement telles que la partie les a repeintes :
- **« Votre partie »** : de 1850 à 2014, l'observé (NOAA), comme à l'accueil ; de 2015 à 2100, la température atteinte tour par tour ;
- **« Sans action »** : une bande fine en dessous, la partie passive, pour comparaison.

Pour cela, l'historique de la partie (`s.hist`) garde désormais la température atteinte à chaque tour (`t`). Une partie enregistrée avant la v0.15.4 n'a pas cette valeur : sa trajectoire est alors reconstituée sur la forme de la partie passive, remise à l'échelle entre 1,0 °C et sa température finale. Le format de sauvegarde reste compatible.

### Le reste de l'écran

- Les grands chiffres des encadrés passent en chasse fixe, les intitulés en vert d'eau.
- Le quadrillage du graphique de trajectoire prend la même teinte.
- Sur téléphone, les encadrés passent en une colonne.

Aucune règle ne change ; `outils/verifier.py` passe.
