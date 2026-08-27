# HEAT — Note de conception v2

**Objet :** départ 2015, camps renommés, catalogue des leviers, contraintes du support jeu vidéo
**Date :** 17 août 2026
**Accompagne :** `HEAT_catalogue_leviers_v1.xlsx` (134 leviers)

---

## 1. Décisions actées

| Sujet | Décision |
|---|---|
| Point de départ | Décembre 2015, signature de l'Accord de Paris |
| Camps | **Climato-actif** contre **Climato-attentiste** |
| Intention | Démontrer qu'être actif n'est pas inefficace |
| Support | Jeu vidéo. PC / console / smartphone non tranché |
| Diffusion | La plus large possible, sans sacrifier la jouabilité |
| Échelle | Monde entier |
| Leviers | Tous inventoriés avant sélection ; l'arbitrage se fait ensuite par niveau de difficulté |

Le renommage règle le problème principal de la v1. « Attentiste » décrit exactement l'acteur réel : quelqu'un qui ne nie rien, ne s'oppose frontalement à rien, et obtient le report. C'est aussi un rôle qu'un joueur peut assumer sans se sentir idiot, condition nécessaire pour qu'il le joue sérieusement.

---

## 2. Ce que le départ 2015 apporte, et pourquoi c'est le meilleur choix possible

Démarrer à Paris n'est pas seulement un marqueur symbolique. C'est ce qui rend la démonstration **mesurable au lieu d'être assénée**.

Entre 2015 et 2025, le monde réel a joué la partie. Le résultat est documenté :

| | 2015 | 2025 |
|---|---|---|
| Réchauffement projeté en 2100, politiques en vigueur (Climate Action Tracker) | **3,6 °C** | **2,6 °C** |
| Réchauffement projeté, engagements pris en compte | — | 2,2 °C |
| Réchauffement d'origine humaine constaté | ~1,0 °C | **1,37 °C** |
| Coût d'installation du solaire utilitaire | — | **−88 % depuis 2010** (667 $/kW) |
| Part des voitures électriques dans les ventes mondiales | ~1 % | **> 20 %** |
| Capacité solaire installée dans le monde | ~230 GW | **2 393 GW** |

**Un degré de réchauffement évité en dix ans, avec une action largement insuffisante, mal coordonnée et constamment attaquée.** C'est la démonstration que le jeu cherche, et elle n'a pas besoin d'être racontée : elle est dans les données.

### La mécanique qui en découle : la ligne fantôme

Sur le graphe de trajectoire, une courbe grise permanente : **le monde réel**, tour par tour, de 2015 à 2025.

Le joueur ne joue pas contre un objectif abstrait. Il joue contre ce qui s'est réellement passé. La question posée à chaque fin de tour est : *fais-tu mieux que le monde réel a fait cette année-là ?*

Trois conséquences :

1. **Le score principal du camp Actif n'est pas la température atteinte, c'est la température évitée.** Un joueur qui finit à 2,4 °C alors que la trajectoire sans lui menait à 3,6 °C a évité 1,2 °C. C'est un chiffre positif dans un contexte négatif — exactement ce dont le message a besoin.
2. **La partie ne peut pas être accusée d'être truquée** : la référence est publique et vérifiable.
3. **Le camp Attentiste a lui aussi un repère** : a-t-il fait mieux que ses homologues réels, qui ont réussi à figer la trajectoire à 2,6 °C pendant quatre années consécutives ?

### Le risque à traiter : le jeu à message

Un jeu conçu pour démontrer quelque chose sera accusé de propagande par exactement le public qu'il veut atteindre. Trois contre-mesures, à décider maintenant parce qu'elles structurent tout :

- **Le camp Attentiste doit pouvoir gagner honnêtement.** Un jeu où l'Actif gagne toujours ne prouve rien et se disqualifie en une partie. La cible reste 25-30 % de bonnes fins pour l'Actif en difficulté Réaliste.
- **Chaque carte affiche sa source.** Un lien, une date, un rapport. Le catalogue ci-joint est déjà construit ainsi : toute carte sans ancrage réel daté ne devient pas une carte.
- **Le modèle est ouvert et auditable.** Les équations et les tables sont publiées. C'est la meilleure défense contre l'accusation de biais, et accessoirement un argument de communication pour un jeu qui revendique le réalisme.

