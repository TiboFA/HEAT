# HEAT — Note d'interface v3

**Objet :** corrections demandées sur la carte, les pastilles, les couleurs et la mise en page
**Date :** 18 août 2026
**Remplace :** `HEAT_interface_v2.html`

---

## Les cinq corrections

### 1. Plus de trous dans la carte
Les zones sombres au milieu de l'Afrique venaient de la méthode : chaque pays était simplifié
**indépendamment**, si bien que des frontières voisines ne se rejoignaient plus après simplification et
laissaient des fentes noires.

Correction : les pays sont désormais **fusionnés géométriquement en un seul polygone par bloc** avant
simplification (union, puis simplification de l'union). Il n'existe plus de frontière interne, donc plus
aucune fente possible. Les seuls creux restants sont réels — les grands lacs africains.

Effet secondaire voulu : la carte est plus lisible. Un bloc est une surface, pas une mosaïque de pays.

### 2. Pastilles compactes, ouverture au survol
Par défaut, chaque bloc porte une **pastille de 40 px** : trois barres miniatures et le code du bloc
(AN, EU, GR, CN, IN, AS, AF, AL). Elle occupe une fraction de la surface qu'occupaient les cartouches
de la v2.

Au survol : la pastille grossit légèrement et une **fiche compacte s'ouvre par-dessus** — nom du bloc,
part des émissions, les trois valeurs chiffrées, et l'alerte de retour de flamme le cas échéant. Le bloc
correspondant s'éclaire sur la carte au même moment.

### 3. Friction séparée du perçu
Le jaune de la friction et le jaune du perçu étaient effectivement trop proches — le contrôle de palette
le confirme : `#ec835a` contre `#c98500`, écart de 9,0 en vision normale, sous le plancher de 15.

Correction : **la friction passe au rouge statut `#d03b3b`**. Vérifié : écart de 16,9 contre le perçu et
de 19,4 contre le réel en vision normale, tous les contrôles passent en mode sombre. Le rouge est aussi
plus juste sémantiquement — la friction est une tension, pas une opinion.

### 4. Clic sur un bloc → fiche détaillée
La modale contient :

- les **trois jauges en grand**, avec l'écart réel/perçu chiffré et le seuil de retour de flamme ;
- le **profil du bloc** : régime politique, PIB par habitant, dépendance à la rente fossile, part des émissions ;
- les **mesures en vigueur** dans ce bloc ;
- l'**historique des jauges** sur les quatre derniers tours ;
- une **note stratégique** propre au bloc.

C'est là que se logera plus tard la couche 3 : quels leviers sont disponibles ici et pourquoi, ce que le
régime politique autorise, l'historique complet.

### 5. Trajectoire sous la carte
La trajectoire 2100 avec ligne fantôme occupe désormais toute la largeur sous la carte, en grand format
et avec infobulle par année. Elle a gagné en lisibilité par rapport au format colonne de la v2, et la
colonne de droite ne contient plus que des leviers.

---

## Ce que le profil du bloc introduit sans le dire

En remplissant les fiches, une règle de jeu s'est imposée d'elle-même : **le régime politique détermine
quels leviers fonctionnent**.

- Golfe & Russie, régime autoritaire, rente fossile très élevée : les campagnes d'opinion n'y produisent
  presque rien. Soutien réel 41, le plus bas du plateau.
- Afrique : soutien réel le plus élevé (74) et capacité d'agir la plus faible. Le financement Nord-Sud
  est le seul levier qui compte.
- Inde : écart réel/perçu de 28 points, le plus fort du plateau — cible idéale de « Révéler la majorité ».

Ce n'est pas une décoration : c'est ce qui rendra les huit blocs réellement différents à jouer, et c'est
le prérequis du choix du pays quand tu voudras l'ouvrir.

---

## Reste à trancher

- **Les pastilles se chevauchent-elles à petite taille ?** À vérifier en dessous de 1200 px de large.
  Prévoir un décalage automatique si deux pastilles se recouvrent.
- **Le clic sur la surface du bloc ouvre aussi la fiche.** À confirmer : c'est pratique, mais ça peut
  gêner si on ajoute plus tard un glisser-déposer de carte sur un bloc.
- **Codes de bloc à deux lettres** (AN, GR, AL) : lisibles mais pas évidents. Alternative : afficher le
  nom complet au survol seulement, ce qui est déjà le cas — les codes ne servent qu'à repérer.
