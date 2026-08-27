# HEAT — Note de conception v3

**Objet :** architecture de simulation (question En-ROADS) et conception du rôle attentiste comme rôle jouable
**Date :** 17 août 2026
**Suite de :** `HEAT_note_de_cadrage_v1.md`, `HEAT_note_conception_v2.md`

---

## Partie A — Peut-on s'appuyer sur En-ROADS ?

### A.1 Ce qui est réellement disponible

| Élément | Statut | Conséquence |
|---|---|---|
| Modèle Vensim d'En-ROADS | **Non public.** Climate Interactive répond explicitement qu'il n'est pas accessible aux utilisateurs | Pas de récupération directe du modèle |
| **SDK En-ROADS** | **Licences commerciale et non commerciale disponibles sur demande** — contact : support@climateinteractive.org | C'est la voie officielle pour intégrer En-ROADS dans une application tierce |
| Usage du simulateur en ligne | Libre, y compris commercial, avec citation obligatoire (« créé par Climate Interactive et MIT Sloan ») ; don suggéré en usage commercial | On peut légalement s'en servir comme outil de travail et de calibration |
| **En-ROADS Technical Reference** | Publique, décrit la structure et une grande partie des équations | Réimplémentation partielle possible sans licence |
| **SDEverywhere** | **Open source, licence MIT, développé par Climate Interactive** | Transpile un modèle Vensim vers C, JavaScript et WebAssembly — c'est le moyen technique par lequel En-ROADS tourne dans un navigateur |
| Supports pédagogiques En-ROADS | Creative Commons BY 4.0 | Réutilisables et adaptables, y compris commercialement |

Donc la réponse courte à ta question est **oui, techniquement et juridiquement, c'est possible** : il existe un SDK sous licence, et la chaîne d'outils qui compile un modèle système-dynamique en WebAssembly est en MIT et maintenue par Climate Interactive eux-mêmes. L'embarquement d'un modèle de ce type dans un jeu est un problème résolu.

### A.2 Pourquoi je te déconseille quand même de l'embarquer

Quatre raisons, dans l'ordre d'importance.

**1. En-ROADS ne modélise pas ce dont HEAT a besoin.** Il modélise l'énergie, l'économie et le climat. Il ne modélise ni l'opinion, ni les élections, ni les médias, ni le lobbying, ni la friction sociale, ni le retour de flamme — c'est-à-dire la totalité de ce qui fait le jeu. Tu embarquerais un moteur remarquable pour la partie la moins intéressante de ton produit, et tu devrais écrire toi-même la partie difficile de toute façon.

**2. Il est mondial, pas régional.** En-ROADS raisonne sur un monde agrégé. Il ne peut pas répondre à « que se passe-t-il si l'Europe agit et que les États-Unis ne bougent pas », qui est précisément la question de HEAT à huit blocs. C'est C-ROADS qui traite les régions, et il est conçu pour la négociation, pas pour la simulation d'un affrontement.

**3. Dépendance de ton cœur de produit à un tiers.** Une licence SDK peut être renégociée, restreinte, ou son mainteneur peut changer de priorité. Faire reposer le moteur d'un jeu commercial sur un composant sous licence tierce et non substituable est un risque que je ne prendrais pas sur un projet destiné à durer.

**4. Reproductibilité.** Un jeu a besoin d'un déterminisme strict : replays, classements, parties asynchrones, corrections d'équilibrage sans casser les sauvegardes. Un modèle système-dynamique intégré par la méthode d'Euler à pas fixe est déterministe, mais tu ne contrôles pas ses versions ni ses changements de calibration. Tu veux figer ton modèle, pas suivre le leur.

### A.3 Architecture recommandée : trois couches, une seule à écrire

