# HEAT — version jouable v0.15.2

## v0.15.2 — l'échelle de couleur des bandes corrigée

Remarque reçue : « couleur encore très bleue alors qu'on n'est pas loin de la moitié ». Elle était fondée. L'échelle de la v0.15 était linéaire de −0,6 à 3,6 °C, ce qui plaçait le blanc à 1,3 °C : les années 1990 à 2026 ressortaient pâles, presque bleues, alors qu'elles représentent déjà 40 % du chemin vers 3,48 °C.

**Nouvelle échelle**, alignée sur celle des « warming stripes » d'Ed Hawkins :
- **blanc** : la moyenne 1971-2000, soit 0,51 °C au-dessus de 1850-1900 dans la série NOAA ;
- **bleus** : de −0,2 °C jusqu'au blanc ;
- **rouges** : du blanc à 3,5 °C, avec un exposant 0,75 qui donne plus de place au premier degré.

| Écart à 1850-1900 | Couleur |
|---|---|
| 0 °C | bleu franc |
| 0,51 °C | blanc |
| 1,0 °C | saumon |
| 1,41 °C (2025, observé) | rouge orangé, vers le milieu des rouges |
| 2,0 °C | rouge |
| 2,7 °C | rouge très sombre |
| 3,48 °C | presque noir |

Aucune règle ne change ; `outils/verifier.py` passe.

### Ce qui reste à trancher

De 2015 à 2025, les bandes montrent la trajectoire du modèle du jeu (de 1,00 à 1,22 °C), alors que l'observé annuel va de 1,18 à 1,53 °C. Le modèle part d'une tendance de 1,0 °C en 2015 et ne reproduit pas les années chaudes récentes (El Niño de 2023-2024). Les bandes juste à gauche du repère « aujourd'hui » sont donc un peu plus claires que la réalité.
