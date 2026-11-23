# HEAT — version jouable v0.14

Fichier : `jeu/jeu.html`, autonome, aucune dépendance, s'ouvre par double-clic.
L'archive datée est à côté, sous `HEAT_jeu_v0.14.html`.

## v0.14 — après la COP31

La COP31 (Antalya, 9-22 novembre 2026) s'est achevée sans accord sur sa décision principale. Le « pacte d'Antalya » n'a pas été adopté : le texte de compromis ne mentionnait pas les énergies fossiles, et l'Union européenne, le Royaume-Uni et les petits États insulaires l'ont refusé. Quelques décisions techniques sont passées (Fonds d'adaptation, programme de transition juste, marchés carbone, transparence). Restent en revanche dans des projets jamais adoptés : l'objectif turc de 35 % d'électrification, le chiffrage de la finance d'adaptation à 120 Md$/an d'ici 2035, et le mécanisme de transition juste Belém-Antalya.

Cette version ne change aucune règle : elle met à jour ce que le jeu affirme du monde réel.

### Le monde réel passe de 2,60 à 2,70 °C

Le Climate Action Tracker a publié sa mise à jour annuelle le 12 novembre 2026, pendant la COP. Avec les politiques en vigueur, la trajectoire mène à **2,7 °C** en 2100, contre 2,6 °C en 2025. Le PNUE (Emissions Gap Report 2026) donne 2,8 °C.

- `REEL_2100 = 2,70`, nouvelle constante unique.
- La courbe grise « monde réel » (`GHOST`) garde sa forme, remise à l'échelle entre 3,48 et 2,70.
- Tous les textes qui citaient 2,60 ont été mis à jour : écran de fin, tableau de bord, guide, règles, verdict.
- Les leviers qui citent la trajectoire 2015-2025 (de 3,6 à 2,6 °C) ajoutent la remontée à 2,7 °C en 2026.

La ligne « monde réel » ne sert qu'à l'affichage : le score et l'étalonnage sont inchangés, et `verifier.py` donne les mêmes chiffres qu'en v0.13.

### Trois ancrages de leviers mis à jour

| Levier | Ce qui est ajouté |
|---|---|
| T64 — Blocage du consensus | COP28 : « transition hors des fossiles » plutôt que sortie ; COP30 : feuille de route de sortie (plus de 80 pays) retirée du texte final ; COP31 : aucun accord, pacte d'Antalya non adopté. L'ancienne formulation (« écartée à répétition, COP28 puis COP29 ») était imprécise pour la COP28. |
| A29 — Financement climat Nord-Sud | 300 Md$/an *d'ici 2035* (Bakou) ; appel à « au moins tripler » la finance d'adaptation d'ici 2035, sans année de référence (Belém) ; chiffrage à 120 Md$/an resté dans un projet non adopté (Antalya). |
| T18 — Occupation des négociations | COP31 : une soixantaine de groupes de l'industrie fossile ont leur délégation, Exxon en tête avec treize personnes ; selon Kick Big Polluters Out, les délégations des grands pollueurs sont cent fois plus nombreuses que celle de Saint-Vincent-et-les-Grenadines. |

### Sources, consultées le 23 novembre 2026

- ONU Info : COP31 ends without climate pact (22 novembre 2026)
- IISD : COP 31 Ends Without Antalya Pact
- Climate Action Tracker : Global Update, novembre 2026
- PNUE : Emissions Gap Report 2026
- Kick Big Polluters Out : Big Polluters at COP31
- Pour la COP30 : Carbon Brief, ODI, C2ES

Ces comptes rendus datent des jours qui suivent la clôture. Le texte officiel des décisions adoptées n'a pas été relu.
