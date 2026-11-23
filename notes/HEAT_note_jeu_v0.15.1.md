# HEAT — version jouable v0.15.1

## v0.15.1 — « aujourd'hui » sur les bandes de l'accueil

Un repère blanc marque l'année en cours sur les bandes de réchauffement. Il porte deux informations :
- **l'année** : celle de l'horloge de l'appareil, bornée entre 2015 et 2100 ;
- **le dernier réchauffement annuel observé** : +1,41 °C en 2025, d'après la même série NOAA GlobalTemp et la même base (1850-1900) que les bandes de gauche.

L'infobulle rappelle que la partie commence en 2015 : les années qui séparent 2015 d'aujourd'hui se rejouent, autrement.

L'étiquette « 2015 · la partie commence » passe à gauche de son trait, pour ne pas croiser le nouveau repère. Sur téléphone, le repère ne montre que l'année.

`OBS_RECENT` (`d_js.txt`) est la valeur à mettre à jour chaque année, en même temps que `REEL_2100`.

Aucune règle ne change ; `outils/verifier.py` passe.
