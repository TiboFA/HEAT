# HEAT — version jouable v0.8

Fichier : `HEAT_jeu_v0.8.html`, autonome, aucune dépendance, s'ouvre par double-clic.

## v0.8 — le niveau de difficulté ne règle plus que l'adversaire

La v0.7 avait laissé une anomalie mesurée : côté actif, le niveau 1 était plus difficile que le niveau 2. Ce chantier la traite. Il a fallu d'abord comprendre ce que le curseur réglait réellement.

### Ce que le curseur faisait, sans le dire

Le niveau commandait trois choses à la fois : **l'adversaire** (nombre de leviers par tour, revenus), **votre propre catalogue** (`c.lvl <= s.level`), et **les aides** (leviers douteux signalés, seuils de soutien perçu abaissés de 10). Un joueur qui choisissait « Découverte » pour affronter un adversaire plus faible se retrouvait aussi avec 31 leviers actifs sur 46 au lieu du répertoire complet — et ce handicap-là pesait plus lourd que l'adversaire allégé.

Trois mesures, 24 à 30 parties par configuration :

| | niveau 1 | niveau 2 | niveau 3 | niveau 4 |
|---|---|---|---|---|
| Score du joueur actif, v0.7 | 322 | 405 | 387 | 302 |
| Le même, catalogue ouvert à tous les niveaux | 386 | 392 | 387 | 302 |

Ouvrir le catalogue supprimait l'anomalie — et découvrait la suivante : les niveaux 1, 2 et 3 devenaient **indiscernables** (386 / 392 / 387). Le seul vrai palier était le quatrième.

### Pourquoi le curseur de l'adversaire ne mordait pas

Le barème promettait 2, 3, 4 puis 6 leviers adverses par tour. Compté sur 340 tours de partie :

| niveau | leviers promis | leviers réellement joués | tours écourtés faute de ressources |
|---|---|---|---|
| 1 | 2 | 2,00 | 0 |
| 2 | 3 | 2,99 | 2 |
| 3 | 4 | 3,50 | 126 |
| 4 | 6 | 4,18 | 285 |

Au niveau Réaliste, l'adversaire n'avait de quoi payer que trois leviers et demi sur les quatre annoncés ; au niveau Expert, quatre sur six. **L'agenda du tour et le panneau « le camp adverse » — les deux endroits où la v0.6 s'était donné pour tâche de rendre l'adversaire visible — annonçaient donc un chiffre faux d'un tiers, puis de moitié.** C'était le défaut le plus gênant des trois : pas un déséquilibre, une promesse non tenue.

### Ce qui change

**Le niveau ne règle plus que l'adversaire.** Le champ `lvl` a été retiré des 91 leviers, et les quatre endroits qui le lisaient avec lui. Le catalogue est entier dès le premier niveau, pour les deux camps. Ce qui l'ouvre au fil de la partie, ce sont les époques et les prérequis introduits en v0.6 — depuis, le filtrage par difficulté faisait doublon avec eux.

**L'adversaire est financé à hauteur de ce qu'on lui demande.** Nouveau barème, et des revenus supplémentaires qui ne vont qu'au camp que vous ne jouez pas :

| | Découverte | Standard | Réaliste | Expert |
|---|---|---|---|---|
| leviers adverses par tour | 2 | 3 | 4 | 5 |
| supplément de capital politique | 0 | +2 | +4 | +6 |
| supplément de capital | 0 | +3 | +7 | +11 |

Mesuré à nouveau : **2,00 · 3,00 · 4,00 · 4,99**. Le nombre annoncé est désormais le nombre joué.

**Les aides restent attachées au niveau Découverte** — c'était le choix retenu — mais elles vont maintenant au joueur quel que soit son camp, alors qu'elles allaient au camp actif même quand il était tenu par la machine.

**Les descriptions de l'accueil étaient fausses d'un cran** — « Standard : l'adversaire joue deux cartes par tour » alors que le moteur en donnait trois, « Expert : quatre cartes » pour six. Elles sont réécrites, et ne parlent plus que de l'adversaire.

### Deux défis d'objectif corrigés au passage

Un défi de maintien dont l'échec est **irréversible** ne doit pas être tiré une fois qu'il est déjà perdu. Rien ne défait une loi-cadre, rien ne fait remonter les émissions après le pic : « Rien de verrouillé » et « Le pic n'est pas passé » étaient donc parfois donnés perdus d'avance. Ils portent maintenant une condition de tirage. « Rien de verrouillé » annonçait par ailleurs trois leviers clefs — T17, T20, T25 — dont **aucun ne retire un verrou** : la mention a été supprimée.

### Calibrage v0.8

Le harnais de calibrage a changé de politique de jeu. Jusqu'ici le joueur automatique prenait **le premier levier jouable de sa main** : or l'ordre de la main est l'ordre de tirage pondéré par la doctrine, il ne corrèle avec rien. Testé sur quatre politiques, l'échelle est monotone pour « le moins cher d'abord » (279 / 245 / 217 / 197), « le plus cher d'abord » (512 / 500 / 471 / 385) et « au hasard » — et pour elle seule, non monotone avec « le premier de la main ». L'anomalie résiduelle était une propriété du harnais, pas du jeu. La campagne de référence utilise désormais **un levier jouable tiré au hasard**, la politique la plus neutre des quatre.

Trente parties par configuration :

| | niveau 1 | niveau 2 | niveau 3 | niveau 4 |
|---|---|---|---|---|
| Joueur actif — température 2100 | 2,47 °C | 2,52 °C | 2,58 °C | 2,72 °C |
| Joueur actif — score | 441 | 390 | 358 | 284 |
| Joueur actif — seuil des 20 Gt franchi | 28/30 | 26/30 | 22/30 | 8/30 |
| Joueur attentiste — température 2100 | 2,46 °C | 2,21 °C | 2,07 °C | 1,93 °C |
| Joueur attentiste — score | 405 | 281 | 228 | 181 |

Ne rien faire donne toujours **3,48 °C** exactement. Les deux camps sont monotones sur les deux mesures, et la ligne « seuil franchi » donne une lecture directe de ce que coûte chaque cran : à Découverte on passe sous 20 GtCO₂/an neuf fois sur dix, à Expert une fois sur quatre.

Les sauvegardes de la v0.7 ne sont pas relues : les revenus et le sens du niveau ont changé, une partie reprise n'aurait pas été la même partie. Le message le dit.

### Ce qui reste ouvert

- **La colonne « Verdict » du catalogue xlsx**, toujours vide.
- **Le choix du bloc joué** — décider quel pays ou quelle région on incarne — reste en attente, à votre demande.
- **Le joueur automatique reste glouton.** Il ne planifie pas, ne vise pas les combinaisons, ne garde rien pour le tour suivant. Tous les chiffres de calibrage sont donc des planchers : un humain qui joue bien fait mieux, et l'écart entre les niveaux est probablement plus marqué qu'ils ne le disent.

---



## v0.7 — la sauvegarde, et un vrai camp attentiste

Deux chantiers, sans retouche du modèle physique.

---

### Chantier 1 — la sauvegarde

Une partie de dix-sept tours ne tient pas dans une session. Deux mécanismes volontairement distincts :

**La sauvegarde automatique.** Écrite dans le navigateur à la fin de chaque tour, au démarrage d'une partie et à la fermeture de l'onglet. À la réouverture du fichier, un bandeau vert en haut de l'accueil annonce la partie en cours — tour, année, camp, niveau, température, date d'enregistrement — avec *Reprendre*, *Charger un fichier* et *Effacer*. Rien ne se reprend tout seul : la reprise est un clic explicite.

**Le fichier de partie.** Un `.json` exporté depuis le panneau **partie** du bandeau du haut. Il survit au nettoyage du cache et se recharge sur une autre machine. C'est la vraie sauvegarde ; le stockage navigateur n'est qu'un confort, et il est bloqué dans certaines configurations — le panneau le dit alors explicitement au lieu d'échouer en silence.

Ce qui est écrit : l'état complet de la partie, plus les trois variables globales qui la déterminent et ne vivent pas dans l'état — **la graine du générateur pseudo-aléatoire** (sans elle, recharger changerait tous les tirages à venir et la reprise ne serait pas la même partie), l'échéance net zéro glissante, et les curseurs de doctrine mémorisés. Le défi du tour est stocké par son titre : c'est le seul objet de l'état qui porte des fonctions, donc le seul que JSON perd.

