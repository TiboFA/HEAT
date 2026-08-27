# HEAT — version jouable v0.1

**Fichier :** `HEAT_jeu_v0.1.html` — un seul fichier, à ouvrir dans un navigateur. Aucune installation.
**Date :** 18 août 2026

---

## Ce qui est jouable

Une partie complète : **8 tours de 5 ans, de l'Accord de Paris (décembre 2015) à 2055**, puis
extrapolation jusqu'en 2100. Vous choisissez votre camp et votre niveau de difficulté, l'autre camp est
tenu par la machine.

**Trois actions par tour.** Vous cliquez une carte, puis un bloc sur la carte du monde. Les blocs
éligibles s'éclairent, les autres restent inertes et la carte vous dit pourquoi (perçu insuffisant,
bloc préempté, ressources manquantes).

L'attribution d'un événement est une **action gratuite** qui coûte 1 attention : c'est délibéré, pour
que le joueur l'utilise et comprenne la règle.

---

## Le modèle, en clair

**Climat.** Une ligne : `T = 1,0 + 0,00058 × CO₂ cumulé depuis 2015`. Le coefficient est la TCRE du GIEC
AR6 (0,45 °C par 1 000 GtCO₂ pour le CO₂ seul) majorée du forçage non-CO₂ co-émis, que le jeu ne suit
pas séparément.

**Émissions.** Huit blocs, 35,5 GtCO₂/an en 2015, répartis selon les parts réelles. Chaque bloc a une
croissance tendancielle qui s'amortit, et une **contrainte** de 0 à 100 qui la contrarie :
`émissions = émissions × (1 + croissance) × (1 − (contrainte/100)^0,8 × 0,60)`.

**Trois repères calibrés**, et c'est ce qui rend le jeu vérifiable :

| Trajectoire | Projection 2100 |
|---|---|
| Personne n'agit | **3,48 °C** — la projection réelle de 2015 était 3,6 °C |
| Le monde réel 2015-2025, prolongé | **2,60 °C** — la ligne grise du graphe, valeur du Climate Action Tracker |
| Une partie bien jouée | **2,0 à 2,3 °C** |
| Le plafond du plausible | **sous 1,9 °C**, quasi hors d'atteinte contre un adversaire à Réaliste |

Le score du camp actif est le **réchauffement évité** : 3,48 moins votre projection. C'est un chiffre
positif dans un contexte négatif — exactement ce dont le message a besoin.

---

## Les mécaniques qui font le jeu

**Quatre jauges par bloc**, dans l'ordre des barres de la pastille : contrainte, soutien réel, soutien
perçu, friction.

- Le **perçu** conditionne l'adoption. Une interdiction datée exige 55 de perçu ; un marché de quotas 45.
  En régime autoritaire il n'y a aucun seuil d'opinion, mais chaque mesure coûte un capital de plus.
- Le **réel** ne se combat pas. Il monte tout seul avec les dommages subis et avec l'éducation. C'est la
  seule jauge que l'adversaire ne peut pas attaquer — et c'est ce qui rend « Révéler la majorité »
  décisive : elle convertit un stock que vous avez patiemment construit.
- La **friction** s'accumule à chaque mesure. Au-delà de 55, retour de flamme : une mesure est annulée,
  le perçu chute de 8. La redistribution du produit de la taxe est la seule parade, et elle ne rapporte
  aucun point. C'est le cœur pédagogique du jeu.
- La **contrainte** est plafonnée. Le verrouillage d'infrastructure adverse abaisse ce plafond
  définitivement : ce que l'adversaire coule ne se déverrouille pas.

**Élections** tous les deux tours dans les blocs démocratiques : au-dessus de 50 de perçu vous gagnez du
capital politique, en dessous l'adversaire gagne du capital et la friction retombe.

**Courbe d'apprentissage.** L'indice technologique monte avec les subventions au déploiement. À 30, votre
capital devient plus efficace. À 40, les blocs déjà contraints progressent seuls. C'est le seul levier
dont l'effet est mondial et gratuit pour les autres — le passager clandestin inversé.

**Verrous.** La loi-cadre rend les mesures d'un bloc inannulables, y compris par le retour de flamme.
C'est la voie de victoire du camp actif : accumuler des irréversibles juridiques plus vite que
l'adversaire n'accumule du béton.

---

## L'adversaire

Une heuristique en six priorités, dans cet ordre : démonter les blocs les plus contraints, verrouiller
l'infrastructure des gros blocs encore ouverts, faire tomber le perçu là où il approche d'un seuil,
préempter un bloc démocratique bien orienté, ajouter de la friction là où il y a des mesures, saturer
l'attention quand un événement est attribuable.

Le niveau de difficulté change **combien de cartes il joue** (1, 2, 3, 4) et **quelles cartes existent** :
la capture réglementaire n'apparaît qu'en Réaliste, la préemption en Standard.

---

## Ce que la v0.1 ne fait pas encore

- **Pas de choix du pays.** Vous jouez le camp, pas un bloc. C'est la prochaine grande décision.
- **Pas de sauvegarde.** Une partie se joue d'un trait, une vingtaine de minutes.
- **Pas de deck construit.** La main de cinq cartes est tirée au hasard dans le pool disponible.
  Un draft en début de partie serait un vrai gain stratégique.
- **26 cartes sur les 75 retenues** au catalogue. Les 49 autres attendent d'être validées en jeu.
- **Le troisième camp** (développement du Sud) n'existe pas.
- **Pas de son, pas d'animation.** L'écran de fin est sobre par choix.

---

## Ce que je regarderais en premier en jouant

1. **Est-ce qu'on comprend la latence ?** L'interdiction datée agit au tour suivant. Si le joueur la joue
   au tour 8, il a perdu une action et il doit s'en rendre compte tout seul.
2. **Est-ce que le retour de flamme se voit venir ?** La friction est visible sur la pastille et dans la
   fiche. Si le joueur le subit sans l'avoir anticipé, c'est un défaut d'interface.
3. **Est-ce qu'on va chercher la Chine ?** Elle pèse 30 % des émissions. Un joueur qui répartit ses
   mesures également entre les huit blocs perd. C'est un enseignement, pas un piège.
4. **Est-ce que la partie est trop facile en Standard ?** Les essais automatiques donnent 2,0 à 2,5 °C
   pour un jeu engagé. Si un humain descend systématiquement sous 2,0 °C, il faut durcir.

---

## Note technique

Un seul fichier HTML, sans dépendance ni réseau. La carte est un tracé Natural Earth simplifié et fusionné
par bloc, embarqué en SVG. Le moteur, l'interface et l'adversaire tiennent en environ 900 lignes de
JavaScript. Aucun stockage local : rafraîchir la page recommence une partie.
