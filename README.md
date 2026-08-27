# HEAT

Un jeu de simulation climatique en un seul fichier HTML autonome. Deux camps
s'affrontent de 2015 à 2100 : le **climato-actif**, qui veut contraindre les
émissions, et le **climato-attentiste**, qui veut retarder, diluer et défaire.

Le jeu existe pour répondre à une objection précise — *« de toute façon ça ne
sert à rien »*. Il ne la réfute pas par un discours : il la met en jeu, donne au
camp attentiste un répertoire aussi riche et aussi documenté que celui d'en
face, et laisse le joueur mesurer ce que l'action retranche à la trajectoire.
Les deux rôles doivent être également jouables et également instructifs.

## Jouer

Ouvrir **`jeu/jeu.html`** par un double-clic. Ce nom ne change jamais : c'est
toujours la dernière version, et le numéro s'affiche sur l'écran d'accueil. Un
raccourci vers ce fichier reste valable d'une version à l'autre.

Aucune installation, aucune dépendance, aucun accès réseau. La partie se
sauvegarde toute seule dans le navigateur, et peut s'exporter en fichier.

Les `HEAT_jeu_vX.Y.html` à côté sont l'archive : les anciennes versions ne sont
plus reconstructibles depuis les sources actuelles, on les garde telles quelles.

Un guide en huit étapes s'ouvre à la première partie.

## Ce qu'il y a dedans

- **112 leviers**, chacun avec son mécanisme, son ancrage réel daté, sa limite,
  son contre-levier et le nom que lui donne le camp d'en face. Sept d'entre eux
  rapportent nettement moins que leur intitulé ne le promet — rien sur la carte
  ne les distingue, seule la fiche le dit.
- **Huit blocs** géographiques, quatre jauges chacun : contrainte, soutien réel,
  soutien perçu, friction.
- **Dix-sept tours** de cinq ans. La température affichée n'est pas une
  extrapolation : c'est celle que la partie atteint, le modèle rejoué jusqu'en
  2100 à contraintes figées.
- **Le climat tient en une ligne** : `T = 1,0 + 0,00058 × CO₂ cumulé depuis 2015`.
  Ne rien faire donne **3,48 °C**.

## Structure du dépôt

```
jeu/jeu.html  la dernière version — c'est celle qu'on ouvre
jeu/          l'archive des versions, un fichier HTML autonome chacune
jeu/src/      les sources — cinq morceaux concaténés par build.py
notes/        une note par version : ce qui a changé, pourquoi, et les mesures
cadrage/      la note de cadrage, les catalogues de leviers, les maquettes
outils/       bancs d'essai, harnais de test, campagnes d'étalonnage
```

## Reconstruire

```
cd jeu/src && python3 build.py
```

`build.py` concatène `a_head.html`, `b_css.txt`, `c_body.html`, `d_js.txt` et
`e_tail.html`, et écrit le résultat deux fois : sous le nom stable `jeu.html`,
et sous `HEAT_jeu_vX.Y.html` — le numéro est lu dans le `<title>` de
`a_head.html`, il n'y a donc rien à tenir à jour ailleurs. Déplacer les deux
fichiers dans `jeu/`.

Il n'y a pas d'autre chaîne de construction : c'est délibéré — la contrainte du
fichier unique est ce qui garde le jeu distribuable par simple copie.

Les harnais de `outils/` ouvrent tous `jeu.html`. Ils n'ont jamais à être
modifiés lors d'un changement de version.

## Vérifier

Les harnais de `outils/` pilotent le jeu dans un Chromium headless
(`pip install playwright && playwright install chromium`). Les quatre qui
comptent, à passer avant toute livraison :

| Harnais | Ce qu'il vérifie |
|---|---|
| `play3.py` | une partie complète de 17 tours dans l'interface, sans erreur console |
| `calib3.py` | l'étalonnage : la partie passive doit donner exactement 3,48 °C, et le score doit décroître à chaque niveau de difficulté, pour les deux camps |
| `chk_coh2.py` | aucun levier ne produit un effet qu'il n'annonce pas |
| `chk_save.py` | une partie sauvegardée puis rechargée est bit à bit identique |

Les `mes_*.py` sont des bancs de mesure, pas des tests : ils servent à établir
des valeurs de règle plutôt qu'à vérifier une invariante. `mes_puissance.py`
rejoue chaque levier seul sur un état standard et mesure ce qu'il déplace ;
c'est lui qui décide quels leviers sont « lourds ».

## Principes de conception

Quatre règles tenues depuis le début, et qui expliquent la plupart des
arbitrages :

1. **Un levier n'est consommé que par un effet obtenu.** Une tentative ratée ou
   une mesure annulée par l'adversaire rend le levier disponible. Sans quoi le
   contre est définitif et le duel n'a lieu qu'une fois.
2. **Un événement n'ajoute jamais de contrainte.** Un événement qui contraint
   déplace la trajectoire passive, et la trajectoire passive est la référence de
   tout le reste.
3. **La crédibilité est un rapport, pas une jauge.** Tout ce qui la déplace la
   déplace des deux côtés : discréditer l'autre vous crédite de la moitié. Ce qui
   décide n'est jamais le niveau mais l'écart entre les deux camps.
4. **Le camp attentiste se nomme lui-même.** Ses leviers portent le nom
   qu'emploient ceux qui les jouent, pas celui qu'emploient ceux qui les
   subissent — ce dernier figure dans une section dédiée de la fiche. Un camp
   décrit par ses adversaires n'est pas jouable.

## Publier une version

`PUBLIER.md` décrit la boucle : commit, push, et la mise en place initiale avec
GitHub Desktop.

## État

Version courante : **v0.11**. `notes/HEAT_note_jeu_v0.11.md` détaille les
mécaniques ajoutées, les mesures qui les justifient, et ce qui reste ouvert.

Les sources de `jeu/src/` n'ont jamais existé ailleurs que dans les sessions de
travail qui ont produit le jeu ; ce dépôt est le premier endroit où elles sont
conservées.
