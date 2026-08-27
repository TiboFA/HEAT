# HEAT — Note de cadrage v1

**Objet :** analyse critique du concept et première scénarisation
**Date :** 17 août 2026
**Statut :** projet en gestation, aucun développement engagé
**Périmètre retenu pour cette note :** échelle mondiale, support non tranché

---

## 1. Résumé de la position

L'idée tient, mais pas sous la forme où elle est formulée. Trois éléments du pitch initial posent problème et doivent être révisés avant toute autre chose :

1. **Le camp adverse est mal défini.** « Climatosceptique » décrit une croyance marginale, pas l'acteur qui freine réellement. L'obstruction efficace est économique et procédurale, pas idéologique.
2. **L'objectif « ne rien changer aux comportements humains » n'est l'objectif de personne** dans le monde réel. C'est un sous-produit, pas une intention. Un joueur à qui l'on donne cet objectif joue une caricature, et la valeur pédagogique s'effondre.
3. **La victoire binaire est incompatible avec le réalisme demandé.** Le budget carbone 1,5 °C est de ~170 GtCO₂ au 1ᵉʳ janvier 2026, soit environ quatre ans d'émissions actuelles. Si le jeu démarre en 2026 et se veut réaliste, « contenir le réchauffement » au sens de l'Accord de Paris est déjà hors d'atteinte au tour 1. Le jeu doit se jouer entre 1,8 °C et 3,5 °C, pas au-dessus ou en dessous d'un seuil.

Ce qui reste après correction est solide, et à ma connaissance inoccupé : **un jeu asymétrique à deux camps sur la dynamique sociale et politique de la transition, où le camp du statu quo gagne par défaut et où l'objet réel de l'affrontement est la perception de l'opinion, pas l'opinion elle-même.** C'est ce point qui fait la singularité du projet, et il est documenté empiriquement (§4.1).

---

## 2. Ce qui existe déjà (et ce que HEAT ne doit pas refaire)

| Produit | Nature | Ce qu'il fait bien | Ce qu'il laisse vide |
|---|---|---|---|
| **En-ROADS** (Climate Interactive / MIT Sloan) | Simulateur en ligne gratuit, curseurs de politiques, réponse instantanée | Modèle physico-économique sérieux, validé académiquement, utilisé en atelier partout dans le monde | Aucun adversaire, aucun conflit, aucune politique. On y déplace des curseurs comme si le pouvoir était donné. |
| **C-ROADS World Climate** | Jeu de rôle de négociation type COP | Le blocage entre blocs, le passager clandestin | Horizon court, pas de dimension opinion/médias |
| **Fate of the World** (2011) | Jeu vidéo de stratégie, joueur unique | Ambition de simulation mondiale, cartes de politiques par région | Solo, opaque, réputé punitif et frustrant. Un précédent commercial peu encourageant. |
| **Daybreak** (Leacock, 2023) | Jeu de plateau coopératif | Excellent objet ludique, aucun joueur ne défend le statu quo | Coopératif par construction : le conflit social est absent |
| **La Fresque du Climat** | Atelier de compréhension | Pénétration massive en France, ~1 h 30 | Explique les causes, ne traite pas de l'action ni du conflit |
| **Bad News** (Cambridge) | Jeu de navigateur où l'on incarne un désinformateur | Preuve que faire jouer le « mauvais camp » fonctionne pédagogiquement | Désinformation générique, non climatique, très court |

**Conclusion :** le créneau vide est le croisement *conflit à deux camps × dimension opinion/politique × horizon long*. En-ROADS couvre la physique, Daybreak la coopération, Bad News la manipulation. Personne ne couvre l'affrontement.

Corollaire pratique : **ne pas construire un moteur climat**. Il existe, il est gratuit, il est meilleur que ce qui sera produit ici. Le climat doit être une fonction abstraite (§4.3) et l'effort doit porter entièrement sur la boucle sociale.