Une sauvegarde porte un numéro de version. Une partie enregistrée par une autre version est refusée avec un message qui le dit, et **rien n'est modifié** — c'est vérifié : après un fichier invalide, la partie en cours est intacte.

Vérification faite : partie jouée jusqu'au tour 5, rechargement complet de la page, reprise — tour, température, émissions, score, graine du générateur, main, journal, défi, événement et échéance net zéro sont **identiques au bit près**, et la partie continue normalement. Une sauvegarde pèse environ 24 ko au tour 5.

---

### Chantier 2 — le camp attentiste

Le camp comptait 31 leviers contre 46, cinq combinaisons contre neuf, et cinq familles contre sept. Il en compte maintenant **45**, avec neuf combinaisons et neuf familles.

**Un défaut plus gênant que le nombre de cartes.** Le joueur attentiste tirait ses objectifs de tour dans l'ensemble des défis, y compris les dix écrits pour le camp actif. Il recevait donc régulièrement des objectifs du type « amener deux blocs au-dessus de 15 de contrainte », et il était **récompensé quand son adversaire réussissait**. Chaque camp tire désormais dans ses propres objectifs. Il fallait pour cela en écrire : les trois défis attentistes existants sont passés à **onze**, répartis sur les cinq paliers de tour, avec leurs leviers clefs garantis en main comme pour le camp actif.

**Quatorze leviers, dans quatre familles que le camp n'avait pas.**

*Électoral* — le camp n'avait aucun levier électoral, alors que ses victoires les plus nettes dans le monde réel sont venues de là : une taxe abrogée après un scrutin tient mieux qu'une taxe contestée devant un juge.
- **T60 Référendum sur une mesure climatique** — soumet la dernière mesure du bloc au vote, jugé deux tours plus tard sur le soutien perçu du moment. Sous 50, la mesure tombe ; au-dessus, elle est confirmée et le bloc devient protégé du retour de flamme. Le seul levier symétrique du jeu : le camp actif peut le retourner en travaillant l'opinion pendant les deux tours. *Loi CO₂ suisse rejetée à 51,6 % en 2021 ; initiatives 732 et 1631 dans l'État de Washington, rejetées.*
- **T61 Coalition du coût de la vie** — friction +16, perçu −7, effet de moitié si la redistribution est installée. *Gilets jaunes 2018 ; « Axe the Tax » australienne.*
- **T62 Financement de campagne** — le prochain scrutin du bloc bascule quel que soit le perçu. *Citizens United, 2010.*
- **T63 Candidat de rupture** — sur le bloc démocratique au perçu le plus bas : contrainte −10, friction −12, bloc fermé deux tours. *Abrogation australienne de 2014, retraits américains de l'Accord de Paris.*

*International* — le camp actif avait trois leviers internationaux et l'attentiste aucun, alors que la règle du consensus est l'outil d'obstruction le plus efficace du régime climatique réel.
- **T64 Blocage du consensus** — sommets sans effet pendant trois tours, tous les effets différés retardés d'un tour. *Règle du consensus de la CCNUCC, appliquée depuis 1995 sans avoir jamais été formellement adoptée.*
- **T65 Clause de sauvegarde compétitivité** — annule l'ajustement carbone aux frontières partout où il était installé. *Contestations du MACF par l'Inde et la Chine, 2023-2024.*
- **T66 Alliance des producteurs** — plafond −7 sur les trois blocs à rente fossile la plus élevée, +3 capital. *Coordination OPEP+ depuis 2016.*

*Technologique* — le solutionnisme est un levier d'obstruction à part entière : il ne conteste pas l'objectif, il déplace la date.
- **T67 Promesse de captage à grande échelle** — contrainte −8 et perçu +4. *Capacité mondiale réellement opérationnelle de l'ordre de 50 MtCO₂/an, moins de 0,2 % des émissions, face à des annonces à l'échelle de la gigatonne depuis 2009.*
- **T68 Géo-ingénierie solaire à l'étude** — perçu −8 partout, mais indice technologique **+6**. Le seul levier du camp qui fasse progresser la courbe d'apprentissage adverse.
- **T69 Attente de la prochaine génération** — vide les effets différés en attente sur le bloc.
- **T70 Contestation du bilan carbone** — indice technologique −7 et seuils de la courbe neutralisés deux tours.

*Réglementaire* — le camp obtenait des reculs par le discours et le contentieux, jamais par la norme, alors que c'est là que se joue l'essentiel du retard réel.
- **T71 Moratoire réglementaire** — bloc fermé un tour, friction −10. *Gels réglementaires à l'entrée en fonction des administrations américaines, pratique constante depuis 1981.*
- **T72 Étude d'impact préalable** — annule le prochain effet différé du bloc. *Analyse coût-bénéfice de l'ordre exécutif 12866.*
- **T73 Test PME** — plafond −5 sur tout bloc portant au moins deux mesures. *« Test PME » européen et paquets omnibus de simplification.*

**Quatre mécaniques nouvelles**, toutes annoncées dans l'agenda du tour et listées dans le panneau « ce qu'il a laissé en place » : le référendum en cours avec le perçu qu'il faut atteindre, le scrutin saturé, le veto de procédure sur les sommets, la neutralisation des seuils technologiques.

**Quatre combinaisons attentistes** — la rue et l'urne (T61+T60), la promesse et le doute (T67+T70), le verrou international (T64+T66), la campagne et le mandat (T62+T63).

**Seize contre-leviers réassignés** pour que chaque nouveau levier attentiste soit la réplique nommée d'un levier actif : quand l'adversaire joue exactement le contre-levier d'un des vôtres, le panneau, le journal et le bilan le disent.

L'adversaire automatique sait jouer treize des quatorze nouveaux leviers ; le quatorzième (T63) exige un bloc démocratique effondré, que le joueur automatique de test ne produit pas.

---

### Calibrage v0.7

Moyennes sur **30 parties par configuration**, joueur automatique glouton, adversaire compris.

| | niveau 1 | niveau 2 | niveau 3 | niveau 4 |
|---|---|---|---|---|
| Joueur actif — température 2100 | 2,61 °C | 2,49 °C | 2,53 °C | 2,65 °C |
| Joueur actif — score | 312 | 410 | 384 | 315 |
| Joueur attentiste — température 2100 | 2,49 °C | 2,30 °C | 2,13 °C | 2,07 °C |
| Joueur attentiste — score | 407 | 317 | 248 | 228 |

Ne rien faire donne toujours **3,48 °C** exactement.

Le camp attentiste est monotone en difficulté sur les deux mesures. **Le camp actif ne l'est pas, et il ne l'était déjà pas** : le niveau 1 y est plus difficile que le niveau 2. La cause n'est pas l'adversaire mais le **double rôle du curseur de difficulté**, qui règle à la fois le nombre de coups adverses *et* la taille du catalogue ouvert (`lvl <= s.level`). Au niveau 1 le joueur n'a accès qu'à 31 leviers actifs sur 46 : il affronte un adversaire plus faible avec un répertoire plus pauvre, et le second effet l'emporte sur le premier. Les campagnes à douze parties des versions précédentes ne le voyaient pas — l'écart-type est de 0,15 °C, il faut une trentaine de parties pour que l'écart sorte du bruit.

C'est exactement la question laissée ouverte depuis la v0.4 — *le niveau Expert est-il un palier de contenu ou un palier de règles ?* — et elle demande maintenant une réponse : séparer les deux curseurs, ou ouvrir tout le catalogue dès le niveau 1 et ne faire varier que l'adversaire. Rien n'a été tranché ici : le corriger changerait l'équilibre de toutes les difficultés, et ce n'est pas une correction à glisser dans une version consacrée à autre chose.

### Ce qui reste ouvert

- **Le double rôle du niveau de difficulté**, ci-dessus. Premier chantier de la v0.8.
- **La colonne « Verdict » du catalogue xlsx**, toujours vide.
- **Le choix du bloc joué** — décider quel pays ou quelle région on incarne — reste en attente, à votre demande.

---



## v0.6 — l'écran, l'adversaire, l'entrée en jeu

