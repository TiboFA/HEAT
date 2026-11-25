# HEAT v0.20.2 — liens d'action, un seul style

Après les liens de repli (v0.18.2), les liens d'action : partie, guide, bilan, rejouer (barre du haut), renouveler, à venir, masqués (main), tout voir / voir l'essentiel (journal, bilan), tout retirer (plan), annuler (consigne de ciblage), trajectoire et bilan (tableau de bord), fermer le guide, reprendre depuis un fichier (accueil), passer (fil de résolution), FR · EN.

Ils avaient quatre couleurs (bleu, gris, vert d'eau, bleu clair) et trois tailles. Ils partagent maintenant un style : chasse fixe 11 px, vert d'eau clair, soulignés (10,5 px dans la barre du haut). Les liens de repli gardent le leur — vert d'eau plus soutenu, avec ▾ / ▸ — pour qu'on distingue « ouvrir ou fermer une section » de « faire quelque chose ». Les liens inactifs restent grisés. Vérifié en lisant le style calculé de tous les liens visibles, en français et en anglais.

## Barre du haut

La chasse fixe étant plus large, la barre passait à la ligne à 1440 px. Elle débordait en fait déjà dès le tour 2, en français, avant ce changement (le lien du bilan n'apparaît qu'à partir du tour 2). Trois raccourcis :
- « bilan du tour 6 » → « bilan », « rejouer le tour 6 » → « rejouer » (le numéro reste dans l'infobulle) ;
- « 1,11 °C → 3,47 °C en 2100 » → « 1,11 °C → 3,47 °C » (l'infobulle dit que c'est la température atteinte en 2100).

Résultat à 1440 px : une ligne en Standard, en français et en anglais. En Découverte, le lien « rejouer » en plus la fait encore passer sur deux lignes en français (pas en anglais, ni à 1600 px).

Aucune règle ni donnée modifiée.
