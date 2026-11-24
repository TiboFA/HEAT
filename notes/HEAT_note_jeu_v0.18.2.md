# HEAT v0.18.2 — liens de repli : un vocabulaire, un style

## Avant

Sept sections repliables, cinq vocabulaires et trois styles :

| Section | Ouverte | Repliée | Style |
|---|---|---|---|
| Ce tour | réduire | afficher | minuscules soulignées |
| Carte | masquer la carte | afficher la carte | minuscules, 11 px |
| Tableau de bord | réduire | afficher | minuscules soulignées |
| Camp adverse | réduire | afficher | capitales à chasse fixe (héritées du titre) |
| Doctrine | replier | régler | capitales, style en ligne |
| Presse | réduire | afficher | capitales |
| Journal | masquer | afficher | capitales |

## Maintenant

- Partout **▾ replier** quand la section est ouverte, **▸ déplier** quand elle est repliée ; « ▾ replier la carte / ▸ déplier la carte » pour la carte.
- Exception assumée : la doctrine repliée dit **▸ régler**, parce que l'ouvrir sert à agir et coûte de l'attention.
- Un seul style (`span.lnk.repl`) : vert d'eau, chasse fixe 10,5 px, minuscules, souligné — y compris dans les titres de la colonne de droite, dont il n'hérite plus les capitales. Vérifié en lisant le style calculé des sept liens, ouverts et repliés, en français et en anglais.
- Les infobulles suivent : « Replie… » / « Déplie… ».
- En anglais : ▾ collapse / ▸ expand / ▸ adjust.

## Au passage

Depuis la v0.18, le sélecteur FR · EN faisait passer « guide » à la ligne dans la barre du jeu à 1440 px. La barre n'affiche plus que la langue d'arrivée (« EN » en français, « FR » en anglais) ; l'accueil et l'écran de fin gardent « FR · EN ».

Aucune règle ni donnée modifiée.