Cette version ne touche ni au modèle ni au calibrage. Elle répond aux sept remarques sorties des parties d'essai.

### 1. L'arrivée dans le jeu

Un guide de huit étapes s'ouvre au premier tour. Il découpe un trou dans un voile sombre autour d'une zone de l'écran et l'explique, dans l'ordre où on s'en sert : la carte, les cartes d'objectif, l'agenda du tour, la main, le bandeau de planification, le camp adverse, le cockpit, le bouton de fin de tour. Flèches et Échap fonctionnent. Il se rouvre à tout moment par le lien **guide** du bandeau du haut — le seul endroit où il ne gêne pas.

Le choix a été de montrer les zones plutôt que d'écrire une règle de plus : la page d'accueil expliquait déjà tout, et ce n'était pas ce qui manquait.

### 2. Les leviers : commandes regroupées, et quatre incohérences corrigées

Les deux commandes de la main étaient à deux endroits différents — « autres leviers » en tête de colonne gauche, « à venir » en tête de colonne droite. Elles sont maintenant sur une seule ligne sous l'en-tête de gauche, avec le nombre de leviers ouverts : **`37 ouverts · autres leviers · 9 à venir`**. La colonne de droite s'annonce pour ce qu'elle est, « suite de votre main ».

Sur le fond, un audit automatique a comparé, pour les 77 leviers, ce que le texte annonce et ce que la fonction fait réellement. Quatre écarts, dont deux vrais bugs :

- **A27 « Retrait de l'assurance sur les projets fossiles » ne faisait rien, jamais.** La condition testait `b.rente >= 2`, or `rente` est le libellé texte de la rente fossile du bloc ; la valeur numérique s'appelle `rentN`. La comparaison était toujours fausse. La carte s'applique désormais aux cinq blocs à rente élevée, et le texte les nomme.
- **A36 « Avis consultatif » annonçait « perçu +5 partout » qui n'était jamais appliqué.** Seule la contrainte différée l'était. Le texte a été corrigé plutôt que la fonction : l'effet du levier est juridique, pas médiatique.
- **T25 « Recours en légalité »** annonçait « contrainte −10 » alors que −10 est un plafond : la carte retire la valeur de la dernière mesure du bloc, et 4 seulement si le bloc n'en a aucune. Le texte le dit maintenant.
- **A20 et A21** annonçaient un relèvement de plafond qui, plafond à 100, ne se voit jamais. Le texte précise qu'il ne joue que si l'adversaire l'a abaissé.

L'audit dans l'autre sens — un effet mesuré qu'aucun texte n'annonce — ne remonte rien.

### 3. Un seul bloc sous la carte au lieu d'une bande en haut

La ligne « votre position / trajectoire / le monde / dommages » occupait toute la largeur en haut de page, en quatre colonnes, loin de la carte. Elle disparaît. Son contenu est fondu avec la courbe d'évolution dans un **cockpit** placé sous la carte : position et score à gauche, jauge de palier au centre, compteurs du monde en pastilles à droite, la courbe juste en dessous. Même information, une ligne au lieu de quatre colonnes, et à côté de ce qu'elle commente.

La carte « indice technologique » du bandeau d'objectifs disparaît aussi : sa valeur est une pastille du cockpit, avec ses deux seuils dans l'infobulle. Le bandeau du haut passe de quatre cartes à trois — l'événement, l'objectif de la partie, le défi du tour.

### 4. La carte du monde vit

Trois choses bougent, toutes lisibles sans légende :

- **la couleur de la terre.** Chaque bloc est teinté par sa situation : il rougit avec le réchauffement et les dommages qu'il subit, il verdit à mesure que la contrainte s'y installe. En fin de partie active, la Chine et l'Europe sont vertes et l'Afrique brune — ce qui est exactement l'histoire de la partie ;
- **le halo d'émissions.** Un disque rouge translucide entoure chaque bloc, de rayon proportionnel à ses émissions. Il rétrécit quand le bloc décarbone. C'est l'objectif de la partie, dessiné ;
- **le bloc frappé par l'événement du tour** bat lentement, et celui où l'adversaire vient de jouer porte un compteur rouge.

La mer se réchauffe elle aussi, très légèrement. Rien de tout cela n'est décoratif : chaque variation est une variable du modèle.

### 5. L'adversaire devient visible

C'était la remarque la plus juste : on ne comprenait pas que quelqu'un jouait contre nous. Une baisse de jauge ne dit ni qui l'a faite ni pourquoi. Quatre ajouts :

- **un panneau permanent « le camp adverse »**, en haut de la colonne droite : qui il est, combien de leviers il joue par tour, combien il en a joué depuis 2015 et sur quels blocs, **le détail nommé de son dernier tour**, et — la partie qui manquait le plus — **ce qu'il a laissé en place** : emprise médiatique, bloc préempté, infrastructure verrouillée avec son plafond, clause de revoyure. Ces effets agissent chaque tour sans qu'il ait à y revenir ; ils n'étaient nulle part ;
- **la réplique est nommée.** Chaque levier du camp actif porte un contre-levier dans le catalogue. Quand l'adversaire joue exactement celui-là sur le bloc concerné, le panneau, le journal et le bilan le disent : *« réplique à votre A19 »*. La partie cesse d'être une course contre un décor ;
- **la résolution nomme ses coups.** La séquence animée affichait « le camp attentiste joue » puis des jauges qui bougeaient. Elle annonce maintenant chaque levier adverse par son nom, sur le bloc visé, qui pulse ;
- **le bilan de fin de tour** a une section dédiée : ce qu'il a joué, où, avec quel effet, et ce qui était une réplique.

L'information cachée reste cachée : on ne voit jamais sa main, seulement ce qu'il en a sorti.

### 6. Ce qui reste ouvert

- **Pas de sauvegarde.** Une partie de dix-sept tours ne survit pas à la fermeture de l'onglet. C'est le premier chantier de la v0.7.
- **Le camp attentiste reste moins riche** que le camp actif : moins de leviers, moins de combinaisons, un catalogue à venir plus court.
- **La colonne « Verdict » du catalogue xlsx** n'est toujours pas remplie, et le niveau Expert reste ambigu — palier de contenu ou palier de règles.

### Calibrage v0.6

Inchangé, vérifié après chaque modification de structure : passif exactement **3,48 °C**, les deux camps monotones en difficulté.

| | niveau 1 | niveau 2 | niveau 3 | niveau 4 |
|---|---|---|---|---|
| Joueur actif — température 2100 | 2,39 °C | 2,43 °C | 2,53 °C | 2,63 °C |
| Joueur attentiste — température 2100 | 2,51 °C | 2,36 °C | 2,27 °C | 2,19 °C |

La correction d'A27 était la seule susceptible de déplacer le calibrage : elle rend jouable un levier mondial à 2 de capital qui donne +7 de contrainte sur cinq blocs. L'écart mesuré reste dans le bruit des douze parties.

---



## v0.5 — la partie va jusqu'en 2100

### Le problème

Huit tours de cinq ans, 2015 à 2055 : la partie se terminait au moment où le climat commence à se jouer, et le score final était une **extrapolation** du rythme atteint. Deux défauts pour le prix d'un. La partie était trop courte, et le chiffre qui la jugeait n'était pas un résultat mais une conjecture.

### Ce qui a changé

**Dix-sept tours de cinq ans, 2015 → 2100.** La température affichée n'est plus extrapolée : c'est celle que la partie atteint. `projeter()` ne fait plus que rejouer le modèle du tour courant jusqu'au dernier, contraintes figées — au dernier tour, la projection *est* le résultat. Le défaut noté depuis la v0.3, « la projection 2100 sur-réagit aux premiers coups », disparaît avec l'extrapolation qui le causait.

**Croissance et réduction sont devenues des taux annuels**, élevés à la puissance du nombre d'années du tour. Avant, elles étaient exprimées par tour : changer la durée d'un tour changeait le climat, ce qui rendait tout réglage d'horizon impossible sans casser le calibrage. Désormais un bloc laissé libre suit sa tendance annuelle, amortie de 4 % par an au fil du siècle ; un bloc porté à 100 de contrainte perd 5,5 % de ses émissions par an. Conséquence de jeu, et elle est juste : **la contrainte installée tôt rapporte beaucoup plus que la même contrainte installée tard**, parce qu'elle s'applique cinq années de plus à chaque tour gagné.

