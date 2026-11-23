# HEAT — version jouable v0.15.8

## v0.15.8 — masquer un levier, réduire le camp adverse

Deux demandes, en attendant la refonte de l'ergonomie (propositions à part).

### Masquer un levier

Chaque carte de la main porte un bouton ⊘ (visible au survol ; toujours visible sur écran tactile).
- Le levier quitte la main et **ne vous est plus tiré de la partie**. Le tirage, l'objectif du tour et la garantie du levier clef l'ignorent tous les trois.
- **Sa place est remplie au tour suivant**, pas tout de suite. Sinon, masquer servirait à renouveler sa main gratuitement, ce qui coûte normalement 1 attention.
- On ne peut pas masquer un levier engagé dans le plan.
- Le lien « N masqués », au-dessus de la main, ouvre la liste. On peut y réafficher un levier, ou tous ; un levier réaffiché revient dans le tirage.
- Les leviers masqués font partie de la partie (`s.masques`) : ils sont conservés par la sauvegarde. Seule la main du joueur est concernée, jamais celle de l'adversaire.

### Réduire le panneau du camp adverse

Un lien « réduire » dans l'en-tête « Le camp adverse » replie le panneau. Il ne reste qu'une ligne avec le budget adverse et le lien « afficher ». Le réglage est mémorisé dans le navigateur. À 1 440 px de large, la colonne de droite perd environ 190 px de hauteur.

Aucune règle ne change ; `outils/verifier.py` passe.