Et une contrainte de fond : **ne pas rendre l'action facile, rendre l'inaction coûteuse.** Si le jeu rend la transition simple, il ment et le joueur le sent. Ce qui doit être visible, c'est l'écart entre ce qui a été évité et ce qu'il aurait fallu.

---

## 3. Le catalogue : 134 leviers

Fichier joint, onglet `Catalogue`, filtrable. Trois camps :

| Camp | Nombre | Puissance moyenne | Coût moyen |
|---|---|---|---|
| Climato-actif | 69 | 3,4 / 5 | 3,2 / 5 |
| Climato-attentiste | 53 | 4,0 / 5 | 2,6 / 5 |
| Pièges (leviers illusoires) | 12 | 1,1 / 5 | 2,8 / 5 |

Répartition par famille : réglementaire 17 · économique 26 · narratif 24 · discours de l'inaction 12 · institutionnel 11 · judiciaire 11 · technologique 10 · pièges 12 · électoral 6 · international 5.

### Ce que le catalogue révèle une fois rempli

Je n'ai pas cherché ces résultats, ils sont sortis du tri. Ils constituent à mon avis la vraie matière du game design.

**1. L'attentiste a des leviers plus puissants et moins chers.** 4,0 contre 3,4 en puissance, 2,6 contre 3,2 en coût. 14 leviers de puissance maximale côté attentiste, 8 côté actif. Ce n'est pas un biais de notation : bloquer coûte structurellement moins cher que construire.

**2. Les deux camps ne consomment pas la même ressource.**

- Actif : 37 leviers sur 69 consomment du **capital politique**. Il doit faire voter, faire adopter, faire tenir.
- Attentiste : 45 leviers sur 53 consomment du **capital** ou de l'**attention**, et seulement 6 du capital politique. **Il n'a pas besoin de faire voter quoi que ce soit.**

C'est la traduction mécanique la plus exacte de l'asymétrie réelle. Les deux camps ne jouent pas au même jeu sur le même plateau.

**3. Les horloges sont inversées.**

- Actif : 53 leviers sur 69 (77 %) ont une latence moyenne ou longue.
- Attentiste : 37 sur 53 (70 %) agissent immédiatement ou en un à deux tours.

L'Actif sème pour dans dix ans. L'Attentiste frappe ce tour-ci. Sur un horizon électoral, l'un des deux est structurellement avantagé.

**4. Et pourtant l'Actif a une voie de victoire — c'est la découverte utile.**

Les leviers **irréversibles** ne se répartissent pas de la même façon :

| Camp | Leviers irréversibles | Nature |
|---|---|---|
| Actif | 8 | Cour régionale des droits humains, avis de la CIJ, contentieux en responsabilité, révélation documentaire, accord transpartisan, constitutionnalisation, protocole sectoriel type Kigali, lanceur d'alerte |
| Attentiste | 4 | Verrouillage d'infrastructure, contrat de long terme, censure constitutionnelle, guerre culturelle |

**Les irréversibles de l'Actif sont juridiques et institutionnels. Ceux de l'Attentiste sont du béton et des contrats.** HEAT est une course entre le droit et le béton : qui accumule ses verrous le plus vite. Tout le reste — campagnes, sondages, polémiques, subventions — est effaçable au tour suivant.

C'est une bonne boucle de jeu, et c'est vrai.

### Les pièges