**L'amortissement de la croissance a été recalé** pour que la trajectoire sans action reste celle qu'on annonce : 3,48 °C en 2100, avec des émissions qui montent de 35,5 à environ 57 GtCO₂/an puis plafonnent. C'est un monde sans aucune politique climatique, pas un scénario extrême. La constante `T_BASELINE` n'est plus une valeur posée à la main : le moteur la produit, et la simulation la vérifie à 3,48 exactement.

**Tout ce qui était dimensionné pour huit tours a été redimensionné.** Revenus par tour réduits (le camp actif passe de +4 à +3 par ressource, l'attentiste de +6 à +4 de capital), paliers de score relevés (0 / 180 / 360 / 540 / 700 / 860), pondérations du score attentiste revues pour qu'il discrimine autre chose que le nombre de mesures évitées, décès recalés sur un rythme annuel (≈ 0,55 M/an à 1,3 °C, ≈ 3 M/an à 3 °C) au lieu d'un forfait par tour, courbe de dommages détendue pour qu'elle ne sature plus dès 2,5 °C, compteur d'actifs préservés ramené à un ordre de grandeur lisible.

### Calibrage v0.5

Moyennes sur 12 parties par configuration, adversaire compris, joueur automatique.

| | niveau 1 | niveau 2 | niveau 3 | niveau 4 |
|---|---|---|---|---|
| Joueur actif — température 2100 | 2,39 °C | 2,46 °C | 2,56 °C | 2,62 °C |
| Joueur attentiste — température 2100 | 2,51 °C | 2,38 °C | 2,37 °C | 2,22 °C |

Ne rien faire donne **3,48 °C**, 57 GtCO₂/an en 2100 et 159 millions de décès cumulés. Une partie active ramène les émissions à 8-18 GtCO₂/an et les décès à 105-127 millions. Les deux camps restent monotones en difficulté, ce qui n'allait pas de soi après un changement d'horizon de cette taille.

### Le catalogue progresse : époques et prérequis

Un levier ne doit pas tomber au hasard, il doit **devenir possible**. Deux verrous, cumulables, symétriques entre les camps.

**L'époque.** Le répertoire de l'action climatique s'est élargi avec le temps, et celui de l'obstruction avec lui : le contentieux climatique, l'ajustement carbone aux frontières, le reporting extra-financier n'existaient pas en 2015 ; en face, la capture réglementaire et l'action en diffamation sont venues quand la dénégation frontale a cessé de fonctionner. Trois époques : ce qui est disponible dès 2015, ce que la décennie 2020 a rendu praticable (ouvert en **2035**), et l'échelon institutionnel et international (ouvert en **2055**). La première est volontairement large — 23 leviers actifs, 17 attentistes — pour que le début de partie garde de la variété.

**Le prérequis.** Quinze leviers exigent en plus quelque chose que la partie doit avoir produit, là où la dépendance est réelle et pas décorative : on ne redistribue pas le produit d'une taxe qui n'existe pas, on n'ajuste pas à la frontière sans prix intérieur, on n'électrifie pas sans réseau, on ne saisit pas la cour régionale sans contentieux national derrière. Côté attentiste, le principe est le même à l'envers : **le recours en légalité, la clause de réexamen, la protection des investissements, l'action en diffamation et la simplification normative exigent que l'adversaire ait d'abord fait voter quelque chose.** Le camp du statu quo n'a rien à attaquer tant que rien n'existe — c'est exactement ce qui rend son répertoire dépendant du succès de l'autre.

**Les leviers fermés restent consultables.** C'est ce qui fait la différence entre une main aléatoire et une trajectoire. Un lien « n à venir » à côté de la main ouvre le catalogue : chaque levier encore fermé y figure avec sa famille, son périmètre et sa condition en clair — « s'ouvre en 2035 », « exige une tarification carbone en vigueur, sans produit il n'y a rien à redistribuer », et les deux quand les deux manquent. Un clic ouvre la fiche complète, qui affiche également le verrou. Et chaque ouverture est annoncée au journal du tour : « ▸ 10 nouveaux leviers ouverts : Ajustement carbone aux frontières, Loi-cadre climat contraignante… »

**Ce que ça a changé sans qu'on le demande.** Le pic des émissions arrive maintenant vers 2030-2035 au lieu de 2040 : la première époque étant concentrée sur les leviers qui réduisent vraiment, le début de partie est plus efficace et moins dilué. Les défis composent correctement avec le nouveau système — « Un verrou », qui exige une loi-cadre, n'est plus tiré avant 2035, vérifié sur 200 tirages par tour.

Calibrage après progression : partie passive 3,48 °C et aucun jalon ; joueur actif 2,39 à 2,63 °C selon la difficulté ; joueur attentiste 2,51 à 2,20. Monotone dans les deux camps, comme avant.

### L'objectif de la partie est une trajectoire d'émissions, datée

« Faire de son mieux pendant quatre-vingt-cinq ans » n'est pas un objectif, c'est une posture. La partie se juge désormais sur **deux jalons**, et l'objectif est annoncé dès l'écran d'accueil : faire plafonner les émissions mondiales, puis ramener le monde **sous 20 GtCO₂ par an**.

**Ce qui compte n'est pas de franchir les jalons, c'est en quelle année.** C'est le point sur lequel j'ai tenu bon contre la version binaire de l'idée. Un objectif atteint-ou-pas réintroduirait exactement le raisonnement que le jeu conteste — « on n'a pas tenu 1,5 °C, donc c'est fichu » — et il serait physiquement faux : la température dépend du CO₂ *cumulé*, pas du point d'arrivée. Atteindre 20 Gt/an en 2065 et l'atteindre en 2095 laissent deux mondes très différents. Chaque tranche de cinq ans gagnée retire des gigatonnes du total, y compris après le passage du seuil, y compris quand le seuil n'est jamais franchi. Le score le dit : chaque jalon rapporte proportionnellement à son avance sur une date de référence, et ne devient jamais négatif.

Le seuil a été choisi sur mesure, pas au jugé. Sur 16 parties par configuration : sous 10 Gt/an est atteint 0 à 5 fois sur 16 et jamais avant 2090 — ce serait un plafond de verre, pas un objectif. Sous 20 Gt/an est franchi 9 à 16 fois sur 16, entre 2070 et 2090 : des dates assez étalées pour que « quand » veuille dire quelque chose. Et le pic, lui, tombe entre 2025 et 2042 selon la qualité du jeu, ce qui donne un premier climax en début de partie plutôt qu'une seule ligne d'arrivée lointaine.

Une partie sans aucune action ne franchit **aucun** des deux jalons : les émissions montent de 35,5 à 57 GtCO₂/an et ne plafonnent jamais. Le camp attentiste marque symétriquement — sur le retard des deux jalons, et au maximum quand ils ne sont jamais franchis.

Concrètement : la carte « Émissions mondiales » du bandeau est devenue la **carte de l'objectif**, avec une jauge qui va du pic au seuil et deux pastilles datées. Le franchissement d'un jalon est annoncé dans la séquence de résolution, écrit dans le journal, et repris dans le bilan de tour et l'écran de fin. La température de 2100 reste affichée partout — mais comme conséquence, plus comme but.

Calibrage après recadrage du score : partie passive 20 points, « Sans effet », aucun jalon. Joueur actif automatique 349 à 484 points selon la difficulté, pic vers 2040, seuil vers 2085. Joueur attentiste 303 à 390, et son score baisse quand la difficulté monte, c'est-à-dire quand l'adversaire actif atteint les jalons plus tôt. Monotone dans les deux camps.

### La cible net zéro glisse avec le calendrier

« Objectif net zéro 2050 » est le seul levier du catalogue dont l'intitulé porte une date. Sur une partie qui s'arrêtait en 2055 c'était tolérable ; sur une partie qui va jusqu'en 2100, proposer une cible 2050 en 2075 est absurde.

Le levier n'a pas été retiré : il fait désormais ce que le procédé fait dans la réalité. Passé 2050, **la cible est repoussée à la décennie suivante**, toujours à vingt ans au moins, toujours assez loin pour n'engager aucun décideur en exercice — 2070, puis 2080, 2090, 2100, 2110. Le journal note le passage : « l'échéance net zéro de 2070 est passée sans être tenue : les annonces visent désormais 2080. »

Et le procédé **s'use** : le gain d'opinion passe de 9 points à 7, puis 5, puis un plancher de 3, parce qu'une cible déjà repoussée trois fois se croit moins qu'une promesse neuve. L'ancrage réel et la limite se réécrivent à chaque report. C'est le seul levier du jeu dont le texte change en cours de partie, et c'est celui qui le méritait : son sujet est précisément la promesse qu'on redate.

### Les leviers nécessaires à l'objectif du tour sont proposés

Le défi « Un verrou » demande un bloc protégé par une loi-cadre. Deux leviers du catalogue posent un verrou. S'ils ne sortaient pas dans les douze cartes du tour, l'objectif était inatteignable sans que le joueur y soit pour rien — un objectif qu'on ne peut pas seulement tenter n'apprend rien.

Cinq défis déclarent maintenant leurs **leviers clefs** : ceux sans lesquels ils sont hors de portée. « Un verrou » → loi-cadre ou accord transpartisan. « Refermer l'écart » → mobilisation de masse, majorité silencieuse, attribution d'événement. « Tenir la rue » → redistribution ou récit désirable. Côté attentiste, « Allumer un feu » et « Le doute s'installe » ont les leurs. Les autres défis n'en déclarent pas, parce que n'importe quel levier de contrainte les sert.

Si aucun levier clef n'est en main au moment du tirage, l'un d'eux prend la place de la carte la moins alignée avec votre doctrine — et le journal le dit. Le levier clef porte une étiquette **★ objectif** dans la main, et la carte du défi indique « levier clef en main ★ » ou « aucun levier clef disponible ». Vérifié sur 200 tirages par défi : zéro main sans levier clef.

Deux garde-fous complètent la mécanique. Un défi dont tous les leviers clefs sont épuisés n'est plus tiré du tout, plutôt que d'être proposé sans espoir. Et le renouvellement de main, qui écarte les cartes rendues jusqu'au tour suivant, ne peut pas faire disparaître le levier clef : il revient, parce que le tirage ne doit pas pouvoir annuler l'objectif du tour.

### La courbe de température se lit tour par tour

La courbe ne disait que son dernier point : pour comparer 2035 à 2060, il fallait se souvenir. Chaque tour a maintenant sa colonne sensible. Au survol : un repère vertical, les deux points de ce tour mis en évidence, et une infobulle qui donne l'année, la température de votre partie, celle du monde réel avec l'écart signé, la variation depuis le tour précédent, et l'écart avec la trajectoire sans action. Les écarts sont colorés du point de vue du camp actif — vert quand on descend.

Le même survol est disponible sur le graphe de fin de partie, où il permet de relire les dix-sept tours d'un coup : à quel moment la courbe a décroché de celle du monde réel, et à quel moment elle a cessé de descendre.

### Les leviers surestimés ne s'appellent plus « pièges »

Six leviers du catalogue rapportent beaucoup moins que ce que leur intitulé promet. Le jeu les désignait de trois façons : un identifiant à part (P01, P04…), une famille littéralement nommée « Piège », et une fiche qui annonçait « Piège proposé au camp actif ». Autant dire qu'ils ne piégeaient personne.

Ils ont rejoint la série A avec des numéros libres (A22, A42, A43, A38, A09, A26) et leurs vraies familles — Économique, Technologique, Narratif. Leurs alias, qui donnaient la réponse (« crédits non additionnels », « exemption déguisée »), ont été retirés : ils venaient en plus du mauvais camp, puisque le camp attentiste ne subit pas ces leviers, il s'en réjouit. Les renvois croisés qui les désignaient depuis d'autres fiches ont été réécrits sans les nommer. Le mot « piège » ne figure plus nulle part dans le fichier.

Ce qui les trahit est désormais ce qui devrait les trahir dans la vraie vie : **le rendement annoncé sur la carte** — « contrainte +2 seulement, crédibilité −8 quand l'écart est révélé » — et la fiche, si on prend le temps de l'ouvrir, où « solidité de la preuve : contestée » est le vrai signal. Au niveau Découverte seulement, une étiquette « à vérifier » les signale encore, et la description du niveau le dit ; elle disparaît dès le niveau Standard.

## v0.4 — le tour devient un plan, pas une suite de coups irréversibles

### Le problème

Jusqu'ici, cliquer une carte puis un bloc appliquait le levier immédiatement : ressources prélevées, jauges déplacées, dé jeté. Le joueur découvrait l'effet une fois qu'il n'était plus rattrapable, et n'avait aucun moyen de comparer deux façons de dépenser son tour. Sur un jeu qui prétend faire comprendre des arbitrages, c'était le contraire de ce qu'il faut : on ne peut pas arbitrer entre des options qu'on ne peut pas mettre côte à côte.

### Ce qui a changé

**Rien n'est appliqué au monde avant la validation du tour.** Les leviers engagés s'empilent dans un bandeau « votre tour », entre le tableau de bord et la carte. On en retire un d'un clic sur son ×, on vide tout d'un lien, on annule le dernier par Ctrl+Z. L'attribution de l'événement est devenue une entrée de plan comme les autres, donc annulable elle aussi.

**Un clic par carte mondiale.** Un levier de bloc demande deux gestes, parce qu'il faut désigner la cible : on clique la carte, puis le bloc. Un levier mondial n'a rien à désigner — il gardait pourtant une confirmation intermédiaire (« carte mondiale — annuler · jouer ») héritée du temps où jouer une carte était irréversible. Ce n'est plus le cas : un clic l'engage directement dans le tour, et le × de sa puce l'en retire. La confirmation ne protégeait plus de rien.

**L'aperçu est calculé, pas estimé.** Le jeu maintient en parallèle de l'état réel un état prévisionnel : une copie complète sur laquelle le plan est rejoué, en supposant les paris réussis. Toute l'interface lit cet état prévisionnel — jauges de la carte, tableau de bord, cartes injouables, progression du défi. Le bandeau, lui, n'affiche que des différences entre les deux : projection 2100 avant → après, score avant → après, coût engagé et ressources restantes, puis le détail jauge par jauge, bloc par bloc. Les valeurs prévisionnelles sont marquées « prévu » là où elles pourraient passer pour acquises, et les blocs concernés prennent un contour pointillé bleu sur la carte.

**Les paris ne sont pas résolus à l'avance.** Un levier probabiliste affiche son taux de réussite dans le bandeau, et l'aperçu suppose la réussite en le disant explicitement. Le dé n'est jeté qu'à la validation. C'était la condition pour que la planification ne devienne pas une machine à relancer : si l'effet était appliqué au clic, retirer un levier après un échec reviendrait à rejouer le dé.

**Le plan se revalide en permanence.** Régler la doctrine en cours de tour change le coût et l'effet des leviers : le plan est recalculé, et un levier devenu injouable est barré avec sa raison plutôt que silencieusement ignoré. Tant qu'il reste un levier barré, la validation refuse de partir. Le renouvellement de la main est bloqué tant que des leviers sont engagés, puisqu'ils sont encore dedans.

**La résolution a gagné au change.** Les effets des leviers du joueur ne sont plus animés au clic, un par un : ils ouvrent maintenant la séquence de résolution, sous un intertitre « Vos leviers », avant les combos, l'adversaire et le monde. Les dés se jettent à l'écran. Au passage, deux fuites ont été bouchées : le compteur de tour et la courbe de trajectoire affichaient déjà le résultat pendant qu'on le révélait.

**Le moteur n'a pas bougé.** Même harnais de simulation sur v0.3 et v0.4, 16 parties par configuration : les huit résultats sont identiques au centième. La phase de planification ne change que le moment où `jouer()` est appelé, pas l'ordre des opérations.

### Le journal dit tout ce que la machine fait

Le journal ne montrait que les décisions : vos leviers, ceux de l'adversaire, les retours de flamme, les élections. Tout le reste du moteur tournait en silence — les dérives naturelles, les effets persistants, la recharge des ressources, les tirages, les dommages. Un joueur qui voyait une jauge bouger sans savoir pourquoi n'avait aucun moyen de le retrouver.

Chaque tour est maintenant écrit en entier, découpé par phase dans l'ordre exact de la résolution : vos leviers, combinaisons, l'adversaire, l'événement, effets différés, retours de flamme, élections, effets persistants, le monde bouge tout seul, physique du climat, dommages, défi et presse, mise en place du tour suivant. Chaque phase écrit une ligne même quand il ne s'est rien passé — « aucun bloc au-dessus du seuil de friction (55) », « pas d'élection ce tour : les blocs démocratiques votent un tour sur deux ». Une phase silencieuse ne se distingue pas d'une phase absente, et c'est précisément là que naissent les malentendus sur les règles.

Sont sortis du silence : la dérive de chaque bloc au tour près (perçu, réel, friction, contrainte), les effets persistants encore actifs et leur échéance, la neutralisation de l'arbitrage investisseur-État et sa date d'expiration, les pertes d'attention infligées à l'adversaire, l'indice de dommages des deux groupes de blocs, les décès du tour et le cumul, le compteur d'actifs préservés du camp attentiste, la projection recalculée, la recharge chiffrée des deux camps, l'événement et le défi tirés, le nombre de leviers piochés, et le nombre de coups dont l'adversaire dispose au niveau choisi. Le journal dit aussi ce que l'adversaire *ne peut pas* faire — ne pas pouvoir attribuer un événement, s'arrêter faute de carte jouable — parce qu'une absence de coup est une information de jeu.

C'est verbeux par construction : une cinquantaine de lignes par tour. D'où deux vues, basculables par un lien à côté du titre. « Tout » est la vue par défaut. « L'essentiel » ne garde que les décisions des deux camps et ce qui les sanctionne, et masque au passage les sous-titres devenus vides.

Aucune de ces lignes n'a modifié le moteur : mêmes huit résultats de calibrage, au centième, avant et après.

### Le défi, lisible d'un coup d'œil

Le défi du tour tenait dans une ligne de texte et un mot d'état. Il est devenu une vraie carte, avec quatre choses qui doivent se lire sans effort : ce qu'il demande, où on en est, ce qu'il rapporte, et quand il est jugé.

La récompense est désormais **annoncée avant** plutôt que découverte après — un objectif dont on ignore le prix n'oriente aucune décision. Chaque défi porte une jauge, et la règle de lecture est la même partout : **pleine et verte, tout va bien.** Les défis d'objectif la remplissent à mesure qu'on approche du but. Les défis de maintien — « aucun bloc au-dessus de 45 de friction » — affichent au contraire la **marge restante** : elle se vide quand on s'approche du seuil, et vire au rouge quand il est franchi. L'inverse aurait été plus direct à coder et aurait dit le contraire de ce qu'on voit.

L'état est une pastille (EN COURS / REMPLI / TENU / SEUIL DÉPASSÉ), suivie du rappel que le défi est jugé à la résolution, **après le coup de l'adversaire** — ce qui explique pourquoi un défi affiché « rempli » peut être manqué. La carte lit l'état prévisionnel : la jauge bouge pendant qu'on construit son tour.

### Les leviers : périmètre et jauges explicites

Trois choses n'étaient pas identifiables sur une carte de levier.

**Le périmètre.** Un levier mondial portait une étiquette « monde » ; un levier de bloc ne portait rien. L'asymétrie faisait du périmètre une information qu'on déduisait, alors que c'est la première décision : ai-je une cible à choisir ? Chaque carte affiche maintenant une pastille de périmètre — **◍ monde** en violet, **◎ bloc** en bleu — doublée d'un liseré de la même couleur sur le bord de la carte, pour que le tri se fasse à la périphérie du regard. La pastille « bloc » porte en plus **le nombre de blocs actuellement éligibles**, et son infobulle les nomme. Quand il n'y en a aucun, la carte dit pourquoi — « perçu insuffisant sur les 8 blocs » plutôt qu'un grisé muet.

**L'influence de la doctrine.** Elle s'affichait en « doc 87 % », noyée parmi cinq étiquettes de même forme. C'est devenu une jauge à part entière, sur sa propre ligne, avec un remplissage à trois niveaux et l'infobulle qui explique ce qu'elle commande : la probabilité d'être proposée au tirage, et l'amplitude de l'effet une fois jouée.

**Le pari.** L'étiquette disait « pari » sans dire combien. Elle affiche maintenant la **fourchette de réussite sur les blocs encore jouables** — « pari 61–80 % » — et l'infobulle nomme le meilleur bloc et le moins favorable. C'est ce qui transforme un avertissement en information de décision.

Au passage, la temporalité est explicite sur toutes les cartes : « immédiat » en neutre, « effet dans 2 tours » en violet, puisque la latence est la vraie contrainte et méritait la couleur.

### L'agenda du tour : ce qui arrivera sans vous

Un bandeau « ce tour, quoi qu'il arrive » s'intercale entre les évènements et le tableau de bord. Il liste tout ce que la résolution produira sans que le joueur ait à le jouer, et que rien dans l'interface n'annonçait jusqu'ici :

- **combien de leviers l'adversaire va jouer** à la difficulté choisie, plus son action gratuite — la seule part du tour qui reste cachée, et le dire est plus honnête que la laisser deviner ;
- **les échéances politiques**, à commencer par les élections : les blocs démocratiques votent un tour sur deux, et le bandeau affiche le soutien perçu de chacun avec un ✓ ou un ✕ selon qu'il passe la barre des 50. Les tours sans scrutin le disent aussi, avec la date du suivant — une règle qu'on n'apprend pas si elle ne se manifeste que par son résultat ;
- **l'effet automatique de l'évènement** du tour, ou le rappel qu'il n'en aura aucun tant que personne ne l'attribue ;
- **les effets différés arrivant à échéance**, avec le levier qui les a posés ;
- **les retours de flamme annoncés** : un bloc au-dessus du seuil de friction affiche qu'une mesure sautera, et il est encore temps de compenser ;
- **les mécanismes installés qui repassent** : clause de revoyure, préemption qui se lève, institution de suivi, emprise médiatique, accord à cliquet, courbe d'apprentissage au-delà de 40, pertes d'attention en cours, neutralisation de l'arbitrage investisseur-État avec son échéance.

Le bandeau est lu **sur l'état prévisionnel**, donc il se recalcule pendant que le joueur construit son tour. C'est ce qui le rend utile plutôt que décoratif : engager une campagne d'opinion fait basculer deux ✕ en ✓ sur la ligne des élections, engager une tarification carbone fait apparaître l'avertissement de retour de flamme sur le bloc visé, et retirer le levier le fait disparaître. Le joueur voit le calendrier réagir à ses arbitrages avant de les valider.

Le même bandeau est repris dans le bilan de fin de tour, sous l'évènement et le défi du tour qui s'ouvre.

### Un bilan de fin de tour, en pop-up

La résolution animée montre les choses une par une et vite. Elle donne le rythme, elle ne donne pas la lecture. Dès que la séquence se termine, une fenêtre s'ouvre sur trois blocs :

**Ce qui a changé**, en avant → après plutôt qu'en valeurs absolues : projection 2100, réchauffement, émissions, indice technologique, décès cumulés, dommages des blocs riches et de tous les autres, score et palier, résultat du défi, puis les quatre ressources dont vous disposez pour le tour qui commence. Chaque écart est coloré **du point de vue de votre camp** — vert quand la variation vous sert, rouge quand elle sert l'autre. Une friction qui baisse est verte pour l'actif, rouge pour l'attentiste, et c'est le même code sur les huit blocs.

**Les huit blocs** dans une table compacte : contrainte, réel, perçu, friction, chacun avec son écart sur le tour, plus l'état du bloc (loi-cadre, préempté, compensé, friction critique). Les blocs que rien n'a touchés sont estompés, pour que l'œil aille aux trois ou quatre qui ont bougé. Dessous : les manchettes que la presse a retenues, puis l'événement et le défi du tour qui s'ouvre.

**Le journal du tour**, en entier, avec le même basculement tout / essentiel que le panneau latéral. C'est la trace écrite de ce que la fenêtre du haut résume en chiffres : si un écart surprend, la ligne qui l'explique est juste en dessous.

Une case à cocher en bas coupe l'ouverture automatique — le bilan reste alors accessible par un lien « bilan du tour N » dans le bandeau du haut, qui pointe toujours sur le dernier tour résolu.

Le bilan lit un instantané pris au moment exact où le tour est validé, avant que le plan ne touche le monde. Il ne recalcule rien : il compare deux états. Calibrage inchangé.

### Effet de bord utile

Le bandeau rend criant un défaut déjà noté en v0.3 : dès le premier tour, trois bonnes cartes font tomber la projection de 3,48 à 2,91 °C. Ce n'était qu'un chiffre au tableau de bord ; c'est maintenant une promesse affichée avant même d'avoir joué. L'amortissement de l'extrapolation sur les deux premiers tours passe du statut de détail à celui de correctif nécessaire.

## Le problème traité en v0.3

La v0.2 était complète et morte. On jouait trois cartes, on cliquait « fin de tour », et des chiffres changeaient en silence dans un journal texte. Aucune tension, aucun risque, aucun retour immédiat, aucun objectif entre le premier tour et 2055. La v0.3 ne rajoute pas de contenu : elle ajoute du jeu.

## 1. Du nerf

**Retour immédiat.** Quand vous jouez un levier, les blocs touchés pulsent et les valeurs s'envolent au-dessus d'eux — « +11 contrainte », « +5 soutien perçu ». Plusieurs effets sur un même bloc s'empilent au lieu de se superposer. Les jauges s'animent au lieu de sauter.

**Phase de résolution.** La fin de tour n'est plus instantanée. Un instantané des jauges est pris avant la résolution, puis la séquence se rejoue devant vous, étape par étape, avec un bandeau qui annonce ce qui se passe :

1. vos combinaisons, s'il y en a ;
2. l'adversaire joue, un coup après l'autre, chaque bloc touché réagissant à l'écran ;
3. les effets différés qui tombent ;
4. les retours de flamme ;
5. les élections, quand c'est un tour pair ;
6. la physique du climat ;
7. le défi du tour, réussi ou manqué ;
8. deux manchettes de presse ;
9. **la révélation** : la nouvelle projection 2100, avec l'écart gagné ou perdu.

Le tableau de bord est **figé** pendant toute la séquence : le résultat ne s'affiche plus en haut de l'écran avant d'avoir été révélé. C'était le principal tueur de tension de la v0.2. Un bouton « passer ▸ » saute la séquence pour ceux qui la connaissent par cœur.

## 2. Du risque

Vingt-quatre leviers sont devenus des **paris**, signalés par un badge sur la carte. Ce sont exactement ceux qu'il faut faire voter, gagner ou obtenir : tarification carbone, loi-cadre, contentieux, campagne électorale, accord transpartisan, préemption législative, capture réglementaire. Les leviers techniques, eux, ne ratent pas — une norme d'efficacité ou un réseau électrique ne dépendent d'aucune majorité.

La probabilité n'est pas fixe. Elle monte avec le soutien perçu du bloc visé, descend avec la friction, varie selon le régime politique et la crédibilité du camp. Une campagne électorale à 64 % de base peut tomber à 35 % sur un bloc braqué, ou monter à 85 % sur un bloc acquis.

Le jet est visible : une barre montre la zone de réussite, un curseur tombe, le résultat s'affiche. En cas d'échec, **la moitié de la mise revient** et le bloc gagne 6 de friction — on a essayé, ça s'est vu, ça n'a rien donné.

Environ un tiers des paris tentés échouent sur une partie type.

## 3. Des objectifs et des combos

**Un défi par tour**, tiré parmi treize et adapté au camp joué et à l'avancement de la partie. Il s'affiche en haut de l'écran avec sa **progression en temps réel** — « Chine : 6 / 10 », « 1 bloc sur 2 », « 2,94 / 2,90 °C ». Réussi à la résolution, il rapporte des ressources.

**Quinze combinaisons** entre deux leviers joués dans le même tour. Le chèque avec la taxe, plafond étanche, la courbe s'effondre, fenêtre d'attention, capital dérisqué, le coup de Kigali — et côté attentiste : colère ciblée, béton et contrats, la promesse sans date. Chacune porte un effet et une explication.

Comme tirer les deux cartes d'une paire précise parmi 77 est improbable, les combos disponibles sont **signalés** : dès que le partenaire d'un levier est dans votre main, un badge « ⚡ combo » apparaît, avec le nom et l'effet de la combinaison au survol.

**Un score et six paliers** — Sans effet, Marginal, Notable, Structurant, Décisif, Historique. Pour le camp actif il combine réchauffement évité, contrainte moyenne pondérée par les émissions, lois-cadres et indice technologique. Pour l'attentiste, trajectoire préservée, mesures évitées et infrastructure verrouillée. Les deux échelles ont été alignées pour être comparables.

## 4. De la vie

Le monde commente. À chaque résolution, deux manchettes sont générées selon l'état réel de la partie : mobilisation contre les mesures, seuil de 1,5 °C officiellement hors d'atteinte, bilan sanitaire, loi-cadre qui survit à l'alternance, collectivités interdites d'agir, lobby fossile qui perd sa crédibilité. Quand rien ne se passe, la presse le dit aussi : « Le climat quitte la une des journaux. »

Elles apparaissent dans la séquence de résolution, puis restent affichées dans la colonne de droite.

## 5. La fiche d'un levier se suffit à elle-même

Premier retour d'usage : les trois pavés de droite parlaient le langage du moteur. « Rendement attendu par bloc : Chine 151 % » — 151 % de quoi ? « Contrainte +11 % (axe contrainte ou incitation) · contrainte +13 % (axe horizon assumé) » — deux fois la même chose avec des noms d'axes internes. « Coût affiché 3 capital / Coût réel 3 cap. » — deux cases identiques côte à côte.

Ce qui a changé :

**Les valeurs réelles remplacent les pourcentages.** La fiche rejoue le levier sur une copie de la partie en cours et affiche ce qu'il ferait vraiment : « Chine : +20 contrainte », « Europe : −25 friction, compensation installée ». Pour un levier ciblé, une ligne par bloc, triée, avec les blocs injouables grisés et la raison affichée dessous. Pour un levier mondial, la liste des blocs touchés. Quand le levier peut échouer, la probabilité de réussite figure sur chaque ligne — elle varie d'un bloc à l'autre.

**Chaque terme de jeu est explicable au survol.** Contrainte, plafond, friction, soutien perçu, soutien réel, indice technologique, crédibilité, attention, capital : ces mots sont soulignés en pointillés partout où ils apparaissent, dans la fiche comme sur les cartes en main, et une infobulle dit ce qu'ils sont. Le plafond, en particulier, n'était défini nulle part alors que la moitié des leviers adverses ne fait que le baisser.

**La doctrine est expliquée en français.** « Contrainte ou incitation — ce levier veut "contraindre" ; votre curseur est à 35⁄100, vous y êtes. » Puis une conclusion unique : « En conséquence : son effet est renforcé de 37 %, et la friction qu'il crée est réduite de 27 %. C'est déjà compris dans les chiffres ci-dessus. » Cette dernière phrase compte : elle dit au joueur qu'il n'a rien à recalculer.

**Les propriétés répondent à une question, pas à un attribut.** « Latence » est devenu « Quand » ; « Réversibilité » est devenu « Si ça tourne mal » ; « Usages restants » est devenu « Encore jouable ». Le coût n'apparaît qu'une fois, avec le détail de l'écart en infobulle quand il diffère du coût de base.

**La réversibilité est devenue mécanique.** Elle n'avait aucun effet en v0.3 initiale. Désormais, quand un bloc dépasse le seuil de friction, le retour de flamme annule d'abord les mesures les plus faciles à annuler, et ne touche jamais une mesure irréversible. Une loi-cadre ou un accord transpartisan vous protègent donc réellement.

La solidité de la preuve reste indicative — elle dit à quel point il est démontré que le levier marche — mais l'infobulle le précise désormais, et signale que « contestée » ou « faible » trahit souvent un piège.

## 6. Douze leviers par tour, et une seconde donne

La main passe de sept à **douze leviers**, six par colonne. Pour que ça tienne à l'écran sans défilement, les cartes ont été resserrées : l'effet est tronqué à deux lignes et se déplie au survol, et les étiquettes sont passées en repères courts — « 4 pol. », « ≥ 45 », « +2 t », « monde », « doc 87 % », « pari », « ⚡ ». Chacune garde son infobulle.

**Et si les douze ne vous plaisent pas**, le lien « autres leviers » en tête de colonne rend tous les leviers non joués et en tire douze autres. Coût : 1 attention, une fois par tour. Les leviers rendus ne reviennent pas avant le tour suivant, donc c'est bien vingt-quatre leviers différents accessibles dans un même tour — sur les soixante-dix-sept du catalogue.

L'élargissement n'a pas déséquilibré la partie parce que l'adversaire tire dans la même main élargie. Le calibrage s'est même amélioré : la progression est désormais monotone dans les deux camps, ce qui n'était pas le cas avec sept cartes.

## 7. Le camp attentiste cesse d'être décrit par ses adversaires

Retour d'usage : les leviers attentistes étaient formulés très négativement, ce qui déséquilibrait la perception du rôle. C'était exact et le défaut était sérieux, pour deux raisons.

**Ludique :** sur trente et un leviers, une bonne moitié portait un nom qui était déjà un verdict — whataboutisme, greenwashing, chantage à l'emploi, instrumentalisation, capture, détricotage, procédure-bâillon, fatalisme, individualisme. Personne ne se pense comme « celui qui fait du whataboutisme ». On ne joue pas un rôle qu'on vous décrit comme méprisable.

**Pédagogique, et c'est le plus grave :** l'intérêt d'incarner ce camp repose sur la théorie de l'inoculation — comprendre de l'intérieur pourquoi ces arguments fonctionnent, pour les reconnaître ensuite. Si le jeu annonce d'emblée « ceci est un mensonge cynique », le joueur n'apprend rien : il regarde des méchants de carton. Dans la vie réelle, ces arguments ne se présentent jamais ainsi — ils se présentent comme du bon sens, de la prudence budgétaire, de la défense des ménages.

### Ce qui a changé

Deux registres qui étaient mélangés dans le même champ ont été séparés.

**La voix du camp** — nom du levier, effet, mécanisme — est désormais formulée comme le camp se formule à lui-même, sans jugement :

| Avant | Maintenant |
|---|---|
| Whataboutisme | Conditionner l'effort aux autres |
| Instrumentalisation du coût de la vie | Défense du pouvoir d'achat |
| Greenwashing publicitaire | Communication sur les engagements |
| Chantage à l'emploi et à la délocalisation | Alerte sur l'emploi industriel |
| Détricotage administratif | Simplification normative |
| Capture de l'agence réglementaire | Allègement du contrôle |
| Procédure-bâillon | Action en diffamation |
| Fatalisme | Réalisme sur les délais |
| Saturation de l'attention | Maîtrise du calendrier |
| Verrouillage d'infrastructure | Investissement d'infrastructure |

Le mécanisme suit. « Rendre chacun responsable de son empreinte dissout la demande de politique publique dans la culpabilité privée » devient « Chacun décide de ses trajets, de son chauffage, de son assiette. Rendre ces choix visibles est plus rapide, moins coûteux et moins clivant qu'une contrainte imposée d'en haut. »

**L'analyse critique n'est pas supprimée** — elle serait remplacée par une fausse symétrie, ce qui serait pire. Elle est déplacée dans les deux champs qui sont explicitement des champs d'analyse, « Dans le monde réel » et « Ce qui peut le faire rater », où elle est datée et sourcée : « L'empreinte carbone individuelle a été popularisée par une campagne de BP en 2004. Les gestes individuels sans changement d'infrastructure plafonnent autour d'un quart de l'empreinte d'un ménage. »

### Le camp actif a été audité aussi

Remplacer un déséquilibre par l'inverse n'aurait rien réglé. Les superlatifs du camp actif ont été dégonflés : « meilleur rapport effet/coût du catalogue » devient « aucune technologie à déployer, aucun délai de mise en œuvre » ; « le levier le plus puissant du camp actif » devient « c'est ce qui a permis au Climate Change Act de survivre à quatre alternances » ; « imbattable » disparaît.

L'étiquette « Piège. » a également été retirée du texte des six pièges — elle donnait la réponse gratuitement à qui ouvrait la fiche, y compris aux niveaux où les pièges ne sont plus signalés. L'analyse reste, sans l'étiquette : qui lit comprend, qui ne lit pas se fait avoir. Deux noms de pièges qui étaient des verdicts ont aussi changé : « Engagement net zéro 2050 sans étape » devient « Objectif net zéro 2050 », « Nucléaire présenté comme réponse à 2030 » devient « Programme nucléaire accéléré ».

### Comment l'autre camp l'appelle

Une section nouvelle dans chaque fiche donne le nom que le camp adverse emploie — dans les deux sens. La tarification carbone est « matraquage fiscal », la loi-cadre un « carcan juridique », le contentieux climatique un « gouvernement des juges », l'institution de suivi un « comité Théodule ». Symétriquement, « conditionner l'effort aux autres » est nommé whataboutisme, « défense du pouvoir d'achat » instrumentalisation du coût de la vie.

Une phrase l'explicite : le nom que porte la carte est celui qu'emploient ceux qui la jouent, celui de la section est celui qu'emploient ceux qui la subissent, et aucun des deux n'est neutre. C'est probablement ce que le jeu enseigne de plus transférable.

Quatorze leviers actifs et aucun attentiste n'ont pas d'alias — ce sont les leviers techniques qui ne font l'objet d'aucune dénomination hostile identifiable : réseau électrique, R&D, normes d'efficacité. Leur absence d'alias est en soi une information sur ce qui est polémique et ce qui ne l'est pas.

## Calibrage après ces ajouts

Moyennes sur 16 parties par configuration, adversaire compris. Les paris perdus ont durci la partie : le rendement des mesures a été remonté de 0,45 à 0,48 pour compenser.

| | niveau 1 | niveau 2 | niveau 3 | niveau 4 |
|---|---|---|---|---|
| Joueur actif — projection 2100 | 2,34 °C | 2,44 °C | 2,52 °C | 2,56 °C |
| Joueur actif — score | 381 | 338 | 313 | 294 |
| Joueur attentiste — projection | 2,60 °C | 2,43 °C | 2,32 °C | 2,20 °C |
| Joueur attentiste — score | 382 | 323 | 286 | 247 |

Ne rien faire donne toujours **3,48 °C**. Les scores simulés plafonnent à « Notable » parce que l'adversaire automatique qui sert de joueur de test suit une liste de priorités écrite à la main : il ne cherche jamais les combos et joue presque toujours sur le plus gros bloc. Un humain qui vise les combinaisons et répartit ses coups montera nettement plus haut.

## Ce qui reste ouvert

**L'aperçu ignore l'adversaire**, et c'est assumé : montrer sa réponse probable reviendrait à la lui dévoiler. Le bandeau le dit dans l'infobulle de la projection, mais l'écart entre l'aperçu et le résultat réel reste la première source de surprise du jeu — ce qui est plutôt le rôle qu'on veut lui donner.

**L'ordre des leviers dans le plan n'est pas modifiable.** Il compte pourtant : une redistribution jouée avant une taxe ne produit pas le même résultat qu'après. Le glisser-déposer sur les puces du bandeau est le prochain ajout naturel.

**Le taux de réussite des défis est faible en simulation** (moins d'un sur huit) — mais c'est le même artefact : le joueur automatique joue tout sur la Chine, ce qui rend « deux blocs différents » quasi impossible. À vérifier sur une vraie partie avant de conclure qu'il faut les assouplir encore.

**La projection 2100 réagit trop fort aux premiers coups.** Dès le premier tour, trois bonnes cartes la font tomber de 3,48 à 2,3 °C, ce qui donne un sentiment de facilité trompeur au début de partie. La fonction d'extrapolation mériterait d'être amortie sur les deux premiers tours.

**Le camp attentiste reste moins riche à jouer** — c'est le chantier de fond identifié depuis la v0.2. Le risque et les combos l'ont un peu rattrapé, pas encore égalisé.

**Aucun son, aucune musique.** C'est le prochain gain facile sur le ressenti, et le seul qui obligerait à sortir du fichier unique.
