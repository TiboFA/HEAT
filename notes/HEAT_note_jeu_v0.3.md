# HEAT — version jouable v0.3

Fichier : `HEAT_jeu_v0.3.html`, autonome, aucune dépendance, s'ouvre par double-clic.

## Le problème traité

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

**Le taux de réussite des défis est faible en simulation** (moins d'un sur huit) — mais c'est le même artefact : le joueur automatique joue tout sur la Chine, ce qui rend « deux blocs différents » quasi impossible. À vérifier sur une vraie partie avant de conclure qu'il faut les assouplir encore.

**La projection 2100 réagit trop fort aux premiers coups.** Dès le premier tour, trois bonnes cartes la font tomber de 3,48 à 2,3 °C, ce qui donne un sentiment de facilité trompeur au début de partie. La fonction d'extrapolation mériterait d'être amortie sur les deux premiers tours.

**Le camp attentiste reste moins riche à jouer** — c'est le chantier de fond identifié depuis la v0.2. Le risque et les combos l'ont un peu rattrapé, pas encore égalisé.

**Aucun son, aucune musique.** C'est le prochain gain facile sur le ressenti, et le seul qui obligerait à sortir du fichier unique.