---

## 3. Analyse critique du concept initial

### 3.1 L'asymétrie n'est pas un défaut à corriger, c'est le sujet

Un jeu équilibré serait ici un mensonge. Dans le réel, le camp du statu quo gagne s'il ne joue pas : l'inertie des infrastructures, la durée d'amortissement du capital fossile et le décalage entre coût immédiat et bénéfice différé travaillent pour lui. Il faut donc l'inscrire dans les règles :

- Le camp Statu quo **marque des points passivement à chaque tour** tant qu'aucune mesure contraignante n'est passée.
- Le camp Transition **doit dépenser pour ne pas perdre**. Toutes ses actions coûtent du capital politique ; aucune n'en produit directement.
- L'équilibre ludique ne vient pas de la symétrie des moyens mais de la **différence des conditions de victoire** (§5.4) et de l'érosion progressive des atouts du Statu quo (baisse des coûts des renouvelables, dommages devenus indéniables, relève générationnelle).

Un jeu où le camp Transition gagne une fois sur deux serait faux. Un jeu où il ne gagne jamais serait injouable. La cible réaliste est de l'ordre de **25-30 % de victoires « bonnes » pour la Transition** en jeu équilibré, avec une large zone grise de résultats médiocres.

### 3.2 Renommer le camp adverse

Le climatoscepticisme dur (nier le phénomène) est aujourd'hui minoritaire et contre-productif dans le débat public. Le freinage réel passe par les **discours de l'inaction** (Lamb et al., 2020), qui n'exigent aucune négation :

| Stratégie | Discours | Traduction en levier de jeu |
|---|---|---|
| Rediriger la responsabilité | Individualisme (« c'est au consommateur d'agir »), whataboutisme (« et la Chine ? ») | Carte qui déplace la cible d'une mesure de la production vers la consommation ; annule une taxe sectorielle |
| Solutions non transformatrices | Optimisme technologique, gaz « énergie de transition », volontariat plutôt que contrainte | Carte qui remplace une mesure contraignante par un engagement volontaire au même coût politique |
| Souligner les inconvénients | Emplois, pouvoir d'achat, justice sociale instrumentalisée | Carte qui convertit une mesure Transition en friction sociale (§5.3) |
| Capitulation | « Trop tard », « la société ne changera pas » | Carte qui gèle la mobilisation d'une région pour N tours |

**Proposition de renommage :** camp **Inertie** (ou *Statu quo*, ou *Rente*) contre camp **Bascule** (ou *Transition*). Et surtout, changement d'objectif : non pas « ne rien changer aux comportements », mais **« préserver la valeur des actifs et éviter les coûts d'ajustement »**. C'est ce que poursuivent réellement les acteurs concernés, c'est jouable, et c'est défendable sans être stupide — condition indispensable pour que quelqu'un accepte de le jouer sérieusement.

### 3.3 Le problème éthique : faire jouer le camp de l'inaction

C'est le risque principal du projet, et il est gérable.

**Ce qui plaide pour :** la littérature sur l'inoculation psychologique montre qu'incarner un manipulateur améliore durablement la capacité à repérer les techniques de manipulation. *Bad News* et *Cranky Uncle* reposent entièrement sur ce principe et ont fait l'objet d'évaluations randomisées avec des effets positifs, bien que les répliques soient parfois mitigées.

**Ce qui plaide contre :** la même littérature signale un risque de retour de flamme quand le rôle manipulateur est trop gratifiant, trop peu contextualisé, ou joué sans débriefing. Un joueur qui gagne facilement et joyeusement en tant qu'Inertie, sans que le jeu ne lui montre le coût, ressort avec un modèle mental erroné.

**Conséquences de conception, non négociables :**