```
COUCHE 1 — PHYSIQUE DU CLIMAT           →  ne pas réinventer
   Runtime  : T = 1,0 + 0,00045 × CO2 cumulé depuis 2015   (TCRE, GIEC AR6)
   Hors ligne : FaIR v2.1 (Python, licence Apache 2.0, calibré AR6,
                utilisé pour l'évaluation des trajectoires du GIEC)
   Rôle    : générer les tables de réponse, vérifier l'émulateur simple,
             produire l'incertitude de sensibilité climatique tirée en début de partie

COUCHE 2 — ÉNERGIE / ÉCONOMIE           →  pré-calculer, pas embarquer
   Méthode : faire tourner En-ROADS sur N combinaisons de leviers,
             enregistrer les trajectoires, interpoler dans le jeu
   Statut  : usage libre y compris commercial, avec citation. Aucune licence à négocier.
   Bénéfice: crédibilité « calibré sur En-ROADS / MIT Sloan » sans dépendance technique

COUCHE 3 — SOCIAL / POLITIQUE / MÉDIA   →  à écrire, c'est le jeu
   Opinion réelle et perçue, élections, attention, friction, retour de flamme,
   verrouillage d'infrastructure, coalitions. Aucun modèle existant ne couvre ça.
```

Autrement dit : **En-ROADS comme oracle de calibration, pas comme moteur.** Tu passes deux semaines à produire des tables, tu gagnes la rigueur, tu ne prends aucune dépendance, et tu peux citer la source.

Si tu veux malgré tout viser l'intégration temps réel, l'ordre des choses est : écrire d'abord la couche 3 et un émulateur simple en couche 2, puis contacter Climate Interactive une fois que tu as un prototype à leur montrer. Une demande de SDK adossée à un projet démontrable a une bien meilleure chance qu'une demande abstraite.

### A.4 Le test de validation qui vaut mieux que toute discussion

Le modèle doit **reproduire la décennie 2015-2025**. On injecte les leviers réellement joués par le monde réel, et on doit retomber sur les valeurs connues :

| Indicateur | Valeur attendue en 2025 |
|---|---|
| Réchauffement d'origine humaine | 1,37 °C |
| CO2 atmosphérique | 425,6 ppm |
| Émissions CO2 fossiles | 38,1 GtCO2/an |
| Projection 2100, politiques en vigueur | 2,6 °C |
| Coût d'installation du solaire utilitaire | 667 $/kW (−88 % depuis 2010) |
| Part des ventes de voitures électriques | > 20 % |

C'est un test unitaire, pas une opinion. Si le modèle ne passe pas, il est faux, quelle que soit son élégance. Et c'est aussi ton meilleur argument public : *notre modèle rejoue la décennie écoulée à x % près*.

### A.5 Autres modèles ouverts, si besoin

| Modèle | Licence | Usage possible |
|---|---|---|
| **FaIR v2.1** | Apache 2.0 | Émulateur climatique de référence. Le meilleur choix pour la couche 1. |
| Hector | Open source | Alternative à FaIR, plus détaillée sur le cycle du carbone |
| DICE / RICE (Nordhaus) | Publiés | Couplage économie-climat très simplifié, utile comme point de comparaison |
| MESSAGEix, REMIND, GCAM | Open source | Modèles d'évaluation intégrée complets. Trop lourds pour un jeu, utiles en calibration. |
| PyPSA | Open source | Système électrique détaillé. Pertinent si tu veux traiter finement le réseau. |

---

## Partie B — Rendre le rôle attentiste aussi jouable que l'autre

### B.1 Le principe directeur

Il ne faut pas que le jeu **punisse** le joueur attentiste. Il faut qu'il lui montre **ce qu'il achète, et à qui il le fait payer**.

La punition produit du rejet et le joueur décroche. Le découplage produit de la compréhension, et il continue à jouer. C'est toute la différence entre un jeu à message qui marche et un jeu à message qu'on abandonne au bout de vingt minutes.

### B.2 Son tableau de bord : des compteurs qui montent

Le rôle attentiste doit être un jeu de gestion satisfaisant, avec ses propres indicateurs positifs :

| Compteur | Ce qu'il mesure |
|---|---|
| **Valeur d'actifs préservée** | Capital fossile non déprécié, en Md$ |
| **Mesures contraignantes évitées** | Compteur simple, très lisible |
| **Années de report gagnées** | Décalage cumulé imposé aux mesures adverses |
| **Rentes distribuées** | Dividendes et rachats d'actions versés à sa base |
| **Indice de stabilité du mode de vie** | Confort du quintile supérieur : mobilité, alimentation, climatisation, sécurité |
| **Marge de manœuvre réglementaire** | Nombre de juridictions encore non contraintes |

C'est un plaisir d'optimisation classique : des courbes qui montent, des arbitrages de tempo, une pression croissante. Rien de moralisateur. C'est précisément ce qui le rend jouable.

