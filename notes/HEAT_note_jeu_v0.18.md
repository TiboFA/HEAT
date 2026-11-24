# HEAT v0.18 — version anglaise et bouton FR · EN

## Ce que voit le joueur

- Un sélecteur **FR · EN** en haut de l'écran d'accueil et dans la barre du jeu.
- Changer de langue en cours de partie enregistre la partie et ouvre l'autre page, qui la reprend au même tour, à l'identique (testé dans les deux sens). Le journal déjà écrit reste dans la langue où il a été écrit.
- En ligne, le choix est retenu : une visite suivante sur l'autre page y renvoie. Pas en local, où le fichier téléchargé seul n'a pas son jumeau à côté de lui.
- En anglais, les décimales passent au point (3.48 °C), les guillemets et la ponctuation suivent l'usage anglais.

## Comment c'est fait

Le jeu reste écrit en français dans `jeu/src/`. `build.py` produit en plus `en.html` en remplaçant chaque morceau de texte par sa traduction, lue dans `jeu/i18n/en.json` — 1 835 morceaux, environ 145 000 caractères : règles, 112 leviers (nom, effet, mécanisme, ancrage réel, limite, nom donné par l'autre camp), événements, défis, combinaisons, presse, journal, bilans, fiches, guide, écran de fin.

`outils/i18n.py` repère le texte sans exécuter le code (chaînes, parties fixes des gabarits, blocs de texte HTML et attributs lisibles), et garde la même traduction pour les mêmes mots : une chaîne comparée ailleurs dans le code reste cohérente avec elle-même.

## Vérifications

- **Le moteur est le même** : l'étalonnage (10 parties par configuration, 8 configurations) donne des résultats identiques au chiffre près en français et en anglais. Une clé interne traduite par erreur les aurait fait diverger.
- Deux parties complètes jouées dans l'interface anglaise (un camp chacune), avec guide, fiches, bilans et journal : aucune erreur, et tout le texte affiché relu à la recherche de français oublié.
- `verifier.py` contrôle désormais aussi que `en.html` est à jour, qu'aucun texte n'est sans traduction, et joue une partie complète en anglais.

## Corrections faites au passage (visibles aussi en français)

- L'étiquette doctrinale d'une carte (aligné / neutre / opposé) servait aussi de classe CSS ; la classe est maintenant séparée du libellé.
- Les accords au pluriel d'adjectifs (« restants », « possibles », « ouverts », « adverses », « autres », « évitées ») passent par une forme entière, `pl(n, singulier, pluriel)`.

## Limites

- La traduction est la mienne, relue écran par écran mais pas par un anglophone natif. Les ancrages réels (lois, procès, rapports) gardent leurs noms d'origine.
- Toute nouvelle phrase française doit recevoir sa traduction (`python3 outils/i18n.py extraire`), sinon la vérification échoue : c'est voulu.

Aucune règle ni donnée modifiée.
