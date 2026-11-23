# HEAT — version jouable v0.16

## v0.16 — nouvelle disposition du plateau

Intégration des huit points de `cadrage/HEAT_maquettes_ergonomie_v1.html`. Aucune règle ne change.

### Ce qui change

1. **Une seule main, en bas.** Les douze cartes, autrefois réparties en deux colonnes de part et d'autre de la carte, sont dans un bandeau horizontal sous le plan. Trois tris sont mémorisés : jouables d'abord, par puissance, par famille. Les commandes de la main (renouveler, à venir, masqués) sont sur la même ligne.
2. **Une ligne « Ce tour ».** Les trois cadres du haut (événement, objectif, défi) et l'agenda « quoi qu'il arrive » sont remplacés par une ligne de pastilles. Le détail est dans l'infobulle de chacune. L'événement garde son bouton d'attribution, puisque c'est une action. Les entrées de l'agenda qui répétaient l'événement ont disparu.
3. **Le plan, collé à la main.** Une ligne : les leviers engagés (réordonnables), la puissance utilisée sur le budget, le coût, la projection 2100 et le score avec leur variation, et « tout retirer ».
   *Écart avec la maquette* : quand le plan est vide, il reste une ligne d'aide d'une phrase au lieu de disparaître. Sans elle, la cinquième étape du guide n'aurait rien à montrer, et un nouveau joueur ne saurait pas où apparaît son plan.
4. **Des cartes lisibles.** Une ligne d'en-tête (identifiant, portée, doctrine en un mot : aligné, neutre ou opposé), le titre, l'effet sur deux lignes, puis la puissance et le coût en clair (« 2 pts · 4 politique ») aux couleurs des ressources. Les particularités passent en petites mentions : dans le plan, objectif, rejouable, à vérifier, délai, seuil, pari, combo, raison d'impossibilité. La barre « doctrine » en pourcentage a disparu. La vue compacte, devenue inutile, aussi.
5. **Le geste guidé sur la carte.** Quand un levier de bloc est sélectionné :
   - une consigne s'affiche au-dessus de la carte : le levier, le nombre de blocs possibles, Échap ou « annuler » ;
   - les blocs possibles s'allument, les autres s'estompent ;
   - chaque bloc impossible dit pourquoi, sous sa pastille : « perçu 30 / 45 », « déjà dans le plan »… Sur téléphone, seule la consigne reste : les raisons y seraient illisibles.
   - **Échap** annule la sélection.
6. **La doctrine en une ligne**, dans la colonne de droite, avec « régler ».
7. **Un seul tableau de bord** : quatre tuiles sous la carte (réchauffement, projection 2100, émissions, score). Chacune donne sa variation au dernier tour, ou celle que produirait le plan en cours. Une ligne discrète garde l'indice technologique, les décès et les dommages. Le graphique de trajectoire est passé dans le bilan de tour, auquel mène un lien sous les tuiles.
8. **Un seul vocabulaire** : Politique, Capital, Attention, Crédibilité, Puissance, avec les mêmes mots et les mêmes couleurs dans la barre du haut, sur les cartes et dans le plan. La barre du haut affiche la puissance restante (« 3 / 5 »), en jauge de demi-points sur les écrans larges.

### Aussi

- **Le journal remplit la place libre** de la colonne de droite au lieu d'avoir un ascenseur au-dessus d'un vide. Il ne défile que si son contenu dépasse.
- **Le panneau du camp adverse est replié par défaut.** Replié, il donne le budget adverse et le nombre de leviers joués au dernier tour.
- **Le guide est réécrit** pour la nouvelle disposition, toujours en huit étapes : carte, ce tour, leviers, plan, adversaire, tableau de bord, doctrine, fin de tour.

### Vérification

`outils/verifier.py` (30 parties par configuration) : tout passe, étalonnage identique à la v0.15.7. Les huit étapes du guide trouvent leur zone, et le graphique de trajectoire s'affiche dans le bilan. Rendu contrôlé à 1 440, 1 920 et 390 px de large, sans débordement horizontal.