1. Le camp Inertie doit **voir les dommages qu'il produit**. Compteur de morts liées à la chaleur, de déplacés, de pertes agricoles, affiché en permanence, y compris quand il gagne.
2. La victoire de l'Inertie doit être **amère** : il conserve ses actifs dans un monde dégradé, et l'écran de fin le montre.
3. **Débriefing obligatoire** en format atelier. Chaque carte jouée par l'Inertie porte le nom du discours réel qu'elle représente et une référence. Le débriefing consiste à retrouver ces discours dans l'actualité de la semaine.
4. Aucune carte ne doit reproduire un argument pseudo-scientifique sans marquage explicite. On joue des *techniques*, pas des *thèses*.

### 3.4 Le télescopage des horloges

Le climat répond en décennies, l'économie en années, la politique en mois, les médias en jours. Un tour unique ne peut pas les couvrir. Deux options :

- **Option A — tour de 2 ans, ~25 tours (2026-2075).** Chaque tour comporte une phase « campagne » (actions médiatiques et politiques) et une phase « bilan » (résolution physique et économique). Durée : jeu vidéo ou jeu web long.
- **Option B — 8 tours de 5 ans (2026-2066).** Les actions courtes deviennent des *postures* maintenues sur cinq ans plutôt que des coups. Perte de finesse, gain de jouabilité. Format atelier 3 h.

Je recommande l'option B pour le prototype dans tous les cas, y compris si la cible finale est un jeu vidéo : elle force à identifier les leviers qui comptent vraiment.

### 3.5 Le duel à deux joueurs est une simplification qui coûte cher

Le réel n'a pas deux camps organisés. Il a des États en compétition, des entreprises opportunistes, une opinion inconstante et des juridictions non alignées. Si HEAT reste strictement 1 contre 1, il faut au minimum un **système de PNJ** qui simule les acteurs non alignés, sans quoi le passager clandestin — le mécanisme central de l'échec climatique mondial — disparaît du jeu.