Les 12 leviers illusoires (compensation volontaire, plantation d'arbres, hydrogène automobile, e-fuels, CCS sur centrale électrique, net zéro 2050 sans étape, géoingénierie comme plan A, nucléaire présenté comme réponse à 2030…) ne sont pas du remplissage. **Ce sont les meilleures armes du camp Attentiste**, parce qu'ils sont joués par l'adversaire.

Un piège adopté par le camp Actif lui coûte un tour, du capital, et de la crédibilité quand il est démasqué. En difficulté Découverte ils sont signalés d'un pictogramme ; à partir de Standard ils ne le sont plus. C'est le mécanisme d'inoculation du jeu, et il fonctionne dans les deux sens : le joueur Actif apprend à les repérer, le joueur Attentiste apprend à les placer.

---

## 4. Le déblocage par difficulté

| Niveau | Leviers disponibles | Ce qui change |
|---|---|---|
| **1 — Découverte** | 40 | Leviers évidents. Pièges signalés. Contre-leviers adverses désactivés. Le joueur apprend la boucle. |
| **2 — Standard** | 92 | Institutionnel et financier courant. Pièges non signalés. Contre-leviers actifs. |
| **3 — Réaliste** | 131 | Capture réglementaire, ISDS, procédures-bâillon, détricotage administratif, portes tournantes. C'est le niveau où le jeu dit la vérité. |
| **4 — Expert** | 134 | Catalogue complet, y compris contentieux en responsabilité, constitutionnalisation et géoingénierie. |

La difficulté ne modifie pas les chiffres, elle modifie **quels leviers existent**. C'est plus honnête qu'un multiplicateur, et c'est aussi la meilleure courbe d'apprentissage : le joueur qui monte en difficulté découvre que le monde réel avait des mécanismes qu'il ne soupçonnait pas.

**Arbitrage à faire de ton côté :** la colonne `Verdict` du catalogue est vide et dotée d'une liste déroulante (Retenu / À tester / Écarté / En attente). L'onglet `Synthèse` compte l'avancement automatiquement.

Mon avis sur la cible : **60 à 70 cartes en jeu simultanément**, tirées d'un pool plus large selon le bloc, l'époque et la difficulté. Au-delà, le joueur ne lit plus.

---

## 5. Contraintes du support et de la diffusion large

### La tension à trancher

134 leviers contre « bonne jouabilité sur smartphone » : c'est le vrai arbitrage du projet. La résolution n'est pas de couper dans le catalogue, c'est de **hiérarchiser les décisions**.

Architecture en trois couches :

- **Couche 1 — la décision du tour.** 3 à 5 cartes proposées, une à trois jouées. C'est tout ce que le joueur mobile voit. Un tour se boucle en moins de deux minutes.
- **Couche 2 — la doctrine.** Réglages persistants (priorité régionale, arbitrage contrainte/incitation, ligne de compensation sociale) modifiés rarement, entre deux tours.
- **Couche 3 — le modèle.** Consultable, jamais obligatoire. Courbes, tables, sources. C'est ce qui donne sa crédibilité au jeu et ce qui intéressera 5 % des joueurs.

Un jeu jouable en couche 1 seule, profond si on descend. C'est ce que fait En-ROADS à l'envers : il ouvre sur la couche 3, et perd tout le monde sauf les experts.

### Ordre de sortie recommandé

1. **PC en premier (Steam).** Public de la simulation et de la stratégie, pas de gardien de plateforme, tolérance à la densité, moddabilité — et la moddabilité est précisément ce qui permet d'ouvrir le modèle et de désamorcer l'accusation de propagande.
2. **Version web gratuite, jouable en navigateur, partie courte.** C'est le vrai vecteur de diffusion large pour un jeu à message : un lien qui se partage, sans installation, sans compte. À concevoir dès le départ, pas en portage.
3. **Mobile ensuite.** Le format tour par tour s'y prête, à condition que la couche 1 ait été conçue mobile-first dès le prototype.
4. **Console en dernier, voire jamais.** Coût de certification élevé, public mal ajusté, aucun bénéfice de diffusion.

### Le modèle économique et son piège

Un financement institutionnel (ADEME, Union européenne, fondation) résout le budget et crée immédiatement le procès en propagande. Si tu prends cette voie, il faut la contrepartie : comité scientifique nommé publiquement, sources ouvertes carte par carte, modèle publié, et un financeur qui accepte de n'avoir aucun droit de regard sur le contenu — par écrit.

L'alternative est un modèle mixte : version web gratuite financée par l'institution, version PC premium autofinancée. Le gratuit fait la diffusion, le payant fait l'indépendance.

### Deux points à ne pas manquer

- **Localisation.** Le catalogue est fortement ancré en Europe et en France. Une diffusion mondiale suppose des jeux de cartes par bloc — l'Attentiste américain, l'Attentiste indien et l'Attentiste européen ne jouent pas les mêmes coups. C'est un travail de contenu considérable, à budgéter tôt.
- **Le public réel.** Le risque principal n'est pas que le jeu soit mauvais, c'est qu'il ne soit joué que par des convaincus. La seule parade est que **le rôle Attentiste soit réellement plaisant à jouer et que ses arguments soient présentés dans leur version la plus forte**. Un adversaire caricatural garantit un public d'entre-soi.

---

## 6. Prochaines étapes proposées

1. **Arbitrer le catalogue** — colonne `Verdict`. C'est le prérequis de tout le reste.
2. **Prototype papier de la couche 1**, 8 tours, 2015-2055, une trentaine de cartes. Objectif : vérifier les trois mécaniques centrales (double jauge perçu/réel, attribution, retour de flamme) et la ligne fantôme.
3. **Fixer la maille temporelle** — tours de 2 ans (20 tours) ou de 5 ans (8 tours).
4. **Écrire le modèle** — une feuille de calcul suffit à ce stade : émissions par bloc, cumul, `T = 1,0 + 0,00045 × cumul depuis 2015`, dommages, opinion. Le calibrer contre la décennie réelle 2015-2025 : si le modèle ne reproduit pas la trajectoire connue, il est faux.
5. **Décider du nom.** HEAT est utilisé par plusieurs jeux et une série. À vérifier avant de s'y attacher.

---

## 7. Sources

- Climate Action Tracker, *Global Update 2025* et *Historical Progress* — https://climateactiontracker.org/publications/warming-projections-global-update-2025/ · https://climateactiontracker.org/global/historical-progress/
- PNUE, *Emissions Gap Report 2025* — https://www.unep.org/resources/emissions-gap-report-2025
- Forster et al., *Indicators of Global Climate Change 2025*, ESSD, juin 2026 — https://essd.copernicus.org/articles/18/3889/2026/
- Friedlingstein et al., *Global Carbon Budget 2025* — https://globalcarbonbudget.org/key-targets-2025/
- IRENA, *Renewable Power Generation Costs in 2025* — https://www.irena.org/-/media/Files/IRENA/Agency/Publication/2026/Jul/IRENA_TEC_RPGC_2025_Executive_summary_2026.pdf
- AIE, *Global EV Outlook 2025 / 2026* — https://www.iea.org/reports/global-ev-outlook-2026/trends-in-electric-cars
- Lamb et al., *Discourses of climate delay*, Global Sustainability, 2020 — https://www.cambridge.org/core/journals/global-sustainability/article/discourses-of-climate-delay/7B11B722E3E3454BB6212378E32985A7
- Andre, Boneva, Chopra, Falk, *Globally representative evidence on the actual and perceived support for climate action*, Nature Climate Change, 2024 — https://www.nature.com/articles/s41558-024-01925-3
- CIJ, *Obligations des États en matière de changement climatique*, avis consultatif, 23 juillet 2025 — https://elaw.org/resource/icj_climateao_2025
- CEDH, *KlimaSeniorinnen c. Suisse*, avril 2024 · Urgenda (2019) · Milieudefensie c. Shell (2021, infirmé 2024)
- CIEL / E3G sur l'ISDS et le Traité sur la Charte de l'énergie — https://www.ciel.org/investors-v-climate-action/ · https://www.e3g.org/news/explained-why-investor-state-dispute-settlement-isds-matters-for-the-energy-transition/
- InfluenceMap, *Climate lobbying by the fossil fuel sector* — https://influencemap.org/report/Climate-Lobbying-by-the-Fossil-Fuel-Sector
- *The natural gas industry, the Republican Party, and state preemption of local building decarbonization*, npj Climate Action, 2024 — https://www.nature.com/articles/s44168-024-00176-4
- Corporate Accountability, *Built to fail? World's largest carbon offset projects* — https://corporateaccountability.org/resources/built-to-fail-carbon-offset-projects/
- Ember, *The UK's journey to a coal power phase-out* — https://ember-energy.org/latest-insights/the-uks-journey-to-a-coal-power-phase-out/
- ADEME, *Transition(s) 2050* · The Shift Project, *Plan de transformation de l'économie française*
