# HEAT — version jouable v0.15.5

## v0.15.5 — le bilan de tour passe au style filaire

### Une mini-carte de ce qui a bougé

En tête de la colonne « Les huit blocs », une carte filaire du tour qui vient d'être résolu :
- **la variation de contrainte** de chaque bloc, en vert si elle vous sert, en orange sinon ;
- **les blocs où rien n'a bougé** (contrainte, réel, perçu, friction) sont estompés ;
- **les blocs où l'adversaire a joué ce tour** sont tracés en orange.

Le tableau chiffré des huit blocs reste en dessous, inchangé.

La carte de l'écran de fin et celle du bilan partagent désormais une seule fonction, `carteFilaire()`.

### Le reste du bilan

- Intitulés de section en vert d'eau ; valeurs et codes de bloc en chasse fixe ; séparateurs teintés.
- Les leviers joués par l'adversaire sont marqués en orange, comme sur le plateau.
- Sur téléphone, les valeurs passent en 11 px et peuvent revenir à la ligne. Sans cela, la chasse fixe, plus large, faisait déborder la colonne de 36 px. Contrôlé sans débordement de 360 à 1 440 px de large.

Aucune règle ne change ; `outils/verifier.py` passe.
