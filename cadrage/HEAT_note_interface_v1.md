# HEAT — Note d'interface v1

**Objet :** proposition d'interface, écran de tour
**Date :** 18 août 2026
**Accompagne :** `HEAT_interface_v1.html` (maquette interactive, à ouvrir dans un navigateur)

---

## 1. Ce que la maquette montre, et ce qu'elle ne montre pas

Elle montre **l'écran de tour** — la couche 1 de l'architecture décidée en v2 : trois à cinq décisions,
moins de deux minutes, tout le reste consultable et jamais imposé.

Le bouton en haut bascule entre les deux camps. C'est **le même écran** : mêmes couleurs, même charte,
même disposition. Seuls la main et le tableau de bord changent. Rien dans l'habillage ne désigne un camp
comme le fautif — c'est la traduction visuelle de la règle posée en v3.

Le sélecteur de difficulté est fonctionnel dans la maquette : en **Découverte** le piège de la main porte
un badge, à partir de **Standard** il disparaît et le libellé de la main cesse d'annoncer combien de pièges
elle contient. C'est le mécanisme d'inoculation, rendu visible.

Les chiffres sont plausibles, pas calculés. Aucun moteur derrière.

**Non traité ici :** les écrans de doctrine détaillée, de modèle, de fin de partie, de bloc, ainsi que
l'onboarding, les animations de transition et le choix du pays — mis de côté à ta demande.

---

## 2. Les six principes

### 1. Une décision à la fois
Quatre cartes proposées, trois actions par tour. Le reste — blocs, courbe, compteurs — est du contexte,
pas de la décision. C'est ce qui rend l'écran portable sur mobile sans le réécrire : sur petit écran, on
garde la main et le compteur principal, on replie le reste en onglets.

### 2. Les deux jauges, toujours côte à côte
**Soutien réel** en barre pleine, **soutien perçu** en contour hachuré. L'écart entre les deux se voit
avant d'être lu. C'est la signature visuelle du jeu, et le joueur attentiste apprend en deux tours qu'il
ne combat jamais la barre pleine — seulement la creuse.

La forme et l'étiquette portent l'information, la couleur ne fait que renforcer. Rien n'est lisible par
la seule teinte.

### 3. La ligne fantôme n'est jamais masquable
Le monde réel 2015-2025 reste sur le graphe en permanence, en gris pointillé, avec son point d'arrivée
annoté à 2,6 °C. Le joueur ne joue pas contre un objectif abstrait, il joue contre ce qui s'est
réellement passé. C'est aussi ce qui rend le score « réchauffement évité » lisible sans explication.

### 4. La latence est écrite sur la carte
`Immédiat` · `1-2 tours` · `3-5 tours` · `> 5 tours`. C'est la première source d'incompréhension d'un jeu
à effets différés : elle doit être lisible **avant** le clic. Le vert signale l'effet immédiat, le gris
l'effet lointain — le joueur comprend en une partie que le camp actif dispose de très peu de vert.

### 5. La source est à un clic, jamais imposée
Chaque carte porte son ancrage réel daté, au survol de la mention « source ». Ça ne coûte rien à qui ne
veut pas le lire, et c'est ce qui distingue HEAT d'un jeu militant. Dans la version finale, la même
mention ouvre le lien.

### 6. Aucune interface accusatrice
Le camp attentiste a les mêmes couleurs, et **ses compteurs montent** : valeur d'actifs préservée en
chiffre héros, mesures évitées, années de report gagnées. Pas de rouge clignotant, pas de jauge de
culpabilité, pas de narrateur.

Le seul endroit où le jeu dit quelque chose, c'est le bloc **Dommages subis**, visible uniquement côté
attentiste : deux barres, sa base et les autres, et une phrase factuelle sur le seuil de retrait
assurantiel. Les chiffres, et l'écart. Rien d'autre.

---

## 3. Inventaire des écrans à produire

| # | Écran | Couche | Priorité | Contenu |
|---|---|---|---|---|
| 1 | **Tour** | 1 | Maquettée | Blocs, trajectoire, événement, main, tableau de bord |
| 2 | **Doctrine** | 2 | Esquissée | Réglages persistants ; présente en bandeau dans la maquette, mérite un écran propre |
| 3 | **Bloc** | 1 | À faire | Détail d'un bloc : régime, mesures en vigueur, friction, historique des jauges |
| 4 | **Modèle** | 3 | À faire | Équations, tables, sources, comparaison à la décennie réelle. Consultable, jamais obligatoire |
| 5 | **Fin de partie** | — | À faire | Les deux courbes de dommages côte à côte, le réchauffement évité, une phrase factuelle |
| 6 | **Sélection de partie** | — | En attente | Camp, difficulté, année de départ — et le choix du bloc quand il sera tranché |

---

## 4. Dégradation vers le web et le mobile

L'écran est conçu en trois colonnes pour le bureau. La règle de repli :

- **Web / tablette (< 1180 px)** — les trois colonnes s'empilent, la main passe à deux cartes par ligne.
  C'est déjà le comportement de la maquette.
- **Mobile** — on ne garde en première vue que **la main et le chiffre héros**. Blocs, trajectoire et
  compteurs deviennent trois onglets. Aucune information ne disparaît, elle change de profondeur.

C'est possible parce que la couche 1 ne contient qu'une décision. Si l'écran de tour avait besoin de
tout afficher simultanément, le portage mobile serait impossible — c'est le piège dans lequel tombe
En-ROADS, qui ouvre sur la couche 3.

---

## 5. Choix visuels et accessibilité

Palette de données validée pour le mode sombre (surface `#1a1a19`) : bande de luminosité, plancher de
chroma, séparation daltonisme sur les paires adjacentes, contraste sur la surface — tous les contrôles
passent.

Affectation des couleurs **par entité, jamais par rang** :

| Entité | Rôle | Teinte |
|---|---|---|
| Trajectoire de la partie | série 1 | bleu `#3987e5` |
| Monde réel | référence, pas une série | gris `#898781`, pointillé |
| Soutien réel | série 3 | vert d'eau `#199e70`, plein |
| Soutien perçu | série 4 | jaune `#c98500`, contour hachuré |
| Dommages — base du joueur | série 7 | violet `#9085e9` |
| Dommages — les autres | série 2 | orange `#d95926` |
| Retour de flamme | statut critique | rouge `#d03b3b`, **avec icône et libellé** |

Encodage secondaire systématique : plein contre contour, étiquettes directes, libellés explicites. Une
vue tableau est disponible sous le graphe. Aucune information n'est portée par la couleur seule.

---

## 6. Ce que je changerais avant de coder quoi que ce soit

**La carte du monde.** La maquette utilise une liste de blocs plutôt qu'une carte géographique. C'est
volontaire : une carte est jolie et illisible pour comparer huit paires de jauges. Si tu veux une carte,
il faut qu'elle soit un écran séparé, pas le tableau de bord principal.

**Le nombre de blocs.** Huit blocs occupent toute une colonne. À six on gagne en lisibilité, à quatre le
dilemme du passager clandestin s'appauvrit. Huit me semble le maximum tenable.

**Le bandeau doctrine.** Il est dans la colonne centrale par commodité de maquette. À terme il devrait
être un écran à part, accessible entre deux tours, pour ne pas encombrer la décision du tour.

---

## 7. Prochaine étape proposée

Tester la maquette sur trois personnes qui ne connaissent pas le projet, avec une seule consigne :
*« explique-moi ce que tu peux faire ce tour-ci, et ce que ça va produire. »* Si la latence et l'écart
réel/perçu ne sortent pas spontanément, c'est l'interface qu'il faut corriger, pas le joueur.