### B.3 La mécanique centrale : le découplage des dommages

**Deux jauges de dommages, affichées séparément et en permanence.**

- **Dommages subis par sa base** (quintile supérieur, blocs riches) : reste bas très longtemps. Il s'adapte — climatisation, assurance, irrigation, relocalisation, sécurité privée.
- **Dommages subis par les autres** : monte tôt, monte fort, et ne se compense pas.

Ce découplage n'est pas une invention morale, il est mesuré :

| Fait | Chiffre | Source |
|---|---|---|
| Émissions du 1 % le plus riche | **75,1 tCO2/personne/an** contre un budget équitable de 2,1 t | Oxfam, janvier 2026 |
| Date d'épuisement de leur part annuelle | **10 janvier** ; le 3 janvier pour le 0,1 % | Oxfam, 2026 |
| Une personne du 0,1 % | émet plus en **un jour** que la moitié la plus pauvre en un an | Oxfam, 2026 |
| Portefeuille d'un milliardaire moyen | **1,9 MtCO2/an** via ses participations | Oxfam, 2026 |
| Morts liées à la chaleur attribuables aux émissions des super-riches de 2019 | **1,3 million** d'ici la fin du siècle | Oxfam, 2026 |
| Dommages économiques aux pays à revenu faible et intermédiaire, 1990-2050 | **44 000 Md$** | Oxfam, 2026 |

Et le mécanisme le plus intéressant à jouer, parce qu'il est physique et non moral : **le retrait assurantiel**. Au-delà d'un seuil de dommages, les assureurs se retirent de zones entières. Le riche paie plus cher et reste couvert ; les autres deviennent non assurables, donc non finançables, donc leur patrimoine s'effondre. C'est documenté aux États-Unis en Floride et en Californie, et c'est le meilleur convertisseur de « température » en « injustice » qui existe : il est comptable, pas idéologique.

Ordre de grandeur pour calibrer : **107 Md$ de pertes assurées en 2025**, sixième année consécutive au-delà de 100 Md$, dont 40 Md$ pour les seuls incendies de Los Angeles ; les périls secondaires — incendies, orages violents, inondations — représentent 92 % du total. Swiss Re projette jusqu'à 320 Md$ dans un scénario de pointe pour 2026.

### B.4 Le moment de bascule — ce qui rend le rôle instructif

Vers le milieu de partie, quelque chose doit se produire dans **son** tableau de bord, pas dans celui de l'adversaire.

Ses propres actifs commencent à être touchés. Le retrait assurantiel qu'il a laissé s'installer atteint ses implantations. Ses chaînes d'approvisionnement cassent. Ses coûts d'adaptation explosent. Ses raffineries sont dans des zones littorales. Il découvre que son gain n'était pas un revenu mais un emprunt.

À ce moment, le jeu lui ouvre une porte : **convertir**. Passer d'attentiste à opportuniste de la transition, en conservant ses points acquis. Celui qui convertit tôt garde presque tout. Celui qui convertit tard perd tout.

C'est la leçon la plus utile que le jeu puisse transmettre, et elle ne se dit pas, elle se joue : **l'attentisme n'est pas rentable jusqu'au bout, il est rentable jusqu'à un point qu'on ne voit pas venir.**

C'est aussi, accessoirement, ce que fait réellement une partie du capital depuis 2015 — et c'est ce qui rend la mécanique défendable devant quelqu'un qui n'est pas d'accord avec toi.

### B.5 Compteurs partagés, visibles des deux joueurs en permanence

| Compteur | Référence réelle pour la calibration |
|---|---|
| Température, avec la ligne fantôme du monde réel | 1,37 °C en 2025 ; projection 3,6 °C → 2,6 °C entre 2015 et 2025 |
| Morts liées à la chaleur, cumulées | **546 000/an** en moyenne récente, **+23 % depuis les années 1990** |
| Heures de travail perdues | **640 milliards d'heures** en 2024, ~**1 090 Md$** de pertes de productivité |
| Coût sanitaire de la surmortalité des personnes âgées | **261 Md$/an** |
| Insécurité alimentaire | **+124 millions de personnes** en 2023 (sécheresses et canicules) |
| Catastrophes de l'année et pertes assurées | **107 Md$** en 2025 |
| Jours de chaleur dangereuse attribuables au changement climatique | **16 jours** en moyenne mondiale en 2024 |

