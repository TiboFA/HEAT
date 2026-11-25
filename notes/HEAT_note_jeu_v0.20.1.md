# HEAT v0.20.1 — résolution plus rapide

La séquence de résolution est accélérée d'un tiers : toutes les durées d'étape sont multipliées par `RYTHME = 0,65` (une seule constante, dans `d_js.txt`, à ajuster si besoin), y compris le moment où le résultat d'un pari s'affiche.

Mesuré sur trois tours identiques : 14,0 s en moyenne par résolution en v0.20, 8,8 s en v0.20.1. Les lignes restent dans le fil de résolution, on peut donc relire à son rythme une fois la séquence finie.

Aucune règle ni donnée modifiée.
