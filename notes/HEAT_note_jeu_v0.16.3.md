# HEAT — version jouable v0.16.3

## v0.16.3 — le panneau « partie » et le catalogue passent au style filaire

Avec cette version, tous les écrans du jeu sont au même style.

### Panneau « partie »
- **Une ligne d'état** en chasse fixe : camp, niveau, scénario, réchauffement et projection 2100.
- **Trois cadres filaires** (sauvegarde automatique, fichier de partie, recommencer), avec coins de cadre et léger quadrillage.
- **Un voyant de sauvegarde automatique** : vert si une sauvegarde existe, jaune si elle est active mais vide, orange si le navigateur bloque le stockage.
- **« Exporter la partie »** en bouton vert d'eau ; les autres boutons sont en contour.

### Catalogue « à venir »
- **Une frise des trois époques** (2015, 2035, 2055), avec la part écoulée en vert d'eau et un repère orange sur l'année en cours.
- **Les identifiants** en chasse fixe vert d'eau, **les conditions d'ouverture** en chasse fixe.

### Correction
La classe des tuiles du tableau de bord (`.tl`, ajoutée en v0.16) portait le même nom que le coin « haut gauche » des cadres filaires. Les coins du guide, du bilan, de l'écran de fin et des fiches avaient donc depuis la v0.16 un arc parasite en haut à gauche. La classe des tuiles s'appelle désormais `.tuile`.

Aucune règle ne change ; `outils/verifier.py` passe.