Et un compteur que le camp actif doit voir monter aussi, pour que le jeu ne soit pas manichéen : **décès évités par la réduction de la pollution au charbon — environ 160 000 par an entre 2010 et 2022.** L'action a des bénéfices sanitaires immédiats et mesurables, indépendants du climat. C'est le meilleur argument du camp actif et il n'est presque jamais joué.

### B.6 Écran de fin

Les deux courbes de dommages côte à côte : la sienne, celle des autres. Aucun commentaire, aucune voix off, aucun jugement. Les chiffres, et l'écart.

Puis une seule phrase factuelle : ce que la partie a coûté, et ce qu'elle aurait coûté sans le camp actif.

### B.7 Ce qu'il ne faut surtout pas faire

Je le liste parce que c'est la pente naturelle d'un jeu à message, et que chacun de ces points tuerait le projet :

- **Pas de jauge de culpabilité, pas de score moral.** Ça transforme le rôle en punition. Le joueur ferme le jeu.
- **Pas de narrateur qui commente ses choix.** S'il faut expliquer la leçon, la mécanique a échoué.
- **Pas de victoire attentiste rendue impossible.** Il doit pouvoir gagner. L'écran de fin doit être froid, pas vengeur.
- **Pas d'arguments attentistes en version faible.** Un adversaire de paille ne s'affronte pas, il se méprise — et le jeu ne se joue plus qu'entre convaincus.
- **Pas de compteur de morts en gros chiffres rouges clignotants.** L'effet obtenu est l'inverse de celui recherché : désensibilisation immédiate. Chiffre sobre, mise à jour discrète, consultable en détail.

### B.8 Deux plaisirs différents, et c'est voulu

| | Camp actif | Camp attentiste |
|---|---|---|
| Nature du plaisir | Construction, coalition, verrouillage | Optimisation, tempo, esquive |
| Horizon | Long, satisfaction différée | Court, gratification immédiate |
| Tension centrale | « Est-ce que ça va tenir ? » | « Jusqu'où je pousse avant que ça me revienne ? » |
| Ressource critique | Capital politique | Attention et capital |
| Fin de partie | Récolte ce qu'il a semé dix tours plus tôt | Doit décider quand convertir |

Deux boucles distinctes, comme dans un jeu asymétrique bien conçu. C'est ce qui donne la rejouabilité : on rejoue pour apprendre l'autre rôle, pas pour refaire le même.

---

## Partie C — Un point d'hygiène des sources, à intégrer dès maintenant

Un jeu qui revendique le réalisme et affiche ses sources carte par carte hérite d'un risque : **les sources bougent**.

Cas concret survenu pendant la préparation de cette note. L'étude la plus citée sur le coût économique du changement climatique — Kotz, Levermann et Wenz, *The economic commitment of climate change*, Nature, avril 2024, qui annonçait 19 % de perte de revenu mondial d'ici 2050 et 38 000 Md$ de dommages annuels — a été **rétractée par ses auteurs en décembre 2025**. Elle a été massivement reprise pendant vingt mois. Un jeu sorti en 2025 avec ce chiffre en dur dans son modèle serait aujourd'hui indéfendable.

Trois conséquences de conception :

1. **Privilégier les indicateurs mesurés aux projections modélisées.** Les pertes assurées, les décès liés à la chaleur, les heures de travail perdues, les ppm de CO2 sont mesurés. Une perte de PIB en 2050 est un modèle. Les deux ont leur place, mais pas au même endroit : le mesuré dans les compteurs, le modélisé dans les projections clairement étiquetées comme telles.
2. **Chaque carte porte sa source avec une date et un état de revue.** Un fichier de sources externalisé, pas des chiffres en dur dans le code.
3. **Prévoir un cycle de mise à jour annuel**, calé sur les publications de référence : Global Carbon Budget et Emissions Gap en novembre, Indicators of Global Climate Change en juin, Climate Action Tracker après chaque COP, Lancet Countdown en octobre.

C'est du travail, et c'est aussi ce qui distinguerait HEAT d'un jeu militant.

---

## Prochaines étapes

