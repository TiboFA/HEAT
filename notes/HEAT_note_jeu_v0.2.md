# HEAT — version jouable v0.2

Fichier : `HEAT_jeu_v0.2.html`, autonome, aucune dépendance, s'ouvre par double-clic.

## Ce qui change depuis la v0.1

Trois demandes, trois réponses.

### 1. Les leviers sont expliqués

Chaque carte porte désormais un bouton **i** qui ouvre une fiche complète. Elle contient :

- l'**effet de jeu** chiffré ;
- le **mécanisme** — pourquoi le levier agit, physiquement ou politiquement ;
- l'**ancrage réel** avec source et date ;
- la **limite** — pourquoi il peut rater, et par quoi il se fait contrer ;
- coût affiché et **coût réel** après application de votre doctrine ;
- latence, portée, réversibilité, robustesse, usages restants ;
- l'**alignement doctrinal**, détaillé axe par axe ;
- pour les leviers ciblés, le **rendement attendu bloc par bloc**, trié ;
- le **contre-levier** adverse, nommé et décrit.

Le survol de la carte donne déjà le mécanisme et l'ancrage, sans ouvrir la fiche.

### 2. Le pool passe de 25 à 77 leviers

Les 75 leviers retenus du catalogue sont implémentés, plus A44 et A47.

| Camp | Nombre |
|---|---|
| Climato-actif | 40 |
| Climato-attentiste | 31 |
| Pièges (proposés au camp actif) | 6 |

**Arbitrage tranché au passage.** A44 (captage industriel) et A47 (hydrogène industrie et maritime) étaient en « à tester » alors que leurs pièges jumeaux P07 et P04 étaient retenus. Les garder dehors rendait la paire incompréhensible : le joueur voyait le piège sans jamais voir l'usage légitime de la même technologie. Ils sont donc remontés dans le noyau, avec un renvoi explicite d'une fiche à l'autre.

**Épuisement.** Un levier mondial ne se joue qu'une fois par partie. Un levier de bloc se joue sur trois blocs au maximum, et jamais deux fois sur le même. Sans cette règle, le pool élargi se réduisait à répéter le meilleur levier.

La main passe de 5 à 7 cartes.

### 3. La doctrine pilote ce qui vous est proposé

Quatre réglages persistants, réglés à l'accueil, ajustables en cours de partie.

| Axe | Camp actif | Camp attentiste |
|---|---|---|
| d1 | contraindre ↔ inciter | nier ↔ retarder |
| d2 | compensation sociale : aucune ↔ élevée | attiser ↔ rassurer |
| d3 | priorité : blocs riches ↔ blocs émergents | terrain défendu : idem |
| d4 | horizon assumé : 2030 ↔ 2060 | gagner le tour ↔ verrouiller la décennie |

Chaque levier porte un vecteur d'affinité sur ces axes. La doctrine agit à deux endroits :

**Sur le tirage.** Le poids d'une carte vaut `0,30 + 1,40 × affinité`. Une carte parfaitement alignée est environ quatre fois plus probable qu'une carte opposée — mais aucune n'est jamais rendue inaccessible. C'est un biais, pas un filtre : vous verrez toujours passer des leviers hors de votre ligne, et c'est voulu.

**Sur les effets.** Alignement sur d1 : contrainte ±22 %. Sur d4 : ±18 %. Sur d3 : ±30 % selon la richesse du bloc visé. La compensation sociale (d2) réduit la friction générée jusqu'à −45 %, au prix d'un point de capital par mesure. L'horizon long rend les leviers à latence moins chers d'un point, l'horizon court les surtaxe.

**Coût de l'ajustement en partie.** Le premier déplacement d'un tour coûte 1 attention, et le total déplaçable est plafonné à 25 points par tour. On ne change pas de doctrine tous les tours sans le payer.

### 4. Les leviers encadrent la carte

La colonne unique de droite est remplacée par deux colonnes, une de chaque côté de la carte du monde. La carte gagne environ 40 % de largeur, et les sept leviers sont lisibles sans défilement sur un écran standard.

La répartition n'est pas arbitraire : les leviers qui agissent sur le réel — réglementaires, économiques, technologiques, internationaux — vont à gauche ; ceux qui agissent sur l'opinion et le pouvoir — narratifs, électoraux, judiciaires, institutionnels — vont à droite. Les colonnes sont ensuite rééquilibrées pour ne jamais différer de plus d'une carte, ce qui peut déplacer un levier de l'autre côté. Les en-têtes n'annoncent donc pas d'axe, seulement un décompte : un libellé qui ment de temps en temps est pire que pas de libellé.

La doctrine est en haut à gauche, repliée ; le journal en bas à droite. L'indication « choisissez un bloc » apparaît dans la colonne où se trouve la carte sélectionnée.

## Ce que le calibrage donne

Mesuré sur 14 parties par configuration, adversaire compris.

| | niveau 1 | niveau 2 | niveau 3 | niveau 4 |
|---|---|---|---|---|
| Joueur actif | 2,33 °C | 2,45 °C | 2,52 °C | 2,51 °C |
| Joueur attentiste | 2,55 °C | 2,33 °C | 2,23 °C | 2,23 °C |

Ne rien faire donne **3,48 °C**, invariablement. La meilleure partie observée sur l'ensemble des simulations atteint 1,97 °C.

Les paramètres ont été resserrés par rapport à la v0.1 : régénération de ressources ramenée de 5 à 4 par tour, facteur de réduction des émissions de 0,60 à 0,45, adversaire jouant de 1 à 6 cartes selon le niveau. Sans cela, le pool élargi rendait la partie trop facile — les premiers essais tombaient à 1,7 °C, ce qui aurait vendu un mensonge confortable.

## Ce qui reste ouvert

**Le camp attentiste est toujours moins riche à jouer que l'actif.** Ses 31 leviers agissent surtout sur la perception et la friction, et le retour visuel est plus faible : on voit une jauge d'opinion baisser, pas une infrastructure se construire. T43 (verrouillage) et T33 (contrôle des médias) sont les seuls vraiment cumulatifs. C'est le prochain chantier si l'exigence d'équivalence entre les deux rôles doit tenir.

**Le choix du bloc d'origine** reste écarté, à votre demande.

**La colonne d'interface devient longue** avec 7 cartes en main. La doctrine est repliée par défaut pour compenser, mais un affichage en grille ou un filtre par famille serait plus confortable au-delà.

**L'IA choisit ses leviers par une liste de priorités écrite à la main.** Elle est plus large qu'en v0.1 mais reste une heuristique, pas une évaluation. Elle joue correctement, pas finement.

## Rappel de méthode

Le jeu ne modélise pas le climat. Il applique une relation linéaire entre CO₂ cumulé et température — `T = 1,0 + 0,00058 × cumul depuis 2015` — qui est la forme réduite du TCRE du GIEC AR6, avec le forçage non-CO₂ replié dedans. C'est un choix, pas un raccourci : un modèle plus fin donnerait une fausse impression de précision sur une mécanique de jeu qui, elle, est délibérément grossière.

Les valeurs de départ des huit blocs, les seuils, et les ordres de grandeur des dommages viennent des sources listées dans les notes de conception v1 à v3. Chaque fiche de levier porte sa propre source datée, vérifiable indépendamment.