Variante à considérer sérieusement : **3 joueurs** (Bascule / Inertie / un troisième camp « Souveraineté » ou « Croissance du Sud » dont l'objectif est le développement, indifférent au carbone). Ce troisième acteur est le plus proche de la réalité des négociations et il rend les deux autres moins manichéens.

---

## 4. Réalisme : quoi modéliser, avec quels chiffres

### 4.1 La mécanique centrale — l'écart de perception

C'est la trouvaille à exploiter. L'enquête de référence (Andre et al., *Nature Climate Change*, 2024 ; 129 902 personnes, 125 pays, 92 % de la population mondiale) établit que :

- **69 %** des habitants de la planète se disent prêts à consacrer 1 % de leur revenu à l'action climatique ;
- **86 %** approuvent les normes sociales pro-climat, **89 %** demandent davantage d'action publique ;
- mais les gens estiment que seulement **43 %** de leurs concitoyens sont prêts à contribuer, soit **26 points d'écart**.

Conséquence de jeu, et c'est le cœur de HEAT : **chaque région possède deux jauges distinctes.**

- **Soutien réel** — lent, difficile à déplacer, monte avec l'expérience et l'éducation. Il détermine ce qui *tiendra* dans le temps.
- **Soutien perçu** — volatile, sensible aux médias, aux sondages, aux mobilisations visibles et aux polémiques. Il détermine ce que les décideurs *osent* faire au tour en cours.

Le camp Inertie ne combat presque jamais le soutien réel : il maintient artificiellement bas le soutien perçu. Le camp Bascule dispose d'une action rare et puissante, **« révéler la majorité »**, qui rapproche brutalement le perçu du réel mais s'épuise si elle est répétée. Cette asymétrie est exacte, documentée, et elle produit un jeu.

### 4.2 État initial (2026) — valeurs de départ

| Variable | Valeur | Source |
|---|---|---|
| Réchauffement d'origine humaine | **1,37 °C** (2025) | IGCC 2025 (publié juin 2026) |
| Rythme de réchauffement | **~0,27 °C / décennie** | IGCC 2025 |
| Émissions CO₂ fossiles | **38,1 GtCO₂/an** (2025) | Global Carbon Budget 2025 |
| Émissions CO₂ totales (avec usage des sols) | **42,2 GtCO₂/an** | GCB 2025 |
| Émissions GES totales | **56,8 GtCO₂éq** (2024, record) | IGCC 2025 |
| CO₂ atmosphérique | **425,6 ppm** (2025) vs 278 préindustriel | GCB 2025 |
| Budget restant 1,5 °C (50 %) | **170 GtCO₂** — ~4 ans | GCB 2025, au 01/01/2026 |
| Budget restant 1,7 °C | **525 GtCO₂** — ~12 ans | GCB 2025 |
| Budget restant 2 °C | **1 055 GtCO₂** — ~25 ans | GCB 2025 |

### 4.3 Le modèle climat tient en une ligne

Inutile de coder un modèle. La relation quasi linéaire entre réchauffement et CO₂ cumulé (TCRE, GIEC AR6) suffit :

```
T(t) = 1,37 + 0,00045 × C(t)
```

où `C(t)` = CO₂ cumulé émis depuis 2026 en GtCO₂, et 0,00045 = 0,45 °C par 1 000 GtCO₂ (valeur centrale AR6 ; fourchette 0,27 – 0,63 utilisable comme aléa de partie, tirée en début de jeu et **non révélée aux joueurs** — l'incertitude sur la sensibilité climatique est elle-même un élément de réalisme et un excellent moteur de tension).

Deux correctifs à ajouter, tous deux justifiés :

- **Inertie thermique** : le réchauffement continue quelques tours après l'arrêt des émissions. Empêche le « coup de frein de dernière minute ».
- **Points de bascule** : cartes à seuil (Amazonie, permafrost, AMOC) dont la probabilité de déclenchement croît avec T et qui ajoutent un forçage irréversible. À utiliser avec parcimonie, sinon le jeu devient une loterie.

### 4.4 La boucle économique — trois faits à respecter

1. **Inertie du capital.** Une centrale à charbon, un haut fourneau, une flotte de véhicules ont 20 à 40 ans de durée de vie. Toute décision d'investissement prise au tour *n* verrouille des émissions jusqu'au tour *n+8*. Le camp Inertie gagne en accélérant les investissements fossiles *avant* qu'une contrainte n'arrive — c'est exactement ce qui se produit dans le réel.
2. **Courbes d'apprentissage.** Le coût des renouvelables et des batteries baisse en fonction du volume cumulé déployé, pas du temps. Le camp Bascule qui subventionne tôt paie cher et fait baisser le coût pour tout le monde, y compris pour les régions qui n'ont rien payé. Passager clandestin intégré.
3. **Coût de l'inaction différé.** Les dommages climatiques n'apparaissent qu'après plusieurs tours et frappent en priorité des régions qui ne sont pas celles qui émettent. Asymétrie géographique à conserver : elle est la raison pour laquelle le problème n'est pas résolu.

### 4.5 Les événements extrêmes — le piège de réalisme à éviter

Intuition à corriger : une canicule ou un incendie ne convertit pas l'opinion. Les méta-analyses sur le lien entre expérience d'événements extrêmes et perception du changement climatique trouvent un effet **positif mais faible**, fortement modéré par l'appartenance politique préalable et surtout par le fait que la personne **attribue ou non** l'événement au changement climatique.

Mécanique qui en découle, et qui vaut mieux qu'un simple « +10 d'opinion » :

> Une carte Événement est tirée. Son effet sur l'opinion est **nul par défaut**. Le camp Bascule peut dépenser une ressource pour l'**attribuer** (science de l'attribution, couverture médiatique, témoignages). Le camp Inertie peut dépenser pour la **désattribuer** (« il a toujours fait chaud », « mauvaise gestion forestière », « fatalité »). Seul l'événement attribué déplace la jauge — et il déplace davantage le *perçu* que le *réel*.

C'est plus juste que le réel naïf, et c'est plus intéressant à jouer.

### 4.6 Le retour de flamme — la mécanique qui manque à tous les jeux existants

Aucun jeu climat existant ne modélise le fait qu'une politique trop rapide ou mal compensée se fait annuler. Gilets jaunes, révolte agricole européenne, détricotage du Pacte vert : c'est pourtant le mode d'échec dominant de la dernière décennie.

> Chaque mesure Bascule génère de la **friction** proportionnelle à sa contrainte et inversement proportionnelle à sa compensation. La friction non compensée s'accumule. Au-delà d'un seuil, un événement de **Retour de flamme** se déclenche : la région bascule politiquement, et **une à trois mesures antérieures sont annulées**. Le camp Inertie peut dépenser pour abaisser le seuil ou pour amplifier une friction existante.

Cette mécanique interdit la stratégie « tout passer en force au tour 1 » et rend la compensation sociale non pas morale mais **instrumentalement nécessaire**. C'est probablement l'enseignement le plus utile que le jeu puisse transmettre.

---

## 5. Première scénarisation

### 5.1 Plateau

Six à huit blocs régionaux, chacun avec un profil chiffré distinct (émissions, PIB/hab, capital fossile installé, régime politique, exposition aux dommages, soutien réel/perçu initial) :

Amérique du Nord · Europe · Chine · Inde · Reste de l'Asie · Golfe & Russie · Afrique · Amérique latine

Trois attributs par bloc suffisent à créer des situations distinctes :

- **Régime** (démocratie électorale / autoritaire / hybride) : détermine quels leviers fonctionnent. Une campagne d'opinion est inutile dans un bloc autoritaire ; la capture réglementaire y est décisive. Inversement en démocratie.
- **Dépendance à la rente fossile** : détermine ce que le bloc a à perdre.
- **Exposition aux dommages** : détermine à quelle vitesse son soutien réel monte tout seul.

### 5.2 Ressources

Quatre monnaies, non convertibles librement — c'est la non-convertibilité qui fait la décision :

| Ressource | Camp Bascule | Camp Inertie |
|---|---|---|
| **Capital** (€) | Rare, issu du public et de la philanthropie | Abondant au départ, décroît avec la dépréciation des actifs fossiles |
| **Capital politique** | Se consomme à chaque mesure, se régénère avec les victoires électorales | Se consomme peu : l'Inertie n'a pas besoin de faire voter, seulement de bloquer |
| **Attention** (bande passante médiatique) | Limitée, partagée avec les autres sujets | Peut être **saturée** délibérément : levier majeur de l'Inertie |
| **Crédibilité** | Chute en cas de promesse non tenue ou d'alarmisme démenti | Chute à chaque catastrophe attribuée |

### 5.3 Structure du tour (format atelier, 8 tours de 5 ans)

1. **Contexte** — révélation de l'événement mondial du tour (croissance, prix de l'énergie, tension géopolitique)
2. **Actions simultanées** — chaque camp joue N cartes face cachée, révélation simultanée (évite le jeu réactif pur)
3. **Résolution influence** — attribution/désattribution, effets sur perçu et réel
4. **Résolution politique** — élections dans les blocs concernés, adoption ou blocage des mesures, contrôle de friction et Retour de flamme
5. **Résolution économique** — investissements verrouillés, courbes d'apprentissage, émissions du tour
6. **Résolution physique** — cumul, température, dommages, tirage des points de bascule
7. **Bilan** — mise à jour des compteurs, dont le compteur de dommages humains

### 5.4 Conditions de victoire

Pas de binaire. Score final à l'horizon du dernier tour, prolongé jusqu'en 2100 par extrapolation :

**Camp Bascule** — maximiser `(3,5 − T_pic)` pondéré par la légitimité conservée. Une transition imposée qui déclenche trois retours de flamme et laisse un monde à 2,8 °C vaut moins qu'une transition plus lente arrivant à 2,4 °C sans rupture démocratique.

**Camp Inertie** — maximiser la valeur d'actifs préservée et le nombre de mesures contraignantes évitées, **moins** les dommages subis par les blocs où se trouvent ses actifs. Il n'a pas intérêt à un monde à 4 °C : ses raffineries y sont sous l'eau. Cette contrainte est réaliste et empêche le jeu de dégénérer en course au pire.

**Grille de lecture partagée en fin de partie :**

| T pic 2100 | Lecture |
|---|---|
| < 1,8 °C | Résultat hors de portée sans hypothèses très optimistes. Si les joueurs l'atteignent, le modèle est trop généreux — à recalibrer. |
| 1,8 – 2,2 °C | Victoire nette Bascule |
| 2,2 – 2,8 °C | Zone grise, celle où se joue réellement la partie |
| 2,8 – 3,5 °C | Victoire Inertie |
| > 3,5 °C | Défaite des deux camps : l'Inertie perd aussi ses actifs |

### 5.5 Exemples de cartes

**Inertie**
- *Énergie de transition* — le gaz est classé actif durable dans un bloc. Verrouille 15 ans d'infrastructure. Coût : capital.
- *Et la Chine ?* — annule l'effet d'une mesure adoptée dans un bloc à faibles émissions relatives. Coût : attention.
- *Facture d'abord* — convertit une mesure Bascule votée en +2 friction. Efficace uniquement si le prix de l'énergie du tour est élevé.
- *Trop tard de toute façon* — gèle la mobilisation d'un bloc pour 2 tours. Ne fonctionne que si T > 2,0 °C. Levier qui devient plus fort à mesure que la partie se dégrade.
- *Saturation* — l'attention mondiale est monopolisée par un autre sujet ce tour-ci. Aucune attribution possible.

**Bascule**
- *Révéler la majorité* — rapproche perçu et réel dans un bloc. Usage limité à 2 ou 3 fois par partie.
- *Attribution rapide* — transforme l'événement du tour en gain d'opinion. Coût : crédibilité si l'attribution est faible.
- *Compensation ciblée* — annule la friction d'une mesure. Coût : capital élevé. Carte ennuyeuse et indispensable, ce qui est exactement le message.
- *Norme sectorielle* — interdit une technologie à partir du tour n+2. Friction élevée, effet durable, difficile à annuler.
- *Coalition industrielle* — retourne une fraction du capital Inertie qui a intérêt à la transition (électriciens, assureurs, constructeurs déjà engagés). Sous-estimé dans le débat public, très efficace dans le réel.

---

## 6. Choix du support

| Critère | Atelier (plateau ou web léger) | Jeu vidéo | Jeu de plateau commercial |
|---|---|---|---|
| Effort | 3 à 6 mois à temps partiel | 2 ans et plus, équipe | 12-18 mois + éditeur |
| Réalisme atteignable | Moyen, par tables calibrées | Élevé, moteur réel | Faible, 5-6 variables maximum |
| Valeur pédagogique | **Élevée**, le débriefing fait le travail | Variable, aucun débriefing | Moyenne |
| Concurrence | Faible sur ce créneau | Forte (En-ROADS gratuit) | Occupée (Daybreak) |
| Réutilisable dans ton activité | Directement | Non | Non |

**Recommandation :** prototype papier d'abord, quelle que soit la cible finale. Il coûte quelques week-ends, il se teste en 3 heures avec six personnes, et il tuera ou validera les mécaniques centrales (double jauge, attribution, retour de flamme) avant qu'une seule ligne de code ne soit écrite. Si les trois mécaniques tiennent sur papier, la question du moteur se posera dans de bien meilleures conditions.

---

## 7. Points ouverts à trancher

1. **Deux camps ou trois ?** L'ajout d'un camp Développement/Souveraineté augmente le réalisme et casse le manichéisme, au prix d'une complexité et d'un besoin de 3 joueurs.
2. **Le camp Inertie est-il jouable par une IA ?** Techniquement oui et c'est même le rôle le plus facile à automatiser (stratégie de blocage, peu de branchements). Utile pour un mode solo et pour éviter d'imposer ce rôle à quelqu'un en atelier.
3. **Que fait-on des acteurs non alignés ?** Système de PNJ, deck de comportements, ou blocs pilotés par des règles fixes.
4. **Année de départ.** 2026 est brutal (budget 1,5 °C épuisé). Démarrer en 2015 (Accord de Paris) permettrait de jouer la décennie perdue et de la faire ressentir, avec l'avantage supplémentaire d'une trajectoire réelle contre laquelle comparer la partie.
5. **Nom.** HEAT fonctionne. Vérifier la disponibilité, un jeu de survie et une série portent déjà ce nom.
6. **Public visé.** Grand public, enseignement supérieur, ou dirigeants d'entreprise ? Le calibrage des cartes Inertie change du tout au tout : un comité de direction reconnaîtra ses propres arguments, ce qui est puissant mais inconfortable.

---

## 8. Sources

- Forster et al., *Indicators of Global Climate Change 2025*, Earth System Science Data, juin 2026 — https://essd.copernicus.org/articles/18/3889/2026/
- Copernicus, *Global warming reached 1.37 °C in 2025* — https://climate.copernicus.eu/global-warming-reached-137degc-2025
- Friedlingstein et al., *Global Carbon Budget 2025*, ESSD — https://essd.copernicus.org/articles/18/3211/2026/ ; cibles clés — https://globalcarbonbudget.org/key-targets-2025/
- Lamb et al., *Discourses of climate delay*, Global Sustainability, 2020 — https://www.cambridge.org/core/journals/global-sustainability/article/discourses-of-climate-delay/7B11B722E3E3454BB6212378E32985A7 ; synthèse Carbon Brief — https://www.carbonbrief.org/guest-post-how-discourses-of-delay-are-used-to-slow-climate-action/
- Andre, Boneva, Chopra, Falk, *Globally representative evidence on the actual and perceived support for climate action*, Nature Climate Change, 2024 — https://www.nature.com/articles/s41558-024-01925-3
- Roozenbeek & van der Linden, *Bad News* / inoculation — https://www.sdmlab.psychol.cam.ac.uk/research/bad-news-game ; évaluation — https://journalofcognition.org/articles/10.5334/joc.91 ; réplication mitigée — https://pmc.ncbi.nlm.nih.gov/articles/PMC12705795/
- Climate Interactive, *En-ROADS* — https://www.climateinteractive.org/en-roads/ ; guide du modèle — https://docs.climateinteractive.org/projects/en-roads/en/latest/
- Évaluation académique d'En-ROADS en atelier, npj Climate Action — https://www.nature.com/articles/s44168-026-00348-4
- InfluenceMap, *Climate lobbying by the fossil fuel sector* — https://influencemap.org/report/Climate-Lobbying-by-the-Fossil-Fuel-Sector
- ADEME, *Transition(s) 2050* — https://librairie.ademe.fr/societe-et-politiques-publiques/5073-prospective-transitions-2050-infographies-scenarios.html
- The Shift Project, *Plan de transformation de l'économie française* — https://theshiftproject.org/app/uploads/2025/05/PTEF_web.pdf
- Sisco et al., *Local warming is real: a meta-analysis*, Current Opinion in Behavioral Sciences, 2021 — https://www.sciencedirect.com/science/article/abs/pii/S2352154621001017
- Daybreak (Leacock, 2023) — https://www.daybreakgame.org/
- Fate of the World, revue critique PAXsims — https://paxsims.wordpress.com/2011/09/12/review-fate-of-the-world/