1. **Arbitrer le catalogue** (colonne `Verdict` de `HEAT_catalogue_leviers_v1.xlsx`) — toujours le prérequis.
2. **Ouvrir En-ROADS et jouer trois scénarios** avec les leviers que tu envisages de retenir. C'est le moyen le plus rapide de vérifier si tes ordres de grandeur tiennent, et c'est gratuit.
3. **Décider de la question du SDK** : je recommande de la reporter jusqu'à avoir un prototype. Un courriel à support@climateinteractive.org adossé à une démo aura une tout autre portée.
4. **Écrire le modèle en tableur** : émissions par bloc, cumul, TCRE, dommages, deux jauges d'opinion, deux jauges de dommages. Le calibrer contre 2015-2025.
5. **Prototype papier** de la couche 1 avec les deux tableaux de bord asymétriques, pour tester si le rôle attentiste est effectivement plaisant à jouer. C'est un test à faire sur des joueurs qui ne partagent pas ton avis sur le sujet — sinon il ne prouve rien.

---

## Sources

**En-ROADS et outillage**
- Conditions d'utilisation et de citation d'En-ROADS et C-ROADS, mention du SDK sous licence — https://support.climateinteractive.org/support/solutions/articles/47001266571-how-to-use-and-cite-en-roads-and-c-roads
- Accès au modèle Vensim : réponse officielle — https://support.climateinteractive.org/support/solutions/articles/47001149457-can-i-get-access-to-the-vensim-model-
- En-ROADS Technical Reference — https://docs.climateinteractive.org/projects/en-roads-reference-guide/en/latest/
- SDEverywhere (Vensim → C / JS / WebAssembly, licence MIT) — https://github.com/climateinteractive/SDEverywhere
- Évaluation académique d'En-ROADS en atelier, npj Climate Action — https://www.nature.com/articles/s44168-026-00348-4

**Modèles ouverts**
- FaIR v2.1 (Apache 2.0) — https://pypi.org/project/fair/ ; calibration et validation, GMD 2024 — https://gmd.copernicus.org/articles/17/8569/2024/
- Émulateurs climatiques utilisés pour l'évaluation des trajectoires du GIEC AR6 WGIII — https://climate-assessment.readthedocs.io/en/latest/emulator.html

**Conséquences et inégalité**
- Oxfam, *Richest 1% have blown through their fair share of carbon emissions for 2026 in just 10 days*, janvier 2026 — https://www.oxfam.org/en/press-releases/richest-1-have-blown-through-their-fair-share-carbon-emissions-2026-just-10-days
- Lancet Countdown 2025, communiqué OMS — https://www.who.int/news/item/29-10-2025-climate-inaction-is-claiming-millions-of-lives-every-year--warns-new-lancet-countdown-report ; rapport — https://lancetcountdown.org/2025-report/
- Swiss Re Institute, sigma 1/2026, pertes catastrophes naturelles 2025 — https://www.swissre.com/institute/research/sigma-research/sigma-2026-01-natcat-2025-wildfire-storm-risk.html
- First Street / CBS News sur les zones devenues « essentiellement non assurables » — https://www.cbsnews.com/news/insurance-policy-california-florida-uninsurable-climate-change-first-street/
- Yale Law Journal, *The Uninsurable Future* — https://yalelawjournal.org/essay/the-uninsurable-future-the-climate-threat-to-property-insurance-and-how-to-stop-it

**Calibration climat**
- Climate Action Tracker, *Global Update 2025* — https://climateactiontracker.org/publications/warming-projections-global-update-2025/
- Forster et al., *Indicators of Global Climate Change 2025*, ESSD 2026 — https://essd.copernicus.org/articles/18/3889/2026/
- Global Carbon Budget 2025 — https://globalcarbonbudget.org/key-targets-2025/
- IRENA, *Renewable Power Generation Costs in 2025* — https://www.irena.org/-/media/Files/IRENA/Agency/Publication/2026/Jul/IRENA_TEC_RPGC_2025_Executive_summary_2026.pdf

**Hygiène des sources**
- Retraction Note, *The economic commitment of climate change*, Nature, décembre 2025 — https://www.nature.com/articles/s41586-025-09726-0 ; contexte — https://retractionwatch.com/2025/12/03/authors-retract-nature-paper-projecting-high-costs-of-climate-change/
