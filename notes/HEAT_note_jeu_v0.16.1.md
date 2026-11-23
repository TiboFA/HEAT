# HEAT — version jouable v0.16.1

## v0.16.1 — une icône

Icône retenue : le H à deux thermomètres, dans sa variante « tubes blancs » (C3c de `cadrage/HEAT_icones_v3.html`). Le H blanc d'origine porte deux colonnes de liquide :
- **à gauche**, un thermomètre bleu à peine levé : le froid ;
- **à droite**, un thermomètre rouge presque plein : la chaleur.

La silhouette du H se lit d'abord, les thermomètres ensuite, de 16 à 180 px.

Tout est dans le fichier unique, sans fichier externe :
- **onglet** : SVG en data URI, environ 600 caractères ;
- **écran d'accueil d'un téléphone** (`apple-touch-icon`) : PNG de 180 px en base64, 3,3 Ko. L'iPhone n'accepte pas le SVG à cet endroit ;
- **couleur de thème** `#0b0d0e`, pour la barre du navigateur mobile.

Aucune règle ne change ; `outils/verifier.py` passe.
